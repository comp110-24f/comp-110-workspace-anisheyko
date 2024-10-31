"""checking Point methods for correctness"""

from CQs.cq09.point import Point

# declare original point
point_1 = Point(1.0, 2.0)

# test scale doesn't change point_1
point_1.scale(2)
print(point_1)

# test scale_by
point_1.scale_by(3)
