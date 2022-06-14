image Zero_fondle_thigh_animation:
    animation
    "Zero_hand"

    subpixel True
    alpha 0.5 zoom 0.7
    rotate 100
    block:
        parallel:
            pause 0.5
            ease 1 yoffset 50
            ease 1 yoffset 0
            repeat
        parallel:
            pause 0.5
            ease 0.5 xoffset 3
            ease 0.5 xoffset 0
            ease 0.5 xoffset 3
            ease 0.5 xoffset 0
            repeat

image Zero_fondle_breasts_right_animation:
    animation
    "Zero_hand"

    subpixel True
    alpha 0.5 zoom (-0.7, 0.7)
    rotate -60
    block:
        ease 1 rotate -30
        ease 1 rotate -60
        repeat

image Zero_fondle_breasts_left_animation:
    animation
    "Zero_hand"

    subpixel True
    alpha 0.5 zoom 0.7
    rotate 90
    block:
        ease 1 rotate 60
        ease 1 rotate 90
        repeat

image Zero_suck_breasts_right_animation:
    animation
    "Zero_tongue"

    subpixel True
    alpha 0.5 zoom (-0.5, 0.5)
    rotate 30
    block:
        ease 0.5 rotate -45 offset (10, -30)
        pause 0.5
        ease 1.5 rotate 30 offset (0, 0)
        repeat

image Zero_suck_breasts_left_animation:
    animation
    "Zero_tongue"

    subpixel True
    alpha 0.5 zoom (-0.5, 0.5)
    rotate 30
    block:
        ease 0.5 rotate -45 offset (40, -30)
        pause 0.5
        ease 1.5 rotate 30 offset (0, 0)
        repeat

image Zero_fondle_pussy_animation:
    animation
    "Zero_hand"

    subpixel True
    alpha 0.5 zoom 0.7
    rotate 170
    block:
        choice:
            ease .5 rotate 190 offset (0, -15)
            ease .75 rotate 170 offset (0, 0)
        choice:
            ease .5 rotate 190 offset (0, -15)
            pause .25
            ease 1 rotate 170 offset (0, 0)
        repeat

image Zero_finger_pussy_animation:
    animation
    "Zero_finger"

    subpixel True
    alpha 0.5 zoom 0.7
    rotate 40
    block:
        choice:
            ease 1 rotate 40 offset (10, -35)
            pause 0.5
            ease 1 rotate 50 offset (0, 0)
        choice:
            ease 0.5 rotate 40 offset (10, -35)
            pause 0.5
            ease 1.75 rotate 50 offset (0, 0)
        choice:
            ease 2 rotate 40 offset (10, -35)
            pause 0.5
            ease 1 rotate 50 offset (0, 0)
        choice:
            ease 0.25 rotate 40 offset (10, -35)
            ease 0.25 rotate 50 offset (0, 0)
            ease 0.25 rotate 40 offset (10, -35)
            ease 0.25 rotate 50 offset (0, 0)
        repeat

image Zero_eat_pussy_animation:
    animation
    "Zero_tongue"

    subpixel True
    alpha 0.5 zoom (-0.5, 0.5)
    rotate 10
    block:
        easeout 0.5 rotate -50 offset (-20, -20)
        linear 0.5 rotate -60 offset (-30, -10)
        easein 1 rotate 10 offset (0, 0)
        repeat

image Zero_doggy_fondle_breast_animation:
    animation
    "Zero_hand_under"

    subpixel True
    block:
        ease 1 rotate 10
        ease 1 rotate 0
        repeat

image Rogue_sex_finger_pussy_animation:
    animation
    "Zero_sex_finger"

    subpixel True
    zoom 1.2
    block:
        ease 0.2 yoffset -40
        pause 0.2
        ease 0.6 yoffset 0
        repeat

image Rogue_sex_finger_ass_animation:
    animation
    "Zero_sex_finger"

    subpixel True
    zoom 1.2
    block:
        ease 0.4 yoffset -50
        pause 0.4
        ease 1.2 yoffset 0
        repeat

image Rogue_doggy_finger_pussy_animation:
    animation
    "Zero_sex_finger"

    subpixel True
    block:
        ease 1 offset (-3, -45)
        pause 1
        ease 3 offset (0, 0)
        repeat

image Rogue_doggy_finger_ass_animation:
    animation
    "Zero_sex_finger"

    subpixel True
    block:
        ease 0.5 yoffset -20
        pause 0.25
        ease 1.75 yoffset 0
        repeat

layeredimage Zero_finger_Rogue:
    if renpy.showing("Rogue_sprite sex") and "finger_pussy" in [Player.primary_action, Player.secondary_action]:
        "Rogue_sex_finger_pussy_animation" pos (0.292, 0.64)

    if renpy.showing("Rogue_sprite sex") and "finger_ass" in [Player.primary_action, Player.secondary_action]:
        "Rogue_sex_finger_ass_animation" pos (0.2923, 0.7)

    if renpy.showing("Rogue_sprite doggy") and "finger_pussy" in [Player.primary_action, Player.secondary_action]:
        "Rogue_doggy_finger_pussy_animation" pos (0.112, 0.625)

    if renpy.showing("Rogue_sprite doggy") and "finger_ass" in [Player.primary_action, Player.secondary_action]:
        "Rogue_doggy_finger_ass_animation" pos (0.112, 0.57)

image Rogue_doggy_anus_fingering_mask_animation:
    animation
    "images/Rogue_doggy/Rogue_doggy_anus_mask.png"

    subpixel True
    anchor (0.52, 0.69) zoom 0.6
    block:
        ease 0.5 zoom 0.75
        pause 0.5
        ease 1.5 zoom 0.6
        repeat

layeredimage Zero_finger_Rogue_mask:
    if not renpy.showing("Rogue_sprite doggy"):
        Null()
    elif "finger_pussy" in [Player.primary_action, Player.secondary_action]:
        "Rogue_doggy_pussy_mask_animation1" offset (217, 514)
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        "Rogue_doggy_anus_fingering_mask_animation" offset (217, 514)

image dildo_pussy_animation:
    animation
    "dildo"

    subpixel True
    block:
        ease 1 yoffset -60
        pause 1
        ease 3 yoffset 0
        repeat

image dildo_ass_animation:
    animation
    "dildo"

    subpixel True
    block:
        ease 1 yoffset -60
        pause 1
        ease 3 yoffset 0
        repeat

image doggy_dildo_pussy_animation:
    animation
    "dildo"

    subpixel True
    block:
        ease 1 xoffset -3 yoffset -45
        pause 1
        ease 3 xoffset 0 yoffset 0
        repeat

image doggy_dildo_ass_animation:
    animation
    "dildo"

    subpixel True
    block:
        ease 0.5 yoffset -65
        pause 0.25
        ease 1.75 yoffset 5
        repeat

layeredimage dildo_Rogue:
    if renpy.showing("Rogue_sprite sex") and "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        "dildo_pussy_animation" pos (0.2923, 0.595) zoom 1.22

    if renpy.showing("Rogue_sprite sex") and "dildo_ass" in [Player.primary_action, Player.secondary_action]:
        "dildo_ass_animation" pos (0.2925, 0.64)

    if renpy.showing("Rogue_sprite doggy") and "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        "doggy_dildo_pussy_animation" pos (0.1117, 0.62)

    if renpy.showing("Rogue_sprite doggy") and "dildo_ass" in [Player.primary_action, Player.secondary_action]:
        "doggy_dildo_ass_animation" pos (0.112, 0.58)

layeredimage dildo_Rogue_mask:
    if not renpy.showing("Rogue_sprite doggy"):
        Null()
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        "Rogue_doggy_pussy_mask_animation1" offset (217, 514)
    elif "dildo_ass" in [Player.primary_action, Player.secondary_action]:
        "Rogue_doggy_anus_mask_animation1" offset (217, 514)

image Zero_handjob_cock_animation0:
    "Zero_handjob_cock"

image Zero_handjob_cock_animation1:
    animation
    "Zero_handjob_cock"

    subpixel True
    block:
        ease 0.75 rotate -2
        pause 0.25
        ease 1.0 rotate 0
        pause 0.1
        repeat

image Zero_handjob_cock_animation2:
    animation
    "Zero_handjob_cock"

    subpixel True
    block:
        ease 0.4 rotate -3
        ease 0.5 rotate 0
        pause 0.1
        repeat

image Rogue_titjob_cock_animation0:
    "Zero_handjob_cock"

image Rogue_titjob_cock_animation1:
    animation
    "Zero_handjob_cock"

    subpixel True
    block:
        ease 1.2 yoffset -60
        easein 1.3 yoffset -20
        repeat

image Rogue_titjob_cock_animation2:
    animation
    "Zero_handjob_cock"

    subpixel True
    block:
        ease 0.35 yoffset -70
        ease 0.4 yoffset -30
        repeat

image Rogue_blowjob_cock_animation0:
    "Zero_blowjob_cock"

    rotate -10

image Rogue_blowjob_cock_animation1:
    animation
    "Zero_blowjob_cock"

    subpixel True
    ease 0.5 rotate 0
    block:
        ease 2 rotate -5
        pause 0.5
        ease 2.5 rotate 0
        repeat

image Rogue_blowjob_cock_animation2:
    "Zero_blowjob_cock"

    offset (1, 0) rotate -1

image Rogue_blowjob_cock_animation3:
    "Zero_blowjob_cock"

image Rogue_blowjob_cock_animation4:
    "Zero_blowjob_cock"

image Rogue_sex_cock_animation0:
    "Zero_doggy_cock_in"

image Rogue_sex_cock_animation1:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (0, -5)
    block:
        ease 1 yoffset -20
        pause 1
        ease 3 yoffset -5
        repeat

image Rogue_sex_cock_animation2:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (0.75, -40)
    block:
        ease 1 offset (1, -110)
        pause 1
        ease 3 offset (0.75, -40)
        repeat

image Rogue_sex_cock_animation3:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (0.75, -40)
    block:
        ease 0.25 offset (1, -110)
        pause 0.25
        ease 1.5 offset (0.75, -40)
        repeat

image Rogue_sex_cock_anal_animation0:
    "Zero_doggy_cock_in"

image Rogue_sex_cock_anal_animation1:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    block:
        ease 1 yoffset -30
        pause 1
        ease 3 yoffset 0
        repeat

image Rogue_sex_cock_anal_animation2:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (0, -40)
    block:
        ease 1 yoffset -120
        pause 1
        ease 3 yoffset -40
        repeat

image Rogue_sex_cock_anal_animation3:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (0, -40)
    block:
        ease 0.25 yoffset -120
        pause 0.25
        ease 1.5 yoffset -40
        repeat

image Rogue_sex_cock_footjob_animation0:
    "Zero_blowjob_cock"

image Rogue_sex_cock_footjob_animation1:
    animation
    "Zero_blowjob_cock"

    subpixel True
    block:
        pause 0.5
        easein 0.75 yoffset 65
        ease 0.25 yoffset 60
        pause 1
        ease 2.50 yoffset -25
        repeat

image Rogue_sex_cock_footjob_animation2:
    animation
    "Zero_blowjob_cock"

    subpixel True
    block:
        pause 0.2
        easein 0.4 yoffset 65
        ease 0.2 yoffset 60
        pause 0.2
        ease 1.0 yoffset -25
        repeat

image Rogue_sex_cock_hotdog_animation0:
    "Zero_doggy_cock_in"

image Rogue_sex_cock_hotdog_animation1:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (0, -70)
    block:
        ease 1 yoffset -10
        pause 0.5
        ease 1.5 yoffset -70
        repeat

image Rogue_sex_cock_hotdog_animation2:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (0, -60)
    block:
        ease 0.5 yoffset -120
        pause 0.5
        ease 1 yoffset -60
        repeat

image Rogue_sex_cock_hotdog_animation3:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (0, -60)
    block:
        ease 0.5 yoffset -120
        pause 0.5
        ease 1 yoffset -60
        repeat

image Rogue_doggy_cock_animation0:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    block:
        ease 1 yoffset -5
        pause 1
        ease 3 yoffset 0
        repeat

image Rogue_doggy_cock_animation1:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    block:
        ease 1 xoffset -3 yoffset -45
        pause 1
        ease 3 xoffset 0 yoffset -5
        repeat

image Rogue_doggy_cock_animation2:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (-3, -45)
    block:
        ease 0.5 offset (-3, -105)
        pause 0.25
        ease 1.75 offset (-3, -45)
        repeat

image Rogue_doggy_cock_animation3:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (-3, -45)
    block:
        ease 0.2 offset (-3, -105)
        pause 0.1
        ease 0.6 offset (-3, -45)
        repeat

image Rogue_doggy_cock_anal_animation0:
    "Zero_doggy_cock_in"

image Rogue_doggy_cock_anal_animation1:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    block:
        ease 0.5 yoffset -75
        pause 0.25
        ease 1.75 yoffset -25
        repeat

image Rogue_doggy_cock_anal_animation2:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    yoffset -60
    block:
        ease 0.5 yoffset -130
        pause 0.25
        ease 1.75 yoffset -65
        repeat

image Rogue_doggy_cock_anal_animation3:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    yoffset -60
    block:
        ease 0.2 yoffset -130
        pause 0.1
        ease 0.6 yoffset -60
        repeat

image Rogue_doggy_cock_hotdog_animation0:
    "Zero_doggy_cock_out"

image Rogue_doggy_cock_hotdog_animation1:
    animation
    "Zero_doggy_cock_out"

    subpixel True
    block:
        ease 1 yoffset -60
        ease 1 yoffset 50
        repeat

image Rogue_doggy_cock_hotdog_animation2:
    animation
    "Zero_doggy_cock_out"

    subpixel True
    block:
        ease 1 yoffset -60
        ease 1 yoffset 50
        repeat

image Rogue_doggy_cock_hotdog_animation3:
    animation
    "Zero_doggy_cock_out"

    subpixel True
    block:
        ease 1 yoffset -60
        ease 1 yoffset 50
        repeat

image Rogue_doggy_cock_footjob_animation0:
    "Zero_doggy_cock_out"

image Rogue_doggy_cock_footjob_animation1:
    animation
    "Zero_doggy_cock_out"

    subpixel True
    block:
        pause 0.4
        ease 1.7 yoffset 20
        ease 0.9 yoffset 0
        repeat

image Rogue_doggy_cock_footjob_animation2:
    animation
    "Zero_doggy_cock_out"

    subpixel True
    block:
        pause 0.07
        ease 0.6 yoffset 20
        ease 0.28 yoffset 0
        repeat

layeredimage Zero_cock_Rogue:
    if renpy.showing("Rogue_sprite handjob"):
        "Zero_handjob_cock_animation[action_speed]" pos (-0.035, 0.455) zoom 0.28

    if renpy.showing("Rogue_sprite titjob"):
        "Rogue_titjob_cock_animation[action_speed]" pos (-0.007, 0.2) zoom 0.65

    if renpy.showing("Rogue_sprite blowjob"):
        "Rogue_blowjob_cock_animation[action_speed]" pos (0.02272, 0.462) zoom 0.2755

    if not renpy.showing("Rogue_sprite sex"):
        Null()
    elif Player.cock_position == "in":
        "Rogue_sex_cock_animation[action_speed]" pos (0.29175, 0.635) zoom 1.25
    elif Player.cock_position == "anal":
        "Rogue_sex_cock_anal_animation[action_speed]" pos (0.293, 0.7) zoom 1.18
    elif Player.cock_position == "out":
        "Rogue_sex_cock_hotdog_animation[action_speed]" pos (0.29175, 0.65) zoom 1.18
    elif Player.cock_position == "footjob":
        "Rogue_sex_cock_footjob_animation[action_speed]" pos (0.28, 0.53) alpha 0.8 zoom 0.6

    if not renpy.showing("Rogue_sprite doggy"):
        Null()
    elif Player.cock_position == "in":
        "Rogue_doggy_cock_animation[action_speed]" pos (0.112, 0.62)
    elif Player.cock_position == "anal":
        "Rogue_doggy_cock_anal_animation[action_speed]" pos (0.1125, 0.605)
    elif Player.cock_position == "out":
        "Rogue_doggy_cock_hotdog_animation[action_speed]" pos (0.1135, 0.52)

image Rogue_doggy_pussy_mask_animation0:
    animation
    "Rogue_doggy_pussy_mask"

    subpixel True
    xzoom 0.6
    block:
        ease 1 xzoom 0.65
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_pussy_mask_animation1:
    animation
    "Rogue_doggy_pussy_mask"

    subpixel True
    xzoom 0.6
    block:
        ease 1 xzoom 1
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_pussy_mask_animation2:
    "Rogue_doggy_pussy_mask"

image Rogue_doggy_pussy_mask_animation3:
    "Rogue_doggy_pussy_mask"

image Rogue_doggy_anus_mask_animation0:
    "Rogue_doggy_anus_mask"

image Rogue_doggy_anus_mask_animation1:
    animation
    "Rogue_doggy_anus_mask"

    subpixel True
    zoom 0.5
    block:
        ease 0.5 zoom 1
        pause 0.5
        ease 1.5 zoom 0.5
        repeat

image Rogue_doggy_anus_mask_animation2:
    "Rogue_doggy_anus_mask"

    zoom 0.9

image Rogue_doggy_anus_mask_animation3:
    "Rogue_doggy_anus_mask"

    zoom 0.9

layeredimage Zero_cock_Rogue_mask:
    if not renpy.showing("Rogue_sprite doggy"):
        Null()
    elif Player.cock_position == "in":
        "Rogue_doggy_pussy_mask_animation[action_speed]" offset (217, 514)
    elif Player.cock_position == "anal":
        "Rogue_doggy_anus_mask_animation[action_speed]" offset (217, 514)

layeredimage Zero_cock_Kitty:
    if renpy.showing("Kitty_sprite handjob"):
        "Zero_handjob_cock_animation[action_speed]" pos (-0.01, 0.455) zoom 0.28

    if renpy.showing("Kitty_sprite titjob"):
        "Zero_blowjob_cock" pos (0.05, 0.3) zoom 0.7

layeredimage Zero_cock_Kitty_mask:
    if renpy.showing("Kitty_sprite titjob"):
        "Kitty_titjob_mask_animation[action_speed]" offset (100, 100)

image Emma_titjob_cock_animation0:
    animation
    "Zero_blowjob_cock"

    subpixel True
    rotate -3
    parallel:
        pause 0.1
        ease 1.6 yoffset 20
        pause 0.1
        ease 1.4 yoffset 0
        repeat
    parallel:
        pause 0.1
        ease 1.6 rotate 4
        pause 0.1
        ease 1.4 rotate -3
        repeat

image Emma_titjob_cock_animation1:
    animation
    "Zero_blowjob_cock"

    subpixel True
    block:
        pause 0.2
        ease 1.4 yoffset -10
        pause 0.3
        ease 0.6 yoffset 0
        repeat

image Emma_titjob_cock_animation2:
    animation
    "Zero_blowjob_cock"

    subpixel True
    block:
        pause 0.05
        ease 0.65 yoffset -10
        ease 0.3 yoffset 0
        repeat

image Emma_titjob_cock_animation3:
    animation
    "Zero_blowjob_cock"

    subpixel True
    offset (0, -20)
    block:
        pause 0.2
        ease 1.6 yoffset -30
        pause 0.4
        ease 0.3 yoffset -20
        pause 0.5
        repeat

layeredimage Zero_cock_Emma:
    if renpy.showing("Emma_sprite handjob"):
        "Zero_handjob_cock_animation[action_speed]" pos (-0.035, 0.455) zoom 0.28

    if renpy.showing("Emma_sprite titjob"):
        "Emma_titjob_cock_animation[action_speed]" pos (0.0, 0.035) zoom 0.45

image Laura_titjob_cock_animation0:
    animation
    "Zero_blowjob_cock"

    subpixel True
    rotate -2
    block:
        ease 2.0 rotate -2
        pause 0.1
        ease 2.0 rotate 3
        pause 0.1
        repeat

image Laura_titjob_cock_animation1:
    animation
    "Zero_blowjob_cock"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset -30
        pause 0.4
        ease 1.8 yoffset -5
        pause 0.5
        repeat
    parallel:
        ease 2 rotate 0
        pause 0.2
        ease 2 rotate -5
        pause 0.5
        repeat

image Laura_titjob_cock_animation2:
    animation
    "Zero_blowjob_cock"

    subpixel True
    rotate -2
    parallel:
        ease 1 yoffset -30
        pause 0.2
        ease 0.4 yoffset 0
        repeat
    parallel:
        ease 1 rotate 0
        pause 0.1
        ease 0.5 rotate -2
        repeat

layeredimage Zero_cock_Laura:
    if renpy.showing("Laura_sprite handjob"):
        "Zero_handjob_cock_animation[action_speed]" pos (0.035, 0.455) zoom 0.28

    if renpy.showing("Laura_sprite titjob"):
        "Laura_titjob_cock_animation[action_speed]" pos (-0.08, 0.2) zoom 0.65

image Jean_titjob_cock_animation0:
    animation
    "Zero_blowjob_cock"

    subpixel True
    rotate -5
    block:
        ease 2 rotate -3
        pause 0.1
        ease 2 rotate -5
        pause 0.1
        repeat

image Jean_titjob_cock_animation1:
    animation
    "Zero_blowjob_cock"

    subpixel True
    rotate -6
    block:
        ease 2 yoffset 0
        pause 0.4
        ease 1.8 yoffset 25
        pause 0.5
        repeat

image Jean_titjob_cock_animation2:
    animation
    "Zero_blowjob_cock"

    subpixel True
    rotate -4
    parallel:
        ease 1 yoffset 0
        pause 0.2
        ease 0.4 yoffset 30
        repeat
    parallel:
        ease 1 rotate -2
        pause 0.1
        ease 0.5 rotate -4
        repeat

layeredimage Zero_cock_Jean:
    if renpy.showing("Jean_sprite handjob"):
        "Zero_handjob_cock_animation[action_speed]" pos (0.035, 0.455) zoom 0.28

    if renpy.showing("Jean_sprite titjob"):
        "Jean_titjob_cock_animation[action_speed]" pos (0.032, 0.35) zoom 0.65

layeredimage Zero_cock_Storm:
    if renpy.showing("Storm_sprite handjob"):
        "Zero_handjob_cock_animation[action_speed]" pos (0.08, 0.455) zoom 0.28

layeredimage Zero_cock_Jubes:
    if renpy.showing("Jubes_sprite handjob"):
        "Zero_handjob_cock_animation[action_speed]" pos (-0.035, 0.455) zoom 0.28







image Kitty_sex_cock_anal_animation0:
    "Zero_doggy_cock_in"

image Kitty_sex_cock_animation1:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (0, -5)
    block:
        ease 1 yoffset -20
        pause 1
        ease 3 yoffset -5
        repeat

image Kitty_sex_cock_animation2:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (0.75, -40)
    block:
        ease 1 offset (1, -110)
        pause 1
        ease 3 offset (0.75, -40)
        repeat

image Kitty_sex_cock_animation3:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (0.75, -40)
    block:
        ease 0.25 offset (1, -110)
        pause 0.25
        ease 1.5 offset (0.75, -40)
        repeat

layeredimage Kitty_sex_cock_animations:
    always:
        "Kitty_sex_cock_animation[action_speed]" pos (0.29175, 0.637) zoom 1.25

image Kitty_sex_cock_anal_animation0:
    "Zero_doggy_cock_in"

image Kitty_sex_cock_anal_animation1:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    block:
        ease 1 yoffset -30
        pause 1
        ease 3 yoffset 0
        repeat

image Kitty_sex_cock_anal_animation2:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (0, -40)
    block:
        ease 1 yoffset -120
        pause 1
        ease 3 yoffset -40
        repeat

image Kitty_sex_cock_anal_animation3:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (0, -40)
    block:
        ease 0.25 yoffset -120
        pause 0.25
        ease 1.5 yoffset -40
        repeat

layeredimage Kitty_sex_cock_anal_animations:
    always:
        "Kitty_sex_cock_anal_animation[action_speed]" pos (0.293, 0.71) zoom 1.25

image Kitty_sex_cock_footjob_animation0:
    "Zero_blowjob_cock"

image Kitty_sex_cock_footjob_animation1:
    animation
    "Zero_blowjob_cock"

    subpixel True
    block:
        pause 0.5
        easein 0.75 yoffset 65
        ease 0.25 yoffset 60
        pause 1
        ease 2.50 yoffset -25
        repeat

image Kitty_sex_cock_footjob_animation2:
    animation
    "Zero_blowjob_cock"

    subpixel True
    block:
        pause 0.2
        easein 0.4 yoffset 65
        ease 0.2 yoffset 60
        pause 0.2
        ease 1.0 yoffset -25
        repeat

image Kitty_sex_cock_hotdog_animation0:
    "Zero_doggy_cock_in"

image Kitty_sex_cock_hotdog_animation1:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (0, -70)
    block:
        ease 1 yoffset -10
        pause 0.5
        ease 1.5 yoffset -70
        repeat

image Kitty_sex_cock_hotdog_animation2:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (0, -60)
    block:
        ease 0.5 yoffset -120
        pause 0.5
        ease 1 yoffset -60
        repeat

image Kitty_sex_cock_hotdog_animation3:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (0, -60)
    block:
        ease 0.5 yoffset -120
        pause 0.5
        ease 1 yoffset -60
        repeat

image Kitty_sex_finger_pussy_animation:
    animation
    "Zero_sex_finger"

    subpixel True
    zoom 1.2
    block:
        ease 0.2 yoffset -40
        pause 0.2
        ease 0.6 yoffset 0
        repeat

layeredimage Kitty_sex_finger_pussy_animations:
    always:
        "Kitty_sex_finger_pussy_animation" pos (0.2918, 0.615) zoom 0.9

image Kitty_sex_finger_ass_animation:
    animation
    "Zero_sex_finger"

    subpixel True
    zoom 1.2
    block:
        ease 0.4 yoffset -40
        pause 0.4
        ease 1.2 yoffset 0
        repeat

layeredimage Kitty_sex_finger_ass_animations:
    always:
        "Kitty_sex_finger_ass_animation" pos (0.2923, 0.687) zoom 0.9

image Kitty_doggy_cock_animation0:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    block:
        ease 1 yoffset -5
        pause 1
        ease 3 yoffset 0
        repeat

image Kitty_doggy_cock_animation1:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    block:
        ease 1 xoffset -3 yoffset -45
        pause 1
        ease 3 xoffset 0 yoffset -5
        repeat

image Kitty_doggy_cock_animation2:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (-3, -45)
    block:
        ease 0.5 offset (-3, -105)
        pause 0.25
        ease 1.75 offset (-3, -45)
        repeat

image Kitty_doggy_cock_animation3:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (-3, -45)
    block:
        ease 0.2 offset (-3, -105)
        pause 0.1
        ease 0.6 offset (-3, -45)
        repeat

layeredimage Kitty_doggy_cock_animations:
    always:
        "Kitty_doggy_cock_animation[action_speed]" pos (0.112, 0.62)

image Kitty_doggy_cock_anal_animation0:
    "Zero_doggy_cock_in"

image Kitty_doggy_cock_anal_animation1:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    block:
        ease 0.5 yoffset -50
        pause 0.25
        ease 1.75 yoffset 0
        repeat

image Kitty_doggy_cock_anal_animation2:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (-2, -35)
    block:
        ease 0.5 offset (-2, -105)
        pause 0.25
        ease 1.75 offset (-2, -40)
        repeat

image Kitty_doggy_cock_anal_animation3:
    animation
    "Zero_doggy_cock_in"

    subpixel True
    offset (-2, -35)
    block:
        ease 0.2 offset (-2, -105)
        pause 0.1
        ease 0.6 offset (-2, -35)
        repeat

layeredimage Kitty_doggy_cock_anal_animations:
    always:
        "Kitty_doggy_cock_anal_animation[action_speed]" pos (0.1125, 0.58)

image Kitty_doggy_cock_hotdog_animation0:
    "Zero_doggy_cock_out"

image Kitty_doggy_cock_hotdog_animation1:
    animation
    "Zero_doggy_cock_out"

    subpixel True
    block:
        ease 1 yoffset -75
        ease 1 yoffset 15
        repeat

image Kitty_doggy_cock_hotdog_animation2:
    animation
    "Zero_doggy_cock_out"

    subpixel True
    block:
        ease 1 yoffset -75
        ease 1 yoffset 15
        repeat

image Kitty_doggy_cock_hotdog_animation3:
    animation
    "Zero_doggy_cock_out"

    subpixel True
    block:
        ease 1 yoffset -75
        ease 1 yoffset 15
        repeat

layeredimage Kitty_doggy_cock_hotdog_animations:
    always:
        "Kitty_doggy_cock_hotdog_animation[action_speed]" pos (0.1135, 0.52)

image Kitty_doggy_cock_footjob_animation0:
    "Zero_doggy_cock_out"

image Kitty_doggy_cock_footjob_animation1:
    animation
    "Zero_doggy_cock_out"

    subpixel True
    block:
        pause 0.4
        ease 1.7 yoffset 20
        ease 0.9 yoffset 0
        repeat

image Kitty_doggy_cock_footjob_animation2:
    animation
    "Zero_doggy_cock_out"

    subpixel True
    block:
        pause 0.07
        ease 0.6 yoffset 20
        ease 0.28 yoffset 0
        repeat

image Kitty_doggy_finger_pussy_animation:
    animation
    "Zero_sex_finger"

    subpixel True
    block:
        ease 1 offset (-3, -45)
        pause 1
        ease 3 offset (0, 0)
        repeat

layeredimage Kitty_doggy_finger_pussy_animations:
    always:
        "Kitty_doggy_finger_pussy_animation" pos (0.112, 0.625)

image Kitty_doggy_finger_anal_animation:
    animation
    "Zero_sex_finger"

    subpixel True
    block:
        ease 0.5 yoffset -20
        pause 0.25
        ease 1.75 yoffset 0
        repeat

layeredimage Kitty_doggy_finger_anal_animations:
    always:
        "Kitty_doggy_finger_anal_animation" pos (0.112, 0.57)














image slap_ass:
    animation
    "UI_Hand"

    subpixel True
    alpha 0.5
    rotate 40
    block:
        parallel:
            ease 0.5 xoffset -300 rotate 80
            ease 0.1 xoffset -290 rotate 80
            pause 0.5
        parallel:
            ease 0.2 yoffset 140
            pause 0.9











image Notslap_ass:
    contains:
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
                ease 0.2 yoffset 520
                pause 0.9
            repeat
