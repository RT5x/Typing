import time
import math
from time import sleep

def function():
  sleep(1)
  print("Get ready . . . ")
  print(" ")
  sleep(2)
  tic1 = time.perf_counter()
  x = str(input("Type your script here: "))
  tic2 = time.perf_counter()
  y = len(x)
  def time1(tic1, tic2):
    return round(tic2 - tic1, 2)
  def cps(y, tic1, tic2):
    return round(y / (tic2 - tic1), 2)
  print("You typed " + str(y) + " characters in " + str(time1(tic1, tic2)) + " seconds.") 
  print(" ")
  print("This translates to " + str(round(cps(len(x), tic1, tic2) * 12, 2)) + " words per minute.")

i = 1
while i <= 100:  # Number of times you want to try speedtest
  function()
  i += 1
