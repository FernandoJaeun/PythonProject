import os
os.environ['CLASSPATH']
os.environ['PATH']
os.chdir("C:/Users/leeja/WorkSpace/Python/Python Project/python basic")
os.getcwd()

os.mkdir("tempDir")
os.system("dir")

f = os.popen("dir")
print(f.read())
import calendar
print(calendar.calendar(2020))