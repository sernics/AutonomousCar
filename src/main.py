import tkinter as tk

# Create a window
window = tk.Tk()
window.title("Matrix")

# Create a canvas
canvas = tk.Canvas(window, width=500, height=500, bg="black")
canvas.pack()

# Print the matri(x - 1)
for i in range(50):
  for j in range(50):
    # Create rectangles
    canvas.create_rectangle(i*10, j*10, i*10+10, j*10+10, fill="white")

# Print a car in a position
def print_car(x, y, color):
  # Create a rectangle
  canvas.create_rectangle(x*10, y*10, x*10+10, y*10+10, fill=color)

print_car(10, 10, "red")

# Run the window's main loop
window.mainloop()