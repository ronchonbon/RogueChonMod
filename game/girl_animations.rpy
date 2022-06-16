label reset_position(Girl):
    $ Girl.pose = "full"

    if Girl.location != bg_current:
        call hide_girl(Girl)

        return

    if Girl == RogueX:
        show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location):
    elif Girl == KittyX:
        show Kitty_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location):
    elif Girl == EmmaX:
        show Emma_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location):
    elif Girl == LauraX:
        show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location):
    elif Girl == JeanX:
        show Jean_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location):
    elif Girl == StormX:
        show Storm_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location):
    elif Girl == JubesX:
        show Jubes_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location):

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
            "Rear view" if Girl in [RogueX, KittyX, EmmaX, LauraX, JeanX]:
                $ Girl.pose = "doggy"

                call show_sex(Girl, None)
            "On top of you" if Girl in [EmmaX, JeanX, StormX]:
                $ Girl.pose = "sex"

                call show_sex(Girl, None)
            "Laying down" if Girl in [RogueX, KittyX, LauraX]:
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

            $ temp_Girls[0].sprite_layer = 100

            $ x_zoom = -1.3
        elif GirlB == temp_Girls[0]:
            if temp_Girls[0] == EmmaX or LauraX:
                $ x_position = 700
            else:
                $ x_position = 715

            $ temp_Girls[0].sprite_layer = 75

            $ x_zoom = 1.3

        # if temp_Girls[0] == RogueX:
        #     show Rogue_sprite standing zorder temp_Girls[0].sprite_layer at sprite_location(x_position, 100):
        #         xzoom x_zoom yzoom 1.3
        # elif temp_Girls[0] == KittyX:
        #     show Kitty_sprite standing zorder temp_Girls[0].sprite_layer at sprite_location(x_position, 100):
        #         xzoom x_zoom yzoom 1.3
        # elif temp_Girls[0] == EmmaX:
        #     show Emma_sprite standing zorder temp_Girls[0].sprite_layer at sprite_location(x_position, 100):
        #         xzoom x_zoom yzoom 1.3
        # elif temp_Girls[0] == LauraX:
        #     show Laura_sprite standing zorder temp_Girls[0].sprite_layer at sprite_location(x_position, 100):
        #         xzoom x_zoom yzoom 1.3
        # elif temp_Girls[0] == JeanX:
        #     show Jean_sprite standing zorder temp_Girls[0].sprite_layer at sprite_location(x_position, 100):
        #         xzoom x_zoom yzoom 1.3
        # elif temp_Girls[0] == StormX:
        #     show Storm_sprite standing zorder temp_Girls[0].sprite_layer at sprite_location(x_position, 100):
        #         xzoom x_zoom yzoom 1.3
        # elif temp_Girls[0] == JubesX:
        #     show Jubes_sprite standing zorder temp_Girls[0].sprite_layer at sprite_location(x_position, 100):
        #         xzoom x_zoom yzoom 1.3

        $ temp_Girls.remove(temp_Girls[0])

    return

transform smooch_animation(location):
    ease 0.5 pos (location, 0.1) xzoom 2.0 yzoom 2.0
    pause 1
    ease 0.5 pos (location, 0.0) xzoom 1.0 yzoom 1.0

label smooch(Girl):
    $ Girl.change_face("_kiss")

    # if Girl == RogueX:
    #     show Rogue_sprite standing zorder Girl.sprite_layer at smooch_animation(Girl.sprite_location)
    # elif Girl == KittyX:
    #     show Kitty_sprite standing zorder Girl.sprite_layer at smooch_animation(Girl.sprite_location)
    # elif Girl == EmmaX:
    #     show Emma_sprite standing zorder Girl.sprite_layer at smooch_animation(Girl.sprite_location)
    # elif Girl == LauraX:
    #     show Laura_sprite standing zorder Girl.sprite_layer at smooch_animation(Girl.sprite_location)
    # elif Girl == JeanX:
    #     show Jean_sprite standing zorder Girl.sprite_layer at smooch_animation(Girl.sprite_location)
    # elif Girl == StormX:
    #     show Storm_sprite standing zorder Girl.sprite_layer at smooch_animation(Girl.sprite_location)
    # elif Girl == JubesX:
    #     show Jubes_sprite standing zorder Girl.sprite_layer at smooch_animation(Girl.sprite_location)

    pause 1

    $ Girl.change_face("_sexy")

    return

transform kiss_launch_animation(location):
    ease 0.5 pos (location, 0.1) xzoom 2.0 yzoom 2.0

label kiss_launch(Girl):
    $ Girl.pose = "kiss"

    $ Girl.change_face("_kiss")

    # if Girl == RogueX:
    #     show Rogue_sprite standing zorder Girl.sprite_layer at kiss_launch_animation(Girl.sprite_location)
    # elif Girl == KittyX:
    #     show Kitty_sprite standing zorder Girl.sprite_layer at kiss_launch_animation(Girl.sprite_location)
    # elif Girl == EmmaX:
    #     show Emma_sprite standing zorder Girl.sprite_layer at kiss_launch_animation(Girl.sprite_location)
    # elif Girl == LauraX:
    #     show Laura_sprite standing zorder Girl.sprite_layer at kiss_launch_animation(Girl.sprite_location)
    # elif Girl == JeanX:
    #     show Jean_sprite standing zorder Girl.sprite_layer at kiss_launch_animation(Girl.sprite_location)
    # elif Girl == StormX:
    #     show Storm_sprite standing zorder Girl.sprite_layer at kiss_launch_animation(Girl.sprite_location)
    # elif Girl == JubesX:
    #     show Jubes_sprite standing zorder Girl.sprite_layer at kiss_launch_animation(Girl.sprite_location)

    return

transform breasts_launch_animation(location):
    ease 0.5 pos (location, -0.2) xzoom 2.0 yzoom 2.0

label breasts_launch(Girl):
    $ Girl.pose = "breasts"

    # if Girl == RogueX:
    #     show Rogue_sprite standing zorder Girl.sprite_layer at breasts_launch_animation(Girl.sprite_location)
    # elif Girl == KittyX:
    #     show Kitty_sprite standing zorder Girl.sprite_layer at breasts_launch_animation(Girl.sprite_location)
    # elif Girl == EmmaX:
    #     show Emma_sprite standing zorder Girl.sprite_layer at breasts_launch_animation(Girl.sprite_location)
    # elif Girl == LauraX:
    #     show Laura_sprite standing zorder Girl.sprite_layer at breasts_launch_animation(Girl.sprite_location)
    # elif Girl == JeanX:
    #     show Jean_sprite standing zorder Girl.sprite_layer at breasts_launch_animation(Girl.sprite_location)
    # elif Girl == StormX:
    #     show Storm_sprite standing zorder Girl.sprite_layer at breasts_launch_animation(Girl.sprite_location)
    # elif Girl == JubesX:
    #     show Jubes_sprite standing zorder Girl.sprite_layer at breasts_launch_animation(Girl.sprite_location)

    return

transform middle_launch_animation(location):
    ease 0.5 pos (location, -0.3) xzoom 1.5 yzoom 1.5

label middle_launch(Girl):
    $ Girl.pose = "middle"

    # if Girl == RogueX:
    #     show Rogue_sprite standing zorder Girl.sprite_layer at middle_launch_animation(Girl.sprite_location)
    # elif Girl == KittyX:
    #     show Kitty_sprite standing zorder Girl.sprite_layer at middle_launch_animation(Girl.sprite_location)
    # elif Girl == EmmaX:
    #     show Emma_sprite standing zorder Girl.sprite_layer at middle_launch_animation(Girl.sprite_location)
    # elif Girl == LauraX:
    #     show Laura_sprite standing zorder Girl.sprite_layer at middle_launch_animation(Girl.sprite_location)
    # elif Girl == JeanX:
    #     show Jean_sprite standing zorder Girl.sprite_layer at middle_launch_animation(Girl.sprite_location)
    # elif Girl == StormX:
    #     show Storm_sprite standing zorder Girl.sprite_layer at middle_launch_animation(Girl.sprite_location)
    # elif Girl == JubesX:
    #     show Jubes_sprite standing zorder Girl.sprite_layer at middle_launch_animation(Girl.sprite_location)

    return

transform pussy_launch_animation(location):
    ease 0.5 pos (location, -0.4) xzoom 2.0 yzoom 2.0

label pussy_launch(Girl):
    $ Girl.pose = "pussy"

    # if Girl == RogueX:
    #     show Rogue_sprite standing zorder Girl.sprite_layer at pussy_launch_animation(Girl.sprite_location)
    # elif Girl == KittyX:
    #     show Kitty_sprite standing zorder Girl.sprite_layer at pussy_launch_animation(Girl.sprite_location)
    # elif Girl == EmmaX:
    #     show Emma_sprite standing zorder Girl.sprite_layer at pussy_launch_animation(Girl.sprite_location)
    # elif Girl == LauraX:
    #     show Laura_sprite standing zorder Girl.sprite_layer at pussy_launch_animation(Girl.sprite_location)
    # elif Girl == JeanX:
    #     show Jean_sprite standing zorder Girl.sprite_layer at pussy_launch_animation(Girl.sprite_location)
    # elif Girl == StormX:
    #     show Storm_sprite standing zorder Girl.sprite_layer at pussy_launch_animation(Girl.sprite_location)
    # elif Girl == JubesX:
    #     show Jubes_sprite standing zorder Girl.sprite_layer at pussy_launch_animation(Girl.sprite_location)

    return

transform show_handjob_animation(location):
    ease 0.5 pos (location, 0.1) xzoom 2.0 yzoom 2.0

label show_handjob(Girl, orgasm = False):
    if renpy.showing(Girl.tag + "_sprite handjob"):
        return

    $ action_speed = 0

    # if Girl == RogueX:
    #     show Rogue_sprite standing zorder Girl.sprite_layer at show_handjob_animation(Girl.sprite_location)
    # elif Girl == KittyX:
    #     show Kitty_sprite standing zorder Girl.sprite_layer at show_handjob_animation(Girl.sprite_location)
    # elif Girl == EmmaX:
    #     show Emma_sprite standing zorder Girl.sprite_layer at show_handjob_animation(Girl.sprite_location)
    # elif Girl == LauraX:
    #     show Laura_sprite standing zorder Girl.sprite_layer at show_handjob_animation(Girl.sprite_location)
    # elif Girl == JeanX:
    #     show Jean_sprite standing zorder Girl.sprite_layer at show_handjob_animation(Girl.sprite_location)
    # elif Girl == StormX:
    #     show Storm_sprite standing zorder Girl.sprite_layer at show_handjob_animation(Girl.sprite_location)
    # elif Girl == JubesX:
    #     show Jubes_sprite standing zorder Girl.sprite_layer at show_handjob_animation(Girl.sprite_location)

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
        show Rogue_sprite handjob zorder 150 at sprite_location(stage_center)
    elif Girl == KittyX:
        show Kitty_sprite handjob zorder 150 at sprite_location(stage_center)
    elif Girl == EmmaX:
        show Emma_sprite handjob zorder 150 at sprite_location(stage_center)
    elif Girl == LauraX:
        show Laura_sprite handjob zorder 150 at sprite_location(stage_center)
    elif Girl == JeanX:
        show Jean_sprite handjob zorder 150 at sprite_location(stage_center)
    elif Girl == StormX:
        show Storm_sprite handjob zorder 150 at sprite_location(stage_center)
    elif Girl == JubesX:
        show Jubes_sprite handjob zorder 150 at sprite_location(stage_center)

    return

transform show_titjob_animation(location):
    ease 0.5 pos (location, 0.1) xzoom 2.0 yzoom 2.0

label show_titjob(Girl, orgasm = False):
    if renpy.showing(Girl.tag + "_sprite titjob"):
        return

    $ action_speed = 0

    # if Girl == RogueX:
    #     show Rogue_sprite standing zorder Girl.sprite_layer at show_titjob_animation(Girl.sprite_location)
    # elif Girl == KittyX:
    #     show Kitty_sprite standing zorder Girl.sprite_layer at show_titjob_animation(Girl.sprite_location)
    # elif Girl == EmmaX:
    #     show Emma_sprite standing zorder Girl.sprite_layer at show_titjob_animation(Girl.sprite_location)
    # elif Girl == LauraX:
    #     show Laura_sprite standing zorder Girl.sprite_layer at show_titjob_animation(Girl.sprite_location)
    # elif Girl == JeanX:
    #     show Jean_sprite standing zorder Girl.sprite_layer at show_titjob_animation(Girl.sprite_location)
    # elif Girl == StormX:
    #     show Storm_sprite standing zorder Girl.sprite_layer at show_titjob_animation(Girl.sprite_location)
    # elif Girl == JubesX:
    #     show Jubes_sprite standing zorder Girl.sprite_layer at show_titjob_animation(Girl.sprite_location)

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
        show Rogue_sprite titjob zorder 150 at sprite_location(stage_center)
    elif Girl == KittyX:
        show Kitty_sprite titjob zorder 150 at sprite_location(stage_center)
    elif Girl == EmmaX:
        show Emma_sprite titjob zorder 150 at sprite_location(stage_center)
    elif Girl == LauraX:
        show Laura_sprite titjob zorder 150 at sprite_location(stage_center)
    elif Girl == JeanX:
        show Jean_sprite titjob zorder 150 at sprite_location(stage_center)
    elif Girl == StormX:
        show Storm_sprite titjob zorder 150 at sprite_location(stage_center)
    elif Girl == JubesX:
        show Jubes_sprite titjob zorder 150 at sprite_location(stage_center)

    return

transform show_blowjob_animation(location):
    ease 0.5 pos (location, 0.1) zoom 2.0

label show_blowjob(Girl, orgasm = False):
    if renpy.showing(Girl.tag + "_sprite blowjob"):
        return

    $ action_speed = 0

    # if Girl == RogueX:
    #     show Rogue_sprite standing zorder Girl.sprite_layer at show_blowjob_animation(Girl.sprite_location)
    # elif Girl == KittyX:
    #     show Kitty_sprite standing zorder Girl.sprite_layer at show_blowjob_animation(Girl.sprite_location)
    # elif Girl == EmmaX:
    #     show Emma_sprite standing zorder Girl.sprite_layer at show_blowjob_animation(Girl.sprite_location)
    # elif Girl == LauraX:
    #     show Laura_sprite standing zorder Girl.sprite_layer at show_blowjob_animation(Girl.sprite_location)
    # elif Girl == JeanX:
    #     show Jean_sprite standing zorder Girl.sprite_layer at show_blowjob_animation(Girl.sprite_location)
    # elif Girl == StormX:
    #     show Storm_sprite standing zorder Girl.sprite_layer at show_blowjob_animation(Girl.sprite_location)
    # elif Girl == JubesX:
    #     show Jubes_sprite standing zorder Girl.sprite_layer at show_blowjob_animation(Girl.sprite_location)

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
        show Rogue_sprite blowjob zorder 150 at sprite_location(stage_center)
    elif Girl == KittyX:
        show Kitty_sprite blowjob zorder 150 at sprite_location(stage_center)
    elif Girl == EmmaX:
        show Emma_sprite blowjob zorder 150 at sprite_location(stage_center)
    elif Girl == LauraX:
        show Laura_sprite blowjob zorder 150 at sprite_location(stage_center)
    elif Girl == JeanX:
        show Jean_sprite blowjob zorder 150 at sprite_location(stage_center)
    elif Girl == StormX:
        show Storm_sprite blowjob zorder 150 at sprite_location(stage_center)
    elif Girl == JubesX:
        show Jubes_sprite blowjob zorder 150 at sprite_location(stage_center)

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

            $ temp_Girls[0].sprite_layer = 100

            $ x_zoom = -1.3
        else:
            if temp_Girls[0] == EmmaX or LauraX:
                $ x_position = 700
            else:
                $ x_position = 715

            if temp_Girls[0] == KittyX:
                if RogueX in (Partner,Girl):
                    $ KittyX.sprite_layer = 100
                else:
                    $ KittyX.sprite_layer = 25
            else:
                $ temp_Girls[0].sprite_layer = 75

            $ x_zoom = 1.3

        # if temp_Girls[0] == RogueX:
        #     show Rogue_sprite standing zorder temp_Girls[0].sprite_layer at sprite_location(x_position, 100):
        #         xzoom x_zoom yzoom 1.3
        # elif temp_Girls[0] == KittyX:
        #     show Kitty_sprite standing zorder temp_Girls[0].sprite_layer at sprite_location(x_position, 100):
        #         xzoom x_zoom yzoom 1.3
        # elif temp_Girls[0] == EmmaX:
        #     show Emma_sprite standing zorder temp_Girls[0].sprite_layer at sprite_location(x_position, 100):
        #         xzoom x_zoom yzoom 1.3
        # elif temp_Girls[0] == LauraX:
        #     show Laura_sprite standing zorder temp_Girls[0].sprite_layer at sprite_location(x_position, 100):
        #         xzoom x_zoom yzoom 1.3
        # elif temp_Girls[0] == JeanX:
        #     show Jean_sprite standing zorder temp_Girls[0].sprite_layer at sprite_location(x_position, 100):
        #         xzoom x_zoom yzoom 1.3
        # elif temp_Girls[0] == StormX:
        #     show Storm_sprite standing zorder temp_Girls[0].sprite_layer at sprite_location(x_position, 100):
        #         xzoom x_zoom yzoom 1.3
        # elif temp_Girls[0] == JubesX:
        #     show Jubes_sprite standing zorder temp_Girls[0].sprite_layer at sprite_location(x_position, 100):
        #         xzoom x_zoom yzoom 1.3

        $ temp_Girls.remove(temp_Girls[0])

    return

image Girl_hand:
    "images/UI_GirlHand.png"

    anchor (0.5, 0.5)

image Girl_finger:
    "images/UI_GirlFinger.png"

    anchor (0.5, 0.5)

image Girl_fondle_thigh:
    "Girl_hand"

    alpha 0.5 zoom 0.6
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

image Girl_fondle_breast_left_animation:
    "Girl_hand"

    alpha 0.5 zoom 0.6
    rotate -20
    block:
        ease 1 rotate -40 offset (-20, -10)
        ease 1 rotate -20 offset (0, 0)
        repeat

image Girl_fondle_breast_right_animation:
    "Girl_hand"

    alpha 0.5 xzoom -0.6 yzoom 0.6
    rotate -10
    block:
        ease 1 rotate -30 yoffset 30
        ease 1 rotate -10 yoffset 0
        repeat

image Girl_fondle_pussy_animation:
    "Girl_hand"

    alpha 0.5 zoom 0.6
    rotate 200
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
    "Girl_finger"

    alpha 0.5 zoom 0.6
    rotate 200
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
            ease 0.3 rotate 205 yoffset 5
            ease 0.3 rotate 200 yoffset 15
            ease 0.3 rotate 205 yoffset 5
            ease 0.3 rotate 200 yoffset 15
        repeat
