import csv, os

os.makedirs('headerRemoved', exist_ok=True)
for f in os.listdir('reports'):
    if f.endswith('.csv'):
        with open(os.path.join('reports', f), 'r') as fo, \
            open(os.path.join('headerRemoved', f), 'w', newline='') as outfo:
            reader = csv.reader(fo)
            writer = csv.writer(outfo)
            for row in reader:
                if reader.line_num > 1:
                    writer.writerow(row)
