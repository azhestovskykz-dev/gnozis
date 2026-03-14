/**
 * ГНОСТИКА — Ядро логики v5.0
 * Полная мобильная поддержка + динамическая загрузка данных
 */

const СОСТОЯНИЕ = {
    автор: null,
    категория: null,
    идея: null,
    списокИдей: [],
    админ: false
};

// Состояние галереи
const ГАЛЕРЕЯ = {
    изображения: [],
    текущий: 0
};

// =====================================================================
// УТИЛИТЫ
// =====================================================================
function isMobile() {
    return window.innerWidth <= 1024;
}

function ideaToId(name, index) {
    return String(index).padStart(3, '0') + '_' + name.replace(/ /g, '_');
}

// =====================================================================
// ИНИЦИАЛИЗАЦИЯ
// =====================================================================
document.addEventListener('DOMContentLoaded', () => {
    console.log('Гностика v5 запущена');
    загрузитьГлобальноеМеню();
    показатьГлавную();

    // Слушатель клавиатуры для навигации
    document.addEventListener('keydown', (e) => {
        if (СОСТОЯНИЕ.идея) {
            if (e.key === 'ArrowRight') ПерейтиКСледующейИдее();
            if (e.key === 'ArrowLeft') ПерейтиКПредыдущейИдее();
        }
    });
});

// =====================================================================
// ГЛАВНАЯ СТРАНИЦА (приветствие)
// =====================================================================
function показатьГлавную() {
    document.getElementById('stage').innerHTML = `
        <div class="home-welcome">
            <div class="welcome-icon">📚</div>
            <h2>ГНОСТИКА</h2>
            <p>Выберите автора в меню слева, чтобы начать изучение его философских идей, книг и дистинкций.</p>
        </div>
    `;
    document.getElementById('breadcrumb').innerText = 'Главная';
    document.getElementById('info-panel').classList.add('hidden');
    document.getElementById('info-panel').classList.remove('panel-open');
}

// =====================================================================
// УПРАВЛЕНИЕ САЙДБАРАМИ (мобильная логика)
// =====================================================================
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebar-overlay');
    const isOpen = sidebar.classList.contains('open');

    if (isOpen) {
        sidebar.classList.remove('open');
        overlay.classList.remove('active');
    } else {
        sidebar.classList.add('open');
        if (isMobile()) {
            overlay.classList.add('active');
        }
    }
}

function closeSidebars() {
    document.getElementById('sidebar').classList.remove('open');
    document.getElementById('sidebar-overlay').classList.remove('active');
    // Также закрываем правую панель
    const infoPanel = document.getElementById('info-panel');
    infoPanel.classList.remove('panel-open');
}

function closeInfoPanel() {
    const infoPanel = document.getElementById('info-panel');
    infoPanel.classList.remove('panel-open');
    document.getElementById('sidebar-overlay').classList.remove('active');
}

function showInfoPanelMobile() {
    if (isMobile()) {
        const infoPanel = document.getElementById('info-panel');
        infoPanel.classList.add('panel-open');
        document.getElementById('sidebar-overlay').classList.add('active');
    }
}

// =====================================================================
// ГЛОБАЛЬНОЕ МЕНЮ (левый сайдбар)
// =====================================================================
function загрузитьГлобальноеМеню() {
    const навигация = document.getElementById('sidebar-nav');
    if (!навигация) return;

    const МЕНЮ = [
        {
            категория: "ПРОБУЖДЕНИЕ",
            авторы: [
                { id: "Георгий_Гурджиев", имя: "ГЕОРГИЙ ГУРДЖИЕВ" },
                { id: "Вернер_Эрхард", имя: "ВЕРНЕР ЭРХАРД" },
                { id: "Нисаргадатта_Махарадж", имя: "НИСАРГАДАТТА МАХАРАДЖ" },
                { id: "УГ_Кришнамурти", имя: "У.Г. КРИШНАМУРТИ" },
                { id: "Руперт_Спайра", имя: "РУПЕРТ СПАЙРА" },
                { id: "Роберт_Антон_Уилсон", имя: "РОБЕРТ АНТОН УИЛСОН" }
            ]
        },
        {
            категория: "ТРАНСФОРМАЦИЯ",
            авторы: [
                { id: "Вим_Хоф", имя: "ВИМ ХОФ" }
            ]
        },
        {
            категория: "СИСТЕМНОЕ МЫШЛЕНИЕ",
            авторы: [
                { id: "Рассел_Акофф", имя: "РАССЕЛ АКОФФ" },
                { id: "Питер_Сенге", имя: "ПИТЕР СЕНГЕ" },
                { id: "Донелла_Медоуз", имя: "ДОНЕЛЛА МЕДОУЗ" },
                { id: "Джон_ОКоннор", имя: "ДЖОН О'КОННОР" },
                { id: "Адамс_Джеймс", имя: "АДАМС ДЖЕЙМС" }
            ]
        },
        {
            категория: "МЕНЕДЖМЕНТ",
            авторы: [
                { id: "Питер_Друкер", имя: "ПИТЕР ДРУКЕР" },
                { id: "Том_Питерс", имя: "ТОМ ПИТЕРС" },
                { id: "Китами_Масао", имя: "КИТАМИ МАСАО" },
                { id: "Рикардо_Семлер", имя: "РИКАРДО СЕМЛЕР" }
            ]
        },
        {
            категория: "НАУКА И СОЗНАНИЕ",
            авторы: [
                { id: "Дональд_Хоффман", имя: "ДОНАЛЬД ХОФФМАН" },
                { id: "Дуглас_Хофштадтер", имя: "ДУГЛАС ХОФШТАДТЕР" },
                { id: "Павел_Флоренский", имя: "ПАВЕЛ ФЛОРЕНСКИЙ" }
            ]
        },
        {
            категория: "ПРОДУКТИВНОСТЬ",
            авторы: [
                { id: "Джессика_Хэги", имя: "ДЖЕССИКА ХЭГИ" }
            ]
        },
        {
            категория: "ОБУЧЕНИЕ",
            авторы: [
                { id: "Мортимер_Адлер", имя: "МОРТИМЕР АДЛЕР" }
            ]
        },
        {
            категория: "ЭЗОТЕРИКА",
            авторы: [
                { id: "Л_Секлитова_и_Л_Стрельникова", имя: "Л. СЕКЛИТОВА И Л. СТРЕЛЬНИКОВА" }
            ]
        }
    ];

    let html = '';

    МЕНЮ.forEach((группа, индекс) => {
        const catId = 'cat-' + индекс;
        const isExpanded = индекс === 0;
        const arrowClass = isExpanded ? 'expanded' : 'collapsed';
        const itemsClass = isExpanded ? '' : 'collapsed';

        html += `
            <div class="cat-header" onclick="toggleCategory('${catId}')">
                <span>${группа.категория}</span>
                <span class="cat-arrow ${arrowClass}" id="arrow-${catId}">▼</span>
            </div>
            <div class="cat-items ${itemsClass}" id="${catId}">
        `;

        группа.авторы.forEach(автор => {
            html += `
                <div class="nav-item" id="nav-${автор.id}" onclick="выбратьАвтора('${автор.id}')">
                    ${автор.имя}
                </div>
            `;
        });

        html += `</div>`;
    });

    навигация.innerHTML = html;
}

window.toggleCategory = function (catId) {
    const el = document.getElementById(catId);
    const arrow = document.getElementById('arrow-' + catId);
    if (!el || !arrow) return;

    if (el.classList.contains('collapsed')) {
        el.classList.remove('collapsed');
        arrow.classList.remove('collapsed');
        arrow.classList.add('expanded');
    } else {
        el.classList.add('collapsed');
        arrow.classList.remove('expanded');
        arrow.classList.add('collapsed');
    }
};

// =====================================================================
// ВЫБОР АВТОРА
// =====================================================================
let ТЕКУЩИЕ_ДАННЫЕ = null;
let ТЕКУЩАЯ_ИДЕЯ_ДАННЫЕ = null;

async function выбратьАвтора(имяПапки) {
    СОСТОЯНИЕ.автор = имяПапки;

    // Подсветка активного автора
    document.querySelectorAll('#sidebar-nav .nav-item').forEach(el => el.classList.remove('active'));
    const activeNav = document.getElementById(`nav-${имяПапки}`);
    if (activeNav) activeNav.classList.add('active');

    // На мобильном — закрываем левый сайдбар
    if (isMobile()) {
        document.getElementById('sidebar').classList.remove('open');
        document.getElementById('sidebar-overlay').classList.remove('active');
    }

    try {
        const ответ = await fetch(`данные/${имяПапки}/инфо.json`);
        if (!ответ.ok) throw new Error('Данные не найдены');
        const данные = await ответ.json();
        ТЕКУЩИЕ_ДАННЫЕ = данные;
        
        // Создаем плоский список идей для навигации
        СОСТОЯНИЕ.списокИдей = [];
        let index = 1;
        данные.группы.forEach(г => {
            г.категории.forEach(к => {
                к.идеи.forEach(идеяName => {
                    СОСТОЯНИЕ.списокИдей.push({
                        id: ideaToId(идеяName, index),
                        название: идеяName
                    });
                    index++;
                });
            });
        });

        document.getElementById('breadcrumb').innerText = '';
        document.getElementById('filter-toggle-btn').style.display = isMobile() ? 'block' : 'none';
        отрисоватьСеткуИдей(данные);
        показатьИнфоАвтора(данные);
    } catch (e) {
        document.getElementById('stage').innerHTML = `
            <div class="home-welcome">
                <div class="welcome-icon">🔨</div>
                <h2>В РАЗРАБОТКЕ</h2>
                <p>Материалы автора ${имяПапки.replace(/_/g, ' ')} ещё формируются.</p>
            </div>
        `;
        document.getElementById('info-panel').classList.add('hidden');
        document.getElementById('info-panel').classList.remove('panel-open');
        document.getElementById('breadcrumb').innerText = '';
        document.getElementById('filter-toggle-btn').style.display = 'none';
    }
}

// =====================================================================
// СЕТКА ИДЕЙ
// =====================================================================
function отрисоватьСеткуИдей(данные) {
    const сцена = document.getElementById('stage');
    let html = '';
    let globalIndex = 1;

    данные.группы.forEach((группа, индексГруппы) => {
        html += `<h2 style="color:var(--accent-color);margin:24px 0 16px;text-transform:uppercase;font-size:16px;letter-spacing:1px;border-bottom:1px solid var(--border-color);padding-bottom:8px;">${группа.название}</h2>`;

        группа.категории.forEach((кат, индексКат) => {
            const containerId = `ideas-cat-${индексГруппы}-${индексКат}`;

            html += `
                <div class="ideas-category-block" style="margin-bottom:24px;">
                    <div class="cat-header" style="margin-bottom:12px;background:var(--hover-bg);border-radius:6px;padding:10px 14px;cursor:pointer;" onclick="toggleIdeasGrid('${containerId}')">
                        <span style="font-weight:600;font-size:14px;color:#fff;">${кат.название}</span>
                        <span class="cat-arrow expanded" id="arrow-${containerId}">▼</span>
                    </div>
                    <div class="ideas-grid" id="${containerId}">
            `;

            кат.идеи.forEach((идея) => {
                const id = ideaToId(идея, globalIndex);
                const safeIdea = идея.replace(/'/g, "\\'");
                html += `
                    <div class="idea-card" onclick="открытьИдею('${id}', '${safeIdea}')">
                        <div class="idea-card-img">
                            <img src="данные/${СОСТОЯНИЕ.автор}/идеи/${id}/рисунки/1.jpg" alt="${идея}"
                                 style="width:100%;height:100%;object-fit:cover;display:block;"
                                 onerror="this.style.display='none';this.parentElement.style.backgroundColor='#121922';">
                        </div>
                        <div class="idea-card-content">
                            <h4>${идея}</h4>
                        </div>
                    </div>
                `;
                globalIndex++;
            });

            html += `
                        </div>
                    </div>
            `;
        });
    });

    сцена.innerHTML = html;
}

window.toggleIdeasGrid = function (containerId) {
    const el = document.getElementById(containerId);
    const arrow = document.getElementById('arrow-' + containerId);
    if (!el || !arrow) return;

    if (el.style.display === 'none') {
        el.style.display = 'grid';
        arrow.innerText = '▼';
        arrow.style.transform = 'rotate(0deg)';
    } else {
        el.style.display = 'none';
        arrow.innerText = '►';
        arrow.style.transform = 'rotate(-90deg)';
    }
};

window.фильтроватьПоКатегории = function(названиеКатегории, navEl) {
    if (navEl) {
        document.querySelectorAll('#author-nav .nav-item').forEach(el => el.classList.remove('active'));
        navEl.classList.add('active');
    }

    // Возврат к сетке, если открыта детальная идея или профиль
    if (document.querySelector('.idea-detail') || document.querySelector('.author-profile-grid')) {
        document.getElementById('breadcrumb').innerText = '';
        отрисоватьСеткуИдей(ТЕКУЩИЕ_ДАННЫЕ);
    }

    if (!названиеКатегории) {
        // "ВСЕ ИДЕИ": разворачиваем абсолютно все разделы
        const headers = document.querySelectorAll('.cat-header');
        for (let el of headers) {
            const match = el.getAttribute('onclick').match(/'([^']+)'/);
            if (match) {
                const grid = document.getElementById(match[1]);
                const arrow = document.getElementById('arrow-' + match[1]);
                if (grid && arrow) {
                    grid.style.display = 'grid';
                    arrow.innerText = '▼';
                    arrow.style.transform = 'rotate(0deg)';
                }
            }
        }
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
        setTimeout(() => {
            let targetY = 0;
            const headers = document.querySelectorAll('.cat-header');
            
            for (let el of headers) {
                const span = el.querySelector('span');
                const match = el.getAttribute('onclick').match(/'([^']+)'/);
                if (!span || !match) continue;

                const grid = document.getElementById(match[1]);
                const arrow = document.getElementById('arrow-' + match[1]);
                
                if (span.innerText.trim() === названиеКатегории.trim()) {
                    // Разворачиваем целевую
                    if (grid && arrow) {
                        grid.style.display = 'grid';
                        arrow.innerText = '▼';
                        arrow.style.transform = 'rotate(0deg)';
                    }
                    targetY = el.getBoundingClientRect().top + window.scrollY - 80;
                } else {
                    // Сворачиваем остальные
                    if (grid && arrow) {
                        grid.style.display = 'none';
                        arrow.innerText = '►';
                        arrow.style.transform = 'rotate(-90deg)';
                    }
                }
            }
            if (targetY > 0) {
                window.scrollTo({ top: targetY, behavior: 'smooth' });
            }
        }, 50);
    }
    
    if (isMobile()) {
        closeInfoPanel();
    }
};

// =====================================================================
// ДЕТАЛЬНЫЙ ВИД ИДЕИ (с галереей)
// =====================================================================
async function открытьИдею(id, name) {
    const путь = `данные/${СОСТОЯНИЕ.автор}/идеи/${id}/описание.json`;
    let данные = {};

    try {
        const ответ = await fetch(путь);
        if (ответ.ok) {
            данные = await ответ.json();
        }
    } catch (e) {
        console.warn('описание.json не найден');
    }

    ТЕКУЩАЯ_ИДЕЯ_ДАННЫЕ = {
        название: name,
        id: id,
        ...данные
    };
    СОСТОЯНИЕ.идея = id;

    // Загружаем список изображений через API
    await загрузитьИзображенияИдеи(id);

    document.getElementById('breadcrumb').innerText = `${СОСТОЯНИЕ.автор.replace(/_/g, ' ')} > ${name}`;

    const сцена = document.getElementById('stage');
    const currentIndex = СОСТОЯНИЕ.списокИдей.findIndex(i => i.id === id);
    const hasNext = currentIndex < СОСТОЯНИЕ.списокИдей.length - 1;
    const hasPrev = currentIndex > 0;

    const adminBtns = СОСТОЯНИЕ.админ ? `
        <div class="admin-idea-controls">
            <button class="btn btn-sm btn-accent" onclick="добавитьВОчередь()" title="Сгенерировать новый рисунок">✨ СГЕНЕРИРОВАТЬ</button>
            <button class="btn btn-sm btn-danger" onclick="удалитьТекущийРисунок()" title="Удалить текущий рисунок" id="btn-delete-img" style="${ГАЛЕРЕЯ.изображения.length === 0 ? 'display:none' : ''}">🗑️ УДАЛИТЬ</button>
            <button class="btn btn-sm" onclick="показатьОчередь()" title="Показать очередь генерации">📋 ОЧЕРЕДЬ</button>
        </div>` : '';

    сцена.innerHTML = `
        <div class="idea-detail">
            <div class="idea-tabs-container">
                <button class="idea-tab active" onclick="переключитьВкладкуИдеи('ОБРАЗ', this)">ОБРАЗ</button>
                <button class="idea-tab" onclick="переключитьВкладкуИдеи('ОПИСАНИЕ', this)">ОПИСАНИЕ</button>
                <button class="idea-tab" onclick="переключитьВкладкуИдеи('СТИХИ', this)">СТИХИ</button>
                <button class="idea-tab" onclick="переключитьВкладкуИдеи('ПРИТЧИ', this)">ПРИТЧИ</button>
                <button class="idea-tab" onclick="переключитьВкладкуИдеи('ПРИМЕРЫ', this)">ПРИМЕРЫ</button>
                <button class="idea-tab" onclick="переключитьВкладкуИдеи('ДИСТИНКЦИИ', this)">ДИСТИНКЦИИ</button>
                <button class="idea-tab" onclick="переключитьВкладкуИдеи('МЕТАФОРЫ', this)">МЕТАФОРЫ</button>
            </div>

            ${adminBtns}

            <div class="idea-nav-wrapper">
                ${hasPrev ? `<button class="idea-nav-btn prev" onclick="ПерейтиКПредыдущейИдее()" title="Предыдущая (←)">‹</button>` : '<div class="idea-nav-placeholder"></div>'}
                
                <div class="idea-main-view">
                    <h2 class="idea-title">${name}</h2>
                    <div id="idea-content-area" class="idea-content-area">
                        ${построитьГалерею()}
                    </div>
                </div>

                ${hasNext ? `<button class="idea-nav-btn next" onclick="ПерейтиКСледующейИдее()" title="Следующая (→)">›</button>` : '<div class="idea-nav-placeholder"></div>'}
            </div>

            <button class="btn btn-secondary" style="margin-top:32px" onclick="СОСТОЯНИЕ.идея=null;выбратьАвтора('${СОСТОЯНИЕ.автор}')">← НАЗАД К СПИСКУ</button>
        </div>
    `;
}

// =====================================================================
// ГАЛЕРЕЯ ИЗОБРАЖЕНИЙ
// =====================================================================
async function загрузитьИзображенияИдеи(id) {
    ГАЛЕРЕЯ.изображения = [];
    ГАЛЕРЕЯ.текущий = 0;
    try {
        const resp = await fetch(`/api/images/${СОСТОЯНИЕ.автор}/${id}`);
        if (resp.ok) {
            const data = await resp.json();
            ГАЛЕРЕЯ.изображения = data.изображения || [];
        }
    } catch (e) {
        // Fallback: пробуем 1.jpg напрямую
        ГАЛЕРЕЯ.изображения = [{
            файл: '1.jpg',
            путь: `данные/${СОСТОЯНИЕ.автор}/идеи/${id}/рисунки/1.jpg`
        }];
    }
}

function построитьГалерею() {
    if (ГАЛЕРЕЯ.изображения.length === 0) {
        return `<div style="text-align:center;padding:60px 20px;color:var(--text-secondary);background:var(--card-bg);border-radius:10px;">
            <div style="font-size:48px;margin-bottom:16px;">🎨</div>
            <p>Изображение ещё не создано</p>
            ${СОСТОЯНИЕ.админ ? '<button class="btn btn-sm btn-accent" style="margin-top:16px" onclick="добавитьВОчередь()">✨ СГЕНЕРИРОВАТЬ</button>' : ''}
        </div>`;
    }

    const img = ГАЛЕРЕЯ.изображения[ГАЛЕРЕЯ.текущий];
    const hasManyImages = ГАЛЕРЕЯ.изображения.length > 1;

    let dotsHtml = '';
    if (hasManyImages) {
        dotsHtml = '<div class="gallery-dots">';
        ГАЛЕРЕЯ.изображения.forEach((_, i) => {
            dotsHtml += `<span class="gallery-dot ${i === ГАЛЕРЕЯ.текущий ? 'active' : ''}" onclick="переключитьОбразГалереи(${i})"></span>`;
        });
        dotsHtml += '</div>';
    }

    let navHtml = '';
    if (hasManyImages) {
        navHtml = `
            <button class="gallery-arrow gallery-arrow-left" onclick="переключитьОбразГалереи(${(ГАЛЕРЕЯ.текущий - 1 + ГАЛЕРЕЯ.изображения.length) % ГАЛЕРЕЯ.изображения.length})">‹</button>
            <button class="gallery-arrow gallery-arrow-right" onclick="переключитьОбразГалереи(${(ГАЛЕРЕЯ.текущий + 1) % ГАЛЕРЕЯ.изображения.length})">›</button>
        `;
    }

    const counterHtml = hasManyImages
        ? `<div class="gallery-counter">${ГАЛЕРЕЯ.текущий + 1} / ${ГАЛЕРЕЯ.изображения.length}</div>`
        : '';

    return `
        <div class="gallery-container">
            ${navHtml}
            <img src="${img.путь}" 
                 style="width:100%;border-radius:10px;display:block;cursor:pointer;"
                 onclick="window.open(this.src,'_blank')"
                 onerror="this.onerror=null;this.alt='Изображение не загружено';this.style.backgroundColor='#121922';this.style.aspectRatio='1/1';">
            ${counterHtml}
        </div>
        ${dotsHtml}
    `;
}

window.переключитьОбразГалереи = function(index) {
    ГАЛЕРЕЯ.текущий = index;
    const area = document.getElementById('idea-content-area');
    if (area) area.innerHTML = построитьГалерею();
};

// =====================================================================
// АДМИН: ОЧЕРЕДЬ ГЕНЕРАЦИИ
// =====================================================================
window.добавитьВОчередь = async function() {
    if (!СОСТОЯНИЕ.автор || !СОСТОЯНИЕ.идея) return;
    try {
        await fetch('/api/queue', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                автор: СОСТОЯНИЕ.автор,
                идея_id: СОСТОЯНИЕ.идея,
                название: ТЕКУЩАЯ_ИДЕЯ_ДАННЫЕ?.название || '',
                действие: 'генерация'
            })
        });
        alert('✨ Добавлено в очередь генерации!');
    } catch (e) {
        alert('Ошибка: ' + e.message);
    }
};

window.удалитьТекущийРисунок = async function() {
    if (ГАЛЕРЕЯ.изображения.length === 0) return;
    const img = ГАЛЕРЕЯ.изображения[ГАЛЕРЕЯ.текущий];
    if (!confirm(`Удалить рисунок ${img.файл}?`)) return;

    try {
        const resp = await fetch(`/api/images/${СОСТОЯНИЕ.автор}/${СОСТОЯНИЕ.идея}/${img.файл}`, { method: 'DELETE' });
        if (resp.ok) {
            // Перезагружаем галерею
            await загрузитьИзображенияИдеи(СОСТОЯНИЕ.идея);
            if (ГАЛЕРЕЯ.текущий >= ГАЛЕРЕЯ.изображения.length) ГАЛЕРЕЯ.текущий = Math.max(0, ГАЛЕРЕЯ.изображения.length - 1);
            const area = document.getElementById('idea-content-area');
            if (area) area.innerHTML = построитьГалерею();
            // Скрыть кнопку если нет изображений
            const delBtn = document.getElementById('btn-delete-img');
            if (delBtn) delBtn.style.display = ГАЛЕРЕЯ.изображения.length === 0 ? 'none' : '';
        }
    } catch (e) {
        alert('Ошибка удаления: ' + e.message);
    }
};

window.показатьОчередь = async function() {
    try {
        const resp = await fetch('/api/queue');
        const data = await resp.json();
        const queue = data.очередь || [];

        if (queue.length === 0) {
            alert('📋 Очередь пуста');
            return;
        }

        let msg = `📋 Очередь генерации (${queue.length}):\n\n`;
        queue.forEach((q, i) => {
            msg += `${i + 1}. ${q.автор.replace(/_/g, ' ')} → ${q.название} [${q.действие}]\n`;
        });
        msg += '\nОчистить очередь?';

        if (confirm(msg)) {
            await fetch('/api/queue/clear', { method: 'POST' });
            alert('Очередь очищена');
        }
    } catch (e) {
        alert('Ошибка: ' + e.message);
    }
};

// =====================================================================
// НАВИГАЦИЯ МЕЖДУ ИДЕЯМИ
// =====================================================================
window.ПерейтиКСледующейИдее = function() {
    const currentIndex = СОСТОЯНИЕ.списокИдей.findIndex(i => i.id === СОСТОЯНИЕ.идея);
    if (currentIndex < СОСТОЯНИЕ.списокИдей.length - 1) {
        const next = СОСТОЯНИЕ.списокИдей[currentIndex + 1];
        открытьИдею(next.id, next.название);
    }
};

window.ПерейтиКПредыдущейИдее = function() {
    const currentIndex = СОСТОЯНИЕ.списокИдей.findIndex(i => i.id === СОСТОЯНИЕ.идея);
    if (currentIndex > 0) {
        const prev = СОСТОЯНИЕ.списокИдей[currentIndex - 1];
        открытьИдею(prev.id, prev.название);
    }
};

// =====================================================================
// ПЕРЕКЛЮЧЕНИЕ ВКЛАДОК ИДЕИ
// =====================================================================
window.переключитьВкладкуИдеи = function (вкладка, btnEl) {
    // Подсветка вкладки
    document.querySelectorAll('.idea-tab').forEach(b => b.classList.remove('active'));
    if (btnEl) btnEl.classList.add('active');

    const area = document.getElementById('idea-content-area');
    if (!area) return;
    const данные = ТЕКУЩАЯ_ИДЕЯ_ДАННЫЕ;
    if (!данные) return;
    const описание = данные.описание || {};

    if (вкладка === 'ОБРАЗ') {
        area.innerHTML = построитьГалерею();
        return;
    }

    const mapKeys = {
        'СТИХИ': ['стих'],
        'ПРИТЧИ': ['притча'],
        'ПРИМЕРЫ': ['примеры из жизни', 'примеры из бизнеса', 'примеры из работы'],
        'ДИСТИНКЦИИ': ['дистинкция'],
        'МЕТАФОРЫ': ['метафора']
    };

    let html = '';

    if (вкладка === 'ОПИСАНИЕ') {
        let knownKeys = ['стих', 'притча', 'примеры из жизни', 'примеры из бизнеса', 'примеры из работы', 'дистинкция', 'метафора'];
        let hasContent = false;

        // Сначала текст из корня
        if (данные.текст) {
            html += `<div class="description-section"><h5>СУТЬ ИДЕИ</h5><div class="description-content">${форматТекст(данные.текст)}</div></div>`;
            hasContent = true;
        }
        // Потом доп. поля из описание
        for (const [key, value] of Object.entries(описание)) {
            if (!knownKeys.includes(key) && typeof value === 'string') {
                html += `<div class="description-section"><h5>${key.toUpperCase()}</h5><div class="description-content">${форматТекст(value)}</div></div>`;
                hasContent = true;
            }
        }

        if (!hasContent) {
            html = `<div style="text-align:center;padding:40px;color:var(--text-secondary);">Описание будет добавлено позже.</div>`;
        }
    } else {
        const keys = mapKeys[вкладка];
        let found = false;

        if (keys) {
            keys.forEach(k => {
                if (описание[k]) {
                    html += `<div class="description-section"><h5>${k.toUpperCase()}</h5><div class="description-content">${форматТекст(описание[k])}</div></div>`;
                    found = true;
                }
            });
        }

        if (!found) {
            html = `<div style="text-align:center;padding:40px;color:var(--text-secondary);">Раздел «${вкладка}» в разработке.</div>`;
        }
    }

    area.innerHTML = html;
};

function форматТекст(text) {
    if (!text) return '';
    return text.replace(/\\n/g, '<br>').replace(/\n/g, '<br>');
}

// =====================================================================
// ПРАВАЯ ПАНЕЛЬ (информация об авторе)
// =====================================================================
function показатьИнфоАвтора(данные) {
    const панель = document.getElementById('info-panel');
    панель.classList.remove('hidden');

    document.getElementById('author-name').innerText = данные.имя;
    document.getElementById('author-role').innerText = данные.роль || 'АВТОР';

    const photoEl = document.getElementById('author-photo');
    if (данные.фото) {
        photoEl.style.backgroundImage = `url('${данные.фото}')`;
        photoEl.style.display = 'block';
        photoEl.onclick = () => открытьПрофильАвтора(СОСТОЯНИЕ.автор);
        photoEl.title = 'Открыть биографию';
    } else {
        photoEl.style.display = 'none';
        photoEl.style.backgroundImage = '';
        photoEl.onclick = null;
    }

    // Навигация по категориям (Оглавление)
    const навигация = document.getElementById('author-nav');
    let html = `<div class="nav-item active" style="font-weight:600;margin-bottom:12px;" onclick="фильтроватьПоКатегории('', this)">ВСЕ ИДЕИ</div>`;

    данные.группы.forEach(группа => {
        html += `<div class="author-group-title">${группа.название}</div>`;
        группа.категории.forEach(кат => {
            const safeCat = кат.название.replace(/'/g, "\\'");
            html += `<div class="nav-item" onclick="фильтроватьПоКатегории('${safeCat}', this)">${кат.название}</div>`;
        });
    });

    навигация.innerHTML = html;

    // На мобильном — не открываем правую панель автоматически
    if (!isMobile()) {
        панель.classList.remove('panel-open');
    }
}

// =====================================================================
// ПРОФИЛЬ АВТОРА (полноэкранная биография + книги)
// =====================================================================
window.открытьПрофильАвтора = async function (авторId) {
    if (!авторId) авторId = СОСТОЯНИЕ.автор;
    const данные = ТЕКУЩИЕ_ДАННЫЕ;
    if (!данные) return;

    let профиль = {};
    try {
        const ответ = await fetch(`данные/${авторId}/профиль.json`);
        if (ответ.ok) {
            профиль = await ответ.json();
        }
    } catch (e) { }

    document.getElementById('breadcrumb').innerText = `${данные.имя} > БИОГРАФИЯ`;
    const сцена = document.getElementById('stage');

    // Левая колонка — портрет + книги
    let leftHtml = `<img src="${данные.фото}" alt="Портрет" style="width:100%;border-radius:12px;margin-bottom:20px;" onerror="this.style.display='none'">`;

    if (профиль.книги && профиль.книги.length > 0) {
        leftHtml += `<h3 style="font-size:15px;color:var(--accent-color);margin-bottom:10px;border-bottom:1px solid var(--border-color);padding-bottom:6px;">ИЗДАННЫЕ КНИГИ</h3>`;
        профиль.книги.forEach(book => {
            leftHtml += `
                <div class="book-card">
                    ${book.обложка ? `<img src="${book.обложка}" style="width:70px;height:100px;object-fit:cover;border-radius:4px;flex-shrink:0;">` : '<div style="width:70px;height:100px;background:var(--hover-bg);border-radius:4px;flex-shrink:0;"></div>'}
                    <div style="min-width:0;">
                        <h4 style="margin:0 0 4px;font-size:13px;color:#fff;line-height:1.3;">${book.название}</h4>
                        <p style="margin:0;font-size:12px;color:var(--text-secondary);line-height:1.4;">${book.описание || ''}</p>
                    </div>
                </div>
            `;
        });
    }

    // Правая колонка — биография
    let rightHtml = `<h2 style="font-size:clamp(22px,4vw,32px);margin:0 0 8px;color:#fff;text-transform:uppercase;">${данные.имя}</h2>`;
    rightHtml += `<div style="color:var(--accent-color);font-weight:600;letter-spacing:2px;margin-bottom:24px;font-size:12px;">${данные.роль || 'АВТОР'}</div>`;

    if (профиль.достижения && профиль.достижения.length > 0) {
        rightHtml += `<div style="margin-bottom:24px;background:var(--hover-bg);padding:16px;border-radius:10px;">
            <h4 style="margin:0 0 10px;color:#fff;font-size:14px;">ВКЛАД И ОСНОВНЫЕ ИДЕИ</h4>
            <ul style="padding-left:18px;color:var(--text-secondary);margin:0;line-height:1.6;font-size:14px;">
                ${профиль.достижения.map(d => `<li style="margin-bottom:4px;">${d}</li>`).join('')}
            </ul>
        </div>`;
    }

    if (профиль.биография) {
        let bioText = Array.isArray(профиль.биография) ? профиль.биография.join('<br><br>') : профиль.биография;
        rightHtml += `<div style="font-size:15px;line-height:1.8;color:var(--text-secondary);">${bioText}</div>`;
    } else {
        rightHtml += `<div style="font-size:15px;color:var(--text-secondary);">Биография в процессе подготовки...</div>`;
    }

    сцена.innerHTML = `
        <div class="author-profile-grid">
            <div class="author-profile-left">${leftHtml}</div>
            <div>${rightHtml}</div>
        </div>
        <div style="padding:20px 0;text-align:left;">
            <button class="btn btn-secondary" onclick="выбратьАвтора('${авторId}')">← НАЗАД К ИДЕЯМ</button>
        </div>
    `;
};

// =====================================================================
// ФУНКЦИИ ИНТЕРФЕЙСА
// =====================================================================
function openAuth() {
    document.getElementById('auth-ov').classList.remove('hidden');
}

function closeAuth() {
    document.getElementById('auth-ov').classList.add('hidden');
}

function checkAuth() {
    const pass = document.getElementById('auth-in').value;
    if (pass === '1234') {
        СОСТОЯНИЕ.админ = true;
        document.getElementById('admin-controls').classList.remove('hidden');
        closeAuth();
    } else {
        alert('Неверный пароль');
    }
}

function goHome() {
    СОСТОЯНИЕ.автор = null;
    document.querySelectorAll('#sidebar-nav .nav-item').forEach(el => el.classList.remove('active'));
    показатьГлавную();
    document.getElementById('filter-toggle-btn').style.display = 'none';
    if (isMobile()) {
        document.getElementById('sidebar').classList.remove('open');
        document.getElementById('sidebar-overlay').classList.remove('active');
    }
}

// При resize — на мобильном убираем .open, чтобы sidebar не налезал
window.addEventListener('resize', () => {
    if (isMobile()) {
        document.getElementById('sidebar').classList.remove('open');
        document.getElementById('sidebar-overlay').classList.remove('active');
    }

    // Показываем/скрываем кнопку фильтров
    if (СОСТОЯНИЕ.автор) {
        document.getElementById('filter-toggle-btn').style.display = isMobile() ? 'block' : 'none';
    } else {
        document.getElementById('filter-toggle-btn').style.display = 'none';
    }
});

// =====================================================================
// ПРИВЯЗКА ФУНКЦИЙ К WINDOW (для onclick атрибутов в HTML)
// =====================================================================
window.показатьГлавную = показатьГлавную;
window.goHome = goHome;
window.openAuth = openAuth;
window.closeAuth = closeAuth;
window.checkAuth = checkAuth;
window.toggleSidebar = toggleSidebar;
window.closeSidebars = closeSidebars;
window.closeInfoPanel = closeInfoPanel;
window.showInfoPanelMobile = showInfoPanelMobile;
window.выбратьАвтора = выбратьАвтора;
window.открытьИдею = открытьИдею;

// =====================================================================
// НЕДОСТАЮЩИЕ ФУНКЦИИ (заглушки)
// =====================================================================
function editMode() {
    alert('Режим редактирования пока в разработке.');
}
window.editMode = editMode;

function logout() {
    СОСТОЯНИЕ.админ = false;
    document.getElementById('admin-controls').classList.add('hidden');
}
window.logout = logout;
