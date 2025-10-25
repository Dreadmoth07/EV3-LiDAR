import fileOps as fo

class Vertex():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def getInfo(self):
        return [self.x,self.y,self.z]

def splitLayers(filePath):
    # Creating 2d array of layers and vertices
    layer = []
    layers = []
    fileContent = fo.readFile(filePath)
    for line in fileContent:
        ints = []
        if line == "\n" or line == "":
            layers.append(layer)
            layer = []
        else:
            ints = getIntsFromString(line)
            v = Vertex(ints[0], ints[1], ints[2])
            layer.append(v)
    return layers

def getIntsFromString(string):
    ints = []
    temp = ""
    for char in string:
        if char == " " or char == "\n":
            ints.append(int(temp))
            temp = ""
        else:
            temp += char
    return ints

def formatFile(inFilePath,outFilePath):
    vGrid = splitLayers(inFilePath)
    content = []
    # Outputting Vertices
    for layer in vGrid:
        for vertex in layer:
            v = vertex.getInfo()
            content.append(f"v {v[0]} {v[1]} {v[2]}\n")
    fo.writeFile(outFilePath, content)

if __name__ == "__main__":
    formatFile("Data-Rep/Test.txt", "Output.obj")