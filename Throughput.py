import urllib

def getsize(uri):
    file = urllib.urlopen(uri)
    return len(file.read())

print getsize("http://www.starfall.com/")

