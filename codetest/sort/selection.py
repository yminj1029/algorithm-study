# selection sort

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  # 가장 적은 원소의 인덱스 #0
    for j in range(i+1, len(array)):  # 1~10
        if array[min_index] > array[j]:  # array[0]>array[1]....
            min_index = j  # min_index== 4
    array[i], array[min_index] = array[min_index], array[i]  # 스와프

print(array)

# 가장 작은 데이터를 앞으로 보내는 과정을 N-1번 반복한다.
# 선택 정렬을 이용하는 경우 데이터의 개수가 10000개 이상이면 정렬 속도가 급격히 느려진다.
# 다른 알고리즘과 비교했을 때 매우 비효율적이다.
# 특정한 리스트에서 가장 작은 데이터를 찾는 일이 코딩테스트에 잦으므로 익숙해질 필요가 있다.
