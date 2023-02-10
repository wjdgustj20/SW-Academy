# 문제
* 길이가 $N$인 수열 $A[1],\ A[2],\ \cdots ,\ A[N]$ 이 주어질 때, **수열의 $L$ 번째 원소부터 $R$ 번째 원소까지의 합**을 구해보자.
* 입력의 범위가 작기 때문에 누적 합 자료구조를 사용하지 않아도 해결할 수 있다.

# 입출력 조건
* 첫째 줄에 정수 $N(1\le N\le 100), M(1\le M\le 100)$ 이 주어진다.
* 둘째 줄에 정수 $A[1],\ A[2],\ \cdots ,\ A[N]\ (-100\le A[i]\le 100)$ 이 주어진다.
* 셋째 줄부터 $M$ 개의 줄에 $L,\ R\ (1\le L\le R\le N)$ 이 주어진다.
* $M$ 개의 줄에 수열의 $L$ 번째 원소부터 $R$ 번째 원소까지의 합을 출력한다.
## 입출력 예시
### 입력 예시
```
4 10
1 2 3 4
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4
```
### 출력 예시
```
1
3
6
10
2
5
9
3
7
4
```