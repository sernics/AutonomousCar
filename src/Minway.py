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

  def first_better(self, initial_position : Point, final_position : Point):
    found = False
    actual_position = initial_position
    self.__visited[actual_position.get_position_x()][actual_position.get_position_y()] = True
    while not found:
      if (actual_position.get_position_x() == final_position.get_position_x()) and (actual_position.get_position_y() == final_position.get_position_y()):
        found = True
      neighbors = self.neighbors(actual_position)
      heuristic = 10000000000
      for neighbor in neighbors:
        # if not self.__visited[neighbor.get_position_x()][neighbor.get_position_y()]:
        if self.__get_heuristic_manhattan(neighbor, final_position) < heuristic:
            heuristic = self.__get_heuristic_manhattan(neighbor, final_position)
            actual_position = neighbor
      self.__matrix.print_position(neighbor.get_position_x(), neighbor.get_position_y() + 1, "orange")      

  def neighbors(self, position : Point):
    neighbors = []
    if position.get_position_x() + 1 < self.__matrix.get_range_i() + 1:
      neighbors.append(Point(position.get_position_x() + 1, position.get_position_y()))
    if position.get_position_x() - 1 >= 0:
      neighbors.append(Point(position.get_position_x() - 1, position.get_position_y()))
    if position.get_position_y() + 1 < self.__matrix.get_range_j() + 1:
      neighbors.append(Point(position.get_position_x(), position.get_position_y() + 1))
    if position.get_position_y() - 1 >= 0:
      neighbors.append(Point(position.get_position_x(), position.get_position_y() - 1))
    return neighbors

  # Funcion que calcula la distancia de manhattan entre dos puntos
  def __get_heuristic_manhattan(self, position1 : Point, position2 : Point):
    return (abs(position1.get_position_x() - position2.get_position_x()) + abs(position1.get_position_y() - position2.get_position_y()))

  # Función que calcula la distancia euclidea entre dos puntos
  def __get_heuristic_euclidean(self, position1 : Point, position2 : Point):
    return (np.sqrt((position1.get_position_x() - position2.get_position_x())**2 + (position1.get_position_y() - position2.get_position_y())**2))