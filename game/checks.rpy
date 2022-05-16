label Rogue_Dildo_Check:
    if "dildo" in Player.Inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in RogueX.Inventory:
        "You ask [RogueX.name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1

label Rogue_Vibrator_Check:
    if "vibrator" in Player.Inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in RogueX.Inventory:
        "You ask [RogueX.name] to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1
