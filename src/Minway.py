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

  def a_star(self, initial_position : Point, final_position : Point):
    actual_position : Point = initial_position
    while actual_position != final_position:
      heuristic = 10000000000000000
      
      self.__matrix.print_position(actual_position.get_position_x(), actual_position.get_position_y(), "orange")
    return 0

  def get_heuristic(self, actual_heuristic, point1 : Point, point2 : Point):
    if ((self.__get_heuristic_manhattan(point1, point2) < actual_heuristic) and (self.__visited[point1.get_position_x()][point1.get_position_y()])):
      return self.__get_heuristic_manhattan(point1, point2)
    return actual_heuristic 

  # Funcion que calcula la distancia de manhattan entre dos nodos
  def __get_heuristic_manhattan(self, position1 : Point, position2 : Point):
    return (abs(position1.get_position_x() - position2.get_position_x()) + abs(position1.get_position_y() - position2.get_position_y()))

  def __get_heuristic_euclidean(self, position1 : Point, position2 : Point):
    return (np.sqrt((position1.get_position_x() - position2.get_position_x())**2 + (position1.get_position_y() - position2.get_position_y())**2))