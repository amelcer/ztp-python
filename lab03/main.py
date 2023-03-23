from fileLoader import load_json
import pandas as pd


# df = pd.read_csv('data.csv')
# print(df)

data = load_json('signals.json')

print(data)
