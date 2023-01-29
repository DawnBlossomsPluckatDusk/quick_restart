import os
import time
import subprocess
from selenium import webdriver
from msedge.selenium_tools import EdgeOptions,Edge
import logging

if __name__ == '__main__':

    # 屏蔽selenium的错误信息
    options = EdgeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    

    # 根据不同的edge版本更换driver
    driver = "./driver/msedgedriver.exe"
    DownloadDir = ""
    installers = "./installers"
    
     # 读取需要下载软件的网页
    ''' 由于搜索结果的不确定性，所以网页仍然需要收集
        同时，由于不同网页的下载元素不同，对应的元素位置也需要收集
    '''  
    urls = {}
    urlfile = open("./config/DownloadUrls.txt")
    xpathfile = open("./config/DownloadXpath.txt")
    url = urlfile.readline().replace("\n","")
    while url:
        xpath = xpathfile.readline().replace("\n","")
        urls[url] = xpath
        url = urlfile.readline().replace("\n","")

    for url,xpath in urls.items():

        # 初始化浏览器
        browser = Edge(driver,options=options)

        # 模拟浏览器进行网页的打开和点击模拟
        browser.get(url)
        element = browser.find_element("xpath",xpath)
        element.click()
        # 可优化选项：等待时长默认1分钟
        time.sleep(60)

        # 关闭浏览器
        browser.quit()

    # 获取用户安装文件夹

    f = os.popen("whoami")
    DownloadDir = "C:\\Users\\" + f.readline().replace("\n","").split("\\")[-1] + "\\Downloads\\"


    # 打开安装文件进行安装
    for file in os.listdir(DownloadDir):
        # 可优化选项
        # 需要将安装包移动到当前目录才能正常使用
        # 目前采用手动安装的方式进行
        print(file)
        if file.endswith(".exe") or file.endswith(".msi") or file.endswith(".EXE"):
            subprocess.call("powershell mv " + DownloadDir + file + " " + installers)
            
            install = subprocess.Popen(installers+"/"+file)
            
            # 等待安装完成
            install.wait()

            # 手动结束
            install.kill()

    # 清理安装包
    for file in os.listdir(installers):
        if file.endswith(".exe") or file.endswith(".msi") or file.endswith(".EXE"):
            os.remove(installers+"/"+file) 
