print("Please enter the string")
my_input1 = list(input())
print("Please enter another to compare")
my_input2 = list(input())

var = 0
count1 = 0
count2 = 0

for i in my_input1:
    count1 = count1 + 1
for i in my_input2:
    count2 = count2 + 1

#if sorted(my_input1) == sorted(my_input2):
#    print(f"Given strings {str(my_input1)} and {str(my_input2)} are Anagrams")
#else:
#    print(f"Given strings {str(my_input1)} and {str(my_input2)} are not Anagrams")

for x in range(0, count1 - 1):
    for y in range(0, len(my_input1) - 1 - x):
        if my_input1[y] > my_input1[y + 1]:
            var = my_input1[y]
            my_input1[y] = my_input1[y + 1]
            my_input1[y + 1] = var

for x in range(0, count2 - 1):
    for y in range(0, len(my_input2) - 1 - x):
        if my_input2[y] > my_input2[y + 1]:
            var = my_input2[y]
            my_input2[y] = my_input2[y + 1]
            my_input2[y + 1] = var


if ''.join(my_input1) == ''.join(my_input2):
    print(f"Given strings {''.join(my_input1)} and {''.join(my_input2)} are Anagrams")
else:
    print(f"Given strings {''.join(my_input1)} and {''.join(my_input2)} are not Anagrams")
