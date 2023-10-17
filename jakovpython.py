import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("Construction_Data_PM_Tasks_All_Projects.csv")

# Ensure that the 'OverDue' column is of type boolean. This might not be necessary if the data is already in boolean format, but it's a safety check.
df["OverDue"] = df["OverDue"].astype(bool)

# Filter the rows where the "OverDue" column indicates the task is overdue
overdue_tasks = df[df["OverDue"] == True]

# Print the total number of overdue tasks
print(f"Total number of overdue tasks: {len(overdue_tasks)}")

# Get unique value counts for the "Task Group" column
task_group_counts = df["Task Group"].value_counts()

# Print the unique values and their counts
print(task_group_counts)

# Group by 'Task Group' and 'Report Status', then count the occurrences
group_status_counts = df.groupby(["Task Group", "Report Status"]).size().unstack(fill_value=0)

# Print the results
print(group_status_counts)

import matplotlib.pyplot as plt


# Filter tasks that are overdue (assuming "OverDue" is either True or False)
overdue_tasks = df[df["OverDue"] == True]

import matplotlib.pyplot as plt

# Ensure "OverDue" is in boolean type
df["OverDue"] = df["OverDue"].astype(bool)

import matplotlib.pyplot as plt

# Ensure "OverDue" is in boolean type
df["OverDue"] = df["OverDue"].astype(bool)

# Group by the "project" column and sum the "OverDue" column
overdue_by_project = df.groupby("project")["OverDue"].sum()

# Plotting
overdue_by_project.plot(kind='bar', figsize=(10,6))
plt.title('Number of OverDue tasks by Project')
plt.ylabel('Number of OverDue tasks')
plt.xlabel('Project')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot as an image
plt.savefig("overdue_by_project.png", dpi=300)
plt.close()


# Group by 'Task Group' and 'Report Status', then count the occurrences
grouped_counts = df.groupby(["Task Group", "Report Status"]).size().unstack()

# Plotting
grouped_counts.plot(kind='bar', figsize=(12,7))
plt.title('Report Status by Task Group')
plt.ylabel('Count')
plt.xlabel('Task Group')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the figure to an image
plt.savefig("report_status_by_task_group.png", dpi=300)
plt.close()

