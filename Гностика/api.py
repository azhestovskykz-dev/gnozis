#!/usr/bin/env python3
"""
ГНОСТИКА — API-сервер v1.1
Управление изображениями + статический сервер + очередь генерации
Исправлена поддержка Cyrillic-путей на Windows
"""

import http.server
import json
import mimetypes
import os
import sys
import urllib.parse
from pathlib import Path

# Fix Windows console encoding
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

PORT = 8090
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "данные"
QUEUE_FILE = BASE_DIR / "очередь_генерации.json"

# Initialize mimetypes
mimetypes.init()
mimetypes.add_type('application/json', '.json')
mimetypes.add_type('text/javascript', '.js')
mimetypes.add_type('text/css', '.css')


def load_queue():
    if QUEUE_FILE.exists():
        with open(QUEUE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_queue(queue):
    with open(QUEUE_FILE, "w", encoding="utf-8") as f:
        json.dump(queue, f, ensure_ascii=False, indent=2)


class APIHandler(http.server.BaseHTTPRequestHandler):
    """Custom handler that serves static files AND API endpoints, with Cyrillic path support."""

    def _send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, filepath):
        """Serve a static file."""
        try:
            if not filepath.exists() or not filepath.is_file():
                self.send_error(404, "File not found")
                return

            # Determine content type
            content_type, _ = mimetypes.guess_type(str(filepath))
            if content_type is None:
                content_type = "application/octet-stream"

            # For JSON/JS/CSS files, set UTF-8 charset
            if content_type in ('application/json', 'text/javascript', 'text/css', 'text/html'):
                content_type += "; charset=utf-8"

            with open(filepath, "rb") as f:
                data = f.read()

            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(data)
        except Exception:
            self.send_error(500, "Internal server error")

    def _decode_path(self):
        """Decode and sanitize URL path."""
        parsed = urllib.parse.urlparse(self.path)
        decoded = urllib.parse.unquote(parsed.path)
        return decoded

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        decoded = self._decode_path()

        # API routes
        if decoded.startswith("/api/"):
            parts = decoded[5:].strip("/").split("/")
            return self._handle_api_get(parts)

        # Static file serving
        if decoded == "/" or decoded == "":
            decoded = "/index.html"

        # Resolve to filesystem path
        rel_path = decoded.lstrip("/")
        filepath = BASE_DIR / rel_path

        # Prevent directory traversal
        try:
            filepath.resolve().relative_to(BASE_DIR.resolve())
        except ValueError:
            self.send_error(403, "Forbidden")
            return

        if filepath.is_dir():
            filepath = filepath / "index.html"

        self._send_file(filepath)

    def _handle_api_get(self, parts):
        # GET /api/images/{author}/{idea_id}
        if len(parts) >= 3 and parts[0] == "images":
            author = parts[1]
            idea_id = parts[2]
            img_dir = DATA_DIR / author / "идеи" / idea_id / "рисунки"

            images = []
            if img_dir.exists():
                for f in sorted(img_dir.iterdir()):
                    if f.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp"):
                        images.append({
                            "файл": f.name,
                            "путь": f"данные/{author}/идеи/{idea_id}/рисунки/{f.name}",
                            "размер": f.stat().st_size
                        })
            return self._send_json({"изображения": images, "всего": len(images)})

        # GET /api/queue
        if len(parts) == 1 and parts[0] == "queue":
            queue = load_queue()
            return self._send_json({"очередь": queue, "всего": len(queue)})

        self._send_json({"ошибка": "Unknown route"}, 404)

    def do_POST(self):
        decoded = self._decode_path()
        if not decoded.startswith("/api/"):
            self._send_json({"ошибка": "Not API"}, 400)
            return

        parts = decoded[5:].strip("/").split("/")
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length) if content_length > 0 else b"{}"

        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            data = {}

        # POST /api/queue
        if len(parts) == 1 and parts[0] == "queue":
            author = data.get("автор", "")
            idea_id = data.get("идея_id", "")
            idea_name = data.get("название", "")
            action = data.get("действие", "генерация")

            if not author or not idea_id:
                return self._send_json({"ошибка": "Need автор and идея_id"}, 400)

            queue = load_queue()
            exists = any(
                q["автор"] == author and q["идея_id"] == idea_id and q["действие"] == action
                for q in queue
            )
            if not exists:
                queue.append({
                    "автор": author,
                    "идея_id": idea_id,
                    "название": idea_name,
                    "действие": action,
                    "статус": "ожидание"
                })
                save_queue(queue)
            return self._send_json({"успех": True, "очередь": len(queue)})

        # POST /api/queue/clear
        if len(parts) == 2 and parts[0] == "queue" and parts[1] == "clear":
            save_queue([])
            return self._send_json({"успех": True})

        # POST /api/queue/remove
        if len(parts) == 2 and parts[0] == "queue" and parts[1] == "remove":
            author = data.get("автор", "")
            idea_id = data.get("идея_id", "")
            queue = load_queue()
            queue = [q for q in queue if not (q["автор"] == author and q["идея_id"] == idea_id)]
            save_queue(queue)
            return self._send_json({"успех": True, "очередь": len(queue)})

        self._send_json({"ошибка": "Unknown route"}, 404)

    def do_DELETE(self):
        decoded = self._decode_path()
        if not decoded.startswith("/api/"):
            self._send_json({"ошибка": "Not API"}, 400)
            return

        parts = decoded[5:].strip("/").split("/")

        # DELETE /api/images/{author}/{idea_id}/{filename}
        if len(parts) >= 4 and parts[0] == "images":
            author = parts[1]
            idea_id = parts[2]
            filename = parts[3]
            filepath = DATA_DIR / author / "идеи" / idea_id / "рисунки" / filename

            if filepath.exists():
                filepath.unlink()
                # Renumber remaining files
                img_dir = filepath.parent
                remaining = sorted(
                    [f for f in img_dir.iterdir() if f.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp")],
                    key=lambda f: f.name
                )
                for idx, f in enumerate(remaining, 1):
                    new_name = f"{idx}{f.suffix}"
                    if f.name != new_name:
                        f.rename(img_dir / new_name)
                return self._send_json({"успех": True, "удалён": filename})
            else:
                return self._send_json({"ошибка": "File not found"}, 404)

        self._send_json({"ошибка": "Unknown route"}, 404)

    def log_message(self, format, *args):
        """Suppress most logging to prevent Windows encoding crashes."""
        pass


if __name__ == "__main__":
    print(f"[SERVER] Gnostika API: http://localhost:{PORT}")
    print(f"[DIR] Root: {BASE_DIR}")
    server = http.server.HTTPServer(("", PORT), APIHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[STOP] Server stopped")
