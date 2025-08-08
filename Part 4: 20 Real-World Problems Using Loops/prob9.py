# Batch Process Data (Data Management)

data = [1,2,3,4,5]

batch_size = 2
for i in range(0, len(data), batch_size):
    batch = data[i:i + batch_size]
    print(f"Processing batch: {batch}")