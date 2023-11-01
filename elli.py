import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point
from shapely.geometry.polygon import LinearRing

# 创建椭圆
def create_ellipse(a, b, center, angle, num_points=100):
    t = np.linspace(0, 2*np.pi, num_points)
    x = center[0] + a * np.cos(t)
    y = center[1] + b * np.sin(t)
    x_rot = center[0] + x*np.cos(angle) - y*np.sin(angle)
    y_rot = center[1] + x*np.sin(angle) + y*np.cos(angle)
    return x_rot, y_rot

# 两个椭圆
x1, y1 = create_ellipse(5, 3, [0, 0], np.pi/6)
x2, y2 = create_ellipse(4, 2, [2, 2], np.pi/3)

# 计算交点
ellipse1 = LinearRing(np.column_stack((x1, y1)))
ellipse2 = LinearRing(np.column_stack((x2, y2)))
intersection = ellipse1.intersection(ellipse2)

# 计算最小包含椭圆
if intersection.geom_type == 'MultiPoint':
    coords = np.array(intersection)
    centroid = np.mean(coords, axis=0)
    a = np.max(np.abs(coords[:, 0] - centroid[0]))
    b = np.max(np.abs(coords[:, 1] - centroid[1]))
    x_enc, y_enc = create_ellipse(a, b, centroid, 0)

# 绘图
plt.figure(figsize=(8, 8))
plt.plot(x1, y1, label='Ellipse 1')
plt.plot(x2, y2, label='Ellipse 2')
plt.scatter(*zip(*intersection), color='red', label='Intersection Points')
plt.plot(x_enc, y_enc, '--', label='Minimum Enclosing Ellipse')
plt.legend()
plt.grid(True)
plt.show()
