import math
from PIL import Image, ImageDraw

W = 800
H = 400

im = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(im)

points = []

for px in range(W):
    x = px / W * 2 * math.pi
    y = math.sin(x)

    py = H/2 - y * 150

    points.append((px, py))

draw.line(points, fill="black", width=2)

im.show()
