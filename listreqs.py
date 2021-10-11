path = input()
with open (path, "r") as myfile:
    data = myfile.read().splitlines()

data = data[2:-1]
for i in range(len(data)):
    lib_name = data[i].split(" ")[0]+"=="+data[i].split(" ")[-1]
    data[i] = lib_name

with open(path, 'w') as f:
    for line in data:
        f.write(line)
        f.write('\n')

