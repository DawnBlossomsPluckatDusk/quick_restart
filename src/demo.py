import os
import subprocess
f = os.popen("whoami")
DownloadDir = "C:\\Users\\" + f.readline().replace("\n","").split("\\")[-1] + "\\Downloads\\"
installers = "./installers"

# 打开安装文件进行安装
# for file in os.listdir(installers):
#     # 可优化选项
#     # 需要将安装包移动到当前目录才能正常使用
#     # 目前采用手动安装的方式进行
#     print(file)
#     if file.endswith(".exe") or file.endswith(".msi") or file.endswith(".EXE"):
#         # subprocess.call("powershell mv " + DownloadDir + file + " " + installers)
#         install = subprocess.Popen(installers+"/"+file)
            
#         # 等待安装完成
#         install.wait()
#         install.kill() 

# 清理安装包
for file in os.listdir(installers):
    if file.endswith(".exe") or file.endswith(".msi"):
       os.remove(installers+"/"+file)
    