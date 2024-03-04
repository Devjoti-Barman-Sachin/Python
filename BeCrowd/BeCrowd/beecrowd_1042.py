numbers = input().split()
numbers = [int(number) for number in numbers]
c = numbers.copy()
numbers.sort()
for prnt in range(0, len(numbers)):
    print(numbers[prnt])
print()
for prnt in range(0, len(numbers)):
    print(c[prnt])