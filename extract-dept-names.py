import pandas as pd

# Load the dataset
url = 'processed-payroll.csv'
df = pd.read_csv(url)

# Get unique department titles and job titles
unique_departments = df['DEPARTMENT_TITLE'].unique()
unique_job_titles = df['JOB_TITLE'].unique()

# Save unique departments to a text file
with open('unique_departments.txt', 'w') as f:
    for dept in unique_departments:
        f.write("%s\n" % dept)

# Save unique job titles to a text file
with open('unique_job_titles.txt', 'w') as f:
    for job in unique_job_titles:
        f.write("%s\n" % job)

print("Unique department titles and job titles saved to text files.")
