from os import path as p
from markdown import markdown as mdToHTML
import json

import fileIO
from htmlobj import *
from fileIO import fopen as open
from cmdio import *

class Article:
    def __init__(self, path) -> None:
        jsonContent = fileIO.getText(path+".json")
        mdContent = fileIO.getText(path+".md")

        loadedJson = json.loads(jsonContent)
        self.id = loadedJson["id"]
        self.fileName = self.id+".html"
        self.dateY = loadedJson["date_year"]
        self.dateM = loadedJson["date_month"]
        self.dateD = loadedJson["date_day"]
        self.dateStr = str(self.dateY) +'/'+ str(self.dateM) +'/'+ str(self.dateD)
        self.title = loadedJson["title"]

        bodyHTML = mdToHTML(mdContent)
        htmlObj = HTMLObject("templates/article/article")
        htmlObj.fillItem("CSS_PATH", "../style.css")
        htmlObj.fillItem("HOMEPAGE_PATH", "../index.html")
        htmlObj.fillItem("TITLE", self.title)
        htmlObj.fillItem("CONTENT", bodyHTML)
        self.htmlText = htmlObj.safeGetText()

    def saveToDir(self, dirPath: str) -> None:
        open(p.join(dirPath, self.fileName), "w+").write(self.htmlText)

class HomePage:
    def __init__(self, pageTemplatePath, itemTemplatePath) -> None:
        self.__itemTexts = []
        self.html = HTMLObject(pageTemplatePath)
        self.__itemTemplatePath = itemTemplatePath
        self.hasGenerated = False
    
    def addSubpageLink(self, urlFull: str, urlDisplay: str, title: str, date: str) -> None:
        if self.hasGenerated:
            logErr("trying to add a subpage to homepage after text has already generated")
            exit(1)
        itemHTML = HTMLObject(self.__itemTemplatePath)
        itemHTML.fillItem("URL_FULL", urlFull)
        itemHTML.fillItem("URL_DISPLAY", urlDisplay)
        itemHTML.fillItem("TITLE", title)
        itemHTML.fillItem("DATE", date)
        self.__itemTexts.append(itemHTML.safeGetText())

    def addSubpageOfArticle(self, article: Article) -> None:
        if self.hasGenerated:
            logErr("trying to add an aricle subpage to homepage after text has already generated")
            exit(1)
        url = "posts/"+article.id+".html"
        self.addSubpageLink(url, url, article.title, article.dateStr)

    def generateText(self) -> str:
        if self.hasGenerated:
            return self.html.text
        self.hasGenerated = True
        self.html.fillItemMultiple("ARTICLE_LIST", self.__itemTexts)
        return self.html.safeGetText()

    def writeToFile(self, path: str) -> None:
        open(path, "w+").write(self.generateText())


