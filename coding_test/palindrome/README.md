# 문제
* 문자열 `str` 과 정수 `n` 이 주어진다.
* 문자열 `str`의 어떤 문자를 `n`번 이하로 제거하였을 경우, 회문이 되는지 그 여부(`True`, `False`)를 출력하시오.
* 회문: 순서대로 읽어도 거꾸로 읽어도 똑같은 문장
  * $abba, tenet, kayak$ 
   
# 입출력 조건
* $1 \le\ $`str.length`$\ \le 1000$
* $0 \le\ $`n`$\ \le \ $`str.length`
* 입력 테스트케이스별 한 줄에 `str` 과 `n` 이 주어지며, 한 칸의 공백으로 구분한다.
* `str` 은 알파벳 소문자로 구성
* 출력은 `True`, `False` 2개 중 하나 문자열로 출력
   
## 입출력 예시 1
### 입력 예시
```
abcdeca 2
```
### 출력 예시
```
True
```
#### 예시 설명
* 'b', 'e' 2개 제거하면 'acdca' 회문


## 입출력 예시 2
### 입력 예시
```
abcdeca 5
```
### 출력 예시
```
True
```
#### 예시 설명
* 'b', 'e' 2개(5 이하) 제거하면 'acdca' 회문

## 입출력 예시 3
### 입력 예시
```
abcdeca 1
```
### 출력 예시
```
False
```
#### 예시 설명
* 'b', 'e'를 제거해야하나 1번 이하로 제거해도 회문을 완성할 수 없음.
