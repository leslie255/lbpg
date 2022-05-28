import sys
import os
from os import mkdir as mkdir
from os import path as p

from htmlobj import *
from pages import *
from cmdio import *

def printHelp():
    logClean("usage:")
    logClean(sys.argv[0] + " -t / --target [target_dir]")
    logClean(sys.argv[0] + " -s / --source [source_dir]")
    logClean(sys.argv[0] + " -h / --help   print this information")

def genTargetDirs(targetdir: str) -> None:
    if os.path.exists(targetdir):
        if askYesOrNo("Target directory exists, delete? (y/N):", default=False):
            os.system("rm -r "+targetdir)
        else:
            exit(2)

    mkdir(targetdir)
    targetresdir = p.join(targetdir, "res/")
    mkdir(targetresdir)
    
    log("copying resources...", end="")
    resdir = os.path.abspath("res/")
    os.system("cp -rf "+resdir+"/* "+targetdir)
    logClean("ok")

def loadArticlesInDir(articlesDir: str) -> list[Article]:
    articles = []
    for file in os.listdir(articlesDir):
        lol = os.path.splitext(file)
        filename = lol[0]
        fileext = lol[1]
        if fileext != ".json":
            continue
        path = p.join(articlesDir, filename)
        log("loading "+path+"...", end="")
        articles.append(Article(path))
        logClean("ok")
    return articles

def main():
    targetdir = os.path.abspath("generated/")
    srcdir = os.path.abspath(".")

    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        argL = arg.lower()
        if argL == "-t" or argL == "--target":
            targetdir = sys.argv[i+1]
            i += 1
        elif argL == "-s" or argL == "--source":
            srcdir = sys.argv[i+1]
            i+= 1
        elif argL == "-h" or argL == "-h":
            printHelp()
            exit(0)
        else:
            logErr("Unknown argument: "+arg)
            printHelp()
            exit(3)
        i += 1

    genTargetDirs(targetdir)
    postsdir = p.join(targetdir, "posts/")
    mkdir(postsdir)

    homePage = HomePage(p.join(srcdir, "templates/home/index"), p.join(srcdir, "templates/home/blogitem"))

    for article in loadArticlesInDir(p.join(srcdir, "articles")):
        article.saveToDir(postsdir)
        homePage.addSubpageOfArticle(article)
    log("all articles generated")
    log("generating homepage...", end="")
    homePage.writeToFile(p.join(targetdir, "index.html"))
    logClean("ok")

    log("all generated, wrapping up...")
    fileIO.closeAllOpenedFiles()

main()

