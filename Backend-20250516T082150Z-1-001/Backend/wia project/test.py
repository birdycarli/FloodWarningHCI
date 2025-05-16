data = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
]

# Your labels
labels = ['rainfall', 'normal', 'alert', 'warning', 'danger']
'''
    with open ('rainfallDatas.csv', mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['state', 'district', 'rainfall', 'normal', 'alert', 'warning', 'danger'])
        writer.writerows(rainfallDatas)
    '''

data_dict = {
    'rainfall':[],
    'normal':[],
    'alert':[],
    'warning':[],
    'danger':[]
}

for row in data:
    for i in range(5):
        data_dict[labels[i]].append(row[i])

# Display the dictionary
print (data_dict)