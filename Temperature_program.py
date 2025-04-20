
# This program converts temperatures to either celicius or fahrenheit

def celsius():
    Cel = float(input("Enter the Celsius value: "))
    temp_Fah = (Cel * 1.8) + 32
    return temp_Fah

def fahrenheit():
    Fah = float(input("Enter the Fahrenheit value: "))
    cel_temp = (Fah - 32)/1.8
    return cel_temp

def main():
    print ("Welcome to The best Temperature converting program ")
    print ("---------------The temperature in balls------------")

    
    while True:
        print ("1. Fahrenheit")
        print ("2. Celsius")
        print ("3. Exit")
        option = int (input("What do you want to convert:"))

        
        if option == 1:
            while True:
                print ("You are converting from Celsius to Fahrenheit:")
                Ans = celsius()
                if Ans > 90:
                    print (f"The temperature in Fahrenheit is {Ans:.3f}F")
                    print ("--------Its so hot ----------")

                elif Ans <50:
                    print (f"The temperature in Fahrenheit is {Ans:.3f}F")
                    print ("----Its so Cold ----my balls are freezing------") 

                else :
                    print (f"The temperature in Fahrenheit is {Ans:.3f}F")
                    print ("--------This temperature is moderate ----------")

                Continue = input ("Do you want to continue (y/n):")
                if Continue == "y":
                    print ("Welcome again----")

                elif Continue == "n":
                    print ("Am so glad i served you Hope to see you back bye !!------")
                    break

                else :
                    print ("invalid input !!!!!!!!! you MotherFucker!!!!!!!")

        elif option == 2:
            while True:
                print ("You are converting from Fahrenheit to Celcius:")
                Ans = fahrenheit()
    
                if Ans > 40:
                        print (f"The temperature in Fahrenheit is {Ans:.3f}C")
                        print ("--------Its so hot ----------")
    
                elif Ans <20:
                    print (f"The temperature in Fahrenheit is {Ans:.3f}C")
                    print ("----Its so Cold ----my balls are freezing------") 
    
                else :
                    print (f"The temperature in Fahrenheit is {Ans:.3f}C")
                    print ("--------This temperature is moderate ----------")
    
                Continue = input ("Do you want to continue (y/n):")
                if Continue == "y":
                    print ("Welcome again----")
    
                elif Continue == "n":
                    print ("Am so glad i served you Hope to see you back bye !!------")
                    break
                
                else :
                    print ("invalid input !!!!!!!!! you MotherFucker!!!!!!!")

        elif option == 3:
            print ("Thank you for passing by see you soon bye ==========!!!!!!")
            break

        else :
            print (" !!!! Invalid choice !!!!! What is wrong with you motherFucker")

main()















                
