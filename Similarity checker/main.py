# Similarity checker
with open('sampletext1.txt','r') as file:
    stxt1 = file.read()
x = list(stxt1)
print("Sample text 1: " + stxt1)
with open('sampletext2.txt','r') as file:
   stxt2 = file.read()
print("Sample text 2: " + stxt2)
y = list(stxt2)
r = len(y)

def loop():
  sum = 0
  j = 0
  for j in range(len(y)):
    if y[j] == x[j]:
      sum += 1
    else:
      sum += 0
  print("Similarity: " + str(round(sum / len(y)*100, 2)) +"%.")
loop()

