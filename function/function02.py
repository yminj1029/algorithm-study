def d(n):
    su = n
    num = list(str(n))
    for i in num:
        su += int(i)
    return su

numlist = []
for number in range(1, 10001):
    su = d(number)
    numlist.append(su)
    if number in numlist:
        pass
    else:
        print(number)


#다른 사람 코드
def self_num(number):
    total = number
    while number != 0:
        total += number % 10
        number = int(number / 10)
    return total

a = list(range(1, 10000))

b = map(self_num, a)
final = set(a) - set(b)
real_final = list(final)
real_final.sort()
for i in real_final:
    print(i)