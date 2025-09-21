## input() vs. sys.stdin.readline()
- `input()`과 `sys.stdin.readline()`은 **동일하게 표준 입력에서 문자열을 읽어오는 함수**지만, 내부 동작과 속도에 차이가 있음 

### `input()`
- 파이썬 내장 함수
- 동작 과정
    1. 내부적으로 `sys.stdin.readline()` 호출
    2. 맨 뒤의 개행 문자(`\n`) 제거
    3. 예외 처리나 기타 편의 기능을 거쳐 문자열 반환 
- 장점 : 코드가 간단하고, 자동으로 개행 제거됨
- 단점 : 여러 처리 단계를 거쳐서 상대적으로 느림

### `sys.stdin.readline()`
- `sys.stdin`(표준 입력 스트림)에서 직접 한 줄을 읽는 함수
- 개행 문자(`\n`)를 그대로 포함한 문자열 반환
- 장점 : 중간 처리 과정이 없어서 빠름 (특히 입력이 많을 때 큰 차이)
- 단점 : `rstrip()`으로 개행 문자 제거를 직접 해줘야 함

### 속도 차이
- `input()`은 매번 호출할 때 내부적으로 여러 처리를 하기 때문에 느림
- `sys.stdin.readline()`은 단순히 한 줄을 읽어서 빠름
- 입력 크기가 작을 때는 차이가 거의 없지만
- N이 100,000 이상 되는 대규모 입력에서는 차이가 큼
    -> 시간 초과 방지를 위해 `sys.stdin.readline` 권장

### 문제 적용
- 오늘 문제에서 다음과 같이 input을 읽음
```
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
for _ in range(M):
    n1, n2, w = map(int, input().split())
    edges.append((n1, n2, w))
```

- `str.split()`은 기본적으로 **공백 문자(스페이스, 탭, 개행 등)**을 기준으로 나눔
    - `"10 20\n".split()` → `["10", "20"]`
- 따라서 `split()`으로 인해 개행문자가 자동으로 잘라지고 무시됨 

#### 문자열을 그대로 input으로 사용할 때는 `rstrip()` 사용
- 예시
```
s = sys.stdin.readline()
print(s)      # "hello\n"
print(s == "hello")  # False
print(s.rstrip() == "hello")  # True
```