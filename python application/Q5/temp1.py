import sys

src = sys.argv[1]
dst = sys.argv[2]

file = open(src, 'w')
file.write("Life    is  too Short")
file.close()

file = open(src)
tap_content = file.read()
file.close()

file = open(dst,'w')
space_content = tap_content.replace("\t"," "*4)
file.write(space_content)
file.close()

