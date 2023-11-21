
def calculate_volume_of_cube(side_len):
    return side_len * side_len * side_len

print(calculate_volume_of_cube(4))  # should print 64

def calculate_volume_of_cylinder(radius, height):
    # defining an inner function - not accessible from anywhere outside of this function
    def calculate_base_area(r):
        return 3.14 * r * r
    return height * calculate_base_area(radius)

print(calculate_volume_of_cylinder(2, 5))
# print(calculate_base_area(1))  # throws error
