from p5 import *

stars = []


def setup():
    size(800, 600)
    no_stroke()
    for i in range(200):
        stars.append({
            "x": random_uniform(0, width),
            "y": random_uniform(0, height),
            "speed": random_uniform(0.5, 2),
            "size": random_uniform(1, 4),
        })


def draw():
    background(10, 10, 30, 20)
    fill(255, 255, 200)
    for star in stars:
        circle((star["x"], star["y"]), star["size"])
        star["y"] += star["speed"]
        if star["y"] > height:
            star["y"] = 0
            star["x"] = random_uniform(0, width)


if __name__ == "__main__":
    run()
