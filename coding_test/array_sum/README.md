# 문제
* 양의 정수가 담긴 배열이 주어진다.
* 더하기를 하는 규칙은 아래와 같다.
 1. 더하기는 오로지 2개만 가능하다.
 2. 더하기 결과는 별도의 리스트(target)에 저장하고 다시 배열에 추가한다.
 3. 배열의 길이가 1이 될 때까지 반복한다.
 4. 배열의 길이가 1이 되었을 때, 별도의 리스트(target)에 저장해두었던 정수값을 모두 더한 후 출력한다.
* 위와 같은 규칙으로 주어진 배열을 계산할 때, 최소값을 찾아 출력하시오.  
   
# 입출력 조건
* 입력은 1 이상 10,000 이하의 양의 정수들이 한 줄로 주어지며 그 길이는 1 이상 10,000 이하다.
* 양의 정수들은 공백으로 구분한다.
* 출력은 정수 1개로 한다.
* **본 문제는 힙 구조로 풀어야 통과하게끔 설계되었음. (시간복잡도 제한 : 정답 코드의 2배)**

## 입출력 예시 1
### 입력 예시
```
4 3 2
```
### 출력 예시
```
14
```
### 예시 설명
1. 2와 3을 더함   [4,3,2] --> [4,5], target : [5]
2. 4와 5를 더함   [4,5] --> [9], target : [5, 9]
3. 배열의 길이가 1이므로 target 의 합계 출력 : 14

## 입출력 예시 2
### 입력 예시
```
1 5 3 8
```
### 출력 예시
```
30
```
### 예시 설명
1. 1과 3을 더함   [1,5,3,8] --> [5,8,4], target : [4]
2. 4와 5를 더함   [5, 8, 4] --> [8, 9], target : [4, 9]
3. 9와 8을 더함   [8, 9] --> [17], target : [4, 9, 17]
4. 배열의 길이가 1이므로 target 의 합계 출력 : 30
