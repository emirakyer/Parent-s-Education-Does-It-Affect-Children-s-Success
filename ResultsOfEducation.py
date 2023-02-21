import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#Codes For Analysis ---


data=pd.read_csv("StudentsPerformance.csv")
df=pd.DataFrame(data)

# We List To Calculate The Number Of Parents With And Without A College Education
infoParents=df["parental level of education"].value_counts()
listForAnalyze=[]
listForAnalyze=infoParents

# We Are Calculating Two Education Status For Compare
gatherHighsSchoolParents=listForAnalyze["high school"]+listForAnalyze["some high school"]
gatherUniversityParents=listForAnalyze["some college"]+listForAnalyze["master's degree"]+listForAnalyze["associate's degree"]+listForAnalyze["bachelor's degree"]

def meanCalculator(a,b):

    return a/b

# Classification
meanHighSchoolParentsChild=df[(df["parental level of education"]=="high school") | (df["parental level of education"]=="some high school")].mean()
meanUniversityParentsChild=df[(df["parental level of education"]=="some college") | (df["parental level of education"]=="master's degree")| (df["parental level of education"]=="associate's degree")| (df["parental level of education"]=="bachelor's degree")].mean()

# Listing
meanHighSchoolParentsChildDict={"Math Score":62,"Reading Score":66,"Writing Score":63}
meanUniversityParentsChildDict1={"Math Score":68,"Reading Score":71,"Writing Score":70}



### CHARTS ---


# 1) Pie Chart ==> Proportions of parents with or without university education

colors=["blue","orange"]
situationOfParentsMeans=[gatherUniversityParents,gatherHighsSchoolParents]
situationParentsLabel="Parents Of University Educated","Parents Of HighSchool Educated"
plt.pie(situationOfParentsMeans,labels=situationParentsLabel,colors=colors, autopct="%1.1f%%",shadow=True,explode=(0.05,0.25))

plt.show()


# 2) Bar Chart ==> Parents Educated At (High School | University) Children's Success

scores = list(meanHighSchoolParentsChildDict.keys())
scores2 = list(meanHighSchoolParentsChildDict.values())
scores3 = list(meanUniversityParentsChildDict1.values())

plt.figure(figsize=(10,5))

plt.bar(scores, scores2, label="Parents Educated At High School | Children's Success")
plt.bar([s + '(Uni)' for s in scores], scores3, label="Parents Educated At University | Children's Success")

plt.xlabel("Students' Exam Results")
plt.ylabel("Scores")
plt.title("Mean | High School Education Parents Child Scores vs University Parents Child Scores")
plt.legend()

plt.show()


# 3) Subplot Chart ==> Parents Educated At (High School | University) Children's Success

scores4=list(meanUniversityParentsChildDict1.keys())
figure = plt.figure(figsize=(7,7))


ax1 = figure.add_subplot(211)
ax1.plot(scores3,scores4)
ax1.set_title("Parents Educated At University | Children's Success")

ax2 = figure.add_subplot(212)
ax2.plot(scores2,scores)
ax2.set_title("Parents Educated At High School | Children's Success")

plt.tight_layout()

plt.show()





