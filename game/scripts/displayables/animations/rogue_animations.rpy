image Rogue_blinking:
    "images/Rogue_blowjob/Rogue_blowjob_eyes_[RogueX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Rogue_blowjob/Rogue_blowjob_eyes_half.png"
    0.05
    "images/Rogue_blowjob/Rogue_blowjob_eyes_closed.png"
    0.15
    "images/Rogue_blowjob/Rogue_blowjob_eyes_half.png"
    0.05
    repeat

layeredimage Rogue_grool_dripping_animation:
    always:
        "grool_dripping_animation" pos (0.26, 1.2)

    if RogueX.grool > 1 and not RogueX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.26, 1.2)

    if RogueX.grool > 1 and not RogueX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.26, 1.2)

    if RogueX.grool > 1 and not RogueX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.26, 1.2)

layeredimage Rogue_grool_animations:
    if not RogueX.grool:
        Null()
    elif RogueX.Clothes["pants"].state:
        AlphaMask("Rogue_grool_dripping_animation", "images/Rogue_standing/Rogue_standing_grool_mask_pants.png")
    elif RogueX.Clothes["underwear"].state:
        AlphaMask("Rogue_grool_dripping_animation", "images/Rogue_standing/Rogue_standing_grool_mask_underwear.png")
    elif not RogueX.Outfit.pussy_covered:
        AlphaMask("Rogue_grool_dripping_animation", "images/Rogue_standing/Rogue_standing_grool_mask.png")

layeredimage Rogue_spunk_dripping_animation:
    always:
        "spunk_dripping_animation" pos (0.26, 1.2)

    if not RogueX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.26, 1.2)

    if not RogueX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.26, 1.2)

    if not RogueX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.26, 1.2)

layeredimage Rogue_spunk_animations:
    if not RogueX.spunk["pussy"] and not RogueX.spunk["anus"]:
        Null()
    elif RogueX.Clothes["pants"].state:
        AlphaMask("Rogue_spunk_dripping_animation", "images/Rogue_standing/Rogue_standing_grool_mask_pants.png")
    elif RogueX.Clothes["underwear"].state:
        AlphaMask("Rogue_spunk_dripping_animation", "images/Rogue_standing/Rogue_standing_grool_mask_underwear.png")
    elif not RogueX.Outfit.pussy_covered:
        AlphaMask("Rogue_spunk_dripping_animation", "images/Rogue_standing/Rogue_standing_grool_mask.png")

layeredimage Rogue_standing_fondling_animations:
    if RogueX.primary_Action.Target != RogueX:
        Null()
    elif RogueX.primary_Action.type == "fondle_breasts":
        "Girl_fondle_breast_right_animation" pos (0.17, 0.72)
    elif RogueX.primary_Action.type == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.235, 1.07)
    elif RogueX.primary_Action.type in "finger_pussy":
        "Girl_finger_pussy_animation" pos (0.242, 1.135)

    if RogueX.secondary_Action.Target != RogueX:
        Null()
    elif RogueX.secondary_Action.type == "fondle_breasts":
        "Girl_fondle_breast_left_animation" pos (0.313, 0.725)
    elif RogueX.secondary_Action.type == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.235, 1.07)
    elif RogueX.secondary_Action.type in "finger_pussy":
        "Girl_finger_pussy_animation" pos (0.242, 1.135)

    if Player.primary_Action.Target != RogueX:
        Null()
    elif Player.primary_Action.type == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.185, 1.3)
    elif Player.primary_Action.type == "fondle_breasts":
        "Zero_fondle_breasts_left_animation" pos (0.277, 0.715)
    elif Player.primary_Action.type == "suck_breasts":
        "Zero_suck_breasts_left_animation" pos (0.305, 0.685)
    elif Player.primary_Action.type == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.245, 1.05)
    elif Player.primary_Action.type == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.215, 1.25)
    elif Player.primary_Action.type == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.25, 1.17)

    if Player.secondary_Action.Target != RogueX:
        Null()
    elif Player.secondary_Action.type == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.185, 1.3)
    elif Player.secondary_Action.type == "fondle_breasts":
        "Zero_fondle_breasts_right_animation" pos (0.212, 0.725)
    elif Player.secondary_Action.type == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.15, 0.66)
    elif Player.secondary_Action.type == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.245, 1.05)
    elif Player.secondary_Action.type == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.215, 1.25)
    elif Player.secondary_Action.type == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.25, 1.17)

image Rogue_handjob_under_hand_animation0:
    "Rogue_handjob_under"

image Rogue_handjob_under_hand_animation1:
    animation
    "Rogue_handjob_under"

    subpixel True
    rotate -5
    block:
        ease 0.75 yoffset 40 rotate 5
        pause 0.25
        ease 1.0 yoffset -10 rotate -5
        pause 0.1
        repeat

image Rogue_handjob_under_hand_animation2:
    animation
    "Rogue_handjob_under"

    subpixel True
    rotate -3
    block:
        ease 0.4 yoffset 30 rotate 3
        pause 0.1
        ease 0.4 yoffset -10 rotate -3
        pause 0.1
        repeat

image Rogue_handjob_over_hand_animation0:
    "Rogue_handjob_over"

image Rogue_handjob_over_hand_animation1:
    animation
    "Rogue_handjob_over"

    subpixel True
    rotate -5
    block:
        ease 0.75 yoffset 40 rotate 5
        pause 0.25
        ease 1.0 yoffset -10 rotate -5
        pause 0.1
        repeat

image Rogue_handjob_over_hand_animation2:
    animation
    "Rogue_handjob_over"

    subpixel True
    rotate -3
    block:
        ease 0.4 yoffset 30 rotate 3
        pause 0.1
        ease 0.4 yoffset -10 rotate -3
        pause 0.1
        repeat

layeredimage Rogue_sprite handjob:
    always:
        "Rogue_sprite standing" pos (0.05, 0.0)

    always:
        "Rogue_handjob_under_hand_animation[RogueX.primary_Action.speed]" pos (-0.035, 0.455) zoom 0.28

    always:
        "Zero_cock_Rogue"

    always:
        "Rogue_handjob_over_hand_animation[RogueX.primary_Action.speed]" pos (-0.035, 0.455) zoom 0.28

    anchor (0.5, 0.0) offset (220, -220) zoom 2.5

image Rogue_titjob_hair_back_animation0:
    "Rogue_hair_back"

image Rogue_titjob_hair_back_animation1:
    animation
    "Rogue_hair_back"

    subpixel True
    block:
        ease 1.0 yoffset 100
        ease 0.2 yoffset 100
        ease 1.3 yoffset -80
        repeat

image Rogue_titjob_hair_back_animation2:
    animation
    "Rogue_hair_back"

    subpixel True
    block:
        ease 0.28 yoffset 10
        ease 0.37 yoffset -55
        ease 0.1 yoffset -50
        repeat

image Rogue_titjob_hair_back_animation3:
    animation
    "Rogue_hair_back"

    subpixel True
    rotate -10
    ease 0.5 offset (-30, 150)
    parallel:
        ease 2.5 offset (-30, 250)
        ease 2 offset (-30, 150)
        pause 0.5
        repeat
    parallel:
        ease 2.5 rotate -10
        ease 2 rotate -5
        pause 0.5
        repeat

image Rogue_titjob_hair_back_animation5:
    animation
    "Rogue_hair_back"

    subpixel True
    block:
        ease 2 yoffset 174
        ease 1.6 yoffset 177
        pause 0.4
        repeat

image Rogue_titjob_body_animation0:
    "Rogue_titjob_body"

image Rogue_titjob_body_animation1:
    animation
    "Rogue_titjob_body"

    subpixel True
    block:
        ease 1.0 yoffset 100
        ease 0.2 yoffset 100
        ease 1.3 yoffset -80
        repeat

image Rogue_titjob_body_animation2:
    animation
    "Rogue_titjob_body"

    subpixel True
    block:
        ease 0.28 yoffset 10
        ease 0.37 yoffset -55
        ease 0.1 yoffset -50
        repeat

image Rogue_titjob_body_animation3:
    animation
    "Rogue_titjob_body"

    subpixel True
    ease 0.5 yoffset 90
    block:
        ease 2.5 yoffset 170
        ease 2 yoffset 90
        pause 0.5
        repeat

image Rogue_titjob_body_animation5:
    animation
    "Rogue_titjob_body"

    subpixel True
    block:
        ease 2.2 yoffset 120
        ease 1.6 yoffset 140
        pause 0.2
        repeat

image Rogue_titjob_head_animation0:
    "Rogue_head"

image Rogue_titjob_head_animation1:
    animation
    "Rogue_head"

    subpixel True
    block:
        ease 1.0 yoffset 100
        ease 0.2 yoffset 100
        ease 1.3 yoffset -80
        repeat

image Rogue_titjob_head_animation2:
    animation
    "Rogue_head"

    subpixel True
    block:
        ease 0.28 yoffset 10
        ease 0.37 yoffset -55
        ease 0.1 yoffset -50
        repeat

image Rogue_titjob_head_animation3:
    animation
    "Rogue_head"

    subpixel True
    rotate -10
    ease 0.5 offset (-30, 150)
    parallel:
        ease 2.5 offset (-30, 250)
        ease 2 offset (-30, 150)
        pause 0.5
        repeat
    parallel:
        ease 2.5 rotate -10
        ease 2 rotate -5
        pause 0.5
        repeat

image Rogue_titjob_head_animation5:
    animation
    "Rogue_head"

    subpixel True
    block:
        ease 2 yoffset 174
        ease 1.6 yoffset 177
        pause 0.4
        repeat

image Rogue_titjob_breasts_animation0:
    "Rogue_titjob_breasts"

image Rogue_titjob_breasts_animation1:
    animation
    "Rogue_titjob_breasts"

    subpixel True
    block:
        ease 1.20 yoffset 100
        ease 0.1 yoffset 100
        ease 1.2 yoffset -80
        repeat

image Rogue_titjob_breasts_animation2:
    animation
    "Rogue_titjob_breasts"

    subpixel True
    block:
        ease 0.33 yoffset 10
        ease 0.32 yoffset -55
        ease 0.1 yoffset -50
        repeat

image Rogue_titjob_breasts_animation3:
    animation
    "Rogue_titjob_breasts"

    subpixel True
    ease 0.5 yoffset 90
    block:
        ease 2.6 yoffset 170
        ease 2.1 yoffset 90
        pause 0.3
        repeat

image Rogue_titjob_breasts_animation5:
    animation
    "Rogue_titjob_breasts"

    subpixel True
    block:
        ease 2.2 yoffset 120
        ease 1.6 yoffset 140
        pause 0.2
        repeat

layeredimage Rogue_sprite titjob:
    always:
        "Rogue_titjob_hair_back_animation[RogueX.primary_Action.speed]" pos (0.025, -0.48) zoom 0.9

    always:
        "Rogue_titjob_body_animation[RogueX.primary_Action.speed]"

    always:
        "Rogue_titjob_head_animation[RogueX.primary_Action.speed]" pos (0.025, -0.48) zoom 0.9

    always:
        "Zero_cock_Rogue"

    always:
        "Rogue_titjob_breasts_animation[RogueX.primary_Action.speed]"

    anchor (0.5, 0.0) offset (200, 850) zoom 0.72

image Rogue_blowjob_hair_back_animation0:
    "Rogue_hair_back"

image Rogue_blowjob_hair_back_animation1:
    animation
    "Rogue_hair_back"

    subpixel True
    ease 0.5 offset (2, -20)
    block:
        ease 2.5 offset (15, 60)
        ease 2 offset (2, -20)
        pause 0.5
        repeat

image Rogue_blowjob_hair_back_animation2:
    animation
    "Rogue_hair_back"

    subpixel True
    block:
        ease 1 yoffset 35
        ease 1.5 yoffset 0
        repeat

image Rogue_blowjob_hair_back_animation3:
    animation
    "Rogue_hair_back"

    subpixel True
    ease 0.5 offset (0, 30)
    block:
        ease 1 offset (-0.3, 60)
        ease 1.5 offset (0, 30)
        repeat

image Rogue_blowjob_hair_back_animation4:
    animation
    "Rogue_hair_back"

    subpixel True
    ease 0.5 offset (0, 40)
    block:
        ease 1 offset (0.5, 85)
        pause 0.5
        ease 2 offset (0, 40)
        repeat

image Rogue_blowjob_body_animation0:
    "Rogue_sprite standing"

image Rogue_blowjob_body_animation1:
    animation
    "Rogue_sprite standing"

    subpixel True
    ease 0.5 offset (2, -20)
    block:
        ease 2.5 offset (20, 55)
        ease 2 offset (2, -20)
        pause 0.5
        repeat

image Rogue_blowjob_body_animation2:
    animation
    "Rogue_sprite standing"

    subpixel True
    block:
        ease 1 yoffset 35
        ease 1.5 yoffset 0
        repeat

image Rogue_blowjob_body_animation3:
    animation
    "Rogue_sprite standing"

    subpixel True
    ease 0.5 offset (0, 30)
    block:
        ease 1 yoffset 45
        ease 1.5 yoffset 30
        repeat

image Rogue_blowjob_body_animation4:
    animation
    "Rogue_sprite standing"

    subpixel True
    ease 0.5 offset (0, 40)
    block:
        ease 1.2 yoffset 70
        pause 0.5
        ease 1.8 yoffset 40
        repeat

image Rogue_blowjob_head_animation0:
    "Rogue_head"

    ease 1.5 offset (0, 0)

image Rogue_blowjob_head_animation1:
    animation
    "Rogue_head"

    subpixel True
    ease 0.5 offset (2, -20)
    block:
        ease 2.5 offset (15, 60)
        ease 2 offset (2, -20)
        pause 0.5
        repeat

image Rogue_blowjob_head_animation2:
    animation
    "Rogue_head"

    subpixel True
    block:
        ease 1 yoffset 35
        ease 1.5 yoffset 0
        repeat

image Rogue_blowjob_head_animation3:
    animation
    "Rogue_head"

    subpixel True
    ease 0.5 offset (0, 30)
    block:
        ease 1 offset (-0.3, 60)
        ease 1.5 offset (0, 30)
        repeat

image Rogue_blowjob_head_animation4:
    animation
    "Rogue_head"

    subpixel True
    ease 0.5 offset (0, 40)
    block:
        ease 1 offset (0.5, 85)
        pause 0.5
        ease 2 offset (0, 40)
        repeat

image Rogue_blowjob_mouth_animation2:
    animation
    "Rogue_blowjob_mouth"

    subpixel True
    zoom 0.94
    block:
        pause 0.10
        ease 0.55 zoom 0.94
        linear 0.10 zoom 0.84
        ease 0.30 zoom 0.94
        pause 0.15
        ease 0.40 zoom 0.84
        linear 0.10 zoom 0.94
        ease 0.45 zoom 0.6
        pause 0.35
        repeat

image Rogue_blowjob_mouth_animation3:
    animation
    "Rogue_blowjob_mouth"

    subpixel True
    zoom 0.9
    block:
        ease 0.5 zoom 0.9
        ease 0.5 zoom 0.97
        ease 0.75 zoom 0.94
        ease 0.75 zoom 0.97
        repeat

image Rogue_blowjob_mouth_animation4:
    animation
    "Rogue_blowjob_mouth"

    subpixel True
    zoom 0.94
    block:
        ease 0.5 zoom 0.94
        ease 0.5 zoom 1.0
        pause 0.5
        ease 0.5 zoom 0.96
        ease 1.5 zoom 1.0
        repeat

image Rogue_blowjob_mask_animation2:
    animation
    "Rogue_blowjob_mask"

    subpixel True
    zoom 0.94
    block:
        pause 0.10
        ease 0.55 zoom 0.94
        linear 0.10 zoom 0.84
        ease 0.30 zoom 0.94
        pause 0.15
        ease 0.40 zoom 0.84
        linear 0.10 zoom 0.94
        ease 0.45 zoom 0.6
        pause 0.35
        repeat

image Rogue_blowjob_mask_animation3:
    animation
    "Rogue_blowjob_mask"

    subpixel True
    zoom 0.9
    block:
        ease 0.5 zoom 0.9
        ease 0.5 zoom 0.97
        ease 0.75 zoom 0.94
        ease 0.75 zoom 0.97
        repeat

image Rogue_blowjob_mask_animation4:
    animation
    "Rogue_blowjob_mask"

    subpixel True
    zoom 0.94
    block:
        ease 0.25 zoom 0.94
        ease 0.25 zoom 1.0
        pause 0.5
        ease 1.0 zoom 0.96
        ease 1.0 zoom 1.0
        repeat

image Rogue_blowjob_face_mask_animation2:
    animation
    AlphaMask("Rogue_head", "Rogue_blowjob_mask_animation2")

    subpixel True
    block:
        ease 1 yoffset 35
        ease 1.5 yoffset 0
        repeat

image Rogue_blowjob_face_mask_animation3:
    animation
    AlphaMask("Rogue_head", "Rogue_blowjob_mask_animation3")

    subpixel True
    ease 0.5 offset (0, 30)
    block:
        ease 1 offset (-0.3, 60)
        ease 1.5 offset (0, 30)
        repeat

image Rogue_blowjob_face_mask_animation4:
    animation
    AlphaMask("Rogue_head", "Rogue_blowjob_mask_animation4")

    subpixel True
    ease 0.5 offset (0, 40)
    block:
        ease 1 offset (0.5, 85)
        pause 0.5
        ease 2 offset (0, 40)
        repeat

layeredimage Rogue_sprite blowjob:
    always:
        "Rogue_blowjob_hair_back_animation[RogueX.primary_Action.speed]" pos (0.031, 0.317) zoom 0.2755

    always:
        "Rogue_blowjob_body_animation[RogueX.primary_Action.speed]"

    always:
        "Rogue_blowjob_head_animation[RogueX.primary_Action.speed]" pos (0.031, 0.317) zoom 0.2755

    always:
        "Zero_cock_Rogue"

    if RogueX.primary_Action.speed > 1:
        "Rogue_blowjob_face_mask_animation[RogueX.primary_Action.speed]" anchor (0.5, 0.5) pos (0.031, 0.317) zoom 0.2755

    anchor (0.5, 0.0) offset (220, -320) zoom 2.75

image Rogue_sex_body_animation0:
    "Rogue_sex_body"

image Rogue_sex_body_animation1:
    animation
    "Rogue_sex_body"

    subpixel True
    block:
        pause 0.5
        ease 0.75 yoffset -5
        pause 1.25
        ease 2.5 yoffset 0
        repeat

image Rogue_sex_body_animation2:
    animation
    "Rogue_sex_body"

    subpixel True
    block:
        pause 0.6
        ease 0.4 yoffset -10
        ease 0.25 yoffset -5
        pause 1
        ease 2.75 yoffset 10
        repeat

image Rogue_sex_body_animation3:
    animation
    "Rogue_sex_body"

    subpixel True
    block:
        pause 0.17
        ease 0.13 yoffset -20
        ease 0.10 yoffset -15
        pause 0.20
        ease 1.4 yoffset 10
        repeat

image Rogue_sex_body_footjob_animation0:
    "Rogue_sex_body"

image Rogue_sex_body_footjob_animation1:
    animation
    "Rogue_sex_body"

    subpixel True
    block:
        pause 0.5
        ease 0.75 yoffset -25
        ease 0.25 yoffset -15
        pause 1
        ease 2.50 yoffset 15
        repeat

image Rogue_sex_body_footjob_animation2:
    animation
    "Rogue_sex_body"

    subpixel True
    block:
        pause 0.2
        ease 0.4 yoffset -25
        ease 0.2 yoffset -15
        pause 0.2
        ease 1.0 yoffset 15
        repeat

image Rogue_sex_body_hotdog_animation0:
    "Rogue_sex_body"

image Rogue_sex_body_hotdog_animation1:
    "Rogue_sex_body"

image Rogue_sex_body_hotdog_animation2:
    animation
    "Rogue_sex_body"

    subpixel True
    block:
        pause 0.30
        ease 0.50 yoffset -10
        pause 0.20
        ease 1 yoffset 0
        repeat

image Rogue_sex_body_hotdog_animation3:
    animation
    "Rogue_sex_body"

    subpixel True
    block:
        pause 0.30
        ease 0.50 yoffset -10
        pause 0.20
        ease 1 yoffset 0
        repeat

image Rogue_sex_legs_animation0:
    "Rogue_sex_legs"

image Rogue_sex_legs_animation1:
    animation
    "Rogue_sex_legs"

    subpixel True
    block:
        pause 0.25
        ease 1 yoffset -5
        pause 1
        ease 2.75 yoffset 0
        repeat

image Rogue_sex_legs_animation2:
    animation
    "Rogue_sex_legs"

    subpixel True
    block:
        pause 0.5
        ease 0.5 yoffset -15
        ease 0.25 yoffset -10
        pause 1
        ease 2.75 yoffset 0
        repeat

image Rogue_sex_legs_animation3:
    animation
    "Rogue_sex_legs"

    subpixel True
    block:
        pause 0.15
        ease 0.15 yoffset -20
        ease 0.10 yoffset -15
        pause 0.20
        ease 1.4 yoffset 0
        repeat

image Rogue_sex_legs_footjob_animation0:
    "Rogue_sex_legs"

image Rogue_sex_legs_footjob_animation1:
    animation
    "Rogue_sex_legs"

    subpixel True
    block:
        pause 0.5
        ease 1.0 yoffset -25
        ease 0.5 yoffset -20
        pause 1
        ease 2. yoffset 25
        repeat

image Rogue_sex_legs_footjob_animation2:
    animation
    "Rogue_sex_legs"

    subpixel True
    block:
        pause 0.2
        ease 0.5 yoffset -25
        ease 0.3 yoffset -20
        pause 0.2
        ease 0.8 yoffset 25
        repeat

image Rogue_sex_legs_hotdog_animation0:
    "Rogue_sex_legs"

image Rogue_sex_legs_hotdog_animation1:
    "Rogue_sex_legs"

image Rogue_sex_legs_hotdog_animation2:
    animation
    "Rogue_sex_legs"

    subpixel True
    block:
        pause 0.20
        ease 0.50 yoffset -10
        pause 0.20
        ease 1.1 yoffset 0
        repeat

image Rogue_sex_legs_hotdog_animation3:
    animation
    "Rogue_sex_legs"

    subpixel True
    block:
        pause 0.20
        ease 0.50 yoffset -10
        pause 0.20
        ease 1.1 yoffset 0
        repeat

image Rogue_sex_anus_animation0:
    "Rogue_sex_anus"

    xzoom 0.6

image Rogue_sex_anus_animation1:
    animation
    "Rogue_sex_anus"

    subpixel True
    xzoom 0.6
    block:
        ease 0.75 xzoom 1.0
        ease 0.25 xzoom 0.9
        pause 1.50
        ease 0.25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Rogue_sex_anus_animation2:
    "Rogue_sex_anus"

image Rogue_sex_anus_animation3:
    "Rogue_sex_anus"

image Rogue_sex_spunk_anus_under_animation:
    animation
    "Rogue_sex_spunk_anus_under"

    subpixel True
    xzoom 0.6
    block:
        ease 0.75 xzoom 1.0
        ease 0.25 xzoom 0.95
        pause 1.50
        ease 0.25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Rogue_sex_spunk_anus_over_animation:
    animation
    "Rogue_sex_spunk_anus_over"

    subpixel True
    xzoom 0.8
    block:
        ease 0.75 xzoom 1.0
        pause 1.75
        ease 0.25 xzoom 1.0
        ease 2.25 xzoom 0.8
        repeat

layeredimage Rogue_sprite sex:
    if Player.primary_Action.type in ["sex", "anal"]:
        "Rogue_sex_body_animation[Player.primary_Action.speed]"
    elif Player.primary_Action.type == "hotdog":
        "Rogue_sex_body_hotdog_animation[Player.primary_Action.speed]"
    elif RogueX.primary_Action.type == "footjob":
        "Rogue_sex_body_footjob_animation[RogueX.primary_Action.speed]"

    if Player.primary_Action.type in ["sex", "anal"]:
        "Rogue_sex_legs_animation[Player.primary_Action.speed]"
    elif Player.primary_Action.type == "hotdog":
        "Rogue_sex_legs_hotdog_animation[Player.primary_Action.speed]"
    elif RogueX.primary_Action.type == "footjob":
        "Rogue_sex_legs_footjob_animation[RogueX.primary_Action.speed]"

    anchor (0.5, 0.0) offset (370, 770)

image Rogue_doggy_blinking:
    "images/Rogue_doggy/Rogue_doggy_eyes_[RogueX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Rogue_doggy/Rogue_doggy_eyes_squint.png"
    0.05
    "images/Rogue_doggy/Rogue_doggy_eyes_closed.png"
    0.15
    "images/Rogue_doggy/Rogue_doggy_eyes_squint.png"
    0.05
    repeat

image Rogue_doggy_body_animation0:
    "Rogue_doggy_body"

image Rogue_doggy_body_animation1:
    animation
    "Rogue_doggy_body"

    subpixel True
    block:
        pause 0.4
        ease 0.3 yoffset -5
        ease 1 yoffset 0
        pause 0.8
        repeat

image Rogue_doggy_body_animation2:
    animation
    "Rogue_doggy_body"

    subpixel True
    block:
        ease 0.5 yoffset 5
        pause 0.25
        ease 1.75 yoffset 15
        repeat

image Rogue_doggy_body_animation3:
    animation
    "Rogue_doggy_body"

    subpixel True
    block:
        pause 0.15
        ease 0.1 yoffset 0
        pause 0.1
        ease 0.5 yoffset 20
        pause 0.05
        repeat

image Rogue_doggy_ass_animation0:
    "Rogue_doggy_ass"

image Rogue_doggy_ass_animation1:
    animation
    "Rogue_doggy_ass"

    subpixel True
    block:
        pause 0.4
        ease 0.2 yoffset -10
        ease 0.1 yoffset -7
        ease 0.9 yoffset 0
        pause 0.9
        repeat

image Rogue_doggy_ass_animation2:
    animation
    "Rogue_doggy_ass"

    subpixel True
    block:
        ease 0.3 yoffset -15
        ease 0.2 yoffset -5
        pause 0.25
        ease 1.75 yoffset 0
        repeat

image Rogue_doggy_ass_animation3:
    animation
    "Rogue_doggy_ass"

    subpixel True
    block:
        pause 0.15
        ease 0.1 yoffset -25
        ease 0.1 yoffset -15
        pause 0.1
        ease 0.4 yoffset 5
        pause 0.05
        repeat

image Rogue_doggy_pussy_hole_animation0:
    animation
    "Rogue_doggy_pussy_hole"

    subpixel True
    xzoom 0.6
    block:
        ease 1 xzoom 0.65
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_pussy_hole_animation1:
    animation
    "Rogue_doggy_pussy_hole"

    subpixel True
    xzoom 0.6
    block:
        ease 1 xzoom 1
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_pussy_hole_animation2:
    "Rogue_doggy_pussy_hole"

image Rogue_doggy_pussy_hole_animation3:
    "Rogue_doggy_pussy_hole"

image Rogue_doggy_pussy_hole_fingering:
    animation
    "Rogue_doggy_pussy_hole"

    subpixel True
    xzoom 0.6
    block:
        ease 1 xzoom 0.67
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_anus_anal_animation1:
    animation
    "Rogue_doggy_anus_hole"

    subpixel True
    zoom 0.5
    block:
        ease 0.5 zoom 1
        pause 0.5
        ease 1.5 zoom 0.5
        repeat

image Rogue_doggy_anus_anal_animation2:
    "Rogue_doggy_anus_hole"

    zoom 0.9

image Rogue_doggy_anus_anal_animation3:
    "Rogue_doggy_anus_hole"

    zoom 0.9

image Rogue_doggy_anus_fingering_animation:
    animation
    "Rogue_doggy_anus_hole"

    subpixel True
    zoom 0.6
    block:
        ease 0.5 zoom 0.67
        pause 0.5
        ease 1.5 zoom 0.6
        repeat

image Rogue_doggy_shin_animation0:
    animation
    "Rogue_doggy_shins"

    subpixel True
    block:
        pause 0.5
        ease 2 yoffset 20
        pause 0.5
        ease 2 yoffset 0
        repeat

image Rogue_doggy_shin_animation1:
    animation
    "Rogue_doggy_shins"

    subpixel True
    block:
        pause 0.3
        ease 1.7 yoffset 100
        ease 1 yoffset 0
        repeat

image Rogue_doggy_shin_animation2:
    animation
    "Rogue_doggy_shins"

    subpixel True
    block:
        pause 0.05
        ease 0.6 yoffset 110
        ease 0.3 yoffset 0
        repeat

image Rogue_doggy_feet_animation0:
    animation
    "Rogue_doggy_feet"

    subpixel True
    block:
        pause 0.5
        ease 2 yoffset 20
        pause 0.5
        ease 2 yoffset 0
        repeat

image Rogue_doggy_feet_animation1:
    animation
    "Rogue_doggy_feet"

    subpixel True
    block:
        pause 0.3
        ease 1.7 yoffset 100
        ease 1 yoffset 0
        repeat

image Rogue_doggy_feet_animation2:
    animation
    "Rogue_doggy_feet"

    subpixel True
    block:
        pause 0.05
        ease 0.6 yoffset 110
        ease 0.3 yoffset 0
        repeat

layeredimage Rogue_sprite doggy:
    if Player.primary_Action.type == "anal":
        "Rogue_doggy_body_animation[Player.primary_Action.speed]"
    elif Player.primary_Action.type == "sex" and Player.primary_Action.speed > 1:
        "Rogue_doggy_body_animation[Player.primary_Action.speed]"
    else:
        "Rogue_doggy_body"

    if Player.primary_Action.type == "anal":
        "Rogue_doggy_ass_animation[Player.primary_Action.speed]"
    elif Player.primary_Action.type == "sex" and Player.primary_Action.speed > 1:
        "Rogue_doggy_ass_animation[Player.primary_Action.speed]"
    else:
        "Rogue_doggy_ass"

    if Player.sprite and RogueX.primary_Action.type == "footjob":
        "Rogue_doggy_shin_animation[RogueX.primary_Action.speed]"
    elif not Player.sprite and show_feet:
        "Rogue_doggy_shins"

    if Player.sprite and RogueX.primary_Action.type == "footjob":
        "Zero_cock_Rogue"

    if Player.primary_Action.type == "footjob":
        "Rogue_doggy_feet_animation[RogueX.primary_Action.speed]"
    elif not Player.sprite and show_feet:
        "Rogue_doggy_feet"

    anchor (0.5, 0.0) offset (150, 700) zoom 1.2
