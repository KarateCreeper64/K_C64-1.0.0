from misc import create

def simpleBlockModel(filePath, blockName):
    content = \
(f"""{{
    "parent": "minecraft:block/cube_all",
    "textures": {{
         "layer0": "kc64:block/{blockName}"
    }}
}}""")
    create(filePath)
    file = open(filePath, "w")
    file.write(content)

def simpleBlockState(filePath, blockName):
    content = \
(f"""{{
    "variants": {{
        "": {{
            "model": "kc64:block/{blockName}"
        }}
    }}
}}""")
    create(filePath)
    file = open(filePath, "w")
    file.write(content)