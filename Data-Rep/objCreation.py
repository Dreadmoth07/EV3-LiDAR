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

def createReferences(grid):
    references = {}
    refNum = 1
    for layer in grid:
        for vertex in layer:
           references[vertex] = refNum
           refNum += 1
    return references

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

def addVertices(grid):
    content = []
    # Outputting Vertices
    for layer in grid:
        for vertex in layer:
            v = vertex.getInfo()
            content.append(f"v {v[0]} {v[1]} {v[2]}\n")
    return content

def addFaces(grid, refTable):
    maxLayers = len(grid) - 1
    faces = []
    # The hard part™
    # Assuming same number of vertices in each layer.
    verticesPerLayer = len(grid[0])

    for layer in range(0,maxLayers):
        # 1st set - going up
        for vertex in range(0,verticesPerLayer):
            v0 = grid[layer][vertex]
            v1 = grid[layer+1][vertex]
            vplus = vertex + 1
            if vplus == verticesPerLayer:
                vplus = 0
            v2 = grid[layer][vplus]


            r0 = refTable[v0]
            r1 = refTable[v1]
            r2 = refTable[v2]
            face = f"f {r0} {r1} {r2}\n"
            faces.append(face)
        
    for layer in range(1,maxLayers+1):
        # 2nd set - going down
        print(layer)
        for vertex in range(0,verticesPerLayer):
            v0 = grid[layer][vertex]
            lminus = layer-1
            if lminus == -1:
                lminus = maxLayers
            print(lminus)
            v1 = grid[lminus][vertex]
            v2 = grid[layer][vertex-1]


            r0 = refTable[v0]
            r1 = refTable[v1]
            r2 = refTable[v2]
            face = f"f {r0} {r1} {r2}\n"
            faces.append(face)
    
    
    face = "f "
    for vertex in grid[0]:
        face += f"{refTable[vertex]} "
    face += "\n"
    faces.append(face)
    face = "f "
    for vertex in grid[-1]:
        face += f"{refTable[vertex]} "
    face += "\n"
    faces.append(face)
    return faces
    


def formatFile(inFilePath,outFilePath):
    vGrid = splitLayers(inFilePath)
    refTable = createReferences(vGrid)

    content = addVertices(vGrid)
    fo.writeFile(outFilePath, "# Vertices\n")
    fo.appendFile(outFilePath, content)

    content = addFaces(vGrid, refTable)
    fo.appendFile(outFilePath, "# Faces\n")
    fo.appendFile(outFilePath, content)

if __name__ == "__main__":
    inFilePath = input("Enter the input file path: ").strip()
    outFilePath = input("Enter the output file name: ") .strip()
    formatFile(inFilePath, outFilePath)
    print("File Created!")