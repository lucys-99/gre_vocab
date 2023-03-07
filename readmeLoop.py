import os

def write_readme():
    allmd = os.listdir("./docs")
    allmd.sort(key = lambda x: int(x[3:-3]))

    with open("README.md", "w") as f:
        f.write("# GRE VOCAB SCHEDULE: \n")
        f.write("https://lucys-99.github.io/gre_vocab/ \n")
        for i in allmd:
            f.write("* ["+ i[:-3] + "](./docs/" + i + ")\n")
        
        f.close()

if __name__ == "__main__" :
    write_readme()

