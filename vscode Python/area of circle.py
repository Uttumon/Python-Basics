pi=22/7
def area_of_circle(radius):
    return pi*(radius**2)
radii=[]
for i in range(2):
    radius=float(input(f"Enter the radius of the circle{i+1}: "))
    radii.append(radius)
for i, radius in enumerate(radii):
    area=area_of_circle(radius)
    print(f"Area of the circle {i+1} using simple function: {area: .2f}")