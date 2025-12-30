import requests

# 주소(https://jsonplaceholder.typicode.com/)에 HTTP 통신 요청
# response = requests.get("https://jsonplaceholder.typicode.com/")

# 응답받은 HTML 문서 텍스트를 변수 doc에 할당
# doc = response.text

url = "https://google.com"

response = requests.get(url=url)

doc = response.json()
for i in doc:
    print(i,end=" : ")
    print(doc[i])
# print(doc)

