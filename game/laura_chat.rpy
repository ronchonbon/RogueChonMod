


label Laura_Relationship:
    while True:
        menu:
            ch_l "What did you want to talk about?"
            "Do you want to be my girlfriend?" if LauraX not in Player.Harem and "ex" not in LauraX.traits:
                $ LauraX.daily_history.append("relationship")
                if "asked boyfriend" in LauraX.daily_history and "_angry" in LauraX.daily_history:
                    $ LauraX.change_face("_angry", 1)
                    ch_l "Like I said, not interested."
                    return
                elif "asked boyfriend" in LauraX.daily_history:
                    $ LauraX.change_face("_angry", 1)
                    ch_l "Still a no."
                    return
                elif LauraX.Break[0]:
                    $ LauraX.change_face("_angry", 1)
                    ch_l "I'm not looking for a pack."
                    if Player.Harem:
                        $ LauraX.daily_history.append("asked boyfriend")
                        return
                    else:
                        ch_p "I'm not anymore."

                $ LauraX.daily_history.append("asked boyfriend")

                if Player.Harem and "LauraYes" not in Player.traits:
                    if len(Player.Harem) >= 2:
                        ch_l "You'd need to clear it with the others first, [LauraX.player_petname]."
                    else:
                        ch_l "You'd need to clear it with [Player.Harem[0].name] first, [LauraX.player_petname]."
                    return

                if LauraX.Event[5]:
                    $ LauraX.change_face("_bemused", 1)
                    ch_l "I asked, you said \"no\". . ."
                else:
                    $ LauraX.change_face("_surprised", 2)
                    ch_l "Huh? . ."
                    $ LauraX.change_face("_smile", 1)

                call Laura_OtherWoman

                if LauraX.love >= 800:
                    $ LauraX.change_face("_surprised", 1)
                    $ LauraX.mouth = "_smile"
                    $ LauraX.change_stat("love", 200, 40)
                    ch_l "Sure!"
                    if "boyfriend" not in LauraX.player_petnames:
                        $ LauraX.player_petnames.append("boyfriend")
                    if "LauraYes" in Player.traits:
                        $ Player.traits.remove("LauraYes")
                    $ Player.Harem.append(LauraX)
                    call Harem_Initiation
                    "[LauraX.name] tackles you and kisses you deeply."
                    $ LauraX.change_face("_kiss", 1)
                    $ LauraX.action_counter["kiss"] += 1
                elif LauraX.obedience >= 500:
                    $ LauraX.change_face("_perplexed")
                    ch_l "I don't know, \"dating\". . ."
                elif LauraX.inhibition >= 500:
                    $ LauraX.change_face("_smile")
                    ch_l "Nah, this is more fun."
                else:
                    $ LauraX.change_face("_perplexed", 1)
                    ch_l "Whoa, slow down, [LauraX.player_petname]."

            "Do you want to get back together?" if "ex" in LauraX.traits:
                $ LauraX.daily_history.append("relationship")
                if "asked boyfriend" in LauraX.daily_history and "_angry" in LauraX.daily_history:
                    $ LauraX.change_face("_angry", 1)
                    ch_l "Like I said, not interested."
                    return
                elif "asked boyfriend" in LauraX.daily_history:
                    $ LauraX.change_face("_angry", 1)
                    ch_l "Still a no."
                    return

                $ LauraX.daily_history.append("asked boyfriend")

                if Player.Harem and "LauraYes" not in Player.traits:
                    if len(Player.Harem) >= 2:
                        ch_l "You'd need to clear it with the others first, [LauraX.player_petname]."
                    else:
                        ch_l "You'd need to clear it with [Player.Harem[0].name] first, [LauraX.player_petname]."
                    return

                $ counter = 0
                call Laura_OtherWoman

                if LauraX.love >= 800:
                    $ LauraX.change_face("_surprised", 1)
                    $ LauraX.mouth = "_smile"
                    $ LauraX.change_stat("love", 90, 5)
                    ch_l "Ok, you've earned another shot!"
                    if "boyfriend" not in LauraX.player_petnames:
                        $ LauraX.player_petnames.append("boyfriend")
                    $ LauraX.traits.remove("ex")
                    if "LauraYes" in Player.traits:
                        $ Player.traits.remove("LauraYes")
                    $ Player.Harem.append(LauraX)
                    call Harem_Initiation
                    "[LauraX.name] pulls you in and kisses you deeply."
                    $ LauraX.change_face("_kiss", 1)
                    $ LauraX.action_counter["kiss"] += 1
                elif LauraX.love >= 600 and approval_check(LauraX, 1500):
                    $ LauraX.change_face("_smile", 1)
                    $ LauraX.change_stat("love", 90, 5)
                    ch_l "Um, ok, I guess."
                    if "boyfriend" not in LauraX.player_petnames:
                        $ LauraX.player_petnames.append("boyfriend")
                    $ LauraX.traits.remove("ex")
                    if "LauraYes" in Player.traits:
                        $ Player.traits.remove("LauraYes")
                    $ Player.Harem.append(LauraX)
                    call Harem_Initiation
                    $ LauraX.change_face("_kiss", 1)
                    "[LauraX.name] gives you a quick kiss."
                    $ LauraX.change_face("_sly", 1)
                    $ LauraX.action_counter["kiss"] += 1
                elif LauraX.obedience >= 500:
                    $ LauraX.change_face("_sad")
                    ch_l "I think it's best we keep things simple."
                elif LauraX.inhibition >= 500:
                    $ LauraX.change_face("_perplexed")
                    ch_l "That ruined the fun."
                else:
                    $ LauraX.change_face("_perplexed", 1)
                    ch_l "I can't trust you like that."



            "I wanted to ask about [[another girl]" if LauraX in Player.Harem:
                call AskDateOther

            "I think we should break up." if LauraX in Player.Harem:
                if "breakup talk" in LauraX.recent_history:
                    ch_l "Are you joking? We just had this conversation."
                elif "breakup talk" in LauraX.daily_history:
                    ch_l "That bored of me?"
                    ch_l "Not today, [LauraX.player_petname]."
                else:
                    call Breakup (LauraX)
            "About that talk we had before. . .":

                menu:
                    "When you said you loved me. . ." if "lover" not in LauraX.traits and LauraX.Event[6] >= 20 and LauraX.Event[6] != 23:
                        call Laura_Love_Redux

                    "When you were telling me all that stuff about yourself. . ." if "lover" not in LauraX.traits and LauraX.Event[6] == 23:
                        call Laura_Love_Redux

                    "You said you wanted me to be more in control?" if "sir" not in LauraX.player_petnames and "sir" in LauraX.history:
                        if "asked sub" in LauraX.recent_history:
                            ch_l "We just had this conversation."
                        elif "asked sub" in LauraX.daily_history:
                            ch_l "Enough of that talk for one day. . ."
                        else:
                            call Laura_Sub_Asked
                    "You said you wanted me to be your Master?" if "master" not in LauraX.player_petnames and "master" in LauraX.history:
                        if "asked sub" in LauraX.recent_history:
                            ch_l "We just had this conversation."
                        elif "asked sub" in LauraX.daily_history:
                            ch_l "Enough of that talk for one day. . ."
                        else:
                            call Laura_Sub_Asked
                    "Never mind":
                        pass
            "Never Mind":

                return

    return

label Laura_OtherWoman(counter=0):

    if not Player.Harem:
        return
    $ counter = int((LauraX.GirlLikeCheck(Player.Harem[0]) - 500)/2)

    $ LauraX.change_face("_perplexed")
    if len(Player.Harem) >= 2:
        ch_l "But you're with [Player.Harem[0].name] right now, and you've got a whole pack going."
    else:
        ch_l "But you're with [Player.Harem[0].name], aren't you?"
    menu:
        extend ""
        "She said I can be with you too." if "LauraYes" in Player.traits:
            if approval_check(LauraX, 1800, Bonus = counter):
                $ LauraX.change_face("_smile", 1)
                if LauraX.love >= LauraX.obedience:
                    ch_l "I guess I can share you."
                elif LauraX.obedience >= LauraX.inhibition:
                    ch_l "If that's what you want."
                else:
                    ch_l "Fine."
            else:
                $ LauraX.change_face("_angry", 1)
                ch_l "Yeah, I imagine she would, but I'm not sharing."
                $ renpy.pop_call()


        "I could ask if she'd be ok with me dating you both." if "LauraYes" not in Player.traits:
            if approval_check(LauraX, 1800, Bonus = counter):
                $ LauraX.change_face("_smile", 1)
                if LauraX.love >= LauraX.obedience:
                    ch_l "I guess I can share you."
                elif LauraX.obedience >= LauraX.inhibition:
                    ch_l "If that's what you want."
                else:
                    ch_l "Fine."
                ch_l "Well ask her and tell me in the morning."
            else:
                $ LauraX.change_face("_angry", 1)
                ch_l "Yeah, I imagine she would, but I'm not sharing."
            $ renpy.pop_call()
        "What she doesn't know won't hurt her.":

            if not approval_check(LauraX, 1800, Bonus = -counter):
                $ LauraX.change_face("_angry", 1)
                if not approval_check(LauraX, 1800):
                    ch_l "Well it'd hurt me."
                else:
                    ch_l "I don't like the sound of that."
                $ renpy.pop_call()
            else:
                $ LauraX.change_face("_smile", 1)
                if LauraX.love >= LauraX.obedience:
                    ch_l "I guess I could. . ."
                elif LauraX.obedience >= LauraX.inhibition:
                    ch_l "If that's what you want."
                else:
                    ch_l "Fine."
                $ LauraX.traits.append("downlow")
        "I can break it off with her.":

            $ LauraX.change_face("_sad")
            ch_l "Get back to me after."
            $ renpy.pop_call()
        "You're right, I was dumb to ask.":

            $ LauraX.change_face("_sad")
            ch_l "Yup."
            $ renpy.pop_call()

    return


label Laura_About(Check=0):
    if Check not in all_Girls:
        ch_l "Who?"
        return
    ch_l "What do I think about her? Well. . ."
    if Check == RogueX:
        if "poly Rogue" in LauraX.traits:
            ch_l "Yeah, we hook up, so. . ."
        elif LauraX.LikeRogue >= 900:
            ch_l "She's got a great ass. . ."
        elif LauraX.LikeRogue >= 800:
            ch_l "She's got a nice shape on her. . ."
        elif LauraX.LikeRogue >= 700:
            ch_l "She's good in a fight."
        elif LauraX.LikeRogue >= 600:
            ch_l "We get along ok."
        elif LauraX.LikeRogue >= 500:
            ch_l "I guess I've seen her around."
        elif LauraX.LikeRogue >= 400:
            ch_l "I don't want to talk about it."
        elif LauraX.LikeRogue >= 300:
            ch_l "Hate her."
        else:
            ch_l "Bitch."
    elif Check == KittyX:
        if "poly Kitty" in LauraX.traits:
            ch_l "Yeah, we hook up, so. . ."
        elif LauraX.LikeKitty >= 900:
            ch_l "I do like her little tits. . ."
        elif LauraX.LikeKitty >= 800:
            ch_l "She keeps in shape. . ."
        elif LauraX.LikeKitty >= 700:
            ch_l "Tough to hold down."
        elif LauraX.LikeKitty >= 600:
            ch_l "She's cool."
        elif LauraX.LikeKitty >= 500:
            ch_l "I guess I've seen her around."
        elif LauraX.LikeKitty >= 400:
            ch_l "I don't want to talk about it."
        elif LauraX.LikeKitty >= 300:
            ch_l "Hate her."
        else:
            ch_l "Bitch."
    elif Check == EmmaX:
        if "poly Emma" in LauraX.traits:
            ch_l "Yeah, we hook up, so. . ."
        elif LauraX.LikeEmma >= 900:
            ch_l "Really great rack on her. . ."
        elif LauraX.LikeEmma >= 800:
            ch_l "She smells really nice. . ."
        elif LauraX.LikeEmma >= 700:
            ch_l "She's nice to me after class."
        elif LauraX.LikeEmma >= 600:
            ch_l "She's a good teacher."
        elif LauraX.LikeEmma >= 500:
            ch_l "She's fine."
        elif LauraX.LikeEmma >= 400:
            ch_l "I could do with less of her attitude."
        elif LauraX.LikeEmma >= 300:
            ch_l "She needs to stay out of my head."
        else:
            ch_l "Grrrrr."
    elif Check == JeanX:
        if "poly Jean" in LauraX.traits:
            ch_l "Yeah, we hook up, so. . ."
        elif LauraX.LikeJean >= 900:
            ch_l "She's got a great ass. . ."
        elif LauraX.LikeJean >= 800:
            ch_l "She's got a nice shape on her. . ."
        elif LauraX.LikeJean >= 700:
            ch_l "She's. . . ok."
        elif LauraX.LikeJean >= 600:
            ch_l "I guess she's ok?"
        elif LauraX.LikeJean >= 500:
            ch_l "She's kind of a chore."
        elif LauraX.LikeJean >= 400:
            ch_l "She needs to stay out of my head."
        elif LauraX.LikeJean >= 300:
            ch_l "Hate her."
        else:
            ch_l "Bitch."
    elif Check == StormX:
        if "poly Storm" in LauraX.traits:
            ch_l "Yeah, we hook up, so. . ."
        elif LauraX.LikeStorm >= 900:
            ch_l "Really great ass on her. . ."
        elif LauraX.LikeStorm >= 800:
            ch_l "She smells like a garden. . ."
        elif LauraX.LikeStorm >= 700:
            ch_l "She's nice to me after class."
        elif LauraX.LikeStorm >= 600:
            ch_l "She's a good teacher."
        elif LauraX.LikeStorm >= 500:
            ch_l "She's fine."
        elif LauraX.LikeStorm >= 400:
            ch_l "She can be mean."
        elif LauraX.LikeStorm >= 300:
            ch_l "She needs to stay out of my way."
        else:
            ch_l "Grrrrr."
    elif Check == JubesX:
        if "poly Jubes" in LauraX.traits:
            ch_l "Yeah, we hook up, so. . ."
        elif LauraX.LikeJubes >= 900:
            ch_l "I do love her smooth skin. . ."
        elif LauraX.LikeJubes >= 800:
            ch_l "She has a nice shape. . ."
        elif LauraX.LikeJubes >= 700:
            ch_l "Tough to pin down."
        elif LauraX.LikeJubes >= 600:
            ch_l "She's cool."
        elif LauraX.LikeJubes >= 500:
            ch_l "I guess I've seen her around."
        elif LauraX.LikeJubes >= 400:
            ch_l "She bites."
        elif LauraX.LikeJubes >= 300:
            ch_l "Hate her."
        else:
            ch_l "Bitch."
    return


label Laura_Monogamy:

    menu:
        "Could you not hook up with other girls?" if "mono" not in LauraX.traits:
            if LauraX.Thirst >= 60 and not approval_check(LauraX, 1700, "LO", TabM=0):

                $ LauraX.change_face("_sly",1)
                if "mono" not in LauraX.daily_history:
                    $ LauraX.change_stat("obedience", 90, -2)
                ch_l "I would, but you aren't around enough. . ."
                return
            elif approval_check(LauraX, 1200, "LO", TabM=0) and LauraX.love >= LauraX.obedience:

                $ LauraX.change_face("_sly",1)
                if "mono" not in LauraX.daily_history:
                    $ LauraX.change_stat("love", 90, 1)
                ch_l "I didn't take you for the jealous type."
                ch_l "Fine, no side pussy. . ."
            elif approval_check(LauraX, 700, "O", TabM=0):

                $ LauraX.change_face("_sly",1,Eyes="_side")
                ch_l "Affirmative."
            else:

                $ LauraX.change_face("_sly",1)
                ch_l "Oh, you wouldn't want to see me when I'm thirsty."
                return
            if "mono" not in LauraX.daily_history:
                $ LauraX.change_stat("obedience", 90, 3)
            $ LauraX.add_word(1,0,"mono")
            $ LauraX.traits.append("mono")
        "Don't hook up with other girls." if "mono" not in LauraX.traits:
            if approval_check(LauraX, 900, "O", TabM=0):

                $ LauraX.change_face("_sly",1,Eyes="_side")
                ch_l "Ok."
            elif LauraX.Thirst >= 60 and not approval_check(LauraX, 1700, "LO", TabM=0):

                $ LauraX.change_face("_sly",1)
                if "mono" not in LauraX.daily_history:
                    $ LauraX.change_stat("obedience", 90, -2)
                ch_l "I would, but you aren't around enough. . ."
                return
            elif approval_check(LauraX, 600, "O", TabM=0):

                $ LauraX.change_face("_sly",1,Eyes="_side")
                ch_l "Hey, fine, your call."
            elif approval_check(LauraX, 1400, "LO", TabM=0):

                $ LauraX.change_face("_sly",1)
                ch_l "I wouldn't come at me like that, but fine."
            else:

                $ LauraX.change_face("_sly",1,Brows="_confused")
                ch_l "Oh, you wouldn't want to see me when I'm thirsty."
                return
            if "mono" not in LauraX.daily_history:
                $ LauraX.change_stat("obedience", 90, 3)
            $ LauraX.add_word(1,0,"mono")
            $ LauraX.traits.append("mono")
        "It's ok if you hook up with other girls." if "mono" in LauraX.traits:
            if approval_check(LauraX, 700, "O", TabM=0):
                $ LauraX.change_face("_sly",1,Eyes="_side")
                ch_l "Affirmative."
            elif approval_check(LauraX, 800, "L", TabM=0):
                $ LauraX.change_face("_sly",1)
                ch_l "You'd better not leave me hangin. . ."
            else:
                $ LauraX.change_face("_sly",1,Brows="_confused")
                if "mono" not in LauraX.daily_history:
                    $ LauraX.change_stat("love", 90, -2)
                ch_l "Well call out the ladies, I've just been given permission!"
            if "mono" not in LauraX.daily_history:
                $ LauraX.change_stat("obedience", 90, 3)
            if "mono" in LauraX.traits:
                $ LauraX.traits.remove("mono")
            $ LauraX.add_word(1,0,"mono")
        "Never mind.":
            pass
    return



label Laura_Jumped:

    ch_p "Hey, Remember that time you threw yourself at me?"
    $ LauraX.change_face("_sly",1,Brows="_confused")
    menu:
        ch_l "Yeah?"
        "Could you maybe just ask instead?" if "chill" not in LauraX.traits:
            if LauraX.Thirst >= 60 and not approval_check(LauraX, 1500, "LO", TabM=0):

                $ LauraX.change_face("_sly",1)
                if "chill" not in LauraX.daily_history:
                    $ LauraX.change_stat("obedience", 90, -2)
                ch_l "Not if you're going to keep dodging me. . ."
                return
            elif approval_check(LauraX, 1000, "LO", TabM=0) and LauraX.love >= LauraX.obedience:

                $ LauraX.change_face("_surprised",1)
                if "chill" not in LauraX.daily_history:
                    $ LauraX.change_stat("love", 90, 1)
                ch_l "Sorry, I was just horny. . ."
                $ LauraX.change_face("_sly",1,Eyes="_side")
                ch_l "I'll try to hold back. . ."
            elif approval_check(LauraX, 500, "O", TabM=0):

                $ LauraX.change_face("_sly",1,Eyes="_side")
                ch_l "Sorry. . ."
            else:

                $ LauraX.change_face("_sly",1)
                ch_l "Only if I can't find you."
                return
            if "chill" not in LauraX.daily_history:
                $ LauraX.change_stat("obedience", 90, 3)
            $ LauraX.add_word(1,0,"chill")
            $ LauraX.traits.append("chill")
        "Don't bother me like that." if "chill" not in LauraX.traits:
            if approval_check(LauraX, 800, "O", TabM=0):

                $ LauraX.change_face("_sly",1,Eyes="_side")
                ch_l "Ok."
            elif LauraX.Thirst >= 60 and not approval_check(LauraX, 500, "O", TabM=0):

                $ LauraX.change_face("_sly",1)
                if "chill" not in LauraX.daily_history:
                    $ LauraX.change_stat("obedience", 90, -2)
                ch_l "Then don't keep dodging me. . ."
                return
            elif approval_check(LauraX, 400, "O", TabM=0):

                $ LauraX.change_face("_sly",1,Eyes="_side")
                ch_l "Affirmative. . ."
            elif approval_check(LauraX, 500, "LO", TabM=0) and not approval_check(LauraX, 500, "I", TabM=0):

                $ LauraX.change_face("_sly",1)
                ch_l "Don't boss me around like that."
                ch_l "Still, I'll try to control myself. . ."
            else:

                $ LauraX.change_face("_sly",1)
                ch_l "Only if I can't find you."
                return
            if "chill" not in LauraX.daily_history:
                $ LauraX.change_stat("obedience", 90, 3)
            $ LauraX.add_word(1,0,"chill")
            $ LauraX.traits.append("chill")
        "Knock yourself out.":
            if approval_check(LauraX, 800, "L", TabM=0):
                $ LauraX.change_face("_sly",1)
                ch_l "Oh, I think we'll both enjoy that. . ."
            elif approval_check(LauraX, 700, "O", TabM=0):
                $ LauraX.change_face("_sly",1,Eyes="_side")
                ch_l "Oh yes sir."
            else:
                $ LauraX.change_face("_sly",1,Brows="_confused")
                if "chill" not in LauraX.daily_history:
                    $ LauraX.change_stat("love", 90, -2)
                ch_l "If I'm horny, sure."
            if "chill" not in LauraX.daily_history:
                $ LauraX.change_stat("obedience", 90, 3)
            if "chill" in LauraX.traits:
                $ LauraX.traits.remove("chill")
            $ LauraX.add_word(1,0,"chill")
        "Um, never mind.":
            pass
    return




label Laura_Hungry:
    if LauraX.Chat[3]:
        ch_l "[[licks her lips] I'm a little thirsty. . ."
    elif LauraX.Chat[2]:
        ch_l "I really enjoy that serum you whipped up."
    else:
        ch_l "[[licks her lips] I'm a little thirsty. . ."
    $ LauraX.traits.append("hungry")
return





label Laura_SexChat:
    $ Line = "Yeah, what did you want to talk about?" if not Line else Line
    while True:
        menu:
            ch_l "[Line]"
            "My favorite thing to do is. . .":
                if "setfav" in LauraX.daily_history:
                    ch_l "I remember."
                else:
                    menu:
                        "Sex.":
                            $ LauraX.change_face("_sly")
                            if LauraX.player_favorite_action == "sex":
                                $ LauraX.change_stat("lust", 80, 5)
                                ch_l "Yeah, I know that. . ."
                            elif LauraX.favorite_action == "sex":
                                $ LauraX.change_stat("love", 90, 5)
                                $ LauraX.change_stat("lust", 80, 10)
                                ch_l "I really like it too!"
                            elif LauraX.action_counter["sex"] >= 5:
                                ch_l "Well I don't mind that."
                            elif not LauraX.action_counter["sex"]:
                                $ LauraX.change_face("_perplexed")
                                ch_l "Who's fucking you?"
                            else:
                                $ LauraX.change_face("_bemused")
                                ch_l "Heh, um, yeah, it's nice. . ."
                            $ LauraX.player_favorite_action = "sex"
                        "Anal.":

                            $ LauraX.change_face("_sly")
                            if LauraX.player_favorite_action == "anal":
                                $ LauraX.change_stat("lust", 80, 5)
                                ch_l "So you've said. . ."
                            elif LauraX.favorite_action == "anal":
                                $ LauraX.change_stat("love", 90, 5)
                                $ LauraX.change_stat("lust", 80, 10)
                                ch_l "I love it too!"
                            elif LauraX.action_counter["anal"] >= 10:
                                ch_l "Yeah, it's. . . nice. . ."
                            elif not LauraX.action_counter["anal"]:
                                $ LauraX.change_face("_perplexed")
                                ch_l "Who's fucking you?"
                            else:
                                $ LauraX.change_face("_bemused",Eyes="_side")
                                ch_l "Heh, heh, yeah, um, it's ok. . ."
                            $ LauraX.player_favorite_action = "anal"
                        "Blowjobs.":

                            $ LauraX.change_face("_sly")
                            if LauraX.player_favorite_action == "blowjob":
                                $ LauraX.change_stat("lust", 80, 3)
                                ch_l "Yeah, I know."
                            elif LauraX.favorite_action == "blowjob":
                                $ LauraX.change_stat("love", 90, 5)
                                $ LauraX.change_stat("lust", 80, 5)
                                ch_l "I love your dick!"
                            elif LauraX.action_counter["blowjob"] >= 10:
                                ch_l "Yeah, you're pretty tasty."
                            elif not LauraX.action_counter["blowjob"]:
                                $ LauraX.change_face("_perplexed")
                                ch_l "Who's sucking your dick?!"
                            else:
                                $ LauraX.change_face("_bemused")
                                ch_l "I'm. . . getting used to the taste. . ."
                            $ LauraX.player_favorite_action = "blowjob"
                        "Titjobs.":

                            $ LauraX.change_face("_sly")
                            if LauraX.player_favorite_action == "titjob":
                                $ LauraX.change_stat("lust", 80, 5)
                                ch_l "Yeah, you've said that before. . ."
                            elif LauraX.favorite_action == "titjob":
                                $ LauraX.change_stat("love", 90, 5)
                                $ LauraX.change_stat("lust", 80, 7)
                                ch_l "Yeah, I enjoy that too. . ."
                            elif LauraX.action_counter["titjob"] >= 10:
                                ch_l "It's certainly an interesting experience . . ."
                            elif not LauraX.action_counter["titjob"]:
                                $ LauraX.change_face("_perplexed")
                                ch_l "Who's titfucking you?"
                            else:
                                $ LauraX.change_face("_bemused")
                                ch_l "That's nice of you to say. . ."
                                $ LauraX.change_stat("love", 80, 5)
                                $ LauraX.change_stat("inhibition", 50, 10)
                            $ LauraX.player_favorite_action = "titjob"
                        "Footjobs.":

                            $ LauraX.change_face("_sly")
                            if LauraX.player_favorite_action == "foot":
                                $ LauraX.change_stat("lust", 80, 5)
                                ch_l "Yeah, you've said that. . ."
                            elif LauraX.favorite_action == "foot":
                                $ LauraX.change_stat("love", 90, 5)
                                $ LauraX.change_stat("lust", 80, 7)
                                ch_l "I do like using my feet. . ."
                            elif LauraX.action_counter["footjob"] >= 10:
                                ch_l "I like it too . . ."
                            elif not LauraX.action_counter["footjob"]:
                                $ LauraX.change_face("_perplexed")
                                ch_l "Who's playing footsie with you?"
                            else:
                                $ LauraX.change_face("_bemused")
                                ch_l "Yeah, it's nice. . ."
                            $ LauraX.player_favorite_action = "foot"
                        "Handjobs.":

                            $ LauraX.change_face("_sly")
                            if LauraX.player_favorite_action == "handjob":
                                $ LauraX.change_stat("lust", 80, 5)
                                ch_l "Yeah, you've said that. . ."
                            elif LauraX.favorite_action == "handjob":
                                $ LauraX.change_stat("love", 90, 5)
                                $ LauraX.change_stat("lust", 80, 7)
                                ch_l "You do feel pretty comfy. . ."
                            elif LauraX.action_counter["handjob"] >= 10:
                                ch_l "I like it too . . ."
                            elif not LauraX.action_counter["handjob"]:
                                $ LauraX.change_face("_perplexed")
                                ch_l "Who's jerking you off?"
                            else:
                                $ LauraX.change_face("_bemused")
                                ch_l "Yeah, it's nice. . ."
                            $ LauraX.player_favorite_action = "handjob"
                        "Feeling you up.":

                            $ counter = LauraX.action_counter["fondle_breasts"]+ LauraX.action_counter["fondle_thighs"]+ LauraX.action_counter["suck_breasts"] + LauraX.action_counter["hotdog"]
                            $ LauraX.change_face("_sly")
                            if LauraX.player_favorite_action == "fondle":
                                $ LauraX.change_stat("lust", 80, 3)
                                ch_l "Yeah, I think we're clear on that. . ."
                            elif LauraX.favorite_action in ("hotdog","suck_breasts","fondle_breasts","fondle_thighs"):
                                $ LauraX.change_stat("love", 90, 5)
                                $ LauraX.change_stat("lust", 80, 5)
                                ch_l "I love when you touch me. . ."
                            elif counter >= 10:
                                ch_l "Yeah, it's really nice . . ."
                            elif not counter:
                                $ LauraX.change_face("_perplexed")
                                ch_l "Who's letting you feel her up?"
                            else:
                                $ LauraX.change_face("_bemused")
                                ch_l "I do like how that feels. . ."
                            $ LauraX.player_favorite_action = "fondle"
                            $ counter = 0
                        "Kissing you.":

                            $ LauraX.change_face("_sly")
                            if LauraX.player_favorite_action == "kiss":
                                $ LauraX.change_stat("love", 90, 3)
                                ch_l "Such a romantic. . ."
                            elif LauraX.favorite_action == "kiss":
                                $ LauraX.change_stat("love", 90, 5)
                                $ LauraX.change_stat("lust", 80, 5)
                                ch_l "Hmm, the taste of you on my lips. . ."
                            elif LauraX.action_counter["kiss"] >= 10:
                                ch_l "I love kissing you too . . ."
                            elif not LauraX.action_counter["kiss"]:
                                $ LauraX.change_face("_perplexed")
                                ch_l "Who are you kissing?"
                            else:
                                $ LauraX.change_face("_bemused")
                                ch_l "I like kissing you too. . ."
                            $ LauraX.player_favorite_action = "kiss"

                    $ LauraX.daily_history.append("setfav")
            "What's your favorite thing to do?":

                if not approval_check(LauraX, 800):
                    $ LauraX.change_face("_perplexed")
                    ch_l ". . ."
                else:
                    if LauraX.SEXP >= 50:
                        $ LauraX.change_face("_sly")
                        ch_l "You should know. . ."
                    else:
                        $ LauraX.change_face("_bemused")
                        $ LauraX.eyes = "_side"
                        ch_l "Hmm. . ."


                    if not LauraX.favorite_action or LauraX.favorite_action == "kiss":
                        ch_l "Kissing?"
                    elif LauraX.favorite_action == "anal":
                        ch_l "Probably anal."
                    elif LauraX.favorite_action == "eat_ass":
                        ch_l "When you lick my ass."
                    elif LauraX.favorite_action == "finger_ass":
                        ch_l "Fingering my asshole, probably."
                    elif LauraX.favorite_action == "sex":
                        ch_l "Just the usual pounding."
                    elif LauraX.favorite_action == "eat_pussy":
                        ch_l "When you lick my pussy."
                    elif LauraX.favorite_action == "fondle_pussy":
                        ch_l "When you finger me."
                    elif LauraX.favorite_action == "blowjob":
                        ch_l "I like how your cock tastes."
                    elif LauraX.favorite_action == "titjob":
                        ch_l "When I use my tits."
                    elif LauraX.favorite_action == "foot":
                        ch_l "Footjobs are pretty fun."
                    elif LauraX.favorite_action == "handjob":
                        ch_l "I like jerking you off."
                    elif LauraX.favorite_action == "hotdog":
                        ch_l "When you grind against me."
                    elif LauraX.favorite_action == "suck_breasts":
                        ch_l "When you suck my tits."
                    elif LauraX.favorite_action == "fondle_breasts":
                        ch_l "When you grab my tits."
                    elif LauraX.favorite_action == "fondle_thighs":
                        ch_l "When you rub my thighs."
                    else:
                        ch_l "How should I know?"



            "Don't talk as much during sex." if "vocal" in LauraX.traits:
                if "setvocal" in LauraX.daily_history:
                    $ LauraX.change_face("_perplexed")
                    ch_l "Make up your mind."
                else:
                    if approval_check(LauraX, 1000) and LauraX.obedience <= LauraX.love:
                        $ LauraX.change_face("_bemused")
                        $ LauraX.change_stat("obedience", 90, 1)
                        ch_l "Stay quiet, got it."
                        $ LauraX.traits.remove("vocal")
                    elif approval_check(LauraX, 700, "O"):
                        $ LauraX.change_face("_sadside")
                        $ LauraX.change_stat("obedience", 90, 1)
                        ch_l ". . ."
                        $ LauraX.traits.remove("vocal")
                    elif approval_check(LauraX, 600):
                        $ LauraX.change_face("_sly")
                        $ LauraX.change_stat("love", 90, -3)
                        $ LauraX.change_stat("obedience", 50, -1)
                        $ LauraX.change_stat("inhibition", 90, 5)
                        ch_l "Don't push it, [LauraX.player_petname]."
                    else:
                        $ LauraX.change_face("_angry")
                        $ LauraX.change_stat("love", 90, -5)
                        $ LauraX.change_stat("obedience", 60, -3)
                        $ LauraX.change_stat("inhibition", 90, 10)
                        ch_l "I don't take orders from you, [LauraX.player_petname]."

                    $ LauraX.daily_history.append("setvocal")
            "Talk dirty to me during sex." if "vocal" not in LauraX.traits:
                if "setvocal" in LauraX.daily_history:
                    $ LauraX.change_face("_perplexed")
                    ch_l "I heard you the first time."
                else:
                    if approval_check(LauraX, 1000) and LauraX.obedience <= LauraX.love:
                        $ LauraX.change_face("_sly")
                        $ LauraX.change_stat("obedience", 90, 2)
                        ch_l "Louder? Ok. . ."
                        $ LauraX.traits.append("vocal")
                    elif approval_check(LauraX, 700, "O"):
                        $ LauraX.change_face("_sadside")
                        $ LauraX.change_stat("obedience", 90, 2)
                        ch_l "If you want, [LauraX.player_petname]."
                        $ LauraX.traits.append("vocal")
                    elif approval_check(LauraX, 600):
                        $ LauraX.change_face("_sly")
                        $ LauraX.change_stat("obedience", 90, 3)
                        ch_l "I guess?"
                        $ LauraX.traits.append("vocal")
                    else:
                        $ LauraX.change_face("_angry")
                        $ LauraX.change_stat("inhibition", 90, 5)
                        ch_l ". . ."

                    $ LauraX.daily_history.append("setvocal")


            "Don't do your own thing as much during sex." if "passive" not in LauraX.traits:
                if "initiative" in LauraX.daily_history:
                    $ LauraX.change_face("_perplexed")
                    ch_l "I heard you the first time."
                else:
                    if approval_check(LauraX, 1200) and LauraX.obedience <= LauraX.love:
                        $ LauraX.change_face("_bemused")
                        $ LauraX.change_stat("obedience", 90, 1)
                        ch_l "Passive, eh?"
                        $ LauraX.traits.append("passive")
                    elif approval_check(LauraX, 700, "O"):
                        $ LauraX.change_face("_sadside")
                        $ LauraX.change_stat("obedience", 90, 1)
                        ch_l "I'll try to hold back."
                        $ LauraX.traits.append("passive")
                    elif approval_check(LauraX, 600):
                        $ LauraX.change_face("_sly")
                        $ LauraX.change_stat("love", 90, -3)
                        $ LauraX.change_stat("obedience", 50, -1)
                        $ LauraX.change_stat("inhibition", 90, 5)
                        ch_l "Hm, no."
                    else:
                        $ LauraX.change_face("_angry")
                        $ LauraX.change_stat("love", 90, -5)
                        $ LauraX.change_stat("obedience", 60, -3)
                        $ LauraX.change_stat("inhibition", 90, 10)
                        ch_l "We'll see."

                    $ LauraX.daily_history.append("initiative")
            "Take more initiative during sex." if "passive" in LauraX.traits:
                if "initiative" in LauraX.daily_history:
                    $ LauraX.change_face("_perplexed")
                    ch_l "I heard you the first time."
                else:
                    if approval_check(LauraX, 1000) and LauraX.obedience <= LauraX.love:
                        $ LauraX.change_face("_bemused")
                        $ LauraX.change_stat("obedience", 90, 1)
                        ch_l "More active, got it."
                        $ LauraX.traits.remove("passive")
                    elif approval_check(LauraX, 700, "O"):
                        $ LauraX.change_face("_sadside")
                        $ LauraX.change_stat("obedience", 90, 1)
                        ch_l "If you insist."
                        $ LauraX.traits.remove("passive")
                    elif approval_check(LauraX, 600):
                        $ LauraX.change_face("_sly")
                        $ LauraX.change_stat("obedience", 90, 3)
                        ch_l "We'll see."
                        $ LauraX.traits.remove("passive")
                    else:
                        $ LauraX.change_face("_angry")
                        $ LauraX.change_stat("inhibition", 90, 5)
                        ch_l "Too much work."

                    $ LauraX.daily_history.append("initiative")

            "About getting Jumped" if "jumped" in LauraX.history:
                call Laura_Jumped
            "About when you masturbate":
                call NoFap (LauraX)

            "Never Mind" if Line == "Yeah, what did you want to talk about?":
                return
            "That's all." if Line != "Yeah, what did you want to talk about?":
                return
        if Line == "Yeah, what did you want to talk about?":
            $ Line = "Anything else?"
    return




label Laura_Chitchat(O=0, Options=["default","default","default"]):
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:
        $ Options = [O]
    else:

        if LauraX not in Digits:
            if approval_check(LauraX, 500, "L") or approval_check(LauraX, 250, "I"):
                ch_l "Oh, here's my number, in case you need back-up."
                $ Digits.append(LauraX)
                return
            elif approval_check(LauraX, 250, "O"):
                ch_l "If you need to contact me, here's my number."
                $ Digits.append(LauraX)
                return

        if "hungry" not in LauraX.traits and (LauraX.event_counter["swallowed"] + LauraX.Chat[2]) >= 10 and LauraX.location == bg_current:
            call Laura_Hungry
            return

        if "partyfoul" in LauraX.history and "partyfix" not in LauraX.history:
            call Laura_Foul
            return

        if bg_current != "bg_restaurant" and bg_current != "HW Party" and (not Taboo or approval_check(LauraX, 800, "I")):
            if LauraX.location == bg_current and LauraX.Thirst >= 30 and "refused" not in LauraX.daily_history and "quicksex" not in LauraX.daily_history:
                $ LauraX.change_face("_sly",1)
                ch_l "Hey, wanna bone?"
                call Quick_Sex (LauraX)
                return




        if LauraX.Event[0] and "key" not in LauraX.Chat:
            $ Options.append("key")

        if "mandrill" in Player.traits and "cologne chat" not in LauraX.daily_history:
            $ Options.append("mandrill")
        if "purple" in Player.traits and "cologne chat" not in LauraX.daily_history:
            $ Options.append("purple")
        if "corruption" in Player.traits and "cologne chat" not in LauraX.daily_history:
            $ Options.append("corruption")

        if "Laura" not in LauraX.names:
            $ Options.append("laura")

        if LauraX.Date >= 1 and bg_current != "bg_restaurant":

            $ Options.append("dated")



        if LauraX.action_counter["kiss"] >= 5:

            $ Options.append("kissed")
        if "dangerroom" in Player.daily_history:

            $ Options.append("dangerroom")
        if "showered" in LauraX.daily_history:

            $ Options.append("showercaught")
        if "fondle_breasts" in LauraX.daily_history or "fondle_pussy" in LauraX.daily_history or "fondle_ass" in LauraX.daily_history:

            $ Options.append("fondled")
        if "Dazzler and Longshot" in LauraX.inventory and "256 Shades of Grey" in LauraX.inventory and "Avengers Tower Penthouse" in LauraX.inventory:

            if "book" not in LauraX.Chat:
                $ Options.append("booked")
        if "lace_bra" in LauraX.inventory or "lace_panties" in LauraX.inventory:

            if "lingerie" not in LauraX.Chat:
                $ Options.append("lingerie")
        if LauraX.action_counter["handjob"]:

            $ Options.append("handy")
        if LauraX.event_counter["swallowed"]:

            $ Options.append("swallowed")
        if "cleaned" in LauraX.daily_history or "painted" in LauraX.daily_history:

            $ Options.append("facial")
        if LauraX.event_counter["sleepover"]:

            $ Options.append("sleep")
        if LauraX.event_counter["creampied"] or LauraX.event_counter["anal_creampied"]:

            $ Options.append("creampie")
        if LauraX.action_counter["sex"] or LauraX.action_counter["anal"]:

            $ Options.append("sexed")
        if LauraX.action_counter["anal"]:

            $ Options.append("anal")

        if "seenpeen" in LauraX.history:
            $ Options.append("seenpeen")
        if "topless" in LauraX.history:
            $ Options.append("topless")
        if "bottomless" in LauraX.history:
            $ Options.append("bottomless")



















        if not approval_check(LauraX, 300):
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)

    if Options[0] == "mandrill":
        $ LauraX.daily_history.append("cologne chat")
        $ LauraX.change_face("_confused")
        ch_l "(sniff, sniff). . . smells like. . . ape . . ."
        $ LauraX.change_face("_sexy", 2)
        ch_l ". . . did you want to do something later?"
    elif Options[0] == "purple":
        $ LauraX.daily_history.append("cologne chat")
        $ LauraX.change_face("_sly",1)
        ch_l "(sniff, sniff). . . what is that? . ."
        $ LauraX.change_face("_normal",0)
        ch_l ". . . what was it you wanted?"
    elif Options[0] == "corruption":
        $ LauraX.daily_history.append("cologne chat")
        $ LauraX.change_face("_confused")
        ch_l "(sniff, sniff). . . that's a strong scent. . ."
        $ LauraX.change_face("_angry")
        ch_l ". . . a dangerous scent. . ."
        $ LauraX.change_face("_sly")

    elif Options[0] == "caught":
        if "caught chat" in LauraX.Chat:
            ch_l "We should be more careful about getting caught."
            if not approval_check(LauraX, 500, "I"):
                ch_l "Unless. . ."
        else:
            ch_l "Sorry we got dragged into the Professor's office like that."
            if not approval_check(LauraX, 500, "I"):
                ch_l "I guess you wouldn't want to get it on in public anymore."
            else:
                ch_l "I kind of enjoyed it though. . ."
            $ LauraX.Chat.append("caught chat")
    elif Options[0] == "key":
        if LauraX.SEXP <= 15:
            ch_l "I gave you the key for convenience, don't abuse it . ."
        else:
            ch_l "I gave you a key, but you don't visit. . ."
        $ LauraX.Chat.append("key")










    elif Options[0] == "laura":

        ch_l "Oh, by the way, I also go by \"Laura.\" Laura Kinney."
        $ LauraX.names.append("Laura")
        menu:
            "Oh, that's nice, I think I'll call you that.":
                $ LauraX.change_stat("love", 70, 5)
                $ LauraX.name = "Laura"
            "Ok, but X-23 sounds cooler.":
                $ LauraX.change_stat("love", 70, -2)
                $ LauraX.change_stat("obedience", 70, 5)
                $ LauraX.name = "X-23"

    elif Options[0] == "dated":

        ch_l "That was fun last night, we should do that again some time."

    elif Options[0] == "kissed":

        $ LauraX.change_face("_normal",1)
        ch_l "You're pretty good at kissing, [LauraX.player_petname]."
        menu:
            extend ""
            "Hey. . .I'm the best there is at what I do.":
                $ LauraX.change_face("_smile",1)
                ch_l "You'll have to back that claim up."
            "No. You think?":
                ch_l "Do I look like a kidder?"

    elif Options[0] == "dangerroom":

        $ LauraX.change_face("_sly",1)
        ch_l "Hey,[LauraX.player_petname]. I saw you in the Danger Room, earlier."
        ch_l "You should probably keep your left up, you were taking too many shots to the head."

    elif Options[0] == "showercaught":

        if "shower" in LauraX.Chat:
            ch_l "You saw me taking a shower again. . ."
        else:
            ch_l "Do you make a habit of bursting into the showers?"
            $ LauraX.Chat.append("shower")
            menu:
                extend ""
                "It was a total accident! I promise!":
                    $ LauraX.change_stat("love", 50, 5)
                    $ LauraX.change_stat("love", 90, 2)
                    if approval_check(LauraX, 1200):
                        $ LauraX.change_face("_sly",1)
                        ch_l "I didn't mind."
                    $ LauraX.change_face("_smile")
                    ch_l "We all make mistakes."
                "Just with you.":
                    $ LauraX.change_stat("obedience", 40, 5)
                    if approval_check(LauraX, 1000) or approval_check(LauraX, 700, "L"):
                        $ LauraX.change_stat("love", 90, 3)
                        $ LauraX.change_face("_sly",1)
                        ch_l "Hmm, I guess that's a compliment."
                    else:
                        $ LauraX.change_stat("love", 70, -5)
                        $ LauraX.change_face("_angry")
                        ch_l "I think I should be insulted."
                "Totally on purpose. I regret nothing.":
                    if approval_check(LauraX, 1200):
                        $ LauraX.change_stat("love", 90, 3)
                        $ LauraX.change_stat("obedience", 70, 10)
                        $ LauraX.change_stat("inhibition", 50, 5)
                        $ LauraX.change_face("_sly",1)
                        ch_l "You seem to know what you want."
                    elif approval_check(LauraX, 800):
                        $ LauraX.change_stat("obedience", 60, 5)
                        $ LauraX.change_stat("inhibition", 50, 5)
                        $ LauraX.change_face("_perplexed",2)
                        ch_l "I guess you show initiative."
                        $ LauraX.blushing = "_blush1"
                    else:
                        $ LauraX.change_stat("love", 50, -10)
                        $ LauraX.change_stat("love", 80, -10)
                        $ LauraX.change_stat("obedience", 50, 10)
                        $ LauraX.change_face("_angry")
                        ch_l "That's a bit disturbing."

    elif Options[0] == "fondled":

        if LauraX.action_counter["fondle_breasts"]+ LauraX.action_counter["fondle_pussy"] + LauraX.action_counter["fondle_ass"] >= 15:
            ch_l "I need your hands on me."
        else:
            ch_l "You could feel me up, if you wanted."

    elif Options[0] == "booked":

        ch_l "Hey, I read those books you gave me."
        menu:
            extend ""
            "Yeah? Did you like them?":
                $ LauraX.change_face("_sly",2)
                ch_l "They were. . .{i}interesting{/i}."
            "Good. You looked like you could use to learn a thing or two from them.":
                $ LauraX.change_stat("love", 90, -3)
                $ LauraX.change_stat("obedience", 70, 5)
                $ LauraX.change_stat("inhibition", 50, 5)
                $ LauraX.change_face("_angry")
                ch_l "I don't see how."
        $ LauraX.blushing = "_blush1"
        $ LauraX.Chat.append("book")

    elif Options[0] == "lingerie":

        $ LauraX.change_face("_sly",2)
        ch_l "That underwear you got me was kind of uncomfortable, but I do like the look."
        $ LauraX.blushing = "_blush1"
        $ LauraX.Chat.append("lingerie")

    elif Options[0] == "handy":

        $ LauraX.change_face("_sly",1)
        ch_l "I was thinking about having your cock in my hand the other day. . ."
        ch_l "You seemed to enjoy it."
        $ LauraX.blushing = ""

    elif Options[0] == "blowjob":
        if "blowjob" not in LauraX.Chat:

            $ LauraX.change_face("_sly",2)
            ch_l "Hey, so did you like that blowjob?"
            menu:
                extend ""
                "You were totally amazing.":
                    $ LauraX.change_stat("love", 90, 5)
                    $ LauraX.change_stat("inhibition", 60, 10)
                    $ LauraX.change_face("_normal",1)
                    ch_l "Cool. Cool. . . "
                    $ LauraX.change_face("_sexy",1)
                    ch_l "I'd like another taste sometime."
                "Honestly? It was good. . .but you could use a little practice, I think.":
                    if approval_check(LauraX, 300, "I") or not approval_check(LauraX, 800):
                        $ LauraX.change_stat("love", 90, -5)
                        $ LauraX.change_stat("obedience", 60, 10)
                        $ LauraX.change_stat("inhibition", 50, 10)
                        $ LauraX.change_face("_perplexed",1)
                        ch_l "Yeah? Sorry to disappoint."
                    else:
                        $ LauraX.change_stat("obedience", 70, 15)
                        $ LauraX.change_stat("inhibition", 50, 5)
                        $ LauraX.change_face("_sexy",1)
                        ch_l "Yeah? I suppose we could keep trying until I get it right."
                "I guess. If you're into weird sounds and too much teeth. Spoiler, I'm not.":
                    $ LauraX.change_stat("love", 90, -10)
                    $ LauraX.change_stat("obedience", 60, 10)
                    $ LauraX.change_face("_angry",2)
                    ch_l "Well, good luck with that then."
            $ LauraX.blushing = "_blush1"
            $ LauraX.Chat.append("blowjob")
        else:
            $ Line = renpy.random.choice(["I gotta tell you, your dick tastes great.", 
                            "I think I nearly dislocated my jaw last time.", 
                            "Let me know if you'd like another blowjob sometime.",
                            "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
            ch_l "[Line]"

    elif Options[0] == "swallowed":

        if "swallow" in LauraX.Chat:
            ch_l "Hey, I wouldn't mind another taste of you some time."
        else:
            ch_l "So. . . the other day. . ."
            ch_l "That was the first time I'd really enjoyed the taste of jiz."
            $ LauraX.change_face("_sly",1)
            ch_l "Good job!"
            $ LauraX.Chat.append("swallow")

    elif Options[0] == "facial":

        ch_l "Hey. . .I know this is kind of odd. . ."
        $ LauraX.change_face("_sexy",2)
        ch_l "I feel so {i}good{/i} with your jiz on my face."
        $ LauraX.blushing = "_blush1"

    elif Options[0] == "sleepover":

        ch_l "I really enjoyed the other night."
        ch_l "It felt so safe sleeping next to someone else."

    elif Options[0] == "creampie":

        "[LauraX.name] draws close to you so she can whisper into your ear."
        ch_l "I can still feel you. . .running down the inside of my thigh."

    elif Options[0] == "sexed":

        ch_l "So. . . you should know. . ."
        $ LauraX.change_face("_sexy",2)
        ch_l ". . .lately when I've been flicking the bean. . ."
        ch_l "I've been thinking about you inside of me."
        $ LauraX.blushing = "_blush1"

    elif Options[0] == "anal":

        $ LauraX.change_face("_sly")
        ch_l "I did't really enjoy anal much."
        $ LauraX.change_face("_sexy",1)
        ch_l "Until you, at least."

    elif Options[0] == "seenpeen":
        $ LauraX.change_face("_sly",1, Eyes="_down")
        ch_l "I forgot to tell you, you've got a pretty nice cock down there. . ."
        $ LauraX.change_face("_bemused",1)
        $ LauraX.change_stat("love", 50, 5)
        $ LauraX.history.remove("seenpeen")
    elif Options[0] == "topless":
        ch_l "Hey,what'd you think of my tits?"
        ch_l "Did you like what you saw?"
        call Laura_First_TMenu
        $ LauraX.history.remove("topless")
    elif Options[0] == "bottomless":
        ch_l "Hey, what'd you think when you saw my pussy earlier?"
        call Laura_First_BMenu
        $ LauraX.history.remove("bottomless")
















    elif Options[0] == "hate":
        $ Line = renpy.random.choice(["Get away from me.", 
                "I don't want to smell you near me.", 
                "Back off.",
                "Buzz off."])
        ch_l "[Line]"
    else:

        $ D20 = renpy.random.randint(1, 21)
        if D20 == 1:
            $ LauraX.change_face("_smile")
            ch_l "I got a good grade on that bio test."
        elif D20 == 2:
            $ LauraX.change_face("annoyed")
            ch_l "If I have to hear him say \"I'm the best there is\" one more time, I swear I'm going .."
        elif D20 == 3:
            $ LauraX.change_face("_surprised")
            ch_l "Huh? Oh, sorry. I sort of spaced out. That's not like me."
        elif D20 == 4:
            $ LauraX.change_face("_sad")
            ch_l "Oh, [LauraX.player_petname]. I was just remembering something. Don't worry about it."
        elif D20 == 5:
            $ LauraX.change_face("_smile")
            ch_l "I had a good nap. It's nice to be somewhere I can just doze off without worry."
        elif D20 == 6:
            $ LauraX.change_face("_perplexed")
            ch_l "Oh, [LauraX.player_petname]. I think I just saw Emma Frost staring at Cyclops. That's.. wierd."
        elif D20 == 7:
            $ LauraX.change_face("_smile")
            ch_l "I just got a new personal best time in the Danger Room."
        elif D20 == 8:
            $ LauraX.change_face("_sad")
            ch_l "I like being here, but sometimes there's just so much noise.."
        elif D20 == 9:
            $ LauraX.change_face("_confused")
            ch_l "I'm still trying to figure out what the mystery meat in the cafeteria was today."
            ch_l "I have enhanced senses, this shouldn't be so difficult!"
        elif D20 == 10:
            $ LauraX.change_face("_smile")
            ch_l "Kitty, Rogue and some of the others asked me if I wanted to go grab some ice cream with them tomorrow."
        elif D20 == 11:
            $ LauraX.change_face("_smile")
            ch_l "I tried out a dance class like Kitty said. Apparently I'm good at it."
        elif D20 == 12:
            $ LauraX.change_face("_sad")
            ch_l "I like talking to Kitty and the others. It makes me feel, I don't know. . ."
            ch_l "{i}not{/i} like a really dangerous mutant who could kill everyone around me if I flipped out."
        elif D20 == 13:
            $ LauraX.change_face("_smile")
            ch_l "Kitty and Rogue dared me to call Logan \"Dad\". I think we might've given him a heart attack."
        elif D20 == 14:
            $ LauraX.change_face("_sad")
            ch_l "I like going out on missions, but catching up with what's been going on while I'm gone is always a pain."
        elif D20 == 15:
            $ LauraX.change_face("_perplexed")
            ch_l "So they're called the \"Avengers\", but do they ever do any avenging?"
            ch_l "At least the Fantastic Four really do things that are strange and fantastic."
        elif D20 == 16:
            $ LauraX.change_face("_perplexed")
            ch_l "Have you ever been to New York? Sometimes I'm surprised anyone still wants to live there."
        elif D20 == 17:
            $ LauraX.change_face("_perplexed")
            ch_l "Logan just walked up and told me that if I ever meet someone called. . ."
            ch_l "\"Dead..Poole?\"..I should just go ahead and stab him in the face."
            ch_l "What's up with that?"
        elif D20 == 18:
            $ LauraX.change_face("_smile")
            ch_l "Don't tell anyone this, but I think Cyclops is kind of wound up tight."
        elif D20 == 19:
            $ LauraX.change_face("_confused")
            ch_l "Do you smell something? Is that.. nachos and.. chocolate syrup?!"
        elif D20 == 20:
            $ LauraX.change_face("_smile")
            ch_l "I like being able to just talk about nothing in particular. It's.. nice."
        else:
            $ LauraX.change_face("_smile")
            ch_l "You're fun to hang with."

    $ Line = 0
    return


label Laura_names:
    menu:
        ch_l "Oh? What would you like me to call you?"
        "My initial's fine.":
            $ LauraX.player_petname = Player.name[:1]
            ch_l "You got it, [LauraX.player_petname]."
        "Call me by my name.":
            $ LauraX.player_petname = Player.name
            ch_l "If you'd rather, [LauraX.player_petname]."
        "Call me \"boyfriend\"." if "boyfriend" in LauraX.player_petnames:
            $ LauraX.player_petname = "boyfriend"
            ch_l "Sure thing, [LauraX.player_petname]."
        "Call me \"lover\"." if "lover" in LauraX.player_petnames:
            $ LauraX.player_petname = "lover"
            ch_l "Oooh, love to, [LauraX.player_petname]."
        "Call me \"sir\"." if "sir" in LauraX.player_petnames:
            $ LauraX.player_petname = "sir"
            ch_l "Yes, [LauraX.player_petname]."
        "Call me \"master\"." if "master" in LauraX.player_petnames:
            $ LauraX.player_petname = "master"
            ch_l "As you wish, [LauraX.player_petname]."
        "Call me \"sex friend\"." if "sex friend" in LauraX.player_petnames:
            $ LauraX.player_petname = "sex friend"
            ch_l "Heh, very cheeky, [LauraX.player_petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in LauraX.player_petnames:
            $ LauraX.player_petname = "fuck buddy"
            ch_l "I'm game if you are, [LauraX.player_petname]."
        "Call me \"daddy\"." if "daddy" in LauraX.player_petnames:
            $ LauraX.player_petname = "daddy"
            ch_l "Oh! You bet, [LauraX.player_petname]."
        "Bub works.":
            $ LauraX.player_petname = "bub"
            ch_l "You got it, bub."
        "Nevermind.":
            return
    return


label Laura_Pet:
    while 1:
        menu:
            extend ""
            "Polite":
                menu:
                    "I think I'll call you. . ."
                    "Laura.":
                        $ LauraX.petname = "Laura"
                        ch_l "I don't see why not, [LauraX.player_petname]."
                    "X-23.":

                        $ LauraX.petname = "X-23"
                        if approval_check(LauraX, 700, "L") and not approval_check(LauraX, 500, "O"):
                            ch_l "Oh, if you say so, [LauraX.player_petname]."
                        else:
                            ch_l "I don't see why not, [LauraX.player_petname]."
                    "\"girl\".":

                        $ LauraX.petname = "girl"
                        if "boyfriend" in LauraX.player_petnames or approval_check(LauraX, 600, "L"):
                            $ LauraX.change_face("_sexy", 1)
                            ch_l "I'm totally your girl, [LauraX.player_petname]."
                        else:
                            $ LauraX.change_face("_angry")
                            ch_l "I'm NOT your girl, [LauraX.player_petname]."
                    "\"boo\".":

                        $ LauraX.petname = "boo"
                        if "boyfriend" in LauraX.player_petnames or approval_check(LauraX, 700, "L"):
                            $ LauraX.change_face("_sexy", 1)
                            ch_l "I am your boo, [LauraX.player_petname]."
                        else:
                            $ LauraX.change_face("_angry")
                            ch_l "I'm NOT your boo, [LauraX.player_petname]."
                    "\"bae\".":

                        $ LauraX.petname = "bae"
                        if "boyfriend" in LauraX.player_petnames or approval_check(LauraX, 600, "L"):
                            $ LauraX.change_face("_sexy", 1)
                            ch_l "I am your bae, [LauraX.player_petname]."
                        else:
                            $ LauraX.change_face("_angry")
                            ch_l "I'm NOT your bae, [LauraX.player_petname]."
                    "\"baby\".":

                        $ LauraX.petname = "baby"
                        if "boyfriend" in LauraX.player_petnames or approval_check(LauraX, 500, "L"):
                            $ LauraX.change_face("_sexy", 1)
                            ch_l "Cute, [LauraX.player_petname]."
                        else:
                            $ LauraX.change_face("_angry")
                            ch_l "I am not a baby."
                    "\"sweetie\".":


                        $ LauraX.petname = "sweetie"
                        if "boyfriend" in LauraX.player_petnames or approval_check(LauraX, 600, "L"):
                            ch_l "Aw, that's sweet, [LauraX.player_petname]."
                        else:
                            $ LauraX.change_face("_angry", 1)
                            ch_l "Too sweet, [LauraX.player_petname]."
                    "\"sexy\".":

                        $ LauraX.petname = "_sexy"
                        if "lover" in LauraX.player_petnames or approval_check(LauraX, 800):
                            $ LauraX.change_face("_sexy", 1)
                            ch_l "You know it, [LauraX.player_petname]."
                        else:
                            $ LauraX.change_face("_angry", 1)
                            ch_l "Pushing a line there, [LauraX.player_petname]."
                    "\"lover\".":

                        $ LauraX.petname = "lover"
                        if "lover" in LauraX.player_petnames or approval_check(LauraX, 1200):
                            $ LauraX.change_face("_sexy", 1)
                            ch_l "I know."
                        else:
                            $ LauraX.change_face("_angry", 1)
                            ch_l "I don't think so, [LauraX.player_petname]."
                    "\"Wolvie\".":

                        $ LauraX.petname = "Wolvie"
                        if approval_check(LauraX, 500, "I"):
                            $ LauraX.change_face("_sexy", 1)
                            ch_l "Heh, ok, [LauraX.player_petname]."
                        else:
                            $ LauraX.change_face("_angry")
                            ch_l "Not really that cute, [LauraX.player_petname]"
                    "Back":

                        pass
            "Risky":

                menu:
                    "I think I'll call you. . ."
                    "\"slave\".":
                        $ LauraX.petname = "slave"
                        if "master" in LauraX.player_petnames or approval_check(LauraX, 800, "O"):
                            $ LauraX.change_face("_bemused", 1)
                            ch_l "As you wish, [LauraX.player_petname]."
                        else:
                            $ LauraX.change_face("_angry", 1)
                            ch_l "I am not your slave, [LauraX.player_petname]."
                    "\"pet\".":

                        $ LauraX.petname = "pet"
                        if "master" in LauraX.player_petnames or approval_check(LauraX, 650, "O"):
                            $ LauraX.change_face("_bemused", 1)
                            ch_l "You can pet me if you want, [LauraX.player_petname]."
                        else:
                            $ LauraX.change_face("_angry", 1)
                            ch_l "I am no one's pet, [LauraX.player_petname]."
                    "\"slut\".":

                        $ LauraX.petname = "slut"
                        if "sex friend" in LauraX.player_petnames or approval_check(LauraX, 900, "OI"):
                            $ LauraX.change_face("_sexy")
                            ch_l "Fair enough."
                        else:
                            $ LauraX.change_face("_angry", 1)
                            $ LauraX.mouth = "_surprised"
                            ch_l "I'd like to see you try it with a busted jaw."
                    "\"whore\".":

                        $ LauraX.petname = "whore"
                        if "fuckbuddy" in LauraX.player_petnames or approval_check(LauraX, 1000, "OI"):
                            $ LauraX.change_face("_sly")
                            ch_l "I mean. . ."
                        else:
                            $ LauraX.change_face("_angry", 1)
                            ch_l "If either of us is going to be turning tricks. . ."
                    "\"sugartits\".":

                        $ LauraX.petname = "sugartits"
                        if "sex friend" in LauraX.player_petnames or approval_check(LauraX, 1400):
                            $ LauraX.change_face("_sly", 1)
                            ch_l "That doesn't even make sense."
                        else:
                            $ LauraX.change_face("_angry", 1)
                            ch_l "Not cool."
                    "\"sex friend\".":

                        $ LauraX.petname = "sex friend"
                        if "sex friend" in LauraX.player_petnames or approval_check(LauraX, 600, "I"):
                            $ LauraX.change_face("_sly")
                            ch_l "Yeah. . ."
                        else:
                            $ LauraX.change_face("_angry", 1)
                            ch_l "Keep it down, [LauraX.player_petname]."
                    "\"fuckbuddy\".":

                        $ LauraX.petname = "fuckbuddy"
                        if "fuckbuddy" in LauraX.player_petnames or approval_check(LauraX, 700, "I"):
                            $ LauraX.change_face("_sly")
                            ch_l "Yup."
                        else:
                            $ LauraX.change_face("_angry", 1)
                            $ LauraX.mouth = "_surprised"
                            ch_l "Don't even joke, [LauraX.player_petname]."
                    "\"baby girl\".":

                        $ LauraX.petname = "baby girl"
                        if "daddy" in LauraX.player_petnames or approval_check(LauraX, 1200):
                            $ LauraX.change_face("_smile", 1)
                            ch_l "I guess?"
                        else:
                            $ LauraX.change_face("_angry", 1)
                            ch_l "Weirdo."
                    "Back":

                        pass
            "Nevermind.":

                return
    return





label Laura_Rename:

    $ LauraX.mouth = "_smile"
    ch_l "Yeah?"
    menu:
        extend ""
        "I think \"Laura's\" a pretty name." if LauraX.name != "Laura" and "Laura" in LauraX.names:
            $ LauraX.name = "Laura"
            ch_l "Sounds good."
        "I thought \"X-23\" sounded cool." if LauraX.name != "X-23" and "X-23" in LauraX.names:
            if not approval_check(LauraX, 500, "O") and not approval_check(LauraX, 800, "L"):
                ch_l "I've put that name behind me, I'd rather not. . ."
            else:
                if not approval_check(LauraX, 500, "O"):
                    $ LauraX.change_face("_sadside", 0,Brows="_normal")
                if "namechange" not in LauraX.daily_history:
                    $ LauraX.change_stat("love", 70, -2)
                    $ LauraX.change_stat("obedience", 70, 5)
                $ LauraX.name = "X-23"
                ch_l "Oh, sure. . . I could go by that again. . ."
        "I liked the sound of \"Wolverine.\"" if LauraX.name != "Wolverine" and "Wolverine" in LauraX.names:
            $ LauraX.change_face("_confused", 1)
            if approval_check(LauraX, 500, "O") or approval_check(LauraX, 500, "I"):
                $ LauraX.name = "Wolverine"
                $ LauraX.change_face("_confused", 1)
                if "namechange" not in LauraX.daily_history:
                    $ LauraX.change_stat("obedience", 70, 2)
                    $ LauraX.change_stat("inhibition", 50, 2)
                ch_l "I guess I could give that one a go. . ."
            else:
                $ LauraX.blushing = "_blush2"
                ch_l "I. . . really don't think that would work for me. . ."
            $ LauraX.change_face()
        "Nevermind.":
            pass
    $ LauraX.add_word(1,0,"namechange")
    return




label Laura_Personality(counter=0):
    if not LauraX.Chat[4] or counter:
        "Since you're doing well in one area, you can convince Laura to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_l "Yeah? What's up?"
        "More Obedient. [[Love to Obedience]" if LauraX.love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_l "If you really care about that, sure."
            $ LauraX.Chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if LauraX.love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_l "I could always be a bit more wild if that's what you want."
            $ LauraX.Chat[4] = 2

        "Less Inhibited. [[Obedience to Inhibition]" if LauraX.obedience > 900:
            ch_p "I want you to be less inhibited."
            ch_l "I guess I could go all-out."
            $ LauraX.Chat[4] = 3
        "More Loving. [[Obedience to Love]" if LauraX.obedience > 900:
            ch_p "I'd like you to learn to love me."
            ch_l "I can try."
            $ LauraX.Chat[4] = 4

        "More Obedient. [[Inhibition to Obedience]" if LauraX.inhibition > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_l "I can give it a shot. . ."
            $ LauraX.Chat[4] = 5

        "More Loving. [[Inhibition to Love]" if LauraX.inhibition > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_l "If that's something you need out of this. . ."
            $ LauraX.Chat[4] = 6

        "I guess just do what you like. . .[[reset]" if LauraX.Chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_l "Um, ok."
            $ LauraX.Chat[4] = 0
        "Repeat the rules":
            call Laura_Personality (1)
            return
        "Nevermind.":
            return
    return







label Laura_Summon(approval_bonus=approval_bonus):
    $ LauraX.change_outfit()
    if "no_summon" in LauraX.recent_history:
        if "_angry" in LauraX.recent_history:
            ch_l "Grrrrrrrrr."
        elif LauraX.recent_history.count("no_summon") > 1:
            ch_l "Back off!"
            $ LauraX.recent_history.append("_angry")
        else:


            ch_l "Like I said, I'm busy."
        $ LauraX.recent_history.append("no_summon")
        return

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    if LauraX.location == "bg_classroom":
        $ approval_bonus = -10
    elif LauraX.location == "bg_dangerroom":
        $ approval_bonus = -10
    elif LauraX.location == "bg_showerroom":
        $ approval_bonus = -30

    if D20 <= 3:

        $ Line = "no"
    if time_index >= 3:
        if approval_check(LauraX, 500, "L") or approval_check(LauraX, 400, "O"):

            ch_l "You're up too? Sure, we can hang."
            $ LauraX.location = bg_current
            call set_the_scene
        else:

            ch_l "Nah."
            $ LauraX.recent_history.append("no_summon")
        return
    elif "les" in LauraX.recent_history:

        if approval_check(LauraX, 2000):
            ch_l "I'm kinda with a girl right now? Wanna come over?"
            menu:
                extend ""
                "Sure":
                    $ Line = "go to"
                "No thanks.":
                    ch_l "Heh, your call."
                    return
        else:
            ch_l "Oh, um, kinda busy here."
            ch_l "I'll see you later, eh?"
            $ LauraX.recent_history.append("no_summon")
            return
    elif not approval_check(LauraX, 700, "L") or not approval_check(LauraX, 600, "O"):

        if not approval_check(LauraX, 300):
            ch_l "I'm busy, [LauraX.player_petname]."
            $ LauraX.recent_history.append("no_summon")
            return


        if "summoned" in LauraX.recent_history:
            pass
        elif "goto" in LauraX.recent_history:
            ch_l "You were just over here."
        elif LauraX.location == "bg_classroom":
            ch_l "I'm in class, did you want to come too?"
        elif LauraX.location == "bg_dangerroom":
            ch_l "I'm in the Danger Room, [LauraX.player_petname], want in?"
        elif LauraX.location == "bg_campus":
            ch_l "I'm napping under a tree here, want to come?"
        elif LauraX.location == "bg_laura":
            ch_l "I'm in my room, [LauraX.player_petname], want to hang?"
        elif LauraX.location == "bg_player":
            ch_l "I'm in your room, [LauraX.player_petname], why aren't you?"
        elif LauraX.location == "bg_showerroom":
            if approval_check(LauraX, 1600):
                ch_l "I'm in the shower right now. Join me?"
            else:
                ch_l "I'm in the shower right now, [LauraX.player_petname]. We can connect later."
                $ LauraX.recent_history.append("no_summon")
                return
        elif LauraX.location == "hold":
            ch_l "I'm on task right now. Sorry?"
            $ LauraX.recent_history.append("no_summon")
            return
        else:
            ch_l "Why don't you come to me?"


        if "summoned" in LauraX.recent_history:
            ch_l "Again? Ok, fine."
            $ Line = "yes"
        elif "goto" in LauraX.recent_history:
            menu:
                extend ""
                "You're right, be right back.":
                    ch_l "See you when you get here."
                    $ Line = "go to"
                "Nah, it's better here.":
                    ch_l "If you say so."
                "But I'd {i}really{/i} like to see you over here.":
                    if approval_check(LauraX, 600, "L") or approval_check(LauraX, 1400):
                        $ Line = "lonely"
                    else:
                        $ Line = "no"
                "I said come over here.":
                    if approval_check(LauraX, 600, "O"):

                        $ Line = "command"
                    elif D20 >= 7 and approval_check(LauraX, 1400):

                        ch_l "Hmph."
                        $ Line = "yes"
                    elif approval_check(LauraX, 200, "O"):

                        ch_l "Whatever."
                        ch_l "I'll be here if you change your mind."
                    else:

                        $ Line = "no"
        else:
            menu:
                extend ""
                "Sure, I'll be right there.":
                    $ LauraX.change_stat("love", 55, 1)
                    $ LauraX.change_stat("inhibition", 30, 1)
                    ch_l "See you when you get here."
                    $ Line = "go to"
                "Nah, we can talk later.":

                    $ LauraX.change_stat("obedience", 50, 1)
                    $ LauraX.change_stat("obedience", 30, 2)
                    ch_l "Ok. Later then."
                "Could you please come visit me? I'm lonely.":

                    if approval_check(LauraX, 650, "L") or approval_check(LauraX, 1500):
                        $ LauraX.change_stat("love", 70, 1)
                        $ LauraX.change_stat("obedience", 50, 1)
                        $ Line = "lonely"
                    else:
                        $ LauraX.change_stat("inhibition", 30, 1)
                        $ Line = "no"
                        ch_l "Man, you are such a sap."
                "Come on, it'll be fun.":

                    if approval_check(LauraX, 400, "L") and approval_check(LauraX, 800):
                        $ LauraX.change_stat("love", 70, 1)
                        $ LauraX.change_stat("obedience", 50, 1)
                        $ Line = "fun"
                    else:
                        $ LauraX.change_stat("inhibition", 30, 1)
                        $ Line = "no"
                "I said come over here.":

                    if approval_check(LauraX, 600, "O"):

                        $ LauraX.change_stat("love", 50, 1, 1)
                        $ LauraX.change_stat("love", 40, -1)
                        $ LauraX.change_stat("obedience", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and approval_check(LauraX, 1500):

                        $ LauraX.change_stat("love", 70, -2)
                        $ LauraX.change_stat("love", 90, -1)
                        $ LauraX.change_stat("obedience", 50, 2)
                        $ LauraX.change_stat("obedience", 90, 1)
                        ch_l "Ok, fine."
                        $ Line = "yes"

                    elif approval_check(LauraX, 200, "O"):

                        $ LauraX.change_stat("love", 60, -4)
                        $ LauraX.change_stat("love", 90, -3)
                        ch_l "Don't even try it."
                        $ LauraX.change_stat("inhibition", 40, 2)
                        $ LauraX.change_stat("inhibition", 60, 1)
                        $ LauraX.change_stat("obedience", 70, -3)
                        ch_l "I'm staying put."
                    else:

                        $ LauraX.change_stat("inhibition", 30, 1)
                        $ LauraX.change_stat("inhibition", 50, 1)
                        $ LauraX.change_stat("love", 50, -1, 1)
                        $ LauraX.change_stat("obedience", 70, -1)
                        $ Line = "no"
    else:


        if LauraX.love > LauraX.obedience:
            ch_l "Sure!"
        else:
            ch_l "Ok, I'm in route."
        $ Line = "yes"

    $ approval_bonus = 0

    if not Line:

        $ LauraX.recent_history.append("no_summon")
        return

    if Line == "no":

        if LauraX.location == "bg_classroom":
            ch_l "I can't skip this lecture."
        elif LauraX.location == "bg_dangerroom":
            ch_l "I'm just getting warmed up though!"
        else:
            ch_l "Sorry, [LauraX.player_petname], I'm kinda busy."
        $ LauraX.recent_history.append("no_summon")
        return

    elif Line == "go to":

        $ renpy.pop_call()
        $ LauraX.recent_history.append("goto")
        $ Player.recent_history.append("goto")
        $ Line = 0
        if LauraX.location == "bg_classroom":
            ch_l "K, there's room next to me."
            jump Class_Room
        elif LauraX.location == "bg_dangerroom":
            ch_l "I'll try to leave some bots for 'ya."
            jump Danger_Room
        elif LauraX.location == "bg_laura":
            ch_l "I'll. . . make some space."
            jump Laura_Room
        elif LauraX.location == "bg_player":
            ch_l "I'll be waiting."
            jump Player_Room
        elif LauraX.location == "bg_showerroom":
            ch_l "I'll leave you some hot water."
            jump Shower_Room
        elif LauraX.location == "bg_campus":
            ch_l "Look for the biggest tree."
            jump Campus
        elif LauraX.location in PersonalRooms:
            ch_l "Yeah, see you."
            $ bg_current = LauraX.location
            jump Misplaced
        else:
            ch_l "Um, I'll just meet you in my room."
            $ LauraX.location = "bg_laura"
            jump Laura_Room


    elif Line == "lonely":
        ch_l "You are such a dork!"
    elif Line == "command":
        ch_l "Yes, [LauraX.player_petname]."

    $ LauraX.recent_history.append("summoned")
    $ Line = 0
    if "locked" in Player.traits:
        call Locked_Door (LauraX)
        return
    $ LauraX.location = bg_current
    call Taboo_Level (0)
    $ LauraX.change_outfit()
    call set_the_scene
    return




label Laura_Leave(approval_bonus=approval_bonus, GirlsNum=0):
    if "leaving" in LauraX.recent_history:
        $ LauraX.drain_word("leaving")
    else:
        return

    if LauraX.location == "hold":

        ch_l "I'm taking off for a bit, later."
        return

    if LauraX in Party or "lockedtravels" in LauraX.traits:


        $ LauraX.location = bg_current
        return

    elif "freetravels" in LauraX.traits or not approval_check(LauraX, 700):

        $ LauraX.change_outfit()
        if GirlsNum:
            ch_l "Yeah, I'm leaving too."

        if LauraX.location == "bg_classroom":
            ch_l "I've got class."
        elif LauraX.location == "bg_dangerroom":
            ch_l "I'm hitting the Danger Room."
        elif LauraX.location == "bg_campus":
            ch_l "I'm taking a nap in the quad."
        elif LauraX.location == "bg_laura":
            ch_l "I'm headed back to my room."
        elif LauraX.location == "bg_player":
            ch_l "I'm gonna hang out in your room for a bit."
        elif LauraX.location == "bg_pool":
            ch_l "I was hitting the pool."
        elif LauraX.location == "bg_showerroom":
            if approval_check(LauraX, 1400):
                ch_l "I'm hitting the showers, later."
            else:
                ch_l "I'm headed out."
        else:
            ch_l "I'm headed out, later."
        hide Laura_Sprite
        return


    if bg_current == "bg_dangerroom":
        call Gym_Exit ([LauraX])

    $ LauraX.change_outfit()

    if "follow" not in LauraX.traits:

        $ LauraX.traits.append("follow")

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0

    if LauraX.location == "bg_classroom":
        $ approval_bonus = 10
    elif LauraX.location == "bg_dangerroom":
        $ approval_bonus = 20
    elif LauraX.location == "bg_showerroom":
        $ approval_bonus = 40


    if GirlsNum:
        ch_l "Yeah, I'm headed out too."

    if LauraX.location == "bg_classroom":
        ch_l "I've got class, want in?"
    elif LauraX.location == "bg_dangerroom":
        ch_l "I've got some Danger Room time, want in?"
    elif LauraX.location == "bg_campus":
        ch_l "I'm taking a nap on the quad, you want in?"
    elif LauraX.location == "bg_laura":
        ch_l "I'm headed back to my room, you want in?"
    elif LauraX.location == "bg_player":
        ch_l "I'm going to hang out in your room for a bit, you coming?"
    elif LauraX.location == "bg_showerroom":
        if approval_check(LauraX, 1600):
            ch_l "I'm hitting the showers, you could use one too."
        else:
            ch_l "I'm hitting the showers, see you later."
            return
    elif LauraX.location == "bg_pool":
        ch_l "I was hitting the pool. Wanna come?"
    else:
        ch_l "Wanna join me?"


    menu:
        extend ""
        "Sure, I'll catch up.":
            if "followed" not in LauraX.recent_history:
                $ LauraX.change_stat("love", 55, 1)
                $ LauraX.change_stat("inhibition", 30, 1)
            $ Line = "go to"
        "Nah, we can talk later.":

            if "followed" not in LauraX.recent_history:
                $ LauraX.change_stat("obedience", 50, 1)
                $ LauraX.change_stat("obedience", 30, 2)
            ch_l "Sure, whatever."
        "Could you please stay with me? I'll get lonely.":

            if approval_check(LauraX, 650, "L") or approval_check(LauraX, 1500):
                if "followed" not in LauraX.recent_history:
                    $ LauraX.change_stat("love", 70, 1)
                    $ LauraX.change_stat("obedience", 50, 1)
                $ Line = "lonely"
            else:
                if "followed" not in LauraX.recent_history:
                    $ LauraX.change_stat("inhibition", 30, 1)
                $ Line = "no"
                ch_l "Man, you are such a sap."
        "Come on, it'll be fun.":

            if approval_check(LauraX, 400, "L") and approval_check(LauraX, 800):
                $ LauraX.change_stat("love", 70, 1)
                $ LauraX.change_stat("obedience", 50, 1)
                $ Line = "fun"
            else:
                $ LauraX.change_stat("inhibition", 30, 1)
                $ Line = "no"
        "No, stay here.":

            if approval_check(LauraX, 600, "O"):

                if "followed" not in LauraX.recent_history:
                    $ LauraX.change_stat("love", 40, -2)
                    $ LauraX.change_stat("obedience", 90, 1)
                $ Line = "command"

            elif D20 >= 7 and approval_check(LauraX, 1400):

                if "followed" not in LauraX.recent_history:
                    $ LauraX.change_stat("love", 70, -2)
                    $ LauraX.change_stat("love", 90, -1)
                    $ LauraX.change_stat("obedience", 50, 2)
                    $ LauraX.change_stat("obedience", 90, 1)
                ch_l "I guess if you need me here."
                $ Line = "yes"

            elif approval_check(LauraX, 200, "O"):

                if "followed" not in LauraX.recent_history:
                    $ LauraX.change_stat("love", 70, -4)
                    $ LauraX.change_stat("love", 90, -2)
                ch_l "Don't tell me what to do."
                if "followed" not in LauraX.recent_history:
                    $ LauraX.change_stat("inhibition", 40, 2)
                    $ LauraX.change_stat("inhibition", 60, 1)
                    $ LauraX.change_stat("obedience", 70, -2)
                ch_l "I'm out of here."
            else:

                if "followed" not in LauraX.recent_history:
                    $ LauraX.change_stat("inhibition", 30, 1)
                    $ LauraX.change_stat("inhibition", 50, 1)
                    $ LauraX.change_stat("love", 50, -1, 1)
                    $ LauraX.change_stat("love", 90, -2)
                    $ LauraX.change_stat("obedience", 70, -1)
                $ Line = "no"


    call Taboo_Level (0)
    $ LauraX.recent_history.append("followed")
    if not Line:

        hide Laura_Sprite
        call Gym_Clothes_Off ([LauraX])
        return

    if Line == "no":

        if LauraX.location == "bg_classroom":
            ch_l "I really can't miss this one."
        elif LauraX.location == "bg_dangerroom":
            ch_l "Sorry [LauraX.player_petname], but I'm going a little stir crazy."
        else:
            ch_l "Sorry, I have stuff to do."
        hide Laura_Sprite
        call Gym_Clothes_Off ([LauraX])
        return

    elif Line == "go to":


        $ approval_bonus = 0
        $ Line = 0
        call DrainAll ("leaving")
        call DrainAll ("arriving")
        $ LauraX.recent_history.append("goto")
        $ Player.recent_history.append("goto")
        hide Laura_Sprite
        call Gym_Clothes_Off ([LauraX])
        if LauraX.location == "bg_classroom":
            ch_l "Ok, get a move on then."
            jump Class_Room_Entry
        elif LauraX.location == "bg_dangerroom":
            ch_l "I'll get warmed up."
            jump Danger_Room_Entry
        elif LauraX.location == "bg_laura":
            ch_l "Ok."
            jump Laura_Room
        elif LauraX.location == "bg_player":
            ch_l "Good."
            jump Player_Room
        elif LauraX.location == "bg_showerroom":
            ch_l "Ok, nice."
            jump Shower_Room_Entry
        elif LauraX.location == "bg_campus":
            ch_l "Ok, nice."
            jump Campus_Entry
        elif LauraX.location == "bg_pool":
            ch_l "Cool."
            jump Pool_Entry
        else:
            ch_l "I'll just meet you in your room."
            $ LauraX.location = "bg_player"
            jump Player_Room



    elif Line == "lonely":
        ch_l "Well, I guess you should never go alone. . ."
    elif Line == "command":
        ch_l "Yes [LauraX.player_petname]."

    $ Line = 0
    ch_l "I'll stick around."
    $ LauraX.location = bg_current
    return





label Laura_Clothes:
    if LauraX.Taboo:
        if "exhibitionist" in LauraX.traits:
            ch_l "Yes? . ."
        elif approval_check(LauraX, 900, TabM=4) or approval_check(LauraX, 400, "I", TabM=3):
            ch_l "I don't think I'm supposed to undress around here. . ."
        else:
            ch_l "I don't think I'm supposed to undress around here. . ."
            ch_l "Can we talk about this in our rooms?"
            return
    elif approval_check(LauraX, 900, TabM=4) or approval_check(LauraX, 600, "L") or approval_check(LauraX, 300, "O"):
        ch_l "Oh? What about them?"
    else:
        ch_l "I don't think about my clothes much."
        ch_l "You shouldn't either."
        return

    if Girl != LauraX or Line == "Giftstore":

        $ renpy.pop_call()
    $ Line = 0
    $ Girl = LauraX
    call shift_focus (Girl)

label Laura_Wardrobe_Menu:
    $ LauraX.change_face()
    $ primary_action = 1
    while True:
        menu:
            ch_l "What about my clothes?"
            "Overshirts":
                call Laura_Clothes_Over
            "Legwear":
                call Laura_Clothes_Legs
            "Underwear":
                call Laura_Clothes_Under
            "Accessories":
                call Laura_Clothes_Misc
            "Outfit Management":
                call Laura_Clothes_Outfits
            "Let's talk about what you wear around.":
                call Clothes_Schedule (LauraX)

            "Could I get a look at it?" if LauraX.location != bg_current:

                call OutfitShame (LauraX, 0, 2)
                if _return:
                    show PhoneSex zorder 150
                    ch_l "Ok, that good?"
                hide PhoneSex
            "Could I get a look at it?" if renpy.showing('DressScreen'):

                call OutfitShame (LauraX, 0, 2)
                if _return:
                    hide DressScreen
            "Would you be more comfortable behind a screen? (locked)" if LauraX.Taboo:
                pass
            "Would you be more comfortable behind a screen?" if LauraX.location == bg_current and not LauraX.Taboo and not renpy.showing('DressScreen'):

                if approval_check(LauraX, 1500) or (LauraX.SeenChest and LauraX.SeenPussy):
                    ch_l "Probably won't need it, thanks."
                else:
                    show DressScreen zorder 150
                    ch_l "Yeah, this is better, thanks."

            "Gift for you (locked)" if Girl.location != bg_current:
                pass
            "Gift for you" if Girl.location == bg_current:
                ch_p "I'd like to give you something."
                call Gifts
            "Switch to. . .":

                if renpy.showing('DressScreen'):
                    call OutfitShame (LauraX, 0, 2)
                    if _return:
                        hide DressScreen
                    else:
                        $ LauraX.change_outfit()
                $ LauraX.Set_Temp_Outfit()
                $ primary_action = 0
                call Switch_Chat
                if Girl != LauraX:
                    ch_p "I wanted to talk about your clothes."
                    call expression Girl.tag +"_Clothes"
                $ Girl = LauraX
                call shift_focus (Girl)
            "Never mind, you look good like that.":

                if "wardrobe" not in LauraX.recent_history:

                    if LauraX.Chat[1] <= 1:
                        $ LauraX.change_stat("love", 70, 15)
                        $ LauraX.change_stat("obedience", 40, 20)
                        ch_l "Oh! Thank you."
                    elif LauraX.Chat[1] <= 10:
                        $ LauraX.change_stat("love", 70, 5)
                        $ LauraX.change_stat("obedience", 40, 7)
                        ch_l "Right?"
                    elif LauraX.Chat[1] <= 50:
                        $ LauraX.change_stat("love", 70, 1)
                        $ LauraX.change_stat("obedience", 40, 1)
                        ch_l "Uh-huh."
                    else:
                        ch_l "Sure."
                    $ LauraX.recent_history.append("wardrobe")
                if renpy.showing('DressScreen'):
                    call OutfitShame (LauraX, 0, 2)
                    if _return:
                        hide DressScreen
                    else:
                        $ LauraX.change_outfit()
                $ LauraX.Set_Temp_Outfit()
                $ LauraX.Chat[1] += 1
                $ primary_action = 0
                return







    menu Laura_Clothes_Outfits:
        "You should remember that one. [[Set Custom]":

            menu:
                "Which slot would you like this saved in?"
                "Custom 1":
                    call OutfitShame (LauraX, 3, 1)
                "Custom 2":
                    call OutfitShame (LauraX, 5, 1)
                "Custom 3":
                    call OutfitShame (LauraX, 6, 1)
                "Gym Clothes":
                    call OutfitShame (LauraX, 4, 1)
                "Sleepwear":
                    call OutfitShame (LauraX, 7, 1)
                "Swimwear":
                    call OutfitShame (LauraX, 10, 1)
                "Never mind":

                    pass
        "Leather combat outfit":

            $ LauraX.change_outfit("casual1")
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ LauraX.Outfit = "casual1"
                    $ LauraX.Shame = 0
                    ch_l "Yeah, I love wearing this one in the field."
                "Let's try something else though.":
                    ch_l "Ok."
        "Leather jacket and skirt combo":

            $ LauraX.change_outfit("casual2")
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ LauraX.Outfit = "casual2"
                    $ LauraX.Shame = 0
                    ch_l "Yeah, I mean, my cousin got it for me."
                "Let's try something else though.":
                    ch_l "Ok."

        "Remember that outfit we put together? [[Set a custom outfit] (locked)" if not LauraX.Custom1[0] and not LauraX.Custom2[0] and not LauraX.Custom3[0]:
            pass

        "Remember that outfit we put together?" if LauraX.Custom1[0] or LauraX.Custom2[0] or LauraX.Custom3[0]:
            $ counter = 0
            while 1:
                menu:
                    "Throw on Custom 1 (locked)" if not LauraX.Custom1[0]:
                        pass
                    "Throw on Custom 1" if LauraX.Custom1[0]:
                        $ LauraX.change_outfit("custom1")
                        $ counter = 3
                    "Throw on Custom 2 (locked)" if not LauraX.Custom2[0]:
                        pass
                    "Throw on Custom 2" if LauraX.Custom2[0]:
                        $ LauraX.change_outfit("custom2")
                        $ counter = 5
                    "Throw on Custom 3 (locked)" if not LauraX.Custom3[0]:
                        pass
                    "Throw on Custom 3" if LauraX.Custom3[0]:
                        $ LauraX.change_outfit("custom3")
                        $ counter = 6

                    "You should wear this one in private. (locked)" if not counter:
                        pass
                    "You should wear this one in private." if counter:
                        if counter == 5:
                            $ LauraX.Clothing[9] = "custom2"
                        elif counter == 6:
                            $ LauraX.Clothing[9] = "custom3"
                        else:
                            $ LauraX.Clothing[9] = "custom1"
                        ch_l "Ok, sure."
                    "On second thought, forget about that one outfit. . .":

                        menu:
                            "Custom 1 [[clear custom 1]" if LauraX.Custom1[0]:
                                ch_l "Ok."
                                $ LauraX.Custom1[0] = 0
                            "Custom 1 [[clear custom 1] (locked)" if not LauraX.Custom1[0]:
                                pass
                            "Custom 2 [[clear custom 2]" if LauraX.Custom2[0]:
                                ch_l "Ok."
                                $ LauraX.Custom2[0] = 0
                            "Custom 2 [[clear custom 2] (locked)" if not LauraX.Custom2[0]:
                                pass
                            "Custom 3 [[clear custom 3]" if LauraX.Custom3[0]:
                                ch_l "Ok."
                                $ LauraX.Custom3[0] = 0
                            "Custom 3 [[clear custom 3] (locked)" if not LauraX.Custom3[0]:
                                pass
                            "Never mind, [[back].":
                                pass

                    "You should wear this one out. [[choose outfit first](locked)" if not counter:
                        pass
                    "You should wear this one out." if counter:
                        call Custom_Out (LauraX, counter)
                    "Ok, back to what we were talking about. . .":
                        $ counter = 0
                        return

        "Gym Clothes?" if not LauraX.Taboo or bg_current == "bg_dangerroom":
            $ LauraX.change_outfit("gym")

        "Sleepwear?" if not LauraX.Taboo:
            if approval_check(LauraX, 1200):
                $ LauraX.change_outfit("sleep")
            else:
                call Display_DressScreen (LauraX)
                if _return:
                    $ LauraX.change_outfit("sleep")

        "Swimwear? (locked)" if (LauraX.Taboo and bg_current != "bg_pool") or not LauraX.Swim[0]:
            $ LauraX.change_outfit("swimwear")
        "Swimwear?" if (not LauraX.Taboo or bg_current == "bg_pool") and LauraX.Swim[0]:
            $ LauraX.change_outfit("swimwear")

        "Halloween Costume?" if "halloween" in LauraX.history:
            ch_l "Ok."
            $ LauraX.change_outfit("costume")
        "Your birthday suit looks really great. . .":


            $ LauraX.change_face("_sexy", 1)
            $ Line = 0
            if not LauraX.bra and not LauraX.underwear and not LauraX.top and not LauraX.legs and not LauraX.hose:
                ch_l "Yeah. . . wait, how would you know?"
            elif LauraX.SeenChest and LauraX.SeenPussy and approval_check(LauraX, 1200, TabM=4):
                ch_l "You know it. . ."
                $ Line = 1
            elif approval_check(LauraX, 2000, TabM=4):
                ch_l "Skipping straight to that?"
                $ Line = 1
            elif LauraX.SeenChest and LauraX.SeenPussy and approval_check(LauraX, 1200, TabM=0):
                ch_l "Maybe, but not here. . ."
            elif approval_check(LauraX, 2000, TabM=0):
                ch_l "Maybe, but not here. . ."
            elif approval_check(LauraX, 1000, TabM=0):
                $ LauraX.change_face("_confused", 1,Mouth="_smirk")
                ch_l "Yeah, but I'm not exactly showing it off."
                $ LauraX.change_face("_bemused", 0)
            else:
                $ LauraX.change_face("_angry", 1)
                ch_l "What's it to you?"

            if Line:

                $ LauraX.change_outfit("nude")
                "She throws her clothes off at her feet."
                call Laura_First_Topless
                call Laura_First_Bottomless (1)
                $ LauraX.change_face("_sexy")
                menu:
                    "You know, you should wear this one out. [[set current outfit]":
                        if "exhibitionist" in LauraX.traits:
                            ch_l "mmmm. . ."
                            $ LauraX.Outfit = "nude"
                            $ LauraX.change_stat("lust", 50, 10)
                            $ LauraX.change_stat("lust", 70, 5)
                            $ LauraX.Shame = 50
                        elif approval_check(LauraX, 800, "I") or approval_check(LauraX, 2800, TabM=0):
                            ch_l "Exciting. . ."
                            $ LauraX.Outfit = "nude"
                            $ LauraX.Shame = 50
                        else:
                            $ LauraX.change_face("_sexy", 1)
                            $ LauraX.eyes = "_surprised"
                            ch_l "I probably shouldn't. Sorry."
                    "Let's try something else though.":

                        if "exhibitionist" in LauraX.traits:
                            ch_l "Are you sure?"
                        elif approval_check(LauraX, 800, "I") or approval_check(LauraX, 2800, TabM=0):
                            $ LauraX.change_face("_bemused", 1)
                            ch_l "I was worried you expected me to go out like this."
                            ch_l ". . ."
                        else:
                            $ LauraX.change_face("_confused", 1)
                            ch_l "I don't mind you seeing my body, but. . ."
            $ Line = 0
        "Never mind":

            return

    return




    menu Laura_Clothes_Over:

        "Why don't you go with no [LauraX.top]?" if LauraX.top:
            $ LauraX.change_face("_bemused", 1)
            if approval_check(LauraX, 800, TabM=3) and (LauraX.bra or LauraX.SeenChest):
                ch_l "Ok."
            elif approval_check(LauraX, 600, TabM=0):
                call Laura_NoBra
                if not _return:
                    if not approval_check(LauraX, 1200):
                        call Display_DressScreen (LauraX)
                        if not _return:
                            return
                    else:
                        return
            else:
                call Display_DressScreen (LauraX)
                if not _return:
                    ch_l "Not right now."
                    if not LauraX.bra:
                        ch_l "I don't have anything under this. . ."
                    return
            $ Line = LauraX.top
            $ LauraX.top = ""
            "She throws her [Line] at her feet."
            if not LauraX.bra and not renpy.showing('DressScreen'):
                call Laura_First_Topless

        "Try on that leather jacket." if LauraX.top != "jacket":
            $ LauraX.change_face("_bemused")
            if not LauraX.top or LauraX.bra == "leather_bra":

                ch_l "Sure."
            elif approval_check(LauraX, 800, TabM=0):
                ch_l "Yeah, ok."
            else:
                call Display_DressScreen (LauraX)
                if not _return:
                    $ LauraX.change_face("_bemused", 1)
                    ch_l "I don't really want to take this [LauraX.top] off at the moment."
                    return
            $ LauraX.top = "jacket"

        "Maybe just throw on a towel?" if LauraX.top != "_towel":
            $ LauraX.change_face("_bemused", 1)
            if LauraX.bra or LauraX.SeenChest:
                ch_l "Weird."
            elif approval_check(LauraX, 1000, TabM=0):
                $ LauraX.change_face("_perplexed", 1)
                ch_l "Huh, ok . ."
            else:
                call Display_DressScreen (LauraX)
                if not _return:
                    ch_l "That wouldn't look right."
                    return
            $ LauraX.top = "_towel"
        "Never mind":

            pass
    return




    label Laura_NoBra:
        menu:
            ch_l "I don't exactly have anything on under this. . ."
            "Then you could slip something on under it. . .":
                if LauraX.SeenChest and approval_check(LauraX, 1000, TabM=3):
                    $ LauraX.blushing = "_blush1"
                    ch_l "-I didn't say that I minded. . ."
                    $ LauraX.blushing = ""
                elif approval_check(LauraX, 1200, TabM=4):
                    $ LauraX.blushing = "_blush1"
                    ch_l "-I didn't say that I minded. . ."
                    $ LauraX.blushing = ""
                elif approval_check(LauraX, 900, TabM=2) and "lace corset" in LauraX.inventory:
                    ch_l "I guess I could find something."
                    $ LauraX.bra  = "lace corset"
                    "She pulls out her lace corset and slips it under her [LauraX.top]."
                elif approval_check(LauraX, 700, TabM=2) and "corset" in LauraX.inventory:
                    ch_l "I guess I could find something."
                    $ LauraX.bra  = "corset"
                    "She pulls out her corset and slips it under her [LauraX.top]."
                elif approval_check(LauraX, 600, TabM=2):
                    ch_l "Yeah, I guess."
                    $ LauraX.bra = "leather_bra"
                    "She pulls out her leather bra and slips it on under her [LauraX.top]."
                else:
                    ch_l "Yeah, I don't think so."
                    return 0
            "You could always just wear nothing at all. . .":

                if approval_check(LauraX, 1100, "LI", TabM=2) and LauraX.love > LauraX.inhibition:
                    ch_l "For you? I guess. . ."
                elif approval_check(LauraX, 700, "OI", TabM=2) and LauraX.obedience > LauraX.inhibition:
                    ch_l "Sure. . ."
                elif approval_check(LauraX, 600, "I", TabM=2):
                    ch_l "Yeah. . ."
                elif approval_check(LauraX, 1300, TabM=2):
                    ch_l "Okay, fine."
                else:
                    $ LauraX.change_face("_surprised")
                    $ LauraX.brows = "_angry"
                    if LauraX.Taboo > 20:
                        ch_l "Not in public, I won't!"
                    else:
                        ch_l "You're not that cute, [LauraX.player_petname]!"
                    return 0
            "Never mind.":
                ch_l "Ok. . ."
                return 0
        return 1




    menu Laura_Clothes_Legs:

        "Maybe go without the [LauraX.legs]." if LauraX.legs:
            $ LauraX.change_face("_sexy", 1)
            if LauraX.SeenPanties and LauraX.underwear and approval_check(LauraX, 500, TabM=5):
                ch_l "Ok, sure."
            elif LauraX.SeenPussy and approval_check(LauraX, 900, TabM=4):
                ch_l "Yeah, ok."
            elif approval_check(LauraX, 1300, TabM=2) and LauraX.underwear:
                ch_l "For you, fine. . ."
            elif approval_check(LauraX, 700) and not LauraX.underwear:
                call Laura_NoPantiesOn
                if not _return and not LauraX.underwear:
                    if not approval_check(LauraX, 1500):
                        call Display_DressScreen (LauraX)
                        if not _return:
                            return
                    else:
                        return
            else:
                call Display_DressScreen (LauraX)
                if not _return:
                    ch_l "Um, not with you around."
                    if not LauraX.underwear:
                        ch_l "I'm going commando today. . ."
                    return

            if LauraX.legs == "leather_pants" or LauraX.legs == "mesh_pants":
                $ LauraX.legs = ""
                "She tugs her pants off and drops them to the ground."
            else:
                $ LauraX.legs = ""
                "She tugs her skirt off and drops it to the ground."
            if renpy.showing('DressScreen'):
                pass
            elif LauraX.underwear:
                $ LauraX.SeenPanties = 1
            else:
                call Laura_First_Bottomless

        "Add leather_pants" if LauraX.legs != "leather_pants":
            ch_p "You look great in those leather_pants"
            ch_l "Yeah, ok."
            $ LauraX.legs = "leather_pants"

        "Add mesh pants." if LauraX.legs != "mesh_pants" and "mesh_pants" in LauraX.inventory:
            ch_p "You look great in those mesh pants."
            if approval_check(LauraX, 1000, TabM=4):
                ch_l "Yeah, ok."
                $ LauraX.legs = "mesh_pants"
            else:
                call Display_DressScreen (LauraX)
                if not _return:
                    ch_l "Sorry, those are kind of. . . breezy."
                else:
                    $ LauraX.legs = "mesh_pants"

        "Add belty_skirt" if LauraX.legs != "_skirt":
            ch_p "What about wearing your leather skirt? With the belts?"
            ch_l "Sure, why not."
            $ LauraX.legs = "_skirt"

        "Add leather_skirt" if LauraX.legs != "other_skirt" and "halloween" in LauraX.history:
            ch_p "What about wearing your leather skirt?"
            ch_l "Sure, why not."
            $ LauraX.legs = "other_skirt"
        "Never mind":

            pass
    return




    label Laura_NoPantiesOn:
        menu:
            ch_l "I'm going commando today."
            "Then you could slip on a pair of panties. . .":
                if LauraX.SeenPussy and approval_check(LauraX, 1100, TabM=4):
                    $ LauraX.blushing = "_blush1"
                    ch_l "No, commando's fine. . ."
                    $ LauraX.blushing = ""
                elif approval_check(LauraX, 1500, TabM=4):
                    $ LauraX.blushing = "_blush1"
                    ch_l "No, commando's fine. . ."
                    $ LauraX.blushing = ""
                elif approval_check(LauraX, 700, TabM=4):
                    ch_l "Yeah, I guess."
                    if "lace_panties" in LauraX.inventory:
                        ch_l "I like how you think."
                        $ LauraX.underwear  = "lace_panties"
                    else:
                        $ LauraX.underwear = "_black_panties"
                    if approval_check(LauraX, 1200, TabM=4):
                        $ Line = LauraX.legs
                        $ LauraX.legs = ""
                        "She pulls off her [Line] and slips on the [LauraX.underwear]."
                    elif LauraX.legs == "_skirt":
                        "She pulls out her [LauraX.underwear] and pulls them up under her skirt."
                        $ LauraX.legs = ""
                        "Then she drops the skirt to the floor."
                    else:
                        $ Line = LauraX.legs
                        $ LauraX.legs = ""
                        "She steps away a moment and then comes back wearing only the [LauraX.underwear]."
                    return
                else:
                    ch_l "Nope."
                    return 0
            "You could always just wear nothing at all. . .":

                if approval_check(LauraX, 1100, "LI", TabM=3) and LauraX.love > LauraX.inhibition:
                    ch_l "True. . ."
                elif approval_check(LauraX, 700, "OI", TabM=3) and LauraX.obedience > LauraX.inhibition:
                    ch_l "Yes. . ."
                elif approval_check(LauraX, 600, "I", TabM=3):
                    ch_l "Hrmm. . ."
                elif approval_check(LauraX, 1300, TabM=3):
                    ch_l "Fine."
                else:
                    $ LauraX.change_face("_surprised")
                    $ LauraX.brows = "_angry"
                    if LauraX.Taboo > 20:
                        ch_l "Yeah, but not in public, [LauraX.player_petname]!"
                    else:
                        ch_l "You aren't that cute, [LauraX.player_petname]!"
                    return 0
            "Never mind.":

                ch_l "Ok. . ."
                return 0
        return 1




    menu Laura_Clothes_Under:
        "Tops":
            menu:
                "How about you lose the [LauraX.bra]?" if LauraX.bra:
                    $ LauraX.change_face("_bemused", 1)
                    if LauraX.SeenChest and approval_check(LauraX, 900, TabM=2.7):
                        ch_l "Ok."
                    elif approval_check(LauraX, 1100, TabM=2):
                        if LauraX.Taboo:
                            ch_l "I don't know, here. . ."
                        else:
                            ch_l "Maybe. . ."
                    elif LauraX.top == "jacket" and approval_check(LauraX, 600, TabM=2):
                        ch_l "This jacket is a bit revealing. . ."
                    elif LauraX.top and approval_check(LauraX, 500, TabM=2):
                        ch_l "I guess I could. . ."
                    elif not LauraX.top:
                        call Display_DressScreen (LauraX)
                        if not _return:
                            ch_l "Not without some other top."
                            return
                    else:
                        call Display_DressScreen (LauraX)
                        if not _return:
                            ch_l "Nah."
                            return
                    $ Line = LauraX.bra
                    $ LauraX.bra = ""
                    if LauraX.top:
                        "She reaches under her [LauraX.top] grabs her [Line], and pulls it off, dropping it to the ground."
                    else:
                        "She pulls off her [Line] and drops it to the ground."
                        if not renpy.showing('DressScreen'):
                            call Laura_First_Topless


                "Add leather_bra" if LauraX.bra != "leather_bra":
                    ch_p "Try on that leather bra."
                    ch_l "Ok."
                    $ LauraX.bra = "leather_bra"

                "Add white tanktop" if LauraX.bra != "white_tank" and "halloween" in LauraX.history:
                    ch_p "Try on that white tanktop."
                    ch_l "Ok."
                    $ LauraX.bra = "white_tank"

                "Add red corset." if LauraX.bra != "corset" and "corset" in LauraX.inventory:
                    ch_p "I like that red corset."
                    if LauraX.SeenChest or approval_check(LauraX, 1000, TabM=1):
                        ch_l "K."
                        $ LauraX.bra = "corset"
                    else:
                        call Display_DressScreen (LauraX)
                        if not _return:
                            ch_l "It's a bit revealing. . ."
                        else:
                            $ LauraX.bra = "corset"

                "Add lace corset" if LauraX.bra != "lace corset" and "lace corset" in LauraX.inventory:
                    ch_p "I like that lace corset."
                    if LauraX.SeenChest or approval_check(LauraX, 1300, TabM=2):
                        ch_l "K."
                        $ LauraX.bra = "lace corset"
                    else:
                        call Display_DressScreen (LauraX)
                        if not _return:
                            ch_l "It's a bit transparent. . ."
                        else:
                            $ LauraX.bra = "lace corset"

                "Add wolverine tanktop" if LauraX.bra != "wolvie_top" and "wolvie_top" in LauraX.inventory:
                    ch_p "I like that wolverine tanktop."
                    if LauraX.SeenChest or approval_check(LauraX, 1000, TabM=2):
                        ch_l "K."
                        $ LauraX.bra = "wolvie_top"
                    else:
                        call Display_DressScreen (LauraX)
                        if not _return:
                            ch_l "It's a {i}little{/i} embarrassing. . ."
                        else:
                            $ LauraX.bra = "wolvie_top"

                "Add bikini_top" if LauraX.bra != "_bikini_top" and "_bikini_top" in LauraX.inventory:
                    ch_p "I like that bikini top."
                    if bg_current == "bg_pool":
                        ch_l "K."
                        $ LauraX.bra = "_bikini_top"
                    else:
                        if LauraX.SeenChest or approval_check(LauraX, 1000, TabM=2):
                            ch_l "K."
                            $ LauraX.bra = "_bikini_top"
                        else:
                            call Display_DressScreen (LauraX)
                            if not _return:
                                ch_l "This is not really a \"bikini\" sort of place. . ."
                            else:
                                $ LauraX.bra = "_bikini_top"
                "Never mind":
                    pass
            return
        "Hose and stockings options":

            menu:
                "You could lose the hose." if LauraX.hose and LauraX.hose != 'ripped_tights' and LauraX.hose != 'tights':
                    $ LauraX.hose = ""
                "The thigh-high hose would look good with that." if LauraX.hose != "_stockings":
                    $ LauraX.hose = "_stockings"
                "The black stockings would look good with that." if LauraX.hose != "black stockings" and "halloween" in LauraX.history:
                    $ LauraX.hose = "black stockings"
                "The stockings and garterbelt would look good with that." if LauraX.hose != "stockings_and_garterbelt" and "stockings_and_garterbelt" in LauraX.inventory:
                    $ LauraX.hose = "stockings_and_garterbelt"
                "Just the garterbelt would look good with that." if LauraX.hose != "garterbelt" and "stockings_and_garterbelt" in LauraX.inventory:
                    $ LauraX.hose = "garterbelt"
                "Never mind":
                    pass
            return
        "Panties":


            menu:
                "You could lose those panties. . ." if LauraX.underwear:
                    $ LauraX.change_face("_bemused", 1)
                    if approval_check(LauraX, 900) and (LauraX.legs or (LauraX.SeenPussy and not LauraX.Taboo)):

                        if approval_check(LauraX, 850, "L"):
                            ch_l "True. . ."
                        elif approval_check(LauraX, 500, "O"):
                            ch_l "Agreed."
                        elif approval_check(LauraX, 350, "I"):
                            ch_l "Heh."
                        else:
                            ch_l "Sure, I guess."
                    else:
                        if approval_check(LauraX, 1100, "LI", TabM=3) and LauraX.love > LauraX.inhibition:
                            ch_l "Well look, it's not about you, but. . ."
                        elif approval_check(LauraX, 700, "OI", TabM=3) and LauraX.obedience > LauraX.inhibition:
                            ch_l "Well. . ."
                        elif approval_check(LauraX, 600, "I", TabM=3):
                            ch_l "Hrmm. . ."
                        elif approval_check(LauraX, 1300, TabM=3):
                            ch_l "Okay, okay."
                        else:
                            call Display_DressScreen (LauraX)
                            if not _return:
                                $ LauraX.change_face("_surprised")
                                $ LauraX.brows = "_angry"
                                if LauraX.Taboo > 20:
                                    ch_l "This is too public."
                                else:
                                    ch_l "You're not that cute, [LauraX.player_petname]!"
                                return
                    $ Line = LauraX.underwear
                    $ LauraX.underwear = ""
                    if not LauraX.legs:
                        "She pulls off her [Line], then drops them to the ground."
                        if not renpy.showing('DressScreen'):
                            call Laura_First_Bottomless
                    elif approval_check(LauraX, 1200, TabM=4):
                        $ primary_action = LauraX.legs
                        $ LauraX.legs = ""
                        pause 0.5
                        $ LauraX.legs = primary_action
                        "She pulls off her [LauraX.legs] and [Line], then pulls the [LauraX.legs] back on."
                        $ primary_action = 1
                        call Laura_First_Bottomless (1)
                    elif LauraX.legs == "_skirt":
                        "She reaches under her skirt and pulls her [Line] off."
                    else:
                        $ LauraX.blushing = "_blush1"
                        "She steps away a moment and then comes back."
                        $ LauraX.blushing = ""
                    $ Line = 0

                "Why don't you wear the black panties instead?" if LauraX.underwear and LauraX.underwear != "_black_panties" and LauraX.underwear != "leather_panties":
                    if approval_check(LauraX, 1100, TabM=3):
                        ch_l "Ok."
                        $ LauraX.underwear = "_black_panties"
                    else:
                        call Display_DressScreen (LauraX)
                        if not _return:
                            ch_l "That's none of your busines."
                        else:
                            $ LauraX.underwear = "_black_panties"

                "Why don't you wear the wolverine panties instead?" if "wolvie_panties" in LauraX.inventory and LauraX.underwear and LauraX.underwear != "wolvie_panties":
                    if approval_check(LauraX, 1000, TabM=3):
                        ch_l "I guess."
                        $ LauraX.underwear = "wolvie_panties"
                    else:
                        call Display_DressScreen (LauraX)
                        if not _return:
                            ch_l "That's none of your busines."
                        else:
                            $ LauraX.underwear = "wolvie_panties"

                "Why don't you wear the lace panties instead?" if "lace_panties" in LauraX.inventory and LauraX.underwear and LauraX.underwear != "lace_panties":
                    if approval_check(LauraX, 1300, TabM=3):
                        ch_l "I guess."
                        $ LauraX.underwear = "lace_panties"
                    else:
                        call Display_DressScreen (LauraX)
                        if not _return:
                            ch_l "That's none of your busines."
                        else:
                            $ LauraX.underwear = "lace_panties"

                "I like those bikini bottoms." if "_bikini_bottoms" in LauraX.inventory and LauraX.underwear != "_bikini_bottoms":
                    if bg_current == "bg_pool":
                        ch_l "K."
                        $ LauraX.underwear = "_bikini_bottoms"
                    else:
                        if approval_check(LauraX, 1000, TabM=2):
                            ch_l "K."
                            $ LauraX.underwear = "_bikini_bottoms"
                        else:
                            call Display_DressScreen (LauraX)
                            if not _return:
                                ch_l "This is not really a \"bikini\" sort of place. . ."
                            else:
                                $ LauraX.underwear = "_bikini_bottoms"

                "You know, you could wear some panties with that. . ." if not LauraX.underwear:
                    $ LauraX.change_face("_bemused", 1)
                    if LauraX.legs and (LauraX.love+LauraX.obedience) <= (2*LauraX.inhibition):
                        $ LauraX.mouth = "_smile"
                        ch_l "I don't know about that."
                        menu:
                            "Fine by me":
                                return
                            "I insist, put some on.":
                                if (LauraX.love+LauraX.obedience) <= (1.5*LauraX.inhibition):
                                    $ LauraX.change_face("_angry", Eyes="_side")
                                    ch_l "Well I insist otherwise."
                                    return
                                else:
                                    $ LauraX.change_face("_sadside")
                                    ch_l "Oh, fine."
                    else:
                        ch_l "I guess. . ."
                    menu:
                        extend ""
                        "How about the black ones?":
                            ch_l "Sure, ok."
                            $ LauraX.underwear = "_black_panties"
                        "How about the wolvie ones?" if "wolvie_panties" in LauraX.inventory:
                            ch_l "Sure."
                            $ LauraX.underwear  = "wolvie_panties"
                        "How about the lace ones?" if "lace_panties" in LauraX.inventory:
                            ch_l "Alright."
                            $ LauraX.underwear  = "lace_panties"
                "Never mind":
                    pass
            return
        "Never mind":
            pass
    return




    menu Laura_Clothes_Misc:

        "Dry Hair" if LauraX.hair == "wet":
            ch_p "Maybe dry out your hair."
            if approval_check(LauraX, 600):
                ch_l "Ok."
                $ LauraX.hair = "long"
            else:
                ch_l "I don't know, it's fine like this."

        "Wet Hair style" if LauraX.hair != "wet":
            ch_p "You should go for that wet look with your hair."
            if approval_check(LauraX, 800):
                ch_l "Hmm?"
                $ LauraX.hair = "wet"
                "She wanders off for a minute and comes back."
                ch_l "Like this?"
            else:
                ch_l "Ugh, too much work."

        "Grow pubes" if not LauraX.pubes:
            ch_p "You know, I like some nice hair down there. Maybe grow it out."
            if "pubes" in LauraX.Todo:
                $ LauraX.change_face("_bemused", 1)
                ch_l "Even I can't grow it out instantly."
            else:
                $ LauraX.change_face("_bemused", 1)
                if approval_check(LauraX, 1000, TabM=0):
                    ch_l "Sure, that's easier. . ."
                else:
                    $ LauraX.change_face("_surprised")
                    $ LauraX.brows = "_angry"
                    ch_l "I think I'll do what I want down there."
                    return
                $ LauraX.Todo.append("pubes")
                $ LauraX.PubeC = 6
        "Shave pubes" if LauraX.pubes == "_hairy":
            ch_p "I like it waxed clean down there."
            $ LauraX.change_face("_bemused", 1)
            if "shave" in LauraX.Todo:
                ch_l "Yeah, I know, I'll get to it."
            else:
                if approval_check(LauraX, 1100, TabM=0):
                    ch_l "Really? I guess I could give it a shave. . ."
                else:
                    $ LauraX.change_face("_surprised")
                    $ LauraX.brows = "_angry"
                    ch_l "I think I'll do what I want down there."
                    return
                $ LauraX.Todo.append("shave")

        "Piercings. [[See what she looks like without them first] (locked)" if not LauraX.SeenPussy and not LauraX.SeenChest:
            pass

        "Add ring piercings" if LauraX.piercings != "_ring" and (LauraX.SeenPussy or LauraX.SeenChest):
            ch_p "You know, you'd look really nice with some ring body piercings."
            if "_ring" in LauraX.Todo:
                ch_l "Yeah, I know, I'll get to it."
            else:
                $ LauraX.change_face("_bemused", 1)
                $ approval = approval_check(LauraX, 1150, TabM=0)
                if approval_check(LauraX, 900, "L", TabM=0) or (approval and LauraX.love > 2* LauraX.obedience):
                    ch_l "You think I'd look good with them?"
                elif approval_check(LauraX, 600, "I", TabM=0) or (approval and LauraX.inhibition > LauraX.obedience):
                    ch_l "I've been thinking about that for a while."
                elif approval_check(LauraX, 500, "O", TabM=0) or approval:
                    ch_l "Yes, [LauraX.player_petname]."
                else:
                    $ LauraX.change_face("_surprised")
                    $ LauraX.brows = "_angry"
                    ch_l "Not interested, [LauraX.player_petname]."
                    return
                $ LauraX.Todo.append("_ring")

        "Add barbell piercings" if LauraX.piercings != "_barbell" and (LauraX.SeenPussy or LauraX.SeenChest):
            ch_p "You know, you'd look really nice with some barbell body piercings."
            if "_barbell" in LauraX.Todo:
                ch_l "Yeah, I know, I'll get to it."
            else:
                $ LauraX.change_face("_bemused", 1)
                $ approval = approval_check(LauraX, 1150, TabM=0)
                if approval_check(LauraX, 900, "L", TabM=0) or (approval and LauraX.love > 2*LauraX.obedience):
                    ch_l "You think I'd look good with them?"
                elif approval_check(LauraX, 600, "I", TabM=0) or (approval and LauraX.inhibition > LauraX.obedience):
                    ch_l "I've been thinking about that for a while."
                elif approval_check(LauraX, 500, "O", TabM=0) or approval:
                    ch_l "Yes, [LauraX.player_petname]."
                else:
                    $ LauraX.change_face("_surprised")
                    $ LauraX.brows = "_angry"
                    ch_l "Not interested, [LauraX.player_petname]."
                    return
                $ LauraX.Todo.append("_barbell")

        "Remove piercings" if LauraX.piercings:
            ch_p "You know, you'd look better without those piercings."
            $ LauraX.change_face("_bemused", 1)
            $ approval = approval_check(LauraX, 1350, TabM=0)
            if approval_check(LauraX, 950, "L", TabM=0) or (approval and LauraX.love > LauraX.obedience):
                ch_l "Make up your mind . ."
            elif approval_check(LauraX, 700, "I", TabM=0) or (approval and LauraX.inhibition > LauraX.obedience):
                ch_l "In, out, snickt."
            elif approval_check(LauraX, 600, "O", TabM=0) or approval:
                ch_l "Fine."
            else:
                $ LauraX.change_face("_surprised")
                $ LauraX.brows = "_angry"
                ch_l "I've sort of grown attached."
                return
            $ LauraX.piercings = ""

        "Medallion_choker" if LauraX.neck != "leash_choker":
            ch_p "Why don't you try on that medallion choker?"
            ch_l "Ok. . ."
            $ LauraX.neck = "leash_choker"
        "Remove Necklace" if LauraX.neck:
            ch_p "Maybe go without a necklace."
            ch_l "Ok. . ."
            $ LauraX.neck = ""

        "Add Suspenders" if LauraX.accessory != "suspenders" and LauraX.accessory != "suspenders2" and "halloween" in LauraX.history:
            $ LauraX.accessory = "suspenders"
        "Remove Suspenders" if LauraX.accessory == "suspenders" or LauraX.accessory == "suspenders2":
            $ LauraX.accessory = ""

        "Shift Suspenders" if LauraX.accessory == "suspenders" or LauraX.accessory == "suspenders2":
            $ LauraX.accessory = "suspenders" if LauraX.accessory == "suspenders2" else "suspenders2"
        "Toggle Wristbands":

            if LauraX.arms != "wrists":
                ch_p "Why don't you put those wristbands on."
            else:
                ch_p "Maybe go without the wristbands."
            ch_l "Ok. . ."
            $ LauraX.arms = "wrists" if LauraX.arms != "wrists" else 0
        "Toggle Gloves" if "halloween" in LauraX.history:
            if LauraX.arms != "_gloves":
                ch_p "Why don't you put those long gloves on."
            else:
                ch_p "Maybe go without the gloves."
            ch_l "Ok. . ."
            $ LauraX.arms = "_gloves" if LauraX.arms != "_gloves" else 0
        "Never mind":

            pass
    return


return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
