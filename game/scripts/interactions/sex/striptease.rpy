label top_off(Girl, context = 1):
    $ shift_focus(Girl)

    if "angry" in Girl.recent_history:
        if Girl == RogueX:
            ch_r "I'm just too annoyed to deal with this right now."
        elif Girl == KittyX:
            ch_k "No titties for you."
        elif Girl == EmmaX:
            ch_e "I'm in no mood, [Girl.player_petname]."
        elif Girl == LauraX:
            ch_l "Don't push it, [Girl.player_petname]."
        elif Girl == JeanX:
            ch_j "No way, [Girl.player_petname]."
        elif Girl == StormX:
            ch_s "These are not for your enjoyment."
        elif Girl == JubesX:
            ch_v "The top stays on. . ."

        return

    if Girl.seen_breasts and approval_check(Girl, 500) and not taboo:
        $ approval_bonus += 20

    if "exhibitionist" in Girl.traits:
        $ approval_bonus += 4*taboo

    if Girl in Player.Harem or "sex friend" in Girl.player_petnames and not taboo:
        $ approval_bonus += 10
    elif "ex" in Girl.traits:
        $ approval_bonus -= 40

    if "no_topless" in Girl.recent_history:
        $ approval_bonus -= 10
    elif Girl == StormX and (not taboo or Girl in Rules):
        $ approval_bonus += 20

    if context and not Girl.top_pulled_up:
        if context == 2:
            if Girl == RogueX:
                ch_r "I don't know, you'd have to touch them. . ."
            elif Girl == KittyX:
                ch_k "So, you'd have to be able to[KittyX.like]touch them, I guess. . ."
            elif Girl == EmmaX:
                ch_e "I would probably need to be bare-chested to get anything out of that. . ."
            elif Girl == LauraX:
                ch_l "I'd need to be topless to get anything from that. . ."
            elif Girl == JeanX:
                ch_j "I guess I'd have to go topless. . ."
            elif Girl == StormX:
                ch_s "If direct contact is necessary. . ."
            elif Girl == JubesX:
                ch_v "Well, I'd need to be topless for that to. . ."
        else:
            if Girl.Clothes["top"]:
                ch_p "This might be easier without your [Girl.Clothes[top].name] on."
            elif Girl.Clothes["bra"]:
                ch_p "This might be easier without your [Girl.Clothes[bra].name] on."

    $ approval = approval_check(Girl, 1100, taboo_modifier = 4)

    if action_context == "auto" and Girl.Outfit.breasts_covered:
        $ line = 0

        if approval_check(Girl, 1250, taboo_modifier = 1) or (Girl.seen_breasts and approval_check(Girl, 500) and not taboo):
            call change_Girl_stat(Girl, "inhibition", 1)

            $ Girl.expose_breasts()

            "[Girl.name] sighs in frustration."

            if Girl == RogueX:
                ch_r "I just wasn't getting much out of it that way."
            elif Girl == KittyX:
                ch_k "I[Girl.like]wasn't feeling it that way."
            elif Girl == EmmaX:
                ch_e "Sometimes only direct contact will do."
            elif Girl == LauraX:
                ch_l "That wasn't working out."
            elif Girl == JeanX:
                ch_j "Ok, try that now, [Girl.player_petname]."
            elif Girl == StormX:
                ch_s "Does that work better?"
            elif Girl == JubesX:
                ch_v "Ok, that's more comfortable. . ."

            if taboo:
                call change_Girl_stat(Girl, "inhibition", (int(taboo/20)))

            call expression Girl.tag + "_First_Topless" pass (1)
        elif Girl.Clothes["top"] and Girl.Clothes["bra"] and approval_check(Girl, 800, taboo_modifier = 1):
            call change_Girl_stat(Girl, "inhibition", 1)

            if Girl.Clothes["jacket"]:
                $ Girl.take_off("jacket")

            $ Girl.take_off("top")

            "[Girl.name] sighs in frustration."

            if Girl == RogueX:
                ch_r "I just wasn't getting much out of it that way."
            elif Girl == KittyX:
                ch_k "I[Girl.like]wasn't feeling it that way."
            elif Girl == EmmaX:
                ch_e "I just wasn't getting much out of it that way."
            elif Girl == LauraX:
                ch_l "That wasn't working out."
            elif Girl == JeanX:
                ch_j "Ok, try that now, [Girl.player_petname]."
            elif Girl == StormX:
                ch_s "Does that work better?"
            elif Girl == JubesX:
                ch_v "Ok, that's a bit better. . ."

        return

    if approval >= 2:
        if "no_topless" in Girl.daily_history:
            if Girl == RogueX:
                ch_r "Ok, fine, top off."
            elif Girl == KittyX:
                ch_k "Okay, okay!"
            elif Girl == EmmaX:
                ch_e "{i}Fine,{/i} if that will shut you up."
            elif Girl == LauraX:
                ch_l "{i}Fine,{/i} but don't think I'm getting soft on you."
            elif Girl == JeanX:
                ch_j "Oh, fine. . ."
            elif Girl == StormX:
                ch_s "Oh, if you insist. . ."
            elif Girl == JubesX:
                ch_v "Well if you insist. . ."

        $ Girl.change_face("sexy", 1)

        if Girl.forced:
            $ Girl.change_face("sad", 1)
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "obedience", 1)
            call change_Girl_stat(Girl, "inhibition", 1)

        call change_Girl_stat(Girl, "inhibition", 3)

        $ done = False

        while Girl.Outfit.breasts_covered and not done:
            if Girl == RogueX:
                ch_r "So, [Girl.player_petname]. Did you want me to take my top off?"
            elif Girl == KittyX:
                ch_k "So[Girl.like]how much did you want me to take off?"
            elif Girl == EmmaX:
                ch_e "What was it you were interested in, [Girl.player_petname]?"
            elif Girl == LauraX:
                ch_l "What did you want to see, [Girl.player_petname]?"
            elif Girl == JeanX:
                ch_j "Oh, what were you looking to see, [Girl.player_petname]."
            elif Girl == StormX:
                ch_s "What should I remove?"
            elif Girl == JubesX:
                ch_v "Ok then, so what did you want off?"

            menu:
                extend ""
                "Why don't you lose the jacket?" if Girl.Clothes["jacket"]:
                    $ Girl.take_off("jacket")
                "Lose the [Girl.Clothes[top].name]." if Girl.Clothes["top"]:
                    $ Girl.change_face("bemused", 1)
                    $ Girl.take_off("top")
                "Why don't you lose the [Girl.Clothes[neck].name]?" if Girl.Clothes["neck"]:
                    $ Girl.take_off("neck")
                "Just lose the [Girl.Clothes[bra].name]." if Girl.Clothes["top"] and Girl.Clothes["bra"]:
                    $ Girl.change_face("bemused", 1)
                    $ Girl.take_off("bra")
                "Lose the [Girl.Clothes[bra].name]." if not Girl.Clothes["top"] and Girl.Clothes["bra"]:
                    $ Girl.change_face("bemused", 1)
                    $ Girl.take_off("bra")
                "Just pull it up." if Girl.Outfit.breasts_covered:
                    $ Girl.change_face("bemused", 1)

                    $ Girl.expose_breasts()
                "Lose it all." if Girl.Clothes["top"] and Girl.Clothes["bra"]:
                    $ Girl.change_face("bemused", 1)
                    $ Girl.take_off("jacket")
                    $ Girl.take_off("top")
                    $ Girl.take_off("bra")
                "Lose the [Girl.Clothes[gloves].name]. . ." if Girl.Clothes["gloves"]:
                    $ Girl.change_face("sexy")
                    $ Girl.take_off("gloves")
                "Why don't you lose the [Girl.Clothes[suspenders].name]?" if Girl.Clothes["suspenders"]:
                    $ Girl.take_off("suspenders")
                "Why don't you lose the [Girl.Clothes[sleeves].name]?" if Girl.Clothes["sleeves"]:
                    $ Girl.take_off("sleeves")
                "Why don't you lose the [Girl.Clothes[face_outer_accessory].name]?" if Girl.Clothes["face_outer_accessory"]:
                    $ Girl.take_off("face_outer_accessory")
                "That's enough.":
                    $ Girl.change_face("bemused", 1)

                    Girl.voice "All right, [Girl.player_petname]."

                    $ done = True

        if not Girl.Outfit.breasts_hidden:
            call change_Girl_stat(Girl, "obedience", 1)
            call change_Girl_stat(Girl, "obedience", 1)
            call expression Girl.tag + "_First_Topless"

        call change_Girl_stat(Girl, "lust", 3)

        $ Girl.recent_history.append("ask topless")
        $ Girl.daily_history.append("ask topless")

        return

    $ Girl.change_face("bemused", 1)

    if Girl == RogueX:
        if context == "massage" and not approval:
            ch_r "I'm ok with a massage, but my top stays on."
        elif "no_topless" in Girl.recent_history:
            $ Girl.change_face("angry")

            ch_r "I just told you no, [Girl.player_petname]."
        elif approval and not Girl.seen_breasts:
            ch_r "I'd like to leave something to the imagination. . ."
        elif not Girl.seen_breasts:
            ch_r "I'm not ready to show you those yet. . ."
        elif "no_topless" in Girl.daily_history:
            ch_r "I wasn't into it earlier, [Girl.player_petname], what's changed?"
        elif "ask topless" in Girl.recent_history:
            ch_r "Outfit_changed your mind, [Girl.player_petname]?"
        elif taboo:
            ch_r "It's a bit exposed here. . ."
        elif approval:
            ch_r "Well, you've seen them before, but. . ."
        else:
            ch_r "Not right now."
    elif Girl == KittyX:
        if context == "massage" and not approval:
            ch_k "A massage is fine, but I'm keeping my top on, ok?"
        elif "no_topless" in Girl.recent_history:
            $ Girl.change_face("angry")

            ch_k "I[Girl.like]already told you, no way!"
        elif approval and not Girl.seen_breasts:
            ch_k "I'm[Girl.like]not really comfortable with that."
        elif not Girl.seen_breasts:
            ch_k "I'd[Girl.like]really rather not, ok?"
        elif "no_topless" in Girl.daily_history:
            ch_k "Do you[Girl.like]think something's changed since earlier?"
        elif "ask topless" in Girl.recent_history:
            ch_k "Did you[Girl.like]want something else off?"
        elif taboo:
            ch_k "I'm[Girl.like]not that comfortable out here. . ."
        elif approval:
            ch_k "Maybe not?"
        else:
            ch_k "Nu-uh."
    elif Girl == EmmaX:
        if context == "massage" and not approval:
            ch_e "I welcome a massage, but I'm staying fully dressed."
        elif "no_topless" in Girl.recent_history:
            $ Girl.change_face("angry")

            ch_e "Learn from previous mistakes, [Girl.player_petname]."
        elif approval and not Girl.seen_breasts:
            ch_e "I don't know if that would be appropriate."
        elif not Girl.seen_breasts:
            ch_e "I don't think you're ready for that."
        elif "no_topless" in Girl.daily_history:
            ch_e "Are you still that obsessed?"
        elif "ask topless" in Girl.recent_history:
            ch_e "You want more?"
        elif taboo:
            ch_e "[Girl.player_petname], not around prying eyes."
        elif approval:
            ch_e "Are you sure you're prepared?"
        else:
            ch_e "No."
    elif Girl == LauraX:
        if context == "massage" and not approval:
            ch_l "I could use a massage, but I'm keeping my clothes on."
        elif "no_topless" in Girl.recent_history:
            $ Girl.change_face("angry")

            ch_l "Don't push it, [Girl.player_petname]."
        elif approval and not Girl.seen_breasts:
            ch_l "I don't know, man."
        elif not Girl.seen_breasts:
            ch_l "I really don't think so."
        elif "no_topless" in Girl.daily_history:
            ch_l "Dude, relax."
        elif "ask topless" in Girl.recent_history:
            ch_l "Again?"
        elif taboo:
            ch_l "[Girl.player_petname], not around here, alright?"
        elif approval:
            ch_l "Are you sure?"
        else:
            ch_l "No."
    elif Girl == JeanX:
        if context == "massage" and not approval:
            ch_j "Massage, yes, but top on."
        elif "no_topless" in Girl.recent_history:
            $ JeanX.change_face("angry")

            ch_j "Relax, [Girl.player_petname]."
        elif "no_topless" in Girl.daily_history:
            ch_j "Not happening."
        elif "ask topless" in Girl.recent_history:
            ch_j "So soon?"
        elif taboo:
            ch_j "Hmm. . . not around here"
        elif approval:
            ch_j "Hmm. . ."
        else:
            ch_j "No way."
    elif Girl == StormX:
        if context == "massage" and not approval:
            ch_s "I would enjoy a massage, but I'm staying fully clothed."
        elif "no_topless" in Girl.recent_history:
            $ Girl.change_face("angry")

            ch_s "I am not so pliable as that, [Girl.player_petname]."
        elif approval and not Girl.seen_breasts:
            ch_s "I don't know if that would be appropriate."
        elif "no_topless" in Girl.daily_history:
            ch_s "Do not ask again."
        elif "ask topless" in Girl.recent_history:
            ch_s "Oh, you'd like to see them again?"
        elif taboo and Girl not in Rules:
            ch_s "I'm afraid not in public, [Girl.player_petname]."
        elif approval:
            ch_s "Are you Certain?"
        else:
            ch_s "No."
    elif Girl == JubesX:
        if context == "massage" and not approval:
            ch_v "I could use a massage, but I'm keeping my clothes on."
        elif "no_topless" in Girl.recent_history:
            $ Girl.change_face("angry")

            ch_v "Don't push it, [Girl.player_petname]."
        elif approval and not Girl.seen_breasts:
            ch_v "I don't know, man."
        elif not Girl.seen_breasts:
            ch_v "I'm not cool with that."
        elif "no_topless" in Girl.daily_history:
            ch_v "Dude, relax."
        elif "ask topless" in Girl.recent_history:
            ch_v "Again?"
        elif taboo:
            ch_v "[Girl.player_petname], it's just public here?"
        elif approval:
            ch_v "I dunno, really?"
        else:
            ch_v "Nah."

    menu:
        extend ""
        "Sorry, sorry." if "no_topless" in Girl.recent_history:
            $ Girl.change_face("bemused", 1)

            if Girl == RogueX:
                ch_r "Ok, just. . . give it a rest, huh?"
            elif Girl == KittyX:
                ch_k "It's cool, I get it, but[Girl.like]chill out, huh?"
            elif Girl == EmmaX:
                ch_e "I can't blame you for your persistance, but learn from your errors."
            elif Girl == LauraX:
                ch_l "Right, I get it, stay thirsty."
            elif Girl == JeanX:
                ch_j "It's not like I can blame you, [Girl.player_petname]."
            elif Girl == StormX:
                ch_s "I cannot blame you."
            elif Girl == JubesX:
                ch_v "Well, you can't win if the don't play, right?"
        "Ok, that's fine." if "no_topless" not in Girl.recent_history:
            if "ask topless" not in Girl.daily_history:
                call change_Girl_stat(Girl, "lust", 3)
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "inhibition", 3)

            if Girl.forced:
                $ Girl.mouth = "smile"

                if Girl == RogueX:
                    ch_r "I really appreciate that."
                elif Girl == KittyX:
                    ch_k "That's[Girl.like]really cool of you."
                elif Girl == EmmaX:
                    ch_e "How. . . generous of you."
                elif Girl == LauraX:
                    ch_l "Ok."
                elif Girl == JeanX:
                    ch_j ". . ."
                elif Girl == StormX:
                    ch_s "Good."
                elif Girl == JubesX:
                    ch_v "Yeah, thanks. . ."

                if "ask topless" not in Girl.daily_history:
                    call change_Girl_stat(Girl, "love", 2)
                    call change_Girl_stat(Girl, "love", 2)
                    call change_Girl_stat(Girl, "inhibition", 1)
        "How about just the [Girl.Clothes[jacket].name]?" if Girl.Clothes["jacket"]:
            if Girl.Clothes["top"] or Girl.Clothes["jacket"].state:
                Girl.voice "Sure, I guess. . ."

                $ Girl.take_off("jacket")
            elif approval_check(Girl, 800, taboo_modifier = 2) and Girl.Clothes["bra"]:
                $ Girl.change_face("sexy")

                Girl.voice "Well, I guess. . ."

                $ Girl.change_face("bemused", 1)
                $ Girl.take_off("jacket")

                call change_Girl_stat(Girl, "obedience", 1)
                call change_Girl_stat(Girl, "inhibition", 2)
            elif not Girl.Clothes["top"] and not Girl.Clothes["bra"]:
                $ Girl.eyes = "surprised"
                $ Girl.blushing = "_blush2"

                Girl.voice "I kinda don't have anything under this. . ."

                call change_Girl_stat(Girl, "inhibition", 1)

                menu:
                    extend ""
                    "Ok, you can leave it on.":
                        $ Girl.mouth = "smile"

                        call change_Girl_stat(Girl, "love", 2)

                        Girl.voice "Whew, thanks. . ."
                    "That doesn't bother me any.":
                        if approval_check(Girl, 500, "I", taboo_modifier = 3) or approval_check(Girl, 1000, "LI", taboo_modifier = 3):
                            $ Girl.change_face("bemused", 1)

                            Girl.voice "Whoa, spicy. . ."

                            call change_Girl_stat(Girl, "obedience", 2)
                            call change_Girl_stat(Girl, "obedience", 1)

                            $ Girl.change_face("sexy")
                            $ Girl.take_off("jacket")

                            call change_Girl_stat(Girl, "inhibition", 2)
                            call change_Girl_stat(Girl, "inhibition", 1)

                            call expression Girl.tag + "_First_Topless"
                        else:
                            $ Girl.change_face("bemused")

                            call top_off_refused(Girl)
                    "I know, take it off.":
                        call topless_or_nothing(Girl)

                $ Girl.blushing = "_blush1"
            else:
                $ Girl.change_face("sexy")

                call top_off_refused(Girl)
        "How about just the [Girl.Clothes[top].name]?" if Girl.Clothes["top"]:
            if approval_check(Girl, 800, taboo_modifier = 2) and Girl.Clothes["bra"]:
                $ Girl.change_face("sexy")

                if Girl == RogueX:
                    ch_r "Well, that's no big deal I guess. . ."
                elif Girl == KittyX:
                    ch_k "Um, I guess I could. . ."
                elif Girl == EmmaX:
                    ch_e "Well, I suppose that would be fine. . ."
                elif Girl == LauraX:
                    ch_l "I mean. . . I guess. . ."
                elif Girl == JeanX:
                    ch_j "Sure, whatever."
                elif Girl == StormX:
                    ch_s "I suppose so."
                elif Girl == JubesX:
                    ch_v "Well, I guess. . ."

                $ Girl.change_face("bemused", 1)
                $ Girl.take_off("top")

                call change_Girl_stat(Girl, "obedience", 1)
                call change_Girl_stat(Girl, "inhibition", 2)
            elif not Girl.Clothes["bra"]:
                $ Girl.eyes = "surprised"
                $ Girl.blushing = "_blush2"

                if Girl == RogueX:
                    ch_r "I'm not exactly decent under this, you know."
                elif Girl == KittyX:
                    ch_k "I'd[Girl.like]be {i}totally{/i} exposed here."
                elif Girl == EmmaX:
                    ch_e "I don't think you're prepared for what's under there."
                elif Girl == LauraX:
                    ch_l "I don't really have anything on under here."
                elif Girl == JeanX:
                    ch_j "I'm not wearing a bra at the moment."
                elif Girl == StormX:
                    ch_s "I am naked under this, you know. . ."
                elif Girl == JubesX:
                    ch_v "I kinda don't have anything under this. . ."

                call change_Girl_stat(Girl, "inhibition", 1)

                menu:
                    extend ""
                    "Ok, you can leave it on.":
                        $ Girl.mouth = "smile"

                        call change_Girl_stat(Girl, "love", 2)

                        if Girl == RogueX:
                            ch_r "Great!"
                        elif Girl == KittyX:
                            ch_k "Thanks!"
                        elif Girl == EmmaX:
                            ch_e "Good."
                        elif Girl == LauraX:
                            ch_l "Right."
                        elif Girl == JeanX:
                            ch_j "That's what I said."
                        elif Girl == StormX:
                            ch_s "Very well then."
                        elif Girl == JubesX:
                            ch_v "Whew, thanks. . ."
                    "That doesn't bother me any.":
                        if approval_check(Girl, 500, "I", taboo_modifier = 3) or approval_check(Girl, 1000, "LI", taboo_modifier = 3):
                            $ Girl.change_face("bemused", 1)

                            if Girl == RogueX:
                                ch_r "Ooh, at least you know what you like"
                            elif Girl == KittyX:
                                ch_k "Why am I not surprised?"
                            elif Girl == EmmaX:
                                ch_e "Well, I suppose it couldn't hurt to try."
                            elif Girl == LauraX:
                                ch_l "Maybe it should. . ."
                            elif Girl == JeanX:
                                ch_j ". . ."
                            elif Girl == StormX:
                                ch_s "It doesn't bother me much either."
                            elif Girl == JubesX:
                                ch_v "Whoa, spicy. . ."

                            $ Girl.change_face("sexy")
                            call change_Girl_stat(Girl, "obedience", 2)
                            call change_Girl_stat(Girl, "obedience", 1)

                            $ Girl.take_off("top")

                            call change_Girl_stat(Girl, "inhibition", 2)
                            call change_Girl_stat(Girl, "inhibition", 1)
                            call expression Girl.tag + "_First_Topless"
                        else:
                            $ Girl.change_face("bemused")

                            call top_off_refused (Girl)
                    "I know, take it off.":
                        call topless_or_nothing (Girl)
                $ Girl.blushing = "_blush1"
            else:
                $ Girl.change_face("sexy")
                call top_off_refused (Girl)
        "Come on, please?":
            if approval and approval_check(Girl, 600, "L", taboo_modifier = 1):
                $ Girl.change_face("sexy")
                call change_Girl_stat(Girl, "obedience", 2)

                if Girl == RogueX:
                    if "no_topless" in Girl.recent_history:
                        ch_r "You're pretty persistent, [Girl.player_petname]. I guess this time it'll be rewarded. . ."
                    else:
                        ch_r "Heh, I suppose I can hardly refuse ya when you use the magic words . . ."
                elif Girl == KittyX:
                    if "no_topless" in Girl.recent_history:
                        ch_k "You just don't know when to quit. . . but you got lucky this time. . ."
                    else:
                        ch_k "You[Girl.like]know how to ask nicely . . ."
                elif Girl == EmmaX:
                    if "no_topless" in Girl.recent_history:
                        ch_e "Fine, I can't take your constant begging."
                    else:
                        ch_e "Well, I suppose if you ask nicely . . ."
                elif Girl == LauraX:
                    ch_l "Fine, you thirsty weirdo."
                elif Girl == JeanX:
                    if "no_topless" in Girl.recent_history:
                        ch_j "Oh, whatever."
                    else:
                        ch_j "I guess. . ."
                elif Girl == StormX:
                    ch_s "Oh, very well."
                elif Girl == JubesX:
                    ch_v "Ok, fine, geeze."

                $ Girl.expose_breasts()
                call change_Girl_stat(Girl, "inhibition", 2)
                call change_Girl_stat(Girl, "inhibition", 1)

                call expression Girl.tag + "_First_Topless"
            elif "no_topless" in Girl.recent_history:
                $ Girl.change_face("angry")

                if Girl == RogueX:
                    ch_r "Nuh uh, [Girl.player_petname]."
                elif Girl == KittyX:
                    ch_k "Noooope!"
                elif Girl == EmmaX:
                    ch_e "Again, no."
                elif Girl == LauraX:
                    ch_l "Still no."
                elif Girl == JeanX:
                    ch_j "Still a \"no\" on that, [Girl.player_petname]."
                elif Girl == StormX:
                    ch_s "Not today, no."
                elif Girl == JubesX:
                    ch_v "Nah. . ."

                call change_Girl_stat(Girl, "love", -5)
                $ Girl.recent_history.append("angry")
                $ Girl.daily_history.append("angry")
            else:
                $ Girl.change_face("sexy")

                call top_off_refused (Girl)
        "Lose the [Girl.Clothes[gloves].name], at least. . ." if Girl.Clothes["gloves"]:
            $ Girl.change_face("sexy")

            Girl.voice "Oh, all right."

            $ Girl.take_off("gloves")
        "No, topless or nothing.":
            call topless_or_nothing (Girl)
        "Never mind.":
            pass

    $ Girl.recent_history.append("ask topless")
    $ Girl.daily_history.append("ask topless")

    return

label top_off_refused(Girl):
    $ shift_focus (Girl)

    $ Girl.change_face("angry")

    if Girl == RogueX:
        if "no_topless" in Girl.recent_history:
            ch_r "Get a clue, [Girl.player_petname]."
        elif "no_topless" in Girl.daily_history:
            ch_r "Give it a rest, [Girl.player_petname]."
        else:
            $ Girl.change_face("sad")
            ch_r "I'm afraid not this time, [Girl.player_petname]. Sure we can't have some fun anyway?"
    elif Girl == KittyX:
        if "no_topless" in Girl.recent_history:
            ch_k "[Girl.Like]back off."
        elif "no_topless" in Girl.daily_history:
            ch_k "Not today, maybe not ever, [Girl.player_petname]."
        else:
            $ Girl.change_face("sad")

            ch_k "[Girl.Like], no way, but I don't want to go. . ."
    elif Girl == EmmaX:
        if "no_topless" in Girl.recent_history:
            ch_e "You should probably back off now."
        elif "no_topless" in Girl.daily_history:
            ch_e "I'm tired of this, [Girl.player_petname]."
        else:
            ch_e "Is this a dealbreaker for you?"
    elif Girl == LauraX:
        if "no_topless" in Girl.recent_history:
            ch_l "You're getting real close to the line, [Girl.player_petname]."
        elif "no_topless" in Girl.daily_history:
            ch_l "You keep coming back with this, [Girl.player_petname]."
        else:
            ch_l "Let it go?"
    elif Girl == JeanX:
        if "no_topless" in Girl.recent_history:
            ch_j "Step carefully, [Girl.player_petname]."
        elif "no_topless" in Girl.daily_history:
            ch_j "Still on about that?"
        else:
            ch_j "Careful. . ."
    elif Girl == StormX:
        if "no_topless" in Girl.recent_history:
            ch_s "I will not move on this."
        elif "no_topless" in Girl.daily_history:
            ch_s "Find your joy elsewhere, [Girl.player_petname]."
        else:
            ch_s "Do you insist on this path?"
    elif Girl == JubesX:
        if "no_topless" in Girl.recent_history:
            ch_v "I thought I was clear. . ."
        elif "no_topless" in Girl.daily_history:
            ch_v "Look, cut it out, [Girl.player_petname]."
        else:
            ch_v "Whoa, slow your roll there. . ."

    menu:
        extend ""
        "Sure, never mind." if "no_topless" not in Girl.recent_history:
            $ Girl.change_face("sexy")
            call change_Girl_stat(Girl, "love", 2)

            if Girl in [RogueX, KittyX]:
                Girl.voice "Great!"
            else:
                Girl.voice "Good."
        "Sorry, I'll drop it." if "no_topless" in Girl.recent_history:
            if Girl == RogueX:
                ch_r "Fine. . ."
            elif Girl == KittyX:
                ch_k "Good!"
            else:
                Girl.voice "Good."
        "No, I insist. . .":
            $ Girl.brows = "angry"

            if Girl == RogueX:
                $ Girl.brows = "confused"

                ch_r "Ok [Girl.player_petname], your loss."
            elif Girl == KittyX:
                ch_k "Fine then!"
            elif Girl == EmmaX:
                ch_e "Very well."
            elif Girl == LauraX:
                ch_l "Your funeral."
            elif Girl == JeanX:
                $ Girl.change_face("smile")

                ch_j "Well that was at least good for a laugh."
            elif Girl == StormX:
                ch_s "So be it."
            elif Girl == JubesX:
                ch_v "Too bad then. . ."

            call change_Girl_stat(Girl, "lust", 5)
            call change_Girl_stat(Girl, "love", 1)

            if "no_topless" not in Girl.recent_history:
                call change_Girl_stat(Girl, "obedience", 4)

            $ Girl.recent_history.append("angry")
            $ Girl.daily_history.append("angry")

    $ Girl.recent_history.append("no_topless")
    $ Girl.daily_history.append("no_topless")

    return

label topless_or_nothing(Girl):
    $ shift_focus (Girl)

    $ Girl.change_face("angry")

    if approval_check(Girl, 800, "OI", taboo_modifier = 4) and approval_check(Girl, 400, "O", taboo_modifier = 3):
        $ Girl.change_face("sad")
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "inhibition", 3)

        if Girl == RogueX:
            if "no_topless" in Girl.recent_history:
                ch_r "Ok, ok, whatever."
            else:
                ch_r "Fine, if that's what you want."
        elif Girl == KittyX:
            if "no_topless" in Girl.recent_history:
                ch_k "Ok, fine. This time."
            else:
                $ Girl.change_face("sad")

                ch_k "Whatever."
        elif Girl == EmmaX:
            if "no_topless" in Girl.recent_history:
                ch_e "Oh, very well. . ."
            else:
                $ Girl.change_face("sad")

                ch_e "Fine."
        elif Girl == LauraX:
            if "no_topless" in Girl.recent_history:
                ch_l "Hrmph, whatever. . ."
            else:
                $ Girl.change_face("sad")

                ch_l "Ugh, whatever."
        elif Girl == JeanX:
            if "no_topless" in Girl.recent_history:
                ch_j "Ok, fine. . ."
            else:
                $ Girl.change_face("sad")

                ch_j "Fine! . . whatever."
        elif Girl == StormX:
            $ Girl.change_face("sad")

            if "no_topless" in Girl.recent_history:
                ch_s "I suppose sometimes I must. . ."
            else:
                ch_s "Fine."
        elif Girl == JubesX:
            if "no_topless" in Girl.recent_history:
                ch_v "Ok, fine, just quit asking."
            else:
                ch_v "Ok, fine, whatever."

        call change_Girl_stat(Girl, "obedience", 4)
        call change_Girl_stat(Girl, "obedience", 2)

        $ Girl.expose_breasts()

        call expression Girl.tag + "_First_Topless"
    else:
        call change_Girl_stat(Girl, "love", -10)
        call change_Girl_stat(Girl, "obedience", 1)

        if Girl == RogueX:
            if "no_topless" in Girl.recent_history:
                ch_r "Seriously, cut this shit out."
            else:
                $ Girl.brows = "confused"

                ch_r "\"Nothing\" it is then."
        elif Girl == KittyX:
            if "no_topless" in Girl.recent_history:
                ch_k "It[Girl.like]wasn't cute the first time."
            else:
                $ Girl.brows = "angry"

                ch_k "[Girl.Like]no way!"
        elif Girl == EmmaX:
            if "no_topless" in Girl.recent_history:
                $ Girl.brows = "angry"

                ch_e "Learn to take \"no\" for an answer."
            else:
                ch_e "I'm afraid not."
        elif Girl == LauraX:
            if "no_topless" in Girl.recent_history:
                $ Girl.brows = "angry"

                ch_l "You have got to chill."
            else:
                ch_l "Nope."
        elif Girl == JeanX:
            if "no_topless" in Girl.recent_history:
                $ Girl.brows = "angry"

                ch_j "Keep it under control."
            else:
                ch_j "Oh, no."
        elif Girl == StormX:
            if "no_topless" in Girl.recent_history:
                $ Girl.brows = "angry"

                ch_s "I say again, \"no.\"."
            else:
                ch_s "Then that would be a \"no.\"."
        elif Girl == JubesX:
            if "no_topless" in Girl.recent_history:
                $ Girl.brows = "angry"

                ch_v "Look, I told you, \"no.\"."
            else:
                ch_v "Sorry, no go."

        $ Girl.recent_history.append("no_topless")
        $ Girl.daily_history.append("no_topless")

        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")

    return

label bottoms_off_refused(Girl, counter):
    $ shift_focus(Girl)

    if Girl == RogueX:
        if "no_bottomless" in Girl.recent_history:
            ch_r "What part of \"no\" escapes you, [Girl.player_petname]?"
        elif "no_bottomless" in Girl.daily_history:
            ch_r "If you keep this up, not ever, [Girl.player_petname]."
        else:
            $ Girl.change_face("sad")

            if counter == 2:
                ch_r "That's enough, [Girl.player_petname]. Sure we can't have some fun anyway?"
            else:
                ch_r "I'm afraid not this time, [Girl.player_petname]. Sure we can't have some fun anyway?"
    elif Girl == KittyX:
        if "no_bottomless" in Girl.recent_history:
            ch_k "You're[Girl.like]on my last nerve here."
        elif "no_bottomless" in Girl.daily_history:
            ch_k "Give it a rest."
        else:
            $ Girl.change_face("sad")

            if counter == 2:
                ch_k "What you see is what you get, but[Girl.like]can't we still have some fun?"
            else:
                ch_k "The answer's \"no,\" but[Girl.like]can't we still have some fun?"
    elif Girl == EmmaX:
        if "no_bottomless" in Girl.recent_history:
            ch_e "Try to control your impulses."
        elif "no_bottomless" in Girl.daily_history:
            ch_e "Not today."
        else:
            $ Girl.change_face("sad")

            if counter == 2:
                ch_e "That's all I'm willing to do, is that a deal-breaker?"
            else:
                ch_e "I'm afraid not, is that a deal-breaker?"
    elif Girl == LauraX:
        if "no_bottomless" in Girl.recent_history:
            ch_l "Reign it in."
        elif "no_bottomless" in Girl.daily_history:
            ch_l "No, not today."
        else:
            $ Girl.change_face("sad")

            if counter == 2:
                ch_l "No more, is that going to be a problem?"
            else:
                ch_l "Nope, is that going to be a problem?"
    elif Girl == JeanX:
        if "no_bottomless" in Girl.recent_history:
            ch_j "Take a breath, [Girl.player_petname]."
        elif "no_bottomless" in Girl.daily_history:
            ch_j "I made myself clear."
        else:
            $ Girl.change_face("sad")

            ch_j "Do we have a problem?"
    elif Girl == StormX:
        if "no_bottomless" in Girl.recent_history:
            ch_s "Show some restraint."
        else:
            $ Girl.change_face("sad")

            if counter == 2:
                ch_s "This is all, can we continue without it?"
            else:
                ch_s "I would rather not, can we continue without it?"
    elif Girl == JubesX:
        if "no_bottomless" in Girl.daily_history:
            ch_v "Like I said, nope."
        else:
            $ Girl.change_face("sad")

            ch_v "This is it, ok?"

    menu:
        extend ""
        "Sure, never mind." if "no_bottomless" not in Girl.recent_history:
            $ Girl.mouth = "smile"
            call change_Girl_stat(Girl, "love", 2)
            call change_Girl_stat(Girl, "obedience", 2)

            if Girl == RogueX:
                ch_r "Great."
            elif Girl == KittyX:
                ch_k "Great!"
            elif Girl == EmmaX:
                ch_e "Excellent."
            elif Girl == LauraX:
                ch_l "Right."
            elif Girl == JeanX:
                ch_j "Good. . ."
            elif Girl == StormX:
                ch_s "Good. . ."
            elif Girl == JubesX:
                ch_v "Cool."
        "Sorry, I'll drop it." if "no_bottomless" in Girl.recent_history:
            if Girl == EmmaX:
                ch_e "Good."
            elif Girl == LauraX:
                ch_l "Cool."
            else:
                Girl.voice "Fine. . ."
        "No, let's do something else.":
            $ Girl.brows = "confused"

            if Girl == RogueX:
                ch_r "Ok [Girl.player_petname], your loss."
            elif Girl == KittyX:
                ch_k "Ok[Girl.like]whatever."
            elif Girl == StormX:
                ch_s "So be it. . ."
            elif Girl == JubesX:
                ch_v "Whatever. . ."
            else:
                Girl.voice "Your loss."

            call change_Girl_stat(Girl, "lust", 5)
            call change_Girl_stat(Girl, "love", 1)

            if "no_bottomless" not in Girl.recent_history:
                call change_Girl_stat(Girl, "obedience", 4)

            $ Girl.recent_history.append("angry")
            $ Girl.daily_history.append("angry")

    $ Girl.recent_history.append("no_bottomless")
    $ Girl.daily_history.append("no_bottomless")

    return

label no_panties_on(Girl, counter):
    $ shift_focus(Girl)

    if Girl == RogueX:
        if Girl.Outfit.pussy_covered:
            ch_r "Well, I'm not exactly decent under here, you know. . ."
        else:
            ch_r "This is the last bit. . ."
    elif Girl == KittyX:
        if Girl.Outfit.pussy_covered:
            ch_k "[Girl.Like]I'm not wearing any panties. . ."
        else:
            ch_k "Not much else on. . ."
    elif Girl == EmmaX:
        if Girl.Outfit.pussy_covered:
            ch_e "I don't have anything on under this. . ."
        else:
            ch_e "This is all I have on. . ."
    elif Girl == LauraX:
        if Girl.Outfit.pussy_covered:
            ch_l "I don't have anything on under this. . ."
        else:
            ch_l "These are all I have on. . ."
    elif Girl == JeanX:
        if Girl.Outfit.pussy_covered:
            ch_j "I don't have panties on right now. . ."
        else:
            ch_j ". . ."
    elif Girl == StormX:
        if Girl.Outfit.pussy_covered:
            ch_s "I am naked under this. . ."
        else:
            ch_s "This is all I have on. . ."
    elif Girl == JubesX:
        if Girl.Outfit.pussy_covered:
            ch_v "I don't have anything on under this. . ."
        else:
            ch_v "This is all I've got on. . ."

    menu:
        extend ""
        "Could you do it anyway?":
            if approval_check(Girl, 1000, "LI", taboo_modifier = 1):
                if Girl == RogueX:
                    ch_r "Well, if you're gonna ask so nicely. . . "
                elif Girl == KittyX:
                    ch_k "I[Girl.like]guess so. . . "
                elif Girl == EmmaX:
                    ch_e "I suppose. . . "
                elif Girl == LauraX:
                    ch_l "I guess. . . "
                elif Girl == JeanX:
                    ch_j "Oh, why not. . ."
                elif Girl == StormX:
                    ch_s "I suppose I could. . ."
                elif Girl == JubesX:
                    ch_v "Well, I guess. . ."
            else:
                if Girl == RogueX:
                    ch_r "Sorry, I don't think so."
                elif Girl == KittyX:
                    ch_k "No thanks."
                elif Girl == EmmaX:
                    ch_e "I'm afraid not."
                elif Girl == LauraX:
                    ch_l "Nah, not right now."
                elif Girl == JeanX:
                    ch_j "Ha! Keep trying, [Girl.player_petname]."
                elif Girl == StormX:
                    ch_s "I do not think so, right now."
                elif Girl == JubesX:
                    ch_v "Nah. . ."

                call bottoms_off_refused(Girl, counter)

                return False
        "Don't care, lose'em.":
            if approval_check(Girl, 800, "OI", taboo_modifier = 1):
                if Girl == RogueX:
                    ch_r "Fine, whatever."
                elif Girl == KittyX:
                    ch_k "Whatev."
                elif Girl == EmmaX:
                    ch_e "If you insist."
                elif Girl == LauraX:
                    ch_l "Fine."
                elif Girl == JeanX:
                    ch_j ". . ."
                elif Girl == StormX:
                    ch_s ". . ."
                elif Girl == JubesX:
                    ch_v "Fine. . ."
            else:
                call bottoms_off_refused(Girl, counter)

                return False
        "Ok, you can leave it on.":
            return False

    return True

label undress_Girl(Girl, context = "ask"):
    $ shift_focus(Girl)

    $ stored_bonus = approval_bonus

    if Partner == Girl:
        $ approval_bonus = 0

    if context == "auto":
        if Girl.upskirt and Girl.Clothes["underwear"].state:
            return
        if Girl.bottom_number() > 5 and approval_bonus < 20:
            $ approval_bonus = 20
        if Girl.lust >= 90:
            $ approval_bonus += 10
        elif Girl.lust >= 80:
            $ approval_bonus += 5

        $ action_context = "auto"

        call Bottoms_Off (Girl, 0)
    elif context == "ask":
        menu:
            "Which parts?"
            "Your top." if Girl.Clothes["top"] or Girl.Clothes["bra"] or Girl.Clothes["gloves"] or Girl.Clothes["jacket"]:
                $ context = "top"
            "Your bottoms." if Girl.Clothes["bottom"] or Girl.Clothes["underwear"] or Girl.Clothes["hose"] or Girl.Clothes["boots"]:
                $ context = "bottom"
            "A little of both. . ." if Girl.Clothes["top"] or Girl.Clothes["bra"] or Girl.Clothes["bottom"] or Girl.Clothes["underwear"] or Girl.Clothes["hose"] or Girl.Clothes["boots"]:
                $ context = "both"
            "Never mind.":
                pass
    elif context == "top":
        if Girl.Outfit.breasts_covered:
            call top_off (Girl, 0)
    elif context == "bottom":
        if Girl.Outfit.pussy_covered:
            call Bottoms_Off (Girl, 0)
    elif context == "both":
        if Girl.Outfit.breasts_covered:
            call top_off (Girl, 0)

        if Partner == Girl:
            $ approval_bonus = 0
        else:
            $ approval_bonus = stored_bonus

        if "angry" in Girl.recent_history:
            pass
        elif not Girl.Outfit.pussy_covered:
            pass
        elif "no_topless" in Girl.recent_history:
            if Girl == RogueX:
                ch_r "You might want to rethink your next question."
            elif Girl == KittyX:
                ch_k "Don't push it. . ."
            elif Girl == EmmaX:
                ch_e "Care to push your luck?"
            elif Girl == LauraX:
                ch_l "Know when to fold'em, [Girl.player_petname]."
            elif Girl == JeanX:
                ch_j "Ha! Keep trying, [Girl.player_petname]."
            elif Girl == StormX:
                ch_s "I do not see this going your way. . ."
            elif Girl == JubesX:
                ch_v "Well now you're pushing it. . ."

            menu:
                extend ""
                "And now the bottoms?":
                    call Bottoms_Off (Girl, 0)
                "You're probably right, sorry.":
                    pass
        else:
            ch_p "And now the bottoms?"

            call Bottoms_Off (Girl, 0)

    $ approval_bonus = stored_bonus

    return

label automatically_strip(Girl):
    if Girl.Outfit.pussy_covered:
        if Girl == RogueX:
            ch_r "Well, I guess some things are necessary, [RogueX.player_petname]."
        elif Girl == KittyX:
            ch_k "We can't exactly do much like this, huh."
        elif Girl == EmmaX:
            ch_e "I suppose we can't do much with all this on."
        elif Girl == LauraX:
            ch_l "Huh. . ."
        elif Girl == JeanX:
            ch_j "Huh. . ."
        elif Girl == StormX:
            ch_s "I suppose our options are limited with these on."
        elif Girl == JubesX:
            ch_v "Let's get these out of the way. . ."

    $ Girl.expose_pussy()

    return

label strip_ultimatum(Girl):
    if "keepdancing" in Girl.recent_history:
        return

    call show_full_body(Girl)

    $ Girl.change_face("bemused", 1)

    if "stripforced" in Girl.recent_history:
        $ Girl.change_face("sad", 1)

        if Girl == RogueX:
            ch_r "That's as far as I care to go, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "That's all you get."
        elif Girl == EmmaX:
            ch_e "I think that's plenty, [Girl.player_petname]."
        elif Girl == LauraX:
            ch_l "Last call, [Girl.player_petname]."
        elif Girl == JeanX:
            ch_j "Ok, that's my limit."
        elif Girl == StormX:
            ch_s "I will go no further. . ."
        elif Girl == JubesX:
            ch_v "Ok, that's all you get. . ."
    else:
        if Girl == RogueX:
            ch_r "I'm sorry, [Girl.player_petname], I'm not ready to show you more. . . Yet."
        elif Girl == KittyX:
            ch_k "I don't know, [Girl.player_petname], that's as far as I'll go for now."
        elif Girl == EmmaX:
            ch_e "I'm afraid that's as far as I'm ready to go, [Girl.player_petname]. . . for now."
        elif Girl == LauraX:
            ch_l "Ok, that's enough, [Girl.player_petname]. . . for now."
        elif Girl == JeanX:
            ch_j "Ok, I think you've seen enough. . ."
        elif Girl == StormX:
            ch_s "That's enough for now. . ."
        elif Girl == JubesX:
            ch_v "I'm kinda done here. . ."

    menu:
        extend ""
        "That's ok, you can stop.":
            if "ultimatum" not in Girl.daily_history:
                call change_Girl_stat(Girl, "love", 2)
                call change_Girl_stat(Girl, "love", 2)
                call change_Girl_stat(Girl, "inhibition", 2)
                $ Girl.daily_history.append("ultimatum")

            $ Girl.recent_history.append("stopdancing")

            return "stop"
        "That's ok, but keep dancing for a bit. . .":
            if "ultimatum" not in Girl.daily_history:
                call change_Girl_stat(Girl, "love", 2)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", 2)
                $ Girl.daily_history.append("ultimatum")

            $ Girl.recent_history.append("keepdancing")

            if "stripforced" in Girl.recent_history:
                Girl.voice ". . ."
            else:
                if Girl == RogueX:
                    ch_r "Heh, ok [Girl.player_petname]."
                elif Girl == KittyX:
                    ch_k "Heh, alright."
                elif Girl == EmmaX:
                    ch_e "Oh, if I must, [Girl.player_petname]."
                elif Girl == LauraX:
                    ch_l "Eh? Fine."
                elif Girl == JeanX:
                    ch_j "Ok, sure."
                elif Girl == StormX:
                    ch_s "Very well. . ."
                elif Girl == JubesX:
                    ch_v "Ok, sure. . ."

            return "dance"
        "You'd better." if Girl.forced:
            if not approval_check(Girl, 500, "O", taboo_modifier=5) and not approval_check(Girl, 800, "L", taboo_modifier=5):
                $ Girl.change_face("angry")

                if Girl == RogueX:
                    ch_r "I don't know who you think I am, but I ain't gonna just jump when you say \"toad\"."
                    ch_r "I think we're done here for now."
                elif Girl == KittyX:
                    ch_k "I'm not just going to do \"whatever\"!"
                    ch_k "I'm done with this."
                elif Girl == EmmaX:
                    ch_e "I think you're overstepping your bounds here, [Girl.player_petname]."
                    ch_e "Remember your place."
                elif Girl == LauraX:
                    ch_l "I don't like that tone, [Girl.player_petname]."
                elif Girl == JeanX:
                    ch_j "Don't talk to me like that. -I- talk to -you- like that."
                elif Girl == StormX:
                    ch_s "I do not appreciate that tone."
                elif Girl == JubesX:
                    ch_v "I'd better not break your face either. . ."

                $ Girl.recent_history.append("angry")
                $ Girl.daily_history.append("angry")

                call remove_Girl(Girl)

                return "stop"

            $ approval_bonus += 20

            $ Girl.forced += 1
            $ Girl.change_face("sad")

            if "stripforced" in Girl.recent_history:
                $ Girl.change_face("angry")

                Girl.voice ". . ."
            else:
                if Girl == RogueX:
                    ch_r "I. . . guess I could. . ."
                elif Girl == KittyX:
                    ch_k "I. . . could show a bit more. . ."
                elif Girl == EmmaX:
                    ch_e "Hmm, forceful. . ."
                elif Girl == LauraX:
                    ch_l "Grrrr. . ."
                elif Girl == JeanX:
                    ch_j ". . . fine."
                elif Girl == StormX:
                    ch_s ". . ."
                elif Girl == JubesX:
                    ch_v "Well. . . ok. . ."

                $ Girl.recent_history.append("stripforced")

            call change_Girl_stat(Girl, "love", -40)
        "You can do better than that. Keep going." if not Girl.forced:
            if not approval_check(Girl, 300, "O", taboo_modifier=5) and not approval_check(Girl, 700, "L", taboo_modifier=5):
                $ Girl.change_face("angry")

                if Girl == RogueX:
                    ch_r "I don't know who you think I am, but I ain't gonna just jump when you say \"toad\"."
                    ch_r "I think we're done here for now."
                elif Girl == KittyX:
                    ch_k "I'm not just going to do \"whatever\"!"
                    ch_k "I'm done with this."
                elif Girl == EmmaX:
                    ch_e "I think you're overstepping your bounds here, [Girl.player_petname]."
                    ch_e "Remember your place."
                elif Girl == LauraX:
                    ch_l "I don't like that tone, [Girl.player_petname]."
                elif Girl == JeanX:
                    ch_j "Don't talk to me like that. -I- talk to -you- like that."
                elif Girl == StormX:
                    ch_s "No, I do not think so."
                elif Girl == JubesX:
                    ch_v "Oh, I can, but you're not goinna see it. . ."

                $ Girl.recent_history.append("angry")
                $ Girl.daily_history.append("angry")

                call remove_Girl(Girl)

                return "stop"

            call change_Girl_stat(Girl, "love", -10)
            call change_Girl_stat(Girl, "obedience", 3)
            call change_Girl_stat(Girl, "obedience", 5)

            $ approval_bonus += 20

            $ Girl.forced += 1

            $ Girl.change_face("sad")

            if Girl == RogueX:
                ch_r "Well, if you insist. . ."
            elif Girl == KittyX:
                ch_k "I mean, maybe. . ."
            elif Girl == EmmaX:
                ch_e "I can't imagine doing better than \"perfection\". . ."
            elif Girl == LauraX:
                ch_l ". . . Right. . ."
            elif Girl == JeanX:
                ch_j "I don't see how anyone could. . ."
            elif Girl == StormX:
                ch_s "We shall see. . ."
            elif Girl == JubesX:
                ch_v "Ok, how about this. . ."

    if "ultimatum" not in Girl.daily_history:
        $ Girl.daily_history.append("ultimatum")

    call show_Girl(Girl, color_transform = dancing(Girl.sprite_location))

    "[Girl.name] begins to dance again."

    return "forced"




label Group_Strip(Girl):
    call check_who_is_present

    if not Present:
        "Nobody's here."
        "You dance alone."
        return

    $ dancing_Girls = Present[:]

    while dancing_Girls[0] != Girl:
        $ renpy.random.shuffle(dancing_Girls)

    $ shift_focus(Girl)
    call set_the_scene

    $ round -= 5 if round > 5 else round - 1

    python:
        for G in dancing_Girls:
            G.change_face("sexy", 1)

    $ counter = len(dancing_Girls)

    while counter:
        $ counter -= 1

        if Girl == EmmaX and "classcaught" in EmmaX.recent_history:
            pass
        elif not approval_check(dancing_Girls[counter], 600, taboo_modifier = 1, Alt = [[EmmaX], (650+taboo*10)]) or (dancing_Girls[counter] == EmmaX and taboo and "taboo" not in EmmaX.history):
            if not approval_check(dancing_Girls[counter], 400):
                if dancing_Girls[counter] == RogueX:
                    ch_r "I'm just some sort'a gogo dancer now?"
                elif dancing_Girls[counter] == KittyX:
                    ch_k "Like I would just dance for you?"
                elif dancing_Girls[counter] == EmmaX:
                    ch_e "Oh, you think I'll dance to your tune?"
                elif dancing_Girls[counter] == LauraX:
                    ch_l "I don't dance."
                elif dancing_Girls[counter] == JeanX:
                    ch_j "I'm not in the mood."
                elif dancing_Girls[counter] == StormX:
                    ch_s "I do not dance."
                elif dancing_Girls[counter] == JubesX:
                    ch_v "I don't wanna dance, weirdo. . ."
            elif dancing_Girls[counter].taboo:
                if dancing_Girls[counter] == RogueX:
                    ch_r "I don't think this is the best place for dance'n."
                elif dancing_Girls[counter] == KittyX:
                    ch_k "I don't know, this really isn't a good place for it?"
                elif dancing_Girls[counter] == EmmaX:
                    ch_e "You must be joking. Here?"
                elif dancing_Girls[counter] == LauraX:
                    if approval_check(LauraX, 600, taboo_modifier = 0):
                        $ dancing_Girls.append(LauraX)
                    else:
                        ch_l "I don't feel like it."
                elif dancing_Girls[counter] == JeanX:
                    ch_j "I don't want to just randomly dance in public."
                elif dancing_Girls[counter] == StormX:
                    ch_s "I would not want to make a scene."
                elif dancing_Girls[counter] == JubesX:
                    ch_v "This isn't really the place for it. . ."
            else:
                if dancing_Girls[counter] == RogueX:
                    ch_r "I dont feel it right now."
                elif dancing_Girls[counter] == KittyX:
                    ch_k "I don't know, I don't really feel like dancing right now."
                elif dancing_Girls[counter] == EmmaX:
                    ch_e "I don't really feel like dancing at the moment."
                elif dancing_Girls[counter] == LauraX:
                    ch_l "I don't feel like it."
                elif dancing_Girls[counter] == JeanX:
                    ch_j "I'm not in the mood."
                elif dancing_Girls[counter] == StormX:
                    ch_s "I do not wish to dance right now."
                elif dancing_Girls[counter] == JubesX:
                    ch_v "Yeah, I don't feel like dancing right now. . ."

            $ dancing_Girls.remove(dancing_Girls[counter])

    if not dancing_Girls:
        return

    if EmmaX.location == Player.location and EmmaX not in dancing_Girls:
        if "classcaught" not in EmmaX.history:
            if EmmaX.location == EmmaX.home:
                ch_e "If the two of you would like to dance, please do it elsewhere."

                return
            else:
                ch_e "I should really be going."

                call remove_Girl(EmmaX)

    if "stripping" in dancing_Girls[0].daily_history and approval_check(dancing_Girls[0], 500, taboo_modifier = 3):
        $ line = renpy.random.choice(["You liked the show earlier?",
            "Didn't get enough earlier?",
            "You're going to wear me out."])
    else:
        $ line = renpy.random.choice(["Ok, that sounds fun.",
            "I could get into that.",
            "Yeah, ok."])

    dancing_Girls[0].voice "[line]"

    $ temp_Girls = dancing_Girls[:]

    while temp_Girls:
        call show_full_body(temp_Girls[0])

        $ temp_Girls.remove(temp_Girls[0])

    $ stored_approval_bonus = []

    $ counter = len(dancing_Girls)

    while counter:
        $ counter -= 1

        call show_Girl(dancing_Girls[counter], animation_transform = dancing(dancing_Girls[counter].sprite_location))

        $ dancing_Girls[counter].recent_history.append("stripping")
        $ dancing_Girls[counter].daily_history.append("stripping")
        $ dancing_Girls[counter].permanent_History["striptease"] += 1
        $ dancing_Girls[counter].remaining_Actions -= 1

        $ temp_approval_bonus = approval_bonus

        if dancing_Girls[counter].seen_breasts or dancing_Girls[counter].seen_pussy:
            $ temp_approval_bonus += 20
        if dancing_Girls[counter].seen_underwear:
            $ temp_approval_bonus += 5
        if "exhibitionist" in dancing_Girls[counter].traits:
            $ temp_approval_bonus += 4*taboo
        if ("sex friend" in dancing_Girls[counter].player_petnames or dancing_Girls[counter] in Player.Harem) and not taboo:
            $ temp_approval_bonus += 15
        elif "ex" in dancing_Girls[counter].traits:
            $ temp_approval_bonus -= 40
        elif dancing_Girls[counter].permanent_History["forced"] and not dancing_Girls[counter].forced:
            $ temp_approval_bonus -= 5*dancing_Girls[counter].permanent_History["forced"]

        $ stored_approval_bonus.append(temp_approval_bonus)

    if len(dancing_Girls) > 1:
        "They start to dance."

        $ Partner = dancing_Girls[1]

        $ between_event_count = 1
    else:
        "She starts to dance."

        $ between_event_count = 0

    if Girl == EmmaX and "classcaught" in EmmaX.recent_history:
        jump Group_Stripping

    python:
        for G in all_Girls:
            if G in Present and G not in dancing_Girls:
                if "stopdancing" not in G.recent_history:
                    G.recent_history.append("stopdancing")

    $ Player.primary_Action = "striptease"

    $ interrupted = False

    while not interrupted and round >= 10:
        $ round -= 2 if round > 2 else round

        python:
            for GA in dancing_Girls:
                for GB in dancing_Girls:
                    if GA != GB:
                        GA.check_if_likes(GB, 600, 1, 1)
                        GB.check_if_likes(GA, 600, 1, 1)

        menu:
            "Continue":
                pass
            "Would you kindly take off some clothes?":
                dancing_Girls[0].voice "Hmm?"

                $ interrupted = True
            "Stop":
                jump Group_Strip_End

    if EmmaX.location == Player.location and len(Present) > 1:
        if "classcaught" not in EmmaX.history or "threesome" not in EmmaX.history or (taboo and "taboo" not in EmmaX.history):
            if EmmaX.location == "bg_emma":
                ch_e "If the two of you would like to get indecent, please do it elsewhere."

                return
            else:
                ch_e "I should really be going."

                call remove_Girl(EmmaX)

label Group_Stripping:
    $ Count = 0

    while round >= 10 and dancing_Girls:
        $ round -= 2 if round > 2 else round

        if dancing_Girls[Count] != Player.focused_Girl:
            $ shift_focus (dancing_Girls[Count])

        call Girl_Stripping (dancing_Girls[Count])

        if not dancing_Girls:
            jump Group_Strip_End

        if "stopdancing" in dancing_Girls[Count].recent_history:
            jump Group_Strip_End

        $ Player.primary_Action = "striptease"

        python:
            for GA in dancing_Girls:
                for GB in dancing_Girls:
                        if GA != GB:
                            GA.check_if_likes(GB, 800, 2, 1)
                            GB.check_if_likes(GA, 800, 2, 1)

        if len(dancing_Girls) >= 2:
            if Count == 0 and "stopdancing" not in dancing_Girls[1].recent_history:
                $ Count = 1
                $ between_event_count = 0
                $ stored_approval_bonus[1] = approval_bonus
                $ approval_bonus = stored_approval_bonus[0]
            elif Count == 1 and "stopdancing" not in dancing_Girls[0].recent_history:
                $ Count = 0
                $ between_event_count = 1
                $ stored_approval_bonus[0] = approval_bonus
                $ approval_bonus = stored_approval_bonus[1]

            $ shift_focus (dancing_Girls[Count])
            call Activity_Check (Player.focused_Girl, Partner)

        if len(dancing_Girls) < 2 or "stopdancing" in dancing_Girls[1].recent_history:

            $ approval_bonus = stored_approval_bonus[Count]
            $ Count = 0
            $ between_event_count = 0
            $ Partner = 0

            call Activity_Check (Player.focused_Girl, Partner)

            if not dancing_Girls or "stopdancing" in dancing_Girls[0].recent_history:
                jump Group_Strip_End

    if dancing_Girls and round < = 15:
        dancing_Girls[0].voice "It's getting late, we should probably take a break."

label Group_Strip_End:
    python:
        for G in dancing_Girls:
            G.drain_word("stopdancing", 1, 0, 0)
            G.drain_word("keepdancing", 1, 0, 0)

    call set_the_scene

    return




label Girl_Stripping(Girl):
    if "stopdancing" in Girl.recent_history:
        return

    $ Girl.arm_pose = 2
    $ Girl.lust_face(1)

    $ Nudist = 0

    if Girl == StormX and (StormX in Rules or Girl.taboo <= 20):
        if Girl.forced:
            $ Nudist = -40
        else:
            $ Nudist = Girl.taboo

    if "keepdancing" not in Girl.recent_history:
        if Girl == JubesX and Girl.Clothes["jacket"] and (Girl.Clothes["top"] or Girl.Clothes["bra"]) and (Girl.Clothes["underwear"] or Girl.Clothes["bottom"] or Girl.Clothes["hose"] == "tights"):
            if approval_check(Girl, 750, taboo_modifier = 3):
                call change_Girl_stat(Girl, "obedience", 1)
                call change_Girl_stat(Girl, "inhibition", 1)
                call change_Player_stat("focus", 60, 3)
                $ line = Girl.Clothes["jacket"]
                $ Girl.take_off("jacket")
                "She shrugs off her [line] and throws it behind her."
            else:
                jump strip_ultimatum
        elif Girl == JubesX and Girl.Clothes["jacket"] and Girl.Clothes["top"] and (Girl.Clothes["underwear"] or Girl.Clothes["bottom"] or Girl.Clothes["hose"] == "tights"):

            if approval_check(Girl, 750, taboo_modifier = 3):
                call change_Girl_stat(Girl, "obedience", 1)
                call change_Girl_stat(Girl, "inhibition", 1)
                call change_Player_stat("focus", 60, 3)
                $ line = Girl.Clothes["jacket"]
                $ Girl.take_off("jacket")
                "She shrugs off her [line] and throws it behind her."
            else:
                jump strip_ultimatum
        elif Girl.Clothes["top"] and Girl.Clothes["bra"] and (Girl.Clothes["underwear"] or Girl.Clothes["bottom"] or Girl.Clothes["hose"] == "tights"):

            if approval_check(Girl, 750, taboo_modifier = 3, Alt = [[StormX], (300-Nudist*3)]):
                call change_Girl_stat(Girl, "obedience", 1)
                call change_Girl_stat(Girl, "inhibition", 1)
                call change_Player_stat("focus", 60, 3)
                $ line = Girl.Clothes["top"]
                $ Girl.take_off("top")
                if Girl == KittyX:
                    "She drops her shoulders and her [line] falls to the floor."
                else:
                    "She pulls her [line] over her head and throws it behind her."
            else:
                jump strip_ultimatum

        elif Girl.Clothes["bottom"] and (Girl.Clothes["underwear"] or Girl.Clothes["hose"] == "tights"):

            if approval_check(Girl, 1200, taboo_modifier = 3, Alt = [[StormX], (600-Nudist*3)]) or (Girl.seen_underwear and approval_check(Girl, 900, taboo_modifier = 3) and not Girl.taboo):
                call change_Girl_stat(Girl, "lust", 5)
                call change_Girl_stat(Girl, "obedience", 1)
                call change_Girl_stat(Girl, "inhibition", 1)
                call change_Player_stat("focus", 60, 5)
                $ line = Girl.Clothes["bottom"]
                $ Girl.Outfit.remove_Clothing(["pants", "skirt"])
                if Girl == KittyX:
                    "Her [line] slide through her legs until they're only on her toes, before she kicks them to the floor."
                else:
                    "She unzips and pulls down her [line], dropping them to the floor."
                if not Girl.seen_underwear:
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "obedience", 3)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    call change_Girl_stat(Girl, "inhibition", 2)
                    $ Girl.seen_underwear = 1
            else:
                jump strip_ultimatum

        elif Girl.Clothes["hose"]:

            if Girl.Clothes["hose"] == "tights":
                if approval_check(Girl, 1200, taboo_modifier = 3):
                    call change_Girl_stat(Girl, "lust", 6)
                    call change_Player_stat("focus", 60, 6)
                else:
                    jump strip_ultimatum

            elif Girl.hose_number() >= 6 and approval_check(Girl, 1200, taboo_modifier = 3):
                if approval_check(Girl, 1200, taboo_modifier = 3, Alt = [[StormX], (600-Nudist*3)]):
                    call change_Girl_stat(Girl, "lust", 4)
                    call change_Player_stat("focus", 60, 4)
                else:
                    jump strip_ultimatum
            else:
                call change_Player_stat("focus", 60, 3)
            $ line = Girl.Clothes["hose"]
            $ Girl.take_off("hose")
            if Girl == KittyX:
                "Her [line] slide down off her legs, leaving them in a small pile."
            else:
                "She rolls the [line] down off her legs, leaving them in a small pile."
            call expression Girl.tag + "_First_Bottomless" pass (1)

        elif Girl == JubesX and Girl.Clothes["jacket"] and (Girl.Clothes["underwear"] or Girl.Clothes["bottom"] or Girl.Clothes["hose"] == "tights"):

            if approval_check(Girl, 1250, taboo_modifier = 3) or (Girl.seen_breasts and approval_check(Girl, 1000, taboo_modifier = 3) and not Girl.taboo):
                call change_Girl_stat(Girl, "lust", 5)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", 10)
                call change_Player_stat("focus", 80, 15)
                $ line = Girl.Clothes["jacket"]
                $ Girl.take_off("jacket")
                "She shrugs off her [line] and throws it behind her."
                if not Girl.seen_breasts:
                    $ Girl.change_face("bemused", 1)
                    call change_Girl_stat(Girl, "obedience", 3)
                    call change_Girl_stat(Girl, "obedience", 4)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    "She hesitantly glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                    call expression Girl.tag + "_First_Topless" pass (1)
            else:
                jump strip_ultimatum
        elif Girl.Clothes["top"] and not Girl.Clothes["bra"] and (Girl.Clothes["underwear"] or Girl.Clothes["hose"] == "tights"):

            if approval_check(Girl, 1250, taboo_modifier = 3, Alt = [[StormX], (650-Nudist*3)]) or (Girl.seen_breasts and approval_check(Girl, 1000, taboo_modifier = 3) and not Girl.taboo):
                call change_Girl_stat(Girl, "lust", 5)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", 10)
                call change_Player_stat("focus", 80, 15)
                $ line = Girl.Clothes["top"]
                $ Girl.take_off("top")
                if not Girl.seen_breasts:
                    $ Girl.change_face("bemused", 1)
                    call change_Girl_stat(Girl, "obedience", 3)
                    call change_Girl_stat(Girl, "obedience", 4)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    if Girl == KittyX:
                        "She hesitantly glances your way, and then with tug her [line] passes through her, tossing it to the ground."
                    elif Girl in (EmmaX,LauraX, StormX):
                        "She glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                    else:
                        "She hesitantly glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                    call expression Girl.tag + "_First_Topless" pass (1)
                else:
                    if Girl == KittyX:
                        "She drops her shoulders and her [line] falls to the floor."
                    else:
                        "She pulls her [line] over her head, tossing it to the ground."
            else:
                jump strip_ultimatum

        elif Girl.Clothes["bra"] and not Girl.Clothes["top"]:

            if approval_check(Girl, 1250, taboo_modifier = 3, Alt = [[StormX], (650-Nudist*3)]) or (Girl.seen_breasts and approval_check(Girl, 1000, taboo_modifier = 3) and not Girl.taboo):
                call change_Girl_stat(Girl, "lust", 5)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", 1)
                call change_Player_stat("focus", 80, 15)
                $ line = Girl.Clothes["bra"]
                $ Girl.take_off("bra")
                if not Girl.seen_breasts:
                    $ Girl.change_face("bemused", 1)
                    if Girl == KittyX:
                        "She hesitantly glances your way, and then with a shrug pulls her [line] through herself, tossing it to the ground."
                    elif Girl in (EmmaX,LauraX, StormX):
                        "She glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                    else:
                        "She hesitantly glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                    call change_Girl_stat(Girl, "obedience", 3)
                    call change_Girl_stat(Girl, "obedience", 4)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    call expression Girl.tag + "_First_Topless" pass (1)
                else:
                    $ Girl.change_face("sexy")
                    if Girl == KittyX:
                        "She pulls her [line] through herself, tossing it to the ground."
                    else:
                        "She pulls her [line] over her head, tossing it to the ground."
            else:
                jump strip_ultimatum

        elif Girl.Clothes["bottom"]:

            if approval_check(Girl, 1350, taboo_modifier = 3, Alt = [[StormX], (800-Nudist*3)]) or (Girl.seen_pussy and approval_check(Girl, 1100, taboo_modifier = 3) and not Girl.taboo):
                call change_Girl_stat(Girl, "lust", 10)
                $ line = Girl.Clothes["bottom"]
                $ Girl.Outfit.remove_Clothing(["pants", "skirt"])
                if not Girl.seen_pussy:
                    call change_Girl_stat(Girl, "obedience", 3)
                    call change_Girl_stat(Girl, "obedience", 5)
                    call change_Girl_stat(Girl, "inhibition", 4)
                    call change_Girl_stat(Girl, "inhibition", 4)
                    if Girl == KittyX:
                        "She shyly looks up at you, and then slowly lets her [line] slide to the floor."
                    elif Girl in (EmmaX,LauraX,JeanX):
                        "She hesitantly looks up at you, and then slowly unzips and pulls down her [line], dropping them to the floor."
                    else:
                        "She shyly looks up at you, and then slowly unzips and pulls down her [line], dropping them to the floor."
                    call expression Girl.tag + "_First_Bottomless" pass (1)
                else:
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "obedience", 1)
                    if Girl == KittyX:
                        "She lets her [line] pass through her legs, dropping them to the floor."
                    else:
                        "She unzips and pulls down her [line], dropping them to the floor."
                    call change_Girl_stat(Girl, "inhibition", 2)
                call change_Player_stat("focus", 85, 15)
            else:
                jump strip_ultimatum

        elif Girl == JubesX and Girl.Clothes["jacket"]:

            if approval_check(Girl, 1350, taboo_modifier = 3) or (Girl.seen_pussy and approval_check(Girl, 1100, taboo_modifier = 3) and not Girl.taboo):
                $ line = Girl.Clothes["jacket"]
                $ Girl.take_off("jacket")
                if not Girl.seen_pussy:
                    call change_Girl_stat(Girl, "obedience", 3)
                    call change_Girl_stat(Girl, "obedience", 5)
                    call change_Girl_stat(Girl, "inhibition", 4)
                    call change_Girl_stat(Girl, "inhibition", 4)
                    "She hesitantly glances your way, and then with a shrug pulls her [line] off, tossing it to the ground."
                    call expression Girl.tag + "_First_Bottomless" pass (1)
                else:
                    "She shrugs her [line] off, tossing it to the ground."

                if not Girl.Clothes["bra"] or Girl.top_pulled_up:
                    if not Girl.seen_breasts:
                        call change_Girl_stat(Girl, "obedience", 3)
                        call change_Girl_stat(Girl, "inhibition", 3)
                        call expression Girl.tag + "_First_Topless" pass (1)
                    else:
                        call change_Girl_stat(Girl, "lust", 15)
                        call change_Girl_stat(Girl, "obedience", 3)
                        call change_Girl_stat(Girl, "obedience", 1)
                        call change_Girl_stat(Girl, "inhibition", 3)
                else:
                    call change_Girl_stat(Girl, "lust", 10)
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "inhibition", 2)
                call change_Player_stat("focus", 85, 15)
            else:
                jump strip_ultimatum
        elif Girl.Clothes["top"] and not Girl.Clothes["underwear"]:

            if approval_check(Girl, 1350, taboo_modifier = 3, Alt = [[StormX], (800-Nudist*3)]) or (Girl.seen_pussy and approval_check(Girl, 1100, taboo_modifier = 3) and not Girl.taboo):
                $ line = Girl.Clothes["top"]
                $ Girl.take_off("top")
                if not Girl.seen_pussy:
                    call change_Girl_stat(Girl, "obedience", 3)
                    call change_Girl_stat(Girl, "obedience", 5)
                    call change_Girl_stat(Girl, "inhibition", 4)
                    call change_Girl_stat(Girl, "inhibition", 4)
                    if Girl == KittyX:
                        "She hesitantly glances your way, and then with a tug pulls her [line] through herself, tossing it to the ground."
                    elif Girl in (EmmaX,LauraX, StormX):
                        "She glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                    else:
                        "She hesitantly glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                    call expression Girl.tag + "_First_Bottomless" pass (1)
                else:
                    if Girl == KittyX:
                        "She drops her shoulders and her [line] falls to the floor."
                    else:
                        "She pulls her [line] over her head, tossing it to the ground."

                if not Girl.Clothes["bra"] or Girl.top_pulled_up:
                    if not Girl.seen_breasts:
                        call change_Girl_stat(Girl, "obedience", 3)
                        call change_Girl_stat(Girl, "inhibition", 3)
                        call expression Girl.tag + "_First_Topless" pass (1)
                    else:
                        call change_Girl_stat(Girl, "lust", 15)
                        call change_Girl_stat(Girl, "obedience", 3)
                        call change_Girl_stat(Girl, "obedience", 1)
                        call change_Girl_stat(Girl, "inhibition", 3)
                else:
                    call change_Girl_stat(Girl, "lust", 10)
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "inhibition", 2)
                call change_Player_stat("focus", 85, 15)
            else:
                jump strip_ultimatum

        elif Girl.Clothes["bra"]:

            if approval_check(Girl, 1250, taboo_modifier = 3, Alt = [[StormX], (750-Nudist*3)]) or (Girl.seen_breasts and approval_check(Girl, 1100, taboo_modifier = 3) and not Girl.taboo):
                call change_Girl_stat(Girl, "lust", 5)
                $ line = Girl.Clothes["bra"]
                $ Girl.take_off("bra")
                if not Girl.seen_breasts:
                    call change_Girl_stat(Girl, "obedience", 3)
                    call change_Girl_stat(Girl, "obedience", 4)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    if Girl == KittyX:
                        "She hesitantly glances your way, and then with a tug pulls her [line] through herself, tossing it to the ground."
                    elif Girl in (EmmaX,LauraX, StormX):
                        "She glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                    else:
                        "She hesitantly glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                    call expression Girl.tag + "_First_Topless" pass (1)
                else:
                    call change_Girl_stat(Girl, "obedience", 2)
                    if Girl == KittyX:
                        "She drops her shoulders and her [line] falls to the floor."
                    else:
                        "She pulls her [line] over her head, tossing it to the ground."
                    call change_Girl_stat(Girl, "inhibition", 1)
                call change_Player_stat("focus", 80, 15)
            else:
                jump strip_ultimatum

        elif Girl.Clothes["underwear"]:

            if approval_check(Girl, 1350, taboo_modifier = 3, Alt = [[StormX], (800-Nudist*3)]) or (Girl.seen_pussy and approval_check(Girl, 1100, taboo_modifier = 3) and not Girl.taboo):
                call change_Girl_stat(Girl, "lust", 10)
                $ line = Girl.Clothes["underwear"]
                $ Girl.take_off("underwear")
                if not Girl.seen_pussy:
                    call change_Girl_stat(Girl, "obedience", 3)
                    call change_Girl_stat(Girl, "obedience", 5)
                    call change_Girl_stat(Girl, "inhibition", 4)
                    call change_Girl_stat(Girl, "inhibition", 4)
                    if Girl == KittyX:
                        "She shyly looks up at you, and then slowly tugs her [line] off, flinging them to the side."
                    elif Girl in (EmmaX,LauraX):
                        "She looks up at you, and then slowly pulls her [line] down, kicking them off to the side."
                    else:
                        "She shyly looks up at you, and then slowly pulls her [line] down, kicking them off to the side."
                    call expression Girl.tag + "_First_Bottomless" pass (1)
                else:
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "obedience", 1)
                    if Girl == KittyX:
                        "She looks up at you, and then gently pulls her [line] off, flicking them to the side."
                    else:
                        "She looks up at you, and then gently pulls her [line] down, kicking them off to the side."
                    call change_Girl_stat(Girl, "inhibition", 2)
                call change_Player_stat("focus", 85, 15)
            else:
                jump strip_ultimatum
        else:

            $ Girl.change_face("sexy")
            if Girl == RogueX:
                ch_r "I'm afraid that's all I have on, [Girl.player_petname]. . ."
            elif Girl == KittyX:
                ch_k "It looks like I've run out of clothes. . ."
            elif Girl == EmmaX:
                ch_e "Well, it appears I've run out of clothes, [Girl.player_petname]. . ."
            elif Girl == LauraX:
                ch_l "Well, that's all I've got, [Girl.player_petname]. . ."
            elif Girl == JeanX:
                ch_j "I'm all out of clothes. . ."
            elif Girl == StormX:
                ch_s "I appear to have lost my clothing. . ."
            elif Girl == JubesX:
                ch_v "Well, it looks like I'm done here. . ."
            menu:
                extend ""
                "Ok, you can stop":
                    $ Girl.recent_history.append("stopdancing")
                    call show_full_body(Girl)
                "Keep on dancing":
                    $ Girl.recent_history.append("keepdancing")


    call change_Girl_stat(Girl, "lust", 2)
    if "exhibitionist" in Girl.traits:
        call change_Girl_stat(Girl, "lust", 2)
    call change_Player_stat("focus", 60, 3)
    if Player.secondary_Action == "jerking_off":
        call change_Girl_stat(Girl, "lust", 2)
        call change_Player_stat("focus", 200, 5)

    if not Player.semen and Player.climax >= 50:
        $ Player.climax = 50

    if Player.climax >= 100 or Girl.lust >= 100:


        if Player.climax >= 100:

            call Player_Cumming (Girl)
            if "angry" in Girl.recent_history:
                return
            call change_Girl_stat(Girl, "lust", 5)
            if not Player.semen and Player.secondary_Action == "jerking_off":
                "You're spitting dust here, maybe just watch quietly for a while."
                $ Player.secondary_Action = None
            if Player.climax > 80:
                jump Group_Strip_End

        if Girl.lust >= 100:

            call Girl_Cumming (Girl)
            if action_context == "shift" or "angry" in Girl.recent_history:
                $ Count = 0
                jump Group_Strip_End

        call show_full_body(Girl)
        call show_Girl(Girl, color_transform = dancing(Girl.sprite_location))

        "[Girl.name] begins to dance again."

    if Partner and Partner.lust >= 100:

        call Girl_Cumming (Partner)

    menu:
        "[Girl.name] should. . ."
        "Keep Going. . ." if "keepdancing" not in Girl.recent_history:
            $ Girl.eyes = "sexy"
            if Girl.love >= 700 or Girl.obedience >= 500:
                if not approval_bonus:
                    $ approval_bonus = 10
                elif approval_bonus <= 20:
                    $ approval_bonus += 1
            if taboo and Girl.permanent_History["striptease"] <= 10:
                call change_Girl_stat(Girl, "obedience", 7)
            elif taboo or Girl.permanent_History["striptease"] <= 10:
                call change_Girl_stat(Girl, "obedience", 5)
            elif Girl.permanent_History["striptease"] <= 50:
                call change_Girl_stat(Girl, "obedience", 3)
        "Keep Dancing. . ." if "keepdancing" in Girl.recent_history:
            $ Girl.eyes = "sexy"

        "Stop stripping, keep dancing" if "keepdancing" not in Girl.recent_history:
            if Girl == RogueX:
                ch_r "Ok. . ."
            elif Girl == KittyX:
                ch_k "K. . ."
            elif Girl == EmmaX:
                ch_e "Oh? Very well."
            elif Girl == LauraX:
                ch_l "Huh? I guess. . ."
            elif Girl == JeanX:
                ch_j "Ok, sure."
            elif Girl == StormX:
                ch_s "Fine. . ."
            elif Girl == JubesX:
                ch_v "Oh, well ok. . ."
            $ Girl.recent_history.append("keepdancing")

        "Start stripping again" if "keepdancing" in Girl.recent_history:
            $ Girl.recent_history.remove("keepdancing")
            if "stripforced" in Girl.recent_history:
                Girl.voice ". . ."
            else:
                if Girl == RogueX:
                    ch_r "Hmm. . ."
                elif Girl == KittyX:
                    ch_k "Huh?"
                else:
                    Girl.voice "Hmm. . ."
        "Just watch silently":

            if "watching" not in Girl.recent_history:
                if "keepdancing" not in Girl.recent_history:
                    if taboo and Girl.permanent_History["striptease"] <= 10:
                        call change_Girl_stat(Girl, "inhibition", 3)
                    elif taboo or Girl.permanent_History["striptease"] <= 10:
                        call change_Girl_stat(Girl, "inhibition", 1)
                elif Girl.permanent_History["striptease"] <= 50:
                    call change_Girl_stat(Girl, "inhibition", 2)
                    call change_Girl_stat(Girl, "lust", 2)
                $ Girl.recent_history.append("watching")

        "Start jack'in it." if Player.secondary_Action != "jerking_off":
            call jerking_off (Girl)
        "Stop jack'in it." if Player.secondary_Action == "jerking_off":
            $ Player.secondary_Action = None

        "Lose the [Girl.Clothes[gloves].name]. . ." if Girl.Clothes["gloves"]:
            $ Girl.change_face("surprised")
            $ Girl.mouth = "kiss"
            Girl.voice "All right, [Girl.player_petname]."
            $ Girl.change_face("sexy")
            $ Girl.take_off("gloves")
        "Ok, that's enough.":

            if Girl == RogueX:
                ch_r "Ok, [Girl.player_petname]. . . "
            elif Girl == KittyX:
                ch_k "Ok. . ."
            else:
                Girl.voice "Alright, [Girl.player_petname]."
            $ renpy.pop_call()
            jump Group_Strip_End

    return











label Bottoms_Off(Girl, Intro = 1):
    $ shift_focus (Girl)

    if "angry" in Girl.recent_history:
        if Girl == RogueX:
            ch_r "I'm just too annoyed to deal with this right now."
        elif Girl == KittyX:
            ch_k "The only \"kitty\" you're getting is up here."
        elif Girl == EmmaX:
            ch_e "I would give up on that."
        elif Girl == LauraX:
            ch_l "You're barking up the wrong tree."
        elif Girl == JeanX:
            ch_j "Definitely not, [Girl.player_petname]."
        elif Girl == StormX:
            ch_s "That is certainly optimistic."
            ch_s "No."
        elif Girl == JubesX:
            ch_v "Definitely not."
        return

    if Girl.seen_pussy and approval_check(Girl, 700):
        $ approval_bonus += 20
    elif not Girl.Clothes["underwear"]:
        $ approval_bonus -= 20
    elif Girl.seen_underwear and approval_check(Girl, 500):
        $ approval_bonus += 5

    if Intro == "dildo":
        $ approval_bonus += 20

    if "exhibitionist" in Girl.traits:
        $ approval_bonus += (taboo*5)

    if (Girl in Player.Harem or "sex friend" in Girl.player_petnames) and not taboo:
        $ approval_bonus += 10
    elif "ex" in Girl.traits:
        $ approval_bonus -= 40

    if "no_bottomless" in Girl.recent_history:
        $ approval_bonus -= 20
    elif Girl == StormX and (not taboo or Girl in Rules):
        $ approval_bonus += 20

    if Intro:
        if Intro == 2 and Girl.Outfit.thighs_covered:
            if Girl == RogueX:
                ch_r "I don't know, I might need my knickers off for that. . ."
            elif Girl == KittyX:
                ch_k "So, you'd have to be able to[KittyX.like]touch down there, I guess. . ."
            elif Girl == EmmaX:
                ch_e "I would probably need to lose these to get anything out of that. . ."
            elif Girl == LauraX:
                ch_l "I'd need to be pantsless to get anything from that. . ."
            elif Girl == JeanX:
                ch_j "I guess I'd have to go bottomless. . ."
            elif Girl == StormX:
                ch_s "I will remove these then. . ."
            elif Girl == JubesX:
                ch_v "I guess these would get in the way. . ."
        else:
            if Girl.Clothes["bottom"] and not Girl.upskirt:
                ch_p "This might be easier without your [Girl.Clothes[bottom].name] on."
            elif Girl.Clothes["underwear"] and not Girl.Clothes["underwear"] and Girl.Clothes["underwear"] and not Girl.Clothes["underwear"].state:
                ch_p "This might be easier without your [Girl.Clothes[underwear].name] on."

    $ approval = approval_check(Girl, 1200, taboo_modifier = 5)

    if action_context == "auto":
        $ counter = 0

        if not Girl.upskirt and not Girl.Clothes["underwear"].state:
            if Girl.wearing_skirt:

                if approval >= 2 or (Girl.seen_pussy and not taboo):
                    call change_Girl_stat(Girl, "inhibition", 1)
                    if taboo:
                        call change_Girl_stat(Girl, "inhibition", (int(taboo/20)))
                    $ Girl.upskirt = True
                    "She slides her skirt up."
                    $ counter = 1

            if Girl.wearing_pants or Girl.hose_number() >= 6:
                if Girl.Clothes["underwear"]:

                    if not approval or (not Girl.seen_underwear and taboo):
                        return
                elif approval < 2 or (not Girl.seen_pussy and taboo):
                    return
                elif Girl.upskirt:
                    return
                call change_Girl_stat(Girl, "inhibition", 1)
                if Girl.hose_number() >= 6:
                    $ line = Girl.Clothes["hose"]
                    $ Girl.take_off("hose")
                $ Girl.Clothes["pants"].state = True

                if Girl == KittyX:
                    if Girl.wearing_pants:
                        "[Girl.name] grumbles to herself, and then allows her [Girl.Clothes[bottom].name] to drop down her legs."
                    else:
                        "[Girl.name] grumbles to herself, and then allows her [line] to drop down her legs."
                    if Girl.Clothes["underwear"]:
                        $ Girl.seen_underwear = 1
                elif Girl.Clothes["underwear"]:
                    if Girl.bottom_number(0) >= 6:
                        "[Girl.name] grumbles to herself, and then unzips her [Girl.Clothes[bottom].name], sliding them down her legs."
                    else:
                        "[Girl.name] grumbles to herself, and then pulls her [line] down her legs."
                    $ Girl.seen_underwear = 1
                else:
                    if Girl.bottom_number(0) >= 6:
                        "[Girl.name] grumbles to herself, and then unzips her [Girl.Clothes[bottom].name], sliding them off her bare ass."
                    else:
                        "[Girl.name] grumbles to herself, and then pulls her [line] down her bare ass."
                call expression Girl.tag + "_First_Bottomless" pass (1)
                if taboo:
                    call change_Girl_stat(Girl, "inhibition", (int(taboo/10)))
                $ counter = 1

        if Girl.Clothes["underwear"] and not Girl.Clothes["underwear"].state:

            if approval >= 2 or (Girl.seen_pussy and not taboo):
                call change_Girl_stat(Girl, "inhibition", 2)
                if taboo:
                    call change_Girl_stat(Girl, "inhibition", (int(taboo/10)))

                $ Girl.expose_pussy(Girl)

                if Girl == KittyX:
                    if counter:
                        "With a second thought, [Girl.name] lets her [Girl.Clothes[underwear].name] drop too."
                    else:
                        "[Girl.name] tsks in irritation, and her [Girl.Clothes[underwear].name] slide off to the ground."
                else:
                    if counter:
                        "[Girl.name] tsks in irritation, and pulls down her [Girl.Clothes[underwear].name] too."
                    else:
                        "[Girl.name] tsks in irritation, and pulls down her [Girl.Clothes[underwear].name]."
                call expression Girl.tag + "_First_Bottomless" pass (1)
                if Girl == RogueX:
                    ch_r "I wasn't getting anything out of it with those on. Give it another go."
                elif Girl == KittyX:
                    ch_k "It's super annoying not being able to phase you through these."
                elif Girl == EmmaX:
                    ch_e "That was just in the way."
                elif Girl == LauraX:
                    ch_l "I guess all that was in the way."
                elif Girl == JeanX:
                    ch_j "Ok, see if you can make that work, [Girl.player_petname]."
                elif Girl == StormX:
                    ch_s "That should simplify things. . ."
                elif Girl == JubesX:
                    ch_v "Ok, that's a bit more comfortable. . ."
        return


    if approval >= 2:

        $ Girl.change_face("sexy", 1)
        if Girl.forced:
            $ Girl.change_face("sad", 1)
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "obedience", 1)
            call change_Girl_stat(Girl, "inhibition", 1)
        if Girl == RogueX:
            if approval >= 3:
                $ line = "Hmmm, what do you want to see? . ."
            else:
                $ line = "Well, ok. I'd kinda like to keep {i}some{/i} modesty though. . ."
        elif Girl == KittyX:
            if approval >= 3:
                $ line = "Heh, what would you like to see? . ."
            else:
                $ line = "Ok, maybe, but don't push it. . ."
        elif Girl == EmmaX:
            if approval >= 3:
                $ line = "Mmmm, what would you like?"
            else:
                $ line = "What would you have me take off?"
        elif Girl == LauraX:
            if approval >= 3:
                $ line = "What did you want off?"
            else:
                $ line = "Hm, what did you want me to lose?"
        elif Girl == JeanX:
            if approval >= 3:
                $ line = "What did you want off?"
            else:
                $ line = "Like. . . what? . ."
        elif Girl == StormX:
            $ line = "What would you have me remove?"
        elif Girl == JubesX:
            $ line =  "Well like what did you have in mind here?"
        call Bottoms_Off_Legs (Girl)

        if not Girl.Clothes["underwear"] and Girl.recent_history.count("bottomless") < 2:
            call change_Girl_stat(Girl, "obedience", 1)
            call change_Girl_stat(Girl, "obedience", 1)
            call change_Girl_stat(Girl, "inhibition", 3)
            call change_Girl_stat(Girl, "lust", 3)

    elif Girl.Clothes["bottom"] or Girl.Clothes["underwear"] or Girl.Clothes["hose"]:

        $ Girl.change_face("bemused", 1)
        if Girl == RogueX:
            if "no_bottomless" in Girl.recent_history:
                $ Girl.change_face("angry")
                ch_r "What did I just tell you, [Girl.player_petname]?"
            elif "no_topless" in Girl.recent_history:
                $ Girl.change_face("angry")
                ch_r "I doubt your odds will be better here, [Girl.player_petname]. . ."
            elif approval and not Girl.seen_pussy:
                ch_r "Not everything, right?"
            elif not Girl.seen_pussy and "ask topless" in Girl.recent_history:
                ch_r "I'm not ready to show you that either."
            elif "no_bottomless" in Girl.daily_history:
                ch_r "Have you forgot what I said earlier, [Girl.player_petname]?"
            elif taboo:
                ch_r "I don't know about doing it here. . ."
            elif approval:
                ch_r "I don't know if I want to take my bottoms off. . ."
            elif Girl.seen_pussy:
                ch_r "Well, you've seen it before, but. . ."
            else:
                ch_r "I'm not taking my bottoms off."
        elif Girl == KittyX:
            if "no_bottomless" in Girl.recent_history:
                $ KittyX.change_face("angry")
                ch_k "Last warning, [Girl.player_petname]. No."
            elif "no_topless" in Girl.recent_history:
                $ KittyX.change_face("angry")
                ch_k "Not learning from your mistakes here, [Girl.player_petname]. . ."
            elif approval and not Girl.seen_pussy:
                ch_k "I'm not sure about that. . ."
            elif not Girl.seen_pussy and "ask topless" in Girl.recent_history:
                ch_k "That's a bit too far."
            elif "no_bottomless" in Girl.daily_history:
                ch_k "Short memory, [Girl.player_petname]?"
            elif taboo:
                ch_k "This is[Girl.like]kinda public. . ."
            elif approval:
                ch_k "I'm[Girl.like]not sure about this. . ."
            elif Girl.seen_pussy:
                ch_k "Well, you've seen[Girl.like]it before . . ."
            elif Girl.bottom_number(0) > 6:
                ch_k "I'm keeping my pants on."
            elif Girl.bottom_number(0) > 5:
                ch_k "I'm keeping my shorts on."
            else:
                ch_k "I'm keeping my panties on."
        elif Girl == EmmaX:
            if "no_bottomless" in Girl.recent_history:
                $ EmmaX.change_face("angry")
                ch_e "Stop asking, you're embarrassing yourself."
            elif "no_topless" in Girl.recent_history:
                $ EmmaX.change_face("angry")
                ch_e "Do you really think that's likely?"
            elif approval and not Girl.seen_pussy:
                ch_e "I don't know if you're ready for that."
            elif not Girl.seen_pussy and "ask topless" in Girl.recent_history:
                ch_e "Be careful how far you push it. . ."
            elif "no_bottomless" in Girl.daily_history:
                ch_e "Don't you learn anything, [Girl.player_petname]?"
            elif taboo:
                ch_e "Not with so many eyes around, [Girl.player_petname]. . ."
            elif approval:
                ch_e "Probably not. . ."
            elif Girl.seen_pussy:
                ch_e "I think you've seen enough . . ."
            elif Girl.bottom_number(0) > 6:
                ch_e "I'm keeping my pants on."
            elif Girl.bottom_number(0) == 5:
                ch_e "I'm keeping my skirt on."
            elif Girl.bottom_number(0) == 6:
                ch_e "I'm keeping my shorts on."
            else:
                ch_e "I'm keeping my panties on."
        elif Girl == LauraX:
            if "no_bottomless" in Girl.recent_history:
                $ LauraX.change_face("angry")
                ch_l "Now you're just embarrassing yourself."
            elif "no_topless" in Girl.recent_history:
                $ LauraX.change_face("angry")
                ch_l "This is really pushing it."
            elif approval and not Girl.seen_pussy:
                ch_l "I don't know if you're earned that yet."
            elif not Girl.seen_pussy and "ask topless" in Girl.recent_history:
                ch_l "Kinda pushing it, [Girl.player_petname]. . ."
            elif "no_bottomless" in Girl.daily_history:
                ch_l "So thirsty. . ."
            elif taboo:
                ch_l "This is pretty exposed, [Girl.player_petname]. . ."
            elif approval:
                ch_l "Probably not. . ."
            elif Girl.seen_pussy:
                ch_l "You've probably seen enough . . ."
            elif Girl.bottom_number(0) > 6:
                ch_l "Well, I'm keeping my pants on."
            elif Girl.bottom_number(0) == 5:
                ch_l "Well, I'm keeping my skirt on."
            elif Girl.bottom_number(0) == 6:
                ch_l "Well, I'm keeping my shorts on."
            else:
                ch_l "Well, I'm keeping my panties on."
        elif Girl == JeanX:
            if "no_bottomless" in Girl.recent_history:
                $ JeanX.change_face("angry")
                ch_j "Look, it's just not happening."
            elif "no_topless" in Girl.recent_history:
                $ JeanX.change_face("angry")
                ch_j "Why did you think that would be different?"
            elif approval and not Girl.seen_pussy:
                ch_j "Hmm. . . have your earned that. . ."
            elif "no_bottomless" in Girl.daily_history:
                ch_j "Again with this?"
            elif taboo:
                ch_j "Not here, [Girl.player_petname]. . ."
            elif approval:
                ch_j "Hmm. . ."
            elif Girl.seen_pussy:
                ch_j "Hmm. . ."
            elif Girl.bottom_number(0) > 6:
                ch_j "I'm keeping my pants on though."
            elif Girl.bottom_number(0) == 5:
                ch_j "I'm keeping my skirt on though."
            elif Girl.bottom_number(0) == 6:
                ch_j "I'm keeping my shorts on though."
            else:
                ch_j "I'm keeping my panties on though."
        elif Girl == StormX:
            if "no_bottomless" in Girl.recent_history:
                $ StormX.change_face("angry")
                ch_s "You need to stop asking about that."
            elif taboo and Girl not in Rules:
                ch_s "I cannot in public, [Girl.player_petname]. . ."
            elif approval:
                ch_s "I am unsure. . ."
            elif Girl.bottom_number(0) > 6:
                ch_s "I will be keeping my pants on."
            elif Girl.bottom_number(0) == 5:
                ch_s "I will be keeping my skirt on."
            elif Girl.bottom_number(0) == 6:
                ch_s "I will be keeping my shorts on."
            else:
                ch_s "I will be keeping my panties on."
        elif Girl == JubesX:
            if "no_bottomless" in Girl.recent_history:
                $ JubesX.change_face("angry")
                ch_v "Don't have a cow, dude."
            elif "no_topless" in Girl.recent_history:
                $ JubesX.change_face("angry")
                ch_v "Don't push it, [Girl.player_petname]."
            elif approval and not Girl.seen_pussy:
                ch_v "I don't know, man."
            elif not Girl.seen_pussy and "ask topless" in Girl.recent_history:
                ch_v "Kinda pushing it, [Girl.player_petname]. . ."
            elif "no_bottomless" in Girl.daily_history:
                ch_v "So thirsty. . ."
            elif taboo:
                ch_v "[Girl.player_petname], it's just public here?"
            elif approval:
                ch_v "Doubtful. . ."
            elif Girl.seen_pussy:
                ch_v "Need another look?"
            elif Girl.bottom_number(0) > 6:
                ch_v "Well, I'm keeping my pants on."


            elif Girl.bottom_number(0) == 6:
                ch_v "Well, I'm keeping my shorts on."
            else:
                ch_v "Well, I'm keeping my panties on."
        menu:
            extend ""
            "Ok, never mind." if "no_bottomless" not in Girl.recent_history:
                if "ask bottomless" not in Girl.daily_history:
                    call change_Girl_stat(Girl, "lust", 2)
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "inhibition", 3)
                if Girl.forced:
                    $ Girl.mouth = "smile"
                    if Girl == RogueX:
                        ch_r "I really appreciate that."
                    elif Girl == KittyX:
                        ch_k ". . . thank you."
                    elif Girl == EmmaX:
                        ch_e "Very. . . generous."
                    elif Girl == LauraX:
                        ch_l "Right."
                    elif Girl == JeanX:
                        ch_j ". . ."
                    elif Girl == StormX:
                        ch_s "Thank you. . ."
                    elif Girl == JubesX:
                        ch_v "Thanks. . ."
                    if "ask bottomless" not in Girl.daily_history:
                        call change_Girl_stat(Girl, "love", 3)
                        call change_Girl_stat(Girl, "love", 4)
                        call change_Girl_stat(Girl, "inhibition", 2)

            "Sorry, sorry." if "no_bottomless" in Girl.recent_history:
                if Girl == RogueX:
                    ch_r "Ok, fine, just chill out about it."
                elif Girl == KittyX:
                    ch_k "[Girl.Like], fine, whatever."
                else:
                    Girl.voice "Good."
            "Come on, please?":

                if "no_bottomless" in Girl.daily_history:
                    $ Girl.change_face("angry", 1)
                    if Girl == RogueX:
                        ch_r "Listen up when I tell you \"no.\""
                    elif Girl == KittyX:
                        ch_k "I already told you \"no.\""
                    elif Girl == EmmaX:
                        ch_e "I believe you've heard my answer on that."
                    elif Girl == LauraX:
                        ch_l "You heard me."
                    elif Girl == JeanX:
                        ch_j "Are you deaf, or stupid?"
                    elif Girl == StormX:
                        ch_s "I have spoken on the matter."
                    elif Girl == JubesX:
                        ch_v "No."
                else:
                    if approval and approval_check(Girl, 600, "L", taboo_modifier = 1):
                        $ Girl.change_face("sexy", 1)
                        $ D20 = renpy.random.randint(1, 3)
                        $ approval += 1 if D20 == 3 else 0
                        if Girl == RogueX:
                            $ line = "Well, what were you thinking then. . ."
                        elif Girl == KittyX:
                            $ line = "I guess. . ."
                        elif Girl == EmmaX:
                            $ line = "Perhaps. . ."
                        elif Girl == LauraX:
                            $ line = "Maybe. . ."
                        elif Girl == JeanX:
                            $ line = "-sigh-. . . like what?"
                        elif Girl == StormX:
                            ch_s ". . ."
                            $ line = "What did you want? . ."
                        elif Girl == JubesX:
                            $ line =  "I mean, maaaybe. . ."
                        call Bottoms_Off_Legs (Girl)
                    else:
                        $ Girl.change_face("sexy")
                        call bottoms_off_refused(Girl, counter)

            "It doesn't have to be everything. . ." if Girl.Clothes["bottom"] or Girl.Clothes["hose"] == "tights" or Girl.Clothes["underwear"] == "shorts":
                if approval and "no_bottomless" not in Girl.daily_history:
                    $ Girl.change_face("bemused", 1)
                    $ line = "Well what did you have in mind then?"
                    call Bottoms_Off_Legs (Girl)
                else:

                    $ Girl.change_face("sexy")
                    call bottoms_off_refused(Girl, counter)
            "It doesn't have to be everything. . . (locked)" if not Girl.Clothes["bottom"] and Girl.Clothes["hose"] != "pantyhose" and Girl.Clothes["underwear"] != "shorts":
                pass
            "No, lose 'em.":

                if (approval and Girl.obedience >= 250) or (approval_check(Girl, 850, "OI", taboo_modifier = 5) and approval_check(Girl, 400, "O")):
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "obedience", 4)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    if Girl == RogueX:
                        $ line =  "Fine, if that's what you want. What do you want to see?"
                    elif Girl == KittyX:
                        $ line =  "Like geez, you're serious. . ."
                    elif Girl == EmmaX:
                        $ line =  "Don't test me. . ."
                    elif Girl == LauraX:
                        $ line =  "Don't push me. . ."
                    elif Girl == JeanX:
                        $ line = "Think very carefully. . ."
                    elif Girl == StormX:
                        ch_s ". . ."
                        $ line = "What did you want? . ."
                    elif Girl == JubesX:
                        $ line =  "Tone. . ."
                    $ approval = 1 if approval < 1 else approval
                    $ Girl.forced = 1
                    call Bottoms_Off_Legs (Girl)
                else:
                    call change_Girl_stat(Girl, "love", -10)
                    if approval_check(Girl, 400, "O"):
                        if Girl == RogueX:
                            ch_r "I. . . I really can't."
                        elif Girl == KittyX:
                            ch_k "Sorry[Girl.like]no way."
                        elif Girl == EmmaX:
                            ch_e "Definitely not."
                        elif Girl == LauraX:
                            ch_l "No way."
                        elif Girl == JeanX:
                            ch_j "Ha! No."
                        elif Girl == StormX:
                            ch_s "I am sorry, no."
                        elif Girl == JubesX:
                            ch_v "Definitely not."
                    else:
                        $ Girl.change_face("angry")
                        if Girl == RogueX:
                            ch_r "Well fuck off then!"
                        elif Girl == KittyX:
                            ch_k "GTFO."
                        elif Girl == EmmaX:
                            ch_e "Out of my sight, [Girl.player_petname]."
                        elif Girl == LauraX:
                            ch_l "Fuck off."
                        elif Girl == JeanX:
                            ch_j "Not even."
                        elif Girl == StormX:
                            ch_s "No."
                        elif Girl == JubesX:
                            ch_v "Nah. . ."
                        $ Girl.recent_history.append("angry")
                        $ Girl.daily_history.append("angry")
                    $ Girl.recent_history.append("no_bottomless")
                    $ Girl.daily_history.append("no_bottomless")

    $ approval_bonus = 0
    $ Girl.recent_history.append("ask bottomless")
    $ Girl.daily_history.append("ask bottomless")
    return

label Bottoms_Off_Legs(Girl):
    $ shift_focus (Girl)

    if Girl.forced:
        $ Girl.change_face("sad", 1)
    elif approval_check(Girl, 1100, "OI", taboo_modifier = 3):
        $ Girl.change_face("sly")
    elif approval_check(Girl, 1400, taboo_modifier = 3):
        $ Girl.change_face("sexy", 1)
    else:
        $ Girl.change_face("bemused", 1)

    $ line = "Well what did you want off?" if not line else line
    $ counter = 1

    while Girl.Outfit.pussy_covered and counter:
        menu:
            Girl.voice "[line]"
            "Take it all off." if line != "Well what did you have in mind then?":
                if not Girl.Clothes["underwear"] and "pussy" not in Girl.Clothes["hose"].covers:
                    call no_panties_on(Girl, counter)

                    if not _return:
                        return

                if Girl.Clothes["pants"] or Girl.Clothes["skirt"]:
                    $ Girl.Outfit.remove_Clothing("pants")
                    $ Girl.Outfit.remove_Clothing("skirt")

                    if not Girl.seen_underwear:
                        $ Girl.seen_underwear = True

                if approval < 2 and not Girl.Clothes["underwear"] and "pussy" not in Girl.Clothes["hose"].hides:
                    call no_panties_on(Girl, counter)

                    if not _return:
                        return

                if Girl.Clothes["jacket"] and Girl.Clothes["jacket"].state == -1:
                    $ Girl.take_off("jacket")

                if Girl.Clothes["hose"]:
                    $ Girl.take_off("hose")

                if approval < 2:
                    call no_panties_on(Girl, counter)

                    if not _return:
                        return

                if Girl.Clothes["underwear"]:
                    $ Girl.take_off("underwear")

                call expression Girl.tag + "_First_Bottomless"
            "Lose the [Girl.Clothes[bottom].name]." if Girl.Clothes["bottom"]:
                if Girl.Clothes["underwear"] and approval >= 2:
                    $ Girl.change_face("sexy")

                    if Girl == RogueX:
                        ch_r "I guess I could do that. . ."
                    elif Girl == KittyX:
                        ch_k "That's. . . doable. . ."
                    elif Girl == EmmaX:
                        ch_e "I can manage that. . ."
                    elif Girl == LauraX:
                        ch_l "I guess I could. . ."
                    elif Girl == JeanX:
                        ch_j ". . .I guess. . ."
                    elif Girl == StormX:
                        ch_s "I could do that. . ."
                    elif Girl == JubesX:
                        ch_v "Well, I could do that. . ."
                elif approval:
                    $ Girl.change_face("sexy", 1)

                    if approval < 2 and not Girl.Clothes["underwear"] and Girl.Clothes["hose"] != "pantyhose":
                        call no_panties_on(Girl, counter)

                        if not _return:
                            return
                else:
                    $ Girl.change_face("sexy")

                    call bottoms_off_refused(Girl, counter)

                    return

                $ line = Girl.Clothes["bottom"]
                $ Girl.Outfit.remove_Clothing(["pants", "skirt"])
                if not Girl.Clothes["underwear"] and Girl.Clothes["hose"] != "pantyhose":
                    $ Girl.change_face("sly", 2)
                    if Girl == KittyX:
                        "She blushes and looks at you as her [line] drops at her feet."
                    elif Girl == RogueX:
                        "She blushes and looks at you slyly before removing her [line]."
                    else:
                        "She glaces at you slyly before removing her [line]."
                    call expression Girl.tag + "_First_Bottomless"
                elif not Girl.seen_underwear:
                    if Girl == KittyX:
                        "She blushes and looks at you as her [line] drops at her feet."
                    elif Girl == RogueX:
                        "She blushes and looks at you slyly before removing her [line]."
                    else:
                        "She glaces at you slyly before removing her [line]."
                    $ Girl.seen_underwear = 1
                else:
                    "[Girl.name] pulls her [line] off."
                $ Girl.change_face("bemused", 1)

            "Lose the [Girl.Clothes[underwear].name]." if Girl.Clothes["underwear"]:
                if approval < 2:
                    if Girl == RogueX:
                        ch_r "No thanks, [Girl.player_petname]."
                    elif Girl == KittyX:
                        ch_k "Sorry, no."
                    elif Girl == EmmaX:
                        ch_e "I'm afraid not."
                    elif Girl == LauraX:
                        ch_l "No way."
                    elif Girl == JeanX:
                        ch_j "Ha! No way."
                    elif Girl == StormX:
                        ch_s "I would rather not."
                    elif Girl == JubesX:
                        ch_v "Um, no thanks. . ."
                    $ Girl.recent_history.append("no_bottomless")
                    $ Girl.daily_history.append("no_bottomless")
                    return
                elif Girl.wearing_pants or Girl.hose_number() >= 6:
                    if Girl == RogueX:
                        ch_r "A little backwards, but sure. . ."
                    elif Girl == KittyX:
                        ch_k "[Girl.Like]I guess. . ."
                    elif Girl == EmmaX:
                        ch_e "I suppose that I could. . ."
                    elif Girl == LauraX:
                        ch_l "Huh, ok. . ."
                    elif Girl == JeanX:
                        ch_j "Hmm. . . I guess. . ."
                    elif Girl == StormX:
                        ch_s "I could do that. . ."
                    elif Girl == JubesX:
                        ch_v "Well, I could do that. . ."
                else:
                    if Girl == EmmaX:
                        ch_e "Of course."
                    elif Girl == LauraX:
                        ch_l "Huh, ok. . ."
                    elif Girl == StormX:
                        ch_s "Fine."
                    else:
                        Girl.voice "Ok, sure, [Girl.player_petname]."
                $ line = Girl.Clothes["underwear"]
                $ Girl.take_off("underwear")
                if Girl == KittyX:
                    if Girl.bottom_number() >= 5:
                        "She reaches a hand into her [Girl.Clothes[bottom].name] and pulls her [line] out through the pocket."
                        "She gives a little wink as she drops them to the ground."
                    elif Girl.Clothes["hose"] in ["tights", "pantyhose"]:
                        "She reaches a hand into her [Girl.Clothes[hose].name] and pulls her [line] out through the pocket."
                        "She gives a little wink as she drops them to the ground."
                    else:
                        "With a little shimmy, her [line] drop to the ground."
                elif Girl.wearing_pants:
                    "She pulls her [Girl.Clothes[bottom].name] off, then removes her [line], before putting them back on."
                elif Girl.hose_number() >= 6:
                    "She pulls her [Girl.Clothes[hose].name] off, then removes her [line], before putting them back on."
                elif Girl == JubesX and JubesX.Clothes["jacket"] == "closed_jacket":
                    "She reaches under her jacket and pulls her [line] down."
                elif Girl.Clothes["bottom"]:
                    "She reaches under her [Girl.Clothes[bottom].name] and pulls her [line] down."
                else:
                    "She glances up at you as she removes her [line]."
                call expression Girl.tag + "_First_Bottomless"

            "Just give me a clear view. . ." if (Girl.Clothes["underwear"] and not Girl.Clothes["underwear"].state) or (Girl.Clothes["bottom"] and not Girl.upskirt):
                if approval >= 2:
                    if Girl == LauraX:
                        ch_l "Whatever."
                    else:
                        Girl.voice "Fine."

                    $ Girl.expose_pussy(Girl)

                    if Girl.Clothes["bottom"]:
                        "She shifts her [Girl.Clothes[bottom].name] out of the way."
                    else:
                        "She shifts her [Girl.Clothes[underwear].name] out of the way."
                elif approval >= 1 and Girl.Clothes["bottom"] and Girl.Clothes["underwear"] and not Girl.Clothes["underwear"] and approval >= 1 and Girl.Clothes["bottom"] and Girl.Clothes["underwear"] and not Girl.Clothes["underwear"].state:
                    if Girl == RogueX:
                        ch_r "I'll show you a little bit. . ."
                    elif Girl == KittyX:
                        ch_k "I guess I could show you something. . ."
                    elif Girl == EmmaX:
                        ch_e "I'll give at least give a little view. . ."
                    elif Girl == LauraX:
                        ch_l "Make do with this. . ."
                    elif Girl == JeanX:
                        ch_j "This should be plenty, [Girl.player_petname]."
                    elif Girl == StormX:
                        ch_s "I have taken off enough. . ."
                    elif Girl == JubesX:
                        ch_v "I guess. . . how 'bout this. . ."
                    $ Girl.upskirt = True
                else:
                    Girl.voice "No."
                    $ Girl.recent_history.append("no_bottomless")
                    $ Girl.daily_history.append("no_bottomless")
                    return
                call expression Girl.tag + "_First_Bottomless"

            "Lose the [Girl.Clothes[hose].name]." if Girl.Clothes["hose"]:
                $ Girl.change_face("bemused", 1)
                if Girl.Clothes["bottom"]:
                    Girl.voice "All right, fine."
                elif approval < 2 and not Girl.Clothes["underwear"] and Girl.Clothes["hose"] == "tights":
                    call no_panties_on(Girl, counter)

                    if not _return:
                        return
                elif not approval and Girl.hose_number() >= 6:
                    if Girl == RogueX:
                        ch_r "No thanks, [Girl.player_petname]."
                    else:
                        Girl.voice "Sorry, no, [Girl.player_petname]."
                    return
                else:
                    if Girl == RogueX:
                        ch_r "Ok, sure, [Girl.player_petname]."
                    else:
                        Girl.voice "Fine, [Girl.player_petname]."
                $ line = Girl.Clothes["hose"]
                $ Girl.take_off("hose")
                if Girl == KittyX:
                    if Girl.bottom_number() >= 5:
                        "She reaches a hand into her [Girl.Clothes[bottom].name] and pulls her [line] right through her legs."
                        "She makes a little flourish and drops them to the ground."
                    else:
                        "She gives a little shake and her [line] drop to the ground."
                elif Girl.wearing_pants:
                    "She pulls off her [Girl.Clothes[bottom].name] and pulls her [line] off, then puts them back on."
                elif Girl.Clothes["bottom"]:
                    "She reaches under her [Girl.Clothes[bottom].name] and pulls her [line] down."
                elif Girl.Clothes["hose"] != "pantyhose":
                    "[Girl.name] pulls her [line] off."
                elif not Girl.Clothes["underwear"]:
                    $ Girl.change_face("sly", 2)
                    "She blushes and looks at you slyly before removing her [line]."
                    $ Girl.blushing = "_blush1"
                    call expression Girl.tag + "_First_Bottomless"
                elif not Girl.seen_underwear:
                    "[Girl.name] shyly removes her [line]."
                    $ Girl.seen_underwear = 1
                else:
                    "[Girl.name] pulls her [line] off."

            "Rip the [Girl.Clothes[hose].name]." if Girl.Clothes["hose"] == "pantyhose" or Girl.Clothes["hose"] == "tights":
                $ Girl.change_face("bemused", 1)
                if Girl.Clothes["bottom"]:
                    Girl.voice "All right, fine."
                elif approval < 2 and not Girl.Clothes["underwear"] and Girl.Clothes["hose"] == "tights":
                    call no_panties_on(Girl, counter)

                    if not _return:
                        return
                elif not approval and Girl.hose_number() >= 6:
                    if Girl == RogueX:
                        ch_r "I'd rather you didn't, [Girl.player_petname]."
                    else:
                        Girl.voice "Sorry, no, [Girl.player_petname]."
                    return

                $ line = Girl.Clothes["hose"]
                if Girl.Clothes["hose"] == "tights":
                    $ Girl.Clothes["hose"] = "ripped_tights"
                elif Girl.Clothes["hose"] == "pantyhose":
                    $ Girl.Clothes["hose"] = "ripped_pantyhose"
                if Girl.Clothes["hose"] not in Girl.inventory:
                    $ Girl.inventory.append(Girl.Clothes["hose"])
                $ Girl.add_word(1, "ripped", "ripped")
                "You tear holes in her [line]."
                if not approval_check(Girl, 1200, taboo_modifier=0):
                    $ Girl.change_face("angry", 1, eyes = "down")
                    if Girl == RogueX:
                        ch_r "Dammit, [Girl.player_petname], those are gettin expensive!"
                    elif Girl == KittyX:
                        ch_k "Hey, I was using those!"
                    elif Girl == EmmaX:
                        ch_e "I hope you're paying for those."
                    elif Girl == LauraX:
                        ch_l "Hey. Not cool."
                    elif Girl == JeanX:
                        ch_j "Oh, whatever."
                    elif Girl == StormX:
                        ch_s "Those do not grow on trees. . ."
                    elif Girl == JubesX:
                        ch_v "Hey! You'd better replace those. . ."
                    $ Girl.change_face("bemused", 1)

            "Why don't you lose the sweater?" if Girl.Clothes["belt"] == "sweater":
                $ Girl.take_off("belt")
                "[Girl.name] tosses her sweater off."

            "Keep it all on for now." if counter == 1:
                $ counter = 0

            "Ok, that's enough for now." if counter == 2:
                $ counter = 0

        $ counter = 2 if counter else counter

        $ line = "Anything else?"

    return
