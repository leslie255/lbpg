import re

class HTMLObject:
    def __init__(self, templateName: str) -> None:
        self.__name = templateName
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

    def fillItemMultiple(self, itemName: str, texts: list[str]) -> None:
        if itemName not in self.items:
            print("trying to replace an unexisted item: "+itemName)
            exit(1)
        self.items[itemName] = True
        fullText = ""
        for text in texts:
            fullText += text
        replaced = re.sub("{" + itemName + "}", fullText, self.text)
        self.text = replaced

    def safeCheck(self) -> bool:
        # check if all items are filled
        for name in self.items:
            if self.items[name] == False:
                return False
        return True

    def safeGetText(self) -> str:
        # returns text only if all items are filled
        # otherwise exists with error information
        if self.safeCheck():
            return self.text
        else:
            print("HTMLObject.safeGetText(...):\ntrying to access text of "+self.__name+" without filling all items")
            print("items not filled:")
            print(self.items)
            for name in self.items:
                if self.items[name] == False:
                    print(name)
            exit(1)

