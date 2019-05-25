import pandas as pd

mfp = 'melb_data.csv'
m_data = pd.read_csv(mfp)
m_print = m_data.describe()
feat = ['Rooms', 'YearBuilt', 'Price']
x = m_data[feat]
print(x.head(10))