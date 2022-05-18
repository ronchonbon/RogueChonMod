


label Jubes_Relationship:
    while True:
        menu:
            ch_v "What did you want to talk about?"
            "Do you want to be my girlfriend?" if JubesX not in Player.Harem and "ex" not in JubesX.traits:
                $ JubesX.daily_history.append("relationship")
                if "asked boyfriend" in JubesX.daily_history and "_angry" in JubesX.daily_history:
                    $ JubesX.change_face("_angry", 1)
                    ch_v "Like I said, not interested."
                    return
                elif "asked boyfriend" in JubesX.daily_history:
                    $ JubesX.change_face("_angry", 1)
                    ch_v "Still a no."
                    return
                elif JubesX.Break[0]:
                    $ JubesX.change_face("_angry", 1)
                    ch_v "I don't want to be with you."
                    if Player.Harem:
                        $ JubesX.daily_history.append("asked boyfriend")
                        return
                    else:
                        ch_p "Not anymore, at least. . ."

                $ JubesX.daily_history.append("asked boyfriend")

                if Player.Harem and "JubesYes" not in Player.traits:
                    if len(Player.Harem) >= 2:
                        ch_v "Well, you need to check in with the others first, [JubesX.player_petname]."
                    else:
                        ch_v "Well, you need to check in with [Player.Harem[0].name] first, [JubesX.player_petname]."
                    return

                if JubesX.Event[5]:
                    $ JubesX.change_face("_bemused", 1)
                    ch_v "You were the one that turned me down. . ."
                else:
                    $ JubesX.change_face("_surprised", 2)
                    ch_v "What? . ."
                    $ JubesX.change_face("_smile", 1)

                call Jubes_OtherWoman

                if JubesX.love >= 800:
                    $ JubesX.change_face("_surprised", 1)
                    $ JubesX.mouth = "_smile"
                    $ JubesX.change_stat("love", 200, 40)
                    ch_v "Sure!"
                    if "boyfriend" not in JubesX.player_petnames:
                        $ JubesX.player_petnames.append("boyfriend")
                    if "JubesYes" in Player.traits:
                        $ Player.traits.remove("JubesYes")
                    $ Player.Harem.append(JubesX)
                    call Harem_Initiation
                    "[JubesX.name] tackles you and kisses you deeply."
                    $ JubesX.change_face("_kiss", 1)
                    $ JubesX.action_counter["kiss"] += 1
                elif JubesX.obedience >= 500:
                    $ JubesX.change_face("_perplexed")
                    ch_v "I don't know if I want to -date- you. . ."
                elif JubesX.inhibition >= 500:
                    $ JubesX.change_face("_smile")
                    ch_v "I just wanna have fun, ya know?"
                else:
                    $ JubesX.change_face("_perplexed", 1)
                    ch_v "Whoa, slow your roll, [JubesX.player_petname]."

            "Do you want to get back together?" if "ex" in JubesX.traits:
                $ JubesX.daily_history.append("relationship")
                if "asked boyfriend" in JubesX.daily_history and "_angry" in JubesX.daily_history:
                    $ JubesX.change_face("_angry", 1)
                    ch_v "I told'ya, not interested."
                    return
                elif "asked boyfriend" in JubesX.daily_history:
                    $ JubesX.change_face("_angry", 1)
                    ch_v "Nope."
                    return

                $ JubesX.daily_history.append("asked boyfriend")

                if Player.Harem and "JubesYes" not in Player.traits:
                    if len(Player.Harem) >= 2:
                        ch_v "Well, you need to check in with the others first, [JubesX.player_petname]."
                    else:
                        ch_v "Well, you need to check in with [Player.Harem[0].name] first, [JubesX.player_petname]."
                    return

                $ counter = 0
                call Jubes_OtherWoman

                if JubesX.love >= 800:
                    $ JubesX.change_face("_surprised", 1)
                    $ JubesX.mouth = "_smile"
                    $ JubesX.change_stat("love", 90, 5)
                    ch_v "Ok, fine, we can give it a try."
                    if "boyfriend" not in JubesX.player_petnames:
                        $ JubesX.player_petnames.append("boyfriend")
                    $ JubesX.traits.remove("ex")
                    if "JubesYes" in Player.traits:
                        $ Player.traits.remove("JubesYes")
                    $ Player.Harem.append(JubesX)
                    call Harem_Initiation
                    "[JubesX.name] pulls you in and kisses you deeply."
                    $ JubesX.change_face("_kiss", 1)
                    $ JubesX.action_counter["kiss"] += 1
                elif JubesX.love >= 600 and approval_check(JubesX, 1500):
                    $ JubesX.change_face("_smile", 1)
                    $ JubesX.change_stat("love", 90, 5)
                    ch_v "Sure, I guess we can try it."
                    if "boyfriend" not in JubesX.player_petnames:
                        $ JubesX.player_petnames.append("boyfriend")
                    $ JubesX.traits.remove("ex")
                    if "JubesYes" in Player.traits:
                        $ Player.traits.remove("JubesYes")
                    $ Player.Harem.append(JubesX)
                    call Harem_Initiation
                    $ JubesX.change_face("_kiss", 1)
                    "[JubesX.name] gives you a quick kiss."
                    $ JubesX.change_face("_sly", 1)
                    $ JubesX.action_counter["kiss"] += 1
                elif JubesX.obedience >= 500:
                    $ JubesX.change_face("_sad")
                    ch_v "Nah, we gave it a shot."
                elif JubesX.inhibition >= 500:
                    $ JubesX.change_face("_perplexed")
                    ch_v "Nah, let's just keep it loose."
                else:
                    $ JubesX.change_face("_perplexed", 1)
                    ch_v "Nope, you blew it."



            "I wanted to ask about [[another girl]" if JubesX in Player.Harem:
                call AskDateOther

            "I think we should break up." if JubesX in Player.Harem:
                if "breakup talk" in JubesX.daily_history:
                    ch_v "Are you having a stroke?"
                else:
                    call Breakup (JubesX)
            "About that talk we had before. . .":

                menu:
                    "When you said you loved me. . ." if "lover" not in JubesX.traits and JubesX.Event[6] >= 20 and JubesX.Event[6] != 23:
                        call Jubes_Love_Redux

                    "When you were telling me all that stuff about yourself. . ." if "lover" not in JubesX.traits and JubesX.Event[6] == 23:
                        call Jubes_Love_Redux

                    "You said you wanted me to be more in control?" if "sir" not in JubesX.player_petnames and "sir" in JubesX.history:
                        if "asked sub" in JubesX.daily_history:
                            ch_v "We should give that a rest for today. . ."
                        else:
                            call Jubes_Sub_Asked
                    "You said you wanted me to be your Master?" if "master" not in JubesX.player_petnames and "master" in JubesX.history:
                        if "asked sub" in JubesX.daily_history:
                            ch_v "We should give that a rest for today. . ."
                        else:
                            call Jubes_Sub_Asked
                    "Never mind":
                        pass
            "Never Mind":

                return

    return

label Jubes_OtherWoman(counter=0):

    if not Player.Harem:
        return
    $ counter = int((JubesX.GirlLikeCheck(Player.Harem[0]) - 500)/2)

    $ JubesX.change_face("_perplexed")
    if len(Player.Harem) >= 2:
        ch_v "You're with [Player.Harem[0].name] though, right? And a bunch of others too!"
    else:
        ch_v "You're with [Player.Harem[0].name] though, right?"
    menu:
        extend ""
        "She said I can be with you too." if "JubesYes" in Player.traits:
            if approval_check(JubesX, 1800, Bonus = counter):
                $ JubesX.change_face("_smile", 1)
                if JubesX.love >= JubesX.obedience:
                    ch_v "Well, I can deal with that."
                elif JubesX.obedience >= JubesX.inhibition:
                    ch_v "Ok then, I can accept that."
                else:
                    ch_v "Cool."
            else:
                $ JubesX.change_face("_angry", 1)
                ch_v "Yeah, ok, but that's not cool with me."
                $ renpy.pop_call()


        "I could ask if she'd be ok with me dating you both." if "JubesYes" not in Player.traits:
            if approval_check(JubesX, 1800, Bonus = counter):
                $ JubesX.change_face("_smile", 1)
                if JubesX.love >= JubesX.obedience:
                    ch_v "Well, I could deal with that."
                elif JubesX.obedience >= JubesX.inhibition:
                    ch_v "Ok then, I could accept that."
                else:
                    ch_v "Cool."
                ch_v "Well ask her and let me know tomorrow."
            else:
                $ JubesX.change_face("_angry", 1)
                ch_v "Yeah, ok, but that's not cool with me."
            $ renpy.pop_call()
        "What she doesn't know won't hurt her.":

            if not approval_check(JubesX, 1800, Bonus = -counter):
                $ JubesX.change_face("_angry", 1)
                if not approval_check(JubesX, 1800):
                    ch_v "Well I'm not her."
                else:
                    ch_v "That sounds ominous."
                $ renpy.pop_call()
            else:
                $ JubesX.change_face("_smile", 1)
                if JubesX.love >= JubesX.obedience:
                    ch_v "I guess I could. . ."
                elif JubesX.obedience >= JubesX.inhibition:
                    ch_v "Ok then, I could accept that."
                else:
                    ch_v "Cool."
                $ JubesX.traits.append("downlow")
        "I can break it off with her.":

            $ JubesX.change_face("_sad")
            ch_v "Do that, and get back to me."
            $ renpy.pop_call()
        "You're right, I was dumb to ask.":

            $ JubesX.change_face("_sad")
            ch_v "Ya'think?"
            $ renpy.pop_call()

    return


label Jubes_About(Check=0):
    if Check not in all_Girls:
        ch_v "Who?"
        return
    ch_v "What do I think about her? Well. . ."
    if Check == RogueX:
        if "poly Rogue" in JubesX.traits:
            ch_v "Well, she's fun in the sack. . ."
        elif JubesX.LikeRogue >= 900:
            ch_v "She's got an amazing ass. . ."
        elif JubesX.LikeRogue >= 800:
            ch_v "She's. . . cool. . . cool. . ."
        elif JubesX.LikeRogue >= 700:
            ch_v "I like palling around with her."
        elif JubesX.LikeRogue >= 600:
            ch_v "She's cool."
        elif JubesX.LikeRogue >= 500:
            ch_v "I guess I've seen her around."
        elif JubesX.LikeRogue >= 400:
            ch_v "Ugh, don't get me started."
        elif JubesX.LikeRogue >= 300:
            ch_v "So annoying!"
        else:
            ch_v "Bitch."
    elif Check == KittyX:
        if "poly Kitty" in JubesX.traits:
            ch_v "Well, she's fun in the sack. . ."
        elif JubesX.LikeKitty >= 900:
            ch_v "She's so. . . perky. . ."
        elif JubesX.LikeKitty >= 800:
            ch_v "She's fit. . ."
        elif JubesX.LikeKitty >= 700:
            ch_v "Kinda slippery. . ."
        elif JubesX.LikeKitty >= 600:
            ch_v "She's cool."
        elif JubesX.LikeKitty >= 500:
            ch_v "I guess I've seen her around."
        elif JubesX.LikeKitty >= 400:
            ch_v "Ugh, don't get me started."
        elif JubesX.LikeKitty >= 300:
            ch_v "So whiney!"
        else:
            ch_v "Bitch."
    elif Check == EmmaX:
        if "poly Emma" in JubesX.traits:
            ch_v "Well, she's fun in the sack. . ."
        elif JubesX.LikeEmma >= 900:
            ch_v "Such amazing tits!"
        elif JubesX.LikeEmma >= 800:
            ch_v "What a figure on her. . ."
        elif JubesX.LikeEmma >= 700:
            ch_v "She's a cool teach. . ."
        elif JubesX.LikeEmma >= 600:
            ch_v "She's fine. . ."
        elif JubesX.LikeEmma >= 500:
            ch_v "I don't mind her."
        elif JubesX.LikeEmma >= 400:
            ch_v "Kinda a pain in the ass, right?"
        elif JubesX.LikeEmma >= 300:
            ch_v "She gives me a headache."
        else:
            ch_v "Witch."
    elif Check == LauraX:
        if "poly Laura" in JubesX.traits:
            ch_v "Well, she's fun in the sack. . ."
        elif JubesX.LikeLaura >= 900:
            ch_v "What a minx!"
        elif JubesX.LikeLaura >= 800:
            ch_v "She smells dangerous. . ."
        elif JubesX.LikeLaura >= 700:
            ch_v "She's one tough cookie."
        elif JubesX.LikeLaura >= 600:
            ch_v "She's a lot of fun."
        elif JubesX.LikeLaura >= 500:
            ch_v "She's fine."
        elif JubesX.LikeLaura >= 400:
            ch_v "She can be a jerk."
        elif JubesX.LikeLaura >= 300:
            ch_v "She needs to mind her business."
        else:
            ch_v "Grrrrr."
    elif Check == JeanX:
        if "poly Jean" in JubesX.traits:
            ch_v "Well, she's fun in the sack. . ."
        elif JubesX.LikeJean >= 900:
            ch_v "She is pretty hot. . ."
        elif JubesX.LikeJean >= 800:
            ch_v "She's not bad looking. . ."
        elif JubesX.LikeJean >= 700:
            ch_v "She's. . . tolerable."
        elif JubesX.LikeJean >= 600:
            ch_v "I guess she's fine?"
        elif JubesX.LikeJean >= 500:
            ch_v "She's kind of a lot of a lot."
        elif JubesX.LikeJean >= 400:
            ch_v "She needs to cut it out with that mind BS."
        elif JubesX.LikeJean >= 300:
            ch_v "Hate her."
        else:
            ch_v "Bitch."
    elif Check == StormX:
        if "poly Storm" in JubesX.traits:
            ch_v "Well, she's fun in the sack. . ."
        elif JubesX.LikeStorm >= 900:
            ch_v "She's totally thicc, right?"
        elif JubesX.LikeStorm >= 800:
            ch_v "She's so beautiful. . ."
        elif JubesX.LikeStorm >= 700:
            ch_v "She's makes sure to get me my homework."
        elif JubesX.LikeStorm >= 600:
            ch_v "She's a great teach."
        elif JubesX.LikeStorm >= 500:
            ch_v "She's cool."
        elif JubesX.LikeStorm >= 400:
            ch_v "She can be mean."
        elif JubesX.LikeStorm >= 300:
            ch_v "She needs to stay out of my business."
        else:
            ch_v "Witch."
    return


label Jubes_Monogamy:

    menu:
        "Could you not hook up with other girls?" if "mono" not in JubesX.traits:
            if JubesX.Thirst >= 60 and not approval_check(JubesX, 1700, "LO", TabM=0):

                $ JubesX.change_face("_sly",1)
                if "mono" not in JubesX.daily_history:
                    $ JubesX.change_stat("obedience", 90, -2)
                ch_v "I could, but where would the fun in that be?"
                return
            elif approval_check(JubesX, 1200, "LO", TabM=0) and JubesX.love >= JubesX.obedience:

                $ JubesX.change_face("_sly",1)
                if "mono" not in JubesX.daily_history:
                    $ JubesX.change_stat("love", 90, 1)
                ch_v "Oh. . . want me for yourself?."
                ch_v "Fine, I'll be more careful. . ."
            elif approval_check(JubesX, 700, "O", TabM=0):

                $ JubesX.change_face("_sly",1,Eyes="_side")
                ch_v "Sure."
            else:

                $ JubesX.change_face("_sly",1)
                ch_v "Nah."
                return
            if "mono" not in JubesX.daily_history:
                $ JubesX.change_stat("obedience", 90, 3)
            $ JubesX.add_word(1,0,"mono")
            $ JubesX.traits.append("mono")
        "Don't hook up with other girls." if "mono" not in JubesX.traits:
            if approval_check(JubesX, 900, "O", TabM=0):

                $ JubesX.change_face("_sly",1,Eyes="_side")
                ch_v "Fine."
            elif JubesX.Thirst >= 60 and not approval_check(JubesX, 1700, "LO", TabM=0):

                $ JubesX.change_face("_sly",1)
                if "mono" not in JubesX.daily_history:
                    $ JubesX.change_stat("obedience", 90, -2)
                ch_v "I could, but where would the fun in that be?"
                return
            elif approval_check(JubesX, 600, "O", TabM=0):

                $ JubesX.change_face("_sly",1,Eyes="_side")
                ch_v "If you insist."
            elif approval_check(JubesX, 1400, "LO", TabM=0):

                $ JubesX.change_face("_sly",1)
                ch_v "Yeah, ok, but ask nicely next time."
            else:

                $ JubesX.change_face("_sly",1,Brows="_confused")
                ch_v "Nah."
                return
            if "mono" not in JubesX.daily_history:
                $ JubesX.change_stat("obedience", 90, 3)
            $ JubesX.add_word(1,0,"mono")
            $ JubesX.traits.append("mono")
        "It's ok if you hook up with other girls." if "mono" in JubesX.traits:
            if approval_check(JubesX, 700, "O", TabM=0):
                $ JubesX.change_face("_sly",1,Eyes="_side")
                ch_v "Cool, cool."
            elif approval_check(JubesX, 800, "L", TabM=0):
                $ JubesX.change_face("_sly",1)
                ch_v "Ok, but make sure you make it up to me. . ."
            else:
                $ JubesX.change_face("_sly",1,Brows="_confused")
                if "mono" not in JubesX.daily_history:
                    $ JubesX.change_stat("love", 90, -2)
                ch_v "Nice. . ."
            if "mono" not in JubesX.daily_history:
                $ JubesX.change_stat("obedience", 90, 3)
            if "mono" in JubesX.traits:
                $ JubesX.traits.remove("mono")
            $ JubesX.add_word(1,0,"mono")
        "Never mind.":
            pass
    return



label Jubes_Jumped:

    ch_p "Hey, Remember that time you threw yourself at me?"
    $ JubesX.change_face("_sly",1,Brows="_confused")
    menu:
        ch_v "Yeah?"
        "Could you maybe just ask instead?" if "chill" not in JubesX.traits:
            if JubesX.Thirst >= 60 and not approval_check(JubesX, 1500, "LO", TabM=0):

                $ JubesX.change_face("_sly",1)
                if "chill" not in JubesX.daily_history:
                    $ JubesX.change_stat("obedience", 90, -2)
                ch_v "Hey, better you than one of these other bloodbags. . ."
                return
            elif approval_check(JubesX, 1000, "LO", TabM=0) and JubesX.love >= JubesX.obedience:

                $ JubesX.change_face("_surprised",1)
                if "chill" not in JubesX.daily_history:
                    $ JubesX.change_stat("love", 90, 1)
                ch_v "Sorry, I. . . have needs. . ."
                $ JubesX.change_face("_sly",1,Eyes="_side")
                ch_v "I'll do better. . ."
            elif approval_check(JubesX, 500, "O", TabM=0):

                $ JubesX.change_face("_sly",1,Eyes="_side")
                ch_v "Sorry. . ."
            else:

                $ JubesX.change_face("_sly",1)
                ch_v "We'll see. . ."
                return
            if "chill" not in JubesX.daily_history:
                $ JubesX.change_stat("obedience", 90, 3)
            $ JubesX.add_word(1,0,"chill")
            $ JubesX.traits.append("chill")
        "Don't bother me like that." if "chill" not in JubesX.traits:
            if approval_check(JubesX, 800, "O", TabM=0):

                $ JubesX.change_face("_sly",1,Eyes="_side")
                ch_v "Fine."
            elif JubesX.Thirst >= 60 and not approval_check(JubesX, 500, "O", TabM=0):

                $ JubesX.change_face("_sly",1)
                if "chill" not in JubesX.daily_history:
                    $ JubesX.change_stat("obedience", 90, -2)
                ch_v "Sorry, I. . . have needs. . ."
                return
            elif approval_check(JubesX, 400, "O", TabM=0):

                $ JubesX.change_face("_sly",1,Eyes="_side")
                ch_v "Sure. . ."
            elif approval_check(JubesX, 500, "LO", TabM=0) and not approval_check(JubesX, 500, "I", TabM=0):

                $ JubesX.change_face("_sly",1)
                ch_v "Hey, don't come at me like that."
                ch_v "I can try though. . ."
            else:

                $ JubesX.change_face("_sly",1)
                ch_v "We'll see. . ."
                return
            if "chill" not in JubesX.daily_history:
                $ JubesX.change_stat("obedience", 90, 3)
            $ JubesX.add_word(1,0,"chill")
            $ JubesX.traits.append("chill")
        "Knock yourself out.":
            if approval_check(JubesX, 800, "L", TabM=0):
                $ JubesX.change_face("_sly",1)
                ch_v "Game on. . ."
            elif approval_check(JubesX, 700, "O", TabM=0):
                $ JubesX.change_face("_sly",1,Eyes="_side")
                ch_v "You got it!"
            else:
                $ JubesX.change_face("_sly",1,Brows="_confused")
                if "chill" not in JubesX.daily_history:
                    $ JubesX.change_stat("love", 90, -2)
                ch_v "Yeah, we'll see. . ."
            if "chill" not in JubesX.daily_history:
                $ JubesX.change_stat("obedience", 90, 3)
            if "chill" in JubesX.traits:
                $ JubesX.traits.remove("chill")
            $ JubesX.add_word(1,0,"chill")
        "Um, never mind.":
            pass
    return




label Jubes_Hungry:
    if JubesX.Chat[3]:
        ch_v "[[licks her lips] I'm a little thirsty. . ."
    elif JubesX.Chat[2]:
        ch_v "I really love that serum you whipped up."
    else:
        ch_v "[[licks her lips] I'm a little thirsty. . ."
    $ JubesX.traits.append("hungry")
return





label Jubes_SexChat:
    $ Line = "Yeah, what did you want to talk about?" if not Line else Line
    while True:
        menu:
            ch_v "[Line]"
            "My favorite thing to do is. . .":
                if "setfav" in JubesX.daily_history:
                    ch_v "I remember."
                else:
                    menu:
                        "Sex.":
                            $ JubesX.change_face("_sly")
                            if JubesX.player_favorite_action == "sex":
                                $ JubesX.change_stat("lust", 80, 5)
                                ch_v "Yeah, I know that. . ."
                            elif JubesX.favorite_action == "sex":
                                $ JubesX.change_stat("love", 90, 5)
                                $ JubesX.change_stat("lust", 80, 10)
                                ch_v "I really like it too!"
                            elif JubesX.action_counter["sex"] >= 5:
                                ch_v "Well I don't mind that."
                            elif not JubesX.action_counter["sex"]:
                                $ JubesX.change_face("_perplexed")
                                ch_v "Who's fucking you?"
                            else:
                                $ JubesX.change_face("_bemused")
                                ch_v "Heh, um, yeah, it's nice. . ."
                            $ JubesX.player_favorite_action = "sex"
                        "Anal.":

                            $ JubesX.change_face("_sly")
                            if JubesX.player_favorite_action == "anal":
                                $ JubesX.change_stat("lust", 80, 5)
                                ch_v "So you've said. . ."
                            elif JubesX.favorite_action == "anal":
                                $ JubesX.change_stat("love", 90, 5)
                                $ JubesX.change_stat("lust", 80, 10)
                                ch_v "I love it too!"
                            elif JubesX.action_counter["anal"] >= 10:
                                ch_v "Yeah, it's. . . nice. . ."
                            elif not JubesX.action_counter["anal"]:
                                $ JubesX.change_face("_perplexed")
                                ch_v "Who's fucking you?"
                            else:
                                $ JubesX.change_face("_bemused",Eyes="_side")
                                ch_v "Heh, heh, yeah, um, it's ok. . ."
                            $ JubesX.player_favorite_action = "anal"
                        "Blowjobs.":

                            $ JubesX.change_face("_sly")
                            if JubesX.player_favorite_action == "blowjob":
                                $ JubesX.change_stat("lust", 80, 3)
                                ch_v "Definitely."
                            elif JubesX.favorite_action == "blowjob":
                                $ JubesX.change_stat("love", 90, 5)
                                $ JubesX.change_stat("lust", 80, 5)
                                ch_v "Me too!"
                            elif JubesX.action_counter["blowjob"] >= 10:
                                ch_v "Yeah, you're delicious."
                            elif not JubesX.action_counter["blowjob"]:
                                $ JubesX.change_face("_perplexed")
                                ch_v "Who's sucking your dick?!"
                            else:
                                $ JubesX.change_face("_bemused")
                                ch_v "I'm. . . it's really good. . ."
                            $ JubesX.player_favorite_action = "blowjob"
                        "Titjobs.":

                            $ JubesX.change_face("_sly")
                            if JubesX.player_favorite_action == "titjob":
                                $ JubesX.change_stat("lust", 80, 5)
                                ch_v "Yeah, you've said that before. . ."
                            elif JubesX.favorite_action == "titjob":
                                $ JubesX.change_stat("love", 90, 5)
                                $ JubesX.change_stat("lust", 80, 7)
                                ch_v "Yeah, I enjoy that too. . ."
                            elif JubesX.action_counter["titjob"] >= 10:
                                ch_v "It's certainly an interesting experience . . ."
                            elif not JubesX.action_counter["titjob"]:
                                $ JubesX.change_face("_perplexed")
                                ch_v "Who's titfucking you?"
                            else:
                                $ JubesX.change_face("_bemused")
                                ch_v "That's nice of you to say. . ."
                                $ JubesX.change_stat("love", 80, 5)
                                $ JubesX.change_stat("inhibition", 50, 10)
                            $ JubesX.player_favorite_action = "titjob"
                        "Footjobs.":

                            $ JubesX.change_face("_sly")
                            if JubesX.player_favorite_action == "footjob":
                                $ JubesX.change_stat("lust", 80, 5)
                                ch_v "Yeah, you've said that. . ."
                            elif JubesX.favorite_action == "footjob":
                                $ JubesX.change_stat("love", 90, 5)
                                $ JubesX.change_stat("lust", 80, 7)
                                ch_v "I do like using my feet. . ."
                            elif JubesX.action_counter["footjob"] >= 10:
                                ch_v "I like it too . . ."
                            elif not JubesX.action_counter["footjob"]:
                                $ JubesX.change_face("_perplexed")
                                ch_v "Who's playing footsie with you?"
                            else:
                                $ JubesX.change_face("_bemused")
                                ch_v "Yeah, it's nice. . ."
                            $ JubesX.player_favorite_action = "footjob"
                        "Handjobs.":

                            $ JubesX.change_face("_sly")
                            if JubesX.player_favorite_action == "handjob":
                                $ JubesX.change_stat("lust", 80, 5)
                                ch_v "Yeah, you've said that. . ."
                            elif JubesX.favorite_action == "handjob":
                                $ JubesX.change_stat("love", 90, 5)
                                $ JubesX.change_stat("lust", 80, 7)
                                ch_v "You do feel pretty comfy. . ."
                            elif JubesX.action_counter["handjob"] >= 10:
                                ch_v "I like it too . . ."
                            elif not JubesX.action_counter["handjob"]:
                                $ JubesX.change_face("_perplexed")
                                ch_v "Who's jerking you off?"
                            else:
                                $ JubesX.change_face("_bemused")
                                ch_v "Yeah, it's nice. . ."
                            $ JubesX.player_favorite_action = "handjob"
                        "Feeling you up.":

                            $ counter = JubesX.action_counter["fondle_breasts"]+ JubesX.action_counter["fondle_thighs"]+ JubesX.action_counter["suck_breasts"] + JubesX.action_counter["hotdog"]
                            $ JubesX.change_face("_sly")
                            if JubesX.player_favorite_action == "fondle":
                                $ JubesX.change_stat("lust", 80, 3)
                                ch_v "Yeah, I think we're clear on that. . ."
                            elif JubesX.favorite_action in ("hotdog","suck_breasts","fondle_breasts","fondle_thighs"):
                                $ JubesX.change_stat("love", 90, 5)
                                $ JubesX.change_stat("lust", 80, 5)
                                ch_v "I love when you touch me. . ."
                            elif counter >= 10:
                                ch_v "Yeah, it's really nice . . ."
                            elif not counter:
                                $ JubesX.change_face("_perplexed")
                                ch_v "Who's letting you feel her up?"
                            else:
                                $ JubesX.change_face("_bemused")
                                ch_v "I do like how that feels. . ."
                            $ JubesX.player_favorite_action = "fondle"
                            $ counter = 0
                        "Kissing you.":

                            $ JubesX.change_face("_sly")
                            if JubesX.player_favorite_action == "kiss":
                                $ JubesX.change_stat("love", 90, 3)
                                ch_v "Mmmmm. . ."
                            elif JubesX.favorite_action == "kiss":
                                $ JubesX.change_stat("love", 90, 5)
                                $ JubesX.change_stat("lust", 80, 5)
                                ch_v "Hmm, the taste of you on my lips. . ."
                            elif JubesX.action_counter["kiss"] >= 10:
                                ch_v "I love kissing you too . . ."
                            elif not JubesX.action_counter["kiss"]:
                                $ JubesX.change_face("_perplexed")
                                ch_v "Who are you kissing?"
                            else:
                                $ JubesX.change_face("_bemused")
                                ch_v "I love kissing you too. . ."
                            $ JubesX.player_favorite_action = "kiss"

                    $ JubesX.daily_history.append("setfav")
            "What's your favorite thing to do?":

                if not approval_check(JubesX, 800):
                    $ JubesX.change_face("_perplexed")
                    ch_v ". . ."
                else:
                    if JubesX.SEXP >= 50:
                        $ JubesX.change_face("_sly")
                        ch_v "You should know. . ."
                    else:
                        $ JubesX.change_face("_bemused")
                        $ JubesX.eyes = "_side"
                        ch_v "Hmm. . ."


                    if not JubesX.favorite_action or JubesX.favorite_action == "kiss":
                        ch_v "Kissing?"
                    elif JubesX.favorite_action == "anal":
                        ch_v "Probably anal."
                    elif JubesX.favorite_action == "eat_ass":
                        ch_v "When you lick my ass."
                    elif JubesX.favorite_action == "finger_ass":
                        ch_v "Fingering my asshole, probably."
                    elif JubesX.favorite_action == "sex":
                        ch_v "Just the usual pounding."
                    elif JubesX.favorite_action == "eat_pussy":
                        ch_v "When you lick my pussy."
                    elif JubesX.favorite_action == "fondle_pussy":
                        ch_v "When you finger me."
                    elif JubesX.favorite_action == "blowjob":
                        ch_v "I -love- how your cock tastes."
                    elif JubesX.favorite_action == "titjob":
                        ch_v "When I use my tits."
                    elif JubesX.favorite_action == "footjob":
                        ch_v "Footjobs are pretty fun."
                    elif JubesX.favorite_action == "handjob":
                        ch_v "I like jerking you off."
                    elif JubesX.favorite_action == "hotdog":
                        ch_v "When you grind against me."
                    elif JubesX.favorite_action == "suck_breasts":
                        ch_v "When you suck my tits."
                    elif JubesX.favorite_action == "fondle_breasts":
                        ch_v "When you grab my tits."
                    elif JubesX.favorite_action == "fondle_thighs":
                        ch_v "When you rub my thighs."
                    else:
                        ch_v "How should I know?"



            "Don't talk as much during sex." if "vocal" in JubesX.traits:
                if "setvocal" in JubesX.daily_history:
                    $ JubesX.change_face("_perplexed")
                    ch_v "Make up your mind."
                else:
                    if approval_check(JubesX, 1000) and JubesX.obedience <= JubesX.love:
                        $ JubesX.change_face("_bemused")
                        $ JubesX.change_stat("obedience", 90, 1)
                        ch_v "Keep quiet, fine."
                        $ JubesX.traits.remove("vocal")
                    elif approval_check(JubesX, 700, "O"):
                        $ JubesX.change_face("_sadside")
                        $ JubesX.change_stat("obedience", 90, 1)
                        ch_v ". . ."
                        $ JubesX.traits.remove("vocal")
                    elif approval_check(JubesX, 600):
                        $ JubesX.change_face("_sly")
                        $ JubesX.change_stat("love", 90, -3)
                        $ JubesX.change_stat("obedience", 50, -1)
                        $ JubesX.change_stat("inhibition", 90, 5)
                        ch_v "Don't push it, [JubesX.player_petname]."
                    else:
                        $ JubesX.change_face("_angry")
                        $ JubesX.change_stat("love", 90, -5)
                        $ JubesX.change_stat("obedience", 60, -3)
                        $ JubesX.change_stat("inhibition", 90, 10)
                        ch_v "Nah."

                    $ JubesX.daily_history.append("setvocal")
            "Talk dirty to me during sex." if "vocal" not in JubesX.traits:
                if "setvocal" in JubesX.daily_history:
                    $ JubesX.change_face("_perplexed")
                    ch_v "Heard you the first time."
                else:
                    if approval_check(JubesX, 1000) and JubesX.obedience <= JubesX.love:
                        $ JubesX.change_face("_sly")
                        $ JubesX.change_stat("obedience", 90, 2)
                        ch_v "Louder? I can do loud. . ."
                        $ JubesX.traits.append("vocal")
                    elif approval_check(JubesX, 700, "O"):
                        $ JubesX.change_face("_sadside")
                        $ JubesX.change_stat("obedience", 90, 2)
                        ch_v "If 'ya want, [JubesX.player_petname]."
                        $ JubesX.traits.append("vocal")
                    elif approval_check(JubesX, 600):
                        $ JubesX.change_face("_sly")
                        $ JubesX.change_stat("obedience", 90, 3)
                        ch_v "Sure?"
                        $ JubesX.traits.append("vocal")
                    else:
                        $ JubesX.change_face("_angry")
                        $ JubesX.change_stat("inhibition", 90, 5)
                        ch_v ". . ."

                    $ JubesX.daily_history.append("setvocal")


            "Don't do your own thing as much during sex." if "passive" not in JubesX.traits:
                if "initiative" in JubesX.daily_history:
                    $ JubesX.change_face("_perplexed")
                    ch_v "Heard you the first time."
                else:
                    if approval_check(JubesX, 1200) and JubesX.obedience <= JubesX.love:
                        $ JubesX.change_face("_bemused")
                        $ JubesX.change_stat("obedience", 90, 1)
                        ch_v "Ok, you can take the lead. . ."
                        $ JubesX.traits.append("passive")
                    elif approval_check(JubesX, 700, "O"):
                        $ JubesX.change_face("_sadside")
                        $ JubesX.change_stat("obedience", 90, 1)
                        ch_v "I'll try to restrain myself. . ."
                        $ JubesX.traits.append("passive")
                    elif approval_check(JubesX, 600):
                        $ JubesX.change_face("_sly")
                        $ JubesX.change_stat("love", 90, -3)
                        $ JubesX.change_stat("obedience", 50, -1)
                        $ JubesX.change_stat("inhibition", 90, 5)
                        ch_v "Hm, no."
                    else:
                        $ JubesX.change_face("_angry")
                        $ JubesX.change_stat("love", 90, -5)
                        $ JubesX.change_stat("obedience", 60, -3)
                        $ JubesX.change_stat("inhibition", 90, 10)
                        ch_v "Uh-huh. . ."

                    $ JubesX.daily_history.append("initiative")
            "Take more initiative during sex." if "passive" in JubesX.traits:
                if "initiative" in JubesX.daily_history:
                    $ JubesX.change_face("_perplexed")
                    ch_v "Heard you the first time."
                else:
                    if approval_check(JubesX, 1000) and JubesX.obedience <= JubesX.love:
                        $ JubesX.change_face("_bemused")
                        $ JubesX.change_stat("obedience", 90, 1)
                        ch_v "I can take the lead. . ."
                        $ JubesX.traits.remove("passive")
                    elif approval_check(JubesX, 700, "O"):
                        $ JubesX.change_face("_sadside")
                        $ JubesX.change_stat("obedience", 90, 1)
                        ch_v "Sure, no problem."
                        $ JubesX.traits.remove("passive")
                    elif approval_check(JubesX, 600):
                        $ JubesX.change_face("_sly")
                        $ JubesX.change_stat("obedience", 90, 3)
                        ch_v "We'll see."
                        $ JubesX.traits.remove("passive")
                    else:
                        $ JubesX.change_face("_angry")
                        $ JubesX.change_stat("inhibition", 90, 5)
                        ch_v "Meh."

                    $ JubesX.daily_history.append("initiative")

            "About getting Jumped" if "jumped" in JubesX.history:
                call Jubes_Jumped
            "About when you masturbate":
                call NoFap (JubesX)

            "Never Mind" if Line == "Yeah, what did you want to talk about?":
                return
            "That's all." if Line != "Yeah, what did you want to talk about?":
                return
        if Line == "Yeah, what did you want to talk about?":
            $ Line = "Anything else?"
    return




label Jubes_Chitchat(O=0, Options=["default","default","default"]):
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:
        $ Options = [O]
    else:

        if JubesX not in Digits:
            if approval_check(JubesX, 500, "L") or approval_check(JubesX, 250, "I"):
                ch_v "Oh, here's my number, call me maybe."
                $ Digits.append(JubesX)
                return
            elif approval_check(JubesX, 250, "O"):
                ch_v "If you need to call me, here's my number."
                $ Digits.append(JubesX)
                return

        if "hungry" not in JubesX.traits and JubesX.event_counter["swallowed"] >= 3 and JubesX.location == bg_current:
            call Jubes_Hungry
            return

        if bg_current != "bg_restaurant" and bg_current != "HW Party" and (not Taboo or approval_check(JubesX, 800, "I")):
            if JubesX.location == bg_current and JubesX.Thirst >= 30 and "refused" not in JubesX.daily_history and "quicksex" not in JubesX.daily_history:
                $ JubesX.change_face("_sly",1)
                ch_v "Hey, did you. . . wanna do something?"
                call Quick_Sex (JubesX)
                return




        if JubesX.Event[0] and "key" not in JubesX.Chat:
            $ Options.append("key")

        if "mandrill" in Player.traits and "cologne chat" not in JubesX.daily_history:
            $ Options.append("mandrill")
        if "purple" in Player.traits and "cologne chat" not in JubesX.daily_history:
            $ Options.append("purple")
        if "corruption" in Player.traits and "cologne chat" not in JubesX.daily_history:
            $ Options.append("corruption")

        if "Jubes" not in JubesX.names:
            $ Options.append("jubes")

        if JubesX.Date >= 1 and bg_current != "bg_restaurant":

            $ Options.append("dated")



        if JubesX.action_counter["kiss"] >= 5:

            $ Options.append("kissed")

        if "vamp" in "contagious" not in JubesX.history:
            $ Options.append("contagious")
        if "dangerroom" in Player.daily_history:

            $ Options.append("dangerroom")
        if "showered" in JubesX.daily_history:

            $ Options.append("showercaught")
        if "fondle_breasts" in JubesX.daily_history or "fondle_pussy" in JubesX.daily_history or "fondle_ass" in JubesX.daily_history:

            $ Options.append("fondled")
        if "Dazzler and Longshot" in JubesX.inventory and "256 Shades of Grey" in JubesX.inventory and "Avengers Tower Penthouse" in JubesX.inventory:

            if "book" not in JubesX.Chat:
                $ Options.append("booked")
        if "lace_bra" in JubesX.inventory or "lace_panties" in JubesX.inventory:

            if "lingerie" not in JubesX.Chat:
                $ Options.append("lingerie")
        if JubesX.action_counter["handjob"]:

            $ Options.append("handy")
        if JubesX.event_counter["swallowed"]:

            $ Options.append("swallowed")
        if "cleaned" in JubesX.daily_history or "painted" in JubesX.daily_history:

            $ Options.append("facial")
        if JubesX.event_counter["sleepover"]:

            $ Options.append("sleep")
        if JubesX.event_counter["creampied"] or JubesX.event_counter["anal_creampied"]:

            $ Options.append("creampie")
        if JubesX.action_counter["sex"] or JubesX.action_counter["anal"]:

            $ Options.append("sexed")
        if JubesX.action_counter["anal"]:

            $ Options.append("anal")

        if "seenpeen" in JubesX.history:
            $ Options.append("seenpeen")
        if "topless" in JubesX.history:
            $ Options.append("topless")
        if "bottomless" in JubesX.history:
            $ Options.append("bottomless")



















        if not approval_check(JubesX, 300):
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)

    if Options[0] == "mandrill":
        $ JubesX.daily_history.append("cologne chat")
        $ JubesX.change_face("_confused")
        ch_v "(sniff, sniff). . . you smell like monkey butt . . ."
        ch_v ". . . why is that turning me on?"
        $ JubesX.change_face("_sexy", 2)
    elif Options[0] == "purple":
        $ JubesX.daily_history.append("cologne chat")
        $ JubesX.change_face("_sly",1)
        ch_v "(sniff, sniff). . . that's an unusual scent. . ."
        $ JubesX.change_face("_normal",0)
        ch_v ". . . did you want something?"
    elif Options[0] == "corruption":
        $ JubesX.daily_history.append("cologne chat")
        $ JubesX.change_face("_confused")
        ch_v "(sniff, sniff). . . that's. . . um, overpowering. . ."
        $ JubesX.change_face("_angry")
        ch_v ". . . dangerous. . ."
        $ JubesX.change_face("_sly")

    elif Options[0] == "caught":
        if "caught chat" in JubesX.Chat:
            ch_v "We should try not to get caught like that."
            if not approval_check(JubesX, 500, "I"):
                ch_v "Unless. . ."
        else:
            ch_v "Sorry we got dragged into the Professor's office like that."
            if not approval_check(JubesX, 500, "I"):
                ch_v "I guess you wouldn't want to be so public anymore."
            else:
                ch_v "I kinda had fun though. . ."
            $ JubesX.Chat.append("caught chat")
    elif Options[0] == "key":
        if JubesX.SEXP <= 15:
            ch_v "Be careful when you use that key . ."
        else:
            ch_v "I gave you a key, but you don't visit. . ."
        $ JubesX.Chat.append("key")










    elif Options[0] == "contagious":
        $ JubesX.change_face("_sadside",2)
        ch_v "Just so you know, the vampire thing. . ."
        ch_v "It's not contagious. . ."
        $ JubesX.change_face("_sadside",1)
        ch_v "It was, but Dr. Strange was able to cast a spell or something."
        ch_v "So you don't need to worry about it spreading to you or anything."
        $ JubesX.change_face("_sad",1)
        $ JubesX.add_word(1,0,0,0,"contagious")

    elif Options[0] == "jubes":

        ch_v "Oh, by the way, I also go by \"Jubes.\""
        ch_v "Thought you might wanna know that."
        $ JubesX.names.append("Jubes")
        $ JubesX.petnames.append("Jubes")
        menu:
            "Oh, that's cool, I think I'll call you that.":
                $ JubesX.change_stat("love", 70, 5)
                $ JubesX.name = "Jubes"
            "Ok, but I like [JubesX.name].":
                $ JubesX.change_stat("love", 70, 2)
                $ JubesX.change_stat("obedience", 70, 2)
                $ JubesX.change_face("_smile",1)
                ch_v "Oh, ok."

    elif Options[0] == "dated":

        ch_v "I liked going out, haven't had too many chances at that lately."

    elif Options[0] == "kissed":

        $ JubesX.change_face("_sly",1)
        ch_v "You're a great kisser, [JubesX.player_petname]."
        menu:
            extend ""
            "Hey. . .I'm the best there is at what I do.":
                $ JubesX.change_face("_smile",1)
                ch_v "Well. . . maybe."
                ch_v "We'll have to test that one out."
            "No. You think?":
                ch_v "Would I have said it otherwise?"

    elif Options[0] == "dangerroom":

        $ JubesX.change_face("_sly",1)
        ch_v "Hey,[JubesX.player_petname]. I saw you in the Danger Room, earlier."
        ch_v "You're surprisingly good at this, considering you lack the ability to pewpew."

    elif Options[0] == "showercaught":

        if "shower" in JubesX.Chat:
            ch_v "You saw me showering again. . ."
        else:
            ch_v "hey. don't you check before entering the showers?"
            $ JubesX.Chat.append("shower")
            menu:
                extend ""
                "It was a total accident! I promise!":
                    $ JubesX.change_stat("love", 50, 5)
                    $ JubesX.change_stat("love", 90, 2)
                    if approval_check(JubesX, 1200):
                        $ JubesX.change_face("_sly",1)
                        ch_v "I didn't say I minded. . ."
                    $ JubesX.change_face("_smile")
                    ch_v "Ok, sure, it's cool."
                "Just with you.":
                    $ JubesX.change_stat("obedience", 40, 5)
                    if approval_check(JubesX, 1000) or approval_check(JubesX, 700, "L"):
                        $ JubesX.change_stat("love", 90, 3)
                        $ JubesX.change_face("_sly",1)
                        ch_v "Well I guess that's kinda sweet. . ."
                    else:
                        $ JubesX.change_stat("love", 70, -5)
                        $ JubesX.change_face("_angry")
                        ch_v "Well, cut it out!"
                "Totally on purpose. I regret nothing.":
                    if approval_check(JubesX, 1200):
                        $ JubesX.change_stat("love", 90, 3)
                        $ JubesX.change_stat("obedience", 70, 10)
                        $ JubesX.change_stat("inhibition", 50, 5)
                        $ JubesX.change_face("_sly",1)
                        ch_v "Fair."
                    elif approval_check(JubesX, 800):
                        $ JubesX.change_stat("obedience", 60, 5)
                        $ JubesX.change_stat("inhibition", 50, 5)
                        $ JubesX.change_face("_perplexed",2)
                        ch_v "Well, I guess I can't blame you. . ."
                        $ JubesX.blushing = "_blush1"
                    else:
                        $ JubesX.change_stat("love", 50, -10)
                        $ JubesX.change_stat("love", 80, -10)
                        $ JubesX.change_stat("obedience", 50, 10)
                        $ JubesX.change_face("_angry")
                        ch_v "That's. . . off-putting. . ."

    elif Options[0] == "fondled":

        ch_v "Hey, um, could you feel me up a little?"

    elif Options[0] == "booked":

        ch_v "Hey, I read those books you gave me."
        menu:
            extend ""
            "Yeah? Did you like them?":
                $ JubesX.change_face("_sly",2)
                ch_v "Well. . . yeah, I guess. . ."
            "Good. You looked like you could use to learn a thing or two from them.":
                $ JubesX.change_stat("love", 90, -3)
                $ JubesX.change_stat("obedience", 70, 5)
                $ JubesX.change_stat("inhibition", 50, 5)
                $ JubesX.change_face("_sad")
                ch_v "Well. . . I guess I could."
        $ JubesX.blushing = "_blush1"
        $ JubesX.Chat.append("book")

    elif Options[0] == "lingerie":

        $ JubesX.change_face("_sly",2)
        ch_v "That underwear you got me was pretty nice. . . thanks."
        $ JubesX.blushing = "_blush1"
        $ JubesX.Chat.append("lingerie")

    elif Options[0] == "handy":

        $ JubesX.change_face("_sly",1)
        ch_v "I was daydreaming about having your cock in my hand. . ."
        ch_v "Maybe I should take it out of the dream. . ."
        $ JubesX.blushing = ""

    elif Options[0] == "blowjob":
        if "blowjob" not in JubesX.Chat:

            $ JubesX.change_face("_sly",2)
            ch_v "Hey, I didn't bite or anything, did I?"
            menu:
                extend ""
                "You were totally amazing.":
                    $ JubesX.change_stat("love", 90, 5)
                    $ JubesX.change_stat("inhibition", 60, 10)
                    $ JubesX.change_face("_normal",1)
                    ch_v "Cool. Cool. . . "
                    $ JubesX.change_face("_sexy",1)
                    ch_v "I'd like another taste sometime."
                "Honestly? It was good. . .but you could use a little practice, I think.":
                    if approval_check(JubesX, 300, "I") or not approval_check(JubesX, 800):
                        $ JubesX.change_stat("love", 90, -5)
                        $ JubesX.change_stat("obedience", 60, 10)
                        $ JubesX.change_stat("inhibition", 50, 10)
                        $ JubesX.change_face("_perplexed",1)
                        ch_v "Oh! Sorry!."
                    else:
                        $ JubesX.change_stat("obedience", 70, 15)
                        $ JubesX.change_stat("inhibition", 50, 5)
                        $ JubesX.change_face("_sexy",1)
                        ch_v "Yeah? Well, practice makes perfect. . ."
                "I guess. If you're into weird sounds and too much teeth. Spoiler, I'm not.":
                    $ JubesX.change_stat("love", 90, -5)
                    $ JubesX.change_stat("obedience", 60, 5)
                    $ JubesX.change_face("_sad",2)
                    ch_v "Well. . . sorry about that. . ."
            $ JubesX.blushing = "_blush1"
            $ JubesX.Chat.append("blowjob")
        else:
            $ Line = renpy.random.choice(["You know, your dick tastes great.", 
                            "I think I nearly dislocated my jaw last time.", 
                            "Lemme know if you want another blowjob sometime.",
                            "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
            ch_v "[Line]"

    elif Options[0] == "swallowed":

        if "swallow" in JubesX.Chat:
            ch_v "I wouldn't mind another taste of your. . ."
        else:
            ch_v "So. . . the other day. . ."
            ch_v "I really got a charge out of drinking your. . ."
            $ JubesX.change_face("_sly",1)
            ch_v "I wouldn't mind that again some time."
            $ JubesX.Chat.append("swallow")

    elif Options[0] == "facial":

        ch_v "Hey. . .I know this is kind of odd. . ."
        $ JubesX.change_face("_sexy",2)
        ch_v "It does feel nice to wear your. . . jiz, but. . ."
        ch_v "Also kinda a waste?"
        $ JubesX.blushing = "_blush1"

    elif Options[0] == "sleepover":

        ch_v "I really enjoyed the other night."
        ch_v "It felt nice spending the night with someone again."

    elif Options[0] == "creampie":

        "[JubesX.name] draws close to you so she can whisper into your ear."
        ch_v "I loved the feeling of having you cum inside me. . ."

    elif Options[0] == "sexed":

        ch_v "Hey, um. . ."
        $ JubesX.change_face("_sexy",2)
        ch_v ". . .when I've been. . . enjoying myself. . ."
        ch_v "I've been thinking about you."
        $ JubesX.blushing = "_blush1"

    elif Options[0] == "anal":

        $ JubesX.change_face("_sly")
        ch_v "I hadn't really done much anal before. . ."
        $ JubesX.change_face("_sexy",1)
        ch_v "Until you, at least."

    elif Options[0] == "seenpeen":
        $ JubesX.change_face("_sly",1, Eyes="_down")
        ch_v "Oh, hey, you're swinging some real meat down there, huh?"
        $ JubesX.change_face("_bemused",1)
        $ JubesX.change_stat("love", 50, 5)
        $ JubesX.history.remove("seenpeen")
    elif Options[0] == "topless":
        ch_v "Hey, so did you like my tits, or what?"
        call Jubes_First_TMenu
        $ JubesX.history.remove("topless")
    elif Options[0] == "bottomless":
        ch_v "Hey, so what'd you think when you first saw my. . . um. . ."
        ch_v "-my pussy. . ."
        call Jubes_First_BMenu
        $ JubesX.history.remove("bottomless")
















    elif Options[0] == "hate":
        $ Line = renpy.random.choice(["Get away from me.", 
                "I don't want you anywhere near me.", 
                "Back off.",
                "Fuck off."])
        ch_v "[Line]"
    else:

        $ D20 = renpy.random.randint(1, 21)
        if D20 == 1:
            $ JubesX.change_face("_smile")
            ch_v "It's nice being able to get out more. . ."
        else:






























































            $ JubesX.change_face("_smile")
            ch_v "I like hanging with you."

    $ Line = 0
    return


label Jubes_names:
    menu:
        ch_v "Oh? What would you like me to call you?"
        "My initial's fine.":
            $ JubesX.player_petname = Player.name[:1]
            ch_v "You got it, [JubesX.player_petname]."
        "Call me by my name.":
            $ JubesX.player_petname = Player.name
            ch_v "If you want, [JubesX.player_petname]."
        "Call me \"boyfriend\"." if "boyfriend" in JubesX.player_petnames:
            $ JubesX.player_petname = "boyfriend"
            ch_v "Sure thing, [JubesX.player_petname]."
        "Call me \"lover\"." if "lover" in JubesX.player_petnames:
            $ JubesX.player_petname = "lover"
            ch_v "Oooh, love to, [JubesX.player_petname]."
        "Call me \"sir\"." if "sir" in JubesX.player_petnames:
            $ JubesX.player_petname = "sir"
            ch_v "Yes, [JubesX.player_petname]."
        "Call me \"master\"." if "master" in JubesX.player_petnames:
            $ JubesX.player_petname = "master"
            ch_v "As you wish, [JubesX.player_petname]."
        "Call me \"sex friend\"." if "sex friend" in JubesX.player_petnames:
            $ JubesX.player_petname = "sex friend"
            ch_v "Heh, very fun, [JubesX.player_petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in JubesX.player_petnames:
            $ JubesX.player_petname = "fuck buddy"
            ch_v "I'm game if you are, [JubesX.player_petname]."
        "Call me \"daddy\"." if "daddy" in JubesX.player_petnames:
            $ JubesX.player_petname = "daddy"
            ch_v "Oh! You bet, [JubesX.player_petname]."
        "Dude works.":
            $ JubesX.player_petname = "dude"
            ch_v "You got it, dude."
        "Bro works." if "bro" in JubesX.player_petnames:
            $ JubesX.player_petname = "bro"
            ch_v "You got it, bro."
        "Nevermind.":
            return
    return


label Jubes_Pet:
    while 1:
        menu:
            extend ""
            "Polite":
                menu:
                    "I think I'll call you. . ."
                    "Jubes.":
                        $ JubesX.petname = "Jubes"
                        ch_v "I don't see why not, [JubesX.player_petname]."
                    "Jubilee.":

                        $ JubesX.petname = "Jubilee"
                        ch_v "I don't see why not, [JubesX.player_petname]."
                    "Jubilation.":

                        $ JubesX.petname = "Jubilation"
                        ch_v "I don't see why not, [JubesX.player_petname]."
                    "\"girl\".":

                        $ JubesX.petname = "girl"
                        if "boyfriend" in JubesX.player_petnames or approval_check(JubesX, 600, "L"):
                            $ JubesX.change_face("_sexy", 1)
                            ch_v "I'm totally your girl, [JubesX.player_petname]."
                        else:
                            $ JubesX.change_face("_angry")
                            ch_v "I am NOT your girl, [JubesX.player_petname]."
                    "\"boo\".":

                        $ JubesX.petname = "boo"
                        if "boyfriend" in JubesX.player_petnames or approval_check(JubesX, 700, "L"):
                            $ JubesX.change_face("_sexy", 1)
                            ch_v "I am your boo, [JubesX.player_petname]."
                        else:
                            $ JubesX.change_face("_angry")
                            ch_v "I'm NOT your boo, [JubesX.player_petname]."
                    "\"bae\".":

                        $ JubesX.petname = "bae"
                        if "boyfriend" in JubesX.player_petnames or approval_check(JubesX, 600, "L"):
                            $ JubesX.change_face("_sexy", 1)
                            ch_v "I am your bae, [JubesX.player_petname]."
                        else:
                            $ JubesX.change_face("_angry")
                            ch_v "I'm NOT your bae, [JubesX.player_petname]."
                    "\"baby\".":

                        $ JubesX.petname = "baby"
                        if "boyfriend" in JubesX.player_petnames or approval_check(JubesX, 500, "L"):
                            $ JubesX.change_face("_sexy", 1)
                            ch_v "Cute, [JubesX.player_petname]."
                        else:
                            $ JubesX.change_face("_angry")
                            ch_v "I am not your baby."
                    "\"sweetie\".":


                        $ JubesX.petname = "sweetie"
                        if "boyfriend" in JubesX.player_petnames or approval_check(JubesX, 600, "L"):
                            ch_v "Aw, that's sweet, [JubesX.player_petname]."
                        else:
                            $ JubesX.change_face("_angry", 1)
                            ch_v "Too sweet, [JubesX.player_petname]."
                    "\"sexy\".":

                        $ JubesX.petname = "_sexy"
                        if "lover" in JubesX.player_petnames or approval_check(JubesX, 800):
                            $ JubesX.change_face("_sexy", 1)
                            ch_v "You know it, [JubesX.player_petname]."
                        else:
                            $ JubesX.change_face("_angry", 1)
                            ch_v "I don't know, [JubesX.player_petname]."
                    "\"lover\".":

                        $ JubesX.petname = "lover"
                        if "lover" in JubesX.player_petnames or approval_check(JubesX, 1200):
                            $ JubesX.change_face("_sexy", 1)
                            ch_v "I know."
                        else:
                            $ JubesX.change_face("_angry", 1)
                            ch_v "I don't think so, [JubesX.player_petname]."
                    "Back":

                        pass
            "Risky":

                menu:
                    "I think I'll call you. . ."
                    "\"slave\".":
                        $ JubesX.petname = "slave"
                        if "master" in JubesX.player_petnames or approval_check(JubesX, 800, "O"):
                            $ JubesX.change_face("_bemused", 1)
                            ch_v "As you wish, [JubesX.player_petname]."
                        else:
                            $ JubesX.change_face("_angry", 1)
                            ch_v "I am not your slave, [JubesX.player_petname]."
                    "\"pet\".":

                        $ JubesX.petname = "pet"
                        if "master" in JubesX.player_petnames or approval_check(JubesX, 650, "O"):
                            $ JubesX.change_face("_bemused", 1)
                            ch_v "You can pet me if you want, [JubesX.player_petname]."
                        else:
                            $ JubesX.change_face("_angry", 1)
                            ch_v "I am no one's pet, [JubesX.player_petname]."
                    "\"slut\".":

                        $ JubesX.petname = "slut"
                        if "sex friend" in JubesX.player_petnames or approval_check(JubesX, 900, "OI"):
                            $ JubesX.change_face("_sexy")
                            ch_v "Fair enough."
                        else:
                            $ JubesX.change_face("_angry", 1)
                            $ JubesX.mouth = "_surprised"
                            ch_v "Not with that mouth you don't."
                    "\"whore\".":

                        $ JubesX.petname = "whore"
                        if "fuckbuddy" in JubesX.player_petnames or approval_check(JubesX, 1000, "OI"):
                            $ JubesX.change_face("_sly")
                            ch_v "Ouch. . ."
                        else:
                            $ JubesX.change_face("_angry", 1)
                            ch_v "If either of us is going to be turning tricks. . ."
                    "\"sugartits\".":

                        $ JubesX.petname = "sugartits"
                        if "sex friend" in JubesX.player_petnames or approval_check(JubesX, 1400):
                            $ JubesX.change_face("_sly", 1)
                            ch_v "Huh?"
                        else:
                            $ JubesX.change_face("_angry", 1)
                            ch_v "Not cool."
                    "\"sex friend\".":

                        $ JubesX.petname = "sex friend"
                        if "sex friend" in JubesX.player_petnames or approval_check(JubesX, 600, "I"):
                            $ JubesX.change_face("_sly")
                            ch_v "Yeah. . ."
                        else:
                            $ JubesX.change_face("_angry", 1)
                            ch_v "Keep it down, [JubesX.player_petname]."
                    "\"fuckbuddy\".":

                        $ JubesX.petname = "fuckbuddy"
                        if "fuckbuddy" in JubesX.player_petnames or approval_check(JubesX, 700, "I"):
                            $ JubesX.change_face("_sly")
                            ch_v "Yup."
                        else:
                            $ JubesX.change_face("_angry", 1)
                            $ JubesX.mouth = "_surprised"
                            ch_v "Not even, [JubesX.player_petname]."
                    "\"baby girl\".":

                        $ JubesX.petname = "baby girl"
                        if "daddy" in JubesX.player_petnames or approval_check(JubesX, 1200):
                            $ JubesX.change_face("_smile", 1)
                            ch_v "I guess?"
                        else:
                            $ JubesX.change_face("_angry", 1)
                            ch_v "Weirdo."

                    "\"Miss Lee\"." if "Miss Lee" in JubesX.names:
                        $ JubesX.petname = "Miss Lee"
                        if approval_check(JubesX, 900):
                            $ JubesX.change_face("_bemused", 1)
                            ch_v "Ok, if that's what you're into, [JubesX.player_petname]."
                        else:
                            $ JubesX.change_face("_sad", 1)
                            ch_v "That's kinda. . . formal, [JubesX.player_petname]."
                    "Back":

                        pass
            "Nevermind.":

                return
    return





label Jubes_Rename:

    $ JubesX.mouth = "_smile"
    ch_v "Yeah?"
    menu:
        extend ""
        "I think \"Jubilee's\" a pretty name." if JubesX.name != "Jubilee":
            $ JubesX.name = "Jubilee"
            ch_v "Sounds good."
        "I think \"Jubes\" is a fun name." if JubesX.name != "Jubes":
            $ JubesX.name = "Jubes"
            ch_v "Ok, if you want. . ."
        "I think \"Jubilation's\" a lovely name." if JubesX.name != "Jubilation" and "Jubilation" in JubesX.names:
            $ JubesX.name = "Jubilation"
            ch_v "Aw, thanks. . ."
        "\"Miss Lee\"." if "Miss Lee" in JubesX.names:
            $ JubesX.name = "Miss Lee"
            if approval_check(JubesX, 900):
                $ JubesX.change_face("_bemused", 1)
                ch_v "Ok, if that's what you're into, [JubesX.player_petname]."
            else:
                $ JubesX.change_face("_sad", 1)
                ch_v "That's kinda. . . formal, [JubesX.player_petname]."
        "Nevermind.":
            pass
    $ JubesX.add_word(1,0,"namechange")
    return




label Jubes_Personality(counter=0):
    if not JubesX.Chat[4] or counter:
        "Since you're doing well in one area, you can convince Jubes to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_v "Yeah? What's up?"
        "More Obedient. [[Love to Obedience]" if JubesX.love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_v "If you really care about that, sure."
            $ JubesX.Chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if JubesX.love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_v "I could always be a bit more wild if that's what you want."
            $ JubesX.Chat[4] = 2

        "Less Inhibited. [[Obedience to Inhibition]" if JubesX.obedience > 900:
            ch_p "I want you to be less inhibited."
            ch_v "I guess I could go all-out."
            $ JubesX.Chat[4] = 3
        "More Loving. [[Obedience to Love]" if JubesX.obedience > 900:
            ch_p "I'd like you to learn to love me."
            ch_v "I can try."
            $ JubesX.Chat[4] = 4

        "More Obedient. [[Inhibition to Obedience]" if JubesX.inhibition > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_v "I can give it a shot. . ."
            $ JubesX.Chat[4] = 5

        "More Loving. [[Inhibition to Love]" if JubesX.inhibition > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_v "If that's something you need out of this. . ."
            $ JubesX.Chat[4] = 6

        "I guess just do what you like. . .[[reset]" if JubesX.Chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_v "Um, ok."
            $ JubesX.Chat[4] = 0
        "Repeat the rules":
            call Jubes_Personality (1)
            return
        "Nevermind.":
            return
    return







label Jubes_Summon(approval_bonus=approval_bonus):
    $ JubesX.change_outfit()
    if "no_summon" in JubesX.recent_history:
        if "_angry" in JubesX.recent_history:
            ch_v "Grrrrrrrrr."
        elif JubesX.recent_history.count("no_summon") > 1:
            ch_v "Back off!"
            $ JubesX.recent_history.append("_angry")
        else:


            ch_v "Like I said, I'm busy."
        $ JubesX.recent_history.append("no_summon")
        return

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    if JubesX.location == "bg_classroom":
        $ approval_bonus = -10
    elif JubesX.location == "bg_dangerroom":
        $ approval_bonus = -10
    elif JubesX.location == "bg_showerroom":
        $ approval_bonus = -30

    if D20 <= 3:

        $ Line = "no"











    if "les" in JubesX.recent_history:

        if approval_check(JubesX, 2000):
            ch_v "I have another guest here right now, but I guess you can drop by. . ."
            menu:
                extend ""
                "Sure":
                    $ Line = "go to"
                "No thanks.":
                    ch_v "Heh, your call."
                    return
        else:
            ch_v "Oh, um, I kinda have a guest."
            ch_v "I'll see you later, though?"
            $ JubesX.recent_history.append("no_summon")
            return
    elif not approval_check(JubesX, 700, "L") or not approval_check(JubesX, 600, "O"):

        if not approval_check(JubesX, 300):
            ch_v "I'm kinda busy, [JubesX.player_petname]."
            $ JubesX.recent_history.append("no_summon")
            return


        if "summoned" in JubesX.recent_history:
            pass
        elif "goto" in JubesX.recent_history:
            ch_v "You just left!"
        elif JubesX.location == "bg_classroom":
            ch_v "I'm in class, did you want to come too?"
        elif JubesX.location == "bg_dangerroom":
            ch_v "I'm in the Danger Room, [JubesX.player_petname], want in?"
        elif JubesX.location == "bg_campus":
            ch_v "I'm just enjoying the sun, want to come?"
        elif JubesX.location == "bg_jubes":
            ch_v "I'm in my room, [JubesX.player_petname], did you wanna drop by?"
        elif JubesX.location == "bg_player":
            ch_v "I'm in your room, [JubesX.player_petname], are you coming back?"
        elif JubesX.location == "bg_showerroom":
            if approval_check(JubesX, 1600):
                ch_v "I'm in the shower right now. Join me?"
            else:
                ch_v "I'm in the shower right now, [JubesX.player_petname]. We can hang later."
                $ JubesX.recent_history.append("no_summon")
                return
        elif JubesX.location == "hold":
            ch_v "I'm a little busy right now. Sorry?"
            $ JubesX.recent_history.append("no_summon")
            return
        else:
            ch_v "Why don't you come to me?"

        if "summoned" in JubesX.recent_history:
            ch_v "Oh, you want me back so soon?"
            $ Line = "yes"
        elif "goto" in JubesX.recent_history:
            menu:
                extend ""
                "You're right, be right back.":
                    ch_v "Cool, see you then."
                    $ Line = "go to"
                "Nah, it's better here.":
                    ch_v "Ok, later then."
                "But I'd {i}really{/i} like to see you over here.":
                    if approval_check(JubesX, 600, "L") or approval_check(JubesX, 1400):
                        $ Line = "lonely"
                    else:
                        $ Line = "no"
                "I said come over here.":
                    if approval_check(JubesX, 600, "O"):

                        $ Line = "command"
                    elif D20 >= 7 and approval_check(JubesX, 1400):

                        ch_v "Fine."
                        $ Line = "yes"
                    elif approval_check(JubesX, 200, "O"):

                        ch_v "Whatever."
                        ch_v "I'll be here if you change your mind."
                    else:

                        $ Line = "no"
        else:
            menu:
                extend ""
                "Sure, I'll be right there.":
                    $ JubesX.change_stat("love", 55, 1)
                    $ JubesX.change_stat("inhibition", 30, 1)
                    ch_v "Cool, see you then."
                    $ Line = "go to"
                "Nah, we can talk later.":

                    $ JubesX.change_stat("obedience", 50, 1)
                    $ JubesX.change_stat("obedience", 30, 2)
                    ch_v "Ok. Later then."
                "Could you please come visit me? I'm lonely.":

                    if approval_check(JubesX, 650, "L") or approval_check(JubesX, 1500):
                        $ JubesX.change_stat("love", 70, 1)
                        $ JubesX.change_stat("obedience", 50, 1)
                        $ Line = "lonely"
                    else:
                        $ JubesX.change_stat("inhibition", 30, 1)
                        $ Line = "no"
                        ch_v "Aw, how could I say \"no\"?"
                "Come on, it'll be fun.":

                    if approval_check(JubesX, 400, "L") and approval_check(JubesX, 800):
                        $ JubesX.change_stat("love", 70, 1)
                        $ JubesX.change_stat("obedience", 50, 1)
                        $ Line = "fun"
                    else:
                        $ JubesX.change_stat("inhibition", 30, 1)
                        $ Line = "no"
                "I said come over here.":

                    if approval_check(JubesX, 600, "O"):

                        $ JubesX.change_stat("love", 50, 1, 1)
                        $ JubesX.change_stat("love", 40, -1)
                        $ JubesX.change_stat("obedience", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and approval_check(JubesX, 1500):

                        $ JubesX.change_stat("love", 70, -2)
                        $ JubesX.change_stat("love", 90, -1)
                        $ JubesX.change_stat("obedience", 50, 2)
                        $ JubesX.change_stat("obedience", 90, 1)
                        ch_v "Ok, fine."
                        $ Line = "yes"

                    elif approval_check(JubesX, 200, "O"):

                        $ JubesX.change_stat("love", 60, -4)
                        $ JubesX.change_stat("love", 90, -3)
                        ch_v "No way."
                        $ JubesX.change_stat("inhibition", 40, 2)
                        $ JubesX.change_stat("inhibition", 60, 1)
                        $ JubesX.change_stat("obedience", 70, -3)
                        ch_v "I'm staying here."
                    else:

                        $ JubesX.change_stat("inhibition", 30, 1)
                        $ JubesX.change_stat("inhibition", 50, 1)
                        $ JubesX.change_stat("love", 50, -1, 1)
                        $ JubesX.change_stat("obedience", 70, -1)
                        $ Line = "no"
    else:


        if JubesX.love > JubesX.obedience:
            ch_v "Sure!"
        else:
            ch_v "Cool, on my way."
        $ Line = "yes"

    $ approval_bonus = 0

    if not Line:

        $ JubesX.recent_history.append("no_summon")
        return

    if Line == "no":

        if JubesX.location == "bg_classroom":
            ch_v "I can't skip this lecture."
        elif JubesX.location == "bg_dangerroom":
            ch_v "I'm just getting into it."
        else:
            ch_v "Sorry, [JubesX.player_petname], I'm kinda busy."
        $ JubesX.recent_history.append("no_summon")
        return

    elif Line == "go to":

        $ renpy.pop_call()
        $ JubesX.recent_history.append("goto")
        $ Player.recent_history.append("goto")
        $ Line = 0
        if JubesX.location == "bg_classroom":
            ch_v "K, there's room next to me."
            jump Class_Room
        elif JubesX.location == "bg_dangerroom":
            ch_v "Don't be long. . ."
            jump Danger_Room
        elif JubesX.location == "bg_jubes":
            ch_v "I'll. . . get ready."
            jump Jubes_Room
        elif JubesX.location == "bg_player":
            ch_v "I'll be waiting."
            jump Player_Room
        elif JubesX.location == "bg_showerroom":
            ch_v "I'll leave you some hot water."
            jump Shower_Room
        elif JubesX.location == "bg_campus":
            ch_v "I'm still in the shade a bit. . ."
            jump Campus
        elif JubesX.location in PersonalRooms:
            ch_v "Yeah, see you."
            $ bg_current = JubesX.location
            jump Misplaced
        else:
            ch_v "Um, I'll just meet you in my room."
            $ JubesX.location = "bg_jubes"
            jump Jubes_Room


    elif Line == "lonely":
        ch_v "Aw, well I can help with that!"
    elif Line == "command":
        ch_v "Ok, [JubesX.player_petname]."

    if bg_current not in PersonalRooms:
        call Jubes_Sunshock
        if _return:

            $ JubesX.recent_history.append("no_summon")
            return

    $ JubesX.recent_history.append("summoned")
    $ Line = 0
    if "locked" in Player.traits:
        call Locked_Door (JubesX)
        return
    $ JubesX.location = bg_current
    call Taboo_Level (0)
    $ JubesX.change_outfit()
    call set_the_scene
    return




label Jubes_Leave(approval_bonus=approval_bonus, GirlsNum=0):
    if "leaving" in JubesX.recent_history:
        $ JubesX.drain_word("leaving")
    else:
        return

    if JubesX.location == "hold":

        ch_v "Ok, peace out."
        return

    if JubesX in Party or "lockedtravels" in JubesX.traits:


        $ JubesX.location = bg_current
        return

    elif "freetravels" in JubesX.traits or not approval_check(JubesX, 700):

        $ JubesX.change_outfit()
        if GirlsNum:
            ch_v "Yeah, I'm leaving too."

        if JubesX.location == "bg_classroom":
            ch_v "I've got class."
        elif JubesX.location == "bg_dangerroom":
            ch_v "I'm hitting the Danger Room."
        elif JubesX.location == "bg_campus":
            ch_v "I'm gonna get some sun."
        elif JubesX.location == "bg_jubes":
            ch_v "I'm headed back to my room."
        elif JubesX.location == "bg_player":
            ch_v "I'm gonna hang out in your room for a bit."
        elif JubesX.location == "bg_pool":
            ch_v "I was hitting the pool."
        elif JubesX.location == "bg_showerroom":
            if approval_check(JubesX, 1400):
                ch_v "I'm hitting the showers, later."
            else:
                ch_v "I'm headed out."
        else:
            ch_v "I'm headed out, later."
        hide Jubes_Sprite
        return


    if bg_current == "bg_dangerroom":
        call Gym_Exit ([JubesX])

    $ JubesX.change_outfit()

    if "follow" not in JubesX.traits:

        $ JubesX.traits.append("follow")

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0

    if JubesX.location == "bg_classroom":
        $ approval_bonus = 10
    elif JubesX.location == "bg_dangerroom":
        $ approval_bonus = 20
    elif JubesX.location == "bg_showerroom":
        $ approval_bonus = 40


    if GirlsNum:
        ch_v "Yeah, I'm headed out too."

    if JubesX.location == "bg_classroom":
        ch_v "I've got class, you interested?"
    elif JubesX.location == "bg_dangerroom":
        ch_v "I've got some Danger Room time, you interested?"
    elif JubesX.location == "bg_campus":
        ch_v "I'm gonna get some sun on the quad, you interested?"
    elif JubesX.location == "bg_jubes":
        ch_v "I'm headed back to my room, you interested?"
    elif JubesX.location == "bg_player":
        ch_v "I'm going to hang out in your room for a bit, you interested?"
    elif JubesX.location == "bg_showerroom":
        if approval_check(JubesX, 1600):
            ch_v "I'm hitting the showers, you should join me."
        else:
            ch_v "I'm hitting the showers, laters."
            return
    elif JubesX.location == "bg_pool":
        ch_v "I was hitting the pool. Wanna come?"
    else:
        ch_v "Wanna join me?"


    menu:
        extend ""
        "Sure, I'll catch up.":
            if "followed" not in JubesX.recent_history:
                $ JubesX.change_stat("love", 55, 1)
                $ JubesX.change_stat("inhibition", 30, 1)
            $ Line = "go to"
        "Nah, we can talk later.":

            if "followed" not in JubesX.recent_history:
                $ JubesX.change_stat("obedience", 50, 1)
                $ JubesX.change_stat("obedience", 30, 2)
            ch_v "Sure, whatever."
        "Could you please stay with me? I'll get lonely.":

            if approval_check(JubesX, 650, "L") or approval_check(JubesX, 1500):
                if "followed" not in JubesX.recent_history:
                    $ JubesX.change_stat("love", 70, 1)
                    $ JubesX.change_stat("obedience", 50, 1)
                $ Line = "lonely"
            else:
                if "followed" not in JubesX.recent_history:
                    $ JubesX.change_stat("inhibition", 30, 1)
                $ Line = "no"
                ch_v "Aw, how could I say \"no\"?"
        "Come on, it'll be fun.":

            if approval_check(JubesX, 400, "L") and approval_check(JubesX, 800):
                $ JubesX.change_stat("love", 70, 1)
                $ JubesX.change_stat("obedience", 50, 1)
                $ Line = "fun"
            else:
                $ JubesX.change_stat("inhibition", 30, 1)
                $ Line = "no"
        "No, stay here.":

            if approval_check(JubesX, 600, "O"):

                if "followed" not in JubesX.recent_history:
                    $ JubesX.change_stat("love", 40, -2)
                    $ JubesX.change_stat("obedience", 90, 1)
                $ Line = "command"

            elif D20 >= 7 and approval_check(JubesX, 1400):

                if "followed" not in JubesX.recent_history:
                    $ JubesX.change_stat("love", 70, -2)
                    $ JubesX.change_stat("love", 90, -1)
                    $ JubesX.change_stat("obedience", 50, 2)
                    $ JubesX.change_stat("obedience", 90, 1)
                ch_v "I guess I could. . ."
                $ Line = "yes"

            elif approval_check(JubesX, 200, "O"):

                if "followed" not in JubesX.recent_history:
                    $ JubesX.change_stat("love", 70, -4)
                    $ JubesX.change_stat("love", 90, -2)
                ch_v "No way."
                if "followed" not in JubesX.recent_history:
                    $ JubesX.change_stat("inhibition", 40, 2)
                    $ JubesX.change_stat("inhibition", 60, 1)
                    $ JubesX.change_stat("obedience", 70, -2)
                ch_v "I'm staying here."
            else:

                if "followed" not in JubesX.recent_history:
                    $ JubesX.change_stat("inhibition", 30, 1)
                    $ JubesX.change_stat("inhibition", 50, 1)
                    $ JubesX.change_stat("love", 50, -1, 1)
                    $ JubesX.change_stat("love", 90, -2)
                    $ JubesX.change_stat("obedience", 70, -1)
                $ Line = "no"


    call Taboo_Level (0)
    $ JubesX.recent_history.append("followed")
    if not Line:

        hide Jubes_Sprite
        call Gym_Clothes_Off ([JubesX])
        return

    if Line == "no":

        if JubesX.location == "bg_classroom":
            ch_v "I really can't miss this one."
        elif JubesX.location == "bg_dangerroom":
            ch_v "Sorry [JubesX.player_petname], I need the exercise."
        else:
            ch_v "Sorry, I'm kinda busy."
        hide Jubes_Sprite
        call Gym_Clothes_Off ([JubesX])
        return

    elif Line == "go to":


        $ approval_bonus = 0
        $ Line = 0
        call DrainAll ("leaving")
        call DrainAll ("arriving")
        $ JubesX.recent_history.append("goto")
        $ Player.recent_history.append("goto")
        hide Jubes_Sprite
        call Gym_Clothes_Off ([JubesX])
        if JubesX.location == "bg_classroom":
            ch_v "Ok, get a move on then."
            jump Class_Room_Entry
        elif JubesX.location == "bg_dangerroom":
            ch_v "I'll get warmed up."
            jump Danger_Room_Entry
        elif JubesX.location == "bg_jubes":
            ch_v "Ok."
            jump Jubes_Room
        elif JubesX.location == "bg_player":
            ch_v "Good."
            jump Player_Room
        elif JubesX.location == "bg_showerroom":
            ch_v "Ok, nice."
            jump Shower_Room_Entry
        elif JubesX.location == "bg_campus":
            ch_v "Ok, nice."
            jump Campus_Entry
        elif JubesX.location == "bg_pool":
            ch_v "Cool."
            jump Pool_Entry
        else:
            ch_v "I'll just meet you in your room."
            $ JubesX.location = "bg_player"
            jump Player_Room



    elif Line == "lonely":
        ch_v "Aw, well I can help with that!"
    elif Line == "command":
        ch_v "Ok, [JubesX.player_petname]."

    $ Line = 0
    ch_v "I'll stay here."
    $ JubesX.location = bg_current
    return





label Jubes_Clothes:
    if JubesX.Taboo:
        if "exhibitionist" in JubesX.traits:
            ch_v "Yes? . ."
        elif approval_check(JubesX, 900, TabM=4) or approval_check(JubesX, 400, "I", TabM=3):
            ch_v "It's pretty public here, I don't think so. . ."
        else:
            ch_v "It's pretty public here, I don't think so. . ."
            ch_v "Can't we talk about this in our rooms?"
            return
    elif approval_check(JubesX, 900, TabM=4) or approval_check(JubesX, 600, "L") or approval_check(JubesX, 300, "O"):
        ch_v "Oh, what were you thinking? . ."
    else:
        ch_v "I don't think I really need your fashion advice."
        return

    if Girl != JubesX or Line == "Giftstore":

        $ renpy.pop_call()
    $ Line = 0
    $ Girl = JubesX
    call shift_focus (Girl)

label Jubes_Wardrobe_Menu:
    $ JubesX.change_face()
    $ primary_action = 1
    while True:
        menu:
            ch_v "What about my clothes?"
            "Overshirts":
                call Jubes_Clothes_Over
            "Legwear":
                call Jubes_Clothes_Legs
            "Underwear":
                call Jubes_Clothes_Under
            "Accessories":
                call Jubes_Clothes_Misc
            "Outfit Management":
                call Jubes_Clothes_Outfits
            "Let's talk about what you wear around.":
                call Clothes_Schedule (JubesX)

            "Could I get a look at it?" if JubesX.location != bg_current:

                call OutfitShame (JubesX, 0, 2)
                if _return:
                    show PhoneSex zorder 150
                    ch_v "Ok, that good?"
                hide PhoneSex
            "Could I get a look at it?" if renpy.showing('DressScreen'):

                call OutfitShame (JubesX, 0, 2)
                if _return:
                    hide DressScreen
            "Would you be more comfortable behind a screen? (locked)" if JubesX.Taboo:
                pass
            "Would you be more comfortable behind a screen?" if JubesX.location == bg_current and not JubesX.Taboo and not renpy.showing('DressScreen'):

                if approval_check(JubesX, 1500) or (JubesX.SeenChest and JubesX.SeenPussy):
                    ch_v "I think I'm fine. . ."
                else:
                    show DressScreen zorder 150
                    ch_v "Yeah, this is better, thanks."

            "Gift for you (locked)" if Girl.location != bg_current:
                pass
            "Gift for you" if Girl.location == bg_current:
                ch_p "I'd like to give you something."
                call Gifts
            "Switch to. . .":

                if renpy.showing('DressScreen'):
                    call OutfitShame (JubesX, 0, 2)
                    if _return:
                        hide DressScreen
                    else:
                        $ JubesX.change_outfit()
                $ JubesX.Set_Temp_Outfit()
                $ primary_action = 0
                call Switch_Chat
                if Girl != JubesX:
                    ch_p "I wanted to talk about your clothes."
                    call expression Girl.tag +"_Clothes"
                $ Girl = JubesX
                call shift_focus (Girl)
            "Never mind, you look good like that.":

                if "wardrobe" not in JubesX.recent_history:

                    if JubesX.Chat[1] <= 1:
                        $ JubesX.change_stat("love", 70, 15)
                        $ JubesX.change_stat("obedience", 40, 20)
                        ch_v "Oh! Thank you."
                    elif JubesX.Chat[1] <= 10:
                        $ JubesX.change_stat("love", 70, 5)
                        $ JubesX.change_stat("obedience", 40, 7)
                        ch_v "Right?"
                    elif JubesX.Chat[1] <= 50:
                        $ JubesX.change_stat("love", 70, 1)
                        $ JubesX.change_stat("obedience", 40, 1)
                        ch_v "Uh-huh."
                    else:
                        ch_v "Sure."
                    $ JubesX.recent_history.append("wardrobe")
                if renpy.showing('DressScreen'):
                    call OutfitShame (JubesX, 0, 2)
                    if _return:
                        hide DressScreen
                    else:
                        $ JubesX.change_outfit()
                $ JubesX.Set_Temp_Outfit()
                $ JubesX.Chat[1] += 1
                $ primary_action = 0
                return







    menu Jubes_Clothes_Outfits:
        "You should remember that one. [[Set Custom]":

            menu:
                "Which slot would you like this saved in?"
                "Custom 1":
                    call OutfitShame (JubesX, 3, 1)
                "Custom 2":
                    call OutfitShame (JubesX, 5, 1)
                "Custom 3":
                    call OutfitShame (JubesX, 6, 1)
                "Gym Clothes":
                    call OutfitShame (JubesX, 4, 1)
                "Sleepwear":
                    call OutfitShame (JubesX, 7, 1)
                "Swimwear":
                    call OutfitShame (JubesX, 10, 1)
                "Never mind":

                    pass
        "Red and blue outfit":

            $ JubesX.change_outfit("casual1")
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ JubesX.Outfit = "casual1"
                    $ JubesX.Shame = 0
                    ch_v "Yeah, this one's a classic, right?"
                "Let's try something else though.":
                    ch_v "Ok."
        "Black Leather combo":

            $ JubesX.change_outfit("casual2")
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ JubesX.Outfit = "casual2"
                    $ JubesX.Shame = 0
                    ch_v "I know it's a little edgy and all, but I like it!"
                "Let's try something else though.":
                    ch_v "Ok."

        "Remember that outfit we put together? [[Set a custom outfit] (locked)" if not JubesX.Custom1[0] and not JubesX.Custom2[0] and not JubesX.Custom3[0]:
            pass

        "Remember that outfit we put together?" if JubesX.Custom1[0] or JubesX.Custom2[0] or JubesX.Custom3[0]:
            $ counter = 0
            while 1:
                menu:
                    "Throw on Custom 1 (locked)" if not JubesX.Custom1[0]:
                        pass
                    "Throw on Custom 1" if JubesX.Custom1[0]:
                        $ JubesX.change_outfit("custom1")
                        $ counter = 3
                    "Throw on Custom 2 (locked)" if not JubesX.Custom2[0]:
                        pass
                    "Throw on Custom 2" if JubesX.Custom2[0]:
                        $ JubesX.change_outfit("custom2")
                        $ counter = 5
                    "Throw on Custom 3 (locked)" if not JubesX.Custom3[0]:
                        pass
                    "Throw on Custom 3" if JubesX.Custom3[0]:
                        $ JubesX.change_outfit("custom3")
                        $ counter = 6

                    "You should wear this one in private. (locked)" if not counter:
                        pass
                    "You should wear this one in private." if counter:
                        if counter == 5:
                            $ JubesX.Clothing[9] = "custom2"
                        elif counter == 6:
                            $ JubesX.Clothing[9] = "custom3"
                        else:
                            $ JubesX.Clothing[9] = "custom1"
                        ch_v "Ok, sure."
                    "On second thought, forget about that one outfit. . .":

                        menu:
                            "Custom 1 [[clear custom 1]" if JubesX.Custom1[0]:
                                ch_v "Ok."
                                $ JubesX.Custom1[0] = 0
                            "Custom 1 [[clear custom 1] (locked)" if not JubesX.Custom1[0]:
                                pass
                            "Custom 2 [[clear custom 2]" if JubesX.Custom2[0]:
                                ch_v "Ok."
                                $ JubesX.Custom2[0] = 0
                            "Custom 2 [[clear custom 2] (locked)" if not JubesX.Custom2[0]:
                                pass
                            "Custom 3 [[clear custom 3]" if JubesX.Custom3[0]:
                                ch_v "Ok."
                                $ JubesX.Custom3[0] = 0
                            "Custom 3 [[clear custom 3] (locked)" if not JubesX.Custom3[0]:
                                pass
                            "Never mind, [[back].":
                                pass

                    "You should wear this one out. [[choose outfit first](locked)" if not counter:
                        pass
                    "You should wear this one out." if counter:
                        call Custom_Out (JubesX, counter)
                    "Ok, back to what we were talking about. . .":
                        $ counter = 0
                        return

        "Gym Clothes?" if not JubesX.Taboo or bg_current == "bg_dangerroom":
            $ JubesX.change_outfit("gym")

        "Sleepwear?" if not JubesX.Taboo:
            if approval_check(JubesX, 1200):
                $ JubesX.change_outfit("sleep")
            else:
                call Display_DressScreen (JubesX)
                if _return:
                    $ JubesX.change_outfit("sleep")

        "Swimwear? (locked)" if (JubesX.Taboo and bg_current != "bg_pool") or not JubesX.Swim[0]:
            $ JubesX.change_outfit("swimwear")
        "Swimwear?" if (not JubesX.Taboo or bg_current == "bg_pool") and JubesX.Swim[0]:
            $ JubesX.change_outfit("swimwear")

        "Halloween Costume?" if "halloween" in JubesX.history:
            ch_v "Ok."
            $ JubesX.change_outfit("costume")
        "Your birthday suit looks really great. . .":


            $ JubesX.change_face("_sexy", 1)
            $ Line = 0
            if not JubesX.bra and not JubesX.underwear and not JubesX.top and not JubesX.legs and not JubesX.hose:
                ch_v "Uh-huh. . . wait, how would you know?!"
            elif JubesX.SeenChest and JubesX.SeenPussy and approval_check(JubesX, 1200, TabM=4):
                ch_v ". . . yeah?"
                $ Line = 1
            elif approval_check(JubesX, 2000, TabM=4):
                ch_v "Well you get to the point!"
                $ Line = 1
            elif JubesX.SeenChest and JubesX.SeenPussy and approval_check(JubesX, 1200, TabM=0):
                ch_v "Maaaybe, but not here. . ."
            elif approval_check(JubesX, 2000, TabM=0):
                ch_v "Maaaybe, but not here. . ."
            elif approval_check(JubesX, 1000, TabM=0):
                $ JubesX.change_face("_confused", 1,Mouth="_smirk")
                ch_v "Yeah, but you'll just have to keep guessing. . ."
                $ JubesX.change_face("_bemused", 0)
            else:
                $ JubesX.change_face("_angry", 1)
                ch_v "That's not really any of your business!"

            if Line:

                $ JubesX.change_outfit("nude")
                "She throws her clothes off at her feet."
                call Jubes_First_Topless
                call Jubes_First_Bottomless (1)
                $ JubesX.change_face("_sexy")
                menu:
                    "You know, you should wear this one out. [[set current outfit]":
                        if "exhibitionist" in JubesX.traits:
                            ch_v "mmmm. . ."
                            $ JubesX.Outfit = "nude"
                            $ JubesX.change_stat("lust", 50, 10)
                            $ JubesX.change_stat("lust", 70, 5)
                            $ JubesX.Shame = 50
                        elif approval_check(JubesX, 800, "I") or approval_check(JubesX, 2800, TabM=0):
                            ch_v "Fun. . ."
                            $ JubesX.Outfit = "nude"
                            $ JubesX.Shame = 50
                        else:
                            $ JubesX.change_face("_sexy", 1)
                            $ JubesX.eyes = "_surprised"
                            ch_v "I really won't."
                    "Let's try something else though.":

                        if "exhibitionist" in JubesX.traits:
                            ch_v "Really?"
                        elif approval_check(JubesX, 800, "I") or approval_check(JubesX, 2800, TabM=0):
                            $ JubesX.change_face("_bemused", 1)
                            ch_v "Oh! i thought you wanted me to wear this out. . ."
                            ch_v ". . ."
                        else:
                            $ JubesX.change_face("_confused", 1)
                            ch_v "Yeah, I mean, I wouldn't. . ."
            $ Line = 0
        "Never mind":

            return

    return




    menu Jubes_Clothes_Over:

        "Why don't you go with no jacket?" if JubesX.accessory:
            $ JubesX.change_face("_bemused", 1)
            if JubesX.top or (approval_check(JubesX, 800, TabM=3) and (JubesX.bra or JubesX.SeenChest)):

                ch_v "Sure."
            elif approval_check(JubesX, 600, TabM=0):
                call Jubes_NoBra
                if not _return:
                    if not approval_check(JubesX, 1200):
                        call Display_DressScreen (JubesX)
                        if not _return:
                            return
                    else:
                        return
            else:
                call Display_DressScreen (JubesX)
                if not _return:
                    ch_v "Not right now."
                    if not JubesX.bra:
                        ch_v "I don't have anything under this. . ."
                    return
            $ JubesX.accessory = ""
            "She throws her Jacket at her feet."
            if not renpy.showing('DressScreen'):
                call Jubes_First_Topless

        "Why don't you go with no [JubesX.top]?" if JubesX.top:
            $ JubesX.change_face("_bemused", 1)
            if approval_check(JubesX, 800, TabM=3) and (JubesX.bra or JubesX.SeenChest):
                ch_v "Sure."
            elif approval_check(JubesX, 600, TabM=0):
                call Jubes_NoBra
                if not _return:
                    if not approval_check(JubesX, 1200):
                        call Display_DressScreen (JubesX)
                        if not _return:
                            return
                    else:
                        return
            else:
                call Display_DressScreen (JubesX)
                if not _return:
                    ch_v "Not right now."
                    if not JubesX.bra:
                        ch_v "I don't have anything under this. . ."
                    return
            $ Line = JubesX.top
            $ JubesX.top = ""
            "She throws her [Line] at her feet."
            if not JubesX.bra and not renpy.showing('DressScreen'):
                call Jubes_First_Topless

        "Try on that yellow jacket." if not JubesX.accessory:
            $ JubesX.change_face("_bemused")
            ch_v "Sure."
            $ JubesX.accessory = "jacket"

        "Maybe open the jacket more?" if JubesX.accessory and JubesX.accessory != "open_jacket":
            $ JubesX.change_face("_bemused")
            if JubesX.top or (approval_check(JubesX, 800, TabM=3) and (JubesX.bra or JubesX.SeenChest)):

                ch_v "Sure."
            elif approval_check(JubesX, 600, TabM=0):
                call Jubes_NoBra
                if not _return:
                    if not approval_check(JubesX, 1200):
                        call Display_DressScreen (JubesX)
                        if not _return:
                            return
                    else:
                        return
            else:
                call Display_DressScreen (JubesX)
                if not _return:
                    ch_v "Not right now."
                    if not JubesX.bra:
                        ch_v "I don't have anything under this. . ."
                    return
            $ JubesX.accessory = "open_jacket"
            if not renpy.showing('DressScreen'):
                call Jubes_First_Topless

        "Maybe just leave the jacket loose?" if JubesX.accessory and JubesX.accessory != "jacket":
            $ JubesX.change_face("_bemused")
            if JubesX.top or (approval_check(JubesX, 800, TabM=3) and (JubesX.bra or JubesX.SeenChest)):

                ch_v "Sure."
            elif approval_check(JubesX, 600, TabM=0):
                call Jubes_NoBra
                if not _return:
                    if not approval_check(JubesX, 1200):
                        call Display_DressScreen (JubesX)
                        if not _return:
                            return
                    else:
                        return
            else:
                call Display_DressScreen (JubesX)
                if not _return:
                    ch_v "Not right now."
                    if not JubesX.bra:
                        ch_v "I don't have anything under this. . ."
                    return
            $ JubesX.accessory = "jacket"
            if not renpy.showing('DressScreen'):
                call Jubes_First_Topless

        "Maybe zip the jacket closed?" if JubesX.accessory and JubesX.accessory != "shut_jacket":
            $ JubesX.change_face("_bemused")
            ch_v "Sure."
            $ JubesX.accessory = "shut_jacket"

        "Try on that red shirt." if JubesX.top != "red_shirt":
            $ JubesX.change_face("_bemused")
            if not JubesX.top:

                ch_v "Sure."
            elif approval_check(JubesX, 800, TabM=0):
                ch_v "Yeah, ok."
            else:
                call Display_DressScreen (JubesX)
                if not _return:
                    $ JubesX.change_face("_bemused", 1)
                    ch_v "I don't really want to take this [JubesX.top] off at the moment."
                    return
            $ JubesX.top = "red_shirt"

        "Try on that leather shirt." if JubesX.top != "black_shirt":
            $ JubesX.change_face("_bemused")
            if not JubesX.top:

                ch_v "Sure."
            elif approval_check(JubesX, 800, TabM=0):
                ch_v "Yeah, ok."
            else:
                call Display_DressScreen (JubesX)
                if not _return:
                    $ JubesX.change_face("_bemused", 1)
                    ch_v "I don't really want to take this [JubesX.top] off at the moment."
                    return
            $ JubesX.top = "black_shirt"

        "Try on that pink tubetop." if JubesX.top != "_tube_top":
            $ JubesX.change_face("_bemused")
            if not JubesX.top:

                ch_v "Sure."
            elif approval_check(JubesX, 800, TabM=0):
                ch_v "Yeah, ok."
            else:
                call Display_DressScreen (JubesX)
                if not _return:
                    $ JubesX.change_face("_bemused", 1)
                    ch_v "I don't really want to take this [JubesX.top] off at the moment."
                    return
            $ JubesX.top = "_tube_top"

        "Maybe just throw on a towel?" if JubesX.top != "_towel":
            $ JubesX.change_face("_bemused", 1)
            if JubesX.bra or JubesX.SeenChest:
                ch_v "Odd."
            elif approval_check(JubesX, 1000, TabM=0):
                $ JubesX.change_face("_perplexed", 1)
                ch_v "Huh, sure . ."
            else:
                call Display_DressScreen (JubesX)
                if not _return:
                    ch_v "Nah."
                    return
            $ JubesX.top = "_towel"
        "Never mind":

            pass
    return




    label Jubes_NoBra:
        menu:
            ch_v "I don't exactly have anything on under this. . ."
            "Then you could slip something on under it. . .":
                if JubesX.SeenChest and approval_check(JubesX, 1000, TabM=3):
                    $ JubesX.blushing = "_blush1"
                    ch_v "Oh, I was just warning -you-. . ."
                    $ JubesX.blushing = ""
                elif approval_check(JubesX, 1200, TabM=4):
                    $ JubesX.blushing = "_blush1"
                    ch_v "Oh, I was just warning -you-. . ."
                    $ JubesX.blushing = ""
                elif approval_check(JubesX, 900, TabM=2) and "lace_bra" in JubesX.inventory:
                    ch_v "Well, I do have something I could throw on. . ."
                    $ JubesX.bra  = "lace_bra"
                    "She pulls out her lace bra and slips it under her [JubesX.top]."
                elif approval_check(JubesX, 600, TabM=2):
                    ch_v "Well, I do have something I could throw on. . ."
                    $ JubesX.bra = "_sports_bra"
                    "She pulls out her sports bra and slips it on under her [JubesX.top]."
                else:
                    ch_v "Yeah, that wouldn't help."
                    return 0
            "You could always just wear nothing at all. . .":

                if approval_check(JubesX, 1100, "LI", TabM=2) and JubesX.love > JubesX.inhibition:
                    ch_v "For you? sure. . ."
                elif approval_check(JubesX, 700, "OI", TabM=2) and JubesX.obedience > JubesX.inhibition:
                    ch_v "Sure. . ."
                elif approval_check(JubesX, 600, "I", TabM=2):
                    ch_v "Yeah. . ."
                elif approval_check(JubesX, 1300, TabM=2):
                    ch_v "Okay, fine."
                else:
                    $ JubesX.change_face("_surprised")
                    $ JubesX.brows = "_angry"
                    if JubesX.Taboo > 20:
                        ch_v "Not in public, I won't!"
                    else:
                        ch_v "Nah."
                    return 0
            "Never mind.":
                ch_v "Ok. . ."
                return 0
        return 1




    menu Jubes_Clothes_Legs:

        "Maybe go without the [JubesX.legs]." if JubesX.legs:
            $ JubesX.change_face("_sexy", 1)
            if JubesX.SeenPanties and JubesX.underwear and approval_check(JubesX, 500, TabM=5):
                ch_v "Ok, sure."
            elif JubesX.SeenPussy and approval_check(JubesX, 900, TabM=4):
                ch_v "Yeah, ok."
            elif approval_check(JubesX, 1300, TabM=2) and JubesX.underwear:
                ch_v "For you, fine. . ."
            elif approval_check(JubesX, 700) and not JubesX.underwear:
                call Jubes_NoPantiesOn
                if not _return and not JubesX.underwear:
                    if not approval_check(JubesX, 1500):
                        call Display_DressScreen (JubesX)
                        if not _return:
                            return
                    else:
                        return
            else:
                call Display_DressScreen (JubesX)
                if not _return:
                    ch_v "Um, not with you around."
                    if not JubesX.underwear:
                        ch_v "I'm not actually wearing any. . ."
                    return

            $ Line = JubesX.legs
            $ JubesX.legs = ""
            "She tugs her [Line] off and drops them to the ground."
            $ Line = 0

            if renpy.showing('DressScreen'):
                pass
            elif JubesX.underwear:
                $ JubesX.SeenPanties = 1
            else:
                call Jubes_First_Bottomless

        "Add leather_pants" if JubesX.legs != "_pants":
            ch_p "You look great in those leather_pants"
            ch_v "Yeah, ok."
            $ JubesX.legs = "_pants"

        "Add jeans_shorts" if JubesX.legs != "_shorts":
            ch_p "What about wearing your jeans shorts?"
            ch_v "Sure, why not."
            $ JubesX.legs = "_shorts"
        "Never mind":






            pass
    return




    label Jubes_NoPantiesOn:
        menu:
            ch_v "I'm actually not wearing any?"
            "Then you could slip on a pair of panties. . .":
                if JubesX.SeenPussy and approval_check(JubesX, 1100, TabM=4):
                    $ JubesX.blushing = "_blush1"
                    ch_v "No, no, it's fine like this. . ."
                    $ JubesX.blushing = ""
                elif approval_check(JubesX, 1500, TabM=4):
                    $ JubesX.blushing = "_blush1"
                    ch_v "No, no, it's fine like this. . ."
                    $ JubesX.blushing = ""
                elif approval_check(JubesX, 700, TabM=4):
                    ch_v "I could, I guess. . ."
                    if "lace_panties" in JubesX.inventory:
                        $ JubesX.underwear  = "lace_panties"
                    else:
                        $ JubesX.underwear = "blue_panties"
                    if approval_check(JubesX, 1200, TabM=4):
                        $ Line = JubesX.legs
                        $ JubesX.legs = ""
                        "She pulls off her [Line] and slips on the [JubesX.underwear]."
                    elif JubesX.legs == "_skirt":
                        "She pulls out her [JubesX.underwear] and pulls them up under her skirt."
                        $ JubesX.legs = ""
                        "Then she drops the skirt to the floor."
                    else:
                        $ Line = JubesX.legs
                        $ JubesX.legs = ""
                        "She steps away a moment and then comes back wearing only the [JubesX.underwear]."
                    return
                else:
                    ch_v "Nope."
                    return 0
            "You could always just wear nothing at all. . .":

                if approval_check(JubesX, 1100, "LI", TabM=3) and JubesX.love > JubesX.inhibition:
                    ch_v "True. . ."
                elif approval_check(JubesX, 700, "OI", TabM=3) and JubesX.obedience > JubesX.inhibition:
                    ch_v "Sure. . ."
                elif approval_check(JubesX, 600, "I", TabM=3):
                    ch_v "Hrmm. . ."
                elif approval_check(JubesX, 1300, TabM=3):
                    ch_v "Fine."
                else:
                    $ JubesX.change_face("_surprised")
                    $ JubesX.brows = "_angry"
                    if JubesX.Taboo > 20:
                        ch_v "Yeah, but not in public, [JubesX.player_petname]!"
                    else:
                        ch_v "Nah."
                    return 0
            "Never mind.":

                ch_v "Ok. . ."
                return 0
        return 1




    menu Jubes_Clothes_Under:
        "Tops":
            menu:
                "How about you lose the [JubesX.bra]?" if JubesX.bra:
                    $ JubesX.change_face("_bemused", 1)
                    if JubesX.SeenChest and approval_check(JubesX, 900, TabM=2.7):
                        ch_v "Sure."
                    elif approval_check(JubesX, 1100, TabM=2):
                        if JubesX.Taboo:
                            ch_v "I don't know, here. . ."
                        else:
                            ch_v "Maaaybe. . ."
                    elif JubesX.accessory == "jacket" and approval_check(JubesX, 600, TabM=2):
                        ch_v "This jacket is a bit revealing. . ."
                    elif JubesX.top and approval_check(JubesX, 500, TabM=2):
                        ch_v "I guess I could. . ."
                    elif not JubesX.top:
                        call Display_DressScreen (JubesX)
                        if not _return:
                            ch_v "Not without something over it. . ."
                            return
                    else:
                        call Display_DressScreen (JubesX)
                        if not _return:
                            ch_v "Nah."
                            return
                    $ Line = JubesX.bra
                    $ JubesX.bra = ""
                    if JubesX.accessory:
                        "She reaches under her jacket grabs her [Line], and pulls it off, dropping it to the ground."
                    elif JubesX.top:
                        "She reaches under her [JubesX.top] grabs her [Line], and pulls it off, dropping it to the ground."
                    else:
                        "She pulls off her [Line] and drops it to the ground."
                        if not renpy.showing('DressScreen'):
                            call Jubes_First_Topless

                "Add sports_bra" if JubesX.bra != "_sports_bra":
                    ch_p "Try on that sports bra."
                    ch_v "Ok."
                    $ JubesX.bra = "_sports_bra"

                "Add lace_bra" if JubesX.bra != "lace_bra" and "lace_bra" in JubesX.inventory:
                    ch_p "I like that bra corset."
                    if JubesX.SeenChest or approval_check(JubesX, 1300, TabM=2):
                        ch_v "K."
                        $ JubesX.bra = "lace_bra"
                    else:
                        call Display_DressScreen (JubesX)
                        if not _return:
                            ch_v "It's kinda revealing. . ."
                        else:
                            $ JubesX.bra = "lace_bra"

                "Add bikini_top" if JubesX.bra != "_bikini_top" and "_bikini_top" in JubesX.inventory:
                    ch_p "I like that bikini top."
                    if bg_current == "bg_pool":
                        ch_v "K."
                        $ JubesX.bra = "_bikini_top"
                    else:
                        if JubesX.SeenChest or approval_check(JubesX, 1000, TabM=2):
                            ch_v "K."
                            $ JubesX.bra = "_bikini_top"
                        else:
                            call Display_DressScreen (JubesX)
                            if not _return:
                                ch_v "This is not really a \"bikini\" sort of place. . ."
                            else:
                                $ JubesX.bra = "_bikini_top"
                "Never mind":
                    pass
            return
        "Hose and stockings options":

            menu:
                "You could lose the hose." if JubesX.hose and JubesX.hose != 'ripped_tights' and JubesX.hose != 'tights':
                    $ JubesX.hose = ""
                "The thigh-high hose would look good with that." if JubesX.hose != "_stockings":
                    $ JubesX.hose = "_stockings"
                "The pantyhose would look good with that." if JubesX.hose != "pantyhose" and "pantyhose" in JubesX.inventory:
                    $ JubesX.hose = "pantyhose"
                "The ripped pantyhose would look good with that." if JubesX.hose != "ripped_pantyhose" and "ripped_pantyhose" in JubesX.inventory:
                    $ JubesX.hose = "ripped_pantyhose"
                "The tall socks would look good with that." if JubesX.hose != "socks" and "socks" in JubesX.inventory:
                    $ JubesX.hose = "socks"
                "The stockings and garterbelt would look good with that." if JubesX.hose != "stockings_and_garterbelt" and "stockings_and_garterbelt" in JubesX.inventory:
                    $ JubesX.hose = "stockings_and_garterbelt"
                "Just the garterbelt would look good with that." if JubesX.hose != "garterbelt" and "stockings_and_garterbelt" in JubesX.inventory:
                    $ JubesX.hose = "garterbelt"
                "Never mind":
                    pass
            return
        "Panties":


            menu:
                "You could lose those panties. . ." if JubesX.underwear:
                    $ JubesX.change_face("_bemused", 1)
                    if approval_check(JubesX, 900) and (JubesX.legs or (JubesX.SeenPussy and not JubesX.Taboo)):

                        if approval_check(JubesX, 850, "L"):
                            ch_v "True. . ."
                        elif approval_check(JubesX, 500, "O"):
                            ch_v "Right. . ."
                        elif approval_check(JubesX, 350, "I"):
                            ch_v "Heh."
                        else:
                            ch_v "Sure, I guess."
                    else:
                        if approval_check(JubesX, 1100, "LI", TabM=3) and JubesX.love > JubesX.inhibition:
                            ch_v "I don't know, it's kinda public here. . ."
                        elif approval_check(JubesX, 700, "OI", TabM=3) and JubesX.obedience > JubesX.inhibition:
                            ch_v "Well. . ."
                        elif approval_check(JubesX, 600, "I", TabM=3):
                            ch_v "Hrmm. . ."
                        elif approval_check(JubesX, 1300, TabM=3):
                            ch_v "Okay, fine."
                        else:
                            call Display_DressScreen (JubesX)
                            if not _return:
                                $ JubesX.change_face("_surprised")
                                $ JubesX.brows = "_angry"
                                if JubesX.Taboo > 20:
                                    ch_v "This is just too public."
                                else:
                                    ch_v "Nah."
                                return
                    $ Line = JubesX.underwear
                    $ JubesX.underwear = ""
                    if not JubesX.legs:
                        "She pulls off her [Line], then drops them to the ground."
                        if not renpy.showing('DressScreen'):
                            call Jubes_First_Bottomless
                    elif approval_check(JubesX, 1200, TabM=4):
                        $ primary_action = JubesX.legs
                        $ JubesX.legs = ""
                        pause 0.5
                        $ JubesX.legs = primary_action
                        "She pulls off her [JubesX.legs] and [Line], then pulls the [JubesX.legs] back on."
                        $ primary_action = 1
                        call Jubes_First_Bottomless (1)
                    elif JubesX.legs == "_skirt":
                        "She reaches under her skirt and pulls her [Line] off."
                    else:
                        $ JubesX.blushing = "_blush1"
                        "She steps away a moment and then comes back."
                        $ JubesX.blushing = ""
                    $ Line = 0

                "Why don't you wear the blue panties instead?" if JubesX.underwear and JubesX.underwear != "blue_panties":
                    if approval_check(JubesX, 1100, TabM=3):
                        ch_v "Ok."
                        $ JubesX.underwear = "blue_panties"
                    else:
                        call Display_DressScreen (JubesX)
                        if not _return:
                            ch_v "That's none of your busines."
                        else:
                            $ JubesX.underwear = "blue_panties"

                "Why don't you wear the lace panties instead?" if "lace_panties" in JubesX.inventory and JubesX.underwear and JubesX.underwear != "lace_panties":
                    if approval_check(JubesX, 1300, TabM=3):
                        ch_v "I guess."
                        $ JubesX.underwear = "lace_panties"
                    else:
                        call Display_DressScreen (JubesX)
                        if not _return:
                            ch_v "That's none of your busines."
                        else:
                            $ JubesX.underwear = "lace_panties"

                "Why don't you wear the tiger panties instead?" if "tiger_panties" in JubesX.inventory and JubesX.underwear and JubesX.underwear != "tiger_panties":
                    if approval_check(JubesX, 1300, TabM=3):
                        ch_v "I guess."
                        $ JubesX.underwear = "tiger_panties"
                    else:
                        call Display_DressScreen (JubesX)
                        if not _return:
                            ch_v "That's none of your busines."
                        else:
                            $ JubesX.underwear = "tiger_panties"

                "I like those bikini bottoms." if "_bikini_bottoms" in JubesX.inventory and JubesX.underwear != "_bikini_bottoms":
                    if bg_current == "bg_pool":
                        ch_v "K."
                        $ JubesX.underwear = "_bikini_bottoms"
                    else:
                        if approval_check(JubesX, 1000, TabM=2):
                            ch_v "K."
                            $ JubesX.underwear = "_bikini_bottoms"
                        else:
                            call Display_DressScreen (JubesX)
                            if not _return:
                                ch_v "This is not really a \"bikini\" sort of place. . ."
                            else:
                                $ JubesX.underwear = "_bikini_bottoms"

                "You know, you could wear some panties with that. . ." if not JubesX.underwear:
                    $ JubesX.change_face("_bemused", 1)
                    if JubesX.legs and (JubesX.love+JubesX.obedience) <= (2*JubesX.inhibition):
                        $ JubesX.mouth = "_smile"
                        ch_v "I don't know about that."
                        menu:
                            "Fine by me":
                                return
                            "I insist, put some on.":
                                if (JubesX.love+JubesX.obedience) <= (1.5*JubesX.inhibition):
                                    $ JubesX.change_face("_angry", Eyes="_side")
                                    ch_v "Well too bad."
                                    return
                                else:
                                    $ JubesX.change_face("_sadside")
                                    ch_v "Oh, fine."
                    else:
                        ch_v "I guess. . ."
                    menu:
                        extend ""
                        "How about the blue ones?":
                            ch_v "Sure, ok."
                            $ JubesX.underwear = "blue_panties"
                        "How about the lace ones?" if "lace_panties" in JubesX.inventory:
                            ch_v "Alright."
                            $ JubesX.underwear  = "lace_panties"
                        "How about the tiger ones?" if "tiger_panties" in JubesX.inventory:
                            ch_v "Alright."
                            $ JubesX.underwear  = "tiger_panties"
                        "How about the bikini bottoms?" if "_bikini_bottoms" in JubesX.inventory:
                            ch_v "Alright."
                            $ JubesX.underwear  = "_bikini_bottoms"
                "Never mind":
                    pass
            return
        "Never mind":
            pass
    return




    menu Jubes_Clothes_Misc:

        "Shades in her hair" if JubesX.hair != "shades":
            ch_p "You're missing those signature shades!"
            if approval_check(JubesX, 600):
                ch_v "Oh yeah!"
                $ JubesX.hair = "shades"
            else:
                ch_v "I don't know, it's fine like this."

        "Shades out of her hair" if JubesX.hair == "shades":
            ch_p "You should try without the shades."
            if approval_check(JubesX, 600):
                ch_v "Ok. . "
                $ JubesX.hair = "short"
            else:
                ch_v "I don't know, it's fine like this."

        "Dry Hair" if JubesX.hair == "wet":
            ch_p "Maybe dry out your hair."
            if approval_check(JubesX, 600):
                ch_v "Ok."
                $ JubesX.hair = "short"
            else:
                ch_v "I don't know, it's fine like this."

        "Wet Hair style" if JubesX.hair != "wet":
            ch_p "You should go for that wet look with your hair."
            if approval_check(JubesX, 800):
                ch_v "Hmm?"
                $ JubesX.hair = "wet"
                "She wanders off for a minute and comes back."
                ch_v "Like this?"
            else:
                ch_v "Ugh, too much work."


        "Grow pubes" if not JubesX.pubes:
            ch_p "You know, I like some nice hair down there. Maybe grow it out."
            if "pubes" in JubesX.Todo:
                $ JubesX.change_face("_bemused", 1)
                ch_v "It doesn't grow out over night!"
            else:
                $ JubesX.change_face("_bemused", 1)
                if approval_check(JubesX, 1000, TabM=0):
                    ch_v "I guess I could. . ."
                else:
                    $ JubesX.change_face("_surprised")
                    $ JubesX.brows = "_angry"
                    ch_v "That's none of your business!"
                    return
                $ JubesX.Todo.append("pubes")
                $ JubesX.PubeC = 6
        "Shave pubes" if JubesX.pubes == "_hairy":
            ch_p "I like it waxed clean down there."
            $ JubesX.change_face("_bemused", 1)
            if "shave" in JubesX.Todo:
                ch_v "I heard you, I'll get around to it."
            else:
                if approval_check(JubesX, 1100, TabM=0):
                    ch_v "That's how you like it then? . ."
                else:
                    $ JubesX.change_face("_surprised")
                    $ JubesX.brows = "_angry"
                    ch_v "That's none of your business!"
                    return
                $ JubesX.Todo.append("shave")

        "Piercings. [[See what she looks like without them first] (locked)" if not JubesX.SeenPussy and not JubesX.SeenChest:
            pass

        "Add ring piercings" if JubesX.piercings != "_ring" and (JubesX.SeenPussy or JubesX.SeenChest):
            ch_p "You know, you'd look really nice with some ring body piercings."
            if "_ring" in JubesX.Todo:
                ch_v "I heard you, I'll get around to it."
            else:
                $ JubesX.change_face("_bemused", 1)
                $ approval = approval_check(JubesX, 1150, TabM=0)
                if approval_check(JubesX, 900, "L", TabM=0) or (approval and JubesX.love > 2* JubesX.obedience):
                    ch_v "You think they'd look good on me?"
                elif approval_check(JubesX, 600, "I", TabM=0) or (approval and JubesX.inhibition > JubesX.obedience):
                    ch_v "I've been thinking about that for a while."
                elif approval_check(JubesX, 500, "O", TabM=0) or approval:
                    ch_v "Yes, [JubesX.player_petname]."
                else:
                    $ JubesX.change_face("_surprised")
                    $ JubesX.brows = "_angry"
                    ch_v "Not into it, [JubesX.player_petname]."
                    return
                $ JubesX.Todo.append("_ring")

        "Add barbell piercings" if JubesX.piercings != "_barbell" and (JubesX.SeenPussy or JubesX.SeenChest):
            ch_p "You know, you'd look really nice with some barbell body piercings."
            if "_barbell" in JubesX.Todo:
                ch_v "I heard you, I'll get around to it."
            else:
                $ JubesX.change_face("_bemused", 1)
                $ approval = approval_check(JubesX, 1150, TabM=0)
                if approval_check(JubesX, 900, "L", TabM=0) or (approval and JubesX.love > 2*JubesX.obedience):
                    ch_v "You think they'd look good on me?"
                elif approval_check(JubesX, 600, "I", TabM=0) or (approval and JubesX.inhibition > JubesX.obedience):
                    ch_v "I've been thinking about that for a while."
                elif approval_check(JubesX, 500, "O", TabM=0) or approval:
                    ch_v "Yes, [JubesX.player_petname]."
                else:
                    $ JubesX.change_face("_surprised")
                    $ JubesX.brows = "_angry"
                    ch_v "Not into it, [JubesX.player_petname]."
                    return
                $ JubesX.Todo.append("_barbell")

        "Remove piercings" if JubesX.piercings:
            ch_p "You know, you'd look better without those piercings."
            $ JubesX.change_face("_bemused", 1)
            $ approval = approval_check(JubesX, 1350, TabM=0)
            if approval_check(JubesX, 950, "L", TabM=0) or (approval and JubesX.love > JubesX.obedience):
                ch_v "Make up your mind . ."
            elif approval_check(JubesX, 700, "I", TabM=0) or (approval and JubesX.inhibition > JubesX.obedience):
                ch_v "Well, this is annoying. . ."
            elif approval_check(JubesX, 600, "O", TabM=0) or approval:
                ch_v "Fine."
            else:
                $ JubesX.change_face("_surprised")
                $ JubesX.brows = "_angry"
                ch_v "I really like them though!"
                return
            $ JubesX.piercings = ""
        "Never mind":

            pass
    return


return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
