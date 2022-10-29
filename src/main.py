from Matrix import Matrix

def main():
  matrix = Matrix(2560, 1080, 50, 50)
  matrix.print()
  matrix.print_position(1, 1, "red")
  matrix.print_position(2, 1, "orange")
  matrix.print_position(3, 1, "blue")
  matrix.print_position(4, 1, "grey")
  matrix.execute()
  
if __name__ == "__main__":
  main()