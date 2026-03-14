import { создатьБиблиотеку } from './generator.js';

let текущаяБиблиотека = [];
let текущийИндекс = 0;

const кнопкаГенерации = document.getElementById('кнопка-генерации');
const инпутТемы = document.getElementById('поле-ввода-темы');
const сетка = document.getElementById('сетка-идей');
const завесаЗагрузки = document.getElementById('завеса-загрузки');
const статусЗагрузки = document.getElementById('статус-загрузки');
const заголовокТемы = document.getElementById('заголовок-текущей-темы');

// Элементы просмотра
const модалкаПросмотра = document.getElementById('модальное-окно-просмотра');
const изобрВПросмотре = document.getElementById('изображение-в-просмотре');
const заголовокВПросмотре = document.getElementById('заголовок-в-просмотре');
const описаниеВПросмотре = document.getElementById('описание-в-просмотре');
const кнопкаЗакрыть = document.getElementById('закрыть-просмотр');
const кнопкаВлево = document.getElementById('стрелка-влево');
const кнопкаВправо = document.getElementById('стрелка-вправо');

кнопкаГенерации.addEventListener('click', async () => {
    const тема = инпутТемы.value.trim();
    if (!тема) {
        alert('Пожалуйста, введите тему для генерации!');
        return;
    }

    начатьЗагрузку(тема);
    
    try {
        текущаяБиблиотека = await создатьБиблиотеку(тема, обновитьСтатус);
        отрисоватьБиблиотеку(текущаяБиблиотека, тема);
    } catch (ошибка) {
        console.error('Ошибка генерации:', ошибка);
        alert('Произошла ошибка при создании контента. Попробуйте еще раз.');
    } finally {
        остановитьЗагрузку();
    }
});

function начатьЗагрузку(тема) {
    завесаЗагрузки.classList.remove('скрыто');
    обновитьСтатус(`Анализируем тему: ${тема}...`);
}

function остановитьЗагрузку() {
    завесаЗагрузки.classList.add('скрыто');
}

function обновитьСтатус(сообщение) {
    статусЗагрузки.textContent = сообщение;
}

function отрисоватьБиблиотеку(библиотека, тема) {
    заголовокТемы.textContent = `Библиотека: ${тема}`;
    сетка.innerHTML = '';

    библиотека.forEach((идея, индекс) => {
        const карточка = document.createElement('div');
        карточка.className = 'карточка';
        карточка.innerHTML = `
            <div class="изображение-карточки">
                <img src="${идея.путьККартинке}" alt="${идея.заголовок}">
            </div>
            <div class="тело-карточки">
                <h3>${идея.заголовок}</h3>
                <p>${идея.описание}</p>
            </div>
        `;
        карточка.addEventListener('click', () => открытьПросмотр(индекс));
        сетка.appendChild(карточка);
    });
}

function открытьПросмотр(индекс) {
    текущийИндекс = индекс;
    обновитьКонтентПросмотра();
    модалкаПросмотра.classList.remove('скрыто');
    document.body.style.overflow = 'hidden';
}

function обновитьКонтентПросмотра() {
    const идея = текущаяБиблиотека[текущийИндекс];
    изобрВПросмотре.src = идея.путьККартинке;
    заголовокВПросмотре.textContent = идея.заголовок;
    описаниеВПросмотре.textContent = идея.описание;
}

function закрытьПросмотр() {
    модалкаПросмотра.classList.add('скрыто');
    document.body.style.overflow = '';
}

function сдвиг(направление) {
    текущийИндекс = (текущийИндекс + направление + текущаяБиблиотека.length) % текущаяБиблиотека.length;
    обновитьКонтентПросмотра();
}

// Слушатели для модалки
кнопкаЗакрыть.addEventListener('click', закрытьПросмотр);
кнопкаВлево.addEventListener('click', () => сдвиг(-1));
кнопкаВправо.addEventListener('click', () => сдвиг(1));

// Закрытие по клику на фон
модалкаПросмотра.addEventListener('click', (e) => {
    if (e.target === модалкаПросмотра) закрытьПросмотр();
});

// Клавиатура
window.addEventListener('keydown', (e) => {
    if (модалкаПросмотра.classList.contains('скрыто')) return;
    
    if (e.key === 'ArrowLeft') сдвиг(-1);
    if (e.key === 'ArrowRight') сдвиг(1);
    if (e.key === 'Escape') закрытьПросмотр();
});
