import pandas as pd
import matplotlib.pyplot as plt

# Loading dataset
df = pd.read_csv('data.csv')

# 1. PIE CHART (distributuon of job titles)

job_counts = df['job_title'].value_counts()

plt.figure()
plt.pie(job_counts, labels=job_counts.index, autopct='%1.1f%%')
plt.title('Job Title Distribution')
plt.show()



# 2. BAR CHART (average salary)

avg_salary = df.groupby('job_title')['salary'].mean()

plt.figure()
plt.bar(avg_salary.index, avg_salary.values)
plt.xticks(rotation=45)
plt.title('Average Salary by Job Title')
plt.xlabel('Job Title')
plt.ylabel('Average Salary')
plt.show()


# 3. STAIR (STEP) CHART (salary vs experience)

df_sorted = df.sort_values('experience_years')

plt.figure()
plt.step(df_sorted['experience_years'], df_sorted['salary'], where='mid')
plt.title('Salary vs Experience (Step Chart)')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary')
plt.show()