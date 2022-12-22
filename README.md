# quick_restart

主要用于重装系统后的快速回复工作环境，安装常用软件

## 项目结构

├─config                            配置文件，保存下载的`url`和`xpath`
│      DownloadLists.txt            `exe`文件的`url`，`install_simple.py`使用
│      DownloadUrls.txt             软件的下载`url`，`spider_selenium.py`使用
│      DownloadXpath.txt            软件的下载元素的`xpath`，`spider_selenium.py`使用
│      
├─driver                            浏览器驱动，需要根据使用的浏览器进行更改，默认使用`edge`
│      chromedriver.exe
│      msedgedriver.exe
│
├─installers                        存放安装包的临时文件，安装完成后会清理安装包
├─src                               源代码
|      demo.py                      测试功能代码
|      install_simple.py            简易版，需要获取`exe`的`url`，一些软件的下载并不支持
|      spider_selenium.py           爬虫版本，通过使用`selenium`模拟点击实现
├─README.back.md                    旧文档
└─README.md                         用户手册


## 快速使用

1. 下载使用浏览器的`driver`，并移动到`driver`目录
2. 在`config`文件夹下的`DownloadUrls.txt`中添加需要的软件的下载界面`url` **该页面需要存在可以直接点击下载的元素，不支持再次跳转到另一个页面**
3. 在`config`文件夹下的`Downloadxpath.txt`中添加下载元素的`xpath`   **确保`xpath`和`url`是一一对应的**
4. 修改`spider_selenium.py`文件
   + 修改`driver`变量
5. 使用管理员权限运行

## 代码逻辑

`install_simple`逻辑简单，使用`wget`命令进行下载，使用`subprocess`模块进行安装

`spider_selenium`使用`selenium`模拟浏览器操作，进行软件的自动下载

`pipeline`:

1. 获取软件的`url`和下载元素的`xpath`
2. 使用`selenium`模拟浏览器打开`url`
3. 模拟浏览器根据`xpath`寻找下载元素
4. 模拟浏览器点击下载元素
5. 结束下载，将下载文件移动到`installers`
6. 安装
7. 清理安装包

**所有操作都要在管理员权限下进行**

## 问题合集

记录使用中的问题


## TODO

- [ ]    软件的自动安装
- [ ]    环境的集成，提供需要的环境