import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("mark2.csv")

print(df)

# plt.pie(df["average marks"], labels=df["name"], autopct="%1.1f%%")
# plt.title("Marks Distribution")
# plt.show()

plt.bar(df["name"], df["average marks"],df["average marks"])
plt.xlabel("Name")  
plt.ylabel("Average Marks")
plt.title("Average Marks of Students")
plt.show()