import re

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


