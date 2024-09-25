import math

def calculate_circle_area(radius):
    if radius < 0:
        return "Error: Radius must be a non-negative value."
    return math.pi * (radius ** 2)

def calculate_rectangle_perimeter(length, width):
    if length < 0 or width < 0:
        return "Error: Length and width must be non-negative values."
    return 2 * (length + width)
