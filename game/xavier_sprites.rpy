image xavier_sprite:
    LiveComposite(
        (429,521),

        (0,0), "images/NPC/Xavier_body.png",

        (0,0), ConditionSwitch(
            "X_Brows == 'concentrate'", "images/NPC/Xavier_brows_concentrate.png",
            "X_Brows == 'happy'", "images/NPC/Xavier_brows_happy.png",
            "X_Brows == 'shocked'", "images/NPC/Xavier_brows_shocked.png",
            "X_Brows == 'neutral'", "images/NPC/Xavier_brows_neutral.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "X_Mouth == 'concentrate'", "images/NPC/Xavier_mouth_stern.png",
            "X_Mouth == 'happy'", "images/NPC/Xavier_mouth_smile.png",
            "X_Mouth == 'neutral'", "images/NPC/Xavier_mouth_neutral.png",
            "True", Null()),

        (0,0), "xavier_blink",

        (0,0), ConditionSwitch(
            "X_Psychic == 1", "images/NPC/Xavier_psychic.png",
            "True", Null())
        )

    anchor (0.5, 0.0)
    offset (0, 150)
    zoom 1.1

image xavier_blink:
    ConditionSwitch(
        "X_Eyes == 'concentrate'", "images/NPC/Xavier_eyes_closed.png",
        "X_Eyes == 'hypno'", "images/NPC/Xavier_eyes_hypno.png",
        "X_Eyes == 'shocked'", "images/NPC/Xavier_eyes_shocked.png",
        "True", "images/NPC/Xavier_eyes_happy.png"),

    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/NPC/Xavier_eyes_closed.png"
    0.25
    repeat

label Xavierface(face = X_Emote):
    if face == "psychic":
        $ X_Mouth = "concentrate"
        $ X_Brows = "concentrate"
        $ X_Eyes = "concentrate"
        $ X_Psychic = 1
    if face == "hypno":
        $ X_Mouth = "neutral"
        $ X_Brows = "neutral"
        $ X_Eyes = "hypno"
        $ X_Psychic = 0
    if face == "shocked":
        $ X_Mouth = "neutral"
        $ X_Brows = "shocked"
        $ X_Eyes = "shocked"
        $ X_Psychic = 0
    if face == "happy":
        $ X_Mouth = "happy"
        $ X_Brows = "happy"
        $ X_Eyes = "happy"
        $ X_Psychic = 0
    if face == "angry":
        $ X_Mouth = "concentrate"
        $ X_Brows = "concentrate"
        $ X_Eyes = "happy"
        $ X_Psychic = 0

    return
