# This program is supposed to count the odd and even numbers
# **string = "this is a string"
integers = 53274527542
print(integers)


# print (f"{len(integers)}")
def count_odd_event():
    count_odd = 0
    count_even = 0
    count_digit = 0
    count_character = 0

    while True:
        Digits = input("Enter the Digits: ")
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

            if not digit.isdigit():
                count_character += 1
                # print (f"{digit} is not a digit")

            else:
                count_digit += 1
                # print (f"{digit} is a digit")

        print(f"Even :{count_even}")
        print(f"Odd :{count_odd}")

        continue_input = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_input != "yes":
            print("Exiting the program..........")
            break
        else:
            count_odd = 0
            count_even = 0
            continue

    return count_odd, count_even


print("Welcome to the Odd and Even number counter")
print("-------------------------------------------")

count_odd_event()
