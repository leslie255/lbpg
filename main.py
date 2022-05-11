import os
from os.path import join as pathjoin
from os import mkdir as mkdir

from markdown import markdown as mdToHTML
from htmlobj import *
import fileIO
from fileIO import fopen as open

class HomePage:
    def __init__(self, pageTemplatePath, itemTemplatePath) -> None:
        self.__itemTexts = []
        self.html = HTMLObject(pageTemplatePath)
        self.__itemTemplatePath = itemTemplatePath
    
    def addSubpage(self, urlFull: str, urlDisplay: str, title: str, date: str) -> None:
        itemHTML = HTMLObject(self.__itemTemplatePath)
        itemHTML.fillItem("URL_FULL", urlFull)
        itemHTML.fillItem("URL_DISPLAY", urlDisplay)
        itemHTML.fillItem("TITLE", title)
        itemHTML.fillItem("DATE", date)
        self.__itemTexts.append(itemHTML.safeGetText())

    def generateText(self) -> str:
        self.html.fillItemMultiple("ARTICLE_LIST", self.__itemTexts)
        return self.html.safeGetText()

def genTargetDirs(targetdir: str) -> None:
    if os.path.exists(targetdir):
         os.system("rm -r "+targetdir)
    mkdir(targetdir)
    targetresdir = pathjoin(targetdir, "res/")
    mkdir(targetresdir)
    
    resdir = os.path.abspath("res/")
    os.system("cp -rf "+resdir+"/* "+targetdir)

def main():
    homePage = HomePage("templates/home/index", "templates/home/blogitem")
    homePage.addSubpage("posts/demo.html", "posts/demo.html", "Demo Article", "2022/05/12")

    demoArticleContent = fileIO.getText("articles/demo.md")

    articleBody = mdToHTML(demoArticleContent)
    articleHTML = HTMLObject("templates/article/article")
    articleHTML.fillItem("CSS_PATH", "../style.css")
    articleHTML.fillItem("TITLE", "Demo Article")
    articleHTML.fillItem("CONTENT", articleBody)
    articleHTML.fillItem("HOMEPAGE_PATH", "../index.html")

    targetdir = os.path.abspath("generated/")
    genTargetDirs(targetdir)
    
    indexhtmlFile = open(pathjoin(targetdir, "index.html"), "w+")
    indexhtmlFile.write(homePage.generateText())

    postsdir = os.path.join(targetdir, "posts/")
    mkdir(postsdir)
    articlehtmlFile = open(pathjoin(postsdir, "demo.html"), "w+")
    articlehtmlFile.write(articleHTML.safeGetText())

    fileIO.closeAllOpenedFiles()

main()

