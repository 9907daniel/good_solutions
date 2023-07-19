## 뉴스 클러스터링lv2 pg
https://school.programmers.co.kr/learn/courses/30/lessons/17677

### 소요시간 : 30분

### 알고리즘 사용 : 해쉬맵 + 문자열
- 생략

### 단계
- 해쉬맵을 통해 문자열을 2단위로 짜르고, alphabet이 아니면 제거, 대문자면 소문자로 변환
- 두 해쉬맵의 공통 개수를 min를 통해 구하고
- 두 해쉬맵의 총합을 max를 통해 구한다

### 복습
```py
a = "ThisisAlphabet"
b = "Thisis Alphabet"
c = "ThisisAlphabet33"

print(a.isalpha())
print(b.isalpha())
print(c.isalpha())

# True
# False
# False
```