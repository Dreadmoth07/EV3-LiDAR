def readFile(filePath):
    file = open(filePath,"r")
    content = []
    line = file.readline()
    while line != "":
        content.append(line)
        line = file.readline()
    content.append("")
    return content

def writeFile(filePath, content):
    file = open(filePath, "w+")
    file.writelines(content)

def appendFile(filePath,content):
    file = open(filePath, "a+")
    file.writelines(content)

if __name__ == "__main__":
    content = readFile("Data-Rep/Test.txt")
    print(content)
    appendFile("Data-Rep/test2.txt", content)
    print(readFile("Data-Rep/test2.txt"))
