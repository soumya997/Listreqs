import subprocess as sp
def listreqs():
    print("give file name")
    path = input()
    sp.run(f'touch {path}')
    with open(path,'w') as f:
        p1 = sp.run('pip list',stdout=f,text=True)

    with open (path, "r") as myfile:
        data = myfile.read().splitlines()


    data = data[2:-1]
    for i in range(len(data)):
        splt = data[i].split(" ")
        if splt[-1][1] == ":":
            lib_name = splt[0]+"=="+splt[3]
        else:
            lib_name = splt[0]+"=="+splt[-1]
        data[i] = lib_name

    with open(path, 'w') as f:
        for line in data:
            f.write(line)
            f.write('\n')



def listreqs_shell():
    # if not (os.path.isfile('listreqs.sh')):
    #     wget.download('https://raw.githubusercontent.com/soumya997/Listreqs/main/listreqs.sh')
    subprocess.call(['sh', 'lr.sh'])

