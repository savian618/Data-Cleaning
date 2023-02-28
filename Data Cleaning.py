import csv

uuid = []
patent_id = []
text = []

file = open('patent_drawing data.csv')
csvreader = csv.reader(file)

rows = []
for row in csvreader:
    uuid.append(row[0])
    patent_id.append(row[1])
    text.append(row[2])

count = 0

for x in text:
    if ("perspective" in x or "view" in x) and (
            "bottom" not in x or "top" not in x or "front" not in x or "rear" not in x):
        count += 1
print("{} rows have the words view or perspective but do not include bottom, top, front or rear in  the text field".format(count))

no_dup = []
for x in patent_id:
    if x not in no_dup:
        no_dup.append(x)

avg_draw = len(patent_id) / len(no_dup)
print("{} ({} rounded) is the average number of drawing descriptions per patent".format(avg_draw, round(avg_draw)))
