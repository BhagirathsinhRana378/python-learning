# for number in range(3):
#     print("loop is running", number+1, (number+1)* '.' )
# # bit complex
# print("loop is finished")
# for number in range(1,5):
#     print("loop is running", number, (number)* '.' )
# # bit complex

# input("press enter to exit")
count = 0
for number in range(1,10):
    if number %2 ==0:
        count += 1
        print(number)
print(f"we have {count} even numbers ")