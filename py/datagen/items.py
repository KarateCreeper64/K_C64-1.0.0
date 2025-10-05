import json
from misc import create

def simpleItemModel(filePath, itemName):
    content = \
(f"""{{
    "parent": "minecraft:item/generated",
    "textures": {{
        "layer0": "kc64:item/{itemName}"
    }}
}}""")
    create(filePath)
    file = open(filePath, "w")
    file.write(content)

def blockItemModel(filePath, blockName):
    content = \
(f"""{{
    "parent": "kc64:block/{blockName}",
}}""")
    create(filePath)
    file = open(filePath, "w")
    file.write(content)

tabItems = []

def addTabItem(itemName):
    global tabItems
    tabItems.append(f"kc64:{itemName}")

def getCreativeTab(icon, title):
    return \
(f"""{{
    "icon": "kc64:{icon}",
    "title": "{title}",
    "items": {json.dumps(tabItems)}
 }}""")