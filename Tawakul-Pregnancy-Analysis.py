
import pandas as pd

# Tawakul Dairy Farm - Pregnancy Records Analysis
# 44 Animals Data as on 26-07-2025

file_path = "Tawakul_Cattle_Pregnancy_Record_26-07-2025.xlsx"
df = pd.read_excel(file_path)

# Analysis
pregnant = df[df['Current Status'].str.contains('Pregnant', na=False)]
open_cows = df[df['Current Status'].str.contains('Open', na=False)]

print(f"Total Animals: {len(df)}")
print(f"Confirmed Pregnant: {len(pregnant)}")
print(f"Open: {len(open_cows)}")
print(f"Average Pregnancy Days: {df['Pregnancy Days Count'].mean():.1f}")

# Show remarks
print("\nRemarks Summary:")
print(df['Remarks'].value_counts())
