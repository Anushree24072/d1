Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 1st input: enter height in meters e.g: 1.65
... height = input()
... # 2nd input: enter weight in kilograms e.g: 72
... weight = input()
... # 🚨 Don't change the code above 👆
... 
... # Write your code below this line 👇
... weight_as_int = int(weight)
... height_as_float = float(height)
... BMI = weight_as_int / height_as_float ** 2
... BMI_as_int = int(BMI)
