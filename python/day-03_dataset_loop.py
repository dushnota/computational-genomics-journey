values = [12.5, 8.0, 20.3, 5.4, 15.7, 3.2]

threshold = 10

count = 0

for value in values:
    if value > threshold:
        print("High expression:", value)
        count = count + 1
    else:
        print("Low expression:", value)

print("Number of values above threshold:", count)
