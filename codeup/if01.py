a, b, c = map(int, input().split())

if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)

if a % 2 == 0:
    print("even")
else:
    print("odd")
if b % 2 == 0:
    print("even")
else:
    print("odd")
if c % 2 == 0:
    print("even")
else:
    print("odd")


num = int(input())
if num < 0 and num % 2 == 0:
    print("A")
elif num < 0 and num % 2 != 0:
    print("B")
elif num >= 0 and num % 2 == 0:
    print("C")
else:
    print("D")

score = int(input())
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
elif score >= 40:
    print("C")
else:
    print("D")

grade = input()
if grade == "A":
    print("best!!!")
elif grade == "B":
    print("good!!")
elif grade == "C":
    print("run!")
elif grade == "D":
    print("slowly~")
else:
    print("what?")

month = int(input())
if month // 3 == 1:
    print("spring")
elif month//3 == 2:
    print("summer")
elif month//3 == 3:
    print("fall")
else:
    print("winter")
