from Point import Point
from Matrix import Matrix
from Minway import Minway
import time

def main():
  weight = int(input("Enter the width of the matrix: "))
  height = int(input("Enter the height of the matrix: "))
  range_i = int(input("Enter the range of the matrix in the i axis: "))
  range_j = int(input("Enter the range of the matrix in the j axis: "))
  matrix = Matrix(weight, height, range_i, range_j)
  matrix.print()
  minway = Minway(matrix)
  initial_x = int(input("Enter de x position of the initial point: "))
  initial_y = int(input("Enter de y position of the initial point: "))
  final_x = int(input("Enter de x position of the final point: "))
  final_y = int(input("Enter de y position of the final point: "))
  point1 : Point = Point(initial_x, initial_y)
  point2 : Point = Point(final_x, final_y)
  inicio = time.time()
  print("El número de pasos de la funcion heurística euclídea es de: ",minway.first_better_with_euclidean(point1, point2))
  # print("El número de pasos de la funcion heurística de Manhattan es de: ",minway.first_better_with_manhattan(point1, point2))
  final = time.time()
  print("El tiempo de ejecución ha sido de: ", (final - inicio))
  matrix.print_position(point1.get_position_x(), point1.get_position_y(), "red")
  matrix.print_position(point2.get_position_x(), point2.get_position_y(), "blue")
  matrix.execute()

if __name__ == "__main__":
  main()