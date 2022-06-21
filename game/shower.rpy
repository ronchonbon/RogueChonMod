label showering:
    $ showering_Girls = []
    $ staying_Girls = []

    $ showered = False

    python:
        for G in all_Girls:
            if G.location == "bg_showerroom":
                showering_Girls.append(G)

    if showering_Girls:
        ch_p "I'm taking a shower, care to join me?"

        $ counter = 0

        $ already_showered = False

        while counter < len(showering_Girls):
            if "showered" in showering_Girls[counter].recent_history:
                if len(showering_Girls) > 1 and counter == 0:
                    if showering_Girls[counter] == RogueX:
                        ch_r "We actually just finished up, so we'll head out."
                    elif showering_Girls[counter] == KittyX:
                        ch_k "We actually just showered, so we're heading out."
                    elif showering_Girls[counter] == EmmaX:
                        ch_e "We were actually finishing up, so we're heading out."
                    elif showering_Girls[counter] == LauraX:
                        ch_l "We were done, actually."
                    elif showering_Girls[counter] == JeanX:
                        ch_j "We were done."
                    elif showering_Girls[counter] == StormX:
                        "I think we're about finished and heading out now."
                    elif showering_Girls[counter] == JubesX:
                        ch_v "We finished getting showered, so we're taking off."
                elif len(showering_Girls) > 1 and counter == 1:
                    $ first_approval = approval_check(showering_Girls[counter], 1400, Alt = [[RogueX, JeanX], 1200])
                    $ second_approval = approval_check(showering_Girls[counter], 700, Alt = [[RogueX, JeanX], 600])

                    if showering_Girls[counter] == EmmaX and not "classcaught" in EmmaX.history or not "threesome" in EmmaX.history:
                        ch_e "I really should be going. . ."
                    elif first_approval or (second_approval and showering_Girls[1].seen_breasts and showering_Girls[1].seen_pussy):
                        if showering_Girls[1] == RogueX:
                            if staying_Girls:
                                ch_r "I could stick around too. . ."
                            else:
                                ch_r "Well, I could probably stay."
                        elif showering_Girls[1] == KittyX:
                            if staying_Girls:
                                ch_k "I guess I could stay too. . ."
                            else:
                                ch_k "Well, I could stay though."
                        elif showering_Girls[1] == EmmaX:
                            if staying_Girls:
                                ch_e "I suppose I could also stay. . ."
                            else:
                                ch_e "But {i}I{/i} could stick around. . ."
                        elif showering_Girls[1] == LauraX:
                            if staying_Girls:
                                ch_l "I could stay too. . ."
                            else:
                                ch_l "I could stick around."
                        elif showering_Girls[1] == JeanX:
                            if staying_Girls:
                                ch_j "I guess I could stay too. . ."
                            else:
                                ch_j "I could stick around."
                        elif showering_Girls[1] == StormX:
                            if staying_Girls:
                                ch_s "I could also stay. . ."
                            else:
                                ch_s "I could stay for a moment though. . ."
                        elif showering_Girls[1] == JubesX:
                            if staying_Girls:
                                ch_k "I could kinda stay too. . ."
                            else:
                                ch_k "Well, -I'm- not that busy. . ."

                        $ staying_Girls.append(showering_Girls[1])
                    else:
                        if showering_Girls[1] == RogueX:
                            if staying_Girls:
                                ch_r "I can't though . ."
                            else:
                                ch_r "I should get going too."
                        elif showering_Girls[1] == KittyX:
                            if staying_Girls:
                                ch_k "I've really got to go though. . ."
                            else:
                                ch_k "Yeah, I should head out too."
                        elif showering_Girls[1] == EmmaX:
                            if staying_Girls:
                                ch_e "But I really must be going. . ."
                            else:
                                ch_e "Yes, let's go."
                        elif showering_Girls[1] == LauraX:
                            if staying_Girls:
                                ch_l "I gotta get going though. . ."
                            else:
                                ch_l "Yeah, me too."
                        elif showering_Girls[1] == JeanX:
                            if staying_Girls:
                                ch_j "I'm heading out though. . ."
                            else:
                                ch_j "Yeah."
                        elif showering_Girls[1] == StormX:
                            if staying_Girls:
                                ch_s "Well I'm afraid I must be going. . ."
                            else:
                                ch_s "Yes, let's."
                        elif showering_Girls[1] == JubesX:
                            if staying_Girls:
                                ch_k "I'm really busy right now though. . ."
                            else:
                                ch_k "Oh, yeah, I gotta go too. . ."
                else:
                    if showering_Girls[counter] == RogueX:
                        ch_r "I actually just finished up, so I'll head out."
                    elif showering_Girls[counter] == KittyX:
                        ch_k "I actually just showered, so I'm heading out."
                    elif showering_Girls[counter] == EmmaX:
                        ch_e "I was actually finishing up, so I'm heading out."
                    elif showering_Girls[counter] == LauraX:
                        ch_l "I'm heading out now."
                    elif showering_Girls[counter] == JeanX:
                        ch_j "I'm heading out."
                    elif showering_Girls[counter] == StormX:
                        "I was about finished and heading out now."
                    elif showering_Girls[counter] == JubesX:
                        "I finished getting showered, so I'm taking off."

                $ already_showered = True
            else:
                $ first_approval = approval_check(showering_Girls[counter], 1400, Alt = [[RogueX], 1200])
                $ second_approval = approval_check(showering_Girls[counter], 700, Alt = [[RogueX], 600])

                if first_approval or (second_approval and showering_Girls[counter].seen_breasts and showering_Girls[counter].seen_pussy):
                    if showering_Girls[counter] == RogueX:
                        ch_r "I suppose I could stick around. . ."

                        $ staying_Girls.append(showering_Girls[counter])
                    elif showering_Girls[counter] == KittyX:
                        "Yeah, I could stick around."

                        $ staying_Girls.append(showering_Girls[counter])
                    elif showering_Girls[counter] == EmmaX:
                        if not "classcaught" in EmmaX.history or "threesome" not in EmmaX.history:
                            ch_e "I really should be going. . ."
                        else:
                            ch_e "I suppose I could stay, for a bit."

                            $ staying_Girls.append(showering_Girls[counter])
                    elif showering_Girls[counter] == LauraX:
                        ch_l "I got nothing better to do."

                        $ staying_Girls.append(showering_Girls[counter])
                    elif showering_Girls[counter] == JeanX:
                        ch_j "Sure, why not."

                        $ staying_Girls.append(showering_Girls[counter])
                    elif showering_Girls[counter] == StormX:
                        ch_s "I could stay, I suppose."

                        $ staying_Girls.append(showering_Girls[counter])
                    elif showering_Girls[counter] == JubesX:
                        ch_v "I guess I could stay a minute. . ."

                        $ staying_Girls.append(showering_Girls[counter])
                else:
                    if showering_Girls[counter] == RogueX:
                        ch_r "Nah, I should probably get going."
                    elif showering_Girls[counter] == KittyX:
                        ch_k "I've got to get going."
                    elif showering_Girls[counter] == EmmaX:
                        ch_e "I'm afraid I really must be going."
                    elif showering_Girls[counter] == LauraX:
                        ch_l "I gotta get going."
                    elif showering_Girls[counter] == JeanX:
                        ch_j "Nah, lol."
                    elif showering_Girls[counter] == StormX:
                        ch_s "I really do have things to do, [StormX.player_petname]."
                    elif showering_Girls[counter] == JubesX:
                        ch_v "I'm kinda busy, [JubesX.player_petname]."

            $ counter += 1

        if len(showering_Girls) > len(staying_Girls):
            menu:
                extend ""
                "Ok, see you later then.":
                    if RogueX.location == bg_current and RogueX not in staying_Girls:
                        ch_r "Yeah, later."
                    if KittyX.location == bg_current and KittyX not in staying_Girls:
                        ch_k "Bye!"
                    if EmmaX.location == bg_current and EmmaX not in staying_Girls:
                        ch_e "Yes, later."
                    if LauraX.location == bg_current and LauraX not in staying_Girls:
                        ch_l "Yup."
                    if JeanX.location == bg_current and JeanX not in staying_Girls:
                        ch_j "Ok."
                    if StormX.location == bg_current and StormX not in staying_Girls:
                        ch_s "Yes, I'll see you."
                    if JubesX.location == bg_current and JubesX not in staying_Girls:
                        ch_v "Laters!"
                "Sure you got every spot?" if already_showered:
                    $ line = "spot"
                "Maybe you could stay and watch?":
                    $ line = "watch me"
                "But I didn't get to watch." if already_showered:
                    $ line = "watch you"

            if line:
                python:
                    for G in showering_Girls:
                        if G.location == bg_current and G not in staying_Girls:
                            if G == EmmaX and (not "classcaught" in EmmaX.history or (staying_Girls and "threesome" not in EmmaX.history)):
                                pass
                            elif G == JeanX and approval_check(G, 600):
                                staying_Girls.append(G)
                            elif G == StormX:
                                if approval_check(G, 700, "LO"):
                                    staying_Girls.append(G)
                            elif approval_check(G, 1200,Alt=[[KittyX], 1400]) or (approval_check(G, 600,Alt=[[KittyX],700]) and G.seen_breasts and G.seen_pussy):
                                staying_Girls.append(G)
                            elif line == "spot" and approval_check(G, 1000, "LI",Alt=[[KittyX], 1200]):
                                staying_Girls.append(G)
                            elif line == "watch you" and approval_check(G, 600, "O",Alt=[[EmmaX],500]):
                                staying_Girls.append(G)

                if line == "spot":
                    if staying_Girls:
                        if staying_Girls[0] == RogueX:
                            ch_r "Fine, I could use another scrub."
                        elif staying_Girls[0] == KittyX:
                            ch_k "Oh, I guess I could take another pass at it."
                        elif staying_Girls[0] == EmmaX:
                            ch_e "I suppose we could take a look. . ."
                        elif staying_Girls[0] == LauraX:
                            ch_l "Well, maybe. . ."
                        elif staying_Girls[0] == JeanX:
                            ch_j "Well. . ."
                        elif staying_Girls[0] == StormX:
                            ch_s "Well, another pass couldn't hurt. . ."
                        elif staying_Girls[0] == JubesX:
                            ch_v "I mean, you can never be -too- clean. . ."

                    if RogueX.location == bg_current and RogueX not in staying_Girls:
                        if staying_Girls:
                            ch_r "Well, [RogueX.player_petname], I think I'm fine."
                        else:
                            ch_r "No, [RogueX.player_petname], I think I'm covered."

                    if KittyX.location == bg_current and KittyX not in staying_Girls:
                        if staying_Girls:
                            ch_k "Oh, well I think I[KittyX.like]got it?"
                            ch_k "See you later, [KittyX.player_petname]."
                        else:
                            ch_k "Ha, I'm squeaky clean, [KittyX.player_petname], see you later."

                    if EmmaX.location == bg_current and EmmaX not in staying_Girls:
                        if staying_Girls:
                            ch_e "Well it appears you'll be taken care of."
                            ch_e "I'll be going, [EmmaX.player_petname]."
                        else:
                            ch_e "I'm afraid not, [EmmaX.player_petname], I'll be going."

                    if LauraX.location == bg_current and LauraX not in staying_Girls:
                        if staying_Girls:
                            ch_l "Looks like you got this handled."
                            ch_l "I'm out, [LauraX.player_petname]."
                        else:
                            ch_l "I'm out."

                    if JeanX.location == bg_current and JeanX not in staying_Girls:
                        if staying_Girls:
                            ch_j "Well, looks like you guys are going to have fun."
                            ch_j "I'll head out, [JeanX.player_petname]."
                        else:
                            ch_j "I'll head out."

                    if StormX.location == bg_current and StormX not in staying_Girls:
                        if staying_Girls:
                            ch_s "It looks like you'll be occupied."
                            ch_s "I'll be going, [StormX.player_petname]."
                        else:
                            ch_s "I really doubt that I could have, [StormX.player_petname], I'll be going."

                    if JubesX.location == bg_current and JubesX not in staying_Girls:
                        if staying_Girls:
                            ch_v "Nah, I think you'll be fine."
                            ch_v "Later, guys."
                        else:
                            ch_v "Nah, I'm good. Later, [JubesX.player_petname]."
                elif line == "watch me":
                    if staying_Girls:
                        if staying_Girls[0] == RogueX:
                            ch_r "Yeah, I guess I do enjoy the view."
                        elif staying_Girls[0] == KittyX:
                            ch_k "I. . . guess I wouldn't mind that. . ."
                        elif staying_Girls[0] == LauraX:
                            ch_l "Ok, let's see what you got."
                        elif staying_Girls[0] == JeanX:
                            ch_j "Ohh, this should be good. . ."
                        elif staying_Girls[0] == StormX:
                            ch_s "I suppose that I could. . ."
                        elif staying_Girls[0] == JubesX:
                            ch_v ". . . Yeah, ok."

                    if RogueX.location == bg_current and RogueX not in staying_Girls:
                        if staying_Girls:
                            ch_r "Oh, well, I'm gonna pass on that, [RogueX.player_petname]."
                        else:
                            ch_r "Yeah, I'm gonna pass on that, [RogueX.player_petname]."

                    if KittyX.location == bg_current and KittyX not in staying_Girls:
                        if staying_Girls:
                            ch_k "Well, [KittyX.like]I don't need to see that."
                            ch_k "See you later, [KittyX.player_petname]."
                        else:
                            ch_k "[KittyX.Like]I don't need to see that."

                    if EmmaX.location == bg_current and EmmaX not in staying_Girls:
                        if staying_Girls:
                            ch_e "You appear to have enough of an audience."
                            ch_e "I'll be going, [EmmaX.player_petname]."
                        else:
                            ch_e "I think I'll be fine, [EmmaX.player_petname], I'll be going."

                    if LauraX.location == bg_current and LauraX not in staying_Girls:
                        if staying_Girls:
                            ch_l "She's got you covered."
                            ch_l "I'm out, [LauraX.player_petname]."
                        else:
                            ch_l "I'm out."

                    if JeanX.location == bg_current and JeanX not in staying_Girls:
                        if staying_Girls:
                            ch_j "Well, looks like you guys are going to have fun."
                            ch_j "I'll head out, [JeanX.player_petname]."
                        else:
                            ch_j "I'll head out."

                    if StormX.location == bg_current and StormX not in staying_Girls:
                        if staying_Girls:
                            ch_s "Oh, I think someone else wants the show."
                            ch_s "I'll be going, [StormX.player_petname]."
                        else:
                            ch_s "I don't see why I would, [StormX.player_petname]. I'll be going."

                    if JubesX.location == bg_current and JubesX not in staying_Girls:
                        if staying_Girls:
                            ch_v "Um, no thanks. . ."
                            ch_v "See you later, [JubesX.player_petname]."
                        else:
                            ch_v "Um, no thanks."
                elif line == "watch you":
                    if staying_Girls:
                        if staying_Girls[0] == RogueX:
                            ch_r "Well, I don't mind putting on a show."
                        elif staying_Girls[0] == KittyX:
                            ch_k "You want to watch me. . ."
                            ch_k "Ok."
                        elif staying_Girls[0] == EmmaX:
                            ch_e "I suppose I can't blame you for that. . ."
                        elif staying_Girls[0] == LauraX:
                            ch_l "Huh. Suit yourself."
                        elif staying_Girls[0] == JeanX:
                            ch_j "Well, we can't have that. . ."
                        elif staying_Girls[0] == StormX:
                            ch_s ". . ."
                        elif staying_Girls[0] == JubesX:
                            ch_v "Well. . . I guess we should make up for that. . ."

                    if RogueX.location == bg_current and RogueX not in staying_Girls:
                        if staying_Girls:
                            ch_r "Really? Well not me."
                            ch_r "Have fun, [RogueX.player_petname]."
                        else:
                            ch_r "Keep dreaming, [RogueX.player_petname]."

                    if KittyX.location == bg_current and KittyX not in staying_Girls:
                        if staying_Girls:
                            ch_k "Seriously?! Well I'm not into that."
                            ch_k "Later, [KittyX.player_petname]."
                        else:
                            ch_k "[KittyX.Like]no way!"

                    if EmmaX.location == bg_current and EmmaX not in staying_Girls:
                        if staying_Girls:
                            ch_e "I wouldn't want to intrude."
                            ch_e "I'll be going."
                        else:
                            ch_e "Hmm, I doubt you could handle it."
                            ch_e "I'll be going."

                    if LauraX.location == bg_current and LauraX not in staying_Girls:
                        if staying_Girls:
                            ch_l "She's got you covered."
                            ch_l "I'm out, [LauraX.player_petname]."
                        else:
                            ch_l "I'm out."

                    if JeanX.location == bg_current and JeanX not in staying_Girls:
                        if staying_Girls:
                            ch_j "Well, looks like you guys are going to have fun."
                            ch_j "I'll head out, [JeanX.player_petname]."
                        else:
                            ch_j "I'll head out."

                    if StormX.location == bg_current and StormX not in staying_Girls:
                        if staying_Girls:
                            ch_s "Well, you two enjoy yourselves."
                            ch_s "I'll be going."
                        else:
                            ch_s "I'm flattered, but no."
                            ch_s "I'll be going."

                    if JubesX.location == bg_current and JubesX not in staying_Girls:
                        if staying_Girls:
                            ch_v "Ok, looks like you two can have fun with that."
                            ch_v "Later, [JubesX.player_petname]."
                        else:
                            ch_v "Yeah, no way."

            if len(staying_Girls) > 1:
                if staying_Girls[1].likes[staying_Girls[0].tag] > 500:
                    if staying_Girls[1] == RogueX:
                        ch_r "I guess I could too."
                    elif staying_Girls[1] == EmmaX:
                        ch_e "I suppose I don't want to be left out of this. . ."
                    elif staying_Girls[1] == JeanX:
                        ch_j "Well, it does look like fun. . ."
                else:
                    if staying_Girls[1] == RogueX:
                        ch_r "Well I guess if she's in, I am too!"
                    elif staying_Girls[1] == EmmaX:
                        ch_e "I wouldn't want to leave you alone with. . . this."
                    elif staying_Girls[1] == JeanX:
                        ch_j "Hmm, maybe I should stick around. . ."

                    if staying_Girls[1] == KittyX:
                        ch_k "I- yeah, me neither!"
                    elif staying_Girls[1] == LauraX:
                        ch_l "Fine."
                    elif staying_Girls[1] == StormX:
                        ch_s "Well I suppose I should join you. . ."
                    elif staying_Girls[1] == JubesX:
                        ch_v "Um, yeah, let's do this."

        $ temp_Girls = showering_Girls[:]

        while temp_Girls:
            if temp_Girls[0].location == bg_current:
                if temp_Girls[0] in staying_Girls:
                    $ temp_Girls[0].change_outfit("nude")
                    $ temp_Girls[0].wet = True

                    python:
                        for key in temp_Girls[0].spunk.keys():
                            temp_Girls[0].spunk[key] = False

                    $ temp_Girls[0].recent_history.append("showered")
                    $ temp_Girls[0].daily_history.append("showered")

                    call expression temp_Girls[0].tag + "_First_Bottomless" pass (1)
                    call expression temp_Girls[0].tag + "_First_Topless" pass (1)
                else:
                    call remove_girl(temp_Girls[0])

                while temp_Girls[0] in Nearby:
                    $ Nearby.remove(temp_Girls[0])

            $ temp_Girls.remove(temp_Girls[0])

    call Seen_First_Peen (0, 0, 0, 1)

    while len(staying_Girls) >= 2 and staying_Girls[1] in Nearby:
        $ Nearby.remove(staying_Girls[1])

    while staying_Girls and staying_Girls[0] in Nearby:
        $ Nearby.remove(staying_Girls[0])

    if Nearby and len(staying_Girls) < 2:
        $ renpy.random.shuffle(Nearby)

        while Nearby and (len(Nearby) + len(staying_Girls)) > 2:
            $ Nearby.remove(Nearby[0])

        if len(Nearby) >= 2:
            "As you finish getting undressed, [Nearby[0].name] and [Nearby[1].name] enter the room."

            $ Nearby[1].location = bg_current
        else:
            "As you finish getting undressed, [Nearby[0].name] enters the room."

        $ Nearby[0].location = bg_current

        $ intruding_Girls = Nearby[:]

        call set_the_scene(check_if_dressed = False)
        call Seen_First_Peen (0, 0, 1, 1)

        if RogueX in intruding_Girls:
            if RogueX.seen_peen == 1:
                $ RogueX.change_face("_surprised",2,eyes = "_down")

                ch_r "Oh!"

                $ RogueX.change_face("_bemused", 1,eyes = "_side")

                ch_r "I am so sorry, I should {i}not{/i} have just barged in like that."
            else:
                $ RogueX.change_face("_bemused", 1,eyes = "_side")

                ch_r "I simply {i}must{/i} be more careful. . ."

        if KittyX in intruding_Girls:
            $ KittyX.change_face("_bemused",2,eyes = "_side")

            if KittyX.seen_peen == 1:
                ch_k "Sorry! Sorry! I need to stop just casually phasing into places!"
            else:
                ch_k "I have {i}got{/i} to knock more. . ."

        if EmmaX in intruding_Girls:
            if EmmaX.seen_peen == 1:
                $ EmmaX.change_face("_surprised")

                ch_e "Oh! Dreadfully sorry."

                $ EmmaX.change_face("_sexy", eyes = "_down")

                ch_e "I hope we can meet again under. . . different circumstances."
            else:
                $ EmmaX.change_face("_sexy", eyes = "_down")

                ch_e "I really should pay closer attention. . ."

            if "classcaught" not in EmmaX.history or ((staying_Girls or len(Nearby) >= 2) and "threesome" not in EmmaX.history):
                "[EmmaX.name] decides to leave immediately."

                call remove_girl(EmmaX)

                $ intruding_Girls.remove(EmmaX)

                $ EmmaX.change_outfit()

        if LauraX in intruding_Girls:
            if LauraX.seen_peen == 1:
                $ LauraX.change_face("_surprised", eyes = "_down")

                ch_l "Hey. That's interesting. . ."
            else:
                $ LauraX.change_face("_normal", eyes = "_down")

                ch_l ". . ."

                $ LauraX.change_face("_normal")

                ch_l "I'm supposed to knock, aren't I."

        if JeanX in intruding_Girls:
            if JeanX.seen_peen == 1:
                $ JeanX.change_face("_surprised", eyes = "_down")

                ch_j "Well what do we have here? . ."
            else:
                $ JeanX.change_face("_normal", eyes = "_down")

                ch_j ". . ."

                $ JeanX.change_face("_normal")

                ch_j "Oh, nice to catch you. . . like this. . ."

        if StormX in intruding_Girls:
            if StormX.seen_peen == 1:
                $ StormX.change_face("_surprised")

                ch_s "Oh! Hello there."

                $ StormX.change_face("_sexy", eyes = "_down")

                ch_s "And hello to you as well. . ."
            else:
                $ StormX.change_face("_sexy", eyes = "_down")

                ch_s "I'm sorry to intrude. . ."

            $ StormX.change_face("_sexy")

        if JubesX in intruding_Girls:
            $ JubesX.change_face("_bemused",2,eyes = "_side")

            if JubesX.seen_peen == 1:
                ch_v "Oh, sorry! I wasn't paying attention."

                $ JubesX.eyes = "_down"

                pause 1

                $ JubesX.eyes = "_side"

                ch_v "um. . . hey. . ."
            else:
                ch_v "Oh, sorry! I wasn't paying attention."

        if EmmaX in staying_Girls and "threesome" not in EmmaX.history:
            if len(intruding_Girls) >= 2:
                "Seeing the other girls arrive, [EmmaX.name] quickly excuses herself."
            else:
                "Seeing [intruding_Girls[0].name] arrive, [EmmaX.name] quickly excuses herself."

            $ staying_Girls.remove(EmmaX)

            call remove_girl(EmmaX)

            $ EmmaX.change_outfit()

        if intruding_Girls:
            if approval_check(intruding_Girls[0], 1200):
                $ staying_Girls.append(intruding_Girls[0])

            if len(intruding_Girls) >=2 and approval_check(intruding_Girls[1], 1200) and len(staying_Girls) < 2:
                $ staying_Girls.append(intruding_Girls[1])

            if len(intruding_Girls) >=2:
                if intruding_Girls[0] not in staying_Girls and intruding_Girls[1] not in staying_Girls:
                    "They both turn right back around."

                    call remove_girl(intruding_Girls[0])
                    call remove_girl(intruding_Girls[1])

                    $ intruding_Girls = []
                elif intruding_Girls[0] not in staying_Girls:
                    "[intruding_Girls[0].name] turns right back around, but [intruding_Girls[1].name] stays."

                    call remove_girl(intruding_Girls[0])

                    $ intruding_Girls.remove(intruding_Girls[0])
                elif intruding_Girls[1] not in staying_Girls:
                    "[intruding_Girls[1].name] turns right back around, but [intruding_Girls[0].name] stays."

                    call remove_girl(intruding_Girls[1])

                    $ intruding_Girls.remove(intruding_Girls[1])
            elif intruding_Girls[0] not in staying_Girls:
                "[intruding_Girls[0].name] turns right back around."

                call remove_girl(intruding_Girls[0])

                $ intruding_Girls.remove(intruding_Girls[0])

            while intruding_Girls:
                $ intruding_Girls[0].change_outfit("nude")
                $ intruding_Girls[0].wet = True

                python:
                    for key in intruding_Girls[0].spunk.keys():
                        intruding_Girls[0].spunk[key] = False

                $ intruding_Girls[0].recent_history.append("showered")
                $ intruding_Girls[0].daily_history.append("showered")

                call expression intruding_Girls[0].tag + "_First_Bottomless" pass (1)
                call expression intruding_Girls[0].tag + "_First_Topless" pass (1)

                if intruding_Girls[0] == RogueX:
                    ch_r "I wouldn't mind stick'in around though."
                elif intruding_Girls[0] == KittyX:
                    ch_k "I {i}could{/i} get in on this."
                elif intruding_Girls[0] == EmmaX:
                    ch_e "But, I could use some face time."
                elif intruding_Girls[0] == LauraX:
                    ch_l "Scoot over."
                elif intruding_Girls[0] == JeanX:
                    ch_j "You're hogging the water."
                elif intruding_Girls[0] == StormX:
                    ch_s "Oh, goodbye then. . ."
                elif intruding_Girls[0] == JubesX:
                    ch_v "Well, I could always join ya."

                $ intruding_Girls.remove(intruding_Girls[0])

    $ round -= 30 if round >= 30 else round

    if staying_Girls:
        if len(staying_Girls) > 1 and staying_Girls[0] == staying_Girls[1]:
            $ staying_Girls.remove(staying_Girls[0])
        if len(staying_Girls) > 1:
            call shift_focus (staying_Girls[0], staying_Girls[1])

            "You take a quick shower with [staying_Girls[0].name] and [staying_Girls[1].name]."
        else:
            call shift_focus (staying_Girls[0])

            "You take a quick shower with [staying_Girls[0].name]."

        call Shower_Sex

        if staying_Girls[0] == RogueX:
            ch_r "That was real nice, [RogueX.player_petname]."
        elif staying_Girls[0] == KittyX:
            ch_k "That was. . . nice."
        elif staying_Girls[0] == EmmaX:
            ch_e "That was. . . distracting."
        elif staying_Girls[0] == LauraX:
            ch_l "Well that was fun."
        elif staying_Girls[0] == JeanX:
            ch_j "That was fun."
        elif staying_Girls[0] == StormX:
            ch_s "Ah, that was relaxing."
        elif staying_Girls[0] == JubesX:
            ch_v "That was fun, [JubesX.player_petname]."

        if len(staying_Girls) > 1:
            if staying_Girls[1] == RogueX:
                ch_r "Yeah."
            elif staying_Girls[1] == KittyX:
                ch_k "Yeah, I had fun."
            elif staying_Girls[1] == EmmaX:
                ch_e "Indeed."
            elif staying_Girls[1] == LauraX:
                ch_l "Yup."
            elif staying_Girls[1] == JeanX:
                ch_j "Yeah, it was."
            elif staying_Girls[1] == StormX:
                ch_s "Certainly."
            elif staying_Girls[1] == JubesX:
                ch_v "Yeah, totally."
    else:
        $ line = "You take a quick shower" + renpy.random.choice([". It was fairly uneventful.",
            ". A few people came and went as you did so.",
            ". That was refreshing."])
        "[line]"

    $ Player.recent_history.append("showered")
    $ Player.daily_history.append("showered")

    if "scent" in Player.daily_history:
        $ Player.daily_history.remove("scent")

    call Get_Dressed

    if RogueX.location == bg_current:
        $ RogueX.change_outfit("shower")

    if KittyX.location == bg_current:
        $ KittyX.change_outfit("shower")

    if EmmaX.location == bg_current:
        $ EmmaX.change_outfit("shower")

    if LauraX.location == bg_current:
        $ LauraX.change_outfit("shower")

    if JeanX.location == bg_current:
        $ JeanX.change_outfit("shower")

    if JubesX.location == bg_current:
        $ JubesX.change_outfit("shower")

    return

label Shower_Sex(Options=0, line=0):

    if len(staying_Girls) > 1 and (approval_check(staying_Girls[1], 1800,Check=1) > approval_check(staying_Girls[0], 1800,Check=1)):
        $ renpy.random.shuffle(staying_Girls)
    call shift_focus (staying_Girls[0])

    $ D20 = renpy.random.randint(1,20)
    $ D20 += 5 if approval_check(staying_Girls[0], 1800) else 0

    if "showered" in Player.recent_history:
        $ D20 = 0

    $ staying_Girls[0].change_face("_sly")

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
            $ staying_Girls[0].change_stat("lust", 50, 15)
            $ staying_Girls[1].change_stat("lust", 50, 15)
            $ staying_Girls[0].change_stat("lust", 90, 10)
            $ staying_Girls[1].change_stat("lust", 90, 10)
            "You got a good look at them washing off, and they didn't seem to mind the view either."
            $ staying_Girls[0].check_if_likes(staying_Girls[1],600,4, 1)
            $ staying_Girls[1].check_if_likes(staying_Girls[0],600,4, 1)
            $ staying_Girls[0].check_if_likes(staying_Girls[1],800,2, 1)
            $ staying_Girls[1].check_if_likes(staying_Girls[0],800,2, 1)
        else:
            $ staying_Girls[0].change_stat("lust", 50, 15)
            $ staying_Girls[0].change_stat("lust", 90, 10)
            "You got a good look at her washing off, and she didn't seem to mind the view either."
        return

    if line:
        if len(staying_Girls) > 1:
            $ staying_Girls[0].change_stat("lust", 50, 5)
            $ staying_Girls[0].change_stat("lust", 70, 3)
            $ staying_Girls[1].change_stat("lust", 50, 5)
            $ staying_Girls[1].change_stat("lust", 70, 3)
        else:
            $ staying_Girls[0].change_stat("lust", 50, 6)
            $ staying_Girls[0].change_stat("lust", 70, 3)
        $ Player.change_stat("focus", 50, 5)
        $ Player.change_stat("focus", 80, 2)
        menu:
            extend ""
            "Continue?":
                pass
            "Stop her." if len(staying_Girls) < 2:
                $ line = 0
                call reset_position(staying_Girls[0])
                "You take a step back, pulling away from her."
                $ staying_Girls[0].change_stat("love", 80, -1)
                $ staying_Girls[0].change_stat("obedience", 80, 5)
                $ staying_Girls[0].change_stat("inhibition", 80, -1)
                $ staying_Girls[0].change_face("_sad")
                "She seems a bit disappointed."
            "Stop them." if len(staying_Girls) > 1:
                $ line = 0
                call reset_position(staying_Girls[0])
                call reset_position(staying_Girls[1])
                "You take a step back, pulling away from them."
                $ staying_Girls[0].change_stat("love", 80, -1)
                $ staying_Girls[0].change_stat("obedience", 80, 5)
                $ staying_Girls[0].change_stat("inhibition", 80, -1)
                $ staying_Girls[1].change_stat("obedience", 80, 5)
                $ staying_Girls[1].change_stat("inhibition", 80, -1)
                $ staying_Girls[0].change_face("_sad")
                $ staying_Girls[1].change_face("_sad")
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
            $ staying_Girls[0].change_stat("lust", 50, 5)
            $ staying_Girls[0].change_stat("lust", 70, 2)
            $ staying_Girls[1].change_stat("lust", 50, 7)
            $ staying_Girls[1].change_stat("lust", 70, 3)
            $ Player.change_stat("focus", 50, 8)
            $ Player.change_stat("focus", 80, 4)
            "[line] reaches over to [staying_Girls[1].name] and begins soaping up her chest."
        elif Options[0] == 3:
            $ staying_Girls[0].change_stat("lust", 50, 7)
            $ staying_Girls[0].change_stat("lust", 70, 3)
            $ staying_Girls[1].change_stat("lust", 50, 8)
            $ staying_Girls[1].change_stat("lust", 70, 4)
            $ Player.change_stat("focus", 50, 8)
            $ Player.change_stat("focus", 80, 5)
            "[line] reaches over to [staying_Girls[1].name] and begins soaping up her pussy."


        elif Options[0] == 4:
            if len(staying_Girls) > 1:
                $ staying_Girls[0].change_stat("lust", 50, 10)
                $ staying_Girls[0].change_stat("lust", 70, 7)
            else:
                $ staying_Girls[0].change_stat("lust", 50, 8)
                $ staying_Girls[0].change_stat("lust", 70, 5)
            $ Player.change_stat("focus", 50, 10)
            $ Player.change_stat("focus", 80, 6)
            "[line] reaches down and takes your cock in her hand, soaping it up."
        elif Options[0] == 5:
            if len(staying_Girls) > 1:
                $ staying_Girls[0].change_stat("lust", 50, 12)
                $ staying_Girls[0].change_stat("lust", 70, 8)
            else:
                $ staying_Girls[0].change_stat("lust", 50, 9)
                $ staying_Girls[0].change_stat("lust", 70, 6)
            $ Player.change_stat("focus", 50, 10)
            $ Player.change_stat("focus", 80, 4)
            "[line] kneels down and wraps her breasts around your cock, soaping it up."


        elif Options[0] == 6:
            if len(staying_Girls) > 1:
                $ staying_Girls[0].change_stat("lust", 50, 11)
                $ staying_Girls[0].change_stat("lust", 70, 6)
            else:
                $ staying_Girls[0].change_stat("lust", 50, 9)
                $ staying_Girls[0].change_stat("lust", 70, 5)
            $ Player.change_stat("focus", 50, 9)
            $ Player.change_stat("focus", 80, 4)
            "[line] reaches down and begins fondling her own pussy, building a nice lather."
        elif Options[0] == 7:
            if len(staying_Girls) > 1:
                $ staying_Girls[0].change_stat("lust", 50, 10)
                $ staying_Girls[0].change_stat("lust", 70, 5)
            else:
                $ staying_Girls[0].change_stat("lust", 50, 9)
                $ staying_Girls[0].change_stat("lust", 70, 4)
            $ Player.change_stat("focus", 50, 8)
            $ Player.change_stat("focus", 80, 3)
            "[line] begins rubbing her own breasts in circles, building a nice lather."


        elif Options[0] == 8:
            $ staying_Girls[0].change_stat("lust", 50, 6)
            $ staying_Girls[0].change_stat("lust", 70, 3)
            $ Player.change_stat("focus", 50, 7)
            $ Player.change_stat("focus", 80, 3)
            "[line] draws her breasts up and down your arm, the soap bubbles squirting out."
        elif Options[0] == 9:
            $ staying_Girls[0].change_stat("lust", 50, 8)
            $ staying_Girls[0].change_stat("lust", 70, 3)
            $ Player.change_stat("focus", 50, 8)
            $ Player.change_stat("focus", 80, 3)
            "[line] kneels down and rubs her breasts against your leg, soaping it up."
        elif Options[0] == 10:
            $ staying_Girls[0].change_stat("lust", 50, 7)
            $ staying_Girls[0].change_stat("lust", 70, 3)
            $ Player.change_stat("focus", 50, 6)
            $ Player.change_stat("focus", 80, 3)
            "[line] presses against your back, her soapy breasts rubbing back and forth against it."
        elif Options[0] == 11:
            $ staying_Girls[0].change_stat("lust", 50, 7)
            $ staying_Girls[0].change_stat("lust", 70, 3)
            $ Player.change_stat("focus", 50, 8)
            $ Player.change_stat("focus", 80, 4)
            "[line] presses against your chest, her soapy breasts rubbing back and forth against it."
        elif Options[0] == 1:
            $ staying_Girls[0].change_stat("lust", 50, 5)
            $ staying_Girls[0].change_stat("lust", 70, 2)
            $ Player.change_stat("focus", 50, 6)
            $ Player.change_stat("focus", 80, 3)
            "[line] stares silently at you as she moves her hands along her soapy body. . ."
            $ line = 0

    if line and len(staying_Girls) > 1:

        $ D20 += 5 if approval_check(staying_Girls[1], 1800) else 0
        if staying_Girls[1].likes[staying_Girls[0].tag] <= 800 and 2 <= Options[0] <=3:
            $ D20 -= 5
        if staying_Girls[1].likes[staying_Girls[0].tag] <= 600:
            $ D20 -= 5

        if 2 <= Options[0] <= 3:

            if approval_check(staying_Girls[1], 1300) and staying_Girls[1].likes[staying_Girls[0].tag] >= 800:
                $ staying_Girls[1].change_face("_sexy", 1)
                $ staying_Girls[0].change_stat("lust", 50, 5)
                $ staying_Girls[0].change_stat("lust", 70, 5)
                $ staying_Girls[1].change_stat("lust", 50, 12)
                $ staying_Girls[1].change_stat("lust", 70, 12)
                call close_launch(staying_Girls[0], staying_Girls[1])
                "[staying_Girls[1].name] seems really into this, and returns the favor."
                $ Player.change_stat("focus", 50, 7)
                $ Player.change_stat("focus", 80, 3)
                $ line = 4
            elif approval_check(staying_Girls[1], 1200) and staying_Girls[1].likes[staying_Girls[0].tag] >= 700:
                $ staying_Girls[1].change_face("_sexy",2,eyes = "_closed")
                $ staying_Girls[1].change_stat("lust", 50, 10)
                $ staying_Girls[1].change_stat("lust", 70, 10)
                $ Player.change_stat("focus", 50, 5)
                $ Player.change_stat("focus", 80, 3)
                call close_launch(staying_Girls[0], staying_Girls[1])
                "[staying_Girls[1].name] seems really into this, and leans into it."
            else:
                $ staying_Girls[1].change_stat("lust", 50, 10)
                $ staying_Girls[1].change_face("_sadside", brows = "_confused")
                "[staying_Girls[1].name] doesn't really seem to appreciate this."
                "She pulls away."
                $ line = 3
        else:

            if (approval_check(staying_Girls[1], 1300) and staying_Girls[1].likes[staying_Girls[0].tag] >= 700) or approval_check(staying_Girls[1], 2000):
                if Options[0] == 5:
                    $ staying_Girls[1].change_stat("lust", 50, 10)
                    $ staying_Girls[1].change_stat("lust", 70, 5)
                    $ Player.change_stat("focus", 50, 6)
                    $ Player.change_stat("focus", 80, 3)
                    call close_launch(staying_Girls[0], staying_Girls[1])
                    "[staying_Girls[1].name] seems really into this, slowly rubbing against you as she watches."
                else:
                    $ staying_Girls[1].change_stat("lust", 50, 10)
                    $ staying_Girls[1].change_stat("lust", 70, 5)
                    $ Player.change_stat("focus", 50, 5)
                    $ Player.change_stat("focus", 80, 3)
                    call close_launch(staying_Girls[0], staying_Girls[1])
                    "[staying_Girls[1].name] seems really into this, and joins her on the other side."
                $ line = 4
            elif ((approval_check(staying_Girls[1], 1200) and staying_Girls[1].likes[staying_Girls[0].tag] >= 600)) or approval_check(staying_Girls[1], 1600):
                $ staying_Girls[1].change_face("_sexy",2,eyes = "_down")
                $ staying_Girls[1].change_stat("lust", 50, 10)
                $ staying_Girls[1].change_stat("lust", 70, 5)
                "[staying_Girls[1].name] seems really into this, and watches her do it."
            else:
                $ staying_Girls[1].change_face("_sadside", brows = "_confused")
                $ staying_Girls[1].change_stat("lust", 50, 5)
                "[staying_Girls[1].name] doesn't really seem to appreciate this."
                $ line = 3
    if line:
        menu:
            extend ""
            "Continue?":
                pass
            "Stop her." if len(staying_Girls) < 2:
                $ line = 0
                call reset_position(staying_Girls[0])
                "You take a step back, pulling away from her."
                $ staying_Girls[0].change_stat("love", 80, -2)
                $ staying_Girls[0].change_stat("obedience", 80, 5)
                $ staying_Girls[0].change_stat("inhibition", 80, -2)
                $ staying_Girls[0].change_face("_sad")
                "She seems a bit disappointed."
            "Stop them." if len(staying_Girls) > 1:
                $ line = 0
                call reset_position(staying_Girls[0])
                call reset_position(staying_Girls[1])
                "You take a step back, pulling away from them."
                $ staying_Girls[0].change_face("_sad")
                $ staying_Girls[0].change_stat("love", 80, -2)
                $ staying_Girls[0].change_stat("obedience", 80, 5)
                $ staying_Girls[0].change_stat("inhibition", 80, -2)
                if line == 3:
                    $ staying_Girls[1].change_stat("love", 80, 4)
                    $ staying_Girls[1].change_stat("obedience", 80, 5)
                    $ staying_Girls[1].change_face("_bemused")
                    "[staying_Girls[0].name] seems a bit disappointed, but [staying_Girls[1].name] seems pleased."
                else:
                    $ staying_Girls[1].change_stat("love", 80, -1)
                    $ staying_Girls[1].change_stat("obedience", 80, 5)
                    $ staying_Girls[1].change_stat("inhibition", 80, -1)
                    $ staying_Girls[1].change_face("_sad")
                    "They seem a bit disappointed."

    if line:

        if len(staying_Girls) > 1 and line != 3:
            $ staying_Girls[0].check_if_likes(staying_Girls[1],600,4, 1)
            $ staying_Girls[1].check_if_likes(staying_Girls[0],600,4, 1)
            $ staying_Girls[0].check_if_likes(staying_Girls[1],800,3, 1)
            $ staying_Girls[1].check_if_likes(staying_Girls[0],800,3, 1)
            $ staying_Girls[0].check_if_likes(staying_Girls[1],900, 1, 1)
            $ staying_Girls[1].check_if_likes(staying_Girls[0],900, 1, 1)
        if 2 <= Options[0] <= 3 and D20 >= 15:

            $ staying_Girls[1].check_if_likes(staying_Girls[0],900,4, 1)
            $ Player.change_stat("focus", 50, 10)
            $ Player.change_stat("focus", 80, 5)
            "After a few minutes of this, it looks like [staying_Girls[1].name] gets off."
            call Girl_Cumming (staying_Girls[1], 1)
            if line == 4:
                $ staying_Girls[0].check_if_likes(staying_Girls[1],900,3, 1)
                "It looks like [staying_Girls[0].name] is reacting positively to it as well. . ."
                call Girl_Cumming (staying_Girls[0], 1)
            if len(staying_Girls) > 1:
                "The girls take a step back."
                call reset_position(staying_Girls[1])
            else:
                "[staying_Girls[0].name] takes a step back."

            call reset_position(staying_Girls[0])

        elif 4 <= Options[0] <= 5 and D20 >= 10:

            $ Player.focus = 15
            if Options[0] == 5:
                $ staying_Girls[0].spunk["breasts"] = True

            if line == 4:
                $ staying_Girls[0].change_stat("inhibition", 90, 7)
                $ staying_Girls[1].change_stat("inhibition", 90, 4)
                $ staying_Girls[0].check_if_likes(staying_Girls[1],900,3, 1)
                $ staying_Girls[1].check_if_likes(staying_Girls[0],900,3, 1)
                "After a few minutes of this, the two of them manage to get you off."
            else:
                $ staying_Girls[0].change_stat("inhibition", 90, 5)
                "After a few minutes of this, she manages to get you off."
            "A little more work is needed to clean up the mess."
            if Options[0] == 5:
                python:
                    for key in staying_Girls[0].spunk.keys():
                        staying_Girls[0].spunk[key] = False
            if len(staying_Girls) > 1:
                "The girls take a step back."
                call reset_position(staying_Girls[1])
            else:
                "[staying_Girls[0].name] takes a step back."
            call reset_position(staying_Girls[0])

        elif 6 <= Options[0] <= 7 and D20 >= 15:

            $ staying_Girls[0].change_stat("inhibition", 90, 7)
            $ Player.change_stat("focus", 50, 15)
            $ Player.change_stat("focus", 80, 5)
            "After a few minutes of this, it looks like [staying_Girls[0].name] gets off."
            call Girl_Cumming (staying_Girls[0], 1)
            if line == 4:
                $ staying_Girls[1].change_stat("inhibition", 90, 6)
                $ staying_Girls[0].check_if_likes(staying_Girls[1],900,3, 1)
                "It looks like [staying_Girls[1].name] is enjoying herself as well. . ."
                call Girl_Cumming (staying_Girls[1], 1)
            if len(staying_Girls) > 1:
                $ staying_Girls[1].check_if_likes(staying_Girls[0],900,3, 1)
                "The girls take a step back."
                call reset_position(staying_Girls[1])
            else:
                "[staying_Girls[0].name] takes a step back."
            call reset_position(staying_Girls[0])
        else:

            if len(staying_Girls) > 1:
                call reset_position(staying_Girls[1])
            call reset_position(staying_Girls[0])
            $ Player.change_stat("focus", 50, 15)
            $ Player.change_stat("focus", 80, 5)
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
    call shift_focus (staying_Girls[0])
    return


label change_out_of_towels:
    $ temp_Girls = all_Girls[:]

    while temp_Girls:
        if temp_Girls[0].location == "bg_showerroom":
            $ temp_Girls[0].add_word(1, "showered", "showered")

        if "met" in temp_Girls[0].history and temp_Girls[0] not in Party:
            $ temp_Girls[0].location = temp_Girls[0].weekly_schedule[weekday][time_index]

        $ temp_Girls[0].change_outfit(temp_Girls[0].today_outfit_name)
        $ temp_Girls.remove(temp_Girls[0])

    return
