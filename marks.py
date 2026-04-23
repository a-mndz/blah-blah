import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("marks.csv")

print(df)

fig,(ax1,ax2) = plt.subplots(1, 2, figsize=(15, 8))

ax1.scatter(df["name"], df["marks"])
ax1.set_xlabel('name')
ax1.set_ylabel('marks')
ax1.set_title('Marks of Students')

ax2.bar(df["name"], df["marks"])
ax2.set_xlabel('name')
ax2.set_ylabel('marks')
ax2.set_title('Marks of Students')
plt.tight_layout()
plt.show()