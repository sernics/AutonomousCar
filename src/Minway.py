from Matrix import Matrix

class Minway(object):
  def __init__(self, matrix, heuristic_file):
    self.__matrix : Matrix = matrix    

  def a_star(self, initial_position, final_position):
    position = initial_position
    if position == final_position:
      return
    else:
      # Buscar a traves del algoritmo de a_estrella el siguiente nodo a visitar
      # f(n) = g(n) + h(n)
      # Asumiendo que g(n) vale 1 ya que en la tabla solo nos movemos una unidad
      print("Hola mundo")
      
