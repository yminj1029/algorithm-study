stack = []

# 삽입5->2->3->7->삭제=>삽입1->4->삭제

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)  # 최하단 원소부터 출력
print(stack[::-1])  # 최상단 원소부터 출력

#  파이썬에서 스택을 이용할 때는 별도의 라이브러리를 사용할 필요가 없다.
# 기본 리스트에서는 append()와 pop() 메서드를 이용하면 스택 자료 구조와 동일하게 동작한다.
# append()메서드는 리스트의 가장 뒤쪽에서 데이터를 삽입하고, pop()메서드는 리스트의 가장 뒤쪽에서 데이터를 꺼내기 때문이다.
