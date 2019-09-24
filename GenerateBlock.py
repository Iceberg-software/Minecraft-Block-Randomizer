import random
from PIL import Image
import numpy as np
import colorsys
import os
import random
import progressbar
from titlecase import titlecase
import settings

def selectRandomFile(dir):
    return random.choice(os.listdir(dir))

def hueChange(filename, img, hue, brightness, saturation):

    width, heigth = img.size

    sat_avg = 0
    brg_avg = 0
    pixels = 0

    if "pickaxe" in filename:
        for x in range(width):
            for y in range(heigth):
                r,g,b,a = img.getpixel((x,y))
                if a == 255:
                    if not (x,y) in settings.pickaxe_pixels():
                        pixels = pixels + 1
                        h,s,v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
                        sat_avg += s + saturation
                        brg_avg += v + brightness
                        rgb = colorsys.hsv_to_rgb(hue/360, max(min(s + saturation, 1), 0), max(min(v + brightness, 1), 0))
                        r, g, b = [int(x*255.) for x in rgb]
                        img.putpixel((x,y),(r,g,b))
        #print("Average saturation: {} : Average brightness: {}".format(max(min((sat_avg/pixels)*100, 100), 0), max(min((sat_avg/pixels)*100, 100), 0)))
    elif "sword" in filename:
        for x in range(width):
            for y in range(heigth):
                r,g,b,a = img.getpixel((x,y))
                if a == 255:
                    if not (x,y) in settings.sword_pixels():
                        pixels = pixels + 1
                        h,s,v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
                        sat_avg += s + saturation
                        brg_avg += v + brightness
                        rgb = colorsys.hsv_to_rgb(hue/360, max(min(s + saturation, 1), 0), max(min(v + brightness, 1), 0))
                        r, g, b = [int(x*255.) for x in rgb]
                        img.putpixel((x,y),(r,g,b))
        #print("Average saturation: {} : Average brightness: {}".format(max(min((sat_avg/pixels)*100, 100), 0), max(min((sat_avg/pixels)*100, 100), 0)))
    elif "shovel" in filename:
        for x in range(width):
            for y in range(heigth):
                r,g,b,a = img.getpixel((x,y))
                if a == 255:
                    if not (x,y) in settings.shovel_pixels():
                        pixels = pixels + 1
                        h,s,v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
                        sat_avg += s + saturation
                        brg_avg += v + brightness
                        rgb = colorsys.hsv_to_rgb(hue/360, max(min(s + saturation, 1), 0), max(min(v + brightness, 1), 0))
                        r, g, b = [int(x*255.) for x in rgb]
                        img.putpixel((x,y),(r,g,b))
        #print("Average saturation: {} : Average brightness: {}".format(max(min((sat_avg/pixels)*100, 100), 0), max(min((sat_avg/pixels)*100, 100), 0)))
    elif "hoe" in filename:
        for x in range(width):
            for y in range(heigth):
                r,g,b,a = img.getpixel((x,y))
                if a == 255:
                    if not (x,y) in settings.hoe_pixels():
                        pixels = pixels + 1
                        h,s,v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
                        sat_avg += s + saturation
                        brg_avg += v + brightness
                        rgb = colorsys.hsv_to_rgb(hue/360, max(min(s + saturation, 1), 0), max(min(v + brightness, 1), 0))
                        r, g, b = [int(x*255.) for x in rgb]
                        img.putpixel((x,y),(r,g,b))
        #print("Average saturation: {} : Average brightness: {}".format(max(min((sat_avg/pixels)*100, 100), 0), max(min((sat_avg/pixels)*100, 100), 0)))
    elif "axe" in filename:
        for x in range(width):
            for y in range(heigth):
                r,g,b,a = img.getpixel((x,y))
                if a == 255:
                    if not (x,y) in settings.axe_pixels():
                        pixels = pixels + 1
                        h,s,v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
                        sat_avg += s + saturation
                        brg_avg += v + brightness
                        rgb = colorsys.hsv_to_rgb(hue/360, max(min(s + saturation, 1), 0), max(min(v + brightness, 1), 0))
                        r, g, b = [int(x*255.) for x in rgb]
                        img.putpixel((x,y),(r,g,b))
        #print("Average saturation: {} : Average brightness: {}".format(max(min((sat_avg/pixels)*100, 100), 0), max(min((sat_avg/pixels)*100, 100), 0)))
    else:
        for x in range(width):
            for y in range(heigth):
                r,g,b,a = img.getpixel((x,y))
                if a == 255:
                    pixels = pixels + 1
                    h,s,v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
                    sat_avg += s + saturation
                    brg_avg += v + brightness
                    rgb = colorsys.hsv_to_rgb(hue/360, max(min(s + saturation, 1), 0), max(min(v + brightness, 1), 0))
                    r, g, b = [int(x*255.) for x in rgb]
                    img.putpixel((x,y),(r,g,b))
        #print("Average saturation: {} : Average brightness: {}".format(max(min((sat_avg/pixels)*100, 100), 0), max(min((sat_avg/pixels)*100, 100), 0)))
    
    return(img)

def camelCase(st):
    output = ''.join(x for x in st.title() if x.isalnum())
    return output[0].lower() + output[1:]

def fileLen(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i-1

def writeJavaBlockImports(file):
    file.write("package com.iceberg.randoblock.blocks; \n\n")
    file.write("import net.minecraft.block.Block; \n")
    file.write("import net.minecraft.block.SoundType; \n")
    file.write("import net.minecraft.block.material.Material; \n\n")

def writeJavaItemImports(file):
    file.write("package com.iceberg.randoblock.blocks; \n\n")
    file.write("import com.iceberg.randoblock.Main; \n")
    file.write("net.minecraft.item.Item; \n")

def CreateNewContent(amount):
    
    names = []
    for i in progressbar.progressbar(range(amount)):
        ## SETTINGS ##
        # ORE
        ORE_Y_LEVEL_MIN = random.randint(0,30)
        ORE_Y_LEVEL_MAX = random.randint(45,75)
        ORE_MINE_LEVEL = random.choice(settings.materials())
        ORE_SMELTABLE = random.choice((True,False))
        if ORE_SMELTABLE:
            ORE_DROP_COUNT = random.randint(1,2)
        else:
            ORE_DROP_COUNT = random.randint(1,6)

        # ITEM
        ITEM_DUNGEON = random.choice((True,False))
        ITEM_TEMPLE = random.choice((True,False))
        ITEM_STRONGHOLD = random.choice((True,False))
        ITEM_MINESHAFT = random.choice((True,False))
        ITEM_VILLAGE = random.choice((True,False))
        ITEM_MANSION = random.choice((True,False))
        ITEM_END_CITY = random.choice((True,False))
        ITEM_END_SHIP = random.choice((True,False))

        # CRAFTING
        CRAFTING_ARMOR = random.choice((True,False))
        CRAFTING_TOOLS = random.choice((True,False))
        CRAFTING_WEAPONS = random.choice((True,False))
        CRAFTING_TORCH = random.choice((True,False))
        CRAFTING_BLOCK = random.choice((True,False))

        # USE
        USE_FUEL = random.choice((True,False))
        USE_FOOD = random.choice((True,False))
        
        ## POPERTIES ##
        # WEAPON
        if CRAFTING_WEAPONS:
            USE_DURABILITY = random.choice(settings.materials())
            USE_DAMAGE = random.randint(1,20)
            USE_ATTACK_EFFECT_NPC = random.choices(settings.effects("ATTACK"), k=random.randint(0,3))
            USE_ATTACK_EFFECT_PLAYER = random.choices(settings.effects("ATTACK"), k=random.randint(0,3))
            USE_HOLDING_EFFECT = random.choices(settings.effects("PASSIVE"), k=random.randint(0,3))
            USE_ENCHANTMENT = random.choices(settings.sword_enchantments(random.choice(("UNDER_POWERED", "NORMAL", "OVER_POWERED"))), k=random.randint(0,3))
        
        
        fn = open("elementInfo/firstNames.txt")
        sn = open("elementInfo/secondNames.txt")
        ln = open("elementInfo/lastNames.txt")

        FULL_NAME = ""

        firstNames = fn.readlines()
        secondNames = sn.readlines()
        lastNames = ln.readlines()

        fn.close()
        sn.close()
        ln.close()

        firstName = random.randint(0,1)
        fourthName = random.randint(0,1)
        fifthName = random.randint(0,1)
        sixthName = random.randint(0,1)

        if firstName == 1:
            FULL_NAME += firstNames[random.randint(0,fileLen("elementInfo/firstNames.txt"))].replace("\n", "")

        FULL_NAME += secondNames[random.randint(0,fileLen("elementInfo/secondNames.txt"))].replace("\n", "")
        FULL_NAME += firstNames[random.randint(0,fileLen("elementInfo/firstNames.txt"))].replace("\n", "")

        if fourthName == 1:
            FULL_NAME += secondNames[random.randint(0,fileLen("elementInfo/secondNames.txt"))].replace("\n", "")

        if fifthName == 1:
            FULL_NAME += firstNames[random.randint(0,fileLen("elementInfo/firstNames.txt"))].replace("\n", "")

        if sixthName == 1:
            FULL_NAME += lastNames[random.randint(0,fileLen("elementInfo/lastNames.txt"))].replace("\n", "")

        #print("")
        #print(FULL_NAME)

        RAW = FULL_NAME
        ore = FULL_NAME + "_ore"

        modBlockFile = os.path.isfile("Complete/Code/java/{}.java".format("ModBlocks"))
        modItemFile = os.path.isfile("Complete/Code/java/{}.java".format("ModItems"))
        langFile = os.path.isfile("Complete/Code/lang/{}.json".format("en_US"))

        if os.path.isdir("Complete/{}".format(FULL_NAME)):
            continue
        if not os.path.isdir("Complete"):
            os.mkdir("Complete")
        if not os.path.isdir("Complete/Code"):
            os.mkdir("Complete/Code")
        if not os.path.isdir("Complete/Code/lang"):
            os.mkdir("Complete/Code/lang")
        if not os.path.isdir("Complete/Code/java"):
            os.mkdir("Complete/Code/java")
        os.mkdir("Complete/{}".format(FULL_NAME))
        os.mkdir("Complete/{}/Crafting".format(FULL_NAME))
        os.mkdir("Complete/{}/Crafting/Block".format(FULL_NAME))
        os.mkdir("Complete/{}/Crafting/Tools".format(FULL_NAME))
        os.mkdir("Complete/{}/Element".format(FULL_NAME))
        os.mkdir("Complete/{}/Block".format(FULL_NAME))
        os.mkdir("Complete/{}/Code".format(FULL_NAME))
        os.mkdir("Complete/{}/Code/blockstates".format(FULL_NAME))
        os.mkdir("Complete/{}/Code/models".format(FULL_NAME))
        os.mkdir("Complete/{}/Code/models/block".format(FULL_NAME))
        os.mkdir("Complete/{}/Code/models/item".format(FULL_NAME))
        os.mkdir("Complete/{}/Code/textures".format(FULL_NAME))
        os.mkdir("Complete/{}/Code/loot_tables".format(FULL_NAME))
        os.mkdir("Complete/{}/Code/java".format(FULL_NAME))

        config = open("Complete/{}/config.cfg".format(FULL_NAME), "w+")

        config.write("//ORE// \n")
        config.write("Spawn level: y{} - y{} \n".format(ORE_Y_LEVEL_MIN, ORE_Y_LEVEL_MAX))
        config.write("Mining level: {} \n".format(ORE_MINE_LEVEL))
        config.write("Smeltable: {}, drop count: {} \n\n".format(ORE_SMELTABLE, ORE_DROP_COUNT))

        config.write("//ITEM// \n")
        config.write("Spawn places: \nDungeon: {} \nTemple: {} \nStonghold: {} \nMineshaft: {} \nVillage: {} \nMansion: {} \nEnd City: {} \nEnd Ship: {} \n".format(ITEM_DUNGEON, ITEM_TEMPLE, ITEM_STRONGHOLD, ITEM_MINESHAFT, ITEM_VILLAGE, ITEM_MANSION, ITEM_END_CITY, ITEM_END_SHIP))
        config.write("Crafting: \nArmor: {} \nTools: {} \nWeapons: {} \nTorch: {} \nBlock: {} \n\n".format(CRAFTING_ARMOR, CRAFTING_TOOLS, CRAFTING_WEAPONS, CRAFTING_TORCH, CRAFTING_BLOCK))
        
        config.write("//USE// \n")
        config.write("FUEL: {} \n".format(USE_FUEL))
        config.write("FOOD: {} \n\n".format(USE_FOOD))

        if CRAFTING_WEAPONS:
            config.write("//SWORD// \n")
            config.write("Durability: {} \n".format(USE_DURABILITY))
            config.write("Damage: {} \n".format(USE_DAMAGE))
            config.write("Attack Effect on NPC: {} \n".format(USE_ATTACK_EFFECT_NPC))
            config.write("Attack Effect on Player: {} \n".format(USE_ATTACK_EFFECT_PLAYER))
            config.write("Idle Effect: {} \n".format(USE_HOLDING_EFFECT))
            config.write("Enchantments: {} \n".format(USE_ENCHANTMENT))

        # IMAGE SETTINGS
        hue = random.randint(1,360)
        brightness = random.randint(-30,30)/100
        saturation = random.randint(-30,30)/100

        # FOREGROUND
        filename = "elementOverlays/" + selectRandomFile("elementOverlays/")
        basename, ext = os.path.splitext(filename)
        img = Image.open(filename).convert('RGBA')
        overlay_IMG = hueChange(filename, img, hue, brightness, saturation)

        # BACKGROUND
        filename = "elementUnderlays/" + selectRandomFile("elementUnderlays/")
        underlay_IMG = Image.open(filename)
        underlay_IMG.paste(overlay_IMG,(0,0), overlay_IMG)
        underlay_IMG.save("Complete/{}/Block/{}.png".format(FULL_NAME, FULL_NAME),"PNG")
        underlay_IMG.save("Complete/{}/Code/textures/{}.png".format(FULL_NAME, ore),"PNG")

        # ELEMENT
        filename = "elementItems/Elements/" + selectRandomFile("elementItems/Elements/")
        basename, ext = os.path.splitext(filename)
        item = Image.open(filename).convert('RGBA')
        item = hueChange(filename, item, hue, brightness, saturation)
        out = 'Complete/{}/Element/{}.png'.format(FULL_NAME,FULL_NAME)
        item.save(out)
        item.save("Complete/{}/Code/textures/{}.png".format(FULL_NAME, RAW))

        #TOOLS
        if CRAFTING_TOOLS:
            for filename in os.listdir("elementItems/Tools/"):
                item = Image.open("elementItems/Tools/" + filename).convert('RGBA')
                item = hueChange(filename, item, hue, brightness, saturation)
                out = 'Complete/{}/Crafting/Tools/{}_{}.png'.format(FULL_NAME, FULL_NAME, filename.split('.')[0])
                item.save(out)

        #BLOCK
        if CRAFTING_BLOCK:
            filename = "elementItems/Block/" + selectRandomFile("elementItems/Block/")
            block = Image.open(filename)
            block = hueChange(filename, block, hue, brightness, saturation)
            out = 'Complete/{}/Crafting/Block/{}_block.png'.format(FULL_NAME, RAW)
            block.save(out)

        blockstates = open("Complete/{}/Code/blockstates/{}.json".format(FULL_NAME,ore), "w+")
        lang = open("Complete/Code/lang/{}.json".format("en_US"), "a+")
        models_block = open("Complete/{}/Code/models/block/{}.json".format(FULL_NAME,ore), "w+")
        models_item_ore = open("Complete/{}/Code/models/item/{}.json".format(FULL_NAME,ore), "w+")
        models_item_raw = open("Complete/{}/Code/models/item/{}.json".format(FULL_NAME,RAW), "w+")
        loot = open("Complete/{}/Code/loot_tables/{}.json".format(FULL_NAME,ore), "w+")
        block_java = open("Complete/{}/Code/java/{}.java".format(FULL_NAME,titlecase(ore)), "w+")
        item_java = open("Complete/{}/Code/java/{}.java".format(FULL_NAME,titlecase(RAW)), "w+")
        main_java = open("Complete/Code/java/{}.txt".format("Main"), "a+")
        modBlock_java = open("Complete/Code/java/{}.java".format("ModBlocks"), "a+")
        modItem_java = open("Complete/Code/java/{}.java".format("ModItems"), "a+")

        # JSON
        blockstates.write('{{"variants": {{"": {{ "model":  "randoblock:block/{}"}}}}}}'.format(ore))
        models_block.write('{{"parent": "block/cube_all","textures": {{"all": "randoblock:block/{}"}}}}'.format(ore))
        models_item_ore.write('{{"parent": "randoblock:block/{}"}}'.format(ore))
        models_item_raw.write('{{"parent": "item/handheld","textures": {{"layer0": "randoblock:item/{}"}}}}'.format(RAW))
        loot.write('{{"type": "minecraft:block","pools": [{{"name": "pool1","rolls": 1,"entries": [{{"type": "minecraft:item","name": "randoblock:{}"}}],"conditions": [{{"condition": "minecraft:survives_explosion"}}]}}]}}'.format(RAW))

        # JAVA
        writeJavaBlockImports(block_java)
        block_java.write("public class {} extends Block {{ \n\n".format(titlecase(ore)))
        block_java.write("  public {}() {{ \n".format(titlecase(ore)))
        block_java.write("      super(Properties.create(Material.EARTH).sound(SoundType.GROUND).hardnessAndResistance(3.0f)); \n")
        block_java.write('      setRegistryName("{}"); \n'.format(ore))
        block_java.write("}}")

        writeJavaItemImports(item_java)
        item_java.write("public class {} extends Item {{ \n\n".format(titlecase(RAW)))
        item_java.write("   public {}() {{ \n".format(titlecase(RAW)))
        item_java.write("       super(new Item.Properties().maxStackSize(64).group(Main.setup.itemGroup)); \n")
        item_java.write('       setRegistryName("{}"); \n'.format(RAW))
        item_java.write("}}")

        # CONTINOUS
        if not langFile:
            lang.write("{ \n")
            lang.write('"_comment": "Creative Tabs", \n')
            lang.write('"itemGroup.randoblock": "RandoBlock" \n')

        lang.write('"block.randoblock.{}": "{}", \n'.format(ore, titlecase(FULL_NAME) + " ore"))
        lang.write('"item.randoblock.{}": "{}", \n'.format(RAW, RAW))

        if not modBlockFile:
            modBlock_java.write("package com.iceberg.randoblock.blocks; \n")
            modBlock_java.write("import net.minecraftforge.registries.ObjectHolder; \n\n")
            modBlock_java.write("public class ModBlocks { \n\n")

        modBlock_java.write('@ObjectHolder("randoblock:{}") \n'.format(ore))
        modBlock_java.write("public static {} {}; \n\n".format(titlecase(ore), ore))

        if not modItemFile:
            modItem_java.write("package com.iceberg.randoblock.items; \n")
            modItem_java.write("import net.minecraftforge.registries.ObjectHolder; \n\n")
            modItem_java.write("public class ModItems { \n\n")

        modItem_java.write('@ObjectHolder("randoblock:{}") \n'.format(RAW))
        modItem_java.write("public static {} {}; \n\n".format(titlecase(RAW), RAW.upper()))

        main_java.write(FULL_NAME + "\n")
        main_java.write("event.getRegistry().register(new {}()); \n".format(titlecase(ore)))
        main_java.write('event.getRegistry().register(new BlockItem(ModBlocks.{}, properties).setRegistryName("{}")); \n'.format(ore,ore))
        main_java.write("event.getRegistry().register(new {}()); \n\n".format(titlecase(RAW)))

        names.append(FULL_NAME)

        modBlock_java.close()
        modItem_java.close()
        block_java.close()
        item_java.close()
        main_java.close()
        loot.close()
        models_item_raw.close()
        models_block.close()
        models_item_ore.close()
        blockstates.close()
        lang.close()
        fn.close()
        sn.close()
        ln.close()
    print("")
    print("Generated content: {} blocks".format(len(names)))
    for name in names:
        print(name)
CreateNewContent(10)