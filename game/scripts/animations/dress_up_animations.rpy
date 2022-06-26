label remove_jacket(Girl):
    if Girl.jacket_closed:
        $ Girl.jacket_closed = False

        pause 0.2

    $ Girl.jacket_opened = True

    pause 0.2

    $ Girl.outfit["jacket"] = ""
    $ Girl.set_outfit_flags()

    if not renpy.showing('dress_screen'):
        call expression Girl.tag + "_First_Topless"

    return

label add_jacket(Girl, item, set_flags = True):
    $ Girl.jacket_opened = True
    $ Girl.outfit["jacket"] = item

    pause 0.2

    $ Girl.jacket_opened = False

    if set_flags:
        $ Girl.set_outfit_flags()

    return

label change_jacket(Girl, item, redress = True):
    if Girl.outfit["cloak"]:
        $ temp_cloak = Girl.outfit["cloak"]

        $ Girl.outfit["cloak"] = ""

        pause 0.2
    else:
        $ temp_cloak = None

    if Girl.outfit["jacket"]:
        call remove_jacket(Girl)

        pause 0.2

    if item:
        call add_jacket(Girl, item, set_flags = False)

        pause 0.2

    if redress:
        if temp_cloak:
            $ Girl.outfit["cloak"] = temp_cloak

    $ Girl.set_outfit_flags()

    return

label remove_suspenders(Girl):
    $ Girl.suspenders_aside = True

    pause 0.2

    $ Girl.outfit["suspenders"] = ""
    $ Girl.set_outfit_flags()

    if not renpy.showing('dress_screen'):
        call expression Girl.tag + "_First_Topless"

    return

label add_suspenders(Girl, item, set_flags = True):
    $ Girl.suspenders_aside = True
    $ Girl.outfit["suspenders"] = item

    pause 0.2

    $ Girl.suspenders_aside = False

    if set_flags:
        $ Girl.set_outfit_flags()

    return

label remove_top(Girl):
    if Girl.outfit["top"]:
        $ Girl.top_pulled_up = True

    pause 0.2

    $ Girl.outfit["top"] = ""
    $ Girl.set_outfit_flags()

    if not renpy.showing('dress_screen'):
        call expression Girl.tag + "_First_Topless"

    return

label add_top(Girl, item, set_flags = True):
    $ Girl.top_pulled_up = True
    $ Girl.outfit["top"] = item

    pause 0.2

    if Girl.outfit["top"]:
        $ Girl.top_pulled_up = False

    if set_flags:
        $ Girl.set_outfit_flags()

    return

label change_top(Girl, item, redress = True):
    if Girl.outfit["cloak"]:
        $ temp_cloak = Girl.outfit["cloak"]

        $ Girl.outfit["cloak"] = ""

        pause 0.2
    else:
        $ temp_cloak = None

    if Girl.outfit["jacket"]:
        $ temp_jacket = Girl.outfit["jacket"]

        call remove_jacket(Girl)

        pause 0.2
    else:
        $ temp_jacket = None

    if Girl.outfit["suspenders"]:
        $ temp_suspenders = Girl.outfit["suspenders"]

        call remove_suspenders(Girl)

        pause 0.2
    else:
        $ temp_suspenders = None

    if Girl.outfit["belt"]:
        $ temp_belt = Girl.outfit["belt"]

        $ Girl.outfit["belt"] = ""

        pause 0.2
    else:
        $ temp_belt = None

    if Girl.outfit["top"]:
        call remove_top(Girl)

        pause 0.2

    if item:
        call add_top(Girl, item, set_flags = False)

        pause 0.2

    if redress:
        if temp_belt:
            $ Girl.outfit["belt"] = temp_belt

            pause 0.2

        if temp_suspenders:
            call add_suspenders(Girl, temp_suspenders, set_flags = False)

            pause 0.2

        if temp_jacket:
            call add_jacket(Girl, temp_jacket, set_flags = False)

            pause 0.2

        if temp_cloak:
            $ Girl.outfit["cloak"] = temp_cloak

    $ Girl.set_outfit_flags()

    return

label remove_dress(Girl):
    $ Girl.dress_upskirt = True

    pause 0.2

    $ Girl.outfit["dress"] = ""
    $ Girl.set_outfit_flags()

    if not renpy.showing('dress_screen'):
        call expression Girl.tag + "_First_Topless"
        call expression Girl.tag + "_First_Bottomless"

    return

label add_dress(Girl, item, set_flags = True):
    $ Girl.dress_upskirt = True
    $ Girl.outfit["dress"] = item

    pause 0.2

    $ Girl.dress_upskirt = False

    if set_flags:
        $ Girl.set_outfit_flags()

    return

label change_dress(Girl, item, redress = True):
    if Girl.outfit["cloak"]:
        $ temp_cloak = Girl.outfit["cloak"]

        $ Girl.outfit["cloak"] = ""

        pause 0.2
    else:
        $ temp_cloak = None

    if Girl.outfit["jacket"]:
        $ temp_jacket = Girl.outfit["jacket"]

        call remove_jacket(Girl)

        pause 0.2
    else:
        $ temp_jacket = None

    if Girl.outfit["suspenders"]:
        $ temp_suspenders = Girl.outfit["suspenders"]

        call remove_suspenders(Girl)

        pause 0.2
    else:
        $ temp_suspenders = None

    if Girl.outfit["belt"]:
        $ temp_belt = Girl.outfit["belt"]

        $ Girl.outfit["belt"] = ""

        pause 0.2
    else:
        $ temp_belt = None

    if Girl.outfit["top"]:
        $ temp_top = Girl.outfit["top"]

        call remove_top(Girl)

        pause 0.2
    else:
        $ temp_top = None

    if Girl.outfit["dress"]:
        call remove_dress(Girl)

        pause 0.2

    if item:
        call add_dress(Girl, item, set_flags = False)

        pause 0.2

    if redress:
        if temp_top:
            call add_top(Girl, temp_top, set_flags = False)

            pause 0.2

        if temp_belt:
            $ Girl.outfit["belt"] = temp_belt

            pause 0.2

        if temp_suspenders:
            call add_suspenders(Girl, temp_suspenders, set_flags = False)

            pause 0.2

        if temp_jacket:
            call add_jacket(Girl, temp_jacket, set_flags = False)

            pause 0.2

        if temp_cloak:
            $ Girl.outfit["cloak"] = temp_cloak

    $ Girl.set_outfit_flags()

    return

label remove_bodysuit(Girl):
    $ Girl.bodysuit_top_pulled_aside = True
    $ Girl.bodysuit_bottom_pulled_aside = True

    pause 0.2

    $ Girl.outfit["bodysuit"] = ""
    $ Girl.set_outfit_flags()

    if not renpy.showing('dress_screen'):
        call expression Girl.tag + "_First_Topless"
        call expression Girl.tag + "_First_Bottomless"

    return

label add_bodysuit(Girl, item, set_flags = True):
    $ Girl.bodysuit_top_pulled_aside = True
    $ Girl.bodysuit_bottom_pulled_aside = True
    $ Girl.outfit["bodysuit"] = item

    pause 0.2

    $ Girl.bodysuit_top_pulled_aside = False
    $ Girl.bodysuit_bottom_pulled_aside = False

    if set_flags:
        $ Girl.set_outfit_flags()

    return

label change_bodysuit(Girl, item, redress = True):
    if Girl.outfit["cloak"]:
        $ temp_cloak = Girl.outfit["cloak"]

        $ Girl.outfit["cloak"] = ""

        pause 0.2
    else:
        $ temp_cloak = None

    if Girl.outfit["jacket"]:
        $ temp_jacket = Girl.outfit["jacket"]

        call remove_jacket(Girl)

        pause 0.2
    else:
        $ temp_jacket = None

    if Girl.outfit["suspenders"]:
        $ temp_suspenders = Girl.outfit["suspenders"]

        call remove_suspenders(Girl)

        pause 0.2
    else:
        $ temp_suspenders = None

    if Girl.outfit["belt"]:
        $ temp_belt = Girl.outfit["belt"]

        $ Girl.outfit["belt"] = ""

        pause 0.2
    else:
        $ temp_belt = None

    if Girl.outfit["top"]:
        $ temp_top = Girl.outfit["top"]

        call remove_top(Girl)

        pause 0.2
    else:
        $ temp_top = None

    if Girl.outfit["boots"]:
        $ temp_boots = Girl.outfit["boots"]

        $ Girl.outfit["boots"] = ""

        pause 0.2
    else:
        $ temp_boots = None

    if Girl.outfit["dress"]:
        $ temp_dress = Girl.outfit["dress"]

        call remove_dress(Girl)

        pause 0.2
    else:
        $ temp_dress = None

    if Girl.outfit["bottom"]:
        $ temp_bottom = Girl.outfit["bottom"]

        call remove_bottom(Girl)

        pause 0.2
    else:
        $ temp_bottom = None

    if Girl.outfit["bra"]:
        $ temp_bra = Girl.outfit["bra"]

        call remove_bra(Girl)

        pause 0.2
    else:
        $ temp_bra = None

    if Girl.outfit["bodysuit"]:
        call remove_bodysuit(Girl)

        pause 0.2

    if item:
        call add_bodysuit(Girl, item, set_flags = False)

        pause 0.2

    if redress:
        if temp_bra:
            call add_bra(Girl, temp_bottom, set_flags = True)

            pause 0.2

        if temp_bottom:
            call add_bottom(Girl, temp_bottom, set_flags = False)

            pause 0.2

        if temp_dress:
            call add_dress(Girl, temp_dress, set_flags = False)

            pause 0.2

        if temp_boots:
            $ Girl.outfit["boots"] = temp_boots

            pause 0.2

        if temp_top:
            call add_top(Girl, temp_top, set_flags = False)

            pause 0.2

        if temp_belt:
            $ Girl.outfit["belt"] = temp_belt

            pause 0.2

        if temp_suspenders:
            call add_suspenders(Girl, temp_suspenders, set_flags = False)

            pause 0.2

        if temp_jacket:
            call add_jacket(Girl, temp_jacket, set_flags = False)

            pause 0.2

        if temp_cloak:
            $ Girl.outfit["cloak"] = temp_cloak

    $ Girl.set_outfit_flags()

    return

label remove_bra(Girl):
    if Girl.outfit["bra"]:
        $ Girl.bra_pulled_up = True

    pause 0.2

    $ Girl.outfit["bra"] = ""
    $ Girl.set_outfit_flags()

    if not renpy.showing('dress_screen'):
        call expression Girl.tag + "_First_Topless"

    return

label add_bra(Girl, item, set_flags = True):
    $ Girl.bra_pulled_up = True
    $ Girl.outfit["bra"] = item

    pause 0.2

    if Girl.outfit["bra"]:
        $ Girl.bra_pulled_up = False

    if set_flags:
        $ Girl.set_outfit_flags()

    return

label change_bra(Girl, item, redress = True):
    if Girl.outfit["cloak"]:
        $ temp_cloak = Girl.outfit["cloak"]

        $ Girl.outfit["cloak"] = ""

        pause 0.2
    else:
        $ temp_cloak = None

    if Girl.outfit["jacket"]:
        $ temp_jacket = Girl.outfit["jacket"]

        call remove_jacket(Girl)

        pause 0.2
    else:
        $ temp_jacket = None

    if Girl.outfit["suspenders"]:
        $ temp_suspenders = Girl.outfit["suspenders"]

        call remove_suspenders(Girl)

        pause 0.2
    else:
        $ temp_suspenders = None

    if Girl.outfit["belt"]:
        $ temp_belt = Girl.outfit["belt"]

        $ Girl.outfit["belt"] = ""

        pause 0.2
    else:
        $ temp_belt = None

    if Girl.outfit["top"]:
        $ temp_top = Girl.outfit["top"]

        call remove_top(Girl)

        pause 0.2
    else:
        $ temp_top = None

    if Girl.outfit["dress"]:
        $ temp_dress = Girl.outfit["dress"]

        call remove_dress(Girl)

        pause 0.2
    else:
        $ temp_dress = None

    if Girl.outfit["bra"]:
        call remove_bra(Girl)

        pause 0.2

    if item:
        call add_bra(Girl, item, set_flags = True)

        pause 0.2

    if redress:
        if temp_dress:
            call add_dress(Girl, temp_dress, set_flags = False)

            pause 0.2

        if temp_top:
            call add_top(Girl, temp_top, set_flags = False)

            pause 0.2

        if temp_belt:
            $ Girl.outfit["belt"] = temp_belt

            pause 0.2

        if temp_suspenders:
            call add_suspenders(Girl, temp_suspenders, set_flags = False)

            pause 0.2

        if temp_jacket:
            call add_jacket(Girl, temp_jacket, set_flags = False)

            pause 0.2

        if temp_cloak:
            $ Girl.outfit["cloak"] = temp_cloak

    $ Girl.set_outfit_flags()

    return

label remove_bottom(Girl):
    if Girl.outfit["bottom"] in pants or Girl.outfit["bottom"] in shorts:
        $ Girl.bottom_pulled_down = True

        pause 0.2
    elif Girl.outfit["bottom"] in skirts:
        $ Girl.upskirt = True

        pause 0.2

    $ Girl.outfit["bottom"] = ""
    $ Girl.set_outfit_flags()

    if not renpy.showing('dress_screen'):
        call expression Girl.tag + "_First_Bottomless" pass(1)

    return

label add_bottom(Girl, item, set_flags = True):
    $ Girl.bottom_pulled_down = True
    $ Girl.upskirt = True

    $ Girl.outfit["bottom"] = item

    pause 0.2

    $ Girl.bottom_pulled_down = False
    $ Girl.upskirt = False

    if set_flags:
        $ Girl.set_outfit_flags()

    return

label change_bottom(Girl, item, redress = True):
    if Girl.outfit["boots"]:
        $ temp_boots = Girl.outfit["boots"]

        $ Girl.outfit["boots"] = ""

        pause 0.2
    else:
        $ temp_boots = None

    if Girl.outfit["belt"]:
        $ temp_belt = Girl.outfit["belt"]

        $ Girl.outfit["belt"] = ""

        pause 0.2
    else:
        $ temp_belt = None

    if Girl.outfit["dress"]:
        $ Girl.dress_upskirt = True

        pause 0.2

    if Girl.outfit["bottom"]:
        call remove_bottom(Girl)

        pause 0.2

    if item:
        call add_bottom(Girl, item, set_flags = False)

        pause 0.2

    if redress:
        if Girl.dress_upskirt:
            $ Girl.dress_upskirt = False

            pause 0.2

        if temp_belt:
            $ Girl.outfit["belt"] = temp_belt

            pause 0.2

        if temp_boots:
            $ Girl.outfit["boots"] = temp_boots

    $ Girl.set_outfit_flags()

    return

label change_hose(Girl, item, redress = True):
    if Girl.outfit["boots"]:
        $ temp_boots = Girl.outfit["boots"]

        $ Girl.outfit["boots"] = ""

        pause 0.2
    else:
        $ temp_boots = None

    if Girl.outfit["belt"]:
        $ temp_belt = Girl.outfit["belt"]

        $ Girl.outfit["belt"] = ""

        pause 0.2
    else:
        $ temp_belt = None

    if Girl.outfit["dress"]:
        $ Girl.dress_upskirt = True

        pause 0.2

    if not Girl.outfit["bottom"]:
        $ temp_bottom = None
    elif Girl.outfit["bottom"] in skirts:
        $ temp_bottom = None

        $ Girl.upskirt = True

        pause 0.2
    else:
        $ temp_bottom = Girl.outfit["bottom"]

        call remove_bottom(Girl)

        pause 0.2

    if Girl.outfit["bodysuit"]:
        if Girl.outfit["cloak"]:
            $ temp_cloak = Girl.outfit["cloak"]

            $ Girl.outfit["cloak"] = ""

            pause 0.2
        else:
            $ temp_cloak = None

        if Girl.outfit["jacket"]:
            $ temp_jacket = Girl.outfit["jacket"]

            call remove_jacket(Girl)

            pause 0.2
        else:
            $ temp_jacket = None

        if Girl.outfit["suspenders"]:
            $ temp_suspenders = Girl.outfit["suspenders"]

            call remove_suspenders(Girl)

            pause 0.2
        else:
            $ temp_suspenders = None

        if Girl.outfit["belt"]:
            $ temp_belt = Girl.outfit["belt"]

            $ Girl.outfit["belt"] = ""

            pause 0.2
        else:
            $ temp_belt = None

        if Girl.outfit["top"]:
            $ temp_top = Girl.outfit["top"]

            call remove_top(Girl)

            pause 0.2
        else:
            $ temp_top = None

        if Girl.outfit["boots"]:
            $ temp_boots = Girl.outfit["boots"]

            $ Girl.outfit["boots"] = ""

            pause 0.2
        else:
            $ temp_boots = None

        if Girl.outfit["dress"]:
            $ temp_dress = Girl.outfit["dress"]

            call remove_dress(Girl)

            pause 0.2
        else:
            $ temp_dress = None

        if Girl.outfit["bottom"]:
            $ temp_bottom = Girl.outfit["bottom"]

            call remove_bottom(Girl)

            pause 0.2
        else:
            $ temp_bottom = None

        $ temp_bodysuit = Girl.outfit["bodysuit"]

        call remove_bodysuit(Girl)

        pause 0.2
    else:
        $ temp_bodysuit = None

    if Girl.outfit["hose"]:
        if Girl.outfit["hose"] == "_stockings_and_garterbelt":
            $ Girl.outfit["hose"] = "_garterbelt"

            pause 0.2

        $ Girl.outfit["hose"] = ""

        pause 0.2

    if item:
        if item == "_stockings_and_garterbelt":
            $ Girl.outfit["hose"] = "_garterbelt"

            pause 0.2

        $ Girl.outfit["hose"] = item

        pause 0.2

    if redress:
        if temp_bodysuit:
            call add_bodysuit(Girl, temp_bodysuit, set_flags = False)

            pause 0.2

            if temp_bottom:
                call add_bottom(Girl, temp_bottom, set_flags = False)

                pause 0.2

                $ temp_bottom = None

            if temp_dress:
                call add_dress(Girl, temp_dress, set_flags = False)

                pause 0.2

            if temp_boots:
                $ Girl.outfit["boots"] = temp_boots

                pause 0.2

            if temp_top:
                call add_top(Girl, temp_top, set_flags = False)

                pause 0.2

            if temp_suspenders:
                call add_suspenders(Girl, temp_suspenders, set_flags = False)

                pause 0.2

            if temp_jacket:
                call add_jacket(Girl, temp_jacket, set_flags = False)

                pause 0.2

            if temp_cloak:
                $ Girl.outfit["cloak"] = temp_cloak

                pause 0.2

        if temp_bottom:
            call add_bottom(Girl, temp_bottom, set_flags = False)

            pause 0.2

        if Girl.upskirt:
            $ Girl.upskirt = False

            pause 0.2

        if Girl.dress_upskirt:
            $ Girl.dress_upskirt = False

            pause 0.2

        if temp_belt:
            $ Girl.outfit["belt"] = temp_belt

            pause 0.2

        if temp_boots:
            $ Girl.outfit["boots"] = temp_boots

    $ Girl.set_outfit_flags()

    return

label change_socks(Girl, item, redress = True):
    if Girl.outfit["boots"]:
        $ temp_boots = Girl.outfit["boots"]

        $ Girl.outfit["boots"] = ""

        pause 0.2
    else:
        $ temp_boots = None

    if Girl.outfit["bottom"] in pants or Girl.outfit["bottom"] in shorts:
        $ temp_bottom = Girl.outfit["bottom"]

        call remove_bottom(Girl)

        pause 0.2

    if Girl.outfit["hose"]:
        if Girl.outfit["hose"] == "_stockings_and_garterbelt":
            $ Girl.outfit["hose"] = "_garterbelt"

            pause 0.2

        $ Girl.outfit["hose"] = ""

        pause 0.2

    if item:
        $ Girl.outfit["hose"] = item

        pause 0.2

    if redress:
        if temp_bottom:
            call add_bottom(Girl, temp_bottom, set_flags = False)

            pause 0.2

        if temp_boots:
            $ Girl.outfit["boots"] = temp_boots

    $ Girl.set_outfit_flags()

    return

label remove_underwear(Girl):
    $ Girl.underwear_pulled_down = True

    pause 0.2

    $ Girl.outfit["underwear"] = ""

    pause 0.2

    $ Girl.set_outfit_flags()

    if not renpy.showing('dress_screen'):
        call expression Girl.tag + "_First_Bottomless"

    return

label add_underwear(Girl, item, set_flags = True):
    $ Girl.underwear_pulled_down = True
    $ Girl.outfit["underwear"] = item

    pause 0.2

    $ Girl.underwear_pulled_down = False

    if set_flags:
        $ Girl.set_outfit_flags()

    return

label change_underwear(Girl, item, redress = True):
    if Girl.outfit["boots"]:
        $ temp_boots = Girl.outfit["boots"]

        $ Girl.outfit["boots"] = ""

        pause 0.2
    else:
        $ temp_boots = None

    if Girl.outfit["belt"]:
        $ temp_belt = Girl.outfit["belt"]

        $ Girl.outfit["belt"] = ""

        pause 0.2
    else:
        $ temp_belt = None

    if Girl.outfit["dress"]:
        $ Girl.dress_upskirt = True

        pause 0.2

    if not Girl.outfit["bottom"]:
        $ temp_bottom = None
    elif Girl.outfit["bottom"] in skirts:
        $ temp_bottom = None

        $ Girl.upskirt = True

        pause 0.2
    else:
        $ temp_bottom = Girl.outfit["bottom"]

        call remove_bottom(Girl)

        pause 0.2

    if Girl.outfit["bodysuit"]:
        if Girl.outfit["cloak"]:
            $ temp_cloak = Girl.outfit["cloak"]

            $ Girl.outfit["cloak"] = ""

            pause 0.2
        else:
            $ temp_cloak = None

        if Girl.outfit["jacket"]:
            $ temp_jacket = Girl.outfit["jacket"]

            call remove_jacket(Girl)

            pause 0.2
        else:
            $ temp_jacket = None

        if Girl.outfit["suspenders"]:
            $ temp_suspenders = Girl.outfit["suspenders"]

            call remove_suspenders(Girl)

            pause 0.2
        else:
            $ temp_suspenders = None

        if Girl.outfit["belt"]:
            $ temp_belt = Girl.outfit["belt"]

            $ Girl.outfit["belt"] = ""

            pause 0.2
        else:
            $ temp_belt = None

        if Girl.outfit["top"]:
            $ temp_top = Girl.outfit["top"]

            call remove_top(Girl)

            pause 0.2
        else:
            $ temp_top = None

        if Girl.outfit["boots"]:
            $ temp_boots = Girl.outfit["boots"]

            $ Girl.outfit["boots"] = ""

            pause 0.2
        else:
            $ temp_boots = None

        if Girl.outfit["dress"]:
            $ temp_dress = Girl.outfit["dress"]

            call remove_dress(Girl)

            pause 0.2
        else:
            $ temp_dress = None

        $ temp_bodysuit = Girl.outfit["bodysuit"]

        call remove_bodysuit(Girl)

        pause 0.2
    else:
        $ temp_bodysuit = None

    if Girl.outfit["hose"] in hoses or Girl.outfit["hose"] == "_stockings_and_garterbelt":
        $ temp_hose = Girl.outfit["hose"]

        if Girl.outfit["hose"] == "_stockings_and_garterbelt":
            $ Girl.outfit["hose"] = "_garterbelt"

            pause 0.2

        $ Girl.outfit["hose"] = ""

        pause 0.2
    else:
        $ temp_hose = None

    if Girl.outfit["underwear"]:
        call remove_underwear(Girl)

        pause 0.2

    if item:
        call add_underwear(Girl, item, set_flags = False)

        pause 0.2

    if redress:
        if temp_hose:
            if temp_hose == "_stockings_and_garterbelt":
                $ Girl.outfit["hose"] = "_garterbelt"

                pause 0.2

            $ Girl.outfit["hose"] = temp_hose

            pause 0.2

        if temp_bodysuit:
            call add_bodysuit(Girl, temp_bodysuit, set_flags = False)

            pause 0.2

            if temp_bottom:
                call add_bottom(Girl, temp_bottom, set_flags = False)

                pause 0.2

                $ temp_bottom = None

            if temp_dress:
                call add_dress(Girl, temp_dress, set_flags = False)

                pause 0.2

            if temp_boots:
                $ Girl.outfit["boots"] = temp_boots

                pause 0.2

            if temp_top:
                call add_top(Girl, temp_top, set_flags = False)

                pause 0.2

            if temp_belt:
                $ Girl.outfit["belt"] = temp_belt

                pause 0.2

            if temp_suspenders:
                call add_suspenders(Girl, temp_suspenders, set_flags = False)

                pause 0.2

            if temp_jacket:
                call add_jacket(Girl, temp_jacket, set_flags = False)

                pause 0.2

            if temp_cloak:
                $ Girl.outfit["cloak"] = temp_cloak

                pause 0.2

        if temp_bottom:
            call add_bottom(Girl, temp_bottom, set_flags = False)

            pause 0.2

        if Girl.upskirt:
            $ Girl.upskirt = False

            pause 0.2

        if Girl.dress_upskirt:
            $ Girl.dress_upskirt = False

            pause 0.2

        if temp_belt:
            $ Girl.outfit["belt"] = temp_belt

            pause 0.2

        if temp_boots:
            $ Girl.outfit["boots"] = temp_boots

    $ Girl.set_outfit_flags()

    return

label expose_underwear(Girl):
    if Girl.outfit["dress"]:
        $ Girl.dress_upskirt = True

        pause 0.2

    if not Girl.outfit["bottom"]:
        pass
    elif Girl.outfit["bottom"] in skirts:
        $ Girl.upskirt = True

        pause 0.2
    else:
        $ Girl.bottom_pulled_down = True

        pause 0.2

    if Girl.outfit["bodysuit"]:
        $ Girl.bodysuit_bottom_pulled_aside = True

        pause 0.2

    if Girl.outfit["hose"] in ["_tights", "_ripped_tights", "_pantyhose", "_ripped_pantyhose"]:
        $ Girl.outfit["hose"] = ""

        pause 0.2

    $ Girl.set_outfit_flags()

    if not renpy.showing('dress_screen'):
        call expression Girl.tag + "_First_Bottomless" pass(1)

    return

label expose_breasts(Girl):
    if Girl.outfit["jacket"]:
        if Girl.jacket_closed:
            $ Girl.jacket_closed = False

            pause 0.2

        $ Girl.jacket_opened = True

        pause 0.2

    if Girl.outfit["suspenders"]:
        $ Girl.suspenders_aside = True

        pause 0.2

    if Girl.outfit["top"]:
        $ Girl.top_pulled_up = True

        pause 0.2

    if Girl.outfit["dress"]:
        $ Girl.dress_top_pulled_down = True

        pause 0.2

    if Girl.outfit["bodysuit"]:
        $ Girl.bodysuit_top_pulled_aside = True

        pause 0.2

    if Girl.outfit["bra"]:
        $ Girl.bra_pulled_up = True

    $ Girl.set_outfit_flags()

    if not renpy.showing('dress_screen'):
        call expression Girl.tag + "_First_Topless" pass(1)

    return

label expose_pussy(Girl):
    call expose_underwear(Girl)

    if Girl.outfit["underwear"]:
        $ Girl.underwear_pulled_down = True

        pause 0.2

    $ Girl.set_outfit_flags()

    if not renpy.showing('dress_screen'):
        call expression Girl.tag + "_First_Bottomless" pass(1)

    return

label fully_expose(Girl):
    call expose_breasts(Girl)

    pause 0.2

    call expose_pussy(Girl)

    return

label fully_undress(Girl):
    if Girl.outfit["cloak"]:
        $ Girl.outfit["cloak"] = ""

        pause 0.2

    if Girl.outfit["jacket"]:
        call remove_jacket(Girl)

        pause 0.2

    if Girl.outfit["suspenders"]:
        call remove_suspenders(Girl)

        pause 0.2

    if Girl.outfit["belt"]:
        $ Girl.outfit["belt"] = ""

        pause 0.2

    if Girl.outfit["top"]:
        call remove_top(Girl)

        pause 0.2

    if Girl.outfit["dress"]:
        call remove_dress(Girl)

        pause 0.2

    if Girl.outfit["bra"]:
        call remove_bra(Girl)

    $ Girl.set_outfit_flags()

    if not renpy.showing('dress_screen'):
        call expression Girl.tag + "_First_Topless" pass(1)

    if Girl.outfit["boots"]:
        $ Girl.outfit["boots"] = ""

        pause 0.2

    if Girl.outfit["bottom"]:
        call remove_bottom(Girl)

        pause 0.2

    if Girl.outfit["bodysuit"]:
        call remove_bodysuit(Girl)

        pause 0.2

    if Girl.outfit["hose"]:
        if Girl.outfit["hose"] == "_stockings_and_garterbelt":
            $ Girl.outfit["hose"] = "_garterbelt"

            pause 0.2

        $ Girl.outfit["hose"] = ""

        pause 0.2

    if Girl.outfit["underwear"]:
        call remove_underwear(Girl)

    $ Girl.set_outfit_flags()

    if not renpy.showing('dress_screen'):
        call expression Girl.tag + "_First_Bottomless" pass(1)

    return

label fix_clothing(Girl):
    if Girl.underwear_pulled_down:
        $ Girl.underwear_pulled_down = False

        pause 0.2

    if Girl.hose_pulled_down:
        $ Girl.hose_pulled_down = False

        pause 0.2

    if Girl.bodysuit_bottom_pulled_aside:
        $ Girl.bodysuit_bottom_pulled_aside = False

        pause 0.2

    if Girl.bottom_pulled_down:
        $ Girl.bottom_pulled_down = False

        pause 0.2

    if Girl.upskirt:
        $ Girl.upskirt = False

        pause 0.2

    if Girl.dress_upskirt:
        $ Girl.dress_upskirt = False

        pause 0.2

    if Girl.bra_pulled_up:
        $ Girl.bra_pulled_up = False

        pause 0.2

    if Girl.bodysuit_top_pulled_aside:
        $ Girl.bodysuit_top_pulled_aside = False

        pause 0.2

    if Girl.dress_top_pulled_down:
        $ Girl.dress_top_pulled_down = False

        pause 0.2

    if Girl.top_pulled_up:
        $ Girl.top_pulled_up = False

        pause 0.2

    if Girl.suspenders_aside:
        $ Girl.suspenders_aside = False

        pause 0.2

    if Girl.jacket_opened:
        $ Girl.jacket_opened = False

    $ Girl.set_outfit_flags()

    return
