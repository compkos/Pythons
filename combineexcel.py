# Section 1
import pandas as pd
files = ['january.xlsx', 'february.xlsx', 'march.xlsx']
combined = pd.DataFrame()

# Section 2
for file in files:
  df = pd.read_excel(file, skiprows = 3)
  combined = combined.append(df, ignore_index = True)
  
# Section 3
combined.to_excel('combined.xlsx')