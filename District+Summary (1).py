
# coding: utf-8

# In[76]:


import pandas as pd
import numpy as np


# In[77]:


students_csv = "../raw_data/students_complete.csv"
schools_csv = "../raw_data/schools_complete.csv"


# In[78]:


students_df = pd.read_csv(students_csv)
schools_df = pd.read_csv(schools_csv)


# In[79]:


students_df.head()


# In[80]:


schools_df.head()


# In[81]:


# average math test score
average_math = students_df["math_score"].mean()
# average reading test score
average_reading = students_df["reading_score"].mean()
# number of kids passing math
passing_math = students_df.loc[(students_df["math_score"] >= 60)]
# number of kids passing reading
passing_reading = students_df.loc[(students_df["reading_score"] >= 60)]
# total number of students in the district
total_students = students_df.name.count()
#total schools in district
total_schools = schools_df.name.count()
# district budget in dollars (add dollar sign)
total_budget = schools_df.budget.sum()
# I want this to return the % of kids who have a passing math score
percentage_passing_math = (passing_math.name.count() / total_students) * 100
# I want this to return the % of kids who have a passing reading score
percentage_passing_reading = (passing_reading.name.count() / total_students) * 100
# Average of Both of the above variables
passing_both = ((percentage_passing_math + percentage_passing_reading) / 2)


# In[82]:


#Name of each school
school_name = schools_df["name"]
#Type of each school
school_type = schools_df["type"]
#Total students per individual school
ind_students = schools_df["size"]
#Total budget per individual school
ind_budget = schools_df["budget"]
#Per student budget per school
ind_budget_per_student = ind_budget / ind_students
#Average Math score per school
groupby_ind_math = students_df['math_score'].groupby(students_df['school'])
ind_average_math = groupby_ind_math.mean()
#Average Reading score per school
groupby_ind_reading = students_df['reading_score'].groupby(students_df['school'])
ind_average_reading = groupby_ind_reading.mean()
#% Passing Math by school
ind_students1 = ind_students.groupby(schools_df['name'])
groupby_ind_passing_math = passing_math.groupby(students_df['school'])
percent_ind_passing_math = (groupby_ind_passing_math["school"].count()) / (ind_students1.sum()) * 100
percent_ind_passing_math
#% Passing Reading by school
groupby_ind_passing_reading = passing_reading.groupby(students_df['school'])
percent_ind_passing_reading = (groupby_ind_passing_reading['school'].count()) / (ind_students1.sum()) * 100
percent_ind_passing_reading 
#Overall Passing (avg of two above)
percent_ind_overall_passing = (percent_ind_passing_math + percent_ind_passing_reading) / 2
percent_ind_overall_passing


# In[84]:


#Table for the Key Metrics for the entire District
district_df = pd.DataFrame([[total_schools,total_students,total_budget,average_math,average_reading,percentage_passing_math, percentage_passing_reading,passing_both]],columns=['Total Schools','Total Students','Total Budget($)','Average Math Score','Average Reading Score', '% Passing Math','% Passing Reading', '% Overall Passing Rate'])
print ("**DISTRICT SUMMARY**")    
district_df


# In[85]:


#Table for the Key Metrics for the each School in the district
individual_schools_df = pd.DataFrame([[school_name,school_type,ind_students, ind_budget,ind_budget_per_student, ind_average_math, ind_average_reading, percent_ind_passing_math, percent_ind_passing_reading, percent_ind_overall_passing]], columns=["School Name", "School Type", "Total Students", "Total School Budget($)", "Per Student Budget($)", "Average Math Score", "Average Reading Score","% Passing Math", "% Passing Reading", "Overall Passing Rate"])
individual_schools_df.set_index('School Name', inplace=True)
print("**SCHOOL SUMMARY**")
individual_schools_df

