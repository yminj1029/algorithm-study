# 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원
# 손님에게 거슬러줘야할 돈이 N원, 거슬러 줘야할 동전의 최소의 개수??

money = int(input())

m1 = money//500
m2 = money % 500//100
m3 = money % 100//50
m4 = money % 50//10
print(m1+m2+m3+m4)

# book

n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]
for coin in coin_types:
    count += n//coin  # 해당 화폐로 거슬로 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)
