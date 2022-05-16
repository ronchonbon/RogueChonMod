


label Jean_Relationship:
    while True:
        menu:
            ch_j "What did you want to talk about?"
            "Do you want to be my girlfriend?" if JeanX not in Player.Harem and "ex" not in JeanX.Traits:
                $ JeanX.daily_history.append("relationship")
                if "asked boyfriend" in JeanX.daily_history and "angry" in JeanX.daily_history:
                    $ JeanX.change_face("angry", 1)
                    ch_j "Again with this? No!"
                    return
                elif "asked boyfriend" in JeanX.daily_history:
                    $ JeanX.change_face("angry", 1)
                    ch_j "Still no."
                    return
                elif JeanX.Break[0]:
                    $ JeanX.change_face("angry", 1)
                    ch_j "You have to be kidding."
                    if Player.Harem:
                        $ JeanX.daily_history.append("asked boyfriend")
                        return
                    else:
                        ch_p "I'm serious."

                $ JeanX.daily_history.append("asked boyfriend")

                if Player.Harem and "JeanYes" not in Player.Traits:
                    if len(Player.Harem) >= 2:
                        ch_j "Hey, apparently it's those other girls' problem, [JeanX.player_petname]."
                    else:
                        ch_j "Hey, apparently it's [Player.Harem[0].name]'s problem, [JeanX.player_petname]."
                    return

                if JeanX.Event[5]:
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
                    $ JeanX.change_stat("love", 200, 40)
                    ch_j "Huh. Ok."
                    if "boyfriend" not in JeanX.player_petnames:
                        $ JeanX.player_petnames.append("boyfriend")
                    if "JeanYes" in Player.Traits:
                        $ Player.Traits.remove("JeanYes")
                    $ Player.Harem.append(JeanX)
                    call Harem_Initiation
                    "[JeanX.name] floats in and kisses you deeply."
                    $ JeanX.change_face("kiss", 1)
                    $ JeanX.action_counter["kiss"] += 1
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

            "Do you want to get back together?" if "ex" in JeanX.Traits:
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

                if Player.Harem and "JeanYes" not in Player.Traits:
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
                    $ JeanX.change_stat("love", 90, 5)
                    ch_j "Oh, fine, whatever."
                    if "boyfriend" not in JeanX.player_petnames:
                        $ JeanX.player_petnames.append("boyfriend")
                    $ JeanX.Traits.remove("ex")
                    if "JeanYes" in Player.Traits:
                        $ Player.Traits.remove("JeanYes")
                    $ Player.Harem.append(JeanX)
                    call Harem_Initiation
                    "[JeanX.name] floats in and kisses you."
                    $ JeanX.change_face("kiss", 1)
                    $ JeanX.action_counter["kiss"] += 1
                elif JeanX.love >= 600 and approval_check(JeanX, 1500):
                    $ JeanX.change_face("smile", 1)
                    $ JeanX.change_stat("love", 90, 5)
                    ch_j "Sure, whatever."
                    if "boyfriend" not in JeanX.player_petnames:
                        $ JeanX.player_petnames.append("boyfriend")
                    $ JeanX.Traits.remove("ex")
                    if "JeanYes" in Player.Traits:
                        $ Player.Traits.remove("JeanYes")
                    $ Player.Harem.append(JeanX)
                    call Harem_Initiation
                    $ JeanX.change_face("kiss", 1)
                    "[JeanX.name] gives you a quick kiss."
                    $ JeanX.change_face("sly", 1)
                    $ JeanX.action_counter["kiss"] += 1
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
            "Never Mind":

                return

    return

label Jean_OtherWoman(counter=0):

    if not Player.Harem:
        return
    $ counter = int((JeanX.GirlLikeCheck(Player.Harem[0]) - 500)/2)

    $ JeanX.change_face("perplexed")
    if len(Player.Harem) >= 2:
        ch_j "Aren't you hanging out with. . . [Player.Harem[0].name] right now?"
        ch_j "And that's not all, if I'm reading the room right."
    else:
        ch_j "Aren't you hanging out with. . . [Player.Harem[0].name] right now?"
    menu:
        extend ""
        "She said I can be with you too." if "JeanYes" in Player.Traits:
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



        "I could ask if she'd be ok with me dating you both." if "JeanYes" not in Player.Traits:
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
            $ JeanX.Traits.append("downlow")
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
        if "poly Rogue" in JeanX.Traits:
            ch_j "I mean, she's a pretty good lay. . ."
        elif JeanX.LikeRogue >= 900:
            ch_j "She is kinda sexy. . ."
        elif JeanX.LikeRogue >= 800:
            ch_j "I don't know, she's fine. . ."
        elif JeanX.LikeRogue >= 700:
            ch_j "She's good in class or something?"
        elif JeanX.LikeRogue >= 600:
            ch_j "She's the one with the white stripe, right?"
        elif JeanX.LikeRogue >= 500:
            ch_j "Who?"
        elif JeanX.LikeRogue >= 400:
            ch_j "I don't spend much time thinking about her."
        elif JeanX.LikeRogue >= 300:
            ch_j "She can go to hell."
        else:
            ch_j "Bitch."
    elif Check == KittyX:
        if "poly Kitty" in JeanX.Traits:
            ch_j "I mean, she's a pretty good lay. . ."
        elif JeanX.LikeKitty >= 900:
            ch_j "She is kinda cute. . ."
        elif JeanX.LikeKitty >= 800:
            ch_j "I don't know, she's fine. . ."
        elif JeanX.LikeKitty >= 700:
            ch_j "She's, uh, a jock or something?"
        elif JeanX.LikeKitty >= 600:
            ch_j "She's the one with the tiny tits, right? Ghost girl?"
        elif JeanX.LikeKitty >= 500:
            ch_j "Who?"
        elif JeanX.LikeKitty >= 400:
            ch_j "I don't spend much time thinking about her."
        elif JeanX.LikeKitty >= 300:
            ch_j "She can go to hell."
        else:
            ch_j "Bitch."
    elif Check == EmmaX:
        if "poly Emma" in JeanX.Traits:
            ch_j "I mean, she's an amazing lay. . ."
        elif JeanX.LikeEmma >= 900:
            ch_j "She is pretty thicc. . ."
        elif JeanX.LikeEmma >= 800:
            ch_j "I don't know, she's fine. . ."
        elif JeanX.LikeEmma >= 700:
            ch_j "She's prety hot, for an old."
        elif JeanX.LikeEmma >= 600:
            ch_j "She's the teacher, right?"
        elif JeanX.LikeEmma >= 500:
            ch_j "Who? Oh, the teacher, right?"
        elif JeanX.LikeEmma >= 400:
            ch_j "I could do with less of her attitude."
        elif JeanX.LikeEmma >= 300:
            ch_j "She needs to mind her business."
        else:
            ch_j "Grrrrr."
    elif Check == LauraX:
        if "poly Laura" in JeanX.Traits:
            ch_j "I mean, she's a pretty good lay. . ."
        elif JeanX.LikeLaura >= 900:
            ch_j "She is pretty fit. . ."
        elif JeanX.LikeLaura >= 800:
            ch_j "I don't know, she's fine. . ."
        elif JeanX.LikeLaura >= 700:
            ch_j "She's good in class or something?"
        elif JeanX.LikeLaura >= 600:
            ch_j "She's the one with the claws, right?"
        elif JeanX.LikeLaura >= 500:
            ch_j "Who?"
        elif JeanX.LikeLaura >= 400:
            ch_j "I don't spend much time thinking about her."
        elif JeanX.LikeLaura >= 300:
            ch_j "She can go to hell."
        else:
            ch_j "Bitch."
    elif Check == StormX:
        if "poly Storm" in JeanX.Traits:
            ch_j "She's so squishy!"
        elif JeanX.LikeStorm >= 900:
            ch_j "She's. . . hot."
        elif JeanX.LikeStorm >= 800:
            ch_j "I don't know, she's fine. . ."
        elif JeanX.LikeStorm >= 700:
            ch_j "She's prety hot, for an old."
        elif JeanX.LikeStorm >= 600:
            ch_j "She's the teacher, right?"
        elif JeanX.LikeStorm >= 500:
            ch_j "Who? Oh, the teacher, right?"
        elif JeanX.LikeStorm >= 400:
            ch_j "I could do with less of her attitude."
        elif JeanX.LikeStorm >= 300:
            ch_j "She needs to mind her business."
        else:
            ch_j "Grrrrr."
    elif Check == JubesX:
        if "poly Jubes" in JeanX.Traits:
            ch_j "I mean, she's a pretty good lay. . ."
        elif JeanX.LikeJubes >= 900:
            ch_j "She is kinda cute. . ."
        elif JeanX.LikeJubes >= 800:
            ch_j "I don't know, she's fine. . ."
        elif JeanX.LikeJubes >= 700:
            ch_j "I think I saw her around. . ."
        elif JeanX.LikeJubes >= 600:
            ch_j "She's the vampire, right?"
        elif JeanX.LikeJubes >= 500:
            ch_j "Who?"
        elif JeanX.LikeJubes >= 400:
            ch_j "I don't spend much time thinking about her."
        elif JeanX.LikeJubes >= 300:
            ch_j "She can get staked."
        else:
            ch_j "Bitch."
    return


label Jean_Monogamy:

    menu:
        "Could you not hook up with other girls?" if "mono" not in JeanX.Traits:
            if JeanX.Thirst >= 60 and not approval_check(JeanX, 1700, "LO", TabM=0):

                $ JeanX.change_face("sly",1)
                if "mono" not in JeanX.daily_history:
                    $ JeanX.change_stat("obedience", 90, -2)
                ch_j "Sorry, I've got plans later."
                return
            elif approval_check(JeanX, 1200, "LO", TabM=0) and JeanX.love >= JeanX.obedience:

                $ JeanX.change_face("sly",1)
                if "mono" not in JeanX.daily_history:
                    $ JeanX.change_stat("love", 90, 1)
                ch_j "Oh, jealous?"
                ch_j "Ok, fine, but you owe me. . ."
            elif approval_check(JeanX, 700, "O", TabM=0):

                $ JeanX.change_face("sly",1,Eyes="side")
                ch_j "Well. . . ok, fine."
            else:

                $ JeanX.change_face("sly",1)
                ch_j "Ha!"
                return
            if "mono" not in JeanX.daily_history:
                $ JeanX.change_stat("obedience", 90, 3)
            $ JeanX.AddWord(1,0,"mono")
            $ JeanX.Traits.append("mono")
        "Don't hook up with other girls." if "mono" not in JeanX.Traits:
            if approval_check(JeanX, 900, "O", TabM=0):

                $ JeanX.change_face("sly",1,Eyes="side")
                ch_j "Well. . . ok, fine."
            elif JeanX.Thirst >= 60 and not approval_check(JeanX, 1700, "LO", TabM=0):

                $ JeanX.change_face("sly",1)
                if "mono" not in JeanX.daily_history:
                    $ JeanX.change_stat("obedience", 90, -2)
                ch_j "Sorry, I've got plans later."
                return
            elif approval_check(JeanX, 600, "O", TabM=0):

                $ JeanX.change_face("sly",1,Eyes="side")
                ch_j "Well. . . ok, fine."
            elif approval_check(JeanX, 1400, "LO", TabM=0):

                $ JeanX.change_face("sly",1)
                ch_j "Oh, jealous?"
                ch_j "Ok, fine, but you owe me. . ."
            else:

                $ JeanX.change_face("sly",1,Brows="confused")
                ch_j "Ha!"
                return
            if "mono" not in JeanX.daily_history:
                $ JeanX.change_stat("obedience", 90, 3)
            $ JeanX.AddWord(1,0,"mono")
            $ JeanX.Traits.append("mono")
        "It's ok if you hook up with other girls." if "mono" in JeanX.Traits:
            if approval_check(JeanX, 700, "O", TabM=0):
                $ JeanX.change_face("sly",1,Eyes="side")
                ch_j ". . . good."
            elif approval_check(JeanX, 800, "L", TabM=0):
                $ JeanX.change_face("sly",1)
                ch_j "Ok. . ."
            else:
                $ JeanX.change_face("sly",1,Brows="confused")
                if "mono" not in JeanX.daily_history:
                    $ JeanX.change_stat("love", 90, -2)
                ch_j "Good to know. . ."
            if "mono" not in JeanX.daily_history:
                $ JeanX.change_stat("obedience", 90, 3)
            if "mono" in JeanX.Traits:
                $ JeanX.Traits.remove("mono")
            $ JeanX.AddWord(1,0,"mono")
        "Never mind.":
            pass
    return



label Jean_Jumped:

    ch_p "Hey, Remember that time you threw yourself at me?"
    $ JeanX.change_face("sly",1,Brows="confused")
    ch_j "I'm not sure I'd put it like that, but. . . yeah?"
    menu:
        ch_j ". . . yeah?"
        "Could you maybe just ask instead?" if "chill" not in JeanX.Traits:
            if JeanX.Thirst >= 60 and not approval_check(JeanX, 1500, "LO", TabM=0):

                $ JeanX.change_face("sly",1)
                if "chill" not in JeanX.daily_history:
                    $ JeanX.change_stat("obedience", 90, -2)
                ch_j "Why waste the time?"
                ch_j "It's not like you'd say \"no.\""
                return
            elif approval_check(JeanX, 1000, "LO", TabM=0) and JeanX.love >= JeanX.obedience:

                $ JeanX.change_face("surprised",1)
                if "chill" not in JeanX.daily_history:
                    $ JeanX.change_stat("love", 90, 1)
                ch_j "I was really horny though. . ."
                $ JeanX.change_face("sly",1,Eyes="side")
                ch_j "I'll give it some thought. . ."
            elif approval_check(JeanX, 500, "O", TabM=0):

                $ JeanX.change_face("sly",1,Eyes="side")
                ch_j "Maybe. . ."
            else:

                $ JeanX.change_face("sly",1)
                ch_j "Why waste the time?"
                ch_j "It's not like you'd say \"no.\""
                return
            if "chill" not in JeanX.daily_history:
                $ JeanX.change_stat("obedience", 90, 3)
            $ JeanX.AddWord(1,0,"chill")
            $ JeanX.Traits.append("chill")
        "Don't bother me like that." if "chill" not in JeanX.Traits:
            if approval_check(JeanX, 800, "O", TabM=0):

                $ JeanX.change_face("sly",1,Eyes="side")
                ch_j ". . . fine. . ."
            elif JeanX.Thirst >= 60 and not approval_check(JeanX, 500, "O", TabM=0):

                $ JeanX.change_face("sly",1)
                if "chill" not in JeanX.daily_history:
                    $ JeanX.change_stat("obedience", 90, -2)
                ch_j "Why waste the time?"
                ch_j "It's not like you'd say \"no.\""
                return
            elif approval_check(JeanX, 400, "O", TabM=0):

                $ JeanX.change_face("sly",1,Eyes="side")
                ch_j "Well. . . ok. . ."
            elif approval_check(JeanX, 500, "LO", TabM=0) and not approval_check(JeanX, 500, "I", TabM=0):

                $ JeanX.change_face("sly",1)
                ch_j "Rude."
                ch_j "I guess I cna try though. . ."
            else:

                $ JeanX.change_face("sly",1)
                ch_j "Why waste the time?"
                ch_j "It's not like you'd say \"no.\""
                return
            if "chill" not in JeanX.daily_history:
                $ JeanX.change_stat("obedience", 90, 3)
            $ JeanX.AddWord(1,0,"chill")
            $ JeanX.Traits.append("chill")
        "Knock yourself out.":
            if approval_check(JeanX, 800, "L", TabM=0):
                $ JeanX.change_face("sly",1)
                ch_j "Heh, you know how I think. . ."
            elif approval_check(JeanX, 700, "O", TabM=0):
                $ JeanX.change_face("sly",1,Eyes="side")
                ch_j "Good to know."
            else:
                $ JeanX.change_face("sly",1,Brows="confused")
                if "chill" not in JeanX.daily_history:
                    $ JeanX.change_stat("love", 90, -2)
                ch_j "We'll see. . ."
            if "chill" not in JeanX.daily_history:
                $ JeanX.change_stat("obedience", 90, 3)
            if "chill" in JeanX.Traits:
                $ JeanX.Traits.remove("chill")
            $ JeanX.AddWord(1,0,"chill")
        "Um, never mind.":
            pass
    return




label Jean_Hungry:
    if JeanX.Chat[3]:
        ch_j "Hey, gimme a taste. . ."
    elif JeanX.Chat[2]:
        ch_j "Hey, I could use some of that. . . serum. . ."
    else:
        ch_j "I really like. . . your flavor. . ."
    $ JeanX.Traits.append("hungry")
return





label Jean_SexChat:
    $ Line = "Yeah, what did you want to talk about?" if not Line else Line
    while True:
        menu:
            ch_j "[Line]"
            "My favorite thing to do is. . .":
                if "setfav" in JeanX.daily_history:
                    ch_j "I remember."
                else:
                    menu:
                        "Sex.":
                            $ JeanX.change_face("sly")
                            if JeanX.player_favorite_action == "sex":
                                $ JeanX.change_stat("lust", 80, 5)
                                ch_j "Yeah, I know that. . ."
                            elif JeanX.favorite_action == "sex":
                                $ JeanX.change_stat("love", 90, 5)
                                $ JeanX.change_stat("lust", 80, 10)
                                ch_j "I really like it too!"
                            elif JeanX.action_counter["sex"] >= 5:
                                ch_j "Well I don't mind that."
                            elif not JeanX.action_counter["sex"]:
                                $ JeanX.change_face("perplexed")
                                ch_j "Oh? Who with?"
                            else:
                                $ JeanX.change_face("bemused")
                                ch_j "Heh, um, yeah, it's nice. . ."
                            $ JeanX.player_favorite_action = "sex"
                        "Anal.":

                            $ JeanX.change_face("sly")
                            if JeanX.player_favorite_action == "anal":
                                $ JeanX.change_stat("lust", 80, 5)
                                ch_j "So you've said. . ."
                            elif JeanX.favorite_action == "anal":
                                $ JeanX.change_stat("love", 90, 5)
                                $ JeanX.change_stat("lust", 80, 10)
                                ch_j "I love it too!"
                            elif JeanX.action_counter["anal"] >= 10:
                                ch_j "Yeah, it's. . . nice. . ."
                            elif not JeanX.action_counter["anal"]:
                                $ JeanX.change_face("perplexed")
                                ch_j "Oh? Who with?"
                            else:
                                $ JeanX.change_face("bemused",Eyes="side")
                                ch_j "Heh, heh, yeah, um, it's ok. . ."
                            $ JeanX.player_favorite_action = "anal"
                        "Blowjobs.":

                            $ JeanX.change_face("sly")
                            if JeanX.player_favorite_action == "blowjob":
                                $ JeanX.change_stat("lust", 80, 3)
                                ch_j "Yeah, I know."
                            elif JeanX.favorite_action == "blowjob":
                                $ JeanX.change_stat("love", 90, 5)
                                $ JeanX.change_stat("lust", 80, 5)
                                ch_j "I can't say I hate it either. . ."
                            elif JeanX.action_counter["blowjob"] >= 10:
                                ch_j "Yeah, you're surprisingly tasty."
                            elif not JeanX.action_counter["blowjob"]:
                                $ JeanX.change_face("perplexed")
                                ch_j "Oh? Who with?"
                            else:
                                $ JeanX.change_face("bemused")
                                ch_j "You're lucky you taste so good."
                            $ JeanX.player_favorite_action = "blowjob"
                        "Titjobs.":

                            $ JeanX.change_face("sly")
                            if JeanX.player_favorite_action == "titjob":
                                $ JeanX.change_stat("lust", 80, 5)
                                ch_j "Yeah, you've said that before. . ."
                            elif JeanX.favorite_action == "titjob":
                                $ JeanX.change_stat("love", 90, 5)
                                $ JeanX.change_stat("lust", 80, 7)
                                ch_j "Yeah, I enjoy that too. . ."
                            elif JeanX.action_counter["titjob"] >= 10:
                                ch_j "Nice, right?"
                            elif not JeanX.action_counter["titjob"]:
                                $ JeanX.change_face("perplexed")
                                ch_j "Oh? Who with?"
                            else:
                                $ JeanX.change_face("bemused")
                                ch_j "They are pretty nice. . ."
                                $ JeanX.change_stat("love", 80, 5)
                                $ JeanX.change_stat("inhibition", 50, 10)
                            $ JeanX.player_favorite_action = "titjob"
                        "Footjobs.":

                            $ JeanX.change_face("sly")
                            if JeanX.player_favorite_action == "foot":
                                $ JeanX.change_stat("lust", 80, 5)
                                ch_j "Yeah, you've said that. . ."
                            elif JeanX.favorite_action == "foot":
                                $ JeanX.change_stat("love", 90, 5)
                                $ JeanX.change_stat("lust", 80, 7)
                                ch_j "I do like using my feet. . ."
                            elif JeanX.action_counter["footjob"] >= 10:
                                ch_j "I like it too . . ."
                            elif not JeanX.action_counter["footjob"]:
                                $ JeanX.change_face("perplexed")
                                ch_j "Oh? Who with?"
                            else:
                                $ JeanX.change_face("bemused")
                                ch_j "Yeah, it's nice. . ."
                            $ JeanX.player_favorite_action = "foot"
                        "Handjobs.":

                            $ JeanX.change_face("sly")
                            if JeanX.player_favorite_action == "handjob":
                                $ JeanX.change_stat("lust", 80, 5)
                                ch_j "Yeah, you've said that. . ."
                            elif JeanX.favorite_action == "handjob":
                                $ JeanX.change_stat("love", 90, 5)
                                $ JeanX.change_stat("lust", 80, 7)
                                ch_j "I do have quite the touch. . ."
                            elif JeanX.action_counter["handjob"] >= 10:
                                ch_j "I like it too . . ."
                            elif not JeanX.action_counter["handjob"]:
                                $ JeanX.change_face("perplexed")
                                ch_j "Oh? Who with?"
                            else:
                                $ JeanX.change_face("bemused")
                                ch_j "Yeah, it's nice. . ."
                            $ JeanX.player_favorite_action = "handjob"
                        "Feeling you up.":

                            $ counter = JeanX.action_counter["fondle_breasts"]+ JeanX.action_counter["fondle_thighs"]+ JeanX.action_counter["suck_breasts"] + JeanX.action_counter["hotdog"]
                            $ JeanX.change_face("sly")
                            if JeanX.player_favorite_action == "fondle":
                                $ JeanX.change_stat("lust", 80, 3)
                                ch_j "Yeah, I think we're clear on that. . ."
                            elif JeanX.favorite_action in ("hotdog","suck_breasts","fondle_breasts","fondle_thighs"):
                                $ JeanX.change_stat("love", 90, 5)
                                $ JeanX.change_stat("lust", 80, 5)
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
                                $ JeanX.change_stat("love", 90, 3)
                                ch_j "Dork. . ."
                            elif JeanX.favorite_action == "kiss":
                                $ JeanX.change_stat("love", 90, 5)
                                $ JeanX.change_stat("lust", 80, 5)
                                ch_j "I. . . do too, ok? . ."
                            elif JeanX.action_counter["kiss"] >= 10:
                                ch_j "Yeah, it's fun . . ."
                            elif not JeanX.action_counter["kiss"]:
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
                    elif JeanX.favorite_action == "foot":
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



            "Don't talk as much during sex." if "vocal" in JeanX.Traits:
                if "setvocal" in JeanX.daily_history:
                    $ JeanX.change_face("perplexed")
                    ch_j "Don't jerk me around, [Girl.player_petname]."
                else:
                    if approval_check(JeanX, 1000) and JeanX.obedience <= JeanX.love:
                        $ JeanX.change_face("bemused")
                        $ JeanX.change_stat("obedience", 90, 1)
                        ch_j ". . . fine."
                        $ JeanX.Traits.remove("vocal")
                    elif approval_check(JeanX, 700, "O"):
                        $ JeanX.change_face("sadside")
                        $ JeanX.change_stat("obedience", 90, 1)
                        ch_j ". . ."
                        $ JeanX.Traits.remove("vocal")
                    elif approval_check(JeanX, 600):
                        $ JeanX.change_face("sly")
                        $ JeanX.change_stat("love", 90, -3)
                        $ JeanX.change_stat("obedience", 50, -1)
                        $ JeanX.change_stat("inhibition", 90, 5)
                        ch_j "Oh, I'll talk and you'll listen, [JeanX.player_petname]."
                    else:
                        $ JeanX.change_face("angry")
                        $ JeanX.change_stat("love", 90, -5)
                        $ JeanX.change_stat("obedience", 60, -3)
                        $ JeanX.change_stat("inhibition", 90, 10)
                        ch_j "Yeah, that'll be the day. . ."

                    $ JeanX.daily_history.append("setvocal")
            "Talk dirty to me during sex." if "vocal" not in JeanX.Traits:
                if "setvocal" in JeanX.daily_history:
                    $ JeanX.change_face("perplexed")
                    ch_j "Don't jerk me around, [Girl.player_petname]."
                else:
                    if approval_check(JeanX, 1000) and JeanX.obedience <= JeanX.love:
                        $ JeanX.change_face("sly")
                        $ JeanX.change_stat("obedience", 90, 2)
                        ch_j "I think that can be arranged. . ."
                        $ JeanX.Traits.append("vocal")
                    elif approval_check(JeanX, 700, "O"):
                        $ JeanX.change_face("sadside")
                        $ JeanX.change_stat("obedience", 90, 2)
                        ch_j "I'll see what I can do, [JeanX.player_petname]."
                        $ JeanX.Traits.append("vocal")
                    elif approval_check(JeanX, 600):
                        $ JeanX.change_face("sly")
                        $ JeanX.change_stat("obedience", 90, 3)
                        ch_j "Sure, whatever."
                        $ JeanX.Traits.append("vocal")
                    else:
                        $ JeanX.change_face("angry")
                        $ JeanX.change_stat("inhibition", 90, 5)
                        ch_j ". . ."

                    $ JeanX.daily_history.append("setvocal")


            "Don't do your own thing as much during sex." if "passive" not in JeanX.Traits:
                if "initiative" in JeanX.daily_history:
                    $ JeanX.change_face("perplexed")
                    ch_j "Don't jerk me around, [Girl.player_petname]."
                else:
                    if approval_check(JeanX, 1200) and JeanX.obedience <= JeanX.love:
                        $ JeanX.change_face("bemused")
                        $ JeanX.change_stat("obedience", 90, 1)
                        ch_j "Like me \"passive?\" I'll see what I can do. . ."
                        $ JeanX.Traits.append("passive")
                    elif approval_check(JeanX, 700, "O"):
                        $ JeanX.change_face("sadside")
                        $ JeanX.change_stat("obedience", 90, 1)
                        ch_j ". . . yeah, ok. . ."
                        $ JeanX.Traits.append("passive")
                    elif approval_check(JeanX, 600):
                        $ JeanX.change_face("sly")
                        $ JeanX.change_stat("love", 90, -3)
                        $ JeanX.change_stat("obedience", 50, -1)
                        $ JeanX.change_stat("inhibition", 90, 5)
                        ch_j "Hm, -NO.-"
                    else:
                        $ JeanX.change_face("angry")
                        $ JeanX.change_stat("love", 90, -5)
                        $ JeanX.change_stat("obedience", 60, -3)
                        $ JeanX.change_stat("inhibition", 90, 10)
                        ch_j "You wish."

                    $ JeanX.daily_history.append("initiative")
            "Take more initiative during sex." if "passive" in JeanX.Traits:
                if "initiative" in JeanX.daily_history:
                    $ JeanX.change_face("perplexed")
                    ch_j "Don't jerk me around, [Girl.player_petname]."
                else:
                    if approval_check(JeanX, 1000) and JeanX.obedience <= JeanX.love:
                        $ JeanX.change_face("bemused")
                        $ JeanX.change_stat("obedience", 90, 1)
                        ch_j "Damned right I will."
                        $ JeanX.Traits.remove("passive")
                    elif approval_check(JeanX, 700, "O"):
                        $ JeanX.change_face("sadside")
                        $ JeanX.change_stat("obedience", 90, 1)
                        ch_j ". . . fine. . ."
                        $ JeanX.Traits.remove("passive")
                    elif approval_check(JeanX, 600):
                        $ JeanX.change_face("sly")
                        $ JeanX.change_stat("obedience", 90, 3)
                        ch_j "Sure."
                        $ JeanX.Traits.remove("passive")
                    else:
                        $ JeanX.change_face("angry")
                        $ JeanX.change_stat("inhibition", 90, 5)
                        ch_j "Ugh, don't bother me with that, figure it out yourself."

                    $ JeanX.daily_history.append("initiative")

            "About getting Jumped" if "jumped" in JeanX.history:
                call Jean_Jumped

            "About that \"mind screen\"" if "screen" in JeanX.Traits or "noscreen" in JeanX.Traits:
                ch_j "You mean how I can make Chuck ignore us a sometimes?"
                menu:
                    extend ""
                    "Yeah, do that." if "noscreen" in JeanX.Traits:
                        ch_j "Nice. . ."
                        $ JeanX.Traits.append("screen")
                    "Don't do that anymore, I want him to know." if "screen" in JeanX.Traits:
                        ch_j "So naughty. . ."
                        if approval_check(JeanX, 900, "OI"):
                            $ JeanX.change_face("sad")
                            ch_j "Fine, I can leave it down."
                            $ JeanX.change_face("bemused")
                            $ JeanX.Traits.append("noscreen")
                        else:
                            ch_j "Still, I don't like him bothering us."
                            ch_j "I'll keep the screen up anyway."
                    "Never mind.":
                        pass


            "About that \"whammy\" you do?" if "whammy" in JeanX.Traits or "nowhammy" in JeanX.Traits:
                ch_j "You mean how I mind wipe the other students so they don't know what a freak I am?"
                menu:
                    extend ""
                    "That is so cool":
                        if "whammytalk" not in JeanX.Chat:
                            $ JeanX.change_stat("love", 60, 10)
                            $ JeanX.change_stat("love", 90, 5)
                            $ JeanX.change_stat("obedience", 60, 10)
                            $ JeanX.change_stat("obedience", 80, 5)
                            $ JeanX.change_stat("inhibition", 90, 10)
                        ch_j "I know, right?"
                        $ JeanX.Chat.append("whammytalk")
                    "Yeah, can should start doing that again." if "nowhammy" in JeanX.Traits:
                        ch_j "Oh, well. . ."
                        if "Alpha" not in Player.Traits:

                            $ JeanX.change_face("sad")
                            ch_j "I'd love to, but Chuck'd have my ovaries over it. . ."
                        elif approval_check(JeanX, 800, "I"):
                            if "whammytalk" not in JeanX.daily_history:
                                $ JeanX.change_stat("love", 80, 10)
                                $ JeanX.change_stat("obedience", 60, 5)
                                $ JeanX.change_stat("inhibition", 90, 10)
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
                                $ JeanX.change_stat("love", 90, 5)
                                $ JeanX.change_stat("obedience", 60, 3)
                            ch_j "Ok, thanks. . ."
                            $ JeanX.Traits.append("whammy")
                        $ JeanX.daily_history.append("whammytalk")
                    "Don't do that anymore, I want them to remember." if "whammy" in JeanX.Traits:
                        if "whammytalk" not in JeanX.daily_history:
                            $ JeanX.change_stat("obedience", 60, 5)
                            $ JeanX.change_stat("obedience", 85, 5)
                            $ JeanX.change_stat("inhibition", 90, 10)
                        ch_j "Oh, well. . ."
                        if approval_check(JeanX, 1500):
                            $ JeanX.change_face("sad")
                            ch_j "Ok, I guess I can. . ."
                            $ JeanX.Traits.append("nowhammy")
                        else:
                            $ JeanX.change_face("bemused")
                            ch_j "Well too bad for you. . ."
                        $ JeanX.daily_history.append("whammytalk")
                    "Never mind.":
                        pass
            "About when you masturbate":


                call NoFap (JeanX)

            "Never Mind" if Line == "Yeah, what did you want to talk about?":
                return
            "That's all." if Line != "Yeah, what did you want to talk about?":
                return
        if Line == "Yeah, what did you want to talk about?":
            $ Line = "Anything else?"
    return




label Jean_Chitchat(O=0, Options=["default","default","default"]):
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:
        $ Options = [O]
    else:

        if JeanX not in Digits:
            if approval_check(JeanX, 500, "L") or approval_check(JeanX, 250, "I"):
                ch_j "Oh, here's my number, gimme a call some time."
                $ Digits.append(JeanX)
                return
            elif approval_check(JeanX, 250, "O"):
                ch_j "I guess you should have my number. . ."
                $ Digits.append(JeanX)
                return

        if "hungry" not in JeanX.Traits and (JeanX.event_counter["swallowed"] + JeanX.Chat[2]) >= 10 and JeanX.location == bg_current:
            call Jean_Hungry
            return

        if bg_current != "bg_restaurant" and bg_current != "HW Party" and (not Taboo or approval_check(JeanX, 800, "I")):
            if JeanX.location == bg_current and JeanX.Thirst >= 30 and "refused" not in JeanX.daily_history and "quicksex" not in JeanX.daily_history:
                $ JeanX.change_face("sly",1)
                ch_j "I could use some stress relief, you busy?"
                call Quick_Sex (JeanX)
                return




        if JeanX.Event[0] and "key" not in JeanX.Chat:
            $ Options.append("key")

        if "mandrill" in Player.Traits and "cologne chat" not in JeanX.daily_history:
            $ Options.append("mandrill")
        if "purple" in Player.Traits and "cologne chat" not in JeanX.daily_history:
            $ Options.append("purple")
        if "corruption" in Player.Traits and "cologne chat" not in JeanX.daily_history:
            $ Options.append("corruption")

        if JeanX.Date >= 1 and bg_current != "bg_restaurant":

            $ Options.append("dated")



        if JeanX.action_counter["kiss"] >= 5:

            $ Options.append("kissed")
        if "dangerroom" in Player.daily_history:

            $ Options.append("dangerroom")
        if "showered" in JeanX.daily_history:

            $ Options.append("showercaught")
        if "fondle_breasts" in JeanX.daily_history or "fondle_pussy" in JeanX.daily_history or "fondle_ass" in JeanX.daily_history:

            $ Options.append("fondled")
        if "Dazzler and Longshot" in JeanX.Inventory and "256 Shades of Grey" in JeanX.Inventory and "Avengers Tower Penthouse" in JeanX.Inventory:

            if "book" not in JeanX.Chat:
                $ Options.append("booked")
        if "lace_bra" in JeanX.Inventory or "lace_panties" in JeanX.Inventory:

            if "lingerie" not in JeanX.Chat:
                $ Options.append("lingerie")
        if JeanX.action_counter["handjob"]:

            $ Options.append("handy")
        if JeanX.event_counter["swallowed"]:

            $ Options.append("swallowed")
        if "cleaned" in JeanX.daily_history or "painted" in JeanX.daily_history:

            $ Options.append("facial")
        if JeanX.event_counter["sleepover"]:

            $ Options.append("sleep")
        if JeanX.event_counter["creampied"] or JeanX.event_counter["anal_creampied"]:

            $ Options.append("creampie")
        if JeanX.action_counter["sex"] or JeanX.action_counter["anal"]:

            $ Options.append("sexed")
        if JeanX.action_counter["anal"]:

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
        $ JeanX.change_face("sly",1)
        ch_j "(sniff, sniff). . . what is that? . ."
        $ JeanX.change_face("normal",0)
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
        if "caught chat" in JeanX.Chat:
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
                    $ JeanX.Traits.append("screen")
                "Nah, I want him to know.":
                    ch_j "Heh, you're naughty."
                    if approval_check(JeanX, 900, "OI"):
                        $ JeanX.change_face("sad")
                        ch_j "Ok, fine, we won't do that."
                        $ JeanX.change_face("bemused")
                        $ JeanX.Traits.append("noscreen")
                    else:
                        ch_j "Still, I don't like him sticking his nose in."
                        ch_j "I think I'll use the screen anyway."
                        $ JeanX.Traits.append("screen")
            $ JeanX.Chat.append("caught chat")
    elif Options[0] == "key":
        if JeanX.SEXP <= 15:
            ch_j "Don't use that key too freely. . ."
        else:
            ch_j "You have my key, but don't visit enough. . ."
        $ JeanX.Chat.append("key")









    elif Options[0] == "dated":

        ch_j "I had fun the other night, we should do that again some time."

    elif Options[0] == "kissed":

        $ JeanX.change_face("normal",1)
        ch_j "I have to say, you are a good kisser, [JeanX.player_petname]."
        menu:
            extend ""
            "Hey. . .I'm the best there is at what I do.":
                $ JeanX.change_face("smile",1)
                ch_j "I've heard that one before. . ."
            "No. You think?":
                ch_j "I wouldn't say it otherwise."

    elif Options[0] == "dangerroom":

        $ JeanX.change_face("sly",1)
        ch_j "Hey,[JeanX.player_petname]. I saw you in the Danger Room, earlier."
        ch_j "You're going surprisingly well for someone with your. . . limitations."

    elif Options[0] == "showercaught":

        if "shower" in JeanX.Chat:
            ch_j "I saw you in the showers again. . ."
        else:
            ch_j "So do you always just bust into the showers?"
            $ JeanX.Chat.append("shower")
            menu:
                extend ""
                "It was a total accident! I promise!":
                    $ JeanX.change_stat("love", 50, 5)
                    $ JeanX.change_stat("love", 90, 2)
                    if approval_check(JeanX, 1200):
                        $ JeanX.change_face("sly",1)
                        ch_j "Well, it's not like I minded."
                    $ JeanX.change_face("smile")
                    ch_j "I guess we can all make mistakes. . ."
                "Just with you.":
                    $ JeanX.change_stat("obedience", 40, 5)
                    if approval_check(JeanX, 1000) or approval_check(JeanX, 700, "L"):
                        $ JeanX.change_stat("love", 90, 3)
                        $ JeanX.change_face("sly",1)
                        ch_j "Oh, a charmer. . ."
                    else:
                        $ JeanX.change_stat("love", 70, -5)
                        $ JeanX.change_face("angry")
                        ch_j "I'll bet. . ."
                "Totally on purpose. I regret nothing.":
                    if approval_check(JeanX, 800):
                        $ JeanX.change_stat("obedience", 60, 5)
                        $ JeanX.change_stat("inhibition", 50, 5)
                        $ JeanX.change_face("perplexed",2)
                        ch_j "fair"
                        $ JeanX.blushing = 1
                    else:
                        $ JeanX.change_stat("love", 50, -10)
                        $ JeanX.change_stat("love", 80, -10)
                        $ JeanX.change_stat("obedience", 50, 10)
                        $ JeanX.change_face("angry")
                        ch_j "Perv."

    elif Options[0] == "fondled":

        if JeanX.action_counter["fondle_breasts"]+ JeanX.action_counter["fondle_pussy"] + JeanX.action_counter["fondle_ass"] >= 15:
            ch_j "Hey, give me a nice, hard, rubdown. . ."
        else:
            ch_j "Hey, gimme another massage. . . "
            ch_j ". . . the good kind. . ."

    elif Options[0] == "booked":

        ch_j "Hey, I read those books you gave me."
        menu:
            extend ""
            "Yeah? Did you like them?":
                $ JeanX.change_face("sly",2)
                ch_j "They were pretty hot."
            "Good. You looked like you could use to learn a thing or two from them.":
                $ JeanX.change_stat("obedience", 70, 5)
                $ JeanX.change_stat("inhibition", 50, 5)
                $ JeanX.change_face("angry")
                ch_j "Yeah right."
        $ JeanX.blushing = 1
        $ JeanX.Chat.append("book")

    elif Options[0] == "lingerie":

        $ JeanX.change_face("sly",2)
        ch_j "I really enjoy those silky underthings you got me. . ."
        $ JeanX.blushing = 1
        $ JeanX.Chat.append("lingerie")

    elif Options[0] == "handy":

        $ JeanX.change_face("sly",1)
        ch_j "I was thinking about your cock in my hand. . ."
        ch_j "I think we should do that again some time. . ."
        $ JeanX.blushing = 0

    elif Options[0] == "blowjob":
        if "blowjob" not in JeanX.Chat:

            $ JeanX.change_face("sly",2)
            ch_j "Hey, so did you enjoy that blowjob?"
            menu:
                extend ""
                "You were totally amazing.":
                    $ JeanX.change_stat("love", 90, 5)
                    $ JeanX.change_stat("obedience", 60, 15)
                    $ JeanX.change_stat("inhibition", 60, 10)
                    $ JeanX.change_face("normal",1)
                    ch_j "You know it."
                    $ JeanX.change_face("sexy",1)
                    ch_j "I wouldn't mind having another taste. . ."
                "Honestly? It was good. . .but you could use a little practice, I think.":
                    if approval_check(JeanX, 300, "I") or not approval_check(JeanX, 800):
                        $ JeanX.change_stat("love", 90, -5)
                        $ JeanX.change_stat("obedience", 60, 10)
                        $ JeanX.change_stat("inhibition", 50, 10)
                        $ JeanX.change_face("perplexed",1)
                        ch_j "Really? I'd never gotten any complaints before. . ."
                    else:
                        $ JeanX.change_stat("obedience", 70, 15)
                        $ JeanX.change_stat("inhibition", 50, 5)
                        $ JeanX.change_face("sexy",1)
                        ch_j "You just don't know quality when you feel it."
                "I guess. If you're into weird sounds and too much teeth. Spoiler, I'm not.":
                    $ JeanX.change_stat("love", 90, -10)
                    $ JeanX.change_stat("obedience", 60, -5)
                    $ JeanX.change_face("angry",2)
                    ch_j "You just don't know quality."
            $ JeanX.blushing = 1
            $ JeanX.Chat.append("blowjob")
        else:
            $ Line = renpy.random.choice(["I gotta tell you, your dick tastes great.", 
                            "I think I nearly dislocated my jaw last time.", 
                            "Let me know if you'd like another blowjob sometime.",
                            "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
            ch_j "[Line]"

    elif Options[0] == "swallowed":

        if "swallow" in JeanX.Chat:
            ch_j "Hey, I wouldn't mind another taste. . ."
        else:
            ch_j "Hey. . . the other day. . ."
            ch_j "Your jiz tasted really good."
            ch_j "Like -really- good."
            $ JeanX.change_face("sly",1)
            ch_j "Weird."
            $ JeanX.Chat.append("swallow")

    elif Options[0] == "facial":

        ch_j "Ok, so. . ."
        ch_j "You know how you came on my face?"
        $ JeanX.change_face("sexy",2)
        ch_j "That just felt -so- good for some reason. . ."
        $ JeanX.blushing = 1

    elif Options[0] == "sleepover":

        ch_j "I really enjoyed the other night."
        ch_j "I really enjoyed the company."

    elif Options[0] == "creampie":

        "[JeanX.name] draws close to you so she can whisper into your ear."
        ch_j "I still ave some of you spilling out of me. . ."

    elif Options[0] == "sexed":

        ch_j "So. . . you should know. . ."
        $ JeanX.change_face("sexy",2)
        ch_j ". . .lately when I've been schlicking. . ."
        ch_j "I've been thinking about you inside of me."
        $ JeanX.blushing = 1

    elif Options[0] == "anal":

        $ JeanX.change_face("sly")
        ch_j "I'm not much of a fan of anal."
        $ JeanX.change_face("sexy",1)
        ch_j "Still, with you it's pretty fun."

    elif Options[0] == "seenpeen":
        $ JeanX.change_face("sly",1, Eyes="down")
        ch_j "Oh, I forgot to mention, congrats on that package you're swinging. . ."
        $ JeanX.change_face("bemused",1)
        $ JeanX.change_stat("love", 50, 5)
        $ JeanX.change_stat("love", 60, 10)
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
        $ Line = renpy.random.choice(["Get away from me.", 
                "I don't want to smell you near me.", 
                "Back off.",
                "Buzz off."])
        ch_j "[Line]"
    else:

        ch_j "Oh, did you have something interesting to say?"

        $ D20 = renpy.random.randint(1, 20)
        if D20 == 1:
            $ JeanX.change_face("normal")
            ch_j "Hey, pass me your physics notes."
            $ JeanX.change_face("angry",Eyes="down")
            ch_j ". . ."
            $ JeanX.change_face("angry")
            ch_j "These notes are trash. Do better."
        elif D20 == 2:
            $ JeanX.change_face("angry")
            ch_j "Where'd Lance go? I haven't seen him around in a while."
        elif D20 == 3:
            $ JeanX.change_face("normal",Eyes="side")
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
            $ JeanX.change_face("angry",Eyes="side")
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

    $ Line = 0
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
                            ch_j "I'm not your -pet,- [JeanX.player_petname]."
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
    $ JeanX.AddWord(1,0,"namechange")
    return




label Jean_Personality(counter=0):
    if not JeanX.Chat[4] or counter:
        "Since you're doing well in one area, you can convince Jean to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_j "Yeah?"
        "More Obedient. [[Love to Obedience]" if JeanX.love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_j "Oh, fine, I'll try. . ."
            $ JeanX.Chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if JeanX.love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_j "Oh, you like it kinky then? . ."
            $ JeanX.Chat[4] = 2

        "Less Inhibited. [[Obedience to Inhibition]" if JeanX.obedience > 900:
            ch_p "I want you to be less inhibited."
            ch_j "I'll give it a try. . ."
            $ JeanX.Chat[4] = 3
        "More Loving. [[Obedience to Love]" if JeanX.obedience > 900:
            ch_p "I'd like you to learn to love me."
            ch_j "Well. . . ok. . ."
            $ JeanX.Chat[4] = 4

        "More Obedient. [[Inhibition to Obedience]" if (JeanX.inhibition - JeanX.IX) > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_j "Hmm. . . kinky. . ."
            $ JeanX.Chat[4] = 5

        "More Loving. [[Inhibition to Love]" if (JeanX.inhibition - JeanX.IX) > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_j "Oh, fine. . ."
            $ JeanX.Chat[4] = 6

        "I guess just do what you like. . .[[reset]" if JeanX.Chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_j "Um, sure. . ."
            $ JeanX.Chat[4] = 0
        "Repeat the rules":
            call Jean_Personality (1)
            return
        "Nevermind.":
            return
    return







label Jean_Summon(approval_bonus=approval_bonus):
    $ JeanX.change_outfit()
    if "no_summon" in JeanX.recent_history:
        if "angry" in JeanX.recent_history:
            ch_j "Go away!"
        elif JeanX.recent_history.count("no_summon") > 1:
            ch_j "Give me some space!"
            $ JeanX.recent_history.append("angry")
        else:


            ch_j "I told you I'm busy!"
        $ JeanX.recent_history.append("no_summon")
        return

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    if JeanX.location == "bg_classroom":
        $ approval_bonus = -10
    elif JeanX.location == "bg_jean":
        $ approval_bonus = -10
    elif JeanX.location == "bg_showerroom":
        $ approval_bonus = -30

    if D20 <= 3:

        $ Line = "no"
    if time_index >= 3:
        if approval_check(JeanX, 500, "L") or approval_check(JeanX, 400, "O"):

            ch_j "You're up too? Yeah, that's fine."
            $ JeanX.location = bg_current
            call set_the_scene
        else:

            ch_j "I'd rather not. . ."
            $ JeanX.recent_history.append("no_summon")
        return
    elif "les" in JeanX.recent_history:

        if approval_check(JeanX, 2000):
            ch_j "I'm getting off with one of the girls. Wanna come over?"
            menu:
                extend ""
                "Sure":
                    $ Line = "go to"
                "No thanks.":
                    ch_j "Heh, ok. . ."
                    return
        else:
            ch_j "I'm a little. . . tied up at the moment."
            ch_j "We can talk later."
            $ JeanX.recent_history.append("no_summon")
            return
    elif not approval_check(JeanX, 700, "L") or not approval_check(JeanX, 600, "O"):

        if not approval_check(JeanX, 300):
            ch_j "I'm busy, [JeanX.player_petname]."
            $ JeanX.recent_history.append("no_summon")
            return


        if "summoned" in JeanX.recent_history:
            pass
        elif "goto" in JeanX.recent_history:
            ch_j "You just left. . ."
        elif JeanX.location == "bg_classroom":
            ch_j "I'm in class right now."
        elif JeanX.location == "bg_dangerroom":
            ch_j "I'm in the Danger Room, [JeanX.player_petname]."
        elif JeanX.location == "bg_campus":
            ch_j "I'm relaxing in the quad right now."
        elif JeanX.location == "bg_jean":
            ch_j "I'm in my room, [JeanX.player_petname]."
        elif JeanX.location == "bg_player":
            ch_j "I'm in your room, [JeanX.player_petname], where are you?"
        elif JeanX.location == "bg_showerroom":
            if approval_check(JeanX, 1600):
                ch_j "I'm in the shower right now."
            else:
                ch_j "I'm in the shower right now, [JeanX.player_petname]."
                ch_j "Don't come knocking."
                $ JeanX.recent_history.append("no_summon")
                return
        elif JeanX.location == "hold":
            ch_j "I'm busy at the moment."
            $ JeanX.recent_history.append("no_summon")
            return
        else:
            ch_j "Why don't you come to me?"


        if "summoned" in JeanX.recent_history:
            ch_j "Again? Ok, fine."
            $ Line = "yes"
        elif "goto" in JeanX.recent_history:
            menu:
                extend ""
                "You're right, be right back.":
                    ch_j "Ok then."
                    $ Line = "go to"
                "Nah, it's better here.":
                    ch_j "Ok then."
                "But I'd {i}really{/i} like to see you over here.":
                    if approval_check(JeanX, 600, "L") or approval_check(JeanX, 1400):
                        $ Line = "lonely"
                    else:
                        $ Line = "no"
                "I said come over here.":
                    if approval_check(JeanX, 600, "O"):

                        $ Line = "command"
                    elif D20 >= 7 and approval_check(JeanX, 1400):

                        ch_j "Well. . ."
                        $ Line = "yes"
                    elif approval_check(JeanX, 200, "O"):

                        ch_j "Whatever."
                    else:

                        $ Line = "no"
        else:
            menu:
                extend ""
                "Ok, I'll be right there.":
                    $ JeanX.change_stat("love", 55, 1)
                    $ JeanX.change_stat("inhibition", 30, 1)
                    ch_j "Good."
                    $ Line = "go to"
                "Ok, we can talk later then.":

                    $ JeanX.change_stat("obedience", 50, 1)
                    $ JeanX.change_stat("obedience", 30, 2)
                    ch_j "Ok."
                "Could you please come visit me? I'm lonely.":

                    if approval_check(JeanX, 650, "L") or approval_check(JeanX, 1500):
                        $ JeanX.change_stat("love", 70, 1)
                        $ JeanX.change_stat("obedience", 50, 1)
                        $ Line = "lonely"
                    else:
                        $ JeanX.change_stat("inhibition", 30, 1)
                        $ Line = "no"
                        ch_j "Needy much?"
                "Come on, it'll be fun.":

                    if approval_check(JeanX, 400, "L") and approval_check(JeanX, 800):
                        $ JeanX.change_stat("love", 70, 1)
                        $ JeanX.change_stat("obedience", 50, 1)
                        $ Line = "fun"
                    else:
                        $ JeanX.change_stat("inhibition", 30, 1)
                        $ Line = "no"
                "I said come over here.":

                    if approval_check(JeanX, 600, "O"):

                        $ JeanX.change_stat("love", 50, 1, 1)
                        $ JeanX.change_stat("love", 40, -1)
                        $ JeanX.change_stat("obedience", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and approval_check(JeanX, 1500):

                        $ JeanX.change_stat("love", 70, -2)
                        $ JeanX.change_stat("love", 90, -1)
                        $ JeanX.change_stat("obedience", 50, 2)
                        $ JeanX.change_stat("obedience", 90, 1)
                        ch_j "Ok, fine."
                        $ Line = "yes"

                    elif approval_check(JeanX, 200, "O"):

                        $ JeanX.change_stat("love", 60, -4)
                        $ JeanX.change_stat("love", 90, -3)
                        ch_j "And I said \"no.\""
                        $ JeanX.change_stat("inhibition", 40, 2)
                        $ JeanX.change_stat("inhibition", 60, 1)
                        $ JeanX.change_stat("obedience", 70, -3)
                        ch_j "I'm staying here."
                    else:

                        $ JeanX.change_stat("inhibition", 30, 1)
                        $ JeanX.change_stat("inhibition", 50, 1)
                        $ JeanX.change_stat("love", 50, -1, 1)
                        $ JeanX.change_stat("obedience", 70, -1)
                        $ Line = "no"
    else:


        if JeanX.love > JeanX.obedience:
            ch_j "Ok, fine."
        else:
            ch_j "Ok, if you insist. . ."
        $ Line = "yes"

    $ approval_bonus = 0

    if not Line:

        $ JeanX.recent_history.append("no_summon")
        return

    if Line == "no":

        ch_j "Sorry, [JeanX.player_petname], I'm kinda busy."
        $ JeanX.recent_history.append("no_summon")
        return

    elif Line == "go to":

        $ renpy.pop_call()
        $ JeanX.recent_history.append("goto")
        $ Player.recent_history.append("goto")
        $ Line = 0
        if JeanX.location == "bg_classroom":
            ch_j "Ok then."
            jump Class_Room
        elif JeanX.location == "bg_dangerroom":
            ch_j "I'll try not to finish the exercise myself."
            jump Danger_Room
        elif JeanX.location == "bg_jean":
            ch_j "Don't keep me waiting."
            jump Jean_Room
        elif JeanX.location == "bg_player":
            ch_j "Don't keep me waiting."
            jump Player_Room
        elif JeanX.location == "bg_showerroom":
            ch_j "I'll see you then."
            jump Shower_Room
        elif JeanX.location == "bg_campus":
            ch_j "Ok."
            jump Campus
        elif JeanX.location in PersonalRooms:
            ch_j "Yeah, see you."
            $ bg_current = JeanX.location
            jump Misplaced
        else:
            ch_j "Um, I'll just meet you in my room."
            $ JeanX.location = "bg_jean"
            jump Jean_Room


    elif Line == "lonely":
        ch_j "Oh. . . fine. . ."
    elif Line == "command":
        ch_j "Fine, [JeanX.player_petname]."

    $ JeanX.recent_history.append("summoned")
    $ Line = 0
    if "locked" in Player.Traits:
        call Locked_Door (JeanX)
        return
    $ JeanX.location = bg_current
    call Taboo_Level (0)
    $ JeanX.change_outfit()
    call set_the_scene
    return




label Jean_Leave(approval_bonus=approval_bonus, GirlsNum=0):
    if "leaving" in JeanX.recent_history:
        $ JeanX.DrainWord("leaving")
    else:
        return

    if JeanX.location == "hold":

        ch_j "Ok, I've got work to do, apparently."
        return

    if JeanX in Party or "lockedtravels" in JeanX.Traits:


        $ JeanX.location = bg_current
        return

    elif "freetravels" in JeanX.Traits or not approval_check(JeanX, 700):

        $ JeanX.change_outfit()
        if GirlsNum:
            ch_j "I'm leaving too."

        if JeanX.location == "bg_classroom":
            ch_j "I've got class."
        elif JeanX.location == "bg_dangerroom":
            ch_j "I'm getting some exercise."
        elif JeanX.location == "bg_campus":
            ch_j "I'm taking a break in the quad."
        elif JeanX.location == "bg_laura":
            ch_j "I'm going back to my room."
        elif JeanX.location == "bg_player":
            ch_j "I'm hanging out in your room for a bit."
        elif JeanX.location == "bg_pool":
            ch_j "I going to hit the pool."
        elif JeanX.location == "bg_showerroom":
            if approval_check(JeanX, 1400):
                ch_j "I'm hitting the showers."
            else:
                ch_j "I'm headed out."
        else:
            ch_j "I'm headed out."
        hide Jean_Sprite
        return


    if bg_current == "bg_dangerroom":
        call Gym_Exit ([JeanX])

    $ JeanX.change_outfit()

    if "follow" not in JeanX.Traits:

        $ JeanX.Traits.append("follow")

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0

    if JeanX.location == "bg_classroom":
        $ approval_bonus = 10
    elif JeanX.location == "bg_showerroom":
        $ approval_bonus = 40


    if GirlsNum:
        ch_j "Yeah, I'm headed out too."

    if JeanX.location == "bg_classroom":
        ch_j "I've got class."
    elif JeanX.location == "bg_dangerroom":
        ch_j "I've got some Danger Room time scheduled."
    elif JeanX.location == "bg_campus":
        ch_j "I'm hanging out on the quad."
    elif JeanX.location == "bg_jean":
        ch_j "I'm headed back to my room."
    elif JeanX.location == "bg_player":
        ch_j "I'm going to hang out in your room for a bit."
    elif JeanX.location == "bg_showerroom":
        if approval_check(JeanX, 1600):
            ch_j "I'm hitting the showers."
        else:
            ch_j "I'm hitting the showers, maybe hang back for a bit."
            return
    elif JeanX.location == "bg_pool":
        ch_j "I was hitting the pool."
    else:
        ch_j "Are you coming with?"


    menu:
        extend ""
        "Ok, I'll catch up.":
            if "followed" not in JeanX.recent_history:
                $ JeanX.change_stat("love", 55, 1)
                $ JeanX.change_stat("inhibition", 30, 1)
            $ Line = "go to"
        "Ok, we can talk later.":

            if "followed" not in JeanX.recent_history:
                $ JeanX.change_stat("obedience", 50, 1)
                $ JeanX.change_stat("obedience", 30, 2)
            ch_j "Fine, whatever."
        "Could you please stay with me? I'll get lonely.":

            if approval_check(JeanX, 650, "L") or approval_check(JeanX, 1500):
                if "followed" not in JeanX.recent_history:
                    $ JeanX.change_stat("love", 70, 1)
                    $ JeanX.change_stat("obedience", 50, 1)
                $ Line = "lonely"
            else:
                if "followed" not in JeanX.recent_history:
                    $ JeanX.change_stat("inhibition", 30, 1)
                $ Line = "no"
                ch_j "Needy much?"
        "Come on, it'll be fun.":

            if approval_check(JeanX, 400, "L") and approval_check(JeanX, 800):
                $ JeanX.change_stat("love", 70, 1)
                $ JeanX.change_stat("obedience", 50, 1)
                $ Line = "fun"
            else:
                $ JeanX.change_stat("inhibition", 30, 1)
                $ Line = "no"
        "No, stay here.":

            if approval_check(JeanX, 600, "O"):

                if "followed" not in JeanX.recent_history:
                    $ JeanX.change_stat("love", 40, -2)
                    $ JeanX.change_stat("obedience", 90, 1)
                $ Line = "command"

            elif D20 >= 7 and approval_check(JeanX, 1400):

                if "followed" not in JeanX.recent_history:
                    $ JeanX.change_stat("love", 70, -2)
                    $ JeanX.change_stat("love", 90, -1)
                    $ JeanX.change_stat("obedience", 50, 2)
                    $ JeanX.change_stat("obedience", 90, 1)
                ch_j ". . . Fine."
                $ Line = "yes"

            elif approval_check(JeanX, 200, "O"):

                if "followed" not in JeanX.recent_history:
                    $ JeanX.change_stat("love", 70, -4)
                    $ JeanX.change_stat("love", 90, -2)
                ch_j "You're not the boss of me."
                if "followed" not in JeanX.recent_history:
                    $ JeanX.change_stat("inhibition", 40, 2)
                    $ JeanX.change_stat("inhibition", 60, 1)
                    $ JeanX.change_stat("obedience", 70, -2)
                ch_j "Ha!"
            else:

                if "followed" not in JeanX.recent_history:
                    $ JeanX.change_stat("inhibition", 30, 1)
                    $ JeanX.change_stat("inhibition", 50, 1)
                    $ JeanX.change_stat("love", 50, -1, 1)
                    $ JeanX.change_stat("love", 90, -2)
                    $ JeanX.change_stat("obedience", 70, -1)
                $ Line = "no"


    call Taboo_Level (0)
    $ JeanX.recent_history.append("followed")
    if not Line:

        hide Jean_Sprite
        call Gym_Clothes_Off ([JeanX])
        return

    if Line == "no":

        ch_j "I'd rather not."
        hide Jean_Sprite
        call Gym_Clothes_Off ([JeanX])
        return

    elif Line == "go to":


        $ approval_bonus = 0
        $ Line = 0
        call DrainAll ("leaving")
        call DrainAll ("arriving")
        $ JeanX.recent_history.append("goto")
        $ Player.recent_history.append("goto")
        hide Jean_Sprite
        call Gym_Clothes_Off ([JeanX])
        if JeanX.location == "bg_classroom":
            ch_j "Ok."
            jump Class_Room_Entry
        elif JeanX.location == "bg_dangerroom":
            ch_j "I'll get warmed up."
            jump Danger_Room_Entry
        elif JeanX.location == "bg_jean":
            ch_j "Ok."
            jump Jean_Room
        elif JeanX.location == "bg_player":
            ch_j "Good."
            jump Player_Room
        elif JeanX.location == "bg_showerroom":
            ch_j "Ok, nice."
            jump Shower_Room_Entry
        elif JeanX.location == "bg_campus":
            ch_j "Ok."
            jump Campus_Entry
        elif JeanX.location == "bg_pool":
            ch_j "Cool."
            jump Pool_Entry
        else:
            ch_j "I'll just meet you in your room."
            $ JeanX.location = "bg_player"
            jump Player_Room



    elif Line == "lonely":
        ch_j "Well, I guess. . ."
    elif Line == "command":
        ch_j "Fine, [JeanX.player_petname]. . ."

    $ Line = 0
    ch_j "I'll stick around."
    $ JeanX.location = bg_current
    return





label Jean_Clothes:
    if JeanX.Taboo:
        if "exhibitionist" in JeanX.Traits:
            ch_j "Yeah? . ."
        elif approval_check(JeanX, 900, TabM=4) or approval_check(JeanX, 400, "I", TabM=3):
            ch_j "Oh, I guess we could. . ."
        else:
            ch_j "I think this is kind of exposed. . ."
            ch_j "Can we talk about this in our rooms?"
            return
    elif approval_check(JeanX, 900, TabM=4) or approval_check(JeanX, 600, "L") or approval_check(JeanX, 300, "O"):
        ch_j "Oh? What about them?"
    else:
        ch_j "Just enjoy, don't advise."
        return

    if Girl != JeanX or Line == "Giftstore":

        $ renpy.pop_call()
    $ Line = 0
    $ Girl = JeanX
    call shift_focus (Girl)

label Jean_Wardrobe_Menu:
    $ JeanX.change_face()
    $ primary_action = 1
    while True:
        menu:
            ch_j "What about my clothes?"
            "Overshirts":
                call Jean_Clothes_Over
            "Legwear":
                call Jean_Clothes_Legs
            "Underwear":
                call Jean_Clothes_Under
            "Accessories":
                call Jean_Clothes_Misc
            "Outfit Management":
                call Jean_Clothes_Outfits
            "Let's talk about what you wear around.":
                call Clothes_Schedule (JeanX)

            "Could I get a look at it?" if JeanX.location != bg_current:

                call OutfitShame (JeanX, 0, 2)
                if _return:
                    show PhoneSex zorder 150
                    ch_j "Nice, right?"
                hide PhoneSex
            "Could I get a look at it?" if renpy.showing('DressScreen'):

                call OutfitShame (JeanX, 0, 2)
                if _return:
                    hide DressScreen
            "Would you be more comfortable behind a screen? (locked)" if JeanX.Taboo:
                pass
            "Would you be more comfortable behind a screen?" if JeanX.location == bg_current and not JeanX.Taboo and not renpy.showing('DressScreen'):

                if approval_check(JeanX, 1500) or (JeanX.SeenChest and JeanX.SeenPussy):
                    ch_j "I don't see why."
                else:
                    show DressScreen zorder 150
                    ch_j "Yeah, this'll work."

            "Gift for you (locked)" if Girl.location != bg_current:
                pass
            "Gift for you" if Girl.location == bg_current:
                ch_p "I'd like to give you something."
                call Gifts
            "Switch to. . .":

                if renpy.showing('DressScreen'):
                    call OutfitShame (JeanX, 0, 2)
                    if _return:
                        hide DressScreen
                    else:
                        $ JeanX.change_outfit()
                $ JeanX.Set_Temp_Outfit()
                $ primary_action = 0
                call Switch_Chat
                if Girl != JeanX:
                    ch_p "I wanted to talk about your clothes."
                    call expression Girl.Tag +"_Clothes"
                $ Girl = JeanX
                call shift_focus (Girl)
            "Never mind, you look good like that.":

                if "wardrobe" not in JeanX.recent_history:

                    if JeanX.Chat[1] <= 1:
                        $ JeanX.change_stat("love", 70, 15)
                        $ JeanX.change_stat("obedience", 40, 20)
                        ch_j "Of course?"
                    elif JeanX.Chat[1] <= 10:
                        $ JeanX.change_stat("love", 70, 5)
                        $ JeanX.change_stat("obedience", 40, 7)
                        ch_j "Right?"
                    elif JeanX.Chat[1] <= 50:
                        $ JeanX.change_stat("love", 70, 1)
                        $ JeanX.change_stat("obedience", 40, 1)
                        ch_j "Uh-huh."
                    else:
                        ch_j "Sure."
                    $ JeanX.recent_history.append("wardrobe")
                if renpy.showing('DressScreen'):
                    call OutfitShame (JeanX, 0, 2)
                    if _return:
                        hide DressScreen
                    else:
                        $ JeanX.change_outfit()
                $ JeanX.Set_Temp_Outfit()
                $ JeanX.Chat[1] += 1
                $ primary_action = 0
                return







    menu Jean_Clothes_Outfits:
        "You should remember that one. [[Set Custom]":

            menu:
                "Which slot would you like this saved in?"
                "Custom 1":
                    call OutfitShame (JeanX, 3, 1)
                "Custom 2":
                    call OutfitShame (JeanX, 5, 1)
                "Custom 3":
                    call OutfitShame (JeanX, 6, 1)
                "Gym Clothes":
                    call OutfitShame (JeanX, 4, 1)
                "Sleepwear":
                    call OutfitShame (JeanX, 7, 1)
                "Swimwear":
                    call OutfitShame (JeanX, 10, 1)
                "Never mind":

                    pass
        "Pink shirt and pants outfit":

            $ JeanX.change_outfit("casual1")
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ JeanX.Outfit = "casual1"
                    $ JeanX.Shame = 0
                    ch_j "Yeah, I've worn this one a long time."
                "Let's try something else though.":
                    ch_j "Sure. . ."
        "Green t-shirt and skirt outfit":

            $ JeanX.change_outfit("casual2")
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ JeanX.Outfit = "casual2"
                    $ JeanX.Shame = 0
                    ch_j "Ok, this one has a real \"classic\" feel. . ."
                "Let's try something else though.":
                    ch_j "Sure. . ."

        "Remember that outfit we put together? [[Set a custom outfit] (locked)" if not JeanX.Custom1[0] and not JeanX.Custom2[0] and not JeanX.Custom3[0]:
            pass

        "Remember that outfit we put together?" if JeanX.Custom1[0] or JeanX.Custom2[0] or JeanX.Custom3[0]:
            $ counter = 0
            while 1:
                menu:
                    "Throw on Custom 1 (locked)" if not JeanX.Custom1[0]:
                        pass
                    "Throw on Custom 1" if JeanX.Custom1[0]:
                        $ JeanX.change_outfit("custom1")
                        $ counter = 3
                    "Throw on Custom 2 (locked)" if not JeanX.Custom2[0]:
                        pass
                    "Throw on Custom 2" if JeanX.Custom2[0]:
                        $ JeanX.change_outfit("custom2")
                        $ counter = 5
                    "Throw on Custom 3 (locked)" if not JeanX.Custom3[0]:
                        pass
                    "Throw on Custom 3" if JeanX.Custom3[0]:
                        $ JeanX.change_outfit("custom3")
                        $ counter = 6

                    "You should wear this one in private. (locked)" if not counter:
                        pass
                    "You should wear this one in private." if counter:
                        if counter == 5:
                            $ JeanX.Clothing[9] = "custom2"
                        elif counter == 6:
                            $ JeanX.Clothing[9] = "custom3"
                        else:
                            $ JeanX.Clothing[9] = "custom1"
                        ch_j "Ok, sure."
                    "On second thought, forget about that one outfit. . .":

                        menu:
                            "Custom 1 [[clear custom 1]" if JeanX.Custom1[0]:
                                ch_j "Ok."
                                $ JeanX.Custom1[0] = 0
                            "Custom 1 [[clear custom 1] (locked)" if not JeanX.Custom1[0]:
                                pass
                            "Custom 2 [[clear custom 2]" if JeanX.Custom2[0]:
                                ch_j "Ok."
                                $ JeanX.Custom2[0] = 0
                            "Custom 2 [[clear custom 2] (locked)" if not JeanX.Custom2[0]:
                                pass
                            "Custom 3 [[clear custom 3]" if JeanX.Custom3[0]:
                                ch_j "Ok."
                                $ JeanX.Custom3[0] = 0
                            "Custom 3 [[clear custom 3] (locked)" if not JeanX.Custom3[0]:
                                pass
                            "Never mind, [[back].":
                                pass

                    "You should wear this one out. [[choose outfit first](locked)" if not counter:
                        pass
                    "You should wear this one out." if counter:
                        call Custom_Out (JeanX, counter)
                    "Ok, back to what we were talking about. . .":
                        $ counter = 0
                        return

        "Gym Clothes?" if not JeanX.Taboo or bg_current == "bg_dangerroom":
            $ JeanX.change_outfit("gym")

        "Sleepwear?" if not JeanX.Taboo:
            if approval_check(JeanX, 1200):
                $ JeanX.change_outfit("sleep")
            else:
                call Display_DressScreen (JeanX)
                if _return:
                    $ JeanX.change_outfit("sleep")

        "Swimwear? (locked)" if (JeanX.Taboo and bg_current != "bg_pool") or not JeanX.Swim[0]:
            $ JeanX.change_outfit("swimwear")
        "Swimwear?" if (not JeanX.Taboo or bg_current == "bg_pool") and JeanX.Swim[0]:
            $ JeanX.change_outfit("swimwear")

        "Halloween Costume?" if "halloween" in JeanX.history:
            ch_j "Ok."
            $ JeanX.change_outfit("costume")
        "Your birthday suit looks really great. . .":


            $ JeanX.change_face("sexy", 1)
            $ Line = 0
            if not JeanX.bra and not JeanX.underwear and not JeanX.top and not JeanX.legs and not JeanX.hose:
                ch_j "Duh."
            elif JeanX.SeenChest and JeanX.SeenPussy and approval_check(JeanX, 1200, TabM=4):
                ch_j "You know it. . ."
                $ Line = 1
            elif approval_check(JeanX, 2000, TabM=4):
                ch_j "Oh, going right for it, huh?"
                $ Line = 1
            elif JeanX.SeenChest and JeanX.SeenPussy and approval_check(JeanX, 1200, TabM=0):
                ch_j "You know it, but maybe not right here. . ."
            elif approval_check(JeanX, 2000, TabM=0):
                ch_j "Maybe, but not here. . ."
            elif approval_check(JeanX, 1000, TabM=0):
                $ JeanX.change_face("confused", 1,Mouth="smirk")
                ch_j "Yeah, but I'm not sharing."
                $ JeanX.change_face("bemused", 0)
            else:
                $ JeanX.change_face("angry", 1)
                ch_j "Of course it is."
                ch_j "Oh, you wanted to see it?"

            if Line:

                $ JeanX.change_outfit("nude")
                "She throws her clothes off at her feet."
                call Jean_First_Topless
                call Jean_First_Bottomless (1)
                $ JeanX.change_face("sexy")
                menu:
                    "You know, you should wear this one out. [[set current outfit]":
                        if "exhibitionist" in JeanX.Traits:
                            ch_j "mmmm. . ."
                            $ JeanX.Outfit = "nude"
                            $ JeanX.change_stat("lust", 50, 10)
                            $ JeanX.change_stat("lust", 70, 5)
                            $ JeanX.Shame = 50
                        elif "nowhammy" not in JeanX.Traits or approval_check(JeanX, 800, "I") or approval_check(JeanX, 2800, TabM=0):
                            ch_j "Sure, ok. . ."
                            $ JeanX.Outfit = "nude"
                            $ JeanX.Shame = 50
                        else:
                            $ JeanX.change_face("sexy", 1)
                            $ JeanX.eyes = "surprised"
                            ch_j "Yeah, um, I'm not into that right now. . ."
                    "Let's try something else though.":

                        if "exhibitionist" in JeanX.Traits:
                            ch_j "Oh, ok. . ."
                        elif "nowhammy" not in JeanX.Traits or approval_check(JeanX, 800, "I") or approval_check(JeanX, 2800, TabM=0):
                            $ JeanX.change_face("bemused", 1)
                            ch_j "I thought you might want me to go out like this. . ."
                            ch_j ". . ."
                        else:
                            $ JeanX.change_face("confused", 1)
                            ch_j "Yeah, I'm not into that right now. . ."
            $ Line = 0
        "Never mind":

            return

    return




    menu Jean_Clothes_Over:

        "Why don't you go with no [JeanX.top]?" if JeanX.top:
            $ JeanX.change_face("bemused", 1)
            if approval_check(JeanX, 800, TabM=3) and (JeanX.bra or JeanX.SeenChest):
                ch_j "Ok."
            elif approval_check(JeanX, 600, TabM=0):
                call Jean_NoBra
                if not _return:
                    if not approval_check(JeanX, 1200):
                        call Display_DressScreen (JeanX)
                        if not _return:
                            return
                    else:
                        return
            else:
                call Display_DressScreen (JeanX)
                if not _return:
                    ch_j "Not right now."
                    if not JeanX.bra:
                        ch_j "I'm not wearing a bra right now."
                    return
            $ Line = JeanX.top
            $ JeanX.top = 0
            "She throws her [Line] at her feet."
            if not JeanX.bra and not renpy.showing('DressScreen'):
                call Jean_First_Topless

        "Try on that pink shirt." if JeanX.top != "pink_shirt":
            $ JeanX.change_face("bemused")
            ch_j "Sure."
            $ JeanX.top = "pink_shirt"

        "Try on that green shirt." if JeanX.top != "green_shirt":
            $ JeanX.change_face("bemused")
            ch_j "Sure."
            $ JeanX.top = "green_shirt"

        "Try on that yellow tanktop." if JeanX.top != "yellow_shirt" and "halloween" in JeanX.history:
            $ JeanX.change_face("bemused")
            ch_j "Sure."
            $ JeanX.top = "yellow_shirt"

        "Maybe just throw on a towel?" if JeanX.top != "towel":
            $ JeanX.change_face("bemused", 1)
            if JeanX.bra or JeanX.SeenChest:
                ch_j "Um, ok. . ."
            elif approval_check(JeanX, 1000, TabM=0):
                $ JeanX.change_face("perplexed", 1)
                ch_j "Huh, ok . ."
            else:
                call Display_DressScreen (JeanX)
                if not _return:
                    ch_j "That wouldn't look right."
                    return
            $ JeanX.top = "towel"
        "Never mind":

            pass
    return




    label Jean_NoBra:
        menu:
            ch_j "I'm not wearing a bra right now."
            "Then you could slip something on under it. . .":
                if approval_check(JeanX, 1200, TabM=4) or (JeanX.SeenChest and approval_check(JeanX, 1000, TabM=3)):
                    $ JeanX.blushing = 1
                    ch_j "Well, it's not like I needed one. . ."
                    $ JeanX.blushing = 0
                elif approval_check(JeanX, 900, TabM=2) and "lace_bra" in JeanX.Inventory:
                    ch_j "I guess I could find something."
                    $ JeanX.bra  = "lace_bra"
                    "She pulls out her lace bra and slips it under her [JeanX.top]."
                elif approval_check(JeanX, 700, TabM=2):
                    ch_j "I guess I could find something."
                    $ JeanX.bra  = "green_bra"
                    "She pulls out her green bra and slips it under her [JeanX.top]."
                else:
                    ch_j "Yeah, I don't think so."
                    return 0
            "You could always just wear nothing at all. . .":

                if approval_check(JeanX, 1100, "LI", TabM=2) and JeanX.love > JeanX.inhibition:
                    ch_j "I guess. . ."
                elif approval_check(JeanX, 700, "OI", TabM=2) and JeanX.obedience > JeanX.inhibition:
                    ch_j "Sure. . ."
                elif approval_check(JeanX, 600, "I", TabM=2):
                    ch_j "Yeah. . ."
                elif approval_check(JeanX, 1300, TabM=2):
                    ch_j "Okay, fine."
                else:
                    $ JeanX.change_face("surprised")
                    $ JeanX.brows = "angry"
                    if JeanX.Taboo > 20:
                        ch_j ". . . not right now. . ."
                    else:
                        ch_j "Ha! Not for you, [JeanX.player_petname]."
                    return 0
            "Never mind.":
                ch_j "Ok. . ."
                return 0
        return 1




    menu Jean_Clothes_Legs:

        "Maybe go without the [JeanX.legs]." if JeanX.legs:
            $ JeanX.change_face("sexy", 1)
            if JeanX.SeenPanties and JeanX.underwear and approval_check(JeanX, 500, TabM=5):
                ch_j "Ok, sure."
            elif JeanX.SeenPussy and approval_check(JeanX, 900, TabM=4):
                ch_j "Yeah, ok."
            elif approval_check(JeanX, 1300, TabM=2) and JeanX.underwear:
                ch_j "For you, fine. . ."
            elif approval_check(JeanX, 700) and not JeanX.underwear:
                call Jean_NoPantiesOn
                if not _return and not JeanX.underwear:
                    if not approval_check(JeanX, 1500):
                        call Display_DressScreen (JeanX)
                        if not _return:
                            return
                    else:
                        return
            else:
                call Display_DressScreen (JeanX)
                if not _return:
                    ch_j "Um, not with you around."
                    if not JeanX.underwear:
                        ch_j "I'm not wearing any panties at the moment."
                    return

            if JeanX.legs == "pants" or JeanX.legs == "yoga_pants":
                $ JeanX.legs = 0
                "She tugs her pants off and drops them to the ground."
            else:
                $ JeanX.legs = 0
                "She tugs her skirt off and drops it to the ground."
            if renpy.showing('DressScreen'):
                pass
            elif JeanX.underwear:
                $ JeanX.SeenPanties = 1
            else:
                call Jean_First_Bottomless

        "You look great in those khaki pants." if JeanX.legs != "pants":
            ch_j "Yeah, I know."
            $ JeanX.legs = "pants"

        "You look great in those yoga pants." if JeanX.legs != "yoga_pants":
            if approval_check(JeanX, 800, TabM=4):
                ch_j "Yeah, I know."
                $ JeanX.legs = "yoga_pants"
            else:
                call Display_DressScreen (JeanX)
                if not _return:
                    ch_j "Those are kind of. . . tight."

        "What about wearing your green skirt?" if JeanX.legs != "skirt":
            ch_j "Sure, why not."
            $ JeanX.legs = "skirt"

        "You look great in those shorts." if JeanX.legs != "shorts" and "halloween" in JeanX.history:
            ch_j "Yeah, I know."
            $ JeanX.legs = "shorts"
        "Never mind":

            pass
    return




    label Jean_NoPantiesOn:
        menu:
            ch_j "I'm not wearing any panties at the moment."
            "Then you could slip on a pair of panties. . .":
                if approval_check(JeanX, 1500, TabM=4) or (JeanX.SeenPussy and approval_check(JeanX, 1100, TabM=4)):
                    $ JeanX.blushing = 1
                    ch_j "No, this is fine. . ."
                    $ JeanX.blushing = 0
                elif approval_check(JeanX, 700, TabM=4):
                    ch_j "Yeah, I guess."
                    if "lace_panties" in JeanX.Inventory:
                        $ JeanX.underwear  = "lace_panties"
                    else:
                        $ JeanX.underwear = "green_panties"
                    if approval_check(JeanX, 1200, TabM=4):
                        $ Line = JeanX.legs
                        $ JeanX.legs = 0
                        "She pulls off her [Line] and slips on the [JeanX.underwear]."
                    elif JeanX.legs == "skirt":
                        "She pulls out her [JeanX.underwear] and pulls them up under her skirt."
                        $ JeanX.legs = 0
                        "Then she drops the skirt to the floor."
                    else:
                        $ Line = JeanX.legs
                        $ JeanX.legs = 0
                        "She steps away a moment and then comes back wearing only the [JeanX.underwear]."
                    return
                else:
                    ch_j "Nope."
                    return 0
            "You could always just wear nothing at all. . .":

                if approval_check(JeanX, 1100, "LI", TabM=3) and JeanX.love > JeanX.inhibition:
                    ch_j "True. . ."
                elif approval_check(JeanX, 700, "OI", TabM=3) and JeanX.obedience > JeanX.inhibition:
                    ch_j "Yes. . ."
                elif approval_check(JeanX, 600, "I", TabM=3):
                    ch_j "Hrmm. . ."
                elif approval_check(JeanX, 1300, TabM=3):
                    ch_j "Fine."
                else:
                    $ JeanX.change_face("surprised")
                    $ JeanX.brows = "angry"
                    if JeanX.Taboo > 20:
                        ch_j ". . . not right now. . ."
                    else:
                        ch_j "Ha! Not for you, [JeanX.player_petname]."
                    return 0
            "Never mind.":

                ch_j "Ok. . ."
                return 0
        return 1




    menu Jean_Clothes_Under:
        "Tops":
            menu:
                "How about you lose the [JeanX.bra]?" if JeanX.bra:
                    $ JeanX.change_face("bemused", 1)
                    if JeanX.SeenChest and approval_check(JeanX, 900, TabM=2.7):
                        ch_j "Ok."
                    elif approval_check(JeanX, 1100, TabM=2):
                        if JeanX.Taboo:
                            ch_j "I don't know, here. . ."
                        else:
                            ch_j "Maybe. . ."
                    elif JeanX.top and approval_check(JeanX, 500, TabM=2):
                        ch_j "I guess I could. . ."
                    elif not JeanX.top:
                        call Display_DressScreen (JeanX)
                        if not _return:
                            ch_j "Not without some other top."
                            return
                    else:
                        call Display_DressScreen (JeanX)
                        if not _return:
                            ch_j "Nah."
                            return
                    $ Line = JeanX.bra
                    $ JeanX.bra = 0
                    if JeanX.top:
                        "She reaches under her [JeanX.top] grabs her [Line], and pulls it off, dropping it to the ground."
                    else:
                        "She pulls off her [Line] and drops it to the ground."
                        if not renpy.showing('DressScreen'):
                            call Jean_First_Topless


                "Try on that green bra." if JeanX.bra != "green_bra":
                    ch_j "Ok."
                    $ JeanX.bra = "green_bra"

                "How about that sports bra." if JeanX.bra != "sports_bra":
                    ch_j "Ok."
                    $ JeanX.bra = "sports_bra"

                "I like that lace bra." if JeanX.bra != "lace_bra" and "lace_bra" in JeanX.Inventory:
                    if JeanX.SeenChest or approval_check(JeanX, 1300, TabM=2):
                        ch_j "Sure."
                        $ JeanX.bra = "lace_bra"
                    else:
                        call Display_DressScreen (JeanX)
                        if not _return:
                            ch_j "It's a little transparent. . ."
                        else:
                            $ JeanX.bra = "lace_bra"

                "I like that black corset." if JeanX.bra != "corset" and "corset" in JeanX.Inventory:
                    if JeanX.SeenChest or approval_check(JeanX, 1000, TabM=1):
                        ch_j "Sure."
                        $ JeanX.bra = "corset"
                    else:
                        call Display_DressScreen (JeanX)
                        if not _return:
                            ch_j "It's a little revealing. . ."
                        else:
                            $ JeanX.bra = "corset"

                "I like that lace corset." if JeanX.bra != "lace corset" and "lace corset" in JeanX.Inventory:
                    if JeanX.SeenChest or approval_check(JeanX, 1300, TabM=2):
                        ch_j "Sure."
                        $ JeanX.bra = "lace corset"
                    else:
                        call Display_DressScreen (JeanX)
                        if not _return:
                            ch_j "It's a little transparent. . ."
                        else:
                            $ JeanX.bra = "lace corset"

                "I like that bikini top." if JeanX.bra != "bikini_top" and "bikini_top" in JeanX.Inventory:
                    if bg_current == "bg_pool":
                        ch_j "Sure."
                        $ JeanX.bra = "bikini_top"
                    else:
                        if JeanX.SeenChest or approval_check(JeanX, 1000, TabM=2):
                            ch_j "Sure."
                            $ JeanX.bra = "bikini_top"
                        else:
                            call Display_DressScreen (JeanX)
                            if not _return:
                                ch_j "This isn't really a \"bikini\" sort of place. . ."
                            else:
                                $ JeanX.bra = "bikini_top"
                "Never mind":
                    pass
            return
        "Hose and stockings options":

            menu:
                "You could lose the hose." if JeanX.hose:
                    $ JeanX.hose = 0
                "The thigh-high hose would look good with that." if JeanX.hose != "stockings":
                    $ JeanX.hose = "stockings"
                "The full length hose would look good with that." if JeanX.hose != "pantyhose" and "pantyhose" in JeanX.Inventory:
                    $ JeanX.hose = "pantyhose"
                "The ripped pantyhose would look good with that." if JeanX.hose != "ripped_pantyhose" and "ripped_pantyhose" in JeanX.Inventory:
                    $ JeanX.hose = "ripped_pantyhose"
                "The stockings and garterbelt would look good with that." if JeanX.hose != "stockings_and_garterbelt" and "stockings_and_garterbelt" in JeanX.Inventory:
                    $ JeanX.hose = "stockings_and_garterbelt"
                "Just the garterbelt would look good with that." if JeanX.hose != "garterbelt" and "stockings_and_garterbelt" in JeanX.Inventory:
                    $ JeanX.hose = "garterbelt"
                "Never mind":
                    pass
            return
        "Panties":


            menu:
                "You could lose those panties. . ." if JeanX.underwear:
                    $ JeanX.change_face("bemused", 1)
                    if approval_check(JeanX, 900) and (JeanX.legs or (JeanX.SeenPussy and not JeanX.Taboo)):

                        if approval_check(JeanX, 850, "L"):
                            ch_j "True. . ."
                        elif approval_check(JeanX, 500, "O"):
                            ch_j "Agreed."
                        elif approval_check(JeanX, 350, "I"):
                            ch_j "Heh."
                        else:
                            ch_j "Sure, I guess."
                    else:
                        if approval_check(JeanX, 1100, "LI", TabM=3) and JeanX.love > JeanX.inhibition:
                            ch_j "Well look, it's not about you, but. . ."
                        elif approval_check(JeanX, 700, "OI", TabM=3) and JeanX.obedience > JeanX.inhibition:
                            ch_j "Well. . ."
                        elif approval_check(JeanX, 600, "I", TabM=3):
                            ch_j "Hrmm. . ."
                        elif approval_check(JeanX, 1300, TabM=3):
                            ch_j "Okay, okay."
                        else:
                            call Display_DressScreen (JeanX)
                            if not _return:
                                $ JeanX.change_face("surprised")
                                $ JeanX.brows = "angry"
                                if JeanX.Taboo > 20:
                                    ch_j ". . . not right now. . ."
                                else:
                                    ch_j "Ha! Not for you, [JeanX.player_petname]."
                                return
                    $ Line = JeanX.underwear
                    $ JeanX.underwear = 0
                    if not JeanX.legs:
                        "She pulls off her [Line], then drops them to the ground."
                        if not renpy.showing('DressScreen'):
                            call Jean_First_Bottomless
                    elif approval_check(JeanX, 1200, TabM=4):
                        $ primary_action = JeanX.legs
                        $ JeanX.legs = 0
                        pause 0.5
                        $ JeanX.legs = primary_action
                        "She pulls off her [JeanX.legs] and [Line], then pulls the [JeanX.legs] back on."
                        $ primary_action = 1
                        call Jean_First_Bottomless (1)
                    elif JeanX.legs == "skirt":
                        "She reaches under her skirt and pulls her [Line] off."
                    else:
                        $ JeanX.blushing = 1
                        "She steps away a moment and then comes back."
                        $ JeanX.blushing = 0
                    $ Line = 0

                "Why don't you wear the green panties instead?" if JeanX.underwear and JeanX.underwear != "green_panties":
                    if approval_check(JeanX, 1100, TabM=3):
                        ch_j "Sure."
                        $ JeanX.underwear = "green_panties"
                    else:
                        call Display_DressScreen (JeanX)
                        if not _return:
                            ch_j "That's none of your busines."
                        else:
                            $ JeanX.underwear = "green_panties"

                "Why don't you wear the lace panties instead?" if "lace_panties" in JeanX.Inventory and JeanX.underwear and JeanX.underwear != "lace_panties":
                    if approval_check(JeanX, 1300, TabM=3):
                        ch_j "I guess."
                        $ JeanX.underwear = "lace_panties"
                    else:
                        call Display_DressScreen (JeanX)
                        if not _return:
                            ch_j "That's none of your busines."
                        else:
                            $ JeanX.underwear = "lace_panties"

                "I like those bikini bottoms." if "bikini_bottoms" in JeanX.Inventory and JeanX.underwear != "bikini_bottoms":
                    if bg_current == "bg_pool":
                        ch_j "Sure."
                        $ JeanX.underwear = "bikini_bottoms"
                    else:
                        if approval_check(JeanX, 1000, TabM=2):
                            ch_j "Sure."
                            $ JeanX.underwear = "bikini_bottoms"
                        else:
                            call Display_DressScreen (JeanX)
                            if not _return:
                                ch_j "This is not really a \"bikini\" sort of place. . ."
                            else:
                                $ JeanX.underwear = "bikini_bottoms"

                "You know, you could wear some panties with that. . ." if not JeanX.underwear:
                    $ JeanX.change_face("bemused", 1)
                    if JeanX.legs and (JeanX.love+JeanX.obedience) <= (2*JeanX.inhibition):
                        $ JeanX.mouth = "smile"
                        ch_j "I -could,- but I'd rather not. . ."
                        menu:
                            "Fine by me":
                                return
                            "I insist, put some on.":
                                if (JeanX.love+JeanX.obedience) <= (1.5*JeanX.inhibition):
                                    $ JeanX.change_face("angry", Eyes="side")
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
                            $ JeanX.underwear = "green_panties"
                        "How about the lace ones?" if "lace_panties" in JeanX.Inventory:
                            ch_j "Fine."
                            $ JeanX.underwear  = "lace_panties"
                "Never mind":
                    pass
            return
        "Never mind":
            pass
    return




    menu Jean_Clothes_Misc:

        "Maybe dry out your hair." if JeanX.hair == "wet":
            ch_p "Maybe dry out your hair"
            if approval_check(JeanX, 600):
                ch_j "Ok."
                $ JeanX.hair = "short"
            else:
                ch_j "I don't know, it's fine like this."

        "Wet hair style." if JeanX.hair != "wet":
            ch_p "You should go for that wet look with your hair"
            if approval_check(JeanX, 800):
                ch_j "Hmm?"
                $ JeanX.hair = "wet"
                "She wanders off for a minute and comes back."
                ch_j "Like this?"
            else:
                ch_j "Ugh, too much work."

        "Ponytail" if JeanX.hair != "pony" and "halloween" in JeanX.history:
            ch_p "Maybe do that side ponytail you had."
            if approval_check(JeanX, 600):
                ch_j "Ok."
                $ JeanX.hair = "pony"
            else:
                ch_j "I don't know, it's fine like this."
        "Let your hair loose" if JeanX.hair == "pony":
            ch_p "Maybe drop the ponytail."
            if approval_check(JeanX, 600):
                ch_j "Ok."
                $ JeanX.hair = "short"
            else:
                ch_j "I don't know, it's fine like this."

        "Grow pubes." if not JeanX.pubes:
            ch_p "You know, I like some nice hair down there. Maybe grow it out."
            if "pubes" in JeanX.Todo:
                $ JeanX.change_face("bemused", 1)
                ch_j "Give it some time. . ."
            else:
                $ JeanX.change_face("bemused", 1)
                if approval_check(JeanX, 1000, TabM=0):
                    ch_j "Ok, sure. . ."
                else:
                    $ JeanX.change_face("surprised")
                    $ JeanX.brows = "angry"
                    ch_j "None of your business."
                    return
                $ JeanX.Todo.append("pubes")
                $ JeanX.PubeC = 6
        "Shave pubes" if JeanX.pubes == 1:
            ch_p "I like it waxed clean down there."
            $ JeanX.change_face("bemused", 1)
            if "shave" in JeanX.Todo:
                ch_j "Yeah, I know, I'll get to it."
            else:
                if approval_check(JeanX, 1100, TabM=0):
                    ch_j "Really? I guess I could give it a shave. . ."
                else:
                    $ JeanX.change_face("surprised")
                    $ JeanX.brows = "angry"
                    ch_j "None of your business."
                    return
                $ JeanX.Todo.append("shave")

        "Piercings. [[See what she looks like without them first] (locked)" if not JeanX.SeenPussy and not JeanX.SeenChest:
            pass

        "Add ring piercings" if JeanX.piercings != "ring" and (JeanX.SeenPussy or JeanX.SeenChest):
            ch_p "You know, you'd look really nice with some ring body piercings"
            if "ring" in JeanX.Todo:
                ch_j "Yeah, I know, I'll get to it."
            else:
                $ JeanX.change_face("bemused", 1)
                $ Approval = approval_check(JeanX, 1150, TabM=0)
                if approval_check(JeanX, 900, "L", TabM=0) or (Approval and JeanX.love > 2* JeanX.obedience):
                    ch_j "You think they'd look good on me?"
                elif approval_check(JeanX, 600, "I", TabM=0) or (Approval and JeanX.inhibition > JeanX.obedience):
                    ch_j "I've been thinking about that for a while."
                elif approval_check(JeanX, 500, "O", TabM=0) or Approval:
                    ch_j "Sure, [JeanX.player_petname]."
                else:
                    $ JeanX.change_face("surprised")
                    $ JeanX.brows = "angry"
                    ch_j "Not interested, [JeanX.player_petname]."
                    return
                $ JeanX.Todo.append("ring")

        "Add barbell piercings" if JeanX.piercings != "barbell" and (JeanX.SeenPussy or JeanX.SeenChest):
            ch_p "You know, you'd look really nice with some barbell body piercings"
            if "barbell" in JeanX.Todo:
                ch_j "Yeah, I know, I'll get to it."
            else:
                $ JeanX.change_face("bemused", 1)
                $ Approval = approval_check(JeanX, 1150, TabM=0)
                if approval_check(JeanX, 900, "L", TabM=0) or (Approval and JeanX.love > 2*JeanX.obedience):
                    ch_j "You think they'd look good on me?"
                elif approval_check(JeanX, 600, "I", TabM=0) or (Approval and JeanX.inhibition > JeanX.obedience):
                    ch_j "I've been thinking about that for a while."
                elif approval_check(JeanX, 500, "O", TabM=0) or Approval:
                    ch_j "Sure, [JeanX.player_petname]."
                else:
                    $ JeanX.change_face("surprised")
                    $ JeanX.brows = "angry"
                    ch_j "Not interested, [JeanX.player_petname]."
                    return
                $ JeanX.Todo.append("barbell")

        "Remove Piercings" if JeanX.piercings:
            ch_p "You know, you'd look better without those piercings."
            $ JeanX.change_face("bemused", 1)
            $ Approval = approval_check(JeanX, 1350, TabM=0)
            if approval_check(JeanX, 950, "L", TabM=0) or (Approval and JeanX.love > JeanX.obedience):
                ch_j "Make up your mind . ."
            elif approval_check(JeanX, 700, "I", TabM=0) or (Approval and JeanX.inhibition > JeanX.obedience):
                ch_j "What?"
            elif approval_check(JeanX, 600, "O", TabM=0) or Approval:
                ch_j "Fine."
            else:
                $ JeanX.change_face("surprised")
                $ JeanX.brows = "angry"
                ch_j "I don't know, I kinda like them now. . ."
                return
            $ JeanX.piercings = 0

        "Add Suspenders" if JeanX.accessory != "suspenders" and JeanX.accessory != "suspenders2" and "halloween" in JeanX.history:
            $ JeanX.accessory = "suspenders"
        "Remove Suspenders" if JeanX.accessory == "suspenders" or JeanX.accessory == "suspenders2":
            $ JeanX.accessory = 0

        "Shift Suspenders" if JeanX.accessory == "suspenders" or JeanX.accessory == "suspenders2":
            $ JeanX.accessory = "suspenders" if JeanX.accessory == "suspenders2" else "suspenders2"
        "Never mind":















            pass
    return


return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
