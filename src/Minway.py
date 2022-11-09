from Matrix import Matrix
from Point import Point
import numpy as np

class Minway(object):
  def __init__(self, matrix : Matrix):
    self.__matrix : Matrix = matrix
    self.__visited = []    
    for i in range(self.__matrix.get_range_i()):
      line = []
      for j in range(self.__matrix.get_range_j()):
        line.append(False)
      self.__visited.append(line)

  def movement(self, initial_position : Point, final_position : Point):
    actual_position : Point = initial_position
    # Mientras la posicion actual no sea la posicion final
    while (actual_position.get_position_x() != final_position.get_position_x()) and (actual_position.get_position_y() != final_position.get_position_y()):
      heuristic = 10000000000000000000000
      next_position : Point
      # En esta versión, solo se puede mover arriba, abajo, izquierda y derecha
      # Calculamos el valor de arriba
      if actual_position.get_position_y() + 1 < self.__matrix.get_range_j():
        if not(self.__visited[actual_position.get_position_x()][actual_position.get_position_y() + 1]):
          heuristic_up = self.__get_heuristic_manhattan(Point(actual_position.get_position_x(), actual_position.get_position_y() + 1), final_position)
          if heuristic_up < heuristic:
            heuristic = heuristic_up
            next_position = Point(actual_position.get_position_x(), actual_position.get_position_y() + 1)
      # Calculamos el valor de abajo
      if actual_position.get_position_y() - 1 >= 0:
        if not(self.__visited[actual_position.get_position_x()][actual_position.get_position_y() - 1]):
          heuristic_down = self.__get_heuristic_manhattan(Point(actual_position.get_position_x(), actual_position.get_position_y() - 1), final_position)
          if heuristic_down < heuristic:
            heuristic = heuristic_down
            next_position = Point(actual_position.get_position_x(), actual_position.get_position_y() - 1)
      # Calculamos el valor de la izquierda
      if actual_position.get_position_x() - 1 >= 0:
        if not(self.__visited[actual_position.get_position_x() - 1][actual_position.get_position_y()]):
          heuristic_left = self.__get_heuristic_manhattan(Point(actual_position.get_position_x() - 1, actual_position.get_position_y()), final_position)
          if heuristic_left < heuristic:
            heuristic = heuristic_left
            next_position = Point(actual_position.get_position_x() - 1, actual_position.get_position_y())
      # Calculamos el valor de la derecha
      if actual_position.get_position_x() + 1 < self.__matrix.get_range_i():
        if not(self.__visited[actual_position.get_position_x() + 1][actual_position.get_position_y()]):
          heuristic_right = self.__get_heuristic_manhattan(Point(actual_position.get_position_x() + 1, actual_position.get_position_y()), final_position)
          if heuristic_right < heuristic:
            heuristic = heuristic_right
            next_position = Point(actual_position.get_position_x() + 1, actual_position.get_position_y())
      self.__matrix.print_position(next_position.get_position_x(), next_position.get_position_y(), "orange")
      actual_position = next_position

  # Funcion que calcula la distancia de manhattan entre dos nodos
  def __get_heuristic_manhattan(self, position1 : Point, position2 : Point):
    return (abs(position1.get_position_x() - position2.get_position_x()) + abs(position1.get_position_y() - position2.get_position_y()))

  def __get_heuristic_euclidean(self, position1 : Point, position2 : Point):
    return (np.sqrt((position1.get_position_x() - position2.get_position_x())**2 + (position1.get_position_y() - position2.get_position_y())**2))