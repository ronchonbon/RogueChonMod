label reset_position:
    if focused_Girl.location != bg_current:
        return

    $ focused_Girl.pose = "full"

    call hide_girl(focused_Girl, hide_sprite = True)

    show Rogue_sprite zorder focused_Girl.sprite_layer at sprite_location(focused_Girl.sprite_location):

    return

label smooch:
    $ focused_Girl.change_face("_kiss")

    show Rogue_sprite zorder focused_Girl.sprite_layer at sprite_location(focused_Girl.sprite_location):
        ease 0.5 pos (focused_Girl.sprite_location, 0.1) zoom 2
        pause 1
        ease 0.5 pos (focused_Girl.sprite_location, 0.0) zoom 1

    pause 1

    $ focused_Girl.change_face("_sexy")

    return

label kiss_launch:
    $ focused_Girl.pose = "kiss"

    call hide_girl(focused_Girl)

    show Rogue_sprite zorder focused_Girl.sprite_layer at sprite_location(focused_Girl.sprite_location):
        ease 0.5 pos (focused_Girl.sprite_location, 0.1) zoom 2

    return

label breasts_launch:
    $ focused_Girl.pose = "breasts"

    call hide_girl(focused_Girl)

    show Rogue_sprite zorder focused_Girl.sprite_layer at sprite_location(focused_Girl.sprite_location):
        ease 0.5 pos (focused_Girl.sprite_location, -0.2) zoom 2

    return

label middle_launch:
    $ focused_Girl.pose = "middle"

    call hide_girl(focused_Girl)

    show Rogue_sprite zorder focused_Girl.sprite_layer at sprite_location(stage_center):
        ease 0.5 pos (focused_Girl.sprite_location, -0.3) zoom 1.5

    return

label pussy_launch:
    $ focused_Girl.pose = "pussy"

    call hide_girl(focused_Girl)

    show Rogue_sprite zorder focused_Girl.sprite_layer at sprite_location(focused_Girl.sprite_location):
        ease 0.5 pos (focused_Girl.sprite_location, -0.4) zoom 2

    return

label handjob_launch:
    if renpy.showing(focused_Girl.tag + "_handjob_animation"):
        return

    show Rogue_sprite zorder focused_Girl.sprite_layer at sprite_location(focused_Girl.sprite_location):
        ease 0.5 pos (focused_Girl.sprite_location, 0.1) zoom 2

    if taboo:
        if len(Present) >= 2:
            if Present[0] != focused_Girl:
                "[focused_Girl.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != focused_Girl:
                "[focused_Girl.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[focused_Girl.name] looks around to see if anyone can see her."

    if not focused_Girl.action_counter["handjob"] and focused_Girl.outfit["gloves"]:
        "As you pull out your cock, [focused_Girl.name] pulls off her gloves, and hesitantly reaches for it. She starts to roughly stroke on it."
    else:
        "She then leans over and grabs your cock."
        "[focused_Girl.name] bends down and grabs your cock."

    $ focused_Girl.outfit["gloves"] = ""
    $ focused_Girl.arm_pose = 1

    call hide_girl(focused_Girl, hide_sprite = True)

    show Rogue_handjob_animation zorder 150 at sprite_location(stage_center) with easeinbottom

    return

label titjob_launch:
    if renpy.showing(focused_Girl.tag + "_titjob_animation"):
        return

    show Rogue_sprite zorder focused_Girl.sprite_layer at sprite_location(focused_Girl.sprite_location):
        ease 0.5 pos (focused_Girl.sprite_location, 0.1) zoom 2

    if taboo:
        if len(Present) >= 2:
            if Present[0] != focused_Girl:
                "[focused_Girl.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != focused_Girl:
                "[focused_Girl.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[focused_Girl.name] looks around to see if anyone can see her."

    if focused_Girl.outfit["bra"] and focused_Girl.outfit["top"]:
        "She throws off her [focused_Girl.outfit[top]] and her [focused_Girl.outfit[bra]]."
    elif focused_Girl.outfit["top"]:
        "She throws off her [focused_Girl.outfit[top]], baring her breasts underneath."
    elif focused_Girl.outfit["bra"]:
        "She tugs off her [focused_Girl.outfit[bra]] and throws it aside."

    $ focused_Girl.outfit["top"] = ""
    $ focused_Girl.outfit["bra"] = ""
    $ focused_Girl.outfit["gloves"] = ""

    call Rogue_First_Topless

    if not focused_Girl.action_counter["titjob"] and "cockout" not in Player.recent_history:
        if not focused_Girl.outfit["bra"] and not focused_Girl.outfit["top"]:
            "As you pull out your cock, [focused_Girl.name] hesitantly places it between her breasts and starts to rub them up and down the shaft."
        elif focused_Girl.outfit["bra"] and not focused_Girl.outfit["top"]:
            "As you pull out your cock, [focused_Girl.name] hesitantly places it under her [focused_Girl.outfit['bra']], between her breasts and starts to rub them up and down the shaft."
        elif focused_Girl.outfit["bra"] and focused_Girl.outfit["top"]:
            "As you pull out your cock, [focused_Girl.name] hesitantly places it under her [focused_Girl.outfit['top']], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, [focused_Girl.name] hesitantly places it under her clothes, between her breasts and starts to rub them up and down the shaft."
    elif "cockout" not in Player.recent_history:
        if not focused_Girl.outfit["bra"] and not focused_Girl.outfit["top"]:
            "As you pull out your cock, [focused_Girl.name] places it between her breasts and starts to rub them up and down the shaft."
        elif focused_Girl.outfit["bra"] and not focused_Girl.outfit["top"]:
            "As you pull out your cock, [focused_Girl.name] places it under her [focused_Girl.outfit['bra']], between her breasts and starts to rub them up and down the shaft."
        elif focused_Girl.outfit["bra"] and focused_Girl.outfit["top"]:
            "As you pull out your cock, [focused_Girl.name] places it under her [focused_Girl.outfit['top']], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, [focused_Girl.name] places it under her clothes, between her breasts and starts to rub them up and down the shaft."
    else:
        "[focused_Girl.name] wraps her tits around your cock."

    call hide_girl(focused_Girl, hide_sprite = True)

    show Rogue_titjob_animation zorder 150 at sprite_location(stage_center)

    return

label blowjob_launch:
    if renpy.showing(focused_Girl.tag + "_blowjob_animation"):
        return

    show Rogue_sprite zorder focused_Girl.sprite_layer at sprite_location(focused_Girl.sprite_location):
        ease 0.5 pos (focused_Girl.sprite_location, 0.1) zoom 2

    if taboo:
        if len(Present) >= 2:
            if Present[0] != focused_Girl:
                "[focused_Girl.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != focused_Girl:
                "[focused_Girl.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[focused_Girl.name] looks around to see if anyone can see her."

    if not focused_Girl.action_counter["blowjob"] and "cockout" not in Player.recent_history:
        "[focused_Girl.name] hesitantly pulls down your pants and touches her mouth to your cock."
    else:
        "[focused_Girl.name] bends down and begins to suck on your cock."

    call hide_girl(focused_Girl, hide_sprite = True)

    show Rogue_blowjob_animation zorder 150 at sprite_location(stage_center)

    return

label sex_launch:
    $ Player.sprite = True

    if primary_action == "sex":
        $ Player.cock_position = "in"

        if offhand_action in pussy_actions:
            $ offhand_action = None
    elif primary_action == "anal":
        $ Player.cock_position = "anal"

        if offhand_action in ass_actions:
            $ offhand_action = None
    elif primary_action == "hotdog":
        $ Player.cock_position = "out"
    elif primary_action == "footjob":
        $ show_feet = True

        $ Player.cock_position = "footjob"
    elif primary_action == "massage":
        $ Player.sprite = False
        $ Player.cock_position = None
    else:
        $ Player.sprite = False
        $ Player.cock_position = "out"

    if focused_Girl.pose == "doggy":
        call doggy_launch

        return

    if renpy.showing(focused_Girl.tag + "_sex_animation"):
        return

    call hide_girl(focused_Girl, hide_sprite = True)

    show Rogue_sex_animation zorder 150 at sprite_location(stage_center)

    return

label doggy_launch:
    if renpy.showing(focused_Girl.tag + "_doggy_animation"):
        return

    call hide_girl(focused_Girl, hide_sprite = True)

    show Rogue_doggy_animation zorder 150 at sprite_location(stage_center)

    return

transform blowjob_starting:
    subpixel True
    ease 1.5 offset (0, 0)

transform blowjob_licking:
    subpixel True
    ease 0.5 offset (2, -20)
    block:
        ease 2.5 offset (15, 60)
        ease 2 offset (2, -20)
        pause 0.5
        repeat

transform blowjob_licking_body:
    subpixel True
    ease 0.5 offset (2, -20)
    block:
        ease 2.5 offset (20, 55)
        ease 2 offset (2, -20)
        pause 0.5
        repeat

transform blowjob_heading:
    subpixel True
    block:
        ease 1 yoffset 35
        ease 1.5 yoffset 0
        repeat

transform blowjob_sucking:
    subpixel True
    ease 0.5 offset (0, 30)
    block:
        ease 1 yoffset 80
        ease 1.5 yoffset 30
        repeat

transform blowjob_sucking_body:
    subpixel True
    ease 0.5 offset (0, 30)
    block:
        ease 1 yoffset 65
        ease 1.5 yoffset 30
        repeat

transform blowjob_deepthroat:
    ease 0.5 offset (0, 40)
    block:
        subpixel True
        ease 1 yoffset 110
        pause 0.5
        ease 2 yoffset 40
        repeat

transform blowjob_deepthroat_body:
    ease 0.5 offset (0, 40)
    block:
        subpixel True
        ease 1.2 yoffset 90
        pause 0.5
        ease 1.8 yoffset 40
        repeat

transform blowjob_mouth_animation2:
    subpixel True
    pos (0.165, 0.521) anchor (0.4, 0.6) zoom 0.90
    block:
        pause 0.10
        easeout 0.55 zoom 0.9
        linear 0.10 zoom 0.87
        easein 0.30 zoom 0.9
        pause 0.15
        easeout 0.40 zoom 0.87
        linear 0.10 zoom 0.9
        easein 0.45 zoom 0.70
        pause 0.35
        repeat

transform blowjob_face_mask_animation2:
    subpixel True
    pos (0.445, 0.616) anchor (0.45, 0.6) zoom 0.90
    block:
        pause 0.10
        easeout 0.55 zoom 0.9
        linear 0.10 zoom 0.87
        easein 0.30 zoom 0.9
        pause 0.15
        easeout 0.40 zoom 0.87
        linear 0.10 zoom 0.9
        easein 0.45 zoom 0.70
        pause 0.35
        repeat
