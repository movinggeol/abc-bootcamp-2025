import time
import requests
import json

def melon_search(query: str) -> list:
    # 원본 url = https://www.melon.com/search/keyword/index.json?jscallback=jQuery19104406029060066261_1753756079350&query=idol&_=1753756079354
    search_url = "https://www.melon.com/search/keyword/index.json"

    # Query Parameters
    params = {
        "jscallback": "jQuery19104406029060066261_1753756079350",
        f"query": "{query}",
        "_": int(time.time()), # _ = ms, 브라우저가 최신 데이터로 검색되도록
    }

    # 이게 없으면 Your user agent는 python일 것, 멜론에서 이것을 막아둠, 구글에서
    # 'what is my user agent' 검색 후 header에 복붙
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }

    res = requests.get(search_url, params=params, headers=headers)
    #print(res)
    #print(res.text)

    # response format : json (o), jsonp (o)
    if res.status_code == 200: # 정상 상태 코드
        jsonp_string = res.text
        json_string = jsonp_string[2:-2] # hard coding
        return json.loads(json_string)
    return []

# 현재 소스파일이 파이썬 실행의 진입점일 때
if __name__ == "__main__":
    print(melon_search("idol"))

'''
# 원본 url = https://www.melon.com/search/keyword/index.json?jscallback=jQuery19104406029060066261_1753756079350&query=idol&_=1753756079354
search_url = "https://www.melon.com/search/keyword/index.json"

    # Query Parameters
params = {
    "jscallback": "jQuery19104406029060066261_1753756079350",
    f"query": "{query}",
    "_": int(time.time()), # _ = ms, 브라우저가 최신 데이터로 검색되도록
}

    # 이게 없으면 Your user agent는 python일 것, 멜론에서 이것을 막아둠, 구글에서
    # 'what is my user agent' 검색 후 header에 복붙
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

res = requests.get(search_url, params=params, headers=headers)
print(res)
print(res.text)

'''
