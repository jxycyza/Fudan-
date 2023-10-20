使用教程：Fudan 课程评估自动化脚本

本教程介绍如何在本地机器上设置和运行Fudan课程评估的自动化脚本。

1. 预备条件

确保您的计算机已经安装了以下软件：

- Python (建议3.6以上版本)

2. 安装所需的Python库

在命令行或终端上运行以下命令，安装必需的Python库：

`pip3 install selenium`

3. 下载驱动程序

此脚本使用Selenium和Edge浏览器。您需要下载与您的浏览器版本相匹配的驱动程序。然后将驱动程序的路径添加到系统的`PATH`环境变量中。

- [Microsoft Edge Driver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

4. 配置账号密码

打开脚本文件，找到以下行：

```python
usrname = ''
password = ''
```

将上述行中的`usrname`和`password`的值更改为您自己的账号和密码。

5. 运行脚本

在命令行或终端中，进入代码库的目录，并运行脚本：

```
python3 work.py
```


6. 注意事项

- 请确保在使用此脚本时遵守相关的使用政策和道德标准。
- 此脚本主要用于学习和研究目的，请不要用于任何可能违反相关规定的活动。
- 最终解释权由本账号所有

结束

至此，您应该已经成功地在您的计算机上设置并运行了Fudan课程评估的自动化脚本。如果您在使用过程中遇到任何问题，请在issue中提问。
