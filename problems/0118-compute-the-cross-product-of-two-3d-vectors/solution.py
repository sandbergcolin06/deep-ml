import numpy as np

def cross_product(a, b):
    # Your code here
    if len(a) != len(b):
        return -1
    else:
        return [a[1]*b[2] - a[2]*b[1],a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]