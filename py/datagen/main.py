import sys, os
sys.path.append(os.path.dirname(__file__))

import json
import items
import blocks
import armor_sets
from pathlib import Path
from misc import create

filePath = Path(__file__).resolve().parent
gitPath = filePath.parent.parent
configPath = filePath / "config"

itemFile = open(configPath / "items.json")
blockFile = open(configPath / "blocks.json")

pItems = json.loads(itemFile.read())
pBlocks = json.loads(blockFile.read())

simpleItems = pItems["item"]
armorSets = pItems["armor_set"]
armorRenderers = pItems["armor_renderer"]

simpleBlocks = pBlocks["block"]
cubeallBlocks = pBlocks["cubeall_block_model"]

def processItems(item):
    for i in item:
        items.simpleItemModel(
            gitPath / "assets" / "kc64" / "models" / "item" / f"{i}.json",
            i
        )
        items.addTabItem(i)

processItems(simpleItems)

for armor_set in armorSets:
    boots = f"{armor_set['name']}_boots"
    chest = f"{armor_set['name']}_chest"
    legs = f"{armor_set['name']}_legs"
    helmet = f"{armor_set['name']}_helmet"
    processItems([boots, chest, legs, helmet])
    armor_sets.basicArmorSet(
        gitPath / "addon" / "kc64" / "suit_sets" / f"{armor_set['name']}.json",
        armor_set["name"],
        armor_set["material"],
        armor_set["renderer"]
    )

for armor_renderer in armorRenderers:
    armor_sets.simpleArmorRenderers(
        gitPath / "assets" / "kc64" / "palladium" / "armor_renderers" / f"{armor_renderer}",
        armor_renderer
    )

for block_state in simpleBlocks:
    blocks.simpleBlockState(
        gitPath / "assets" / "kc64" / "blockstates" / f"{block_state}.json",
        block_state
    )

for block in cubeallBlocks:
    blocks.simpleBlockModel(
        gitPath / "assets" / "kc64" / "models" / "block" / f"{block}.json",
        block
    )

create(gitPath / "addon" / "kc64" / "creative_mode_tabs" / "superheroes.json")
open(gitPath / "addon" / "kc64" / "creative_mode_tabs" / "superheroes.json", "wt").write(items.getCreativeTab("omni_helmet", "KC_64's Superheroes"))