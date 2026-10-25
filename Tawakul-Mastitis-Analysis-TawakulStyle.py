
import pandas as pd

# Tawakul Dairy Farm - Mastitis Analysis
# 20 Cows Data Analysis

file_path = "Tawakul_Mastitis_Record_20cows_Tawakul_Style.xlsx"
df = pd.read_excel(file_path)

# Analysis
mastitis_cows = df[df['SCC x1000'] > 200]
healthy_cows = df[df['SCC x1000'] <= 200]

avg_scc_mastitis = mastitis_cows['SCC x1000'].mean()
avg_scc_healthy = healthy_cows['SCC x1000'].mean()
avg_milk_mastitis = mastitis_cows['Milk Yield (L)'].mean()
avg_milk_healthy = healthy_cows['Milk Yield (L)'].mean()
milk_loss = avg_milk_healthy - avg_milk_mastitis

print(f"Total Cows: {len(df)}")
print(f"Mastitis Cows (SCC>200k): {len(mastitis_cows)}")
print(f"Healthy Cows: {len(healthy_cows)}")
print(f"Avg SCC Mastitis: {avg_scc_mastitis:.1f} x1000")
print(f"Avg SCC Healthy: {avg_scc_healthy:.1f} x1000")
print(f"Milk Loss due to Mastitis: {milk_loss:.1f} L per cow per day")
