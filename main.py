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
serotypes = df["Serotype"].dropna().unique()
#print(serotypes)
print("Number of serotypes:", len(serotypes))



###############################################################################
Sumalltotals = df.groupby("Serotype")["No_of_illnesses"].sum()

hightolowtotals = Sumalltotals.sort_values(ascending=False).head(10)
print(hightolowtotals)



#############################################################################
# sum illnesses by serotype & year
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
plt.show()
###############################################################################################
