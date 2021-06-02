outfile = open("names-formatted.txt", "w")

with open("names.txt") as infile:
    nameList = infile.readlines()

for x in nameList:
    nameSep = x.title()
    outfile.write(nameSep)

outfile.close()
infile.close()