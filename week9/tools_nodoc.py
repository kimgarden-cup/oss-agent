import requests
from secret import API_KEY
BASE_URL = ("https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json")

def get_boxoffice_rank_1(date):

    params= {"key": API_KEY, "targetDt": date}
    response = requests.get(BASE_URL, params=params, timeout=10)
    data = response.json()
    movies = data['boxOfficeResult']['dailyBoxOfficeList']
    return movies[0]["movieNm"]

def get_movie_audience(date, title):
    params = {"key": API_KEY, "targetDt": date}
    response = requests.get(BASE_URL, params=params, timeout=10)
    data = response.json()
    movies = data["boxOfficeResult"]["dailyBoxOfficeList"]

    for movie in movies:
        if movie["movieNm"] == title:
            audi = int(movie["audiCnt"])
            return f"{audi:,}명"

    return f"'{title}' 은(는) {date} 순위에 없습니다."