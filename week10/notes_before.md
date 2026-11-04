# week9/tools.py 함수 정리

## 개요

`week9/tools.py.py`는 KOBIS(영화진흥위원회) 오픈 API로 일별 박스오피스 정보를 가져오는 도구 모음입니다.

- `requests` 라이브러리로 HTTP 요청을 보냅니다.
- API 키는 `secret.py`의 `API_KEY`에서 가져옵니다 (코드에 직접 적지 않음).
- `BASE_URL`: 일별 박스오피스 조회 엔드포인트 (`searchDailyBoxOfficeList.json`)

## 함수 목록

### `get_boxoffice_rank_1(date)`

주어진 날짜의 박스오피스 1위 영화 제목을 돌려줍니다.

| 항목 | 내용 |
| --- | --- |
| 받는 것 | `date` (문자열) — 8자리 날짜, 예: `"20260824"` |
| 돌려주는 것 | (문자열) 1위 영화 제목, 예: `"오디세이"` |

동작 순서:

1. `key`(API 키)와 `targetDt`(조회 날짜)로 쿼리 파라미터를 만듭니다.
2. `BASE_URL`에 GET 요청을 보냅니다 (타임아웃 10초).
3. 응답 JSON에서 `boxOfficeResult` → `dailyBoxOfficeList` 목록을 꺼냅니다.
4. 첫 번째 항목의 `movieNm`(영화 제목)을 반환합니다.

### `get_movie_audience(date, title)`

주어진 날짜에 특정 영화의 관객 수를 돌려줍니다.

| 항목 | 내용 |
| --- | --- |
| 받는 것 | `date` (문자열) — 8자리 날짜 / `title` (문자열) — 영화 제목 |
| 돌려주는 것 | (문자열) `"1,234명"` 형식의 관객 수, 또는 순위에 없을 때 안내 문장 |

동작 순서:

1. `get_boxoffice_rank_1`과 같은 방식으로 일별 박스오피스 목록을 받아옵니다.
2. 목록을 돌면서 `movieNm`이 `title`과 정확히 같은 항목을 찾습니다.
3. 찾으면 `audiCnt`(해당 일 관객 수)를 천 단위 쉼표를 붙여 반환합니다.
4. 없으면 `"'제목'은(는) 날짜 순위에 없습니다."`를 반환합니다.

## 눈에 띄는 점

- 두 함수가 API 호출 코드를 똑같이 반복하고 있어, 공통 함수로 묶을 수 있습니다.
- HTTP 오류나 잘못된 날짜·API 키에 대한 예외 처리가 없어 `KeyError` 등이 그대로 날 수 있습니다.
- 박스오피스 목록이 비어 있으면 `get_boxoffice_rank_1`에서 `IndexError`가 납니다.
- 제목은 완전히 같아야 찾을 수 있습니다 (띄어쓰기·부제 차이에 약함).
- 파일 이름이 `tools.py.py`로 되어 있어, `main.py`에서 `import tools`가 실패할 수 있습니다.
