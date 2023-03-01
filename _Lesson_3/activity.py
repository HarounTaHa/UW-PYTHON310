import csv
import pathlib

path = pathlib.Path()
header = ['FIRST_NAME', 'LAST_NAME', 'EMAIL']
data = [
    ['Haroun', 'Taha', 'h@h.sa'],
    ['Test', 'Test', 't@t.sa'],
    ['Jamal', 'Tihi', 'j@j.sa'],
    ['Ahmed', 'Taha', 'a@a.sa']

]
file = open(pathlib.Path(path.absolute(), 'employees.csv'), 'w', newline='')
writer = csv.writer(file)
writer.writerow(header)
writer.writerows(data)
file.close()
# ---------------------------------------

path = pathlib.Path()
file = open(pathlib.Path(path.absolute(), 'employees.csv'))
reader = csv.reader(file)
data = []
for row in reader:
    if reader.line_num == 1:  # line_num is  Iterator for file csv
        header = tuple(row)
        data.append(header)
    else:
        data.append(row)

print(header)
print(data)
file.close()
