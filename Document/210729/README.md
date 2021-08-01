# 업무일지

### ✔ Summary

- [x] 10:30~11:50 프로토타입 회원가입/로그인
- [x] 13:20~14:10 Jeplin + Vuejs
- [x] 15:20~16:10 Jeplin + Vuejs
- [x] 16:20~17:00 prototype
- [x] 17:10~18:00 prototype
- [x] 20:30~00:00 prototype
- [x] 00:30~02:45 OOP



## ✨ 오늘 배운 내용

- [데이터 크롤링의 세계](./live/데이터크롤링.md)
- [객체지향 프로그래밍](./APS/객체지향.md)
- 제플린 + Vuejs



## 👀 수행한 업무 및 작성한 코드

- 추상 클래스
- 인스턴스 매서드, 스태틱 매서드
- 클래스 매서드

```python
class Figure:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calc_area(self):
        return self.width * self.height
	
    @staticmethod
    def is_square(rec_width, rec_height):
        if rec_width == rec_height:
            print(True)
        else:
            print(False)

figure = Figure(2, 3)
figure.is_square(2, 3)
Figure.is_square(5, 5)

# 정적 메서드에서 클래스 속성에 접근 가능
# 정적 메서드에서 인스턴스(객체) 속성에는 접근 불가능
```

```python
class Figure:
    count = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height
        Figure.count += 1
        
    def calc_area(self):
        return self.width * self.height
	
    @classmethod
    def print_count(cls):
        return cls.count

figure1 = Figure(2, 3)
figure2 = Figure(5, 5)
Figure.count
Figure.print_count()
figure1.print_count()
```



## 🐱‍💻 아쉬운 점 & 느낀 점

- 클래스로 코드를 짜는 연습을 해봐야겠습니다.
- OOP !

 

