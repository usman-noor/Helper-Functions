import pandas as pd 
df = pd.read_excel('Book1.xlsx', sheetname = 'Sheet1')

pairs = []
for index, row in df.iterrows():
    if len(row['NAME'].split(',')) > 1 :
        names = row['NAME'].split(',')
        for name in names:
            pairs.append([row['DocID '],name])
    else:
         pairs.append([row['DocID '], row['NAME']])
print(pairs)

df2 = pd.DataFrame(pairs, columns = ['DocID' , 'NAME'])

df2_dedup = df2.drop_duplicates()

df2_dedup

final_dict = {}

for index, row in df2_dedup.iterrows():
    if row['DocID'] in final_dict:
        final_dict[row['DocID']]  = final_dict[row['DocID']] + '|' + row['NAME']
    else :
        final_dict[row['DocID']]  =  row['NAME']
        


pd.DataFrame(list(final_dict.items()) ,columns = ['DocID' , 'NAME'])
