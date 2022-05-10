import re
import os
import shutil

class HTMLObject:
    def __init__(self, templateName: str) -> None:
        self.text = ""
        self.items = {}
        f = open(templateName+".html.txt", "r")
        lines = f.readlines()
        for line in lines:
            self.text += line
        
        f = open(templateName+".items.txt", "r")
        lines = f.readlines()
        for line in lines:
            self.items[line.replace('\n', '')] = False

    def fillItem(self, itemName: str, text: str) -> None:
        if itemName not in self.items:
            print("trying to replace an unexisted item: "+itemName)
            exit(1)
        self.items[itemName] = True
        replaced = re.sub("{" + itemName + "}", text, self.text)
        self.text = replaced

    # check if all items are filled
    def safeCheck(self) -> bool:
        for name in self.items:
            if self.items[name] == False:
                return False
        return True

    # returns text only if all items are filled
    def safeGetText(self) -> str:
        if self.safeCheck():
            return self.text
        else:
            print("trying to access text without filling all items")
            print("items not filled:")
            for name in self.items:
                if self.items[name] == False:
                    print(name)
            exit(1)

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

