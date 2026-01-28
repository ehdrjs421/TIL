# SQL 
> 데이터를 보는 언어가 아닌 데이터에 질문하는 언어

+ 테이블(table)이라는 구조에 저장도니 데이터를 대상으로 작동
+ 공통 키(key)로 연결된 여러 테이블을 조합
  + 필요한 데이터
  + 원하는 조건
  + 원하는 형태  
  
+  기본 문장 구조
```SQL
SELECT [칼럼/식]
FROM [테이블]
WHERE [조건];
```
   + SELECT : 무엇을 볼 것인가
   + FROM : 어디에서 가져올 것인가
   + WHERE : 어떤 조건으로 볼 것인가


## SQL의 종류
+ 기능별로 DDL, DML, DCL로 분류하며 경우에 따라 TCL을 따로 구분하기도 한다. 
![이미지](https://www.notion.so/image/attachment%3A97ce2947-fe88-417d-b0b5-6aa3e5a29196%3Aimage.png%3FspaceId%3Df2678325-6f7b-4a25-b188-86c42030d6d5?table=block&id=2f6611ac-3a00-8011-aa87-f5af226bd68a&cache=v2)
  
+ DDL (Data Definition Language)
  + 데이터 구조 정의를 위한 명령어 집합
+ DML (Data Manipulation Language)
  + 데이터 조작을 위한 명령어 집합
+ DCL (Data Control Language)
  + 권한 제어 및 데이터 보안 무결성 유지
+ TCL (Transaction Control Language)
  + 트랜잭션(DML 작업의 일종) 진행 중 작업을 확정하거나 되돌리는 명령어
  

## DDL / DML

|DDL|DML|
|------|---|
|데이터 베이스의 구조를 정의|구조 안의 데이터 내용을 다룸|
|테이블 컬럼 등의 스키마|실제 데이터|
|시스템 전체에 영향|데이터 상태에 영향|

### DDL
> 데이터베이스의 구조를 생성 변경 삭제 하는 SQL 명령어
 + 데이터가 없어도 실행 가능
 + 무엇을 저장할 것인지 구조화 하는 단계
  
#### 1. CREATE (생성)
```SQL
-- 데이터 베이스 생성
CREATE DATABASE 데이터베이스이름;

-- 테이블 생성
CREATE TABLE 테이블명 (
    컬럼명 데이터타입 [제약조건]
)
```
<details>
<summary>데이터 타입</summary>

<div markdown="1">

### 1. 숫자 타입
- **INT** : 정수
- **BIGINT** : 큰 정수
- **DECIMAL(p, s)** : 고정 소수점 실수 (정확한 계산 필요 시)
- **FLOAT / DOUBLE** : 부동 소수점 실수 (근사값)

### 2. 문자 타입
- **CHAR(n)** : 고정 길이 문자열
- **VARCHAR(n)** : 가변 길이 문자열
- **TEXT** : 긴 문자열 (본문, 설명 등)

### 3. 날짜·시간 타입
- **DATE** : 날짜
- **TIME** : 시간
- **DATETIME** : 날짜 + 시간
- **TIMESTAMP** : 날짜 + 시간 (시스템 시간 기준)

### 4. 논리 타입
- **BOOLEAN / BOOL** : 참(True) / 거짓(False)

### 5. 기타 타입
- **ENUM** : 미리 정의된 값 중 하나
- **JSON** : JSON 형식 데이터
- **BLOB** : 이진 데이터 (이미지, 파일 등)

</div>
</details>

#### 2. ALTER
```SQL
-- 컬럼 추가
ALTER TABLE 테이블명
ADD 컬럼명 데이터타입 [제약조건];

-- 컬럼 수정
ALTER TABLE 테이블명
MODIFY 컬럼명 새로운데이터타입 [새로운제약조건];
```

#### 3. DROP
```SQL
--데이터베이스 삭제
DROP DATABASE IF EXISTS database_name; 

--테이블 삭제
DROP TABLE IF EXISTS student;
```

#### 4. RENAME
```SQL
RENAME TABLE old_table TO new_table;
```

### DML
> 크게 CRUD(Create, Read, Update, Delete)기능을 수행하는 명령어
> 
#### 1. INSERT
```SQL
-- 단일 행 입력
INSERT INTO table_name (column1, column2) 
VALUES (value1, value2);

-- 다중 행 입력
INSERT INTO table_name (column1, column2) VALUES
	(value1, value2),
	(value3, value4);
```

#### 2. SELECT
```SQL
SELECT name, email
FROM users
WHERE user_id > 100;
```

#### 3. UPDATE
```SQL
UPDATE table_name
SET columns_name = new_value
WHERE condition;
```

#### 4. DELETE
```SQL
DELETE FROM table_name
WHERE condition;
```
