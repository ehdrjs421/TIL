-- Active: 1769567196501@@127.0.0.1@3306@world
USE sakila;

-- 고객을 조회하시오. 

WITH Actionsrentor AS (
    SELECT DISTINCT r.customer_id
    FROM rental r
    JOIN inventory i ON r.inventory_id = i.inventory_id
    JOIN film_category fc ON i.film_id = fc.film_id
    JOIN category cat ON fc.category_id = cat.category_id
    AND cat.name = 'Action'
)
SELECT c.first_name, c.last_name
FROM customer c
    LEFT JOIN Actionsrentor AS ar
    ON ar.customer_id = c.customer_id
WHERE ar.customer_id IS NULL;


WITH bestcustomer AS (
    SELECT customer_id
    FROM rental
    GROUP BY customer_id
    HAVING COUNT(*) >= 40
),
filmrental AS (
    SELECT DISTINCT i.film_id
    FROM bestcustomer as bc
        LEFT JOIN rental AS r USING(customer_id)
        LEFT JOIN inventory AS i USING(inventory_id)
)
SELECT f.title
FROM film AS f
    JOIN filmrental AS fr ON fr.film_id = f.film_id
;


------------------------------ 실습 10
USE sakila;

SELECT CONCAT(c.first_name,', ',c.last_name) AS full_name
FROM customer AS c;

SELECT UPPER(f.title), LOWER(f.description)
FROM film AS f;

SELECT c.email, SUBSTRING_INDEX(c.email,'@',1)
FROM customer AS c;


SELECT p.amount,ROUND(p.amount,1) 반올림, CEIL(p.amount) 올림, TRUNCATE(p.amount,1) 버림
FROM payment AS p;

SELECT DATE_FORMAT(r.rental_date,'%Y-%m-%d (%a)')
FROM rental AS r;

SELECT DATE_FORMAT(r.rental_date , '%a'),count(*),SUM(p.amount)
FROM rental AS r
    JOIN payment AS p USING(rental_id)
GROUP BY DATE_FORMAT(r.rental_date, '%a');

SELECT DATEDIFF(r.return_date,r.rental_date)
FROM rental AS r;

-------------------------------- 실습 11
USE world;

SHOW TABLES;

SELECT  c.`Name`,c.`Continent`,c.`LifeExpectancy`,c.`GNP`
FROM country AS c
WHERE c.`LifeExpectancy` IS NULL
    OR c.`GNP` IS NULL;

SELECT c1.`Name`,COALESCE(c1.`LifeExpectancy`,c2.avg_le)
FROM country AS c1
    JOIN (
        SELECT c.`Continent`, AVG(c.`LifeExpectancy`) AS avg_le
        FROM country AS c
        GROUP BY c.`Continent`
    ) AS c2 ON c2.`Continent` = c1.`Continent`
-- WHERE c1.`Name` = 'Christmas Island'
;


SELECT
    Name,
    if( GovernmentForm LIKE '%Republic%', 'Republic', GovernmentForm) AS GovernmentForm
FROM country;

SELECT c.`Name`, c.`Population`/c.`SurfaceArea`
FROM country AS c
WHERE c.`SurfaceArea` <> 0
    AND c.`Population` <> 0
ORDER BY c.`Population`/c.`SurfaceArea` ASC;
