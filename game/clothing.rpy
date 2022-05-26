label alternate_clothes(Girl, outfit = 1):
    if Girl.clothing[outfit] == 1 or not Girl.clothing[outfit]:
        $ Girl.outfit_name = "casual1"
    elif Girl.clothing[outfit] == 2:
        $ Girl.outfit_name = "casual2"
    elif Girl.clothing[outfit] == 4:
        $ Girl.outfit_name = "gym_clothes"
    elif Girl.clothing[outfit] == 7:
        $ Girl.outfit_name = "sleepwear"
    elif Girl.clothing[outfit] == 10:
        $ Girl.outfit_name = "swimwear"
    elif Girl.clothing[outfit] == 3:
        $ Girl.outfit_name = "custom1"
    elif Girl.clothing[outfit] == 5:
        $ Girl.outfit_name = "custom2"
    elif Girl.clothing[outfit] == 6:
        $ Girl.outfit_name = "custom3"
    else:
        $ Girl.outfit_name = "casual1"

    return

label set_clothes_schedule(Girl):
    call shift_focus(Girl)

    $ counter = 0

    if approval_check(Girl, 1500, "LO"):
        if Girl == RogueX:
            ch_r "So, you'd like to choose what I wear for the week? Ok, shoot."
        elif Girl == KittyX:
            ch_k "Let me know what you like."
        elif Girl == EmmaX:
            ch_e "I'm open to suggestions."
        elif Girl == LauraX:
            ch_l "Fine, you pick, whatever."
        elif Girl == JeanX:
            ch_j "Ok, I'm tired of having to pick outfits. . ."
        elif Girl == StormX:
            ch_s "I'm willing to listen."
        elif Girl == JubesX:
            ch_v "What're you thinking?"

        $ counter = 3
    elif approval_check(Girl, 1200, "LO"):
        if Girl == RogueX:
            ch_r "I guess I could set aside a few schooldays for you."
        elif Girl == KittyX:
            ch_k "I could let you pick a few days. . ."
        elif Girl == EmmaX:
            ch_e "I could let you choose a few days. . ."
        elif Girl == LauraX:
            ch_l "I don't know, you could pick a few days. . ."
        elif Girl == JeanX:
            ch_j "I guess you do have some taste. . ."
        elif Girl == StormX:
            ch_s "I suppose you could choose a few days. . ."
        elif Girl == JubesX:
            ch_v "You could help with a few days?"

        $ counter = 2
    elif approval_check(Girl, 1000, "LO"):
        if Girl == RogueX:
            ch_r "We can talk about what I wear outside of classes."
        elif Girl == KittyX:
            ch_k "We could talk about weekends, maybe. . ."
        elif Girl == EmmaX:
            ch_e "Perhaps when I'm off the clock. . ."
        elif Girl == LauraX:
            ch_l "Maybe on weekends. . ."
        elif Girl == JeanX:
            ch_j "I guess my weekends are free. . ."
        elif Girl == StormX:
            ch_s "Perhaps when I'm not working. . ."
        elif Girl == JubesX:
            ch_v "I don't know, weekends maybe?"

        $ counter = 1
    else:
        if Girl == RogueX:
            ch_r "You know, I don't really need fashion advice from you."
        elif Girl == KittyX:
            ch_k "I think I'll[Girl.like]figure out my own outfits."
        elif Girl == EmmaX:
            ch_e "I'd prefer to handle my own wardrobe."
        elif Girl == LauraX:
            ch_l "Nah, I got it covered."
        elif Girl == JeanX:
            ch_j "Huh? No."
        elif Girl == StormX:
            ch_s "I think I'd rather choose my own clothing."
        elif Girl == JubesX:
            ch_v "Nah, I'll figure it out myself."

        return

    while True:
        menu:
            extend ""
            "Every day":
                "This sets her outfit for every day of the week in one go."
                "This overwrites the default schedule, and any scheduling you've already made."
                "Any choices you make later will overwrite this choice."

                menu:
                    "Pick an outfit to wear":
                        call choose_outfit

                        if counter > 1:
                            $ Girl.clothing[0] = _return
                            $ Girl.clothing[2] = _return
                            $ Girl.clothing[4] = _return
                        if counter > 2:
                            $ Girl.clothing[1] = _return
                            $ Girl.clothing[3] = _return

                        $ Girl.clothing[5] = _return
                        $ Girl.clothing[6] = _return
                    "Never mind.":
                        pass
            "Days":
                menu:
                    "On Monday you should wear. . ." if counter > 1:
                        call choose_outfit

                        $ Girl.clothing[0] = _return
                    "On Monday you should wear. . . (locked)" if counter <= 1:
                        pass
                    "On Tuesday you should wear. . ." if counter > 2:
                        call choose_outfit

                        $ Girl.clothing[1] = _return
                    "On Tuesday you should wear. . . (locked)" if counter <= 2:
                        pass
                    "On Wednesday you should wear. . ." if counter > 1:
                        call choose_outfit

                        $ Girl.clothing[2] = _return
                    "On Wednesday you should wear. . . (locked)" if counter <= 1:
                        pass
                    "On Thursday you should wear. . ." if counter > 2:
                        call choose_outfit

                        $ Girl.clothing[3] = _return
                    "On Thursday you should wear. . . (locked)" if counter <= 2:
                        pass
                    "On Friday you should wear. . ." if counter > 1:
                        call choose_outfit

                        $ Girl.clothing[4] = _return
                    "On Friday you should wear. . . (locked)" if counter <= 1:
                        pass
                    "On Saturday you should wear. . . (locked)" if counter < 1:
                        pass
                    "On Saturday you should wear. . ." if counter >= 1:
                        call choose_outfit

                        $ Girl.clothing[5] = _return
                    "On Sunday you should wear. . . (locked)" if counter < 1:
                        pass
                    "On Sunday you should wear. . ." if counter >= 1:
                        call choose_outfit

                        $ Girl.clothing[6] = _return
                    "Back":
                        pass
            "Other":
                menu:
                    "In our rooms you should wear. . . (locked)" if counter < 1:
                        pass
                    "In our rooms you should wear. . ." if counter >= 1:
                        call choose_outfit (Girl, 99)

                        $ Girl.clothing[9] = _return
                    "On dates you should wear. . . (locked)" if counter < 1:
                        pass
                    "On dates you should wear. . ." if counter >= 1:
                        call choose_outfit

                        $ Girl.clothing[7] = _return
                    "When teaching you should wear. . . (locked)" if Girl in (EmmaX,StormX) and counter < 3:
                        pass
                    "When teaching you should wear. . ." if Girl in (EmmaX,StormX) and counter >= 3:
                        call choose_outfit (Girl, 90)

                        $ Girl.clothing[8] = _return
                    "Back":
                        pass
            "About gym clothes":
                menu:
                    ch_p "You asked me before about your gym clothes?"
                    "Don't ask before changing into gym clothes" if "no_ask gym" not in Girl.traits:
                        Girl.voice "Sure."

                        $ Girl.traits.append("no_ask gym")
                    "Ask me before changing into gym clothes" if "no_ask gym" in Girl.traits:
                        Girl.voice "Sure."

                        $ Girl.traits.remove("no_ask gym")
                    "Never Mind":
                        pass
            "Private outfit" if Girl.clothing[9]:
                ch_p "You know that outfit you wear in private?"

                if Girl in [EmmaX, StormX]:
                    Girl.voice "Yes?"
                else:
                    Girl.voice "Yeah?"

                menu:
                    extend ""
                    "Just put them on without asking me about it." if "comfy" not in Girl.traits:
                        Girl.voice "Sure."

                        $ Girl.traits.append("comfy")
                    "Ask before changing into that." if "comfy" in Girl.traits:
                        Girl.voice "Sure."

                        $ Girl.traits.remove("comfy")
                    "Never Mind":
                        pass
            "Never mind [[Done]":
                return

    jump set_clothes_schedule

label choose_outfit(Girl, count = 0):
    menu:
        "Your green outfit." if Girl == RogueX:
            $ count = 1
        "That pink outfit, with the jeans." if Girl == RogueX:
            $ count = 2

        "That pink outfit, with the jeans." if Girl == KittyX:
            $ count = 1
        "Your red shirt outfit." if Girl == KittyX:
            $ count = 2

        "That teacher outfit." if Girl == EmmaX:
            $ count = 1
        "Your superhero outfit." if Girl == EmmaX:
            $ count = 2

        "That leather combat look." if Girl == LauraX:
            $ count = 1
        "Your jacket and skirt." if Girl == LauraX:
            $ count = 2

        "That pink shirt and khakis look." if Girl == JeanX:
            $ count = 1
        "Your green shirt and skirt." if Girl == JeanX:
            $ count = 2

        "That white top and skirt look." if Girl == StormX:
            $ count = 1
        "Your black jacket and pants look." if Girl == StormX:
            $ count = 2

        "That red and blue look." if Girl == JubesX:
            $ count = 1
        "Your black top and pants look." if Girl == JubesX:
            $ count = 2

        "That outfit we put together [[custom]":
            if Girl == RogueX:
                ch_r "Which one again?"
            elif Girl == KittyX:
                ch_k "[Girl.Like]which?"
            elif Girl == EmmaX:
                ch_e "Which were you thinking?"
            elif Girl == LauraX:
                ch_l "Which one?"
            elif Girl == JeanX:
                ch_j "What outfit?"
            elif Girl == StormX:
                ch_s "Which did you mean?"
            elif Girl == JubesX:
                ch_v "Which one?"

            menu:
                extend ""
                "The first one. (locked)" if not Girl.first_custom_outfit["outfit_active"]:
                    pass
                "The first one." if Girl.first_custom_outfit["outfit_active"]:
                    if Girl.first_custom_outfit["outfit_active"] == 2 or count == 99:
                        $ count = 3
                    else:
                        Girl.voice "Well. . ."

                        call quick_outfit_check (Girl, 3)

                        if Girl.first_custom_outfit["outfit_active"] == 2:
                            $ count = 3
                        else:
                            $ line = "no"
                "The second one. (locked)" if not Girl.second_custom_outfit["outfit_active"]:
                    pass
                "The second one." if Girl.second_custom_outfit["outfit_active"]:
                    if Girl.second_custom_outfit["outfit_active"] == 2 or count == 99:
                        $ count = 5
                    else:
                        Girl.voice "Well. . ."

                        call quick_outfit_check (Girl, 5)

                        if Girl.second_custom_outfit["outfit_active"] == 2:
                            $ count = 5
                        else:
                            $ line = "no"
                "The third one. (locked)" if not Girl.third_custom_outfit["outfit_active"]:
                    pass
                "The third one." if Girl.third_custom_outfit["outfit_active"]:
                    if Girl.third_custom_outfit["outfit_active"] == 2 or count == 99:
                        $ count = 6
                    else:
                        Girl.voice "Well. . ."

                        call quick_outfit_check (Girl, 6)

                        if Girl.third_custom_outfit["outfit_active"] == 2:
                            $ count = 6
                        else:
                            $ line = "no"
                "Never mind":
                    pass
            if line == "no":
                if Girl == RogueX:
                    ch_r "No, I'm not wearing that outside, [Girl.player_petname]."
                elif Girl == KittyX:
                    ch_k "I'm[Girl.like]definitely not wearing that one out."
                elif Girl == EmmaX:
                    ch_e "I'm certainly not wearing that one in public."
                elif Girl == LauraX:
                    ch_l "I won't wear that out."
                elif Girl == JeanX:
                    ch_j "Yeah, I wouldn't be caught out in that."
                elif Girl == StormX:
                    ch_s "I cannot wear that one in public."
                elif Girl == JubesX:
                    ch_v "That one's private. . ."

                $ line = 0
            else:
                Girl.voice "Fine. . ."
        "Your gym clothes.":
            if count == 90:
                Girl.voice "Not in class, [Girl.player_petname]."

                $ count = 0
            else:
                $ count = 4
        "Your sleepwear.":
            if count == 99:
                $ count = 7
            else:
                Girl.voice "Well. . ."

                call quick_outfit_check (Girl, 7)

                if Girl.first_custom_outfit["outfit_active"] == 2:
                    $ count = 7

                    Girl.voice "Fine. . ."
                else:
                    if Girl == RogueX:
                        ch_r "I don't know about that, [Girl.player_petname]."
                    elif Girl == KittyX:
                        ch_k "That's not really appropriate, [Girl.player_petname]."
                    elif Girl == EmmaX:
                        ch_e "I don't think that would be appropriate, [Girl.player_petname]."
                    elif Girl == LauraX:
                        ch_l "That's kinda skimpy, [Girl.player_petname]."
                    elif Girl == JeanX:
                        ch_j "I -sleep- in that, I don't wear it out."
                    elif Girl == StormX:
                        ch_s "That's more sleepwear than casual wear."
                    elif Girl == JubesX:
                        ch_v "That's for sleeping in, not going out. . ."

                    $ count = 0
        "Whatever you like.":
            pass

    if Girl == RogueX:
        if count:
            ch_r "Ok, sure, I'll wear that."
        else:
            ch_r "I'll just wear whatever then."
    elif Girl == KittyX:
        if count:
            ch_k "Ok, sure, I'll wear that."
        else:
            ch_k "I'll just wear whatever then."
    elif Girl == EmmaX:
        if count:
            ch_e "Very well."
        else:
            ch_e "I'll wear something else instead."
    elif Girl == LauraX:
        if count:
            ch_l "Ok, sure."
        else:
            ch_l "I'll figure something else out."
    elif Girl == JeanX:
        if count:
            ch_j "Ok, fine."
        else:
            ch_j "I've got my own plans."
    elif Girl == StormX:
        if count:
            ch_s "I will wear it."
        else:
            ch_s "I will choose something else instead. . ."
    elif Girl == JubesX:
        if count:
            ch_v "I'd wear it."
        else:
            ch_v "I'll pick something else. . ."

    return count

label quick_outfit_check(Girl, outfit_to_check = 3):

    $ count = 0
    $ shame = 50

    if outfit_to_check == 3:
        $ outfit_holder = Girl.first_custom_outfit
    elif outfit_to_check == 5:
        $ outfit_holder = Girl.second_custom_outfit
    elif outfit_to_check == 6:
        $ outfit_holder = Girl.third_custom_outfit
    elif outfit_to_check == 4:
        $ outfit_holder = Girl.gym_clothes
    elif outfit_to_check == 7:
        $ outfit_holder = Girl.sleepwear
    elif outfit_to_check == 10:
        $ outfit_holder = Girl.swimwear

    if outfit_holder["bra"] in ["_tank", "_white_tank", "button_tank", "_sports_bra", "_tube_top", "_corset"]:
        $ count = 20
    elif outfit_holder["bra"] == "wolvie_top":
        $ count = 10
    elif outfit_holder["bra"] in ["_lace_bra", "_lace_corset"]:
        $ count = 5
    elif outfit_holder["bra"]:
        $ count = 10
    elif outfit_holder["front_outer_accessory"] == "_suspenders" or outfit_holder["front_outer_accessory"] == "_suspenders2":
        $ count = 5
    else:
        $ count = 0

    if outfit_holder["top"] in ["_nighty", "_mesh_top"]:
        $ count += 5
    elif outfit_holder["top"] == "_towel":
        if Girl == EmmaX:
            $ count += 5
        elif Girl == StormX:
            pass
        else:
            $ count += 10
    elif outfit_holder["top"] in ["_jacket", "_dress", "_pink_top"] or outfit_holder["front_outer_accessory"] == "_jacket":
        $ count += 15
    elif outfit_holder["top"] or outfit_holder["front_outer_accessory"] == "_shut_jacket":
        $ count += 20

    if Girl.outfit["front_inner_accessory"] and count <= 10:
        $ count = -5

    $ count = 20 if count >= 20 else count

    $ shame -= count

    if outfit_holder["bottom"] and outfit_holder["underwear"]:
        $ count = 30
    elif outfit_holder["bottom"] in ["_blue_skirt", "_skirt", "_other_skirt"]:
        $ count = 20
    elif outfit_holder["bottom"] or outfit_holder["front_outer_accessory"] == "_shut_jacket":
        $ count = 25
    elif outfit_holder["underwear"] == "_shorts":
        $ count = 25
    elif outfit_holder["underwear"] in ["_bikini", "_sports_panties", "_shorts"]:
        $ count = 15
    elif outfit_holder["underwear"] == "_lace_panties":
        $ count = 5
    elif outfit_holder["underwear"]:
        $ count = 10

    if outfit_holder["hose"] == "_tights":
        $ count = 25 if count < 25 else count

    if outfit_holder["top"] == "_towel" and Girl not in [EmmaX, StormX]:
        $ count = 25 if count else 15

    $ shame -= count

    if "exhibitionist" in Girl.traits:
        $ agree = True
    elif shame <= 5:
        $ agree = True
    elif shame <= 15 and (approval_check(Girl, 1700, taboo_modifier = 0, C = 0) or approval_check(Girl, 400, "I", taboo_modifier = 0, C = 0)):
        $ agree = True
    elif outfit_to_check == 10 and shame <= 20:
        $ agree = True
    elif Girl == EmmaX and shame >= 15 and "public" not in Girl.history:
        $ agree = 0
    elif Girl == StormX and StormX in Rules:
        $ agree = True
    elif shame <= 25:
        if approval_check(Girl, 2300, taboo_modifier = 0, C = 0) or approval_check(Girl, 700, "I", taboo_modifier = 0, C = 0):
            $ agree = True
        else:
            $ agree = False
    elif (approval_check(Girl, 2500, taboo_modifier = 0, C = 0) or approval_check(Girl, 800, "I", taboo_modifier = 0, C = 0)):
        $ agree = True
    else:
        $ agree = False

    if outfit_to_check == 3:
        $ Girl.first_custom_outfit["outfit_active"] = 2 if agree else 1
    elif outfit_to_check == 5:
        $ Girl.second_custom_outfit["outfit_active"] = 2 if agree else 1
    elif outfit_to_check == 6:
        $ Girl.third_custom_outfit["outfit_active"] = 2 if agree else 1
    elif outfit_to_check == 4:
        $ Girl.gym_clothes["outfit_active"] = 2 if agree else 1
    elif outfit_to_check == 7:
        $ Girl.sleepwear["outfit_active"] = 2 if agree else 1
    elif outfit_to_check == 10:
        $ Girl.swimwear["outfit_active"] = 2 if agree else 1

    return

label Private_outfit(Girl):
    if Girl.broken_up[0] or "_angry" in Girl.daily_history:
        return

    if Girl.outfit_name == "temporary" or not Girl.clothing[9]:
        return

    if "comfy" in Girl.recent_history or "comfy" in Girl.traits or Girl.outfit_name == Girl.clothing[9]:
        call alternate_clothes(Girl, 9)

        $ Girl.change_outfit(outfit_changed = True)
    elif "no_comfy" in Girl.recent_history:
        pass
    elif approval_check(Girl, 1200, "LI") and (2*Girl.inhibition) >= (Girl.love + Girl.obedience +100):
        call shift_focus (Girl)

        if Girl == RogueX:
            ch_r "Be right there [Girl.player_petname]. . ."
            ch_r "I'm slippin' inta somethin' more comfortable. . ."
        elif Girl == KittyX:
            ch_k "Gimme a sec. . ."
            ch_k "I'm throwing on something a bit more. . . fun."
        elif Girl == EmmaX:
            ch_e "I'll be just a moment. . ."
            ch_e "I'll just slip into something more comfortable. . ."
        elif Girl == LauraX:
            ch_l "One minute. . ."
            ch_l "I'm getting a bit more comfortable."
        elif Girl == JeanX:
            ch_j "Let me get changed. . ."
        elif Girl == StormX:
            ch_s "Give me one moment. . ."
            ch_s "I need to change into something more comfortable. . ."
        elif Girl == JubesX:
            ch_v "Gimme a minute. . ."
            ch_v "I wanna slip something else on. . ."

        call alternate_clothes(Girl, 9)

        $ Girl.change_outfit(outfit_changed = True)
        $ Girl.recent_history.append("comfy")
    else:
        call shift_focus (Girl)

        if Girl == RogueX:
            ch_r "Be right there [Girl.player_petname]. . ."
            ch_r "Should I throw on somethin' more comfortable?"
        elif Girl == KittyX:
            ch_k "Gimme a sec. . ."
            ch_k "Want me to wear something more fun?"
        elif Girl == EmmaX:
            ch_e "I'll be just a moment. . ."
            ch_e "Would you like me to change into something more comfortable?"
        elif Girl == LauraX:
            ch_l "One minute. . ."
            ch_l "I could throw on something a bit more fun. . ."
        elif Girl == JeanX:
            ch_j "I do have a more fun look. . ."
        elif Girl == StormX:
            ch_s "I'll be just a moment. . ."
            ch_s "Would you like me to change into something more comfortable?"
        elif Girl == JubesX:
            ch_v "Gimme a minute. . ."
            ch_v "Hey, how'bout I throw something. . . nice on?"

        menu:
            extend ""
            "Sure.":
                if Girl == RogueX:
                    ch_r "Love to. . ."
                elif Girl == KittyX:
                    ch_k "Hehe. . ."
                elif Girl == EmmaX:
                    ch_e "Lovely. . ."
                elif Girl == LauraX:
                    ch_l "Cool. . ."
                elif Girl == JeanX:
                    pass
                elif Girl == StormX:
                    ch_s "Excellent. . ."
                elif Girl == JubesX:
                    ch_v "Cool. . ."

                call alternate_clothes (Girl, 9)

                $ Girl.change_outfit(outfit_changed = True)
                $ Girl.recent_history.append("comfy")
            "No thanks.":
                if Girl == RogueX:
                    ch_r "Suit yourself."
                elif Girl == KittyX:
                    ch_k "Oh, ok."
                elif Girl == EmmaX:
                    ch_e "Very well."
                elif Girl == LauraX:
                    ch_l "Oh, ok."
                elif Girl == JeanX:
                    ch_j "Huh. Ok. . ."
                elif Girl == StormX:
                    ch_s "Very well."
                elif Girl == JubesX:
                    ch_v "Ok, fine."

                $ Girl.recent_history.append("no_comfy")

    return




label Custom_Out(Girl=0, Custom=3, Shame=0, Agree=0):

    $ Girl = check_girl(Girl)
    call shift_focus (Girl)
    $ Girl.change_face("_sexy", 1)

    if Custom == 3:
        $ Shame = Girl.first_custom_outfit[10]
        if Girl.first_custom_outfit["outfit_active"] == 2 or "exhibitionist" in Girl.traits:
            $ Girl.outfit_name = "custom1"
            $ Agree = 1
        else:
            call quick_outfit_check (Girl, 3)
            if Girl.first_custom_outfit["outfit_active"] == 2:
                $ Girl.outfit_name = "custom1"
                $ Agree = 1
    elif Custom == 5:
        $ Shame = Girl.second_custom_outfit[10]
        if Girl.second_custom_outfit["outfit_active"] == 2 or "exhibitionist" in Girl.traits:
            $ Girl.outfit_name = "custom2"
            $ Agree = 1
        else:
            call quick_outfit_check (Girl, 5)
            if Girl.second_custom_outfit["outfit_active"] == 2:
                $ Girl.outfit_name = "custom2"
                $ Agree = 1
    else:
        $ Shame = Girl.third_custom_outfit[10]
        if Girl.third_custom_outfit["outfit_active"] == 2 or "exhibitionist" in Girl.traits:
            $ Girl.outfit_name = "custom3"
            $ Agree = 1
        else:
            call quick_outfit_check (Girl, 6)
            if Girl.third_custom_outfit["outfit_active"] == 2:
                $ Girl.outfit_name = "custom3"
                $ Agree = 1

    if Girl == RogueX:
        if Agree:

            $ Girl.outfit["shame"] = Shame
            if "exhibitionist" in Girl.traits:
                ch_r "Ooo, momma likes."
            elif Shame >= 50:
                ch_r "You realize I'm pretty much naked here, right?"
            elif Shame >= 25:
                ch_r "This is pretty shameless. . ."
            elif Shame >= 15:
                $ Girl.change_face("_bemused", 1)
                ch_r "I don't know, I guess I could try it. . ."
            else:
                ch_r "Sure, [Girl.player_petname], that one's nice."
        else:

            if Shame >= 50:
                $ Girl.change_face("_angry", 1)
                ch_r "Come on, I'd be totally nude!"
            elif Shame >= 25:
                $ Girl.change_face("_angry", 1)
                ch_r "You're lucky I show {i}you{/i} this."
            else:
                $ Girl.change_face("_bemused", 1)
                ch_r "It's kind of daring for me, sorry."
    elif Girl == KittyX:
        if Agree:

            $ Girl.outfit["shame"] = Shame
            if "exhibitionist" in Girl.traits:
                ch_k "Hmm, I'm getting excited. . ."
            elif Shame >= 50:
                ch_k "This is. . . kinda slutty. . . but. . ."
            elif Shame >= 25:
                ch_k "I'm not really comfortable with this one. . ."
            elif Shame >= 15:
                $ Girl.change_face("_bemused", 1)
                ch_k "I'll give it a shot. . ."
            else:
                ch_k "Yeah, I like that one too."
        else:

            if Shame >= 50:
                $ Girl.change_face("_angry", 1)
                ch_k "You have GOT to be kidding me here."
            elif Shame >= 25:
                $ Girl.change_face("_angry", 1)
                ch_k "This is just between us."
            else:
                $ Girl.change_face("_bemused", 1)
                ch_k "I can't wear this out!"
    elif Girl == EmmaX:
        if Agree:

            $ Girl.outfit["shame"] = Shame
            if "exhibitionist" in Girl.traits:
                ch_e "Hmm, I'm getting excited. . ."
            elif Shame >= 50:
                ch_e "This is rather. . . shameless. . ."
            elif Shame >= 25:
                ch_e "I'm a bit uncomfortable with this one. . ."
            elif Shame >= 15:
                $ Girl.change_face("_bemused", 1)
                ch_e "I'll try it. . ."
            else:
                ch_e "Yeah, I like that one too."
        else:

            if Shame >= 50:
                $ Girl.change_face("_angry", 1)
                ch_e "You have GOT to be kidding me here."
            elif Shame >= 25:
                $ Girl.change_face("_angry", 1)
                ch_e "This is just between us."
            else:
                $ Girl.change_face("_bemused", 1)
                ch_e "I can't wear this out!"
    elif Girl == LauraX:
        if Agree:

            $ Girl.outfit["shame"] = Shame
            if "exhibitionist" in Girl.traits:
                ch_l "Mmmmmm. . ."
            elif Shame >= 50:
                ch_l "This is. . . really brave. . ."
            elif Shame >= 25:
                ch_l "This one's pretty skimpy. . ."
            elif Shame >= 15:
                $ Girl.change_face("_bemused", 1)
                ch_l "Yeah, ok. . ."
            else:
                ch_l "Yup."
        else:

            if Shame >= 50:
                $ Girl.change_face("_angry", 1)
                ch_l "Perv."
            elif Shame >= 25:
                $ Girl.change_face("_angry", 1)
                ch_l "Yeah, not in public."
            else:
                $ Girl.change_face("_bemused", 1)
                ch_l "Nah."
    elif Girl == JeanX:
        if Agree:

            $ Girl.outfit["shame"] = Shame
            if "exhibitionist" in Girl.traits:
                ch_j ". . ."
            elif Shame >= 50:
                ch_j "Pretty daring. . ."
            elif Shame >= 25:
                ch_j "Kinda skimpy. . ."
            elif Shame >= 15:
                $ Girl.change_face("_bemused", 1)
                ch_j "Sure, whatever. . ."
            else:
                ch_j "Sure."
        else:

            if Shame >= 50:
                $ Girl.change_face("_angry", 1)
                ch_j "Gross."
            elif Shame >= 25:
                $ Girl.change_face("_angry", 1)
                ch_j "You wish."
            else:
                $ Girl.change_face("_bemused", 1)
                ch_j "No way."
    elif Girl == StormX:
        $ Girl.change_face("_bemused", 1)
        if Agree:

            $ Girl.outfit["shame"] = Shame
            if "exhibitionist" in Girl.traits:
                ch_s "Oooh. . ."
            elif Shame >= 25:
                ch_s "You are going to get me into trouble. . ."
            else:
                ch_s "Yes, this will do nicely."
        else:

            $ Girl.change_face("_bemused", 1)
            ch_s "I am afraid cannot wear this out."
    elif Girl == JubesX:
        $ Girl.change_face("_bemused", 1)
        if Agree:

            $ Girl.outfit["shame"] = Shame
            if "exhibitionist" in Girl.traits:
                ch_s "Oooh. . ."
            elif Shame >= 25:
                ch_s "Whew, this is flat out pornographic. . ."
            else:
                ch_s "Oh, yeah, this'll do. . ."
        else:

            $ Girl.change_face("_bemused", 1)
            ch_s "I really can't wear this one out. . ."
    return



label outfitShame(Girl=0, Custom=3, Check=0, Count=0, Tempshame=50, Agree=1):






    $ Girl = check_girl(Girl)

    if not Check and not taboo and not Girl.taboo and Custom != 20:

        if Girl.clothing[9] and bg_current in personal_rooms:

            if "halloween" not in Player.daily_history:
                call Private_outfit
        return

    if Girl.bra_number() >= 5:
        $ Count = 20
    elif Girl.bra_number() >= 4:
        $ Count = 15
    elif Girl.bra_number() >= 3:
        $ Count = 10
    elif Girl.bra_number() >= 2:
        $ Count = 5
    else:
        $ Count = 0



    if Custom == 20 and Girl.top_pulled_up:
        $ Count = 0
    elif Girl.top_number() >= 5:
        $ Count += 20
    elif Girl.top_number() >= 4:
        $ Count += 15
    elif Girl.top_number() >= 3:
        $ Count += 10
    elif Girl.top_number() >= 2:
        $ Count += 5



    if Girl.outfit["front_inner_accessory"] and Count <= 10:
        $ Count = -5

    $ Girl.change_face("_sexy", 0)
    if Custom == 9 or Custom == 7:
        pass
    elif Count >= 20:
        $ Count = 20
        if Check:
            if Girl == RogueX:
                ch_r "Oh, I think this top combination works."
            elif Girl == KittyX:
                ch_k "This is[Girl.like]totally a cute top."
            elif Girl == EmmaX:
                ch_e "This is a fashionable top."
            elif Girl == LauraX:
                ch_l "This top works."
            elif Girl == JeanX:
                ch_j "The top is fine."
            elif Girl == StormX:
                ch_s "The top is fine."
            elif Girl == JubesX:
                ch_v "Yeah, the_top'll work. . ."
    elif not Check:
        pass
    elif Girl == RogueX:
        if Count >= 10 and (approval_check(Girl, 1200, taboo_modifier=0) or approval_check(Girl, 500, "I", taboo_modifier=0)):
            ch_r "This top is pretty sexy. . ."
        elif Count >= 10:
            ch_r "This top might be a bit daring to wear outside."
        elif Count >= 5 and (approval_check(Girl, 2300, taboo_modifier=0) or approval_check(Girl, 800, "I", taboo_modifier=0)):
            ch_r "Not leaving much to the imagination. . ."
        elif Count >= 5:
            $ Girl.change_face("startled", 1)
            ch_r "I really think this is a bit scandalous to wear out. . ."
        elif (approval_check(Girl, 2700, taboo_modifier=0) or approval_check(Girl, 950, "I", taboo_modifier=0)):
            ch_r "Oooh, I'm getting turned on already. . ."
        else:
            $ Girl.change_face("_bemused", 1)
            ch_r "This is just for in private, right. . ."
    elif Girl == KittyX:
        if Count >= 10 and (approval_check(Girl, 1200, taboo_modifier=0) or approval_check(Girl, 500, "I", taboo_modifier=0)):
            ch_k "Kinda hot top."
        elif Count >= 10:
            ch_k "I wouldn't[Girl.like]feel comfortable in this top."
        elif Count >= 5 and (approval_check(Girl, 2300, taboo_modifier=0) or approval_check(Girl, 800, "I", taboo_modifier=0)):
            ch_k "This top is is[Girl.like]kinda breezy. . ."
        elif Count >= 5:
            $ Girl.change_face("startled", 1)
            ch_k "This top is[Girl.like]way too slutty."
        elif (approval_check(Girl, 2700, taboo_modifier=0) or approval_check(Girl, 950, "I", taboo_modifier=0)):
            ch_k "Is it hot in here? Whew. . ."
        else:
            $ Girl.change_face("_bemused", 1)
            ch_k "I wouldn't wear this out, but maybe indoors."
    elif Girl == EmmaX:
        if Count >= 10:
            if approval_check(Girl, 1200, taboo_modifier=0) or approval_check(Girl, 500, "I", taboo_modifier=0):
                ch_e "A bit daring. . ."
            else:
                ch_e "I'm not sure about this top."
        elif Count >= 5:
            if approval_check(Girl, 2300, taboo_modifier=0) or approval_check(Girl, 800, "I", taboo_modifier=0):
                ch_e "I typically cover a {i}bit{/i} more than this."
            else:
                $ Girl.change_face("startled", 1)
                ch_e "This is a bit more cleavage than even I'm comforable with."
        elif (approval_check(Girl, 2700, taboo_modifier=0) or approval_check(Girl, 950, "I", taboo_modifier=0)):
            ch_e "Aren't my assets a bit. . . exposed here?"
        else:
            $ Girl.change_face("_bemused", 1)
            ch_e "This is considerably more cleavage than even I'm comforable with."
    elif Girl == LauraX:
        if Count >= 10 and (approval_check(Girl, 1200, taboo_modifier=0) or approval_check(Girl, 500, "I", taboo_modifier=0)):
            ch_l "This top works."
        elif Count >= 10:
            ch_l "The_top's not really a good look."
        elif Count >= 5 and (approval_check(Girl, 2300, taboo_modifier=0) or approval_check(Girl, 800, "I", taboo_modifier=0)):
            ch_l "I don't know, the_top's a little light."
        elif Count >= 5:
            $ Girl.change_face("startled", 1)
            ch_l "I can't really wear this top out."
        elif (approval_check(Girl, 2700, taboo_modifier=0) or approval_check(Girl, 950, "I", taboo_modifier=0)):
            ch_l ". . ."
        else:
            $ Girl.change_face("_bemused", 1)
            ch_l "I wouldn't go out with my tits out."
    elif Girl == JeanX:
        if Count >= 10:
            ch_j "You must really enjoy these tits. . ."


        elif Count >= 5:
            ch_j "I've kinda got my tits out here. . ."



        elif (approval_check(Girl, 2700, taboo_modifier=0) or approval_check(Girl, 950, "I", taboo_modifier=0)):
            ch_j ". . ."
        else:
            $ Girl.change_face("_bemused", 1)
            ch_j "You think I'd go out with my tits on display?"
    elif Girl == StormX:
        if Count >= 10:
            ch_s "A lovely choice for the top."
        elif Count >= 5:
            if StormX not in Rules:
                ch_s "I do typically cover more than this around the school."
            else:
                $ Girl.change_face("_bemused", 1)
                ch_s "I'm not sure Charles would approve of this top."
        elif (approval_check(Girl, 2700, taboo_modifier=0) or approval_check(Girl, 950, "I", taboo_modifier=0)):
            ch_s "Aren't my assets a bit. . . exposed here?"
        else:
            $ Girl.change_face("_bemused", 1)
            ch_s "I'm not sure Charles would approve of this top."
    elif Girl == JubesX:
        if Count >= 10 and (approval_check(Girl, 1200, taboo_modifier=0) or approval_check(Girl, 500, "I", taboo_modifier=0)):
            ch_v "Yeah, the_top'll work. . ."
        elif Count >= 10:
            ch_v "I don't know about this top. . ."
        elif Count >= 5 and (approval_check(Girl, 2300, taboo_modifier=0) or approval_check(Girl, 800, "I", taboo_modifier=0)):
            ch_v "I don't know, the_top's a little skimpy."
        elif Count >= 5:
            $ Girl.change_face("startled", 1)
            ch_v "I can't really wear this top out."
        elif (approval_check(Girl, 2700, taboo_modifier=0) or approval_check(Girl, 950, "I", taboo_modifier=0)):
            ch_v "I don't know. . ."
        else:
            $ Girl.change_face("_bemused", 1)
            ch_v "Well, I wouldn't go anywhere with my tits out like this. . ."


    $ Tempshame -= Count
    $ Count = 0

    if Girl.outfit["bottom"] and Girl.outfit["underwear"]:
        $ Count = 30
    else:
        if Girl.bottom_number() > 5:

            $ Count = 25
        elif Girl.bottom_number() == 5:

            $ Count = 20
        elif Girl.underwear_number() >= 8:

            $ Count = 25
        elif Girl.underwear_number() >= 6:

            $ Count = 15
        elif Girl.underwear_number() >= 4:

            $ Count = 10
        elif Girl.underwear_number() >= 2:

            $ Count = 5


        if Girl.hose_number() >= 10:

            $ Count = 25 if Count < 25 else Count

        if Girl.outfit["top"] == "_towel" and Count:

            $ Count = 25
        elif Girl.outfit["top"] == "_towel":

            $ Count = 15
    if not Check:

        pass
    elif Custom == 9 or Custom == 7:
        pass
    elif Girl == RogueX:
        if Count >= 20:
            if Girl.bottom_number() > 6:
                ch_r "Oh, I think these pants will work fine."
            elif Girl.bottom_number() == 5:
                ch_r "Oh, I think this skirt will work fine."
            elif Girl.hose_number() >= 10:
                ch_r "Oh, these [Girl.outfit['hose']] will work."
            elif Girl.outfit["underwear"] == "_shorts":
                ch_r "Oh, I think these shorts will work fine."
            elif Girl.outfit["top"] == "_towel":
                ch_r "The towel's an odd choice. . ."
            else:
                ch_r "Kinda breezy across my nethers, [Girl.player_petname]. . ."
            if not Girl.outfit["underwear"] and approval_check(Girl, 500, "I", taboo_modifier=0):
                ch_r "I kinda like going commando."
            elif not Girl.outfit["underwear"]:
                ch_r "Don't know about going commando though."
        elif Count >= 10 and (approval_check(Girl, 2000, taboo_modifier=0) or approval_check(Girl, 700, "I", taboo_modifier=0)):
            ch_r "These don't really leave much to the imagination. . ."
        elif Count >= 10:
            $ Girl.change_face("_angry", 1)
            ch_r "I'm warning you, I'm not running around in my panties. . ."
        elif (approval_check(Girl, 2500, taboo_modifier=0) or approval_check(Girl, 800, "I", taboo_modifier=0)):
            ch_r "Hmm, Breezy. . ."
        else:
            ch_r "So long as we stay inside. . ."
    elif Girl == KittyX:
        if Count >= 20:
            if Girl.bottom_number() >= 5:
                ch_k "and these pants look cute on me."
            elif Girl.outfit["bottom"] == "_shorts":
                ch_k "and these are cute shorts."
            elif Girl.hose_number() >= 10:
                ch_k "I guess these [Girl.outfit['hose']] will work fine."
            elif Girl.outfit["top"] == "_towel":
                ch_k "The towel's an odd choice. . ."
            else:
                ch_k "This is kinda breezy."
            if not Girl.outfit["underwear"] and approval_check(Girl, 500, "I", taboo_modifier=0):
                ch_k "I like going without panties."
            elif not Girl.outfit["underwear"]:
                ch_k "It's a little uncomfortable without panties."
        elif Count >= 10 and (approval_check(Girl, 2000, taboo_modifier=0) or approval_check(Girl, 700, "I", taboo_modifier=0)):
            ch_k "I'm not sure about the coverage down here. . ."
        elif Count >= 10:
            $ Girl.change_face("_angry", 1)
            ch_k "I'm barely covered down here. . ."
        elif (approval_check(Girl, 2500, taboo_modifier=0) or approval_check(Girl, 800, "I", taboo_modifier=0)):
            ch_k "kinda chilly. . ."
        else:
            ch_k "if it's just[Girl.like]you and me. . ."
    elif Girl == EmmaX:
        if Count >= 20:
            if Girl.bottom_number() > 5:
                ch_e "and these pants always did suit me."
            elif Girl.bottom_number() >= 5:
                ch_e "and this skirt always did suit me."
            elif Girl.hose_number() >= 10:
                ch_e "I guess these [Girl.outfit['hose']] will work fine."
            elif Girl.outfit["top"] == "_towel":
                ch_e "I'm unsure about wearing a towel out, [Girl.player_petname]. . ."
            else:
                ch_e "I probably could wear something more downstairs, [Girl.player_petname]. . ."
            if not Girl.outfit["underwear"]:
                if approval_check(Girl, 500, "I", taboo_modifier=0):
                    ch_e "I do enjoy going without panties."
                else:
                    ch_e "I don't know about going without panties in this situation."
        elif Count >= 10:
            if approval_check(Girl, 2000, taboo_modifier=0) or approval_check(Girl, 700, "I", taboo_modifier=0):
                ch_e "I hope you don't expect me to wear this out. . ."
            else:
                $ Girl.change_face("_angry", 1)
                ch_e "I don't know about wearing this outside. . ."
        elif (approval_check(Girl, 2500, taboo_modifier=0) or approval_check(Girl, 800, "I", taboo_modifier=0)):
            ch_e "This really tests my limits."
        else:
            ch_e "I'll need to put something else on to leave the room though."
    elif Girl == LauraX:
        if Count >= 20:
            if Girl.bottom_number() > 5:
                ch_l "and these pants work."
            elif Girl.bottom_number() >= 5:
                ch_l "and this skirt works."
            elif Girl.hose_number() >= 10:
                ch_l "and these [Girl.outfit['hose']] will work fine."
            elif Girl.outfit["top"] == "_towel":
                ch_l "The towel's an odd choice. . ."
            else:
                ch_l "but there's a draft."
            if not Girl.outfit["underwear"] and approval_check(Girl, 500, "I", taboo_modifier=0):
                ch_l "Commando's cool."
            elif not Girl.outfit["underwear"]:
                ch_l "I might accidentally flash some people like this though."
        elif Count >= 10 and (approval_check(Girl, 2000, taboo_modifier=0) or approval_check(Girl, 700, "I", taboo_modifier=0)):
            ch_l "I don't think I'm fully covered. . ."
        elif Count >= 10:
            $ Girl.change_face("_angry", 1)
            ch_l "I'm not covered like this. . ."
        elif (approval_check(Girl, 2500, taboo_modifier=0) or approval_check(Girl, 800, "I", taboo_modifier=0)):
            ch_l "It's pretty minimal. . ."
        else:
            ch_l "I wouldn't show off my cooch either. . ."
    elif Girl == JeanX:
        if Count >= 20:
            if Girl.bottom_number() > 5:
                ch_j "I do like these pants. . ."
            elif Girl.bottom_number() >= 5:
                ch_j "I do like this skirt. . ."
            elif Girl.hose_number() >= 10:
                ch_j "these [Girl.outfit['hose']] will work fine."
            elif Girl.outfit["top"] == "_towel":
                ch_j "A towel though? . ."
            else:
                ch_j "kinda exposed here. . ."
            if not Girl.outfit["underwear"] and approval_check(Girl, 500, "I", taboo_modifier=0):
                ch_j "I don't mind doing without the panties. . ."
            elif not Girl.outfit["underwear"]:
                ch_j "I'd kinda need panties with this. . ."


        elif Count >= 10:
            if (approval_check(Girl, 2000, taboo_modifier=0) or approval_check(Girl, 700, "I", taboo_modifier=0)):
                $ Girl.change_face("_sly", 1)
            else:
                $ Girl.change_face("_angry", 1)
            ch_j "So you want my puss on display? . ."
        elif (approval_check(Girl, 2500, taboo_modifier=0) or approval_check(Girl, 800, "I", taboo_modifier=0)):
            ch_j "This is basically \"nothing\". . ."
        else:
            ch_j "I'm not interested in showing off the goods. . ."
    elif Girl == StormX:
        if Girl.bottom_number() > 5:
            ch_s "and these pants always did suit me."
        elif Girl.bottom_number() >= 5:
            ch_s "and this skirt always did suit me."
        elif Girl.hose_number() >= 10:
            ch_s "I supposed that these [Girl.outfit['hose']] will work fine."
        elif Girl.outfit["top"] == "_towel":
            ch_s "I'm unsure about wearing a towel out, [Girl.player_petname]. . ."
        else:
            ch_s "A rather breezy ensemble, [Girl.player_petname]. . ."
        if not Girl.outfit["underwear"]:
            if approval_check(Girl, 500, "I", taboo_modifier=0):
                ch_s "I do enjoy doing without panties."
            else:
                ch_s "Certainly quite exposed without panties. . ."
        if Count >= 10 and StormX not in Rules:
            $ Girl.change_face("_bemused", 1)
            ch_s "I don't know that Charles would let me roam the halls in such an exposed state."
        elif StormX in Rules and (approval_check(Girl, 1200, taboo_modifier=0) or approval_check(Girl, 500, "I", taboo_modifier=0)):
            ch_s "This is quite the daring look you've put together."
        else:
            ch_s "I doubt Charles would let me roam the halls in such an exposed state."
    elif Girl == JubesX:
        if Count >= 20:
            if Girl.bottom_number() > 6:
                ch_v "and these pants work."
            elif Girl.bottom_number() >= 6:
                ch_v "and these shorts work."
            elif Girl.bottom_number() >= 5:
                ch_v "and this skirt works."
            elif Girl.hose_number() >= 10:
                ch_v "and these [Girl.outfit['hose']] will work fine."
            elif Girl.outfit["top"] == "_towel":
                ch_v "The towel's an odd choice. . ."
            else:
                ch_v "but I don't know about this. . ."
            if not Girl.outfit["underwear"] and approval_check(Girl, 500, "I", taboo_modifier=0):
                ch_v "I guess we're not doing panties now?"
            elif not Girl.outfit["underwear"]:
                ch_v "I don't think I'd want to go without panties. . ."
        elif Count >= 10 and (approval_check(Girl, 2000, taboo_modifier=0) or approval_check(Girl, 700, "I", taboo_modifier=0)):
            ch_v "This is pretty skimpy. . ."
        elif Count >= 10:
            $ Girl.change_face("_angry", 1)
            ch_v "This is pretty skimpy. . ."
        elif (approval_check(Girl, 2500, taboo_modifier=0) or approval_check(Girl, 800, "I", taboo_modifier=0)):
            ch_v "Wow, this look is. . . a lot. . ."
        else:
            ch_v "I don't really go around showing the goods. . ."


    $ Tempshame -= Count

    if Check:

        if Check == 2:
            ch_p "So can I see it then?"
        elif Custom == 4:
            ch_p "So would you work out in that?"
        elif Custom == 7:
            ch_p "So would you sleep in that?"
        else:
            ch_p "So would you wear that outside?"

        $ Girl.change_face("_sexy", 0)
        if Girl.bottom_number() > 2:
            pass
        elif Girl == StormX and StormX in Rules:
            pass
        elif Girl.underwear_number() > 2 and (Girl.seen_underwear or approval_check(Girl, 900, taboo_modifier=0)):
            pass
        elif Girl.seen_pussy or approval_check(Girl, 1200, taboo_modifier=0):
            pass
        else:
            $ Agree = 0

        if not Agree:
            pass
        elif Girl == StormX and StormX in Rules:
            pass
        elif Girl.top_number() > 2:
            pass
        elif Girl.bra_number() > 2 and (Girl.seen_breasts or approval_check(Girl, 900, taboo_modifier=0)):
            pass
        elif Girl.seen_breasts or approval_check(Girl, 1200, taboo_modifier=0):
            pass
        else:
            $ Agree = 0

        if Check == 2 and Agree:

            $ Girl.outfit["shame"] = Tempshame
            $ Girl.change_face("_sly")
            if Girl == RogueX:
                ch_r "This ain't a bad look, I guess. . ."
            elif Girl == KittyX:
                ch_k "I suppose you've put together a cute little outfit. . ."
            elif Girl == EmmaX:
                ch_e "I suppose I could pull this off. . ."
            elif Girl == LauraX:
                ch_l "Huh, this'll work. . ."
            elif Girl == JeanX:
                ch_j "It does look good on me. . ."
            elif Girl == StormX:
                ch_s "I don't see why not. . ."
            elif Girl == JubesX:
                ch_v "Sure, take a look. . ."
            hide dress_screen
            return True
        if not Agree:

            $ Girl.change_face("_bemused", 2,eyes="_side")
            if Girl == RogueX:
                ch_r "I don't really feel comfortable in this. . ."
            elif Girl == KittyX:
                ch_k "I don't think I'd be comfortable with you seeing me like this. . ."
            elif Girl == EmmaX:
                ch_e "I wouldn't want to blind you. . ."
            elif Girl == LauraX:
                ch_l "You'll have to earn it."
            elif Girl == JeanX:
                ch_j "It's cute, yeah, but I can't go out in it."
            elif Girl == StormX:
                ch_s "I think you're making fun of me. . ."
            elif Girl == JubesX:
                ch_v "I really can't let you see this. . ."
            menu:
                extend ""
                "Ok then, you can put your normal clothes back on.":
                    $ Girl.change_outfit(outfit_changed = True)
                    hide dress_screen
                "Ok, we can keep tweaking it.":
                    pass
            $ Girl.change_face("_smile", 1)
            if Girl == RogueX:
                ch_r "Thanks, [Girl.player_petname]."
            elif Girl == KittyX:
                ch_k "Thanks."
            elif Girl == EmmaX:
                ch_e "Appreciated."
            elif Girl == LauraX:
                ch_l "Thanks."
            elif Girl == JeanX:
                ch_j ". . . that's what I said."
            elif Girl == StormX:
                ch_s "Very well. . ."
            elif Girl == JubesX:
                ch_v "Cool, cool. . ."
            return
        if Girl == RogueX:
            if Girl.taboo >= 40:
                $ Girl.change_face("_confused",1)
                $ Girl.mouth = "_smile"
                ch_r "It's a little late to worry about that, right?"
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                ch_r "Hmm. . . yeah, I'd love to. . ."
                $ Girl.change_stat("lust", 80, 10)
            elif Custom == 7:

                $ Girl.change_face("_bemused", 1)
                if Tempshame >= 30:
                    ch_r "A bit scandalous, but yeah."
                elif Tempshame >= 15:
                    ch_r "Yeah, you're worth it."
                else:
                    ch_r "Sure, it's cute."
            elif Tempshame <= 5:
                $ Girl.change_face("_smile")
                ch_r "Yeah, I think I like this style, I'd wear this."
            elif Tempshame <= 15:
                if approval_check(Girl, 1700, taboo_modifier=0, C = 0) or approval_check(Girl, 400, "I", taboo_modifier=0, C = 0):
                    ch_r "It's pretty skimpy, but I can make it work."
                else:
                    $ Girl.change_face("_bemused", 1)
                    ch_r "I think this looks is a bit daring to wear."
                    $ Agree = 0
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("_bemused", 1)
                ch_r "Sure, I can swim in this. . ."
            elif Tempshame <= 25:
                if approval_check(Girl, 2300, taboo_modifier=0, C = 0) or approval_check(Girl, 700, "I", taboo_modifier=0, C = 0):
                    ch_r "Kinky, but I can rock this."
                else:
                    $ Girl.change_face("_angry", 1)
                    ch_r "I'm definitely not going out in this."
                    $ Agree = 0
            elif approval_check(Girl, 2500, taboo_modifier=0, C = 0) or approval_check(Girl, 800, "I", taboo_modifier=0, C = 0):
                $ Girl.change_face("_bemused", 1)
                ch_r "I can't believe it. . . but yeah."
            else:
                $ Girl.change_face("_angry", 1)
                ch_r "You have got to be kidding."
                $ Agree = 0
        elif Girl == KittyX:
            if Girl.taboo >= 40:
                $ Girl.change_face("_confused",1)
                $ Girl.mouth = "_smile"
                ch_k "Kinda late to ask, right?"
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                ch_k "I'm getting wet just thinking about it. . ."
                $ Girl.change_stat("lust", 80, 10)
            elif Tempshame <= 5:
                $ Girl.change_face("_smile")
                ch_k "Sure, it's a cute look!"
            elif Tempshame <= 15 and (approval_check(Girl, 1700, taboo_modifier=0, C = 0) or approval_check(Girl, 400, "I", taboo_modifier=0, C = 0)):
                ch_k "It's pretty hot, right?"
            elif Custom == 7:

                $ Girl.change_face("_bemused", 1)
                if Tempshame >= 30:
                    ch_k "This is[Girl.like]pretty exposed, but ok."
                elif Tempshame >= 15:
                    ch_k "It's kinda naughty, I like it."
                else:
                    ch_k "Yeah, these are fine."
            elif Tempshame <= 15:
                $ Girl.change_face("_bemused", 1)
                ch_k "It's too slutty to wear out."
                $ Agree = 0
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("_bemused", 1)
                ch_k "This is a cute swimsuit. . ."
            elif Tempshame <= 25 and (approval_check(Girl, 2300, taboo_modifier=0, C = 0) or approval_check(Girl, 700, "I", taboo_modifier=0, C = 0)):
                ch_k "So sexy, but I can handle it."
            elif Tempshame <= 25:
                $ Girl.change_face("_angry", 1)
                ch_k "{i}Way{/i} too sexy for outside."
                $ Agree = 0
            elif (approval_check(Girl, 2500, taboo_modifier=0, C = 0) or approval_check(Girl, 800, "I", taboo_modifier=0, C = 0)):
                $ Girl.change_face("_bemused", 1)
                ch_k "OMG, I can't believe I'm doing this."
            else:
                $ Girl.change_face("_angry", 1)
                ch_k "I - can't - even."
                $ Agree = 0
        elif Girl == EmmaX:
            if Girl.taboo >= 40:
                $ Girl.change_face("_confused",1)
                $ Girl.mouth = "_smile"
                "She glances around."
                ch_e "Is that a trick question?"
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                ch_e "The thought of it gets me moist. . ."
                $ Girl.change_stat("lust", 80, 10)
            elif Tempshame <= 5:
                $ Girl.change_face("_smile")
                ch_e "Yes, it's a fine choice."
            elif Tempshame <= 15 and (approval_check(Girl, 1700, taboo_modifier=0, C = 0) or approval_check(Girl, 400, "I", taboo_modifier=0, C = 0)):
                ch_e "Rather daring, how could I resist?"
            elif Custom == 7:

                $ Girl.change_face("_bemused", 1)
                if Tempshame >= 30:
                    ch_e "You understand I only wear this sort of thing in private."
                else:
                    ch_e "It is a comfortable outfit."
            elif Tempshame <= 15:
                $ Girl.change_face("_bemused", 1)
                ch_e "Rather too daring, don't you think?"
                $ Agree = 0
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("_bemused", 1)
                ch_e "Fine, this is decent swimwear. . ."
            elif Tempshame >= 15 and "public" not in Girl.history:
                ch_e "I doubt I could get away with this in public, [Girl.player_petname]."
                $ Agree = 0
            elif Tempshame <= 25 and (approval_check(Girl, 2300, taboo_modifier=0, C = 0) or approval_check(Girl, 700, "I", taboo_modifier=0, C = 0)):
                ch_e "This is particularly inappropriate. . . in the best ways."
            elif Tempshame <= 25:
                $ Girl.change_face("_angry", 1)
                ch_e "I don't believe even I could pull off this look, [Girl.player_petname]."
                $ Agree = 0
            elif (approval_check(Girl, 2500, taboo_modifier=0, C = 0) or approval_check(Girl, 800, "I", taboo_modifier=0, C = 0)):
                $ Girl.change_face("_bemused", 1)
                ch_e "This look certainly pushes the boundaries."
            else:
                $ Girl.change_face("_angry", 1)
                ch_e "Even I can't pull this off."
                $ Agree = 0
        elif Girl == LauraX:
            if Girl.taboo >= 40:
                $ Girl.change_face("_confused",1)
                $ Girl.mouth = "_smile"
                ch_l "Well a bit late for that, I guess."
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                $ Girl.change_stat("lust", 80, 10)
                $ Girl.change_face("_sexy", 2)
                ch_l ". . ."
                $ Girl.change_face("_sexy", 1)
            elif Tempshame <= 5:
                $ Girl.change_face("_smile")
                ch_l "I don't see why not."
            elif Tempshame <= 15 and (approval_check(Girl, 1700, taboo_modifier=0, C = 0) or approval_check(Girl, 400, "I", taboo_modifier=0, C = 0)):
                ch_l "It looks good, right?"
            elif Custom == 7:

                $ Girl.change_face("_bemused", 1)
                if Tempshame >= 30:
                    ch_l "Sure, perv."
                elif Tempshame >= 15:
                    ch_l "Sure, why not."
                else:
                    ch_l "Yeah, I guess."
            elif Tempshame <= 15:
                $ Girl.change_face("_bemused", 1)
                ch_l "I can't move freely in this without showing off the goods."
                $ Agree = 0
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("_bemused", 1)
                ch_l "Yeah, I can swim in this. . ."
            elif Tempshame <= 25 and (approval_check(Girl, 2300, taboo_modifier=0, C = 0) or approval_check(Girl, 700, "I", taboo_modifier=0, C = 0)):
                ch_l "I can handle this."
            elif Tempshame <= 25:
                $ Girl.change_face("_angry", 1)
                ch_l "Nah, too slutty."
                $ Agree = 0
            elif (approval_check(Girl, 2500, taboo_modifier=0, C = 0) or approval_check(Girl, 800, "I", taboo_modifier=0, C = 0)):
                $ Girl.change_face("_bemused", 1)
                ch_l "Pretty daring, eh?"
            else:
                $ Girl.change_face("_angry", 1)
                ch_l "As if."
                $ Agree = 0
        elif Girl == JeanX:
            if Girl.taboo >= 40:
                $ Girl.change_face("_confused",1)
                $ Girl.mouth = "_smile"
                ch_j "Well, I guess so, right?"
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                $ Girl.change_stat("lust", 80, 10)
                $ Girl.change_face("_sexy", 2)
                ch_j ". . ."
                $ Girl.change_face("_sexy", 1)
            elif Tempshame <= 5:
                $ Girl.change_face("_smile")
                ch_j "Sure, whatever."
            elif Tempshame <= 15 and (approval_check(Girl, 1700, taboo_modifier=0, C = 0) or approval_check(Girl, 400, "I", taboo_modifier=0, C = 0)):
                ch_j "I almost have to. . ."
            elif Custom == 7:

                $ Girl.change_face("_bemused", 1)
                if Tempshame >= 30:
                    ch_j "If it'll keep you hard. . ."
                elif Tempshame >= 15:
                    ch_j "Yeah, sure."
                else:
                    ch_j "Why not."
            elif Tempshame <= 15:
                $ Girl.change_face("_bemused", 1)
                ch_j "I can pull this one off. . ."
                $ Agree = 0
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("_bemused", 1)
                ch_j "Yeah, sure."
            elif Tempshame <= 25 and (approval_check(Girl, 2300, taboo_modifier=0, C = 0) or approval_check(Girl, 700, "I", taboo_modifier=0, C = 0)):
                ch_j "This'll turn some heads. . ."
            elif Tempshame <= 25:
                $ Girl.change_face("_angry", 1)
                ch_j "I wouldn't want to break anyone. . ."
                $ Agree = 0
            elif (approval_check(Girl, 2500, taboo_modifier=0, C = 0) or approval_check(Girl, 800, "I", taboo_modifier=0, C = 0)):
                $ Girl.change_face("_bemused", 1)
                ch_j "Kinky, but sure."
            else:
                $ Girl.change_face("_angry", 1)
                ch_j "You have to be joking."
                $ Agree = 0
        elif Girl == StormX:

            if Girl.taboo >= 40:
                $ Girl.change_face("_confused",1)
                $ Girl.mouth = "_smile"
                "She glances around."
                ch_s "It seems a bit late for that question. . ."
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                ch_s "I do find the idea. . . exciting. . ."
                $ Girl.change_stat("lust", 80, 10)
            elif Tempshame <= 10:
                $ Girl.change_face("_smile")
                ch_s "Yes, it's a fine choice."
            elif Custom == 7:

                $ Girl.change_face("_bemused", 1)
                if Tempshame >= 20:
                    ch_s "This is a fine outfit."
                else:
                    ch_s "It may be a bit more than I'm used to. . ."
            elif StormX in Rules:
                ch_s "I don't see why not. . ."
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("_bemused", 1)
                ch_s "I suppose I could swim well like this. . ."
            elif Tempshame <= 20 and (approval_check(Girl, 1700, taboo_modifier=0, C = 0) or approval_check(Girl, 400, "I", taboo_modifier=0, C = 0)):
                ch_s "This certainly does push the limits of good taste. . ."
            elif Tempshame <= 25 and (approval_check(Girl, 2300, taboo_modifier=0, C = 0) or approval_check(Girl, 700, "I", taboo_modifier=0, C = 0)):
                $ Girl.change_face("_bemused", 1)
                ch_s "I doubt Charles would approve, but so what?"
            elif Tempshame <= 25:
                $ Girl.change_face("_bemused", 1)
                ch_s "I'm afraid that Charles would never approve."
                $ Agree = 0
            elif (approval_check(Girl, 2500, taboo_modifier=0, C = 0) or approval_check(Girl, 800, "I", taboo_modifier=0, C = 0)):
                $ Girl.change_face("_bemused", 1)
                ch_s "I doubt Charles would approve, but so what?"
            else:
                $ Girl.change_face("_bemused", 1)
                ch_s "I'm afraid that Charles would never approve."
                $ Agree = 0
        elif Girl == JubesX:
            if Girl.taboo >= 40:
                $ Girl.change_face("_confused",1)
                $ Girl.mouth = "_smile"
                ch_v "I guess that ship has sailed. . ."
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                $ Girl.change_stat("lust", 80, 10)
                $ Girl.change_face("_sexy", 2)
                ch_v ". . ."
                $ Girl.change_face("_sexy", 1)
            elif Tempshame <= 5:
                $ Girl.change_face("_smile")
                ch_v "I guess?"
            elif Tempshame <= 15 and (approval_check(Girl, 1700, taboo_modifier=0, C = 0) or approval_check(Girl, 400, "I", taboo_modifier=0, C = 0)):
                ch_v "It looks totally hot, right?"
            elif Custom == 7:

                $ Girl.change_face("_bemused", 1)
                if Tempshame >= 30:
                    ch_v "Whatever, perv."
                elif Tempshame >= 15:
                    ch_v "Sure, why not."
                else:
                    ch_v "Sure, I guess."
            elif Tempshame <= 15:
                $ Girl.change_face("_bemused", 1)
                ch_v "I think this is too breezy."
                $ Agree = 0
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("_bemused", 1)
                ch_v "I could swim in this. . ."
            elif Tempshame <= 25 and (approval_check(Girl, 2300, taboo_modifier=0, C = 0) or approval_check(Girl, 700, "I", taboo_modifier=0, C = 0)):
                ch_v "I guess this is fine. . ."
            elif Tempshame <= 25:
                $ Girl.change_face("_angry", 1)
                ch_v "I really couldn't wear this out."
                $ Agree = 0
            elif (approval_check(Girl, 2500, taboo_modifier=0, C = 0) or approval_check(Girl, 800, "I", taboo_modifier=0, C = 0)):
                $ Girl.change_face("_bemused", 1)
                ch_v "It's pretty hot, right?"
            else:
                $ Girl.change_face("_angry", 1)
                ch_v "As if."
                $ Agree = 0



        if Custom == 5:
            $ Girl.second_custom_outfit = [2,Girl.outfit["gloves"],Girl.outfit["bottom"],Girl.outfit["top"],Girl.outfit["neck"],Girl.outfit["bra"],Girl.outfit["underwear"],Girl.outfit["front_outer_accessory"],Girl.outfit["hair"],Girl.outfit["hose"],Tempshame]
            $ Girl.second_custom_outfit["outfit_active"] = 2 if Agree else 1
        elif Custom == 6:
            $ Girl.third_custom_outfit = [2,Girl.outfit["gloves"],Girl.outfit["bottom"],Girl.outfit["top"],Girl.outfit["neck"],Girl.outfit["bra"],Girl.outfit["underwear"],Girl.outfit["front_outer_accessory"],Girl.outfit["hair"],Girl.outfit["hose"],Tempshame]
            $ Girl.third_custom_outfit["outfit_active"] = 2 if Agree else 1
        elif Custom == 4:
            if Agree:
                $ Girl.gym_clothes = [2,Girl.outfit["gloves"],Girl.outfit["bottom"],Girl.outfit["top"],Girl.outfit["neck"],Girl.outfit["bra"],Girl.outfit["underwear"],Girl.outfit["front_outer_accessory"],Girl.outfit["hair"],Girl.outfit["hose"],Tempshame]
        elif Custom == 7:
            $ Girl.sleepwear = [2,Girl.outfit["gloves"],Girl.outfit["bottom"],Girl.outfit["top"],Girl.outfit["neck"],Girl.outfit["bra"],Girl.outfit["underwear"],Girl.outfit["front_outer_accessory"],Girl.outfit["hair"],Girl.outfit["hose"],Tempshame]
            $ Girl.sleepwear["outfit_active"] = 2 if Agree else 1
        elif Custom == 10:
            if Agree:
                $ Girl.swimwear = [2,Girl.outfit["gloves"],Girl.outfit["bottom"],Girl.outfit["top"],Girl.outfit["neck"],Girl.outfit["bra"],Girl.outfit["underwear"],Girl.outfit["front_outer_accessory"],Girl.outfit["hair"],Girl.outfit["hose"],Tempshame]
        elif Custom == 3:
            $ Girl.first_custom_outfit = [2,Girl.outfit["gloves"],Girl.outfit["bottom"],Girl.outfit["top"],Girl.outfit["neck"],Girl.outfit["bra"],Girl.outfit["underwear"],Girl.outfit["front_outer_accessory"],Girl.outfit["hair"],Girl.outfit["hose"],Tempshame]
            $ Girl.first_custom_outfit["outfit_active"] = 2 if Agree else 1
        else:
            "Tell Oni Custom outfit was [Custom]"
            $ RogueX.gibberish = 5
    elif Girl.taboo <= 20:

        $ Tempshame /= 2

    $ Girl.outfit["shame"] = Tempshame

    if Custom == 20:

        return

    if Check:
        pass
    elif bg_current == "HW Party" or (bg_current == "bg_player" and "halloween" in Player.daily_history):

        pass
    elif "exhibitionist" in Girl.traits and Tempshame <= 20:

        pass
    elif Girl == StormX and StormX in Rules:
        pass
    elif Tempshame <= 12:

        pass
    elif Girl.outfit["top"] == "_towel" and Girl.location == "bg_showerroom":

        pass
    elif Tempshame <= 15 and (approval_check(Girl, 1500) or approval_check(Girl, 500, "I")):

        pass
    elif Tempshame <= 20 and (Girl.location == "bg_dangerroom" or Girl.location == "bg_pool"):

        pass
    elif Tempshame <= 20 and (approval_check(Girl, 1800) or approval_check(Girl, 650, "I")):

        pass
    elif Tempshame <= 25 and (approval_check(Girl, 2000) or approval_check(Girl, 700, "I")):

        pass
    elif (approval_check(Girl, 2500) or approval_check(Girl, 800, "I")):

        pass
    elif Girl.location == "bg_dangerroom" and Girl.outfit_name == "gym_clothes":
        $ Girl.change_outfit("gym_clothes",outfit_changed = 1)
    elif not Girl.taboo:
        pass
    elif Girl.outfit_name == "swimwear" and bg_current == "bg_pool":
        pass
    elif bg_current == "bg_pool" and Girl.bra_number() >= 3 and Girl.underwear_number() >= 6:
        pass
    elif Girl.outfit_name == "gym_clothes" and bg_current == "bg_dangerroom":
        pass
    else:

        if Girl.location == bg_current:
            if Girl == RogueX:
                ch_r "I'll be right back, I've got to change out of this."
            elif Girl == KittyX:
                ch_k "One sec, I gotta change real quick."
            elif Girl == EmmaX:
                ch_e "I'm afraid I'll have to change, one moment."
            elif Girl == LauraX:
                ch_l "One sec, I gotta change real quick."
            elif Girl == JeanX:
                ch_j "Wait while I get changed."
            elif Girl == StormX:
                ch_s "I'll need to change into something more substantial."
            elif Girl == JubesX:
                ch_v "I need to throw something on real quick. . ."
        if Girl.location == "bg_dangerroom":
            $ Girl.outfit_name =  "gym_clothes"
        elif Girl.location == "bg_pool" and Girl.swimwear["outfit_active"]:
            $ Girl.outfit_name =  "swimwear"
        else:
            $ Girl.outfit_name = renpy.random.choice(["casual1", "casual2"])

        $ Girl.add_word(1,"modesty", "modesty")
        $ Girl.wet = False
        $ Girl.change_outfit(outfit_changed = True)
        if Girl == RogueX:
            ch_r "That wasn't really \"outdoor ready\"."
        elif Girl == KittyX:
            ch_k "I just needed to throw some more on."
        elif Girl == EmmaX:
            ch_e "I wouldn't want to be \"inappropriate\"."
        elif Girl == LauraX:
            ch_l "That wasn't really \"outdoors\" wear."
        elif Girl == JeanX:
            ch_j "Couldn't really be out in that."
        elif Girl == StormX:
            ch_s "I'm afraid Charles would not approve of that look around students."
        elif Girl == JubesX:
            ch_v "That was kinda. . . private. . ."
    return











label Display_dress_screen(Girl=focused_Girl):


    if renpy.showing('dress_screen'):
        return True

    if Girl == StormX:
        if not Girl.taboo or StormX in Rules:
            return True
        else:
            ch_s "I'm afraid rules are rules."

    if Girl.taboo:
        return False

    $ Girl.change_face("_bemused",1,eyes="_side")
    if "screen" in Girl.daily_history:
        pass
    elif Girl == RogueX:
        ch_r "I'm not really comfortable like this."
    elif Girl == KittyX:
        ch_k "I'm getting kinda exposed here."
    elif Girl == EmmaX:
        ch_e "I'm feeling a bit exposed here. . ."
    elif Girl == LauraX:
        ch_l "I don't know about showing this much skin."
    elif Girl == JeanX:
        ch_j "I don't think you're ready for this. . ."
    elif Girl == JeanX:
        ch_j "I don't think you're ready for this. . ."
    elif Girl == JubesX:
        ch_v "I don't know, this is moving a little fast. . ."
    $ Girl.add_word(1,0, "screen")
    $ Girl.change_face("_bemused",1)
    Girl.voice "Mind if I get behind a dressing screen?"
    menu:
        extend ""
        "Go ahead":
            show dress_screen zorder 150
            if Girl == RogueX:
                ch_r "Thanks."
            elif Girl == KittyX:
                ch_k "Great."
            elif Girl == EmmaX:
                ch_e "Thank you."
            elif Girl == LauraX:
                ch_l "K."
            elif Girl == JeanX:
                ch_j "Good."
            elif Girl == JubesX:
                ch_v "Oh, thanks. . ."
            return True
        "No, don't":
            if Girl == RogueX:
                ch_r "Fine then. . ."
            elif Girl == KittyX:
                ch_k "Ok then. . ."
            elif Girl == EmmaX:
                ch_e "Fair enough. . ."
            elif Girl == LauraX:
                ch_l "Ok. . ."
            elif Girl == JeanX:
                ch_j "Ok then."
            elif Girl == JubesX:
                ch_v "Well, fine. . ."

    return False
