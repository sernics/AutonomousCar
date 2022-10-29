from Matrix import Matrix

def main():
  matrix = Matrix(1920, 1080, 100, 100)
  matrix.print()
  for i in range(1, 100 + 1):
    matrix.print_position(i - 1, 1, "orange")
    matrix.print_position(i, 1, "red")
  matrix.execute()
  
if __name__ == "__main__":
  main()