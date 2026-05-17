with open("pi.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    storage = []
    n = len(lines)
    for i in range(len(lines)):
        okay = False
        if i + 5 >= n:
            okay = False
            break
        if lines[i] < lines[i+1] < lines[i+2] < lines[i+3] and lines[i+4] > lines[i+5]: #0123 98
            okay = True
        elif lines[i] < lines[i+1] < lines[i+2] and lines[i+3] > lines[i+4] > lines[i+5]: #012 984 albo 019 984
            okay = True
        elif lines[i] < lines[i+1] and lines[i+2] > lines[i+3] > lines[i+4] > lines[i+5]: #01 9876
            okay = True

        if okay:
            storage.append([
                lines[i],
                lines[i+1],
                lines[i+2],
                lines[i+3],
                lines[i+4],
                lines[i+5],
            ])
print(len(storage))
print(storage)