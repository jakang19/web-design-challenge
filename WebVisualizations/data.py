import pandas as pd

df = pd.read_csv('Resources/cities.csv')
table = df.to_html('data.html', index=False)
print(table)