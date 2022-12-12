import subprocess
import os

SHELL_COMMAND = "powershell wget -O"
INSTALL_DIR = "./installers"

if __name__ == '__main__':
    
    # 1. 获取下载列表
    filesURL = []
    filesName = []
    with open("./DownloadLists.txt") as f:
        text = f.readline().replace("\n","")
        while text:
            filesURL.append(text)
            filesName.append(filesURL[-1].split('/')[-1])
            text = f.readline().replace("\n","")

    # 2. 下载对应的文件
    for index in range(len(filesURL)):
        cmd = SHELL_COMMAND + " ./installers/" + filesName[index] + " " + filesURL[index]
        subprocess.call(cmd,shell=True)
    
    # 3. 安装下载的文件
    for name in filesName:
        subprocess.Popen(INSTALL_DIR+name)
    
    # 4. 清理安装包
    for f in os.listdir(INSTALL_DIR):
        os.remove(os.path.join(INSTALL_DIR,f))
    