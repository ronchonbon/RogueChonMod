image Jubes_blinking:
    "images/Jubes_standing/Jubes_standing_eyes_[JubesX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Jubes_standing/Jubes_standing_eyes_squint.png"
    0.05
    "images/Jubes_standing/Jubes_standing_eyes_closed.png"
    0.15
    "images/Jubes_standing/Jubes_standing_eyes_squint.png"
    0.05
    repeat

layeredimage Jubes_grool_dripping_animation:
    always:
        "grool_dripping_animation" pos (0.295, 1.05)

    if JubesX.grool > 1 and not JubesX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.295, 1.05)

    if JubesX.grool > 1 and not JubesX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.295, 1.05)

    if JubesX.grool > 1 and not JubesX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.295, 1.05)

layeredimage Jubes_grool_animations:
    if not JubesX.grool:
        Null()
    elif JubesX.Clothes["pants"].state:
        AlphaMask("Jubes_grool_dripping_animation", "images/Jubes_standing/Jubes_standing_grool_mask_pants.png")
    elif JubesX.Clothes["underwear"].state:
        AlphaMask("Jubes_grool_dripping_animation", "images/Jubes_standing/Jubes_standing_grool_mask_underwear.png")
    elif not JubesX.Outfit.pussy_covered:
        AlphaMask("Jubes_grool_dripping_animation", "images/Jubes_standing/Jubes_standing_grool_mask.png")

layeredimage Jubes_spunk_dripping_animation:
    always:
        "spunk_dripping_animation" pos (0.295, 1.05)

    if not JubesX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.295, 1.05)

    if not JubesX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.295, 1.05)

    if not JubesX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.295, 1.05)

layeredimage Jubes_spunk_animations:
    if not JubesX.spunk["pussy"] and not JubesX.spunk["anus"]:
        Null()
    elif JubesX.Clothes["pants"].state:
        AlphaMask("Jubes_spunk_dripping_animation", "images/Jubes_standing/Jubes_standing_grool_mask_pants.png")
    elif JubesX.Clothes["underwear"].state:
        AlphaMask("Jubes_spunk_dripping_animation", "images/Jubes_standing/Jubes_standing_grool_mask_underwear.png")
    elif not JubesX.Outfit.pussy_covered:
        AlphaMask("Jubes_spunk_dripping_animation", "images/Jubes_standing/Jubes_standing_grool_mask.png")

layeredimage Jubes_standing_fondling_animations:
    if JubesX.primary_Action.Target != JubesX:
        Null()
    elif JubesX.primary_Action.type == "fondle_breasts":
        "Girl_fondle_breast_right_animation" pos (0.195, 0.665)
    elif JubesX.primary_Action.type == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.28, 1.013)
    elif JubesX.primary_Action.type in "finger_pussy":
        "Girl_finger_pussy_animation" pos (0.28, 1.06)

    if JubesX.secondary_Action.Target != JubesX:
        Null()
    elif JubesX.secondary_Action.type == "fondle_breasts":
        "Girl_fondle_breast_left_animation" pos (0.33, 0.68)
    elif JubesX.secondary_Action.type == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.28, 1.013)
    elif JubesX.secondary_Action.type in "finger_pussy":
        "Girl_finger_pussy_animation" pos (0.28, 1.06)

    if Player.primary_Action.Target != JubesX:
        Null()
    elif Player.primary_Action.type == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.215, 1.22)
    elif Player.primary_Action.type == "fondle_breasts":
        "Zero_fondle_breasts_left_animation" pos (0.29, 0.655)
    elif Player.primary_Action.type == "suck_breasts":
        "Zero_suck_breasts_left_animation" pos (0.315, 0.615)
    elif Player.primary_Action.type == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.28, 1.0)
    elif Player.primary_Action.type == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.255, 1.17)
    elif Player.primary_Action.type == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.287, 1.1)

    if Player.secondary_Action.Target != JubesX:
        Null()
    elif Player.secondary_Action.type == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.215, 1.22)
    elif Player.secondary_Action.type == "fondle_breasts":
        "Zero_fondle_breasts_right_animation" pos (0.24, 0.675)
    elif Player.secondary_Action.type == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.175, 0.605)
    elif Player.secondary_Action.type == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.28, 1.0)
    elif Player.secondary_Action.type == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.255, 1.17)
    elif Player.secondary_Action.type == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.287, 1.1)

image Jubes_handjob_under_hand_animation0:
    "Jubes_handjob_under"

image Jubes_handjob_under_hand_animation1:
    animation
    "Jubes_handjob_under"

    subpixel True
    rotate -5
    block:
        ease 0.75 yoffset 40 rotate -10
        pause 0.25
        ease 1.0 yoffset -10 rotate -5
        pause 0.1
        repeat

image Jubes_handjob_under_hand_animation2:
    animation
    "Jubes_handjob_under"

    subpixel True
    rotate -3
    block:
        ease 0.4 yoffset 30 rotate -7
        pause 0.1
        ease 0.4 yoffset -10 rotate -3
        pause 0.1
        repeat

image Jubes_handjob_over_hand_animation0:
    "Jubes_handjob_over"

image Jubes_handjob_over_hand_animation1:
    animation
    "Jubes_handjob_over"

    subpixel True
    rotate -5
    block:
        ease 0.75 yoffset 40 rotate -10
        pause 0.25
        ease 1.0 yoffset -10 rotate -5
        pause 0.1
        repeat

image Jubes_handjob_over_hand_animation2:
    animation
    "Jubes_handjob_over"

    subpixel True
    rotate -3
    block:
        ease 0.4 yoffset 30 rotate -7
        pause 0.1
        ease 0.4 yoffset -10 rotate -3
        pause 0.1
        repeat

layeredimage Jubes_sprite handjob:
    always:
        "Jubes_sprite standing" pos (0.05, 0.0)

    always:
        "Jubes_handjob_under_hand_animation[JubesX.primary_Action.speed]" pos (-0.035, 0.455) zoom 0.28

    always:
        "Zero_cock_Jubes"

    always:
        "Jubes_handjob_over_hand_animation[JubesX.primary_Action.speed]" pos (-0.035, 0.455) zoom 0.28

    anchor (0.5, 0.0) offset (220, -220) zoom 2.5

image Jubes_titjob_jacket_back_animation0:
    animation
    "Jubes_titjob_jacket_back"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Jubes_titjob_jacket_back_animation1:
    animation
    "Jubes_titjob_jacket_back"

    subpixel True
    block:
        ease 2 yoffset -50
        pause 0.2
        ease 2 yoffset 60
        pause 0.5
        repeat

image Jubes_titjob_jacket_back_animation2:
    animation
    "Jubes_titjob_jacket_back"

    subpixel True
    block:
        ease 1 yoffset -5
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Jubes_titjob_jacket_back_animation3:
    animation
    "Jubes_titjob_jacket_back"

    subpixel True
    block:
        ease 1 yoffset 60
        pause 0.15
        ease 0.45 yoffset 110
        repeat

image Jubes_titjob_jacket_back_animation5:
    animation
    "Jubes_titjob_jacket_back"

    subpixel True
    block:
        ease 2 yoffset 130
        pause 0.2
        ease 2 yoffset 140
        pause 0.5
        repeat

image Jubes_titjob_bra_back_animation0:
    animation
    "Jubes_titjob_bra_back"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Jubes_titjob_bra_back_animation1:
    animation
    "Jubes_titjob_bra_back"

    subpixel True
    block:
        pause 0.1
        ease 1.9 yoffset -60
        pause 0.4
        ease 1.8 yoffset 60
        ease 0.5 yoffset 56
        repeat

image Jubes_titjob_bra_back_animation2:
    animation
    "Jubes_titjob_bra_back"

    subpixel True
    block:
        ease 0.3 yoffset 65
        ease 0.7 yoffset -20
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Jubes_titjob_bra_back_animation3:
    animation
    "Jubes_titjob_bra_back"

    subpixel True
    block:
        ease 0.3 yoffset 100
        ease 0.7 yoffset 60
        pause 0.2
        ease 0.4 yoffset 110
        repeat

image Jubes_titjob_bra_back_animation5:
    animation
    "Jubes_titjob_bra_back"

    subpixel True
    block:
        pause 0.1
        ease 2 yoffset 100
        pause 0.2
        ease 2 yoffset 110
        pause 0.4
        repeat

image Jubes_titjob_body_animation0:
    animation
    "Jubes_titjob_body"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Jubes_titjob_body_animation1:
    animation
    "Jubes_titjob_body"

    subpixel True
    block:
        ease 2 yoffset -50
        pause 0.2
        ease 2 yoffset 60
        pause 0.5
        repeat

image Jubes_titjob_body_animation2:
    animation
    "Jubes_titjob_body"

    subpixel True
    block:
        ease 1 yoffset -5
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Jubes_titjob_body_animation3:
    animation
    "Jubes_titjob_body"

    subpixel True
    block:
        ease 1 yoffset 60
        pause 0.15
        ease 0.45 yoffset 110
        repeat

image Jubes_titjob_body_animation5:
    animation
    "Jubes_titjob_body"

    subpixel True
    block:
        ease 2 yoffset 130
        pause 0.2
        ease 2 yoffset 140
        pause 0.5
        repeat

image Jubes_titjob_head_animation0:
    animation
    "Jubes_blowjob_head"

    subpixel True
    parallel:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat
    parallel:
        pause 0.1
        ease 2 rotate -0.5
        pause 0.1
        ease 2 rotate 0
        repeat

image Jubes_titjob_head_animation1:
    animation
    "Jubes_blowjob_head"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset -40
        pause 0.2
        ease 2 yoffset 60
        pause 0.5
        repeat
    parallel:
        ease 2.3 rotate 0
        pause 0.2
        ease 2.2 rotate -5
        pause 0.5
        repeat

image Jubes_titjob_head_animation2:
    animation
    "Jubes_blowjob_head"

    subpixel True
    rotate -5
    parallel:
        ease 1 yoffset -20
        pause 0.1
        ease 0.5 yoffset 80
        repeat
    parallel:
        ease 1 rotate 0
        pause 0.1
        ease 0.5 rotate -5
        repeat

image Jubes_titjob_head_animation3:
    animation
    "Jubes_blowjob_head"

    subpixel True
    rotate -5
    parallel:
        ease 1 yoffset 80
        pause 0.1
        ease 0.5 yoffset 140
        repeat
    parallel:
        ease 1 rotate 0
        pause 0.1
        ease 0.5 rotate -5
        repeat

image Jubes_titjob_head_animation5:
    animation
    "Jubes_blowjob_head"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset 125
        pause 0.2
        ease 2 yoffset 130
        pause 0.5
        repeat
    parallel:
        ease 2 rotate -5
        pause 0.5
        repeat

image Jubes_titjob_breasts_under_animation0:
    animation
    "Jubes_titjob_breasts_under"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Jubes_titjob_breasts_under_animation1:
    animation
    "Jubes_titjob_breasts_under"

    subpixel True
    block:
        pause 0.1
        ease 1.9 yoffset -60
        pause 0.4
        ease 1.8 yoffset 60
        ease 0.5 yoffset 56
        repeat

image Jubes_titjob_breasts_under_animation2:
    animation
    "Jubes_titjob_breasts_under"

    subpixel True
    block:
        ease 0.3 yoffset 65
        ease 0.7 yoffset -20
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Jubes_titjob_breasts_under_animation3:
    animation
    "Jubes_titjob_breasts_under"

    subpixel True
    block:
        ease 0.3 yoffset 100
        ease 0.7 yoffset 60
        pause 0.2
        ease 0.4 yoffset 110
        repeat

image Jubes_titjob_breasts_under_animation5:
    animation
    "Jubes_titjob_breasts_under"

    subpixel True
    block:
        pause 0.1
        ease 2 yoffset 100
        pause 0.2
        ease 2 yoffset 110
        pause 0.4
        repeat

image Jubes_titjob_breasts_animation0:
    animation
    "Jubes_titjob_breasts"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Jubes_titjob_breasts_animation1:
    animation
    "Jubes_titjob_breasts"

    subpixel True
    block:
        pause 0.1
        ease 1.9 yoffset -60
        pause 0.4
        ease 1.8 yoffset 60
        ease 0.5 yoffset 56
        repeat

image Jubes_titjob_breasts_animation2:
    animation
    "Jubes_titjob_breasts"

    subpixel True
    block:
        ease 0.3 yoffset 65
        ease 0.7 yoffset -20
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Jubes_titjob_breasts_animation3:
    animation
    "Jubes_titjob_breasts"

    subpixel True
    block:
        ease 0.3 yoffset 100
        ease 0.7 yoffset 60
        pause 0.2
        ease 0.4 yoffset 110
        repeat

image Jubes_titjob_breasts_animation5:
    animation
    "Jubes_titjob_breasts"

    subpixel True
    block:
        pause 0.1
        ease 2 yoffset 100
        pause 0.2
        ease 2 yoffset 110
        pause 0.4
        repeat

layeredimage Jubes_sprite titjob:
    # if JubesX.Clothes["jacket"].string:
    #     "Jubes_titjob_jacket_back_animation[JubesX.primary_Action.speed]"
    #
    # if JubesX.Clothes["bra"].string in ["blue_sports_bra", "pink_bikini_top"]:
    #     "Jubes_titjob_bra_back_animation[JubesX.primary_Action.speed]"

    always:
        "Jubes_titjob_body_animation[JubesX.primary_Action.speed]"

    always:
        "Jubes_titjob_head_animation[JubesX.primary_Action.speed]" pos (0.0, -0.19) zoom 0.9

    always:
        "Jubes_titjob_breasts_under_animation[JubesX.primary_Action.speed]"

    always:
        "Zero_cock_Jubes"

    always:
        "Jubes_titjob_breasts_animation[JubesX.primary_Action.speed]"

    anchor (0.5, 0.0) offset (360, 800) zoom 1.15

image Jubes_blowjob_blinking:
    "images/Jubes_blowjob/Jubes_blowjob_eyes_[JubesX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Jubes_blowjob/Jubes_blowjob_eyes_squint.png"
    0.05
    "images/Jubes_blowjob/Jubes_blowjob_eyes_closed.png"
    0.15
    "images/Jubes_blowjob/Jubes_blowjob_eyes_squint.png"
    0.05
    repeat
