# Tuples are immutable array-like structures

point = (5, 2)

x = point[0]
y = point[1]


#using tuples to store orederd imuatable values
#and to return multiple values from a function.
def calculate_square_properties(side_length):
  area = side_length * side_length
  perimeter = 4 * side_length
  return (area, perimeter)

result = calculate_square_properties(5)
print("Area: ", result[0])
print("Perimeter ", result[1])