import sys

src = sys.argv[1]
dst = sys.argv[2]

file = open(src)
tap_content = file.read()
file.close()

space_content = tap_content.replace("\t"," "*4)
print(tap_content)
print(space_content)

file = open(dst,'w')
file.write(space_content)
file.close()

