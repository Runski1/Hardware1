"""
My side project for playing with SSD1306 and OLED
School of ICT
Metropolia University of Applied Sciences
27.1.2023, Matias Ruonala

I forked Sakari Lukkarinen' demo project
https://wokwi.com/projects/354671838787709953
and used its' initialization code
"""
from machine import Pin, I2C
import ssd1306
from ulab import numpy as np
import utime
import math

led = Pin("LED", Pin.OUT)
OLED_SDA = 14  # Data
OLED_SCL = 15  # Clock

# Initialize I2C to use OLED
i2c = I2C(1, scl=Pin(OLED_SCL), sda=Pin(OLED_SDA), freq=3200000)
OLED_WIDTH = 128
OLED_HEIGHT = 64
oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)

utime.sleep(1)
print("boot initialized")

origin = np.array([64, 32, 0]) # Center of the screen
cube_size = 13
# 8 corner points of a cube
cube_corners = np.array([
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
])
# Edges between the corners
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom face
    (4, 5), (5, 6), (6, 7), (7, 4),  # Top face
    (0, 4), (1, 5), (2, 6), (3, 7)   # Vertical edges
]
angle_deg = 0 # Beginning rotation angle in degrees
pulse_min = 0.5 # Minimum scale of the cube
while True:
    oled.fill(0)
    angle = angle_deg * (math.pi / 180)
    # Rotation matrices
    rotation_Z = np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])
    rotation_Y = np.array([
        [np.cos(angle), 0, -np.sin(angle)],
        [0, 1, 0],
        [np.sin(angle), 0, np.cos(angle)]
    ])
    rotation_X = np.array([
        [1, 0, 0],
        [0, np.cos(angle), -np.sin(angle)],
        [0, np.sin(angle), np.cos(angle)]
    ])
    # Rotate and pulse the cube
    points_3d = cube_corners * cube_size * (pulse_min + abs(np.sin(angle)))
    rotated_points_3d = np.dot(
        points_3d, np.dot(
            np.dot(rotation_X, rotation_Y), rotation_Z)) + origin
    # Draw edges, Z-coordinate is dropped
    for edge in edges:
        p1 = rotated_points_3d[edge[0]]
        p2 = rotated_points_3d[edge[1]]
        oled.line(int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]), 1)

    oled.show()
    angle_deg += 1
