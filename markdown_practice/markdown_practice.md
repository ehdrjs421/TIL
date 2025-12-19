# 마크다운

## '#+space 제목'

```
## 제목1
### 제목3
#### 제목4
##### 제목5
###### 제목6
```

## 목록
순서가 없는 목록 : -, *, +

- 목록
* 목록
  * 목록
    + 목록

순서가 있는 목록 : 1. 2. 3.

1. 목록
2. 목록
   1. 목록
   2. 목록
   3. 목록 (넘버링 자동화 5-> 3)

## 문자 서식
굵게, 기울임, 취소

**굵게**, __굵게__  
*기울임*, _기울임_
~~취소~~

개행하고 싶다면, 문당 뒤 space 2번 입력

## 코드
인라인 코드 : 문장 중간에 코드를 삽입하고 싶을 때

> 파이썬에서 문장을 출력할 땐 `print()`

블럭 코드 : 코드에 언어를 선택하여, syntax highligiht를 넣을 수 있다.

```python
for i in range(10):
    print(i)
```

```bash
touch a.txt
mv a.txt hello
```

## 링크
'[표시글자](url)'

[LMS](https://learn.dailyalgo.kr/courses/%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4-%EB%AC%B8%EC%A0%9C-%ED%95%B4%EA%B2%B0%EC%9D%84-%EC%9C%84%ED%95%9C-%EC%8B%A4%EB%AC%B4%ED%98%95-ai%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B6%84%EC%84%9D-%EA%B3%BC%EC%A0%95-2%EA%B8%B0/2cb611ac-3a00-800c-b753-fb7f955e29cc)

## 이미지

' ![이미지](주소) '

![git 로고](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Git-logo.svg/1024px-Git-logo.svg.png)



## 인용
이렇게 '>이렇게'

## 표
| 동물 | 종류 | 다리수 |
|---- |----|----|
|사자|표유류 |4개|

마크다운으로 표 만들때, 직접 그려도 되지만 에디터들의 도움 받기
[표링크](https://www.tablesgenerator.com/markdown_tables)