import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()  # .env 파일의 변수들을 환경변수로 등록
api_key = os.getenv('TMDB_KEY')  # 환경변수에서 API 키 불러오기


# API 요청을 위한 기본 URL
base_url = "https://api.themoviedb.org/3"

# 어떤 API를 요청할지 결정하는 url(엔드포인트)
endpoint = "movie/now_playing"

# API 요청에 포함할 추가 정보(파라미터)
params = {
    "language": "ko-KR",
    "api_key": api_key,
}

headers = {"accept": "application/json"}

# API 요청 URL 조합
request_url = f"{base_url}/{endpoint}"
data_list = []
for i in range(5):
    params["page"] = i + 1
# API 요청 함수 호출
    response = requests.get(request_url, params=params, headers=headers)


# 응답 데이터 처리(json -> python)
    response_data = response.json()
    data_results = response_data['results']
    for j in data_results:
        data_list.append([j['title'],j['vote_average']])

data_list.sort(key = lambda x: -x[1])

print(f"{data_list[0][0]} / {data_list[0][1]}")

params = {
    "language": "en-US",
    "api_key": api_key,
}

response = requests.get(request_url, params=params, headers=headers)
response_data = response.json()
data_results = response_data['results']
data_results.sort(key = lambda x: -x['vote_average'])
vote = data_results[0]['original_title']
votes = data_results[0]['id']
endpoint = f"movie/{votes}/reviews"
request_url = f"{base_url}/{endpoint}"

response = requests.get(request_url, params=params, headers=headers)
response_data = response.json()
pprint(response_data['results'])