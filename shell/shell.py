import gzip

#  streamLinesGzipF :: Filename -> Stream Str
def streamLinesGzipF(filename):
    with gzip.open(filename, mode="rt", encoding="ascii") as fh:
        for line in fh.readlines():
            yield line.strip()

def streamLinesTextF(filename):
    with open(filename, mode="rt", encoding="ascii") as fh:
        for line in fh.readlines():
            yield line.strip()

#  writeLinesF :: [Str] -> Filename -> ()
def writeLinesF(xs, filename):
    for x in xs:
        print(x, file=filename)

#  printL :: [Str] -> ()
def printL(xs):
    for x in xs:
        print(x)

def hasExtension(extension, filename):
    return (extension in filename.split(".")[1:])

#  isgzF :: Filename -> Bool
def isGzipF(filename):
    """
    Determines if a file is gzip'd based on its extension

    This is not ideal. It should check for the magic numbers in the binary. But good enough for now.
    """
    return filename[-3:] == ".gz"
