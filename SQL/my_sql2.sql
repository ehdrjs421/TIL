-- Active: 1769567196501@@127.0.0.1@3306@world
USE world;

SHOW TABLES;

SELECT Name, Population
FROM city;


SELECT c.Continent AS 대륙, c.Name AS 국가, c.Population AS 인구, c.IndepYear
FROM country AS c
WHERE Continent = 'Asia'
    AND Population > 1000000
    AND IndepYear > 1990;

SELECT *
FROM country AS c
WHERE c.Name LIKE 'S%S%S';


--------------------------------------------------- 실습 1
SELECT * FROM city;

SELECT c.Name, c.Population
FROM city AS c
WHERE c.`Population` >= 8000000;


SELECT c.`Name`, c.`CountryCode`
FROM city AS c
WHERE c. `CountryCode` = "KOR";

SELECT c.Name
FROM city AS c
WHERE c.`Name` LIKE "San%";

SELECT c.Name
FROM city AS c
WHERE c.`Population` BETWEEN 1000000 AND 2000000
    AND c.`CountryCode` = 'KOR';

SELECT c.Name, c.`CountryCode`, c.`Population`
FROM city AS c
WHERE c.`Population` >= 5000000
    AND c.`CountryCode` IN ('KOR','JPN','CHN');


SELECT *
FROM country;

SELECT c.`Name`,c.`Population`, c.`LifeExpectancy`, c.`Continent`
FROM country AS c
WHERE c.`Continent` = 'Oceania'
    AND c.`LifeExpectancy` IS NULL;

SELECT Region, COUNT(Name) ,AVG(Population) as avg_pop
FROM country
GROUP BY Region;


-------------------
SELECT co.`Continent`, COUNT(*)
FROM country AS co
GROUP BY co.`Continent`;


----------------------------- 실습 2
SELECT co.`Continent`, SUM(co.`Population`)
FROM country as co
GROUP BY co.`Continent`;

SELECT co.`Region`, MAX(co.`GNP`)
FROM country AS co
GROUP BY co.`Region`;

SELECT co.`Continent`, AVG(co.`GNP`), AVG(co.`Population`)
FROM country AS co
GROUP BY co.`Continent`;

SELECT c.`District`, COUNT(*)
FROM city AS c
WHERE c.`Population` BETWEEN 500000 and 1000000
GROUP BY c.`District`;

SELECT co.`Region`, SUM(co.`GNP`) '총 GNP'
FROM country AS co
WHERE co.`Continent` = 'Asia'
GROUP BY co.`Region`;