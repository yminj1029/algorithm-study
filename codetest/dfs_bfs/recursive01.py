# 재귀함수 예제

def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()


recursive_function()


# RecursionError: maximum recursion depth exceeded while calling a Python object
# 재귀의 최대 깊이를 초과함. 파이썬 인터프리터는 호출 횟수 제한이 있는데 이 한계를 벗어나서 생긴다.
