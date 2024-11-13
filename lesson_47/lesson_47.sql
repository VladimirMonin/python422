-- Lesson 47: Однотабличные запросы на выборку данных.

-- | `SELECT`   | Используется для выборки данных из таблицы.                                                                  |
-- | ---------- | ------------------------------------------------------------------------------------------------------------ |
-- | `FROM`     | Указывает таблицу, из которой следует извлекать данные.                                                      |
-- | `WHERE`    | Фильтрует записи на основе заданных условий.                                                                 |
-- | `AND`      | Логический оператор, который позволяет комбинировать несколько условий в `WHERE`.                            |
-- | `OR`       | Логический оператор, который позволяет использовать альтернативные условия в `WHERE`.                        |
-- | `NOT`      | Инвертирует условие, исключая записи, которые соответствуют условию.                                         |
-- | `BETWEEN`  | Используется для фильтрации значений в заданном диапазоне (включительно).                                    |
-- | `IN`       | Позволяет указать несколько значений в условии `WHERE`, чтобы выбрать записи, соответствующие любому из них. |
-- | `LIKE`     | Используется для поиска по шаблону, например, с использованием символов подстановки `%` и `_`.               |
-- | `ORDER BY` | Упорядочивает результаты выборки по указанному столбцу (или столбцам).                                       |
-- | `ASC`      | Указывает, что результаты должны быть отсортированы в порядке возрастания (по умолчанию).                    |
-- | `DESC`     | Указывает, что результаты должны быть отсортированы в порядке убывания.                                      |
-- | `COUNT()`  | Агрегатная функция, которая возвращает количество строк, соответствующих заданному условию.                  |
-- | `MIN()`    | Агрегатная функция, которая возвращает минимальное значение в указанном столбце.                             |
-- | `MAX()`    | Агрегатная функция, которая возвращает максимальное значение в указанном столбце.                            |

-- SQL - декларативный язык программирования. Это означает что  на выборку данных в SQL не содержат инструкций по тому как получить результат. Вместо этого мы описываем что мы хотим получить.

-- Выборка данных из таблицы начинается с ключевого слова `SELECT`
-- Затем нам надо указать из какой таблицы мы хотим получить данные. Для этого используется ключевое слово `FROM`


-- 1. Выбрать всё из таблицы marvelcharacters
SELECT *
FROM marvelcharacters

-- 2. Выбрать имена и частоту появлений из таблицы marvelcharacters
SELECT name, APPEARANCES
FROM marvelcharacters

-- 3. Мы можем задать порядок столбцов и псевдонимы
SELECT APPEARANCES as "Количество появлений", name as "Имя"
FROM marvelcharacters

-- WHERE - ГДЕ. Возможность фильтровать данные по заданным условиям
-- В условии WHERE мы можем использовать следующие операторы сравнения:
-- = равно
-- != или <> не равно
-- > больше
-- < меньше
-- >= больше или равно
-- <= меньше или равно
-- BETWEEN значение BETWEEN начало AND конец (включительно)
-- IN (значение1, значение2, ...) - проверка на вхождение в список значений
-- LIKE - для поиска по шаблону, где:
--   % - любое количество любых символов
--   _ - один любой символ
-- IS NULL - проверка на NULL
-- IS NOT NULL - проверка на не NULL

-- Логические операторы для комбинации условий:
-- AND - логическое И (все условия должны выполняться)
-- OR - логическое ИЛИ (должно выполняться хотя бы одно условие)
-- NOT - логическое отрицание

-- 4. Найдем записи младше 1940
SELECT name, APPEARANCES, year
FROM MarvelCharacters
WHERE year < 1940

-- 5. Добавьте второе условие. Появлений БОЛЬШЕ 5
SELECT name, APPEARANCES, year
FROM MarvelCharacters
WHERE year < 1940 AND APPEARANCES > 5

-- 6. Уберем из запроса №4 выдачу, где appearances null
SELECT name, APPEARANCES, year
FROM MarvelCharacters
WHERE year < 1940
AND APPEARANCES IS NOT NULL

-- 7. Попробуйте получить персонажей между 1940 и 1945 годом включительно
SELECT name, APPEARANCES, year
FROM MarvelCharacters
WHERE year BETWEEN 1940 AND 1945
-- Как сделать сортировку?
ORDER BY year DESC

-- 8. Два признака сортировки
SELECT name, APPEARANCES, year
FROM MarvelCharacters
WHERE year BETWEEN 1940 AND 1945
AND APPEARANCES IS NOT NULL
AND APPEARANCES > 5
ORDER BY year ASC, APPEARANCES DESC

-- 9. Равенство со строками и AND или IN Aug-62 Mar-41
SELECT name, appearances, FIRST_APPEARANCE
FROM marvelcharacters
WHERE FIRST_APPEARANCE = 'Aug-62'
OR FIRST_APPEARANCE = 'Mar-41'
ORDER BY FIRST_APPEARANCE

-- Вариант с IN - похожий, но компактный и читается проще
SELECT name, appearances, FIRST_APPEARANCE
FROM marvelcharacters
WHERE FIRST_APPEARANCE IN ('Aug-62', 'Mar-41')
ORDER BY FIRST_APPEARANCE

-- 10. Попробуйте получить персонажей у которых name = "Spider-Man (Peter Parker)"
SELECT name, year, appearances
FROM marvelcharacters
WHERE name = 'Spider-Man (Peter Parker)'

-- LIKE - поиск по шаблону. % - любое количество любых символов, _ - один любой символ
SELECT name, year, appearances
FROM marvelcharacters
WHERE name LIKE '%spider%man%'
OR name LIKE "%peter%parker%"

-- Уникальные значения - DISTINCT. Получить itentify 

SELECT DISTINCT SEX
FROM marvelcharacters

-- GROUP BY - результат такой же, но выполняется в 5 раз дольше. Потому что мы группируем ВСЕ 16 тыс строк в группы.

SELECT SEX
FROM marvelcharacters
GROUP BY SEX


-- А как бы добавить еще столбец с количеством строк в группе?


SELECT SEX, COUNT(*)
FROM marvelcharacters
GROUP BY SEX

-- А как тут будет работать фильтрация?

SELECT SEX, COUNT(*) as total
FROM marvelcharacters
WHERE SEX IS NOT NULL
GROUP BY SEX
ORDER BY total DESC


-- А как будет работать фильтрация ВЫЧИСЛЕНИЙ полученных от группировки?
-- HAVING - фильтрация по вычисленным значениям

SELECT SEX, COUNT(*) as total
FROM marvelcharacters
WHERE SEX IS NOT NULL
GROUP BY SEX
HAVING total > 50
ORDER BY total DESC


-- Функция MAX - максимальное значение в столбце. Найдем самую популярную девушку

SELECT name, SEX, MAX(APPEARANCES)
FROM marvelcharacters
WHERE SEX = 'Female Characters'


-- LIMIT - ограничение количества строк в результате
-- OFFSET - смещение результата на указанное количество строк

SELECT name, SEX, appearances
FROM marvelcharacters
WHERE SEX = 'Female Characters'
ORDER BY appearances DESC
LIMIT 5

-- 11. Группируем по цвету глаз, и выводим имя и количество появлений с этим цветом глаз лидера по появлениям MAX(APPEARANCES)

SELECT EYE, name, max(APPEARANCES), appearances
FROM marvelcharacters
GROUP BY EYE
ORDER BY appearances DESC


SELECT name, EYE, MAX(APPEARANCES), APPEARANCES, COUNT(*)
FROM MarvelCharacters
GROUP BY EYE
ORDER BY COUNT() DESC;