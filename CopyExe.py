import os
import shutil
import subprocess
import time
from pathlib import Path
import sys

class CopyExe(object):
    def __init__(self):
        pass
    
    def copyAllFiles(self, src, dest, exceptFile):
        #src:原文件夹；dest:目标文件夹
        if Path(src).exists() == False:
            print("file or fodder is not exist...")
            return
        for files in os.listdir(src):
            name = os.path.join(src, files)
            back_name = os.path.join(dest, files)
            if os.path.isfile(name):
                if name in exceptFile:
                    continue
                shutil.copy(name, back_name)
            else:
                if not os.path.isdir(back_name):
                    os.makedirs(back_name)
                self.copyAllFiles(name, back_name, exceptFile)

    #删除文件夹下的所有文件和子文件夹
    def delFileAndFolder(self, filepath):
        if Path(filepath).exists() == False:
            print("file or fodder is not exist...")
            return
        del_list = os.listdir(filepath)
        for f in del_list:
            file_path = os.path.join(filepath, f)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        os.rmdir(filepath)

    #重命名单个文件
    def renameFile(self, filePath, newFileName):
        if Path(filePath).exists() == False:
            print("file or fodder %s is not exist..."%(filePath))
            return
        path, name = os.path.split(filePath)
        if os.path.isfile(filePath):
            os.rename(filePath, os.path.join(path, newFileName))
            print("delete file %s successs..."%(filePath))

    #删除单个文件
    def delFile(self, filePath):
        if Path(filePath).exists() == False:
            print("file or fodder %s is not exist..."%(filePath))
            return
        if os.path.isfile(filePath):
            os.remove(filePath)
            print("delete file %s successs..."%(filePath))

if __name__ == '__main__':    
    copyExe = CopyExe()
    infoList = sys.argv
    # with open("test.txt","a") as f:
    #     for t in infoList:
    #         f.write(t)
    if len(infoList) == 7:
        destPath = infoList[1]
        srcPath = infoList[2]
        md5File = infoList[3]
        md55File = infoList[4]
        exceptFileList = infoList[5].split(',')
        exePath = infoList[6]
        time.sleep(0.5)
        copyExe.copyAllFiles(srcPath, destPath, exceptFileList)
        time.sleep(0.1)
        copyExe.delFileAndFolder(srcPath)
        copyExe.delFile(md5File)
        copyExe.renameFile(md55File, md5File)
        copyExe.delFile(md55File)
        if Path(exePath).exists() == True:
            subprocess.Popen(exePath)
            print("open exe")
        else:
            print("file or fodder %s is not exist..."%(exePath))