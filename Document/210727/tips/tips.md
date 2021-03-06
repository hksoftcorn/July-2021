# 개발자의 나쁜 습관

> 최호근 컨설턴트



## 1. 코드관리

### 1.1. 즉시성

- 사소한 버그가 일으키는 나비효과는 예상보다 크다
  - 사소한 버그라고 디버깅을 미루면 후폭풍이 돌아온다.
  - 할 일 목록을 적극적으로 활용하자.

### 1.2. 가독성

- 코드는 가독성을 해치지 않는 선에서 간결해져야 한다.
- 코드의 접근성을 먼저 생각하고 "똑똑한" 코드는 그 다음에 생각하자.

### 1.3. 최적화

- 몇 바이트라도 최적화를 시키는 것은.. 프로젝트의 마지막에 두자.
- 너무 이른 최적화는 만악의 근원이다.

### 1.4. 코드관리

- 코딩 스타일을 지키지 않으면 진행하기 어려운 프로젝트가 된다.
- 작은 부분이라도 스타일을 꼭 지키자.
- 변수명을 명시적으로 정합니다.
- 미래의 내가 현재의 나를 욕하지 않도록 유지보수가 쉬운 코드를 작성합니다.

### 1.5. 로그관리

- 예외를 무시하든 에러를 보고하지 않는 라이브러리를 쓰든 오류 가능성을 숨기는 방법은 여러 가지 있다.
- 작은 에러 메세지를 즉각적으로 처리합니다.

### 1.6. 개발자 툴과 IDE 사용법

- 핫키, 단축키, 환경 세팅은 자신의 업무 효율성 측면에서 중요하다
- 코드 그 자체에 집중할 수 있게 합니다.

### 1.7. 소스코드 & 라이브러리 복붙

- 직접 써보고 분석하면서 익히는 것이 중요하다.
- 이 라이브러리가 현재 프로젝트에 딱 맞는 조각이 아닐지도 모릅니다. 항상 의심하면서 붙여넣습니다.



## 2. 팀워크

### 2.1. 계획을 자꾸 바꾸기

- 계획 변경은 개발 기간을 고려하여 신중하게 

### 2.2. 실현 가능성이 낮은 계획 고집하기

- 실현 불가능한 것을 고집하지 말자. ("다음 프로젝트는 페이스북을 만들어요")

### 2.3. 혼자 일하기

- 모든 것을 도맡아 하려고 한다. 

- 혼자만 일하는 당신은 아마추어 (조별과제에서 얼마나 힘들었으면. :scream::scream:)

### 2.4. 나쁜 코드

- 나쁜 코드를 알면서도 짜는 순간이 온다. (자의, 타의)

- 이것을 기술 부채라고 생각을 하고 업무가 여유로울 때, 갚으면서 발전해나가자.

### 2.5. 본인의 실수를 인정하지 않음

- 누구든 실수할 수 있다.

- Git으로 다 볼 수 있어서 책임 회피 하기도 힘들다. 

### 2.6. 내가 배운 것을 공유하지 않기

- 나만 알아야지?

- 코드짜고 공유하는 것이 나를 스킬 업 시키는 과정이다.

- 처음이 힘들면, 기술 블로그를 활용하자.

### 2.7. 늦은 피드백

- 늦은 피드백은 결정사항의 지연, 일정 지연

- 결정할 수 있는건 최대한 빨리

### 2.8. 내 코드에 집착하기

- 나의 코드를 딴지? -> 나에게 딴지 아님.

- 더 나은 방법이 있으면 받아들이는게 좋다. (확실히 이렇게 얻은 지식은 까먹지 않는다.)



## 3. 테스트 및 유지보수

### 3.1. 통과할 정도의 테스트만 만들기

- 통과를 못할 테스트도 만들어야 한다.

- 이슈 트래킹도 필요하다. (어는 부분이 약한지 확인할 수 있다.)

### 3.2. 기능구현 이외의 사항을 무시

- 체크 리스트에 관리

- 기능 구현만 하면 성능과 보안 문제가 일어나기 쉽다



## 4. 결론

- 좋은 습관은 말 그대로 습관 가지고 있으면 상당히 편하다. 

- 습관을 가지기 위해서는 익히려고 하는 노력이 필요하다.

- 패시브 스킬을 잘 찍어보자. (:grinning::grinning:)