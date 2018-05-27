# Introduction

StudyWhere project of Team 'SoftWhere'


# 팀 프로젝트 목표 및 가이드라인
## 평가 항목
### 구현
>In final presentation, we will evaluate a completeness of your implementation

= *완성도*를 볼 것

### 설계
* 테이블 5개 이상, 정규형은 2NF 이상
* 시스템을 나타내는 Entity-Relationship Diagram을 그려야 한다.
    * MySQL WorkBench의 EER Diagram 기능 사용
* ER Diagram을 바탕으로 설계한 스키마를 보여야 한다.
* 스키마가 정규형(2NF, 3NF, ...)을 만족한다는 것을 보여야 한다.

### SQL
서비스에서 다음의 쿼리문을 사용해야 한다.

* DDL
    * `CREATE TABLE`
        * [ ] MySQL WorkBench에서 스키마만 SQL 문으로 내보내서 만든다.
    * `INSERT INTO TABLE`
        * [ ] SQLAlchemy ORM을 사용하여 DB에 새 항목을 추가하는 코드를 찾아서 보여준다.
* DML
    * Selection & projection (`SELECT`)
        * [ ] 뷰 함수와 템플릿에서 ORM 객체와 상호작용하는 코드를 찾아서 보여준다.
    * `JOIN`
        * [ ] 뷰 함수와 템플릿에서 ORM 객체와 상호작용하는 코드를 찾아서 보여준다.
    * Subquery
        * [ ] 뷰 함수와 템플릿에서 ORM 객체와 상호작용하는 코드를 찾아서 보여준다.
    * Aggregation
        * [ ] 뷰 함수와 템플릿에서 ORM 객체와 상호작용하는 코드를 찾아서 보여준다.

### 선택사항
* 아래 항목 중 한 가지 이상을 사용한다.
    * View
    * Trigger
    * Stored Procedure
    * PL/SQL: SQL에 프로그래밍 언어의 요소(조건문, 반복문 등)를 추가한 언어. => X

## 최종 발표
* 서비스에 대한 간단한 소개
* ER Diagram과 스키마를 보여주고 설명
* 서비스 시연
    * 어떤 SQL문을 사용했는지 설명하고 결과를 보여준다.


# 프로젝트 디렉토리 설명
* `/ui-samples/`: 템플릿 만들 때 참고할 HTML 샘플
* `/static/`: 이미지, CSS, JS 파일 경로

# 사용하는 라이브러리
## JavaScript / CSS:
* jQuery 3.3.1 (slim)
* Bootstrap 4.1.1 (bundle)
* Bootstrap Datepicker 1.8.0

# 사용하는 이미지
* `crowd-1.png`, `crowd-2.png`, `crowd-3.png`: By [Oksana Latysheva](https://thenounproject.com/latyshevaoksana/)
* `like-0.png`, `like-1.png`, `like-2.png`, `like-3.png`, `crowd-0.png`: By [shashank singh](https://thenounproject.com/rshashank19/)