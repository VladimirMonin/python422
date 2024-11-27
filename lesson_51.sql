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

CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT DEFAULT NULL,
    last_name TEXT NOT NULL,
    hourly_rate INTEGER NOT NULL,
    raitng INTEGER NOT NULL
)

-- Внесем группу python422
INSERT INTO groups (name)
VALUES ('python422')

-- Внесем преподавателя
INSERT INTO teachers (first_name, last_name, hourly_rate, raitng)
VALUES ('Михаил', 'Галустян', 2000, 5)

-- Добавляем преподавателя в группу id 1 - 1
INSERT INTO teachers_groups (teacher_id, group_id)
VALUES (1, 1)

-- Вариант 2. Где мы НЕ знаем id преподавателя и группы
INSERT INTO teachers_groups (teacher_id, group_id)
VALUES (
    (SELECT id FROM teachers WHERE first_name = 'Михаил' AND last_name = 'Галустян'),
    (SELECT id FROM groups WHERE name = 'python422')
)


-- Сводная таблица многие ко многим. Преподаватели и группы
CREATE TABLE IF NOT EXISTS teachers_groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_id INTEGER NOT NULL REFERENCES teachers(id)
    ON DELETE CASCADE,
    group_id INTEGER NOT NULL REFERENCES groups(id)
    ON DELETE CASCADE,
    UNIQUE (teacher_id, group_id)
)





-- Как будет выглядить вариант, где нет отдельного id а внешние ключи являются составным первичным ключом
-- CREATE TABLE IF NOT EXISTS teachers_groups (
--     teacher_id INTEGER NOT NULL REFERENCES teachers(id),
--     group_id INTEGER NOT NULL REFERENCES groups(id),
--     PRIMARY KEY (teacher_id, group_id)
-- )