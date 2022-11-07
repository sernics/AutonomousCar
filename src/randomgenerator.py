from random import *

def randomgenerator(filename, size):
  for i in range(size):
    filename.write(str(randint(0, 100)))
    filename.write("\n")

filename = open("/home/seguisergio/dev/IA-2022/p02-IA/data/inputFile.csv", "r")

# randomgenerator(filename, 1000000)