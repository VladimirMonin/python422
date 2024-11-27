-- План урока 51 - CRUD операции в SQLite

-- INSERT операции

-- Базовый синтаксис INSERT
-- INSERT с указанием конкретных полей
-- Множественный INSERT
-- INSERT с подзапросами
-- Обработка ошибок при вставке

-- UPDATE операции

-- Базовый синтаксис UPDATE
-- UPDATE с условиями WHERE
-- Множественное обновление
-- UPDATE с подзапросами
-- Обновление связанных таблиц

-- DELETE операции

-- Базовый синтаксис DELETE
-- DELETE с условиями WHERE
-- Массовое удаление
-- Каскадное удаление
-- Soft Delete (логическое удаление)

-- Практика на созданной схеме блога

-- Создание новых постов с тегами
-- Добавление категорий
-- Связывание постов с тегами
-- Обновление существующих постов
-- Удаление с учётом связей

-- Типичные сценарии работы с блогом

-- Публикация поста
-- Редактирование поста
-- Управление тегами
-- Перемещение между категориями
-- Архивация контента

-- Проверка целостности данных

-- Проверка внешних ключей
-- Уникальные значения
-- Обработка обязательных полей
-- Валидация перед операциями


-- Студенты
-- Группы
-- Преподы
-- Студбилет


CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT DEFAULT NULL,
    last_name TEXT NOT NULL,
    group_id INTEGER NOT NULL REFERENCES groups(id)
);

CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    -- Автонаполняемое поле с датой
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS student_cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL REFERENCES students(id),
    card_number INTEGER NOT NULL UNIQUE,
    -- Статусы меняются и проверяются на уровне приложения
    card_status TEXT NOT NULL DEFAULT 'active',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
