n = int(input(f'Enter the number : '))
numbers = list(range(1,n+1))
m=2
while m*m <n: 
    if m in numbers:
        numbers = [num for num in numbers if num % m != 0 or num == m]
    m+=1
print(numbers)