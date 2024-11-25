-- План урока 50 - Проектирование БД и создание таблиц
-- Типы данных в SQLite
-- Динамическая типизация
-- TEXT, INTEGER, REAL, BLOB, NULL
-- Дата и время (форматы хранения)
-- BOOLEAN как INTEGER
-- Ключи и ограничения
-- Первичные ключи (PRIMARY KEY)
-- Автоинкремент (AUTOINCREMENT)
-- Внешние ключи (FOREIGN KEY)
-- Составные ключи
-- Уникальность (UNIQUE)
-- NOT NULL
-- DEFAULT значения
-- CHECK ограничения?
-- Типы связей между таблицами
-- Один к одному (1:1)
-- Один ко многим (1:N)
-- Многие ко многим (M:N)
-- Промежуточные таблицы
-- Проектирование схемы блога
-- Основные сущности (статьи, категории, теги, авторы)
-- Определение связей
-- Атрибуты каждой сущности
-- Ограничения целостности
-- Практическое задание
-- Спроектировать схему блога
-- Определить все поля и их типы
-- Прописать все связи
-- Составить список необходимых ограничений
-- Обсуждение edge cases
-- Обработка NULL значений
-- Каскадное удаление
-- Уникальные комбинации полей
-- Валидация данных на уровне БД
-- Студенты
-- Группы
-- Домашние задания
-- Предметы
-- Промпты
-- Обратная связь
-- Студенты
-- Группы
-- Преподы
-- Студбилет
-- Создание таблицы create if not exists
-- Создание таблицы если она не существует
CREATE TABLE
    IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        middle_name TEXT DEFAULT NULL,
        last_name TEXT NOT NULL,
        student_card_id INTEGER UNIQUE NOT NULL,
        group_name TEXT NOT NULL
    );

-- Удаление таблицы
-- DROP TABLE IF EXISTS students
-- Внесем одного студента
INSERT INTO
    students (
        first_name,
        last_name,
        student_card_id,
        group_name
    )
VALUES
    ('Филипп', 'Киркоров', 123456, 'Python422');

-- 4. Вставить несколько студентов
INSERT INTO
    students (
        first_name,
        middle_name,
        last_name,
        student_card_id,
        group_name
    )
VALUES
    (
        "Николай",
        "Викторович",
        "Басков",
        123457,
        "Python 422"
    ),
    (
        "Ольга",
        "Игоревна",
        "Бузова",
        123458,
        "Python 422 "
    )

-- Выбрать всех студентов группы Python 422
-- Мы увидим последствия аномалии вставки (группы записаны по разному, поэтому
-- вместо 3х студентов видим только Филиппа)
SELECT * FROM students
WHERE group_name = 'Python422';

SELECT group_name, COUNT(*), first_name
FROM students
GROUP BY group_name

-- 5. Давайте переопределим название группы, чтобы оно было у всех одинаковым
UPDATE students
SET group_name = 'python422'
WHERE group_name = 'Python422'
OR group_name = 'Python 422'
OR group_name = 'Python 422 '

-- Проверяем
SELECT * FROM students
WHERE group_name = 'python422';

-- 6. Создаем таблицу групп и добавляем в неё уникальные группы из таблицы студентов
CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
    );

-- Вставка уникальных групп
INSERT INTO groups (name)
SELECT DISTINCT group_name
FROM students;


-- 7. Создаем таблицу студентов с внешним ключом на группу

CREATE TABLE IF NOT EXISTS students_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT DEFAULT NULL,
    last_name TEXT NOT NULL,
    student_card_id INTEGER UNIQUE NOT NULL,
    group_id INTEGER NOT NULL,

    -- Внешний ключ на группу
    FOREIGN KEY (group_id) REFERENCES groups(id)
)


--- 8. Давайте наполним эту таблицу
INSERT INTO students_new (
    first_name,
    middle_name,
    last_name,
    student_card_id,
    group_id
)
SELECT 
    first_name,
    middle_name,
    last_name,
    student_card_id,
    (SELECT id FROM groups WHERE name = group_name)

FROM students;



-- INSERT INTO students_new (
--     first_name,
--     middle_name,
--     last_name,
--     student_card_id,
--     group_id
-- )
-- SELECT 
--     s.first_name,
--     s.middle_name,
--     s.last_name,
--     s.student_card_id,
--     g.id as group_id
-- FROM students s
-- JOIN groups g ON g.name = s.group_name;

-- 9. Удаляем таблицу студентов
DROP TABLE students;

-- Переименовываем таблицу студентов
ALTER TABLE students_new RENAME TO students;


-- Студенты
-- Группы
-- Преподы
-- Студбилет

-- DROP TABLE students
-- DROP TABLE groups

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

