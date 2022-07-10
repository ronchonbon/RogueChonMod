label Jean_Relationship:
    while True:
        menu:
            ch_j "What did you want to talk about?"
            "Do you want to be my girlfriend?" if JeanX not in Player.Harem and "ex" not in JeanX.traits:
                $ JeanX.daily_history.append("relationship")
                if "asked boyfriend" in JeanX.daily_history and "angry" in JeanX.daily_history:
                    $ JeanX.change_face("angry", 1)
                    ch_j "Again with this? No!"
                    return
                elif "asked boyfriend" in JeanX.daily_history:
                    $ JeanX.change_face("angry", 1)
                    ch_j "Still no."
                    return
                elif JeanX.broken_up[0]:
                    $ JeanX.change_face("angry", 1)
                    ch_j "You have to be kidding."
                    if Player.Harem:
                        $ JeanX.daily_history.append("asked boyfriend")
                        return
                    else:
                        ch_p "I'm serious."

                $ JeanX.daily_history.append("asked boyfriend")

                if Player.Harem and "JeanYes" not in Player.traits:
                    if len(Player.Harem) >= 2:
                        ch_j "Hey, apparently it's those other girls' problem, [JeanX.player_petname]."
                    else:
                        ch_j "Hey, apparently it's [Player.Harem[0].name]'s problem, [JeanX.player_petname]."
                    return

                if JeanX.event_happened[5]:
                    $ JeanX.change_face("bemused", 1)
                    ch_j "Hey, you were the one that said \"no\". . ."
                else:
                    $ JeanX.change_face("surprised", 2)
                    ch_j "What? Why?"
                    $ JeanX.change_face("smile", 1)

                call Jean_OtherWoman

                if JeanX.love >= 800:
                    $ JeanX.change_face("surprised", 1)
                    $ JeanX.mouth = "smile"
                    call change_Girl_stat(JeanX, "love", 40)
                    ch_j "Huh. Ok."
                    if "boyfriend" not in JeanX.player_petnames:
                        $ JeanX.player_petnames.append("boyfriend")
                    if "JeanYes" in Player.traits:
                        $ Player.traits.remove("JeanYes")
                    $ Player.Harem.append(JeanX)
                    call Harem_Initiation
                    "[JeanX.name] floats in and kisses you deeply."
                    $ JeanX.change_face("kiss", 1)
                    $ JeanX.permanent_History["kiss"] += 1
                elif JeanX.obedience >= 500:
                    $ JeanX.change_face("perplexed")
                    ch_j "\"Dating\". . . I mean. . ."
                    ch_j "That's not really what this is. . ."
                elif JeanX.inhibition >= 500:
                    $ JeanX.change_face("smile")
                    ch_j "-No-."
                else:
                    $ JeanX.change_face("perplexed", 1)
                    ch_j "Relax there, [JeanX.player_petname]."

            "Do you want to get back together?" if "ex" in JeanX.traits:
                $ JeanX.daily_history.append("relationship")
                if "asked boyfriend" in JeanX.daily_history and "angry" in JeanX.daily_history:
                    $ JeanX.change_face("angry", 1)
                    ch_j "Again with this? No!"
                    return
                elif "asked boyfriend" in JeanX.daily_history:
                    $ JeanX.change_face("angry", 1)
                    ch_j "Still no."
                    return

                $ JeanX.daily_history.append("asked boyfriend")

                if Player.Harem and "JeanYes" not in Player.traits:
                    if len(Player.Harem) >= 2:
                        ch_j "Hey, apparently it's those other girls' problem, [JeanX.player_petname]."
                    else:
                        ch_j "Hey, apparently it's [Player.Harem[0].name]'s problem, [JeanX.player_petname]."
                    return

                $ counter = 0
                call Jean_OtherWoman

                if JeanX.love >= 800:
                    $ JeanX.change_face("surprised", 1)
                    $ JeanX.mouth = "smile"
                    call change_Girl_stat(JeanX, "love", 5)
                    ch_j "Oh, fine, whatever."
                    if "boyfriend" not in JeanX.player_petnames:
                        $ JeanX.player_petnames.append("boyfriend")
                    $ JeanX.traits.remove("ex")
                    if "JeanYes" in Player.traits:
                        $ Player.traits.remove("JeanYes")
                    $ Player.Harem.append(JeanX)
                    call Harem_Initiation
                    "[JeanX.name] floats in and kisses you."
                    $ JeanX.change_face("kiss", 1)
                    $ JeanX.permanent_History["kiss"] += 1
                elif JeanX.love >= 600 and approval_check(JeanX, 1500):
                    $ JeanX.change_face("smile", 1)
                    call change_Girl_stat(JeanX, "love", 5)
                    ch_j "Sure, whatever."
                    if "boyfriend" not in JeanX.player_petnames:
                        $ JeanX.player_petnames.append("boyfriend")
                    $ JeanX.traits.remove("ex")
                    if "JeanYes" in Player.traits:
                        $ Player.traits.remove("JeanYes")
                    $ Player.Harem.append(JeanX)
                    call Harem_Initiation
                    $ JeanX.change_face("kiss", 1)
                    "[JeanX.name] gives you a quick kiss."
                    $ JeanX.change_face("sly", 1)
                    $ JeanX.permanent_History["kiss"] += 1
                elif JeanX.obedience >= 500:
                    $ JeanX.change_face("sad")
                    ch_j "That's not really where we're at."
                elif JeanX.inhibition >= 500:
                    $ JeanX.change_face("perplexed")
                    ch_j "That's no fun."
                else:
                    $ JeanX.change_face("perplexed", 1)
                    ch_j "Um, no."



            "I wanted to ask about [[another girl]" if JeanX in Player.Harem:
                call AskDateOther

            "I think we should break up." if JeanX in Player.Harem:
                if "breakup talk" in JeanX.recent_history:
                    ch_j "I'm pretty sure we already covered that."
                elif "breakup talk" in JeanX.daily_history:
                    ch_j "Silly rabbit."
                    ch_j "Not today, [JeanX.player_petname]."
                else:
                    call Breakup (JeanX)
            "About that talk we had before. . .":

                menu:
                    "Never mind":




















                        pass
            "Never mind":

                return

    return

label Jean_OtherWoman(counter=0):

    if not Player.Harem:
        return
    $ counter = int((JeanX.likes[Player.Harem[0].tag] - 500)/2)

    $ JeanX.change_face("perplexed")
    if len(Player.Harem) >= 2:
        ch_j "Aren't you hanging out with. . . [Player.Harem[0].name] right now?"
        ch_j "And that's not all, if I'm reading the room right."
    else:
        ch_j "Aren't you hanging out with. . . [Player.Harem[0].name] right now?"
    menu:
        extend ""
        "She said I can be with you too." if "JeanYes" in Player.traits:
            if approval_check(JeanX, 1800, Bonus = counter):
                $ JeanX.change_face("smile", 1)
                if JeanX.love >= JeanX.obedience:
                    ch_j "Oh, well ok then."
                elif JeanX.obedience >= JeanX.inhibition:
                    ch_j "Smooth."
                else:
                    ch_j "Oh, cool."
            else:
                $ JeanX.change_face("smile", 1)
                ch_j "Lol, cuck."



        "I could ask if she'd be ok with me dating you both." if "JeanYes" not in Player.traits:
            if approval_check(JeanX, 1800, Bonus = counter):
                $ JeanX.change_face("smile", 1)
                if JeanX.love >= JeanX.obedience:
                    ch_j "Probably a good idea."
                elif JeanX.obedience >= JeanX.inhibition:
                    ch_j "Uh-huh. . ."
                else:
                    ch_j "bawk, bawkbawk baawk."
                ch_j "Fine, ask her and let me know in the morning."
            else:
                $ JeanX.change_face("smile", 1)
                ch_j "Lol, I bet she would. . ."
            $ renpy.pop_call()
        "What she doesn't know won't hurt her.":









            $ JeanX.change_face("smile", 1)
            if JeanX.love >= JeanX.obedience:
                ch_j "True. . ."
            elif JeanX.obedience >= JeanX.inhibition:
                ch_j "Hmm. . ."
            else:
                ch_j "Lol, true."
            $ JeanX.traits.append("downlow")
        "I can break it off with her.":

            $ JeanX.change_face("sad")
            ch_j "Yeah, get on that."
            $ renpy.pop_call()
        "You're right, I was dumb to ask.":

            $ JeanX.change_face("sad")
            ch_j "Definitely."
            $ renpy.pop_call()

    return


label Jean_About(Check=0):
    if Check not in all_Girls:
        ch_j "Who?"
        return
    ch_j "What do I think about [Check.name]? Huh. . ."
    if Check == RogueX:
        if "poly Rogue" in JeanX.traits:
            ch_j "I mean, she's a pretty good lay. . ."
        elif JeanX.likes[RogueX.tag] >= 900:
            ch_j "She is kinda sexy. . ."
        elif JeanX.likes[RogueX.tag] >= 800:
            ch_j "I don't know, she's fine. . ."
        elif JeanX.likes[RogueX.tag] >= 700:
            ch_j "She's good in class or something?"
        elif JeanX.likes[RogueX.tag] >= 600:
            ch_j "She's the one with the white stripe, right?"
        elif JeanX.likes[RogueX.tag] >= 500:
            ch_j "Who?"
        elif JeanX.likes[RogueX.tag] >= 400:
            ch_j "I don't spend much time thinking about her."
        elif JeanX.likes[RogueX.tag] >= 300:
            ch_j "She can go to hell."
        else:
            ch_j "Bitch."
    elif Check == KittyX:
        if "poly Kitty" in JeanX.traits:
            ch_j "I mean, she's a pretty good lay. . ."
        elif JeanX.likes[KittyX.tag] >= 900:
            ch_j "She is kinda cute. . ."
        elif JeanX.likes[KittyX.tag] >= 800:
            ch_j "I don't know, she's fine. . ."
        elif JeanX.likes[KittyX.tag] >= 700:
            ch_j "She's, uh, a jock or something?"
        elif JeanX.likes[KittyX.tag] >= 600:
            ch_j "She's the one with the tiny tits, right? Ghost girl?"
        elif JeanX.likes[KittyX.tag] >= 500:
            ch_j "Who?"
        elif JeanX.likes[KittyX.tag] >= 400:
            ch_j "I don't spend much time thinking about her."
        elif JeanX.likes[KittyX.tag] >= 300:
            ch_j "She can go to hell."
        else:
            ch_j "Bitch."
    elif Check == EmmaX:
        if "poly Emma" in JeanX.traits:
            ch_j "I mean, she's an amazing lay. . ."
        elif JeanX.likes[EmmaX.tag] >= 900:
            ch_j "She is pretty thicc. . ."
        elif JeanX.likes[EmmaX.tag] >= 800:
            ch_j "I don't know, she's fine. . ."
        elif JeanX.likes[EmmaX.tag] >= 700:
            ch_j "She's prety hot, for an old."
        elif JeanX.likes[EmmaX.tag] >= 600:
            ch_j "She's the teacher, right?"
        elif JeanX.likes[EmmaX.tag] >= 500:
            ch_j "Who? Oh, the teacher, right?"
        elif JeanX.likes[EmmaX.tag] >= 400:
            ch_j "I could do with less of her attitude."
        elif JeanX.likes[EmmaX.tag] >= 300:
            ch_j "She needs to mind her business."
        else:
            ch_j "Grrrrr."
    elif Check == LauraX:
        if "poly Laura" in JeanX.traits:
            ch_j "I mean, she's a pretty good lay. . ."
        elif JeanX.likes[LauraX.tag] >= 900:
            ch_j "She is pretty fit. . ."
        elif JeanX.likes[LauraX.tag] >= 800:
            ch_j "I don't know, she's fine. . ."
        elif JeanX.likes[LauraX.tag] >= 700:
            ch_j "She's good in class or something?"
        elif JeanX.likes[LauraX.tag] >= 600:
            ch_j "She's the one with the claws, right?"
        elif JeanX.likes[LauraX.tag] >= 500:
            ch_j "Who?"
        elif JeanX.likes[LauraX.tag] >= 400:
            ch_j "I don't spend much time thinking about her."
        elif JeanX.likes[LauraX.tag] >= 300:
            ch_j "She can go to hell."
        else:
            ch_j "Bitch."
    elif Check == StormX:
        if "poly Storm" in JeanX.traits:
            ch_j "She's so squishy!"
        elif JeanX.likes[StormX.tag] >= 900:
            ch_j "She's. . . hot."
        elif JeanX.likes[StormX.tag] >= 800:
            ch_j "I don't know, she's fine. . ."
        elif JeanX.likes[StormX.tag] >= 700:
            ch_j "She's prety hot, for an old."
        elif JeanX.likes[StormX.tag] >= 600:
            ch_j "She's the teacher, right?"
        elif JeanX.likes[StormX.tag] >= 500:
            ch_j "Who? Oh, the teacher, right?"
        elif JeanX.likes[StormX.tag] >= 400:
            ch_j "I could do with less of her attitude."
        elif JeanX.likes[StormX.tag] >= 300:
            ch_j "She needs to mind her business."
        else:
            ch_j "Grrrrr."
    elif Check == JubesX:
        if "poly Jubes" in JeanX.traits:
            ch_j "I mean, she's a pretty good lay. . ."
        elif JeanX.likes[JubesX.tag] >= 900:
            ch_j "She is kinda cute. . ."
        elif JeanX.likes[JubesX.tag] >= 800:
            ch_j "I don't know, she's fine. . ."
        elif JeanX.likes[JubesX.tag] >= 700:
            ch_j "I think I saw her around. . ."
        elif JeanX.likes[JubesX.tag] >= 600:
            ch_j "She's the vampire, right?"
        elif JeanX.likes[JubesX.tag] >= 500:
            ch_j "Who?"
        elif JeanX.likes[JubesX.tag] >= 400:
            ch_j "I don't spend much time thinking about her."
        elif JeanX.likes[JubesX.tag] >= 300:
            ch_j "She can get staked."
        else:
            ch_j "Bitch."
    return


label Jean_Monogamy:

    menu:
        "Could you not hook up with other girls?" if "monogamous" not in JeanX.traits:
            if JeanX.thirst >= 60 and not approval_check(JeanX, 1700, "LO", taboo_modifier=0):

                $ JeanX.change_face("sly", 1)
                if "monogamous" not in JeanX.daily_history:
                    call change_Girl_stat(JeanX, "obedience", -2)
                ch_j "Sorry, I've got plans later."
                return
            elif approval_check(JeanX, 1200, "LO", taboo_modifier=0) and JeanX.love >= JeanX.obedience:

                $ JeanX.change_face("sly", 1)
                if "monogamous" not in JeanX.daily_history:
                    call change_Girl_stat(JeanX, "love", 1)
                ch_j "Oh, jealous?"
                ch_j "Ok, fine, but you owe me. . ."
            elif approval_check(JeanX, 700, "O", taboo_modifier=0):

                $ JeanX.change_face("sly", 1, eyes = "side")
                ch_j "Well. . . ok, fine."
            else:

                $ JeanX.change_face("sly", 1)
                ch_j "Ha!"
                return
            if "monogamous" not in JeanX.daily_history:
                call change_Girl_stat(JeanX, "obedience", 3)
            $ JeanX.add_word(1, 0, "monogamous")
            $ JeanX.traits.append("monogamous")
        "Don't hook up with other girls." if "monogamous" not in JeanX.traits:
            if approval_check(JeanX, 900, "O", taboo_modifier=0):

                $ JeanX.change_face("sly", 1, eyes = "side")
                ch_j "Well. . . ok, fine."
            elif JeanX.thirst >= 60 and not approval_check(JeanX, 1700, "LO", taboo_modifier=0):

                $ JeanX.change_face("sly", 1)
                if "monogamous" not in JeanX.daily_history:
                    call change_Girl_stat(JeanX, "obedience", -2)
                ch_j "Sorry, I've got plans later."
                return
            elif approval_check(JeanX, 600, "O", taboo_modifier=0):

                $ JeanX.change_face("sly", 1, eyes = "side")
                ch_j "Well. . . ok, fine."
            elif approval_check(JeanX, 1400, "LO", taboo_modifier=0):

                $ JeanX.change_face("sly", 1)
                ch_j "Oh, jealous?"
                ch_j "Ok, fine, but you owe me. . ."
            else:

                $ JeanX.change_face("sly", 1, brows = "confused")
                ch_j "Ha!"
                return
            if "monogamous" not in JeanX.daily_history:
                call change_Girl_stat(JeanX, "obedience", 3)
            $ JeanX.add_word(1, 0, "monogamous")
            $ JeanX.traits.append("monogamous")
        "It's ok if you hook up with other girls." if "monogamous" in JeanX.traits:
            if approval_check(JeanX, 700, "O", taboo_modifier=0):
                $ JeanX.change_face("sly", 1, eyes = "side")
                ch_j ". . . good."
            elif approval_check(JeanX, 800, "L", taboo_modifier=0):
                $ JeanX.change_face("sly", 1)
                ch_j "Ok. . ."
            else:
                $ JeanX.change_face("sly", 1, brows = "confused")
                if "monogamous" not in JeanX.daily_history:
                    call change_Girl_stat(JeanX, "love", -2)
                ch_j "Good to know. . ."
            if "monogamous" not in JeanX.daily_history:
                call change_Girl_stat(JeanX, "obedience", 3)
            if "monogamous" in JeanX.traits:
                $ JeanX.traits.remove("monogamous")
            $ JeanX.add_word(1, 0, "monogamous")
        "Never mind.":
            pass
    return



label Jean_Jumped:

    ch_p "Hey, Remember that time you threw yourself at me?"
    $ JeanX.change_face("sly", 1, brows = "confused")
    ch_j "I'm not sure I'd put it like that, but. . . yeah?"
    menu:
        ch_j ". . . yeah?"
        "Could you maybe just ask instead?" if "chill" not in JeanX.traits:
            if JeanX.thirst >= 60 and not approval_check(JeanX, 1500, "LO", taboo_modifier=0):

                $ JeanX.change_face("sly", 1)
                if "chill" not in JeanX.daily_history:
                    call change_Girl_stat(JeanX, "obedience", -2)
                ch_j "Why waste the time?"
                ch_j "It's not like you'd say \"no.\""
                return
            elif approval_check(JeanX, 1000, "LO", taboo_modifier=0) and JeanX.love >= JeanX.obedience:

                $ JeanX.change_face("surprised", 1)
                if "chill" not in JeanX.daily_history:
                    call change_Girl_stat(JeanX, "love", 1)
                ch_j "I was really horny though. . ."
                $ JeanX.change_face("sly", 1, eyes = "side")
                ch_j "I'll give it some thought. . ."
            elif approval_check(JeanX, 500, "O", taboo_modifier=0):

                $ JeanX.change_face("sly", 1, eyes = "side")
                ch_j "Maybe. . ."
            else:

                $ JeanX.change_face("sly", 1)
                ch_j "Why waste the time?"
                ch_j "It's not like you'd say \"no.\""
                return
            if "chill" not in JeanX.daily_history:
                call change_Girl_stat(JeanX, "obedience", 3)
            $ JeanX.add_word(1, 0, "chill")
            $ JeanX.traits.append("chill")
        "Don't bother me like that." if "chill" not in JeanX.traits:
            if approval_check(JeanX, 800, "O", taboo_modifier=0):

                $ JeanX.change_face("sly", 1, eyes = "side")
                ch_j ". . . fine. . ."
            elif JeanX.thirst >= 60 and not approval_check(JeanX, 500, "O", taboo_modifier=0):

                $ JeanX.change_face("sly", 1)
                if "chill" not in JeanX.daily_history:
                    call change_Girl_stat(JeanX, "obedience", -2)
                ch_j "Why waste the time?"
                ch_j "It's not like you'd say \"no.\""
                return
            elif approval_check(JeanX, 400, "O", taboo_modifier=0):

                $ JeanX.change_face("sly", 1, eyes = "side")
                ch_j "Well. . . ok. . ."
            elif approval_check(JeanX, 500, "LO", taboo_modifier=0) and not approval_check(JeanX, 500, "I", taboo_modifier=0):

                $ JeanX.change_face("sly", 1)
                ch_j "Rude."
                ch_j "I guess I cna try though. . ."
            else:

                $ JeanX.change_face("sly", 1)
                ch_j "Why waste the time?"
                ch_j "It's not like you'd say \"no.\""
                return
            if "chill" not in JeanX.daily_history:
                call change_Girl_stat(JeanX, "obedience", 3)
            $ JeanX.add_word(1, 0, "chill")
            $ JeanX.traits.append("chill")
        "Knock yourself out.":
            if approval_check(JeanX, 800, "L", taboo_modifier=0):
                $ JeanX.change_face("sly", 1)
                ch_j "Heh, you know how I think. . ."
            elif approval_check(JeanX, 700, "O", taboo_modifier=0):
                $ JeanX.change_face("sly", 1, eyes = "side")
                ch_j "Good to know."
            else:
                $ JeanX.change_face("sly", 1, brows = "confused")
                if "chill" not in JeanX.daily_history:
                    call change_Girl_stat(JeanX, "love", -2)
                ch_j "We'll see. . ."
            if "chill" not in JeanX.daily_history:
                call change_Girl_stat(JeanX, "obedience", 3)
            if "chill" in JeanX.traits:
                $ JeanX.traits.remove("chill")
            $ JeanX.add_word(1, 0, "chill")
        "Um, never mind.":
            pass
    return




label Jean_Hungry:
    if JeanX.had_chat[3]:
        ch_j "Hey, gimme a taste. . ."
    elif JeanX.had_chat[2]:
        ch_j "Hey, I could use some of that. . . serum. . ."
    else:
        ch_j "I really like. . . your flavor. . ."
    $ JeanX.traits.append("hungry")
return





label Jean_SexChat:
    $ line = "Yeah, what did you want to talk about?" if not line else line
    while True:
        menu:
            ch_j "[line]"
            "My favorite thing to do is. . .":
                if "setfav" in JeanX.daily_history:
                    ch_j "I remember."
                else:
                    menu:
                        "Sex.":
                            $ JeanX.change_face("sly")
                            if JeanX.player_favorite_action == "sex":
                                call change_Girl_stat(JeanX, "lust", 5)
                                ch_j "Yeah, I know that. . ."
                            elif JeanX.favorite_action == "sex":
                                call change_Girl_stat(JeanX, "love", 5)
                                call change_Girl_stat(JeanX, "lust", 10)
                                ch_j "I really like it too!"
                            elif JeanX.permanent_History["sex"] >= 5:
                                ch_j "Well I don't mind that."
                            elif not JeanX.permanent_History["sex"]:
                                $ JeanX.change_face("perplexed")
                                ch_j "Oh? Who with?"
                            else:
                                $ JeanX.change_face("bemused")
                                ch_j "Heh, um, yeah, it's nice. . ."
                            $ JeanX.player_favorite_action = "sex"
                        "Anal.":

                            $ JeanX.change_face("sly")
                            if JeanX.player_favorite_action == "anal":
                                call change_Girl_stat(JeanX, "lust", 5)
                                ch_j "So you've said. . ."
                            elif JeanX.favorite_action == "anal":
                                call change_Girl_stat(JeanX, "love", 5)
                                call change_Girl_stat(JeanX, "lust", 10)
                                ch_j "I love it too!"
                            elif JeanX.permanent_History["anal"] >= 10:
                                ch_j "Yeah, it's. . . nice. . ."
                            elif not JeanX.permanent_History["anal"]:
                                $ JeanX.change_face("perplexed")
                                ch_j "Oh? Who with?"
                            else:
                                $ JeanX.change_face("bemused", eyes = "side")
                                ch_j "Heh, heh, yeah, um, it's ok. . ."
                            $ JeanX.player_favorite_action = "anal"
                        "Blowjobs.":

                            $ JeanX.change_face("sly")
                            if JeanX.player_favorite_action == "blowjob":
                                call change_Girl_stat(JeanX, "lust", 3)
                                ch_j "Yeah, I know."
                            elif JeanX.favorite_action == "blowjob":
                                call change_Girl_stat(JeanX, "love", 5)
                                call change_Girl_stat(JeanX, "lust", 5)
                                ch_j "I can't say I hate it either. . ."
                            elif JeanX.permanent_History["blowjob"] >= 10:
                                ch_j "Yeah, you're surprisingly tasty."
                            elif not JeanX.permanent_History["blowjob"]:
                                $ JeanX.change_face("perplexed")
                                ch_j "Oh? Who with?"
                            else:
                                $ JeanX.change_face("bemused")
                                ch_j "You're lucky you taste so good."
                            $ JeanX.player_favorite_action = "blowjob"
                        "Titjobs.":

                            $ JeanX.change_face("sly")
                            if JeanX.player_favorite_action == "titjob":
                                call change_Girl_stat(JeanX, "lust", 5)
                                ch_j "Yeah, you've said that before. . ."
                            elif JeanX.favorite_action == "titjob":
                                call change_Girl_stat(JeanX, "love", 5)
                                call change_Girl_stat(JeanX, "lust", 7)
                                ch_j "Yeah, I enjoy that too. . ."
                            elif JeanX.permanent_History["titjob"] >= 10:
                                ch_j "Nice, right?"
                            elif not JeanX.permanent_History["titjob"]:
                                $ JeanX.change_face("perplexed")
                                ch_j "Oh? Who with?"
                            else:
                                $ JeanX.change_face("bemused")
                                ch_j "They are pretty nice. . ."
                                call change_Girl_stat(JeanX, "love", 5)
                                call change_Girl_stat(JeanX, "inhibition", 10)
                            $ JeanX.player_favorite_action = "titjob"
                        "Footjobs.":

                            $ JeanX.change_face("sly")
                            if JeanX.player_favorite_action == "footjob":
                                call change_Girl_stat(JeanX, "lust", 5)
                                ch_j "Yeah, you've said that. . ."
                            elif JeanX.favorite_action == "footjob":
                                call change_Girl_stat(JeanX, "love", 5)
                                call change_Girl_stat(JeanX, "lust", 7)
                                ch_j "I do like using my feet. . ."
                            elif JeanX.permanent_History["footjob"] >= 10:
                                ch_j "I like it too . . ."
                            elif not JeanX.permanent_History["footjob"]:
                                $ JeanX.change_face("perplexed")
                                ch_j "Oh? Who with?"
                            else:
                                $ JeanX.change_face("bemused")
                                ch_j "Yeah, it's nice. . ."
                            $ JeanX.player_favorite_action = "footjob"
                        "Handjobs.":

                            $ JeanX.change_face("sly")
                            if JeanX.player_favorite_action == "handjob":
                                call change_Girl_stat(JeanX, "lust", 5)
                                ch_j "Yeah, you've said that. . ."
                            elif JeanX.favorite_action == "handjob":
                                call change_Girl_stat(JeanX, "love", 5)
                                call change_Girl_stat(JeanX, "lust", 7)
                                ch_j "I do have quite the touch. . ."
                            elif JeanX.permanent_History["handjob"] >= 10:
                                ch_j "I like it too . . ."
                            elif not JeanX.permanent_History["handjob"]:
                                $ JeanX.change_face("perplexed")
                                ch_j "Oh? Who with?"
                            else:
                                $ JeanX.change_face("bemused")
                                ch_j "Yeah, it's nice. . ."
                            $ JeanX.player_favorite_action = "handjob"
                        "Feeling you up.":

                            $ counter = JeanX.permanent_History["fondle_breasts"]+ JeanX.permanent_History["fondle_thighs"]+ JeanX.permanent_History["suck_breasts"] + JeanX.permanent_History["hotdog"]
                            $ JeanX.change_face("sly")
                            if JeanX.player_favorite_action == "fondle":
                                call change_Girl_stat(JeanX, "lust", 3)
                                ch_j "Yeah, I think we're clear on that. . ."
                            elif JeanX.favorite_action in ("hotdog", "suck_breasts", "fondle_breasts", "fondle_thighs"):
                                call change_Girl_stat(JeanX, "love", 5)
                                call change_Girl_stat(JeanX, "lust", 5)
                                ch_j "I love when you touch me. . ."
                            elif counter >= 10:
                                ch_j "Yeah, it's really nice . . ."
                            elif not counter:
                                $ JeanX.change_face("perplexed")
                                ch_j "Oh? Who with?"
                            else:
                                $ JeanX.change_face("bemused")
                                ch_j "I do like how that feels. . ."
                            $ JeanX.player_favorite_action = "fondle"
                            $ counter = 0
                        "Kissing you.":

                            $ JeanX.change_face("sly")
                            if JeanX.player_favorite_action == "kiss":
                                call change_Girl_stat(JeanX, "love", 3)
                                ch_j "Dork. . ."
                            elif JeanX.favorite_action == "kiss":
                                call change_Girl_stat(JeanX, "love", 5)
                                call change_Girl_stat(JeanX, "lust", 5)
                                ch_j "I. . . do too, ok? . ."
                            elif JeanX.permanent_History["kiss"] >= 10:
                                ch_j "Yeah, it's fun . . ."
                            elif not JeanX.permanent_History["kiss"]:
                                $ JeanX.change_face("perplexed")
                                ch_j "Oh? Who with?"
                            else:
                                $ JeanX.change_face("bemused")
                                ch_j "I do too. . ."
                            $ JeanX.player_favorite_action = "kiss"

                    $ JeanX.daily_history.append("setfav")
            "What's your favorite thing to do?":

                if not approval_check(JeanX, 800):
                    $ JeanX.change_face("perplexed")
                    ch_j ". . ."
                else:
                    if JeanX.SEXP >= 50:
                        $ JeanX.change_face("perplexed")
                        ch_j "You should know that by now. . ."
                    else:
                        $ JeanX.change_face("bemused")
                        $ JeanX.eyes = "side"
                        ch_j "Hmm. . ."


                    if not JeanX.favorite_action or JeanX.favorite_action == "kiss":
                        ch_j "Kissing?"
                    elif JeanX.favorite_action == "anal":
                        ch_j "Probably anal."
                    elif JeanX.favorite_action == "eat_ass":
                        ch_j "When you lick my ass."
                    elif JeanX.favorite_action == "finger_ass":
                        ch_j "Fingering my asshole, probably."
                    elif JeanX.favorite_action == "sex":
                        ch_j "Just stick it in me."
                    elif JeanX.favorite_action == "eat_pussy":
                        ch_j "When you lick my pussy."
                    elif JeanX.favorite_action == "fondle_pussy":
                        ch_j "When you finger me."
                    elif JeanX.favorite_action == "blowjob":
                        ch_j "I do like how your cock tastes. . ."
                    elif JeanX.favorite_action == "titjob":
                        ch_j "When I use my tits."
                    elif JeanX.favorite_action == "footjob":
                        ch_j "Footjobs are pretty fun."
                    elif JeanX.favorite_action == "handjob":
                        ch_j "I like to jerk you off."
                    elif JeanX.favorite_action == "hotdog":
                        ch_j "When you grind against me."
                    elif JeanX.favorite_action == "suck_breasts":
                        ch_j "When you suck my tits."
                    elif JeanX.favorite_action == "fondle_breasts":
                        ch_j "When you massage my tits."
                    elif JeanX.favorite_action == "fondle_thighs":
                        ch_j "When you massage my thighs."
                    else:
                        ch_j "I don't know, surprise me."



            "Don't talk as much during sex." if "vocal" in JeanX.traits:
                if "setvocal" in JeanX.daily_history:
                    $ JeanX.change_face("perplexed")
                    ch_j "Don't jerk me around, [Girl.player_petname]."
                else:
                    if approval_check(JeanX, 1000) and JeanX.obedience <= JeanX.love:
                        $ JeanX.change_face("bemused")
                        call change_Girl_stat(JeanX, "obedience", 1)
                        ch_j ". . . fine."
                        $ JeanX.traits.remove("vocal")
                    elif approval_check(JeanX, 700, "O"):
                        $ JeanX.change_face("sadside")
                        call change_Girl_stat(JeanX, "obedience", 1)
                        ch_j ". . ."
                        $ JeanX.traits.remove("vocal")
                    elif approval_check(JeanX, 600):
                        $ JeanX.change_face("sly")
                        call change_Girl_stat(JeanX, "love", -3)
                        call change_Girl_stat(JeanX, "obedience", -1)
                        call change_Girl_stat(JeanX, "inhibition", 5)
                        ch_j "Oh, I'll talk and you'll listen, [JeanX.player_petname]."
                    else:
                        $ JeanX.change_face("angry")
                        call change_Girl_stat(JeanX, "love", -5)
                        call change_Girl_stat(JeanX, "obedience", -3)
                        call change_Girl_stat(JeanX, "inhibition", 10)
                        ch_j "Yeah, that'll be the day. . ."

                    $ JeanX.daily_history.append("setvocal")
            "Talk dirty to me during sex." if "vocal" not in JeanX.traits:
                if "setvocal" in JeanX.daily_history:
                    $ JeanX.change_face("perplexed")
                    ch_j "Don't jerk me around, [Girl.player_petname]."
                else:
                    if approval_check(JeanX, 1000) and JeanX.obedience <= JeanX.love:
                        $ JeanX.change_face("sly")
                        call change_Girl_stat(JeanX, "obedience", 2)
                        ch_j "I think that can be arranged. . ."
                        $ JeanX.traits.append("vocal")
                    elif approval_check(JeanX, 700, "O"):
                        $ JeanX.change_face("sadside")
                        call change_Girl_stat(JeanX, "obedience", 2)
                        ch_j "I'll see what I can do, [JeanX.player_petname]."
                        $ JeanX.traits.append("vocal")
                    elif approval_check(JeanX, 600):
                        $ JeanX.change_face("sly")
                        call change_Girl_stat(JeanX, "obedience", 3)
                        ch_j "Sure, whatever."
                        $ JeanX.traits.append("vocal")
                    else:
                        $ JeanX.change_face("angry")
                        call change_Girl_stat(JeanX, "inhibition", 5)
                        ch_j ". . ."

                    $ JeanX.daily_history.append("setvocal")


            "Don't do your own thing as much during sex." if "passive" not in JeanX.traits:
                if "initiative" in JeanX.daily_history:
                    $ JeanX.change_face("perplexed")
                    ch_j "Don't jerk me around, [Girl.player_petname]."
                else:
                    if approval_check(JeanX, 1200) and JeanX.obedience <= JeanX.love:
                        $ JeanX.change_face("bemused")
                        call change_Girl_stat(JeanX, "obedience", 1)
                        ch_j "Like me \"passive?\" I'll see what I can do. . ."
                        $ JeanX.traits.append("passive")
                    elif approval_check(JeanX, 700, "O"):
                        $ JeanX.change_face("sadside")
                        call change_Girl_stat(JeanX, "obedience", 1)
                        ch_j ". . . yeah, ok. . ."
                        $ JeanX.traits.append("passive")
                    elif approval_check(JeanX, 600):
                        $ JeanX.change_face("sly")
                        call change_Girl_stat(JeanX, "love", -3)
                        call change_Girl_stat(JeanX, "obedience", -1)
                        call change_Girl_stat(JeanX, "inhibition", 5)
                        ch_j "Hm, -NO.-"
                    else:
                        $ JeanX.change_face("angry")
                        call change_Girl_stat(JeanX, "love", -5)
                        call change_Girl_stat(JeanX, "obedience", -3)
                        call change_Girl_stat(JeanX, "inhibition", 10)
                        ch_j "You wish."

                    $ JeanX.daily_history.append("initiative")
            "Take more initiative during sex." if "passive" in JeanX.traits:
                if "initiative" in JeanX.daily_history:
                    $ JeanX.change_face("perplexed")
                    ch_j "Don't jerk me around, [Girl.player_petname]."
                else:
                    if approval_check(JeanX, 1000) and JeanX.obedience <= JeanX.love:
                        $ JeanX.change_face("bemused")
                        call change_Girl_stat(JeanX, "obedience", 1)
                        ch_j "Damned right I will."
                        $ JeanX.traits.remove("passive")
                    elif approval_check(JeanX, 700, "O"):
                        $ JeanX.change_face("sadside")
                        call change_Girl_stat(JeanX, "obedience", 1)
                        ch_j ". . . fine. . ."
                        $ JeanX.traits.remove("passive")
                    elif approval_check(JeanX, 600):
                        $ JeanX.change_face("sly")
                        call change_Girl_stat(JeanX, "obedience", 3)
                        ch_j "Sure."
                        $ JeanX.traits.remove("passive")
                    else:
                        $ JeanX.change_face("angry")
                        call change_Girl_stat(JeanX, "inhibition", 5)
                        ch_j "Ugh, don't bother me with that, figure it out yourself."

                    $ JeanX.daily_history.append("initiative")

            "About getting Jumped" if "jumped" in JeanX.history:
                call Jean_Jumped

            "About that \"mind screen\"" if "screen" in JeanX.traits or "noscreen" in JeanX.traits:
                ch_j "You mean how I can make Chuck ignore us a sometimes?"
                menu:
                    extend ""
                    "Yeah, do that." if "noscreen" in JeanX.traits:
                        ch_j "Nice. . ."
                        $ JeanX.traits.append("screen")
                    "Don't do that anymore, I want him to know." if "screen" in JeanX.traits:
                        ch_j "So naughty. . ."
                        if approval_check(JeanX, 900, "OI"):
                            $ JeanX.change_face("sad")
                            ch_j "Fine, I can leave it down."
                            $ JeanX.change_face("bemused")
                            $ JeanX.traits.append("noscreen")
                        else:
                            ch_j "Still, I don't like him bothering us."
                            ch_j "I'll keep the screen up anyway."
                    "Never mind.":
                        pass


            "About that \"whammy\" you do?" if "whammy" in JeanX.traits or "nowhammy" in JeanX.traits:
                ch_j "You mean how I mind wipe the other students so they don't know what a freak I am?"
                menu:
                    extend ""
                    "That is so cool":
                        if "whammytalk" not in JeanX.had_chat:
                            call change_Girl_stat(JeanX, "love", 10)
                            call change_Girl_stat(JeanX, "love", 5)
                            call change_Girl_stat(JeanX, "obedience", 10)
                            call change_Girl_stat(JeanX, "obedience", 5)
                            call change_Girl_stat(JeanX, "inhibition", 10)
                        ch_j "I know, right?"
                        $ JeanX.had_chat.append("whammytalk")
                    "Yeah, can should start doing that again." if "nowhammy" in JeanX.traits:
                        ch_j "Oh, well. . ."
                        if "Alpha" not in Player.traits:

                            $ JeanX.change_face("sad")
                            ch_j "I'd love to, but Chuck'd have my ovaries over it. . ."
                        elif approval_check(JeanX, 800, "I"):
                            if "whammytalk" not in JeanX.daily_history:
                                call change_Girl_stat(JeanX, "love", 10)
                                call change_Girl_stat(JeanX, "obedience", 5)
                                call change_Girl_stat(JeanX, "inhibition", 10)
                            if not approval_check(JeanX, 800, "LO"):

                                $ JeanX.change_face("sad")
                                ch_j "Actually, I like it that way."
                            else:

                                $ JeanX.change_face("sad")
                                ch_j "Ok, fine. . ."
                                $ JeanX.change_face("bemused")
                                ch_j "I did kind of enjoy the thrill though. . ."
                        else:

                            if "whammytalk" not in JeanX.daily_history:
                                call change_Girl_stat(JeanX, "love", 5)
                                call change_Girl_stat(JeanX, "obedience", 3)
                            ch_j "Ok, thanks. . ."
                            $ JeanX.traits.append("whammy")
                        $ JeanX.daily_history.append("whammytalk")
                    "Don't do that anymore, I want them to remember." if "whammy" in JeanX.traits:
                        if "whammytalk" not in JeanX.daily_history:
                            call change_Girl_stat(JeanX, "obedience", 5)
                            call change_Girl_stat(JeanX, "obedience", 5)
                            call change_Girl_stat(JeanX, "inhibition", 10)
                        ch_j "Oh, well. . ."
                        if approval_check(JeanX, 1500):
                            $ JeanX.change_face("sad")
                            ch_j "Ok, I guess I can. . ."
                            $ JeanX.traits.append("nowhammy")
                        else:
                            $ JeanX.change_face("bemused")
                            ch_j "Well too bad for you. . ."
                        $ JeanX.daily_history.append("whammytalk")
                    "Never mind.":
                        pass
            "About when you masturbate":


                call NoFap (JeanX)

            "Never mind" if line == "Yeah, what did you want to talk about?":
                return
            "That's all." if line != "Yeah, what did you want to talk about?":
                return
        if line == "Yeah, what did you want to talk about?":
            $ line = "Anything else?"
    return




label Jean_Chitchat(O=0, Options = ["default", "default", "default"]):
    $ round -= 3 if round > 3 else (round-1)
    if O:
        $ Options = [O]
    else:

        if JeanX not in Player.Phonebook:
            if approval_check(JeanX, 500, "L") or approval_check(JeanX, 250, "I"):
                ch_j "Oh, here's my number, gimme a call some time."
                $ Player.Phonebook.append(JeanX)
                return
            elif approval_check(JeanX, 250, "O"):
                ch_j "I guess you should have my number. . ."
                $ Player.Phonebook.append(JeanX)
                return

        if "hungry" not in JeanX.traits and (JeanX.permanent_History["swallowed"] + JeanX.had_chat[2]) >= 10 and JeanX.location == Player.location:
            call Jean_Hungry
            return

        if Player.location != "bg_restaurant" and Player.location != "bg_halloween" and (not taboo or approval_check(JeanX, 800, "I")):
            if JeanX.location == Player.location and JeanX.thirst >= 30 and "refused" not in JeanX.daily_history and "quicksex" not in JeanX.daily_history:
                $ JeanX.change_face("sly", 1)
                ch_j "I could use some stress relief, you busy?"
                call Quick_Sex (JeanX)
                return




        if JeanX.event_happened[0] and "key" not in JeanX.had_chat:
            $ Options.append("key")

        if "mandrill" in Player.traits and "cologne chat" not in JeanX.daily_history:
            $ Options.append("mandrill")
        if "purple" in Player.traits and "cologne chat" not in JeanX.daily_history:
            $ Options.append("purple")
        if "corruption" in Player.traits and "cologne chat" not in JeanX.daily_history:
            $ Options.append("corruption")

        if JeanX.went_on_date >= 1 and Player.location != "bg_restaurant":

            $ Options.append("dated")



        if JeanX.permanent_History["kiss"] >= 5:

            $ Options.append("kissed")
        if "dangerroom" in Player.daily_history:

            $ Options.append("dangerroom")
        if "showered" in JeanX.daily_history:

            $ Options.append("showercaught")
        if "fondle_breasts" in JeanX.daily_history or "fondle_pussy" in JeanX.daily_history or "fondle_ass" in JeanX.daily_history:

            $ Options.append("fondled")
        if "Dazzler and Longshot" in JeanX.inventory and "256 Shades of Grey" in JeanX.inventory and "Avengers Tower Penthouse" in JeanX.inventory:

            if "book" not in JeanX.had_chat:
                $ Options.append("booked")
        if "lace_bra" in JeanX.inventory or "lace_panties" in JeanX.inventory:

            if "lingerie" not in JeanX.had_chat:
                $ Options.append("lingerie")
        if JeanX.permanent_History["handjob"]:

            $ Options.append("handy")
        if JeanX.permanent_History["swallowed"]:

            $ Options.append("swallowed")
        if "cleaned" in JeanX.daily_history or "painted" in JeanX.daily_history:

            $ Options.append("facial")
        if JeanX.permanent_History["sleepover"]:

            $ Options.append("sleepwear")
        if JeanX.permanent_History["creampied"] or JeanX.permanent_History["anal_creampied"]:

            $ Options.append("creampie")
        if JeanX.permanent_History["sex"] or JeanX.permanent_History["anal"]:

            $ Options.append("sexed")
        if JeanX.permanent_History["anal"]:

            $ Options.append("anal")

        if "seenpeen" in JeanX.history:
            $ Options.append("seenpeen")
        if "topless" in JeanX.history:
            $ Options.append("topless")
        if "bottomless" in JeanX.history:
            $ Options.append("bottomless")

        if not approval_check(JeanX, 300):
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)

    if Options[0] == "mandrill":
        $ JeanX.daily_history.append("cologne chat")
        $ JeanX.change_face("confused")
        ch_j "(sniff, sniff). . . have you been fucking Hank? . ."
        $ JeanX.change_face("sexy", 2)
        ch_j ". . . still, you do smell kinda good. . ."
    elif Options[0] == "purple":
        $ JeanX.daily_history.append("cologne chat")
        $ JeanX.change_face("sly", 1)
        ch_j "(sniff, sniff). . . what is that? . ."
        $ JeanX.change_face("normal", 0)
        ch_j ". . . what was it you wanted?"
    elif Options[0] == "corruption":
        $ JeanX.daily_history.append("cologne chat")
        $ JeanX.change_face("confused")
        ch_j "(sniff, sniff). . . that's a strong scent. . ."
        $ JeanX.change_face("angry")
        ch_j ". . . a dangerous scent. . ."
        $ JeanX.change_face("sly")

    elif Options[0] == "caught":
        $ JeanX.change_face("angry")
        if "caught chat" in JeanX.had_chat:
            ch_j "That asshole Chuck."
            ch_j "I'm tired of him sticking his nose in where it doesn't belong."
        else:
            ch_j "That asshole Chuck."
            ch_j "I'm tired of him sticking his nose in where it doesn't belong."
            $ JeanX.change_face("surprised")
            ch_j "Oh!"
            $ JeanX.change_face("sly")
            ch_j "I've got an idea."
            ch_j "I could use my own powers to jam out his a little bit, make it more likely that he'll ignore us."
            menu:
                "Sure, that sounds good.":
                    ch_j "Excellent. . ."
                    $ JeanX.traits.append("screen")
                "Nah, I want him to know.":
                    ch_j "Heh, you're naughty."
                    if approval_check(JeanX, 900, "OI"):
                        $ JeanX.change_face("sad")
                        ch_j "Ok, fine, we won't do that."
                        $ JeanX.change_face("bemused")
                        $ JeanX.traits.append("noscreen")
                    else:
                        ch_j "Still, I don't like him sticking his nose in."
                        ch_j "I think I'll use the screen anyway."
                        $ JeanX.traits.append("screen")
            $ JeanX.had_chat.append("caught chat")
    elif Options[0] == "key":
        if JeanX.SEXP <= 15:
            ch_j "Don't use that key too freely. . ."
        else:
            ch_j "You have my key, but don't visit enough. . ."
        $ JeanX.had_chat.append("key")









    elif Options[0] == "dated":

        ch_j "I had fun the other night, we should do that again some time."

    elif Options[0] == "kissed":

        $ JeanX.change_face("normal", 1)
        ch_j "I have to say, you are a good kisser, [JeanX.player_petname]."
        menu:
            extend ""
            "Hey. . .I'm the best there is at what I do.":
                $ JeanX.change_face("smile", 1)
                ch_j "I've heard that one before. . ."
            "No. You think?":
                ch_j "I wouldn't say it otherwise."

    elif Options[0] == "dangerroom":

        $ JeanX.change_face("sly", 1)
        ch_j "Hey,[JeanX.player_petname]. I saw you in the Danger Room, earlier."
        ch_j "You're going surprisingly well for someone with your. . . limitations."

    elif Options[0] == "showercaught":

        if "shower" in JeanX.had_chat:
            ch_j "I saw you in the showers again. . ."
        else:
            ch_j "So do you always just bust into the showers?"
            $ JeanX.had_chat.append("shower")
            menu:
                extend ""
                "It was a total accident! I promise!":
                    call change_Girl_stat(JeanX, "love", 5)
                    call change_Girl_stat(JeanX, "love", 2)
                    if approval_check(JeanX, 1200):
                        $ JeanX.change_face("sly", 1)
                        ch_j "Well, it's not like I minded."
                    $ JeanX.change_face("smile")
                    ch_j "I guess we can all make mistakes. . ."
                "Just with you.":
                    call change_Girl_stat(JeanX, "obedience", 5)
                    if approval_check(JeanX, 1000) or approval_check(JeanX, 700, "L"):
                        call change_Girl_stat(JeanX, "love", 3)
                        $ JeanX.change_face("sly", 1)
                        ch_j "Oh, a charmer. . ."
                    else:
                        call change_Girl_stat(JeanX, "love", -5)
                        $ JeanX.change_face("angry")
                        ch_j "I'll bet. . ."
                "Totally on purpose. I regret nothing.":
                    if approval_check(JeanX, 800):
                        call change_Girl_stat(JeanX, "obedience", 5)
                        call change_Girl_stat(JeanX, "inhibition", 5)
                        $ JeanX.change_face("perplexed", 2)
                        ch_j "fair"
                        $ JeanX.blushing = "_blush1"
                    else:
                        call change_Girl_stat(JeanX, "love", -10)
                        call change_Girl_stat(JeanX, "love", -10)
                        call change_Girl_stat(JeanX, "obedience", 10)
                        $ JeanX.change_face("angry")
                        ch_j "Perv."

    elif Options[0] == "fondled":

        if JeanX.permanent_History["fondle_breasts"]+ JeanX.permanent_History["fondle_pussy"] + JeanX.permanent_History["fondle_ass"] >= 15:
            ch_j "Hey, give me a nice, hard, rubdown. . ."
        else:
            ch_j "Hey, gimme another massage. . . "
            ch_j ". . . the good kind. . ."

    elif Options[0] == "booked":

        ch_j "Hey, I read those books you gave me."
        menu:
            extend ""
            "Yeah? Did you like them?":
                $ JeanX.change_face("sly", 2)
                ch_j "They were pretty hot."
            "Good. You looked like you could use to learn a thing or two from them.":
                call change_Girl_stat(JeanX, "obedience", 5)
                call change_Girl_stat(JeanX, "inhibition", 5)
                $ JeanX.change_face("angry")
                ch_j "Yeah right."
        $ JeanX.blushing = "_blush1"
        $ JeanX.had_chat.append("book")

    elif Options[0] == "lingerie":

        $ JeanX.change_face("sly", 2)
        ch_j "I really enjoy those silky underthings you got me. . ."
        $ JeanX.blushing = "_blush1"
        $ JeanX.had_chat.append("lingerie")

    elif Options[0] == "handy":

        $ JeanX.change_face("sly", 1)
        ch_j "I was thinking about your cock in my hand. . ."
        ch_j "I think we should do that again some time. . ."
        $ JeanX.blushing = ""

    elif Options[0] == "blowjob":
        if "blowjob" not in JeanX.had_chat:

            $ JeanX.change_face("sly", 2)
            ch_j "Hey, so did you enjoy that blowjob?"
            menu:
                extend ""
                "You were totally amazing.":
                    call change_Girl_stat(JeanX, "love", 5)
                    call change_Girl_stat(JeanX, "obedience", 15)
                    call change_Girl_stat(JeanX, "inhibition", 10)
                    $ JeanX.change_face("normal", 1)
                    ch_j "You know it."
                    $ JeanX.change_face("sexy", 1)
                    ch_j "I wouldn't mind having another taste. . ."
                "Honestly? It was good. . .but you could use a little practice, I think.":
                    if approval_check(JeanX, 300, "I") or not approval_check(JeanX, 800):
                        call change_Girl_stat(JeanX, "love", -5)
                        call change_Girl_stat(JeanX, "obedience", 10)
                        call change_Girl_stat(JeanX, "inhibition", 10)
                        $ JeanX.change_face("perplexed", 1)
                        ch_j "Really? I'd never gotten any complaints before. . ."
                    else:
                        call change_Girl_stat(JeanX, "obedience", 15)
                        call change_Girl_stat(JeanX, "inhibition", 5)
                        $ JeanX.change_face("sexy", 1)
                        ch_j "You just don't know quality when you feel it."
                "I guess. If you're into weird sounds and too much teeth. Spoiler, I'm not.":
                    call change_Girl_stat(JeanX, "love", -10)
                    call change_Girl_stat(JeanX, "obedience", -5)
                    $ JeanX.change_face("angry", 2)
                    ch_j "You just don't know quality."
            $ JeanX.blushing = "_blush1"
            $ JeanX.had_chat.append("blowjob")
        else:
            $ line = renpy.random.choice(["I gotta tell you, your dick tastes great.",
                            "I think I nearly dislocated my jaw last time.",
                            "Let me know if you'd like another blowjob sometime.",
                            "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
            ch_j "[line]"

    elif Options[0] == "swallowed":

        if "swallow" in JeanX.had_chat:
            ch_j "Hey, I wouldn't mind another taste. . ."
        else:
            ch_j "Hey. . . the other day. . ."
            ch_j "Your jizz tasted really good."
            ch_j "Like -really- good."
            $ JeanX.change_face("sly", 1)
            ch_j "Weird."
            $ JeanX.had_chat.append("swallow")

    elif Options[0] == "facial":

        ch_j "Ok, so. . ."
        ch_j "You know how you came on my face?"
        $ JeanX.change_face("sexy", 2)
        ch_j "That just felt -so- good for some reason. . ."
        $ JeanX.blushing = "_blush1"

    elif Options[0] == "sleepover":

        ch_j "I really enjoyed the other night."
        ch_j "I really enjoyed the company."

    elif Options[0] == "creampie":

        "[JeanX.name] draws close to you so she can whisper into your ear."
        ch_j "I still ave some of you spilling out of me. . ."

    elif Options[0] == "sexed":

        ch_j "So. . . you should know. . ."
        $ JeanX.change_face("sexy", 2)
        ch_j ". . .lately when I've been schlicking. . ."
        ch_j "I've been thinking about you inside of me."
        $ JeanX.blushing = "_blush1"

    elif Options[0] == "anal":

        $ JeanX.change_face("sly")
        ch_j "I'm not much of a fan of anal."
        $ JeanX.change_face("sexy", 1)
        ch_j "Still, with you it's pretty fun."

    elif Options[0] == "seenpeen":
        $ JeanX.change_face("sly", 1, eyes = "down")
        ch_j "Oh, I forgot to mention, congrats on that package you're swinging. . ."
        $ JeanX.change_face("bemused", 1)
        call change_Girl_stat(JeanX, "love", 5)
        call change_Girl_stat(JeanX, "love", 10)
        $ JeanX.history.remove("seenpeen")
    elif Options[0] == "topless":
        ch_j "So you got a good look at my tits earlier, Pretty great, right?"
        call Jean_First_TMenu
        $ JeanX.history.remove("topless")
    elif Options[0] == "bottomless":
        ch_j "So you got a good look at my pussy earlier, not bad, right?"
        call Jean_First_BMenu
        $ JeanX.history.remove("bottomless")
















    elif Options[0] == "hate":
        $ line = renpy.random.choice(["Get away from me.",
                "I don't want to smell you near me.",
                "Back off.",
                "Buzz off."])
        ch_j "[line]"
    else:

        ch_j "Oh, did you have something interesting to say?"

        $ D20 = renpy.random.randint(1, 20)
        if D20 == 1:
            $ JeanX.change_face("normal")
            ch_j "Hey, pass me your physics notes."
            $ JeanX.change_face("angry", eyes = "down")
            ch_j ". . ."
            $ JeanX.change_face("angry")
            ch_j "These notes are trash. Do better."
        elif D20 == 2:
            $ JeanX.change_face("angry")
            ch_j "Where'd Lance go? I haven't seen him around in a while."
        elif D20 == 3:
            $ JeanX.change_face("normal", eyes = "side")
            ch_j ". . ."
            $ JeanX.change_face("surprised")
            ch_j "Oh, what were you talking about?"
            $ JeanX.change_face("normal")
        elif D20 == 4:
            $ JeanX.change_face("sad")
            ch_j "I don't know why I still attend these classes. I already know everything I need to know."
        elif D20 == 5:
            $ JeanX.change_face("smile")
            ch_j "Nothing like a quick nap to recharge the batteries."
        elif D20 == 6:
            $ JeanX.change_face("perplexed")
            ch_j "Oh, I just noticed your outfit. . . interesting choice."
        elif D20 == 7:
            $ JeanX.change_face("smile")
            ch_j "Did you see me wreck the Danger Room earlier?"
            ch_j "I mean to do that!"
        elif D20 == 8:
            $ JeanX.change_face("angry")
            ch_j "Quiet."
            $ JeanX.change_face("angry", eyes = "side")
            ch_j "It's thinking time."
            $ JeanX.change_face("smile")
            ch_j "Ok, done."
        elif D20 == 9:
            $ JeanX.change_face("confused")
            ch_j "I was just picking up some stray thoughts from Professor McCoy."
            ch_j "They were. . . unhealthy."
        elif D20 == 10:
            $ JeanX.change_face("smile")
            ch_j "I hear some of the girls are going out for ice cream, treat me."
        elif D20 == 11:
            $ JeanX.change_face("smile")
            ch_j "I might catch a swim later. Make sure to bring a towel."
        elif D20 == 12:
            $ JeanX.change_face("smile")
            ch_j "I kind of like talking to you. . ."
            ch_j "You're. . ."
            ch_j "Simple."
        elif D20 == 13:
            $ JeanX.change_face("smile")
            ch_j "If I've told you once, I've told you a thousand times. . ."
            ch_j "Well. . . you know!"
        elif D20 == 14:
            $ JeanX.change_face("smile")
            ch_j "Missions are a serious pain, but at least I can get some action."
        elif D20 == 15:
            $ JeanX.change_face("perplexed")
            ch_j "Have you seen a weird girl wandering around. . . "
            ch_j "She thinks in. . . pink. . ."
        elif D20 == 16:
            $ JeanX.change_face("perplexed")
            ch_j "I haven't been home in a while. I almost forget where it is."
        elif D20 == 17:
            $ JeanX.change_face("perplexed")
            ch_j "So, Emma's a bitch, right?"
            ch_j "It's not just me?"
        elif D20 == 18:
            $ JeanX.change_face("smile")
            ch_j "You know, sometimes I think I need a hobby."
            ch_j "And then I just get someone else to do it."
        else:
            $ JeanX.change_face("smile")
            ch_j "You're fun to hang with."

    $ line = 0
    return


label Jean_names:
    menu:
        ch_j "Oh? What would you like me to call you?"
        "My initial's fine.":
            $ JeanX.player_petname = Player.name[:1]
            ch_j "You got it, [JeanX.player_petname]."
        "Call me by my name.":
            if Player.name in JeanX.player_petnames:
                $ JeanX.player_petname = Player.name
                ch_j "Sure, [JeanX.player_petname]."
            else:
                ch_j "Sure, [JeanX.player_petname]."
                menu:
                    extend ""
                    "Fine, whatever.":
                        pass
                    "No, my -real- name, [Player.name].":
                        if approval_check(JeanX, 700, "LO"):
                            $ JeanX.player_petname = Player.name
                            $ JeanX.player_petnames.append(Player.name)
                            ch_j "Ok, fine, I'mm remember that one. . . [JeanX.player_petname]."
                        else:
                            call Jeanname (1)
                            ch_j "Right, right. . . [JeanX.player_petname]!"
                            menu:
                                extend ""
                                "Fine, whatever.":
                                    pass
                                "No, [Player.name]!":
                                    call Jeanname
                                    ch_j "Ok, don't shout. . . [JeanX.player_petname], got it."

        "Call me \"boyfriend\"." if "boyfriend" in JeanX.player_petnames:
            $ JeanX.player_petname = "boyfriend"
            ch_j ". . . ok, [JeanX.player_petname]."
        "Call me \"lover\"." if "lover" in JeanX.player_petnames:
            $ JeanX.player_petname = "lover"
            ch_j ". . ."
            ch_j ". . . ok, [JeanX.player_petname]."
        "Call me \"sir\"." if "sir" in JeanX.player_petnames:
            $ JeanX.player_petname = "sir"
            ch_j "Lol, sure, [JeanX.player_petname]."
        "Call me \"master\"." if "master" in JeanX.player_petnames:
            $ JeanX.player_petname = "master"
            ch_j "Um. . yes, [JeanX.player_petname]."
        "Call me \"sex friend\"." if "sex friend" in JeanX.player_petnames:
            $ JeanX.player_petname = "sex friend"
            ch_j "Lol, ok, [JeanX.player_petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in JeanX.player_petnames:
            $ JeanX.player_petname = "fuck buddy"
            ch_j "Heh, ok, [JeanX.player_petname]."
        "Call me \"daddy\"." if "daddy" in JeanX.player_petnames:
            $ JeanX.player_petname = "daddy"
            ch_j "Hmm. . . [JeanX.player_petname]."
        "Nevermind.":
            return
    return


label Jean_Pet:
    while True:
        menu:
            extend ""
            "Polite":
                menu:
                    extend ""
                    "I think I'll just call you Jean.":
                        $ JeanX.petname = "Jean"
                        ch_j "Ok."
                    "I think I'll call you \"girl\".":

                        $ JeanX.petname = "girl"
                        if "boyfriend" in JeanX.player_petnames or approval_check(JeanX, 600, "L"):
                            $ JeanX.change_face("sexy", 1)
                            ch_j "Yeah, ok, [JeanX.player_petname]."
                        else:
                            $ JeanX.change_face("angry")
                            ch_j "I'm NOT your girl, [JeanX.player_petname]."
                    "I think I'll call you \"boo\".":

                        $ JeanX.petname = "boo"
                        if "boyfriend" in JeanX.player_petnames or approval_check(JeanX, 700, "L"):
                            $ JeanX.change_face("sexy", 1)
                            ch_j "I guess I am your boo, [JeanX.player_petname]."
                        else:
                            $ JeanX.change_face("angry")
                            ch_j "I'm NOT your boo, [JeanX.player_petname]."
                    "I think I'll call you \"bae\".":

                        $ JeanX.petname = "bae"
                        if "boyfriend" in JeanX.player_petnames or approval_check(JeanX, 600, "L"):
                            $ JeanX.change_face("sexy", 1)
                            ch_j "I guess I am your bae, [JeanX.player_petname]."
                        else:
                            $ JeanX.change_face("angry")
                            ch_j "I'm NOT your bae, [JeanX.player_petname]."
                    "I think I'll call you \"baby\".":

                        $ JeanX.petname = "baby"
                        if "boyfriend" in JeanX.player_petnames or approval_check(JeanX, 500, "L"):
                            $ JeanX.change_face("sexy", 1)
                            ch_j "Cute, [JeanX.player_petname]."
                        else:
                            $ JeanX.change_face("angry")
                            ch_j "I am not a baby."
                    "I think I'll call you \"sweetie\".":


                        $ JeanX.petname = "sweetie"
                        if "boyfriend" in JeanX.player_petnames or approval_check(JeanX, 600, "L"):
                            ch_j "Sounds good, [JeanX.player_petname]."
                        else:
                            $ JeanX.change_face("angry", 1)
                            ch_j "Too sweet, [JeanX.player_petname]."
                    "I think I'll call you \"sexy\".":

                        $ JeanX.petname = "sexy"
                        if "lover" in JeanX.player_petnames or approval_check(JeanX, 800):
                            $ JeanX.change_face("sexy", 1)
                            ch_j "You know it, [JeanX.player_petname]."
                        else:
                            $ JeanX.change_face("angry", 1)
                            ch_j "True, but a little rude, [JeanX.player_petname]."
                    "I think I'll call you \"lover\".":

                        $ JeanX.petname = "lover"
                        if "lover" in JeanX.player_petnames or approval_check(JeanX, 1200):
                            $ JeanX.change_face("sexy", 1)
                            ch_j "Heh, ok."
                        else:
                            $ JeanX.change_face("angry", 1)
                            ch_j "I don't think so, [JeanX.player_petname]."
                    "Back":

                        pass
            "Risky":

                menu:
                    "I think I'll call you \"slave\".":
                        $ JeanX.petname = "slave"
                        if "master" in JeanX.player_petnames or approval_check(JeanX, 800, "O"):
                            $ JeanX.change_face("bemused", 1)
                            ch_j ". . . ok, [JeanX.player_petname]."
                        else:
                            $ JeanX.change_face("angry", 1)
                            ch_j "I am not your slave, [JeanX.player_petname]."
                    "I think I'll call you \"pet\".":

                        $ JeanX.petname = "pet"
                        if "master" in JeanX.player_petnames or approval_check(JeanX, 650, "O"):
                            $ JeanX.change_face("bemused", 1)
                            ch_j ". . . fine, [JeanX.player_petname]."
                        else:
                            $ JeanX.change_face("angry", 1)
                            ch_j "I'm not your -pet, - [JeanX.player_petname]."
                    "I think I'll call you \"slut\".":

                        $ JeanX.petname = "slut"
                        if "sex friend" in JeanX.player_petnames or approval_check(JeanX, 900, "OI"):
                            $ JeanX.change_face("sexy")
                            ch_j "Well. . . yeah."
                        else:
                            $ JeanX.change_face("angry", 1)
                            $ JeanX.mouth = "surprised"
                            ch_j "How attached are you to having a vocabulary?"
                    "I think I'll call you \"whore\".":

                        $ JeanX.petname = "whore"
                        if "fuckbuddy" in JeanX.player_petnames or approval_check(JeanX, 1000, "OI"):
                            $ JeanX.change_face("sly")
                            ch_j ". . ."
                        else:
                            $ JeanX.change_face("angry", 1)
                            ch_j "You'd better not. . ."
                    "I think I'll call you \"sugartits\".":

                        $ JeanX.petname = "sugartits"
                        if "sex friend" in JeanX.player_petnames or approval_check(JeanX, 1400):
                            $ JeanX.change_face("sly", 1)
                            ch_j ". . . ok."
                        else:
                            $ JeanX.change_face("angry", 1)
                            ch_j "Not cool."
                    "I think I'll call you \"sex friend\".":

                        $ JeanX.petname = "sex friend"
                        if "sex friend" in JeanX.player_petnames or approval_check(JeanX, 600, "I"):
                            $ JeanX.change_face("sly")
                            ch_j "Yeah. . ."
                        else:
                            $ JeanX.change_face("angry", 1)
                            ch_j "Keep it down, [JeanX.player_petname]."
                    "I think I'll call you \"fuckbuddy\".":

                        $ JeanX.petname = "fuckbuddy"
                        if "fuckbuddy" in JeanX.player_petnames or approval_check(JeanX, 700, "I"):
                            $ JeanX.change_face("sly")
                            ch_j "Yup."
                        else:
                            $ JeanX.change_face("angry", 1)
                            $ JeanX.mouth = "surprised"
                            ch_j "Don't even joke, [JeanX.player_petname]."
                    "I think I'll call you \"baby girl\".":

                        $ JeanX.petname = "baby girl"
                        if "daddy" in JeanX.player_petnames or approval_check(JeanX, 1200):
                            $ JeanX.change_face("smile", 1)
                            ch_j "I guess?"
                        else:
                            $ JeanX.change_face("angry", 1)
                            ch_j "Weirdo."
                    "Back":

                        pass
            "Nevermind.":

                return
    return





label Jean_Rename:

    $ JeanX.mouth = "smile"
    ch_j "Yeah?"
    menu:
        extend ""
        "I think \"Jean's\" a pretty name." if JeanX.name != "Jean" and "Jean" in JeanX.names:
            $ JeanX.name = "Jean"
            ch_j "Well, yeah. I like it."
        "Nevermind.":
            pass
    $ JeanX.add_word(1, 0, "namechange")
    return




label Jean_Personality(counter=0):
    if not JeanX.had_chat[4] or counter:
        "Since you're doing well in one area, you can convince Jean to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_j "Yeah?"
        "More Obedient. [[Love to Obedience]" if JeanX.love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_j "Oh, fine, I'll try. . ."
            $ JeanX.had_chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if JeanX.love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_j "Oh, you like it kinky then? . ."
            $ JeanX.had_chat[4] = 2

        "Less Inhibited. [[Obedience to Inhibition]" if JeanX.obedience > 900:
            ch_p "I want you to be less inhibited."
            ch_j "I'll give it a try. . ."
            $ JeanX.had_chat[4] = 3
        "More Loving. [[Obedience to Love]" if JeanX.obedience > 900:
            ch_p "I'd like you to learn to love me."
            ch_j "Well. . . ok. . ."
            $ JeanX.had_chat[4] = 4

        "More Obedient. [[Inhibition to Obedience]" if (JeanX.inhibition - JeanX.IX) > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_j "Hmm. . . kinky. . ."
            $ JeanX.had_chat[4] = 5

        "More Loving. [[Inhibition to Love]" if (JeanX.inhibition - JeanX.IX) > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_j "Oh, fine. . ."
            $ JeanX.had_chat[4] = 6

        "I guess just do what you like. . .[[reset]" if JeanX.had_chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_j "Um, sure. . ."
            $ JeanX.had_chat[4] = 0
        "Repeat the rules":
            call Jean_Personality (1)
            return
        "Nevermind.":
            return
    return





















label Jean_NoPantiesOn:
    menu:
        ch_j "I'm not wearing any panties at the moment."
        "Then you could slip on a pair of panties. . .":
            if approval_check(JeanX, 1500, taboo_modifier=4) or (JeanX.seen_pussy and approval_check(JeanX, 1100, taboo_modifier=4)):
                $ JeanX.blushing = "_blush1"
                ch_j "No, this is fine. . ."
                $ JeanX.blushing = ""
            elif approval_check(JeanX, 700, taboo_modifier=4):
                ch_j "Yeah, I guess."
                if "lace_panties" in JeanX.inventory:
                    $ JeanX.Clothes["underwear"]  = "lace_panties"
                else:
                    $ JeanX.Clothes["underwear"] = "green_panties"
                if approval_check(JeanX, 1200, taboo_modifier=4):
                    $ line = JeanX.Clothes["bottom"]
                    $ JeanX.Outfit.remove_Clothing(["pants", "skirt"])
                    "She pulls off her [line] and slips on the [JeanX.Clothes[underwear].name]."
                elif JeanX.Clothes["bottom"] == "skirt":
                    "She pulls out her [JeanX.Clothes[underwear].name] and pulls them up under her skirt."
                    $ JeanX.Outfit.remove_Clothing(["pants", "skirt"])
                    "Then she drops the skirt to the floor."
                else:
                    $ line = JeanX.Clothes["bottom"]
                    $ JeanX.Outfit.remove_Clothing(["pants", "skirt"])
                    "She steps away a moment and then comes back wearing only the [JeanX.Clothes[underwear].name]."
                return
            else:
                ch_j "Nope."
                return False
        "You could always just wear nothing at all. . .":

            if approval_check(JeanX, 1100, "LI", taboo_modifier = 3) and JeanX.love > JeanX.inhibition:
                ch_j "True. . ."
            elif approval_check(JeanX, 700, "OI", taboo_modifier = 3) and JeanX.obedience > JeanX.inhibition:
                ch_j "Yes. . ."
            elif approval_check(JeanX, 600, "I", taboo_modifier = 3):
                ch_j "Hrmm. . ."
            elif approval_check(JeanX, 1300, taboo_modifier = 3):
                ch_j "Fine."
            else:
                $ JeanX.change_face("surprised")
                $ JeanX.brows = "angry"
                if JeanX.taboo > 20:
                    ch_j ". . . not right now. . ."
                else:
                    ch_j "Ha! Not for you, [JeanX.player_petname]."
                return False
        "Never mind.":

            ch_j "Ok. . ."
            return False
    return True




menu Jean_Clothes_Under:
    "Tops":
        menu:
            "How about you lose the [JeanX.Clothes[bra].name]?" if JeanX.Clothes["bra"]:
                $ JeanX.change_face("bemused", 1)
                if JeanX.seen_breasts and approval_check(JeanX, 900, taboo_modifier=2.7):
                    ch_j "Ok."
                elif approval_check(JeanX, 1100, taboo_modifier=2):
                    if JeanX.taboo:
                        ch_j "I don't know, here. . ."
                    else:
                        ch_j "Maybe. . ."
                elif JeanX.Clothes["top"] and approval_check(JeanX, 500, taboo_modifier=2):
                    ch_j "I guess I could. . ."
                elif not JeanX.Clothes["top"]:
                    call ask_for_dress_screen (JeanX)
                    if not _return:
                        ch_j "Not without some other top."
                        return
                else:
                    call ask_for_dress_screen (JeanX)
                    if not _return:
                        ch_j "Nah."
                        return
                $ line = JeanX.Clothes["bra"]
                $ JeanX.take_off("bra")
                if JeanX.Clothes["top"]:
                    "She reaches under her [JeanX.Clothes[top].name] grabs her [line], and pulls it off, dropping it to the ground."
                else:
                    "She pulls off her [line] and drops it to the ground."
                    if not renpy.showing('dress_screen'):
                        call Jean_First_Topless


            "Try on that green bra." if JeanX.Clothes["bra"] != "green_bra":
                ch_j "Ok."
                $ JeanX.Clothes["bra"] = "green_bra"

            "How about that sports bra." if JeanX.Clothes["bra"] != "sports_bra":
                ch_j "Ok."
                $ JeanX.Clothes["bra"] = "sports_bra"

            "I like that lace bra." if JeanX.Clothes["bra"] != "lace_bra" and "lace_bra" in JeanX.inventory:
                if JeanX.seen_breasts or approval_check(JeanX, 1300, taboo_modifier=2):
                    ch_j "Sure."
                    $ JeanX.Clothes["bra"] = "lace_bra"
                else:
                    call ask_for_dress_screen (JeanX)
                    if not _return:
                        ch_j "It's a little transparent. . ."
                    else:
                        $ JeanX.Clothes["bra"] = "lace_bra"

            "I like that black corset." if JeanX.Clothes["bra"] != "corset" and "corset" in JeanX.inventory:
                if JeanX.seen_breasts or approval_check(JeanX, 1000, taboo_modifier = 1):
                    ch_j "Sure."
                    $ JeanX.Clothes["bra"] = "corset"
                else:
                    call ask_for_dress_screen (JeanX)
                    if not _return:
                        ch_j "It's a little revealing. . ."
                    else:
                        $ JeanX.Clothes["bra"] = "corset"

            "I like that lace corset." if JeanX.Clothes["bra"] != "lace_corset" and "lace_corset" in JeanX.inventory:
                if JeanX.seen_breasts or approval_check(JeanX, 1300, taboo_modifier=2):
                    ch_j "Sure."
                    $ JeanX.Clothes["bra"] = "lace_corset"
                else:
                    call ask_for_dress_screen (JeanX)
                    if not _return:
                        ch_j "It's a little transparent. . ."
                    else:
                        $ JeanX.Clothes["bra"] = "lace_corset"

            "I like that bikini top." if JeanX.Clothes["bra"] != "bikini_top" and "bikini_top" in JeanX.inventory:
                if Player.location == "bg_pool":
                    ch_j "Sure."
                    $ JeanX.Clothes["bra"] = "bikini_top"
                else:
                    if JeanX.seen_breasts or approval_check(JeanX, 1000, taboo_modifier=2):
                        ch_j "Sure."
                        $ JeanX.Clothes["bra"] = "bikini_top"
                    else:
                        call ask_for_dress_screen (JeanX)
                        if not _return:
                            ch_j "This isn't really a \"bikini\" sort of place. . ."
                        else:
                            $ JeanX.Clothes["bra"] = "bikini_top"
            "Never mind":
                pass
        return
    "Hose and stockings options":

        menu:
            "You could lose the hose." if JeanX.Clothes["hose"]:
                $ JeanX.take_off("hose")
            "The thigh-high hose would look good with that." if JeanX.Clothes["hose"] != "stockings":
                $ JeanX.Clothes["hose"] = "stockings"
            "The full length hose would look good with that." if JeanX.Clothes["hose"] != "pantyhose" and "pantyhose" in JeanX.inventory:
                $ JeanX.Clothes["hose"] = "pantyhose"
            "The ripped pantyhose would look good with that." if JeanX.Clothes["hose"] != "ripped_pantyhose" and "ripped_pantyhose" in JeanX.inventory:
                $ JeanX.Clothes["hose"] = "ripped_pantyhose"
            "The stockings and garterbelt would look good with that." if JeanX.Clothes["hose"] != "stockings_and_garterbelt" and "stockings_and_garterbelt" in JeanX.inventory:
                $ JeanX.Clothes["hose"] = "stockings_and_garterbelt"
            "Just the garterbelt would look good with that." if JeanX.Clothes["hose"] != "garterbelt" and "stockings_and_garterbelt" in JeanX.inventory:
                $ JeanX.Clothes["hose"] = "garterbelt"
            "Never mind":
                pass
        return
    "Panties":


        menu:
            "You could lose those panties. . ." if JeanX.Clothes["underwear"]:
                $ JeanX.change_face("bemused", 1)
                if approval_check(JeanX, 900) and (JeanX.Clothes["bottom"] or (JeanX.seen_pussy and not JeanX.taboo)):

                    if approval_check(JeanX, 850, "L"):
                        ch_j "True. . ."
                    elif approval_check(JeanX, 500, "O"):
                        ch_j "Agreed."
                    elif approval_check(JeanX, 350, "I"):
                        ch_j "Heh."
                    else:
                        ch_j "Sure, I guess."
                else:
                    if approval_check(JeanX, 1100, "LI", taboo_modifier = 3) and JeanX.love > JeanX.inhibition:
                        ch_j "Well look, it's not about you, but. . ."
                    elif approval_check(JeanX, 700, "OI", taboo_modifier = 3) and JeanX.obedience > JeanX.inhibition:
                        ch_j "Well. . ."
                    elif approval_check(JeanX, 600, "I", taboo_modifier = 3):
                        ch_j "Hrmm. . ."
                    elif approval_check(JeanX, 1300, taboo_modifier = 3):
                        ch_j "Okay, okay."
                    else:
                        call ask_for_dress_screen (JeanX)
                        if not _return:
                            $ JeanX.change_face("surprised")
                            $ JeanX.brows = "angry"
                            if JeanX.taboo > 20:
                                ch_j ". . . not right now. . ."
                            else:
                                ch_j "Ha! Not for you, [JeanX.player_petname]."
                            return
                $ line = JeanX.Clothes["underwear"]
                $ JeanX.take_off("underwear")
                if not JeanX.Clothes["bottom"]:
                    "She pulls off her [line], then drops them to the ground."
                    if not renpy.showing('dress_screen'):
                        call Jean_First_Bottomless
                elif approval_check(JeanX, 1200, taboo_modifier=4):
                    $ temp_bottom = JeanX.Clothes["bottom"]
                    $ JeanX.Outfit.remove_Clothing(["pants", "skirt"])
                    pause 0.5
                    $ JeanX.Clothes["bottom"] = temp_bottom
                    "She pulls off her [JeanX.Clothes[bottom]] and [line], then pulls the [JeanX.Clothes[bottom].name] back on."
                    call Jean_First_Bottomless (1)
                elif JeanX.Clothes["bottom"] == "skirt":
                    "She reaches under her skirt and pulls her [line] off."
                else:
                    $ JeanX.blushing = "_blush1"
                    "She steps away a moment and then comes back."
                    $ JeanX.blushing = ""
                $ line = 0

            "Why don't you wear the green panties instead?" if JeanX.Clothes["underwear"] and JeanX.Clothes["underwear"] != "green_panties":
                if approval_check(JeanX, 1100, taboo_modifier = 3):
                    ch_j "Sure."
                    $ JeanX.Clothes["underwear"] = "green_panties"
                else:
                    call ask_for_dress_screen (JeanX)
                    if not _return:
                        ch_j "That's none of your busines."
                    else:
                        $ JeanX.Clothes["underwear"] = "green_panties"

            "Why don't you wear the lace panties instead?" if "lace_panties" in JeanX.inventory and JeanX.Clothes["underwear"] and JeanX.Clothes["underwear"] != "lace_panties":
                if approval_check(JeanX, 1300, taboo_modifier = 3):
                    ch_j "I guess."
                    $ JeanX.Clothes["underwear"] = "lace_panties"
                else:
                    call ask_for_dress_screen (JeanX)
                    if not _return:
                        ch_j "That's none of your busines."
                    else:
                        $ JeanX.Clothes["underwear"] = "lace_panties"

            "I like those bikini bottoms." if "bikini_bottoms" in JeanX.inventory and JeanX.Clothes["underwear"] != "bikini_bottoms":
                if Player.location == "bg_pool":
                    ch_j "Sure."
                    $ JeanX.Clothes["underwear"] = "bikini_bottoms"
                else:
                    if approval_check(JeanX, 1000, taboo_modifier=2):
                        ch_j "Sure."
                        $ JeanX.Clothes["underwear"] = "bikini_bottoms"
                    else:
                        call ask_for_dress_screen (JeanX)
                        if not _return:
                            ch_j "This is not really a \"bikini\" sort of place. . ."
                        else:
                            $ JeanX.Clothes["underwear"] = "bikini_bottoms"

            "You know, you could wear some panties with that. . ." if not JeanX.Clothes["underwear"]:
                $ JeanX.change_face("bemused", 1)
                if JeanX.Clothes["bottom"] and (JeanX.love+JeanX.obedience) <= (2*JeanX.inhibition):
                    $ JeanX.mouth = "smile"
                    ch_j "I -could, - but I'd rather not. . ."
                    menu:
                        "Fine by me":
                            return
                        "I insist, put some on.":
                            if (JeanX.love+JeanX.obedience) <= (1.5*JeanX.inhibition):
                                $ JeanX.change_face("angry", eyes = "side")
                                ch_j "Well too bad."
                                return
                            else:
                                $ JeanX.change_face("sadside")
                                ch_j "Oh, fine."
                else:
                    ch_j "I guess. . ."
                menu:
                    extend ""
                    "How about the green ones?":
                        ch_j "Sure, ok."
                        $ JeanX.Clothes["underwear"] = "green_panties"
                    "How about the lace ones?" if "lace_panties" in JeanX.inventory:
                        ch_j "Fine."
                        $ JeanX.Clothes["underwear"]  = "lace_panties"
            "Never mind":
                pass
        return
    "Never mind":
        pass
return




menu Jean_Clothes_Misc:

    "Maybe dry out your hair." if JeanX.Clothes["hair"] == "wet":
        ch_p "Maybe dry out your hair"
        if approval_check(JeanX, 600):
            ch_j "Ok."
            $ JeanX.Clothes["hair"] = "short"
        else:
            ch_j "I don't know, it's fine like this."

    "Wet hair style." if JeanX.Clothes["hair"] != "wet":
        ch_p "You should go for that wet look with your hair"
        if approval_check(JeanX, 800):
            ch_j "Hmm?"
            $ JeanX.Clothes["hair"] = "wet"
            "She wanders off for a minute and comes back."
            ch_j "Like this?"
        else:
            ch_j "Ugh, too much work."

    "Ponytail" if JeanX.Clothes["hair"] != "pony" and "halloween" in JeanX.history:
        ch_p "Maybe do that side ponytail you had."
        if approval_check(JeanX, 600):
            ch_j "Ok."
            $ JeanX.Clothes["hair"] = "pony"
        else:
            ch_j "I don't know, it's fine like this."
    "Let your hair loose" if JeanX.Clothes["hair"] == "pony":
        ch_p "Maybe drop the ponytail."
        if approval_check(JeanX, 600):
            ch_j "Ok."
            $ JeanX.Clothes["hair"] = "short"
        else:
            ch_j "I don't know, it's fine like this."

    "Grow pubes." if not JeanX.pubes:
        ch_p "You know, I like some nice hair down there. Maybe grow it out."
        if "pubes" in JeanX.to_do:
            $ JeanX.change_face("bemused", 1)
            ch_j "Give it some time. . ."
        else:
            $ JeanX.change_face("bemused", 1)
            if approval_check(JeanX, 1000, taboo_modifier=0):
                ch_j "Ok, sure. . ."
            else:
                $ JeanX.change_face("surprised")
                $ JeanX.brows = "angry"
                ch_j "None of your business."
                return
            $ JeanX.to_do.append("pubes")
            $ JeanX.pubes_counter = 6
    "Shave pubes" if JeanX.pubes == "_hairy":
        ch_p "I like it waxed clean down there."
        $ JeanX.change_face("bemused", 1)
        if "shave" in JeanX.to_do:
            ch_j "Yeah, I know, I'll get to it."
        else:
            if approval_check(JeanX, 1100, taboo_modifier=0):
                ch_j "Really? I guess I could give it a shave. . ."
            else:
                $ JeanX.change_face("surprised")
                $ JeanX.brows = "angry"
                ch_j "None of your business."
                return
            $ JeanX.to_do.append("shave")

    "Piercings. [[See what she looks like without them first] (locked)" if not JeanX.seen_pussy and not JeanX.seen_breasts:
        pass

    "Add ring piercings" if JeanX.Clothes["piercings"] != "ring" and (JeanX.seen_pussy or JeanX.seen_breasts):
        ch_p "You know, you'd look really nice with some ring body piercings"
        if "ring" in JeanX.to_do:
            ch_j "Yeah, I know, I'll get to it."
        else:
            $ JeanX.change_face("bemused", 1)
            $ approval = approval_check(JeanX, 1150, taboo_modifier=0)
            if approval_check(JeanX, 900, "L", taboo_modifier=0) or (approval and JeanX.love > 2* JeanX.obedience):
                ch_j "You think they'd look good on me?"
            elif approval_check(JeanX, 600, "I", taboo_modifier=0) or (approval and JeanX.inhibition > JeanX.obedience):
                ch_j "I've been thinking about that for a while."
            elif approval_check(JeanX, 500, "O", taboo_modifier=0) or approval:
                ch_j "Sure, [JeanX.player_petname]."
            else:
                $ JeanX.change_face("surprised")
                $ JeanX.brows = "angry"
                ch_j "Not interested, [JeanX.player_petname]."
                return
            $ JeanX.to_do.append("ring")

    "Add barbell piercings" if JeanX.Clothes["piercings"] != "barbell" and (JeanX.seen_pussy or JeanX.seen_breasts):
        ch_p "You know, you'd look really nice with some barbell body piercings"
        if "barbell" in JeanX.to_do:
            ch_j "Yeah, I know, I'll get to it."
        else:
            $ JeanX.change_face("bemused", 1)
            $ approval = approval_check(JeanX, 1150, taboo_modifier=0)
            if approval_check(JeanX, 900, "L", taboo_modifier=0) or (approval and JeanX.love > 2*JeanX.obedience):
                ch_j "You think they'd look good on me?"
            elif approval_check(JeanX, 600, "I", taboo_modifier=0) or (approval and JeanX.inhibition > JeanX.obedience):
                ch_j "I've been thinking about that for a while."
            elif approval_check(JeanX, 500, "O", taboo_modifier=0) or approval:
                ch_j "Sure, [JeanX.player_petname]."
            else:
                $ JeanX.change_face("surprised")
                $ JeanX.brows = "angry"
                ch_j "Not interested, [JeanX.player_petname]."
                return
            $ JeanX.to_do.append("barbell")

    "Remove Piercings" if JeanX.Clothes["piercings"]:
        ch_p "You know, you'd look better without those piercings."
        $ JeanX.change_face("bemused", 1)
        $ approval = approval_check(JeanX, 1350, taboo_modifier=0)
        if approval_check(JeanX, 950, "L", taboo_modifier=0) or (approval and JeanX.love > JeanX.obedience):
            ch_j "Make up your mind . ."
        elif approval_check(JeanX, 700, "I", taboo_modifier=0) or (approval and JeanX.inhibition > JeanX.obedience):
            ch_j "What?"
        elif approval_check(JeanX, 600, "O", taboo_modifier=0) or approval:
            ch_j "Fine."
        else:
            $ JeanX.change_face("surprised")
            $ JeanX.brows = "angry"
            ch_j "I don't know, I kinda like them now. . ."
            return
        $ JeanX.take_off("piercings")

    "Add Suspenders" if JeanX.Clothes["suspenders"] != "suspenders" and JeanX.Clothes["suspenders"] != "suspenders2" and "halloween" in JeanX.history:
        $ JeanX.Clothes["suspenders"] = "suspenders"
    "Remove Suspenders" if JeanX.Clothes["suspenders"] == "suspenders" or JeanX.Clothes["suspenders"] == "suspenders2":
        $ JeanX.take_off("suspenders")

    "Shift Suspenders" if JeanX.Clothes["suspenders"] == "suspenders" or JeanX.Clothes["suspenders"] == "suspenders2":
        $ JeanX.Clothes["suspenders"] = "suspenders" if JeanX.Clothes["suspenders"] == "suspenders2" else "suspenders2"
    "Never mind":















        pass
return
