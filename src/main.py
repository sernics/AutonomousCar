from Point import Point
from Matrix import Matrix
from Minway import Minway

def main():
  weight = 500 # int(input("Enter the width of the matrix: "))
  height = 500 # int(input("Enter the height of the matrix: "))
  range_i = int(input("Enter the range of the matrix in the i axis: "))
  range_j = int(input("Enter the range of the matrix in the j axis: "))
  matrix = Matrix(weight, height, range_i, range_j)
  minway = Minway(matrix)
  matrix.print()
  initial_position = Point(0, 0)
  final_position = Point(10, 10)
  minway.a_star(initial_position, final_position)
  matrix.execute()
if __name__ == "__main__":
  main()