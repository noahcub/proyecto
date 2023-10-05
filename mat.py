import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt (r'TEMP_MADRID.txt', dtype='str', skiprows=1)

print(data)

print(data.shape)