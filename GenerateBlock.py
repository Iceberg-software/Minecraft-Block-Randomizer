import random
from PIL import Image
import numpy as np
import colorsys
import os
import random
import progressbar
from titlecase import titlecase
from pixels import axe_pixels, sword_pixels, pickaxe_pixels, hoe_pixels, shovel_pixels

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
                    if not (x,y) in pickaxe_pixels():
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
                    if not (x,y) in sword_pixels():
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
                    if not (x,y) in shovel_pixels():
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
                    if not (x,y) in hoe_pixels():
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
                    if not (x,y) in axe_pixels():
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
        fn = open("firstNames.txt")
        sn = open("secondNames.txt")
        ln = open("lastNames.txt")

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
            FULL_NAME += firstNames[random.randint(0,fileLen("firstNames.txt"))].replace("\n", "")

        FULL_NAME += secondNames[random.randint(0,fileLen("secondNames.txt"))].replace("\n", "")
        FULL_NAME += firstNames[random.randint(0,fileLen("firstNames.txt"))].replace("\n", "")

        if fourthName == 1:
            FULL_NAME += secondNames[random.randint(0,fileLen("secondNames.txt"))].replace("\n", "")

        if fifthName == 1:
            FULL_NAME += firstNames[random.randint(0,fileLen("firstNames.txt"))].replace("\n", "")

        if sixthName == 1:
            FULL_NAME += lastNames[random.randint(0,fileLen("lastNames.txt"))].replace("\n", "")

        #print("")
        #print(FULL_NAME)

        RAW = FULL_NAME
        ore = FULL_NAME + "_ore"

        modBlockFile = os.path.isfile("Complete/Code/java/{}.java".format("ModBlocks"))
        modItemFile = os.path.isfile("Complete/Code/java/{}.java".format("ModItems"))
        langFile = os.path.isfile("Complete/Code/lang/{}.json".format("en_US"))

        if os.path.isdir("Complete/{}".format(FULL_NAME)):
            continue

        if not os.path.isdir("Complete/Code"):
            os.mkdir("Complete/Code")
        if not os.path.isdir("Complete/Code/lang"):
            os.mkdir("Complete/Code/lang")
        if not os.path.isdir("Complete/Code/java"):
            os.mkdir("Complete/Code/java")
        os.mkdir("Complete/{}".format(FULL_NAME))
        os.mkdir("Complete/{}/Tools".format(FULL_NAME))
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
        underlay_width, underlay_height = underlay_IMG.size
        overlay_width, overlay_height = overlay_IMG.size
        offset = (int(round((underlay_width - overlay_width) / 2)), int(round((underlay_height - overlay_height) / 2)))
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
        for filename in os.listdir("elementItems/Tools/"):
            item = Image.open("elementItems/Tools/" + filename).convert('RGBA')
            item = hueChange(filename, item, hue, brightness, saturation)
            out = 'Complete/{}/Tools/{}_{}.png'.format(FULL_NAME, FULL_NAME, filename.split('.')[0])
            item.save(out)

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
