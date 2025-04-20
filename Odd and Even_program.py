
#This program is supposed to count the odd and even numbers
# **string = "this is a string"
integers = 53274527542
print (integers)
# print (f"{len(integers)}")
def count_odd_event():
    count_odd = 0
    count_even = 0

    Digits = input("Enter the digits separated by space: ")
    # Digits = [int(digit) for digit in Digits.split()]
    # for digit in Digits:
    #     if digit%2 == 0:
    #         count_even = count_even+1
    #         print (count_even)

    #     else:
    #         count_odd = count_odd + 1
    #         print(count_odd)

    for digit in Digits:
        if digit.isdigit():
            if int(digit) % 2 == 0:
                count_even += 1

            else:
                count_odd += 1

    print (f"Even :{count_even}")
    print (f"Odd :{count_odd}")

    return count_odd,count_even

    # print ("Enter the digits separated by space")


count_odd_event()

