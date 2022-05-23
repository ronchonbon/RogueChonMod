image Kitty_Drip_Mask:

    contains:
        "images/KittySprite/Kitty_sprite_WetMask.png"
        offset (-225,-560)

image Kitty_Drip_MaskP:

    contains:
        "images/KittySprite/Kitty_sprite_WetMaskP.png"
        offset (-225,-560)






















image Kitty_sex_body_Anim0:
    contains:
        "Kitty_sex_body"
    pos (650,230)

image Kitty_sex_legs_Anim0:
    contains:
        "Kitty_sex_legs"
    pos (650,230)



image Kitty_Sex_Lick_Breasts:
    "licking"
    zoom 0.6
    offset (450,210)

image Kitty_Sex_Fondle_Breasts:
    "GropeLeftBreast"
    zoom 1.1
    offset (320,-180)


image Kitty_Sex_Lick_Pussy:
    "licking"
    zoom 0.7
    offset (530,510)

image Kitty_Sex_Lick_Ass:
    "licking"
    zoom 0.7
    offset (535,590)

image GropeBack:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        zoom 0.7
        pos (300,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image TestingSolid:

    contains:
        Solid("#75d7ec", xysize=(1500,1500))
        alpha 0.2


image Kitty_Pussy_Fucking0:

    contains:

        "images/Kitty_sex/Kitty_sex_pussy_open.png"
    contains:

        ConditionSwitch(
                "not KittyX.pubes", Null(),
                "True", "images/Kitty_sex/Kitty_sex_pubes_open.png",
                ),
    contains:

        AlphaMask("Kitty_Sex_Zero_Anim0", "Kitty_Pussy_Open_Mask")

image Kitty_Pussy_Fucking1:

    contains:

        "images/Kitty_sex/Kitty_sex_pussy_open.png"
    contains:

        ConditionSwitch(
                "not KittyX.pubes", Null(),
                "True", "images/Kitty_sex/Kitty_sex_pubes_open.png",
                ),
    contains:

        AlphaMask("Kitty_Sex_Zero_Anim1", "Kitty_Pussy_Open_Mask")

image Kitty_Pussy_Fucking2:

    contains:

        "images/Kitty_sex/Kitty_sex_pussy_fucking.png"
    contains:

        ConditionSwitch(
                "not KittyX.pubes", Null(),
                "True", "images/Kitty_sex/Kitty_sex_pubes_fucking.png",
                ),
    contains:

        AlphaMask("Kitty_Sex_Zero_Anim2", "Kitty_Pussy_Fucking_Mask")
image Kitty_Pussy_Fucking3:

    contains:

        "images/Kitty_sex/Kitty_sex_pussy_fucking.png"
    contains:

        ConditionSwitch(
                "not KittyX.pubes", Null(),
                "True", "images/Kitty_sex/Kitty_sex_pubes_fucking.png",
                ),
    contains:

        AlphaMask("Kitty_Sex_Zero_Anim3", "Kitty_Pussy_Fucking_Mask")

image Kitty_Pussy_Fucking_Mask:

    contains:
        "images/Kitty_sex/Kitty_sex_pussy_mask.png"

image Kitty_Pussy_Open_Mask:

    contains:
        "images/Kitty_sex/Kitty_sex_pussy_mask.png"
        yoffset 3















image Kitty_Pussy_Spunk_Heading:
    "images/Kitty_sex/Kitty_sex_spunk_pussy_over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8






image Kitty_Sex_Zero_Anim0:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (498,530)
        zoom 1.4

image Kitty_Sex_Zero_Anim1:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (498,525)
        zoom 1.4
        block:
            ease 1 pos (498,510)
            pause 1
            ease 3 pos (498,525)
            repeat

image Kitty_Sex_Zero_Anim2:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (500,490)
        zoom 1.4
        block:
            ease 1 pos (500,380)
            pause 1
            ease 3 pos (500,490)
            repeat

image Kitty_Sex_Zero_Anim3:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (500,490)
        zoom 1.4
        block:
            ease 0.25 pos (500,380)
            pause 0.25
            ease 1.5 pos (500,490)
            repeat



image Kitty_sex_legs_Anim1:

    contains:
        subpixel True
        "Kitty_sex_legs"
        pos (0,0)
        block:

            pause 0.25
            easein 1 pos (0,-5)
            pause 1
            ease 2.75 pos (0,0)
            repeat

image Kitty_sex_legs_Anim2:

    contains:
        subpixel True
        "Kitty_sex_legs"
        pos (0,0)
        block:

            pause 0.5
            easein 0.5 pos (0,-15)
            ease 0.25 pos (0,-10)
            pause 1
            ease 2.75 pos (0,0)
            repeat

image Kitty_sex_legs_Anim3:

    contains:
        subpixel True
        "Kitty_sex_legs"
        pos (0,0)
        block:

            pause 0.15
            easein 0.15 pos (0,-20)
            ease 0.10 pos (0,-15)
            pause 0.20
            ease 1.4 pos (0,0)
            repeat



image Kitty_sex_body_Anim1:

    contains:
        subpixel True
        "Kitty_sex_body"
        pos (0,0)
        block:

            pause 0.5
            easein 0.75 pos (0,-5)
            pause 1.25
            ease 2.5 pos (0,0)
            repeat

image Kitty_sex_body_Anim2:

    contains:
        subpixel True
        "Kitty_sex_body"
        pos (0,0)
        block:

            pause 0.6
            easein 0.4 pos (0,-10)
            ease 0.25 pos (0,-5)
            pause 1
            ease 2.75 pos (0,10)
            repeat

image Kitty_sex_body_Anim3:

    contains:
        subpixel True
        "Kitty_sex_body"
        pos (0,0)
        block:

            pause 0.17
            easein 0.13 pos (0,-20)
            ease 0.10 pos (0,-15)
            pause 0.20
            ease 1.4 pos (0,10)
            repeat









image Kitty_Sex_Anal_Fucking0:

    contains:

        "Kitty_Sex_Anal0"
    contains:

        AlphaMask("Kitty_Anal_Zero_Anim0", "Kitty_Sex_Anal_Fucking_Mask")

image Kitty_Sex_Anal_Fucking1:

    contains:

        "Kitty_Anal_Heading"
    contains:


        AlphaMask("Kitty_Anal_Zero_Anim1", "Kitty_Sex_Anal_Fucking_Mask")

image Kitty_Sex_Anal_Fucking2:

    contains:

        "images/Kitty_sex/Kitty_sex_anus_open.png"
    contains:

        AlphaMask("Kitty_Anal_Zero_Anim2", "Kitty_Sex_Anal_Fucking_Mask")

image Kitty_Sex_Anal_Fucking3:

    contains:

        "images/Kitty_sex/Kitty_sex_anus_open.png"
    contains:

        AlphaMask("Kitty_Anal_Zero_Anim3", "Kitty_Sex_Anal_Fucking_Mask")

image Kitty_Sex_Anal_Fucking_Mask:

    contains:
        "images/Kitty_sex/Kitty_sex_anus_mask.png"

image Kitty_Sex_Anal_Open_Mask:

    contains:
        "images/Kitty_sex/Kitty_sex_anus_mask.png"
        yoffset 3

image Kitty_Sex_Anal1:
    "images/Kitty_sex/Kitty_sex_anus_open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:

        ease 0.75 xzoom 1.0
        ease 0.25 xzoom 0.9
        pause 1.50
        ease 0.25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Kitty_Sex_Anal_Spunk_Heading_Over:
    "images/Kitty_sex/Kitty_sex_spunk_anal_over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8
    block:

        ease 0.75 xzoom 1.0
        pause 1.75
        ease 0.25 xzoom 1.0
        ease 2.25 xzoom 0.8
        repeat
image Kitty_Sex_Anal_Spunk_Heading_Under:
    "images/Kitty_sex/Kitty_sex_spunk_anal_under.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:

        ease 0.75 xzoom 1.0
        ease 0.25 xzoom 0.95
        pause 1.50
        ease 0.25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Kitty_Sex_Anal0:
    "images/Kitty_sex/Kitty_sex_anus_open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6




image Kitty_Anal_Zero_Anim0:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (500,600)
        zoom 1.4

image Kitty_Anal_Zero_Anim1:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (500,600)
        zoom 1.4
        block:
            ease 1 pos (500,570)
            pause 1
            ease 3 pos (500,600)
            repeat

image Kitty_Anal_Zero_Anim2:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (500,570)
        zoom 1.4
        block:
            ease 1 pos (500,450)
            pause 1
            ease 3 pos (500,570)
            repeat

image Kitty_Anal_Zero_Anim3:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (500,570)
        zoom 1.4
        block:
            ease 0.25 pos (500,450)
            pause 0.25
            ease 1.5 pos (500,570)
            repeat



image Kitty_Hotdog_Zero_Anim0:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (498,570)
        zoom 1.4

image Kitty_Hotdog_Zero_Anim1:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (498,500)
        zoom 1.4
        block:
            ease 1 pos (498,560)
            pause 0.5
            ease 1.5 pos (498,500)
            repeat

image Kitty_Hotdog_Zero_Anim2:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (500,510)
        zoom 1.4
        block:
            ease 0.5 pos (500,400)
            pause 0.5
            ease 1 pos (500,510)
            repeat

image Kitty_Hotdog_Body_Anim2:

    contains:
        subpixel True
        "Kitty_sex_body"
        pos (0,0)
        block:

            pause 0.30
            ease 0.50 pos (0,-10)
            pause 0.20
            ease 1 pos (0,0)
            repeat

image Kitty_Hotdog_Legs_Anim2:

    contains:
        subpixel True
        "Kitty_sex_legs"
        pos (0,0)
        block:

            pause 0.20
            ease 0.50 pos (0,-10)
            pause 0.20
            ease 1.1 pos (0,0)
            repeat





image Kitty_Footcock:
    contains:
        subpixel True
        "Zero_cock_blowjob"
        alpha 0.8
        zoom 0.7
        anchor (0.5,0.5)
        offset (465,70)
        pos (0,0)
    pos (750,230)

image Kitty_Footcock_Anim0:
    contains:
        subpixel True
        "Kitty_Footcock"
        pos (392,295)
    pos (750,230)

image Kitty_Footcock_Zero_Anim1:
    contains:
        subpixel True
        "Kitty_Footcock"
        pos (392,295)
        block:

            pause 0.5
            easein 0.75 ypos 360
            ease 0.25 ypos 355
            pause 1
            ease 2.50 ypos 270
            repeat
    pos (750,230)

image Kitty_Footcock_Zero_Anim2:
    contains:
        subpixel True
        "Kitty_Footcock"
        pos (392,295)
        block:

            pause 0.2
            easein 0.4 ypos 360
            ease 0.2 ypos 355
            pause 0.2
            ease 1.00 ypos 270
            repeat
    pos (750,230)

transform Kitty_Footcock_Zero_Anim1A():
    subpixel True
    offset (0,0)
    block:

        pause 0.5
        easein 0.75 yoffset 60
        ease 0.25 yoffset 55
        pause 1
        ease 1.50 yoffset -30
        repeat

transform Kitty_Footcock_Zero_Anim2A():
    subpixel True
    offset (0,0)
    block:

        pause 0.2
        easein 0.4 yoffset 60
        ease 0.2 yoffset 55
        pause 0.2
        ease 1.00 yoffset -30
        pause 0.2
        easein 0.4 yoffset 60
        ease 0.2 yoffset 55
        pause 0.2
        ease 1.00 yoffset -30
        repeat

transform Kitty_Footcock_Anim0A():
    subpixel True
    offset (0,-5)
    block:

        pause 0.5
        ease 1 yoffset 0
        pause 1
        ease 1.50 yoffset -5
        repeat

image Kitty_sex_legs_FootAnim1:

    contains:
        subpixel True
        "Kitty_sex_legs"
        pos (0,0)
        block:

            pause 0.5
            easein 0.75 pos (0,-65)
            ease 0.25 pos (0,-60)
            pause 1
            ease 2.50 pos (0,25)
            repeat
    pos (750,230)

image Kitty_sex_legs_FootAnim2:

    contains:
        subpixel True
        "Kitty_sex_legs"
        pos (0,0)
        block:

            pause 0.2
            easein 0.4 pos (0,-65)
            ease 0.2 pos (0,-60)
            pause 0.2
            ease 1.0 pos (0,25)
            repeat
    pos (750,230)

image Kitty_sex_legs_FootAnim0:

    contains:
        subpixel True
        "Kitty_sex_legs"
        pos (0,0)
    pos (750,230)

transform Kitty_sex_legs_FootAnim1A():

    subpixel True
    offset (0,0)
    block:

        pause 0.5
        easein 0.75 yoffset -65
        ease 0.25 yoffset -60
        pause 1
        ease 1.50 yoffset 25
        repeat

transform Kitty_sex_legs_FootAnim2A():

    subpixel True
    offset (0,0)
    block:

        pause 0.2
        easein 0.4 yoffset -65
        ease 0.2 yoffset -60
        pause 0.2
        ease 1.0 yoffset 25
        pause 0.2
        easein 0.4 yoffset -65
        ease 0.2 yoffset -60
        pause 0.2
        ease 1.0 yoffset 25
        repeat

transform Kitty_sex_legs_FootAnim0A():

    subpixel True
    offset (0,0)
    block:

        pause 0.5
        ease 1 yoffset -5
        pause 1
        ease 1.50 yoffset 0
        repeat





image Kitty_sex_body_FootAnim1:

    contains:
        subpixel True
        "Kitty_sex_body"
        pos (0,0)
        block:

            pause 0.5
            easein 0.75 pos (0,-25)
            ease 0.25 pos (0,-15)
            pause 1
            ease 2.50 pos (0,15)
            repeat
    pos (750,230)

image Kitty_sex_body_FootAnim2:

    contains:
        subpixel True
        "Kitty_sex_body"
        pos (0,0)
        block:

            pause 0.2
            easein 0.4 pos (0,-25)
            ease 0.2 pos (0,-15)
            pause 0.2
            ease 1.0 pos (0,15)
            repeat
    pos (750,230)

image Kitty_sex_body_FootAnim0:

    contains:
        subpixel True
        "Kitty_sex_body"
        pos (0,0)
    pos (750,230)

transform Kitty_sex_body_FootAnim1A():

    subpixel True
    offset (0,0)
    block:

        pause 0.5
        easein 0.75 yoffset -25
        ease 0.25 yoffset -15
        pause 1
        ease 1.50 yoffset 15
        repeat

transform Kitty_sex_body_FootAnim2A():

    subpixel True
    offset (0,0)
    block:

        pause 0.2
        easein 0.4 yoffset -25
        ease 0.2 yoffset -15
        pause 0.2
        ease 1.0 yoffset 15
        pause 0.2
        easein 0.4 yoffset -25
        ease 0.2 yoffset -15
        pause 0.2
        ease 1.0 yoffset 15
        repeat

transform Kitty_sex_body_FootAnim0A():

    subpixel True
    offset (0,0)
    block:

        pause 0.5
        ease 1 yoffset -5
        pause 1
        ease 1.50 yoffset 0
        repeat





label Kitty_Sex_Launch(Line=primary_action):
    $ girl_offhand_action = 0 if girl_offhand_action == "handjob" else girl_offhand_action





    $ Player.sprite = 1
    $ Line = "solo" if not Line else Line
    if Line == "sex":
        $ Player.cock_position = "sex"
        if offhand_action in ("fondle_pussy","dildo_pussy","eat_pussy"):
            $ offhand_action = 0
    elif Line == "anal":
        $ Player.cock_position = "anal"
        if offhand_action in ("finger_ass","dildo_anal","eat_ass"):
            $ offhand_action = 0
    elif Line == "hotdog":
        $ Player.cock_position = "out"
    elif Line == "footjob":
        $ show_feet = 1
        $ Player.cock_position = "footjob"
    elif Line == "massage":
        $ Player.sprite = 0
        $ Player.cock_position = 0
    else:
        $ Player.sprite = 0
        $ Player.cock_position = "out"
        $ action_speed = 0
    $ primary_action = Line

    if KittyX.pose == "doggy":
        call Kitty_Doggy_Launch (Line)
        return
    if renpy.showing("Kitty_sex_animation"):
        return
    $ action_speed = 0
    call Kitty_Hide (1)
    # show Kitty_sex_animation zorder 150
    # with dissolve
    return

label Kitty_Sex_Reset:
    if renpy.showing("Kitty_Doggy_Animation"):
        call Kitty_Doggy_Reset
        return
    if not renpy.showing("Kitty_sex_animation"):
        return
    $ KittyX.arm_pose = 2
    hide Kitty_sex_animation
    call Kitty_Hide

    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
        anchor (0.5, 0.0)
    with dissolve
    $ action_speed = 0
    return












image Kitty_Doggy_Animation:
    LiveComposite(

        (420,750),
        (0,0), ConditionSwitch(

            "not Player.sprite", "Kitty_Doggy_Body",
            "Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Doggy_Fuck2_Top",
                    "action_speed > 1", "Kitty_Doggy_Fuck_Top",
                    "action_speed ", "Kitty_Doggy_Anal_Head_Top",
                    "True", "Kitty_Doggy_Body",
                    ),
            "Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Doggy_Fuck2_Top",
                    "action_speed > 1", "Kitty_Doggy_Fuck_Top",
                    "True", "Kitty_Doggy_Body",
                    ),
            "True", "Kitty_Doggy_Body",
            ),
        (0,0), ConditionSwitch(

            "not Player.sprite", "Kitty_Doggy_Ass",
            "Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Kitty_Doggy_Fuck_Ass",
                    "action_speed ", "Kitty_Doggy_Anal_Head_Ass",
                    "True", "Kitty_Doggy_Ass",
                    ),
            "Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Kitty_Doggy_Fuck_Ass",
                    "True", "Kitty_Doggy_Ass",
                    ),
            "True", "Kitty_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(

            "Player.cock_position == 'foot'", ConditionSwitch(
                    "action_speed > 1", "Kitty_Doggy_Feet2",
                    "action_speed ", "Kitty_Doggy_Feet1",
                    "True", "Kitty_Doggy_Feet0",
                    ),
            "not Player.sprite and show_feet", "Kitty_Doggy_Feet0",
            "True", Null(),
            ),
        )
    align (0.6,0.0)



image Kitty_Doggy_Body:
    LiveComposite(

        (420,750),

        (0,105), "Kitty_Doggy_Head",


        (0,0), "images/KittyDoggy/Kitty_Doggy_Body.png",
        (0,0), ConditionSwitch(

            "not KittyX.bra", Null(),
            "KittyX.top_pulled_up", ConditionSwitch(
                    "KittyX.top and KittyX.top != 'towel' and KittyX.top != '_jacket'", Null(),
                    "KittyX.bra == '_dress' and KittyX.top and KittyX.top != 'towel'", "images/KittyDoggy/Kitty_Doggy_Bra_Dress_UpC.png",
                    "KittyX.bra == '_dress'", "images/KittyDoggy/Kitty_Doggy_Bra_Dress_Up.png",
                    "KittyX.bra == 'cami'", "images/KittyDoggy/Kitty_Doggy_Bra_Cami_Up.png",
                    "KittyX.bra == 'lace_bra'", "images/KittyDoggy/Kitty_Doggy_Bra_Lace.png",
                    "KittyX.bra == 'sports_bra'", "images/KittyDoggy/Kitty_Doggy_Bra_Sports_Up.png",
                    "KittyX.bra == 'bikini_top'", "images/KittyDoggy/Kitty_Doggy_Bra_Bikini_Up.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Bra.png",
                    ),
            "KittyX.bra == '_dress'", "images/KittyDoggy/Kitty_Doggy_Bra_Dress.png",
            "KittyX.bra == 'cami'", "images/KittyDoggy/Kitty_Doggy_Bra_Cami.png",
            "KittyX.bra == 'lace_bra'", "images/KittyDoggy/Kitty_Doggy_Bra_Lace.png",
            "KittyX.bra == 'sports_bra'", "images/KittyDoggy/Kitty_Doggy_Bra_Sports.png",
            "KittyX.bra == 'bikini_top'", "images/KittyDoggy/Kitty_Doggy_Bra_Bikini.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Bra.png",
            ),
        (0,0), ConditionSwitch(

            "KittyX.wet", "images/KittyDoggy/Kitty_Doggy_Body_Wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.top", Null(),
            "KittyX.top == '_jacket'", "images/KittyDoggy/Kitty_Doggy_Over_Jacket.png",
            "KittyX.top == 'red_shirt'", "images/KittyDoggy/Kitty_Doggy_Over_Red.png",
            "KittyX.top == 'pink_top'", "images/KittyDoggy/Kitty_Doggy_Over_Pink.png",
            "KittyX.top == 'towel' and not KittyX.top_pulled_up", "images/KittyDoggy/Kitty_Doggy_Over_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'back' in KittyX.spunk", "images/KittyDoggy/Kitty_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'fondle_breasts' or offhand_action == 'fondle_breasts'", "Kitty_Doggy_GropeBreast",
            "True", Null()
            ),


        )


    offset (-30,0)



image Kitty_Doggy_Head:
    LiveComposite(

        (420,750),


        (0,0), ConditionSwitch(


            "KittyX.blushing", "images/KittyDoggy/Kitty_Doggy_Head_Blush.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(

            "KittyX.mouth == 'normal'", "images/KittyDoggy/Kitty_Doggy_Mouth_Normal.png",
            "KittyX.mouth == 'lipbite'", "images/KittyDoggy/Kitty_Doggy_Mouth_Smile.png",
            "KittyX.mouth == 'sucking'", "images/KittyDoggy/Kitty_Doggy_Mouth_Tongue.png",
            "KittyX.mouth == 'kiss'", "images/KittyDoggy/Kitty_Doggy_Mouth_Kiss.png",
            "KittyX.mouth == 'sad'", "images/KittyDoggy/Kitty_Doggy_Mouth_Sad.png",
            "KittyX.mouth == 'smile'", "images/KittyDoggy/Kitty_Doggy_Mouth_Smile.png",
            "KittyX.mouth == 'grimace'", "images/KittyDoggy/Kitty_Doggy_Mouth_Smile.png",
            "KittyX.mouth == 'surprised'", "images/KittyDoggy/Kitty_Doggy_Mouth_Kiss.png",
            "KittyX.mouth == 'tongue'", "images/KittyDoggy/Kitty_Doggy_Mouth_Tongue.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Mouth_Normal.png",
            ),





        (0,0), ConditionSwitch(

            "'mouth' not in KittyX.spunk", Null(),


            "KittyX.mouth == 'lipbite'", "images/KittyDoggy/Kitty_Doggy_Spunk_Smile.png",
            "KittyX.mouth == 'smile'", "images/KittyDoggy/Kitty_Doggy_Spunk_Smile.png",
            "KittyX.mouth == 'grimace'", "images/KittyDoggy/Kitty_Doggy_Spunk_Smile.png",
            "KittyX.mouth == 'sucking'", "images/KittyDoggy/Kitty_Doggy_Spunk_Tongue.png",


            "KittyX.mouth == 'tongue'", "images/KittyDoggy/Kitty_Doggy_Spunk_Tongue.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Spunk_Normal.png",
            ),
        (0,0), ConditionSwitch(


            "KittyX.brows == 'angry'", "images/KittyDoggy/Kitty_Doggy_Brows_Angry.png",
            "KittyX.brows == 'sad'", "images/KittyDoggy/Kitty_Doggy_Brows_Sad.png",
            "KittyX.brows == 'surprised'", "images/KittyDoggy/Kitty_Doggy_Brows_Surprised.png",

            "True", "images/KittyDoggy/Kitty_Doggy_Brows_Normal.png",
            ),
        (0,0), "Kitty Doggy Blink",





        (0,0), ConditionSwitch(

            "'facial' in KittyX.spunk", "images/KittyDoggy/Kitty_Doggy_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.wet or KittyX.hair == '_wet'", "images/KittyDoggy/Kitty_Doggy_Hair_Wet.png",
            "KittyX.hair == 'long'", "images/KittyDoggy/Kitty_Doggy_Hair_Long.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Hair_Evo.png",
            ),
        (0,0), ConditionSwitch(

            "KittyX.wet", "images/KittyDoggy/Kitty_Doggy_Head_Wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'hair' in KittyX.spunk", "images/KittyDoggy/Kitty_Doggy_Spunk_Hair.png",
            "True", Null(),
            ),
        )
    zoom 0.8
































image Kitty Doggy Blink:

    ConditionSwitch(
        "KittyX.eyes == 'sexy'", "images/KittyDoggy/Kitty_Doggy_Eyes_Sexy.png",
        "KittyX.eyes == 'side'", "images/KittyDoggy/Kitty_Doggy_Eyes_Side.png",

        "KittyX.eyes == 'closed'", "images/KittyDoggy/Kitty_Doggy_Eyes_Closed.png",

        "KittyX.eyes == 'down'", "images/KittyDoggy/Kitty_Doggy_Eyes_Down.png",
        "KittyX.eyes == 'stunned'", "images/KittyDoggy/Kitty_Doggy_Eyes_Stunned.png",

        "KittyX.eyes == 'squint'", "images/KittyDoggy/Kitty_Doggy_Eyes_Sexy.png",
        "True", "images/KittyDoggy/Kitty_Doggy_Eyes_Normal.png",
        ),






    3

    "images/KittyDoggy/Kitty_Doggy_Eyes_Closed.png"
    0.25
    repeat

image Kitty_Doggy_Ass:
    LiveComposite(

        (420,750),
        (0,0), ConditionSwitch(

            "not KittyX.upskirt", Null(),
            "KittyX.legs == '_dress'", "images/KittyDoggy/Kitty_Doggy_Legs_Dress_Back.png",
            "KittyX.legs == 'shorts' and KittyX.grool", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_BackW.png",
            "KittyX.legs == 'shorts'", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_Back.png",
            "KittyX.legs == 'yoga_pants'", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.underwear_pulled_down or (KittyX.legs and KittyX.legs != 'blue_skirt' and not KittyX.upskirt)", Null(),
            "KittyX.underwear == 'green_panties' and KittyX.grool", "images/KittyDoggy/Kitty_Doggy_Panties_Green_BackW.png",
            "KittyX.underwear == 'green_panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Green_Back.png",
            "KittyX.underwear == 'bikini_bottoms' and KittyX.grool","images/KittyDoggy/Kitty_Doggy_Panties_Bikini_BackW.png",
            "KittyX.underwear == 'bikini_bottoms'","images/KittyDoggy/Kitty_Doggy_Panties_Bikini_Back.png",
            "KittyX.underwear == 'lace_panties'","images/KittyDoggy/Kitty_Doggy_Panties_Lace_Back.png",
            "True", Null(),
            ),
        (0,0), "images/KittyDoggy/Kitty_Doggy_Ass.png",
        (0,0), ConditionSwitch(

            "KittyX.wet", "images/KittyDoggy/Kitty_Doggy_Ass_Wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.hose == 'stockings'", "images/KittyDoggy/Kitty_Doggy_Hose_Stockings.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "(KittyX.legs and KittyX.legs != 'blue_skirt') and not KittyX.upskirt", Null(),
            "KittyX.hose == 'pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_Pantyhose.png",
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "not KittyX.underwear_pulled_down or (KittyX.legs and KittyX.legs != 'blue_skirt' and not KittyX.upskirt)", Null(),
            "KittyX.underwear == 'green_panties' and KittyX.grool", "images/KittyDoggy/Kitty_Doggy_Panties_Green_DownW.png",
            "KittyX.underwear == 'green_panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Green_Down.png",
            "KittyX.underwear == 'bikini_bottoms' and KittyX.grool", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini_DownW.png",
            "KittyX.underwear == 'bikini_bottoms'", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini_Down.png",
            "KittyX.underwear == 'lace_panties'","images/KittyDoggy/Kitty_Doggy_Panties_Lace_Down.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "KittyX.hose and KittyX.hose != 'garterbelt'", Null(),
            "KittyX.legs == 'capris' and KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Blue_Down.png",
            "KittyX.legs == 'black jeans' and KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Black_Down.png",
            "KittyX.legs == 'yoga_pants' and KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga_Down.png",
            "KittyX.legs == 'shorts' and KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_Down.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "Player.sprite and Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Pussy_Fucking3",
                    "action_speed > 1", "Kitty_Pussy_Fucking2",
                    "action_speed ", "Kitty_Pussy_Heading",
                    "True", "Kitty_Pussy_Static",
                    ),
            "primary_action == 'eat_pussy'", "images/KittyDoggy/Kitty_Doggy_Pussy_Open.png",
            "KittyX.legs and not KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Pussy_Closed.png",
            "KittyX.underwear and not KittyX.underwear_pulled_down", "images/KittyDoggy/Kitty_Doggy_Pussy_Closed.png",
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'", "Kitty_Pussy_Fingering",
            "primary_action == 'dildo_pussy'", "Kitty_Pussy_Fucking2",
            "True", "images/KittyDoggy/Kitty_Doggy_Pussy_Closed.png",
            ),

        (0,0), ConditionSwitch(

            "'in' in KittyX.spunk and Player.cock_position == 'in'",Null(),
            "'in' in KittyX.spunk ", "images/JeanDoggy/Jean_Doggy_SpunkPussyClosed.png",
            "KittyX.grool and Player.cock_position == 'in'", "images/Kitty_doggy/Kitty_doggy_pussy_wet_open.png",
            "KittyX.grool", "images/Kitty_doggy/Kitty_doggy_pussy_wet_closed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.pubes", Null(),
            "Player.sprite and Player.cock_position == 'in'", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo_pussy'", Null(),
            "(KittyX.legs and KittyX.legs != 'blue_skirt') and not KittyX.upskirt", Null(),
            "KittyX.underwear_pulled_down and primary_action == 'eat_pussy'", "images/KittyDoggy/Kitty_Doggy_Pubes_Open.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", "images/KittyDoggy/Kitty_Doggy_Pubes.png",
            "KittyX.underwear", "images/KittyDoggy/Kitty_Doggy_PubesC.png",
            "KittyX.hose == 'pantyhose' and primary_action == 'eat_pussy'", "images/KittyDoggy/Kitty_Doggy_Pubes_OpenC.png",
            "KittyX.hose == 'pantyhose'", "images/KittyDoggy/Kitty_Doggy_PubesC.png",
            "primary_action == 'eat_pussy'", "images/KittyDoggy/Kitty_Doggy_Pubes_Open.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Pubes.png",
            ),
        (0,0), ConditionSwitch(

            "Player.sprite", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo_pussy'", Null(),
            "KittyX.piercings == 'barbell'", "images/KittyDoggy/Kitty_Doggy_Pierce_Barbell.png",
            "KittyX.piercings == 'ring' and KittyX.underwear and not KittyX.underwear_pulled_down", "images/KittyDoggy/Kitty_Doggy_Pierce_RingC.png",
            "KittyX.piercings == 'ring' and KittyX.hose == 'pantyhose' and not (KittyX.underwear and KittyX.underwear_pulled_down)", "images/KittyDoggy/Kitty_Doggy_Pierce_RingC.png",
            "KittyX.piercings == 'ring' and KittyX.legs and KittyX.legs != 'blue_skirt' and not KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Pierce_RingC.png",
            "KittyX.piercings == 'ring'", "images/KittyDoggy/Kitty_Doggy_Pierce_Ring.png",
            "True", Null(),
            ),


        (0,0), ConditionSwitch(

            "Player.sprite and Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Anal_Fucking2",
                    "action_speed > 1", "Kitty_Anal_Fucking",
                    "action_speed ", "Kitty_Anal_Heading",
                    "True", "Kitty_Anal",
                    ),


            "KittyX.legs and not KittyX.upskirt", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "KittyX.underwear and not KittyX.underwear_pulled_down", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "primary_action == 'finger_ass' or offhand_action == 'finger_ass'", "Kitty_Anal_Fingering",
            "primary_action == 'dildo_anal'", "Kitty_Anal_Fucking",
            "KittyX.used_to_anal", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "True", "images/JeanDoggy/Jean_Doggy_Asshole_Tight.png",
            ),









        (0,0), ConditionSwitch(

            "KittyX.underwear_pulled_down or not KittyX.underwear", Null(),
            "Player.sprite and (Player.cock_position == 'in' or Player.cock_position == 'anal')", Null(),


            "KittyX.underwear == 'green_panties' and KittyX.grool", "images/KittyDoggy/Kitty_Doggy_Panties_GreenW.png",
            "KittyX.underwear == 'green_panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Green.png",
            "KittyX.underwear == 'lace_panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Lace.png",
            "KittyX.underwear == 'bikini_bottoms' and KittyX.grool", "images/KittyDoggy/Kitty_Doggy_Panties_BikiniW.png",
            "KittyX.underwear == 'bikini_bottoms'", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Panties_Green.png",
            ),
        (0,0), ConditionSwitch(

            "Player.sprite and (Player.cock_position == 'in' or Player.cock_position == 'anal')", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo_pussy'", Null(),

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "(KittyX.legs or KittyX.legs == 'blue_skirt') or not KittyX.upskirt", Null(),
            "KittyX.hose == 'pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_Pantyhose.png",
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.legs == '_dress'", ConditionSwitch(
                    "KittyX.upskirt and Player.sprite and Player.cock_position == 'anal' and action_speed" , "images/KittyDoggy/Kitty_Doggy_Legs_Dress_Up.png",
                    "KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Dress_Up.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Dress.png",
                    ),
            "KittyX.legs == 'blue_skirt'", ConditionSwitch(
                    "KittyX.upskirt and Player.sprite and Player.cock_position == 'anal' and action_speed" , "images/KittyDoggy/Kitty_Doggy_Legs_BlueSkirt_Up.png",
                    "KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_BlueSkirt_Up.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_BlueSkirt.png",
                    ),

            "KittyX.upskirt", Null(),
            "KittyX.legs == 'capris'", ConditionSwitch(

                    "KittyX.grool > 1", "images/KittyDoggy/Kitty_Doggy_Legs_BlueW.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Blue.png",
                    ),
            "KittyX.legs == 'black jeans'", ConditionSwitch(

                    "KittyX.grool > 1", "images/KittyDoggy/Kitty_Doggy_Legs_BlackW.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Black.png",
                    ),
            "KittyX.legs == 'yoga_pants'", ConditionSwitch(

                    "KittyX.grool > 1", "images/KittyDoggy/Kitty_Doggy_Legs_YogaW.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga.png",
                    ),
            "KittyX.legs == 'shorts'", ConditionSwitch(

                    "KittyX.grool > 1", "images/KittyDoggy/Kitty_Doggy_Legs_ShortsW.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts.png",
                    ),





            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.legs == 'blue_skirt' and KittyX.upskirt", Null(),
            "KittyX.legs == '_dress' and KittyX.upskirt", Null(),
            "KittyX.top == 'pink_top'", "images/KittyDoggy/Kitty_Doggy_Over_Pink_Tail.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.legs == '_dress' and KittyX.upskirt", Null(),
            "KittyX.top == 'towel' and KittyX.top_pulled_up", Null(),
            "KittyX.top == 'towel' and KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Towel_Up.png",
            "KittyX.top == 'towel'", "images/KittyDoggy/Kitty_Doggy_Legs_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'back' in KittyX.spunk", "images/KittyDoggy/Kitty_Doggy_Spunk_Ass.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "Player.sprite and Player.cock_position", Null(),
            "primary_action == 'eat_pussy'", "doggy_licking_pussy",
            "primary_action == 'eat_ass'", "doggy_licking_ass",
            "True", Null()
            ),
        (0,0), ConditionSwitch(

            "not Player.sprite or Player.cock_position != 'out'", Null(),

            "True", "images/KittyDoggy/Kitty_Doggy_HotdogBack.png",
            ),
        (0,0), ConditionSwitch(

            "not Player.sprite or Player.cock_position != 'out'", Null(),


            "action_speed ", AlphaMask("Zero_hotdog_moving", "images/Kitty_doggy/Rogue_Doggy_HotdogMask.png"),
            "True", AlphaMask("Zero_hotdog_static", "images/Kitty_doggy/Rogue_Doggy_HotdogMask.png"),
            ),






        )


image Kitty_Doggy_Feet:
    contains:
        AlphaMask("Kitty_Doggy_Shins", "images/KittyDoggy/Kitty_Doggy_Feet_Mask.png")

image Kitty_Doggy_Shins:



    contains:

        ConditionSwitch(
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Hole.png",
            "KittyX.hose and KittyX.hose != 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Hose.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Feet_Legs.png"
            )
    contains:

        ConditionSwitch(
            "KittyX.legs == 'capris'", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Blue.png",
            "KittyX.legs == 'black jeans'", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Black.png",
            "KittyX.legs == 'yoga_pants'", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Yoga.png",
            "True", Null(),
            )
    contains:



        ConditionSwitch(
            "not Player.sprite or Player.cock_position == 'foot'", ConditionSwitch(
                    "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Feet_Hose_HoleF.png",
                    "KittyX.hose and KittyX.hose != 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Feet_HoseF.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_FeetF.png"
                    ),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Feet_Hose_Hole.png",
            "KittyX.hose and KittyX.hose != 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Feet_Hose.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Feet.png"
            )












image Kitty_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom 0.55
        offset (110,420)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10
            ease 1 rotate 0
            repeat

















image Zero_Kitty_Hotdog_Static:


    contains:
        "Zero_cock_doggy_out"
        pos (175, 370)

image Zero_Kitty_Hotdog_Moving:


    contains:
        "Zero_cock_doggy_out"
        pos (175, 370)
        block:
            ease 1 ypos 330
            ease 1 ypos 420
            repeat






















image Zero_Kitty_Doggy_Static:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (169,545)
        block:
            ease 1 ypos 540
            pause 1
            ease 3 ypos 545
            repeat

image Zero_Kitty_Doggy_Heading:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (171,545)
        block:
            ease 1 xpos 168 ypos 500
            pause 1
            ease 3 xpos 171 ypos 545
            repeat

image Zero_Kitty_Doggy_Fucking2:

    contains:
        "Zero_cock_doggy_in"
        pos (169,500)
        block:
            ease 0.5 ypos 440
            pause 0.25
            ease 1.75 ypos 500
            repeat

image Zero_Kitty_Doggy_Fucking3:

    contains:
        "Zero_cock_doggy_in"
        pos (169,500)
        block:
            ease 0.2 ypos 440
            pause 0.1
            ease 0.6 ypos 500
            repeat

image Kitty_Pussy_Mask:


    contains:

        "images/Rogue_doggy/Rogue_doggy_sex_mask.png"
        anchor (0.52,0.69)
        pos (217,518)
        xzoom 0.6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom 0.6
            repeat

image Kitty_Pussy_Mask_Static:


    contains:

        "images/Rogue_doggy/Rogue_doggy_sex_mask.png"
        anchor (0.52,0.69)
        pos (217,518)
        xzoom 0.6
        block:
            ease 1 xzoom 0.65
            pause 1
            ease 3 xzoom 0.6
            repeat


































image Kitty_Pussy_Static:

    subpixel True
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom 0.6
        block:
            ease 1 xzoom 0.65
            pause 1
            ease 3 xzoom 0.6
            repeat
    contains:
        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Kitty_Doggy_Static", "Kitty_Pussy_Mask_Static")
    contains:


        AlphaMask("Kitty_PussyHole_Static", "Kitty_Pussy_Hole_Mask_Static")

image Kitty_Pussy_Hole_Mask_Static:

    contains:

        AlphaMask("images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png", "images/Rogue_doggy/Rogue_doggy_sex_mask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom 0.6
        block:
            ease 1 xzoom 0.65
            pause 1
            ease 3 xzoom 0.6
            repeat

image Kitty_PussyHole_Static:

    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha 0.9
        block:
            ease 1 ypos 512
            pause 1
            ease 3 ypos 515
            repeat


image Kitty_Pussy_Heading:

    subpixel True
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom 0.6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom 0.6
            repeat
    contains:
        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Kitty_Doggy_Heading", "Kitty_Pussy_Mask")
    contains:


        AlphaMask("Kitty_Pussy_Heading_Flap", "Kitty_Pussy_Hole_Mask")


image Kitty_Pussy_Hole_Mask:

    contains:

        AlphaMask("images/JeanDoggy/Jean_Doggy_Pussy_FHole.png", "images/Rogue_doggy/Rogue_doggy_sex_mask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom 0.6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom 0.6
            repeat

image Kitty_Pussy_Heading_Flap:

    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha 0.9
        block:
            ease 1 ypos 505
            pause 1
            ease 3 ypos 515
            repeat


image Kitty_Pussy_Fingering:

    subpixel True
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom 0.6
        block:
            ease 1 xzoom 0.9
            pause 1
            ease 3 xzoom 0.6
            repeat
    contains:
        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",

            "True", Null(),
            ),
    contains:

        AlphaMask("Zero_Pussy_Finger", "Rogue_Pussy_Mask")
    contains:



        AlphaMask("Kitty_Pussy_Heading_Flap", "Kitty_Pussy_Hole_Mask")



image Kitty_Pussy_Fucking2:

    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png"
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "primary_action == 'dildo_pussy'", AlphaMask("Rogue_Doggy_Fucking_Dildo", "images/Rogue_doggy/Rogue_doggy_sex_mask.png"),
            "True",AlphaMask("Zero_Kitty_Doggy_Fucking2", "images/Rogue_doggy/Rogue_doggy_sex_mask.png"),
            ),



image Kitty_Pussy_Fucking3:

    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png"
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Kitty_Doggy_Fucking3", "images/Rogue_doggy/Rogue_doggy_sex_mask.png")





image Kitty_Anal:

    contains:

        "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png"
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:
        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        "Zero_cock_doggy_in"
        pos (172,500)

image Kitty_Anal_Fingering:

    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png"
    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom 0.6
        block:
            ease 0.5 zoom 0.75
            pause 0.5
            ease 1.5 zoom 0.6
            repeat
    contains:
        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",

            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Doggy_Anal_Finger", "Rogue_Doggy_Anal_Fingering_Mask")


image Kitty_Anal_Heading:

    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png"
    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom 0.5
        block:
            ease 0.5 zoom 1
            pause 0.5
            ease 1.5 zoom 0.5
            repeat
    contains:
        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Kitty_Doggy_Anal_Heading", "Zero_Kitty_Doggy_Anal_HeadingJunk")
    contains:

        AlphaMask("Zero_Kitty_Doggy_Anal_Heading", "Kitty_Doggy_Anal_Heading_Mask")

image Zero_Kitty_Doggy_Anal_Heading:

    contains:
        "Zero_cock_doggy_in"
        pos (172,500)
        block:
            ease 0.5 ypos 450
            pause 0.25
            ease 1.75 ypos 500
            repeat

image Zero_Kitty_Doggy_Anal_HeadingJunk:

    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease 0.5 ypos 550
            pause 0.25
            ease 1.75 ypos 600
            repeat

image Kitty_Doggy_Anal_Heading_Mask:

    contains:
        "images/Rogue_doggy/Rogue_doggy_anal_mask.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom 0.5
        block:
            ease 0.5 zoom 1
            pause 0.5
            ease 1.5 zoom 0.5
            repeat

image Kitty_Doggy_Anal_Head_Top:

    contains:
        subpixel True
        "Kitty_Doggy_Body"
        ypos 0
        block:
            pause 0.4
            ease 0.3 ypos -5
            easeout 1 ypos 0
            pause 0.8
            repeat

image Kitty_Doggy_Anal_Head_Ass:

    contains:
        subpixel True
        "Kitty_Doggy_Ass"
        ypos 0
        block:
            pause 0.4
            ease 0.2 ypos -10
            easeout 0.1 ypos -7
            easein 0.9 ypos 0
            pause 0.9
            repeat


image Zero_Kitty_Doggy_Anal1:

    contains:
        "Zero_cock_doggy_in"
        pos (172,460)
        block:
            ease 0.5 ypos 395
            pause 0.25
            ease 1.75 ypos 460
            repeat

image Kitty_Anal_Fucking:

    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png"
    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom 0.5
        block:
            pause 0.25
            ease 0.25 zoom 1
            pause 0.75
            ease 1 zoom 0.95
            pause 0.25
            repeat
    contains:
        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(

            "primary_action == 'dildo_anal'", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/Rogue_doggy/Rogue_doggy_anal_mask.png"),
            "True", AlphaMask("Zero_Kitty_Doggy_Anal1", "images/Rogue_doggy/Rogue_doggy_anal_mask.png"),
            ),


image Kitty_Doggy_Anal_FullMask:
    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png"
    contains:



        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )

image Kitty_Doggy_Fuck_Top:

    contains:
        subpixel True
        "Kitty_Doggy_Body"
        ypos 0
        pause 0.4
        block:
            ease 0.2 ypos -10
            pause 0.3
            ease 2 ypos 0
            repeat

image Kitty_Doggy_Fuck_Ass:

    contains:
        subpixel True
        "Kitty_Doggy_Ass"
        ypos 0
        block:
            pause 0.4
            ease 0.2 ypos -15
            ease 0.1 ypos -5
            pause 0.2
            ease 1.6 ypos 0
            repeat



image Zero_Kitty_Doggy_Anal2:

    contains:
        "Zero_cock_doggy_in"
        pos (172,460)
        block:
            ease 0.2 ypos 395
            pause 0.1
            ease 0.6 ypos 465
            repeat

image Kitty_Anal_Fucking2:

    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png"
    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom 0.5
        block:
            pause 0.1
            ease 0.1 zoom 1
            pause 0.3
            ease 0.3 zoom 0.95
            pause 0.1
            repeat
    contains:






        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Kitty_Doggy_Anal2", "images/Rogue_doggy/Rogue_doggy_anal_mask.png")

image Kitty_Doggy_Fuck2_Top:

    contains:
        subpixel True
        "Kitty_Doggy_Body"
        ypos 0
        block:
            pause 0.15
            ease 0.1 ypos -20
            pause 0.1
            easein 0.5 ypos 0
            pause 0.05
            repeat

image Kitty_Doggy_Fuck2_Ass:

    contains:
        subpixel True
        "Kitty_Doggy_Ass"
        ypos 5
        block:
            pause 0.15
            ease 0.1 ypos -25
            ease 0.1 ypos -15
            pause 0.1
            ease 0.4 ypos 5
            pause 0.05
            repeat




image Kitty_Doggy_Feet0:

    contains:
        "Kitty_Doggy_Shins"
        pos (0, -20)
        block:
            subpixel True
            pause 0.5
            ease 2 ypos 0
            pause 0.5
            ease 2 ypos -20
            repeat
    contains:
        ConditionSwitch(
                "Player.sprite", "Zero_cock_doggy_out",
                "True", Null(),
                )
        zoom 1.2
        pos (158,520)
    contains:
        "Kitty_Doggy_Feet"
        pos (0, -20)
        block:
            subpixel True
            pause 0.5
            ease 2 ypos 0
            pause 0.5
            ease 2 ypos -20
            repeat

image Kitty_Doggy_Feet1:

    contains:
        "Kitty_Doggy_Shins"
        pos (0, -20)
        block:
            pause 0.3
            ease 1.7 ypos 100
            ease 1 ypos -20
            repeat
    contains:
        "Zero_cock_doggy_out"
        zoom 1.2
        pos (158,520)
        block:
            pause 0.4
            ease 1.7 ypos 540
            ease 0.9 ypos 520
            repeat
    contains:
        "Kitty_Doggy_Feet"
        pos (0, -20)
        block:
            pause 0.3
            ease 1.7 ypos 100
            ease 1 ypos -20
            repeat

image Kitty_Doggy_Feet2:

    contains:
        "Kitty_Doggy_Shins"
        pos (0, -20)
        block:
            pause 0.05
            ease 0.6 ypos 110
            ease 0.3 ypos -20
            repeat
    contains:
        "Zero_cock_doggy_out"
        zoom 1.2
        pos (158,520)
        block:
            pause 0.07
            ease 0.6 ypos 540
            ease 0.28 ypos 520
            repeat
    contains:
        "Kitty_Doggy_Feet"
        pos (0, -20)
        block:
            pause 0.05
            ease 0.6 ypos 110
            ease 0.3 ypos -20
            repeat




label Kitty_Doggy_Launch(Line=primary_action):
    if renpy.showing("Kitty_Doggy_Animation"):
        return
    $ action_speed = 0
    call Kitty_Hide (1)
    # show Kitty_Doggy_Animation zorder 150 at sprite_location(stage_center+50)
    # with dissolve
    return

label Kitty_Doggy_Reset:
    if not renpy.showing("Kitty_Doggy_Animation"):
        return

    $ KittyX.arm_pose = 2
    $ KittyX.spriteVer = 0
    hide Kitty_Doggy_Animation
    call Kitty_Hide
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        zoom 1
        offset (0,0)
        anchor (0.6, 0.0)
    with dissolve
    $ action_speed = 0
    return













image Kitty_blowjob_animation:
    LiveComposite(
        (858,928),
        (0,0), ConditionSwitch(

            "action_speed == 0", At("Kitty_BJ_Backdrop", blowjob_starting()),
            "action_speed == 1", At("Kitty_BJ_Backdrop", blowjob_licking_body()),
            "action_speed == 2", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_2()),
            "action_speed == 3", At("Kitty_BJ_Backdrop", blowjob_sucking_body()),
            "action_speed == 4", At("Kitty_BJ_Backdrop", blowjob_deepthroat_body()),
            "action_speed == 5", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_5()),
            "action_speed == 6", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_6()),
            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(

            "action_speed == 0", At("Kitty_BJ_Head", blowjob_starting()),
            "action_speed == 1", At("Kitty_BJ_Head", blowjob_licking()),
            "action_speed == 2", At("Kitty_BJ_Head", blowjob_heading()),
            "action_speed == 3", At("Kitty_BJ_Head", blowjob_sucking()),
            "action_speed == 4", At("Kitty_BJ_Head", blowjob_deepthroat()),
            "action_speed == 5", At("Kitty_BJ_Head", Kitty_BJ_Head_5()),
            "action_speed == 6", At("Kitty_BJ_Head", Kitty_BJ_Head_6()),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "action_speed == 0", At("Zero_cock_blowjob", blowjob_starting_cock()),
            "action_speed == 1", At("Zero_cock_blowjob", blowjob_licking_cock()),
            "action_speed >= 2", At("Zero_cock_blowjob", blowjob_straight_cock()),



            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(

            "action_speed < 3", Null(),
            "action_speed == 3", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MouthSuckingMask"), blowjob_sucking()),
            "action_speed == 4", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MouthSuckingMask"), blowjob_deepthroat()),
            "action_speed == 6", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MouthSuckingMask"), Kitty_BJ_Head_6()),
            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(

            "action_speed == 2", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MaskHeadingComposite"), blowjob_heading()),
            "action_speed == 5", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MaskHeadingComposite"), Kitty_BJ_Head_5()),
            "True", Null(),
            ),
        (325,490), ConditionSwitch(

            "action_speed < 3 or 'mouth' not in KittyX.spunk", Null(),
            "action_speed == 3", At("KittySuckingSpunk", blowjob_sucking()),
            "action_speed == 4", At("KittySuckingSpunk", blowjob_deepthroat()),
            "action_speed == 6", At("KittySuckingSpunk", Kitty_BJ_Head_6()),
            "True", Null(),
            ),
        (325,490), ConditionSwitch(

            "action_speed == 2 and 'mouth' in KittyX.spunk", At("Kitty_BJ_MaskHeadingSpunk", blowjob_heading()),
            "action_speed == 5 and 'mouth' in KittyX.spunk", At("Kitty_BJ_MaskHeadingSpunk", Kitty_BJ_Head_5()),
            "True", Null(),
            ),
        )
    zoom 0.55
    anchor (.5,.5)

image Kitty_BJ_hairback:

    ConditionSwitch(
            "KittyX.wet and KittyX.hair == 'evo'", "images/KittyBJFace/Kitty_BJ_hairbackWet.png",
            "KittyX.hair == 'long'", "images/KittyBJFace/Kitty_BJ_hairbackWet.png",
            "True", Null(),
            ),
    zoom 1.4
    anchor (0.5, 0.5)
    yoffset 50







image Kitty_BJ_Backdrop:

    LiveComposite(
        (858,928),
        (-375,250), ConditionSwitch(

            "'blanket' in KittyX.recent_history", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.top == 'red_shirt'", "images/KittyBJFace/Kitty_BJ_Over_RedUnder.png",
            "True", Null(),
            ),
        (0,0),"images/KittyBJFace/Kitty_BJ_Body.png",

        (0,0), ConditionSwitch(

            "KittyX.neck == 'gold necklace'", "images/KittyBJFace/Kitty_BJ_Neck_Gold.png",
            "KittyX.neck == 'star necklace'", "images/KittyBJFace/Kitty_BJ_Neck_Star.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.piercings", Null(),
            "KittyX.piercings == 'ring'", "images/KittyBJFace/Kitty_BJ_PierceRing.png",
            "True", "images/KittyBJFace/Kitty_BJ_PierceBall.png",
            ),
        (0,0), ConditionSwitch(

            "not KittyX.wet", Null(),
            "True", "images/KittyBJFace/Kitty_BJ_Wet_Body.png",
            ),

        (0,0), ConditionSwitch(

            "not KittyX.bra", Null(),
            "KittyX.bra == 'lace_bra'", "images/KittyBJFace/Kitty_BJ_Bra_Lace.png",
            "KittyX.bra == 'sports_bra'", "images/KittyBJFace/Kitty_BJ_Bra_Sport.png",
            "KittyX.bra == 'bra'", "images/KittyBJFace/Kitty_BJ_Bra.png",
            "KittyX.bra == 'cami'", "images/KittyBJFace/Kitty_BJ_Bra_Cami.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "not KittyX.top", Null(),
            "KittyX.top == 'pink_top'", "images/KittyBJFace/Kitty_BJ_Over_PinkShirt.png",
            "KittyX.top == 'red_shirt'", "images/KittyBJFace/Kitty_BJ_Over_RedShirt.png",
            "KittyX.top == 'towel'", "images/KittyBJFace/Kitty_BJ_Over_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'tits' not in KittyX.spunk", Null(),
            "True", "images/KittyBJFace/Kitty_BJ_Spunk_Body.png",
            ),
        )
    zoom 1.5
    offset (-300,-200)

image Kitty_BJ_Head:
    LiveComposite(
        (858,928),
        (0,0), ConditionSwitch(

            "KittyX.wet or KittyX.hair == '_wet'", "images/KittyBJFace/Kitty_BJ_hairbackWet.png",
            "True", Null(),
            ),
















        (0,0), ConditionSwitch(

            "action_speed <= 2 or action_speed == 5 or not renpy.showing('Kitty_blowjob_animation')", ConditionSwitch(

                    "KittyX.wet", ConditionSwitch(

                            "KittyX.blushing", "images/KittyBJFace/Kitty_BJ_FaceClosed_Wet_Blush.png",
                            "True", "images/KittyBJFace/Kitty_BJ_FaceClosed_Wet.png",
                            ),
                    "KittyX.blushing", "images/KittyBJFace/Kitty_BJ_FaceClosed_Blush.png",
                    "True", "images/KittyBJFace/Kitty_BJ_FaceClosed.png"
                    ),

            "KittyX.wet", ConditionSwitch(

                    "KittyX.blushing", "images/KittyBJFace/Kitty_BJ_FaceOpen_Wet_Blush.png",
                    "True", "images/KittyBJFace/Kitty_BJ_FaceOpen_Wet.png",
                    ),
            "KittyX.blushing", "images/KittyBJFace/Kitty_BJ_FaceOpen_Blush.png",
            "True",  "images/KittyBJFace/Kitty_BJ_FaceOpen.png"
            ),
        (0,0), ConditionSwitch(

            "action_speed and renpy.showing('Kitty_blowjob_animation')", ConditionSwitch(

                    "action_speed == 1", "images/KittyBJFace/Kitty_BJ_Mouth_Tongue.png",
                    "(action_speed== 2 or action_speed == 5)", Null(),
                    "action_speed == 3", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png",
                    "action_speed == 4", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png",
                    "action_speed == 6", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png",
                    "True", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png",
                    ),
            "action_speed == 3 and renpy.showing('Kitty_TJ_Animation')", "images/KittyBJFace/Kitty_BJ_Mouth_Tongue.png",
            "action_speed >= 5 and renpy.showing('Kitty_TJ_Animation')", "images/KittyBJFace/Kitty_BJ_Mouth_Kiss.png",
            "KittyX.mouth == 'normal'", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            "KittyX.mouth == 'lipbite'", "images/KittyBJFace/Kitty_BJ_Mouth_Lipbite.png",
            "KittyX.mouth == 'sucking'", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png",
            "KittyX.mouth == 'kiss'", "images/KittyBJFace/Kitty_BJ_Mouth_Kiss.png",
            "KittyX.mouth == 'sad'", "images/KittyBJFace/Kitty_BJ_Mouth_Sad.png",
            "KittyX.mouth == 'smile'", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            "KittyX.mouth == 'grimace'", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            "KittyX.mouth == 'surprised'", "images/KittyBJFace/Kitty_BJ_Mouth_Surprised.png",
            "KittyX.mouth == 'tongue'", "images/KittyBJFace/Kitty_BJ_Mouth_Tongue.png",
            "True", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            ),
        (428,605), ConditionSwitch(


            "not renpy.showing('Kitty_blowjob_animation')", Null(),
            "action_speed == 2", At("Kitty_BJ_MouthHeading", Kitty_BJ_MouthAnim()),
            "action_speed == 5", At("Kitty_BJ_MouthHeading", Kitty_BJ_MouthAnimC()),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'mouth' not in KittyX.spunk", Null(),
            "action_speed and renpy.showing('Kitty_blowjob_animation')", ConditionSwitch(

                    "action_speed == 1", "images/KittyBJFace/Kitty_BJ_Spunk_Tongue.png",
                    "(action_speed== 2 or action_speed == 5)", Null(),
                    "action_speed == 3", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png",
                    "action_speed == 4", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png",
                    "True", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png",
                    ),
            "action_speed >= 5 and renpy.showing('Kitty_TJ_Animation')", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "KittyX.mouth == 'normal'", "images/KittyBJFace/Kitty_BJ_Spunk_Smile.png",
            "KittyX.mouth == 'lipbite'", "images/KittyBJFace/Kitty_BJ_Spunk_Lipbite.png",
            "KittyX.mouth == 'kiss'", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "KittyX.mouth == 'sad'", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "KittyX.mouth == 'smile'", "images/KittyBJFace/Kitty_BJ_Spunk_Smile.png",
            "KittyX.mouth == 'surprised'", "images/KittyBJFace/Kitty_BJ_Spunk_Surprised.png",
            "KittyX.mouth == 'tongue'", "images/KittyBJFace/Kitty_BJ_Spunk_Tongue.png",
            "KittyX.mouth == 'sucking'", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.brows == 'normal'", "images/KittyBJFace/Kitty_BJ_Brows_Normal.png",
            "KittyX.brows == 'angry'", "images/KittyBJFace/Kitty_BJ_Brows_Angry.png",
            "KittyX.brows == 'sad'", "images/KittyBJFace/Kitty_BJ_Brows_Sad.png",
            "KittyX.brows == 'surprised'", "images/KittyBJFace/Kitty_BJ_Brows_Surprised.png",
            "KittyX.brows == 'confused'", "images/KittyBJFace/Kitty_BJ_Brows_Confused.png",
            "True", "images/KittyBJFace/Kitty_BJ_Brows_Normal.png",
            ),
        (0,0), "Kitty BJ Blink",

        (0,0), ConditionSwitch(

            "'facial' in KittyX.spunk", "images/KittyBJFace/Kitty_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.wet or KittyX.hair == '_wet'", "images/KittyBJFace/Kitty_BJ_Hair_Wet.png",
            "KittyX.hair == 'long'", "images/KittyBJFace/Kitty_BJ_Hair_Long.png",
            "KittyX.hair == 'evo'", "images/KittyBJFace/Kitty_BJ_Hair_Evo.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.wet", Null(),
            "action_speed > 2", "images/KittyBJFace/Kitty_BJ_Wet_HeadOpen.png",
            "True", "images/KittyBJFace/Kitty_BJ_Wet_HeadClosed.png",
            ),
        (0,0), ConditionSwitch(

            "'hair' in KittyX.spunk", "images/KittyBJFace/Kitty_BJ_Spunk_Hair.png",
            "True", Null(),
            ),
        )
    zoom 1.4
    anchor (0.5, 0.5)

image Kitty BJ Blink:

    ConditionSwitch(
            "KittyX.eyes == 'normal'", "images/KittyBJFace/Kitty_BJ_Eyes_Normal.png",
            "KittyX.eyes == 'sexy'", "images/KittyBJFace/Kitty_BJ_Eyes_Sexy.png",
            "KittyX.eyes == 'closed'", "images/KittyBJFace/Kitty_BJ_Eyes_Closed.png",
            "KittyX.eyes == 'surprised'", "images/KittyBJFace/Kitty_BJ_Eyes_Surprised.png",
            "KittyX.eyes == 'side'", "images/KittyBJFace/Kitty_BJ_Eyes_Side.png",
            "KittyX.eyes == 'stunned'", "images/KittyBJFace/Kitty_BJ_Eyes_Surprised.png",
            "KittyX.eyes == 'down'", "images/KittyBJFace/Kitty_BJ_Eyes_Down.png",
            "KittyX.eyes == 'manic'", "images/KittyBJFace/Kitty_BJ_Eyes_Surprised.png",
            "KittyX.eyes == 'squint'", "images/KittyBJFace/Kitty_BJ_Eyes_Squint.png",
            "True", "images/KittyBJFace/Kitty_BJ_Eyes_Normal.png",
            ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/KittyBJFace/Kitty_BJ_Eyes_Closed.png"
    0.25
    repeat

image Kitty_BJ_MouthHeading:

    contains:
        "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png"
        zoom 1.4
        anchor (0.50,0.65)

image Kitty_BJ_MouthSuckingMask:

    contains:
        "images/KittyBJFace/Kitty_BJ_Mouth_SuckingMask.png"
        zoom 1.4
    contains:
        ConditionSwitch(
            "'mouth' not in KittyX.spunk", Null(),
            "action_speed != 2 and action_speed != 5", Null(),
            "True", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png",
            )
        zoom 1.4

image Kitty_BJ_MaskHeading:

    contains:
        "images/KittyBJFace/Kitty_BJ_Mouth_SuckingMask.png"
        offset (-380,-595)

image Kitty_BJ_MaskHeadingComposite:

    LiveComposite(
        (858,928),
        (300,462), ConditionSwitch(
            "action_speed == 2", At("Kitty_BJ_MaskHeading", Kitty_BJ_MouthAnim()),
            "action_speed == 5", At("Kitty_BJ_MaskHeading", Kitty_BJ_MouthAnimC()),
            "True", Null(),
            ),
        )
    zoom 1.8

image Kitty_BJ_MaskHeadingSpunk:

    At("KittySuckingSpunk", Kitty_BJ_MouthAnim())
    zoom 1.8

image KittySuckingSpunk:
    contains:
        "images/KittyBJFace/Kitty_BJ_Spunk_SuckingO.png"
        zoom 1.4
        anchor (0.5, 0.5)

transform Kitty_BJ_MouthAnim():

    subpixel True
    zoom 0.7
    block:
        pause 0.40
        easeout 0.40 zoom 0.69
        linear 0.10 zoom 0.7
        easein 0.45 zoom 0.65
        pause 0.15

        easeout 0.25 zoom 0.7
        linear 0.10 zoom 0.69
        easein 0.30 zoom 0.7
        pause 0.35

        repeat
transform Kitty_BJ_MouthAnimC():

    subpixel True
    zoom 0.7
    block:
        pause 0.20
        ease 0.50 zoom 0.65
        pause 0.60
        ease 0.30 zoom 0.7
        pause 0.10
        ease 0.30 zoom 0.65
        pause 0.20
        ease 0.30 zoom 0.7
        repeat

image Blanket:
    contains:
        "images/KittyBJFace/Kitty_BJFace_Blanket.png"
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image Blanket = LiveComposite(
    (858,928),
    (0, 0), "images/KittyBJFace/Kitty_BJFace_Blanket.png"
    )




transform Kitty_BJ_Body_2():

    subpixel True
    offset (0,-40)
    block:
        ease 1 yoffset 15
        ease 1.5 offset (0,-40)
        repeat



transform Kitty_BJ_Head_5():

    subpixel True
    offset (0,-30)
    block:
        ease 1 yoffset -20
        ease 1.5 offset (0,-30)
        repeat
transform Kitty_BJ_Body_5():

    subpixel True
    offset (0,-30)
    block:
        ease 1 yoffset -20
        ease 1.5 offset (0,-30)
        repeat

transform Kitty_BJ_Head_6():

    ease 0.5 offset (0,230)
    block:
        subpixel True
        ease 1 yoffset 250
        pause 0.5
        ease 2 yoffset 230
        repeat
transform Kitty_BJ_Body_6():

    ease 0.5 offset (0,190)
    block:
        subpixel True
        ease 1.2 yoffset 200
        pause 0.5
        ease 1.8 yoffset 190
        repeat






label Kitty_BJ_Launch(Line=primary_action):
    if renpy.showing("Kitty_blowjob_animation"):
        return

    call Kitty_Hide
    if Line == "L" or Line == "cum":
        show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(stage_center):
            alpha 1
            ease 1 zoom 2.5 offset (150,80)
        with dissolve
    else:
        show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(stage_center):
            alpha 1
            zoom 2.5 offset (150,80)
        with dissolve

    if Line == "L":
        if taboo:
            if len(Present) >= 2:
                if Present[0] != KittyX:
                    "[KittyX.name] looks back at [Present[0].name] to see if she's watching."
                elif Present[1] != KittyX:
                    "[KittyX.name] looks back at [Present[1].name] to see if she's watching."
            else:
                "[KittyX.name] casually glances around to see if anyone can see her."
        if not KittyX.action_counter["blowjob"]:
            "[KittyX.name] hesitantly kneels down and touches her mouth to your cock."
        else:
            "[KittyX.name] kneels down and begins to suck on your cock."

    $ action_speed = 0

    if Line != "cum":
        $ primary_action = "blowjob"

    show Kitty_sprite zorder KittyX.sprite_layer:
        alpha 0
    # show Kitty_blowjob_animation zorder 150:
    #     pos (645,510)
    return

label Kitty_BJ_Reset:
    if not renpy.showing("Kitty_blowjob_animation"):
        return
    call Kitty_Hide
    $ action_speed = 0

    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(stage_center):
        alpha 1
        zoom 2.5 offset (150,80)
    with dissolve

    show Kitty_sprite zorder KittyX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause 0.5
        ease 0.5 zoom 1 offset (0,0)
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)

    return









image Kitty_TJ_Animation:

    contains:
        ConditionSwitch(

            "Player.sprite", ConditionSwitch(

                    "action_speed == 1", "Kitty_TJ_Body_1",
                    "action_speed == 2", "Kitty_TJ_Body_2",
                    "action_speed == 3", "Kitty_TJ_Body_3",
                    "action_speed >= 5", "Kitty_TJ_Body_5",
                    "True",       "Kitty_TJ_Body_0",
                    ),
            "True","Kitty_TJ_Body_0",
            ),
    zoom 1.35
    anchor (.5,.5)
    pos (600,605)


image Kitty_TJ_Torso:

    contains:

        "images/KittyBJFace/Kitty_TJ_Body.png"












































image Kitty_TJ_Arms:

    contains:

        "images/KittyBJFace/Kitty_TJ_Arms.png"

image Kitty_TJ_Tits:

    contains:


        ConditionSwitch(
            "Player.sprite and action_speed", "images/KittyBJFace/Kitty_TJ_Tits_Smooshed.png",
            "True", "images/KittyBJFace/Kitty_TJ_Tits.png",
            )






















































image Kitty_Mega_Mask:

    contains:
        Solid("#159457", xysize=(1750,1750))
        alpha 0.5





image Kitty_TJ_Body_0:

    contains:

        "Kitty_BJ_hairback"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,260)
        subpixel True
        block:
            ease 2.4 ypos 250
            ease 1.6 ypos 260
            repeat
    contains:

        "Kitty_TJ_Torso"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.4 ypos 325
            ease 1.6 ypos 330
            repeat
    contains:

        "Kitty_TJ_Arms"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.4 ypos 325
            ease 1.6 ypos 330
            repeat
    contains:

        "Kitty_BJ_Head"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,260)
        subpixel True
        block:
            ease 2.4 ypos 250
            ease 1.6 ypos 260
            repeat
    contains:

        "Kitty_TJ_Tits"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.4 ypos 325
            ease 1.6 ypos 330
            repeat
    contains:

        ConditionSwitch(
                    "Player.sprite", "Zero_cock_blowjob",
                    "True", Null(),
                    )
        subpixel True
        pos (640,150)
        anchor (0.5,0.5)
        zoom 0.4



image Kitty_TJ_Mask_1:
    contains:
        "images/KittyBJFace/Kitty_TJ_Mask.png"
        pos (100,60)
        anchor (0.5, 0.5)
        zoom 1.4
        subpixel True
        block:
            ease 2.9 ypos -40
            ease 1 ypos 60
            pause 0.1
            repeat

image Kitty_TJ_Body_1:

    contains:

        "Kitty_BJ_hairback"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,260)
        subpixel True
        block:
            ease 3 ypos 210
            ease 1 ypos 260
            repeat
    contains:

        "Kitty_TJ_Torso"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.8 ypos 280
            ease 1 ypos 330
            pause 0.2
            repeat
    contains:

        "Kitty_TJ_Arms"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.85 ypos 280
            ease 1 ypos 330
            pause 0.15
            repeat
    contains:

        "Kitty_BJ_Head"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,260)
        subpixel True
        block:
            ease 2.9 ypos 210
            ease 1 ypos 260
            pause 0.1
            repeat
    contains:

        "Kitty_TJ_Tits"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.9 ypos 280
            ease 1 ypos 330
            pause 0.1
            repeat
    contains:

        ConditionSwitch(
                    "Player.sprite", AlphaMask("Zero_cock_blowjob", "Kitty_TJ_Mask_1"),
                    "True", Null(),
                    )
        subpixel True
        pos (665,500)
        anchor (0.5,0.5)
        zoom 0.4
        block:
            ease 2.8 ypos 490
            ease 0.8 ypos 500
            pause 0.4
            repeat



image Kitty_TJ_Mask_2:
    contains:
        "images/KittyBJFace/Kitty_TJ_Mask.png"
        pos (100,60)
        anchor (0.5, 0.5)
        zoom 1.4
        subpixel True
        block:
            ease 0.71 ypos -15
            ease 0.27 ypos 60
            pause 0.02
            repeat

image Kitty_TJ_Body_2:

    contains:

        "Kitty_BJ_hairback"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,260)
        subpixel True
        block:
            ease 0.7 ypos 215
            ease 0.25 ypos 260
            pause 0.05
            repeat
    contains:

        "Kitty_TJ_Torso"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 0.65 ypos 285
            ease 0.25 ypos 330
            pause 0.1
            repeat
    contains:

        "Kitty_TJ_Arms"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 0.68 ypos 285
            ease 0.25 ypos 330
            pause 0.07
            repeat
    contains:

        "Kitty_TJ_Tits"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 0.71 ypos 290
            ease 0.27 ypos 330
            pause 0.02
            repeat
    contains:

        "Kitty_BJ_Head"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,260)
        subpixel True
        block:
            ease 0.68 ypos 215
            ease 0.25 ypos 260
            pause 0.07
            repeat
    contains:

        ConditionSwitch(
                    "Player.sprite", AlphaMask("Zero_cock_blowjob", "Kitty_TJ_Mask_2"),
                    "True", Null(),
                    )
        subpixel True
        pos (665,500)
        anchor (0.5,0.5)
        zoom 0.4
        block:
            ease 0.72 ypos 490
            ease 0.27 ypos 500
            pause 0.01
            repeat



image Kitty_TJ_Mask_3:
    contains:
        "images/KittyBJFace/Kitty_TJ_Mask.png"
        pos (100,140)
        anchor (0.5, 0.5)
        zoom 1.4
        subpixel True
        block:
            ease 2.2 ypos 90
            ease 0.6 ypos 140
            pause 0.2
            repeat

image Kitty_TJ_Body_3:

    contains:

        "Kitty_BJ_hairback"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (500,260)
        rotate 0
        subpixel True
        parallel:
            block:

                ease 2 pos (500,290)
                ease 0.6 pos (500,315)
                pause 0.4
                repeat 2
            block:

                ease 2.2 pos (500,290)
                ease 0.8 pos (520,320)
                ease 2.2 pos (510,290)
                ease 0.8 pos (520,320)
            block:

                ease 2 pos (500,290)
                ease 0.6 pos (500,315)
                pause 0.4
                repeat 2
            block:

                ease 2.2 pos (500,290)
                ease 0.8 pos (475,320)
                ease 2.2 pos (490,290)
                ease 0.8 pos (475,320)
            repeat
    contains:

        "Kitty_TJ_Torso"
        pos (545,360)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.2 ypos 340
            ease 0.6 ypos 360
            pause 0.2
            repeat
    contains:

        "Kitty_TJ_Arms"
        pos (545,360)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.2 ypos 340
            ease 0.6 ypos 360
            pause 0.2
            repeat
    contains:

        "Kitty_TJ_Tits"
        pos (545,360)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.2 ypos 340
            ease 0.6 ypos 360
            pause 0.2
            repeat
    contains:

        "Kitty_BJ_Head"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (500,310)
        subpixel True
        rotate 0
        parallel:
            block:

                ease 2 pos (500,290)
                ease 0.6 pos (500,315)
                pause 0.4
                repeat 2
            block:

                ease 2.2 pos (500,290)
                ease 0.8 pos (520,320)
                ease 2.2 pos (510,290)
                ease 0.8 pos (520,320)
            block:

                ease 2 pos (500,290)
                ease 0.6 pos (500,315)
                pause 0.4
                repeat 2
            block:

                ease 2.2 pos (500,290)
                ease 0.8 pos (475,320)
                ease 2.2 pos (490,290)
                ease 0.8 pos (475,320)
            repeat
        parallel:
            block:

                ease 2.2 rotate 0
                pause 3.8
            block:

                ease 2.2 rotate 0
                ease 0.8 rotate 10
                ease 2.2 rotate 0
                ease 0.8 rotate 5
            block:

                ease 2.2 rotate 0
                pause 3.8
            block:

                ease 2.2 rotate 0
                ease 0.8 rotate -10
                ease 2.2 rotate 0
                ease 0.8 rotate -5
            repeat
    contains:

        ConditionSwitch(
                    "Player.sprite", AlphaMask("Zero_cock_blowjob", "Kitty_TJ_Mask_3"),
                    "True", Null(),
                    )
        subpixel True
        pos (665,500)
        anchor (0.5,0.5)
        zoom 0.4



image Kitty_TJ_Mask_5:
    contains:
        "images/KittyBJFace/Kitty_TJ_Mask.png"
        pos (100,140)
        anchor (0.5, 0.5)
        zoom 1.4
        subpixel True
        block:
            ease 2.2 ypos 120
            ease 1.6 ypos 140
            pause 0.2
            repeat

image Kitty_TJ_Body_5:

    contains:

        "Kitty_BJ_hairback"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (500,260)
        rotate 0
        subpixel True
        block:

            ease 2 pos (500,304)
            ease 1.6 pos (500,307)
            pause 0.4
            repeat
    contains:

        "Kitty_TJ_Torso"
        pos (545,360)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.2 ypos 350
            ease 1.6 ypos 360
            pause 0.2
            repeat
    contains:

        "Kitty_TJ_Arms"
        pos (545,360)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.2 ypos 350
            ease 1.6 ypos 360
            pause 0.2
            repeat
    contains:

        "Kitty_BJ_Head"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (500,307)
        subpixel True
        rotate 0
        block:

            ease 2 pos (500,304)
            ease 1.6 pos (500,307)
            pause 0.4
            repeat
    contains:

        "Kitty_TJ_Tits"
        pos (545,360)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.2 ypos 350
            ease 1.6 ypos 360
            pause 0.2
            repeat
    contains:













        ConditionSwitch(

                    "Player.sprite", AlphaMask("Zero_cock_blowjob", "Kitty_TJ_Mask_5"),

                    "True", Null(),
                    )
        subpixel True
        pos (665,500)
        anchor (0.5,0.5)
        zoom 0.4





























label Kitty_TJ_Launch(Line=primary_action):
    if renpy.showing("Kitty_TJ_Animation"):
        return
    call Kitty_Hide
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        ease 1 zoom 2 xpos 700 yoffset 50
    if Line == "L" and taboo:
        if len(Present) >= 2:
            if Present[0] != KittyX:
                "[KittyX.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != KittyX:
                "[KittyX.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[KittyX.name] casually glances around to see if anyone can see her."
    if KittyX.bra and KittyX.top:
        "She throws off her [KittyX.top] and her [KittyX.bra]."
    elif KittyX.top:
        "She throws off her [KittyX.top], baring her breasts underneath."
    elif KittyX.bra:
        "She tugs off her [KittyX.bra] and throws it aside."
    $ KittyX.top = ""
    $ KittyX.bra = ""
    $ KittyX.arm_pose = 0
    call Kitty_First_Topless
    if Line == "L":
        if not KittyX.action_counter["titjob"]:
            "She hesitantly presses your cock against her chest."
        else:
            "She squeezes her breasts around your cock."


    show blackscreen onlayer black with dissolve
    show Kitty_sprite zorder KittyX.sprite_layer:
        alpha 0
    $ action_speed = 0
    if Line != "cum":
        $ primary_action = "titjob"
    # show Kitty_TJ_Animation zorder 150
    $ Player.sprite = 1
    hide blackscreen onlayer black with dissolve
    return

label Kitty_TJ_Reset:
    if not renpy.showing("Kitty_TJ_Animation"):
        return
    call Kitty_Hide
    $ Player.sprite = 0

    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        zoom 2 xpos 550 yoffset 50
    show Kitty_sprite zorder KittyX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 xpos 700 yoffset 50
        pause 0.5
        ease 0.5 zoom 1 xpos KittyX.sprite_location yoffset 0
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        zoom 1 offset (0,0) xpos KittyX.sprite_location

    return






















image Kitty_handjob_under:
    "images/Kitty_sprite/Kitty_handjob_hand2.png"
    anchor (0.5,0.5)
    pos (0,0)


image Kitty_handjob_over:
    "images/Kitty_sprite/Kitty_handjob_hand1.png"
    anchor (0.5,0.5)
    pos (0,0)


















transform Kitty_Hand_1():
    subpixel True
    ease 0.5 ypos 150 rotate 5
    pause 0.25
    ease 1.0 ypos -100 rotate -5
    pause 0.1
    repeat

transform Kitty_Hand_2():
    subpixel True
    ease 0.2 ypos 0 rotate 3
    pause 0.1
    ease 0.4 ypos -100 rotate -3
    pause 0.1
    repeat

image Kitty_HJ_Animation:
    contains:
        ConditionSwitch(
            "not action_speed", Transform("Kitty_handjob_under"),
            "action_speed == 1", At("Kitty_handjob_under", Kitty_Hand_1()),
            "action_speed >= 2", At("Kitty_handjob_under", Kitty_Hand_2()),
            "action_speed ", Null(),
            ),
    contains:
        ConditionSwitch(
            "not action_speed", Transform("Zero_cock_handjob"),
            "action_speed == 1", At("Zero_cock_handjob", Handcock_1()),
            "action_speed >= 2", At("Zero_cock_handjob", Handcock_2()),
            "action_speed ", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(
            "not action_speed", Transform("Kitty_handjob_over"),
            "action_speed == 1", At("Kitty_handjob_over", Kitty_Hand_1()),
            "action_speed >= 2", At("Kitty_handjob_over", Kitty_Hand_2()),
            "action_speed ", Null(),
            ),
    anchor (0.51, -1.3)
    zoom 0.4


label Kitty_HJ_Launch(Line=primary_action):
    if renpy.showing("Kitty_HJ_Animation"):
        $ primary_action = "handjob"
        return
    call Kitty_Hide
    if Line == "L":
        show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(stage_right):
            alpha 1
            ease 1 zoom 1.7 offset (-50,200)
    else:
        show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(stage_right):
            alpha 1
            ease 1 zoom 1.7 offset (-50,200)
        with dissolve

    if Line == "L":
        if taboo:
            if len(Present) >= 2:
                if Present[0] != KittyX:
                    "[KittyX.name] looks back at [Present[0].name] to see if she's watching."
                elif Present[1] != KittyX:
                    "[KittyX.name] looks back at [Present[1].name] to see if she's watching."
            else:
                "[KittyX.name] casually glances around to see if anyone can see her."

    $ action_speed = 0
    if Line != "cum":
        $ primary_action = "handjob"
    else:
        $ action_speed = 1
    pause 0.5
    # show Kitty_HJ_Animation zorder 150 at sprite_location(stage_center) with easeinbottom:
    #
    #     offset (100,250)
    return

label Kitty_HJ_Reset:
    if not renpy.showing("Kitty_HJ_Animation"):
        return
    $ action_speed = 0
    hide Kitty_HJ_Animation with easeoutbottom
    call Kitty_Hide
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        zoom 1.7 offset (-50,200)
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause 0.5
        ease 0.5 zoom 1 offset (0,0)
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
    return


label Kitty_Kissing_Launch(T=primary_action, Set=1):
    call Kitty_Hide
    $ primary_action = T
    $ KittyX.pose = "kiss" if Set else KittyX.pose
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location)
    show Kitty_sprite at sprite_location(stage_center):
        ease 0.5 offset (0,0) zoom 2 alpha 1
    return

label Kitty_Kissing_Smooch:
    $ KittyX.change_face("_kiss")
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(stage_center):
        ease 0.5 xpos stage_center offset (0,0) zoom 2 alpha 1
        pause 1
        ease 0.5 xpos KittyX.sprite_location zoom 1
    $ KittyX.change_face("_sexy")
    return

label Kitty_Breasts_Launch(T=primary_action, Set=1):
    call Kitty_Hide
    $ primary_action = T
    $ KittyX.pose = "breasts" if Set else KittyX.pose
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
    return

label Kitty_Middle_Launch(T=primary_action, Set=1):
    call Kitty_Hide
    $ primary_action = T
    $ KittyX.pose = "mid" if Set else KittyX.pose
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):

        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
    return

label Kitty_Pussy_Launch(T=primary_action, Set=1):
    call Kitty_Hide
    $ primary_action = T
    $ KittyX.pose = "pussy" if Set else KittyX.pose
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
    return

label Kitty_Pos_Reset(T=0, Set=0):
    if KittyX.location != bg_current:
        return
    call Kitty_Hide
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        ease 0.5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
    show Kitty_sprite zorder KittyX.sprite_layer:
        offset (0,0)
        anchor (0.5, 0.0)
        zoom 1
        xzoom 1
        yzoom 1
        alpha 1
        pos (KittyX.sprite_location,50)
    $ KittyX.pose = "full" if Set else 0
    $ primary_action = T
    return

label Kitty_Hide(Sprite=0):
    call Kitty_Sex_Reset
    hide Kitty_sex_animation
    hide Kitty_Doggy_Animation
    hide Kitty_HJ_Animation
    hide Kitty_blowjob_animation
    hide Kitty_TJ_Animation
    if Sprite:
        hide Kitty_sprite
    return

label Kitty_ThreewayBreasts_Launch:
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):

        ease 0.5 pos (700,200) xzoom -1.5 yzoom 1.5
    $ KittyX.arm_pose = 1
    return













image GropeLeftBreast_Kitty:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65
        pos (215,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image GropeRightBreast_Kitty:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (120,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30
            ease 1 rotate -60
            repeat


image LickRightBreast_Kitty:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (115,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease 0.5 rotate -40 pos (95,370)
            pause 0.5
            ease 1.5 rotate 30 pos (115,400)
            repeat

image LickLeftBreast_Kitty:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (200,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease 0.5 rotate -40 pos (190,380)
            pause 0.5
            ease 1.5 rotate 30 pos (200,410)
            repeat

image GropeThigh_Kitty:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65
        pos (200,720)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel:
            pause 0.5
            ease 1 ypos 780
            ease 1 ypos 720
            repeat
        parallel:
            pause 0.5
            ease 1 rotate 110 xpos 180
            ease 1 rotate 100 xpos 200
            repeat

image GropePussy_Kitty:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65
        pos (210,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease 0.5 rotate 190 pos (210,625)
                ease 0.75 rotate 170 pos (210,640)
            choice:
                ease 0.5 rotate 190 pos (210,625)
                pause 0.25
                ease 1 rotate 170 pos (210,640)
            repeat

image FingerPussy_Kitty:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (220,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (230,695)
                pause 0.5
                ease 1 rotate 50 pos (220,730)
            choice:
                ease 0.5 rotate 40 pos (230,695)
                pause 0.5
                ease 1.75 rotate 50 pos (220,730)
            choice:
                ease 2 rotate 40 pos (230,695)
                pause 0.5
                ease 1 rotate 50 pos (220,730)
            choice:
                ease 0.25 rotate 40 pos (230,695)
                ease 0.25 rotate 50 pos (220,730)
                ease 0.25 rotate 40 pos (230,695)
                ease 0.25 rotate 50 pos (220,730)
            repeat

image Lickpussy_Kitty:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (240,680)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout 0.5 rotate -50 pos (220,660)
            linear 0.5 rotate -60 pos (210,670)
            easein 1 rotate 10 pos (240,680)
            repeat

image VibratorRightBreast_Kitty:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (150,380)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 370
            pause 0.25
            ease 1 rotate 55 ypos 380
            pause 0.25
            repeat

image VibratorLeftBreast_Kitty:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (270,400)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 390
            pause 0.25
            ease 1 rotate 55 ypos 400
            pause 0.25
            repeat

image VibratorPussy_Kitty:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,665)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 xpos 230 ypos 655
            pause 0.25
            ease 1 rotate 70 xpos 240 ypos 665
            pause 0.25
            repeat

image VibratorAnal_Kitty:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (270,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 10
        block:
            ease 1 rotate 0 xpos 260 ypos 655
            pause 0.25
            ease 1 rotate 10 xpos 270 ypos 665
            pause 0.25
            repeat

image VibratorPussyInsert_Kitty:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Kitty:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0




image GirlGropeLeftBreast_Kitty:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (240,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -20
        block:
            ease 1 rotate -40 pos (230,390)
            ease 1 rotate -20 pos (240,400)
            repeat

image GirlGropeRightBreast_Kitty:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (110,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate -30 pos (110,410)
            ease 1 rotate -10 pos (110,380)
            repeat

image GirlGropeThigh_Kitty:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (210,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel:
            pause 0.5
            ease 1 ypos 780
            ease 1 ypos 730
            repeat
        parallel:
            pause 0.5
            ease 0.5 xpos 213
            ease 0.5 xpos 210
            ease 0.5 xpos 213
            ease 0.5 xpos 210
            repeat

image GirlGropePussy_Kitty:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (210,625)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease 0.75 rotate 210 pos (215,640)
                ease 0.5 rotate 195
                ease 0.75 rotate 210
                ease 0.5 rotate 195
            choice:
                ease 0.5 rotate 210 pos (215,640)
                ease 1 rotate 195
                pause 0.25
                ease 0.5 rotate 210
                ease 1 rotate 195
                pause 0.25
            choice:


                ease 0.5 rotate 205 pos (215,640)
                ease 0.75 rotate 200 pos (215,645)
                ease 0.5 rotate 205 pos (215,640)
                ease 0.75 rotate 200 pos (215,645)
            choice:
                ease 0.3 rotate 205 pos (215,640)
                ease 0.3 rotate 200 pos (215,650)
                ease 0.3 rotate 205 pos (215,640)
                ease 0.3 rotate 200 pos (215,650)
            repeat

image GirlFingerPussy_Kitty:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom 0.6
        pos (220,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease 0.75 rotate 210 pos (220,645)
                ease 0.5 rotate 195
                ease 0.75 rotate 210
                ease 0.5 rotate 195
            choice:
                ease 0.5 rotate 210 pos (220,645)
                ease 1 rotate 195
                pause 0.25
                ease 0.5 rotate 210
                ease 1 rotate 195
                pause 0.25
            choice:
                ease 0.5 rotate 205 pos (220,655)
                ease 0.75 rotate 200 pos (220,660)
                ease 0.5 rotate 205 pos (220,655)
                ease 0.75 rotate 200 pos (220,660)
            choice:
                ease 0.3 rotate 205 pos (220,655)
                ease 0.3 rotate 200 pos (220,665)
                ease 0.3 rotate 205 pos (220,655)
                ease 0.3 rotate 200 pos (220,665)
            repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
