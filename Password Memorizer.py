import time
from time import sleep

n = 40   # Set number of repetitions you want to practice
for i in range(0, n, 1):
  x = str(input("enter password here: "))
  if x == "password":     # Set password
    print("correct")
    print(" ")
  else: 
    print("incorrect")
    print(" ")
