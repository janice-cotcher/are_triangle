# Example of using a function to calculate a formula
def area_tri(b, h):
    """Find the area, A, of a triangle for base, b, and height, h"""
    A = 0.5 * b * h
    # print out the value of the area
    print("The area of the triangle is " + str(A) + "cm^2")


area_tri(1, 2)
area_tri(3, 7)
area_tri(19, 23.0)
