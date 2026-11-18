# boxoffice — KOBIS 박스오피스 조회 스킬

## 하는 일
날짜를 주고 박스오피스 1위 영화나 관객 수를 물으면, 영화진흥위원회(KOBIS) 일별 박스오피스를 조회해서 1위 영화 제목과 그 영화의 그날 관객 수를 알려 줌.
- 예: "2026년 11월 14일 박스오피스 1위 영화 알려줘" → 극장판 치이카와: 인어 섬의 비밀 / 57,190명

## 들어 있는 파일
- .claude/skills/boxoffice/SKILL.md
- .claude/skills/boxoffice/scripts/boxoffice.py
- .claude/skills/boxoffice/LICENSE

## 필요한 것
- 프로젝트 폴더(스킬을 실행하는 폴더)에 tools.py — 실제로 KOBIS 에 요청하는 함수가 들어 있음. 이 저장소의 week12/tools.py 를 쓰면 됨
- 프로젝트 폴더에 secret.py — 자기 KOBIS 키를 넣은 파일 (아래 "키" 참고)
- Python 3 와 requests 패키지 (`python -m pip install requests`)

## 설치
1. boxoffice 폴더를 프로젝트 폴더의 `.claude/skills/` 아래에 둠 → `.claude/skills/boxoffice/`
2. tools.py 와 secret.py 를 프로젝트 폴더 바로 아래에 둠
3. 프로젝트 폴더에서 Claude Code 를 실행하고 `/reload-skills` 를 침
4. 박스오피스를 물어보거나 `/boxoffice 2026년 11월 14일 1위 영화 알려줘` 처럼 직접 부름

## 바깥으로 요청하는 곳
- `https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json` (영화진흥위원회 오픈 API) 한 곳
- 보내는 값은 키(key)와 날짜(targetDt) 두 가지. 요청은 tools.py 에서 함

## 키
- 이 저장소에는 키가 없음. secret.py 는 .gitignore 로 빼 두었음
- KOBIS 오픈 API 에서 자기 키를 받아 프로젝트 폴더의 secret.py 에 `API_KEY = "자기 키"` 한 줄로 넣을 것
- 키를 SKILL.md, 스크립트, 커밋 어디에도 적지 말 것

## 권한
- SKILL.md 에 allowed-tools 가 없음. 따로 넓혀 둔 권한이 없음
- 그래서 스크립트를 실행할 때마다 Claude Code 가 `python .claude/skills/boxoffice/scripts/boxoffice.py rank 날짜` 같은 명령을 실행해도 되는지 물어봄. 명령 줄을 읽고 허락하면 됨
- 스크립트는 파일을 고치지 않고 결과 한 줄만 출력함

## 라이선스
- MIT License
- 전문은 `.claude/skills/boxoffice/LICENSE` 에 있음 (Copyright (c) 2026 김정원)
