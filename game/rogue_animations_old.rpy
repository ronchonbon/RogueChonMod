





image Rogue_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom 0.55
        offset (150,340)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10
            ease 1 rotate 0
            repeat





image Rogue_Pussy_Mask:


    contains:

        "images/Rogue_doggy/Rogue_Doggy_SexMask.png"
        anchor (0.52,0.69)
        pos (217,518)
        xzoom 0.6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom 0.6
            repeat

image Rogue_Pussy_Mask_Static:


    contains:

        "images/Rogue_doggy/Rogue_Doggy_SexMask.png"
        anchor (0.52,0.69)
        pos (217,518)
        xzoom 0.6
        block:
            ease 1 xzoom 0.65
            pause 1
            ease 3 xzoom 0.6
            repeat


































image Rogue_Pussy_Static:

    subpixel True
    contains:

        "images/Rogue_doggy/Rogue_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/Rogue_doggy/Rogue_Doggy_Pussy_FHole.png"
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

            "RogueX.hose == 'garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwear_pulled_down", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/Rogue_doggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/Rogue_doggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
    contains:

        AlphaMask("Zero_doggy_static", "Rogue_Pussy_Mask_Static")
    contains:


        AlphaMask("Rogue_PussyHole_Static", "Rogue_Pussy_Hole_Mask_Static")

image Rogue_Pussy_Hole_Mask_Static:

    contains:

        AlphaMask("images/Rogue_doggy/Rogue_Doggy_Pussy_FHole.png", "images/Rogue_doggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom 0.6
        block:
            ease 1 xzoom 0.65
            pause 1
            ease 3 xzoom 0.6
            repeat

image Rogue_PussyHole_Static:

    contains:

        "images/Rogue_doggy/Rogue_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha 0.9
        block:
            ease 1 ypos 512
            pause 1
            ease 3 ypos 515
            repeat


image Rogue_Pussy_Heading:

    subpixel True
    contains:

        "images/Rogue_doggy/Rogue_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/Rogue_doggy/Rogue_Doggy_Pussy_FHole.png"
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

            "RogueX.hose == 'garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwear_pulled_down", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/Rogue_doggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/Rogue_doggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
    contains:

        AlphaMask("Zero_doggy_heading", "Rogue_Pussy_Mask")
    contains:


        AlphaMask("Rogue_Pussy_Heading_Flap", "Rogue_Pussy_Hole_Mask")


image Rogue_Pussy_Hole_Mask:

    contains:

        AlphaMask("images/Rogue_doggy/Rogue_Doggy_Pussy_FHole.png", "images/Rogue_doggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom 0.6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom 0.6
            repeat

image Rogue_Pussy_Heading_Flap:

    contains:

        "images/Rogue_doggy/Rogue_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha 0.9
        block:
            ease 1 ypos 505
            pause 1
            ease 3 ypos 515
            repeat


image Rogue_Pussy_Fingering:

    subpixel True
    contains:

        "images/Rogue_doggy/Rogue_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/Rogue_doggy/Rogue_Doggy_Pussy_FHole.png"
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

            "RogueX.hose == 'garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwear_pulled_down", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/Rogue_doggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/Rogue_doggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
    contains:

        AlphaMask("Zero_Pussy_Finger", "Rogue_Pussy_Mask")
    contains:


        AlphaMask("Rogue_Pussy_Heading_Flap", "Rogue_Pussy_Hole_Mask")

image Zero_Pussy_Finger:

    contains:
        subpixel True
        "images/UI_Fingering.png"
        pos (171,545)
        block:
            ease 1 xpos 168 ypos 500
            pause 1
            ease 3 xpos 171 ypos 545
            repeat



image Rogue_Pussy_Fucking2:

    contains:

        "images/Rogue_doggy/Rogue_Doggy_Pussy_FBase.png"
    contains:

        "images/Rogue_doggy/Rogue_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "RogueX.hose == 'garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwear_pulled_down", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/Rogue_doggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/Rogue_doggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
    contains:




        ConditionSwitch(
            "primary_action == 'dildo_pussy'", AlphaMask("Rogue_Doggy_Fucking_Dildo", "images/Rogue_doggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_doggy_fucking2", "images/Rogue_doggy/Rogue_Doggy_SexMask.png"),
            ),


image Rogue_Pussy_Fucking3:

    contains:

        "images/Rogue_doggy/Rogue_Doggy_Pussy_FBase.png"
    contains:

        "images/Rogue_doggy/Rogue_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "RogueX.hose == 'garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwear_pulled_down", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/Rogue_doggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/Rogue_doggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
    contains:

        AlphaMask("Zero_doggy_fucking3", "images/Rogue_doggy/Rogue_Doggy_SexMask.png")

image Rogue_Doggy_Fucking_Dildo:

    contains:
        "images/DildoIn.png"
        pos (169,500)
        block:
            ease 0.5 ypos 440
            pause 0.25
            ease 1.75 ypos 500
            repeat





image Rogue_Anal:

    contains:

        "images/Rogue_doggy/Rogue_doggy_anus_loose.png"
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:
        ConditionSwitch(

            "RogueX.hose == 'garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwear_pulled_down", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/Rogue_doggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/Rogue_doggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:

        "Zero_cock_doggy_in"
        pos (172,500)



image Rogue_Anal_Fingering:

    contains:

        "images/Rogue_doggy/Rogue_doggy_anal_full_base.png"
    contains:

        "images/Rogue_doggy/Rogue_doggy_anal_full_hole.png"
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

            "RogueX.hose == 'garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwear_pulled_down", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/Rogue_doggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/Rogue_doggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:




        AlphaMask("Zero_Doggy_Anal_Finger", "Rogue_Doggy_Anal_Fingering_Mask")

image Zero_Doggy_Anal_Finger:

    contains:
        "images/UI_Fingering.png",
        pos (172,480)
        block:
            ease 0.5 ypos 460
            pause 0.25
            ease 1.75 ypos 480
            repeat

image Rogue_Doggy_Anal_Fingering_Mask:

    contains:
        "images/Rogue_doggy/Rogue_doggy_anal_mask.png"

        anchor (0.52,0.69)
        pos (218,518)
        zoom 0.6
        block:
            ease 0.5 zoom 0.75
            pause 0.5
            ease 1.5 zoom 0.6
            repeat


image Rogue_Anal_Heading:

    contains:

        "images/Rogue_doggy/Rogue_doggy_anal_full_base.png"
    contains:

        "images/Rogue_doggy/Rogue_doggy_anal_full_hole.png"
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

            "RogueX.hose == 'garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwear_pulled_down", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/Rogue_doggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/Rogue_doggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_doggy_anal_heading", "Zero_doggy_anal_headingJunk")
    contains:

        AlphaMask("Zero_doggy_anal_heading", "Rogue_Doggy_Anal_Heading_Mask")



image Rogue_Doggy_Anal_Heading_Mask:

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

image Rogue_Doggy_Anal_Head_Top:

    contains:
        subpixel True
        "Rogue_doggy_body"
        ypos 0
        block:
            pause 0.4
            ease 0.3 ypos -5
            easeout 1 ypos 0
            pause 0.8
            repeat

image Rogue_Doggy_Anal_Head_Ass:

    contains:
        subpixel True
        "Rogue_doggy_ass"
        ypos 0
        block:
            pause 0.4
            ease 0.2 ypos -10
            easeout 0.1 ypos -7
            easein 0.9 ypos 0
            pause 0.9
            repeat
































image Rogue_Anal_Fucking:

    contains:

        "images/Rogue_doggy/Rogue_doggy_anal_full_base.png"
    contains:

        "images/Rogue_doggy/Rogue_doggy_anal_full_hole.png"
    contains:

        "images/Rogue_doggy/Rogue_doggy_anal_full_cheeks.png"
    contains:
        ConditionSwitch(

            "RogueX.hose == 'garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwear_pulled_down", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/Rogue_doggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/Rogue_doggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
    contains:

        ConditionSwitch(

            "primary_action == 'dildo_anal'", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/Rogue_doggy/Rogue_doggy_anal_mask.png"),
            "True", AlphaMask("Zero_doggy_anal1", "images/Rogue_doggy/Rogue_doggy_anal_mask.png"),
            ),

image Rogue_Doggy_Anal_Dildo:

    contains:
        "images/DildoIn.png"
        pos (172,460)
        block:
            ease 0.5 ypos 395
            pause 0.25
            ease 1.75 ypos 460
            repeat


image Rogue_Doggy_Anal_FullMask:
    contains:

        "images/Rogue_doggy/Rogue_Doggy_Anal_FullMask.png"
    contains:

        "images/Rogue_doggy/Rogue_doggy_anal_full_cheeks.png"
    contains:
        ConditionSwitch(

            "RogueX.hose == 'garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwear_pulled_down", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/Rogue_doggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/Rogue_doggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )

image Rogue_Doggy_Fuck_Top:

    contains:
        subpixel True
        "Rogue_doggy_body"
        ypos 15
        pause 0.4
        block:
            ease 0.2 ypos 5
            pause 0.3
            ease 2 ypos 15
            repeat

image Rogue_Doggy_Fuck_Ass:

    contains:
        subpixel True
        "Rogue_doggy_ass"
        ypos 0
        block:
            pause 0.4
            ease 0.2 ypos -15
            ease 0.1 ypos -5
            pause 0.2
            ease 1.6 ypos 0
            repeat





image Rogue_Anal_Fucking2:

    contains:

        "images/Rogue_doggy/Rogue_doggy_anal_full_base.png"
    contains:

        "images/Rogue_doggy/Rogue_doggy_anal_full_hole.png"
    contains:




        "images/Rogue_doggy/Rogue_doggy_anal_full_cheeks.png"
    contains:
        ConditionSwitch(

            "RogueX.hose == 'garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/Rogue_doggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwear_pulled_down", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/Rogue_doggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/Rogue_doggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_doggy_anal2", "images/Rogue_doggy/Rogue_doggy_anal_mask.png")

image Rogue_Doggy_Fuck2_Top:

    contains:
        subpixel True
        "Rogue_doggy_body"
        ypos 20
        block:
            pause 0.15
            ease 0.1 ypos 0
            pause 0.1
            easein 0.5 ypos 20
            pause 0.05
            repeat

image Rogue_Doggy_Fuck2_Ass:

    contains:
        subpixel True
        "Rogue_doggy_ass"
        ypos 5
        block:
            pause 0.15
            ease 0.1 ypos -25
            ease 0.1 ypos -15
            pause 0.1
            ease 0.4 ypos 5
            pause 0.05
            repeat




image Rogue_doggy_feet0:

    contains:
        "Rogue_doggy_shins"
        pos (0, 0)
        block:
            subpixel True
            pause 0.5
            ease 2 ypos 20
            pause 0.5
            ease 2 ypos 0
            repeat
    contains:
        ConditionSwitch(
                "Player.sprite", "Zero_cock_doggy_out",
                "True", Null(),
                )
        zoom 1.2
        pos (145,480)
    contains:
        "Rogue_doggy_feet"
        pos (0, 0)
        block:
            subpixel True
            pause 0.5
            ease 2 ypos 20
            pause 0.5
            ease 2 ypos 0
            repeat

image Rogue_doggy_feet1:

    contains:
        "Rogue_doggy_shins"
        pos (0, 0)
        block:
            pause 0.3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat
    contains:
        "Zero_cock_doggy_out"
        zoom 1.2
        pos (145,480)
        block:
            pause 0.4
            ease 1.7 ypos 500
            ease 0.9 ypos 480
            repeat
    contains:
        "Rogue_doggy_feet"
        pos (0, 0)
        block:
            pause 0.3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat

image Rogue_doggy_feet2:

    contains:
        "Rogue_doggy_shins"
        pos (0, 0)
        block:
            pause 0.05
            ease 0.6 ypos 110
            ease 0.3 ypos 0
            repeat
    contains:
        "Zero_cock_doggy_out"
        zoom 1.2
        pos (145,480)
        block:
            pause 0.07
            ease 0.6 ypos 500
            ease 0.28 ypos 480
            repeat
    contains:
        "Rogue_doggy_feet"
        pos (0, 0)
        block:
            pause 0.05
            ease 0.6 ypos 110
            ease 0.3 ypos 0
            repeat




image Slap_Ass:
    contains:
        "SlapHand"
        pause 1.2
        Null()

image Slap_Ass:
    contains:
        "UI_Hand"
        subpixel True
        zoom 1
        alpha 0.5
        anchor (0.5,0.5)
        pos (600,380)
        rotate 40
        block:
            parallel:
                ease 0.5 xpos 300 rotate 80
                ease 0.1 xpos 310 rotate 80
                pause 0.5
            parallel:
                ease 0.2 ypos 520
                pause 0.9

image NotSlap_Ass:
    contains:
        subpixel True
        "UI_Hand"
        zoom 1
        pos (600,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            pos (600,380)
            rotate 40
            parallel:
                ease 0.5 xpos 300 rotate 80
                ease 0.1 xpos 310 rotate 80
                pause 0.5
            parallel:
                ease 0.2 ypos 520
                pause 0.9
            repeat




label Rogue_Doggy_Launch(line=primary_action):
    if renpy.showing("Rogue_doggy_animation"):
        return
    $ action_speed = 0
    call hide_girl(RogueX, hide_sprite = True)
    show Rogue_doggy_animation zorder 150 at sprite_location(stage_center+50)
    with dissolve
    return

label Rogue_Doggy_Reset:
    if not renpy.showing("Rogue_doggy_animation"):
        return

    $ RogueX.arm_pose = 2
    $ RogueX.spriteVer = 0
    hide Rogue_doggy_animation
    call hide_girl(RogueX)
    show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        alpha 1
        zoom 1
        offset (0,0)
        anchor (0.6, 0.0)
    with dissolve
    $ action_speed = 0
    return












image Rogue_sex_body_Anim0:
    contains:
        "Rogue_sex_body"
    pos (650,230)

image Rogue_sex_legs_Anim0:
    contains:
        "Rogue_sex_legs"
    pos (650,230)


image Rogue_sex_Lick_Breasts:
    "licking"
    zoom 0.6
    offset (450,270)

image Rogue_sex_Fondle_Breasts:
    "GropeLeftBreast"
    zoom 1.1
    offset (320,-130)

image Rogue_head_Sex:

    "Rogue_head"
    zoom 1.28
    anchor (0.5,0.5)
    rotate -10

image Rogue_hairback_Sex:

    "Rogue_hairback"
    zoom 1.28
    anchor (0.5,0.5)
    rotate -10

image Rogue_sex_Lick_Pussy:
    "licking"
    zoom 0.7
    offset (530,510)

image Rogue_sex_Lick_Ass:
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

image Rogue_sex_pussy_Fucking0:

    contains:

        "images/Rogue_sex/Rogue_sex_pussy_Open.png"
    contains:

        ConditionSwitch(
                "not RogueX.pubes", Null(),
                "True", "images/Rogue_sex/Rogue_sex_Pubes_Open.png",
                ),
    contains:

        AlphaMask("Rogue_sex_Zero_Anim0", "Rogue_Pussy_Open_Mask")

image Rogue_sex_pussy_Fucking1:

    contains:

        "images/Rogue_sex/Rogue_sex_pussy_Open.png"
    contains:

        ConditionSwitch(
                "not RogueX.pubes", Null(),
                "True", "images/Rogue_sex/Rogue_sex_Pubes_Open.png",
                ),
    contains:

        AlphaMask("Rogue_sex_Zero_Anim1", "Rogue_Pussy_Open_Mask")

image Rogue_sex_pussy_Fucking2:

    contains:

        "images/Rogue_sex/Rogue_sex_pussy_Fucking.png"
    contains:

        ConditionSwitch(
                "not RogueX.pubes", Null(),
                "True", "images/Rogue_sex/Rogue_sex_Pubes_Fucking.png",
                ),
    contains:

        AlphaMask("Rogue_sex_Zero_Anim2", "Rogue_Pussy_Fucking_Mask")

image Rogue_sex_pussy_Fucking3:

    contains:

        "images/Rogue_sex/Rogue_sex_pussy_Fucking.png"
    contains:

        ConditionSwitch(
                "not RogueX.pubes", Null(),
                "True", "images/Rogue_sex/Rogue_sex_Pubes_Fucking.png",
                ),
    contains:

        AlphaMask("Rogue_sex_Zero_Anim3", "Rogue_Pussy_Fucking_Mask")

image Rogue_Pussy_Fucking_Mask:
    contains:
        "images/Rogue_sex/Rogue_sex_pussy_mask.png"

image Rogue_Pussy_Open_Mask:
    contains:
        "images/Rogue_sex/Rogue_sex_pussy_mask.png"
        yoffset 3

image Rogue_sex_pussy_Spunk_Heading:
    "images/Kitty_sex/Kitty_sex_spunk_pussy_over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8



image Rogue_sex_FingerP_Anim1:

    contains:
        subpixel True
        "images/UI_Fingering.png"
        pos (507,520)
        zoom 1.2
        block:
            ease 0.2 ypos 480
            pause 0.2
            ease 0.6 ypos 520
            repeat

image Rogue_sex_Dildo_Anim2:

    contains:
        subpixel True
        "images/DildoIn.png"
        pos (504,490)
        zoom 1.3
        block:
            ease 1 ypos 380
            pause 1
            ease 3 ypos 490
            repeat


image Rogue_sex_Zero_Anim0:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (503,530)
        zoom 1.3

image Rogue_sex_Zero_Anim1:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (503,525)
        zoom 1.3
        block:
            ease 1 ypos 510
            pause 1
            ease 3 ypos 525
            repeat

image Rogue_sex_Zero_Anim2:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (504,490)
        zoom 1.3
        block:
            ease 1 ypos 380
            pause 1
            ease 3 ypos 490
            repeat

image Rogue_sex_Zero_Anim3:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (504,490)
        zoom 1.3
        block:
            ease 0.25 ypos 380
            pause 0.25
            ease 1.5 ypos 490
            repeat



image Rogue_sex_legs_Anim1:

    contains:
        subpixel True
        "Rogue_sex_legs"
        pos (0,0)
        block:

            pause 0.25
            easein 1 pos (0,-5)
            pause 1
            ease 2.75 pos (0,0)
            repeat

image Rogue_sex_legs_Anim2:

    contains:
        subpixel True
        "Rogue_sex_legs"
        pos (0,0)
        block:

            pause 0.5
            easein 0.5 pos (0,-15)
            ease 0.25 pos (0,-10)
            pause 1
            ease 2.75 pos (0,0)
            repeat

image Rogue_sex_legs_Anim3:

    contains:
        subpixel True
        "Rogue_sex_legs"
        pos (0,0)
        block:

            pause 0.15
            easein 0.15 pos (0,-20)
            ease 0.10 pos (0,-15)
            pause 0.20
            ease 1.4 pos (0,0)
            repeat



image Rogue_sex_body_Anim1:

    contains:
        subpixel True
        "Rogue_sex_body"
        pos (0,0)
        block:

            pause 0.5
            easein 0.75 pos (0,-5)
            pause 1.25
            ease 2.5 pos (0,0)
            repeat

image Rogue_sex_body_Anim2:

    contains:
        subpixel True
        "Rogue_sex_body"
        pos (0,0)
        block:

            pause 0.6
            easein 0.4 pos (0,-10)
            ease 0.25 pos (0,-5)
            pause 1
            ease 2.75 pos (0,10)
            repeat

image Rogue_sex_body_Anim3:

    contains:
        subpixel True
        "Rogue_sex_body"
        pos (0,0)
        block:

            pause 0.17
            easein 0.13 pos (0,-20)
            ease 0.10 pos (0,-15)
            pause 0.20
            ease 1.4 pos (0,10)
            repeat






image Rogue_sex_FingerA_Anim1:

    contains:
        subpixel True
        "images/UI_Fingering.png"
        pos (507,600)
        zoom 1.2
        block:
            ease 0.4 ypos 550
            pause 0.4
            ease 1.2 ypos 600
            repeat

image Rogue_Anal_Dildo_Anim2:

    contains:
        subpixel True
        "images/DildoIn.png"
        pos (505,570)
        zoom 1.3
        block:
            ease 1 ypos 450
            pause 1
            ease 3 ypos 570
            repeat

image Rogue_sex_Anal_Fucking0:

    contains:

        "Rogue_Anal_Tip"
    contains:

        AlphaMask("Rogue_Anal_Zero_Anim0", "Rogue_Anal_Fucking_Mask")

image Rogue_sex_Anal_Fucking1:

    contains:

        "Rogue_Anal_Heading"
    contains:

        AlphaMask("Rogue_Anal_Zero_Anim1", "Rogue_Anal_Fucking_Mask")

image Rogue_sex_Anal_Fucking2:

    contains:

        "images/Kitty_sex/Kitty_sex_anus_open.png"
    contains:

        AlphaMask("Rogue_Anal_Zero_Anim2", "Rogue_Anal_Fucking_Mask")

image Rogue_sex_Anal_Fucking3:

    contains:

        "images/Kitty_sex/Kitty_sex_anus_open.png"
    contains:

        AlphaMask("Kitty_Anal_Zero_Anim3", "Kitty_Anal_Fucking_Mask")

image Rogue_Anal_Fucking_Mask:

    contains:
        "images/Kitty_sex/Kitty_sex_anus_mask.png"
        yoffset 1

image Rogue_Anal_Open_Mask:

    contains:
        "images/Kitty_sex/Kitty_sex_anus_mask.png"
        yoffset 3

image Rogue_sex_Anal_Heading:
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

image Rogue_Anal_Spunk_Heading_Over:
    "images/Kitty_sex/Kitty_sex_Spunk_Anal_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8
    block:

        ease 0.75 xzoom 1.0
        pause 1.75
        ease 0.25 xzoom 1.0
        ease 2.25 xzoom 0.8
        repeat
image Rogue_Anal_Spunk_Heading_Under:
    "images/Kitty_sex/Kitty_sex_Spunk_Anal_Under.png"
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

image Rogue_sex_Anal_Tip:
    "images/Kitty_sex/Kitty_sex_anus_open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6




image Rogue_Anal_Zero_Anim0:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (505,600)
        zoom 1.3

image Rogue_Anal_Zero_Anim1:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (505,600)
        zoom 1.3
        block:
            ease 1 ypos 570
            pause 1
            ease 3 ypos 600
            repeat

image Rogue_Anal_Zero_Anim2:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (505,570)
        zoom 1.3
        block:
            ease 1 ypos 450
            pause 1
            ease 3 ypos 570
            repeat

image Rogue_Anal_Zero_Anim3:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (505,570)
        zoom 1.3
        block:
            ease 0.25 ypos 450
            pause 0.25
            ease 1.5 ypos 570
            repeat



image Rogue_Hotdog_Zero_Anim0:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (503,570)
        zoom 1.3

image Rogue_Hotdog_Zero_Anim1:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (503,500)
        zoom 1.3
        block:
            ease 1 ypos 560
            pause 0.5
            ease 1.5 ypos 500
            repeat

image Rogue_Hotdog_Zero_Anim2:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (503,510)
        zoom 1.3
        block:
            ease 0.5 ypos 400
            pause 0.5
            ease 1 ypos 510
            repeat

image Rogue_Hotdog_Body_Anim2:

    contains:
        subpixel True
        "Rogue_sex_body"
        pos (0,0)
        block:

            pause 0.30
            ease 0.50 pos (0,-10)
            pause 0.20
            ease 1 pos (0,0)
            repeat

image Rogue_Hotdog_Legs_Anim2:

    contains:
        subpixel True
        "Rogue_sex_legs"
        pos (0,0)
        block:

            pause 0.20
            ease 0.50 pos (0,-10)
            pause 0.20
            ease 1.1 pos (0,0)
            repeat





image Rogue_Footcock:
    contains:
        subpixel True
        "Zero_cock_blowjob"
        alpha 0.8
        zoom 0.7
        anchor (0.5,0.5)
        offset (465,70)
        pos (0,0)
    pos (750,230)

image Rogue_Footcock_Anim0:
    contains:
        subpixel True
        "Rogue_Footcock"
        pos (392,295)

    offset (0,-100)

image Rogue_Footcock_Zero_Anim1:
    contains:
        subpixel True
        "Rogue_Footcock"
        pos (392,295)
        block:

            pause 0.5
            easein 0.75 ypos 360
            ease 0.25 ypos 355
            pause 1
            ease 2.50 ypos 270
            repeat
    offset (0,-100)

image Rogue_Footcock_Zero_Anim2:
    contains:
        subpixel True
        "Rogue_Footcock"
        pos (392,295)
        block:

            pause 0.2
            easein 0.4 ypos 360
            ease 0.2 ypos 355
            pause 0.2
            ease 1.00 ypos 270
            repeat
    offset (0,-100)

transform Rogue_Footcock_Zero_Anim1A():
    subpixel True
    offset (0,0)
    block:

        pause 0.5
        easein 0.75 yoffset 60
        ease 0.25 yoffset 55
        pause 1
        ease 1.50 yoffset -30
        repeat

transform Rogue_Footcock_Zero_Anim2A():
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

transform Rogue_Footcock_Anim0A():
    subpixel True
    offset (0,-5)
    block:

        pause 0.5
        ease 1 yoffset 0
        pause 1
        ease 1.50 yoffset -5
        repeat

image Rogue_sex_legs_FootAnim1:

    contains:
        subpixel True
        "Rogue_sex_legs"
        pos (0,0)
        block:

            pause 0.5
            easein 0.75 pos (0,-65)
            ease 0.25 pos (0,-60)
            pause 1
            ease 2.50 pos (0,25)
            repeat

    offset (0,100)

image Rogue_sex_legs_FootAnim2:

    contains:
        subpixel True
        "Rogue_sex_legs"
        pos (0,0)
        block:

            pause 0.2
            easein 0.4 pos (0,-65)
            ease 0.2 pos (0,-60)
            pause 0.2
            ease 1.0 pos (0,25)
            repeat
    offset (0,100)

image Rogue_sex_legs_FootAnim0:

    contains:
        subpixel True
        "Rogue_sex_legs"
        pos (0,0)
    offset (0,100)

transform Rogue_sex_legs_FootAnim1A():

    subpixel True
    offset (0,0)
    block:

        pause 0.5
        easein 0.75 yoffset -65
        ease 0.25 yoffset -60
        pause 1
        ease 1.50 yoffset 25
        repeat

transform Rogue_sex_legs_FootAnim2A():

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

transform Rogue_sex_legs_FootAnim0A():

    subpixel True
    offset (0,0)
    block:

        pause 0.5
        ease 1 yoffset -5
        pause 1
        ease 1.50 yoffset 0
        repeat





image Rogue_sex_body_FootAnim1:

    contains:
        subpixel True
        "Rogue_sex_body"
        pos (0,0)
        block:

            pause 0.5
            easein 0.75 pos (0,-25)
            ease 0.25 pos (0,-15)
            pause 1
            ease 2.50 pos (0,15)
            repeat

    offset (0,100)

image Rogue_sex_body_FootAnim2:

    contains:
        subpixel True
        "Rogue_sex_body"
        pos (0,0)
        block:

            pause 0.2
            easein 0.4 pos (0,-25)
            ease 0.2 pos (0,-15)
            pause 0.2
            ease 1.0 pos (0,15)
            repeat
    offset (0,100)

image Rogue_sex_body_FootAnim0:

    contains:
        subpixel True
        "Rogue_sex_body"
        pos (0,0)
    offset (0,100)

transform Rogue_sex_body_FootAnim1A():

    subpixel True
    offset (0,0)
    block:

        pause 0.5
        easein 0.75 yoffset -25
        ease 0.25 yoffset -15
        pause 1
        ease 1.50 yoffset 15
        repeat

transform Rogue_sex_body_FootAnim2A():

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

transform Rogue_sex_body_FootAnim0A():

    subpixel True
    offset (0,0)
    block:

        pause 0.5
        ease 1 yoffset -5
        pause 1
        ease 1.50 yoffset 0
        repeat





label Rogue_sex_Launch(line=primary_action):
    $ girl_offhand_action = None if girl_offhand_action == "handjob" else girl_offhand_action

    $ line = "solo" if not line else line
    $ Player.sprite = 1
    if line == "sex":
        $ Player.cock_position = "sex"
        if offhand_action in ("fondle_pussy","dildo_pussy","eat_pussy"):
            $ offhand_action = None
    elif line == "anal":
        $ Player.cock_position = "anal"
        if offhand_action in ("finger_ass","dildo_anal","eat_ass"):
            $ offhand_action = None
    elif line == "hotdog":
        $ Player.cock_position = "out"
    elif line == "footjob":
        $ show_feet = 1
        $ Player.cock_position = "footjob"
    elif line == "massage":
        $ Player.sprite = 0
        $ Player.cock_position = 0
    else:
        $ Player.sprite = 0
        $ Player.cock_position = "out"
        $ action_speed = 0

    if RogueX.pose == "doggy":
        call Rogue_Doggy_Launch (line)
        return
    if renpy.showing("Rogue_sex_animation"):
        return
    $ action_speed = 0
    call hide_girl(RogueX, hide_sprite = True)
    show Rogue_sex_animation zorder 150



    with dissolve
    return

label Rogue_sex_Reset:
    if renpy.showing("Rogue_doggy_animation"):
        call Rogue_Doggy_Reset
        return
    if not renpy.showing("Rogue_sex_animation"):
        return
    $ RogueX.arm_pose = 2
    hide Rogue_sex_animation
    call hide_girl(RogueX)

    show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
        anchor (0.5, 0.0)
    with dissolve
    $ action_speed = 0
    return















label Rogue_BJ_Launch(line=primary_action):

    if renpy.showing("Rogue_blowjob_animation"):
        return

    call hide_girl(RogueX)
    if line == "L" or line == "cum":
        show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(stage_center):
            alpha 1

            ease 1 zoom 2.5 offset (70,140)
        with dissolve
    else:
        show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(stage_center):
            alpha 1
            zoom 2.5 offset (70,140)
        with dissolve

    if taboo and line == "L":

        if len(Present) >= 2:
            if Present[0] != RogueX:
                "[RogueX.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != RogueX:
                "[RogueX.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[RogueX.name] looks around to see if anyone can see her."
    if line == "L":
        if not RogueX.action_counter["blowjob"]:
            "[RogueX.name] hesitantly pulls down your pants and touches her mouth to your cock."
        else:
            "[RogueX.name] bends down and begins to suck on your cock."

    $ action_speed = 0

    if line != "cum":
        $ primary_action = "blowjob"

    show Rogue_sprite zorder RogueX.sprite_layer:
        alpha 0
    show Rogue_blowjob_animation zorder 150:
        pos (645,510)
    return

label Rogue_BJ_Reset:
    if not renpy.showing("Rogue_blowjob_animation"):
        return

    call hide_girl(RogueX)
    $ action_speed = 0

    show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        zoom 2 offset (70,140)
        alpha 1
        block:
            pause 0.5
            ease 1 zoom 1.5 offset (-50,50)
            pause 0.5
            ease 0.5 zoom 1 offset (0,0)
    show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
    $ RogueX.change_face("sexy")
    return








image Rogue_titjob_under:
    contains:
        "Rogue_blowjob_hairback"
        pos (150, -560)
        zoom 0.95
    contains:
        "images/RogueBJFace/Rogue_tj_base.png"
    contains:
        ConditionSwitch(
            "'tits' in RogueX.spunk", "images/RogueBJFace/Rogue_tj_spunkU.png",
            "True", Null(),
            ),
    contains:
        "Rogue_blowjob_head"
        pos (150, -560)
        zoom 0.95
    pos (-60, 200)

image Rogue_titjob_over:
    contains:
        ConditionSwitch(
            "RogueX.piercings == 'barbell'", "images/RogueBJFace/Rogue_tj_tits_b.png",
            "RogueX.piercings == 'ring'", "images/RogueBJFace/Rogue_tj_tits_r.png",
            "RogueX.piercings != 'barbell'", "images/RogueBJFace/Rogue_tj_tits.png",
            ),
    contains:
        ConditionSwitch(
            "'tits' in RogueX.spunk", "images/RogueBJFace/Rogue_tj_spunk.png",
            "True", Null(),
            ),
    pos (-60, 200)


transform Rogue_titjob_under_1():
    ypos 200
    subpixel True
    block:
        ease 1 ypos 300
        easeout 0.2 ypos 300
        easein 1.3 ypos 120
        repeat

transform Rogue_titjob_over_1():
    ypos 200
    subpixel True
    block:
        ease 1.20 ypos 300
        easeout 0.1 ypos 300
        easein 1.2 ypos 120
        repeat

transform Rogue_titjob_under_2():
    ypos 200
    subpixel True
    block:
        ease 0.25 ypos 200
        ease 0.4 ypos 120
        ease 0.1 ypos 125
        repeat

transform Rogue_titjob_over_2():
    ypos 200
    subpixel True
    block:
        ease 0.3 ypos 200
        ease 0.35 ypos 120
        ease 0.1 ypos 125
        repeat


transform Zero_TJ_Cock():

    anchor (.5,.5)
    pos (440,1020)
    rotate 0

transform Zero_TJ_Cock_1():
    pos (440,1020)
    subpixel True
    block:
        ease 1 ypos 1050
        easeout 0.2 ypos 1060
        easein 1.3 ypos 1020
        repeat

transform Zero_TJ_Cock_2():
    pos (440,1020)
    subpixel True
    block:
        ease 0.35 ypos 1030
        ease 0.4 ypos 1020

        repeat





label Rogue_TJ_Launch(line=primary_action):

    if renpy.showing("Rogue_TJ_Animation"):
        return
    call hide_girl(RogueX)
    show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        alpha 1
        ease 1 zoom 2 xpos 550 offset (0,50)
    if taboo:
        if len(Present) >= 2:
            if Present[0] != RogueX:
                "[RogueX.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != RogueX:
                "[RogueX.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[RogueX.name] looks around to see if anyone can see her."

    if RogueX.bra and RogueX.top:
        "She throws off her [RogueX.top] and her [RogueX.bra]."
    elif RogueX.top:
        "She throws off her [RogueX.top], baring her breasts underneath."
    elif RogueX.bra:
        "She tugs off her [RogueX.bra] and throws it aside."
    $ RogueX.top = 0
    $ RogueX.bra = 0
    $ RogueX.arms = ""

    call Rogue_First_Topless

    if not RogueX.action_counter["titjob"] and line == "L":
        if not RogueX.bra and not RogueX.top:
            "As you pull out your cock, [RogueX.name] hesitantly places it between her breasts and starts to rub them up and down the shaft."
        elif RogueX.bra and not RogueX.top:
            "As you pull out your cock, [RogueX.name] hesitantly places it under her [RogueX.bra], between her breasts and starts to rub them up and down the shaft."
        elif RogueX.bra and RogueX.top:
            "As you pull out your cock, [RogueX.name] hesitantly places it under her [RogueX.top], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, [RogueX.name] hesitantly places it under her clothes, between her breasts and starts to rub them up and down the shaft."
    elif line == "L":
        if not RogueX.bra and not RogueX.top:
            "As you pull out your cock, [RogueX.name] places it between her breasts and starts to rub them up and down the shaft."
        elif RogueX.bra and not RogueX.top:
            "As you pull out your cock, [RogueX.name] places it under her [RogueX.bra], between her breasts and starts to rub them up and down the shaft."
        elif RogueX.bra and RogueX.top:
            "As you pull out your cock, [RogueX.name] places it under her [RogueX.top], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, [RogueX.name] places it under her clothes, between her breasts and starts to rub them up and down the shaft."
    else:
        "[RogueX.name] wraps her tits around your cock."
    show black_screen onlayer black with dissolve
    show Rogue_sprite zorder RogueX.sprite_layer:
        alpha 0
    $ action_speed = 0
    if line != "cum":
        $ primary_action = "titjob"
    show Rogue_TJ_Animation zorder 150 at sprite_location(stage_right)
    hide black_screen onlayer black with dissolve
    return

label Rogue_TJ_Reset:

    if not renpy.showing("Rogue_TJ_Animation"):
        return
    hide Rogue_TJ_Animation
    call hide_girl(RogueX)
    show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        zoom 2 xpos 550 offset (0,50)
    show Rogue_sprite zorder RogueX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 xpos 500 offset (0,50)
        pause 0.5
        ease 0.5 zoom 1 xpos RogueX.sprite_location yoffset 0
    show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        alpha 1
        zoom 1 xpos RogueX.sprite_location yoffset 0

    "[RogueX.name] pulls back"
    return




image Zero_cock_handjob:
    contains:
        ConditionSwitch(
            "Player.color == 'pink'", "images/RogueBJFace/handcock_P.png",
            "Player.color == 'brown'", "images/RogueBJFace/handcock_B.png",
            "Player.color == 'green'", "images/RogueBJFace/handcock_G.png",
            "Player.color != 'pink'", Null(),
            ),
    anchor (0.5,1.0)
    pos (200,400)

image Rogue_handjob_under:
    "images/Rogue_sprite/Rogue_handjob_hand2.png"
    anchor (0.5,0.5)
    pos (0,0)


image Rogue_handjob_over:
    "images/Rogue_sprite/Rogue_handjob_hand1.png"
    anchor (0.5,0.5)
    pos (0,0)

transform Handcock_1():
    subpixel True
    rotate_pad False
    ease 0.5 ypos 450 rotate -2
    pause 0.25
    ease 1.0 ypos 400 rotate 0
    pause 0.1
    repeat

transform Handcock_2():
    subpixel True
    rotate_pad False
    ease 0.2 ypos 430 rotate -3
    ease 0.5 ypos 400 rotate 0
    pause 0.1
    repeat

transform Rogue_Hand_1():
    subpixel True
    ease 0.5 ypos 150 rotate 5
    pause 0.25
    ease 1.0 ypos -100 rotate -5
    pause 0.1
    repeat

transform Rogue_Hand_2():
    subpixel True
    ease 0.2 ypos 0 rotate 3
    pause 0.1
    ease 0.4 ypos -100 rotate -3
    pause 0.1
    repeat



label Rogue_HJ_Launch(line=primary_action):
    if renpy.showing("Rogue_HJ_Animation"):
        $ primary_action = "handjob"
        return
    call hide_girl(RogueX)
    $ RogueX.arms = ""
    $ RogueX.arm_pose = 1
    if not renpy.showing("Rogue_sprite"):
        show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
            alpha 1
            zoom 1.7 xpos 700 offset (0,200)
        with dissolve
    show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        alpha 1
        ease 1 zoom 1.7 xpos 700 offset (0,200)

    if taboo and line == "L":

        if len(Present) >= 2:
            if Present[0] != RogueX:
                "[RogueX.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != RogueX:
                "[RogueX.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[RogueX.name] looks around to see if anyone can see her."
        if not RogueX.action_counter["handjob"] and RogueX.arms:
            "As you pull out your cock, [RogueX.name] pulls off her gloves, and hesitantly reaches for it. She starts to roughly stroke on it."
        else:
            "She then leans over and grabs your cock."
    elif line == "L":
        if not RogueX.action_counter["handjob"] and RogueX.arms:
            "As you pull out your cock, [RogueX.name] pulls off her gloves, and hesitantly reaches for it. She starts to roughly stroke on it."
        else:
            "[RogueX.name] bends down and grabs your cock."
    else:
        "[RogueX.name] bends down and grabs your cock."

    $ action_speed = 0
    if line != "cum":
        $ primary_action = "handjob"
    show Rogue_HJ_Animation zorder 150 at sprite_location(RogueX.sprite_location) with easeinbottom
    return

label Rogue_HJ_Reset:
    if not renpy.showing("Rogue_HJ_Animation"):
        return
    $ action_speed = 0
    hide Rogue_HJ_Animation
    with dissolve
    call hide_girl(RogueX)
    show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        alpha 1
        zoom 1.7 xpos 700 offset (0,200)
    show Rogue_sprite zorder RogueX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 offset (0,50)
        pause 0.5
        ease 0.5 zoom 1 xpos RogueX.sprite_location yoffset 0
    show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        alpha 1
        zoom 1 xpos RogueX.sprite_location yoffset 0
    return




transform Vibrate():
    subpixel True
    block:
        linear 0.5 xoffset 2
        linear 0.5 xoffset -2
        repeat


image UI_Vibrator = LiveComposite(
        (224,224),
        (0,0), ConditionSwitch(
            "not Vibration", "UI_VibA",
            "Vibration", At("UI_VibB", Vibrate()),
            ),
        )

image GropeLeftBreast:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.7
        pos (300,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image GropeRightBreast:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.7
        xzoom -0.7
        pos (180,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30
            ease 1 rotate -60
            repeat


image LickRightBreast:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.5
        xzoom -0.5
        pos (160,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease 0.5 rotate -45 pos (150,370)
            pause 0.5
            ease 1.5 rotate 30 pos (160,400)
            repeat

image LickLeftBreast:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.5
        xzoom -0.5
        pos (280,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease 0.5 rotate -45 pos (260,380)
            pause 0.5
            ease 1.5 rotate 30 pos (280,410)
            repeat

image GropeThigh:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.7
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

image GropePussy:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.7
        pos (220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease 0.5 rotate 190 pos (220,620)
                ease 0.75 rotate 170 pos (220,635)
            choice:
                ease 0.5 rotate 190 pos (220,620)
                pause 0.25
                ease 1 rotate 170 pos (220,635)
            repeat

image FingerPussy:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.7
        pos (230,720)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (240,685)
                pause 0.5
                ease 1 rotate 50 pos (230,720)
            choice:
                ease 0.5 rotate 40 pos (240,685)
                pause 0.5
                ease 1.75 rotate 50 pos (230,720)
            choice:
                ease 2 rotate 40 pos (240,685)
                pause 0.5
                ease 1 rotate 50 pos (230,720)
            choice:
                ease 0.25 rotate 40 pos (240,685)
                ease 0.25 rotate 50 pos (230,720)
                ease 0.25 rotate 40 pos (240,685)
                ease 0.25 rotate 50 pos (230,720)
            repeat

image Lickpussy:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.5
        xzoom -0.5
        pos (250,670)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout 0.5 rotate -50 pos (230,650)
            linear 0.5 rotate -60 pos (220,660)
            easein 1 rotate 10 pos (250,670)
            repeat

image VibratorRightBreast:
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

image VibratorLeftBreast:
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

image VibratorPussy:
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

image VibratorAnal:
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

image VibratorPussyInsert:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0

image TestUIAnimation:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (270,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            ease 1 rotate 0 xpos 260 ypos 655
            pause 0.25
            ease 1 rotate 10 xpos 270 ypos 665
            pause 0.25
            repeat


image GirlGropeLeftBreast:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (300,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -20
        block:
            ease 1 rotate -40 pos (280,390)
            ease 1 rotate -20 pos (300,400)
            repeat

image GirlGropeRightBreast:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (160,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate -30 pos (160,410)
            ease 1 rotate -10 pos (160,380)
            repeat

image GirlGropeThigh:
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

image GirlGropePussy:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (230,615)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease 0.75 rotate 210 pos (225,620)
                ease 0.5 rotate 195
                ease 0.75 rotate 210
                ease 0.5 rotate 195
            choice:
                ease 0.5 rotate 210 pos (225,620)
                ease 1 rotate 195
                pause 0.25
                ease 0.5 rotate 210
                ease 1 rotate 195
                pause 0.25
            choice:
                ease 0.5 rotate 205 pos (225,620)
                ease 0.75 rotate 200 pos (225,625)
                ease 0.5 rotate 205 pos (225,620)
                ease 0.75 rotate 200 pos (225,625)
            choice:
                ease 0.3 rotate 205 pos (225,620)
                ease 0.3 rotate 200 pos (225,630)
                ease 0.3 rotate 205 pos (225,620)
                ease 0.3 rotate 200 pos (225,630)
            repeat

image GirlFingerPussy:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom 0.6
        pos (230,630)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease 0.75 rotate 210 pos (230,635)
                ease 0.5 rotate 195
                ease 0.75 rotate 210
                ease 0.5 rotate 195
            choice:
                ease 0.5 rotate 210 pos (230,635)
                ease 1 rotate 195
                pause 0.25
                ease 0.5 rotate 210
                ease 1 rotate 195
                pause 0.25
            choice:
                ease 0.5 rotate 205 pos (230,635)
                ease 0.75 rotate 200 pos (230,640)
                ease 0.5 rotate 205 pos (230,635)
                ease 0.75 rotate 200 pos (230,640)
            choice:
                ease 0.3 rotate 205 pos (230,635)
                ease 0.3 rotate 200 pos (230,645)
                ease 0.3 rotate 205 pos (230,635)
                ease 0.3 rotate 200 pos (230,645)
            repeat





image Spunk_Drip:

    contains:
        "images/SpermdropB.png"
        zoom 0.3
        alpha 0
        block:
            choice:
                pause 1
            choice:
                pause 0.5
            choice:
                pos (0,0)
                alpha 1
                easeout 2.5 ypos 70
                easeout 0.9 ypos 350
                alpha 0
                pause 1
            choice:
                pos (9,0)
                pause 0.2
                alpha 1
                easeout 2.5 ypos 75
                easeout 0.9 ypos 350
                alpha 0
                pause 0.4
            choice:
                pos (6,0)
                pause 0.4
                alpha 1
                easeout 2.5 ypos 65
                easeout 0.9 ypos 350
                alpha 0
            choice:
                pos (12,0)
                pause 0.8
                alpha 1
                easeout 2.5 ypos 60
                easeout 0.9 ypos 350
                alpha 0
            repeat

image Spunk_Drip2:

    contains:
        "images/SpermdropB.png"
        pos (0,0)
        zoom 0.3
        parallel:
            pos (0,0)
            alpha 1
            easeout 2.5 ypos 70
            easeout 0.9 ypos 350
            alpha 0
            pause 1
            repeat
    contains:
        "images/SpermdropB.png"
        pos (0,0)
        zoom 0.3
        parallel:
            pos (9,0)
            pause 0.2
            alpha 1
            easeout 2.5 ypos 75
            easeout 0.9 ypos 350
            alpha 0
            pause 0.4
            repeat
    contains:
        "images/SpermdropB.png"
        pos (0,0)
        zoom 0.3
        parallel:
            pos (6,0)
            pause 0.4
            alpha 1
            easeout 2.5 ypos 65
            easeout 0.9 ypos 350
            alpha 0
            repeat
    contains:
        "images/SpermdropB.png"
        pos (0,0)
        zoom 0.3
        parallel:
            pos (12,0)
            pause 0.8
            alpha 1
            easeout 2.5 ypos 60
            easeout 0.9 ypos 350
            alpha 0
            repeat


image Spunk_Dripp:

    contains:
        "images/SpermdropP.png"
        zoom 0.3
        alpha 0
        block:
            choice:
                pause 1
            choice:
                pause 0.5
            choice:
                pos (0,0)
                alpha 1
                easeout 2.5 ypos 70
                easeout 0.9 ypos 350
                alpha 0
                pause 1
            choice:
                pos (9,0)
                pause 0.2
                alpha 1
                easeout 2.5 ypos 75
                easeout 0.9 ypos 350
                alpha 0
                pause 0.4
            choice:
                pos (6,0)
                pause 0.4
                alpha 1
                easeout 2.5 ypos 65
                easeout 0.9 ypos 350
                alpha 0
            choice:
                pos (12,0)
                pause 0.8
                alpha 1
                easeout 2.5 ypos 60
                easeout 0.9 ypos 350
                alpha 0
            repeat

image Wet_Drip:

    contains:
        "images/Wetdrop.png"
        zoom 0.2
        alpha 0
        block:
            choice:
                pause 1
            choice:
                pause 0.5
            choice:
                pos (14,0)
                alpha 0.8
                easeout 0.9 ypos 70
                easeout 0.9 ypos 350
                alpha 0
                pause 1
            choice:
                pos (9,0)
                pause 0.2
                alpha 0.8
                easeout 0.9 ypos 75
                easeout 0.9 ypos 350
                alpha 0
                pause 0.4
            choice:
                pos (6,0)
                pause 0.4
                alpha 0.8
                easeout 0.9 ypos 65
                easeout 0.9 ypos 350
                alpha 0
            choice:
                pos (12,0)
                pause 0.8
                alpha 0.8
                easeout 0.9 ypos 60
                easeout 0.9 ypos 350
                alpha 0
            repeat

image Wet_Drip2:

    contains:
        "images/Wetdrop.png"
        pos (0,0)
        zoom 0.2
        parallel:
            pos (14,0)
            alpha 0.8
            easeout 0.9 ypos 70
            easeout 0.9 ypos 350
            alpha 0
            pause 1.5
            repeat
    contains:
        "images/Wetdrop.png"
        pos (0,0)
        zoom 0.2
        parallel:
            pos (9,0)
            pause 0.3
            alpha 0.8
            easeout 0.9 ypos 75
            easeout 0.9 ypos 350
            alpha 0
            pause 0.6
            repeat
    contains:
        "images/Wetdrop.png"
        pos (0,0)
        zoom 0.2
        parallel:
            pos (6,0)
            pause 0.6
            alpha 0.8
            easeout 0.9 ypos 65
            easeout 0.9 ypos 350
            alpha 0
            repeat
    contains:
        "images/Wetdrop.png"
        pos (0,0)
        zoom 0.2
        parallel:
            pos (12,0)
            pause 0.8
            alpha 0.8
            easeout 0.9 ypos 60
            easeout 0.9 ypos 350
            alpha 0
            pause 0.2
            repeat


image Zero_Chibicock:
    LiveComposite(
        (225,350),
        (0,0), ConditionSwitch(
            "Player.color == 'pink'", "images/Chibi_Cock_P.png",
            "Player.color == 'brown'", "images/Chibi_Cock_B.png",
            "Player.color == 'green'", "images/Chibi_Cock_G.png",
            "True", Null(),
            ),








        )
    anchor (0.5,0.5)



image Chibi_Null:

    contains:
        "Zero_Chibicock"
        anchor (0.5,0.5)
        pos (0,0)
        rotate 0
        xzoom 1
    pos (75,675)
    zoom 0.5

image Chibi_jerking_off:

    contains:
        "Zero_Chibicock"
        anchor (0.5,0.5)
        pos (0,0)
        rotate 0
        xzoom 1
    contains:
        subpixel True
        "images/Chibi_Hand_M.png"
        pos (-10,-80)
        anchor (0.5,0.5)
        rotate 20
        block:
            ease 0.3 rotate -10 pos (0,50)
            ease 0.7 rotate 20 pos (-10,-80)
            repeat
    pos (75,675)
    zoom 0.5

image Chibi_Handy:

    contains:
        "Zero_Chibicock"
        anchor (0.5,0.5)
        pos (0,0)
        rotate 0
        xzoom 1
    contains:
        subpixel True
        ConditionSwitch(
            "(Partner == StormX and second_girl_primary_action == 'hand') or (focused_Girl == StormX and girl_offhand_action == 'hand')", "images/Chibi_Hand_S.png",
            "True", "images/Chibi_Hand_G.png"
            )

        pos (0,-110)
        anchor (0.5,0.5)
        rotate -10
        block:
            ease 0.3 rotate 0 pos (10,10)
            ease 0.7 rotate -10 pos (0,-130)
            repeat
    pos (75,675)
    zoom 0.5

image Chibi_Mouth_Mask:
    "images/Chibi_Mouth_Mask.png"
    anchor (0.5,0.5)

image Chibi_Mouth_Rogue:
    "images/Chibi_Mouth_R.png"
    anchor (0.5,0.5)
image Chibi_Mouth_Kitty:
    "images/Chibi_Mouth_K.png"
    anchor (0.5,0.5)
image Chibi_Mouth_Emma:
    "images/Chibi_Mouth_E.png"
    anchor (0.5,0.5)
image Chibi_Mouth_Storm:
    "images/Chibi_Mouth_S.png"
    anchor (0.5,0.5)

image Chibi_Sucking:

    contains:
        "Chibi_SuckingB"
    pos (75,675)

image Chibi_SuckingB:

    LiveComposite(
        (225,350),
        (0,0), ConditionSwitch(
            "Partner == RogueX", "Chibi_Mouth_Rogue",
            "Partner == EmmaX", "Chibi_Mouth_Emma",
            "Partner == StormX", "Chibi_Mouth_Storm",
            "True", "Chibi_Mouth_Kitty"
            ),
        (0,0), AlphaMask("Chibi_Sucking_Cock", "Chibi_Mouth_Mask")
        )
    subpixel True
    pos (7,0)
    anchor (0.5,0.5)
    zoom 0.5
    xzoom 0.71
    block:
        easeout 0.25 rotate 0 pos (2,48) xzoom 1
        easein 0.25 rotate 0 pos (6,92) xzoom 1
        easeout 0.5 rotate 0 pos (2,48) xzoom 1
        easein 0.5 rotate 0 pos (5,0) xzoom 0.71
        repeat

image Chibi_Sucking_Cock:

    contains:
        subpixel True
        "Zero_Chibicock"
        pos (100,175)
        xzoom 1.5
        anchor (0.5,0.5)

        rotate 0
        block:
            easeout 0.25 rotate 0 pos (110,80) xzoom 1
            easein 0.25 rotate 0 pos (100,-10) xzoom 1
            easeout 0.5 rotate 0 pos (110,80) xzoom 1
            easein 0.5 rotate 0 pos (100,175) xzoom 1.5
            repeat




image Chibi_UI:

    contains:
        ConditionSwitch(
            "'cockout' not in Player.recent_history", Null(),
            "offhand_action == 'jerking_off'", "Chibi_jerking_off",
            "girl_offhand_action == 'hand' or second_girl_primary_action == 'hand'", "Chibi_Handy",
            "second_girl_primary_action == 'blow'", "Chibi_Sucking",
            "True", "Chibi_Null",
            )



label Rogue_Kissing_Launch(T=primary_action, Set=1):
    call hide_girl(RogueX)
    $ primary_action = T
    $ RogueX.pose = "kiss" if Set else RogueX.pose
    show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location)
    show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(stage_center):
        ease 0.5 offset (0,0) zoom 2 alpha 1
    return

label Rogue_Kissing_Smooch:
    $ RogueX.change_face("_kiss")
    show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(stage_center):
        offset (0,0)
        alpha 1
        ease 0.5 xpos stage_center zoom 2
        pause 1
        ease 0.5 xpos RogueX.sprite_location zoom 1
    pause 1
    $ RogueX.change_face("sexy")
    return

label Rogue_Breasts_Launch(T=primary_action, Set=1):
    call hide_girl(RogueX)
    $ primary_action = T
    $ RogueX.pose = "breasts" if Set else RogueX.pose
    show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        ease 0.5 pos (700,-50) zoom 2 offset (0,0) alpha 1
    return

label Rogue_Middle_Launch(T=primary_action, Set=1):
    call hide_girl(RogueX)
    $ primary_action = T
    $ RogueX.pose = "mid" if Set else RogueX.pose
    show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):

        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
    return

label Rogue_Pussy_Launch(T=primary_action, Set=1):
    call hide_girl(RogueX)
    $ primary_action = T
    $ RogueX.pose = "pussy" if Set else RogueX.pose
    show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        ease 0.5 pos (700,-400) zoom 2 offset (0,0) alpha 1
    return

label Rogue_Pos_Reset(T=0, Set=0):
    if RogueX.location != bg_current:
        return
    call hide_girl(RogueX)
    show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        ease 0.5 offset (0,0) anchor (0.6, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
    show Rogue_sprite zorder RogueX.sprite_layer:
        offset (0,0)
        anchor (0.6, 0.0)
        zoom 1
        xzoom 1
        yzoom 1
        alpha 1
        pos (RogueX.sprite_location,50)
    $ RogueX.pose = "full" if Set else 0
    $ primary_action = T
    return

image cellphone:
    "images/cellphone.png"
    xoffset 0
    yoffset 100


image PhoneSex:

    contains:

        "images/PhoneFrame.png"
    contains:

        AlphaMask("PhoneScreen", "images/PhoneMask.png")
    offset (300,50)

image PhoneRG:

    "bg_rogue"
    xoffset 500

image PhoneScreen:
    contains:
        ConditionSwitch(
            "focused_Girl.location == 'bg_rogue'","PhoneRG",
            "True", "[focused_Girl.location]")

        offset (-800,-300)
        zoom 1.5

    contains:
        "[focused_Girl.Tag]_sprite"
        pos (0,0)
        offset (290,50)
        anchor (0.6,0)
        zoom 1.1


image dress_screen:

    contains:

        "images/dress_screen.png"
    contains:

        AlphaMask("images/dress_screenShadow.png","DressShadow")
    zoom 1
    offset (375,225)

image DressShadow:

    contains:

        ConditionSwitch(
            "RogueX.sprite_layer == 100", "Rogue_sprite",
            "KittyX.sprite_layer == 100", "Kitty_sprite",
            "EmmaX.sprite_layer == 100", "Emma_Sprite",
            "LauraX.sprite_layer == 100", "Laura_Sprite",
            "JeanX.sprite_layer == 100", "Jean_Sprite",
            "StormX.sprite_layer == 100", "Storm_Sprite",
            "JubesX.sprite_layer == 100", "Jubes_Sprite",




            "True", Null(),
            )
        offset (210,-170)
        zoom 1





image Gwen_Sprite:
    LiveComposite(
        (574,964),

        (0,0), "images/GS_B.png",


        (80,15), "Gwen_Sprite_Head",
        )
    anchor (0.6, 0.0)
    yoffset 15
    zoom 0.75



image Gwen_Sprite_Head:
    LiveComposite(
        (820,820),
        (0,0), ConditionSwitch(

                "G_Blush", "images/NPC/Gwen_Sprite_Head_Blush.png",
                "True", "images/NPC/Gwen_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(
            "G_Mouth == 'open'", "images/NPC/Gwen_Sprite_Mouth_Open.png",
            "G_Mouth == 'kiss'", "images/NPC/Gwen_Sprite_Mouth_Kiss.png",
            "G_Mouth == 'smile'", "images/NPC/Gwen_Sprite_Mouth_Smile.png",
            "G_Mouth == 'shocked'", "images/NPC/Gwen_Sprite_Mouth_Shocked.png",
            "True", "images/NPC/Gwen_Sprite_Mouth_Smile.png",
            ),
        (0,0), ConditionSwitch(

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
        (0,0), "Gwen Blink",
        )
    anchor (0.6, 0.0)
    zoom 0.5

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
    0.20
    repeat

default G_Mouth = "normal"
default G_Brows = "normal"
default G_Eyes = "normal"
default G_Blush = 0

label GwenFace(emotion="normal", B=G_Blush, M=0, Mouth=0, Eyes=0, Brows=0):


    $ B = G_Blush if B == 5 else B

    if emotion == "normal":
        $ G_Mouth = "normal"
        $ G_Brows = "normal"
        $ G_Eyes = "normal"
    elif emotion == "angry":
        $ G_Mouth = "_kiss"
        $ G_Brows = "angry"
        $ G_Eyes = "angry"
    elif emotion == "closed":
        $ G_Mouth = "normal"
        $ G_Brows = "_sad"
        $ G_Eyes = "closed"
    elif emotion == "_sad":
        $ G_Mouth = "_kiss"
        $ G_Brows = "_sad"
        $ G_Eyes = "normal"
    elif emotion == "smile":
        $ G_Mouth = "smile"
        $ G_Brows = "normal"
        $ G_Eyes = "normal"
    elif emotion == "surprised":
        $ G_Mouth = "open"
        $ G_Brows = "normal"
        $ G_Eyes = "surprised"
    elif emotion == "shocked":
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
                    $ G_Brows = "_confused"
                elif G_Brows == "_confused":
                    $ G_Brows = "_sad"
                elif G_Brows == "_sad":
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
                    $ G_Mouth = "_sad"
                elif G_Mouth == "_sad":
                    $ G_Mouth = "smile"
                elif G_Mouth == "smile":
                    $ G_Mouth = "surprised"
                else:
                    $ G_Mouth = "normal"
            "Toggle Mouth Sexy":
                if G_Mouth  == "normal":
                    $ G_Mouth = "_kiss"
                elif G_Mouth == "kiss":
                    $ G_Mouth = "_sucking"
                elif G_Mouth == "_sucking":
                    $ G_Mouth = "_tongue"
                elif G_Mouth == "_tongue":
                    $ G_Mouth = "_lipbite"
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














label Display_Gwen(GwLoc=350, YLoc=50):



    show Gwen_Sprite:
        alpha 1
        zoom 1
        offset (0,0)
        anchor (0.5, 0.0)
        easeout 0.5 pos (GwLoc,YLoc)
    show Gwen_Sprite:
        alpha 1
        zoom 1
        offset (0,0)
        anchor (0.5, 0.0)
        pos (GwLoc,YLoc)
    return


label Close_Launch(GirlA=0, GirlB=0, XLoc=0, YLoc=0, XZoom=0):



    if GirlB:
        $ temp_Girls = [GirlA,GirlB]
    elif GirlA:
        $ temp_Girls = [GirlA]
    while temp_Girls:
        if temp_Girls[0] == KittyX or temp_Girls[0] == LauraX:
            $ temp_Girls[0].arm_pose = 1
        else:
            $ temp_Girls[0].arm_pose = 2
        $ YLoc = 100
        if GirlA == temp_Girls[0]:

            if temp_Girls[0] == KittyX:
                $ XLoc = 450
            elif temp_Girls[0] == RogueX:
                $ XLoc = 550
            else:
                $ XLoc = 500
            $ temp_Girls[0].sprite_layer = 100
            $ XZoom = -1.3
        elif GirlB == temp_Girls[0]:

            if temp_Girls[0] == EmmaX or LauraX:
                $ XLoc = 700
            else:
                $ XLoc = 715
            $ temp_Girls[0].sprite_layer = 75
            $ XZoom = 1.3

        if temp_Girls[0] == RogueX:
            call hide_girl(RogueX)
            show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.6, 0.0)
        elif temp_Girls[0] == KittyX:
            call hide_girl(KittyX)
            show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif temp_Girls[0] == EmmaX:
            call Emma_Hide
            show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif temp_Girls[0] == LauraX:
            call Laura_Hide
            show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif temp_Girls[0] == JeanX:
            call Jean_Hide
            show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif temp_Girls[0] == StormX:
            call Storm_Hide
            show Storm_Sprite zorder StormX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.6, 0.0)
        elif temp_Girls[0] == JubesX:
            call Jubes_Hide
            show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.6, 0.0)
        $ temp_Girls.remove(temp_Girls[0])
    return
















label Les_Launch(Girl=0, XLoc=0, YLoc=0, XZoom=0, temp_Girls=[]):



    if Partner not in all_Girls:
        return
    $ temp_Girls = [Girl,Partner]
    while temp_Girls:
        if "unseen" in temp_Girls[0].recent_history:
            $ temp_Girls[0].eyes = "closed"
        elif Girl == temp_Girls[0]:
            if Girl == RogueX:
                $ temp_Girls[0].eyes = "side"
            elif Girl == EmmaX:
                $ temp_Girls[0].eyes = "_sly"
            else:
                $ temp_Girls[0].eyes = "leftside"
        else:
            $ temp_Girls[0].eyes = "side"

        if temp_Girls[0] == KittyX or temp_Girls[0] == LauraX:
            $ temp_Girls[0].arm_pose = 1
        else:
            $ temp_Girls[0].arm_pose = 2
        $ YLoc = 100
        if Girl == temp_Girls[0]:

            if temp_Girls[0] == KittyX:
                $ XLoc = 450
            elif temp_Girls[0] == RogueX:
                $ XLoc = 550
            else:
                $ XLoc = 500
            $ temp_Girls[0].sprite_layer = 100
            $ XZoom = -1.3
        else:

            if temp_Girls[0] == EmmaX or LauraX:
                $ XLoc = 700
            else:
                $ XLoc = 715
            if temp_Girls[0] == KittyX:
                if RogueX in (Partner,Girl):
                    $ KittyX.sprite_layer = 100
                else:
                    $ KittyX.sprite_layer = 25
            else:
                $ temp_Girls[0].sprite_layer = 75
            $ XZoom = 1.3

        if temp_Girls[0] == RogueX:
            call hide_girl(RogueX)
            show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.6, 0.0)
        elif temp_Girls[0] == KittyX:
            call hide_girl(KittyX)
            show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif temp_Girls[0] == EmmaX:
            call Emma_Hide
            show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif temp_Girls[0] == LauraX:
            call Laura_Hide
            show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif temp_Girls[0] == JeanX:
            call Jean_Hide
            show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif temp_Girls[0] == StormX:
            call Storm_Hide
            show Storm_Sprite zorder StormX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.6, 0.0)
        elif temp_Girls[0] == JubesX:
            call Jubes_Hide
            show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.6, 0.0)
        $ temp_Girls.remove(temp_Girls[0])
    return

image CircleTest:
    contains:
        subpixel True
        "images/Clockbase.png"
        anchor (0.5,0.5)

        yzoom -1
    contains:

        ConditionSwitch(
            "round>= 50", "ClockWhite",
            "True",Null(),
            ),
    contains:
        ConditionSwitch(
            "round<= 50", "ClockRed",
            "True",Null(),
            ),
    contains:
        subpixel True
        "images/Clockface.png"
        anchor (0.5,0.5)

image ClockWhite:
    contains:
        subpixel True
        "images/Clockwhite.png"
        anchor (0.5,0.5)
        rotate -(int(round *3.6))

image ClockRed:
    contains:
        subpixel True
        "images/Clockred.png"
        anchor (0.5,0.5)
        rotate -(int(round *3.6-180))

image blue_screen:

    alpha 0.1
    contains:
        Solid("#00B3D6", xysize=(1024, 768))

image SilhouetteBase:

    alpha 0.95
    contains:
        Solid("#14142d", xysize=(1024, 768))


image Silhouettes:





    contains:

        AlphaMask("SilhouetteBase","Storm_Sprite")



# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
