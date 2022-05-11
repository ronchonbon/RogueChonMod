

# Gwenpool sprites Start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Gwen_Sprite:
    LiveComposite(
        (574,964),
        #body
        (0,0), "images/GS_B.png",
#        (0,0), "images/GS_H.png",
        #Head
        (80,15), "Gwen_Sprite_Head",
        )
    anchor (0.6, 0.0)
    yoffset 15
    zoom .75



image Gwen_Sprite_Head:
    LiveComposite(
        (820,820),
        (0,0), ConditionSwitch(
                # Face background plate
                "G_Blush", "images/NPC/Gwen_Sprite_Head_Blush.png",
                "True", "images/NPC/Gwen_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(#Mouths
            "G_Mouth == 'open'", "images/NPC/Gwen_Sprite_Mouth_Open.png",
            "G_Mouth == 'kiss'", "images/NPC/Gwen_Sprite_Mouth_Kiss.png",
            "G_Mouth == 'smile'", "images/NPC/Gwen_Sprite_Mouth_Smile.png",
            "G_Mouth == 'shocked'", "images/NPC/Gwen_Sprite_Mouth_Shocked.png",
            "True", "images/NPC/Gwen_Sprite_Mouth_Smile.png",
            ),
        (0,0), ConditionSwitch(
            #brows
            "G_Blush", ConditionSwitch(
                    "G_Brows == 'angry' or G_Eyes == 'angry'", "images/NPC/Gwen_Sprite_Brows_Angry_B.png",
                    "G_Brows == 'sad'", "images/NPC/Gwen_Sprite_Brows_Sad_B.png",
                    "True", "images/NPC/Gwen_Sprite_Brows_Normal.png",
                    ),
            "True", ConditionSwitch(
                    "G_Brows == 'angry' or G_Eyes == 'angry'", "images/NPC/Gwen_Sprite_Brows_Angry.png",
                    "G_Brows == 'sad'", "images/NPC/Gwen_Sprite_Brows_Sad.png",
                    "True", "images/NPC/Gwen_Sprite_Brows_Normal.png",
                    ),
            ),
        (0,0), "Gwen Blink",     #Eyes
        )
    anchor (0.6, 0.0)
    zoom .5

image Gwen Blink:
    ConditionSwitch(
    "G_Eyes == 'angry'", "images/NPC/Gwen_Sprite_Eyes_Angry.png",
    "G_Eyes == 'surprised'", "images/NPC/Gwen_Sprite_Eyes_Surprised.png",
    "G_Eyes == 'closed'", "images/NPC/Gwen_Sprite_Eyes_Closed.png",
    "True", "images/NPC/Gwen_Sprite_Eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/NPC/Gwen_Sprite_Eyes_Closed.png"
    .20
    repeat

default G_Mouth = "normal"
default G_Brows = "normal"
default G_Eyes = "normal"
default G_Blush = 0

label GwenFace(Emote = "normal", B = G_Blush, M = 0, Mouth = 0, Eyes = 0, Brows = 0):
        # Emote is the chosen emote, B is the lush state
        # M is whether the character is in a  manic state
        $ B = G_Blush if B == 5 else B

        if Emote == "normal":
                $ G_Mouth = "normal"
                $ G_Brows = "normal"
                $ G_Eyes = "normal"
        elif Emote == "angry":
                $ G_Mouth = "kiss"
                $ G_Brows = "angry"
                $ G_Eyes = "angry"
        elif Emote == "closed":
                $ G_Mouth = "normal"
                $ G_Brows = "sad"
                $ G_Eyes = "closed"
        elif Emote == "sad":
                $ G_Mouth = "kiss"
                $ G_Brows = "sad"
                $ G_Eyes = "normal"
        elif Emote == "smile":
                $ G_Mouth = "smile"
                $ G_Brows = "normal"
                $ G_Eyes = "normal"
        elif Emote == "surprised":
                $ G_Mouth = "open"
                $ G_Brows = "normal"
                $ G_Eyes = "surprised"
        elif Emote == "shocked":
                $ G_Mouth = "shocked"
                $ G_Brows = "normal"
                $ G_Eyes = "surprised"

        if B > 1:
                $ G_Blush = 2
        elif B:
                $ G_Blush = 1
        else:
                $ G_Blush = 0

        if Mouth:
                $ G_Mouth = Mouth
        if Eyes:
                $ G_Eyes = Eyes
        if Brows:
                $ G_Brows = Brows

        return

label Gwen_FaceEditor:
            while True:
                menu:
                    "Brows=[G_Brows], Eyes=[G_Eyes], Mouth=[G_Mouth]"
                    "Toggle Brows":
                            if G_Brows == "normal":
                                $ G_Brows = "angry"
                            elif G_Brows == "angry":
                                $ G_Brows = "confused"
                            elif G_Brows == "confused":
                                $ G_Brows = "sad"
                            elif G_Brows == "sad":
                                $ G_Brows = "surprised"
                            else:
                                $ G_Brows = "normal"
                    "Toggle Eyes Emotions":
                            if G_Eyes == "normal":
                                $ G_Eyes = "surprised"
                            elif G_Eyes == "surprised":
                                $ G_Eyes = "sexy"
                            elif G_Eyes == "sexy":
                                $ G_Eyes = "squint"
                            elif G_Eyes == "squint":
                                $ G_Eyes = "closed"
                            else:
                                $ G_Eyes = "normal"
                    "Toggle Eyes Directions":
                            if G_Eyes == "normal":
                                $ G_Eyes = "side"
                            elif G_Eyes == "side":
                                $ G_Eyes = "down"
                            elif G_Eyes == "down":
                                $ G_Eyes = "leftside"
                            elif G_Eyes == "leftside":
                                $ G_Eyes = "stunned"
                            else:
                                $ G_Eyes = "normal"
                    "Toggle Mouth Normal":
                            if G_Mouth  == "normal":
                                $ G_Mouth = "sad"
                            elif G_Mouth == "sad":
                                $ G_Mouth = "smile"
                            elif G_Mouth == "smile":
                                $ G_Mouth = "surprised"
                            else:
                                $ G_Mouth = "normal"
                    "Toggle Mouth Sexy":
                            if G_Mouth  == "normal":
                                $ G_Mouth = "kiss"
                            elif G_Mouth == "kiss":
                                $ G_Mouth = "sucking"
                            elif G_Mouth == "sucking":
                                $ G_Mouth = "tongue"
                            elif G_Mouth == "tongue":
                                $ G_Mouth = "lipbite"
                            else:
                                $ G_Mouth = "normal"
                    "Toggle Blush":
                        if G_Blush == 1:
                            $ G_Blush = 2
                        elif G_Blush:
                            $ G_Blush = 0
                        else:
                            $ G_Blush = 1

                    "Back":
                            return
#image Gwen_Sprite_Head:
#    LiveComposite(
#        (806,806),
#        (0,0), ConditionSwitch(
#                # Face background plate
#                "L_Blush == 2", "images/LauraSprite/Laura_Sprite_Head_Blush2.png",
#                "L_Blush", "images/LauraSprite/Laura_Sprite_Head_Blush.png",
#                "True", "images/LauraSprite/Laura_Sprite_Head.png",
#                ),
#        )
#    anchor (0.6, 0.0)
#    zoom .5


label Display_Gwen(GwLoc = 350, YLoc=50):
   # If Dress, then check whether the character is underdressed when displaying her

    #Display Gwen
    show Gwen_Sprite:
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)
            easeout .5 pos (GwLoc,YLoc)
    show Gwen_Sprite:
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)
            pos (GwLoc,YLoc)
    return
