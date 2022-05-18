transform blowjob_starting_cock:
    anchor (.5,.5)
    rotate -10

transform blowjob_licking_cock:
    subpixel True
    anchor (.5,.5)
    ease 0.5 rotate 0
    block:
        ease 2 rotate -5
        pause 0.5
        ease 2.5 rotate 0
        repeat

transform blowjob_straight_cock:
    anchor (.5,.5)
    rotate 0

image Zero_blowjob_cock_animation0:
    "Zero_cock_blowjob"
    blowjob_starting_cock

image Zero_blowjob_cock_animation1:
    "Zero_cock_blowjob"
    blowjob_licking_cock

image Zero_blowjob_cock_animation2:
    "Zero_cock_blowjob"
    blowjob_straight_cock

image Zero_blowjob_cock_animation3:
    "Zero_cock_blowjob"
    blowjob_straight_cock

image Zero_blowjob_cock_animation4:
    "Zero_cock_blowjob"
    blowjob_straight_cock

image Zero_hotdog_static:
    contains:
        "Zero_cock_doggy_out"
        pos (175, 370)

image Zero_hotdog_moving:
    contains:
        "Zero_cock_doggy_out"
        pos (175, 370)
        block:
            ease 1 ypos 330
            ease 1 ypos 420
            repeat

image Zero_doggy_static:
    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (169, 545)
        block:
            ease 1 ypos 540
            pause 1
            ease 3 ypos 545
            repeat

image Zero_doggy_heading:
    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (171, 545)
        block:
            ease 1 xpos 168 ypos 500
            pause 1
            ease 3 xpos 171 ypos 545
            repeat

image Zero_doggy_fucking2:
    contains:
        "Zero_cock_doggy_in"
        pos (169, 500)
        block:
            ease 0.5 ypos 440
            pause 0.25
            ease 1.75 ypos 500
            repeat

image Zero_doggy_fucking3:
    contains:
        "Zero_cock_doggy_in"
        pos (169, 500)
        block:
            ease 0.2 ypos 440
            pause 0.1
            ease 0.6 ypos 500
            repeat

image Zero_doggy_anal_headingjunk:
    contains:
        Solid("#159457", xysize=(150,150))
        pos (152, 600)
        block:
            ease 0.5 ypos 550
            pause 0.25
            ease 1.75 ypos 600
            repeat

image Zero_doggy_anal_heading:
    contains:
        "Zero_cock_doggy_in"
        pos (172, 500)
        block:
            ease 0.5 ypos 450
            pause 0.25
            ease 1.75 ypos 500
            repeat

image Zero_doggy_anal1:
    contains:
        "Zero_cock_doggy_in"
        pos (172, 460)
        block:
            ease 0.5 ypos 395
            pause 0.25
            ease 1.75 ypos 460
            repeat

image Zero_doggy_anal2:
    contains:
        "Zero_cock_doggy_in"
        pos (172, 460)
        block:
            ease 0.2 ypos 395
            pause 0.1
            ease 0.6 ypos 465
            repeat
