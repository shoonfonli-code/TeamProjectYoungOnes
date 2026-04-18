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