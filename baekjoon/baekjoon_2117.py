# 원형 댄스
"""
N(1 ≤ n ≤ 32767)명의 사람들이 잔치에서 춤을 추게 되었다.
처음에는 1번부터 N번까지의 사람들이 차례대로, 둥글게 손을 잡고 서 있다.
그리고 춤이 끝날 때에는 이 순서가 반대(거꾸로, 뒤집힌)가 되어야 한다. 물론 사람들이 모두 손을 놓고 다시 자리를 잡으면 되겠지만,
그렇게 하면 둥그런 모양이 깨지게 된다. 따라서 자리를 바꿀 때에는, 서로 손을 잡고 있는 두 명의 사람만 자리를 바꿀 수 있다.

예를 들어 n=6인 경우를 보자. 맨 처음의 순서는 (1, 2, 3, 4, 5, 6)이 된다. 둥글게 서 있기 때문에 1번과 6번도 손을 잡고 있다.
이제 (1, 2, 3, 4, 5, 6) → (6, 2, 3, 4, 5, 1) → (2, 6, 3, 4, 5, 1) → (1, 6, 3, 4, 5, 2) → (1, 6, 3, 5, 4, 2) →
(1, 6, 5, 3, 4, 2) → (1, 6, 5, 4, 3, 2)의 순서대로 바꾸면 자리가 반대가 된다.
(6, 5, 4, 3, 2, 1)이 되는 게 맞겠지만, 어차피 둥글게 서 있기 때문에 (1, 6, 5, 4, 3, 2)와 같은 경우도 순서는 반대가 되는 게 맞다.

가급적이면 자리를 최소로 바꾸려고 한다. 최소로 자리를 바꾸려면 어떻게 해야 할까?
"""
"""
1234 이라는 순서가 있다고 하자, 순서를 거꾸로 하려면 4321이 되는 것을 일반적으로 생각할 수 있다.
그런데 문제를 읽어보면 굳이 4321이 아니라 1432 또한 순서를 거꾸로 한 것과 동일하다고 한다.
1234 뿐 아니라 12345, 123456 등을 시뮬레이션 해보면 알 수 있 지만, 가장 최적의 방법은 순서를 절반으로 나눠서 처리하는 것이다.
마치 DP처럼 생겨서 DP로 볼 수 있지 않을까 고민해봤지만
123456에서 123의 순서를 거꾸로하는 것과 123에서 123의 순서를 거꾸로하는 데에는 횟수의 차이가 있으므로, DP라고 볼 수는 없다.
문제의 요점은 결국 1234의 순서를 거꾸로 하는 최적의 방법은 2143으로 만드는 것이라는 것이다.
12345라면 21543 혹은 32154가 최적의 해가 된다.
이렇게 하려면 12345를 반으로 나눠서 123/45 혹은 12/345로 나눈 다음(여기선 123/45로 나눴다고 가정) 왼쪽인 123을 거꾸로 만들고, 오른쪽 45도 거꾸로 만들면 된다.
123을 거꾸로 만들려면 123 -> 132 -> 312 -> 321로 결국 2+1 횟수가 걸리며, 즉 (n-1 + n-2 + n-3 ... 1)이라는 점화식을 세울 수 있다.
유명한 공식인 가우스 공식 (n+1)*n/2을 활용하면 왼쪽, 오른쪽을 거꾸로 할 때 각각 (n**2-n)/2 회 rotate 해야 한다.
밑에선 그냥 (n**2-n)/2가 아닌 (n+1)*n/2를 사용했다. 어차피 변수를 쓸 것이며, 변수로 설정해줘야 코드가 말끔해지고 코드 길이도 줄기 때문이다.
"""
import math
import sys

N = int(sys.stdin.readline().rstrip())
left = math.ceil(N / 2) - 1
right = N // 2 - 1
print(round(((left + 1) * left) / 2 + ((right + 1) * right) / 2))
