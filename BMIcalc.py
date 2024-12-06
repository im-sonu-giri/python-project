user_height = float(input("Enter your height"))
user_weight = float(input("Enter your weight"))
bmi_calculation = (user_weight/user_height*user_height)
if(bmi_calculation>18.5):
    print("you are Underweight")
elif(bmi_calculation>18.5 and bmi_calculation<25):
    print("you are normal weight")
elif(bmi_calculation>25 and  bmi_calculation<30):
    print(f"{bmi_calculation}you are overweight")
elif(bmi_calculation>30 and  bmi_calculation<35):
    print("you are obese")
elif(bmi_calculation>35):
    print("you are  clinically obese")
else:
    print("Input a right information")
