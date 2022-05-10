import os
from htmlobj import *

def main():
    item0 = HTMLObject("templates/home/blogitem")
    item0.fillItem("URL_FULL", "http://github.com/p-z-l/nvim-config")
    item0.fillItem("TITLE", "My Epic NeoVim Configuration")
    item0.fillItem("URL_DISPLAY", "github.com/p-z-l/nvim-config")
    item0.fillItem("DATE", "2022/05/10")
    item1 = HTMLObject("templates/home/blogitem")
    item1.fillItem("URL_FULL", "http://github.com/p-z-l/nvim-config")
    item1.fillItem("TITLE", "My Epic NeoVim Configuration (another one!)")
    item1.fillItem("URL_DISPLAY", "github.com/p-z-l/nvim-config")
    item1.fillItem("DATE", "2022/05/10")
    homePage = HTMLObject("templates/home/index")
    homePage.fillItem("ARTICLE_LIST", item0.safeGetText()+item1.safeGetText())

    targetdir = os.path.abspath("generated/")
    targetresdir = os.path.join(targetdir, "res/")
    if os.path.exists(targetdir):
        os.system("rm -r "+targetdir)
    os.mkdir(targetdir)
    os.mkdir(targetresdir)
    
    resdir = os.path.abspath("res/")
    os.system("cp -rf "+resdir+"/* "+targetdir)
    
    indexhtmlFile = open(os.path.join(targetdir, "index.html"), "w+");
    indexhtmlFile.write(homePage.safeGetText())

main()

