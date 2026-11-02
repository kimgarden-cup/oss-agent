# week09 - 박스오피스 도구

## 무엇을 하는 코드인가
영화진흥위원회(KOBIS) Open API로 일별 박스오피스를 조회합니다.
- `get_boxoffice_rank_1(date)`: 그날 1위 영화 제목을 돌려줍니다.
- `get_movie_audience(date, title)`: 그날 해당 영화의 관객 수(예: `"123,456명"`)를 돌려줍니다.

날짜는 `"20260824"`처럼 8자리 문자열로 넣습니다.

## 설치
```bash
pip install -r requirements.txt
```
같은 폴더에 `secret.py`를 만들고 KOBIS API 키를 넣습니다.
```python
API_KEY = "발급받은_키"
```

## 실행
```bash
python main.py
```
