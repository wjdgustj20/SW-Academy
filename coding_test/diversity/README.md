# 문제
* 대전시에는 일자로 흐르는 갑천을 따라 형성된 갑천생태공원이 있다. 생태공원은 강의 상류에서 하류방향으로 $N$ 개의 구역으로 나뉘어져 있고 $i$ 번째 구역의 $S[i]$ 라는 종 이름을 가진 물고기들이 서식하고 있다. 종의 이름은 편의 상 알파벳 소문자 하나이고, 이름이 같다면 두 종은 같은 종이다.
* 대전시는 환경 보호를 위해 생태공원을 두 구간으로 나누려고 한다. 그리고 나뉜 두 구간에 대해서 각각 **생태 점수**를 측정하려고 한다. 어떤 구간에 대한 생태 점수는 그 구간에 서식하는 서로 다른 물고기 종의 개수와 같다.
<img width="700" src="https://user-images.githubusercontent.com/90139789/218032076-3431a450-86ac-4e5d-a0e0-790cc921b97b.png">

* 예를 들어 위 그림은 $N = 7$ 이고 $S$ 는 `abcabcd` 인 생태공원의 예시이다. 만약 생태공원을 `abc`와 `abcd`로 나눈다면 각각의 생태 점수는 3+4 로 총 7점으로 최대가 된다.
* 알파벳 빈도에서 했던 것처럼 모든 알파벳별 등장 빈도를 저장하면 임의의 구간의 서로 다른 알파벳의 개수를 빠르게 구할 수 있다.

# 입출력 조건
* 첫째 줄에 정수 $N\ (2\le N\le 100,000)$ 이 주어진다.
* 둘째 줄에 알파벳 소문자로 이루어진 문자열 $S$ 가 주어진다.
* 주어진 생태 공원을 두 구간으로 나눴을 때 얻을 수 있는 최대 생태 점수를 출력한다.
   
## 입출력 예시 1
### 입력 예시
```
7
abcabcd
```
### 출력 예시
```
7
```

## 입출력 예시 2
### 입력 예시
```
4
aazz
```
### 출력 예시
```
3
```

## 입출력 예시 3
### 입력 예시
```
9
swacademy
```
### 출력 예시
```
9
```