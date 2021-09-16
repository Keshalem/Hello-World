#Enter your Weight (in Kg)
Weight = int(input('Enter your weight : ')) 

#Enter your Height (in m)
Height = float(input('Enter your height : ')) #In Meter

#Calculate BMI
BMI = (Weight/pow(Height,2))

#print('Your BMI is:', round(BMI , 1))
print('Your BMI is: {}'.format(round(BMI , 1)))

if BMI < 18.5 :
    print("Oops! You are Underweight.")
elif BMI >= 18.5 and BMI < 24.9 :
    print("Wow! You are fit.")
else :
    print("Sorry! You are Overweight.")