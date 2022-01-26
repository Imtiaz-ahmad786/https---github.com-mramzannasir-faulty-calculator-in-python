#this is exercise 2 and in this we make a fualty calculater this calculater nake some value wrong like if user want to calculate 15 * 10 then show 400, 865 / 5 then show 768 and 1000 - 888 then show 1222


a = int(input("Enter your 1st value: "))
c = input("Enter your oprater: ")
b = int(input("Enter your 2nd value: "))


if a == 15 and b == 10 and c == "+":
    print("Your Ans is 400")
elif a == 865 and b == 5 and c == "/":
    print("Your Ans is 768")
elif a == 1000 and b == 888 and c =="-":   
     print("your ans is 1222") 
elif c == '+':
    print("Your Sum is: ", a + b)
elif c == '-':
    print("Your sub is: ", a - b)
elif c == '/':
    print("Your divid is: ", a / b)
else:
    print("Uneccepted Error Please check your Input")