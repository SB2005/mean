import pandas as pd 
import statistics as st 

h_df = pd.read_csv("SOCR-HeightWeight.csv")
print(h_df)

h_list = h_df["Height(Inches)"].tolist()
#print(h_list)

sum = 0
for h in h_list:
    sum = sum + h

mean = sum/len(h_list)
print(f"Mean of height list is {mean}")

mean = st.mean(h_list)
mode = st.mode(h_list)
median = st.median(h_list)

print(f"Mean of height list is {mean}")

print(f"Mode of height list is {mode}")
print(f"Median of height list is {median}")
