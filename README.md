# 🤖 RPA Mini Projects — BrityRPA 기반 업무 자동화

> 작성자: **김한결**
> 개발 기간: 2026.05 ~ 2026.06
> 플랫폼: **BrityRPA** (Workflow Automation)

두 건의 미니 프로젝트를 통해 RPA 워크플로우 설계, 외부 API 연동, 웹 자동화, 예외처리 로직 설계 경험을 다뤘습니다. 각 프로젝트는 PDD(Process Definition Document) 기반으로 설계하고 실제 데이터로 동작을 검증했습니다.

---

## 📌 프로젝트 목록

| # | 프로젝트명 | 핵심 내용 | 사용 기술 |
|---|-----------|-----------|-----------|
| 1 | [GPT API 기반 이미지 분석 & 생성 자동화](#project-1--gpt-api-기반-이미지-분석--생성-자동화) | 엑셀 데이터 → GPT 이미지 분석/요약/생성 → 결과 메일 발송 | BrityRPA, GPT API, Python, Excel |
| 2 | [제조사별 판매실적 시각화 자동화](#project-2--제조사별-판매실적-시각화-자동화) | 웹 데이터 수집 → 정제 → 조건부 서식 리포트 생성 | BrityRPA, Chrome 자동화, Excel |

---

## Project 1 — GPT API 기반 이미지 분석 & 생성 자동화

**개발 기간**: 2026.05.27 ~ 2026.05.29
**업무 요약**: 사용자의 요청사항에 맞는 이미지를 GPT API로 생성·분석하고, 결과를 자동으로 이메일 전송하는 파이프라인 구축

### 워크플로우 

<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0002" src="https://github.com/user-attachments/assets/96658b76-2643-4fe1-8ae0-d521fb2f99a0" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0003" src="https://github.com/user-attachments/assets/2df1b46c-59cc-466f-b9ba-ceeecdd2e9d4" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0004" src="https://github.com/user-attachments/assets/287585cc-fdd8-47ee-a7bb-251a30b74712" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0005" src="https://github.com/user-attachments/assets/0bb3c7f6-0ff5-40e7-ab69-4dcd08416d4e" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0006" src="https://github.com/user-attachments/assets/5b3a9953-a4cc-4fd3-b181-9cf89c2a0a80" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0007" src="https://github.com/user-attachments/assets/bfa5490c-03b5-4c26-9a12-072fb0cfd0e7" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0009" src="https://github.com/user-attachments/assets/a0d745cb-0f2f-4be6-bf14-832498ca7589" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0008" src="https://github.com/user-attachments/assets/35146a09-7e0e-4467-a587-b2a84b7b6571" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0010" src="https://github.com/user-attachments/assets/29a7540d-7e1c-4d4d-8a27-86631874bca0" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0011" src="https://github.com/user-attachments/assets/ad85f84c-8354-47d1-b626-0f3db4bde045" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0012" src="https://github.com/user-attachments/assets/6cf6c737-3ed2-4141-bcf4-e860c1f8a324" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0013" src="https://github.com/user-attachments/assets/7978d900-bd6c-4725-8fd9-4d5b3e96d155" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0014" src="https://github.com/user-attachments/assets/7f4ead36-9f97-485c-b14c-86a0de3d178a" />


### 핵심 구현 & 트러블슈팅

- **API 연동 및 예외처리**: `SendRequest`로 GPT API를 호출하는 각 구간에 `Try-Catch` + `Goto` 롤백을 적용해, 호출 실패 시 자동 재시도되도록 구성하여 데이터 누락을 방지했습니다.
- **반복 구간 변수 초기화 이슈 해결**: `For` 카드 진입 전 응답값을 담을 변수(`this.responseinput`, `this.summaryinput`)를 배열 형태로 미리 선언해, 반복마다 초기화되어 데이터가 누락되는 문제를 해결했습니다.
- **데이터 무결성 확보**: 엑셀에서 추출한 값을 `ToJson`으로 변환/재할당하여 API 요청 시 데이터 누락 없이 전달되도록 설계했습니다.
- **파일 중복 방지**: 반복 생성되는 이미지·텍스트 파일명에 요청자 이름을 동적으로 부여(`RenameFile`)하여 덮어쓰기 문제를 방지했습니다.
- **결과 검증**: 요청자별 이미지 생성 성공/실패 여부에 따라 메일 본문이 동적으로 분기되어 발송되는 것까지 실제로 확인했습니다.

### 사용 기술
`BrityRPA` · `GPT API (SendRequest)` · `Python` · `Excel`

### 최종 산출물
- 요청자별 분석 결과 엑셀 파일
- 생성 이미지 & 분석 텍스트 파일
- 요청자 메일함 자동 발송 완료

---

## Project 2 — 제조사별 판매실적 시각화 자동화

**개발 기간**: 2026.06.01 ~ 2026.06.05
**업무 요약**: 다나와 자동차 사이트에서 제조사·기간별 판매 데이터를 수집해 정제 후, 조건부 서식이 적용된 엑셀 리포트를 자동 생성

### 워크플로우 

<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0016" src="https://github.com/user-attachments/assets/f13ab29b-a095-47c6-9c0a-4e1c5531c196" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0017" src="https://github.com/user-attachments/assets/40d0ec70-efe2-479d-a502-5788641e3e41" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0018" src="https://github.com/user-attachments/assets/2cdc732b-edc9-4d5b-abce-4bf9187186e8" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0019" src="https://github.com/user-attachments/assets/a7c269f1-4f97-438a-b028-124d532e14a7" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0020" src="https://github.com/user-attachments/assets/ed511034-d829-43ac-ba4e-6043ed41cf6f" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0021" src="https://github.com/user-attachments/assets/d119247e-9392-4d94-9282-91b6992115c3" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0022" src="https://github.com/user-attachments/assets/4be119f7-cb28-4557-a5ff-a77a4438f54c" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0023" src="https://github.com/user-attachments/assets/605217f2-3013-45dd-bde7-83c139891e84" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0024" src="https://github.com/user-attachments/assets/6ac0bf25-f7f8-4a80-bf45-d14669628b9c" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0025" src="https://github.com/user-attachments/assets/e6f89fd3-d81a-46f6-8435-da0dda7be0d4" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0026" src="https://github.com/user-attachments/assets/bf02c3e5-c1f3-4357-907a-73ab65e92b46" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0027" src="https://github.com/user-attachments/assets/9889a6c1-88d0-4aa0-b3bf-015e87f4c215" />
<img width="2000" height="1125" alt="김한결_RPA프로젝트_page-0028" src="https://github.com/user-attachments/assets/5b047cfa-f7e2-4623-babe-fb7ea0d9f711" />


### 핵심 구현 & 트러블슈팅

- **입력 검증 로직**: `InputBox`로 입력받은 조회 기간을 `ExecuteScript`로 정해진 양식과 비교·검증하고, `Today()` 함수 기반으로 유효하지 않은 기간 입력을 사전에 걸러내는 `do-while` 구조를 설계했습니다.
- **조회 실패 시 자동 복구**: 조회하려는 제조사를 찾지 못하거나 데이터가 없을 경우, 자동으로 데이터 입력 단계로 되돌아가 재입력을 요청하도록 구성했습니다.
- **웹 자동화 최적화**: 판매 실적 페이지 객체가 이미 존재하는 경우 페이지 이동 작업을 건너뛰도록 분기 처리하여 불필요한 반복을 줄였습니다.
- **데이터 정제 파이프라인**: 연료별 데이터와 총합계 데이터를 병합해 하나의 데이터셋으로 통합하고, 2차원 배열 정제를 거쳐 엑셀 양식에 맞게 가공했습니다.
- **엑셀 리포트 자동화**: 조건부 서식으로 판매 등락에 따른 색상 구분을 적용하고, 누적판매 그래프 이미지를 좌표 기반 캡처(`CaptureBounds`, `ClipboradToFile`)로 삽입해 별도 가공 없이 바로 보고 가능한 리포트를 완성했습니다.
- **엑셀 라이센스 팝업 예외처리**: `IsExist` 카드로 라이센스 창 발생 여부를 확인 후 자동으로 처리하는 로직을 추가했습니다.
- **결과 검증**: 2026년 2월 현대차 26개 모델의 실데이터로 동작을 검증하고, `{년}년 {월}월 {제조사} 판매실적.xlsx` 형식으로 자동 저장되는 것을 확인했습니다.

### 사용 기술
`BrityRPA (Web Automation)` · `Chrome (auto.danawa.com)` · `Excel (조건부 서식 · 그래프)`

### 최종 산출물
- 제조사·기간별 판매실적 엑셀 리포트
- 누적판매 그래프 자동 삽입
- 조건부 서식 적용 완료 보고서

---

## 💡 회고

두 프로젝트를 통해 **API 연동 자동화(비정형 데이터 처리)** 와 **웹 스크래핑 기반 리포트 자동화(정형 데이터 처리)** 라는 서로 다른 유형의 RPA 업무를 경험했습니다. 특히 반복 구간에서의 변수 초기화 문제, API 호출 실패에 대한 예외처리, 웹 조회 실패 시 복구 로직 등 실무에서 자주 마주치는 안정성 이슈를 직접 설계하고 해결하며 RPA 워크플로우의 견고성을 높이는 방법을 익혔습니다.

---

## 📁 참고 문서
- `김한결_RPA프로젝트.pptx` — 두 프로젝트의 PDD(순서도, 세부 Activity, 작업 절차) 원본 문서
