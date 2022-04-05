import pandas as pd
import csv
df = pd.read_csv('final.csv')
print(df.shape)
df.drop(['Unnamed: 0','Unnamed: 5', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1'],axis=1,inplace=True)
print(df.shape)
final_data = df.dropna()
final_data.to_csv('final_data.csv')