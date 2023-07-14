# Write your solution here
def create_tuple(x: int, y: int, z: int):
    a = min(x,y,z)
    b = max(x,y,z)
    c = x+y+z
    tple = (a, b, c)
    return tple