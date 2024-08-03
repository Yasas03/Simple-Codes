n = int(input(f'Enter the number : '))
numbers = list(range(2,n+1))
m=2
while m*m <n: 
        if m in numbers:
            for num in numbers[:]:
                if num % m == 0 and num != m:
                    numbers.remove(num)
        m+=1
print(numbers)
