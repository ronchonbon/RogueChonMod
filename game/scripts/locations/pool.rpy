label swim:
    python:
        Swimmers = []
        Chillers = []
        Changers = []

        for G in Present:
            if approval_check(G, 700):
                if G.Wardrobe.current_Outfit.name == "swimwear":
                    Swimmers.append(G)
                elif G.Wardrobe.current_Outfit.fully_nude:
                    Swimmers.append(G)
                else:
                    if "swimwear" not in G.Wardrobe.Outfits.keys():
                        if G == RogueX:
                            ch_r("I don't really have a swimsuit I could wear. . .")
                        elif G == KittyX:
                            ch_k("I wish I had something cute to wear, but I don't. . .")
                        elif G == EmmaX:
                            ch_e("I really don't own the proper attire. . .")
                        elif G == LauraX:
                            ch_l("Don't have a suit. . .")
                        elif G == JeanX:
                            ch_j("I might, if you buy me a suit. . .")
                        elif G == StormX:
                            ch_s("I -am- afraid I don't have a suit. . .")
                        elif G == JubesX:
                            ch_v("I haven't picked out a suit yet. . .")
                    else:
                        Changers.append(G)

    if Changers:
        show black_screen onlayer black

        python:
            for G in Changers:
                G.change_Outfit(G.Wardrobe.swimming_Outfit.name, instant = True)

        hide black_screen onlayer black

    if len(Swimmers) > 1 and len(Chillers) > 1:
        "Some of the girls get changed and join you, while the others chill out poolside."
    elif len(Swimmers) > 1 and Chillers:
        "[Chillers[0].name] chills out poolside while the rest of the girls get changed and join you."
    elif len(Swimmers) > 1:
        "The girls get changed and join you."
    elif Swimmers and len(Chillers) > 1:
        "[Swimmers[0].name] gets changed and joins you while the rest of the girls chill out poolside."
    elif Swimmers:
        "[Swimmers[0].name] gets changed and joins you."
    elif len(Chillers) > 1:
        "The girls chill out poolside."
    elif Swimmers and Chillers:
        "[Swimmers[0].name] gets changed and joins you while [Chillers[0].name] chills out poolside."
    elif Chillers:
        "[Chillers[0].name] chills out poolside."

    call show_swimming(Swimmers[:])

    $ D20 = renpy.random.randint(1, 20)

    # if D20 >= 15 and Swimmers:
    #     call wardrobe_malfunction (Swimmers[0])

    if D20 >= 11:
        "You take a nice, refreshing swim."
    elif D20 < 3:
        "You join some of the others in a rousing game of Marco Polo."
    elif D20 == 3:
        "You manage to snag one of the floating chairs and drift lazily on the water."
    elif D20 == 4:
        "You manage to snag one of the floating chairs and drift lazily on the water."
        "Until, that is, Kurt teleports up in the air nearby and performs an admittedly awesome cannonball."
        "Too bad it capsizes your chair."
    elif D20 == 5:
        "You test yourself by swimming from one end of the pool to the other."
    elif D20 == 6:
        "You try to impress some of the girls by doing a running jump into the pool."
        "You wind up triggering a cannonball competition that’s ironically NOT won by Cannonball, much to his shock."
    elif D20 == 7:
        "You are about to get into the pool when you hear annoyed cries and shouts of, \"Bobby!\""
        "Looks like Iceman made himself a floating chair again."
        "You stick to the far end of the pool, where it isn’t freezing cold."
    elif D20 == 8:
        "You relax on one of the poolside chairs instead."
    elif D20 == 9:
        "Cyclops is instructing some of the other students in water rescues."
        "You listen in as he talks about approaching a drowning victim from behind so that their panicked flailing won’t cause you injury."
    elif D20 == 10:
        "You decide to make use of the diving board. You do a couple of dives before taking it easy and just swimming around."

    call change_Present_stat("love", 3)
    call change_Present_stat("lust", 5)

    $ round -= 20 if round >= 20 else round

    $ temp_Girls = Swimmers[:]

    while temp_Girls:
        call show_Girl(temp_Girls[0], sprite_layer = 6, animation_transform = reset_zoom_instantly, transition = dissolve)

        $ temp_Girls.remove(temp_Girls[0])

    if len(Swimmers) > 1:
        "You all get out of the pool and rest for a bit."
    elif Swimmers:
        "You both hop out of the pool and rest for a bit."
    else:
        "You hop out of the pool and rest for a bit."


    return

label sunbathe:
    $ Sunbathers = []

    $ chosen = False

    while not chosen:
        menu:
            "With whom?"
            "[RogueX.name]" if Player.location == RogueX.location and RogueX not in Sunbathers:
                $ Sunbathers.append(RogueX)
            "[KittyX.name]" if Player.location == KittyX.location and KittyX not in Sunbathers:
                $ Sunbathers.append(KittyX)
            "[EmmaX.name]" if Player.location == EmmaX.location and EmmaX not in Sunbathers:
                $ Sunbathers.append(EmmaX)
            "[LauraX.name]" if Player.location == LauraX.location and LauraX not in Sunbathers:
                $ Sunbathers.append(LauraX)
            "[JeanX.name]" if Player.location == JeanX.location and JeanX not in Sunbathers:
                $ Sunbathers.append(JeanX)
            "[StormX.name]" if Player.location == StormX.location and StormX not in Sunbathers:
                $ Sunbathers.append(StormX)
            "[JubesX.name]" if Player.location == JubesX.location and JubesX not in Sunbathers:
                $ Sunbathers.append(JubesX)
            "Done.":
                $ chosen = True

    if not Sunbathers:
        "You lay out in the sun's rays for a little while."

        $ round -= 20 if round >= 20 else round

        return

    if len(Sunbathers) == 2:
        $ line = Sunbathers[0].name + ", " + Sunbathers[1].name
    elif len(Sunbathers) > 1:
        $ line = "girls"
    else:
        $ line = Sunbathers[0].name

    ch_p "Hey [line], want to sunbathe with me?"

    python:
        nonnude_Girls = []

        for G in Sunbathers:
            if G.Outfit.breasts_covered or G.Outfit.pussy_covered:
                nonnude_Girls.append(G)

    if len(nonnude_Girls) > 1:
        $ line = len(nonnude_Girls)

        ch_p "You [line] don't want to get tanlines, right? You could. . ."
    else:
        ch_p "You don't want to get tanlines, right? You could. . ."

    ch_p ". . . take off a few layers?"

    python:
        for G in nonnude_Girls:
            G.undress()

    if len(Sunbathers) > 1:
        "You all lay out in the sun's rays together."
    else:
        "You all lay out in the sun's rays together."

    $ round -= 20 if round >= 20 else round

    return

label skinny_dip:
    $ Dippers = []

    $ chosen = False

    while not chosen:
        menu:
            "With whom?"
            "[RogueX.name]" if Player.location == RogueX.location and RogueX not in Dippers:
                $ Dippers.append(RogueX)
            "[KittyX.name]" if Player.location == KittyX.location and KittyX not in Dippers:
                $ Dippers.append(KittyX)
            "[EmmaX.name]" if Player.location == EmmaX.location and EmmaX not in Dippers:
                $ Dippers.append(EmmaX)
            "[LauraX.name]" if Player.location == LauraX.location and LauraX not in Dippers:
                $ Dippers.append(LauraX)
            "[JeanX.name]" if Player.location == JeanX.location and JeanX not in Dippers:
                $ Dippers.append(JeanX)
            "[StormX.name]" if Player.location == StormX.location and StormX not in Dippers:
                $ Dippers.append(StormX)
            "[JubesX.name]" if Player.location == JubesX.location and JubesX not in Dippers:
                $ Dippers.append(JubesX)
            "Done.":
                $ chosen = True

    if not Dippers:
        "You quickly strip and jump into the pool naked."
        "After swimming around for a bit, you hop out and get dressed."

        $ round -= 20 if round >= 20 else round

        return

    if len(Dippers) == 2:
        $ line = Dippers[0].name + ", " + Dippers[1].name
    elif len(Dippers) > 1:
        $ line = "girls"
    else:
        $ line = Dippers[0].name

    ch_p "Hey [line], why don't we skinny dip?"

    python:
        for G in Dippers:
            if not G.Outfit.fully_nude:
                G.undress()

    call show_swimming(Dippers[:])

    if len(Dippers):
        "You all swim around for a bit."
    else:
        "You both swim around for a bit."

    $ round -= 20 if round >= 20 else round

    $ temp_Girls = Dippers[:]

    while temp_Girls:
        call show_Girl(temp_Girls[0], sprite_layer = 6, animation_transform = reset_zoom_instantly, transition = dissolve)

        $ temp_Girls.remove(temp_Girls[0])

    if len(Dippers) > 1:
        "You all get out of the pool and rest for a bit."
    else:
        "You both out of the pool and rest for a bit."

    return

label show_swimming(Swimmers):
    if Swimmers in all_Girls:
        $ Swimmers = [Swimmers]

    while Swimmers:
        $ Swimmers[0].wet = True

        python:
            for key in Swimmers[0].spunk.keys():
                Swimmers[0].spunk[key] = False

        $ x_position = renpy.random.random()

        while x_position < 0.3 or x_position > 0.7:
            $ x_position = renpy.random.random()

        call show_Girl(Swimmers[0], sprite_layer = 1, animation_transform = swimming(x_position), transition = dissolve)

        $ Swimmers.remove(Swimmers[0])

    return





label wardrobe_malfunction(Girl):
    $ shift_focus(Girl)

    $ Girl.expose_breasts()

    "[Girl.name] dives into the pool."
    "It appears she's had a wardrobe malfunction."

    menu:
        extend ""
        "Hey, [Girl.name]. . .":
            ch_p "Looks like you might be missing something there. . ."

            $ Girl.change_face("confused")

            if Girl != StormX:
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", -2)
                Girl.voice ". . ."
                $ Girl.change_face("surprised", 2, eyes = "down")

            call change_Girl_stat(Girl, "love", 3)
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "lust", 2)

            $ offset = 100
        "Say nothing.":
            $ Girl.change_face("surprised", 2, eyes = "down")

            "After a few moments, [Girl.name] seems to notice that her top is up."

            if approval_check(Girl, 1200):
                $ offset = 0
            else:
                $ offset = -100

    if approval_check(Girl, 800 - offset, "I") or approval_check(Girl, 1600 - offset) or (Girl == StormX and StormX in Rules):
        $ Girl.change_face("sly")

        $ Girl.remove_Clothing("bra")

        call change_Girl_stat(Girl, "obedience", 2)
        call change_Girl_stat(Girl, "inhibition", 4)
        call change_Girl_stat(Girl, "inhibition", 2)
        call change_Girl_stat(Girl, "lust", 5)

        "She smiles and tosses her top over her head."

        call expression Girl.tag + "_First_Topless"
    elif approval_check(Girl, 500 - offset, "I") or approval_check(Girl, 1200 - offset):
        $ Girl.change_face("sly", 1)

        call change_Girl_stat(Girl, "obedience", 2)
        call change_Girl_stat(Girl, "inhibition", 3)
        call change_Girl_stat(Girl, "inhibition", 2)
        call change_Girl_stat(Girl, "lust", 3)

        "She smiles, and leaves the top how it is."

        call expression Girl.tag + "_First_Topless"
    else:
        if approval_check(Girl, 800 - offset) or (Girl == StormX):
            call change_Girl_stat(Girl, "obedience", 2)
            call change_Girl_stat(Girl, "inhibition", 2)
            call change_Girl_stat(Girl, "lust", 1)

            $ Girl.change_face("bemused", 2)
        else:
            call change_Girl_stat(Girl, "love", -2)
            call change_Girl_stat(Girl, "inhibition", 1)

            $ Girl.change_face("angry", 2)

        call expression Girl.tag + "_First_Topless" pass (1)

        $ Girl.fix_clothing()

        "She tugs her top back into place."

        if offset == 0:
            call change_Girl_stat(Girl, "love", -5)
            call change_Girl_stat(Girl, "obedience", -2)
            call change_Girl_stat(Girl, "inhibition", 2)

            Girl.voice "You could have told me."

    return
