import time
from time import sleep

for i in range(1, 30, 1):
  x = str(input("enter password here: "))
  if x == "password":
    print("correct")
    print(" ")
  else: 
    print("incorrect")
    print(" ")
