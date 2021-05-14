A, B, C= map(int, input().split())
print((A+B)%C, ((A%C) + (B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep="\n")

D = int(input())
E = int(input())

print(D*(E%10), D*(int(E%100/10)), D*(int(E/100)), D*E, sep="\n")
