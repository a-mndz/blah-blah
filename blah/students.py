import matplotlib.pyplot as plt
import numpy as np
students=["Arun","Bina","Chitra","Dinesh","Esha","Alex"]
marks=[85,90,78,92,88,95]
fig,(ax1, ax2, ax3,ax4) = plt.subplots(1, 4, figsize=(15, 8))
ax1.bar(students, marks)
ax2.plot(students, marks, marker='o', color='red')
ax3.pie(marks, labels=students)
ax4.hist(marks, bins=5, color='green', edgecolor='black')
plt.tight_layout()
plt.show()