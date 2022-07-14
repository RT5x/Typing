import random
import time 
from time import sleep
def stringToList(data):
   return list(data)
data = "abcdefghijklmnopqrstuvwxyz1234567890;'[],./!@#$%^&*()_+'"    # characters you want to practice
lst = stringToList(data)

def rfunct():
  print(" ")
  z = random.choice(lst)
  print(z)
  tic1 = time.perf_counter()
  x = input("Type here: ")
  tic2 = time.perf_counter()
  def time1(tic1, tic2):
    return tic2 - tic1
  print("Time: " + str(round(time1(tic1, tic2), 2)) + " seconds.")
  if x == z:
    print("Nice")
  else:
    print("Nope")
  print(" ")

i = 0
while i <= 100:   # Number of times you want to practice
  rfunct()
  i += 1
