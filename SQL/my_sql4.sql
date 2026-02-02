-- Active: 1769567196501@@127.0.0.1@3306@sakila

USE world;

SHOW TABLES;

SELECT *
FROM city AS c
    JOIN country AS co
    ON  co.`Code` = c.`CountryCode`;

---------------------- 실습 6
SELECT c.first_name AS 이름,
        c.last_name AS 성,
        c.email AS 이메일,
        a.address AS 주소,
        ct.city AS 도시명
FROM 
    customer AS c
LEFT JOIN
    address AS a
    ON c.address_id = a.address_id
LEFT JOIN
    city AS ct
    ON ct.city_id = a.city_id;



SELECT c.first_name AS 이름,
        c.last_name AS 성,
        c.email AS 이메일,
        a.address AS 주소,
        ct.city AS 도시명
FROM 
    customer AS c
LEFT JOIN
    address AS a
    ON c.address_id = a.address_id
LEFT JOIN
    city AS ct
    ON ct.city_id = a.city_id
WHERE ct.city ='London';

SELECT ct.city, COUNT(*)
FROM 
    customer AS c
LEFT JOIN
    address AS a
    ON c.address_id = a.address_id
LEFT JOIN
    city AS ct
    ON ct.city_id = a.city_id
GROUP BY ct.city
ORDER BY count(*) DESC;

SELECT
    c.first_name AS 이름,
    c.last_name AS 성,
    a.address AS 주소,
    co.country AS 국가,
    ct.city AS 도시
FROM
    customer AS c
    LEFT JOIN address AS a USING(address_id)
    LEFT JOIN city as ct USING(city_id)
    LEFT JOIN country AS co USING(country_id);



SELECT
    a.last_name AS 성,
    COUNT(f.title) AS 영화수
FROM
    actor AS a
    JOIN film_actor AS fa ON fa.actor_id = a.actor_id
    JOIN film AS f ON f.film_id = fa.film_id
WHERE a.first_name = 'PENELOPE'
GROUP BY a.last_name;


----------------------------------
USE world;

DESC country;


SELECT co.`Name` AS 국가명, c.`Name` AS 수도명 , co.`Population` AS 인구수, co.`GNP`
FROM country AS co
    INNER JOIN city AS c ON c.`ID` = co.`Capital`
WHERE co.`Continent` = 'Asia';

CREATE VIEW asia_countries_view AS
SELECT co.`Name` AS 국가명, c.`Name` AS 수도명 , co.`Population` AS 인구수, co.`GNP`
FROM country AS co
    INNER JOIN city AS c ON c.`ID` = co.`Capital`
WHERE co.`Continent` = 'Asia';

SELECT *
FROM asia_countries_view AS acv
WHERE 인구수 < 100000000
ORDER BY 인구수 DESC
LIMIT 5;

DROP VIEW IF EXISTS asia_countries_view;

--------------------------- subquery

SELECT COUNT(*) AS count, CountryCode
FROM city
WHERE CountryCode IN 
			(SELECT CountryCode 
			FROM city 
			WHERE Name = 'Alexandria')
GROUP BY CountryCode;


----------------------------- 실습7
USE sakila;
SELECT DATABASE();
SHOW TABLES;

DESC film;

SELECT AVG(f.rental_rate)
FROM film AS f;

SELECT f.title AS 영화제목, f.rental_rate AS 가격
FROM film AS f
WHERE f.rental_rate >
(SELECT AVG(f.rental_rate)
FROM film AS f)
ORDER BY f.rental_rate DESC;

SELECT c.first_name AS 이름, p.payment_id, p.amount, (SELECT AVG(amount) FROM payment) AS 평균
FROM customer AS c
    JOIN payment AS p USING(customer_id)
WHERE c.customer_id = 5;


SELECT *
FROM film AS f
    JOIN film_category AS fc USING(film_id)
    JOIN category AS c USING(category_id)
WHERE c.name = 'Action';

SELECT i.inventory_id,film_id
FROM inventory as i
WHERE 
    i.film_id IN(
        SELECT f.film_id
        FROM film AS f
        JOIN film_category AS fc USING(film_id)
        JOIN category AS c USING(category_id)
        WHERE c.name = 'Action');


SELECT c.first_name
FROM customer AS c
JOIN address AS a USING(address_id)
JOIN city AS ct USING(city_id)
JOIN country AS co USING(country_id)
WHERE co.country = 'Canada';

SELECT c.first_name 이름, c.last_name 성, p_summary.total,p_summary.AVG
FROM customer AS c
JOIN (
    SELECT customer_id,  SUM(p.amount) AS total, AVG(p.amount) AS AVG
    FROM payment AS p
    GROUP BY customer_id
) AS p_summary ON p_summary.customer_id = c.customer_id
GROUP BY c.customer_id;

-------------------------------- 실습 8
USE sakila;

SELECT f.title
FROM film AS f
    JOIN film_category USING(film_id)
    JOIN category USING(category_id)
WHERE category.name = 'Action'

SELECT ft.title, f.description
FROM film AS f
    JOIN (
        SELECT f.title
        FROM film AS f
            JOIN film_category USING(film_id)
            JOIN category USING(category_id)
        WHERE category.name = 'Action'
    ) AS ft ON ft.title = f.title;

SELECT c.first_name, (
        SELECT MAX(r.rental_date)
        FROM rental AS r
        WHERE r.customer_id = c.customer_id
    )    
FROM customer AS c;