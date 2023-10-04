import pandas as pd 
df = pd.read_csv("projectC233_studentData.csv")
df["Total_marks_obtained"]=df.iloc[:,[2,3,4]].sum(axis = 1)
df.loc[df["Total_marks_obtained"]>250,"grade"]="A"
df.loc[df["Total_marks_obtained"]<250,"grade"]="B"
df["Precentage"]=(df["Total_marks_obtained"]/df["Overall_Total"])*100
print("The overall students report: \n",df)