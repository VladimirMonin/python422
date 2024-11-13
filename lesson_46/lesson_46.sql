-- lesson_46 - Знакомство с SQL
-- Расширения sqlite: .sqlite3, .sqlite, .db .db3 
-- Если Node.js не ставит npm install sqlite3
-- Set-ExecutionPolicy -Scope CurrentUser RemoteSigned СДЕЛАЙТЕ ЭТО и повторите

-- Особенности SQLite:
-- 1. БД хранится в одном файле
-- 2. Нет авторизации, системы пользователей
-- 3. Динамическая типизация

-- Создание БД
-- Автор
-- Заголовок
-- Текст
-- Дата
-- Категория
-- Теги
-- Просмотры

-- Создание таблицы
CREATE TABLE posts (
    id INTEGER,
    title TEXT,
    body TEXT,
    created_at DATETIME,
    category TEXT,
    tags TEXT,
    views INTEGER
)

-- CRUD - Create Read Update Delete

-- CREATE

INSERT INTO posts (
    id,
    title,
    body,
    created_at,
    category,
    tags,
    views
)
VALUES (
    1,
    'Базы данных для чайников',
    'SQL это невероятно просто!',
    '2021-01-01 00:00:00',
    'Программирование',
    'SQL, База данных, Обучение',
    42
)


-- UPDATE - изменим название на "Базы данных для уток"
UPDATE posts
SET title = 'Базы данных для уток'
WHERE id = 1

-- DELETE - удалим запись
DELETE FROM posts
WHERE id = 1