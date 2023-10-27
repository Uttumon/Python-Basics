pi = 22/7                                    # Define the value of pi
def area_of_circle(radius):                  # Simple function to calculate the area of a circle
    return pi * (radius ** 2)
def area_of_circle_param(pi, radius):        # Parameterized function to calculate the area of a circle
    return pi * (radius ** 2)
def area_of_circle_return(radius):           # Function with return type to calculate the area of a circle
    area = pi * (radius ** 2)
    return area
def area_of_circle_param_return(pi, radius): # Parameterized function with return type to calculate the area of a circle
    area = pi * (radius ** 2)
    return area
radii = []
for i in range(10):                          # Get the radius of the 10 different circles from the user
    radius = float(input(f"Enter the radius of circle {i+1}: "))
    radii.append(radius)
for i, radius in enumerate(radii):           # Calculate the area of each circle using different functions
    area1 = area_of_circle(radius)
    area2 = area_of_circle_param(pi, radius)
    area3 = area_of_circle_return(radius)
    area4 = area_of_circle_param_return(pi, radius)
    print(f"Area of circle {i+1} using Simple Function: {area1:.2f}")
    print(f"Area of circle {i+1} using Parameterized Function: {area2:.2f}")
    print(f"Area of circle {i+1} using Return Type with Function: {area3:.2f}")
    print(f"Area of circle {i+1} using Return Type with Parameterized Function: {area4:.2f}")
