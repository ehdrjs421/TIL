import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()  # .env 파일의 변수들을 환경변수로 등록
serviceKey = os.getenv('WEA_KEY')  # 환경변수에서 API 키 불러오기
print(serviceKey)
base_url = "https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0"
endpoint = "getUltraSrtFcst"

# 요청 추가 정보(파라미터)
base_data =  '20251228'
base_time = '0100'
nx =  '55'
ny =  '127'

params = {
    "serviceKey": serviceKey,
    "pageNo": "1",
    "numOfRows": "1000",
    "dataType": "JSON",
    "base_date": base_data,
    "base_time": base_time,
    "nx": nx,
    "ny": ny,
}

request_url = f"{base_url}/{endpoint}"

# API 요청
response = requests.get(request_url, params=params)

# 응답 데이터 처리
response_data = response.json()
data = response_data['response']['body']['items']['item']
T1H = []
for i in data:
    if i['category'] == 'T1H':
        T1H.append([i['fcstDate'],i['fcstTime'],i['fcstValue']])

pprint(T1H)

REH = []
for i in data:
    if i['category'] == 'REH':
        REH.append([i['fcstDate'],i['fcstTime'],i['fcstValue']])
        
pprint(REH)