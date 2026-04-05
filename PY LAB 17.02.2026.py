def f_r(n):
    if n<=1:
        return n
    else:
        return f_r(n-1) + f_r(n-2)
#terms=10
#print(f"Fibonacci series up to {terms} terms:")

num=int(input("Enter a Positive Number:"))
print("Fibonacci Series:")


#for i in range(terms):
for i in range(num):
    print(f_r(i), end=" ")
