import pandas as pd

excel_data_path = "C:\\Users\\AST-TITAN\\Documents\\Python Scripts\\out.csv"

df = pd.read_csv(excel_data_path)
print(df)
defect_tiles = df[df >= 95].count(axis = 'columns')

data = []
for i in range (0, len(defect_tiles), 456):
        slc = defect_tiles.iloc[i : i + 456]
        pred = slc.sum(axis='rows')
       
        data.append(pred)

print(data)        