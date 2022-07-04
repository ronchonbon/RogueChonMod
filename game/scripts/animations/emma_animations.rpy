image Emma_blinking:
    "images/Emma_standing/Emma_standing_eyes_[EmmaX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Emma_standing/Emma_standing_eyes_squint.png"
    0.05
    "images/Emma_standing/Emma_standing_eyes_closed.png"
    0.15
    "images/Emma_standing/Emma_standing_eyes_squint.png"
    0.05
    repeat

image Emma_blinking_diamond:
    "images/Emma_standing/Emma_standing_eyes_[EmmaX.eyes]_diamond.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Emma_standing/Emma_standing_eyes_squint_diamond.png"
    0.05
    "images/Emma_standing/Emma_standing_eyes_closed_diamond.png"
    0.15
    "images/Emma_standing/Emma_standing_eyes_squint_diamond.png"
    0.05
    repeat

layeredimage Emma_grool_dripping_animation:
    always:
        "grool_dripping_animation" pos (0.232, 1.1)

    if EmmaX.grool > 1 and not EmmaX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.232, 1.1)

    if EmmaX.grool > 1 and not EmmaX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.232, 1.1)

    if EmmaX.grool > 1 and not EmmaX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.232, 1.1)

layeredimage Emma_grool_animations:
    if not EmmaX.grool:
        Null()
    elif EmmaX.Clothes["pants"].state:
        AlphaMask("Emma_grool_dripping_animation", "images/Emma_standing/Emma_standing_grool_mask_pants.png")
    elif EmmaX.Clothes["underwear"].state:
        AlphaMask("Emma_grool_dripping_animation", "images/Emma_standing/Emma_standing_grool_mask_underwear.png")
    elif not EmmaX.Outfit.pussy_covered:
        AlphaMask("Emma_grool_dripping_animation", "images/Emma_standing/Emma_standing_grool_mask.png")

layeredimage Emma_spunk_dripping_animation:
    always:
        "spunk_dripping_animation" pos (0.232, 1.1)

    if not EmmaX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.232, 1.1)

    if not EmmaX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.232, 1.1)

    if not EmmaX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.232, 1.1)

layeredimage Emma_spunk_animations:
    if not EmmaX.spunk["pussy"] and not EmmaX.spunk["anus"]:
        Null()
    elif EmmaX.Clothes["pants"].state:
        AlphaMask("Emma_spunk_dripping_animation", "images/Emma_standing/Emma_standing_grool_mask_pants.png")
    elif EmmaX.Clothes["underwear"].state:
        AlphaMask("Emma_spunk_dripping_animation", "images/Emma_standing/Emma_standing_grool_mask_underwear.png")
    elif not EmmaX.Outfit.pussy_covered:
        AlphaMask("Emma_spunk_dripping_animation", "images/Emma_standing/Emma_standing_grool_mask.png")

layeredimage Emma_standing_fondling_animations:
    if EmmaX.primary_Action.Target != EmmaX:
        Null()
    elif EmmaX.primary_Action.type == "fondle_breasts":
        "Girl_fondle_breast_right_animation" pos (0.115, 0.715)
    elif EmmaX.primary_Action.type == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.22, 1.055)
    elif EmmaX.primary_Action.type in "finger_pussy":
        "Girl_finger_pussy_animation" pos (0.226, 1.1)

    if EmmaX.secondary_Action.Target != EmmaX:
        Null()
    elif EmmaX.secondary_Action.type == "fondle_breasts":
        "Girl_fondle_breast_left_animation" pos (0.245, 0.72)
    elif EmmaX.secondary_Action.type == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.22, 1.055)
    elif EmmaX.secondary_Action.type in "finger_pussy":
        "Girl_finger_pussy_animation" pos (0.226, 1.1)

    if Player.primary_Action.Target != EmmaX:
        Null()
    elif Player.primary_Action.type == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.15, 1.25)
    elif Player.primary_Action.type == "fondle_breasts":
        "Zero_fondle_breasts_left_animation" pos (0.205, 0.72)
    elif Player.primary_Action.type == "suck_breasts":
        "Zero_suck_breasts_left_animation" pos (0.23, 0.65)
    elif Player.primary_Action.type == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.25, 1.1)
    elif Player.primary_Action.type == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.2, 1.22)
    elif Player.primary_Action.type == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.225, 1.125)

    if Player.secondary_Action.Target != EmmaX:
        Null()
    elif Player.secondary_Action.type == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.15, 1.25)
    elif Player.secondary_Action.type == "fondle_breasts":
        "Zero_fondle_breasts_right_animation" pos (0.14, 0.735)
    elif Player.secondary_Action.type == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.09, 0.67)
    elif Player.secondary_Action.type == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.25, 1.1)
    elif Player.secondary_Action.type == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.2, 1.22)
    elif Player.secondary_Action.type == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.225, 1.125)

image Emma_handjob_under_hand_animation0:
    "Emma_handjob_under"

image Emma_handjob_under_hand_animation1:
    animation
    "Emma_handjob_under"

    subpixel True
    rotate 8
    block:
        ease 0.75 yoffset 40 rotate 3
        pause 0.25
        ease 1.0 yoffset -10 rotate 8
        pause 0.1
        repeat

image Emma_handjob_under_hand_animation2:
    animation
    "Emma_handjob_under"

    subpixel True
    rotate 5
    block:
        ease 0.4 yoffset 30 rotate 3
        pause 0.1
        ease 0.4 yoffset -10 rotate 5
        pause 0.1
        repeat

image Emma_handjob_over_hand_animation0:
    "Emma_handjob_over"

image Emma_handjob_over_hand_animation1:
    animation
    "Emma_handjob_over"

    subpixel True
    rotate 8
    block:
        ease 0.75 yoffset 40 rotate 3
        pause 0.25
        ease 1.0 yoffset -10 rotate 8
        pause 0.1
        repeat

image Emma_handjob_over_hand_animation2:
    animation
    "Emma_handjob_over"

    subpixel True
    rotate 5
    block:
        ease 0.4 yoffset 30 rotate 3
        pause 0.1
        ease 0.4 yoffset -10 rotate 5
        pause 0.1
        repeat

layeredimage Emma_sprite handjob:
    always:
        "Emma_sprite standing" pos (0.05, 0.0)

    always:
        "Emma_handjob_under_hand_animation[EmmaX.primary_Action.speed]" pos (-0.035, 0.455) zoom 0.28

    always:
        "Zero_cock_Emma"

    always:
        "Emma_handjob_over_hand_animation[EmmaX.primary_Action.speed]" pos (-0.035, 0.455) zoom 0.28

    anchor (0.5, 0.0) offset (220, -220) zoom 2.5

image Emma_titjob_hair_back_animation0:
    animation
    "Emma_blowjob_hair_back"

    subpixel True
    block:
        ease 2.4 yoffset -10
        ease 1.6 yoffset 0
        repeat

image Emma_titjob_hair_back_animation1:
    animation
    "Emma_blowjob_hair_back"

    subpixel True
    block:
        pause 0.2
        ease 1.4 yoffset -10
        pause 0.3
        ease 0.6 yoffset 0
        repeat

image Emma_titjob_hair_back_animation2:
    animation
    "Emma_blowjob_hair_back"

    subpixel True
    block:
        pause 0.1
        ease 0.6 yoffset 0
        ease 0.3 yoffset 20
        repeat

image Emma_titjob_hair_back_animation3:
    animation
    "Emma_blowjob_hair_back"

    subpixel True
    block:
        ease 1.5 yoffset 10
        pause 0.7
        ease 0.9 yoffset 40
        pause 0.5
        repeat

image Emma_titjob_hair_back_animation5:
    animation
    "Emma_blowjob_hair_back"

    subpixel True
    block:
        ease 1.5 yoffset 38
        pause 0.7
        ease 0.3 yoffset 40
        pause 0.5
        repeat

image Emma_titjob_body_animation0:
    animation
    "Emma_sex_body"

    subpixel True
    block:
        ease 2 yoffset -5
        ease 2 yoffset 5
        repeat

image Emma_titjob_body_animation1:
    animation
    "Emma_sex_body"

    subpixel True
    block:
        pause 0.2
        ease 1.4 yoffset -20
        pause 0.3
        ease 0.6 yoffset 0
        repeat

image Emma_titjob_body_animation2:
    animation
    "Emma_sex_body"

    subpixel True
    block:
        pause 0.1
        ease 0.5 yoffset -20
        ease 0.3 yoffset 15
        pause 0.1
        repeat

image Emma_titjob_body_animation3:
    animation
    "Emma_sex_body"

    subpixel True
    block:
        ease 1.6 yoffset -20
        pause 0.7
        ease 0.8 yoffset 0
        pause 0.5
        repeat

image Emma_titjob_body_animation5:
    animation
    "Emma_sex_body"

    subpixel True
    block:
        ease 1.3 yoffset -5
        pause 0.7
        ease 1.1 yoffset 0
        pause 0.5
        repeat

image Emma_titjob_head_animation0:
    animation
    "Emma_blowjob_head"

    subpixel True
    block:
        ease 2.4 yoffset -10
        ease 1.6 yoffset 0
        repeat

image Emma_titjob_head_animation1:
    animation
    "Emma_blowjob_head"

    subpixel True
    block:
        pause 0.2
        ease 1.4 yoffset -10
        pause 0.3
        ease 0.6 yoffset 0
        repeat

image Emma_titjob_head_animation2:
    animation
    "Emma_blowjob_head"

    subpixel True
    block:
        pause 0.1
        ease 0.6 yoffset 0
        ease 0.3 yoffset 20
        repeat

image Emma_titjob_head_animation3:
    animation
    "Emma_blowjob_head"

    subpixel True
    block:
        ease 1.5 yoffset 10
        pause 0.7
        ease 0.9 yoffset 40
        pause 0.5
        repeat

image Emma_titjob_head_animation5:
    animation
    "Emma_blowjob_head"

    subpixel True
    block:
        ease 1.5 yoffset 38
        pause 0.7
        ease 0.3 yoffset 40
        pause 0.5
        repeat

image Emma_titjob_breasts_animation0:
    animation
    "Emma_titjob_breasts"

    subpixel True
    block:
        ease 2.2 yoffset -5
        ease 1.8 yoffset 0
        repeat

image Emma_titjob_breasts_animation1:
    animation
    "Emma_titjob_breasts"

    subpixel True
    block:
        ease 1.5 yoffset -30
        pause 0.3
        ease 0.7 yoffset 20
        repeat

image Emma_titjob_breasts_animation2:
    animation
    "Emma_titjob_breasts"

    subpixel True
    block:
        ease 0.6 yoffset -30
        ease 0.3 yoffset 10
        pause 0.1
        repeat

image Emma_titjob_breasts_animation3:
    animation
    "Emma_titjob_breasts"

    subpixel True
    block:
        ease 1.8 yoffset -30
        pause 0.3
        ease 1.0 yoffset 20
        pause 0.5
        repeat

image Emma_titjob_breasts_animation5:
    animation
    "Emma_titjob_breasts"

    subpixel True
    block:
        ease 1.5 yoffset 0
        pause 0.3
        ease 0.9 yoffset 20
        pause 0.5
        repeat

layeredimage Emma_sprite titjob:
    always:
        "Emma_titjob_hair_back_animation[EmmaX.primary_Action.speed]" pos (0.0, -0.24) zoom 0.56

    always:
        "Emma_titjob_body_animation[EmmaX.primary_Action.speed]"

    always:
        "Emma_titjob_head_animation[EmmaX.primary_Action.speed]" pos (0.0, -0.24) zoom 0.56

    always:
        "Zero_cock_Emma"

    always:
        "Emma_titjob_breasts_animation[EmmaX.primary_Action.speed]" pos (0.0, -0.04) zoom 0.9

    anchor (0.5, 0.0) offset (440, 1050) zoom 1.72

image Emma_blowjob_blinking:
    "images/Emma_blowjob/Emma_blowjob_eyes_[EmmaX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Emma_blowjob/Emma_blowjob_eyes_squint.png"
    0.05
    "images/Emma_blowjob/Emma_blowjob_eyes_closed.png"
    0.15
    "images/Emma_blowjob/Emma_blowjob_eyes_squint.png"
    0.05
    repeat
