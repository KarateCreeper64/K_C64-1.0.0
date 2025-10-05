from misc import create


def basicArmorSet(filePath, setName, armorMaterial, armorRenderer):
    content = \
(f"""{{
    "armor_material": "kc64:{armorMaterial}",
    "chest": {{
        "item_name": "{setName}_chestplate",
        "max_stack_size": 1,
        "is_fire_resistant": false,
        "armor_renderer": "kc64:{armorRenderer}/chest"
    }},
    "legs": {{
        "item_name": "{setName}_leggings",
        "max_stack_size": 1,
        "is_fire_resistant": false,
        "armor_renderer": "kc64:{armorRenderer}/legs"
    }},
    "feet": {{
        "item_name": "{setName}_boots",
        "max_stack_size": 1,
        "is_fire_resistant": false,
        "armor_renderer": "kc64:{armorRenderer}/boots"
    }},
    "head": {{
        "item_name": "{setName}_helmet",
        "max_stack_size": 1,
        "is_fire_restant": false,
        "armor_renderer": "kc64:{armorRenderer}/helmet"
    }}
}}""")
    create(filePath)
    file = open(filePath, "w")
    file.write(content)

def simpleArmorRenderers(filePath, setName):
    create(f"{filePath}/boots.json")
    boots = open(f"{filePath}/boots.json", "w")
    (boots.write
(f"""{{
    "textures": "kc64:textures/models/armor/{setName}/boots.png",
    "model_layers": "palladium:humanoid#suit"
}}"""))
    create(f"{filePath}/chest.json")
    chest = open(f"{filePath}/chest.json", "w")
    (chest.write
(f"""{{
    "textures": {{
        "normal": "kc64:textures/models/armor/{setName}/chest.png",
        "slim": "kc64:textures/models/armor/{setName}/chest_slim.png"
     }},
    "model_layers": {{
        "normal": "palladium:humanoid#suit",
        "slim": "palladium:humanoid#suit_slim"
    }}
}}"""))
    create(f"{filePath}/legs.json")
    legs = open(f"{filePath}/legs.json", "w")
    (legs.write
(f"""{{
    "textures": "kc64:textures/models/armor/{setName}/legs.png",
    "model_layers": "palladium:humanoid#suit"
}}"""))
    create(f"{filePath}/helmet.json")
    helmet = open(f"{filePath}/helmet.json", "w")
    (helmet.write
(f"""{{
    "textures": "kc64:textures/models/armor/{setName}/helmet.png",
    "model_layers": "palladium:humanoid#suit"
}}"""))