import tkinter as tk

# Create a window
window = tk.Tk()
window.title("Matrix")

v_width = 2560
v_height = 1080

# Create a canvas
canvas = tk.Canvas(window, width = v_width, height = v_height, bg="black")
canvas.pack()

range_i = 50
range_j = 50

valor_i = v_width / range_i
valor_j = v_height / range_j

# Print the matri(x - 1)
for i in range(range_i):
  for j in range(range_j):
    # Create rectangles
    canvas.create_rectangle(i * valor_i, j * valor_j, i * valor_i + valor_i, j * valor_j + valor_j, fill="white")

# Print a car in a position
def print_car(x, y, color):
  # Print the rectangle
  canvas.create_rectangle(x * valor_i, y * valor_j, x * valor_i + valor_i, y * valor_j + valor_j, fill=color)

print_car(10, 10, "red")

# Run the window's main loop
window.mainloop()