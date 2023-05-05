# -*- coding: utf-8 -*-
"""
Created on Wed May  4 22:05:06 2022

@author: Gowtham S
"""

"""
1. Beginners I suggest u to download Anaconda
Look into a youtube video

2. Already have Any Code editor - use that

ANY ONE

No to ipynb files, download it As py

You can see the App assignments in your MyCaptain App

1. Do not call me sir
2. Do not be rude, be helpful
3. 10% of replies

Go thru ur mycaptain App 


Deadline - 6th of June 2022 12:30 AM
"""



x = 10
y = 20

name2 = 10

my_var = 10

x = 10

X = 10

"""
Same ??

Case Sensitivity

Comments
"""
# This is a single line comment

'''
Extra information
to other developers/humans
This will not run as a code
'''



# Etiquettes

myName = "Gowtham"  # Camel case
my_name = "Gowtham" # Snake case
MyName = "Gowtham" # Pascal Case






# Arithmetic Operators
# +, -, /, **, %, //, *

x = 4
y = 2

x + y

x/y

x%y # Remainder





x = 10

y = 2.5

myName = "Gowtham"

letter = 'G'

#x -> float??

# Type Casting

x_float = float(x)

1. Arithmetic operators
2. Float -> integer
3. String -> integer



1. Live sessions
2. Live sessions Assignments (Optional) given by me
3. App assignments (cm)

Deadline - 6th June 2022 - 12:30 AM

30 mins to 1 hr everyday

IMPORTANT
1. Learning to Code is it ok to use Google??

Yes you can use it - Googling as a skill in the resume

BUT

DO NOT COPY PASTE THE CODE
TYPE IT OUT - TO UNDERSTAND WHAT EACH LINE DOES
MAKE CHANGES IF NECESSARY





x = 10

x_float = float(x)

y = 20.5

y_int = int(y)

x = "2"

can you convert this to an integer??

1. Yes
2. No

x_int = int(x)




# Assignment Operator
=

x = 20

x += 1 # Short hand

x = x+1

BUT DO NOT USE THIS WHEN U CODE


# Comparison Operators
>, <, ==, >=, <=, !=

x = 11

y = 10

x==y # Boolean


x==y






Functions

float()

In-built Function - A particular task
print, input


print(x+y)

# 1
x = 10
y = 11

print("The value of x: ",x," and the value of y: ",y)

# 2
print("The value of x: {} and the value of y: {}".format(y, x))


# 3
print(f"The value of x: {x} and the value of y: {y}")


BUT


1. print("The value of x: ",x)

2. print("The value of x: "+str(x))

print("The value of x: "+repr(x))

wrong?? - 2

1 - right
Easy

Time and Space complexity




# Input function

x = input()

Default - string

x = int(input("Enter the value of x: "))

y = int(input("Enter the value of y: "))

print("Addition of x and y is: ", x+y)



Go thru the App - Study

Errors that people do,
1. Do not .py extension - not approved
2. str, repr - not approved
3. Your first assignment in the app has 2 questions

user input-> abc.py

extract -> py

print/op-> python

Try ur best

3 questions max






1. print("The value of x: ",x)

2. print("The value of x: "+str(x))

3. print("The value of x: "+repr(x))

Right??

Right - 1

Why?? - Simple
Time And Space complexity

Occams Razor


Alan Turing - Imitation Games - movie
Turing test - Captcha ?? - I am not a robot

Terminators - NOT

BOTS - crawler, scrapers


Turing complete programming language - modern, logic
If, Loops

If conditions

If it rains I will take an umbrella
Else I will study a book

rain = 0 # 1 or 0, true or false for example sake

if rain==1:
    print("ITU") # 2
else:
    print("ISB") # 1








If it rains I will take an umbrella - 1
Else 
If it snows I will take my boots - 2
Else
I will study a book - 3


conditions?? - 3

rain = 1
snow = 1

else + if = elif

if rain==1:
    print("IWTU") # 1
elif snow==1:
    print("IWTB") # 2
else:
    print("ISB") # 3




print("----- CALCI ------")

choice = int(input("1.Add\n2.Subtraction\nEnter: "))

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))


if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
else:
    print("Wrong Choice !!")



If it rains
And
snows
I will take Boots And Umbrella


rain = 1
snow = 0

if rain==1 and snow==1:
    print("IWBU")



Data Structures In Python

Lists, Dictionary, Tuples 


Lists
ordered - Indexed
Heterogenous

l1 = ["Seema", "Kushhagra", "DR"]

l1[1:4]

methods means functions used only For Data Structs

"Iram"

l1.append("Iram")

l1.append("GUDE")

l1.append("Gomes")

l1.pop()


l1 = ["G", "o", "w", "t", "h", "a", "m"]

s1 = "Gowtham"

l1[0]

s1[1]

String also behaves like DS in Python

s1 = "Go.tham"

s1.upper()

s1.lower()

s1.split('.')



Assignment 1 (optional)
Strongly suggest u to complete this

1. Try to create a calculator for atleast 3 operations
2. Complete all the methods of List in w3schools
3. Complete all the methods of Strings in w3schools
4. To start ur app assignments

First assignment in  ur app
has 2 questions

DO NOT SHARE THIS IN GROUP
TAKE A SCREENSHOT




l1 = [1, 2, 3, 4, 5]


l1[2]

1. O/p-?
2. Error
3. No output

s1 = "Mycaptain"

s1[5]

1. O/p-?
2. Error
3. No output


Turing complete programming languages
If And Loops

Loops
For And While


for i in range(0, 11):
    print(i)


i = 0
while i<10:
    print(i)
    i = i+1

1. 0 to 9
2. No output
3. Error


for index in range(0, len(5)):
    print(l1[index])


index = 1

l1[index]


index = 0
while index<len(5):
    index = index+1 # Error
    print(l1[index])

length of a List?? - len(l1)

for values in l1:
    print(values)



Functions

def addition(a, b):
    print(a+b)

addition(1, 2)

addition(44, 55)


def addition(a, b):
    return a+b

stored_var = addition(1, 2)



Dictionary

List - stored data inside a square brackets like a matrix

Apple

A
Ap
App
Appl
Apple

Apple -> A
Ball -> B




Dictionary
Key - Value pair

A:Apple

d1 = {"name":"Gowtham", "Mycaptain":"Python"}

d1["name"]

d1.popitem()

d1["Mycaptain"] = "Python"


Tuples

Immutable

t1 = (1, 2, 3, 4, 5)

l1 = [1, 2, 3, 4, 5]

tuples are faster than a List to display those items

Numpy





Assignments - optional

1. w3schools functions on Dictionary
2. Pattern using For or While loop
* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *
3. Find a year is Leap year Or Not

d1 = {"username":["gowtham", "drew", "seema"]}

try to append a name to the above List




import functions


functions.addition(1, 2)




1. Access the page - requests
2. Extract the title and price from the page - beautifulsoup


import requests

"requests" cannot be found - install

from bs4 import BeautifulSoup as bs

url = "https://www.newegg.com/global/in-en/samsung-galaxy-z-flip-3-5g-6-7-black/p/N82E16875168090?Item=N82E16875168090"

page = requests.get(url)

soup = bs(page.content, "html.parser")

title = soup.find_all('h1', attrs={"class":"product-title"})[0].get_text()

price = soup.find_all('div', attrs={"class":"price-current"})[0].get_text()


how to replace ₹ to space??
how to replace , to . ??


url = "https://www.amazon.in/United-Colors-Benetton-Sneakers-11-19P8SNEA3113I_902_40/dp/B07L57G7MV/ref=pd_d0_recs_v4_ac_w2_22/258-3905153-5220442?pd_rd_w=1uyYc&pf_rd_p=d07e23a0-088f-4edf-84b9-2836fb74cf31&pf_rd_r=4TKKTDR8TCG1WV73P70B&pd_rd_r=e725627d-a833-48c0-8d14-1869b648be09&pd_rd_wg=thhbR&pd_rd_i=B07LGJZ3YP&th=1&psc=1"


page = requests.get(url)

soup = bs(page.content, "html.parser")

pp = str(page.content)




car1 = "Lambo"

car1_wheels = 4

car1_seats = 2

car2 = "City"

car2_wheels = 4

car2_seats = 4





class Vehicle:
    def __init__(self, wheels, seats):
        self.wheels = wheels
        self.seats = seats


lambo = Vehicle(4, 2)


lambo.wheels


lambo.wheels = 4





import pytesseract


import cv2


import numpy as np



# reads an image and convert it to a matrix
image = cv2.imread("ce_sam_p_ed2.jpg")
# Filter
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(3,3),0)
blur1 = cv2.GaussianBlur(image,(3,3),0)
gray1 = cv2.cvtColor(blur1, cv2.COLOR_BGR2GRAY)
kernel = np.ones((3, 3), np.uint8)

img_erosion = cv2.erode(image, kernel, iterations=1) 
img_dilation = cv2.dilate(image, kernel, iterations=1) 
img_erdil = cv2.dilate(img_erosion, kernel, iterations=1)
erdil_blur = cv2.GaussianBlur(img_erdil,(3,3),0)

# EXTRACTION
text_image_sup = pytesseract.image_to_string(image)
text_blur_sup = pytesseract.image_to_string(blur)
text_gray_sup = pytesseract.image_to_string(gray)
text_blur1_sup = pytesseract.image_to_string(blur1)
text_gray1_sup = pytesseract.image_to_string(gray1)
text_erosion_sup = pytesseract.image_to_string(img_erosion)
text_erdil_sup = pytesseract.image_to_string(img_erdil)
text_erdil_blur_sup = pytesseract.image_to_string(erdil_blur)


#cv2.imshow("Image", image)
'''cv2.imshow("blur", blur)
cv2.imshow("Gray", gray)
cv2.imshow("Gray1", gray1)
cv2.imshow("Gray2", gray2)
cv2.imshow("Gray3", gray3)
cv2.imshow("Gray4", gray4)'''
cv2.imshow("blur", blur)
cv2.imshow("Gray", gray)
cv2.imshow("Erosion", img_erosion)
cv2.imshow("Dilation", img_dilation)
cv2.imshow("Er - Dil", img_erdil)
#cv2.imshow("Gray5", gray5)
#cv2.imshow("thresh", thresh)
#cv2.imshow("blur", blur)
#cv2.imshow("blur", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




































