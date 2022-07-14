import time
import math
from time import sleep
sleep(1)
print("Get ready . . . ")
print(" ")
sleep(2)
tic1 = time.perf_counter()
x = str(input("Type your script here: "))
tic2 = time.perf_counter()
y = len(x)
def time(tic1, tic2):
  return round(tic2 - tic1, 2)
def cps(y, tic1, tic2):
  return round(y / (tic2 - tic1), 2)
print("You typed " + str(y) + " characters in " + str(time(tic1, tic2)) + " seconds.") 
print(" ")
print("This translates to " + str(cps(len(x), tic1, tic2) * 12) + " words per minute.")
