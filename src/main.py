from Point import Point
from Matrix import Matrix
from Minway import Minway

def main():
  weight = 500 # int(input("Enter the width of the matrix: "))
  height = 500 # int(input("Enter the height of the matrix: "))
  range_i = int(input("Enter the range of the matrix in the i axis: "))
  range_j = int(input("Enter the range of the matrix in the j axis: "))
  matrix = Matrix(weight, height, range_i, range_j)
  matrix.print()
  minway = Minway(matrix)
  point1 : Point = Point(8, 14)
  point2 : Point = Point(4, 7)
  minway.first_better(point1, point2)
  matrix.print_position(point1.get_position_x(), point1.get_position_y(), "red")
  matrix.print_position(point2.get_position_x(), point2.get_position_y(), "blue")
  matrix.execute()

if __name__ == "__main__":
  main()