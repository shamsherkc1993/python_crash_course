import pandas as pd
import matplotlib.pyplot as plt

json_file = "/Users/shamsher/Desktop/Project/python_crash_course/DATAS/departments.json"
df = pd.read_json(json_file)

plt.figure()
plt.bar(df['dept_name'], df['dept_id'])

plt.xlabel("Department Name")
plt.ylabel("Department ID")
plt.title("Departments Chart")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()