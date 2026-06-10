for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

fruits = ["apple", "bannana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")


count = 9

while count > 10:
    print(f"Count is {count}")
    count = count + 1

print("Done!")


for i in range(10):
    if i == 9:
        break
print(i)

number = 7

number = int(input("Enter a number to see its times table: "))

print(f"\nTimes table for {number}:\n")

for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")


number = int(input("Enter a number to see its times table: "))

print(f"\nTimes table for {number}:\n")

for i in range(1, 13):
    print(f"{number} x {i} = {number * i}") 