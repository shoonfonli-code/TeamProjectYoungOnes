# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
    # Use a breakpoint in the code line below to debug your script.  # Press ⌘F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Provided Libraries
import pandas as pd                 # For Excel File, also need openpyxl
import matplotlib.pyplot as plt     # Plotting
import numpy as np                  # Calculations

excel_file = "BEAM_Dashboard_-_Serotypes_of_concern__Illnesses_and_Outbreaks_20260418.xlsx"
df = pd.read_excel("BEAM_Dashboard_-_Serotypes_of_concern__Illnesses_and_Outbreaks_20260418.xlsx")

#Step 2/3: Aggregate by Serotype # Record Data
serotypes = df["Serotype"].dropna().unique()
print("Number of serotypes:", len(serotypes))

###############################################################################################
#Step 4: Sort by Year
#To determine which is the most FREQUENT, as in, most times of no_of_illness not being 0
nonzero = df[df["No_of_illnesses"] > 0]
freq = nonzero["Serotype"].value_counts().head(10) #Count how many times each serotype appears
print(freq)
#We can see expectedly that Enteritidis is the most frequently reported illness irrespective of meat
####################################################################################
#Step 5: Trend Analysis
# sum illnesses for each serotype in each year
yearlytotals = df.groupby(
    ["Serotype", "Year_first_ill"]
)["No_of_illnesses"].sum().reset_index()

# #Plotting the graph
plt.figure(figsize=(14,8))
for name, group in yearlytotals.groupby("Serotype"):
    group = group.sort_values("Year_first_ill")
    plt.plot(group["Year_first_ill"], group["No_of_illnesses"], marker="o", label=name)


plt.xlabel("Year")
plt.ylabel("Total Illnesses")
plt.title("Number of Illnesses for each Serotypes across time")
plt.legend()
#the legend is covering up the grid
plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left")
plt.grid()
plt.show()


Sumalltotals = df.groupby("Serotype")["No_of_illnesses"].sum()

hightolowtotals = Sumalltotals.sort_values(ascending=False)
print(hightolowtotals)

##############################################################################################
#Step 6:Top 10 Over Time

# sum illnesses by serotype & year
hightolowtotals = Sumalltotals.sort_values(ascending=False).head(10)
print(hightolowtotals)
yearlytotals = df.groupby(["Serotype", "Year_first_ill"])["No_of_illnesses"].sum().reset_index()
top10 = hightolowtotals.index
# keep only those rows
top10data = yearlytotals[yearlytotals["Serotype"].isin(top10)]

#Plotting the graph of the top 10
plt.figure(figsize=(14,8))
for name, group in top10data.groupby("Serotype"):
    group = group.sort_values("Year_first_ill")
    plt.plot(group["Year_first_ill"], group["No_of_illnesses"], marker="o", label=name)

plt.xlabel("Year")
plt.ylabel("Total Illnesses")
plt.title("Number of Illnesses for the Top 10 Serotypes across time")
plt.legend()
plt.legend(bbox_to_anchor=(0.86, 1), loc="upper left")
plt.grid(True)
plt.show() #shows graph

###############################################################################################
#Step 7: Resort by Serotype
meat_serotype = df.groupby(["Serotype", "Food_category"])["No_of_illnesses"].sum().reset_index()
pivot = meat_serotype.pivot(
    index="Serotype",
    columns="Food_category",
    values="No_of_illnesses").fillna(0)
# A pivot basically reshapes the data into a new data table that can be used to make a bar graph
##############################################################################################
#Step 8, Bar graph of serotype and meat type
pivot.plot(kind="bar", stacked=True, figsize=(14,8))

plt.title("Illnesses by Meat Type for Each Serotype")
plt.xlabel("Serotype")
plt.ylabel("Total Illnesses")
plt.xticks(rotation=45)
plt.legend(title="Food Category", bbox_to_anchor=(0.90,1), loc="upper left")
plt.tight_layout()
plt.show()