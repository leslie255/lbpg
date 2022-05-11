import os
from os.path import join as pathjoin
from os import mkdir as mkdir

import fileIO
from htmlobj import *
from fileIO import fopen as open
from pages import *

def genTargetDirs(targetdir: str) -> None:
    if os.path.exists(targetdir):
         os.system("rm -r "+targetdir)
    mkdir(targetdir)
    targetresdir = pathjoin(targetdir, "res/")
    mkdir(targetresdir)
    
    print("copying resources...", end="")
    resdir = os.path.abspath("res/")
    os.system("cp -rf "+resdir+"/* "+targetdir)
    print("ok")

def loadArticlesInDir(articlesDir: str) -> list[Article]:
    articles = []
    for file in os.listdir(articlesDir):
        lol = os.path.splitext(file)
        filename = lol[0]
        fileext = lol[1]
        if fileext != ".json":
            continue
        path = pathjoin(articlesDir, filename)
        print("loading "+path+"...", end="")
        articles.append(Article(path))
        print("ok")
    return articles

def main():
    targetdir = os.path.abspath("generated/")
    genTargetDirs(targetdir)
    postsdir = pathjoin(targetdir, "posts/")
    mkdir(postsdir)

    homePage = HomePage("templates/home/index", "templates/home/blogitem")

    for article in loadArticlesInDir("articles"):
        article.saveToDir(postsdir)
        homePage.addSubpageOfArticle(article)
    print("all articles generated")
    print("generating homepage...", end="")
    homePage.writeToFile(pathjoin(targetdir, "index.html"))
    print("ok")

    print("all generated, wrapping up...")
    fileIO.closeAllOpenedFiles()

main()

