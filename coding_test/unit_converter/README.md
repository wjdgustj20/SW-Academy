# 문제
* kilometer 와 mile 을 서로 변환할 수 있는 코드를 작성하세요.
* `K` 가 주어졌을 때는 mile 로 변환된 숫자를 출력
* `M` 이 주어졌을 때는 kilometer 로 변환된 숫자를 출력
  ### 변환 공식
  * 1 mile = 1.6 km
   
# 입출력 조건
* 첫째 줄에 테스트 케이스의 개수 $T$ 가 주어진다.
* 각 테스트 케이스의 첫째 줄에 입력값 $N$ 과 입력값의 단위가 주어진다.
* 주어지는 입력값은 1 ~ 2,147,483,647 사이의 값
* 답은 소수점 두번째 자리까지 표기(double)
* **두 번째 자리가 0일 경우 소수점 첫 번째 자리까지만 표기**
  * ex.  1.00 (X),  1.0 (O)
   
## 입출력 예시
### 입력 예시
```
3
1 K
2 M
10 M
```
### 출력 예시
```
0.63
3.2
16.0
```
