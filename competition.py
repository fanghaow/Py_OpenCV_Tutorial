# This file is used to randomly layout the competition feild.
# Author : fanghao_w
#  DATE  : 2021.07.23
import numpy as np

"""
yellow -> 黄基座 * 3
empty  -> 种子盘 * 3
green  -> 绿基座 * 18
"""

layout = 3 * ["yellow"] + 3 * ["empty"] + 18 * ["green"]
np.random.shuffle(layout)

print("The 1st row layout : ",layout[:12])
print("The 2nd row layout : ",layout[12:])