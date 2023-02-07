# 문제
* 리포그램(lipogram)은 팬그램(pangram)과 반대되는 개념으로, 알파벳의 일부 글자를 사용하지 않고 만든 문장이다. 주어진 문자열이 리포그램인지 확인해보자.

# 입출력 조건
* 첫째 줄에 알파벳 소문자로 이루어진 문자열 $S\ (1\le |S|\le 100)$ 가 주어진다. $S$ 는 공백 또는 알파벳 대소문자로 이루어진 문자열이다.
* 주어진 문자열 $S$ 가 리포그램이라면 `YES`를 출력하고 두 번째 줄에 사용하지 않은 알파벳을 출력한다. 사용하지 않은 알파벳은 소문자로 출력하며, 알파벳 순서대로 출력한다. 리포그램이 아니라면 `NO`를 출력한다.

## 입출력 예시 1
### 입력 예시
```
The Quick Brown Fox Jumps Over The Lazy Dog
```
### 출력 예시
```
NO
```

## 입출력 예시 2
### 입력 예시
```
Bubble sort Quick sort Merge sort prefix sum Binary search Fibonacci Dijkstra
```
### 출력 예시
```
YES
vwz
```

## 입출력 예시 3
### 입력 예시
```
AbCdEfGhIjKlMnOpQrStUvWxYz
```
### 출력 예시
```
NO
```
