import os   # 파일 경로를 찾기 위한 라이브러리
import sys  # 파일을 가져오기 위한 라이브러리

# 파일을 가져온다 : 파일 경로, 파일 이름
# 파일을 연다
# 파일의 탭을 공백으로 바꾼다. 저장한다.

# 1.파일의 위치를 찾음
def search(dirName, setFileName):
    try:
        files = os.listdir(dirName)
        for fileName in files:
            fullFileName = os.path.join(dirName, fileName)
            if os.path.isdir(fullFileName):     # fullFileName 이 디렉토리라면 또 파고든다
                search(fullFileName, setFileName)
            else:
                getFilePath(fullFileName,setFileName)
    except PermissionError:
        print(fullFileName, "해당 디렉터리는 접근 권한이 없습니다")
        pass

def getFilePath(fullFileName,setFileName):
    ext = os.path.splitext(fullFileName)[-1]    # fullFileName이 파일이라면 확장자명만 가져온다.
    if ext == '.py':   # splittext는 확장자명을 가져오는 함수다.
        if os.path.basename(fullFileName) == setFileName:
            print(fullFileName)

# 1.1 파일 이름 입력, 검색 //  예)"c:/Users/leeja/WorkSpace/Python/Python Project"
dirName = input("파일의 경로를 입력해주세요 : ")
if os.path.isdir(dirName):
    setFileName = input("파일 이름을 입력하세요 : ")
search(dirName, setFileName)    
