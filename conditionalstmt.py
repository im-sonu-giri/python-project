height=float(input("Enter a height of the person"))
cusomer_age =int(input("Enter a age"))
if(height<120):
    if(cusomer_age<18):
        print("eligible to ride")
    else:
        print("not eligible")
else:
    print("not eligible")
