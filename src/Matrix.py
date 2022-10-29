import tkinter as tk

class Matrix(object):
  def __init__(self, width, height, range_i, range_j):
    self.__v_width = width
    self.__v_height = height
    self.__range_i = range_i
    self.__range_j = range_j
    self.__valor_i = self.__v_width / self.__range_i
    self.__valor_j = self.__v_height / self.__range_j
    self.__window = tk.Tk()
    self.__window.title("Matrix")
    self.__canvas = tk.Canvas(self.__window, width=self.__v_width,
                              height=self.__v_height, bg="black")
    self.__canvas.pack()

  def print(self):
    for i in range(self.__range_i):
      for j in range(self.__range_j):
        # Create rectangles
        self.__canvas.create_rectangle(i * self.__valor_i, j * self.__valor_j, i * self.__valor_i +
                                       self.__valor_i, j * self.__valor_j + self.__valor_j, fill="white")

    self.__window.mainloop()

  # def print_position(self, x, y, color):
  #   self.__canvas.create_rectangle(x * self.__valor_i, y * self.__valor_j, x *
  #                                  self.__valor_i + self.__valor_i, y * self.__valor_j + self.__valor_j, fill=color)
