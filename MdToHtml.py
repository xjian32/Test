#coding=utf-8

import os
import sys
from bs4 import BeautifulSoup
import markdown

class MarkdownToHtml:

    headTag = '<head><meta charset="utf-8" /></head>'

    # 构造方法
    def __init__(self, cssFilePath = None):
        if cssFilePath != None:
            self.genStyle(cssFilePath)

    # 读取外部css文件存放在headTag中
    def genStyle(self, cssFilePath):
        # with as 文件用完后会自动关闭
        with open(cssFilePath, 'r') as f:
            cssString = f.read()
        self.headTag = self.headTag[:-7] + '<style type="text/css">{}</style>'.format(cssString) + self.headTag[-7:]

    # 编译Markdown输出HTML
    # sourceFilePath(源码路径)
    # destinationDirectory（输出文件目录，可选）
    # outputFileName（输出文件名称，可选）
    def markdownToHtml(self, sourceFilePath, destinationDirectory = None, outputFileName = None):

        '''
        os.path.abspath()  将参数路径转为绝对路径并返回
        os.path.dirname()  获得参数路径的目录部分并返回（如 "\home\a.txt" 为参数，返回 "\home"）
        os.path.basename() 返回参数路径字符串中的完整文件名，文件名+后缀名
        os.path.splitext() 将参数转换为包含文件名和后缀名两个元素的元组并返回
        '''

        # 未定义输出目录则将源文件目录作为输出目录
        if not destinationDirectory:
            destinationDirectory = os.path.dirname(os.path.abspath(sourceFilePath))
        # 未定义输出文件名称，则沿用输入文件名
        if not outputFileName:
            outputFileName = os.path.splitext(os.path.basename(sourceFilePath))[0] + '.html'
        # 对destinationDirectory不是以'/'结尾时进行处理
        if destinationDirectory[-1] != '/':
            destinationDirectory += '/'

        with open(sourceFilePath, 'r', encoding='utf-8') as f:
            markdownText = f.read()

        # 编译出html5文本
        rawHtml = self.headTag + markdown.markdown(markdownText, output_format='html5')
        # 把rawHtml中的html代码用BeautifulSoup格式化
        #beautifyHtml = BeautifulSoup(rawHtml, 'html5lib').prettify()
        # 将beautifyHtml写入文件
        with open(destinationDirectory + outputFileName, 'w', encoding='utf-8') as f:
            f.write(rawHtml)

if __name__ == "__main__":
    mth = MarkdownToHtml()

    argv = sys.argv[1:]
    outputDirectory = None
    # index()函数用于在列表中找出匹配项的索引位置，返回值为int型
    if '-s' in argv:
        cssArgIndex = argv.index('-s') + 1
        cssFilePath = argv[cssArgIndex]
        # 判断样式表文件路径是否有效
        if not os.path.isfile(cssFilePath):
            print('Invalid Path :' + cssFilePath)
            sys.exit()
        mth.genStyle(cssFilePath)
        # 删除列表中元素
        argv.pop(cssArgIndex)
        argv.pop(cssArgIndex-1)

    if '-o' in argv:
        dirArgIndex = argv.index('-o') + 1
        outputDirectory = argv[dirArgIndex]
        # os.path.isdir() 检测参数是否为目录，返回True、False
        if not os.path.isdir(outputDirectory):
            print('Invalid Directory:' + outputDirectory)
            sys.exit()
        argv.pop(dirArgIndex)
        argv.pop(dirArgIndex-1)

    # 列表argv中的元素均为源文件路径
    # 遍历所有源文件路径
    for filePath in argv:
        # 判断路径是否有效
        # os.path.isfile() 检测参数是否为文件路径，返回True、False
        if os.path.isfile(filePath):
            mth.markdownToHtml(filePath, outputDirectory)
        else:
            print('Invalid Path:' + filePath)















