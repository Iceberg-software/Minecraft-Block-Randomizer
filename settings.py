import random

def axe_pixels():
    return ((11,4),(12,4),(12,5),(8,7),
            (9,6),(10,7),(9,7),(8,8),
            (9,8),(7,8),(7,9),(6,9),
            (8,9),(6,10),(5,10),(7,10),
            (5,11),(6,11),(4,11),(3,13),
            (4,12),(5,12),(3,12),(2,13),
            (4,13),(2,14),(3,14))

def hoe_pixels():
    return ((9,6),(10,7),(9,7),(8,8),
            (9,8),(7,8),(7,9),(6,9),
            (8,9),(6,10),(5,10),(7,10),
            (5,11),(6,11),(4,11),(3,13),
            (4,12),(5,12),(3,12),(2,13),
            (4,13),(2,14),(3,14),(10,6),
            (11,6),(10,5),(12,4),(12,3),
            (13,4),(8,7))

def pickaxe_pixels():
    return ((9,6),(10,7),(9,7),(8,8),
            (9,8),(7,8),(7,9),(6,9),
            (8,9),(6,10),(5,10),(7,10),
            (5,11),(6,11),(4,11),(3,13),
            (4,12),(5,12),(3,12),(2,13),
            (4,13),(2,14),(3,14),(10,6),
            (10,5),(11,6),(12,4),(13,4),
            (12,3),(13,3),(8,7))

def shovel_pixels():
    return ((9,6),(10,7),(9,7),(8,8),
            (9,8),(7,8),(7,9),(6,9),
            (8,9),(6,10),(5,10),(7,10),
            (5,11),(6,11),(4,11),(3,13),
            (4,12),(3,12),(2,12),(2,13),
            (3,13),(4,13),(5,12),(3,14),
            (4,14),(8,7))

def sword_pixels():
    return ((4,11),(3,13),(3,11),(2,12),
            (4,12),(5,12),(3,12),(2,13))

def sword_enchantments(power):
    if power == "UNDER_POWERED":
        return((("Bane of Arthropods", random.randint(0,1)), ("Fire Aspect", random.randint(0,1)), ("Knockback", random.randint(0,1)), ("Looting", random.randint(0,1)), ("Sharpness", random.randint(0,1)), ("Smite", random.randint(0,5)), ("Sweeping Edge", random.randint(0,1)), ("Unbreaking", random.randint(0,1)), ("Mending", random.randint(0,1))))
    if power == "NORMAL":
        return((("Bane of Arthropods", random.randint(0,5)), ("Fire Aspect", random.randint(0,2)), ("Knockback", random.randint(0,2)), ("Looting", random.randint(0,3)), ("Sharpness", random.randint(0,5)), ("Smite", random.randint(0,5)), ("Sweeping Edge", random.randint(0,3)), ("Unbreaking", random.randint(0,3)), ("Mending", random.randint(0,1))))
    if power == "OVER_POWERED":
        return((("Bane of Arthropods", random.randint(0,10)), ("Fire Aspect", random.randint(0,10)), ("Knockback", random.randint(0,10)), ("Looting", random.randint(0,10)), ("Sharpness", random.randint(0,10)), ("Smite", random.randint(0,10)), ("Sweeping Edge", random.randint(0,1)), ("Unbreaking", random.randint(0,10)), ("Mending", random.randint(0,1))))

def bow_enchantments(power):
    if power == "UNDER_POWERED":
        return((("Flame", random.randint(0,1)), ("Ifinity", random.randint(0,1)), ("Power", random.randint(0,1)), ("Punch", random.randint(0,1)), ("Unbreaking", random.randint(0,1)), ("Mending", random.randint(0,1))))
    if power == "NORMAL":
        return((("Flame", random.randint(0,1)), ("Ifinity", random.randint(0,1)), ("Power", random.randint(0,5)), ("Punch", random.randint(0,2)), ("Unbreaking", random.randint(0,3)), ("Mending", random.randint(0,1))))
    if power == "OVER_POWERED":
        return((("Flame", random.randint(0,1)), ("Ifinity", random.randint(0,1)), ("Power", random.randint(0,10)), ("Punch", random.randint(0,10)), ("Unbreaking", random.randint(0,10)), ("Mending", random.randint(0,1))))

def tool_enchantments(power):
    if power == "UNDER_POWERED":
        return((("Efficiency", random.randint(0,1)), ("Fortune", random.randint(0,1)), ("Silk Touch", random.randint(0,1)), ("Unbreaking", random.randint(0,1)), ("Mending", random.randint(0,1))))
    if power == "NORMAL":
        return((("Efficiency", random.randint(0,5)), ("Fortune", random.randint(0,3)), ("Silk Touch", random.randint(0,1)), ("Unbreaking", random.randint(0,3)), ("Mending", random.randint(0,1))))
    if power == "OVER_POWERED":
        return((("Efficiency", random.randint(0,10)), ("Fortune", random.randint(0,10)), ("Silk Touch", random.randint(0,1)), ("Unbreaking", random.randint(0,10)), ("Mending", random.randint(0,1))))

def crossbow_enchantments(power):
    if power == "UNDER_POWERED":
        return((("Multishot", random.randint(0,1)), ("Quick Charge", random.randint(0,1)), ("Piercing", random.randint(0,1)), ("Unbreaking", random.randint(0,1)), ("Mending", random.randint(0,1))))
    if power == "NORMAL":
        return((("Multishot", random.randint(0,1)), ("Quick Charge", random.randint(0,3)), ("Piercing", random.randint(0,5)), ("Unbreaking", random.randint(0,3)), ("Mending", random.randint(0,1))))
    if power == "OVER_POWERED":
        return((("Multishot", random.randint(0,1)), ("Quick Charge", random.randint(0,10)), ("Piercing", random.randint(0,10)), ("Unbreaking", random.randint(0,10)), ("Mending", random.randint(0,1))))

def armor_enchantments(power):
    if power == "UNDER_POWERED":
        return((("Blast Protection", random.randint(0,1)), ("Fire Protection", random.randint(0,1)), ("Projectile Protection", random.randint(0,1)), ("Protection", random.randint(0,1)), ("Thorns", random.randint(0,1)), ("Curse of Binding", random.randint(0,1)), ("Mending", random.randint(0,1))))
    if power == "NORMAL":
        return((("Blast Protection", random.randint(0,5)), ("Fire Protection", random.randint(0,3)), ("Projectile Protection", random.randint(0,1)), ("Protection", random.randint(0,3)), ("Thorns", random.randint(0,3)), ("Curse of Binding", random.randint(0,1)), ("Mending", random.randint(0,1))))
    if power == "OVER_POWERED":
        return((("Blast Protection", random.randint(0,10)), ("Fire Protection", random.randint(0,10)), ("Projectile Protection", random.randint(0,1)), ("Protection", random.randint(0,10)), ("Thorns", random.randint(0,10)), ("Curse of Binding", random.randint(0,1)), ("Mending", random.randint(0,1))))

def helmet_enchantments(power):
    if power == "UNDER_POWERED":
        return((("Blast Protection", random.randint(0,1)), ("Fire Protection", random.randint(0,1)), ("Projectile Protection", random.randint(0,1)), ("Protection", random.randint(0,1)), ("Thorns", random.randint(0,1)), ("Curse of Binding", random.randint(0,1)), ("Aqua Affinity", random.randint(0,1)), ("Respiration", random.randint(0,1)), ("Mending", random.randint(0,1))))
    if power == "NORMAL":
        return((("Blast Protection", random.randint(0,5)), ("Fire Protection", random.randint(0,3)), ("Projectile Protection", random.randint(0,1)), ("Protection", random.randint(0,3)), ("Thorns", random.randint(0,3)), ("Curse of Binding", random.randint(0,1)), ("Aqua Affinity", random.randint(0,1)), ("Respiration", random.randint(0,3)), ("Mending", random.randint(0,1))))
    if power == "OVER_POWERED":
        return((("Blast Protection", random.randint(0,10)), ("Fire Protection", random.randint(0,10)), ("Projectile Protection", random.randint(0,1)), ("Protection", random.randint(0,10)), ("Thorns", random.randint(0,10)), ("Curse of Binding", random.randint(0,1)), ("Aqua Affinity", random.randint(0,1)), ("Respiration", random.randint(0,10)), ("Mending", random.randint(0,1))))

def boot_enchantments(power):
    if power == "UNDER_POWERED":
        return((("Blast Protection", random.randint(0,1)), ("Fire Protection", random.randint(0,1)), ("Projectile Protection", random.randint(0,1)), ("Protection", random.randint(0,1)), ("Thorns", random.randint(0,1)), ("Curse of Binding", random.randint(0,1)), ("Depth Strider", random.randint(0,1)), ("Feather Falling", random.randint(0,1)), ("Frost Walker", random.randint(0,1)), ("Mending", random.randint(0,1))))
    if power == "NORMAL":
        return((("Blast Protection", random.randint(0,5)), ("Fire Protection", random.randint(0,3)), ("Projectile Protection", random.randint(0,1)), ("Protection", random.randint(0,3)), ("Thorns", random.randint(0,3)), ("Curse of Binding", random.randint(0,1)), ("Depth Strider", random.randint(0,3)), ("Feather Falling", random.randint(0,4)), ("Frost Walker", random.randint(0,1)), ("Mending", random.randint(0,1))))
    if power == "OVER_POWERED":
        return((("Blast Protection", random.randint(0,10)), ("Fire Protection", random.randint(0,10)), ("Projectile Protection", random.randint(0,1)), ("Protection", random.randint(0,10)), ("Thorns", random.randint(0,10)), ("Curse of Binding", random.randint(0,1)), ("Depth Strider", random.randint(0,10)), ("Feather Falling", random.randint(0,10)), ("Frost Walker", random.randint(0,1)), ("Mending", random.randint(0,1))))

def materials():
    return(("WOOD", "STONE", "IRON", "DIAMOND"))

def effects(action):
    if action == "PASSIVE":
        return(("Speed", "Slowness", "Haste", "Mining Fatigue", "Strength", "Jump Boost", "Nausea", "Regeneration", "Resistance", "Fire Resistance", "Water Breathing", "Invisibility", "Blindness", "Night Vision", "Hunger", "Weakness", "Poison", "Wither", "Health Boost", "Absorption", "Glowing", "Levitation", "Fatal Poison", "Luck", "Bad Luck", "Slow Falling", "Conduit Power", "Dolphin's Grace", "Bad Omen", "Hero of the Village"))
    if action == "ATTACK":
        return(("Speed", "Slowness", "Haste", "Mining Fatigue", "Strength", "Jump Boost", "Nausea", "Regeneration", "Resistance", "Fire Resistance", "Water Breathing", "Invisibility", "Blindness", "Night Vision", "Hunger", "Weakness", "Poison", "Wither", "Health Boost", "Absorption", "Glowing", "Levitation", "Fatal Poison", "Luck", "Bad Luck", "Slow Falling", "Conduit Power", "Dolphin's Grace", "Bad Omen", "Hero of the Village", "Instant Health", "Instant Damage", "Saturation"))