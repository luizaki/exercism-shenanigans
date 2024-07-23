def triangle(sides):
    sides = sorted(sides)

    for s in sides:
        if s == 0:
            return False
        
    return sum(sides[:2]) >= sides[2]

def equilateral(sides):
    return triangle(sides) and len(set(sides)) == 1

def isosceles(sides):
    return triangle(sides) and len(set(sides)) < 3

def scalene(sides):
    return triangle(sides) and len(set(sides)) == 3
