import os

class DirectoryHandler:
    def __init__(self, searchStr):
        self.searchStr = searchStr
        self.__BASE_DIR = './GoogleImages'


    def setBaseDir(self, baseDir):
        self.__BASE_DIR = baseDir

    def getBaseDir(self):
        return self.__BASE_DIR

    def getPath(self):
        try:
            return self.__PATH
        except Exception as e:
            target_path = self.__BASE_DIR
            return os.path.join(target_path, '_'.join(self.searchStr.lower().split(' ')))

    def setPath(self, path=''):
        try:
            if path:
                self.__PATH = path
            else:
                self.__PATH = self.getPath()
        except Exception as e:
            print(str(e))

    def isPathExist(self):
        try:
            return os.path.exists(self.getPath())
        except Exception as e:
            print(str(e))

    def createPath(self):
        try:
            if not self.isPathExist():
                os.makedirs(self.getPath())
        except Exception as e:
            print(str(e))