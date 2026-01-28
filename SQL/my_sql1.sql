USE world;

SHOW TABLES;

SELECT *
FROM city
LIMIT 5;

SELECT c.`Name`, c.`District`, c.`Population`
FROM city AS c
WHERE c.`Population` > 1000000; -- 인구가 100만 초과인 경우

/* 
여러줄
주석
*/
-- 데이터베이스 생성
SHOW DATABASES;

CREATE DATABASE lecture;

USE lecture;

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
);

SHOW TABLES;
-- 데이터베이스 추가 및 수정
ALTER TABLE `users`
ADD birthday DATE NOT NULL;

DESC users;

ALTER TABLE users
MODIFY name VARCHAR(20) NOT NULL;

CREATE TABLE test(
    id INT PRIMARY KEY,
    name VARCHAR(20)
);

DESC test;

SHOW TABLES;
-- 삭제
DROP TABLE test;

DROP TABLE IF EXISTS test;

-- 이름 변경

RENAME TABLE users
TO user_info;

-- 생성 쿼리 구경하기
SHOW CREATE TABLE user_info;

-- DML 데이터 조작
SELECT *
FROM user_info;
-- 데이터 입력
INSERT INTO user_info (user_id, name, email, birthday)
VALUES (101,'alex','alex@example.com','2002.01.01');

SELECT *
FROM user_info;

INSERT INTO user_info (user_id, name, email, birthday)
VALUES  (102,'jun','jun@example.com','1996.10.30'),
        (103,'chelsea','chelsea@example.com','1990.01.20');

-- INSERT INTO user_info (user_id, name)
-- VALUES (104,'ken');

INSERT INTO user_info (user_id, name, birthday)
VALUES  (104,'ken','1976.12.03');

-- 데이터 조회

SELECT *
FROM user_info
WHERE birthday < '2000.01.01';

-- 데이터 수정
UPDATE user_info
SET birthday = '1988-12-31'
WHERE name = 'jun';

-- 데이터 삭제
DELETE FROM user_info
WHERE user_id = 101;


-------------------------------------------------------
-- 실습

CREATE DATABASE practice;

USE practice;

CREATE TABLE student(
    student_id int AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    grade int
);

SELECT *
FROM student;

INSERT student (name,grade) VALUES
('홍길동',3),
('김철수',2),
('박병철',1),
('안새싹',3);

UPDATE student
SET grade = 4
WHERE name = '안새싹';

DELETE FROM student
WHERE grade = 2;

DROP DATABASE IF EXISTS practice;

