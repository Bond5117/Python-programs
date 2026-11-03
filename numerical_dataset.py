
num_list = []
total = 0
average = 0
largest = 0
smallest = 0
even = 0
odd = 0
length = int(input("Enter the length of your numerical dataset: "))

while length < 1:
    length = int(input("Enter the length of your numerical dataset (non-zero integer): "))

while len(num_list) != length:
    value = int(input("Enter a real number: "))
    num_list.append(value)

largest = num_list[0]
smallest = num_list[0]


for num in range(0, length):
    total += num_list[num]

    if num_list[num] > largest:
        largest = num_list[num]
    if num_list[num] < smallest:
        smallest = num_list[num]

    if num_list[num] % 2 == 0:
        even += 1
    else:
        odd += 1

average = total / length

print(f"Numerical dataset used: {num_list}")
print(f"Sum of all values: {total}")
print(f"Average of all values: {average}")
if length > 1:
    print(f"Largest value in dataset: {largest}")
    print(f"Smallest value in dataset: {smallest}")
print(f"Total number of even values in dataset: {even}")
print(f"Total number of odd values in dataset: {odd}")