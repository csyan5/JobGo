import json

f=open('/Users/yan/BigDataLab1/JobSearch/BeautifuSoup/GDSal/Final_Salaries.json')

low = []
for line in f:
    line = json.loads(line)
    low.append(line['low_sal'])

print([i for i in low if i < 25000])

f.close()
