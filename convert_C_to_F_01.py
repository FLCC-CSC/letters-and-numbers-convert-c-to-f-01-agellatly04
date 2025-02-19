# FILE NAME - convert_C_to_F_01.py
# DRG - Rerun for points 2025-02-18-2351
# NAME: Andrew Gellatly
# DATE: 2/18/2025
# BRIEF DESCRIPTION:  A program that converts from C to F in degrees.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience




    
# Don't forget to cast user input as a float!
    
########## ENTER YER CODE BELOW THIS LINE ##########

C = float(input('Enter a temperature in Celsius: '))
F = C * (9/5) + 32

print()
print(f'{C} degrees Celsius is {F} degrees Fahrenheit.')

########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a temperature in Celsius: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: 1

1 degrees Celsius is 33.8 degrees Fahrenheit.

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What does `float` mean?

It's equal to 'double' in Java and allows for numbers with decimals to be stored.



2. Why do you think it is important to use `float` as opposed to
   a different type of variable type?

I think it's important in this case because we're multiplying by a fraction of '9/5' so we might get a decimal in our answer.



'''
