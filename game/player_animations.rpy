image Zero_fondle_thigh_animation:
    "Zero_hand"
    alpha 0.5 zoom 0.7
    rotate 100
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
    "Zero_hand"
    alpha 0.5 zoom (-0.7, 0.7)
    rotate -60
    block:
        ease 1 rotate -30
        ease 1 rotate -60
        repeat

image Zero_fondle_breasts_left_animation:
    "Zero_hand"
    alpha 0.5 zoom 0.7
    rotate 90
    block:
        ease 1 rotate 60
        ease 1 rotate 90
        repeat

image Zero_suck_breasts_right_animation:
    "Zero_tongue"
    alpha 0.5 zoom (-0.5, 0.5)
    rotate 30
    block:
        ease 0.5 rotate -45 offset (10, -30)
        pause 0.5
        ease 1.5 rotate 30 offset (0, 0)
        repeat

image Zero_suck_breasts_left_animation:
    "Zero_tongue"
    alpha 0.5 zoom (-0.5, 0.5)
    rotate 30
    block:
        ease 0.5 rotate -45 offset (40, -30)
        pause 0.5
        ease 1.5 rotate 30 offset (0, 0)
        repeat

image Zero_fondle_pussy_animation:
    "Zero_hand"
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
    "Zero_finger"
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
    "Zero_tongue"
    alpha 0.5 zoom (-0.5, 0.5)
    rotate 10
    block:
        easeout 0.5 rotate -50 offset (-20, -20)
        linear 0.5 rotate -60 offset (-30, -10)
        easein 1 rotate 10 offset (0, 0)
        repeat

image Zero_doggy_fondle_breast_animation:
    "Zero_hand_under"
    block:
        ease 1 rotate 10
        ease 1 rotate 0
        repeat

image Rogue_handjob_cock_animation0:
    "Zero_handjob_cock"

image Rogue_handjob_cock_animation1:
    "Zero_handjob_cock"
    rotate_pad False
    ease 0.5 yoffset 0 rotate -2
    pause 0.25
    ease 1.0 yoffset 0 rotate 0
    pause 0.1
    repeat

image Rogue_handjob_cock_animation2:
    "Zero_handjob_cock"
    rotate_pad False
    ease 0.2 yoffset 0 rotate -3
    ease 0.5 yoffset 0 rotate 0
    pause 0.1
    repeat

layeredimage Rogue_handjob_cock_animations:
    always:
        "Rogue_handjob_cock_animation[action_speed]" pos (-0.04, 0.455) zoom 0.28

image Rogue_titjob_cock_animation0:
    "Zero_handjob_cock"

image Rogue_titjob_cock_animation1:
    "Zero_handjob_cock"
    block:
        ease 1 yoffset -60
        easeout 0.2 yoffset -70
        easein 1.3 yoffset -20
        repeat

image Rogue_titjob_cock_animation2:
    "Zero_handjob_cock"
    block:
        ease 0.35 yoffset -50
        ease 0.4 yoffset -30
        repeat

layeredimage Rogue_titjob_cock_animations:
    always:
        "Rogue_titjob_cock_animation[action_speed]" pos (-0.05, 1.0) zoom 0.65

image Rogue_blowjob_cock_animation0:
    "Zero_blowjob_cock"
    rotate -10

image Rogue_blowjob_cock_animation1:
    "Zero_blowjob_cock"
    ease 0.5 rotate 0
    block:
        ease 2 rotate -5
        pause 0.5
        ease 2.5 rotate 0
        repeat

image Rogue_blowjob_cock_animation2:
    "Zero_blowjob_cock"

image Rogue_blowjob_cock_animation3:
    "Zero_blowjob_cock"

image Rogue_blowjob_cock_animation4:
    "Zero_blowjob_cock"

layeredimage Rogue_blowjob_cock_animations:
    always:
        "Rogue_blowjob_cock_animation[action_speed]" pos (0.021, 0.455) zoom 0.28

image Rogue_sex_cock_animation0:
    "Zero_doggy_cock_in"

image Rogue_sex_cock_animation1:
    "Zero_doggy_cock_in"
    block:
        ease 1 yoffset -20
        pause 1
        ease 3 yoffset 0
        repeat

image Rogue_sex_cock_animation2:
    "Zero_doggy_cock_in"
    block:
        ease 1 yoffset -90
        pause 1
        ease 3 yoffset -40
        repeat

image Rogue_sex_cock_animation3:
    "Zero_doggy_cock_in"
    block:
        ease 0.25 yoffset -90
        pause 0.25
        ease 1.5 yoffset -40
        repeat

layeredimage Rogue_sex_cock_animations:
    always:
        "Rogue_sex_cock_animation[action_speed]" pos (0.29175, 0.65) zoom 1.18

image Rogue_sex_cock_anal_animation0:
    "Zero_doggy_cock_in"

image Rogue_sex_cock_anal_animation1:
    "Zero_doggy_cock_in"
    block:
        ease 1 yoffset -30
        pause 1
        ease 3 yoffset 0
        repeat

image Rogue_sex_cock_anal_animation2:
    "Zero_doggy_cock_in"
    block:
        ease 1 yoffset -120
        pause 1
        ease 3 yoffset 0
        repeat

image Rogue_sex_cock_anal_animation3:
    "Zero_doggy_cock_in"
    block:
        ease 0.25 yoffset -120
        pause 0.25
        ease 1.5 yoffset 0
        repeat

layeredimage Rogue_sex_cock_anal_animations:
    always:
        "Rogue_sex_cock_anal_animation[action_speed]" pos (0.293, 0.7) zoom 1.18

image Rogue_sex_cock_footjob_animation0:
    "Zero_blowjob_cock"

image Rogue_sex_cock_footjob_animation1:
    "Zero_blowjob_cock"
    block:
        pause 0.5
        easein 0.75 yoffset -90
        ease 0.25 yoffset -85
        pause 1
        ease 2.50 yoffset 0
        repeat

image Rogue_sex_cock_footjob_animation2:
    "Zero_blowjob_cock"
    block:
        pause 0.2
        easein 0.4 yoffset -90
        ease 0.2 yoffset -85
        pause 0.2
        ease 1.00 yoffset 0
        repeat

layeredimage Rogue_sex_cock_footjob_animations:
    always:
        "Rogue_sex_cock_footjob_animation[action_speed]" pos (0.28, 0.6) alpha 0.8 zoom 0.6

image Rogue_sex_cock_hotdog_animation0:
    "Zero_doggy_cock_in"

image Rogue_sex_cock_hotdog_animation1:
    "Zero_doggy_cock_in"
    block:
        ease 1 yoffset -60
        pause 0.5
        ease 1.5 yoffset 0
        repeat

image Rogue_sex_cock_hotdog_animation2:
    "Zero_doggy_cock_in"
    block:
        ease 0.5 yoffset -110
        pause 0.5
        ease 1 yoffset 0
        repeat

image Rogue_sex_cock_hotdog_animation3:
    "Zero_doggy_cock_in"
    block:
        ease 0.5 yoffset -110
        pause 0.5
        ease 1 yoffset 0
        repeat

layeredimage Rogue_sex_cock_hotdog_animations:
    always:
        "Rogue_sex_cock_hotdog_animation[action_speed]" pos (0.29175, 0.65) zoom 1.18

image Rogue_sex_finger_pussy_animation:
    "Zero_sex_finger"
    block:
        ease 0.2 yoffset -40
        pause 0.2
        ease 0.6 yoffset 0
        repeat

layeredimage Rogue_sex_finger_pussy_animations:
    always:
        "Rogue_sex_finger_pussy_animation" pos (0.28, 0.6) zoom 1.2

image Rogue_sex_finger_ass_animation:
    "Zero_sex_finger"
    block:
        ease 0.4 yoffset -50
        pause 0.4
        ease 1.2 yoffset 0
        repeat

layeredimage Rogue_sex_finger_ass_animations:
    always:
        "Rogue_sex_finger_ass_animation" zoom 1.2

image Rogue_doggy_cock_animation0:
    "Zero_doggy_cock_in"
    block:
        ease 1 yoffset -5
        pause 1
        ease 3 yoffset 0
        repeat

image Rogue_doggy_cock_animation1:
    "Zero_doggy_cock_in"
    block:
        ease 1 xoffset -3 yoffset -45
        pause 1
        ease 3 xoffset 0 yoffset 0
        repeat

image Rogue_doggy_cock_animation2:
    "Zero_doggy_cock_in"
    block:
        ease 0.5 yoffset -60
        pause 0.25
        ease 1.75 yoffset 0
        repeat

image Rogue_doggy_cock_animation3:
    "Zero_doggy_cock_in"
    block:
        ease 0.2 yoffset -60
        pause 0.1
        ease 0.6 yoffset 0
        repeat

layeredimage Rogue_doggy_cock_animations:
    always:
        "Rogue_doggy_cock_animation[action_speed]" pos (0.112, 0.65)

image Rogue_doggy_cock_anal_animation0:
    "Zero_doggy_cock_in"

image Rogue_doggy_cock_anal_animation1:
    "Zero_doggy_cock_in"
    block:
        ease 0.5 yoffset -50
        pause 0.25
        ease 1.75 yoffset 0
        repeat

image Rogue_doggy_cock_anal_animation2:
    "Zero_doggy_cock_in"
    block:
        ease 0.5 yoffset -65
        pause 0.25
        ease 1.75 yoffset 0
        repeat

image Rogue_doggy_cock_anal_animation3:
    "Zero_doggy_cock_in"
    block:
        ease 0.2 yoffset -70
        pause 0.1
        ease 0.6 yoffset 0
        repeat

layeredimage Rogue_doggy_cock_anal_animations:
    always:
        "Rogue_doggy_cock_anal_animation[action_speed]" pos (0.112, 0.55)

image Rogue_doggy_cock_hotdog_animation0:
    "Zero_doggy_cock_out"

image Rogue_doggy_cock_hotdog_animation1:
    "Zero_doggy_cock_out"
    block:
        ease 1 yoffset -90
        ease 1 yoffset 0
        repeat

image Rogue_doggy_cock_hotdog_animation2:
    "Zero_doggy_cock_out"
    block:
        ease 1 yoffset -90
        ease 1 yoffset 0
        repeat

image Rogue_doggy_cock_hotdog_animation3:
    "Zero_doggy_cock_out"
    block:
        ease 1 yoffset -90
        ease 1 yoffset 0
        repeat

layeredimage Rogue_doggy_cock_hotdog_animations:
    always:
        "Rogue_doggy_cock_hotdog_animation[action_speed]" pos (0.112, 0.65)

image Rogue_doggy_cock_footjob_animation0:
    "Zero_doggy_cock_out"

image Rogue_doggy_cock_footjob_animation1:
    "Zero_doggy_cock_out"
    block:
        pause 0.4
        ease 1.7 yoffset 20
        ease 0.9 yoffset 0
        repeat

image Rogue_doggy_cock_footjob_animation2:
    "Zero_doggy_cock_out"
    block:
        pause 0.07
        ease 0.6 yoffset 20
        ease 0.28 yoffset 0
        repeat

layeredimage Rogue_doggy_cock_footjob_animations:
    always:
        "Rogue_doggy_cock_footjob_animation[action_speed]" pos (-0.005, 0.24) zoom 1.1

image Rogue_doggy_finger_pussy_animation:
    "Zero_sex_finger"
    block:
        ease 1 offset (-3, -45)
        pause 1
        ease 3 offset (0, 0)
        repeat

layeredimage Rogue_doggy_finger_pussy_animations:
    always:
        "Rogue_doggy_finger_pussy_animation" pos (0.1, 0.47)

image Rogue_doggy_finger_anal_animation:
    "Zero_sex_finger"
    block:
        ease 0.5 yoffset -20
        pause 0.25
        ease 1.75 yoffset 0
        repeat

layeredimage Rogue_doggy_finger_anal_animations:
    always:
        "Rogue_doggy_finger_anal_animation" pos (0.1, 0.47)








image slap_ass:
    contains:
        "UI_Hand"
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
                ease 0.2 ypos 520
                pause 0.9
            repeat
