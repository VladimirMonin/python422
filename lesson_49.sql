-- lesson 49 - JOIN

-- DDL

-- CREATE TABLE MarvelCharacters (
--     id               INTEGER PRIMARY KEY AUTOINCREMENT,
--     page_id          INTEGER,
--     name             TEXT,
--     urlslug          TEXT,
--     identity_id      INTEGER,
--     align_id         INTEGER,
--     eye_id           INTEGER,
--     hair_id          INTEGER,
--     sex_id           INTEGER,
--     status_id        INTEGER,
--     APPEARANCES      INTEGER,
--     FIRST_APPEARANCE TEXT,
--     Year             INTEGER,
--     FOREIGN KEY (
--         identity_id
--     )
--     REFERENCES Identity (identity_id),
--     FOREIGN KEY (
--         align_id
--     )
--     REFERENCES Alignment (align_id),
--     FOREIGN KEY (
--         eye_id
--     )
--     REFERENCES EyeColor (eye_id),
--     FOREIGN KEY (
--         hair_id
--     )
--     REFERENCES HairColor (hair_id),
--     FOREIGN KEY (
--         sex_id
--     )
--     REFERENCES Sex (sex_id),
--     FOREIGN KEY (
--         status_id
--     )
--     REFERENCES LivingStatus (status_id) 
-- );

-- CREATE TABLE LivingStatus (
--     status_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     status    TEXT    UNIQUE
-- );


-- CREATE TABLE Identity (
--     identity_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     identity    TEXT    UNIQUE
-- );


-- CREATE TABLE HairColor (
--     hair_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     color   TEXT    UNIQUE
-- );

-- CREATE TABLE EyeColor (
--     eye_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     color  TEXT    UNIQUE
-- );

-- CREATE TABLE Alignment (
--     align_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     name     TEXT    UNIQUE
-- );


-- Найдем персонажа с максимальным количеством появлений
SELECT name, MAX(appearances) as max_app, eye_id
FROM MarvelCharacters

SELECT eye_id, color
FROM EyeColor
WHERE eye_id = 1

--1.  Покажем через JOIN цвет глаз всех персонажей
SELECT MarvelCharacters.name, EyeColor.color
FROM MarvelCharacters
JOIN EyeColor ON MarvelCharacters.eye_id = EyeColor.eye_id

-- 2. Покажем через JOIN цвет глаз Spider-Man
SELECT MarvelCharacters.name, EyeColor.color
FROM MarvelCharacters
JOIN EyeColor ON MarvelCharacters.eye_id = EyeColor.eye_id
WHERE MarvelCharacters.name LIKE '%Spider-Man%'


-- 3. Попробуем сгруппировать по цвету глаз и посчитать количество персонажей с таким цветом (от куда тут сортировка
-- названий глаз???)
SELECT EyeColor.color, COUNT(*) as total_heroes
FROM MarvelCharacters
JOIN EyeColor ON MarvelCharacters.eye_id = EyeColor.eye_id
GROUP BY EyeColor.color


-- 4. Сделаем это с псевдонимами
SELECT e.color, COUNT(*) as total_heroes
FROM MarvelCharacters AS mc
JOIN EyeColor AS e ON mc.eye_id = e.eye_id
GROUP BY e.color
ORDER BY total_heroes DESC


-- В контексте SQLite (и SQL в целом) декларативность означает, что вы описываете ЖЕЛАЕМЫЙ результат, а не указываете точную последовательность шагов для его получения.

-- В вашем примере вы декларативно описываете:

-- Какие данные нужны (цвет глаз и количество героев)
-- Откуда брать данные (две таблицы)
-- Как объединять (JOIN)
-- Как группировать (GROUP BY)
-- Как сортировать (ORDER BY)
-- Важные характеристики декларативности в SQLite:

-- Порядок выполнения неявный Хотя логический порядок операторов такой:
-- FROM
-- JOIN
-- WHERE
-- GROUP BY
-- HAVING
-- SELECT
-- ORDER BY

-- Попробуйте сделать JOIN всех таблиц и посмотреть на результат.
-- mc.name, mc.appearances, e.color, h.color, s.status, a.name, i.identity