# Git - commit message convention

> 21.07.26. | SSAFY5_6반_7조

```git
git commit -m "커밋 제목
(한 줄 띄우고)
커밋 내용
(한 줄 띄우고)
커밋 꼬릿말
"
```

```
<type>(<scope>): [#]<subject>          -- 헤더
<BLANK LINE>
<body>                              -- 본문
<BLANK LINE>
<footer>                            -- 바닥글

===========================================
<type>

feat : 새로운 기능에 대한 커밋
fix : 버그 수정에 대한 커밋
build : 빌드 관련 파일 수정에 대한 커밋
chore : 그 외 자잘한 수정에 대한 커밋
ci : CI관련 설정 수정에 대한 커밋
docs : 문서 수정에 대한 커밋
style : 코드 스타일 혹은 포맷 등에 관한 커밋
refactor :  코드 리팩토링에 대한 커밋
test : 테스트 코드 수정에 대한 커밋

=============================================
<footer>

Fixes: 이슈 수정중 (아직 해결되지 않은 경우)
Resolves: 이슈를 해결했을 때 사용
Ref: 참고할 이슈가 있을 때 사용
Related to: 해당 커밋에 관련된 이슈번호 (아직 해결되지 않은 경우)

```

```git
// i.g.
git commit -m "[#S05P12A607-2] feat: 패킷 송신 이벤트에 관련된 로그 출력 기능 추가

커밋에 대한 자세한 설명을 써줍니다(What & Why)

Resolves: #123
Ref: #456
Related to: #48
"

```

