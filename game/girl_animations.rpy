label show_Girl(Girl, x_position = None, y_position = 0, sprite_layer = None, transition = None, transformation = None):
    if x_position:
        $ Girl.sprite_location = x_position

    if sprite_layer:
        $ Girl.sprite_layer = sprite_layer

    if transition and transformation:
        if Girl == RogueX:
            show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), transformation with transition
        elif Girl == KittyX:
            show Kitty_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), transformation with transition
        elif Girl == EmmaX:
            if Girl.diamond:
                show Emma_sprite standing diamond zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), transformation with transition
            else:
                show Emma_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), transformation with transition
        elif Girl == LauraX:
            $ Girl.claws = False

            show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), transformation with transition
        elif Girl == JeanX:
            show Jean_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), transformation with transition
        elif Girl == StormX:
            show Storm_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), transformation with transition
        elif Girl == JubesX:
            show Jubes_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), transformation with transition
        elif Girl == MystiqueX:
            if Girl.disguise:
                show expression "Mystique_sprite standing " + Girl.disguise zorder Girl.sprite_layer as Mystique_sprite at sprite_location(Girl.sprite_location, y_position), transformation with transition
            else:
                show Mystique_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), transformation with transition
    elif transition:
        if Girl == RogueX:
            show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position) with transition
        elif Girl == KittyX:
            show Kitty_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position) with transition
        elif Girl == EmmaX:
            if Girl.diamond:
                show Emma_sprite standing diamond zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position) with transition
            else:
                show Emma_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position) with transition
        elif Girl == LauraX:
            $ Girl.claws = False

            show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position) with transition
        elif Girl == JeanX:
            show Jean_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position) with transition
        elif Girl == StormX:
            show Storm_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position) with transition
        elif Girl == JubesX:
            show Jubes_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position) with transition
        elif Girl == MystiqueX:
            if Girl.disguise:
                show expression "Mystique_sprite standing " + Girl.disguise zorder Girl.sprite_layer as Mystique_sprite at sprite_location(Girl.sprite_location, y_position) with transition
            else:
                show Mystique_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position) with transition
    elif transformation:
        if Girl == RogueX:
            show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), transformation
        elif Girl == KittyX:
            show Kitty_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), transformation
        elif Girl == EmmaX:
            if Girl.diamond:
                show Emma_sprite standing diamond zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), transformation
            else:
                show Emma_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), transformation
        elif Girl == LauraX:
            $ Girl.claws = False

            show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), transformation
        elif Girl == JeanX:
            show Jean_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), transformation
        elif Girl == StormX:
            show Storm_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), transformation
        elif Girl == JubesX:
            show Jubes_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), transformation
        elif Girl == MystiqueX:
            if Girl.disguise:
                show expression "Mystique_sprite standing " + Girl.disguise zorder Girl.sprite_layer as Mystique_sprite at sprite_location(Girl.sprite_location, y_position), transformation
            else:
                show Mystique_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), transformation
    else:
        if Girl == RogueX:
            show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position)
        elif Girl == KittyX:
            show Kitty_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position)
        elif Girl == EmmaX:
            if Girl.diamond:
                show Emma_sprite standing diamond zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position)
            else:
                show Emma_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position)
        elif Girl == LauraX:
            $ Girl.claws = False

            show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position)
        elif Girl == JeanX:
            show Jean_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position)
        elif Girl == StormX:
            show Storm_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position)
        elif Girl == JubesX:
            show Jubes_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position)
        elif Girl == MystiqueX:
            if Girl.disguise:
                show expression "Mystique_sprite standing " + Girl.disguise zorder Girl.sprite_layer as Mystique_sprite at sprite_location(Girl.sprite_location, y_position)
            else:
                show Mystique_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position)

    return

label hide_Girl(Girl, transition = None):
    if transition:
        if Girl == RogueX:
            hide Rogue_sprite with transition
        elif Girl == KittyX:
            hide Kitty_sprite with transition
        elif Girl == EmmaX:
            hide Emma_sprite with transition
        elif Girl == LauraX:
            hide Laura_sprite with transition
        elif Girl == JeanX:
            hide Jean_sprite with transition
        elif Girl == StormX:
            hide Storm_sprite with transition
        elif Girl == JubesX:
            hide Jubes_sprite with transition
        elif Girl == MystiqueX:
            hide Mystique_sprite with transition
    else:
        if Girl == RogueX:
            hide Rogue_sprite
        elif Girl == KittyX:
            hide Kitty_sprite
        elif Girl == EmmaX:
            hide Emma_sprite
        elif Girl == LauraX:
            hide Laura_sprite
        elif Girl == JeanX:
            hide Jean_sprite
        elif Girl == StormX:
            hide Storm_sprite
        elif Girl == JubesX:
            hide Jubes_sprite
        elif Girl == MystiqueX:
            hide Mystique_sprite

    return

label hide_all:
    hide Rogue_sprite
    hide Kitty_sprite
    hide Emma_sprite
    hide Laura_sprite
    hide Jean_sprite
    hide Storm_sprite
    hide Jubes_sprite

    hide Xavier_sprite

    return

transform reset_zoom:
    ease 0.75 zoom 1.0

transform instant_reset:
    zoom 1.0

label reset_position(Girl):
    $ Girl.pose = "full"

    call show_Girl(Girl, transformation = reset_zoom)

    return

label shift_view(Girl, view):
    if view == "menu":
        menu:
            "Full body":
                call reset_position(Girl)
            "Upper half":
                call breasts_launch(Girl)
            "Middle view":
                call middle_launch(Girl)
            "Lower half":
                call pussy_launch(Girl)
            "Doggy" if Girl in [RogueX, KittyX, EmmaX, LauraX, JeanX]:
                $ Girl.pose = "doggy"

                call show_sex(Girl, None)
            "Cowgirl" if Girl in [EmmaX, JeanX, StormX]:
                $ Girl.pose = "sex"

                call show_sex(Girl, None)
            "Missionary" if Girl in [RogueX, KittyX, LauraX]:
                $ Girl.pose = "sex"

                call show_sex(Girl, None)
            "Never mind":
                pass
    else:
        if view == "full":
            call reset_position(Girl)
        elif view == "breasts":
            call breasts_launch(Girl)
        elif view == "middle":
            call middle_launch(Girl)
        elif view == "pussy":
            call pussy_launch(Girl)
        elif view in ["sex", "doggy"]:
            call show_sex(Girl, None)
        elif view == "kiss":
            call kiss_launch(Girl)

    return

transform close_launch_animation(x_zoom):
    ease 0.75 xzoom x_zoom yzoom 1.3

label close_launch(GirlA, GirlB = None):
    if GirlB:
        $ temp_Girls = [GirlA, GirlB]
    elif GirlA:
        $ temp_Girls = [GirlA]

    while temp_Girls:
        if temp_Girls[0] == KittyX or temp_Girls[0] == LauraX:
            $ temp_Girls[0].arm_pose = 1
        else:
            $ temp_Girls[0].arm_pose = 2

        if GirlA == temp_Girls[0]:
            if temp_Girls[0] == KittyX:
                $ x_position = 450
            elif temp_Girls[0] == RogueX:
                $ x_position = 550
            else:
                $ x_position = 500

            $ temp_Girls[0].sprite_layer = 4

            $ x_zoom = -1.3
        elif GirlB == temp_Girls[0]:
            if temp_Girls[0] == EmmaX or LauraX:
                $ x_position = 700
            else:
                $ x_position = 715

            $ temp_Girls[0].sprite_layer = 3

            $ x_zoom = 1.3

        call display_Girl(temp_Girls[0], x_position = x_position, y_position = 0.15, transformation = close_launch_animation(x_zoom))

        $ temp_Girls.remove(temp_Girls[0])

    return

transform smooch_animation:
    ease 0.6 ypos 0.1 zoom 2.0
    pause 1.0
    ease 0.6 ypos 0.0 zoom 1.0

label smooch(Girl):
    $ Girl.change_face("_kiss")

    call show_Girl(Girl, transformation = smooch_animation)

    pause 1.0

    $ Girl.change_face("_sexy")

    return

transform kiss_launch_animation:
    ease 0.75 ypos 0.1 zoom 2.0

label kiss_launch(Girl):
    $ Girl.pose = "kiss"
    $ Girl.change_face("_kiss")

    call show_Girl(Girl, transformation = kiss_launch_animation)

    return

transform breasts_launch_animation:
    ease 0.75 ypos -0.2 zoom 2.0

label breasts_launch(Girl):
    $ Girl.pose = "breasts"

    call show_Girl(Girl, transformation = breasts_launch_animation)

    return

transform middle_launch_animation:
    ease 0.75 ypos -0.3 zoom 1.5

label middle_launch(Girl):
    $ Girl.pose = "middle"

    call show_Girl(Girl, transformation = middle_launch_animation)

    return

transform pussy_launch_animation:
    ease 0.75 ypos -0.4 zoom 2.0

label pussy_launch(Girl):
    $ Girl.pose = "pussy"

    call show_Girl(Girl, transformation = pussy_launch_animation)

    return

transform show_handjob_animation:
    ease 0.75 ypos 0.1 zoom 2.0

label show_handjob(Girl, orgasm = False):
    if renpy.showing(Girl.tag + "_sprite handjob"):
        return

    $ action_speed = 0

    call show_Girl(Girl, transformation = show_handjob_animation)

    if taboo:
        if len(Present) >= 2:
            if Present[0] != Girl:
                "[Girl.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != Girl:
                "[Girl.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[Girl.name] looks around to see if anyone can see her."

    if not orgasm:
        if not Girl.action_counter["handjob"] and Girl.outfit["gloves"]:
            "As you pull out your cock, [Girl.name] pulls off her gloves, and hesitantly reaches for it. She starts to roughly stroke on it."
        else:
            "She then leans over and grabs your cock."
    else:
        "[Girl.name] bends down and grabs your cock."

    $ Girl.outfit["gloves"] = ""
    $ Girl.arm_pose = 1

    if Girl == RogueX:
        show Rogue_sprite handjob zorder 150 at sprite_location(stage_center):
            zoom 1.0
    elif Girl == KittyX:
        show Kitty_sprite handjob zorder 150 at sprite_location(stage_center):
            zoom 1.0
    elif Girl == EmmaX:
        show Emma_sprite handjob zorder 150 at sprite_location(stage_center):
            zoom 1.0
    elif Girl == LauraX:
        show Laura_sprite handjob zorder 150 at sprite_location(stage_center):
            zoom 1.0
    elif Girl == JeanX:
        show Jean_sprite handjob zorder 150 at sprite_location(stage_center):
            zoom 1.0
    elif Girl == StormX:
        show Storm_sprite handjob zorder 150 at sprite_location(stage_center):
            zoom 1.0
    elif Girl == JubesX:
        show Jubes_sprite handjob zorder 150 at sprite_location(stage_center):
            zoom 1.0

    return

transform show_titjob_animation:
    ease 0.5 ypos 0.05 zoom 2.0

label show_titjob(Girl, orgasm = False):
    if renpy.showing(Girl.tag + "_sprite titjob"):
        return

    $ action_speed = 0

    call show_Girl(Girl, transformation = show_titjob_animation)

    if taboo:
        if len(Present) >= 2:
            if Present[0] != Girl:
                "[Girl.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != Girl:
                "[Girl.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[Girl.name] looks around to see if anyone can see her."

    if Girl.outfit["bra"] and Girl.outfit["top"]:
        "She throws off her [Girl.outfit[top]] and her [Girl.outfit[bra]]."
    elif Girl.outfit["top"]:
        "She throws off her [Girl.outfit[top]], baring her breasts underneath."
    elif Girl.outfit["bra"]:
        "She tugs off her [Girl.outfit[bra]] and throws it aside."

    $ Girl.outfit["top"] = ""
    $ Girl.outfit["bra"] = ""
    $ Girl.outfit["gloves"] = ""

    call expression Girl.tag + "_First_Topless"

    if not orgasm:
        if not Girl.action_counter["titjob"] and "cockout" not in Player.recent_history:
            if not Girl.outfit["bra"] and not Girl.outfit["top"]:
                "As you pull out your cock, [Girl.name] hesitantly places it between her breasts and starts to rub them up and down the shaft."
            elif Girl.outfit["bra"] and not Girl.outfit["top"]:
                "As you pull out your cock, [Girl.name] hesitantly places it under her [Girl.outfit['bra']], between her breasts and starts to rub them up and down the shaft."
            elif Girl.outfit["bra"] and Girl.outfit["top"]:
                "As you pull out your cock, [Girl.name] hesitantly places it under her [Girl.outfit['top']], between her breasts and starts to rub them up and down the shaft."
            else:
                "As you pull out your cock, [Girl.name] hesitantly places it under her clothes, between her breasts and starts to rub them up and down the shaft."
        elif "cockout" not in Player.recent_history:
            if not Girl.outfit["bra"] and not Girl.outfit["top"]:
                "As you pull out your cock, [Girl.name] places it between her breasts and starts to rub them up and down the shaft."
            elif Girl.outfit["bra"] and not Girl.outfit["top"]:
                "As you pull out your cock, [Girl.name] places it under her [Girl.outfit['bra']], between her breasts and starts to rub them up and down the shaft."
            elif Girl.outfit["bra"] and Girl.outfit["top"]:
                "As you pull out your cock, [Girl.name] places it under her [Girl.outfit['top']], between her breasts and starts to rub them up and down the shaft."
            else:
                "As you pull out your cock, [Girl.name] places it under her clothes, between her breasts and starts to rub them up and down the shaft."
    else:
        "[Girl.name] wraps her tits around your cock."

    if Girl == RogueX:
        show Rogue_sprite titjob zorder 150 at sprite_location(stage_center):
            zoom 1.0
    elif Girl == KittyX:
        show Kitty_sprite titjob zorder 150 at sprite_location(stage_center):
            zoom 1.0
    elif Girl == EmmaX:
        show Emma_sprite titjob zorder 150 at sprite_location(stage_center):
            zoom 1.0
    elif Girl == LauraX:
        show Laura_sprite titjob zorder 150 at sprite_location(stage_center):
            zoom 1.0
    elif Girl == JeanX:
        show Jean_sprite titjob zorder 150 at sprite_location(stage_center):
            zoom 1.0
    elif Girl == StormX:
        show Storm_sprite titjob zorder 150 at sprite_location(stage_center):
            zoom 1.0
    elif Girl == JubesX:
        show Jubes_sprite titjob zorder 150 at sprite_location(stage_center):
            zoom 1.0

    return

transform show_blowjob_animation:
    ease 0.5 ypos 0.1 zoom 2.0

label show_blowjob(Girl, orgasm = False):
    if renpy.showing(Girl.tag + "_sprite blowjob"):
        return

    $ action_speed = 0

    call show_Girl(Girl, transformation = show_blowjob_animation)

    if taboo:
        if len(Present) >= 2:
            if Present[0] != Girl:
                "[Girl.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != Girl:
                "[Girl.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[Girl.name] looks around to see if anyone can see her."

    if not orgasm:
        if not Girl.action_counter["blowjob"] and "cockout" not in Player.recent_history:
            "[Girl.name] hesitantly pulls down your pants and touches her mouth to your cock."
    else:
        "[Girl.name] bends down and begins to suck on your cock."

    if Girl == RogueX:
        show Rogue_sprite blowjob zorder 150 at sprite_location(stage_center):
            zoom 1.0
    elif Girl == KittyX:
        show Kitty_sprite blowjob zorder 150 at sprite_location(stage_center):
            zoom 1.0
    elif Girl == EmmaX:
        show Emma_sprite blowjob zorder 150 at sprite_location(stage_center):
            zoom 1.0
    elif Girl == LauraX:
        show Laura_sprite blowjob zorder 150 at sprite_location(stage_center):
            zoom 1.0
    elif Girl == JeanX:
        show Jean_sprite blowjob zorder 150 at sprite_location(stage_center):
            zoom 1.0
    elif Girl == StormX:
        show Storm_sprite blowjob zorder 150 at sprite_location(stage_center):
            zoom 1.0
    elif Girl == JubesX:
        show Jubes_sprite blowjob zorder 150 at sprite_location(stage_center):
            zoom 1.0

    return

label show_sex(Girl, action):
    if action == "massage":
        $ Player.cock_position = None
    elif action == "footjob":
        $ show_feet = True

        $ Player.cock_position = "footjob"
    elif action == "hotdog":
        $ Player.cock_position = "out"
    elif action == "sex":
        $ Player.cock_position = "in"

        if Player.secondary_action in pussy_actions:
            $ Player.secondary_action = None
    elif action == "anal":
        $ Player.cock_position = "anal"

        if Player.secondary_action in ass_actions:
            $ Player.secondary_action = None

    if Girl.pose == "doggy":
        call show_doggy(Girl)

        return

    if renpy.showing(Girl.tag + "_sprite sex"):
        return

    $ action_speed = 0

    if Girl == RogueX:
        show Rogue_sprite sex zorder 150 at sprite_location(stage_center)
    elif Girl == KittyX:
        show Kitty_sprite sex zorder 150 at sprite_location(stage_center)
    elif Girl == EmmaX:
        show Emma_sprite sex zorder 150 at sprite_location(stage_center)
    elif Girl == LauraX:
        show Laura_sprite sex zorder 150 at sprite_location(stage_center)
    elif Girl == JeanX:
        show Jean_sprite sex zorder 150 at sprite_location(stage_center)
    elif Girl == StormX:
        show Storm_sprite sex zorder 150 at sprite_location(stage_center)
    elif Girl == JubesX:
        show Jubes_sprite sex zorder 150 at sprite_location(stage_center)

    return

label show_doggy(Girl):
    if renpy.showing(Girl.tag + "_sprite doggy"):
        return

    $ action_speed = 0

    if Girl == RogueX:
        show Rogue_sprite doggy zorder 150 at sprite_location(stage_center)
    elif Girl == KittyX:
        show Kitty_sprite doggy zorder 150 at sprite_location(stage_center)
    elif Girl == EmmaX:
        show Emma_sprite doggy zorder 150 at sprite_location(stage_center)
    elif Girl == LauraX:
        show Laura_sprite doggy zorder 150 at sprite_location(stage_center)
    elif Girl == JeanX:
        show Jean_sprite doggy zorder 150 at sprite_location(stage_center)
    elif Girl == StormX:
        show Storm_sprite doggy zorder 150 at sprite_location(stage_center)
    elif Girl == JubesX:
        show Jubes_sprite doggy zorder 150 at sprite_location(stage_center)

    return

label lesbian_launch(Girl):
    $ temp_Girls = [Girl, Partner]

    while temp_Girls:
        if "unseen" in temp_Girls[0].recent_history:
            $ temp_Girls[0].eyes = "_closed"
        elif Girl == temp_Girls[0]:
            if Girl == RogueX:
                $ temp_Girls[0].eyes = "_side"
            elif Girl == EmmaX:
                $ temp_Girls[0].eyes = "_squint"
            else:
                $ temp_Girls[0].eyes = "_leftside"
        else:
            $ temp_Girls[0].eyes = "_side"

        if temp_Girls[0] == KittyX or temp_Girls[0] == LauraX:
            $ temp_Girls[0].arm_pose = 1
        else:
            $ temp_Girls[0].arm_pose = 2

        if Girl == temp_Girls[0]:
            if temp_Girls[0] == KittyX:
                $ x_position = 450
            elif temp_Girls[0] == RogueX:
                $ x_position = 550
            else:
                $ x_position = 500

            $ temp_Girls[0].sprite_layer = 4

            $ x_zoom = -1.3
        else:
            if temp_Girls[0] == EmmaX or LauraX:
                $ x_position = 700
            else:
                $ x_position = 715

            if temp_Girls[0] == KittyX:
                if RogueX in (Partner,Girl):
                    $ KittyX.sprite_layer = 3
                else:
                    $ KittyX.sprite_layer = 1
            else:
                $ temp_Girls[0].sprite_layer = 3

            $ x_zoom = 1.3

        call show_Girl(temp_Girls[0], x_position = x_position, y_position = 0.15, transformation = close_launch_animation(x_zoom))

        $ temp_Girls.remove(temp_Girls[0])

    return

image Girl_hand_white:
    "images/misc/Girl_hand_white.png"

    anchor (0.5, 0.5)

image Girl_fingering_white:
    "images/misc/Girl_fingering_white.png"

    anchor (0.5, 0.5)

image Girl_hand_black:
    "images/misc/Girl_hand_black.png"

    anchor (0.5, 0.5)

image Girl_fingering_black:
    "images/misc/Girl_fingering_black.png"

    anchor (0.5, 0.5)

image Girl_fondle_breast_left_animation:
    "Girl_hand_white"

    alpha 0.5 zoom 0.6
    block:
        ease 1 rotate -40 offset (-20, -10)
        ease 1 rotate -20 offset (0, 0)
        repeat

image Girl_fondle_breast_right_animation:
    "Girl_hand_white"

    alpha 0.5 xzoom -0.6 yzoom 0.6
    block:
        ease 1 rotate -30 yoffset 30
        ease 1 rotate -10 yoffset 0
        repeat

image Girl_fondle_pussy_animation:
    "Girl_hand_white"

    alpha 0.5 zoom 0.6
    block:
        choice:
            ease 0.75 rotate 210 offset (-5, 5)
            ease 0.5 rotate 195
            ease 0.75 rotate 210
            ease 0.5 rotate 195
        choice:
            ease 0.5 rotate 210 offset (-5, 5)
            ease 1 rotate 195
            pause 0.25
            ease 0.5 rotate 210
            ease 1 rotate 195
            pause 0.25
        choice:
            ease 0.5 rotate 205 offset (-5, 5)
            ease 0.75 rotate 200 offset (-5, 10)
            ease 0.5 rotate 205 offset (-5, 5)
            ease 0.75 rotate 200 offset (-5, 10)
        choice:
            ease 0.3 rotate 205 offset (-5, 5)
            ease 0.3 rotate 200 offset (-5, 15)
            ease 0.3 rotate 205 offset (-5, 5)
            ease 0.3 rotate 200 offset (-5, 15)
        repeat

image Girl_finger_pussy_animation:
    "Girl_fingering_white"

    alpha 0.5 zoom 0.6
    block:
        choice:
            ease 0.75 rotate 210 yoffset 5
            ease 0.5 rotate 195
            ease 0.75 rotate 210
            ease 0.5 rotate 195
        choice:
            ease 0.5 rotate 210 yoffset 5
            ease 1 rotate 195
            pause 0.25
            ease 0.5 rotate 210
            ease 1 rotate 195
            pause 0.25
        choice:
            ease 0.5 rotate 205 yoffset 5
            ease 0.75 rotate 200 yoffset 10
            ease 0.5 rotate 205 yoffset 5
            ease 0.75 rotate 200 yoffset 10
        choice:
            ease 0.75 rotate 205 yoffset 5
            ease 0.75 rotate 200 yoffset 15
            ease 0.75 rotate 205 yoffset 5
            ease 0.75 rotate 200 yoffset 15
        repeat

image Storm_fondle_breast_left_animation:
    "Girl_hand_black"

    alpha 0.5 zoom 0.6
    block:
        ease 1 rotate -40 offset (-20, -10)
        ease 1 rotate -20 offset (0, 0)
        repeat

image Storm_fondle_breast_right_animation:
    "Girl_hand_black"

    alpha 0.5 xzoom -0.6 yzoom 0.6
    block:
        ease 1 rotate -30 yoffset 30
        ease 1 rotate -10 yoffset 0
        repeat

image Storm_fondle_pussy_animation:
    "Girl_hand_black"

    alpha 0.5 zoom 0.6
    block:
        choice:
            ease 0.75 rotate 210 offset (-5, 5)
            ease 0.5 rotate 195
            ease 0.75 rotate 210
            ease 0.5 rotate 195
        choice:
            ease 0.5 rotate 210 offset (-5, 5)
            ease 1 rotate 195
            pause 0.25
            ease 0.5 rotate 210
            ease 1 rotate 195
            pause 0.25
        choice:
            ease 0.5 rotate 205 offset (-5, 5)
            ease 0.75 rotate 200 offset (-5, 10)
            ease 0.5 rotate 205 offset (-5, 5)
            ease 0.75 rotate 200 offset (-5, 10)
        choice:
            ease 0.3 rotate 205 offset (-5, 5)
            ease 0.3 rotate 200 offset (-5, 15)
            ease 0.3 rotate 205 offset (-5, 5)
            ease 0.3 rotate 200 offset (-5, 15)
        repeat

image Storm_finger_pussy_animation:
    "Girl_fingering_black"

    alpha 0.5 zoom 0.6
    block:
        choice:
            ease 0.75 rotate 210 yoffset 5
            ease 0.5 rotate 195
            ease 0.75 rotate 210
            ease 0.5 rotate 195
        choice:
            ease 0.5 rotate 210 yoffset 5
            ease 1 rotate 195
            pause 0.25
            ease 0.5 rotate 210
            ease 1 rotate 195
            pause 0.25
        choice:
            ease 0.5 rotate 205 yoffset 5
            ease 0.75 rotate 200 yoffset 10
            ease 0.5 rotate 205 yoffset 5
            ease 0.75 rotate 200 yoffset 10
        choice:
            ease 0.75 rotate 205 yoffset 5
            ease 0.75 rotate 200 yoffset 15
            ease 0.75 rotate 205 yoffset 5
            ease 0.75 rotate 200 yoffset 15
        repeat
