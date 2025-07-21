# Text Based Calculator Using Python
def get_number(number):
    while True:
        num =input(f"Enter NUmber {number}: ")
        try:
            return float(num)
        except:
            print(f"Enter the number ass*@")

while True:
    num1 = get_number(1)
    num2 =get_number(2)

    calc =input("Enter what to do? (+,-,*,/) : ")
    print(num1,calc,num2)
    if calc == '+':
        print(f'Addition of {num1} and {num2} is {num1+num2}')
    elif calc == '-':
        print(f'Subraction of {num1} and {num2} is {num1-num2}')
    elif calc == '*':
        print(f'Multiple of {num1} and {num2} is {num1*num2}')
    elif calc == '/':
        if num1 != 0:
            print(f'Division of {num1} and {num2} is {num1/num2}')
        else:
            print("Zero is not a valid divisor")
    else:
        print("Enter the valid Symbol !")
