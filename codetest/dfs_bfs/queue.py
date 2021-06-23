from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입 5->2->3->7->삭제->1->4->삭제
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)  # 면저 들어온 순서대로 출력
queue.reverse()  # 다음 출력을 위해 역순으로 바꾸기
print(queue)

# 파이썬으로 큐를 구현할 때는 collections 모듈에서 제공하는 deque자료구조를 활용하자.
# deque는 스택과 큐의 장점을 모두 채택한 것인데 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며 queue라이브러리를 이용하는 것보다 더 간단하다.
# 대부분의 코딩 테스트에서는 collections 모듈과 같은 기본 라이브러리 사용을 허용한다.
# deque 객체를 리스트 자료형으로 변경하고자한다면 list()메서드를 사용하면 된다. ex. list(queue)
