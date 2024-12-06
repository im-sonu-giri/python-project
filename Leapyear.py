input_year = int(input("Enter a year you want to check leap year"))
if(input_year%4 == 0):
    if(input_year%400==0 or input_year%100!=0):
        print("Input year is leap year")
    else:
        print(f"Input year{input_year} is not a leap year")
else:
    print(f"Input year{input_year} is not a leap year")