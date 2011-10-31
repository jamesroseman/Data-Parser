def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return (i + 1)
x = file_len("input.txt")
y = file_len("output.txt")
z = file_len("input.csv")
q = file_len("corrected.csv")
print ("input.txt: ", x)
print ("output.txt: ", y)
print ("input.csv: ", z)
print ("corrected.csv ", q)
user = input()
