


label Jubes_Relationship:
    while True:
        menu:
            ch_v "What did you want to talk about?"
            "Do you want to be my girlfriend?" if JubesX not in Player.Harem and "ex" not in JubesX.traits:
                $ JubesX.daily_history.append("relationship")
                if "asked boyfriend" in JubesX.daily_history and "angry" in JubesX.daily_history:
                    $ JubesX.change_face("angry", 1)
                    ch_v "Like I said, not interested."
                    return
                elif "asked boyfriend" in JubesX.daily_history:
                    $ JubesX.change_face("angry", 1)
                    ch_v "Still a no."
                    return
                elif JubesX.broken_up[0]:
                    $ JubesX.change_face("angry", 1)
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

                if JubesX.event_happened[5]:
                    $ JubesX.change_face("bemused", 1)
                    ch_v "You were the one that turned me down. . ."
                else:
                    $ JubesX.change_face("surprised", 2)
                    ch_v "What? . ."
                    $ JubesX.change_face("smile", 1)

                call Jubes_OtherWoman

                if JubesX.love >= 800:
                    $ JubesX.change_face("surprised", 1)
                    $ JubesX.mouth = "smile"
                    call change_Girl_stat(JubesX, "love", 40)
                    ch_v "Sure!"
                    if "boyfriend" not in JubesX.player_petnames:
                        $ JubesX.player_petnames.append("boyfriend")
                    if "JubesYes" in Player.traits:
                        $ Player.traits.remove("JubesYes")
                    $ Player.Harem.append(JubesX)
                    call Harem_Initiation
                    "[JubesX.name] tackles you and kisses you deeply."
                    $ JubesX.change_face("kiss", 1)
                    $ JubesX.permanent_History["kiss"] += 1
                elif JubesX.obedience >= 500:
                    $ JubesX.change_face("perplexed")
                    ch_v "I don't know if I want to -date- you. . ."
                elif JubesX.inhibition >= 500:
                    $ JubesX.change_face("smile")
                    ch_v "I just wanna have fun, ya know?"
                else:
                    $ JubesX.change_face("perplexed", 1)
                    ch_v "Whoa, slow your roll, [JubesX.player_petname]."

            "Do you want to get back together?" if "ex" in JubesX.traits:
                $ JubesX.daily_history.append("relationship")
                if "asked boyfriend" in JubesX.daily_history and "angry" in JubesX.daily_history:
                    $ JubesX.change_face("angry", 1)
                    ch_v "I told'ya, not interested."
                    return
                elif "asked boyfriend" in JubesX.daily_history:
                    $ JubesX.change_face("angry", 1)
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
                    $ JubesX.change_face("surprised", 1)
                    $ JubesX.mouth = "smile"
                    call change_Girl_stat(JubesX, "love", 5)
                    ch_v "Ok, fine, we can give it a try."
                    if "boyfriend" not in JubesX.player_petnames:
                        $ JubesX.player_petnames.append("boyfriend")
                    $ JubesX.traits.remove("ex")
                    if "JubesYes" in Player.traits:
                        $ Player.traits.remove("JubesYes")
                    $ Player.Harem.append(JubesX)
                    call Harem_Initiation
                    "[JubesX.name] pulls you in and kisses you deeply."
                    $ JubesX.change_face("kiss", 1)
                    $ JubesX.permanent_History["kiss"] += 1
                elif JubesX.love >= 600 and approval_check(JubesX, 1500):
                    $ JubesX.change_face("smile", 1)
                    call change_Girl_stat(JubesX, "love", 5)
                    ch_v "Sure, I guess we can try it."
                    if "boyfriend" not in JubesX.player_petnames:
                        $ JubesX.player_petnames.append("boyfriend")
                    $ JubesX.traits.remove("ex")
                    if "JubesYes" in Player.traits:
                        $ Player.traits.remove("JubesYes")
                    $ Player.Harem.append(JubesX)
                    call Harem_Initiation
                    $ JubesX.change_face("kiss", 1)
                    "[JubesX.name] gives you a quick kiss."
                    $ JubesX.change_face("sly", 1)
                    $ JubesX.permanent_History["kiss"] += 1
                elif JubesX.obedience >= 500:
                    $ JubesX.change_face("sad")
                    ch_v "Nah, we gave it a shot."
                elif JubesX.inhibition >= 500:
                    $ JubesX.change_face("perplexed")
                    ch_v "Nah, let's just keep it loose."
                else:
                    $ JubesX.change_face("perplexed", 1)
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
                    "When you said you loved me. . ." if "lover" not in JubesX.traits and JubesX.event_happened[6] >= 20 and JubesX.event_happened[6] != 23:
                        call Jubes_Love_Redux

                    "When you were telling me all that stuff about yourself. . ." if "lover" not in JubesX.traits and JubesX.event_happened[6] == 23:
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
            "Never mind":

                return

    return

label Jubes_OtherWoman(counter=0):

    if not Player.Harem:
        return
    $ counter = int((JubesX.likes[Player.Harem[0].tag] - 500)/2)

    $ JubesX.change_face("perplexed")
    if len(Player.Harem) >= 2:
        ch_v "You're with [Player.Harem[0].name] though, right? And a bunch of others too!"
    else:
        ch_v "You're with [Player.Harem[0].name] though, right?"
    menu:
        extend ""
        "She said I can be with you too." if "JubesYes" in Player.traits:
            if approval_check(JubesX, 1800, Bonus = counter):
                $ JubesX.change_face("smile", 1)
                if JubesX.love >= JubesX.obedience:
                    ch_v "Well, I can deal with that."
                elif JubesX.obedience >= JubesX.inhibition:
                    ch_v "Ok then, I can accept that."
                else:
                    ch_v "Cool."
            else:
                $ JubesX.change_face("angry", 1)
                ch_v "Yeah, ok, but that's not cool with me."
                $ renpy.pop_call()


        "I could ask if she'd be ok with me dating you both." if "JubesYes" not in Player.traits:
            if approval_check(JubesX, 1800, Bonus = counter):
                $ JubesX.change_face("smile", 1)
                if JubesX.love >= JubesX.obedience:
                    ch_v "Well, I could deal with that."
                elif JubesX.obedience >= JubesX.inhibition:
                    ch_v "Ok then, I could accept that."
                else:
                    ch_v "Cool."
                ch_v "Well ask her and let me know tomorrow."
            else:
                $ JubesX.change_face("angry", 1)
                ch_v "Yeah, ok, but that's not cool with me."
            $ renpy.pop_call()
        "What she doesn't know won't hurt her.":

            if not approval_check(JubesX, 1800, Bonus = -counter):
                $ JubesX.change_face("angry", 1)
                if not approval_check(JubesX, 1800):
                    ch_v "Well I'm not her."
                else:
                    ch_v "That sounds ominous."
                $ renpy.pop_call()
            else:
                $ JubesX.change_face("smile", 1)
                if JubesX.love >= JubesX.obedience:
                    ch_v "I guess I could. . ."
                elif JubesX.obedience >= JubesX.inhibition:
                    ch_v "Ok then, I could accept that."
                else:
                    ch_v "Cool."
                $ JubesX.traits.append("downlow")
        "I can break it off with her.":

            $ JubesX.change_face("sad")
            ch_v "Do that, and get back to me."
            $ renpy.pop_call()
        "You're right, I was dumb to ask.":

            $ JubesX.change_face("sad")
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
        elif JubesX.likes[RogueX.tag] >= 900:
            ch_v "She's got an amazing ass. . ."
        elif JubesX.likes[RogueX.tag] >= 800:
            ch_v "She's. . . cool. . . cool. . ."
        elif JubesX.likes[RogueX.tag] >= 700:
            ch_v "I like palling around with her."
        elif JubesX.likes[RogueX.tag] >= 600:
            ch_v "She's cool."
        elif JubesX.likes[RogueX.tag] >= 500:
            ch_v "I guess I've seen her around."
        elif JubesX.likes[RogueX.tag] >= 400:
            ch_v "Ugh, don't get me started."
        elif JubesX.likes[RogueX.tag] >= 300:
            ch_v "So annoying!"
        else:
            ch_v "Bitch."
    elif Check == KittyX:
        if "poly Kitty" in JubesX.traits:
            ch_v "Well, she's fun in the sack. . ."
        elif JubesX.likes[KittyX.tag] >= 900:
            ch_v "She's so. . . perky. . ."
        elif JubesX.likes[KittyX.tag] >= 800:
            ch_v "She's fit. . ."
        elif JubesX.likes[KittyX.tag] >= 700:
            ch_v "Kinda slippery. . ."
        elif JubesX.likes[KittyX.tag] >= 600:
            ch_v "She's cool."
        elif JubesX.likes[KittyX.tag] >= 500:
            ch_v "I guess I've seen her around."
        elif JubesX.likes[KittyX.tag] >= 400:
            ch_v "Ugh, don't get me started."
        elif JubesX.likes[KittyX.tag] >= 300:
            ch_v "So whiney!"
        else:
            ch_v "Bitch."
    elif Check == EmmaX:
        if "poly Emma" in JubesX.traits:
            ch_v "Well, she's fun in the sack. . ."
        elif JubesX.likes[EmmaX.tag] >= 900:
            ch_v "Such amazing tits!"
        elif JubesX.likes[EmmaX.tag] >= 800:
            ch_v "What a figure on her. . ."
        elif JubesX.likes[EmmaX.tag] >= 700:
            ch_v "She's a cool teach. . ."
        elif JubesX.likes[EmmaX.tag] >= 600:
            ch_v "She's fine. . ."
        elif JubesX.likes[EmmaX.tag] >= 500:
            ch_v "I don't mind her."
        elif JubesX.likes[EmmaX.tag] >= 400:
            ch_v "Kinda a pain in the ass, right?"
        elif JubesX.likes[EmmaX.tag] >= 300:
            ch_v "She gives me a headache."
        else:
            ch_v "Witch."
    elif Check == LauraX:
        if "poly Laura" in JubesX.traits:
            ch_v "Well, she's fun in the sack. . ."
        elif JubesX.likes[LauraX.tag] >= 900:
            ch_v "What a minx!"
        elif JubesX.likes[LauraX.tag] >= 800:
            ch_v "She smells dangerous. . ."
        elif JubesX.likes[LauraX.tag] >= 700:
            ch_v "She's one tough cookie."
        elif JubesX.likes[LauraX.tag] >= 600:
            ch_v "She's a lot of fun."
        elif JubesX.likes[LauraX.tag] >= 500:
            ch_v "She's fine."
        elif JubesX.likes[LauraX.tag] >= 400:
            ch_v "She can be a jerk."
        elif JubesX.likes[LauraX.tag] >= 300:
            ch_v "She needs to mind her business."
        else:
            ch_v "Grrrrr."
    elif Check == JeanX:
        if "poly Jean" in JubesX.traits:
            ch_v "Well, she's fun in the sack. . ."
        elif JubesX.likes[JeanX.tag] >= 900:
            ch_v "She is pretty hot. . ."
        elif JubesX.likes[JeanX.tag] >= 800:
            ch_v "She's not bad looking. . ."
        elif JubesX.likes[JeanX.tag] >= 700:
            ch_v "She's. . . tolerable."
        elif JubesX.likes[JeanX.tag] >= 600:
            ch_v "I guess she's fine?"
        elif JubesX.likes[JeanX.tag] >= 500:
            ch_v "She's kind of a lot of a lot."
        elif JubesX.likes[JeanX.tag] >= 400:
            ch_v "She needs to cut it out with that mind BS."
        elif JubesX.likes[JeanX.tag] >= 300:
            ch_v "Hate her."
        else:
            ch_v "Bitch."
    elif Check == StormX:
        if "poly Storm" in JubesX.traits:
            ch_v "Well, she's fun in the sack. . ."
        elif JubesX.likes[StormX.tag] >= 900:
            ch_v "She's totally thicc, right?"
        elif JubesX.likes[StormX.tag] >= 800:
            ch_v "She's so beautiful. . ."
        elif JubesX.likes[StormX.tag] >= 700:
            ch_v "She's makes sure to get me my homework."
        elif JubesX.likes[StormX.tag] >= 600:
            ch_v "She's a great teach."
        elif JubesX.likes[StormX.tag] >= 500:
            ch_v "She's cool."
        elif JubesX.likes[StormX.tag] >= 400:
            ch_v "She can be mean."
        elif JubesX.likes[StormX.tag] >= 300:
            ch_v "She needs to stay out of my business."
        else:
            ch_v "Witch."
    return


label Jubes_Monogamy:

    menu:
        "Could you not hook up with other girls?" if "monogamous" not in JubesX.traits:
            if JubesX.thirst >= 60 and not approval_check(JubesX, 1700, "LO", taboo_modifier=0):

                $ JubesX.change_face("sly", 1)
                if "monogamous" not in JubesX.daily_history:
                    call change_Girl_stat(JubesX, "obedience", -2)
                ch_v "I could, but where would the fun in that be?"
                return
            elif approval_check(JubesX, 1200, "LO", taboo_modifier=0) and JubesX.love >= JubesX.obedience:

                $ JubesX.change_face("sly", 1)
                if "monogamous" not in JubesX.daily_history:
                    call change_Girl_stat(JubesX, "love", 1)
                ch_v "Oh. . . want me for yourself?."
                ch_v "Fine, I'll be more careful. . ."
            elif approval_check(JubesX, 700, "O", taboo_modifier=0):

                $ JubesX.change_face("sly", 1, eyes = "side")
                ch_v "Sure."
            else:

                $ JubesX.change_face("sly", 1)
                ch_v "Nah."
                return
            if "monogamous" not in JubesX.daily_history:
                call change_Girl_stat(JubesX, "obedience", 3)
            $ JubesX.add_word(1, 0, "monogamous")
            $ JubesX.traits.append("monogamous")
        "Don't hook up with other girls." if "monogamous" not in JubesX.traits:
            if approval_check(JubesX, 900, "O", taboo_modifier=0):

                $ JubesX.change_face("sly", 1, eyes = "side")
                ch_v "Fine."
            elif JubesX.thirst >= 60 and not approval_check(JubesX, 1700, "LO", taboo_modifier=0):

                $ JubesX.change_face("sly", 1)
                if "monogamous" not in JubesX.daily_history:
                    call change_Girl_stat(JubesX, "obedience", -2)
                ch_v "I could, but where would the fun in that be?"
                return
            elif approval_check(JubesX, 600, "O", taboo_modifier=0):

                $ JubesX.change_face("sly", 1, eyes = "side")
                ch_v "If you insist."
            elif approval_check(JubesX, 1400, "LO", taboo_modifier=0):

                $ JubesX.change_face("sly", 1)
                ch_v "Yeah, ok, but ask nicely next time."
            else:

                $ JubesX.change_face("sly", 1, brows = "confused")
                ch_v "Nah."
                return
            if "monogamous" not in JubesX.daily_history:
                call change_Girl_stat(JubesX, "obedience", 3)
            $ JubesX.add_word(1, 0, "monogamous")
            $ JubesX.traits.append("monogamous")
        "It's ok if you hook up with other girls." if "monogamous" in JubesX.traits:
            if approval_check(JubesX, 700, "O", taboo_modifier=0):
                $ JubesX.change_face("sly", 1, eyes = "side")
                ch_v "Cool, cool."
            elif approval_check(JubesX, 800, "L", taboo_modifier=0):
                $ JubesX.change_face("sly", 1)
                ch_v "Ok, but make sure you make it up to me. . ."
            else:
                $ JubesX.change_face("sly", 1, brows = "confused")
                if "monogamous" not in JubesX.daily_history:
                    call change_Girl_stat(JubesX, "love", -2)
                ch_v "Nice. . ."
            if "monogamous" not in JubesX.daily_history:
                call change_Girl_stat(JubesX, "obedience", 3)
            if "monogamous" in JubesX.traits:
                $ JubesX.traits.remove("monogamous")
            $ JubesX.add_word(1, 0, "monogamous")
        "Never mind.":
            pass
    return



label Jubes_Jumped:

    ch_p "Hey, Remember that time you threw yourself at me?"
    $ JubesX.change_face("sly", 1, brows = "confused")
    menu:
        ch_v "Yeah?"
        "Could you maybe just ask instead?" if "chill" not in JubesX.traits:
            if JubesX.thirst >= 60 and not approval_check(JubesX, 1500, "LO", taboo_modifier=0):

                $ JubesX.change_face("sly", 1)
                if "chill" not in JubesX.daily_history:
                    call change_Girl_stat(JubesX, "obedience", -2)
                ch_v "Hey, better you than one of these other bloodbags. . ."
                return
            elif approval_check(JubesX, 1000, "LO", taboo_modifier=0) and JubesX.love >= JubesX.obedience:

                $ JubesX.change_face("surprised", 1)
                if "chill" not in JubesX.daily_history:
                    call change_Girl_stat(JubesX, "love", 1)
                ch_v "Sorry, I. . . have needs. . ."
                $ JubesX.change_face("sly", 1, eyes = "side")
                ch_v "I'll do better. . ."
            elif approval_check(JubesX, 500, "O", taboo_modifier=0):

                $ JubesX.change_face("sly", 1, eyes = "side")
                ch_v "Sorry. . ."
            else:

                $ JubesX.change_face("sly", 1)
                ch_v "We'll see. . ."
                return
            if "chill" not in JubesX.daily_history:
                call change_Girl_stat(JubesX, "obedience", 3)
            $ JubesX.add_word(1, 0, "chill")
            $ JubesX.traits.append("chill")
        "Don't bother me like that." if "chill" not in JubesX.traits:
            if approval_check(JubesX, 800, "O", taboo_modifier=0):

                $ JubesX.change_face("sly", 1, eyes = "side")
                ch_v "Fine."
            elif JubesX.thirst >= 60 and not approval_check(JubesX, 500, "O", taboo_modifier=0):

                $ JubesX.change_face("sly", 1)
                if "chill" not in JubesX.daily_history:
                    call change_Girl_stat(JubesX, "obedience", -2)
                ch_v "Sorry, I. . . have needs. . ."
                return
            elif approval_check(JubesX, 400, "O", taboo_modifier=0):

                $ JubesX.change_face("sly", 1, eyes = "side")
                ch_v "Sure. . ."
            elif approval_check(JubesX, 500, "LO", taboo_modifier=0) and not approval_check(JubesX, 500, "I", taboo_modifier=0):

                $ JubesX.change_face("sly", 1)
                ch_v "Hey, don't come at me like that."
                ch_v "I can try though. . ."
            else:

                $ JubesX.change_face("sly", 1)
                ch_v "We'll see. . ."
                return
            if "chill" not in JubesX.daily_history:
                call change_Girl_stat(JubesX, "obedience", 3)
            $ JubesX.add_word(1, 0, "chill")
            $ JubesX.traits.append("chill")
        "Knock yourself out.":
            if approval_check(JubesX, 800, "L", taboo_modifier=0):
                $ JubesX.change_face("sly", 1)
                ch_v "Game on. . ."
            elif approval_check(JubesX, 700, "O", taboo_modifier=0):
                $ JubesX.change_face("sly", 1, eyes = "side")
                ch_v "You got it!"
            else:
                $ JubesX.change_face("sly", 1, brows = "confused")
                if "chill" not in JubesX.daily_history:
                    call change_Girl_stat(JubesX, "love", -2)
                ch_v "Yeah, we'll see. . ."
            if "chill" not in JubesX.daily_history:
                call change_Girl_stat(JubesX, "obedience", 3)
            if "chill" in JubesX.traits:
                $ JubesX.traits.remove("chill")
            $ JubesX.add_word(1, 0, "chill")
        "Um, never mind.":
            pass
    return




label Jubes_Hungry:
    if JubesX.had_chat[3]:
        ch_v "[[licks her lips] I'm a little thirsty. . ."
    elif JubesX.had_chat[2]:
        ch_v "I really love that serum you whipped up."
    else:
        ch_v "[[licks her lips] I'm a little thirsty. . ."
    $ JubesX.traits.append("hungry")
return





label Jubes_SexChat:
    $ line = "Yeah, what did you want to talk about?" if not line else line
    while True:
        menu:
            ch_v "[line]"
            "My favorite thing to do is. . .":
                if "setfav" in JubesX.daily_history:
                    ch_v "I remember."
                else:
                    menu:
                        "Sex.":
                            $ JubesX.change_face("sly")
                            if JubesX.player_favorite_action == "sex":
                                call change_Girl_stat(JubesX, "lust", 5)
                                ch_v "Yeah, I know that. . ."
                            elif JubesX.favorite_action == "sex":
                                call change_Girl_stat(JubesX, "love", 5)
                                call change_Girl_stat(JubesX, "lust", 10)
                                ch_v "I really like it too!"
                            elif JubesX.permanent_History["sex"] >= 5:
                                ch_v "Well I don't mind that."
                            elif not JubesX.permanent_History["sex"]:
                                $ JubesX.change_face("perplexed")
                                ch_v "Who's fucking you?"
                            else:
                                $ JubesX.change_face("bemused")
                                ch_v "Heh, um, yeah, it's nice. . ."
                            $ JubesX.player_favorite_action = "sex"
                        "Anal.":

                            $ JubesX.change_face("sly")
                            if JubesX.player_favorite_action == "anal":
                                call change_Girl_stat(JubesX, "lust", 5)
                                ch_v "So you've said. . ."
                            elif JubesX.favorite_action == "anal":
                                call change_Girl_stat(JubesX, "love", 5)
                                call change_Girl_stat(JubesX, "lust", 10)
                                ch_v "I love it too!"
                            elif JubesX.permanent_History["anal"] >= 10:
                                ch_v "Yeah, it's. . . nice. . ."
                            elif not JubesX.permanent_History["anal"]:
                                $ JubesX.change_face("perplexed")
                                ch_v "Who's fucking you?"
                            else:
                                $ JubesX.change_face("bemused", eyes = "side")
                                ch_v "Heh, heh, yeah, um, it's ok. . ."
                            $ JubesX.player_favorite_action = "anal"
                        "Blowjobs.":

                            $ JubesX.change_face("sly")
                            if JubesX.player_favorite_action == "blowjob":
                                call change_Girl_stat(JubesX, "lust", 3)
                                ch_v "Definitely."
                            elif JubesX.favorite_action == "blowjob":
                                call change_Girl_stat(JubesX, "love", 5)
                                call change_Girl_stat(JubesX, "lust", 5)
                                ch_v "Me too!"
                            elif JubesX.permanent_History["blowjob"] >= 10:
                                ch_v "Yeah, you're delicious."
                            elif not JubesX.permanent_History["blowjob"]:
                                $ JubesX.change_face("perplexed")
                                ch_v "Who's sucking your dick?!"
                            else:
                                $ JubesX.change_face("bemused")
                                ch_v "I'm. . . it's really good. . ."
                            $ JubesX.player_favorite_action = "blowjob"
                        "Titjobs.":

                            $ JubesX.change_face("sly")
                            if JubesX.player_favorite_action == "titjob":
                                call change_Girl_stat(JubesX, "lust", 5)
                                ch_v "Yeah, you've said that before. . ."
                            elif JubesX.favorite_action == "titjob":
                                call change_Girl_stat(JubesX, "love", 5)
                                call change_Girl_stat(JubesX, "lust", 7)
                                ch_v "Yeah, I enjoy that too. . ."
                            elif JubesX.permanent_History["titjob"] >= 10:
                                ch_v "It's certainly an interesting experience . . ."
                            elif not JubesX.permanent_History["titjob"]:
                                $ JubesX.change_face("perplexed")
                                ch_v "Who's titfucking you?"
                            else:
                                $ JubesX.change_face("bemused")
                                ch_v "That's nice of you to say. . ."
                                call change_Girl_stat(JubesX, "love", 5)
                                call change_Girl_stat(JubesX, "inhibition", 10)
                            $ JubesX.player_favorite_action = "titjob"
                        "Footjobs.":

                            $ JubesX.change_face("sly")
                            if JubesX.player_favorite_action == "footjob":
                                call change_Girl_stat(JubesX, "lust", 5)
                                ch_v "Yeah, you've said that. . ."
                            elif JubesX.favorite_action == "footjob":
                                call change_Girl_stat(JubesX, "love", 5)
                                call change_Girl_stat(JubesX, "lust", 7)
                                ch_v "I do like using my feet. . ."
                            elif JubesX.permanent_History["footjob"] >= 10:
                                ch_v "I like it too . . ."
                            elif not JubesX.permanent_History["footjob"]:
                                $ JubesX.change_face("perplexed")
                                ch_v "Who's playing footsie with you?"
                            else:
                                $ JubesX.change_face("bemused")
                                ch_v "Yeah, it's nice. . ."
                            $ JubesX.player_favorite_action = "footjob"
                        "Handjobs.":

                            $ JubesX.change_face("sly")
                            if JubesX.player_favorite_action == "handjob":
                                call change_Girl_stat(JubesX, "lust", 5)
                                ch_v "Yeah, you've said that. . ."
                            elif JubesX.favorite_action == "handjob":
                                call change_Girl_stat(JubesX, "love", 5)
                                call change_Girl_stat(JubesX, "lust", 7)
                                ch_v "You do feel pretty comfy. . ."
                            elif JubesX.permanent_History["handjob"] >= 10:
                                ch_v "I like it too . . ."
                            elif not JubesX.permanent_History["handjob"]:
                                $ JubesX.change_face("perplexed")
                                ch_v "Who's jerking you off?"
                            else:
                                $ JubesX.change_face("bemused")
                                ch_v "Yeah, it's nice. . ."
                            $ JubesX.player_favorite_action = "handjob"
                        "Feeling you up.":

                            $ counter = JubesX.permanent_History["fondle_breasts"]+ JubesX.permanent_History["fondle_thighs"]+ JubesX.permanent_History["suck_breasts"] + JubesX.permanent_History["hotdog"]
                            $ JubesX.change_face("sly")
                            if JubesX.player_favorite_action == "fondle":
                                call change_Girl_stat(JubesX, "lust", 3)
                                ch_v "Yeah, I think we're clear on that. . ."
                            elif JubesX.favorite_action in ("hotdog", "suck_breasts", "fondle_breasts", "fondle_thighs"):
                                call change_Girl_stat(JubesX, "love", 5)
                                call change_Girl_stat(JubesX, "lust", 5)
                                ch_v "I love when you touch me. . ."
                            elif counter >= 10:
                                ch_v "Yeah, it's really nice . . ."
                            elif not counter:
                                $ JubesX.change_face("perplexed")
                                ch_v "Who's letting you feel her up?"
                            else:
                                $ JubesX.change_face("bemused")
                                ch_v "I do like how that feels. . ."
                            $ JubesX.player_favorite_action = "fondle"
                            $ counter = 0
                        "Kissing you.":

                            $ JubesX.change_face("sly")
                            if JubesX.player_favorite_action == "kiss":
                                call change_Girl_stat(JubesX, "love", 3)
                                ch_v "Mmmmm. . ."
                            elif JubesX.favorite_action == "kiss":
                                call change_Girl_stat(JubesX, "love", 5)
                                call change_Girl_stat(JubesX, "lust", 5)
                                ch_v "Hmm, the taste of you on my lips. . ."
                            elif JubesX.permanent_History["kiss"] >= 10:
                                ch_v "I love kissing you too . . ."
                            elif not JubesX.permanent_History["kiss"]:
                                $ JubesX.change_face("perplexed")
                                ch_v "Who are you kissing?"
                            else:
                                $ JubesX.change_face("bemused")
                                ch_v "I love kissing you too. . ."
                            $ JubesX.player_favorite_action = "kiss"

                    $ JubesX.daily_history.append("setfav")
            "What's your favorite thing to do?":

                if not approval_check(JubesX, 800):
                    $ JubesX.change_face("perplexed")
                    ch_v ". . ."
                else:
                    if JubesX.SEXP >= 50:
                        $ JubesX.change_face("sly")
                        ch_v "You should know. . ."
                    else:
                        $ JubesX.change_face("bemused")
                        $ JubesX.eyes = "side"
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
                    $ JubesX.change_face("perplexed")
                    ch_v "Make up your mind."
                else:
                    if approval_check(JubesX, 1000) and JubesX.obedience <= JubesX.love:
                        $ JubesX.change_face("bemused")
                        call change_Girl_stat(JubesX, "obedience", 1)
                        ch_v "Keep quiet, fine."
                        $ JubesX.traits.remove("vocal")
                    elif approval_check(JubesX, 700, "O"):
                        $ JubesX.change_face("sadside")
                        call change_Girl_stat(JubesX, "obedience", 1)
                        ch_v ". . ."
                        $ JubesX.traits.remove("vocal")
                    elif approval_check(JubesX, 600):
                        $ JubesX.change_face("sly")
                        call change_Girl_stat(JubesX, "love", -3)
                        call change_Girl_stat(JubesX, "obedience", -1)
                        call change_Girl_stat(JubesX, "inhibition", 5)
                        ch_v "Don't push it, [JubesX.player_petname]."
                    else:
                        $ JubesX.change_face("angry")
                        call change_Girl_stat(JubesX, "love", -5)
                        call change_Girl_stat(JubesX, "obedience", -3)
                        call change_Girl_stat(JubesX, "inhibition", 10)
                        ch_v "Nah."

                    $ JubesX.daily_history.append("setvocal")
            "Talk dirty to me during sex." if "vocal" not in JubesX.traits:
                if "setvocal" in JubesX.daily_history:
                    $ JubesX.change_face("perplexed")
                    ch_v "Heard you the first time."
                else:
                    if approval_check(JubesX, 1000) and JubesX.obedience <= JubesX.love:
                        $ JubesX.change_face("sly")
                        call change_Girl_stat(JubesX, "obedience", 2)
                        ch_v "Louder? I can do loud. . ."
                        $ JubesX.traits.append("vocal")
                    elif approval_check(JubesX, 700, "O"):
                        $ JubesX.change_face("sadside")
                        call change_Girl_stat(JubesX, "obedience", 2)
                        ch_v "If 'ya want, [JubesX.player_petname]."
                        $ JubesX.traits.append("vocal")
                    elif approval_check(JubesX, 600):
                        $ JubesX.change_face("sly")
                        call change_Girl_stat(JubesX, "obedience", 3)
                        ch_v "Sure?"
                        $ JubesX.traits.append("vocal")
                    else:
                        $ JubesX.change_face("angry")
                        call change_Girl_stat(JubesX, "inhibition", 5)
                        ch_v ". . ."

                    $ JubesX.daily_history.append("setvocal")


            "Don't do your own thing as much during sex." if "passive" not in JubesX.traits:
                if "initiative" in JubesX.daily_history:
                    $ JubesX.change_face("perplexed")
                    ch_v "Heard you the first time."
                else:
                    if approval_check(JubesX, 1200) and JubesX.obedience <= JubesX.love:
                        $ JubesX.change_face("bemused")
                        call change_Girl_stat(JubesX, "obedience", 1)
                        ch_v "Ok, you can take the lead. . ."
                        $ JubesX.traits.append("passive")
                    elif approval_check(JubesX, 700, "O"):
                        $ JubesX.change_face("sadside")
                        call change_Girl_stat(JubesX, "obedience", 1)
                        ch_v "I'll try to restrain myself. . ."
                        $ JubesX.traits.append("passive")
                    elif approval_check(JubesX, 600):
                        $ JubesX.change_face("sly")
                        call change_Girl_stat(JubesX, "love", -3)
                        call change_Girl_stat(JubesX, "obedience", -1)
                        call change_Girl_stat(JubesX, "inhibition", 5)
                        ch_v "Hm, no."
                    else:
                        $ JubesX.change_face("angry")
                        call change_Girl_stat(JubesX, "love", -5)
                        call change_Girl_stat(JubesX, "obedience", -3)
                        call change_Girl_stat(JubesX, "inhibition", 10)
                        ch_v "Uh-huh. . ."

                    $ JubesX.daily_history.append("initiative")
            "Take more initiative during sex." if "passive" in JubesX.traits:
                if "initiative" in JubesX.daily_history:
                    $ JubesX.change_face("perplexed")
                    ch_v "Heard you the first time."
                else:
                    if approval_check(JubesX, 1000) and JubesX.obedience <= JubesX.love:
                        $ JubesX.change_face("bemused")
                        call change_Girl_stat(JubesX, "obedience", 1)
                        ch_v "I can take the lead. . ."
                        $ JubesX.traits.remove("passive")
                    elif approval_check(JubesX, 700, "O"):
                        $ JubesX.change_face("sadside")
                        call change_Girl_stat(JubesX, "obedience", 1)
                        ch_v "Sure, no problem."
                        $ JubesX.traits.remove("passive")
                    elif approval_check(JubesX, 600):
                        $ JubesX.change_face("sly")
                        call change_Girl_stat(JubesX, "obedience", 3)
                        ch_v "We'll see."
                        $ JubesX.traits.remove("passive")
                    else:
                        $ JubesX.change_face("angry")
                        call change_Girl_stat(JubesX, "inhibition", 5)
                        ch_v "Meh."

                    $ JubesX.daily_history.append("initiative")

            "About getting Jumped" if "jumped" in JubesX.history:
                call Jubes_Jumped
            "About when you masturbate":
                call NoFap (JubesX)

            "Never mind" if line == "Yeah, what did you want to talk about?":
                return
            "That's all." if line != "Yeah, what did you want to talk about?":
                return
        if line == "Yeah, what did you want to talk about?":
            $ line = "Anything else?"
    return




label Jubes_Chitchat(O=0, Options = ["default", "default", "default"]):
    $ round -= 3 if round > 3 else (round-1)
    if O:
        $ Options = [O]
    else:

        if JubesX not in Player.Phonebook:
            if approval_check(JubesX, 500, "L") or approval_check(JubesX, 250, "I"):
                ch_v "Oh, here's my number, call me maybe."
                $ Player.Phonebook.append(JubesX)
                return
            elif approval_check(JubesX, 250, "O"):
                ch_v "If you need to call me, here's my number."
                $ Player.Phonebook.append(JubesX)
                return

        if "hungry" not in JubesX.traits and JubesX.permanent_History["swallowed"] >= 3 and JubesX.location == Player.location:
            call Jubes_Hungry
            return

        if Player.location != "bg_restaurant" and Player.location != "bg_halloween" and (not taboo or approval_check(JubesX, 800, "I")):
            if JubesX.location == Player.location and JubesX.thirst >= 30 and "refused" not in JubesX.daily_history and "quicksex" not in JubesX.daily_history:
                $ JubesX.change_face("sly", 1)
                ch_v "Hey, did you. . . wanna do something?"
                call Quick_Sex (JubesX)
                return




        if JubesX.event_happened[0] and "key" not in JubesX.had_chat:
            $ Options.append("key")

        if "mandrill" in Player.traits and "cologne chat" not in JubesX.daily_history:
            $ Options.append("mandrill")
        if "purple" in Player.traits and "cologne chat" not in JubesX.daily_history:
            $ Options.append("purple")
        if "corruption" in Player.traits and "cologne chat" not in JubesX.daily_history:
            $ Options.append("corruption")

        if "Jubes" not in JubesX.names:
            $ Options.append("jubes")

        if JubesX.went_on_date >= 1 and Player.location != "bg_restaurant":

            $ Options.append("dated")



        if JubesX.permanent_History["kiss"] >= 5:

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

            if "book" not in JubesX.had_chat:
                $ Options.append("booked")
        if "lace_bra" in JubesX.inventory or "lace_panties" in JubesX.inventory:

            if "lingerie" not in JubesX.had_chat:
                $ Options.append("lingerie")
        if JubesX.permanent_History["handjob"]:

            $ Options.append("handy")
        if JubesX.permanent_History["swallowed"]:

            $ Options.append("swallowed")
        if "cleaned" in JubesX.daily_history or "painted" in JubesX.daily_history:

            $ Options.append("facial")
        if JubesX.permanent_History["sleepover"]:

            $ Options.append("sleepwear")
        if JubesX.permanent_History["creampied"] or JubesX.permanent_History["anal_creampied"]:

            $ Options.append("creampie")
        if JubesX.permanent_History["sex"] or JubesX.permanent_History["anal"]:

            $ Options.append("sexed")
        if JubesX.permanent_History["anal"]:

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
        $ JubesX.change_face("confused")
        ch_v "(sniff, sniff). . . you smell like monkey butt . . ."
        ch_v ". . . why is that turning me on?"
        $ JubesX.change_face("sexy", 2)
    elif Options[0] == "purple":
        $ JubesX.daily_history.append("cologne chat")
        $ JubesX.change_face("sly", 1)
        ch_v "(sniff, sniff). . . that's an unusual scent. . ."
        $ JubesX.change_face("normal", 0)
        ch_v ". . . did you want something?"
    elif Options[0] == "corruption":
        $ JubesX.daily_history.append("cologne chat")
        $ JubesX.change_face("confused")
        ch_v "(sniff, sniff). . . that's. . . um, overpowering. . ."
        $ JubesX.change_face("angry")
        ch_v ". . . dangerous. . ."
        $ JubesX.change_face("sly")

    elif Options[0] == "caught":
        if "caught chat" in JubesX.had_chat:
            ch_v "We should try not to get caught like that."
            if not approval_check(JubesX, 500, "I"):
                ch_v "Unless. . ."
        else:
            ch_v "Sorry we got dragged into the Professor's office like that."
            if not approval_check(JubesX, 500, "I"):
                ch_v "I guess you wouldn't want to be so public anymore."
            else:
                ch_v "I kinda had fun though. . ."
            $ JubesX.had_chat.append("caught chat")
    elif Options[0] == "key":
        if JubesX.SEXP <= 15:
            ch_v "Be careful when you use that key . ."
        else:
            ch_v "I gave you a key, but you don't visit. . ."
        $ JubesX.had_chat.append("key")










    elif Options[0] == "contagious":
        $ JubesX.change_face("sadside", 2)
        ch_v "Just so you know, the vampire thing. . ."
        ch_v "It's not contagious. . ."
        $ JubesX.change_face("sadside", 1)
        ch_v "It was, but Dr. Strange was able to cast a spell or something."
        ch_v "So you don't need to worry about it spreading to you or anything."
        $ JubesX.change_face("sad", 1)
        $ JubesX.add_word(1, 0, 0, 0, "contagious")

    elif Options[0] == "jubes":

        ch_v "Oh, by the way, I also go by \"Jubes.\""
        ch_v "Thought you might wanna know that."
        $ JubesX.names.append("Jubes")
        $ JubesX.petnames.append("Jubes")
        menu:
            "Oh, that's cool, I think I'll call you that.":
                call change_Girl_stat(JubesX, "love", 5)
                $ JubesX.name = "Jubes"
            "Ok, but I like [JubesX.name].":
                call change_Girl_stat(JubesX, "love", 2)
                call change_Girl_stat(JubesX, "obedience", 2)
                $ JubesX.change_face("smile", 1)
                ch_v "Oh, ok."

    elif Options[0] == "dated":

        ch_v "I liked going out, haven't had too many chances at that lately."

    elif Options[0] == "kissed":

        $ JubesX.change_face("sly", 1)
        ch_v "You're a great kisser, [JubesX.player_petname]."
        menu:
            extend ""
            "Hey. . .I'm the best there is at what I do.":
                $ JubesX.change_face("smile", 1)
                ch_v "Well. . . maybe."
                ch_v "We'll have to test that one out."
            "No. You think?":
                ch_v "Would I have said it otherwise?"

    elif Options[0] == "dangerroom":

        $ JubesX.change_face("sly", 1)
        ch_v "Hey,[JubesX.player_petname]. I saw you in the Danger Room, earlier."
        ch_v "You're surprisingly good at this, considering you lack the ability to pewpew."

    elif Options[0] == "showercaught":

        if "shower" in JubesX.had_chat:
            ch_v "You saw me showering again. . ."
        else:
            ch_v "hey. don't you check before entering the showers?"
            $ JubesX.had_chat.append("shower")
            menu:
                extend ""
                "It was a total accident! I promise!":
                    call change_Girl_stat(JubesX, "love", 5)
                    call change_Girl_stat(JubesX, "love", 2)
                    if approval_check(JubesX, 1200):
                        $ JubesX.change_face("sly", 1)
                        ch_v "I didn't say I minded. . ."
                    $ JubesX.change_face("smile")
                    ch_v "Ok, sure, it's cool."
                "Just with you.":
                    call change_Girl_stat(JubesX, "obedience", 5)
                    if approval_check(JubesX, 1000) or approval_check(JubesX, 700, "L"):
                        call change_Girl_stat(JubesX, "love", 3)
                        $ JubesX.change_face("sly", 1)
                        ch_v "Well I guess that's kinda sweet. . ."
                    else:
                        call change_Girl_stat(JubesX, "love", -5)
                        $ JubesX.change_face("angry")
                        ch_v "Well, cut it out!"
                "Totally on purpose. I regret nothing.":
                    if approval_check(JubesX, 1200):
                        call change_Girl_stat(JubesX, "love", 3)
                        call change_Girl_stat(JubesX, "obedience", 10)
                        call change_Girl_stat(JubesX, "inhibition", 5)
                        $ JubesX.change_face("sly", 1)
                        ch_v "Fair."
                    elif approval_check(JubesX, 800):
                        call change_Girl_stat(JubesX, "obedience", 5)
                        call change_Girl_stat(JubesX, "inhibition", 5)
                        $ JubesX.change_face("perplexed", 2)
                        ch_v "Well, I guess I can't blame you. . ."
                        $ JubesX.blushing = "_blush1"
                    else:
                        call change_Girl_stat(JubesX, "love", -10)
                        call change_Girl_stat(JubesX, "love", -10)
                        call change_Girl_stat(JubesX, "obedience", 10)
                        $ JubesX.change_face("angry")
                        ch_v "That's. . . off-putting. . ."

    elif Options[0] == "fondled":

        ch_v "Hey, um, could you feel me up a little?"

    elif Options[0] == "booked":

        ch_v "Hey, I read those books you gave me."
        menu:
            extend ""
            "Yeah? Did you like them?":
                $ JubesX.change_face("sly", 2)
                ch_v "Well. . . yeah, I guess. . ."
            "Good. You looked like you could use to learn a thing or two from them.":
                call change_Girl_stat(JubesX, "love", -3)
                call change_Girl_stat(JubesX, "obedience", 5)
                call change_Girl_stat(JubesX, "inhibition", 5)
                $ JubesX.change_face("sad")
                ch_v "Well. . . I guess I could."
        $ JubesX.blushing = "_blush1"
        $ JubesX.had_chat.append("book")

    elif Options[0] == "lingerie":

        $ JubesX.change_face("sly", 2)
        ch_v "That underwear you got me was pretty nice. . . thanks."
        $ JubesX.blushing = "_blush1"
        $ JubesX.had_chat.append("lingerie")

    elif Options[0] == "handy":

        $ JubesX.change_face("sly", 1)
        ch_v "I was daydreaming about having your cock in my hand. . ."
        ch_v "Maybe I should take it out of the dream. . ."
        $ JubesX.blushing = ""

    elif Options[0] == "blowjob":
        if "blowjob" not in JubesX.had_chat:

            $ JubesX.change_face("sly", 2)
            ch_v "Hey, I didn't bite or anything, did I?"
            menu:
                extend ""
                "You were totally amazing.":
                    call change_Girl_stat(JubesX, "love", 5)
                    call change_Girl_stat(JubesX, "inhibition", 10)
                    $ JubesX.change_face("normal", 1)
                    ch_v "Cool. Cool. . . "
                    $ JubesX.change_face("sexy", 1)
                    ch_v "I'd like another taste sometime."
                "Honestly? It was good. . .but you could use a little practice, I think.":
                    if approval_check(JubesX, 300, "I") or not approval_check(JubesX, 800):
                        call change_Girl_stat(JubesX, "love", -5)
                        call change_Girl_stat(JubesX, "obedience", 10)
                        call change_Girl_stat(JubesX, "inhibition", 10)
                        $ JubesX.change_face("perplexed", 1)
                        ch_v "Oh! Sorry!."
                    else:
                        call change_Girl_stat(JubesX, "obedience", 15)
                        call change_Girl_stat(JubesX, "inhibition", 5)
                        $ JubesX.change_face("sexy", 1)
                        ch_v "Yeah? Well, practice makes perfect. . ."
                "I guess. If you're into weird sounds and too much teeth. Spoiler, I'm not.":
                    call change_Girl_stat(JubesX, "love", -5)
                    call change_Girl_stat(JubesX, "obedience", 5)
                    $ JubesX.change_face("sad", 2)
                    ch_v "Well. . . sorry about that. . ."
            $ JubesX.blushing = "_blush1"
            $ JubesX.had_chat.append("blowjob")
        else:
            $ line = renpy.random.choice(["You know, your dick tastes great.",
                            "I think I nearly dislocated my jaw last time.",
                            "Lemme know if you want another blowjob sometime.",
                            "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
            ch_v "[line]"

    elif Options[0] == "swallowed":

        if "swallow" in JubesX.had_chat:
            ch_v "I wouldn't mind another taste of your. . ."
        else:
            ch_v "So. . . the other day. . ."
            ch_v "I really got a charge out of drinking your. . ."
            $ JubesX.change_face("sly", 1)
            ch_v "I wouldn't mind that again some time."
            $ JubesX.had_chat.append("swallow")

    elif Options[0] == "facial":

        ch_v "Hey. . .I know this is kind of odd. . ."
        $ JubesX.change_face("sexy", 2)
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
        $ JubesX.change_face("sexy", 2)
        ch_v ". . .when I've been. . . enjoying myself. . ."
        ch_v "I've been thinking about you."
        $ JubesX.blushing = "_blush1"

    elif Options[0] == "anal":

        $ JubesX.change_face("sly")
        ch_v "I hadn't really done much anal before. . ."
        $ JubesX.change_face("sexy", 1)
        ch_v "Until you, at least."

    elif Options[0] == "seenpeen":
        $ JubesX.change_face("sly", 1, eyes = "down")
        ch_v "Oh, hey, you're swinging some real meat down there, huh?"
        $ JubesX.change_face("bemused", 1)
        call change_Girl_stat(JubesX, "love", 5)
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
        $ line = renpy.random.choice(["Get away from me.",
                "I don't want you anywhere near me.",
                "Back off.",
                "Fuck off."])
        ch_v "[line]"
    else:

        $ D20 = renpy.random.randint(1, 21)
        if D20 == 1:
            $ JubesX.change_face("smile")
            ch_v "It's nice being able to get out more. . ."
        else:






























































            $ JubesX.change_face("smile")
            ch_v "I like hanging with you."

    $ line = 0
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
                            $ JubesX.change_face("sexy", 1)
                            ch_v "I'm totally your girl, [JubesX.player_petname]."
                        else:
                            $ JubesX.change_face("angry")
                            ch_v "I am NOT your girl, [JubesX.player_petname]."
                    "\"boo\".":

                        $ JubesX.petname = "boo"
                        if "boyfriend" in JubesX.player_petnames or approval_check(JubesX, 700, "L"):
                            $ JubesX.change_face("sexy", 1)
                            ch_v "I am your boo, [JubesX.player_petname]."
                        else:
                            $ JubesX.change_face("angry")
                            ch_v "I'm NOT your boo, [JubesX.player_petname]."
                    "\"bae\".":

                        $ JubesX.petname = "bae"
                        if "boyfriend" in JubesX.player_petnames or approval_check(JubesX, 600, "L"):
                            $ JubesX.change_face("sexy", 1)
                            ch_v "I am your bae, [JubesX.player_petname]."
                        else:
                            $ JubesX.change_face("angry")
                            ch_v "I'm NOT your bae, [JubesX.player_petname]."
                    "\"baby\".":

                        $ JubesX.petname = "baby"
                        if "boyfriend" in JubesX.player_petnames or approval_check(JubesX, 500, "L"):
                            $ JubesX.change_face("sexy", 1)
                            ch_v "Cute, [JubesX.player_petname]."
                        else:
                            $ JubesX.change_face("angry")
                            ch_v "I am not your baby."
                    "\"sweetie\".":


                        $ JubesX.petname = "sweetie"
                        if "boyfriend" in JubesX.player_petnames or approval_check(JubesX, 600, "L"):
                            ch_v "Aw, that's sweet, [JubesX.player_petname]."
                        else:
                            $ JubesX.change_face("angry", 1)
                            ch_v "Too sweet, [JubesX.player_petname]."
                    "\"sexy\".":

                        $ JubesX.petname = "sexy"
                        if "lover" in JubesX.player_petnames or approval_check(JubesX, 800):
                            $ JubesX.change_face("sexy", 1)
                            ch_v "You know it, [JubesX.player_petname]."
                        else:
                            $ JubesX.change_face("angry", 1)
                            ch_v "I don't know, [JubesX.player_petname]."
                    "\"lover\".":

                        $ JubesX.petname = "lover"
                        if "lover" in JubesX.player_petnames or approval_check(JubesX, 1200):
                            $ JubesX.change_face("sexy", 1)
                            ch_v "I know."
                        else:
                            $ JubesX.change_face("angry", 1)
                            ch_v "I don't think so, [JubesX.player_petname]."
                    "Back":

                        pass
            "Risky":

                menu:
                    "I think I'll call you. . ."
                    "\"slave\".":
                        $ JubesX.petname = "slave"
                        if "master" in JubesX.player_petnames or approval_check(JubesX, 800, "O"):
                            $ JubesX.change_face("bemused", 1)
                            ch_v "As you wish, [JubesX.player_petname]."
                        else:
                            $ JubesX.change_face("angry", 1)
                            ch_v "I am not your slave, [JubesX.player_petname]."
                    "\"pet\".":

                        $ JubesX.petname = "pet"
                        if "master" in JubesX.player_petnames or approval_check(JubesX, 650, "O"):
                            $ JubesX.change_face("bemused", 1)
                            ch_v "You can pet me if you want, [JubesX.player_petname]."
                        else:
                            $ JubesX.change_face("angry", 1)
                            ch_v "I am no one's pet, [JubesX.player_petname]."
                    "\"slut\".":

                        $ JubesX.petname = "slut"
                        if "sex friend" in JubesX.player_petnames or approval_check(JubesX, 900, "OI"):
                            $ JubesX.change_face("sexy")
                            ch_v "Fair enough."
                        else:
                            $ JubesX.change_face("angry", 1)
                            $ JubesX.mouth = "surprised"
                            ch_v "Not with that mouth you don't."
                    "\"whore\".":

                        $ JubesX.petname = "whore"
                        if "fuckbuddy" in JubesX.player_petnames or approval_check(JubesX, 1000, "OI"):
                            $ JubesX.change_face("sly")
                            ch_v "Ouch. . ."
                        else:
                            $ JubesX.change_face("angry", 1)
                            ch_v "If either of us is going to be turning tricks. . ."
                    "\"sugartits\".":

                        $ JubesX.petname = "sugartits"
                        if "sex friend" in JubesX.player_petnames or approval_check(JubesX, 1400):
                            $ JubesX.change_face("sly", 1)
                            ch_v "Huh?"
                        else:
                            $ JubesX.change_face("angry", 1)
                            ch_v "Not cool."
                    "\"sex friend\".":

                        $ JubesX.petname = "sex friend"
                        if "sex friend" in JubesX.player_petnames or approval_check(JubesX, 600, "I"):
                            $ JubesX.change_face("sly")
                            ch_v "Yeah. . ."
                        else:
                            $ JubesX.change_face("angry", 1)
                            ch_v "Keep it down, [JubesX.player_petname]."
                    "\"fuckbuddy\".":

                        $ JubesX.petname = "fuckbuddy"
                        if "fuckbuddy" in JubesX.player_petnames or approval_check(JubesX, 700, "I"):
                            $ JubesX.change_face("sly")
                            ch_v "Yup."
                        else:
                            $ JubesX.change_face("angry", 1)
                            $ JubesX.mouth = "surprised"
                            ch_v "Not even, [JubesX.player_petname]."
                    "\"baby girl\".":

                        $ JubesX.petname = "baby girl"
                        if "daddy" in JubesX.player_petnames or approval_check(JubesX, 1200):
                            $ JubesX.change_face("smile", 1)
                            ch_v "I guess?"
                        else:
                            $ JubesX.change_face("angry", 1)
                            ch_v "Weirdo."

                    "\"Miss Lee\"." if "Miss Lee" in JubesX.names:
                        $ JubesX.petname = "Miss Lee"
                        if approval_check(JubesX, 900):
                            $ JubesX.change_face("bemused", 1)
                            ch_v "Ok, if that's what you're into, [JubesX.player_petname]."
                        else:
                            $ JubesX.change_face("sad", 1)
                            ch_v "That's kinda. . . formal, [JubesX.player_petname]."
                    "Back":

                        pass
            "Nevermind.":

                return
    return





label Jubes_Rename:

    $ JubesX.mouth = "smile"
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
                $ JubesX.change_face("bemused", 1)
                ch_v "Ok, if that's what you're into, [JubesX.player_petname]."
            else:
                $ JubesX.change_face("sad", 1)
                ch_v "That's kinda. . . formal, [JubesX.player_petname]."
        "Nevermind.":
            pass
    $ JubesX.add_word(1, 0, "namechange")
    return




label Jubes_Personality(counter=0):
    if not JubesX.had_chat[4] or counter:
        "Since you're doing well in one area, you can convince Jubes_sprite to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_v "Yeah? What's up?"
        "More Obedient. [[Love to Obedience]" if JubesX.love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_v "If you really care about that, sure."
            $ JubesX.had_chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if JubesX.love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_v "I could always be a bit more wild if that's what you want."
            $ JubesX.had_chat[4] = 2

        "Less Inhibited. [[Obedience to Inhibition]" if JubesX.obedience > 900:
            ch_p "I want you to be less inhibited."
            ch_v "I guess I could go all-out."
            $ JubesX.had_chat[4] = 3
        "More Loving. [[Obedience to Love]" if JubesX.obedience > 900:
            ch_p "I'd like you to learn to love me."
            ch_v "I can try."
            $ JubesX.had_chat[4] = 4

        "More Obedient. [[Inhibition to Obedience]" if JubesX.inhibition > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_v "I can give it a shot. . ."
            $ JubesX.had_chat[4] = 5

        "More Loving. [[Inhibition to Love]" if JubesX.inhibition > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_v "If that's something you need out of this. . ."
            $ JubesX.had_chat[4] = 6

        "I guess just do what you like. . .[[reset]" if JubesX.had_chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_v "Um, ok."
            $ JubesX.had_chat[4] = 0
        "Repeat the rules":
            call Jubes_Personality (1)
            return
        "Nevermind.":
            return
    return








    label Jubes_NoPantiesOn:
        menu:
            ch_v "I'm actually not wearing any?"
            "Then you could slip on a pair of panties. . .":
                if JubesX.seen_pussy and approval_check(JubesX, 1100, taboo_modifier=4):
                    $ JubesX.blushing = "_blush1"
                    ch_v "No, no, it's fine like this. . ."
                    $ JubesX.blushing = ""
                elif approval_check(JubesX, 1500, taboo_modifier=4):
                    $ JubesX.blushing = "_blush1"
                    ch_v "No, no, it's fine like this. . ."
                    $ JubesX.blushing = ""
                elif approval_check(JubesX, 700, taboo_modifier=4):
                    ch_v "I could, I guess. . ."
                    if "lace_panties" in JubesX.inventory:
                        $ JubesX.Clothes["underwear"]  = "lace_panties"
                    else:
                        $ JubesX.Clothes["underwear"] = "blue_panties"
                    if approval_check(JubesX, 1200, taboo_modifier=4):
                        $ line = JubesX.Clothes["bottom"]
                        $ JubesX.Outfit.remove_Clothing(["pants", "skirt"])
                        "She pulls off her [line] and slips on the [JubesX.Clothes[underwear].name]."
                    elif JubesX.Clothes["bottom"] == "skirt":
                        "She pulls out her [JubesX.Clothes[underwear].name] and pulls them up under her skirt."
                        $ JubesX.Outfit.remove_Clothing(["pants", "skirt"])
                        "Then she drops the skirt to the floor."
                    else:
                        $ line = JubesX.Clothes["bottom"]
                        $ JubesX.Outfit.remove_Clothing(["pants", "skirt"])
                        "She steps away a moment and then comes back wearing only the [JubesX.Clothes[underwear].name]."
                    return
                else:
                    ch_v "Nope."
                    return False
            "You could always just wear nothing at all. . .":

                if approval_check(JubesX, 1100, "LI", taboo_modifier = 3) and JubesX.love > JubesX.inhibition:
                    ch_v "True. . ."
                elif approval_check(JubesX, 700, "OI", taboo_modifier = 3) and JubesX.obedience > JubesX.inhibition:
                    ch_v "Sure. . ."
                elif approval_check(JubesX, 600, "I", taboo_modifier = 3):
                    ch_v "Hrmm. . ."
                elif approval_check(JubesX, 1300, taboo_modifier = 3):
                    ch_v "Fine."
                else:
                    $ JubesX.change_face("surprised")
                    $ JubesX.brows = "angry"
                    if JubesX.taboo > 20:
                        ch_v "Yeah, but not in public, [JubesX.player_petname]!"
                    else:
                        ch_v "Nah."
                    return False
            "Never mind.":

                ch_v "Ok. . ."
                return False
        return True




    menu Jubes_Clothes_Under:
        "Tops":
            menu:
                "How about you lose the [JubesX.Clothes[bra].name]?" if JubesX.Clothes["bra"]:
                    $ JubesX.change_face("bemused", 1)
                    if JubesX.seen_breasts and approval_check(JubesX, 900, taboo_modifier=2.7):
                        ch_v "Sure."
                    elif approval_check(JubesX, 1100, taboo_modifier=2):
                        if JubesX.taboo:
                            ch_v "I don't know, here. . ."
                        else:
                            ch_v "Maaaybe. . ."
                    elif JubesX.Clothes["jacket"] == "jacket" and approval_check(JubesX, 600, taboo_modifier=2):
                        ch_v "This jacket is a bit revealing. . ."
                    elif JubesX.Clothes["top"] and approval_check(JubesX, 500, taboo_modifier=2):
                        ch_v "I guess I could. . ."
                    elif not JubesX.Clothes["top"]:
                        call ask_for_dress_screen (JubesX)
                        if not _return:
                            ch_v "Not without something over it. . ."
                            return
                    else:
                        call ask_for_dress_screen (JubesX)
                        if not _return:
                            ch_v "Nah."
                            return
                    $ line = JubesX.Clothes["bra"]
                    $ JubesX.take_off("bra")
                    if JubesX.Clothes["jacket"]:
                        "She reaches under her jacket grabs her [line], and pulls it off, dropping it to the ground."
                    elif JubesX.Clothes["top"]:
                        "She reaches under her [JubesX.Clothes[top].name] grabs her [line], and pulls it off, dropping it to the ground."
                    else:
                        "She pulls off her [line] and drops it to the ground."
                        if not renpy.showing('dress_screen'):
                            call Jubes_First_Topless

                "Add sports_bra" if JubesX.Clothes["bra"] != "sports_bra":
                    ch_p "Try on that sports bra."
                    ch_v "Ok."
                    $ JubesX.Clothes["bra"] = "sports_bra"

                "Add lace_bra" if JubesX.Clothes["bra"] != "lace_bra" and "lace_bra" in JubesX.inventory:
                    ch_p "I like that bra corset."
                    if JubesX.seen_breasts or approval_check(JubesX, 1300, taboo_modifier=2):
                        ch_v "K."
                        $ JubesX.Clothes["bra"] = "lace_bra"
                    else:
                        call ask_for_dress_screen (JubesX)
                        if not _return:
                            ch_v "It's kinda revealing. . ."
                        else:
                            $ JubesX.Clothes["bra"] = "lace_bra"

                "Add bikini_top" if JubesX.Clothes["bra"] != "bikini_top" and "bikini_top" in JubesX.inventory:
                    ch_p "I like that bikini top."
                    if Player.location == "bg_pool":
                        ch_v "K."
                        $ JubesX.Clothes["bra"] = "bikini_top"
                    else:
                        if JubesX.seen_breasts or approval_check(JubesX, 1000, taboo_modifier=2):
                            ch_v "K."
                            $ JubesX.Clothes["bra"] = "bikini_top"
                        else:
                            call ask_for_dress_screen (JubesX)
                            if not _return:
                                ch_v "This is not really a \"bikini\" sort of place. . ."
                            else:
                                $ JubesX.Clothes["bra"] = "bikini_top"
                "Never mind":
                    pass
            return
        "Hose and stockings options":

            menu:
                "You could lose the hose." if JubesX.Clothes["hose"] and JubesX.Clothes["hose"] != 'ripped_tights' and JubesX.Clothes["hose"] != '_tights':
                    $ JubesX.take_off("hose")
                "The thigh-high hose would look good with that." if JubesX.Clothes["hose"] != "stockings":
                    $ JubesX.Clothes["hose"] = "stockings"
                "The pantyhose would look good with that." if JubesX.Clothes["hose"] != "pantyhose" and "pantyhose" in JubesX.inventory:
                    $ JubesX.Clothes["hose"] = "pantyhose"
                "The ripped pantyhose would look good with that." if JubesX.Clothes["hose"] != "ripped_pantyhose" and "ripped_pantyhose" in JubesX.inventory:
                    $ JubesX.Clothes["hose"] = "ripped_pantyhose"
                "The tall socks would look good with that." if JubesX.Clothes["hose"] != "socks" and "socks" in JubesX.inventory:
                    $ JubesX.Clothes["hose"] = "socks"
                "The stockings and garterbelt would look good with that." if JubesX.Clothes["hose"] != "stockings_and_garterbelt" and "stockings_and_garterbelt" in JubesX.inventory:
                    $ JubesX.Clothes["hose"] = "stockings_and_garterbelt"
                "Just the garterbelt would look good with that." if JubesX.Clothes["hose"] != "garterbelt" and "stockings_and_garterbelt" in JubesX.inventory:
                    $ JubesX.Clothes["hose"] = "garterbelt"
                "Never mind":
                    pass
            return
        "Panties":


            menu:
                "You could lose those panties. . ." if JubesX.Clothes["underwear"]:
                    $ JubesX.change_face("bemused", 1)
                    if approval_check(JubesX, 900) and (JubesX.Clothes["bottom"] or (JubesX.seen_pussy and not JubesX.taboo)):

                        if approval_check(JubesX, 850, "L"):
                            ch_v "True. . ."
                        elif approval_check(JubesX, 500, "O"):
                            ch_v "Right. . ."
                        elif approval_check(JubesX, 350, "I"):
                            ch_v "Heh."
                        else:
                            ch_v "Sure, I guess."
                    else:
                        if approval_check(JubesX, 1100, "LI", taboo_modifier = 3) and JubesX.love > JubesX.inhibition:
                            ch_v "I don't know, it's kinda public here. . ."
                        elif approval_check(JubesX, 700, "OI", taboo_modifier = 3) and JubesX.obedience > JubesX.inhibition:
                            ch_v "Well. . ."
                        elif approval_check(JubesX, 600, "I", taboo_modifier = 3):
                            ch_v "Hrmm. . ."
                        elif approval_check(JubesX, 1300, taboo_modifier = 3):
                            ch_v "Okay, fine."
                        else:
                            call ask_for_dress_screen (JubesX)
                            if not _return:
                                $ JubesX.change_face("surprised")
                                $ JubesX.brows = "angry"
                                if JubesX.taboo > 20:
                                    ch_v "This is just too public."
                                else:
                                    ch_v "Nah."
                                return
                    $ line = JubesX.Clothes["underwear"]
                    $ JubesX.take_off("underwear")
                    if not JubesX.Clothes["bottom"]:
                        "She pulls off her [line], then drops them to the ground."
                        if not renpy.showing('dress_screen'):
                            call Jubes_First_Bottomless
                    elif approval_check(JubesX, 1200, taboo_modifier=4):
                        $ temp_bottom = JubesX.Clothes["bottom"]
                        $ JubesX.Outfit.remove_Clothing(["pants", "skirt"])
                        pause 0.5
                        $ JubesX.Clothes["bottom"] = temp_bottom
                        "She pulls off her [JubesX.Clothes[bottom]] and [line], then pulls the [JubesX.Clothes[bottom].name] back on."
                        call Jubes_First_Bottomless (1)
                    elif JubesX.Clothes["bottom"] == "skirt":
                        "She reaches under her skirt and pulls her [line] off."
                    else:
                        $ JubesX.blushing = "_blush1"
                        "She steps away a moment and then comes back."
                        $ JubesX.blushing = ""
                    $ line = 0

                "Why don't you wear the blue panties instead?" if JubesX.Clothes["underwear"] and JubesX.Clothes["underwear"] != "blue_panties":
                    if approval_check(JubesX, 1100, taboo_modifier = 3):
                        ch_v "Ok."
                        $ JubesX.Clothes["underwear"] = "blue_panties"
                    else:
                        call ask_for_dress_screen (JubesX)
                        if not _return:
                            ch_v "That's none of your busines."
                        else:
                            $ JubesX.Clothes["underwear"] = "blue_panties"

                "Why don't you wear the lace panties instead?" if "lace_panties" in JubesX.inventory and JubesX.Clothes["underwear"] and JubesX.Clothes["underwear"] != "lace_panties":
                    if approval_check(JubesX, 1300, taboo_modifier = 3):
                        ch_v "I guess."
                        $ JubesX.Clothes["underwear"] = "lace_panties"
                    else:
                        call ask_for_dress_screen (JubesX)
                        if not _return:
                            ch_v "That's none of your busines."
                        else:
                            $ JubesX.Clothes["underwear"] = "lace_panties"

                "Why don't you wear the tiger panties instead?" if "tiger_panties" in JubesX.inventory and JubesX.Clothes["underwear"] and JubesX.Clothes["underwear"] != "tiger_panties":
                    if approval_check(JubesX, 1300, taboo_modifier = 3):
                        ch_v "I guess."
                        $ JubesX.Clothes["underwear"] = "tiger_panties"
                    else:
                        call ask_for_dress_screen (JubesX)
                        if not _return:
                            ch_v "That's none of your busines."
                        else:
                            $ JubesX.Clothes["underwear"] = "tiger_panties"

                "I like those bikini bottoms." if "bikini_bottoms" in JubesX.inventory and JubesX.Clothes["underwear"] != "bikini_bottoms":
                    if Player.location == "bg_pool":
                        ch_v "K."
                        $ JubesX.Clothes["underwear"] = "bikini_bottoms"
                    else:
                        if approval_check(JubesX, 1000, taboo_modifier=2):
                            ch_v "K."
                            $ JubesX.Clothes["underwear"] = "bikini_bottoms"
                        else:
                            call ask_for_dress_screen (JubesX)
                            if not _return:
                                ch_v "This is not really a \"bikini\" sort of place. . ."
                            else:
                                $ JubesX.Clothes["underwear"] = "bikini_bottoms"

                "You know, you could wear some panties with that. . ." if not JubesX.Clothes["underwear"]:
                    $ JubesX.change_face("bemused", 1)
                    if JubesX.Clothes["bottom"] and (JubesX.love+JubesX.obedience) <= (2*JubesX.inhibition):
                        $ JubesX.mouth = "smile"
                        ch_v "I don't know about that."
                        menu:
                            "Fine by me":
                                return
                            "I insist, put some on.":
                                if (JubesX.love+JubesX.obedience) <= (1.5*JubesX.inhibition):
                                    $ JubesX.change_face("angry", eyes = "side")
                                    ch_v "Well too bad."
                                    return
                                else:
                                    $ JubesX.change_face("sadside")
                                    ch_v "Oh, fine."
                    else:
                        ch_v "I guess. . ."
                    menu:
                        extend ""
                        "How about the blue ones?":
                            ch_v "Sure, ok."
                            $ JubesX.Clothes["underwear"] = "blue_panties"
                        "How about the lace ones?" if "lace_panties" in JubesX.inventory:
                            ch_v "Alright."
                            $ JubesX.Clothes["underwear"]  = "lace_panties"
                        "How about the tiger ones?" if "tiger_panties" in JubesX.inventory:
                            ch_v "Alright."
                            $ JubesX.Clothes["underwear"]  = "tiger_panties"
                        "How about the bikini bottoms?" if "bikini_bottoms" in JubesX.inventory:
                            ch_v "Alright."
                            $ JubesX.Clothes["underwear"]  = "bikini_bottoms"
                "Never mind":
                    pass
            return
        "Never mind":
            pass
    return




    menu Jubes_Clothes_Misc:

        "Shades in her hair" if JubesX.Clothes["hair"] != "shades":
            ch_p "You're missing those signature shades!"
            if approval_check(JubesX, 600):
                ch_v "Oh yeah!"
                $ JubesX.Clothes["hair"] = "shades"
            else:
                ch_v "I don't know, it's fine like this."

        "Shades out of her hair" if JubesX.Clothes["hair"] == "shades":
            ch_p "You should try without the shades."
            if approval_check(JubesX, 600):
                ch_v "Ok. . "
                $ JubesX.Clothes["hair"] = "short"
            else:
                ch_v "I don't know, it's fine like this."

        "Dry Hair" if JubesX.Clothes["hair"] == "wet":
            ch_p "Maybe dry out your hair."
            if approval_check(JubesX, 600):
                ch_v "Ok."
                $ JubesX.Clothes["hair"] = "short"
            else:
                ch_v "I don't know, it's fine like this."

        "Wet Hair style" if JubesX.Clothes["hair"] != "wet":
            ch_p "You should go for that wet look with your hair."
            if approval_check(JubesX, 800):
                ch_v "Hmm?"
                $ JubesX.Clothes["hair"] = "wet"
                "She wanders off for a minute and comes back."
                ch_v "Like this?"
            else:
                ch_v "Ugh, too much work."


        "Grow pubes" if not JubesX.pubes:
            ch_p "You know, I like some nice hair down there. Maybe grow it out."
            if "pubes" in JubesX.to_do:
                $ JubesX.change_face("bemused", 1)
                ch_v "It doesn't grow out over night!"
            else:
                $ JubesX.change_face("bemused", 1)
                if approval_check(JubesX, 1000, taboo_modifier=0):
                    ch_v "I guess I could. . ."
                else:
                    $ JubesX.change_face("surprised")
                    $ JubesX.brows = "angry"
                    ch_v "That's none of your business!"
                    return
                $ JubesX.to_do.append("pubes")
                $ JubesX.pubes_counter = 6
        "Shave pubes" if JubesX.pubes == "_hairy":
            ch_p "I like it waxed clean down there."
            $ JubesX.change_face("bemused", 1)
            if "shave" in JubesX.to_do:
                ch_v "I heard you, I'll get around to it."
            else:
                if approval_check(JubesX, 1100, taboo_modifier=0):
                    ch_v "That's how you like it then? . ."
                else:
                    $ JubesX.change_face("surprised")
                    $ JubesX.brows = "angry"
                    ch_v "That's none of your business!"
                    return
                $ JubesX.to_do.append("shave")

        "Piercings. [[See what she looks like without them first] (locked)" if not JubesX.seen_pussy and not JubesX.seen_breasts:
            pass

        "Add ring piercings" if JubesX.Clothes["piercings"] != "ring" and (JubesX.seen_pussy or JubesX.seen_breasts):
            ch_p "You know, you'd look really nice with some ring body piercings."
            if "ring" in JubesX.to_do:
                ch_v "I heard you, I'll get around to it."
            else:
                $ JubesX.change_face("bemused", 1)
                $ approval = approval_check(JubesX, 1150, taboo_modifier=0)
                if approval_check(JubesX, 900, "L", taboo_modifier=0) or (approval and JubesX.love > 2* JubesX.obedience):
                    ch_v "You think they'd look good on me?"
                elif approval_check(JubesX, 600, "I", taboo_modifier=0) or (approval and JubesX.inhibition > JubesX.obedience):
                    ch_v "I've been thinking about that for a while."
                elif approval_check(JubesX, 500, "O", taboo_modifier=0) or approval:
                    ch_v "Yes, [JubesX.player_petname]."
                else:
                    $ JubesX.change_face("surprised")
                    $ JubesX.brows = "angry"
                    ch_v "Not into it, [JubesX.player_petname]."
                    return
                $ JubesX.to_do.append("ring")

        "Add barbell piercings" if JubesX.Clothes["piercings"] != "barbell" and (JubesX.seen_pussy or JubesX.seen_breasts):
            ch_p "You know, you'd look really nice with some barbell body piercings."
            if "barbell" in JubesX.to_do:
                ch_v "I heard you, I'll get around to it."
            else:
                $ JubesX.change_face("bemused", 1)
                $ approval = approval_check(JubesX, 1150, taboo_modifier=0)
                if approval_check(JubesX, 900, "L", taboo_modifier=0) or (approval and JubesX.love > 2*JubesX.obedience):
                    ch_v "You think they'd look good on me?"
                elif approval_check(JubesX, 600, "I", taboo_modifier=0) or (approval and JubesX.inhibition > JubesX.obedience):
                    ch_v "I've been thinking about that for a while."
                elif approval_check(JubesX, 500, "O", taboo_modifier=0) or approval:
                    ch_v "Yes, [JubesX.player_petname]."
                else:
                    $ JubesX.change_face("surprised")
                    $ JubesX.brows = "angry"
                    ch_v "Not into it, [JubesX.player_petname]."
                    return
                $ JubesX.to_do.append("barbell")

        "Remove piercings" if JubesX.Clothes["piercings"]:
            ch_p "You know, you'd look better without those piercings."
            $ JubesX.change_face("bemused", 1)
            $ approval = approval_check(JubesX, 1350, taboo_modifier=0)
            if approval_check(JubesX, 950, "L", taboo_modifier=0) or (approval and JubesX.love > JubesX.obedience):
                ch_v "Make up your mind . ."
            elif approval_check(JubesX, 700, "I", taboo_modifier=0) or (approval and JubesX.inhibition > JubesX.obedience):
                ch_v "Well, this is annoying. . ."
            elif approval_check(JubesX, 600, "O", taboo_modifier=0) or approval:
                ch_v "Fine."
            else:
                $ JubesX.change_face("surprised")
                $ JubesX.brows = "angry"
                ch_v "I really like them though!"
                return
            $ JubesX.take_off("piercings")
        "Never mind":

            pass
    return


return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
