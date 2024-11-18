-- Lesson 48 - SQL
-- Запросы с GROUP BY, HAVING и подзапросы

-- Агрегатные функции SQLite для использования с GROUP BY:

-- COUNT() - подсчитывает количество строк в группе
-- COUNT(*) - все строки включая NULL
-- COUNT(column) - строки где значение не NULL
-- Пример: SELECT department, COUNT(*) FROM employees GROUP BY department

-- SUM() - вычисляет сумму значений в группе
-- Пример: SELECT category, SUM(price) FROM products GROUP BY category

-- AVG() - вычисляет среднее значение в группе
-- Пример: SELECT department, AVG(salary) FROM employees GROUP BY department

-- MAX() - находит максимальное значение в группе
-- Пример: SELECT category, MAX(price) FROM products GROUP BY category

-- MIN() - находит минимальное значение в группе
-- Пример: SELECT category, MIN(price) FROM products GROUP BY category

-- GROUP_CONCAT() - объединяет значения строк в группе в одну строку
-- Пример: SELECT department, GROUP_CONCAT(name) FROM employees GROUP BY department

-- Важные особенности:
-- 1. GROUP BY группирует строки с одинаковыми значениями в указанном столбце
-- 2. Можно группировать по нескольким столбцам через запятую
-- 3. HAVING используется для фильтрации после группировки
-- 4. В SELECT можно использовать только сгруппированные поля или агрегатные функции


SELECT eye, name, MAX(APPEARANCES) as app
FROM marvelcharacters
WHERE EYE NOT NULL
GROUP BY eye
ORDER BY app DESC

-- 1. Добавьте вывод количества персонажей в каждой группе
-- 2. Средний год появления группы


SELECT eye, name, MAX(APPEARANCES) as max_appearances, 
COUNT(*) as total_heroes, 
ROUND(AVG(year)) as average_year, 
ROUND(AVG(appearances), 2) as avg_appearances
FROM marvelcharacters
WHERE EYE NOT NULL
GROUP BY eye
ORDER BY max_appearances DESC


-- Найдем персонажа с самым длинным name используя LENGTH
SELECT name, LENGTH(name) as name_length
FROM marvelcharacters
ORDER BY name_length DESC
LIMIT 1

SELECT name, MAX(LENGTH(name)) as name_length
FROM marvelcharacters

SELECT name, MIN(LENGTH(name)) as name_length
FROM marvelcharacters

-- Найдем пересонажей с длиной имени больше 10 символов
SELECT name, LENGTH(name) as name_length
FROM marvelcharacters
WHERE LENGTH(name) > 10
ORDER BY name_length DESC

-- Персонажи появившиеся в том же году что и человек паук

-- Найдем человека паука
SELECT name, year, appearances
FROM marvelcharacters
WHERE name LIKE '%Spider%'
ORDER BY appearances DESC
LIMIT 1

-- Найдем персонажей появившихся в том же году что и человек паук
SELECT name, year, appearances
FROM marvelcharacters
WHERE year = 1962

-- Один запрос. Найди человека паука и персонажей появившихся в том же году
SELECT name, year, appearances
from marvelcharacters
WHERE year = (
    SELECT year
    FROM marvelcharacters
    WHERE name LIKE '%Spider%'
    ORDER BY appearances DESC
    LIMIT 1
) 
AND APPEARANCES > 10


SELECT ((Year/10) * 10) as decade, count(*) as total
FROM MarvelCharacters
GROUP BY decade


SELECT 
    LENGTH(name) as name_length,
    COUNT(*) as heroes_count
FROM MarvelCharacters
GROUP BY name_length

HAVING heroes_count BETWEEN 10 AND 100
ORDER BY name_length DESC


-- Отложим как неработающую
-- SELECT 
--     LENGTH(name) as name_length,
--     COUNT(*) as heroes_count
-- FROM MarvelCharacters
-- GROUP BY name_length

-- HAVING heroes_count BETWEEN MIN(name_length) 0.9 AND MAX(name_length) * 0.5
-- ORDER BY name_length DESC

-- С использованием UNION выведем MAX и MIN длину имени
SELECT MAX(LENGTH(name)), name
FROM MarvelCharacters
UNION
SELECT MIN(LENGTH(name)), name
FROM MarvelCharacters

-- UNION - объединяет результаты двух или более запросов в одну таблицу
-- UNION ALL - объединяет результаты двух или более запросов в одну таблицу, включая дубликаты

SELECT MAX(LENGTH(name)) as name_length, 
       name, 
       'Самое длинное имя' as description
FROM MarvelCharacters
UNION
SELECT MIN(LENGTH(name)) as name_length, 
       name, 
       'Самое короткое имя' as description
FROM MarvelCharacters
ORDER BY name_length DESC

-- Попробуйте в одну таблицу с использованием UNION ALL вывести MAX,  MIN и AVG появлений с группировкой по цвету глаз, второй группой по цвету волос

-- Должны будут быть 2 запроса. 
-- 1. По цвету глаз группируем, и считаем 3 функции (числа)
-- 2. По цвету волос группируем, и считаем 3 функции (числа)
-- 3. Объединяем 2 запроса в одну таблицу через UNION ALL

SELECT eye as color, 
MAX(appearances) as max_app, 
MIN(appearances) as min_app, 
ROUND(AVG(appearances), 2) as avg_app,
COUNT(*) as total_heroes,
'eye' as data_type
FROM MarvelCharacters
WHERE eye NOT NULL
GROUP BY eye
UNION ALL
SELECT hair, 
MAX(appearances), 
MIN(appearances), 
ROUND(AVG(appearances), 2),
COUNT(*),
'hair' as data_type
FROM MarvelCharacters
WHERE hair NOT NULL
GROUP BY hair
ORDER BY data_type, total_heroes DESC


-- Виртуальная таблица или же представление (view)
-- Создать VIEW 

CREATE VIEW heroes_by_eye AS
SELECT eye as color, 
MAX(appearances) as max_app, 
MIN(appearances) as min_app, 
ROUND(AVG(appearances), 2) as avg_app,
COUNT(*) as total_heroes,
'eye' as data_type
FROM MarvelCharacters
WHERE eye NOT NULL
GROUP BY eye
UNION ALL
SELECT hair, 
MAX(appearances), 
MIN(appearances), 
ROUND(AVG(appearances), 2),
COUNT(*),
'hair' as data_type
FROM MarvelCharacters
WHERE hair NOT NULL
GROUP BY hair
ORDER BY data_type, total_heroes DESC


SELECT * FROM heroes_by_eye



SELECT eye as color,
    MAX(appearances) as max_app,
    MIN(appearances) as min_app,
    ROUND(AVG(appearances), 2) as avg_app,
    COUNT(*) as total_heroes,
    'eye ' || eye as data_type
FROM MarvelCharacters
WHERE eye NOT NULL
GROUP BY eye

UNION ALL

SELECT hair,
    MAX(appearances),
    MIN(appearances),
    ROUND(AVG(appearances), 2),
    COUNT(*),
    'hair ' || hair as data_type
FROM MarvelCharacters
WHERE hair NOT NULL
GROUP BY hair
ORDER BY data_type, total_heroes DESC


SELECT eye as color,
    MAX(appearances) as max_app,
    MIN(appearances) as min_app,
    ROUND(AVG(appearances), 2) as avg_app,
    COUNT(*) as total_heroes,
    CONCAT('eye ', eye) as data_type
FROM MarvelCharacters
WHERE eye NOT NULL
GROUP BY eye

UNION ALL

SELECT hair,
    MAX(appearances),
    MIN(appearances),
    ROUND(AVG(appearances), 2),
    COUNT(*),
    CONCAT('hair ', hair) as data_type
FROM MarvelCharacters
WHERE hair NOT NULL
GROUP BY hair
ORDER BY data_type, total_heroes DESC


