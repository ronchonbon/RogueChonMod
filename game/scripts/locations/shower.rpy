label showering:
    python:
        showering_Girls = []

        for G in all_Girls:
            if G.location == "bg_shower":
                showering_Girls.append(G)

    if showering_Girls:
        ch_p "I'm taking a shower, care to join me?"

        $ temp_Girls = showering_Girls[:]

        while temp_Girls:
            if temp_Girls[0].location == Player.location:
                $ temp_Girls[0].undress()
                $ temp_Girls[0].wet = True

                python:
                    for key in temp_Girls[0].spunk.keys():
                        temp_Girls[0].spunk[key] = False

            $ temp_Girls.remove(temp_Girls[0])

    if showering_Girls:
        $ renpy.random.shuffle(showering_Girls)

        $ shift_focus(showering_Girls[0])

        if len(showering_Girls) > 1:
            "You take a quick shower with [showering_Girls[0].name] and [showering_Girls[1].name]."
        else:
            "You take a quick shower with [showering_Girls[0].name]."
    else:
        $ line = "You take a quick shower" + renpy.random.choice([". It was fairly uneventful.",
            ". A few people came and went as you did so.",
            ". That was refreshing."])

        "[line]"

    $ round -= 30 if round >= 30 else round

    call get_dressed

    python:
        for G in showering_Girls:
            G.change_Outfit("shower")

    return




label Shower_Sex(Options=0, line=0):
    if len(staying_Girls) > 1 and (approval_check(staying_Girls[1], 1800,Check = 1) > approval_check(staying_Girls[0], 1800,Check = 1)):
        $ renpy.random.shuffle(staying_Girls)
    $ shift_focus (staying_Girls[0])

    $ D20 = renpy.random.randint(1, 20)
    $ D20 += 5 if approval_check(staying_Girls[0], 1800) else 0

    if "showered" in Player.recent_history:
        $ D20 = 0

    $ staying_Girls[0].change_face("sly")

    if len(staying_Girls) > 1 and D20 >= 10:
        "As you do so, both girls press their bodies body up against yours."
        $ line = staying_Girls[0].name
        call close_launch(staying_Girls[0], staying_Girls[1])
    elif D20 >= 5:
        "As you do so, [staying_Girls[0].name] presses her body up against you."
        $ line = "She"
        call close_launch(staying_Girls[0])
    else:
        $ line = renpy.random.choice(["It was fairly uneventful.",
                    "A few people came and went as you did so.",
                    "That was refreshing."])
        "[line]"
        if len(staying_Girls) > 1:
            call change_Girl_stat(staying_Girls[0], "lust", 15)
            call change_Girl_stat(staying_Girls[1], "lust", 15)
            call change_Girl_stat(staying_Girls[0], "lust", 10)
            call change_Girl_stat(staying_Girls[1], "lust", 10)
            "You got a good look at them washing off, and they didn't seem to mind the view either."
            $ staying_Girls[0].check_if_likes(staying_Girls[1], 600,4, 1)
            $ staying_Girls[1].check_if_likes(staying_Girls[0], 600,4, 1)
            $ staying_Girls[0].check_if_likes(staying_Girls[1],800, 2, 1)
            $ staying_Girls[1].check_if_likes(staying_Girls[0],800, 2, 1)
        else:
            call change_Girl_stat(staying_Girls[0], "lust", 15)
            call change_Girl_stat(staying_Girls[0], "lust", 10)
            "You got a good look at her washing off, and she didn't seem to mind the view either."
        return

    if line:
        if len(staying_Girls) > 1:
            call change_Girl_stat(staying_Girls[0], "lust", 5)
            call change_Girl_stat(staying_Girls[0], "lust", 3)
            call change_Girl_stat(staying_Girls[1], "lust", 5)
            call change_Girl_stat(staying_Girls[1], "lust", 3)
        else:
            call change_Girl_stat(staying_Girls[0], "lust", 6)
            call change_Girl_stat(staying_Girls[0], "lust", 3)
        call change_Player_stat("focus", 50, 5)
        call change_Player_stat("focus", 80, 2)
        menu:
            extend ""
            "Continue?":
                pass
            "Stop her." if len(staying_Girls) < 2:
                $ line = 0
                call show_full_body(staying_Girls[0])
                "You take a step back, pulling away from her."
                call change_Girl_stat(staying_Girls[0], "love", -1)
                call change_Girl_stat(staying_Girls[0], "obedience", 5)
                call change_Girl_stat(staying_Girls[0], "inhibition", -1)
                $ staying_Girls[0].change_face("sad")
                "She seems a bit disappointed."
            "Stop them." if len(staying_Girls) > 1:
                $ line = 0
                call show_full_body(staying_Girls[0])
                call show_full_body(staying_Girls[1])
                "You take a step back, pulling away from them."
                call change_Girl_stat(staying_Girls[0], "love", -1)
                call change_Girl_stat(staying_Girls[0], "obedience", 5)
                call change_Girl_stat(staying_Girls[0], "inhibition", -1)
                call change_Girl_stat(staying_Girls[1], "obedience", 5)
                call change_Girl_stat(staying_Girls[1], "inhibition", -1)
                $ staying_Girls[0].change_face("sad")
                $ staying_Girls[1].change_face("sad")
                "They seem a bit disappointed."
    if line:

        $ Options = [1]
        if len(staying_Girls) > 1:
            if approval_check(staying_Girls[0], 1300) and staying_Girls[0].likes[staying_Girls[1].tag] >= 800:
                $ Options.append(2)
            if approval_check(staying_Girls[0], 1200) and staying_Girls[0].likes[staying_Girls[1].tag] >= 700:
                $ Options.append(3)

        if approval_check(staying_Girls[0], 1300):
            $ Options.append(4)
        if approval_check(staying_Girls[0], 1400):
            $ Options.append(5)

        if approval_check(staying_Girls[0], 1300):
            $ Options.append(6)
        if approval_check(staying_Girls[0], 1200):
            $ Options.append(7)

        if not approval_check(staying_Girls[0], 1400):

            if approval_check(staying_Girls[0], 1000):
                $ Options.append(8)
            if approval_check(staying_Girls[0], 1100):
                $ Options.append(9)
            if approval_check(staying_Girls[0], 1000):
                $ Options.append(10)
            if approval_check(staying_Girls[0], 1100):
                $ Options.append(11)

        $ renpy.random.shuffle(Options)



        if Options[0] == 2:
            call change_Girl_stat(staying_Girls[0], "lust", 5)
            call change_Girl_stat(staying_Girls[0], "lust", 2)
            call change_Girl_stat(staying_Girls[1], "lust", 7)
            call change_Girl_stat(staying_Girls[1], "lust", 3)
            call change_Player_stat("focus", 50, 8)
            call change_Player_stat("focus", 80, 4)
            "[line] reaches over to [staying_Girls[1].name] and begins soaping up her chest."
        elif Options[0] == 3:
            call change_Girl_stat(staying_Girls[0], "lust", 7)
            call change_Girl_stat(staying_Girls[0], "lust", 3)
            call change_Girl_stat(staying_Girls[1], "lust", 8)
            call change_Girl_stat(staying_Girls[1], "lust", 4)
            call change_Player_stat("focus", 50, 8)
            call change_Player_stat("focus", 80, 5)
            "[line] reaches over to [staying_Girls[1].name] and begins soaping up her pussy."


        elif Options[0] == 4:
            if len(staying_Girls) > 1:
                call change_Girl_stat(staying_Girls[0], "lust", 10)
                call change_Girl_stat(staying_Girls[0], "lust", 7)
            else:
                call change_Girl_stat(staying_Girls[0], "lust", 8)
                call change_Girl_stat(staying_Girls[0], "lust", 5)
            call change_Player_stat("focus", 50, 10)
            call change_Player_stat("focus", 80, 6)
            "[line] reaches down and takes your cock in her hand, soaping it up."
        elif Options[0] == 5:
            if len(staying_Girls) > 1:
                call change_Girl_stat(staying_Girls[0], "lust", 12)
                call change_Girl_stat(staying_Girls[0], "lust", 8)
            else:
                call change_Girl_stat(staying_Girls[0], "lust", 9)
                call change_Girl_stat(staying_Girls[0], "lust", 6)
            call change_Player_stat("focus", 50, 10)
            call change_Player_stat("focus", 80, 4)
            "[line] kneels down and wraps her breasts around your cock, soaping it up."


        elif Options[0] == 6:
            if len(staying_Girls) > 1:
                call change_Girl_stat(staying_Girls[0], "lust", 11)
                call change_Girl_stat(staying_Girls[0], "lust", 6)
            else:
                call change_Girl_stat(staying_Girls[0], "lust", 9)
                call change_Girl_stat(staying_Girls[0], "lust", 5)
            call change_Player_stat("focus", 50, 9)
            call change_Player_stat("focus", 80, 4)
            "[line] reaches down and begins fondling her own pussy, building a nice lather."
        elif Options[0] == 7:
            if len(staying_Girls) > 1:
                call change_Girl_stat(staying_Girls[0], "lust", 10)
                call change_Girl_stat(staying_Girls[0], "lust", 5)
            else:
                call change_Girl_stat(staying_Girls[0], "lust", 9)
                call change_Girl_stat(staying_Girls[0], "lust", 4)
            call change_Player_stat("focus", 50, 8)
            call change_Player_stat("focus", 80, 3)
            "[line] begins rubbing her own breasts in circles, building a nice lather."


        elif Options[0] == 8:
            call change_Girl_stat(staying_Girls[0], "lust", 6)
            call change_Girl_stat(staying_Girls[0], "lust", 3)
            call change_Player_stat("focus", 50, 7)
            call change_Player_stat("focus", 80, 3)
            "[line] draws her breasts up and down your arm, the soap bubbles squirting out."
        elif Options[0] == 9:
            call change_Girl_stat(staying_Girls[0], "lust", 8)
            call change_Girl_stat(staying_Girls[0], "lust", 3)
            call change_Player_stat("focus", 50, 8)
            call change_Player_stat("focus", 80, 3)
            "[line] kneels down and rubs her breasts against your leg, soaping it up."
        elif Options[0] == 10:
            call change_Girl_stat(staying_Girls[0], "lust", 7)
            call change_Girl_stat(staying_Girls[0], "lust", 3)
            call change_Player_stat("focus", 50, 6)
            call change_Player_stat("focus", 80, 3)
            "[line] presses against your back, her soapy breasts rubbing back and forth against it."
        elif Options[0] == 11:
            call change_Girl_stat(staying_Girls[0], "lust", 7)
            call change_Girl_stat(staying_Girls[0], "lust", 3)
            call change_Player_stat("focus", 50, 8)
            call change_Player_stat("focus", 80, 4)
            "[line] presses against your chest, her soapy breasts rubbing back and forth against it."
        elif Options[0] == 1:
            call change_Girl_stat(staying_Girls[0], "lust", 5)
            call change_Girl_stat(staying_Girls[0], "lust", 2)
            call change_Player_stat("focus", 50, 6)
            call change_Player_stat("focus", 80, 3)
            "[line] stares silently at you as she moves her hands along her soapy body. . ."
            $ line = 0

    if line and len(staying_Girls) > 1:

        $ D20 += 5 if approval_check(staying_Girls[1], 1800) else 0
        if staying_Girls[1].likes[staying_Girls[0].tag] <= 800 and 2 <= Options[0] < = 3:
            $ D20 -= 5
        if staying_Girls[1].likes[staying_Girls[0].tag] <= 600:
            $ D20 -= 5

        if 2 <= Options[0] <= 3:

            if approval_check(staying_Girls[1], 1300) and staying_Girls[1].likes[staying_Girls[0].tag] >= 800:
                $ staying_Girls[1].change_face("sexy", 1)
                call change_Girl_stat(staying_Girls[0], "lust", 5)
                call change_Girl_stat(staying_Girls[0], "lust", 5)
                call change_Girl_stat(staying_Girls[1], "lust", 12)
                call change_Girl_stat(staying_Girls[1], "lust", 12)
                call close_launch(staying_Girls[0], staying_Girls[1])
                "[staying_Girls[1].name] seems really into this, and returns the favor."
                call change_Player_stat("focus", 50, 7)
                call change_Player_stat("focus", 80, 3)
                $ line = 4
            elif approval_check(staying_Girls[1], 1200) and staying_Girls[1].likes[staying_Girls[0].tag] >= 700:
                $ staying_Girls[1].change_face("sexy", 2, eyes = "closed")
                call change_Girl_stat(staying_Girls[1], "lust", 10)
                call change_Girl_stat(staying_Girls[1], "lust", 10)
                call change_Player_stat("focus", 50, 5)
                call change_Player_stat("focus", 80, 3)
                call close_launch(staying_Girls[0], staying_Girls[1])
                "[staying_Girls[1].name] seems really into this, and leans into it."
            else:
                call change_Girl_stat(staying_Girls[1], "lust", 10)
                $ staying_Girls[1].change_face("sadside", brows = "confused")
                "[staying_Girls[1].name] doesn't really seem to appreciate this."
                "She pulls away."
                $ line = 3
        else:

            if (approval_check(staying_Girls[1], 1300) and staying_Girls[1].likes[staying_Girls[0].tag] >= 700) or approval_check(staying_Girls[1], 2000):
                if Options[0] == 5:
                    call change_Girl_stat(staying_Girls[1], "lust", 10)
                    call change_Girl_stat(staying_Girls[1], "lust", 5)
                    call change_Player_stat("focus", 50, 6)
                    call change_Player_stat("focus", 80, 3)
                    call close_launch(staying_Girls[0], staying_Girls[1])
                    "[staying_Girls[1].name] seems really into this, slowly rubbing against you as she watches."
                else:
                    call change_Girl_stat(staying_Girls[1], "lust", 10)
                    call change_Girl_stat(staying_Girls[1], "lust", 5)
                    call change_Player_stat("focus", 50, 5)
                    call change_Player_stat("focus", 80, 3)
                    call close_launch(staying_Girls[0], staying_Girls[1])
                    "[staying_Girls[1].name] seems really into this, and joins her on the other side."
                $ line = 4
            elif ((approval_check(staying_Girls[1], 1200) and staying_Girls[1].likes[staying_Girls[0].tag] >= 600)) or approval_check(staying_Girls[1], 1600):
                $ staying_Girls[1].change_face("sexy", 2, eyes = "down")
                call change_Girl_stat(staying_Girls[1], "lust", 10)
                call change_Girl_stat(staying_Girls[1], "lust", 5)
                "[staying_Girls[1].name] seems really into this, and watches her do it."
            else:
                $ staying_Girls[1].change_face("sadside", brows = "confused")
                call change_Girl_stat(staying_Girls[1], "lust", 5)
                "[staying_Girls[1].name] doesn't really seem to appreciate this."
                $ line = 3
    if line:
        menu:
            extend ""
            "Continue?":
                pass
            "Stop her." if len(staying_Girls) < 2:
                $ line = 0
                call show_full_body(staying_Girls[0])
                "You take a step back, pulling away from her."
                call change_Girl_stat(staying_Girls[0], "love", -2)
                call change_Girl_stat(staying_Girls[0], "obedience", 5)
                call change_Girl_stat(staying_Girls[0], "inhibition", -2)
                $ staying_Girls[0].change_face("sad")
                "She seems a bit disappointed."
            "Stop them." if len(staying_Girls) > 1:
                $ line = 0
                call show_full_body(staying_Girls[0])
                call show_full_body(staying_Girls[1])
                "You take a step back, pulling away from them."
                $ staying_Girls[0].change_face("sad")
                call change_Girl_stat(staying_Girls[0], "love", -2)
                call change_Girl_stat(staying_Girls[0], "obedience", 5)
                call change_Girl_stat(staying_Girls[0], "inhibition", -2)
                if line == 3:
                    call change_Girl_stat(staying_Girls[1], "love", 4)
                    call change_Girl_stat(staying_Girls[1], "obedience", 5)
                    $ staying_Girls[1].change_face("bemused")
                    "[staying_Girls[0].name] seems a bit disappointed, but [staying_Girls[1].name] seems pleased."
                else:
                    call change_Girl_stat(staying_Girls[1], "love", -1)
                    call change_Girl_stat(staying_Girls[1], "obedience", 5)
                    call change_Girl_stat(staying_Girls[1], "inhibition", -1)
                    $ staying_Girls[1].change_face("sad")
                    "They seem a bit disappointed."

    if line:

        if len(staying_Girls) > 1 and line != 3:
            $ staying_Girls[0].check_if_likes(staying_Girls[1], 600,4, 1)
            $ staying_Girls[1].check_if_likes(staying_Girls[0], 600,4, 1)
            $ staying_Girls[0].check_if_likes(staying_Girls[1],800,3, 1)
            $ staying_Girls[1].check_if_likes(staying_Girls[0],800,3, 1)
            $ staying_Girls[0].check_if_likes(staying_Girls[1], 900, 1, 1)
            $ staying_Girls[1].check_if_likes(staying_Girls[0], 900, 1, 1)
        if 2 <= Options[0] <= 3 and D20 >= 15:

            $ staying_Girls[1].check_if_likes(staying_Girls[0], 900,4, 1)
            call change_Player_stat("focus", 50, 10)
            call change_Player_stat("focus", 80, 5)
            "After a few minutes of this, it looks like [staying_Girls[1].name] gets off."
            call Girl_Cumming (staying_Girls[1], 1)
            if line == 4:
                $ staying_Girls[0].check_if_likes(staying_Girls[1], 900,3, 1)
                "It looks like [staying_Girls[0].name] is reacting positively to it as well. . ."
                call Girl_Cumming (staying_Girls[0], 1)
            if len(staying_Girls) > 1:
                "The girls take a step back."
                call show_full_body(staying_Girls[1])
            else:
                "[staying_Girls[0].name] takes a step back."

            call show_full_body(staying_Girls[0])

        elif 4 <= Options[0] <= 5 and D20 >= 10:

            $ Player.climax = 15
            if Options[0] == 5:
                $ staying_Girls[0].spunk["breasts"] = True

            if line == 4:
                call change_Girl_stat(staying_Girls[0], "inhibition", 7)
                call change_Girl_stat(staying_Girls[1], "inhibition", 4)
                $ staying_Girls[0].check_if_likes(staying_Girls[1], 900,3, 1)
                $ staying_Girls[1].check_if_likes(staying_Girls[0], 900,3, 1)
                "After a few minutes of this, the two of them manage to get you off."
            else:
                call change_Girl_stat(staying_Girls[0], "inhibition", 5)
                "After a few minutes of this, she manages to get you off."
            "A little more work is needed to clean up the mess."
            if Options[0] == 5:
                python:
                    for key in staying_Girls[0].spunk.keys():
                        staying_Girls[0].spunk[key] = False
            if len(staying_Girls) > 1:
                "The girls take a step back."
                call show_full_body(staying_Girls[1])
            else:
                "[staying_Girls[0].name] takes a step back."
            call show_full_body(staying_Girls[0])

        elif 6 <= Options[0] <= 7 and D20 >= 15:

            call change_Girl_stat(staying_Girls[0], "inhibition", 7)
            call change_Player_stat("focus", 50, 15)
            call change_Player_stat("focus", 80, 5)
            "After a few minutes of this, it looks like [staying_Girls[0].name] gets off."
            call Girl_Cumming (staying_Girls[0], 1)
            if line == 4:
                call change_Girl_stat(staying_Girls[1], "inhibition", 6)
                $ staying_Girls[0].check_if_likes(staying_Girls[1], 900,3, 1)
                "It looks like [staying_Girls[1].name] is enjoying herself as well. . ."
                call Girl_Cumming (staying_Girls[1], 1)
            if len(staying_Girls) > 1:
                $ staying_Girls[1].check_if_likes(staying_Girls[0], 900,3, 1)
                "The girls take a step back."
                call show_full_body(staying_Girls[1])
            else:
                "[staying_Girls[0].name] takes a step back."
            call show_full_body(staying_Girls[0])
        else:

            if len(staying_Girls) > 1:
                call show_full_body(staying_Girls[1])
            call show_full_body(staying_Girls[0])
            call change_Player_stat("focus", 50, 15)
            call change_Player_stat("focus", 80, 5)
            if D20 >= 15:
                "After a minute or two, it sounds like someone is coming, so you scramble apart."
                "Disappointing. . ."
            elif D20 >= 10:
                "After a minute or two, she seems satisfied with her efforts, and pulls back."
                if 4 <= Options[0] <= 5:
                    "You're left pretty hard."
            else:
                "After a minute or so of this, she draws back and finshes washing herself off."
                if 4 <= Options[0] <= 5:
                    "You're left pretty hard."
    $ shift_focus (staying_Girls[0])
    return
