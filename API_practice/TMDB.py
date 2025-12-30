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

# API 요청 함수 호출
response = requests.get(request_url, params=params, headers=headers)


# 응답 데이터 처리(json -> python)
response_data = response.json()

# 응답 데이터 자료형 출력
print(type(response_data))

# 응답 데이터 출력
pprint(response_data)