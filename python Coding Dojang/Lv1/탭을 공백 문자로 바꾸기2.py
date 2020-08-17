class Modified:

    def searchFile(filePath, fileName):     # 파일찾기
        try:
            fileDir = os.listdir(filePath)    # filePath의 모든 디렉토리를 가져옴
            for fileName in fileDir:
                fullFilePath = os.path.join(filePath, fileName)
                if os.path.isdir(fullFilePath):     # fullFilePath 이 디렉토리라면 또 파고든다
                    search(fullFilePath, setFileName)
                else:
                    getFilePath(fullFilePath, setFileName)
        except PermissionError:
            print(fullFilePath, "해당 디렉터리는 접근 권한이 없습니다")
            pass

    def getFile():      # 파일가져오기
        pass

    def setFile():      # 파일수정하기
        pass

    def saveFile():     # 파일저장하기
        pass


filePath = input("찾는 파일의 경로를 입력하세요 : ")     # 파일경로
if os.path.isdir(dirName):   # 받은 입력이 올바른 경로일 시 다음 입력
    if os.path.isfile(dirName):
        print("파일 이름을 입력하였습니다. -> %s " % dirName)  # 파일이름
        setFileName = dirName
    else:
        setFileName = input("파일 이름을 입력하세요 : ")
