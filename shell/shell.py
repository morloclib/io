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

def streamLinesF(filename):
    if isGzipF(filename):
        return streamLinesGzipF(filename)
    else:
        return streamLinesTextF(filename)

#  writeLinesF :: [Str] -> Filename -> ()
def writeLinesF(xs, filename):
    with open(filename, "w") as fh:
        for x in xs:
            print(x, file=fh)

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

def headF(nlines, filename):
    """
    Return a list of the first n lines from a file. If the file is gzip'd then unzip it. Stream the file, so it is not all loaded into memory.
    """
    gen = streamLinesF(filename)
    xs = []
    for _ in range(nlines):
        xs.append(next(gen))
    return xs


def tailF(nlines, filename):
    """
    Return a list of the first n lines from a file. If the file is gzip'd then unzip it. Stream the file, so it is not all loaded into memory.
    """
    from collections import deque
    gen = streamLinesF(filename)
    xs = deque()
    for line in gen:
        xs.append(line)
        if len(xs) > nlines:
            xs.popleft()
    return xs


def nlines(filename):
    gen = streamLinesF(filename)
    n = 0
    for _ in gen:
        n += 1
    return n
