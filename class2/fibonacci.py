first = 0
second = 1

next = first + second

limit = int(input("Enter the limit: ")) 

print(first)
print(second)

while next <= limit:
    print(next)
    
    first = second
    second = next
    next = first + second
    
    