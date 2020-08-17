
import os

def search(dirname):
    fileNames = os.listdir(dirname)
    try:
        for fileName in fileNames:
            fullFileName = os.path.join(dirname, fileName)
            if os.path.isdir(fullFileName):     # fullFileName 이 디렉토리라면 또 파고든다
                search(fullFileName)
            else:
                # fullFileName이 파일이라면 확장자명만 가져온다.
                ext = os.path.splitext(fullFileName)[-1]
                # splittext는 확장자명을 가져오는 함수다.
                if ext == '.py' or ext == '.txt':
                    print(fullFileName)
    except PermissionError:
        pass


# search('C:/Users/leeja/WorkSpace/Python/Python Project')


for (path, dir, files) in os.walk("C:/Users/leeja/WorkSpace/Python/Python Project"):
    for filename in files:
        ext = os.path.splitext(filename[-1])
        if ext == '.py':
            print("%s %s" % (path,dir))        


