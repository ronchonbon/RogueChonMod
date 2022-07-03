transform sprite_location(x_position = stage_right, y_position = 0):
    pos (x_position, y_position)

transform silhouette:
    matrixcolor TintMatrix(Color(rgb = (0.3, 0.4, 0.4)))*OpacityMatrix(0.95)*BrightnessMatrix(-0.9)

transform morning:
    matrixcolor TintMatrix(Color(rgb = (1.0, 0.95, 0.9)))*BrightnessMatrix(0.02)

transform daylight:
    matrixcolor TintMatrix(Color(rgb = (1.0, 1.0, 1.0)))*BrightnessMatrix(0.02)

transform sunset:
    matrixcolor TintMatrix(Color(rgb = (1.0, 0.8, 0.65)))*BrightnessMatrix(0.01)

transform moonlight:
    matrixcolor TintMatrix(Color(rgb = (0.5, 0.6, 1.0)))*BrightnessMatrix(0.0)

transform indoors:
    matrixcolor TintMatrix(Color(rgb = (1.0, 1.0, 1.0)))*BrightnessMatrix(0.0)

transform lights_off:
    matrixcolor TintMatrix(Color(rgb = (0.45, 0.45, 0.65)))*BrightnessMatrix(-0.07)

transform candlelit:
    matrixcolor TintMatrix(Color(rgb = (1.0, 0.95, 0.95)))*BrightnessMatrix(-0.1)

transform theater:
    matrixcolor TintMatrix(Color(rgb = (0.45, 0.45, 0.65)))*BrightnessMatrix(-0.05)

transform reset_zoom:
    ease 0.75 offset (0, 0) xzoom 1.0 yzoom 1.0 zoom 1.0

transform reset_zoom_instantly:
    offset (0, 0) xzoom 1.0 yzoom 1.0 zoom 1.0

transform null:
    alpha 1.0

transform smooch_animation:
    ease 0.6 ypos 0.0 zoom 2.0
    pause 1.0
    ease 0.6 ypos 0.0 zoom 1.0

transform kiss_launch_animation:
    ease 0.75 ypos 0.0 zoom 2.0

transform breasts_launch_animation:
    ease 0.75 ypos -0.2 zoom 2.0

transform middle_launch_animation:
    ease 0.75 ypos -0.3 zoom 1.5

transform pussy_launch_animation:
    ease 0.75 ypos -0.4 zoom 2.0

transform show_handjob_animation:
    ease 0.75 ypos 0.1 zoom 2.0

transform show_titjob_animation:
    ease 0.5 ypos 0.05 zoom 2.0

transform show_blowjob_animation:
    ease 0.5 ypos 0.1 zoom 2.0

transform close_launch_animation(x_zoom):
    ease 0.75 xzoom x_zoom yzoom 1.3

transform teaching:
    pos (0.4, 0.15) zoom 0.4

transform dining:
    ypos 0.15 zoom 1.15

transform dancing(x_position):
    subpixel True
    pos (x_position, 0.05)
    choice:
        parallel:
            ease 2.5 xoffset -40
            ease 2.5 xoffset 0
        parallel:
            easeout 1.0 yoffset 30
            linear 0.5 yoffset 40
            easein 1.0 yoffset 0
            easeout 1.0 yoffset 40
            linear 0.5 yoffset 50
            easein 1.0 yoffset 0
    choice:
        parallel:
            ease 2.5 xoffset 40
            ease 2.5 xoffset 0
        parallel:
            easeout 1.0 yoffset 30
            linear 0.5 yoffset 40
            easein 1.0 yoffset 0
            easeout 1.0 yoffset 40
            linear 0.5 yoffset 50
            easein 1.0 yoffset 0
    choice (0.3):
        parallel:
            ease 2.5 xoffset -30
            ease 2.5 xoffset 0
        parallel:
            ease 1.5 yoffset 150
            ease 3.5 yoffset 0
    repeat

transform swimming(x_position):
    subpixel True
    pos (x_position, 0.2) zoom 0.8
    choice:
        yoffset 0
    choice:
        pause 0.3
    choice:
        pause 0.5
    block:
        ease 1 yoffset 10
        ease 1.5 yoffset 0
        repeat

transform vampire:
    subpixel True
    ease 0.1 offset (100, 50) zoom 2.5
    block:
        ease 1 yoffset 100
        pause .2
        ease 1 yoffset 50
        repeat

label show_Girl(Girl, x_position = None, y_position = None, sprite_layer = None, color_transform = None, animation_transform = None, transition = None):
    $ renpy.start_predict("images/" + Girl.tag + "_standing/*.*")

    if Girl == RogueX:
        $ renpy.start_predict("images/" + Girl.tag + "_blowjob/*.*")
    elif Girl == MystiqueX:
        $ renpy.start_predict("images/Raven_standing/*.*")

    if x_position:
        $ Girl.sprite_location = x_position

    if not y_position:
        $ y_position = 0

    if sprite_layer:
        $ Girl.sprite_layer = sprite_layer

    if color_transform and animation_transform and transition:
        if Girl == RogueX:
            show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform with transition
        elif Girl == KittyX:
            show Kitty_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform with transition
        elif Girl == EmmaX:
            if Girl.diamond:
                show Emma_sprite standing diamond zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform with transition
            else:
                show Emma_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform with transition
        elif Girl == LauraX:
            show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform with transition
        elif Girl == JeanX:
            show Jean_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform with transition
        elif Girl == StormX:
            show Storm_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform with transition
        elif Girl == JubesX:
            show Jubes_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform with transition
        elif Girl == MystiqueX:
            if Girl.disguise:
                show expression "Mystique_sprite standing " + Girl.disguise zorder Girl.sprite_layer as Mystique_sprite at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform with transition
            else:
                show Mystique_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform with transition
    elif color_transform and animation_transform:
        if Girl == RogueX:
            show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform
        elif Girl == KittyX:
            show Kitty_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform
        elif Girl == EmmaX:
            if Girl.diamond:
                show Emma_sprite standing diamond zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform
            else:
                show Emma_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform
        elif Girl == LauraX:
            show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform
        elif Girl == JeanX:
            show Jean_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform
        elif Girl == StormX:
            show Storm_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform
        elif Girl == JubesX:
            show Jubes_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform
        elif Girl == MystiqueX:
            if Girl.disguise:
                show expression "Mystique_sprite standing " + Girl.disguise zorder Girl.sprite_layer as Mystique_sprite at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform
            else:
                show Mystique_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform
    elif color_transform and transition:
        if Girl == RogueX:
            show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform with transition
        elif Girl == KittyX:
            show Kitty_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform with transition
        elif Girl == EmmaX:
            if Girl.diamond:
                show Emma_sprite standing diamond zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform with transition
            else:
                show Emma_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform with transition
        elif Girl == LauraX:
            show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform with transition
        elif Girl == JeanX:
            show Jean_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform with transition
        elif Girl == StormX:
            show Storm_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform with transition
        elif Girl == JubesX:
            show Jubes_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform with transition
        elif Girl == MystiqueX:
            if Girl.disguise:
                show expression "Mystique_sprite standing " + Girl.disguise zorder Girl.sprite_layer as Mystique_sprite at sprite_location(Girl.sprite_location, y_position), color_transform with transition
            else:
                show Mystique_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform with transition
    elif animation_transform and transition:
        if Girl == RogueX:
            show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform with transition
        elif Girl == KittyX:
            show Kitty_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform with transition
        elif Girl == EmmaX:
            if Girl.diamond:
                show Emma_sprite standing diamond zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform with transition
            else:
                show Emma_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform with transition
        elif Girl == LauraX:
            show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform with transition
        elif Girl == JeanX:
            show Jean_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform with transition
        elif Girl == StormX:
            show Storm_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform with transition
        elif Girl == JubesX:
            show Jubes_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform with transition
        elif Girl == MystiqueX:
            if Girl.disguise:
                show expression "Mystique_sprite standing " + Girl.disguise zorder Girl.sprite_layer as Mystique_sprite at sprite_location(Girl.sprite_location, y_position), animation_transform with transition
            else:
                show Mystique_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform with transition
    elif color_transform:
        if Girl == RogueX:
            show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform
        elif Girl == KittyX:
            show Kitty_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform
        elif Girl == EmmaX:
            if Girl.diamond:
                show Emma_sprite standing diamond zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform
            else:
                show Emma_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform
        elif Girl == LauraX:
            show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform
        elif Girl == JeanX:
            show Jean_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform
        elif Girl == StormX:
            show Storm_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform
        elif Girl == JubesX:
            show Jubes_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform
        elif Girl == MystiqueX:
            if Girl.disguise:
                show expression "Mystique_sprite standing " + Girl.disguise zorder Girl.sprite_layer as Mystique_sprite at sprite_location(Girl.sprite_location, y_position), color_transform
            else:
                show Mystique_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform
    elif animation_transform:
        if Girl == RogueX:
            show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform
        elif Girl == KittyX:
            show Kitty_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform
        elif Girl == EmmaX:
            if Girl.diamond:
                show Emma_sprite standing diamond zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform
            else:
                show Emma_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform
        elif Girl == LauraX:
            show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform
        elif Girl == JeanX:
            show Jean_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform
        elif Girl == StormX:
            show Storm_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform
        elif Girl == JubesX:
            show Jubes_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform
        elif Girl == MystiqueX:
            if Girl.disguise:
                show expression "Mystique_sprite standing " + Girl.disguise zorder Girl.sprite_layer as Mystique_sprite at sprite_location(Girl.sprite_location, y_position), animation_transform
            else:
                show Mystique_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform
    elif transition:
        if Girl == RogueX:
            show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null with transition
        elif Girl == KittyX:
            show Kitty_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null with transition
        elif Girl == EmmaX:
            if Girl.diamond:
                show Emma_sprite standing diamond zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null with transition
            else:
                show Emma_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null with transition
        elif Girl == LauraX:
            show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null with transition
        elif Girl == JeanX:
            show Jean_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null with transition
        elif Girl == StormX:
            show Storm_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null with transition
        elif Girl == JubesX:
            show Jubes_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null with transition
        elif Girl == MystiqueX:
            if Girl.disguise:
                show expression "Mystique_sprite standing " + Girl.disguise zorder Girl.sprite_layer as Mystique_sprite at sprite_location(Girl.sprite_location, y_position), null with transition
            else:
                show Mystique_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null with transition
    else:
        if Girl == RogueX:
            show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null
        elif Girl == KittyX:
            show Kitty_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null
        elif Girl == EmmaX:
            if Girl.diamond:
                show Emma_sprite standing diamond zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null
            else:
                show Emma_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null
        elif Girl == LauraX:
            show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null
        elif Girl == JeanX:
            show Jean_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null
        elif Girl == StormX:
            show Storm_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null
        elif Girl == JubesX:
            show Jubes_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null
        elif Girl == MystiqueX:
            if Girl.disguise:
                show expression "Mystique_sprite standing " + Girl.disguise zorder Girl.sprite_layer as Mystique_sprite at sprite_location(Girl.sprite_location, y_position), null
            else:
                show Mystique_sprite standing normal zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null

    return

label hide_Girl(Girl, transition = None):
    if transition is None:
        call get_transition
        $ transition = _return[1]

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

    $ renpy.stop_predict("images/" + Girl.tag + "_standing/*.*")
    $ renpy.stop_predict("images/" + Girl.tag + "_handjob/*.*")
    $ renpy.stop_predict("images/" + Girl.tag + "_titjob/*.*")
    $ renpy.stop_predict("images/" + Girl.tag + "_footjob/*.*")
    $ renpy.stop_predict("images/" + Girl.tag + "_blowjob/*.*")
    $ renpy.stop_predict("images/" + Girl.tag + "_sex/*.*")
    $ renpy.stop_predict("images/" + Girl.tag + "_doggy/*.*")

    return

label hide_all(fade = False):
    if fade:
        show black_screen onlayer black

        pause 0.4

    $ temp_Girls = all_Girls[:]

    while temp_Girls:
        if temp_Girls not in Player.Party and renpy.showing(temp_Girls[0].tag + "_sprite"):
            call hide_Girl(temp_Girls[0], transition = False)

        $ temp_Girls.remove(temp_Girls[0])

    if renpy.showing("Xavier_sprite"):
        hide Xavier_sprite

    if fade:
        hide black_screen onlayer black

    return

label get_color_transform:
    if Player.location in ["bg_campus", "bg_pool", "bg_storm"] and time_index == 0:
        $ color_transform = morning
    elif Player.location in ["bg_campus", "bg_pool", "bg_storm"] and time_index == 1:
        $ color_transform = daylight
    elif Player.location in ["bg_campus", "bg_pool", "bg_storm"] and time_index == 2:
        $ color_transform = sunset
    elif Player.location in ["bg_campus", "bg_pool", "bg_storm"] and time_index > 2:
        $ color_transform = moonlight
    elif (Player.location in bedrooms or Player.location in ["bg_classroom", "bg_dangerroom"]) and time_index == 4:
        $ color_transform = lights_off
    elif Player.location == "bg_restaurant":
        $ color_transform = candlelit
    elif Player.location == "bg_movies":
        $ color_transform = theater
    else:
        $ color_transform = indoors

    return color_transform

label get_transition:
    if Player.location in ["bg_dangerroom", "bg_jean", "bg_jubes", "bg_laura", "bg_mall", "bg_player", "bg_pool", "bg_shop", "bg_shower", "bg_storm"]:
        $ entrance_transition = easeinleft
        $ exit_transition = easeoutleft
    elif Player.location in ["bg_classroom", "bg_movies", "bg_restaurant", "bg_study"]:
        $ entrance_transition = easeinright
        $ exit_transition = easeoutright
    else:
        if renpy.random.randint(0, 1):
            $ entrance_transition = easeinleft
            $ exit_transition = easeoutleft
        else:
            $ entrance_transition = easeinright
            $ exit_transition = easeoutright

    return entrance_transition, exit_transition

label add_Girls(Girls, fade = False, static = False):
    if Girls in all_Girls:
        $ Girls = [Girls]

    python:
        for G in Girls:
            G.location = Player.location

            if G not in Present:
                Present.append(G)

    call set_the_scene(fade = fade, static = static)
    call shift_focus(Girls[0])

    return

label remove_Girl(Girl, transition = None):
    if Girl in Player.Party:
        $ Player.Party.remove(Girl)

    if Girl in Present:
        $ Present.remove(Girl)

    if Girl in Nearby:
        $ Nearby.remove(Girl)

    if Partner == Girl:
        $ Partner = None

    if Player.location in ["bg_campus", "bg_classroom", "bg_dangerroom", "bg_pool"]:
        $ Nearby.append(Girl)

        $ Girl.location = "nearby"
    elif Player.location == Girl.home:
        if Girl == JubesX and JubesX.addiction >= 60:
            $ Girl.location = "bg_shower"
        else:
            $ Girl.location = "bg_campus"
    else:
        $ Girl.location = Girl.home

    if door_locked:
        "[Girl.name] unlocks the door on her way out."

        $ door_locked = False

    call hide_Girl(Girl, transition = transition)

    return

label remove_all:
    call check_who_is_present

    if Present:
        $ temp_Girls = Present[:]

        while temp_Girls:
            if temp_Girls[0] not in Player.Party:
                call remove_Girl(temp_Girls[0])

            $ temp_Girls.remove(temp_Girls[0])

    return

label shift_view(Girl, view):
    if view == "menu":
        menu:
            "Full body":
                call show_full_body(Girl)
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
            call show_full_body(Girl)
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

label show_full_body(Girl):
    $ Girl.pose = "full"

    call show_Girl(Girl, animation_transform = reset_zoom)

    return

label smooch(Girl):
    $ Girl.change_face("kiss")

    call show_Girl(Girl, animation_transform = smooch_animation)

    pause 1.0

    $ Girl.change_face("sexy")

    return

label kiss_launch(Girl):
    $ Girl.pose = "kiss"
    $ Girl.change_face("kiss")

    call show_Girl(Girl, animation_transform = kiss_launch_animation)

    return

label breasts_launch(Girl):
    $ Girl.pose = "breasts"

    call show_Girl(Girl, animation_transform = breasts_launch_animation)

    return

label middle_launch(Girl):
    $ Girl.pose = "middle"

    call show_Girl(Girl, animation_transform = middle_launch_animation)

    return

label pussy_launch(Girl):
    $ Girl.pose = "pussy"

    call show_Girl(Girl, animation_transform = pussy_launch_animation)

    return

label show_handjob(Girl, orgasm = False):
    if renpy.showing(Girl.tag + "_sprite handjob"):
        return

    $ action_speed = 0

    call show_Girl(Girl, animation_transform = show_handjob_animation)

    if taboo:
        if len(Present) >= 2:
            if Present[0] != Girl:
                "[Girl.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != Girl:
                "[Girl.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[Girl.name] looks around to see if anyone can see her."

    if not orgasm:
        if not Girl.Action_counter["handjob"] and Girl.Clothes["gloves"]:
            "As you pull out your cock, [Girl.name] pulls off her gloves, and hesitantly reaches for it. She starts to roughly stroke on it."
        else:
            "She then leans over and grabs your cock."
    else:
        "[Girl.name] bends down and grabs your cock."

    $ Girl.take_off("gloves")
    $ Girl.arm_pose = 1

    $ renpy.start_predict("images/" + Girl.tag + "_handjob/*.*")

    call get_color_transform
    $ color_transform = _return

    if Girl == RogueX:
        show Rogue_sprite handjob zorder 150 at sprite_location(stage_center), color_transform:
            zoom 1.0
    elif Girl == KittyX:
        show Kitty_sprite handjob zorder 150 at sprite_location(stage_center), color_transform:
            zoom 1.0
    elif Girl == EmmaX:
        show Emma_sprite handjob zorder 150 at sprite_location(stage_center), color_transform:
            zoom 1.0
    elif Girl == LauraX:
        show Laura_sprite handjob zorder 150 at sprite_location(stage_center), color_transform:
            zoom 1.0
    elif Girl == JeanX:
        show Jean_sprite handjob zorder 150 at sprite_location(stage_center), color_transform:
            zoom 1.0
    elif Girl == StormX:
        show Storm_sprite handjob zorder 150 at sprite_location(stage_center), color_transform:
            zoom 1.0
    elif Girl == JubesX:
        show Jubes_sprite handjob zorder 150 at sprite_location(stage_center), color_transform:
            zoom 1.0

    return

label show_titjob(Girl, orgasm = False):
    if renpy.showing(Girl.tag + "_sprite titjob"):
        return

    $ action_speed = 0

    call show_Girl(Girl, animation_transform = show_titjob_animation)

    if taboo:
        if len(Present) >= 2:
            if Present[0] != Girl:
                "[Girl.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != Girl:
                "[Girl.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[Girl.name] looks around to see if anyone can see her."

    if Girl.Clothes["bra"] and Girl.Clothes["top"]:
        "She throws off her [Girl.Clothes[top]] and her [Girl.Clothes[bra].name]."
    elif Girl.Clothes["top"]:
        "She throws off her [Girl.Clothes[top].name], baring her breasts underneath."
    elif Girl.Clothes["bra"]:
        "She tugs off her [Girl.Clothes[bra].name] and throws it aside."

    $ Girl.take_off("top")
    $ Girl.take_off("bra")
    $ Girl.take_off("gloves")

    call expression Girl.tag + "_First_Topless"

    if not orgasm:
        if not Girl.Action_counter["titjob"] and "cockout" not in Player.recent_history:
            if not Girl.Clothes["bra"] and not Girl.Clothes["top"]:
                "As you pull out your cock, [Girl.name] hesitantly places it between her breasts and starts to rub them up and down the shaft."
            elif Girl.Clothes["bra"] and not Girl.Clothes["top"]:
                "As you pull out your cock, [Girl.name] hesitantly places it under her [Girl.Clothes[bra].name], between her breasts, and starts to rub them up and down the shaft."
            elif Girl.Clothes["bra"] and Girl.Clothes["top"]:
                "As you pull out your cock, [Girl.name] hesitantly places it under her [Girl.Clothes[top].name], between her breasts, and starts to rub them up and down the shaft."
            else:
                "As you pull out your cock, [Girl.name] hesitantly places it under her clothes, between her breasts, and starts to rub them up and down the shaft."
        elif "cockout" not in Player.recent_history:
            if not Girl.Clothes["bra"] and not Girl.Clothes["top"]:
                "As you pull out your cock, [Girl.name] places it between her breasts and starts to rub them up and down the shaft."
            elif Girl.Clothes["bra"] and not Girl.Clothes["top"]:
                "As you pull out your cock, [Girl.name] places it under her [Girl.Clothes[bra].name], between her breasts, and starts to rub them up and down the shaft."
            elif Girl.Clothes["bra"] and Girl.Clothes["top"]:
                "As you pull out your cock, [Girl.name] places it under her [Girl.Clothes[top].name], between her breasts, and starts to rub them up and down the shaft."
            else:
                "As you pull out your cock, [Girl.name] places it under her clothes, between her breasts and starts to rub them up and down the shaft."
    else:
        "[Girl.name] wraps her tits around your cock."

    $ renpy.start_predict("images/" + Girl.tag + "_titjob/*.*")

    call get_color_transform
    $ color_transform = _return

    if Girl == RogueX:
        show Rogue_sprite titjob zorder 150 at sprite_location(stage_center), color_transform:
            zoom 1.0
    elif Girl == KittyX:
        show Kitty_sprite titjob zorder 150 at sprite_location(stage_center), color_transform:
            zoom 1.0
    elif Girl == EmmaX:
        show Emma_sprite titjob zorder 150 at sprite_location(stage_center), color_transform:
            zoom 1.0
    elif Girl == LauraX:
        show Laura_sprite titjob zorder 150 at sprite_location(stage_center), color_transform:
            zoom 1.0
    elif Girl == JeanX:
        show Jean_sprite titjob zorder 150 at sprite_location(stage_center), color_transform:
            zoom 1.0
    elif Girl == StormX:
        show Storm_sprite titjob zorder 150 at sprite_location(stage_center), color_transform:
            zoom 1.0
    elif Girl == JubesX:
        show Jubes_sprite titjob zorder 150 at sprite_location(stage_center), color_transform:
            zoom 1.0

    return

label show_blowjob(Girl, orgasm = False):
    if renpy.showing(Girl.tag + "_sprite blowjob"):
        return

    $ action_speed = 0

    call show_Girl(Girl, animation_transform = show_blowjob_animation)

    if taboo:
        if len(Present) >= 2:
            if Present[0] != Girl:
                "[Girl.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != Girl:
                "[Girl.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[Girl.name] looks around to see if anyone can see her."

    if not orgasm:
        if not Girl.Action_counter["blowjob"] and "cockout" not in Player.recent_history:
            "[Girl.name] hesitantly pulls down your pants and touches her mouth to your cock."
    else:
        "[Girl.name] bends down and begins to suck on your cock."

    $ renpy.start_predict("images/" + Girl.tag + "_blowjob/*.*")

    call get_color_transform
    $ color_transform = _return

    if Girl == RogueX:
        show Rogue_sprite blowjob zorder 150 at sprite_location(stage_center), color_transform:
            zoom 1.0
    elif Girl == KittyX:
        show Kitty_sprite blowjob zorder 150 at sprite_location(stage_center), color_transform:
            zoom 1.0
    elif Girl == EmmaX:
        show Emma_sprite blowjob zorder 150 at sprite_location(stage_center), color_transform:
            zoom 1.0
    elif Girl == LauraX:
        show Laura_sprite blowjob zorder 150 at sprite_location(stage_center), color_transform:
            zoom 1.0
    elif Girl == JeanX:
        show Jean_sprite blowjob zorder 150 at sprite_location(stage_center), color_transform:
            zoom 1.0
    elif Girl == StormX:
        show Storm_sprite blowjob zorder 150 at sprite_location(stage_center), color_transform:
            zoom 1.0
    elif Girl == JubesX:
        show Jubes_sprite blowjob zorder 150 at sprite_location(stage_center), color_transform:
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

    $ renpy.start_predict("images/" + Girl.tag + "_sex/*.*")

    call get_color_transform
    $ color_transform = _return

    if Girl == RogueX:
        show Rogue_sprite sex zorder 150 at sprite_location(stage_center), color_transform
    elif Girl == KittyX:
        show Kitty_sprite sex zorder 150 at sprite_location(stage_center), color_transform
    elif Girl == EmmaX:
        show Emma_sprite sex zorder 150 at sprite_location(stage_center), color_transform
    elif Girl == LauraX:
        show Laura_sprite sex zorder 150 at sprite_location(stage_center), color_transform
    elif Girl == JeanX:
        show Jean_sprite sex zorder 150 at sprite_location(stage_center), color_transform
    elif Girl == StormX:
        show Storm_sprite sex zorder 150 at sprite_location(stage_center), color_transform
    elif Girl == JubesX:
        show Jubes_sprite sex zorder 150 at sprite_location(stage_center), color_transform

    return

label show_doggy(Girl):
    if renpy.showing(Girl.tag + "_sprite doggy"):
        return

    $ action_speed = 0

    $ renpy.start_predict("images/" + Girl.tag + "_doggy/*.*")

    call get_color_transform
    $ color_transform = _return

    if Girl == RogueX:
        show Rogue_sprite doggy zorder 150 at sprite_location(stage_center), color_transform
    elif Girl == KittyX:
        show Kitty_sprite doggy zorder 150 at sprite_location(stage_center), color_transform
    elif Girl == EmmaX:
        show Emma_sprite doggy zorder 150 at sprite_location(stage_center), color_transform
    elif Girl == LauraX:
        show Laura_sprite doggy zorder 150 at sprite_location(stage_center), color_transform
    elif Girl == JeanX:
        show Jean_sprite doggy zorder 150 at sprite_location(stage_center), color_transform
    elif Girl == StormX:
        show Storm_sprite doggy zorder 150 at sprite_location(stage_center), color_transform
    elif Girl == JubesX:
        show Jubes_sprite doggy zorder 150 at sprite_location(stage_center), color_transform

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
                $ x_position = 0.44
            elif temp_Girls[0] == RogueX:
                $ x_position = 0.54
            else:
                $ x_position = 0.5
        elif GirlB == temp_Girls[0]:
            if temp_Girls[0] == EmmaX or LauraX:
                $ x_position = 0.68
            else:
                $ x_position = 0.7

        call show_Girl(temp_Girls[0], x_position = x_position, animation_transform = close_launch_animation(1.3))

        $ temp_Girls.remove(temp_Girls[0])

    return

label lesbian_launch(Girl):
    $ temp_Girls = [Girl, Partner]

    while temp_Girls:
        if "unseen" in temp_Girls[0].recent_history:
            $ temp_Girls[0].eyes = "closed"
        elif Girl == temp_Girls[0]:
            if Girl == RogueX:
                $ temp_Girls[0].eyes = "side"
            elif Girl == EmmaX:
                $ temp_Girls[0].eyes = "squint"
            else:
                $ temp_Girls[0].eyes = "leftside"
        else:
            $ temp_Girls[0].eyes = "side"

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
        else:
            if temp_Girls[0] == EmmaX or LauraX:
                $ x_position = 700
            else:
                $ x_position = 715

        call show_Girl(temp_Girls[0], x_position = x_position, color_transform = close_launch_animation(1.3))

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

image Girl_hand_blue:
    "images/misc/Girl_hand_blue.png"

    anchor (0.5, 0.5)

image Girl_fingering_blue:
    "images/misc/Girl_fingering_blue.png"

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

image Mystique_fondle_breast_left_animation:
    "Girl_hand_blue"

    alpha 0.5 zoom 0.6
    block:
        ease 1 rotate -40 offset (-20, -10)
        ease 1 rotate -20 offset (0, 0)
        repeat

image Mystique_fondle_breast_right_animation:
    "Girl_hand_blue"

    alpha 0.5 xzoom -0.6 yzoom 0.6
    block:
        ease 1 rotate -30 yoffset 30
        ease 1 rotate -10 yoffset 0
        repeat

image Mystique_fondle_pussy_animation:
    "Girl_hand_blue"

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

image Mystique_finger_pussy_animation:
    "Girl_fingering_blue"

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
