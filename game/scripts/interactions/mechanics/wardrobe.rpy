label change_wardrobe(Girl):
    if Girl.taboo:
        if "exhibitionist" in Girl.traits:
            if Girl == RogueX:
                ch_r "Oooh, naughty. . ."
            elif Girl == KittyX:
                ch_k "Mmmmm. . ."
            elif Girl == EmmaX:
                ch_e "Mmmmm. . ."
            elif Girl == LauraX:
                ch_l "Yes? . ."
            elif Girl == JeanX:
                ch_j "Yeah? . ."
            elif Girl == StormX:
                ch_s "Oh, here? . ."
            elif Girl == JubesX:
                ch_v "Yes? . ."
        elif approval_check(Girl, 900, taboo_modifier = 4) or approval_check(Girl, 400, "I", taboo_modifier = 3):
            if Girl == RogueX:
                ch_r "Well, I mean, it's pretty public here, but I guess I could. . ."
            elif Girl == KittyX:
                ch_k "This is[Girl.like]pretty. . . exposed. . ."
            elif Girl == EmmaX:
                ch_e "This isn't really the appropriate place for it, however. . ."
            elif Girl == LauraX:
                ch_l "I don't think I'm supposed to undress around here. . ."
            elif Girl == JeanX:
                ch_j "Oh, I guess we could. . ."
            elif Girl == StormX:
                ch_s "I'm not supposed to undress here. . ."
            elif Girl == JubesX:
                ch_v "It's pretty public here, I don't think so. . ."
        else:
            if Girl == RogueX:
                ch_r "This is a pretty public place for that, don't you think?"
                ch_r "We can talk about that back in our rooms."
            elif Girl == KittyX:
                ch_k "This is[Girl.like]pretty exposed, right?"
                ch_k "Can't we talk about this in our rooms?"
            elif Girl == EmmaX:
                ch_e "I'd rather discuss that in private."
            elif Girl == LauraX:
                ch_l "I don't think I'm supposed to undress around here. . ."
                ch_l "Can we talk about this in our rooms?"
            elif Girl == JeanX:
                ch_j "I think this is kind of exposed. . ."
                ch_j "Can we talk about this in our rooms?"
            elif Girl == StormX:
                ch_s "I'm not supposed to undress here. . ."
                ch_s "Can we talk about this in our rooms?"
            elif Girl == JubesX:
                ch_v "It's pretty public here, I don't think so. . ."
                ch_v "Can't we talk about this in our rooms?"

            return
    elif approval_check(Girl, 900, taboo_modifier = 4) or approval_check(Girl, 600, "L") or approval_check(Girl, 300, "O"):
        if Girl == RogueX:
            ch_r "Ok, what did you want to tell me about my clothes?"
        elif Girl == KittyX:
            ch_k "[Girl.Like]what were you thinking here?"
        elif Girl == EmmaX:
            ch_e "What about my style?"
        elif Girl == LauraX:
            ch_l "Oh? What about them?"
        elif Girl == JeanX:
            ch_j "Oh? What about them?"
        elif Girl == StormX:
            ch_s "Oh? What about them?"
        elif Girl == JubesX:
            ch_v "Oh, what were you thinking? . ."
    else:
        if Girl == RogueX:
            ch_r "I'm not really interested in your fashion opinions."
        elif Girl == KittyX:
            ch_k "I'll let you know when I care what you think."
        elif Girl == EmmaX:
            ch_e "I'll let you know when I care what you think."
        elif Girl == LauraX:
            ch_l "I don't think about my clothes much."
            ch_l "You shouldn't either."
        elif Girl == JeanX:
            ch_j "Just enjoy, don't advise."
        elif Girl == StormX:
            ch_s "I don't really need fashion advice, thank you."
        elif Girl == JubesX:
            ch_v "I don't think I really need your fashion advice."

        return

    $ shift_focus(Girl)

    $ public = 0

    if "exhibitionist" in Girl.traits:
        $ public += 1

    if Girl.reputation <= 200:
        $ public += 2
    elif Girl.reputation <= 400:
        $ public += 1

    if "public" in Girl.history:
        $ public += 2

    while True:
        $ Girl.change_face()

        menu:
            extend ""
            "Let's talk about your outfits.":
                call outfits_menu(Girl)
            "Let's talk about your outfit schedule.":
                call set_outfit_schedule(Girl)
            "About your tops. . .":
                call tops_menu(Girl)
            "About your legwear. . .":
                call bottoms_menu(Girl)
            "About your underwear. . .":
                call lingerie_menu(Girl)
            "About your special clothing. . .":
                call special_menu(Girl)
            "About your accessories. . .":
                call accessories_menu(Girl)
            "Would you be more comfortable behind a screen?(locked)" if Girl.location == Player.location and (Girl.taboo or renpy.showing("dress_screen")):
                pass
            "Would you be more comfortable behind a screen?" if Girl.location == Player.location and (not Girl.taboo and not renpy.showing('dress_screen')):
                if Girl == StormX:
                    ch_s "I won't need it, but I appreciate the offer."
                elif approval_check(Girl, 1500) or (Girl.seen_breasts and Girl.seen_pussy):
                    if Girl == RogueX:
                        ch_r "Don't really need that, thanks."
                    elif Girl == KittyX:
                        ch_k "Probably won't need it, thanks."
                    elif Girl == EmmaX:
                        ch_e "Oh, I think we can handle this."
                    elif Girl == LauraX:
                        ch_l "Probably won't need it, thanks."
                    elif Girl == JeanX:
                        ch_j "I don't see why."
                    elif Girl == JubesX:
                        ch_v "I think I'm fine. . ."

                else:
                    show dress_screen zorder 150

                    if Girl == RogueX:
                        ch_r "This is more comfortable, thanks."
                    elif Girl == KittyX:
                        ch_k "Yeah, this is a bit more comfortable, thanks."
                    elif Girl == EmmaX:
                        ch_e "Yes, this will be more comfortable."
                    elif Girl == LauraX:
                        ch_l "Yeah, this is better, thanks."
                    elif Girl == JeanX:
                        ch_j "Yeah, this'll work."
                    elif Girl == JubesX:
                        ch_v "Yeah, this is better, thanks."

            "Could I get a look?" if renpy.showing('dress_screen'):
                call outfitShame(Girl, 0, 2)

                if _return:
                    hide dress_screen
            "Could I get a look?" if Girl.location != Player.location:
                call outfitShame(Girl, 0, 2)

                if _return:
                    show PhoneSex zorder 150

                    if Girl == RogueX:
                        ch_r "How's that? . ."
                    elif Girl == KittyX:
                        ch_k "Cute? . ."
                    elif Girl == EmmaX:
                        ch_e "Ok, a quick shot for you. . ."
                    elif Girl == LauraX:
                        ch_l "Ok, that good?"
                    elif Girl == JeanX:
                        ch_j "Nice, right?"
                    elif Girl == StormX:
                        ch_s "What do you think?"
                    elif Girl == JubesX:
                        ch_v "Ok, that good?"

                    hide PhoneSex
            # "Gift for you(locked)" if Girl.location != Player.location:
            #     pass
            # "Gift for you" if Girl.location == Player.location:
            #     ch_p "I'd like to give you something."
            #
            #     call gifts
            "Switch to. . .":
                if renpy.showing('dress_screen'):
                    call outfitShame(Girl, 0, 2)

                    if _return:
                        hide dress_screen
                    else:
                        $ Girl.change_Outfit()

                $ Girl.set_temp_outfit()

                $ stored_Girl = Girl

                call switch_chat
                call change_wardrobe(Girl)

                $ Girl = stored_Girl

                $ shift_focus(Girl)
            "You look good like that.":
                if "wardrobe" not in Girl.recent_history:
                    if Girl == StormX and (Girl.top_number() + Girl.bra_number()<4) or (Girl.underwear_number() + Girl.bottom_number() < 5):
                        $ Girl.change_face("sly", eyes = "down")

                        ch_s "I understand why -you- would think so. . ."

                        $ Girl.change_face("sly")
                    elif Girl.had_chat[1] <= 1:
                        call change_Girl_stat(Girl, "love", 15)
                        call change_Girl_stat(Girl, "obedience", 20)

                        if Girl == RogueX:
                            ch_r "Aw, that's sweet."
                        elif Girl == KittyX:
                            ch_k "That's[Girl.like]really nice of you to say."
                        elif Girl == EmmaX:
                            ch_e "I thought so as well."
                        elif Girl == LauraX:
                            ch_l "Oh! Thank you."
                        elif Girl == JeanX:
                            ch_j "Of course?"
                        elif Girl == StormX:
                            ch_s "Oh, how sweet of you to say so."
                        elif Girl == JubesX:
                            ch_v "Oh! Thank you."
                    elif Girl.had_chat[1] <= 10:
                        call change_Girl_stat(Girl, "love", 5)
                        call change_Girl_stat(Girl, "obedience", 7)

                        if Girl == RogueX:
                            ch_r "Thanks."
                        elif Girl == KittyX:
                            ch_k "I like it too."
                        elif Girl == EmmaX:
                            ch_e "Isn't it?"
                        elif Girl == LauraX:
                            ch_l "Right?"
                        elif Girl == JeanX:
                            ch_j "Right?"
                        elif Girl == StormX:
                            ch_s "I do enjoy this look."
                        elif Girl == JubesX:
                            ch_v "Right?"
                    elif Girl.had_chat[1] <= 50:
                        call change_Girl_stat(Girl, "love", 1)
                        call change_Girl_stat(Girl, "obedience", 1)

                        if Girl == RogueX:
                            ch_r "Ok."
                        elif Girl == KittyX:
                            ch_k "Yeah."
                        elif Girl == LauraX:
                            ch_l "Uh-huh."
                        elif Girl == JeanX:
                            ch_j "Uh-huh."
                        elif Girl == StormX:
                            ch_s "Thank you. . ."
                        elif Girl == JubesX:
                            ch_v "Uh-huh."
                    else:
                        if Girl == RogueX:
                            ch_r "Ok."
                        elif Girl == KittyX:
                            ch_k "Sure."
                        elif Girl == LauraX:
                            ch_l "Sure."
                        elif Girl == JeanX:
                            ch_j "Sure."
                        elif Girl == StormX:
                            ch_s "Certainly."
                        elif Girl == JubesX:
                            ch_v "Sure."

                    $ Girl.recent_history.append("wardrobe")

                if renpy.showing('dress_screen'):
                    call outfitShame(Girl, 0, 2)

                    if _return:
                        hide dress_screen
                    else:
                        $ Girl.change_Outfit()

                $ Girl.set_temp_outfit()
                $ Girl.had_chat[1] += 1

                return

label outfits_menu(Girl):
    while True:
        menu:
            "That looks really good on you, you should remember that one.":
                menu:
                    "Which slot would you like this saved in?"
                    "First custom outfit":
                        call outfitShame(Girl, 3, 1)
                    "Second custom outfit":
                        call outfitShame(Girl, 5, 1)
                    "Third custom outfit":
                        call outfitShame(Girl, 6, 1)
                    "Gym clothes":
                        call outfitShame(Girl, 4, 1)
                    "Sleepwear":
                        call outfitShame(Girl, 7, 1)
                    "Swimwear":
                        call outfitShame(Girl, 10, 1)
                    "Never mind":
                        pass
            "I really like that green top and skirt outfit you have." if Girl == RogueX:
                $ Girl.change_Outfit()

                menu:
                    "You should wear this one for now.":
                        $ Girl.outfit_name = "default"

                        ch_r "Ok, [Girl.player_petname], I like this one too."
                    "Let's try something else though.":
                        ch_r "Sure."
            "That pink top and pants look really nice on you." if Girl == RogueX:
                $ Girl.change_Outfit("second_casual")

                menu:
                    "You should wear this one for now.":
                        $ Girl.outfit_name = "second_casual"

                        ch_r "Sure, [Girl.player_petname], that one's nice."
                    "Let's try something else though.":
                        ch_r "Ok."
            "I really like that pink shirt and capris outfit you wear." if Girl == KittyX:
                $ Girl.change_Outfit()

                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ Girl.outfit_name = "default"

                        ch_k "I used to wear that one[Girl.like]every day!"
                    "Let's try something else though.":
                        ch_k "K."
            "That red shirt and black jeans look really nice on you." if Girl == KittyX:
                $ Girl.change_Outfit("second_casual")

                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ Girl.outfit_name = "second_casual"

                        ch_k "That one[Girl.like]used to be my favorite too!"
                    "Let's try something else though.":
                        ch_k "K."
            "I really like that teacher's look you wear." if Girl == EmmaX:
                $ Girl.change_Outfit()

                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ Girl.outfit_name = "default"

                        ch_e "Yes, a very tasteful look."
                    "Let's try something else though.":
                        ch_e "Very well."
            "That combat uniform you have looks really nice on you." if Girl == EmmaX:
                $ Girl.change_Outfit("second_casual")

                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ Girl.outfit_name = "second_casual"

                        ch_e "I really enjoyed wearing that one."
                    "Let's try something else though.":
                        ch_e "Very well."
            "Your leather combat outfit looks awesome." if Girl == LauraX:
                $ Girl.change_Outfit()

                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ Girl.outfit_name = "default"

                        ch_l "Yeah, I love wearing this one in the field."
                    "Let's try something else though.":
                        ch_l "Ok."
            "I like your leather jacket and skirt combo." if Girl == LauraX:
                $ Girl.change_Outfit("second_casual")
                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ Girl.outfit_name = "second_casual"

                        ch_l "Yeah, I mean, my cousin got it for me."
                    "Let's try something else though.":
                        ch_l "Ok."
            "Your pink shirt and pants outfit is cute." if Girl == JeanX:
                $ Girl.change_Outfit()

                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ Girl.outfit_name = "default"

                        ch_j "Yeah, I've worn this one a long time."
                    "Let's try something else though.":
                        ch_j "Sure. . ."
            "What about your green t-shirt and skirt outfit?" if Girl == JeanX:
                $ Girl.change_Outfit("second_casual")
                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ Girl.outfit_name = "second_casual"

                        ch_j "Ok, this one has a real \"classic\" feel. . ."
                    "Let's try something else though.":
                        ch_j "Sure. . ."
            "Try on that skirt combo." if Girl == StormX:
                $ Girl.change_Outfit()

                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ Girl.outfit_name = "default"

                        ch_s "Yes, this is my preferred casual outfit."
                    "Let's try something else though.":
                        ch_s "Ok."
            "Can I see your leather jacket and pants combo?" if Girl == StormX:
                $ Girl.change_Outfit("second_casual")

                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ Girl.outfit_name = "second_casual"

                        ch_s "Yes, I find this one more stylish."
                    "Let's try something else though.":
                        ch_s "Ok."
            "You look great in your red and blue outfit." if Girl == JubesX:
                $ Girl.change_Outfit()

                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ Girl.outfit_name = "default"

                        ch_v "Yeah, this one's a classic, right?"
                    "Let's try something else though.":
                        ch_v "Ok."
            "Can I see your black leather combo?" if Girl == JubesX:
                $ Girl.change_Outfit("second_casual")

                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ Girl.outfit_name = "second_casual"

                        ch_v "I know it's a little edgy and all, but I like it!"
                    "Let's try something else though.":
                        ch_v "Ok."
            "Remember that outfit we put together?" if Girl.first_custom_outfit["outfit_active"] or Girl.second_custom_outfit["outfit_active"] or Girl.third_custom_outfit["outfit_active"]:
                $ counter = 0

                while 1:
                    menu:
                        "Throw on first custom outfit." if Girl.first_custom_outfit["outfit_active"]:
                            $ Girl.change_Outfit("custom1")

                            $ counter = 3
                        "Throw on first custom outfit.(locked)" if not Girl.first_custom_outfit["outfit_active"]:
                            pass
                        "Throw on second custom outfit." if Girl.second_custom_outfit["outfit_active"]:
                            $ Girl.change_Outfit("custom2")

                            $ counter = 5
                        "Throw on second custom outfit.(locked)" if not Girl.second_custom_outfit["outfit_active"]:
                            pass
                        "Throw on third custom outfit." if Girl.third_custom_outfit["outfit_active"]:
                            $ Girl.change_Outfit("custom3")

                            $ counter = 6
                        "Throw on third custom outfit.(locked)" if not Girl.third_custom_outfit["outfit_active"]:
                            pass
                        "You should wear this one in private.(locked)" if not counter:
                            pass
                        "You should wear this one in private." if counter:
                            if counter == 5:
                                $ Girl.clothing[9] = 5
                            elif counter == 6:
                                $ Girl.clothing[9] = 6
                            else:
                                $ Girl.clothing[9] = 3

                            if Girl == StormX:
                                ch_s "That would be fine."
                            else:
                                Girl.voice "Ok, sure."
                        "On second thought, forget about that one outfit. . .":
                            if Girl == RogueX:
                                $ forget_line = "Ok, no problem."
                            elif Girl == KittyX:
                                $ forget_line = "Ok, no problem."
                            elif Girl == EmmaX:
                                $ forget_line = "Very well."
                            elif Girl == LauraX:
                                $ forget_line = "Ok."
                            elif Girl == JeanX:
                                $ forget_line = "Ok."
                            elif Girl == StormX:
                                $ forget_line = "Fine."
                            elif Girl == JubesX:
                                $ forget_line = "Ok."

                            menu:
                                extend "Which one did you mean?"
                                "Forget first custom outfit." if Girl.first_custom_outfit["outfit_active"]:
                                    Girl.voice "[forget_line]"

                                    $ Girl.first_custom_outfit["outfit_active"] = 0
                                "Forget first custom outfit.(locked)" if not Girl.first_custom_outfit["outfit_active"]:
                                    pass
                                "Forget second custom outfit." if Girl.second_custom_outfit["outfit_active"]:
                                    Girl.voice "[forget_line]"

                                    $ Girl.second_custom_outfit["outfit_active"] = 0
                                "Forget second custom outfit.(locked)" if not Girl.second_custom_outfit["outfit_active"]:
                                    pass
                                "Forget third custom outfit." if Girl.third_custom_outfit["outfit_active"]:
                                    Girl.voice "[forget_line]"

                                    $ Girl.third_custom_outfit["outfit_active"] = 0
                                "Forget third custom outfit(locked)" if not Girl.third_custom_outfit["outfit_active"]:
                                    pass
                                "Back to the other outfits.":
                                    pass
                        "You should wear this one out." if counter:
                            call Custom_Out(Girl, counter)
                        "You should wear this one out. [[choose outfit first](locked)" if not counter:
                            pass
                        "Ok, back to what we were talking about. . .":
                            $ counter = 0

                            return
            "Remember that outfit we put together?(locked)" if not Girl.first_custom_outfit["outfit_active"] and not Girl.second_custom_outfit["outfit_active"] and not Girl.third_custom_outfit["outfit_active"]:
                pass
            "Could you put on your gym clothes?" if not Girl.taboo or Player.location == "bg_dangerroom":
                $ Girl.change_Outfit("gym_clothes")
            "Could you try on your sleep outfit?" if not Girl.taboo:
                if approval_check(Girl, 1200):
                    $ Girl.change_Outfit("sleepwear")
                else:
                    call ask_for_dress_screen(Girl)

                    if _return:
                        $ Girl.change_Outfit("sleepwear")
            "Can I see your swimsuit?" if (not Girl.taboo or Player.location == "bg_pool") and Girl.swimwear["outfit_active"]:
                $ Girl.change_Outfit("swimwear")
            "Can I see your swimsuit?(locked)" if (Girl.taboo and Player.location != "bg_pool") or not Girl.swimwear["outfit_active"]:
                pass
            "Could you put on your Halloween costume again?" if "halloween" in Girl.history:
                if Girl == RogueX:
                    ch_r "Sure."
                elif Girl == KittyX:
                    ch_k "Sure."
                elif Girl == EmmaX:
                    ch_e "Very well. . ."
                elif Girl == LauraX:
                    ch_l "Ok."
                elif Girl == JeanX:
                    ch_j "Ok."
                elif Girl == StormX:
                    ch_s "Fine."
                elif Girl == JubesX:
                    ch_v "Ok."

                $ Girl.change_Outfit("costume")
            "Your birthday suit looks really great. . .":
                $ Girl.change_face("sexy", 1)

                $ agreed = False

                if Girl.fully_nude:
                    if Girl == RogueX:
                        ch_r "Can't get much more naked than this."
                    elif Girl == KittyX:
                        ch_k "You're kidding, right?"
                    elif Girl == EmmaX:
                        ch_e "Apparently so. . ."
                    elif Girl == LauraX:
                        ch_l "Yeah. . . wait, how would you know?"
                    elif Girl == JeanX:
                        ch_j "Duh."
                    elif Girl == StormX:
                        ch_s "Thank you."
                    elif Girl == JubesX:
                        ch_v "Uh-huh. . . wait, how would you know?!"
                elif Girl.seen_breasts and Girl.seen_pussy and approval_check(Girl, 1200, taboo_modifier=(5-public)):
                    if Girl == RogueX:
                        ch_r "Naughty boy. . ."
                    elif Girl == KittyX:
                        ch_k "[Girl.Like]Reow. . ."
                    elif Girl == EmmaX:
                        ch_e "I'll take that as an invitation. . ."
                    elif Girl == LauraX:
                        ch_l "You know it. . ."
                    elif Girl == JeanX:
                        ch_j "You know it. . ."
                    elif Girl == StormX:
                        ch_s "Certainly. . ."
                    elif Girl == JubesX:
                        ch_v ". . . yeah?"

                    $ agreed = True
                elif approval_check(Girl, 2000, taboo_modifier=(5-public)):
                    if Girl == RogueX:
                        ch_r "Hmm. . . you move fast, but I suppose for you. . ."
                    elif Girl == KittyX:
                        ch_k "You don't[Girl.like]mess around, huh."
                    elif Girl == EmmaX:
                        ch_e "I suppose you've earned it. . ."
                    elif Girl == LauraX:
                        ch_l "Skipping straight to that?"
                    elif Girl == JeanX:
                        ch_j "Oh, going right for it, huh?"
                    elif Girl == StormX:
                        ch_s "No foreplay?"
                    elif Girl == JubesX:
                        ch_v "Well you get to the point!"

                    $ agreed = True
                elif Girl == StormX and not approval_check(Girl, 500, taboo_modifier=0):
                    $ Girl.change_face("confused", 1, mouth = "smirk")

                    ch_s "I don't exactly get nude on command, you know. . ."

                    $ Girl.change_face("bemused", 0)
                elif Girl == StormX and Girl.taboo and StormX not in Rules:
                    ch_s "Maybe, but not here. . ."
                elif Girl.seen_breasts and Girl.seen_pussy and approval_check(Girl, 1200, taboo_modifier=0):
                    if Girl == RogueX:
                        ch_r "Well, maybe if it weren't quite so. . . public here."
                    elif Girl == KittyX:
                        ch_k "[Girl.Like]this is a little exposed. . ."
                    elif Girl == EmmaX:
                        ch_e "As you're well aware, but this isn't the appropriate venue. . ."
                    elif Girl == LauraX:
                        ch_l "Maybe, but not here. . ."
                    elif Girl == JeanX:
                        ch_j "You know it, but maybe not right here. . ."
                    elif Girl == JubesX:
                        ch_v "Maaaybe, but not here. . ."
                elif approval_check(Girl, 2000, taboo_modifier=0):
                    if Girl == RogueX:
                        ch_r "I might consider it if we had some privacy. . ."
                    elif Girl == KittyX:
                        ch_k "Maybe if we were alone?"
                    elif Girl == EmmaX:
                        ch_e "I assure you it is, but this isn't the appropriate venue. . ."
                    elif Girl == LauraX:
                        ch_l "Maybe, but not here. . ."
                    elif Girl == JeanX:
                        ch_j "Maybe, but not here. . ."
                    elif Girl == JubesX:
                        ch_v "Maaaybe, but not here. . ."
                elif approval_check(Girl, 1000, taboo_modifier=0):
                    if Girl == RogueX:
                        $ Girl.change_face("surprised", 1)

                        ch_r "Hmm. . . you're getting a bit ahead of yourself, [Girl.player_petname]."
                    elif Girl == KittyX:
                        $ Girl.change_face("surprised", 1)

                        ch_k "[Girl.Like]get to know a girl first, [Girl.player_petname]."
                    elif Girl == EmmaX:
                        $ Girl.change_face("surprised", 1)

                        ch_e "I assure you that it is, but that's not the way to ask."
                    elif Girl == LauraX:
                        $ Girl.change_face("confused", 1, mouth = "smirk")

                        ch_l "Yeah, but I'm not exactly showing it off."

                        $ Girl.change_face("bemused", 0)
                    elif Girl == JeanX:
                        $ Girl.change_face("confused", 1, mouth = "smirk")

                        ch_j "Yeah, but I'm not sharing."

                        $ Girl.change_face("bemused", 0)
                    elif Girl == StormX:
                        $ Girl.change_face("confused", 1, mouth = "smirk")

                        ch_s "Yeah, but I'm not exactly showing it off."

                        $ Girl.change_face("bemused", 0)
                    elif Girl == JubesX:
                        $ Girl.change_face("confused", 1, mouth = "smirk")

                        ch_v "Yeah, but you'll just have to keep guessing. . ."

                        $ Girl.change_face("bemused", 0)
                else:
                    $ Girl.change_face("angry", 1)

                    if Girl == RogueX:
                        ch_r "What sort of common strumpet do you take me for?"
                    elif Girl == KittyX:
                        ch_k "Yeah[Girl.like]it does."
                    elif Girl == EmmaX:
                        ch_e "Not the worst line I've heard."
                        ch_e ". . . but close."
                    elif Girl == LauraX:
                        ch_l "What's it to you?"
                    elif Girl == JeanX:
                        ch_j "Of course it is."
                        ch_j "Oh, you wanted to see it?"
                    elif Girl == StormX:
                        ch_s "I would rather not."
                    elif Girl == JubesX:
                        ch_v "That's not really any of your business!"

                if agreed:
                    call fully_undress(Girl)

                    $ lines = ["She lets all her clothes drop into a pile at her feet.",
                        "She pulls all her clothes off and throws them in a heap on the floor.",
                        "She strips down.",
                        "She throws her clothes off at her feet."]

                    $ line = renpy.random.choice(lines)

                    "[line]"

                    $ Girl.change_face("sexy")

                    menu:
                        "You know, you should stay like this for now.":
                            if "exhibitionist" in Girl.traits:
                                if Girl == RogueX:
                                    ch_r "You sure know how to rev my engines. . ."
                                elif Girl == KittyX:
                                    ch_k "I'm[Girl.like]getting a little wet just thinking about it."
                                elif Girl == EmmaX:
                                    ch_e "Mmmmm. . ."
                                elif Girl == LauraX:
                                    ch_l "Mmmmm. . ."
                                elif Girl == JeanX:
                                    ch_l "Mmmmm. . ."
                                elif Girl == StormX:
                                    ch_l "Mmmmm. . ."
                                elif Girl == JubesX:
                                    ch_l "Mmmmm. . ."

                                call change_Girl_stat(Girl, "lust", 10)
                                call change_Girl_stat(Girl, "lust", 5)
                                $ Girl.change_face("sexy", 1)
                            elif (Girl == JeanX and "nowhammy" not in Girl.traits) or approval_check(Girl, 800, "I") or approval_check(Girl, 2800, taboo_modifier=0):
                                if Girl == RogueX:
                                    ch_r "Heh, all right [Girl.player_petname]."
                                elif Girl == KittyX:
                                    ch_k "I guess we could. . ."
                                elif Girl == EmmaX:
                                    ch_e "Oooh, that would cause quite a stir. . ."
                                elif Girl == LauraX:
                                    ch_l "Exciting. . ."
                                elif Girl == JeanX:
                                    ch_j "Sure, ok. . ."
                                elif Girl == StormX:
                                    ch_s "You know, I might. . ."
                                elif Girl == JubesX:
                                    ch_v "Fun. . ."

                            elif Girl == EmmaX and approval_check(Girl, 400, "I") and approval_check(Girl, 1200, taboo_modifier=0):
                                $ Girl.change_face("bemused", 1, eyes = "side")

                                ch_e "You shouldn't suggest such things. . ."
                            else:
                                $ Girl.change_face("sexy", 1, eyes = "surprised")

                                if Girl == RogueX:
                                    ch_r "I'm afraid not, [Girl.player_petname], this is just for between you and me."
                                elif Girl == KittyX:
                                    ch_k "No way! That'd be[Girl.like]totally embarrassing!"
                                elif Girl == EmmaX:
                                    ch_e "Impossible."
                                elif Girl == LauraX:
                                    ch_l "I probably shouldn't. Sorry."
                                elif Girl == JeanX:
                                    ch_j "Yeah, um, I'm not into that right now. . ."
                                elif Girl == StormX:
                                    ch_s "I probably shouldn't. I am sorry."
                                elif Girl == JubesX:
                                    ch_v "I really won't."
                        "Let's try something else though.":
                            if "exhibitionist" in Girl.traits:
                                if Girl == RogueX:
                                    ch_r "Hmm, too bad you didn't want me to wear this out. . ."
                                elif Girl == KittyX:
                                    ch_k "Aw, do I have to?"
                                elif Girl == EmmaX:
                                    ch_e "Too much for you to handle?"
                                elif Girl == LauraX:
                                    ch_l "Are you sure?"
                                elif Girl == JeanX:
                                    ch_j "Oh, ok. . ."
                                elif Girl == StormX:
                                    ch_s "Are you certain?"
                                elif Girl == JubesX:
                                    ch_v "Really?"
                            elif (Girl == JeanX and "nowhammy" not in Girl.traits) or approval_check(Girl, 800, "I") or approval_check(Girl, 2800, taboo_modifier=0):
                                $ Girl.change_face("bemused", 1)

                                if Girl == RogueX:
                                    ch_r "You know, for a second there I thought you might want me to wear this out. . ."
                                    ch_r "Hehe, um. . ."
                                elif Girl == KittyX:
                                    ch_k "It's a good thing you didn't[Girl.like]ask me to wear this outside."
                                    ch_k "A good thing. . ."
                                elif Girl == EmmaX:
                                    ch_e "Because obviously I couldn't go around like this. . ."
                                elif Girl == LauraX:
                                    ch_l "I was worried you expected me to go out like this."
                                    ch_l ". . ."
                                elif Girl == JeanX:
                                    ch_j "I thought you might want me to go out like this. . ."
                                    ch_j ". . ."
                                elif Girl == StormX:
                                    ch_s "I expected that you wanted me to go out like this."
                                    ch_s ". . ."
                                elif Girl == JubesX:
                                    ch_v "Oh! i thought you wanted me to wear this out. . ."
                                    ch_v ". . ."
                            else:
                                $ Girl.change_face("confused", 1)

                                if Girl == RogueX:
                                    ch_r "Well obviously. It's not like I'd ever go out like this."
                                elif Girl == KittyX:
                                    ch_k "I[Girl.like]don't mind this around the room, but definitely not outside."
                                elif Girl == EmmaX:
                                    ch_e "So long as it's just the two of us, I don't mind this."
                                elif Girl == LauraX:
                                    ch_l "I don't mind you seeing my body, but. . ."
                                elif Girl == JeanX:
                                    ch_j "Yeah, I'm not into that right now. . ."
                                elif Girl == StormX:
                                    ch_s "I don't mind you seeing my body, but Charles does have his rules. . ."
                                elif Girl == JubesX:
                                    ch_v "Yeah, I mean, I wouldn't. . ."
            "Let's talk about something else.":
                return

label tops_menu(Girl):
    while True:
        $ Girl.change_face("bemused", 1)

        menu:
            "Why don't you take off the [Girl.Clothes[jacket].name]?" if Girl.Clothes["jacket"]:
                $ item = "no_jacket"
            "Why don't you go with no [Girl.Clothes[top].name]?" if Girl.Clothes["top"]:
                $ item = "no_top"
            "How about that green hoodie?" if Girl == RogueX and Girl.Clothes["jacket"] != "hoodie":
                $ item = "hoodie"
            "Put on your red jacket." if Girl == KittyX and Girl.Clothes["jacket"] != "jacket" and "halloween" in Girl.history:
                $ item = "jacket"
            "Put on that white jacket you have." if Girl == EmmaX and Girl.Clothes["jacket"] != "jacket":
                $ item = "jacket"
            "Try on that leather jacket." if Girl == LauraX and Girl.Clothes["jacket"] != "jacket":
                $ item = "jacket"
            "You look great in that leather jacket." if Girl == StormX and Girl.Clothes["jacket"] != "jacket":
                $ item = "jacket"
            "Throw on your yellow jacket." if Girl == JubesX and Girl.Clothes["jacket"] != "jacket":
                $ item = "jacket"
            "Try on the green mesh top." if Girl == RogueX and Girl.Clothes["top"] != "mesh_top":
                $ item = "mesh_top"
            "How about that pink top?" if Girl == RogueX and Girl.Clothes["top"] != "pink_top":
                $ item = "pink_top"
            "Try on that pink shirt you have." if Girl == KittyX and Girl.Clothes["top"] != "pink_top":
                $ item = "pink_top"
            "Try on that red T-shirt you have." if Girl == KittyX and Girl.Clothes["top"] != "red_shirt":
                $ item = "red_shirt"
            "Try on that white dress top." if Girl == EmmaX and Girl.Clothes["top"] != "dress_top" and "halloween" in Girl.history:
                $ item = "dress_top"
            "Try on that pink shirt." if Girl == JeanX and Girl.Clothes["top"] != "pink_shirt":
                $ item = "pink_shirt"
            "How about that green shirt?" if Girl == JeanX and Girl.Clothes["top"] != "pink_shirt":
                $ item = "green_shirt"
            "Try on that white shirt." if Girl == StormX and Girl.Clothes["top"] != "white_shirt":
                $ item = "white_shirt"
            "Try on that red shirt." if Girl == JubesX and Girl.Clothes["top"] != "red_shirt":
                $ item = "red_shirt"
            "How about your leather shirt?" if Girl == JubesX and Girl.Clothes["top"] != "black_shirt":
                $ item = "black_shirt"
            "Could you try on that yellow tanktop?" if Girl == JeanX and Girl.Clothes["top"] != "yellow_shirt" and "halloween" in Girl.history:
                $ item = "yellow_shirt"
            "How about that green nighty I got you?" if Girl == RogueX and Girl.Clothes["top"] != "nighty" and "nighty" in Girl.inventory:
                $ item = "nighty"
            "Try on that lace nighty." if Girl in [KittyX, EmmaX] and Girl.Clothes["top"] != "nighty":
                $ item = "nighty"
            "Maybe just throw on a towel?" if Girl != StormX and Girl.Clothes["top"] != "towel":
                $ item = "towel"
            "What about the opaque fetish top?" if Girl == RogueX and Girl.Clothes["top"] != "opaque_fetish_top" and "opaque_fetish_top" in Girl.inventory:
                $ item = "opaque_fetish_top"
            "What about the sheer fetish top?" if Girl == RogueX and Girl.Clothes["top"] != "sheer_fetish_top" and "sheer_fetish_top" in Girl.inventory:
                $ item = "sheer_fetish_top"
            "How about your violet shirt?" if Girl == KittyX and Girl.Clothes["top"] != "violet_shirt" and "violet_shirt" in Girl.inventory:
                $ item = "violet_shirt"
            "You look really sexy in your leather top." if Girl == KittyX and Girl.Clothes["top"] != "leather_top" and "leather_top" in Girl.inventory:
                $ item = "leather_top"
            "Let's see that fishnet top." if Girl == LauraX and Girl.Clothes["top"] != "fishnet_top" and "fishnet_top" in Girl.inventory:
                $ item = "fishnet_top"
            "You know how much I like your school uniform shirt." if Girl == LauraX and Girl.Clothes["top"] != "school_uniform_shirt" and "school_uniform_shirt" in Girl.inventory:
                $ item = "school_uniform_shirt"
            "Try on your Sakura top." if Girl == JeanX and Girl.Clothes["top"] != "Sakura_top" and "Sakura_top" in Girl.inventory:
                $ item = "Sakura_top"
            "Try on your classic jacket?" if Girl == RogueX and Girl.Clothes["jacket"] != "classic_jacket" and "classic_jacket" in Girl.inventory:
                $ item = "classic_jacket"
            "I want to see you in your black jacket." if Girl == EmmaX and Girl.Clothes["jacket"] != "black_jacket" and "black_jacket" in Girl.inventory:
                $ item = "black_jacket"
            "I want to see something else.":
                return

        # if (item == "no_jacket" and not Girl.Clothes["top"]) or item in ["no_top", "mesh_top", "sheer_fetish_top"]:
        #     if (Girl.Clothes["bra"] or Girl.seen_breasts) and approval_check(Girl, 800, taboo_modifier=(3-public)):
        #         if Girl == RogueX:
        #             ch_r "Sure."
        #         elif Girl == KittyX:
        #             ch_k "Why not?"
        #         elif Girl == EmmaX:
        #             ch_e "Certainly."
        #         elif Girl == LauraX:
        #             ch_l "Ok."
        #         elif Girl == JeanX:
        #             ch_j "Ok."
        #         elif Girl == StormX:
        #             ch_s "Fine."
        #         elif Girl == JubesX:
        #             ch_v "Sure."
        #     elif approval_check(Girl, 600, taboo_modifier=0):
        #         if Girl == RogueX:
        #             ch_r "I don't have anything under this. . ."
        #         elif Girl == KittyX:
        #             ch_k "I don't exactly have anything on under this. . ."
        #         elif Girl == EmmaX:
        #             ch_e "I'm not wearing much of anything under this. . ."
        #         elif Girl == LauraX:
        #             ch_l "I don't have anything under this. . ."
        #         elif Girl == JeanX:
        #             ch_j "I'm not wearing a bra right now."
        #         elif Girl == StormX:
        #             ch_s "I don't have much on under this. . ."
        #         elif Girl == JubesX:
        #             ch_v "I don't exactly have anything on under this. . ."
        #
        #         menu:
        #             extend ""
        #             "Then you could slip something on under it. . .":
        #                 if Girl == StormX and (StormX in Rules or Girl.taboo < 20):
        #                     ch_s "No, I suppose it's fine, for now at least."
        #                 elif Girl.seen_breasts and approval_check(Girl, 1000, taboo_modifier= 4 - public) or approval_check(Girl, 1200, taboo_modifier= 5 - public):
        #                     $ Girl.blushing = "_blush2"
        #
        #                     if Girl == RogueX:
        #                         ch_r "'course, I don't exactly need something under it either. . ."
        #                     elif Girl == KittyX:
        #                         ch_k "-not that that's a problem. . ."
        #                     elif Girl == EmmaX:
        #                         ch_e "-not that I'm overly concerned about it. . ."
        #                     elif Girl == LauraX:
        #                         ch_l "-I didn't say that I minded. . ."
        #                     elif Girl == JeanX:
        #                         ch_j "Well, it's not like I needed one. . ."
        #                     elif Girl == StormX:
        #                         ch_s "I truly don't mind though. . ."
        #                     elif Girl == JubesX:
        #                         ch_v "Oh, I was just warning -you-. . ."
        #
        #                     $ Girl.blushing = "_blush1"
        #                 elif approval_check(Girl, 900, taboo_modifier = 3 - public) and "lace_bra" in Girl.inventory:
        #                     if Girl == RogueX:
        #                         ch_r "I suppose this would work. . ."
        #                     elif Girl == KittyX:
        #                         ch_k "I could find {i}something{/i} to wear."
        #                     elif Girl == EmmaX:
        #                         ch_e "I suppose I could."
        #                     elif Girl == JeanX:
        #                         ch_j "I guess I could find something."
        #                     elif Girl == StormX:
        #                         ch_s "Fine."
        #                     elif Girl == JubesX:
        #                         ch_v "Well, I do have something I could throw on. . ."
        #
        #                     call add_bra(Girl, "lace_bra")
        #
        #                     if Girl == KittyX:
        #                         "She pulls out her [Girl.Clothes[bra]] and passes it through her [Girl.Clothes[top].name]."
        #                     else:
        #                         "She pulls out her [Girl.Clothes[bra]] and slips it on under her [Girl.Clothes[top].name]."
        #                 elif Girl in [RogueX, KittyX] and approval_check(Girl, 800, taboo_modifier = 3 - public):
        #                     if Girl == RogueX:
        #                         ch_r "Yeah, I guess."
        #                     elif Girl == KittyX:
        #                         ch_k "Yeah, I guess."
        #
        #                     call add_bra(Girl, "bra")
        #
        #                     if Girl == KittyX:
        #                         "She pulls out her [Girl.Clothes[bra]] and passes it through her [Girl.Clothes[top].name]."
        #                     else:
        #                         "She pulls out her [Girl.Clothes[bra]] and slips it on under her [Girl.Clothes[top].name]."
        #                 elif Girl == RogueX and approval_check(Girl, 600, taboo_modifier = 3 - public):
        #                     ch_r "Yeah, I guess."
        #
        #                     call add_bra(Girl, "tank")
        #
        #                     "She pulls out her [Girl.Clothes[bra]] and slips it on under her [Girl.Clothes[top].name]."
        #                 elif Girl == KittyX and approval_check(Girl, 700, taboo_modifier = 3 - public):
        #                     ch_k "Yeah, I guess."
        #
        #                     call add_bra(Girl, "cami")
        #
        #                     "She pulls out her camisole and passes it through her [Girl.Clothes[top].name]."
        #                 elif Girl in [EmmaX, LauraX] and approval_check(Girl, 700, taboo_modifier=(3-public)):
        #                     if Girl == EmmaX:
        #                         ch_e "I suppose I could."
        #                     elif Girl == LauraX:
        #                         ch_l "I guess I could find something."
        #
        #                     call add_bra(Girl, "corset")
        #
        #                     "She pulls out her corset and slips it on under her [Girl.Clothes[top].name]."
        #                 elif Girl in [EmmaX, JubesX] and approval_check(Girl, 600, taboo_modifier=(3-public)):
        #                     if Girl == EmmaX:
        #                         ch_e "I suppose I could."
        #                     elif Girl == JubesX:
        #                         ch_v "Well, I do have something I could throw on. . ."
        #
        #                     call add_bra(Girl, "sports_bra")
        #
        #                     "She pulls out her sports bra and slips it on under her [Girl.Clothes[top].name]."
        #                 elif Girl == LauraX and approval_check(Girl, 900, taboo_modifier = 3 - public) and "lace_corset" in Girl.inventory:
        #                     ch_l "I guess I could find something."
        #
        #                     call add_bra(Girl, "lace_corset")
        #
        #                     "She pulls out her lace corset and slips it under her [Girl.Clothes[top].name]."
        #                 elif Girl == LauraX and approval_check(Girl, 600, taboo_modifier = 3 - public):
        #                     ch_l "Yeah, I guess."
        #
        #                     call add_bra(Girl, "leather_bra")
        #
        #                     "She pulls out her leather bra and slips it on under her [Girl.Clothes[top].name]."
        #                 elif Girl == JeanX and approval_check(Girl, 700, taboo_modifier = 3 - public):
        #                     ch_j "I guess I could find something."
        #
        #                     call add_bra(Girl, "green_bra")
        #
        #                     "She pulls out her green bra and slips it under her [Girl.Clothes[top].name]."
        #                 elif Girl == StormX and approval_check(Girl, 700, taboo_modifier = 3 - public) and "black_bra" in Girl.inventory:
        #                     ch_s "Fine."
        #
        #                     call add_bra(Girl, "black_bra")
        #
        #                     "She pulls out her black bra and slips it under her [Girl.Clothes[top].name]."
        #                 elif Girl == StormX and approval_check(Girl, 600, taboo_modifier = 3 - public):
        #                     ch_s "Fine."
        #
        #                     call add_bra(Girl, "tube_top")
        #
        #                     "She pulls out her tube top and slips it on under her [Girl.Clothes[top].name]."
        #                 else:
        #                     if Girl == RogueX:
        #                         ch_r "Yeah, I don't think so."
        #                     elif Girl == KittyX:
        #                         ch_k "Yeah, I don't think so."
        #                     elif Girl == EmmaX:
        #                         ch_e "Yes, but I'd rather not."
        #                     elif Girl == LauraX:
        #                         ch_l "Yeah, I don't think so."
        #                     elif Girl == JeanX:
        #                         ch_l "Yeah, I don't think so."
        #                     elif Girl == StormX:
        #                         ch_s "I don't think it would be appropriate."
        #                     elif Girl == JubesX:
        #                         ch_v "Yeah, that wouldn't help."
        #
        #                     $ item = ""
        #             "You could always just wear nothing at all. . .":
        #                 if Girl == StormX and (StormX in Rules or not Girl.taboo):
        #                     ch_s "I suppose it's fine, for now at least."
        #                 elif approval_check(Girl, 1100, "LI", taboo_modifier = 3 - public) and Girl.love > Girl.inhibition:
        #                     if Girl == RogueX:
        #                         ch_r "I suppose I could. . ."
        #                     elif Girl == KittyX:
        #                         ch_k "I guess for you. . ."
        #                     elif Girl == EmmaX:
        #                         ch_e "The things I do for you. . ."
        #                     elif Girl == LauraX:
        #                         ch_l "For you? I guess. . ."
        #                     elif Girl == JeanX:
        #                         ch_j "I guess. . ."
        #                     elif Girl == StormX:
        #                         ch_s "For you? I suppose. . ."
        #                     elif Girl == JubesX:
        #                         ch_v "For you? sure. . ."
        #                 elif approval_check(Girl, 700, "OI", taboo_modifier = 3 - public) and Girl.obedience > Girl.inhibition:
        #                     if Girl == RogueX:
        #                         ch_r "Sure. . ."
        #                     elif Girl == KittyX:
        #                         ch_k "Sure. . ."
        #                     elif Girl == EmmaX:
        #                         ch_e "If that's what you insist. . ."
        #                     elif Girl == LauraX:
        #                         ch_l "Sure. . ."
        #                     elif Girl == JeanX:
        #                         ch_j "Sure. . ."
        #                     elif Girl == StormX:
        #                         ch_s "Fine. . ."
        #                     elif Girl == JubesX:
        #                         ch_v "Sure. . ."
        #                 elif approval_check(Girl, 600, "I", taboo_modifier = 3 - public):
        #                     if Girl == RogueX:
        #                         ch_r "Yeah. . ."
        #                     elif Girl == KittyX:
        #                         ch_k "Yeah. . ."
        #                     elif Girl == EmmaX:
        #                         ch_e "I suppose I could. . ."
        #                     elif Girl == LauraX:
        #                         ch_l "Yeah. . ."
        #                     elif Girl == JeanX:
        #                         ch_j "Yeah. . ."
        #                     elif Girl == StormX:
        #                         ch_s "Yes. . ."
        #                     elif Girl == JubesX:
        #                         ch_v "Yeah. . ."
        #                 elif approval_check(Girl, 1300, taboo_modifier = 3 - public):
        #                     if Girl == RogueX:
        #                         ch_r "Okay, fine."
        #                     elif Girl == KittyX:
        #                         ch_k "Okay, fine."
        #                     elif Girl == EmmaX:
        #                         ch_e "Very well."
        #                     elif Girl == LauraX:
        #                         ch_l "Okay, fine."
        #                     elif Girl == JeanX:
        #                         ch_j "Okay, fine."
        #                     elif Girl == StormX:
        #                         ch_s "Okay, fine."
        #                     elif Girl == JubesX:
        #                         ch_v "Okay, fine."
        #                 else:
        #                     $ Girl.change_face("surprised", brows = "angry")
        #
        #                     if Girl.taboo > 20:
        #                         if Girl == RogueX:
        #                             ch_r "Not in public, [Girl.player_petname]!"
        #                         elif Girl == KittyX:
        #                             ch_k "Not in public, [Girl.player_petname]!"
        #                         elif Girl == EmmaX:
        #                             ch_e "I'm afraid I couldn't do that in public."
        #                         elif Girl == LauraX:
        #                             ch_l "Not in public, I won't!"
        #                         elif Girl == JeanX:
        #                             ch_j ". . . not right now. . ."
        #                         elif Girl == StormX:
        #                             ch_s "Not in public, I'm afraid"
        #                         elif Girl == JubesX:
        #                             ch_v "Not in public, I won't!"
        #                     else:
        #                         if Girl == RogueX:
        #                             ch_r "Don't push it, [Girl.player_petname]."
        #                         elif Girl == KittyX:
        #                             ch_k "I don't like you {i}that{/i} much, [Girl.player_petname]!"
        #                         elif Girl == EmmaX:
        #                             ch_e "I could, but I wouldn't."
        #                         elif Girl == LauraX:
        #                             ch_l "You're not that cute, [Girl.player_petname]!"
        #                         elif Girl == JeanX:
        #                             ch_j "Ha! Not for you, [Girl.player_petname]."
        #                         elif Girl == StormX:
        #                             ch_s "I'm afraid not, [Girl.player_petname]!"
        #                         elif Girl == JubesX:
        #                             ch_v "Nah."
        #
        #                     $ item = ""
        #             "Never mind.":
        #                 Girl.voice "Ok. . ."
        #
        #                 $ item = ""
        #
        #         if item and not approval_check(Girl, 1200):
        #             call ask_for_dress_screen(Girl)
        #
        #             if not _return:
        #                 $ item = ""
        #     else:
        #         call ask_for_dress_screen(Girl)
        #
        #         if not _return:
        #             if item in ["no_top", "no_jacket"]:
        #                 if Girl == RogueX:
        #                     ch_r "I'd rather not. . ."
        #
        #                     if not Girl.Clothes["bra"]:
        #                         ch_r "I'm afraid I don't have anything on under this."
        #                         ch_r "I don't have anything on under this."
        #                 elif Girl == KittyX:
        #                     ch_k "Lol, not around you."
        #
        #                     if not Girl.Clothes["bra"]:
        #                         ch_k "I don't have anything under this. . ."
        #                 elif Girl == EmmaX:
        #                     ch_e "I'm afraid not."
        #
        #                     if not Girl.Clothes["bra"]:
        #                         ch_e "I'm indecent under this. . ."
        #                 elif Girl == LauraX:
        #                     ch_l "Not right now."
        #
        #                     if not Girl.Clothes["bra"]:
        #                         ch_l "I don't have anything under this. . ."
        #                 elif Girl == JeanX:
        #                     ch_j "Not right now."
        #
        #                     if not Girl.Clothes["bra"]:
        #                         ch_j "I'm not wearing a bra right now."
        #                 elif Girl == StormX:
        #                     ch_s "I would rather not."
        #
        #                     if not Girl.Clothes["bra"]:
        #                         ch_s "I don't have anything under this. . ."
        #                 elif Girl == JubesX:
        #                     ch_v "Not right now."
        #
        #                     if not Girl.Clothes["bra"]:
        #                         ch_v "I don't have anything under this. . ."
        #             elif item in ["mesh_top", "sheer_fetish_top"]:
        #                 if Girl == RogueX:
        #                     ch_r "I'm afraid that top is a bit sheer to have nothing under it."
        #
        #             $ item = ""
        # elif item in ["pink_top", "jacket", "dress"]:
        #     $ Girl.change_face("bemused")
        #
        #     if Girl.Clothes["bra"] or Girl.seen_breasts:
        #         if Girl == KittyX:
        #             ch_k "K."
        #         elif Girl == EmmaX:
        #             ch_e "Yeah, ok."
        #         elif Girl == LauraX:
        #             ch_l "Sure."
        #         elif Girl == StormX:
        #             ch_s "Very well."
        #     elif approval_check(Girl, 900, taboo_modifier=0):
        #         if Girl == KittyX:
        #             ch_k "Yeah, ok."
        #         elif Girl == EmmaX:
        #             ch_e "Yeah, ok."
        #         elif Girl == LauraX:
        #             ch_l "Yeah, ok."
        #         elif Girl == StormX:
        #             ch_s "Very well."
        #     else:
        #         call ask_for_dress_screen(Girl)
        #
        #         if not _return:
        #             $ Girl.change_face("bemused", 1)
        #
        #             if Girl == KittyX:
        #                 ch_k "This is a little skimpy for what I have on under it."
        #             elif Girl == EmmaX:
        #                 ch_e "I'm not sure this is appropriate without something more substantial underneath."
        #             elif Girl == LauraX:
        #                 ch_l "I don't really want to take this [Girl.Clothes[top].name] off at the moment."
        #             elif Girl == StormX:
        #                 ch_s "I cannot really take this [Girl.Clothes[jacket].name] off at the moment."
        #
        #             $ item = ""
        # elif item == "nighty":
        #     if not approval_check(Girl, 1100, taboo_modifier=(3-public)):
        #         call ask_for_dress_screen(Girl)
        #
        #         if not _return:
        #             if Girl == RogueX:
        #                 ch_r "That's a bit . . . revealing."
        #             elif Girl == EmmaX:
        #                 ch_e "This is a bit shear."
        #
        #             $ item = ""
        #     else:
        #         if Girl == RogueX:
        #             ch_r "Sure. . ."
        #         elif Girl == EmmaX:
        #             ch_e "Yeah, ok."
        # elif item == "towel":
        #     $ Girl.change_face("bemused", 1)
        #
        #     $ bonus = 5 if Player.location == "bg_shower" else 0
        #
        #     if Girl.Clothes["bra"] or (Girl.seen_breasts and approval_check(Girl, 500, taboo_modifier=(3-public-bonus))):
        #         if Girl == RogueX:
        #             ch_r "Fresh."
        #         elif Girl == KittyX:
        #             ch_k "Weirdo."
        #         elif Girl == EmmaX:
        #             ch_e "Oh, you like this?"
        #         elif Girl == LauraX:
        #             ch_l "Weird."
        #         elif Girl == JeanX:
        #             ch_j "Um, ok. . ."
        #         elif Girl == StormX:
        #             ch_s "If that's what you want. . ."
        #         elif Girl == JubesX:
        #             ch_v "Odd."
        #     elif approval_check(Girl, 1000, taboo_modifier=(3-public-bonus)):
        #         $ Girl.change_face("perplexed", 1)
        #
        #         if Girl == RogueX:
        #             ch_r "I suppose? . ."
        #         elif Girl == KittyX:
        #             ch_k "I guess? . ."
        #         elif Girl == EmmaX:
        #             ch_e "Fine."
        #         elif Girl == LauraX:
        #             ch_l "Huh, ok . ."
        #         elif Girl == JeanX:
        #             ch_j "Huh, ok . ."
        #         elif Girl == StormX:
        #             ch_s "If that's what you want. . ."
        #         elif Girl == JubesX:
        #             ch_v "Huh, sure . ."
        #     else:
        #         call ask_for_dress_screen(Girl)
        #
        #         if not _return:
        #             if Girl == RogueX:
        #                 ch_r "That doesn't leave much to the imagination. . ."
        #             elif Girl == KittyX:
        #                 ch_k "I don't think so with what I have on under it."
        #             elif Girl == EmmaX:
        #                 ch_e "This wouldn't leave much to the imagination."
        #             elif Girl == LauraX:
        #                 ch_l "That wouldn't look right."
        #             elif Girl == JeanX:
        #                 ch_j "That wouldn't look right."
        #             elif Girl == StormX:
        #                 ch_s "I'm afraid I couldn't."
        #             elif Girl == JubesX:
        #                 ch_v "Nah."
        #
        #             $ item = ""

        if item == "no_jacket":
            call change_jacket(Girl, "")
        elif item == "no_top":
            call change_top(Girl, "")
        elif item in jackets:
            call change_jacket(Girl, item)
        elif item in tops:
            call change_top(Girl, item)

        # if item in ["nighty", "towel"] and (Girl.Clothes["jacket"] or Girl.Clothes["dress"] or Girl.Clothes["bodysuit"] or Girl.Clothes["bra"] or Girl.Clothes["underwear"]):
        #     menu:
        #         extend ""
        #         "Nice.":
        #             pass
        #         "I meant {i}just{/i} the [item].":
        #             if approval_check(Girl, 1400, taboo_modifier = 3):
        #                 if Girl == RogueX:
        #                     ch_r "Hmmm, alright. . ."
        #                 elif Girl == KittyX:
        #                     ch_r "Hmmm, alright. . ."
        #                 elif Girl == EmmaX:
        #                     ch_r "Hmmm, alright. . ."
        #                 elif Girl == LauraX:
        #                     ch_r "Hmmm, alright. . ."
        #                 elif Girl == JeanX:
        #                     ch_r "Hmmm, alright. . ."
        #                 elif Girl == StormX:
        #                     ch_r "Hmmm, alright. . ."
        #                 elif Girl == JubesX:
        #                     ch_r "Hmmm, alright. . ."
        #
        #                 call fully_undress(Girl)
        #                 call change_top(Girl, item)
        #             elif approval_check(Girl, 1200, taboo_modifier = 3):
        #                 call remove_bra(Girl)
        #
        #                 if Girl == RogueX:
        #                     ch_r "I'll keep my panties on, thanks."
        #                 elif Girl == KittyX:
        #                     ch_r "I'll keep my panties on, thanks."
        #                 elif Girl == EmmaX:
        #                     ch_r "I'll keep my panties on, thanks."
        #                 elif Girl == LauraX:
        #                     ch_r "I'll keep my panties on, thanks."
        #                 elif Girl == JeanX:
        #                     ch_r "I'll keep my panties on, thanks."
        #                 elif Girl == StormX:
        #                     ch_r "I'll keep my panties on, thanks."
        #                 elif Girl == JubesX:
        #                     ch_r "I'll keep my panties on, thanks."
        #
        #                 call change_top(Girl, item, redress = False)
        #             else:
        #                 if Girl == RogueX:
        #                     ch_r "Be happy with what you get."
        #                 elif Girl == KittyX:
        #                     ch_r "Be happy with what you get."
        #                 elif Girl == EmmaX:
        #                     ch_r "Be happy with what you get."
        #                 elif Girl == LauraX:
        #                     ch_r "Be happy with what you get."
        #                 elif Girl == JeanX:
        #                     ch_r "Be happy with what you get."
        #                 elif Girl == StormX:
        #                     ch_r "Be happy with what you get."
        #                 elif Girl == JubesX:
        #                     ch_r "Be happy with what you get."

label bottoms_menu(Girl):
    while True:
        $ Girl.change_face("sexy", 1)

        menu:
            "Maybe go without the [Girl.Clothes[bottom].name]." if Girl.Clothes["bottom"]:
                $ item = "no_bottom"
            "Take off the [Girl.Clothes[boots].name]?" if Girl.Clothes["boots"]:
                $ item = "no_boots"
            "Your ass looks tight in those jeans." if Girl == RogueX and Girl.Clothes["bottom"] != "jeans":
                $ item = "jeans"
            "You look great in those capris." if Girl == KittyX and Girl.Clothes["bottom"] != "capris":
                $ item = "capris"
            "I really like those black jeans." if Girl in [KittyX, StormX] and Girl.Clothes["bottom"] != "black_jeans":
                $ item = "black_jeans"
            "How about your yoga pants?" if Girl in [KittyX, EmmaX, JeanX, StormX] and Girl.Clothes["bottom"] != "yoga_pants":
                $ item = "yoga_pants"
            "Try on that pink dress skirt you have." if Girl == KittyX and Girl.Clothes["bottom"] != "dress_skirt" and "halloween" in Girl.history:
                $ item = "dress_skirt"
            "You look great in those white pants." if Girl == EmmaX and Girl.Clothes["bottom"] != "white_pants":
                $ item = "white_pants"
            "Could I see you in your leather pants?" if Girl in [LauraX, JubesX] and Girl.Clothes["bottom"] != "leather_pants":
                $ item = "leather_pants"
            "How about your mesh pants?" if Girl == LauraX and Girl.Clothes["bottom"] != "mesh_pants" and "mesh_pants" in Girl.inventory:
                $ item = "mesh_pants"
            "You look great in those khaki pants." if Girl == JeanX and Girl.Clothes["bottom"] != "khaki_pants":
                $ item = "khaki_pants"
            "Try on that white dress skirt you have." if Girl == EmmaX and Girl.Clothes["bottom"] != "dress_skirt" and "halloween" in Girl.history:
                $ item = "dress_skirt"
            "How about that skirt?" if Girl == RogueX and Girl.Clothes["bottom"] != "skirt":
                $ item = "skirt"
            "I really like your belty skirt." if Girl == LauraX and Girl.Clothes["bottom"] != "skirt":
                $ item = "skirt"
            "You could wear your leather skirt." if Girl == LauraX and Girl.Clothes["bottom"] != "cosplay_skirt"and "halloween" in Girl.history:
                $ item = "cosplay_skirt"
            "What about wearing your green skirt?" if Girl == JeanX and Girl.Clothes["bottom"] != "skirt":
                $ item = "skirt"
            "What about wearing your purple skirt?" if Girl == StormX and Girl.Clothes["bottom"] != "skirt":
                $ item = "skirt"
            "I like you in that little skirt." if Girl == EmmaX and Girl.Clothes["bottom"] != "skirt":
                $ item = "skirt"
            "How about the blue skirt?" if Girl == KittyX and Girl.Clothes["bottom"] != "blue_skirt" and "blue_skirt" in Girl.inventory:
                $ item = "blue_skirt"
            "What about wearing your yellow shorts?" if Girl == KittyX and Girl.Clothes["bottom"] != "shorts":
                $ item = "shorts"
            "Could you wear those shorts?" if Girl == JeanX and Girl.Clothes["bottom"] != "shorts" and "halloween" in Girl.history:
                $ item = "shorts"
            "Could you wear those jean shorts?" if Girl == JubesX and Girl.Clothes["bottom"] != "shorts":
                $ item = "shorts"
            "Try on your boots for me." if Girl == EmmaX and Girl.Clothes["boots"] != "thigh_boots":
                $ item = "thigh_boots"
            "Could you wear your ring anklets for me?" if Girl == StormX and Girl.Clothes["boots"] != "ring_anklets" and "halloween" in Girl.history:
                $ item = "ring_anklets"
            "What about those opaque fetish pants?" if Girl == RogueX and Girl.Clothes["bottom"] != "opaque_fetish_pants" and "opaque_fetish_pants" in Girl.inventory:
                $ item = "opaque_fetish_pants"
            "What about those sheer fetish pants?" if Girl == RogueX and Girl.Clothes["bottom"] != "sheer_fetish_pants" and "sheer_fetish_pants" in Girl.inventory:
                $ item = "sheer_fetish_pants"
            "I want to see your jean shorts." if Girl in [RogueX, LauraX] and Girl.Clothes["bottom"] != "jean_shorts" and "jean_shorts" in Girl.inventory:
                $ item = "jean_shorts"
            "Try on your plaid skirt for me." if Girl == RogueX and Girl.Clothes["bottom"] != "plaid_skirt" and "plaid_skirt" in Girl.inventory:
                $ item = "plaid_skirt"
            "You could always wear your black and blue pants." if Girl == KittyX and Girl.Clothes["bottom"] != "black_and_blue_pants" and "black_and_blue_pants" in Girl.inventory:
                $ item = "black_and_blue_pants"
            "Maybe try on your black shorts." if Girl in [KittyX, EmmaX, StormX] and Girl.Clothes["bottom"] != "black_shorts" and "black_shorts" in Girl.inventory:
                $ item = "black_shorts"
            "What about your pink shorts?" if Girl == KittyX and Girl.Clothes["bottom"] != "pink_shorts" and "pink_shorts" in Girl.inventory:
                $ item = "pink_shorts"
            "I like your star skirt." if Girl == KittyX and Girl.Clothes["bottom"] != "star_skirt" and "star_skirt" in Girl.inventory:
                $ item = "star_skirt"
            "I like your black yoga pants." if Girl == EmmaX and Girl.Clothes["bottom"] != "black_yoga_pants" and "black_yoga_pants" in Girl.inventory:
                $ item = "black_yoga_pants"
            "What about your leather pants?" if Girl == EmmaX and Girl.Clothes["bottom"] != "leather_pants" and "leather_pants" in Girl.inventory:
                $ item = "leather_pants"
            "You look so tight in those sports shorts." if Girl == EmmaX and Girl.Clothes["bottom"] != "sports_shorts" and "sports_shorts" in Girl.inventory:
                $ item = "sports_shorts"
            "I'd like to see your white shorts." if Girl == EmmaX and Girl.Clothes["bottom"] != "white_shorts" and "white_shorts" in Girl.inventory:
                $ item = "white_shorts"
            "What about your school uniform skirt?" if Girl == LauraX and Girl.Clothes["bottom"] != "school_uniform_skirt" and "school_uniform_skirt" in Girl.inventory:
                $ item = "school_uniform_skirt"
            "Can you wear your yoga pants?" if Girl == LauraX and Girl.Clothes["bottom"] != "yoga_pants" and "yoga_pants" in Girl.inventory:
                $ item = "yoga_pants"
            "Can you wear your Sakura skirt?" if Girl == JeanX and Girl.Clothes["bottom"] != "Sakura_skirt" and "Sakura_skirt" in Girl.inventory:
                $ item = "Sakura_skirt"
            "Throw on your purple skirt." if Girl == JeanX and Girl.Clothes["bottom"] != "purple_skirt" and "purple_skirt" in Girl.inventory:
                $ item = "purple_skirt"
            "What about your leather boots?." if Girl == EmmaX and Girl.Clothes["boots"] != "domme_boots" and "domme_boots" in Girl.inventory:
                $ item = "domme_boots"
            "I want to see something else.":
                return

#         if item == "no_bottom":
#             if Girl.seen_underwear and Girl.Clothes["underwear"] and approval_check(Girl, 500, taboo_modifier=5):
#                 if Girl == RogueX:
#                     ch_r "Sure."
#                 elif Girl == KittyX:
#                 elif Girl == EmmaX:
#                 elif Girl == LauraX:
#                 elif Girl == JeanX:
#                 elif Girl == StormX:
#                 elif Girl == JubesX:
#
#             elif Girl.seen_pussy and approval_check(Girl, 900, taboo_modifier=4):
#                 if Girl == RogueX:
#                     ch_r "Sure, why not?"
#                 elif Girl == KittyX:
#                 elif Girl == EmmaX:
#                 elif Girl == LauraX:
#                 elif Girl == JeanX:
#                 elif Girl == StormX:
#                 elif Girl == JubesX:
#
#             elif approval_check(Girl, 1300, taboo_modifier=2) and Girl.Clothes["underwear"]:
#                 if Girl == RogueX:
#                     ch_r "Well, I suppose if it's for you. . ."
#                 elif Girl == KittyX:
#                 elif Girl == EmmaX:
#                 elif Girl == LauraX:
#                 elif Girl == JeanX:
#                 elif Girl == StormX:
#                 elif Girl == JubesX:
#
#             elif approval_check(Girl, 700) and not Girl.Clothes["underwear"]:
#                 if Girl == RogueX:
#                     ch_r "I'm not wearing anything under these, you know. . ."
#                 elif Girl == KittyX:
#                 elif Girl == EmmaX:
#                 elif Girl == LauraX:
#                 elif Girl == JeanX:
#                 elif Girl == StormX:
#                 elif Girl == JubesX:
#
#
#                 menu:
#                     extend ""
#                     "Then you could slip on a pair of panties. . .":
#                         if (Girl.seen_pussy and approval_check(Girl, 1100, taboo_modifier=4)) or approval_check(Girl, 1500, taboo_modifier=4):
#                             $ Girl.blushing = "_blush1"
#
#                             if Girl == RogueX:
#                                 ch_r "Alright, I guess it's fine."
#                             elif Girl == KittyX:
#                             elif Girl == EmmaX:
#                             elif Girl == LauraX:
#                             elif Girl == JeanX:
#                             elif Girl == StormX:
#                             elif Girl == JubesX:
#
#
#                             $ Girl.blushing = ""
#                         elif approval_check(Girl, 700, taboo_modifier=4):
#                             if Girl == RogueX:
#                                 ch_r "I like how you think."
#                             elif Girl == KittyX:
#                             elif Girl == EmmaX:
#                             elif Girl == LauraX:
#                             elif Girl == JeanX:
#                             elif Girl == StormX:
#                             elif Girl == JubesX:
#
#
#                             if "lace_panties" in Girl.inventory:
#                                 $ item = "lace_panties"
#                             else:
#                                 $ item = "black_panties"
#
#                             if approval_check(Girl, 1200, taboo_modifier=4) and Girl.Clothes["bottom"]:
#                                 $ line = Girl.Clothes["bottom"]
#
#                                 call change_underwear(Girl, item, redress = False)
#
#                                 "She pulls off her [line] and slips on the [item]."
#                             elif Girl.Clothes["bottom"] in skirts:
#                                 call add_underwear(Girl, item)
#
#                                 "She pulls out her [item] and pulls them up under her skirt."
#                                 "Then she drops the skirt to the floor."
#
#                                 call remove_bottom(Girl)
#                             else:
#                                 show black_screen onlayer black
#
#                                 $ Girl.Outfit.remove_Clothing(["pants", "skirt"])
#
#                                 hide black_screen onlayer black
#
#                                 "She steps away a moment and then comes back wearing only the [item]."
#
#                             $ item = ""
#                         else:
#                             ch_r "Nope."
#
#                             $ item = ""
#                     "You could always just wear nothing at all. . .":
#                         if approval_check(Girl, 1100, "LI", taboo_modifier = 3) and Girl.love > Girl.inhibition:
#                             if Girl == RogueX:
#                                 ch_r "Well aren't you cheeky. . . I suppose I could give you a show. . ."
#                             elif Girl == KittyX:
#                             elif Girl == EmmaX:
#                             elif Girl == LauraX:
#                             elif Girl == JeanX:
#                             elif Girl == StormX:
#                             elif Girl == JubesX:
#
#                         elif approval_check(Girl, 750, "OI", taboo_modifier = 3) and Girl.obedience > Girl.inhibition:
#                             if Girl == RogueX:
#                                 ch_r "If that's what you want."
#                             elif Girl == KittyX:
#                             elif Girl == EmmaX:
#                             elif Girl == LauraX:
#                             elif Girl == JeanX:
#                             elif Girl == StormX:
#                             elif Girl == JubesX:
#
#                         elif approval_check(Girl, 500, "I", taboo_modifier = 3):
#                             if Girl == RogueX:
#                                 ch_r "Oooh, naughty."
#                             elif Girl == KittyX:
#                             elif Girl == EmmaX:
#                             elif Girl == LauraX:
#                             elif Girl == JeanX:
#                             elif Girl == StormX:
#                             elif Girl == JubesX:
#
#                         elif approval_check(Girl, 1400, taboo_modifier = 3):
#                             if Girl == RogueX:
#                                 ch_r "Oh, fine. You've been a good boy."
#                             elif Girl == KittyX:
#                             elif Girl == EmmaX:
#                             elif Girl == LauraX:
#                             elif Girl == JeanX:
#                             elif Girl == StormX:
#                             elif Girl == JubesX:
#
#                         else:
#                             $ Girl.change_face("surprised", brows = "angry")
#
#                             if Girl.taboo:
#                                 if Girl == RogueX:
#                                     ch_r "Not here,[Girl.player_petname]!"
#                                 elif Girl == KittyX:
#                                 elif Girl == EmmaX:
#                                 elif Girl == LauraX:
#                                 elif Girl == JeanX:
#                                 elif Girl == StormX:
#                                 elif Girl == JubesX:
#
#                             else:
#                                 if Girl == RogueX:
#                                     ch_r "Not with you around,[Girl.player_petname]!"
#                                 elif Girl == KittyX:
#                                 elif Girl == EmmaX:
#                                 elif Girl == LauraX:
#                                 elif Girl == JeanX:
#                                 elif Girl == StormX:
#                                 elif Girl == JubesX:
#
#
#                             $ item = ""
#                     "Never mind.":
#                         if Girl == RogueX:
#                             ch_r "Ok. . ."
#                         elif Girl == KittyX:
#                         elif Girl == EmmaX:
#                         elif Girl == LauraX:
#                         elif Girl == JeanX:
#                         elif Girl == StormX:
#                         elif Girl == JubesX:
#
#
#                         $ item = ""
#
#                 if item and not Girl.Clothes["underwear"] and not approval_check(Girl, 1500):
#                     call ask_for_dress_screen(Girl)
#
#                     if not _return:
#                         $ item = ""
#             else:
#                 call ask_for_dress_screen(Girl)
#
#                 if not _return:
#                     if Girl == RogueX:
#                         ch_r "Not in front of you, [Girl.player_petname]."
#
#                         if not Girl.Clothes["underwear"]:
#                             ch_r "Maybe if I put some panties on first. . ."
#                     elif Girl == KittyX:
#                     elif Girl == EmmaX:
#                     elif Girl == LauraX:
#                     elif Girl == JeanX:
#                     elif Girl == StormX:
#                     elif Girl == JubesX:
#
#
#                     $ item = ""

        if item == "no_bottom":
            call change_bottom(Girl, "")
        elif item == "no_boots":
            $ Girl.take_off("boots")
        elif item == "no_socks":
            call change_hose(Girl, "")
        elif item in pants or item in skirts or item in shorts:
            call change_bottom(Girl, item)
        elif item in socks:
            call change_socks(Girl, item)
        elif item in boots:
            $ Girl.Clothes["boots"] = item

label lingerie_menu(Girl):
    while True:
        menu:
            "Let me see your bras.":
                call bras_menu(Girl)
            "What about your underwear?":
                call underwears_menu(Girl)
            "Try on some hosiery for me.":
                call hoses_menu(Girl)
            "I want to see something else.":
                return

label bras_menu(Girl):
    while True:
        $ Girl.change_face("bemused", 1)

        menu:
            "How about you lose the [Girl.Clothes[bra].name]?" if Girl.Clothes["bra"]:
                $ item = "no_bra"
            "What about your pink dress corset?" if Girl == KittyX and Girl.Clothes["bra"] != "dress_corset" and "halloween" in Girl.history:
                $ item = "dress_corset"
            "Try on that black tank top." if Girl == RogueX and Girl.Clothes["bra"] != "tank":
                $ item = "tank"
            "I like that buttoned tank top." if Girl == RogueX and Girl.Clothes["bra"] != "buttoned_tank":
                $ item = "buttoned_tank"
            "I liked that white tank top." if Girl == LauraX and Girl.Clothes["bra"] != "white_tank" and "halloween" in Girl.history:
                $ item = "white_tank"
            "Could you try on your wolverine tanktop?" if Girl == LauraX and Girl.Clothes["bra"] != "wolvie_bra" and "wolvie_bra" in Girl.inventory:
                $ item = "wolvie_bra"
            "I like that blue tube top." if Girl == RogueX and Girl.Clothes["bra"] != "tube_top" and "halloween" in Girl.history:
                $ item = "tube_top"
            "Try on your tube top." if Girl == StormX and Girl.Clothes["bra"] != "tube_top":
                $ item = "tube top"
            "Can you wear on your pink tubetop?" if Girl == JubesX and Girl.Clothes["bra"] != "tube_top":
                $ item = "tube_top"
            "What about your sports bra?" if Girl in [RogueX, KittyX, EmmaX, JeanX, StormX, JubesX] and Girl.Clothes["bra"] != "sports_bra":
                $ item = "sports_bra"
            "Try on that yellow camisole." if Girl == KittyX and Girl.Clothes["bra"] != "cami":
                $ item = "cami"
            "Try on your bikini top?" if Girl.Clothes["bra"] != "bikini_top" and "bikini_top" in Girl.inventory:
                $ item = "bikini_top"
            "I like that top you had on at the party." if Girl == StormX and Girl.Clothes["bra"] != "cosplay_bra" and "halloween" in Girl.history:
                $ item = "cosplay_bra"
            "I like your leather bra." if Girl == LauraX and Girl.Clothes["bra"] != "leather_bra":
                $ item = "leather_bra"
            "I like that corset you have." if Girl == EmmaX and Girl.Clothes["bra"] != "corset":
                $ item = "corset"
            "Try on that corset I got you." if Girl in [LauraX, JeanX] and Girl.Clothes["bra"] != "corset" and "corset" in Girl.inventory:
                $ item = "corset"
            "You look amazing in your lace corset." if Girl in [LauraX, JeanX] and Girl.Clothes["bra"] != "lace_corset" and "lace_corset" in Girl.inventory:
                $ item = "lace_corset"
            "I like your black bra." if Girl in [RogueX, StormX] and Girl.Clothes["bra"] != "black_bra":
                $ item = "black_bra"
            "I like that strapless bra." if Girl == KittyX and Girl.Clothes["bra"] != "strapless_bra":
                $ item = "strapless_bra"
            "Try on that green bra." if Girl == JeanX and Girl.Clothes["bra"] != "green_bra":
                $ item = "green_bra"
            "You look great in your lace bra." if Girl.Clothes["bra"] != "lace_bra" and "lace_bra" in Girl.inventory:
                $ item = "lace_bra"
            "How about your blue corset?" if Girl.Clothes["bra"] != "blue_corset" and "blue_corset" in Girl.inventory:
                $ item = "blue_corset"
            "Try on your harness bra." if Girl == RogueX and Girl.Clothes["bra"] != "harness_bra" and "harness_bra" in Girl.inventory:
                $ item = "harness_bra"
            "Put on your string bikini top." if Girl == RogueX and Girl.Clothes["bra"] != "string_bikini_top" and "string_bikini_top" in Girl.inventory:
                $ item = "string_bikini_top"
            "Try on that kitty bra." if Girl == KittyX and Girl.Clothes["bra"] != "kitty_bra" and "kitty_bra" in Girl.inventory:
                $ item = "kitty_bra"
            "What about your orange top?" if Girl == KittyX and Girl.Clothes["bra"] != "orange_top" and "orange_top" in Girl.inventory:
                $ item = "orange_top"
            "What about your black bra?" if Girl == KittyX and Girl.Clothes["bra"] != "black_strapless_bra" and "black_strapless_bra" in Girl.inventory:
                $ item = "black_strapless_bra"
            "I want to see your bustier." if Girl == KittyX and Girl.Clothes["bra"] != "bustier" and "bustier" in Girl.inventory:
                $ item = "bustier"
            "What about your pink bra?" if Girl == KittyX and Girl.Clothes["bra"] != "pink_strapless_bra" and "pink_strapless_bra" in Girl.inventory:
                $ item = "pink_strapless_bra"
            "Maybe your purple bra?" if Girl == KittyX and Girl.Clothes["bra"] != "purple_strapless_bra" and "purple_strapless_bra" in Girl.inventory:
                $ item = "purple_strapless_bra"
            "Maybe your black bustier?" if Girl == EmmaX and Girl.Clothes["bra"] != "black_bustier" and "black_bustier" in Girl.inventory:
                $ item = "black_bustier"
            "I like your black corset." if Girl == EmmaX and Girl.Clothes["bra"] != "black_corset" and "black_corset" in Girl.inventory:
                $ item = "black_corset"
            "Try on your ino top." if Girl == EmmaX and Girl.Clothes["bra"] != "ino_top" and "ino_top" in Girl.inventory:
                $ item = "ino_top"
            "Your white bustier is really nice." if Girl == EmmaX and Girl.Clothes["bra"] != "white_bustier" and "white_bustier" in Girl.inventory:
                $ item = "white_bustier"
            "Never mind.":
                return

#         if item == "no_bra":
#             if Girl.seen_breasts and approval_check(Girl, 1100, taboo_modifier=2):
#                 if Girl == RogueX:
#                     ch_r "Sure."
#                 elif Girl == KittyX:
#                 elif Girl == EmmaX:
#                 elif Girl == LauraX:
#                 elif Girl == JeanX:
#                 elif Girl == StormX:
#                 elif Girl == JubesX:
#
#             elif approval_check(Girl, 1100, taboo_modifier=2):
#                 if Girl == RogueX:
#                     ch_r "I guess I don't really mind if you see them. . ."
#                 elif Girl == KittyX:
#                 elif Girl == EmmaX:
#                 elif Girl == LauraX:
#                 elif Girl == JeanX:
#                 elif Girl == StormX:
#                 elif Girl == JubesX:
#
#             elif Girl.Clothes["jacket"] == "hoodie" and approval_check(Girl, 500, taboo_modifier=2):
#                 if Girl == RogueX:
#                     ch_r "I guess this covers enough. . ."
#                 elif Girl == KittyX:
#                 elif Girl == EmmaX:
#                 elif Girl == LauraX:
#                 elif Girl == JeanX:
#                 elif Girl == StormX:
#                 elif Girl == JubesX:
#
#             else:
#                 call ask_for_dress_screen(Girl)
#
#                 if not _return:
#                     if Girl.Clothes["top"] == "pink_top" and approval_check(Girl, 950, taboo_modifier=2):
#                         if Girl == RogueX:
#                             ch_r "This look is a bit revealing. . ."
#                     elif Girl.Clothes["top"] == "mesh_top":
#                         if Girl == RogueX:
#                             ch_r "In this top? That would leave nothing to the imagination!"
#                     elif not Girl.Clothes["top"]:
#                         if Girl == RogueX:
#                             ch_r "Not without a little coverage, for modesty."
#                         elif Girl == KittyX:
#                         elif Girl == EmmaX:
#                         elif Girl == LauraX:
#                         elif Girl == JeanX:
#                         elif Girl == StormX:
#                         elif Girl == JubesX:
#
#                     else:
#                         if Girl == RogueX:
#                             ch_r "I don't think so, [Girl.player_petname]."
#                         elif Girl == KittyX:
#                         elif Girl == EmmaX:
#                         elif Girl == LauraX:
#                         elif Girl == JeanX:
#                         elif Girl == StormX:
#                         elif Girl == JubesX:
#
#
#                     $ item = ""
#         elif item == "bikini_top":
#             if Player.location == "bg_pool":
#                 if Girl == RogueX:
#                     ch_r "Sure."
#                 elif Girl == KittyX:
#                 elif Girl == EmmaX:
#                 elif Girl == LauraX:
#                 elif Girl == JeanX:
#                 elif Girl == StormX:
#                 elif Girl == JubesX:
#
#             else:
#                 if Girl.seen_breasts or approval_check(Girl, 1000, taboo_modifier=2):
#                     if Girl == RogueX:
#                         ch_r "Sure."
#                     elif Girl == KittyX:
#                     elif Girl == EmmaX:
#                     elif Girl == LauraX:
#                     elif Girl == JeanX:
#                     elif Girl == StormX:
#                     elif Girl == JubesX:
#
#                 else:
#                     call ask_for_dress_screen(Girl)
#
#                     if not _return:
#                         if Girl == RogueX:
#                             ch_r "I kinda don't feel right about that. . ."
#                         elif Girl == KittyX:
#                         elif Girl == EmmaX:
#                         elif Girl == LauraX:
#                         elif Girl == JeanX:
#                         elif Girl == StormX:
#                         elif Girl == JubesX:
#
#
#                         $ item = ""
#         elif item in ["bra", "lace_bra", "harness_bra"]:
#             if (Girl.seen_breasts and approval) or approval_check(Girl, 1100, taboo_modifier=2):
#                 if Girl == RogueX:
#                     ch_r "Sure."
#                 elif Girl == KittyX:
#                 elif Girl == EmmaX:
#                 elif Girl == LauraX:
#                 elif Girl == JeanX:
#                 elif Girl == StormX:
#                 elif Girl == JubesX:
#
#             else:
#                 call ask_for_dress_screen(Girl)
#
#                 if not _return:
#                     if Girl == RogueX:
#                         ch_r "That's a bit too revealing. . ."
#                     elif Girl == KittyX:
#                     elif Girl == EmmaX:
#                     elif Girl == LauraX:
#                     elif Girl == JeanX:
#                     elif Girl == StormX:
#                     elif Girl == JubesX:
#
#
#                     $ item = ""
#

        if item == "no_bra":
            $ line = Girl.Clothes["bra"]

            if Girl.Clothes["top"] or Girl.Clothes["jacket"] or Girl.Clothes["dress"] or Girl.Clothes["bodysuit"]:
                $ Girl.take_off("bra")

                if Girl.Clothes["dress"]:
                    "She reaches into her [Girl.Clothes[dress].name] grabs her [line], and pulls it out, dropping it to the ground."
                elif Girl.Clothes["bodysuit"]:
                    "She reaches into her [Girl.Clothes[dress].name] grabs her [line], and pulls it out, dropping it to the ground."
                elif Girl.Clothes["top"]:
                    "She reaches into her [Girl.Clothes[top].name] grabs her [line], and pulls it out, dropping it to the ground."
                elif Girl.Clothes["jacket"]:
                    "She reaches into her [Girl.Clothes[jacket].name] grabs her [line], and pulls it out, dropping it to the ground."

                if not renpy.showing('dress_screen'):
                    call expression Girl.tag + "_First_Topless"
            else:
                call change_bra(Girl, "", redress = False)

                "She lets her [line] fall to the ground."
        elif item in bras:
            call change_bra(Girl, item)

label underwears_menu(Girl):
    while True:
        $ Girl.change_face("bemused", 1)

        menu:
            "You could lose those [Girl.Clothes[underwear].name]. . ." if Girl.Clothes["underwear"]:
                $ item = "no_underwear"
            "What about wearing your shorts?" if Girl == RogueX and Girl.Clothes["underwear"] != "shorts":
                $ item = "shorts"
            "I like those bikini bottoms." if Girl.Clothes["underwear"] != "bikini_bottoms" and "bikini_bottoms" in Girl.inventory:
                $ item = "bikini_bottoms"
            "Can you try on those panties from the Halloween party?" if Girl == StormX and Girl.Clothes["underwear"] != "cosplay_panties" and "halloween" in Girl.history:
                $ item = "cosplay_panties"
            "How about your sporty panties?" if Girl == EmmaX and Girl.Clothes["underwear"] != "sports_panties":
                $ item = "sports_panties"
            "Why don't you wear the green panties?" if Girl in [RogueX, KittyX, JeanX] and Girl.Clothes["underwear"] != "green_panties":
                $ item = "green_panties"
            "How about the black panties?" if Girl in [RogueX, StormX] and Girl.Clothes["underwear"] != "black_panties":
                $ item = "black_panties"
            "Try on the lace panties." if Girl.Clothes["underwear"] != "lace_panties" and "lace_panties" in Girl.inventory:
                $ item = "lace_panties"
            "Why don't you wear the white panties?" if Girl in [EmmaX, StormX] and Girl.Clothes["underwear"] != "white_panties":
                $ item = "white_panties"
            "What about your leather panties?" if Girl == LauraX and Girl.Clothes["underwear"] != "leather_panties":
                $ item = "leather_panties"
            "Could you try on your wolverine panties?" if Girl == LauraX and Girl.Clothes["underwear"] != "wolvie_panties" and "wolvie_panties" in Girl.inventory:
                $ item = "wolvie_panties"
            "Why don't you wear your blue panties?" if Girl == JubesX and Girl.Clothes["underwear"] != "blue_panties":
                $ item = "blue_panties"
            "Your tiger-striped panties are hot." if Girl == JubesX and Girl.Clothes["underwear"] != "tiger_panties" and "tiger_panties" in Girl.inventory:
                $ item = "tiger_panties"
            "What about those harness panties I bought you?" if Girl in [RogueX, LauraX] and Girl.Clothes["underwear"] != "harness_panties" and "harness_panties" in Girl.inventory:
                $ item = "harness_panties"
            "Try on your seethrough panties." if Girl in [RogueX, JeanX] and Girl.Clothes["underwear"] != "seethrough_panties" and "seethrough_panties" in Girl.inventory:
                $ item = "seethrough_panties"
            "I like your spider-web panties." if Girl in [RogueX, LauraX, JeanX] and Girl.Clothes["underwear"] != "spider_web_panties" and "spider_web_panties" in Girl.inventory:
                $ item = "spider_web_panties"
            "Maybe your string bikini bottoms." if Girl in [RogueX, LauraX] and Girl.Clothes["underwear"] != "string_bikini_bottoms" and "string_bikini_bottoms" in Girl.inventory:
                $ item = "string_bikini_bottoms"
            "Maybe your pink micropanties." if Girl == KittyX and Girl.Clothes["underwear"] != "pink_micropanties" and "pink_micropanties" in Girl.inventory:
                $ item = "pink_micropanties"
            "I really like your purple micropanties." if Girl == KittyX and Girl.Clothes["underwear"] != "purple_micropanties" and "purple_micropanties" in Girl.inventory:
                $ item = "purple_micropanties"
            "Nothing sexier than your zipper panties." if Girl == KittyX and Girl.Clothes["underwear"] != "zipper_panties" and "zipper_panties" in Girl.inventory:
                $ item = "zipper_panties"
            "How about those kitty panties I got you?" if Girl == KittyX and Girl.Clothes["underwear"] != "kitty_panties" and "kitty_panties" in Girl.inventory:
                $ item = "kitty_panties"
            "You look nice in those nighty panties." if Girl == KittyX and Girl.Clothes["underwear"] != "nighty_panties" and "nighty_panties" in Girl.inventory:
                $ item = "nighty_panties"
            "I want to see those boy shorts." if Girl == LauraX and Girl.Clothes["underwear"] != "boy_shorts" and "boy_shorts" in Girl.inventory:
                $ item = "boy_shorts"
            "You look really nice in that G-string." if Girl == LauraX and Girl.Clothes["underwear"] != "g_string" and "g_string" in Girl.inventory:
                $ item = "g_string"
            "Nothing sexier than your crotchless panties." if Girl == JeanX and Girl.Clothes["underwear"] != "crotchless_panties" and "crotchless_panties" in Girl.inventory:
                $ item = "crotchless_panties"
            "You look really nice in those black lace panties." if Girl == StormX and Girl.Clothes["underwear"] != "black_lace_panties" and "black_lace_panties" in Girl.inventory:
                $ item = "black_lace_panties"
            "Never mind.":
                return

#         if item == "no_underwear":
#             if (Girl.seen_pussy and approval_check(Girl, 900)) and not Girl.taboo:
#                 if approval_check(Girl, 850, "L", taboo_modifier=2):
#                     if Girl == RogueX:
#                         ch_r "Well aren't you cheeky. . ."
#                     elif Girl == KittyX:
#                     elif Girl == EmmaX:
#                     elif Girl == LauraX:
#                     elif Girl == JeanX:
#                     elif Girl == StormX:
#                     elif Girl == JubesX:
#
#                 elif approval_check(Girl, 500, "O", taboo_modifier=2):
#                     if Girl == RogueX:
#                         ch_r "Fine by me."
#                     elif Girl == KittyX:
#                     elif Girl == EmmaX:
#                     elif Girl == LauraX:
#                     elif Girl == JeanX:
#                     elif Girl == StormX:
#                     elif Girl == JubesX:
#
#                 elif approval_check(Girl, 350, "I", taboo_modifier=2):
#                     if Girl == RogueX:
#                         ch_r "Oooh, naughty."
#                     elif Girl == KittyX:
#                     elif Girl == EmmaX:
#                     elif Girl == LauraX:
#                     elif Girl == JeanX:
#                     elif Girl == StormX:
#                     elif Girl == JubesX:
#
#                 else:
#                     if Girl == RogueX:
#                         ch_r "Oh, I guess I could."
#                     elif Girl == KittyX:
#                     elif Girl == EmmaX:
#                     elif Girl == LauraX:
#                     elif Girl == JeanX:
#                     elif Girl == StormX:
#                     elif Girl == JubesX:
#
#             else:
#                 if approval_check(Girl, 1100, "LI", taboo_modifier=2):
#                     if Girl == RogueX:
#                         ch_r "Well aren't you cheeky. . . I suppose I could give you a show. . ."
#                     elif Girl == KittyX:
#                     elif Girl == EmmaX:
#                     elif Girl == LauraX:
#                     elif Girl == JeanX:
#                     elif Girl == StormX:
#                     elif Girl == JubesX:
#
#                 elif approval_check(Girl, 750, "OI", taboo_modifier=2):
#                     if Girl == RogueX:
#                         ch_r "If that's what you want."
#                     elif Girl == KittyX:
#                     elif Girl == EmmaX:
#                     elif Girl == LauraX:
#                     elif Girl == JeanX:
#                     elif Girl == StormX:
#                     elif Girl == JubesX:
#
#                 elif approval_check(Girl, 500, "I", taboo_modifier=2):
#                     if Girl == RogueX:
#                         ch_r "Oooh, naughty."
#                     elif Girl == KittyX:
#                     elif Girl == EmmaX:
#                     elif Girl == LauraX:
#                     elif Girl == JeanX:
#                     elif Girl == StormX:
#                     elif Girl == JubesX:
#
#                 elif approval_check(Girl, 1400, taboo_modifier = 3):
#                     if Girl == RogueX:
#                         ch_r "Oh, fine. You've been a good boy."
#                     elif Girl == KittyX:
#                     elif Girl == EmmaX:
#                     elif Girl == LauraX:
#                     elif Girl == JeanX:
#                     elif Girl == StormX:
#                     elif Girl == JubesX:
#
#                 else:
#                     call ask_for_dress_screen(Girl)
#
#                     if not _return:
#                         $ Girl.change_face("surprised", brows = "angry")
#
#                         if Girl.taboo > 20:
#                             if Girl == RogueX:
#                                 ch_r "Not in public, [Girl.player_petname]!"
#                             elif Girl == KittyX:
#                             elif Girl == EmmaX:
#                             elif Girl == LauraX:
#                             elif Girl == JeanX:
#                             elif Girl == StormX:
#                             elif Girl == JubesX:
#
#                         else:
#                             if Girl == RogueX:
#                                 ch_r "Not with you around,[Girl.player_petname]!"
#                             elif Girl == KittyX:
#                             elif Girl == EmmaX:
#                             elif Girl == LauraX:
#                             elif Girl == JeanX:
#                             elif Girl == StormX:
#                             elif Girl == JubesX:
#
#
#                         $ item = ""
#         elif item == "bikini_bottoms":
#             if Player.location == "bg_pool":
#                 if Girl == RogueX:
#                     ch_r "Sure."
#                 elif Girl == KittyX:
#                 elif Girl == EmmaX:
#                 elif Girl == LauraX:
#                 elif Girl == JeanX:
#                 elif Girl == StormX:
#                 elif Girl == JubesX:
#
#             else:
#                 if approval_check(Girl, 1000, taboo_modifier=2):
#                     if Girl == RogueX:
#                         ch_r "Sure."
#                     elif Girl == KittyX:
#                     elif Girl == EmmaX:
#                     elif Girl == LauraX:
#                     elif Girl == JeanX:
#                     elif Girl == StormX:
#                     elif Girl == JubesX:
#
#                 else:
#                     call ask_for_dress_screen(Girl)
#
#                     if not _return:
#                         if Girl == RogueX:
#                             ch_r "I kinda don't feel right about that. . ."
#                         elif Girl == KittyX:
#                         elif Girl == EmmaX:
#                         elif Girl == LauraX:
#                         elif Girl == JeanX:
#                         elif Girl == StormX:
#                         elif Girl == JubesX:
#
#
#                         $ item = ""
#         elif item in ["green_panties", "black_panties", "lace_panties", "harness_panties"]:
#             if approval:
#                 if Girl == RogueX:
#                     ch_r "Sure, ok."
#                 elif Girl == KittyX:
#                 elif Girl == EmmaX:
#                 elif Girl == LauraX:
#                 elif Girl == JeanX:
#                 elif Girl == StormX:
#                 elif Girl == JubesX:
#
#             elif Girl.Clothes["underwear"]:
#                 if Girl == RogueX:
#                     ch_r "Heh, no, I think I'll stick with these, thanks."
#                 elif Girl == KittyX:
#                 elif Girl == EmmaX:
#                 elif Girl == LauraX:
#                 elif Girl == JeanX:
#                 elif Girl == StormX:
#                 elif Girl == JubesX:
#
#             else:
#                 call ask_for_dress_screen(Girl)
#
#                 if not _return:
#                     if Girl == RogueX:
#                         ch_r "I think I'll choose my own underwear, thank you."
#                         ch_r "I don't see how that's any business of yours, [Girl.player_petname]."
#                     elif Girl == KittyX:
#                     elif Girl == EmmaX:
#                     elif Girl == LauraX:
#                     elif Girl == JeanX:
#                     elif Girl == StormX:
#                     elif Girl == JubesX:
#
#
#                     $ item = ""

        if item == "no_underwear":
            $ line = Girl.Clothes["underwear"]

            if not Girl.Clothes["bottom"] and not Girl.Clothes["dress"] and not Girl.Clothes["bodysuit"]:
                call change_underwear(Girl, "", redress = False)

                "She pulls off her [line], then drops them to the ground."
            elif approval_check(Girl, 1200, taboo_modifier = 4):
                call change_underwear(Girl, "")

                "She pulls off her [Girl.Clothes[bottom]] and [line], then pulls the [Girl.Clothes[bottom].name] back on."
            elif not Girl.Clothes["bodysuit"] and ((Girl.Clothes["dress"] and not Girl.Clothes["bottom"]) or Girl.Clothes["bottom"] in skirts or Girl.Clothes["bottom"] in dresses):
                call remove_underwear(Girl)

                "She reaches under her skirt and pulls her [line] off."
            else:
                $ Girl.blushing = "_blush1"

                show black_screen onlayer black

                $ Girl.take_off("underwear")

                hide black_screen onlayer black

                "She steps away a moment and then comes back."

                $ Girl.blushing = ""
        elif item in underwears:
            call change_underwear(Girl, item)

label hoses_menu(Girl):
    while True:
        menu:
            "You could lose the [Girl.Clothes[hose].name]." if Girl.Clothes["hose"]:
                $ item = "no_hose"
            "I like you in tights." if Girl == RogueX and Girl.Clothes["hose"] != '_tights':
                $ item = "tights"
            "Your ripped tights are a good look." if Girl == RogueX and Girl.Clothes["hose"] != 'ripped_tights' and "ripped_tights" in Girl.inventory:
                $ item = "ripped_tights"
            "The knee-high hose look good with that." if Girl == KittyX and Girl.Clothes["hose"] != "knee_stockings" and "knee_stockings" in Girl.inventory:
                $ item = "knee_stockings"
            "The tall socks would look good with that." if Girl == JubesX and Girl.Clothes["hose"] != "socks" and "socks" in Girl.inventory:
                $ item = "socks"
            "You look great in pantyhose." if Girl.Clothes["hose"] != "pantyhose":
                $ item = "pantyhose"
            "Your ripped pantyhose would look good with that." if Girl.Clothes["hose"] != "ripped_pantyhose" and "ripped_pantyhose" in Girl.inventory:
                $ item = "ripped_pantyhose"
            "I like your thigh-high stockings." if Girl.Clothes["hose"] != "stockings":
                $ item = "stockings"
            "What about your black stockings?" if Girl == LauraX and Girl.Clothes["hose"] != "black_stockings" and "black_stockings" in Girl.inventory:
                $ item = "black_stockings"
            "The stockings and garterbelt would look good with that." if Girl.Clothes["hose"] != "stockings_and_garterbelt" and "stockings_and_garterbelt" in Girl.inventory:
                $ item = "stockings_and_garterbelt"
            "Maybe just the garterbelt?" if Girl.Clothes["hose"] != "garterbelt" and "stockings_and_garterbelt" in Girl.inventory:
                $ item = "garterbelt"
            "Try on your knee socks." if Girl == KittyX and Girl.Clothes["hose"] != "knee_socks" and "knee_socks" in Girl.inventory:
                $ item = "knee_socks"
            "Your fishnet stockings are so hot." if Girl in [KittyX, LauraX] and Girl.Clothes["hose"] != "fishnet_stockings" and "fishnet_stockings" in Girl.inventory:
                $ item = "fishnet_stockings"
            "Maybe the fishnet pantyhose." if Girl == LauraX and Girl.Clothes["hose"] != "fishnet_pantyhose" and "fishnet_pantyhose" in Girl.inventory:
                $ item = "fishnet_pantyhose"
            "Try the ripped fishnet pantyhose." if Girl == LauraX and Girl.Clothes["hose"] != "ripped_fishnet_pantyhose" and "ripped_fishnet_pantyhose" in Girl.inventory:
                $ item = "ripped_fishnet_pantyhose"
            "Never mind.":
                return

        if item == "no_hose":
            if Girl.Clothes["hose"] in hoses:
                call change_hose(Girl, "")
            elif Girl.Clothes["hose"] in socks:
                call change_socks(Girl, "")
        elif item in hoses:
            call change_hose(Girl, item)
        elif item in socks:
            call change_socks(Girl, item)

label special_menu(Girl):
    while True:
        menu:
            "Can you take off the [Girl.Clothes[cloak].name]?" if Girl.Clothes["cloak"]:
                $ item = "no_cloak"
            "Maybe take off the [Girl.Clothes[dress].name]." if Girl.Clothes["dress"]:
                $ item = "no_dress"
            "Try without the [Girl.Clothes[bodysuit].name]." if Girl.Clothes["bodysuit"]:
                $ item = "no_bodysuit"
            "How about the Raven cloak?" if Girl == RogueX and Girl.Clothes["cloak"] != "Raven_cloak" and "Raven_cloak" in Girl.inventory:
                $ item = "Raven_cloak"
            "What about your black cape?" if Girl == EmmaX and Girl.Clothes["cloak"] != "black_cape" and "black_cape" in Girl.inventory:
                $ item = "black_cape"
            "Hmm, try on your white cape." if Girl == EmmaX and Girl.Clothes["cloak"] != "white_cape" and "white_cape" in Girl.inventory:
                $ item = "white_cape"
            "What about your blue dress?" if Girl == RogueX and Girl.Clothes["dress"] != "blue_dress" and "blue_dress" in Girl.inventory:
                $ item = "blue_dress"
            "I like your red dress." if Girl == RogueX and Girl.Clothes["dress"] != "red_dress" and "red_dress" in Girl.inventory:
                $ item = "red_dress"
            "Try on that qipao." if Girl in [KittyX, LauraX] and Girl.Clothes["dress"] != "qipao" and "qipao" in Girl.inventory:
                $ item = "qipao"
            "You know I love your Raven suit." if Girl == RogueX and Girl.Clothes["bodysuit"] != "Raven_suit" and "Raven_suit" in Girl.inventory:
                $ item = "Raven_suit"
            "What about the latex suit?" if Girl == RogueX and Girl.Clothes["bodysuit"] != "latex_suit" and "latex_suit" in Girl.inventory:
                $ item = "latex_suit"
            "Try on your one-piece swimsuit." if Girl == RogueX and Girl.Clothes["bodysuit"] != "swimsuit" and "swimsuit" in Girl.inventory:
                $ item = "swimsuit"
            "What about your sexy one-piece swimsuit?" if Girl == RogueX and Girl.Clothes["bodysuit"] != "sexy_swimsuit" and "sexy_swimsuit" in Girl.inventory:
                $ item = "sexy_swimsuit"
            "You could wear your classic catsuit." if Girl == RogueX and Girl.Clothes["bodysuit"] != "catsuit" and "catsuit" in Girl.inventory:
                $ item = "catsuit"
            "Could you put on your black swimsuit?" if Girl == KittyX and Girl.Clothes["bodysuit"] != "black_swimsuit" and "black_swimsuit" in Girl.inventory:
                $ item = "black_swimsuit"
            "Try on the Taimanin leotard." if Girl == KittyX and Girl.Clothes["bodysuit"] != "Taimanin_leotard" and "Taimanin_leotard" in Girl.inventory:
                $ item = "Taimanin_leotard"
            "You have that pretty black dress." if Girl == KittyX and Girl.Clothes["dress"] != "black_dress" and "black_dress" in Girl.inventory:
                $ item = "black_dress"
            "Can you wear that domme outfit?" if Girl == EmmaX and Girl.Clothes["bodysuit"] != "domme_suit" and "domme_suit" in Girl.inventory:
                $ item = "domme_suit"
            "Throw on that bunny outfit." if Girl == LauraX and Girl.Clothes["bodysuit"] != "bunny_suit" and "bunny_suit" in Girl.inventory:
                $ item = "bunny_suit"
            "What about your slave outfit?" if Girl == LauraX and Girl.Clothes["bodysuit"] != "slave_outfit" and "slave_outfit" in Girl.inventory:
                $ item = "slave_outfit"
            "Try on your Ahsoka outfit." if Girl == LauraX and Girl.Clothes["dress"] != "Ahsoka_outfit" and "Ahsoka_outfit" in Girl.inventory:
                $ item = "Ahsoka_outfit"
            "Hmm, maybe your Mavis dress?" if Girl == LauraX and Girl.Clothes["dress"] != "Mavis_dress" and "Mavis_dress" in Girl.inventory:
                $ item = "Mavis_dress"
            "Try on that sci-fi suit." if Girl == JeanX and Girl.Clothes["bodysuit"] != "sci_fi_suit" and "sci_fi_suit" in Girl.inventory:
                $ item = "sci_fi_suit"
            "I want to see something else.":
                return

        if item == "no_cloak":
            $ Girl.take_off("cloak")
        elif item == "no_dress":
            call change_dress(Girl, "")
        elif item == "no_bodysuit":
            call change_bodysuit(Girl, "")
        elif item in cloaks:
            $ Girl.Clothes["cloak"] = item
        elif item in dresses:
            call change_dress(Girl, item)
        elif item in bodysuits:
            call change_bodysuit(Girl, item)

label accessories_menu(Girl):
    while True:
        menu:
            "I liked your original hair style." if Girl == RogueX and Girl.Clothes["hair"] != "evo":
                $ approval = approval_check(Girl, 600)

                if approval:
                    ch_r "Oh, ok."

                    $ Girl.Clothes["hair"] = "evo"
                else:
                    ch_r "I kinda prefer this look."
            "Can you put your hair up in a ponytail?" if Girl == KittyX and Girl.Clothes["hair"] != "evo":
                $ approval = approval_check(Girl, 600)

                if approval:
                    ch_k "Like this?"

                    $ Girl.Clothes["hair"] = "evo"
                else:
                    ch_k "Yeah, I know that."
            "I like your loose hair style." if Girl == KittyX and Girl.Clothes["hair"] != "long":
                $ approval = approval_check(Girl, 600)

                if approval:
                    ch_k "You think?"

                    $ Girl.Clothes["hair"] = "long"
                else:
                    ch_k "I[Girl.like]kinda prefer to keep it up."
            "You look good with your hair flowing." if Girl == EmmaX and Girl.Clothes["hair"] != "wavy":
                $ approval = approval_check(Girl, 600)

                if approval:
                    ch_e "Like this?"

                    $ Girl.Clothes["hair"] = "wavy"
                else:
                    ch_e "Yes, I do."
            "Maybe keep your hair straight." if Girl == EmmaX and Girl.Clothes["hair"] != "wet":
                $ approval = approval_check(Girl, 600)

                if approval:
                    ch_e "You think?"

                    $ Girl.Clothes["hair"] = "wet"
                else:
                    ch_e "I tend to prefer it a bit more loose."
            "You look good with your hair loose." if Girl == LauraX and Girl.Clothes["hair"] != "long":
                $ approval = approval_check(Girl, 600)

                if approval:
                    ch_l "Ok."

                    $ Girl.Clothes["hair"] = "long"
                else:
                    ch_l "I don't know, it's fine like this."
            "I like your loose hair style." if Girl == JeanX and Girl.Clothes["hair"] != "short":
                $ approval = approval_check(Girl, 600)

                if approval:
                    ch_j "Ok."

                    $ Girl.Clothes["hair"] = "short"
                else:
                    ch_j "I don't know, it's fine like this."
            "Can you grow out your hair for me?" if Girl == StormX and Girl.Clothes["hair"] not in ["long", "wet_long"]:
                if "hair" in Girl.recent_history:
                    ch_s "I have already messed with it too much today."
                elif approval_check(StormX, 900):
                    ch_s "Oh, you did?"
                    ch_s "I suppose I could speak to Hank about that. . ."

                    show black_screen onlayer black

                    "She steps away for a few minutes."

                    hide black_screen onlayer black

                    if Girl.Clothes["hair"] == "wet_mohawk":
                        $ Girl.Clothes["hair"] = "wet_long"
                    else:
                        $ Girl.Clothes["hair"] = "long"

                    $ Girl.add_word(1, "hair", "hair", 0, 0)

                    ch_s "Like this?"
                else:
                    ch_s "Thank you, but I'm not interested in that style right now."
            "What about a mohawk?" if Girl == StormX and Girl.Clothes["hair"] not in ["mohawk", "wet_mohawk"]:
                if "hair" in Girl.recent_history:
                    ch_s "I have already messed with it too much today."
                elif approval_check(StormX, 900):
                    ch_s "You liked it?"

                    show black_screen onlayer black

                    "She steps away for a few minutes."

                    hide black_screen onlayer black

                    if Girl.Clothes["hair"] == "wet_long":
                        $ Girl.Clothes["hair"] = "wet_mohawk"
                    else:
                        $ Girl.Clothes["hair"] = "mohawk"

                    $ Girl.add_word(1, "hair", "hair", 0, 0)

                    ch_s "Like this?"
                else:
                    ch_s "Thank you, but I'm not interested in that style right now."
            "I like your normal hair best." if Girl == JubesX and Girl.Clothes["hair"] != "short":
                $ approval = approval_check(Girl, 600)

                if approval:
                    ch_v "Ok."

                    $ Girl.Clothes["hair"] = "short"
                else:
                    ch_v "I don't know, it's fine like this."
            "Try that wet look with your hair." if Girl in [RogueX, KittyX, LauraX, StormX, JubesX] and Girl.Clothes["hair"] not in ["wet", "wet_long", "wet_mohawk"]:
                $ approval = approval_check(Girl, 800)

                if Girl == RogueX:
                    if approval:
                        ch_r "Hmm?"

                        $ Girl.Clothes["hair"] = "wet"

                        "She wanders off for a minute and comes back."

                        ch_r "Like this?"
                    else:
                        ch_r "Not really into that."
                elif Girl == KittyX:
                    if approval:
                        ch_k "You think so?"

                        $ Girl.Clothes["hair"] = "wet"

                        "She rummages in her bag and grabs some gel, running it through her hair."

                        ch_k "Like this?"
                    else:
                        ch_k "It's too high maintenance."
                elif Girl == LauraX:
                    if approval:
                        ch_l "Hmm?"

                        $ Girl.Clothes["hair"] = "wet"

                        "She wanders off for a minute and comes back."

                        ch_l "Like this?"
                    else:
                        ch_l "Ugh, too much work."
                elif Girl == JeanX:
                    if approval:
                        ch_j "Hmm?"

                        $ Girl.Clothes["hair"] = "wet"

                        "She wanders off for a minute and comes back."

                        ch_j "Like this?"
                    else:
                        ch_j "Ugh, too much work."
                elif Girl == StormX:
                    if approval:
                        ch_s "Really?"

                        if Girl.Clothes["hair"] == "mohawk":
                            $ Girl.Clothes["hair"] = "wet_mohawk"
                        else:
                            $ Girl.Clothes["hair"] = "wet_long"

                        "A concentrated hurricane swirls around her head for a moment, leaving her hair limp."

                        ch_s "Like this?"
                    else:
                        ch_s "I'd rather not."
                elif Girl == JubesX:
                    if approval:
                        ch_v "Hmm?"

                        $ Girl.Clothes["hair"] = "wet"

                        "She wanders off for a minute and comes back."

                        ch_v "Like this?"
                    else:
                        ch_v "Ugh, too much work."
            "Can you dry out your hair?" if Girl == StormX and Girl.Clothes["hair"] in ["wet_long", "wet_mohawk"]:
                $ approval = approval_check(Girl, 600)

                if approval:
                    ch_s "Fine."

                    "A gust of wind swirls around her hair."

                    if Girl.Clothes["hair"] == "wet_mohawk":
                        $ Girl.Clothes["hair"] = "mohawk"
                    else:
                        $ Girl.Clothes["hair"] = "long"
                else:
                    ch_s "I'm unsure, I think this is fine."
            "Try the hair you had at the Halloween party." if Girl == RogueX and Girl.Clothes["hair"] != "cosplay" and "halloween" in Girl.history:
                $ approval = approval_check(Girl, 600)

                if Girl == RogueX:
                    if approval:
                        ch_r "Oh, ok."

                        $ Girl.Clothes["hair"] = "cosplay"
                    else:
                        ch_r "I kinda prefer this look."
            "Can you put your hair up in a side ponytail?" if Girl == JeanX and Girl.Clothes["hair"] != "pony" and "halloween" in Girl.history:
                $ approval = approval_check(Girl, 600)

                if approval:
                    ch_j "Ok."

                    $ Girl.Clothes["hair"] = "pony"
                else:
                    ch_j "I don't know, it's fine like this."
            "That hair style you had at the Halloween party was great." if Girl == StormX and Girl.Clothes["hair"] != "short" and "halloween" in Girl.history:
                if "hair" in Girl.recent_history:
                    ch_s "I have already messed with it too much today."
                elif approval_check(StormX, 900):
                    ch_s "Oh, you did?"
                    ch_s "I suppose I could speak to Hank about that. . ."

                    show black_screen onlayer black

                    "She steps away for a few minutes."

                    hide black_screen onlayer black

                    $ Girl.Clothes["hair"] = "short"

                    $ Girl.add_word(1, "hair", "hair", 0, 0)

                    ch_s "Like this?"
                else:
                    ch_s "Thank you, but I'm not interested in that style right now."
            "Try dying your hair." if Girl == KittyX and Girl.Clothes["hair"] != "dyed":
                $ approval = approval_check(Girl, 600)

                if approval:
                    ch_k "Hmm, I suppose so. . ."

                    $ Girl.Clothes["hair"] = "dyed"
                else:
                    ch_k "I[Girl.like]kinda prefer it the way it is."
            "Try wearing your hair with bangs." if Girl == EmmaX and Girl.Clothes["hair"] != "bangs":
                $ approval = approval_check(Girl, 600)

                if approval:
                    ch_e "You think?"

                    $ Girl.Clothes["hair"] = "bangs"
                else:
                    ch_e "I tend to prefer it a bit more loose."
            "Grow out your pubic hair." if not Girl.pubes:
                if "pubes" in Girl.to_do:
                    $ Girl.change_face("bemused", 1)

                    if Girl == RogueX:
                        ch_r "Yeah, I know, [Girl.player_petname]. It doesn't grow out overnight!"
                    elif Girl == KittyX:
                        ch_k "[[snort] You've got to give it some time!"
                else:
                    $ Girl.change_face("bemused", 1)

                    $ approval = approval_check(Girl, 1150, taboo_modifier=0)

                    if approval_check(Girl, 850, "L", taboo_modifier=0) or (approval and Girl.love > Girl.obedience):
                        if Girl == RogueX:
                            ch_r "Well. . . if that's how you like it. . ."
                        elif Girl == KittyX:
                            ch_k "I guess I could. . ."

                        $ Girl.to_do.append("pubes")
                        $ Girl.pubes_counter = 6
                    elif approval_check(Girl, 500, "O", taboo_modifier=0) or (approval and Girl.obedience > Girl.inhibition):
                        if Girl == RogueX:
                            ch_r "If that's what you want."
                        elif Girl == KittyX:
                            ch_k "You want a furry kitty to pet?"

                        $ Girl.to_do.append("pubes")
                        $ Girl.pubes_counter = 6
                    elif approval_check(Girl, 500, "I", taboo_modifier=0) or approval:
                        if Girl == RogueX:
                            ch_r "Heh, I like a man knows what he wants, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k "If you want me to. . ."

                        $ Girl.to_do.append("pubes")
                        $ Girl.pubes_counter = 6
                    else:
                        $ Girl.change_face("surprised", brows = "angry")

                        if Girl == RogueX:
                            ch_r "Well I don't see how that's any of your business, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k "Not that it's any of your business, [Girl.player_petname]."
            "I like it waxed clean down there." if Girl.pubes == "_hairy":
                $ Girl.change_face("bemused", 1)

                if "shave" in Girl.to_do:
                    if Girl == RogueX:
                        ch_r "I know, I'll get on that. Not right this second, obviously."
                    elif Girl == KittyX:
                        ch_k "I know, I know. I'll take care of it later."
                else:
                    $ approval = approval_check(Girl, 1150, taboo_modifier=0)

                    if approval_check(Girl, 850, "L", taboo_modifier=0) or (approval and Girl.love > Girl.obedience):
                        if Girl == RogueX:
                            ch_r "I can keep it tidy if you like. . ."
                        elif Girl == KittyX:
                            ch_k "I guess I could tidy up a bit. . ."

                        $ Girl.to_do.append("shave")
                    elif approval_check(Girl, 500, "O", taboo_modifier=0) or (approval and Girl.obedience > Girl.inhibition):
                        if Girl == RogueX:
                            ch_r "I'll take care of it."
                        elif Girl == KittyX:
                            ch_k "I'll keep it smooth."

                        $ Girl.to_do.append("shave")
                    elif approval_check(Girl, 500, "I", taboo_modifier=0) or approval:
                        if Girl == RogueX:
                            ch_r "You better earn it, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k "I'll get it done."

                        $ Girl.to_do.append("shave")
                    else:
                        $ Girl.change_face("surprised", brows = "angry")

                        if Girl == RogueX:
                            ch_r "I don't see how that's any of your beeswax, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k "Not that it's any of your business, [Girl.player_petname]."
            "You'd look nice with ring body piercings." if Girl.Clothes["piercings"] != "ring" and (Girl.seen_pussy or Girl.seen_breasts):
                $ Girl.change_face("bemused", 1)

                if "ring" in Girl.to_do:
                    if Girl == RogueX:
                        ch_r "Yeah, I know, I'll get to it."
                    elif Girl == KittyX:
                        ch_k "I know, I know. I'll take care of it later."
                else:
                    $ approval = approval_check(Girl, 1350, taboo_modifier=0)

                    if approval_check(Girl, 950, "L", taboo_modifier=0) or (approval and Girl.love > Girl.obedience):
                        if Girl == RogueX:
                            ch_r "You really like those? Well, I suppose. . ."
                        elif Girl == KittyX:
                            ch_k "If you think they'd look good on me. . ."

                        $ Girl.to_do.append("ring")
                    elif approval_check(Girl, 600, "O", taboo_modifier=0) or (approval and Girl.obedience > Girl.inhibition):
                        if Girl == RogueX:
                            ch_r "I'll go get that taken care of."

                        $ Girl.to_do.append("ring")
                    elif approval_check(Girl, 600, "I", taboo_modifier=0) or approval:
                        if Girl == RogueX:
                            ch_r "I've always kind of liked the look of those. . ."
                        elif Girl == KittyX:
                            ch_k "I think they'd look great too!"

                        $ Girl.to_do.append("ring")
                    else:
                        $ Girl.change_face("surprised", brows = "angry")

                        if Girl == RogueX:
                            ch_r "I don't see how that's any of your beeswax, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k "Not that it's any of your business, [Girl.player_petname]."
            "You'd look nice with barbell body piercings." if Girl.Clothes["piercings"] != "barbell" and (Girl.seen_pussy or Girl.seen_breasts):
                $ Girl.change_face("bemused", 1)

                if "barbell" in Girl.to_do:
                    if Girl == RogueX:
                        ch_r "Yeah, I know, I'll get to it."
                    elif Girl == KittyX:
                        ch_k "I know, I know. I'll take care of it later."
                else:
                    $ approval = approval_check(Girl, 1350, taboo_modifier=0)

                    if approval_check(Girl, 950, "L", taboo_modifier=0) or (approval and Girl.love > Girl.obedience):
                        if Girl == RogueX:
                            ch_r "You really like those? Well, I suppose. . ."
                        elif Girl == KittyX:
                            ch_k "If you think they'd look good on me. . ."

                        $ Girl.to_do.append("barbell")
                    elif approval_check(Girl, 600, "O", taboo_modifier=0) or (approval and Girl.obedience > Girl.inhibition):
                        if Girl == RogueX:
                            ch_r "I'll go get that taken care of."
                        elif Girl == KittyX:
                            ch_k "I think they'd look great too!"

                        $ Girl.to_do.append("barbell")
                    elif approval_check(Girl, 600, "I", taboo_modifier=0) or approval:
                        if Girl == RogueX:
                            ch_r "I've always kind of liked the look of those. . ."
                        elif Girl == KittyX:
                            ch_k "K, I'll take care of it."

                        $ Girl.to_do.append("barbell")
                    else:
                        $ Girl.change_face("surprised", brows = "angry")

                        if Girl == RogueX:
                            ch_r "I don't see how that's any of your beeswax, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k "Not that it's any of your business, [Girl.player_petname]."

            "You'd look better without those piercings." if Girl.Clothes["piercings"]:
                $ Girl.change_face("bemused", 1)

                $ approval = approval_check(Girl, 1350, taboo_modifier=0)

                if approval_check(Girl, 950, "L", taboo_modifier=0) or (approval and Girl.love > Girl.obedience):
                    if Girl == RogueX:
                        ch_r "You really think so? I guess I could lose them. . ."
                    elif Girl == KittyX:
                        ch_k "I guess if they're getting in the way . ."

                    $ Girl.take_off("piercings")
                elif approval_check(Girl, 600, "O", taboo_modifier=0) or (approval and Girl.obedience > Girl.inhibition):
                    if Girl == RogueX:
                        ch_r "I'll take them out then."
                    elif Girl == KittyX:
                        ch_k "I'll take them out then."

                    $ Girl.take_off("piercings")
                elif approval_check(Girl, 600, "I", taboo_modifier=0) or approval:
                    if Girl == RogueX:
                        ch_r "I guess I prefered not having them in. . ."
                    elif Girl == KittyX:
                        ch_k "They were getting a little annoying."

                    $ Girl.take_off("piercings")
                else:
                    $ Girl.change_face("surprised", brows = "angry")

                    if Girl == RogueX:
                        ch_r "I'll keep them, if you don't mind."
                    elif Girl == KittyX:
                        ch_k "Well {i}I{/i} kinda like'em."
            "Toggle DVA headband." if Girl == KittyX and "DVA_headband" in Girl.inventory:
                if Girl.Clothes["face_outer_accessory"] == "DVA_headband":
                    $ Girl.take_off("face_outer_accessory")
                else:
                    $ Girl.Clothes["face_outer_accessory"] = "DVA_headband"
            "Toggle pink ears." if Girl == KittyX and "pink_ears" in Girl.inventory:
                if Girl.Clothes["face_outer_accessory"] == "pink_ears":
                    $ Girl.take_off("face_outer_accessory")
                else:
                    $ Girl.Clothes["face_outer_accessory"] = "pink_ears"
            "Toggle hat." if Girl == EmmaX and "halloween" in Girl.history:
                if Girl.Clothes["face_outer_accessory"] == "hat":
                    $ Girl.take_off("face_outer_accessory")
                else:
                    $ Girl.Clothes["face_outer_accessory"] = "hat"
            "Toggle shades." if Girl == JubesX:
                if Girl.Clothes["face_outer_accessory"] == "shades":
                    $ Girl.take_off("face_outer_accessory")
                else:
                    $ Girl.Clothes["face_outer_accessory"] = "shades"
            "Toggle blindfold." if Girl == KittyX:
                if Girl.Clothes["face_inner_accessory"] == "blindfold":
                    $ Girl.take_off("face_inner_accessory")
                else:
                    $ Girl.Clothes["face_inner_accessory"] = "blindfold"
            "Toggle earrings." if Girl in [StormX, JubesX]:
                if Girl.Clothes["face_inner_accessory"] == "earrings":
                    $ Girl.take_off("face_inner_accessory")
                else:
                    $ Girl.Clothes["face_inner_accessory"] = "earrings"
            "Toggle gag." if Girl == KittyX:
                if Girl.Clothes["gag"] == "ballgag":
                    $ Girl.take_off("gag")
                else:
                    $ Girl.Clothes["gag"] = "ballgag"
            "Toggle spiked collar." if Girl == RogueX:
                if Girl.Clothes["neck"] == "spiked_collar":
                    $ Girl.take_off("neck")
                else:
                    $ Girl.Clothes["neck"] = "spiked_collar"
            "Toggle spiked collar." if Girl == EmmaX and "spiked_collar" in Girl.inventory:
                if Girl.Clothes["neck"] == "spiked_collar":
                    $ Girl.take_off("neck")
                else:
                    $ Girl.Clothes["neck"] = "spiked_collar"
            "Toggle necklace." if Girl == KittyX:
                if Girl.Clothes["neck"] == "":
                    $ Girl.Clothes["neck"] = "gold_necklace"
                elif Girl.Clothes["neck"] == "gold_necklace":
                    $ Girl.Clothes["neck"] = "star_necklace"
                elif Girl.Clothes["neck"] == "star_necklace":
                    $ Girl.Clothes["neck"] = "flower_necklace"
                elif Girl.Clothes["neck"] == "flower_necklace":
                    $ Girl.take_off("neck")
            "Toggle choker." if Girl == EmmaX:
                if Girl.Clothes["neck"] == "choker":
                    $ Girl.take_off("neck")
                else:
                    $ Girl.Clothes["neck"] = "choker"
            "Toggle medallion choker." if Girl == LauraX:
                if Girl.Clothes["neck"] == "leash_choker":
                    $ Girl.take_off("neck")
                else:
                    $ Girl.Clothes["neck"] = "leash_choker"
            "Toggle necklace." if Girl == StormX:
                if Girl.Clothes["neck"] == "":
                    $ Girl.Clothes["neck"] = "gold_necklace"
                elif Girl.Clothes["neck"] == "gold_necklace":
                    if "halloween" in Girl.history:
                        $ Girl.Clothes["neck"] = "ring_necklace"
                    else:
                        $ Girl.take_off("neck")
                elif Girl.Clothes["neck"] == "ring_necklace":
                    $ Girl.take_off("neck")
            "Toggle slut choker." if Girl == RogueX and "slut_choker" in Girl.inventory:
                if Girl.Clothes["neck"] == "slut_choker":
                    $ Girl.take_off("neck")
                else:
                    $ Girl.Clothes["neck"] = "slut_choker"
            "Toggle shawl." if Girl == KittyX and "shawl" in Girl.inventory:
                if Girl.Clothes["neck"] == "shawl":
                    $ Girl.take_off("neck")
                else:
                    $ Girl.Clothes["neck"] = "shawl"
            "Open/close jacket." if Girl.Clothes["jacket"] and not Girl.jacket_closed:
                if Girl.jacket_opened:
                    $ Girl.jacket_opened = False
                else:
                    $ Girl.jacket_opened = True
            "Zip the jacket up/down?" if Girl == JubesX and Girl.Clothes["jacket"] and not Girl.jacket_opened:
                if Girl.jacket_closed:
                    $ Girl.jacket_closed = False
                else:
                    $ Girl.jacket_closed = True
            "Toggle suspenders." if Girl in [LauraX, JeanX]:
                if Girl.Clothes["suspenders"] == "suspenders":
                    $ Girl.take_off("suspenders")
                else:
                    $ Girl.Clothes["suspenders"] = "suspenders"
            "Shift suspenders." if Girl.Clothes["suspenders"]:
                if Girl.Clothes["suspenders"].state:
                    $ Girl.Clothes["suspenders"].state = False
                else:
                    $ Girl.Clothes["suspenders"].state = True
            "Toggle tattoos." if Girl == StormX:
                if Girl.Clothes["tattoos"] == "tattoos":
                    $ Girl.take_off("tattoos")
                else:
                    $ Girl.Clothes["tattoos"] = "tattoos"
            "Toggle spider-web nipple covers." if Girl == LauraX:
                if Girl.Clothes["nipple_accessories"] == "spider_webs":
                    $ Girl.take_off("nipple_accessories")
                else:
                    $ Girl.Clothes["nipple_accessories"] = "spider_webs"
            "Toggle ring armlets." if Girl == StormX and "halloween" in Girl.history:
                if Girl.Clothes["sleeves"] == "ring_armlets":
                    $ Girl.take_off("sleeves")
                else:
                    $ Girl.Clothes["sleeves"] = "ring_armlets"
            "Toggle gloves." if Girl in [RogueX, EmmaX]:
                if Girl.Clothes["gloves"] == "gloves":
                    $ Girl.take_off("gloves")
                else:
                    $ Girl.Clothes["gloves"] = "gloves"
            "Toggle gloves." if Girl == KittyX:
                if Girl.Clothes["gloves"] == "black_gloves":
                    $ Girl.take_off("gloves")
                else:
                    $ Girl.Clothes["gloves"] = "black_gloves"
            "Toggle wristbands." if Girl == LauraX:
                if Girl.Clothes["gloves"] == "wrists":
                    $ Girl.take_off("gloves")
                else:
                    $ Girl.Clothes["gloves"] = "wrists"
            "Toggle gloves." if Girl == LauraX and "halloween" in Girl.history:
                if Girl.Clothes["gloves"] == "gloves":
                    $ Girl.take_off("gloves")
                else:
                    $ Girl.Clothes["gloves"] = "gloves"
            "Toggle bunny cuffs." if Girl == LauraX and "bunny_gloves" in Girl.inventory:
                if Girl.Clothes["gloves"] == "bunny_gloves":
                    $ Girl.take_off("gloves")
                else:
                    $ Girl.Clothes["gloves"] = "bunny_gloves"
            "Toggle sweater." if Girl == RogueX and "halloween" in Girl.history:
                if Girl.Clothes["belt"] == "sweater":
                    $ Girl.take_off("belt")
                else:
                    $ Girl.Clothes["belt"] = "sweater"
            "Never mind":
                return

label alternate_clothes(Girl, outfit = 1):
    if Girl.clothing[outfit] == 1 or not Girl.clothing[outfit]:
        $ Girl.outfit_name = "default"
    elif Girl.clothing[outfit] == 2:
        $ Girl.outfit_name = "second_casual"
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
        $ Girl.outfit_name = "default"

    return

label set_outfit_schedule(Girl):
    $ shift_focus(Girl)

    while True:
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
                "Everyday":
                    menu:
                        "Pick an outfit for [Girl.name] to wear everyday.":
                            call choose_outfit(Girl)

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
                            call choose_outfit(Girl)

                            $ Girl.clothing[0] = _return
                        "On Monday you should wear. . .(locked)" if counter <= 1:
                            pass
                        "On Tuesday you should wear. . ." if counter > 2:
                            call choose_outfit(Girl)

                            $ Girl.clothing[1] = _return
                        "On Tuesday you should wear. . .(locked)" if counter <= 2:
                            pass
                        "On Wednesday you should wear. . ." if counter > 1:
                            call choose_outfit(Girl)

                            $ Girl.clothing[2] = _return
                        "On Wednesday you should wear. . .(locked)" if counter <= 1:
                            pass
                        "On Thursday you should wear. . ." if counter > 2:
                            call choose_outfit(Girl)

                            $ Girl.clothing[3] = _return
                        "On Thursday you should wear. . .(locked)" if counter <= 2:
                            pass
                        "On Friday you should wear. . ." if counter > 1:
                            call choose_outfit(Girl)

                            $ Girl.clothing[4] = _return
                        "On Friday you should wear. . .(locked)" if counter <= 1:
                            pass
                        "On Saturday you should wear. . .(locked)" if counter < 1:
                            pass
                        "On Saturday you should wear. . ." if counter >= 1:
                            call choose_outfit(Girl)

                            $ Girl.clothing[5] = _return
                        "On Sunday you should wear. . .(locked)" if counter < 1:
                            pass
                        "On Sunday you should wear. . ." if counter >= 1:
                            call choose_outfit(Girl)

                            $ Girl.clothing[6] = _return
                        "Back":
                            pass
                "Other":
                    menu:
                        "In our rooms you should wear. . ." if counter >= 1:
                            call choose_outfit(Girl, 99)

                            $ Girl.clothing[9] = _return
                        "In our rooms you should wear. . .(locked)" if counter < 1:
                            pass
                        "On dates you should wear. . ." if counter >= 1:
                            call choose_outfit(Girl)

                            $ Girl.clothing[7] = _return
                        "On dates you should wear. . .(locked)" if counter < 1:
                            pass
                        "When teaching you should wear. . ." if Girl in(EmmaX, StormX) and counter >= 3:
                            call choose_outfit(Girl, 90)

                            $ Girl.clothing[8] = _return
                        "When teaching you should wear. . .(locked)" if Girl in(EmmaX, StormX) and counter < 3:
                            pass
                        "Back":
                            pass
                "About gym clothes":
                    menu:
                        ch_p "You asked me before about your gym clothes?"
                        "Don't ask before changing into gym clothes." if "no_ask gym" not in Girl.traits:
                            Girl.voice "Sure."

                            $ Girl.traits.append("no_ask gym")
                        "Ask me before changing into gym clothes." if "no_ask gym" in Girl.traits:
                            Girl.voice "Sure."

                            $ Girl.traits.remove("no_ask gym")
                        "Never mind.":
                            pass
                "Private" if Girl.clothing[9]:
                    ch_p "You know that outfit you wear in private?"

                    if Girl in [EmmaX, StormX]:
                        Girl.voice "Yes?"
                    else:
                        Girl.voice "Yeah?"

                    menu:
                        extend ""
                        "Just put it on without asking me about it." if "comfy" not in Girl.traits:
                            Girl.voice "Sure."

                            $ Girl.traits.append("comfy")
                        "Ask before changing into that." if "comfy" in Girl.traits:
                            Girl.voice "Sure."

                            $ Girl.traits.remove("comfy")
                        "Never mind.":
                            pass
                "Never mind.":
                    return

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
                "The first one." if Girl.first_custom_outfit["outfit_active"]:
                    if Girl.first_custom_outfit["outfit_active"] == 2 or count == 99:
                        $ count = 3
                    else:
                        Girl.voice "Well. . ."

                        call quick_outfit_check(Girl, 3)

                        if Girl.first_custom_outfit["outfit_active"] == 2:
                            $ count = 3
                        else:
                            $ line = "no"
                "The first one.(locked)" if not Girl.first_custom_outfit["outfit_active"]:
                    pass
                "The second one." if Girl.second_custom_outfit["outfit_active"]:
                    if Girl.second_custom_outfit["outfit_active"] == 2 or count == 99:
                        $ count = 5
                    else:
                        Girl.voice "Well. . ."

                        call quick_outfit_check(Girl, 5)

                        if Girl.second_custom_outfit["outfit_active"] == 2:
                            $ count = 5
                        else:
                            $ line = "no"
                "The second one.(locked)" if not Girl.second_custom_outfit["outfit_active"]:
                    pass
                "The third one." if Girl.third_custom_outfit["outfit_active"]:
                    if Girl.third_custom_outfit["outfit_active"] == 2 or count == 99:
                        $ count = 6
                    else:
                        Girl.voice "Well. . ."

                        call quick_outfit_check(Girl, 6)

                        if Girl.third_custom_outfit["outfit_active"] == 2:
                            $ count = 6
                        else:
                            $ line = "no"
                "The third one.(locked)" if not Girl.third_custom_outfit["outfit_active"]:
                    pass
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

                call quick_outfit_check(Girl, 7)

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

    if outfit_holder["bra"] in ["tank", "white_tank", "button_tank", "sports_bra", "tube_top", "corset"]:
        $ count = 20
    elif outfit_holder["bra"] == "wolvie_bra":
        $ count = 10
    elif outfit_holder["bra"] in ["lace_bra", "lace_corset"]:
        $ count = 5
    elif outfit_holder["bra"]:
        $ count = 10
    elif outfit_holder["suspenders"] == "suspenders" or outfit_holder["suspenders"] == "suspenders2":
        $ count = 5
    else:
        $ count = 0

    if outfit_holder["top"] in ["nighty", "mesh_top"]:
        $ count += 5
    elif outfit_holder["top"] == "towel":
        if Girl == EmmaX:
            $ count += 5
        elif Girl == StormX:
            pass
        else:
            $ count += 10
    elif outfit_holder["top"] in ["jacket", "dress", "pink_top"] or outfit_holder["jacket"] == "jacket":
        $ count += 15
    elif outfit_holder["top"] or outfit_holder["jacket"] == "closed_jacket":
        $ count += 20

    if Girl.Clothes["piercings"] and count <= 10:
        $ count = -5

    $ count = 20 if count >= 20 else count

    $ shame -= count

    if outfit_holder["bottom"] and outfit_holder["underwear"]:
        $ count = 30
    elif outfit_holder["bottom"] in ["blue_skirt", "skirt", "cosplay_skirt"]:
        $ count = 20
    elif outfit_holder["bottom"] or outfit_holder["jacket"] == "closed_jacket":
        $ count = 25
    elif outfit_holder["underwear"] == "shorts":
        $ count = 25
    elif outfit_holder["underwear"] in ["bikini", "sports_panties", "shorts"]:
        $ count = 15
    elif outfit_holder["underwear"] == "lace_panties":
        $ count = 5
    elif outfit_holder["underwear"]:
        $ count = 10

    if outfit_holder["hose"] == "tights":
        $ count = 25 if count < 25 else count

    if outfit_holder["top"] == "towel" and Girl not in [EmmaX, StormX]:
        $ count = 25 if count else 15

    $ shame -= count

    if "exhibitionist" in Girl.traits:
        $ agree = True
    elif shame <= 5:
        $ agree = True
    elif shame <= 15 and (approval_check(Girl, 1700, taboo_modifier = 0, cologne = 0) or approval_check(Girl, 400, "I", taboo_modifier = 0, cologne = 0)):
        $ agree = True
    elif outfit_to_check == 10 and shame <= 20:
        $ agree = True
    elif Girl == EmmaX and shame >= 15 and "public" not in Girl.history:
        $ agree = 0
    elif Girl == StormX and StormX in Rules:
        $ agree = True
    elif shame <= 25:
        if approval_check(Girl, 2300, taboo_modifier = 0, cologne = 0) or approval_check(Girl, 700, "I", taboo_modifier = 0, cologne = 0):
            $ agree = True
        else:
            $ agree = False
    elif (approval_check(Girl, 2500, taboo_modifier = 0, cologne = 0) or approval_check(Girl, 800, "I", taboo_modifier = 0, cologne = 0)):
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

label ask_for_dress_screen(Girl):
    if renpy.showing('dress_screen'):
        return True

    if Girl == StormX:
        if not Girl.taboo or StormX in Rules:
            return True
        else:
            ch_s "I'm afraid rules are rules."

    if Girl.taboo:
        return False

    $ Girl.change_face("bemused", 1, eyes = "side")

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

    $ Girl.add_word(1, 0, "screen")
    $ Girl.change_face("bemused", 1)

    menu:
        Girl.voice "Mind if I get behind a dressing screen?"
        "Go ahead.":
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






label Private_outfit(Girl):
    if Girl.broken_up[0] or "angry" in Girl.daily_history:
        return

    if Girl.outfit_name == "temporary" or not Girl.clothing[9]:
        return

    if "comfy" in Girl.recent_history or "comfy" in Girl.traits or Girl.outfit_name == Girl.clothing[9]:
        call alternate_clothes(Girl, 9)

        $ Girl.change_Outfit()
    elif "no_comfy" in Girl.recent_history:
        pass
    elif approval_check(Girl, 1200, "LI") and (2*Girl.inhibition) >=(Girl.love + Girl.obedience +100):
        $ shift_focus(Girl)

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

        $ Girl.change_Outfit()
        $ Girl.recent_history.append("comfy")
    else:
        $ shift_focus(Girl)

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

                call alternate_clothes(Girl, 9)

                $ Girl.change_Outfit()
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




label Custom_Out(Girl=0, Custom = 3, Shame=0, Agree=0):

    $ Girl = check_girl(Girl)
    $ shift_focus(Girl)
    $ Girl.change_face("sexy", 1)

    if Custom == 3:
        $ Shame = Girl.first_custom_outfit[10]
        if Girl.first_custom_outfit["outfit_active"] == 2 or "exhibitionist" in Girl.traits:
            $ Girl.outfit_name = "custom1"
            $ Agree = 1
        else:
            call quick_outfit_check(Girl, 3)
            if Girl.first_custom_outfit["outfit_active"] == 2:
                $ Girl.outfit_name = "custom1"
                $ Agree = 1
    elif Custom == 5:
        $ Shame = Girl.second_custom_outfit[10]
        if Girl.second_custom_outfit["outfit_active"] == 2 or "exhibitionist" in Girl.traits:
            $ Girl.outfit_name = "custom2"
            $ Agree = 1
        else:
            call quick_outfit_check(Girl, 5)
            if Girl.second_custom_outfit["outfit_active"] == 2:
                $ Girl.outfit_name = "custom2"
                $ Agree = 1
    else:
        $ Shame = Girl.third_custom_outfit[10]
        if Girl.third_custom_outfit["outfit_active"] == 2 or "exhibitionist" in Girl.traits:
            $ Girl.outfit_name = "custom3"
            $ Agree = 1
        else:
            call quick_outfit_check(Girl, 6)
            if Girl.third_custom_outfit["outfit_active"] == 2:
                $ Girl.outfit_name = "custom3"
                $ Agree = 1

    if Girl == RogueX:
        if Agree:
            if "exhibitionist" in Girl.traits:
                ch_r "Ooo, momma likes."
            elif Shame >= 50:
                ch_r "You realize I'm pretty much naked here, right?"
            elif Shame >= 25:
                ch_r "This is pretty shameless. . ."
            elif Shame >= 15:
                $ Girl.change_face("bemused", 1)
                ch_r "I don't know, I guess I could try it. . ."
            else:
                ch_r "Sure, [Girl.player_petname], that one's nice."
        else:

            if Shame >= 50:
                $ Girl.change_face("angry", 1)
                ch_r "Come on, I'd be totally nude!"
            elif Shame >= 25:
                $ Girl.change_face("angry", 1)
                ch_r "You're lucky I show {i}you{/i} this."
            else:
                $ Girl.change_face("bemused", 1)
                ch_r "It's kind of daring for me, sorry."
    elif Girl == KittyX:
        if Agree:
            if "exhibitionist" in Girl.traits:
                ch_k "Hmm, I'm getting excited. . ."
            elif Shame >= 50:
                ch_k "This is. . . kinda slutty. . . but. . ."
            elif Shame >= 25:
                ch_k "I'm not really comfortable with this one. . ."
            elif Shame >= 15:
                $ Girl.change_face("bemused", 1)
                ch_k "I'll give it a shot. . ."
            else:
                ch_k "Yeah, I like that one too."
        else:

            if Shame >= 50:
                $ Girl.change_face("angry", 1)
                ch_k "You have GOT to be kidding me here."
            elif Shame >= 25:
                $ Girl.change_face("angry", 1)
                ch_k "This is just between us."
            else:
                $ Girl.change_face("bemused", 1)
                ch_k "I can't wear this out!"
    elif Girl == EmmaX:
        if Agree:
            if "exhibitionist" in Girl.traits:
                ch_e "Hmm, I'm getting excited. . ."
            elif Shame >= 50:
                ch_e "This is rather. . . shameless. . ."
            elif Shame >= 25:
                ch_e "I'm a bit uncomfortable with this one. . ."
            elif Shame >= 15:
                $ Girl.change_face("bemused", 1)
                ch_e "I'll try it. . ."
            else:
                ch_e "Yeah, I like that one too."
        else:

            if Shame >= 50:
                $ Girl.change_face("angry", 1)
                ch_e "You have GOT to be kidding me here."
            elif Shame >= 25:
                $ Girl.change_face("angry", 1)
                ch_e "This is just between us."
            else:
                $ Girl.change_face("bemused", 1)
                ch_e "I can't wear this out!"
    elif Girl == LauraX:
        if Agree:
            if "exhibitionist" in Girl.traits:
                ch_l "Mmmmmm. . ."
            elif Shame >= 50:
                ch_l "This is. . . really brave. . ."
            elif Shame >= 25:
                ch_l "This one's pretty skimpy. . ."
            elif Shame >= 15:
                $ Girl.change_face("bemused", 1)
                ch_l "Yeah, ok. . ."
            else:
                ch_l "Yup."
        else:

            if Shame >= 50:
                $ Girl.change_face("angry", 1)
                ch_l "Perv."
            elif Shame >= 25:
                $ Girl.change_face("angry", 1)
                ch_l "Yeah, not in public."
            else:
                $ Girl.change_face("bemused", 1)
                ch_l "Nah."
    elif Girl == JeanX:
        if Agree:
            if "exhibitionist" in Girl.traits:
                ch_j ". . ."
            elif Shame >= 50:
                ch_j "Pretty daring. . ."
            elif Shame >= 25:
                ch_j "Kinda skimpy. . ."
            elif Shame >= 15:
                $ Girl.change_face("bemused", 1)
                ch_j "Sure, whatever. . ."
            else:
                ch_j "Sure."
        else:

            if Shame >= 50:
                $ Girl.change_face("angry", 1)
                ch_j "Gross."
            elif Shame >= 25:
                $ Girl.change_face("angry", 1)
                ch_j "You wish."
            else:
                $ Girl.change_face("bemused", 1)
                ch_j "No way."
    elif Girl == StormX:
        $ Girl.change_face("bemused", 1)
        if Agree:
            if "exhibitionist" in Girl.traits:
                ch_s "Oooh. . ."
            elif Shame >= 25:
                ch_s "You are going to get me into trouble. . ."
            else:
                ch_s "Yes, this will do nicely."
        else:

            $ Girl.change_face("bemused", 1)
            ch_s "I am afraid cannot wear this out."
    elif Girl == JubesX:
        $ Girl.change_face("bemused", 1)
        if Agree:
            if "exhibitionist" in Girl.traits:
                ch_s "Oooh. . ."
            elif Shame >= 25:
                ch_s "Whew, this is flat out pornographic. . ."
            else:
                ch_s "Oh, yeah, this'll do. . ."
        else:

            $ Girl.change_face("bemused", 1)
            ch_s "I really can't wear this one out. . ."
    return



label outfitShame(Girl, Custom = 3, Check=0, Count=0, Tempshame=50, Agree = 1):
    if not Check and not taboo and not Girl.taboo and Custom != 20:
        if Girl.clothing[9] and Player.location in bedrooms:
            if "halloween" not in Player.daily_history:
                call Private_outfit(Girl)
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

    if Girl.Clothes["piercings"] and Count <= 10:
        $ Count = -5

    $ Girl.change_face("sexy", 0)
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
            $ Girl.change_face("bemused", 1)
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
            $ Girl.change_face("bemused", 1)
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
            $ Girl.change_face("bemused", 1)
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
            $ Girl.change_face("bemused", 1)
            ch_l "I wouldn't go out with my tits out."
    elif Girl == JeanX:
        if Count >= 10:
            ch_j "You must really enjoy these tits. . ."
        elif Count >= 5:
            ch_j "I've kinda got my tits out here. . ."
        elif (approval_check(Girl, 2700, taboo_modifier=0) or approval_check(Girl, 950, "I", taboo_modifier=0)):
            ch_j ". . ."
        else:
            $ Girl.change_face("bemused", 1)
            ch_j "You think I'd go out with my tits on display?"
    elif Girl == StormX:
        if Count >= 10:
            ch_s "A lovely choice for the top."
        elif Count >= 5:
            if StormX not in Rules:
                ch_s "I do typically cover more than this around the school."
            else:
                $ Girl.change_face("bemused", 1)
                ch_s "I'm not sure Charles would approve of this top."
        elif (approval_check(Girl, 2700, taboo_modifier=0) or approval_check(Girl, 950, "I", taboo_modifier=0)):
            ch_s "Aren't my assets a bit. . . exposed here?"
        else:
            $ Girl.change_face("bemused", 1)
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
            $ Girl.change_face("bemused", 1)
            ch_v "Well, I wouldn't go anywhere with my tits out like this. . ."

    $ Tempshame -= Count
    $ Count = 0

    if Girl.Clothes["bottom"] and Girl.Clothes["underwear"]:
        $ Count = 30
    else:
        if Girl.bottom_number() > 5:

            $ Count = 25
        elif Girl.wearing_skirt:

            $ Count = 20
        elif Girl.Clothes["underwear"] in ["sports_panties", "shorts"]:

            $ Count = 25
        elif Girl.underwear_number() >= 6:

            $ Count = 15
        elif Girl.underwear_number() >= 4:

            $ Count = 10
        elif Girl.underwear_number() >= 2:

            $ Count = 5


        if Girl.Clothes["hose"] == "tights":

            $ Count = 25 if Count < 25 else Count

        if Girl.Clothes["top"] == "towel" and Count:

            $ Count = 25
        elif Girl.Clothes["top"] == "towel":

            $ Count = 15
    if not Check:

        pass
    elif Custom == 9 or Custom == 7:
        pass
    elif Girl == RogueX:
        if Count >= 20:
            if Girl.wearing_pants:
                ch_r "Oh, I think these pants will work fine."
            elif Girl.wearing_skirt:
                ch_r "Oh, I think this skirt will work fine."
            elif Girl.Clothes["hose"] == "tights":
                ch_r "Oh, these [Girl.Clothes[hose].name] will work."
            elif Girl.Clothes["underwear"] == "shorts":
                ch_r "Oh, I think these shorts will work fine."
            elif Girl.Clothes["top"] == "towel":
                ch_r "The towel's an odd choice. . ."
            else:
                ch_r "Kinda breezy across my nethers, [Girl.player_petname]. . ."
            if not Girl.Clothes["underwear"] and approval_check(Girl, 500, "I", taboo_modifier=0):
                ch_r "I kinda like going commando."
            elif not Girl.Clothes["underwear"]:
                ch_r "Don't know about going commando though."
        elif Count >= 10 and (approval_check(Girl, 2000, taboo_modifier=0) or approval_check(Girl, 700, "I", taboo_modifier=0)):
            ch_r "These don't really leave much to the imagination. . ."
        elif Count >= 10:
            $ Girl.change_face("angry", 1)
            ch_r "I'm warning you, I'm not running around in my panties. . ."
        elif (approval_check(Girl, 2500, taboo_modifier=0) or approval_check(Girl, 800, "I", taboo_modifier=0)):
            ch_r "Hmm, Breezy. . ."
        else:
            ch_r "So long as we stay inside. . ."
    elif Girl == KittyX:
        if Count >= 20:
            if Girl.bottom_number() >= 5:
                ch_k "and these pants look cute on me."
            elif Girl.Clothes["bottom"] == "shorts":
                ch_k "and these are cute shorts."
            elif Girl.Clothes["hose"] == "tights":
                ch_k "I guess these [Girl.Clothes[hose].name] will work fine."
            elif Girl.Clothes["top"] == "towel":
                ch_k "The towel's an odd choice. . ."
            else:
                ch_k "This is kinda breezy."
            if not Girl.Clothes["underwear"] and approval_check(Girl, 500, "I", taboo_modifier=0):
                ch_k "I like going without panties."
            elif not Girl.Clothes["underwear"]:
                ch_k "It's a little uncomfortable without panties."
        elif Count >= 10 and (approval_check(Girl, 2000, taboo_modifier=0) or approval_check(Girl, 700, "I", taboo_modifier=0)):
            ch_k "I'm not sure about the coverage down here. . ."
        elif Count >= 10:
            $ Girl.change_face("angry", 1)
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
            elif Girl.Clothes["hose"] == "tights":
                ch_e "I guess these [Girl.Clothes[hose].name] will work fine."
            elif Girl.Clothes["top"] == "towel":
                ch_e "I'm unsure about wearing a towel out, [Girl.player_petname]. . ."
            else:
                ch_e "I probably could wear something more downstairs, [Girl.player_petname]. . ."
            if not Girl.Clothes["underwear"]:
                if approval_check(Girl, 500, "I", taboo_modifier=0):
                    ch_e "I do enjoy going without panties."
                else:
                    ch_e "I don't know about going without panties in this situation."
        elif Count >= 10:
            if approval_check(Girl, 2000, taboo_modifier=0) or approval_check(Girl, 700, "I", taboo_modifier=0):
                ch_e "I hope you don't expect me to wear this out. . ."
            else:
                $ Girl.change_face("angry", 1)
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
            elif Girl.Clothes["hose"] == "tights":
                ch_l "and these [Girl.Clothes[hose].name] will work fine."
            elif Girl.Clothes["top"] == "towel":
                ch_l "The towel's an odd choice. . ."
            else:
                ch_l "but there's a draft."
            if not Girl.Clothes["underwear"] and approval_check(Girl, 500, "I", taboo_modifier=0):
                ch_l "Commando's cool."
            elif not Girl.Clothes["underwear"]:
                ch_l "I might accidentally flash some people like this though."
        elif Count >= 10 and (approval_check(Girl, 2000, taboo_modifier=0) or approval_check(Girl, 700, "I", taboo_modifier=0)):
            ch_l "I don't think I'm fully covered. . ."
        elif Count >= 10:
            $ Girl.change_face("angry", 1)
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
            elif Girl.Clothes["hose"] == "tights":
                ch_j "these [Girl.Clothes[hose].name] will work fine."
            elif Girl.Clothes["top"] == "towel":
                ch_j "A towel though? . ."
            else:
                ch_j "kinda exposed here. . ."
            if not Girl.Clothes["underwear"] and approval_check(Girl, 500, "I", taboo_modifier=0):
                ch_j "I don't mind doing without the panties. . ."
            elif not Girl.Clothes["underwear"]:
                ch_j "I'd kinda need panties with this. . ."


        elif Count >= 10:
            if (approval_check(Girl, 2000, taboo_modifier=0) or approval_check(Girl, 700, "I", taboo_modifier=0)):
                $ Girl.change_face("sly", 1)
            else:
                $ Girl.change_face("angry", 1)
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
        elif Girl.Clothes["hose"] == "tights":
            ch_s "I supposed that these [Girl.Clothes[hose].name] will work fine."
        elif Girl.Clothes["top"] == "towel":
            ch_s "I'm unsure about wearing a towel out, [Girl.player_petname]. . ."
        else:
            ch_s "A rather breezy ensemble, [Girl.player_petname]. . ."
        if not Girl.Clothes["underwear"]:
            if approval_check(Girl, 500, "I", taboo_modifier=0):
                ch_s "I do enjoy doing without panties."
            else:
                ch_s "Certainly quite exposed without panties. . ."
        if Count >= 10 and StormX not in Rules:
            $ Girl.change_face("bemused", 1)
            ch_s "I don't know that Charles would let me roam the halls in such an exposed state."
        elif StormX in Rules and (approval_check(Girl, 1200, taboo_modifier=0) or approval_check(Girl, 500, "I", taboo_modifier=0)):
            ch_s "This is quite the daring look you've put together."
        else:
            ch_s "I doubt Charles would let me roam the halls in such an exposed state."
    elif Girl == JubesX:
        if Count >= 20:
            if Girl.wearing_pants:
                ch_v "and these pants work."
            elif Girl.wearing_pants:
                ch_v "and these shorts work."
            elif Girl.bottom_number() >= 5:
                ch_v "and this skirt works."
            elif Girl.Clothes["hose"] == "tights":
                ch_v "and these [Girl.Clothes[hose].name] will work fine."
            elif Girl.Clothes["top"] == "towel":
                ch_v "The towel's an odd choice. . ."
            else:
                ch_v "but I don't know about this. . ."
            if not Girl.Clothes["underwear"] and approval_check(Girl, 500, "I", taboo_modifier=0):
                ch_v "I guess we're not doing panties now?"
            elif not Girl.Clothes["underwear"]:
                ch_v "I don't think I'd want to go without panties. . ."
        elif Count >= 10 and (approval_check(Girl, 2000, taboo_modifier=0) or approval_check(Girl, 700, "I", taboo_modifier=0)):
            ch_v "This is pretty skimpy. . ."
        elif Count >= 10:
            $ Girl.change_face("angry", 1)
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

        $ Girl.change_face("sexy", 0)
        if Girl.Clothes["bottom"]:
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
        elif Girl.Clothes["top"]:
            pass
        elif Girl.bra_number() > 2 and (Girl.seen_breasts or approval_check(Girl, 900, taboo_modifier=0)):
            pass
        elif Girl.seen_breasts or approval_check(Girl, 1200, taboo_modifier=0):
            pass
        else:
            $ Agree = 0

        if Check == 2 and Agree:
            $ Girl.change_face("sly")
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

            $ Girl.change_face("bemused", 2, eyes = "side")
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
                    $ Girl.change_Outfit()
                    hide dress_screen
                "Ok, we can keep tweaking it.":
                    pass
            $ Girl.change_face("smile", 1)
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
                $ Girl.change_face("confused", 1)
                $ Girl.mouth = "smile"
                ch_r "It's a little late to worry about that, right?"
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                ch_r "Hmm. . . yeah, I'd love to. . ."
                call change_Girl_stat(Girl, "lust", 10)
            elif Custom == 7:

                $ Girl.change_face("bemused", 1)
                if Tempshame >= 30:
                    ch_r "A bit scandalous, but yeah."
                elif Tempshame >= 15:
                    ch_r "Yeah, you're worth it."
                else:
                    ch_r "Sure, it's cute."
            elif Tempshame <= 5:
                $ Girl.change_face("smile")
                ch_r "Yeah, I think I like this style, I'd wear this."
            elif Tempshame <= 15:
                if approval_check(Girl, 1700, taboo_modifier=0, cologne = 0) or approval_check(Girl, 400, "I", taboo_modifier=0, cologne = 0):
                    ch_r "It's pretty skimpy, but I can make it work."
                else:
                    $ Girl.change_face("bemused", 1)
                    ch_r "I think this looks is a bit daring to wear."
                    $ Agree = 0
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("bemused", 1)
                ch_r "Sure, I can swim in this. . ."
            elif Tempshame <= 25:
                if approval_check(Girl, 2300, taboo_modifier=0, cologne = 0) or approval_check(Girl, 700, "I", taboo_modifier=0, cologne = 0):
                    ch_r "Kinky, but I can rock this."
                else:
                    $ Girl.change_face("angry", 1)
                    ch_r "I'm definitely not going out in this."
                    $ Agree = 0
            elif approval_check(Girl, 2500, taboo_modifier=0, cologne = 0) or approval_check(Girl, 800, "I", taboo_modifier=0, cologne = 0):
                $ Girl.change_face("bemused", 1)
                ch_r "I can't believe it. . . but yeah."
            else:
                $ Girl.change_face("angry", 1)
                ch_r "You have got to be kidding."
                $ Agree = 0
        elif Girl == KittyX:
            if Girl.taboo >= 40:
                $ Girl.change_face("confused", 1)
                $ Girl.mouth = "smile"
                ch_k "Kinda late to ask, right?"
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                ch_k "I'm getting wet just thinking about it. . ."
                call change_Girl_stat(Girl, "lust", 10)
            elif Tempshame <= 5:
                $ Girl.change_face("smile")
                ch_k "Sure, it's a cute look!"
            elif Tempshame <= 15 and (approval_check(Girl, 1700, taboo_modifier=0, cologne = 0) or approval_check(Girl, 400, "I", taboo_modifier=0, cologne = 0)):
                ch_k "It's pretty hot, right?"
            elif Custom == 7:

                $ Girl.change_face("bemused", 1)
                if Tempshame >= 30:
                    ch_k "This is[Girl.like]pretty exposed, but ok."
                elif Tempshame >= 15:
                    ch_k "It's kinda naughty, I like it."
                else:
                    ch_k "Yeah, these are fine."
            elif Tempshame <= 15:
                $ Girl.change_face("bemused", 1)
                ch_k "It's too slutty to wear out."
                $ Agree = 0
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("bemused", 1)
                ch_k "This is a cute swimsuit. . ."
            elif Tempshame <= 25 and (approval_check(Girl, 2300, taboo_modifier=0, cologne = 0) or approval_check(Girl, 700, "I", taboo_modifier=0, cologne = 0)):
                ch_k "So sexy, but I can handle it."
            elif Tempshame <= 25:
                $ Girl.change_face("angry", 1)
                ch_k "{i}Way{/i} too sexy for outside."
                $ Agree = 0
            elif (approval_check(Girl, 2500, taboo_modifier=0, cologne = 0) or approval_check(Girl, 800, "I", taboo_modifier=0, cologne = 0)):
                $ Girl.change_face("bemused", 1)
                ch_k "OMG, I can't believe I'm doing this."
            else:
                $ Girl.change_face("angry", 1)
                ch_k "I - can't - even."
                $ Agree = 0
        elif Girl == EmmaX:
            if Girl.taboo >= 40:
                $ Girl.change_face("confused", 1)
                $ Girl.mouth = "smile"
                "She glances around."
                ch_e "Is that a trick question?"
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                ch_e "The thought of it gets me moist. . ."
                call change_Girl_stat(Girl, "lust", 10)
            elif Tempshame <= 5:
                $ Girl.change_face("smile")
                ch_e "Yes, it's a fine choice."
            elif Tempshame <= 15 and (approval_check(Girl, 1700, taboo_modifier=0, cologne = 0) or approval_check(Girl, 400, "I", taboo_modifier=0, cologne = 0)):
                ch_e "Rather daring, how could I resist?"
            elif Custom == 7:

                $ Girl.change_face("bemused", 1)
                if Tempshame >= 30:
                    ch_e "You understand I only wear this sort of thing in private."
                else:
                    ch_e "It is a comfortable outfit."
            elif Tempshame <= 15:
                $ Girl.change_face("bemused", 1)
                ch_e "Rather too daring, don't you think?"
                $ Agree = 0
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("bemused", 1)
                ch_e "Fine, this is decent swimwear. . ."
            elif Tempshame >= 15 and "public" not in Girl.history:
                ch_e "I doubt I could get away with this in public, [Girl.player_petname]."
                $ Agree = 0
            elif Tempshame <= 25 and (approval_check(Girl, 2300, taboo_modifier=0, cologne = 0) or approval_check(Girl, 700, "I", taboo_modifier=0, cologne = 0)):
                ch_e "This is particularly inappropriate. . . in the best ways."
            elif Tempshame <= 25:
                $ Girl.change_face("angry", 1)
                ch_e "I don't believe even I could pull off this look, [Girl.player_petname]."
                $ Agree = 0
            elif (approval_check(Girl, 2500, taboo_modifier=0, cologne = 0) or approval_check(Girl, 800, "I", taboo_modifier=0, cologne = 0)):
                $ Girl.change_face("bemused", 1)
                ch_e "This look certainly pushes the boundaries."
            else:
                $ Girl.change_face("angry", 1)
                ch_e "Even I can't pull this off."
                $ Agree = 0
        elif Girl == LauraX:
            if Girl.taboo >= 40:
                $ Girl.change_face("confused", 1)
                $ Girl.mouth = "smile"
                ch_l "Well a bit late for that, I guess."
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                call change_Girl_stat(Girl, "lust", 10)
                $ Girl.change_face("sexy", 2)
                ch_l ". . ."
                $ Girl.change_face("sexy", 1)
            elif Tempshame <= 5:
                $ Girl.change_face("smile")
                ch_l "I don't see why not."
            elif Tempshame <= 15 and (approval_check(Girl, 1700, taboo_modifier=0, cologne = 0) or approval_check(Girl, 400, "I", taboo_modifier=0, cologne = 0)):
                ch_l "It looks good, right?"
            elif Custom == 7:

                $ Girl.change_face("bemused", 1)
                if Tempshame >= 30:
                    ch_l "Sure, perv."
                elif Tempshame >= 15:
                    ch_l "Sure, why not."
                else:
                    ch_l "Yeah, I guess."
            elif Tempshame <= 15:
                $ Girl.change_face("bemused", 1)
                ch_l "I can't move freely in this without showing off the goods."
                $ Agree = 0
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("bemused", 1)
                ch_l "Yeah, I can swim in this. . ."
            elif Tempshame <= 25 and (approval_check(Girl, 2300, taboo_modifier=0, cologne = 0) or approval_check(Girl, 700, "I", taboo_modifier=0, cologne = 0)):
                ch_l "I can handle this."
            elif Tempshame <= 25:
                $ Girl.change_face("angry", 1)
                ch_l "Nah, too slutty."
                $ Agree = 0
            elif (approval_check(Girl, 2500, taboo_modifier=0, cologne = 0) or approval_check(Girl, 800, "I", taboo_modifier=0, cologne = 0)):
                $ Girl.change_face("bemused", 1)
                ch_l "Pretty daring, eh?"
            else:
                $ Girl.change_face("angry", 1)
                ch_l "As if."
                $ Agree = 0
        elif Girl == JeanX:
            if Girl.taboo >= 40:
                $ Girl.change_face("confused", 1)
                $ Girl.mouth = "smile"
                ch_j "Well, I guess so, right?"
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                call change_Girl_stat(Girl, "lust", 10)
                $ Girl.change_face("sexy", 2)
                ch_j ". . ."
                $ Girl.change_face("sexy", 1)
            elif Tempshame <= 5:
                $ Girl.change_face("smile")
                ch_j "Sure, whatever."
            elif Tempshame <= 15 and (approval_check(Girl, 1700, taboo_modifier=0, cologne = 0) or approval_check(Girl, 400, "I", taboo_modifier=0, cologne = 0)):
                ch_j "I almost have to. . ."
            elif Custom == 7:

                $ Girl.change_face("bemused", 1)
                if Tempshame >= 30:
                    ch_j "If it'll keep you hard. . ."
                elif Tempshame >= 15:
                    ch_j "Yeah, sure."
                else:
                    ch_j "Why not."
            elif Tempshame <= 15:
                $ Girl.change_face("bemused", 1)
                ch_j "I can pull this one off. . ."
                $ Agree = 0
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("bemused", 1)
                ch_j "Yeah, sure."
            elif Tempshame <= 25 and (approval_check(Girl, 2300, taboo_modifier=0, cologne = 0) or approval_check(Girl, 700, "I", taboo_modifier=0, cologne = 0)):
                ch_j "This'll turn some heads. . ."
            elif Tempshame <= 25:
                $ Girl.change_face("angry", 1)
                ch_j "I wouldn't want to break anyone. . ."
                $ Agree = 0
            elif (approval_check(Girl, 2500, taboo_modifier=0, cologne = 0) or approval_check(Girl, 800, "I", taboo_modifier=0, cologne = 0)):
                $ Girl.change_face("bemused", 1)
                ch_j "Kinky, but sure."
            else:
                $ Girl.change_face("angry", 1)
                ch_j "You have to be joking."
                $ Agree = 0
        elif Girl == StormX:

            if Girl.taboo >= 40:
                $ Girl.change_face("confused", 1)
                $ Girl.mouth = "smile"
                "She glances around."
                ch_s "It seems a bit late for that question. . ."
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                ch_s "I do find the idea. . . exciting. . ."
                call change_Girl_stat(Girl, "lust", 10)
            elif Tempshame <= 10:
                $ Girl.change_face("smile")
                ch_s "Yes, it's a fine choice."
            elif Custom == 7:

                $ Girl.change_face("bemused", 1)
                if Tempshame >= 20:
                    ch_s "This is a fine outfit."
                else:
                    ch_s "It may be a bit more than I'm used to. . ."
            elif StormX in Rules:
                ch_s "I don't see why not. . ."
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("bemused", 1)
                ch_s "I suppose I could swim well like this. . ."
            elif Tempshame <= 20 and (approval_check(Girl, 1700, taboo_modifier=0, cologne = 0) or approval_check(Girl, 400, "I", taboo_modifier=0, cologne = 0)):
                ch_s "This certainly does push the limits of good taste. . ."
            elif Tempshame <= 25 and (approval_check(Girl, 2300, taboo_modifier=0, cologne = 0) or approval_check(Girl, 700, "I", taboo_modifier=0, cologne = 0)):
                $ Girl.change_face("bemused", 1)
                ch_s "I doubt Charles would approve, but so what?"
            elif Tempshame <= 25:
                $ Girl.change_face("bemused", 1)
                ch_s "I'm afraid that Charles would never approve."
                $ Agree = 0
            elif (approval_check(Girl, 2500, taboo_modifier=0, cologne = 0) or approval_check(Girl, 800, "I", taboo_modifier=0, cologne = 0)):
                $ Girl.change_face("bemused", 1)
                ch_s "I doubt Charles would approve, but so what?"
            else:
                $ Girl.change_face("bemused", 1)
                ch_s "I'm afraid that Charles would never approve."
                $ Agree = 0
        elif Girl == JubesX:
            if Girl.taboo >= 40:
                $ Girl.change_face("confused", 1)
                $ Girl.mouth = "smile"
                ch_v "I guess that ship has sailed. . ."
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                call change_Girl_stat(Girl, "lust", 10)
                $ Girl.change_face("sexy", 2)
                ch_v ". . ."
                $ Girl.change_face("sexy", 1)
            elif Tempshame <= 5:
                $ Girl.change_face("smile")
                ch_v "I guess?"
            elif Tempshame <= 15 and (approval_check(Girl, 1700, taboo_modifier=0, cologne = 0) or approval_check(Girl, 400, "I", taboo_modifier=0, cologne = 0)):
                ch_v "It looks totally hot, right?"
            elif Custom == 7:

                $ Girl.change_face("bemused", 1)
                if Tempshame >= 30:
                    ch_v "Whatever, perv."
                elif Tempshame >= 15:
                    ch_v "Sure, why not."
                else:
                    ch_v "Sure, I guess."
            elif Tempshame <= 15:
                $ Girl.change_face("bemused", 1)
                ch_v "I think this is too breezy."
                $ Agree = 0
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("bemused", 1)
                ch_v "I could swim in this. . ."
            elif Tempshame <= 25 and (approval_check(Girl, 2300, taboo_modifier=0, cologne = 0) or approval_check(Girl, 700, "I", taboo_modifier=0, cologne = 0)):
                ch_v "I guess this is fine. . ."
            elif Tempshame <= 25:
                $ Girl.change_face("angry", 1)
                ch_v "I really couldn't wear this out."
                $ Agree = 0
            elif (approval_check(Girl, 2500, taboo_modifier=0, cologne = 0) or approval_check(Girl, 800, "I", taboo_modifier=0, cologne = 0)):
                $ Girl.change_face("bemused", 1)
                ch_v "It's pretty hot, right?"
            else:
                $ Girl.change_face("angry", 1)
                ch_v "As if."
                $ Agree = 0



        if Custom == 5:
            $ Girl.second_custom_outfit = Girl.outfit.copy()
            $ Girl.second_custom_outfit["shame"] = Tempshame
            $ Girl.second_custom_outfit["outfit_active"] = 2 if Agree else 1
        elif Custom == 6:
            $ Girl.third_custom_outfit = Girl.outfit.copy()
            $ Girl.third_custom_outfit["shame"] = Tempshame
            $ Girl.third_custom_outfit["outfit_active"] = 2 if Agree else 1
        elif Custom == 4:
            if Agree:
                $ Girl.gym_clothes = Girl.outfit.copy()
                $ Girl.gym_clothes["shame"] = Tempshame
        elif Custom == 7:
            $ Girl.sleepwear = Girl.outfit.copy()
            $ Girl.sleepwear["shame"] = Tempshame
            $ Girl.sleepwear["outfit_active"] = 2 if Agree else 1
        elif Custom == 10:
            if Agree:
                $ Girl.swimwear = Girl.outfit.copy()
                $ Girl.swimwear["shame"] = Tempshame
        elif Custom == 3:
            $ Girl.first_custom_outfit = Girl.outfit.copy()
            $ Girl.first_custom_outfit["shame"] = Tempshame
            $ Girl.first_custom_outfit["outfit_active"] = 2 if Agree else 1
        else:
            "Tell Oni Custom outfit was [Custom]"
            $ RogueX.gibberish = 5
    elif Girl.taboo <= 20:

        $ Tempshame /= 2

    $ Girl.Clothes["shame"] = Tempshame

    if Custom == 20:

        return

    if Check:
        pass
    elif Player.location == "bg_halloween" or (Player.location == "bg_player" and "halloween" in Player.daily_history):

        pass
    elif "exhibitionist" in Girl.traits and Tempshame <= 20:

        pass
    elif Girl == StormX and StormX in Rules:
        pass
    elif Tempshame <= 12:

        pass
    elif Girl.Clothes["top"] == "towel" and Girl.location == "bg_shower":

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
        $ Girl.change_Outfit("gym_clothes")
    elif not Girl.taboo:
        pass
    elif Girl.outfit_name == "swimwear" and Player.location == "bg_pool":
        pass
    elif Player.location == "bg_pool" and Girl.bra_number() >= 3 and Girl.underwear_number() >= 6:
        pass
    elif Girl.outfit_name == "gym_clothes" and Player.location == "bg_dangerroom":
        pass
    else:

        if Girl.location == Player.location:
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
            $ Girl.outfit_name = renpy.random.choice(["default", "second_casual"])

        $ Girl.add_word(1, "modesty", "modesty")
        $ Girl.wet = False
        $ Girl.change_Outfit()
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
