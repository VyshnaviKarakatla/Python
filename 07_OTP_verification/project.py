#OTP Verification
import random
otp=random.randint(1000,9999)
print(otp)
attempts=3
while attempts:
    user_input=(int(input("Enter OTP:")))
    if len(str(user_input))!=4:
        print("OTP Must be 4 digit number only")
    if otp==user_input:
        print("Correct OTP - Success")
        break
    attempts-=1
else:
    print("Maximum attempts done, try after 24 Hours")