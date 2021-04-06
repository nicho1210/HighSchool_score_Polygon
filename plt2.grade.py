import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.collections import PolyCollection

dataset = pd.read_csv('high_score.csv')

fig = plt.figure(figsize=(10, 10), dpi=300)
ax = fig.gca(projection='3d')

semesters = ["","1_first", "1_second", "2_first","2_second", "3_first",""]
subjects = ["math", "physics", "english", "computer", "chinese", "overall"]

semesterIdx = range(0, 7)
subIdx = range(0,6)

precipitation = [] 
precipitation.append(list(zip(semesterIdx, dataset.math_score)))
precipitation.append(list(zip(semesterIdx, dataset.physics_score)))
precipitation.append(list(zip(semesterIdx, dataset.english_score)))
precipitation.append(list(zip(semesterIdx, dataset.computer_score)))
precipitation.append(list(zip(semesterIdx, dataset.chinese_score)))
precipitation.append(list(zip(semesterIdx, dataset.overall)))

poly = PolyCollection(precipitation, facecolors=['b','c','r','m','y','g'])
poly.set_alpha(0.7)

ax.add_collection3d(poly, zs=subIdx, zdir='y')
ax.set_xlabel('Semester')
ax.set_xticks(np.arange(len(semesters)))
ax.set_xticklabels(semesters)
#ax.set_xlim3d(0, 6)
ax.set_ylabel('subjects')
ax.set_yticks(np.arange(len(subjects)))
ax.set_yticklabels(subjects)
#ax.set_ylim3d(0, 5)
ax.set_zlabel('Precipitation')
ax.set_zlim3d(0, 100)

plt.show()