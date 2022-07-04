image Laura_blinking:
    "images/Laura_standing/Laura_standing_eyes_[LauraX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Laura_standing/Laura_standing_eyes_squint.png"
    0.05
    "images/Laura_standing/Laura_standing_eyes_closed.png"
    0.15
    "images/Laura_standing/Laura_standing_eyes_squint.png"
    0.05
    repeat

layeredimage Laura_grool_dripping_animation:
    always:
        "grool_dripping_animation" pos (0.155, 1.1)

    if LauraX.grool > 1 and not LauraX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.155, 1.1)

    if LauraX.grool > 1 and not LauraX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.155, 1.1)

    if LauraX.grool > 1 and not LauraX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.155, 1.1)

layeredimage Laura_grool_animations:
    if not LauraX.grool:
        Null()
    elif LauraX.Clothes["pants"].state:
        AlphaMask("Laura_grool_dripping_animation", "images/Laura_standing/Laura_standing_grool_mask_pants.png")
    elif LauraX.Clothes["underwear"].state:
        AlphaMask("Laura_grool_dripping_animation", "images/Laura_standing/Laura_standing_grool_mask_underwear.png")
    elif not LauraX.Outfit.pussy_covered:
        AlphaMask("Laura_grool_dripping_animation", "images/Laura_standing/Laura_standing_grool_mask.png")

layeredimage Laura_spunk_dripping_animation:
    always:
        "spunk_dripping_animation" pos (0.155, 1.1)

    if not LauraX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.155, 1.1)

    if not LauraX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.155, 1.1)

    if not LauraX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.155, 1.1)

layeredimage Laura_spunk_animations:
    if not LauraX.spunk["pussy"] and not LauraX.spunk["anus"]:
        Null()
    elif LauraX.Clothes["pants"].state:
        AlphaMask("Laura_spunk_dripping_animation", "images/Laura_standing/Laura_standing_grool_mask_pants.png")
    elif LauraX.Clothes["underwear"].state:
        AlphaMask("Laura_spunk_dripping_animation", "images/Laura_standing/Laura_standing_grool_mask_underwear.png")
    elif not LauraX.Outfit.pussy_covered:
        AlphaMask("Laura_spunk_dripping_animation", "images/Laura_standing/Laura_standing_grool_mask.png")

layeredimage Laura_standing_fondling_animations:
    if LauraX.primary_Action.Target != LauraX:
        Null()
    elif LauraX.primary_Action.type == "fondle_breasts":
        "Girl_fondle_breast_right_animation" pos (0.1, 0.69)
    elif LauraX.primary_Action.type == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.14, 1.09)
    elif LauraX.primary_Action.type in "finger_pussy":
        "Girl_finger_pussy_animation" pos (0.145, 1.14)

    if LauraX.secondary_Action.Target != LauraX:
        Null()
    elif LauraX.secondary_Action.type == "fondle_breasts":
        "Girl_fondle_breast_left_animation" pos (0.235, 0.695)
    elif LauraX.secondary_Action.type == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.14, 1.09)
    elif LauraX.secondary_Action.type in "finger_pussy":
        "Girl_finger_pussy_animation" pos (0.145, 1.14)

    if Player.primary_Action.Target != LauraX:
        Null()
    elif Player.primary_Action.type == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.09, 1.32)
    elif Player.primary_Action.type == "fondle_breasts":
        "Zero_fondle_breasts_left_animation" pos (0.185, 0.712)
    elif Player.primary_Action.type == "suck_breasts":
        "Zero_suck_breasts_left_animation" pos (0.2152, 0.64)
    elif Player.primary_Action.type == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.15, 1.07)
    elif Player.primary_Action.type == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.22, 1.3)
    elif Player.primary_Action.type == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.15, 1.16)

    if Player.secondary_Action.Target != LauraX:
        Null()
    elif Player.secondary_Action.type == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.09, 1.32)
    elif Player.secondary_Action.type == "fondle_breasts":
        "Zero_fondle_breasts_right_animation" pos (0.14, 0.705)
    elif Player.secondary_Action.type == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.085, 0.635)
    elif Player.secondary_Action.type == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.15, 1.07)
    elif Player.secondary_Action.type == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.22, 1.3)
    elif Player.secondary_Action.type == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.15, 1.16)

image Laura_handjob_under_hand_animation0:
    "Laura_handjob_under"

image Laura_handjob_under_hand_animation1:
    animation
    "Laura_handjob_under"

    subpixel True
    rotate -5
    block:
        ease 0.75 yoffset 40 rotate 1
        pause 0.25
        ease 1.0 yoffset -10 rotate -5
        pause 0.1
        repeat

image Laura_handjob_under_hand_animation2:
    animation
    "Laura_handjob_under"

    subpixel True
    rotate -3
    block:
        ease 0.4 yoffset 30 rotate 0
        pause 0.1
        ease 0.4 yoffset -10 rotate -3
        pause 0.1
        repeat

image Laura_handjob_over_hand_animation0:
    "Laura_handjob_over"

image Laura_handjob_over_hand_animation1:
    animation
    "Laura_handjob_over"

    subpixel True
    rotate -5
    block:
        ease 0.75 yoffset 40 rotate 1
        pause 0.25
        ease 1.0 yoffset -10 rotate -5
        pause 0.1
        repeat

image Laura_handjob_over_hand_animation2:
    animation
    "Laura_handjob_over"

    subpixel True
    rotate -3
    block:
        ease 0.4 yoffset 30 rotate 0
        pause 0.1
        ease 0.4 yoffset -10 rotate -3
        pause 0.1
        repeat

layeredimage Laura_sprite handjob:
    always:
        "Laura_sprite standing"

    always:
        "Laura_handjob_under_hand_animation[LauraX.primary_Action.speed]" pos (0.035, 0.455) zoom 0.28

    always:
        "Zero_cock_Laura"

    always:
        "Laura_handjob_over_hand_animation[LauraX.primary_Action.speed]" pos (0.035, 0.455) zoom 0.28

    anchor (0.5, 0.0) offset (220, -220) zoom 2.5

image Laura_titjob_hair_back_animation0:
    animation
    "Laura_hair_back"

    subpixel True
    parallel:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat
    parallel:
        pause 0.1
        ease 2 rotate -5
        pause 0.1
        ease 2 rotate 0
        repeat

image Laura_titjob_hair_back_animation1:
    animation
    "Laura_hair_back"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset 0
        pause 0.2
        ease 2 yoffset 150
        pause 0.5
        repeat
    parallel:
        ease 2 rotate 0
        pause 0.2
        ease 2 rotate -5
        pause 0.5
        repeat

image Laura_titjob_hair_back_animation2:
    animation
    "Laura_hair_back"

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

image Laura_titjob_hair_back_animation3:
    animation
    "Laura_hair_back"

    subpixel True
    parallel:
        ease 2 yoffset 80
        pause 0.1
        ease 2 yoffset 100
        pause 0.1
        repeat
    parallel:
        pause 0.1
        ease 2 rotate -5
        pause 0.1
        ease 2 rotate 0
        repeat

image Laura_titjob_hair_back_animation5:
    animation
    "Laura_hair_back"

    subpixel True
    parallel:
        ease 2 yoffset 20
        pause 0.1
        ease 2 yoffset 40
        pause 0.1
        repeat

image Laura_titjob_body_animation0:
    animation
    "Laura_titjob_body"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Laura_titjob_body_animation1:
    animation
    "Laura_titjob_body"

    subpixel True
    block:
        ease 2 yoffset 0
        pause 0.2
        ease 2 yoffset 150
        pause 0.5
        repeat

image Laura_titjob_body_animation2:
    animation
    "Laura_titjob_body"

    subpixel True
    block:
        ease 1 yoffset -20
        pause 0.1
        ease 0.5 yoffset 80
        repeat

image Laura_titjob_body_animation3:
    animation
    "Laura_titjob_body"

    subpixel True
    block:
        ease 2 yoffset 60
        pause 0.1
        ease 2 yoffset 100
        pause 0.1
        repeat

image Laura_titjob_body_animation5:
    animation
    "Laura_titjob_body"

    subpixel True
    block:
        ease 2 yoffset 20
        pause 0.1
        ease 2 yoffset 40
        pause 0.1
        repeat

image Laura_titjob_right_arm_back_animation0:
    animation
    "Laura_titjob_right_arm_back"

    subpixel True
    block:
        ease 2 yoffset -5
        pause 0.1
        ease 2 yoffset -15
        pause 0.1
        repeat

image Laura_titjob_right_arm_back_animation1:
    animation
    "Laura_titjob_right_arm_back"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.4
        ease 1.8 yoffset 150
        pause 0.5
        repeat

image Laura_titjob_right_arm_back_animation2:
    animation
    "Laura_titjob_right_arm_back"

    subpixel True
    block:
        ease 1 yoffset 0
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Laura_titjob_right_arm_back_animation3:
    animation
    "Laura_titjob_right_arm_back"

    subpixel True
    block:
        ease 2 yoffset 70
        pause 0.1
        ease 2 yoffset 100
        pause 0.1
        repeat

image Laura_titjob_right_arm_back_animation5:
    animation
    "Laura_titjob_right_arm_back"

    subpixel True
    block:
        ease 2 yoffset 10
        pause 0.1
        ease 2 yoffset 40
        pause 0.1
        repeat

image Laura_titjob_right_breast_animation0:
    animation
    "Laura_titjob_right_breast"

    subpixel True
    block:
        pause 0.1
        ease 2 yoffset -5
        pause 0.1
        ease 2 yoffset -15
        repeat

image Laura_titjob_right_breast_animation1:
    animation
    "Laura_titjob_right_breast"

    subpixel True
    block:
        pause 0.1
        ease 1.9 yoffset -20
        pause 0.4
        ease 1.8 yoffset 150
        ease 0.5 yoffset 140
        repeat

image Laura_titjob_right_breast_animation2:
    animation
    "Laura_titjob_right_breast"

    subpixel True
    block:
        ease 0.3 yoffset 50
        ease 0.7 yoffset 0
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Laura_titjob_right_breast_animation3:
    animation
    "Laura_titjob_right_breast"

    subpixel True
    block:
        pause 0.2
        ease 1.9 yoffset 70
        pause 0.2
        ease 1.9 yoffset 105
        repeat

image Laura_titjob_right_breast_animation5:
    animation
    "Laura_titjob_right_breast"

    subpixel True
    block:
        pause 0.2
        ease 1.9 yoffset 10
        pause 0.2
        ease 1.9 yoffset 45
        repeat

image Laura_titjob_right_arm_animation0:
    animation
    "Laura_titjob_right_arm"

    subpixel True
    block:
        ease 2 yoffset 10
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Laura_titjob_right_arm_animation1:
    animation
    "Laura_titjob_right_arm"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.4
        ease 1.8 yoffset 150
        pause 0.5
        repeat

image Laura_titjob_right_arm_animation2:
    animation
    "Laura_titjob_right_arm"

    subpixel True
    block:
        ease 1 yoffset 0
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Laura_titjob_right_arm_animation3:
    animation
    "Laura_titjob_right_arm"

    subpixel True
    block:
        ease 2 yoffset 70
        pause 0.1
        ease 2 yoffset 100
        pause 0.1
        repeat

image Laura_titjob_right_arm_animation5:
    animation
    "Laura_titjob_right_arm"

    subpixel True
    block:
        ease 2 yoffset 10
        pause 0.1
        ease 2 yoffset 40
        pause 0.1
        repeat

image Laura_titjob_head_animation0:
    animation
    "Laura_head"

    subpixel True
    parallel:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat
    parallel:
        pause 0.1
        ease 2 rotate -5
        pause 0.1
        ease 2 rotate 0
        repeat

image Laura_titjob_head_animation1:
    animation
    "Laura_head"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset 0
        pause 0.2
        ease 2 yoffset 150
        pause 0.5
        repeat
    parallel:
        ease 2 rotate 0
        pause 0.2
        ease 2 rotate -5
        pause 0.5
        repeat

image Laura_titjob_head_animation2:
    animation
    "Laura_head"

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

image Laura_titjob_head_animation3:
    animation
    "Laura_head"

    subpixel True
    parallel:
        ease 2 yoffset 80
        pause 0.1
        ease 2 yoffset 100
        pause 0.1
        repeat
    parallel:
        pause 0.1
        ease 2 rotate -5
        pause 0.1
        ease 2 rotate 0
        repeat

image Laura_titjob_head_animation5:
    animation
    "Laura_head"

    subpixel True
    block:
        ease 2 yoffset 20
        pause 0.1
        ease 2 yoffset 40
        pause 0.1
        repeat

image Laura_titjob_left_breast_animation0:
    animation
    "Laura_titjob_left_breast"

    subpixel True
    block:
        pause 0.1
        ease 2 yoffset -40
        pause 0.1
        ease 2 yoffset 0
        repeat

image Laura_titjob_left_breast_animation1:
    animation
    "Laura_titjob_left_breast"

    subpixel True
    block:
        pause 0.1
        ease 1.9 yoffset -20
        pause 0.4
        ease 1.8 yoffset 150
        ease 0.5 yoffset 140
        repeat

image Laura_titjob_left_breast_animation2:
    animation
    "Laura_titjob_left_breast"

    subpixel True
    block:
        ease 0.3 yoffset 50
        ease 0.7 yoffset 0
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Laura_titjob_left_breast_animation3:
    animation
    "Laura_titjob_left_breast"

    subpixel True
    block:
        pause 0.2
        ease 1.9 yoffset 70
        pause 0.2
        ease 1.9 yoffset 105
        repeat

image Laura_titjob_left_breast_animation5:
    animation
    "Laura_titjob_left_breast"

    subpixel True
    rotate -10
    block:
        pause 0.2
        ease 1.9 yoffset 10
        pause 0.2
        ease 1.9 yoffset 45
        repeat

image Laura_titjob_left_arm_animation0:
    animation
    "Laura_titjob_left_arm"

    subpixel True
    block:
        ease 2 yoffset -40
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Laura_titjob_left_arm_animation1:
    animation
    "Laura_titjob_left_arm"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.4
        ease 1.8 yoffset 150
        pause 0.5
        repeat

image Laura_titjob_left_arm_animation2:
    animation
    "Laura_titjob_left_arm"

    subpixel True
    block:
        ease 1 yoffset -20
        pause 0.1
        ease 0.5 yoffset 80
        repeat

image Laura_titjob_left_arm_animation3:
    animation
    "Laura_titjob_left_arm"

    subpixel True
    block:
        ease 2 yoffset 60
        pause 0.1
        ease 2 yoffset 90
        pause 0.1
        repeat

image Laura_titjob_left_arm_animation5:
    animation
    "Laura_titjob_left_arm"

    subpixel True
    rotate -10
    block:
        ease 2 yoffset 0
        pause 0.1
        ease 2 yoffset 30
        pause 0.1
        repeat

image Laura_titjob_hair_mid_animation0:
    animation
    "Laura_titjob_hair_mid"

    subpixel True
    parallel:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat
    parallel:
        pause 0.1
        ease 2 rotate -5
        pause 0.1
        ease 2 rotate 0
        repeat

image Laura_titjob_hair_mid_animation1:
    animation
    "Laura_titjob_hair_mid"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset -20
        pause 0.4
        ease 1.8 yoffset 160
        pause 0.5
        repeat
    parallel:
        ease 2 rotate 0
        pause 0.2
        ease 2 rotate -5
        pause 0.5
        repeat

image Laura_titjob_hair_mid_animation2:
    animation
    "Laura_titjob_hair_mid"

    subpixel True
    rotate -5
    parallel:
        ease 1 yoffset -40
        pause 0.2
        ease 0.4 yoffset 90
        repeat
    parallel:
        ease 1 rotate 0
        pause 0.2
        ease 0.4 rotate -5
        repeat

image Laura_titjob_hair_mid_animation3:
    animation
    "Laura_titjob_hair_mid"

    subpixel True
    parallel:
        ease 2 yoffset 85
        pause 0.1
        ease 2 yoffset 100
        pause 0.1
        repeat
    parallel:
        pause 0.1
        ease 2 rotate -5
        pause 0.1
        ease 2 rotate 0
        repeat

image Laura_titjob_hair_mid_animation5:
    animation
    "Laura_titjob_hair_mid"

    subpixel True
    block:
        ease 2 yoffset 25
        pause 0.1
        ease 2 yoffset 40
        pause 0.1
        repeat

image Laura_titjob_hair_animation0:
    animation
    "Laura_titjob_hair"

    subpixel True
    parallel:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat
    parallel:
        pause 0.1
        ease 2 rotate -5
        pause 0.1
        ease 2 rotate 0
        repeat

image Laura_titjob_hair_animation1:
    animation
    "Laura_titjob_hair"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset 0
        pause 0.2
        ease 2 yoffset 150
        pause 0.5
        repeat
    parallel:
        ease 2 rotate 0
        pause 0.2
        ease 2 rotate -5
        pause 0.5
        repeat

image Laura_titjob_hair_animation2:
    animation
    "Laura_titjob_hair"

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

image Laura_titjob_hair_animation3:
    animation
    "Laura_titjob_hair"

    subpixel True
    rotate 0
    parallel:
        ease 2 yoffset 80
        pause 0.1
        ease 2 yoffset 100
        pause 0.1
        repeat
    parallel:
        pause 0.1
        ease 2 rotate -5
        pause 0.1
        ease 2 rotate 0
        repeat

image Laura_titjob_hair_animation5:
    animation
    "Laura_titjob_hair"

    subpixel True
    block:
        ease 2 yoffset 20
        pause 0.1
        ease 2 yoffset 40
        pause 0.1
        repeat

layeredimage Laura_sprite titjob:
    always:
        "Laura_titjob_hair_back_animation[LauraX.primary_Action.speed]" pos (-0.035, -0.26) zoom 0.55

    always:
        "Laura_titjob_body_animation[LauraX.primary_Action.speed]"

    always:
        "Laura_titjob_right_arm_back_animation[LauraX.primary_Action.speed]" pos (0.0, 0.01)

    always:
        "Laura_titjob_right_breast_animation[LauraX.primary_Action.speed]" pos (0.0, 0.01)

    always:
        "Laura_titjob_right_arm_animation[LauraX.primary_Action.speed]" pos (0.0, 0.01)

    always:
        "Laura_titjob_head_animation[LauraX.primary_Action.speed]" pos (-0.035, -0.26) zoom 0.55

    always:
        "Zero_cock_Laura"

    always:
        "Laura_titjob_left_breast_animation[LauraX.primary_Action.speed]"

    always:
        "Laura_titjob_left_arm_animation[LauraX.primary_Action.speed]" pos (0.0, 0.01)

    always:
        "Laura_titjob_hair_mid_animation[LauraX.primary_Action.speed]" pos (-0.035, -0.26) zoom 0.55

    always:
        "Laura_titjob_hair_animation[LauraX.primary_Action.speed]" pos (-0.035, -0.26) zoom 0.55

    anchor (0.5, 0.0) offset (400, 900) zoom 1.05
