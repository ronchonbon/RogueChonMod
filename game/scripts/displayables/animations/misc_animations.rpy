transform stat_rising(x_position):
    ypos 0.25 alpha 0.0
    choice:
        xpos x_position alpha 1.0
    choice:
        pause 0.1
        xpos x_position - 0.015 alpha 1.0
    choice:
        pause 0.2
        xpos x_position + 0.015 alpha 1.0
    choice:
        pause 0.3
        xpos x_position - 0.03 alpha 1.0
    choice:
        pause 0.4
        xpos x_position + 0.03 alpha 1.0
    choice:
        pause 0.5
        xpos x_position alpha 1.0
    choice:
        pause 0.6
        xpos x_position - 0.015 alpha 1.0
    choice:
        pause 0.7
        xpos x_position + 0.015 alpha 1.0
    choice:
        pause 0.8
        xpos x_position - 0.03 alpha 1.0
    choice:
        pause 0.9
        xpos x_position + 0.03 alpha 1.0
    parallel:
        linear 1.0 ypos 0.0
    parallel:
        linear 1.0 alpha 0.0

transform stat_falling(x_position):
    ypos 0.0 alpha 0.05
    choice:
        xpos x_position alpha 1.0
    choice:
        pause 0.1
        xpos x_position - 0.015 alpha 1.0
    choice:
        pause 0.2
        xpos x_position + 0.015 alpha 1.0
    choice:
        pause 0.3
        xpos x_position - 0.03 alpha 1.0
    choice:
        pause 0.4
        xpos x_position + 0.03 alpha 1.0
    choice:
        pause 0.5
        xpos x_position alpha 1.0
    choice:
        pause 0.6
        xpos x_position - 0.015 alpha 1.0
    choice:
        pause 0.7
        xpos x_position + 0.015 alpha 1.0
    choice:
        pause 0.8
        xpos x_position - 0.03 alpha 1.0
    choice:
        pause 0.9
        xpos x_position + 0.03 alpha 1.0
    parallel:
        linear 1.0 ypos 0.25
    parallel:
        linear 1.0 alpha 0.0

transform dripping(x_offset = 0, start = 0, transparency = 1.0):
    offset (x_offset, start) alpha transparency
    easeout 0.9 yoffset 350 alpha 0.0

image grool_dripping_animation:
    animation
    "images/misc/grool.png"

    subpixel True
    anchor (0.5, 0.5) alpha 0.0 zoom 0.2
    block:
        choice:
            pause 1
        choice:
            pause 0.5
        choice:
            dripping(8, 10, 0.8)
            pause 1
        choice:
            pause 0.2
            dripping(3, 15, 0.8)
            pause 0.4
        choice:
            pause 0.4
            dripping(0, 5, 0.8)
        choice:
            pause 0.8
            dripping(6, 0, 0.8)
        repeat

image spunk_dripping_animation:
    animation
    "images/misc/sperm.png"

    subpixel True
    anchor (0.5, 0.5) alpha 0.0 zoom 0.3
    block:
        choice:
            pause 1
        choice:
            pause 0.5
        choice:
            dripping(8, 10)
            pause 1
        choice:
            pause 0.2
            dripping(3, 15)
            pause 0.4
        choice:
            pause 0.4
            dripping(0, 5)
        choice:
            pause 0.8
            dripping(6, 0)
        repeat

image licking:
    animation
    subpixel True
    anchor (0.5, 0.5)
    parallel:
        "images/misc/licking1.png"
        0.6
        "images/misc/licking6.png"
        0.15
        "images/misc/licking2.png"
        0.15
        "images/misc/licking3.png"
        0.15
        "images/misc/licking4.png"
        0.6
        "images/misc/licking3.png"
        0.075
        "images/misc/licking2.png"
        0.075
        repeat
    parallel:
        pause 0.45
        easein 0.525 yoffset -15
        pause 0.225
        easein 0.6 yoffset 0
        repeat

image punchout:
    Null(0, 0)

label punch:
    show punchout with vpunch
    hide punchout

    return

image dildo:
    "images/misc/dildo.png"

    anchor (0.5, 0.5)















image dress_screen:

    contains:

        "images/dress_screen.png"
    contains:

        AlphaMask("images/dress_screen_shadow.png", "dress_screen_shadow")
    zoom 1
    offset (375, 225)

image dress_screen_shadow:

    contains:

        ConditionSwitch(
            "RogueX.sprite_layer == 100", "Rogue_sprite standing",
            "KittyX.sprite_layer == 100", "Kitty_sprite standing",
            "EmmaX.sprite_layer == 100", "Emma_sprite standing",
            "LauraX.sprite_layer == 100", "Laura_sprite standing",
            "JeanX.sprite_layer == 100", "Jean_sprite standing",
            "StormX.sprite_layer == 100", "Storm_sprite standing",
            "JubesX.sprite_layer == 100", "Jubes_sprite standing",




            "True", Null(),
            )
        offset (210, -170)
        zoom 1














image blue_screen:

    alpha 0.1
    contains:
        Solid("#00B3D6", xysize=(1024, 768))





transform Vibrate():
    block:
        linear 0.5 xoffset 2
        linear 0.5 xoffset -2
        repeat


image UI_Vibrator = LiveComposite(
        (224, 224),
        (0, 0), ConditionSwitch(
            "not Vibration", "UI_VibA",
            "Vibration", At("UI_VibB", Vibrate()),
            ),
        )










image VibratorRightBreast:
    contains:
        "UI_Vibrator"
        pos (150,380)
        zoom 0.5
        anchor (0.5, 0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 370
            pause 0.25
            ease 1 rotate 55 ypos 380
            pause 0.25
            repeat

image VibratorLeftBreast:
    contains:
        "UI_Vibrator"
        pos (270,400)
        zoom 0.5
        anchor (0.5, 0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 390
            pause 0.25
            ease 1 rotate 55 ypos 400
            pause 0.25
            repeat

image VibratorPussy:
    contains:
        "UI_Vibrator"
        pos (240, 665)
        zoom 0.5
        anchor (0.5, 0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 xpos 230 ypos 655
            pause 0.25
            ease 1 rotate 70 xpos 240 ypos 665
            pause 0.25
            repeat

image VibratorAnal:
    contains:
        "UI_Vibrator"
        pos (270, 640)
        zoom 0.5
        anchor (0.5, 0.5)
        alpha 0.3
        rotate 10
        block:
            ease 1 rotate 0 xpos 260 ypos 655
            pause 0.25
            ease 1 rotate 10 xpos 270 ypos 665
            pause 0.25
            repeat

image VibratorPussyInsert:
    contains:
        "UI_Vibrator"
        pos (240, 645)
        zoom 0.5
        anchor (0.5, 0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert:
    contains:
        "UI_Vibrator"
        pos (250, 640)
        zoom 0.5
        anchor (0.5, 0.5)
        alpha 0.3
        rotate 0
