from Matrix import Matrix

def main():
  weight = 500 # int(input("Enter the width of the matrix: "))
  height = 500 # int(input("Enter the height of the matrix: "))
  range_i = int(input("Enter the range of the matrix in the i axis: "))
  range_j = int(input("Enter the range of the matrix in the j axis: "))
  matrix = Matrix(weight, height, range_i, range_j)
  matrix.print()
  matrix.print_position(1,1, "red")
  for i in  range(1, range_i + 1):
    matrix.print_position(i, i, "orange")
    matrix.print_position(i, i + 1, "orange")
  matrix.print_position(1, 1, "red")
  matrix.print_position(range_i, range_j, "blue")
  matrix.execute()
if __name__ == "__main__":
  main()