label Laura_Relationship:
    while True:
        menu:
            ch_l "What did you want to talk about?"
            "Do you want to be my girlfriend?" if LauraX not in Player.Harem and "ex" not in LauraX.traits:
                $ LauraX.daily_history.append("relationship")
                if "asked boyfriend" in LauraX.daily_history and "angry" in LauraX.daily_history:
                    $ LauraX.change_face("angry", 1)
                    ch_l "Like I said, not interested."
                    return
                elif "asked boyfriend" in LauraX.daily_history:
                    $ LauraX.change_face("angry", 1)
                    ch_l "Still a no."
                    return
                elif LauraX.broken_up[0]:
                    $ LauraX.change_face("angry", 1)
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

                if LauraX.event_happened[5]:
                    $ LauraX.change_face("bemused", 1)
                    ch_l "I asked, you said \"no\". . ."
                else:
                    $ LauraX.change_face("surprised", 2)
                    ch_l "Huh? . ."
                    $ LauraX.change_face("smile", 1)

                call Laura_OtherWoman

                if LauraX.love >= 800:
                    $ LauraX.change_face("surprised", 1)
                    $ LauraX.mouth = "smile"
                    call change_Girl_stat(LauraX, "love", 40)
                    ch_l "Sure!"
                    if "boyfriend" not in LauraX.player_petnames:
                        $ LauraX.player_petnames.append("boyfriend")
                    if "LauraYes" in Player.traits:
                        $ Player.traits.remove("LauraYes")
                    $ Player.Harem.append(LauraX)
                    call Harem_Initiation
                    "[LauraX.name] tackles you and kisses you deeply."
                    $ LauraX.change_face("kiss", 1)
                    $ LauraX.permanent_History["kiss"] += 1
                elif LauraX.obedience >= 500:
                    $ LauraX.change_face("perplexed")
                    ch_l "I don't know, \"dating\". . ."
                elif LauraX.inhibition >= 500:
                    $ LauraX.change_face("smile")
                    ch_l "Nah, this is more fun."
                else:
                    $ LauraX.change_face("perplexed", 1)
                    ch_l "Whoa, slow down, [LauraX.player_petname]."

            "Do you want to get back together?" if "ex" in LauraX.traits:
                $ LauraX.daily_history.append("relationship")
                if "asked boyfriend" in LauraX.daily_history and "angry" in LauraX.daily_history:
                    $ LauraX.change_face("angry", 1)
                    ch_l "Like I said, not interested."
                    return
                elif "asked boyfriend" in LauraX.daily_history:
                    $ LauraX.change_face("angry", 1)
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
                    $ LauraX.change_face("surprised", 1)
                    $ LauraX.mouth = "smile"
                    call change_Girl_stat(LauraX, "love", 5)
                    ch_l "Ok, you've earned another shot!"
                    if "boyfriend" not in LauraX.player_petnames:
                        $ LauraX.player_petnames.append("boyfriend")
                    $ LauraX.traits.remove("ex")
                    if "LauraYes" in Player.traits:
                        $ Player.traits.remove("LauraYes")
                    $ Player.Harem.append(LauraX)
                    call Harem_Initiation
                    "[LauraX.name] pulls you in and kisses you deeply."
                    $ LauraX.change_face("kiss", 1)
                    $ LauraX.permanent_History["kiss"] += 1
                elif LauraX.love >= 600 and approval_check(LauraX, 1500):
                    $ LauraX.change_face("smile", 1)
                    call change_Girl_stat(LauraX, "love", 5)
                    ch_l "Um, ok, I guess."
                    if "boyfriend" not in LauraX.player_petnames:
                        $ LauraX.player_petnames.append("boyfriend")
                    $ LauraX.traits.remove("ex")
                    if "LauraYes" in Player.traits:
                        $ Player.traits.remove("LauraYes")
                    $ Player.Harem.append(LauraX)
                    call Harem_Initiation
                    $ LauraX.change_face("kiss", 1)
                    "[LauraX.name] gives you a quick kiss."
                    $ LauraX.change_face("sly", 1)
                    $ LauraX.permanent_History["kiss"] += 1
                elif LauraX.obedience >= 500:
                    $ LauraX.change_face("sad")
                    ch_l "I think it's best we keep things simple."
                elif LauraX.inhibition >= 500:
                    $ LauraX.change_face("perplexed")
                    ch_l "That ruined the fun."
                else:
                    $ LauraX.change_face("perplexed", 1)
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
                    "When you said you loved me. . ." if "lover" not in LauraX.traits and LauraX.event_happened[6] >= 20 and LauraX.event_happened[6] != 23:
                        call Laura_Love_Redux

                    "When you were telling me all that stuff about yourself. . ." if "lover" not in LauraX.traits and LauraX.event_happened[6] == 23:
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
            "Never mind":

                return

    return

label Laura_OtherWoman(counter=0):

    if not Player.Harem:
        return
    $ counter = int((LauraX.likes[Player.Harem[0].tag] - 500)/2)

    $ LauraX.change_face("perplexed")
    if len(Player.Harem) >= 2:
        ch_l "But you're with [Player.Harem[0].name] right now, and you've got a whole pack going."
    else:
        ch_l "But you're with [Player.Harem[0].name], aren't you?"
    menu:
        extend ""
        "She said I can be with you too." if "LauraYes" in Player.traits:
            if approval_check(LauraX, 1800, Bonus = counter):
                $ LauraX.change_face("smile", 1)
                if LauraX.love >= LauraX.obedience:
                    ch_l "I guess I can share you."
                elif LauraX.obedience >= LauraX.inhibition:
                    ch_l "If that's what you want."
                else:
                    ch_l "Fine."
            else:
                $ LauraX.change_face("angry", 1)
                ch_l "Yeah, I imagine she would, but I'm not sharing."
                $ renpy.pop_call()


        "I could ask if she'd be ok with me dating you both." if "LauraYes" not in Player.traits:
            if approval_check(LauraX, 1800, Bonus = counter):
                $ LauraX.change_face("smile", 1)
                if LauraX.love >= LauraX.obedience:
                    ch_l "I guess I can share you."
                elif LauraX.obedience >= LauraX.inhibition:
                    ch_l "If that's what you want."
                else:
                    ch_l "Fine."
                ch_l "Well ask her and tell me in the morning."
            else:
                $ LauraX.change_face("angry", 1)
                ch_l "Yeah, I imagine she would, but I'm not sharing."
            $ renpy.pop_call()
        "What she doesn't know won't hurt her.":

            if not approval_check(LauraX, 1800, Bonus = -counter):
                $ LauraX.change_face("angry", 1)
                if not approval_check(LauraX, 1800):
                    ch_l "Well it'd hurt me."
                else:
                    ch_l "I don't like the sound of that."
                $ renpy.pop_call()
            else:
                $ LauraX.change_face("smile", 1)
                if LauraX.love >= LauraX.obedience:
                    ch_l "I guess I could. . ."
                elif LauraX.obedience >= LauraX.inhibition:
                    ch_l "If that's what you want."
                else:
                    ch_l "Fine."
                $ LauraX.traits.append("downlow")
        "I can break it off with her.":

            $ LauraX.change_face("sad")
            ch_l "Get back to me after."
            $ renpy.pop_call()
        "You're right, I was dumb to ask.":

            $ LauraX.change_face("sad")
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
        elif LauraX.likes[RogueX.tag] >= 900:
            ch_l "She's got a great ass. . ."
        elif LauraX.likes[RogueX.tag] >= 800:
            ch_l "She's got a nice shape on her. . ."
        elif LauraX.likes[RogueX.tag] >= 700:
            ch_l "She's good in a fight."
        elif LauraX.likes[RogueX.tag] >= 600:
            ch_l "We get along ok."
        elif LauraX.likes[RogueX.tag] >= 500:
            ch_l "I guess I've seen her around."
        elif LauraX.likes[RogueX.tag] >= 400:
            ch_l "I don't want to talk about it."
        elif LauraX.likes[RogueX.tag] >= 300:
            ch_l "Hate her."
        else:
            ch_l "Bitch."
    elif Check == KittyX:
        if "poly Kitty" in LauraX.traits:
            ch_l "Yeah, we hook up, so. . ."
        elif LauraX.likes[KittyX.tag] >= 900:
            ch_l "I do like her little tits. . ."
        elif LauraX.likes[KittyX.tag] >= 800:
            ch_l "She keeps in shape. . ."
        elif LauraX.likes[KittyX.tag] >= 700:
            ch_l "Tough to hold down."
        elif LauraX.likes[KittyX.tag] >= 600:
            ch_l "She's cool."
        elif LauraX.likes[KittyX.tag] >= 500:
            ch_l "I guess I've seen her around."
        elif LauraX.likes[KittyX.tag] >= 400:
            ch_l "I don't want to talk about it."
        elif LauraX.likes[KittyX.tag] >= 300:
            ch_l "Hate her."
        else:
            ch_l "Bitch."
    elif Check == EmmaX:
        if "poly Emma" in LauraX.traits:
            ch_l "Yeah, we hook up, so. . ."
        elif LauraX.likes[EmmaX.tag] >= 900:
            ch_l "Really great rack on her. . ."
        elif LauraX.likes[EmmaX.tag] >= 800:
            ch_l "She smells really nice. . ."
        elif LauraX.likes[EmmaX.tag] >= 700:
            ch_l "She's nice to me after class."
        elif LauraX.likes[EmmaX.tag] >= 600:
            ch_l "She's a good teacher."
        elif LauraX.likes[EmmaX.tag] >= 500:
            ch_l "She's fine."
        elif LauraX.likes[EmmaX.tag] >= 400:
            ch_l "I could do with less of her attitude."
        elif LauraX.likes[EmmaX.tag] >= 300:
            ch_l "She needs to stay out of my head."
        else:
            ch_l "Grrrrr."
    elif Check == JeanX:
        if "poly Jean" in LauraX.traits:
            ch_l "Yeah, we hook up, so. . ."
        elif LauraX.likes[JeanX.tag] >= 900:
            ch_l "She's got a great ass. . ."
        elif LauraX.likes[JeanX.tag] >= 800:
            ch_l "She's got a nice shape on her. . ."
        elif LauraX.likes[JeanX.tag] >= 700:
            ch_l "She's. . . ok."
        elif LauraX.likes[JeanX.tag] >= 600:
            ch_l "I guess she's ok?"
        elif LauraX.likes[JeanX.tag] >= 500:
            ch_l "She's kind of a chore."
        elif LauraX.likes[JeanX.tag] >= 400:
            ch_l "She needs to stay out of my head."
        elif LauraX.likes[JeanX.tag] >= 300:
            ch_l "Hate her."
        else:
            ch_l "Bitch."
    elif Check == StormX:
        if "poly Storm" in LauraX.traits:
            ch_l "Yeah, we hook up, so. . ."
        elif LauraX.likes[StormX.tag] >= 900:
            ch_l "Really great ass on her. . ."
        elif LauraX.likes[StormX.tag] >= 800:
            ch_l "She smells like a garden. . ."
        elif LauraX.likes[StormX.tag] >= 700:
            ch_l "She's nice to me after class."
        elif LauraX.likes[StormX.tag] >= 600:
            ch_l "She's a good teacher."
        elif LauraX.likes[StormX.tag] >= 500:
            ch_l "She's fine."
        elif LauraX.likes[StormX.tag] >= 400:
            ch_l "She can be mean."
        elif LauraX.likes[StormX.tag] >= 300:
            ch_l "She needs to stay out of my way."
        else:
            ch_l "Grrrrr."
    elif Check == JubesX:
        if "poly Jubes" in LauraX.traits:
            ch_l "Yeah, we hook up, so. . ."
        elif LauraX.likes[JubesX.tag] >= 900:
            ch_l "I do love her smooth skin. . ."
        elif LauraX.likes[JubesX.tag] >= 800:
            ch_l "She has a nice shape. . ."
        elif LauraX.likes[JubesX.tag] >= 700:
            ch_l "Tough to pin down."
        elif LauraX.likes[JubesX.tag] >= 600:
            ch_l "She's cool."
        elif LauraX.likes[JubesX.tag] >= 500:
            ch_l "I guess I've seen her around."
        elif LauraX.likes[JubesX.tag] >= 400:
            ch_l "She bites."
        elif LauraX.likes[JubesX.tag] >= 300:
            ch_l "Hate her."
        else:
            ch_l "Bitch."
    return


label Laura_Monogamy:

    menu:
        "Could you not hook up with other girls?" if "monogamous" not in LauraX.traits:
            if LauraX.thirst >= 60 and not approval_check(LauraX, 1700, "LO", taboo_modifier=0):

                $ LauraX.change_face("sly", 1)
                if "monogamous" not in LauraX.daily_history:
                    call change_Girl_stat(LauraX, "obedience", -2)
                ch_l "I would, but you aren't around enough. . ."
                return
            elif approval_check(LauraX, 1200, "LO", taboo_modifier=0) and LauraX.love >= LauraX.obedience:

                $ LauraX.change_face("sly", 1)
                if "monogamous" not in LauraX.daily_history:
                    call change_Girl_stat(LauraX, "love", 1)
                ch_l "I didn't take you for the jealous type."
                ch_l "Fine, no side pussy. . ."
            elif approval_check(LauraX, 700, "O", taboo_modifier=0):

                $ LauraX.change_face("sly", 1, eyes = "side")
                ch_l "Affirmative."
            else:

                $ LauraX.change_face("sly", 1)
                ch_l "Oh, you wouldn't want to see me when I'm thirsty."
                return
            if "monogamous" not in LauraX.daily_history:
                call change_Girl_stat(LauraX, "obedience", 3)
            $ LauraX.add_word(1, 0, "monogamous")
            $ LauraX.traits.append("monogamous")
        "Don't hook up with other girls." if "monogamous" not in LauraX.traits:
            if approval_check(LauraX, 900, "O", taboo_modifier=0):

                $ LauraX.change_face("sly", 1, eyes = "side")
                ch_l "Ok."
            elif LauraX.thirst >= 60 and not approval_check(LauraX, 1700, "LO", taboo_modifier=0):

                $ LauraX.change_face("sly", 1)
                if "monogamous" not in LauraX.daily_history:
                    call change_Girl_stat(LauraX, "obedience", -2)
                ch_l "I would, but you aren't around enough. . ."
                return
            elif approval_check(LauraX, 600, "O", taboo_modifier=0):

                $ LauraX.change_face("sly", 1, eyes = "side")
                ch_l "Hey, fine, your call."
            elif approval_check(LauraX, 1400, "LO", taboo_modifier=0):

                $ LauraX.change_face("sly", 1)
                ch_l "I wouldn't come at me like that, but fine."
            else:

                $ LauraX.change_face("sly", 1, brows = "confused")
                ch_l "Oh, you wouldn't want to see me when I'm thirsty."
                return
            if "monogamous" not in LauraX.daily_history:
                call change_Girl_stat(LauraX, "obedience", 3)
            $ LauraX.add_word(1, 0, "monogamous")
            $ LauraX.traits.append("monogamous")
        "It's ok if you hook up with other girls." if "monogamous" in LauraX.traits:
            if approval_check(LauraX, 700, "O", taboo_modifier=0):
                $ LauraX.change_face("sly", 1, eyes = "side")
                ch_l "Affirmative."
            elif approval_check(LauraX, 800, "L", taboo_modifier=0):
                $ LauraX.change_face("sly", 1)
                ch_l "You'd better not leave me hangin. . ."
            else:
                $ LauraX.change_face("sly", 1, brows = "confused")
                if "monogamous" not in LauraX.daily_history:
                    call change_Girl_stat(LauraX, "love", -2)
                ch_l "Well call out the ladies, I've just been given permission!"
            if "monogamous" not in LauraX.daily_history:
                call change_Girl_stat(LauraX, "obedience", 3)
            if "monogamous" in LauraX.traits:
                $ LauraX.traits.remove("monogamous")
            $ LauraX.add_word(1, 0, "monogamous")
        "Never mind.":
            pass
    return



label Laura_Jumped:

    ch_p "Hey, Remember that time you threw yourself at me?"
    $ LauraX.change_face("sly", 1, brows = "confused")
    menu:
        ch_l "Yeah?"
        "Could you maybe just ask instead?" if "chill" not in LauraX.traits:
            if LauraX.thirst >= 60 and not approval_check(LauraX, 1500, "LO", taboo_modifier=0):

                $ LauraX.change_face("sly", 1)
                if "chill" not in LauraX.daily_history:
                    call change_Girl_stat(LauraX, "obedience", -2)
                ch_l "Not if you're going to keep dodging me. . ."
                return
            elif approval_check(LauraX, 1000, "LO", taboo_modifier=0) and LauraX.love >= LauraX.obedience:

                $ LauraX.change_face("surprised", 1)
                if "chill" not in LauraX.daily_history:
                    call change_Girl_stat(LauraX, "love", 1)
                ch_l "Sorry, I was just horny. . ."
                $ LauraX.change_face("sly", 1, eyes = "side")
                ch_l "I'll try to hold back. . ."
            elif approval_check(LauraX, 500, "O", taboo_modifier=0):

                $ LauraX.change_face("sly", 1, eyes = "side")
                ch_l "Sorry. . ."
            else:

                $ LauraX.change_face("sly", 1)
                ch_l "Only if I can't find you."
                return
            if "chill" not in LauraX.daily_history:
                call change_Girl_stat(LauraX, "obedience", 3)
            $ LauraX.add_word(1, 0, "chill")
            $ LauraX.traits.append("chill")
        "Don't bother me like that." if "chill" not in LauraX.traits:
            if approval_check(LauraX, 800, "O", taboo_modifier=0):

                $ LauraX.change_face("sly", 1, eyes = "side")
                ch_l "Ok."
            elif LauraX.thirst >= 60 and not approval_check(LauraX, 500, "O", taboo_modifier=0):

                $ LauraX.change_face("sly", 1)
                if "chill" not in LauraX.daily_history:
                    call change_Girl_stat(LauraX, "obedience", -2)
                ch_l "Then don't keep dodging me. . ."
                return
            elif approval_check(LauraX, 400, "O", taboo_modifier=0):

                $ LauraX.change_face("sly", 1, eyes = "side")
                ch_l "Affirmative. . ."
            elif approval_check(LauraX, 500, "LO", taboo_modifier=0) and not approval_check(LauraX, 500, "I", taboo_modifier=0):

                $ LauraX.change_face("sly", 1)
                ch_l "Don't boss me around like that."
                ch_l "Still, I'll try to control myself. . ."
            else:

                $ LauraX.change_face("sly", 1)
                ch_l "Only if I can't find you."
                return
            if "chill" not in LauraX.daily_history:
                call change_Girl_stat(LauraX, "obedience", 3)
            $ LauraX.add_word(1, 0, "chill")
            $ LauraX.traits.append("chill")
        "Knock yourself out.":
            if approval_check(LauraX, 800, "L", taboo_modifier=0):
                $ LauraX.change_face("sly", 1)
                ch_l "Oh, I think we'll both enjoy that. . ."
            elif approval_check(LauraX, 700, "O", taboo_modifier=0):
                $ LauraX.change_face("sly", 1, eyes = "side")
                ch_l "Oh yes sir."
            else:
                $ LauraX.change_face("sly", 1, brows = "confused")
                if "chill" not in LauraX.daily_history:
                    call change_Girl_stat(LauraX, "love", -2)
                ch_l "If I'm horny, sure."
            if "chill" not in LauraX.daily_history:
                call change_Girl_stat(LauraX, "obedience", 3)
            if "chill" in LauraX.traits:
                $ LauraX.traits.remove("chill")
            $ LauraX.add_word(1, 0, "chill")
        "Um, never mind.":
            pass
    return




label Laura_Hungry:
    if LauraX.had_chat[3]:
        ch_l "[[licks her lips] I'm a little thirsty. . ."
    elif LauraX.had_chat[2]:
        ch_l "I really enjoy that serum you whipped up."
    else:
        ch_l "[[licks her lips] I'm a little thirsty. . ."
    $ LauraX.traits.append("hungry")
return





label Laura_SexChat:
    $ line = "Yeah, what did you want to talk about?" if not line else line
    while True:
        menu:
            ch_l "[line]"
            "My favorite thing to do is. . .":
                if "setfav" in LauraX.daily_history:
                    ch_l "I remember."
                else:
                    menu:
                        "Sex.":
                            $ LauraX.change_face("sly")
                            if LauraX.player_favorite_action == "sex":
                                call change_Girl_stat(LauraX, "lust", 5)
                                ch_l "Yeah, I know that. . ."
                            elif LauraX.favorite_action == "sex":
                                call change_Girl_stat(LauraX, "love", 5)
                                call change_Girl_stat(LauraX, "lust", 10)
                                ch_l "I really like it too!"
                            elif LauraX.permanent_History["sex"] >= 5:
                                ch_l "Well I don't mind that."
                            elif not LauraX.permanent_History["sex"]:
                                $ LauraX.change_face("perplexed")
                                ch_l "Who's fucking you?"
                            else:
                                $ LauraX.change_face("bemused")
                                ch_l "Heh, um, yeah, it's nice. . ."
                            $ LauraX.player_favorite_action = "sex"
                        "Anal.":

                            $ LauraX.change_face("sly")
                            if LauraX.player_favorite_action == "anal":
                                call change_Girl_stat(LauraX, "lust", 5)
                                ch_l "So you've said. . ."
                            elif LauraX.favorite_action == "anal":
                                call change_Girl_stat(LauraX, "love", 5)
                                call change_Girl_stat(LauraX, "lust", 10)
                                ch_l "I love it too!"
                            elif LauraX.permanent_History["anal"] >= 10:
                                ch_l "Yeah, it's. . . nice. . ."
                            elif not LauraX.permanent_History["anal"]:
                                $ LauraX.change_face("perplexed")
                                ch_l "Who's fucking you?"
                            else:
                                $ LauraX.change_face("bemused", eyes = "side")
                                ch_l "Heh, heh, yeah, um, it's ok. . ."
                            $ LauraX.player_favorite_action = "anal"
                        "Blowjobs.":

                            $ LauraX.change_face("sly")
                            if LauraX.player_favorite_action == "blowjob":
                                call change_Girl_stat(LauraX, "lust", 3)
                                ch_l "Yeah, I know."
                            elif LauraX.favorite_action == "blowjob":
                                call change_Girl_stat(LauraX, "love", 5)
                                call change_Girl_stat(LauraX, "lust", 5)
                                ch_l "I love your dick!"
                            elif LauraX.permanent_History["blowjob"] >= 10:
                                ch_l "Yeah, you're pretty tasty."
                            elif not LauraX.permanent_History["blowjob"]:
                                $ LauraX.change_face("perplexed")
                                ch_l "Who's sucking your dick?!"
                            else:
                                $ LauraX.change_face("bemused")
                                ch_l "I'm. . . getting used to the taste. . ."
                            $ LauraX.player_favorite_action = "blowjob"
                        "Titjobs.":

                            $ LauraX.change_face("sly")
                            if LauraX.player_favorite_action == "titjob":
                                call change_Girl_stat(LauraX, "lust", 5)
                                ch_l "Yeah, you've said that before. . ."
                            elif LauraX.favorite_action == "titjob":
                                call change_Girl_stat(LauraX, "love", 5)
                                call change_Girl_stat(LauraX, "lust", 7)
                                ch_l "Yeah, I enjoy that too. . ."
                            elif LauraX.permanent_History["titjob"] >= 10:
                                ch_l "It's certainly an interesting experience . . ."
                            elif not LauraX.permanent_History["titjob"]:
                                $ LauraX.change_face("perplexed")
                                ch_l "Who's titfucking you?"
                            else:
                                $ LauraX.change_face("bemused")
                                ch_l "That's nice of you to say. . ."
                                call change_Girl_stat(LauraX, "love", 5)
                                call change_Girl_stat(LauraX, "inhibition", 10)
                            $ LauraX.player_favorite_action = "titjob"
                        "Footjobs.":

                            $ LauraX.change_face("sly")
                            if LauraX.player_favorite_action == "footjob":
                                call change_Girl_stat(LauraX, "lust", 5)
                                ch_l "Yeah, you've said that. . ."
                            elif LauraX.favorite_action == "footjob":
                                call change_Girl_stat(LauraX, "love", 5)
                                call change_Girl_stat(LauraX, "lust", 7)
                                ch_l "I do like using my feet. . ."
                            elif LauraX.permanent_History["footjob"] >= 10:
                                ch_l "I like it too . . ."
                            elif not LauraX.permanent_History["footjob"]:
                                $ LauraX.change_face("perplexed")
                                ch_l "Who's playing footsie with you?"
                            else:
                                $ LauraX.change_face("bemused")
                                ch_l "Yeah, it's nice. . ."
                            $ LauraX.player_favorite_action = "footjob"
                        "Handjobs.":

                            $ LauraX.change_face("sly")
                            if LauraX.player_favorite_action == "handjob":
                                call change_Girl_stat(LauraX, "lust", 5)
                                ch_l "Yeah, you've said that. . ."
                            elif LauraX.favorite_action == "handjob":
                                call change_Girl_stat(LauraX, "love", 5)
                                call change_Girl_stat(LauraX, "lust", 7)
                                ch_l "You do feel pretty comfy. . ."
                            elif LauraX.permanent_History["handjob"] >= 10:
                                ch_l "I like it too . . ."
                            elif not LauraX.permanent_History["handjob"]:
                                $ LauraX.change_face("perplexed")
                                ch_l "Who's jerking you off?"
                            else:
                                $ LauraX.change_face("bemused")
                                ch_l "Yeah, it's nice. . ."
                            $ LauraX.player_favorite_action = "handjob"
                        "Feeling you up.":

                            $ counter = LauraX.permanent_History["fondle_breasts"]+ LauraX.permanent_History["fondle_thighs"]+ LauraX.permanent_History["suck_breasts"] + LauraX.permanent_History["hotdog"]
                            $ LauraX.change_face("sly")
                            if LauraX.player_favorite_action == "fondle":
                                call change_Girl_stat(LauraX, "lust", 3)
                                ch_l "Yeah, I think we're clear on that. . ."
                            elif LauraX.favorite_action in ("hotdog", "suck_breasts", "fondle_breasts", "fondle_thighs"):
                                call change_Girl_stat(LauraX, "love", 5)
                                call change_Girl_stat(LauraX, "lust", 5)
                                ch_l "I love when you touch me. . ."
                            elif counter >= 10:
                                ch_l "Yeah, it's really nice . . ."
                            elif not counter:
                                $ LauraX.change_face("perplexed")
                                ch_l "Who's letting you feel her up?"
                            else:
                                $ LauraX.change_face("bemused")
                                ch_l "I do like how that feels. . ."
                            $ LauraX.player_favorite_action = "fondle"
                            $ counter = 0
                        "Kissing you.":

                            $ LauraX.change_face("sly")
                            if LauraX.player_favorite_action == "kiss":
                                call change_Girl_stat(LauraX, "love", 3)
                                ch_l "Such a romantic. . ."
                            elif LauraX.favorite_action == "kiss":
                                call change_Girl_stat(LauraX, "love", 5)
                                call change_Girl_stat(LauraX, "lust", 5)
                                ch_l "Hmm, the taste of you on my lips. . ."
                            elif LauraX.permanent_History["kiss"] >= 10:
                                ch_l "I love kissing you too . . ."
                            elif not LauraX.permanent_History["kiss"]:
                                $ LauraX.change_face("perplexed")
                                ch_l "Who are you kissing?"
                            else:
                                $ LauraX.change_face("bemused")
                                ch_l "I like kissing you too. . ."
                            $ LauraX.player_favorite_action = "kiss"

                    $ LauraX.daily_history.append("setfav")
            "What's your favorite thing to do?":

                if not approval_check(LauraX, 800):
                    $ LauraX.change_face("perplexed")
                    ch_l ". . ."
                else:
                    if LauraX.SEXP >= 50:
                        $ LauraX.change_face("sly")
                        ch_l "You should know. . ."
                    else:
                        $ LauraX.change_face("bemused")
                        $ LauraX.eyes = "side"
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
                    elif LauraX.favorite_action == "footjob":
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
                    $ LauraX.change_face("perplexed")
                    ch_l "Make up your mind."
                else:
                    if approval_check(LauraX, 1000) and LauraX.obedience <= LauraX.love:
                        $ LauraX.change_face("bemused")
                        call change_Girl_stat(LauraX, "obedience", 1)
                        ch_l "Stay quiet, got it."
                        $ LauraX.traits.remove("vocal")
                    elif approval_check(LauraX, 700, "O"):
                        $ LauraX.change_face("sadside")
                        call change_Girl_stat(LauraX, "obedience", 1)
                        ch_l ". . ."
                        $ LauraX.traits.remove("vocal")
                    elif approval_check(LauraX, 600):
                        $ LauraX.change_face("sly")
                        call change_Girl_stat(LauraX, "love", -3)
                        call change_Girl_stat(LauraX, "obedience", -1)
                        call change_Girl_stat(LauraX, "inhibition", 5)
                        ch_l "Don't push it, [LauraX.player_petname]."
                    else:
                        $ LauraX.change_face("angry")
                        call change_Girl_stat(LauraX, "love", -5)
                        call change_Girl_stat(LauraX, "obedience", -3)
                        call change_Girl_stat(LauraX, "inhibition", 10)
                        ch_l "I don't take orders from you, [LauraX.player_petname]."

                    $ LauraX.daily_history.append("setvocal")
            "Talk dirty to me during sex." if "vocal" not in LauraX.traits:
                if "setvocal" in LauraX.daily_history:
                    $ LauraX.change_face("perplexed")
                    ch_l "I heard you the first time."
                else:
                    if approval_check(LauraX, 1000) and LauraX.obedience <= LauraX.love:
                        $ LauraX.change_face("sly")
                        call change_Girl_stat(LauraX, "obedience", 2)
                        ch_l "Louder? Ok. . ."
                        $ LauraX.traits.append("vocal")
                    elif approval_check(LauraX, 700, "O"):
                        $ LauraX.change_face("sadside")
                        call change_Girl_stat(LauraX, "obedience", 2)
                        ch_l "If you want, [LauraX.player_petname]."
                        $ LauraX.traits.append("vocal")
                    elif approval_check(LauraX, 600):
                        $ LauraX.change_face("sly")
                        call change_Girl_stat(LauraX, "obedience", 3)
                        ch_l "I guess?"
                        $ LauraX.traits.append("vocal")
                    else:
                        $ LauraX.change_face("angry")
                        call change_Girl_stat(LauraX, "inhibition", 5)
                        ch_l ". . ."

                    $ LauraX.daily_history.append("setvocal")


            "Don't do your own thing as much during sex." if "passive" not in LauraX.traits:
                if "initiative" in LauraX.daily_history:
                    $ LauraX.change_face("perplexed")
                    ch_l "I heard you the first time."
                else:
                    if approval_check(LauraX, 1200) and LauraX.obedience <= LauraX.love:
                        $ LauraX.change_face("bemused")
                        call change_Girl_stat(LauraX, "obedience", 1)
                        ch_l "Passive, eh?"
                        $ LauraX.traits.append("passive")
                    elif approval_check(LauraX, 700, "O"):
                        $ LauraX.change_face("sadside")
                        call change_Girl_stat(LauraX, "obedience", 1)
                        ch_l "I'll try to hold back."
                        $ LauraX.traits.append("passive")
                    elif approval_check(LauraX, 600):
                        $ LauraX.change_face("sly")
                        call change_Girl_stat(LauraX, "love", -3)
                        call change_Girl_stat(LauraX, "obedience", -1)
                        call change_Girl_stat(LauraX, "inhibition", 5)
                        ch_l "Hm, no."
                    else:
                        $ LauraX.change_face("angry")
                        call change_Girl_stat(LauraX, "love", -5)
                        call change_Girl_stat(LauraX, "obedience", -3)
                        call change_Girl_stat(LauraX, "inhibition", 10)
                        ch_l "We'll see."

                    $ LauraX.daily_history.append("initiative")
            "Take more initiative during sex." if "passive" in LauraX.traits:
                if "initiative" in LauraX.daily_history:
                    $ LauraX.change_face("perplexed")
                    ch_l "I heard you the first time."
                else:
                    if approval_check(LauraX, 1000) and LauraX.obedience <= LauraX.love:
                        $ LauraX.change_face("bemused")
                        call change_Girl_stat(LauraX, "obedience", 1)
                        ch_l "More active, got it."
                        $ LauraX.traits.remove("passive")
                    elif approval_check(LauraX, 700, "O"):
                        $ LauraX.change_face("sadside")
                        call change_Girl_stat(LauraX, "obedience", 1)
                        ch_l "If you insist."
                        $ LauraX.traits.remove("passive")
                    elif approval_check(LauraX, 600):
                        $ LauraX.change_face("sly")
                        call change_Girl_stat(LauraX, "obedience", 3)
                        ch_l "We'll see."
                        $ LauraX.traits.remove("passive")
                    else:
                        $ LauraX.change_face("angry")
                        call change_Girl_stat(LauraX, "inhibition", 5)
                        ch_l "Too much work."

                    $ LauraX.daily_history.append("initiative")

            "About getting Jumped" if "jumped" in LauraX.history:
                call Laura_Jumped
            "About when you masturbate":
                call NoFap (LauraX)

            "Never mind" if line == "Yeah, what did you want to talk about?":
                return
            "That's all." if line != "Yeah, what did you want to talk about?":
                return
        if line == "Yeah, what did you want to talk about?":
            $ line = "Anything else?"
    return




label Laura_Chitchat(O=0, Options = ["default", "default", "default"]):
    $ round -= 3 if round > 3 else (round-1)
    if O:
        $ Options = [O]
    else:

        if LauraX not in Player.Phonebook:
            if approval_check(LauraX, 500, "L") or approval_check(LauraX, 250, "I"):
                ch_l "Oh, here's my number, in case you need back-up."
                $ Player.Phonebook.append(LauraX)
                return
            elif approval_check(LauraX, 250, "O"):
                ch_l "If you need to contact me, here's my number."
                $ Player.Phonebook.append(LauraX)
                return

        if "hungry" not in LauraX.traits and (LauraX.permanent_History["swallowed"] + LauraX.had_chat[2]) >= 10 and LauraX.location == Player.location:
            call Laura_Hungry
            return

        if "partyfoul" in LauraX.history and "partyfix" not in LauraX.history:
            call Laura_Foul
            return

        if Player.location != "bg_restaurant" and Player.location != "bg_halloween" and (not taboo or approval_check(LauraX, 800, "I")):
            if LauraX.location == Player.location and LauraX.thirst >= 30 and "refused" not in LauraX.daily_history and "quicksex" not in LauraX.daily_history:
                $ LauraX.change_face("sly", 1)
                ch_l "Hey, wanna bone?"
                call Quick_Sex (LauraX)
                return




        if LauraX.event_happened[0] and "key" not in LauraX.had_chat:
            $ Options.append("key")

        if "mandrill" in Player.traits and "cologne chat" not in LauraX.daily_history:
            $ Options.append("mandrill")
        if "purple" in Player.traits and "cologne chat" not in LauraX.daily_history:
            $ Options.append("purple")
        if "corruption" in Player.traits and "cologne chat" not in LauraX.daily_history:
            $ Options.append("corruption")

        if "Laura" not in LauraX.names:
            $ Options.append("laura")

        if LauraX.went_on_date >= 1 and Player.location != "bg_restaurant":

            $ Options.append("dated")



        if LauraX.permanent_History["kiss"] >= 5:

            $ Options.append("kissed")
        if "dangerroom" in Player.daily_history:

            $ Options.append("dangerroom")
        if "showered" in LauraX.daily_history:

            $ Options.append("showercaught")
        if "fondle_breasts" in LauraX.daily_history or "fondle_pussy" in LauraX.daily_history or "fondle_ass" in LauraX.daily_history:

            $ Options.append("fondled")
        if "Dazzler and Longshot" in LauraX.inventory and "256 Shades of Grey" in LauraX.inventory and "Avengers Tower Penthouse" in LauraX.inventory:

            if "book" not in LauraX.had_chat:
                $ Options.append("booked")
        if "lace_bra" in LauraX.inventory or "lace_panties" in LauraX.inventory:

            if "lingerie" not in LauraX.had_chat:
                $ Options.append("lingerie")
        if LauraX.permanent_History["handjob"]:

            $ Options.append("handy")
        if LauraX.permanent_History["swallowed"]:

            $ Options.append("swallowed")
        if "cleaned" in LauraX.daily_history or "painted" in LauraX.daily_history:

            $ Options.append("facial")
        if LauraX.permanent_History["sleepover"]:

            $ Options.append("sleepwear")
        if LauraX.permanent_History["creampied"] or LauraX.permanent_History["anal_creampied"]:

            $ Options.append("creampie")
        if LauraX.permanent_History["sex"] or LauraX.permanent_History["anal"]:

            $ Options.append("sexed")
        if LauraX.permanent_History["anal"]:

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
        $ LauraX.change_face("confused")
        ch_l "(sniff, sniff). . . smells like. . . ape . . ."
        $ LauraX.change_face("sexy", 2)
        ch_l ". . . did you want to do something later?"
    elif Options[0] == "purple":
        $ LauraX.daily_history.append("cologne chat")
        $ LauraX.change_face("sly", 1)
        ch_l "(sniff, sniff). . . what is that? . ."
        $ LauraX.change_face("normal", 0)
        ch_l ". . . what was it you wanted?"
    elif Options[0] == "corruption":
        $ LauraX.daily_history.append("cologne chat")
        $ LauraX.change_face("confused")
        ch_l "(sniff, sniff). . . that's a strong scent. . ."
        $ LauraX.change_face("angry")
        ch_l ". . . a dangerous scent. . ."
        $ LauraX.change_face("sly")

    elif Options[0] == "caught":
        if "caught chat" in LauraX.had_chat:
            ch_l "We should be more careful about getting caught."
            if not approval_check(LauraX, 500, "I"):
                ch_l "Unless. . ."
        else:
            ch_l "Sorry we got dragged into the Professor's office like that."
            if not approval_check(LauraX, 500, "I"):
                ch_l "I guess you wouldn't want to get it on in public anymore."
            else:
                ch_l "I kind of enjoyed it though. . ."
            $ LauraX.had_chat.append("caught chat")
    elif Options[0] == "key":
        if LauraX.SEXP <= 15:
            ch_l "I gave you the key for convenience, don't abuse it . ."
        else:
            ch_l "I gave you a key, but you don't visit. . ."
        $ LauraX.had_chat.append("key")










    elif Options[0] == "laura":

        ch_l "Oh, by the way, I also go by \"Laura.\" Laura Kinney."
        $ LauraX.names.append("Laura")
        menu:
            "Oh, that's nice, I think I'll call you that.":
                call change_Girl_stat(LauraX, "love", 5)
                $ LauraX.name = "Laura"
            "Ok, but X-23 sounds cooler.":
                call change_Girl_stat(LauraX, "love", -2)
                call change_Girl_stat(LauraX, "obedience", 5)
                $ LauraX.name = "X-23"

    elif Options[0] == "dated":

        ch_l "That was fun last night, we should do that again some time."

    elif Options[0] == "kissed":

        $ LauraX.change_face("normal", 1)
        ch_l "You're pretty good at kissing, [LauraX.player_petname]."
        menu:
            extend ""
            "Hey. . .I'm the best there is at what I do.":
                $ LauraX.change_face("smile", 1)
                ch_l "You'll have to back that claim up."
            "No. You think?":
                ch_l "Do I look like a kidder?"

    elif Options[0] == "dangerroom":

        $ LauraX.change_face("sly", 1)
        ch_l "Hey,[LauraX.player_petname]. I saw you in the Danger Room, earlier."
        ch_l "You should probably keep your left up, you were taking too many shots to the head."

    elif Options[0] == "showercaught":

        if "shower" in LauraX.had_chat:
            ch_l "You saw me taking a shower again. . ."
        else:
            ch_l "Do you make a habit of bursting into the showers?"
            $ LauraX.had_chat.append("shower")
            menu:
                extend ""
                "It was a total accident! I promise!":
                    call change_Girl_stat(LauraX, "love", 5)
                    call change_Girl_stat(LauraX, "love", 2)
                    if approval_check(LauraX, 1200):
                        $ LauraX.change_face("sly", 1)
                        ch_l "I didn't mind."
                    $ LauraX.change_face("smile")
                    ch_l "We all make mistakes."
                "Just with you.":
                    call change_Girl_stat(LauraX, "obedience", 5)
                    if approval_check(LauraX, 1000) or approval_check(LauraX, 700, "L"):
                        call change_Girl_stat(LauraX, "love", 3)
                        $ LauraX.change_face("sly", 1)
                        ch_l "Hmm, I guess that's a compliment."
                    else:
                        call change_Girl_stat(LauraX, "love", -5)
                        $ LauraX.change_face("angry")
                        ch_l "I think I should be insulted."
                "Totally on purpose. I regret nothing.":
                    if approval_check(LauraX, 1200):
                        call change_Girl_stat(LauraX, "love", 3)
                        call change_Girl_stat(LauraX, "obedience", 10)
                        call change_Girl_stat(LauraX, "inhibition", 5)
                        $ LauraX.change_face("sly", 1)
                        ch_l "You seem to know what you want."
                    elif approval_check(LauraX, 800):
                        call change_Girl_stat(LauraX, "obedience", 5)
                        call change_Girl_stat(LauraX, "inhibition", 5)
                        $ LauraX.change_face("perplexed", 2)
                        ch_l "I guess you show initiative."
                        $ LauraX.blushing = "_blush1"
                    else:
                        call change_Girl_stat(LauraX, "love", -10)
                        call change_Girl_stat(LauraX, "love", -10)
                        call change_Girl_stat(LauraX, "obedience", 10)
                        $ LauraX.change_face("angry")
                        ch_l "That's a bit disturbing."

    elif Options[0] == "fondled":

        if LauraX.permanent_History["fondle_breasts"]+ LauraX.permanent_History["fondle_pussy"] + LauraX.permanent_History["fondle_ass"] >= 15:
            ch_l "I need your hands on me."
        else:
            ch_l "You could feel me up, if you wanted."

    elif Options[0] == "booked":

        ch_l "Hey, I read those books you gave me."
        menu:
            extend ""
            "Yeah? Did you like them?":
                $ LauraX.change_face("sly", 2)
                ch_l "They were. . .{i}interesting{/i}."
            "Good. You looked like you could use to learn a thing or two from them.":
                call change_Girl_stat(LauraX, "love", -3)
                call change_Girl_stat(LauraX, "obedience", 5)
                call change_Girl_stat(LauraX, "inhibition", 5)
                $ LauraX.change_face("angry")
                ch_l "I don't see how."
        $ LauraX.blushing = "_blush1"
        $ LauraX.had_chat.append("book")

    elif Options[0] == "lingerie":

        $ LauraX.change_face("sly", 2)
        ch_l "That underwear you got me was kind of uncomfortable, but I do like the look."
        $ LauraX.blushing = "_blush1"
        $ LauraX.had_chat.append("lingerie")

    elif Options[0] == "handy":

        $ LauraX.change_face("sly", 1)
        ch_l "I was thinking about having your cock in my hand the other day. . ."
        ch_l "You seemed to enjoy it."
        $ LauraX.blushing = ""

    elif Options[0] == "blowjob":
        if "blowjob" not in LauraX.had_chat:

            $ LauraX.change_face("sly", 2)
            ch_l "Hey, so did you like that blowjob?"
            menu:
                extend ""
                "You were totally amazing.":
                    call change_Girl_stat(LauraX, "love", 5)
                    call change_Girl_stat(LauraX, "inhibition", 10)
                    $ LauraX.change_face("normal", 1)
                    ch_l "Cool. Cool. . . "
                    $ LauraX.change_face("sexy", 1)
                    ch_l "I'd like another taste sometime."
                "Honestly? It was good. . .but you could use a little practice, I think.":
                    if approval_check(LauraX, 300, "I") or not approval_check(LauraX, 800):
                        call change_Girl_stat(LauraX, "love", -5)
                        call change_Girl_stat(LauraX, "obedience", 10)
                        call change_Girl_stat(LauraX, "inhibition", 10)
                        $ LauraX.change_face("perplexed", 1)
                        ch_l "Yeah? Sorry to disappoint."
                    else:
                        call change_Girl_stat(LauraX, "obedience", 15)
                        call change_Girl_stat(LauraX, "inhibition", 5)
                        $ LauraX.change_face("sexy", 1)
                        ch_l "Yeah? I suppose we could keep trying until I get it right."
                "I guess. If you're into weird sounds and too much teeth. Spoiler, I'm not.":
                    call change_Girl_stat(LauraX, "love", -10)
                    call change_Girl_stat(LauraX, "obedience", 10)
                    $ LauraX.change_face("angry", 2)
                    ch_l "Well, good luck with that then."
            $ LauraX.blushing = "_blush1"
            $ LauraX.had_chat.append("blowjob")
        else:
            $ line = renpy.random.choice(["I gotta tell you, your dick tastes great.",
                            "I think I nearly dislocated my jaw last time.",
                            "Let me know if you'd like another blowjob sometime.",
                            "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
            ch_l "[line]"

    elif Options[0] == "swallowed":

        if "swallow" in LauraX.had_chat:
            ch_l "Hey, I wouldn't mind another taste of you some time."
        else:
            ch_l "So. . . the other day. . ."
            ch_l "That was the first time I'd really enjoyed the taste of jiz."
            $ LauraX.change_face("sly", 1)
            ch_l "Good job!"
            $ LauraX.had_chat.append("swallow")

    elif Options[0] == "facial":

        ch_l "Hey. . .I know this is kind of odd. . ."
        $ LauraX.change_face("sexy", 2)
        ch_l "I feel so {i}good{/i} with your jizz on my face."
        $ LauraX.blushing = "_blush1"

    elif Options[0] == "sleepover":

        ch_l "I really enjoyed the other night."
        ch_l "It felt so safe sleeping next to someone else."

    elif Options[0] == "creampie":

        "[LauraX.name] draws close to you so she can whisper into your ear."
        ch_l "I can still feel you. . .running down the inside of my thigh."

    elif Options[0] == "sexed":

        ch_l "So. . . you should know. . ."
        $ LauraX.change_face("sexy", 2)
        ch_l ". . .lately when I've been flicking the bean. . ."
        ch_l "I've been thinking about you inside of me."
        $ LauraX.blushing = "_blush1"

    elif Options[0] == "anal":

        $ LauraX.change_face("sly")
        ch_l "I did't really enjoy anal much."
        $ LauraX.change_face("sexy", 1)
        ch_l "Until you, at least."

    elif Options[0] == "seenpeen":
        $ LauraX.change_face("sly", 1, eyes = "down")
        ch_l "I forgot to tell you, you've got a pretty nice cock down there. . ."
        $ LauraX.change_face("bemused", 1)
        call change_Girl_stat(LauraX, "love", 5)
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
        $ line = renpy.random.choice(["Get away from me.",
                "I don't want to smell you near me.",
                "Back off.",
                "Buzz off."])
        ch_l "[line]"
    else:

        $ D20 = renpy.random.randint(1, 21)
        if D20 == 1:
            $ LauraX.change_face("smile")
            ch_l "I got a good grade on that bio test."
        elif D20 == 2:
            $ LauraX.change_face("annoyed")
            ch_l "If I have to hear him say \"I'm the best there is\" one more time, I swear I'm going .."
        elif D20 == 3:
            $ LauraX.change_face("surprised")
            ch_l "Huh? Oh, sorry. I sort of spaced out. That's not like me."
        elif D20 == 4:
            $ LauraX.change_face("sad")
            ch_l "Oh, [LauraX.player_petname]. I was just remembering something. Don't worry about it."
        elif D20 == 5:
            $ LauraX.change_face("smile")
            ch_l "I had a good nap. It's nice to be somewhere I can just doze off without worry."
        elif D20 == 6:
            $ LauraX.change_face("perplexed")
            ch_l "Oh, [LauraX.player_petname]. I think I just saw Emma Frost staring at Cyclops. That's.. wierd."
        elif D20 == 7:
            $ LauraX.change_face("smile")
            ch_l "I just got a new personal best time in the Danger Room."
        elif D20 == 8:
            $ LauraX.change_face("sad")
            ch_l "I like being here, but sometimes there's just so much noise.."
        elif D20 == 9:
            $ LauraX.change_face("confused")
            ch_l "I'm still trying to figure out what the mystery meat in the cafeteria was today."
            ch_l "I have enhanced senses, this shouldn't be so difficult!"
        elif D20 == 10:
            $ LauraX.change_face("smile")
            ch_l "Kitty, Rogue and some of the others asked me if I wanted to go grab some ice cream with them tomorrow."
        elif D20 == 11:
            $ LauraX.change_face("smile")
            ch_l "I tried out a dance class like Kitty said. Apparently I'm good at it."
        elif D20 == 12:
            $ LauraX.change_face("sad")
            ch_l "I like talking to Kitty and the others. It makes me feel, I don't know. . ."
            ch_l "{i}not{/i} like a really dangerous mutant who could kill everyone around me if I flipped out."
        elif D20 == 13:
            $ LauraX.change_face("smile")
            ch_l "Kitty and Rogue dared me to call Logan \"Dad\". I think we might've given him a heart attack."
        elif D20 == 14:
            $ LauraX.change_face("sad")
            ch_l "I like going out on missions, but catching up with what's been going on while I'm gone is always a pain."
        elif D20 == 15:
            $ LauraX.change_face("perplexed")
            ch_l "So they're called the \"Avengers\", but do they ever do any avenging?"
            ch_l "At least the Fantastic Four really do things that are strange and fantastic."
        elif D20 == 16:
            $ LauraX.change_face("perplexed")
            ch_l "Have you ever been to New York? Sometimes I'm surprised anyone still wants to live there."
        elif D20 == 17:
            $ LauraX.change_face("perplexed")
            ch_l "Logan just walked up and told me that if I ever meet someone called. . ."
            ch_l "\"Dead..Poole?\"..I should just go ahead and stab him in the face."
            ch_l "What's up with that?"
        elif D20 == 18:
            $ LauraX.change_face("smile")
            ch_l "Don't tell anyone this, but I think Cyclops is kind of wound up tight."
        elif D20 == 19:
            $ LauraX.change_face("confused")
            ch_l "Do you smell something? Is that.. nachos and.. chocolate syrup?!"
        elif D20 == 20:
            $ LauraX.change_face("smile")
            ch_l "I like being able to just talk about nothing in particular. It's.. nice."
        else:
            $ LauraX.change_face("smile")
            ch_l "You're fun to hang with."

    $ line = 0
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
                            $ LauraX.change_face("sexy", 1)
                            ch_l "I'm totally your girl, [LauraX.player_petname]."
                        else:
                            $ LauraX.change_face("angry")
                            ch_l "I'm NOT your girl, [LauraX.player_petname]."
                    "\"boo\".":

                        $ LauraX.petname = "boo"
                        if "boyfriend" in LauraX.player_petnames or approval_check(LauraX, 700, "L"):
                            $ LauraX.change_face("sexy", 1)
                            ch_l "I am your boo, [LauraX.player_petname]."
                        else:
                            $ LauraX.change_face("angry")
                            ch_l "I'm NOT your boo, [LauraX.player_petname]."
                    "\"bae\".":

                        $ LauraX.petname = "bae"
                        if "boyfriend" in LauraX.player_petnames or approval_check(LauraX, 600, "L"):
                            $ LauraX.change_face("sexy", 1)
                            ch_l "I am your bae, [LauraX.player_petname]."
                        else:
                            $ LauraX.change_face("angry")
                            ch_l "I'm NOT your bae, [LauraX.player_petname]."
                    "\"baby\".":

                        $ LauraX.petname = "baby"
                        if "boyfriend" in LauraX.player_petnames or approval_check(LauraX, 500, "L"):
                            $ LauraX.change_face("sexy", 1)
                            ch_l "Cute, [LauraX.player_petname]."
                        else:
                            $ LauraX.change_face("angry")
                            ch_l "I am not a baby."
                    "\"sweetie\".":


                        $ LauraX.petname = "sweetie"
                        if "boyfriend" in LauraX.player_petnames or approval_check(LauraX, 600, "L"):
                            ch_l "Aw, that's sweet, [LauraX.player_petname]."
                        else:
                            $ LauraX.change_face("angry", 1)
                            ch_l "Too sweet, [LauraX.player_petname]."
                    "\"sexy\".":

                        $ LauraX.petname = "sexy"
                        if "lover" in LauraX.player_petnames or approval_check(LauraX, 800):
                            $ LauraX.change_face("sexy", 1)
                            ch_l "You know it, [LauraX.player_petname]."
                        else:
                            $ LauraX.change_face("angry", 1)
                            ch_l "Pushing a line there, [LauraX.player_petname]."
                    "\"lover\".":

                        $ LauraX.petname = "lover"
                        if "lover" in LauraX.player_petnames or approval_check(LauraX, 1200):
                            $ LauraX.change_face("sexy", 1)
                            ch_l "I know."
                        else:
                            $ LauraX.change_face("angry", 1)
                            ch_l "I don't think so, [LauraX.player_petname]."
                    "\"Wolvie\".":

                        $ LauraX.petname = "Wolvie"
                        if approval_check(LauraX, 500, "I"):
                            $ LauraX.change_face("sexy", 1)
                            ch_l "Heh, ok, [LauraX.player_petname]."
                        else:
                            $ LauraX.change_face("angry")
                            ch_l "Not really that cute, [LauraX.player_petname]"
                    "Back":

                        pass
            "Risky":

                menu:
                    "I think I'll call you. . ."
                    "\"slave\".":
                        $ LauraX.petname = "slave"
                        if "master" in LauraX.player_petnames or approval_check(LauraX, 800, "O"):
                            $ LauraX.change_face("bemused", 1)
                            ch_l "As you wish, [LauraX.player_petname]."
                        else:
                            $ LauraX.change_face("angry", 1)
                            ch_l "I am not your slave, [LauraX.player_petname]."
                    "\"pet\".":

                        $ LauraX.petname = "pet"
                        if "master" in LauraX.player_petnames or approval_check(LauraX, 650, "O"):
                            $ LauraX.change_face("bemused", 1)
                            ch_l "You can pet me if you want, [LauraX.player_petname]."
                        else:
                            $ LauraX.change_face("angry", 1)
                            ch_l "I am no one's pet, [LauraX.player_petname]."
                    "\"slut\".":

                        $ LauraX.petname = "slut"
                        if "sex friend" in LauraX.player_petnames or approval_check(LauraX, 900, "OI"):
                            $ LauraX.change_face("sexy")
                            ch_l "Fair enough."
                        else:
                            $ LauraX.change_face("angry", 1)
                            $ LauraX.mouth = "surprised"
                            ch_l "I'd like to see you try it with a busted jaw."
                    "\"whore\".":

                        $ LauraX.petname = "whore"
                        if "fuckbuddy" in LauraX.player_petnames or approval_check(LauraX, 1000, "OI"):
                            $ LauraX.change_face("sly")
                            ch_l "I mean. . ."
                        else:
                            $ LauraX.change_face("angry", 1)
                            ch_l "If either of us is going to be turning tricks. . ."
                    "\"sugartits\".":

                        $ LauraX.petname = "sugartits"
                        if "sex friend" in LauraX.player_petnames or approval_check(LauraX, 1400):
                            $ LauraX.change_face("sly", 1)
                            ch_l "That doesn't even make sense."
                        else:
                            $ LauraX.change_face("angry", 1)
                            ch_l "Not cool."
                    "\"sex friend\".":

                        $ LauraX.petname = "sex friend"
                        if "sex friend" in LauraX.player_petnames or approval_check(LauraX, 600, "I"):
                            $ LauraX.change_face("sly")
                            ch_l "Yeah. . ."
                        else:
                            $ LauraX.change_face("angry", 1)
                            ch_l "Keep it down, [LauraX.player_petname]."
                    "\"fuckbuddy\".":

                        $ LauraX.petname = "fuckbuddy"
                        if "fuckbuddy" in LauraX.player_petnames or approval_check(LauraX, 700, "I"):
                            $ LauraX.change_face("sly")
                            ch_l "Yup."
                        else:
                            $ LauraX.change_face("angry", 1)
                            $ LauraX.mouth = "surprised"
                            ch_l "Don't even joke, [LauraX.player_petname]."
                    "\"baby girl\".":

                        $ LauraX.petname = "baby girl"
                        if "daddy" in LauraX.player_petnames or approval_check(LauraX, 1200):
                            $ LauraX.change_face("smile", 1)
                            ch_l "I guess?"
                        else:
                            $ LauraX.change_face("angry", 1)
                            ch_l "Weirdo."
                    "Back":

                        pass
            "Nevermind.":

                return
    return





label Laura_Rename:

    $ LauraX.mouth = "smile"
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
                    $ LauraX.change_face("sadside", 0, brows = "normal")
                if "namechange" not in LauraX.daily_history:
                    call change_Girl_stat(LauraX, "love", -2)
                    call change_Girl_stat(LauraX, "obedience", 5)
                $ LauraX.name = "X-23"
                ch_l "Oh, sure. . . I could go by that again. . ."
        "I liked the sound of \"Wolverine.\"" if LauraX.name != "Wolverine" and "Wolverine" in LauraX.names:
            $ LauraX.change_face("confused", 1)
            if approval_check(LauraX, 500, "O") or approval_check(LauraX, 500, "I"):
                $ LauraX.name = "Wolverine"
                $ LauraX.change_face("confused", 1)
                if "namechange" not in LauraX.daily_history:
                    call change_Girl_stat(LauraX, "obedience", 2)
                    call change_Girl_stat(LauraX, "inhibition", 2)
                ch_l "I guess I could give that one a go. . ."
            else:
                $ LauraX.blushing = "_blush2"
                ch_l "I. . . really don't think that would work for me. . ."
            $ LauraX.change_face()
        "Nevermind.":
            pass
    $ LauraX.add_word(1, 0, "namechange")
    return




label Laura_Personality(counter=0):
    if not LauraX.had_chat[4] or counter:
        "Since you're doing well in one area, you can convince Laura to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_l "Yeah? What's up?"
        "More Obedient. [[Love to Obedience]" if LauraX.love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_l "If you really care about that, sure."
            $ LauraX.had_chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if LauraX.love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_l "I could always be a bit more wild if that's what you want."
            $ LauraX.had_chat[4] = 2

        "Less Inhibited. [[Obedience to Inhibition]" if LauraX.obedience > 900:
            ch_p "I want you to be less inhibited."
            ch_l "I guess I could go all-out."
            $ LauraX.had_chat[4] = 3
        "More Loving. [[Obedience to Love]" if LauraX.obedience > 900:
            ch_p "I'd like you to learn to love me."
            ch_l "I can try."
            $ LauraX.had_chat[4] = 4

        "More Obedient. [[Inhibition to Obedience]" if LauraX.inhibition > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_l "I can give it a shot. . ."
            $ LauraX.had_chat[4] = 5

        "More Loving. [[Inhibition to Love]" if LauraX.inhibition > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_l "If that's something you need out of this. . ."
            $ LauraX.had_chat[4] = 6

        "I guess just do what you like. . .[[reset]" if LauraX.had_chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_l "Um, ok."
            $ LauraX.had_chat[4] = 0
        "Repeat the rules":
            call Laura_Personality (1)
            return
        "Nevermind.":
            return
    return















label Laura_NoPantiesOn:
    menu:
        ch_l "I'm going commando today."
        "Then you could slip on a pair of panties. . .":
            if LauraX.seen_pussy and approval_check(LauraX, 1100, taboo_modifier=4):
                $ LauraX.blushing = "_blush1"
                ch_l "No, commando's fine. . ."
                $ LauraX.blushing = ""
            elif approval_check(LauraX, 1500, taboo_modifier=4):
                $ LauraX.blushing = "_blush1"
                ch_l "No, commando's fine. . ."
                $ LauraX.blushing = ""
            elif approval_check(LauraX, 700, taboo_modifier=4):
                ch_l "Yeah, I guess."
                if "lace_panties" in LauraX.inventory:
                    ch_l "I like how you think."
                    $ LauraX.Clothes["underwear"]  = "lace_panties"
                else:
                    $ LauraX.Clothes["underwear"] = "leather_panties"
                if approval_check(LauraX, 1200, taboo_modifier=4):
                    $ line = LauraX.Clothes["bottom"]
                    $ LauraX.Outfit.remove_Clothing(["pants", "skirt"])
                    "She pulls off her [line] and slips on the [LauraX.Clothes[underwear].name]."
                elif LauraX.Clothes["bottom"] == "skirt":
                    "She pulls out her [LauraX.Clothes[underwear].name] and pulls them up under her skirt."
                    $ LauraX.Outfit.remove_Clothing(["pants", "skirt"])
                    "Then she drops the skirt to the floor."
                else:
                    $ line = LauraX.Clothes["bottom"]
                    $ LauraX.Outfit.remove_Clothing(["pants", "skirt"])
                    "She steps away a moment and then comes back wearing only the [LauraX.Clothes[underwear].name]."
                return
            else:
                ch_l "Nope."
                return False
        "You could always just wear nothing at all. . .":

            if approval_check(LauraX, 1100, "LI", taboo_modifier = 3) and LauraX.love > LauraX.inhibition:
                ch_l "True. . ."
            elif approval_check(LauraX, 700, "OI", taboo_modifier = 3) and LauraX.obedience > LauraX.inhibition:
                ch_l "Yes. . ."
            elif approval_check(LauraX, 600, "I", taboo_modifier = 3):
                ch_l "Hrmm. . ."
            elif approval_check(LauraX, 1300, taboo_modifier = 3):
                ch_l "Fine."
            else:
                $ LauraX.change_face("surprised")
                $ LauraX.brows = "angry"
                if LauraX.taboo > 20:
                    ch_l "Yeah, but not in public, [LauraX.player_petname]!"
                else:
                    ch_l "You aren't that cute, [LauraX.player_petname]!"
                return False
        "Never mind.":

            ch_l "Ok. . ."
            return False
    return True




menu Laura_Clothes_Under:
    "Tops":
        menu:
            "How about you lose the [LauraX.Clothes[bra].name]?" if LauraX.Clothes["bra"]:
                $ LauraX.change_face("bemused", 1)
                if LauraX.seen_breasts and approval_check(LauraX, 900, taboo_modifier=2.7):
                    ch_l "Ok."
                elif approval_check(LauraX, 1100, taboo_modifier=2):
                    if LauraX.taboo:
                        ch_l "I don't know, here. . ."
                    else:
                        ch_l "Maybe. . ."
                elif LauraX.Clothes["top"] == "jacket" and approval_check(LauraX, 600, taboo_modifier=2):
                    ch_l "This jacket is a bit revealing. . ."
                elif LauraX.Clothes["top"] and approval_check(LauraX, 500, taboo_modifier=2):
                    ch_l "I guess I could. . ."
                elif not LauraX.Clothes["top"]:
                    call ask_for_dress_screen (LauraX)
                    if not _return:
                        ch_l "Not without some other top."
                        return
                else:
                    call ask_for_dress_screen (LauraX)
                    if not _return:
                        ch_l "Nah."
                        return
                $ line = LauraX.Clothes["bra"]
                $ LauraX.take_off("bra")
                if LauraX.Clothes["top"]:
                    "She reaches under her [LauraX.Clothes[top].name] grabs her [line], and pulls it off, dropping it to the ground."
                else:
                    "She pulls off her [line] and drops it to the ground."
                    if not renpy.showing('dress_screen'):
                        call Laura_First_Topless


            "Add leather_bra" if LauraX.Clothes["bra"] != "leather_bra":
                ch_p "Try on that leather bra."
                ch_l "Ok."
                $ LauraX.Clothes["bra"] = "leather_bra"

            "Add _white_tanktop" if LauraX.Clothes["bra"] != "white_tank" and "halloween" in LauraX.history:
                ch_p "Try on that _white_tanktop."
                ch_l "Ok."
                $ LauraX.Clothes["bra"] = "white_tank"

            "Add red corset." if LauraX.Clothes["bra"] != "corset" and "corset" in LauraX.inventory:
                ch_p "I like that red corset."
                if LauraX.seen_breasts or approval_check(LauraX, 1000, taboo_modifier = 1):
                    ch_l "K."
                    $ LauraX.Clothes["bra"] = "corset"
                else:
                    call ask_for_dress_screen (LauraX)
                    if not _return:
                        ch_l "It's a bit revealing. . ."
                    else:
                        $ LauraX.Clothes["bra"] = "corset"

            "Add lace corset" if LauraX.Clothes["bra"] != "lace_corset" and "lace_corset" in LauraX.inventory:
                ch_p "I like that lace corset."
                if LauraX.seen_breasts or approval_check(LauraX, 1300, taboo_modifier=2):
                    ch_l "K."
                    $ LauraX.Clothes["bra"] = "lace_corset"
                else:
                    call ask_for_dress_screen (LauraX)
                    if not _return:
                        ch_l "It's a bit transparent. . ."
                    else:
                        $ LauraX.Clothes["bra"] = "lace_corset"

            "Add wolverine tanktop" if LauraX.Clothes["bra"] != "wolvie_bra" and "wolvie_bra" in LauraX.inventory:
                ch_p "I like that wolverine tanktop."
                if LauraX.seen_breasts or approval_check(LauraX, 1000, taboo_modifier=2):
                    ch_l "K."
                    $ LauraX.Clothes["bra"] = "wolvie_bra"
                else:
                    call ask_for_dress_screen (LauraX)
                    if not _return:
                        ch_l "It's a {i}little{/i} embarrassing. . ."
                    else:
                        $ LauraX.Clothes["bra"] = "wolvie_bra"

            "Add bikini_top" if LauraX.Clothes["bra"] != "bikini_top" and "bikini_top" in LauraX.inventory:
                ch_p "I like that bikini top."
                if Player.location == "bg_pool":
                    ch_l "K."
                    $ LauraX.Clothes["bra"] = "bikini_top"
                else:
                    if LauraX.seen_breasts or approval_check(LauraX, 1000, taboo_modifier=2):
                        ch_l "K."
                        $ LauraX.Clothes["bra"] = "bikini_top"
                    else:
                        call ask_for_dress_screen (LauraX)
                        if not _return:
                            ch_l "This is not really a \"bikini\" sort of place. . ."
                        else:
                            $ LauraX.Clothes["bra"] = "bikini_top"
            "Never mind":
                pass
        return
    "Hose and stockings options":

        menu:
            "You could lose the hose." if LauraX.Clothes["hose"] and LauraX.Clothes["hose"] != 'ripped_tights' and LauraX.Clothes["hose"] != '_tights':
                $ LauraX.take_off("hose")
            "The thigh-high hose would look good with that." if LauraX.Clothes["hose"] != "stockings":
                $ LauraX.Clothes["hose"] = "stockings"
            "The black stockings would look good with that." if LauraX.Clothes["hose"] != "black_stockings" and "halloween" in LauraX.history:
                $ LauraX.Clothes["hose"] = "black_stockings"
            "The stockings and garterbelt would look good with that." if LauraX.Clothes["hose"] != "stockings_and_garterbelt" and "stockings_and_garterbelt" in LauraX.inventory:
                $ LauraX.Clothes["hose"] = "stockings_and_garterbelt"
            "Just the garterbelt would look good with that." if LauraX.Clothes["hose"] != "garterbelt" and "stockings_and_garterbelt" in LauraX.inventory:
                $ LauraX.Clothes["hose"] = "garterbelt"
            "Never mind":
                pass
        return
    "Panties":


        menu:
            "You could lose those panties. . ." if LauraX.Clothes["underwear"]:
                $ LauraX.change_face("bemused", 1)
                if approval_check(LauraX, 900) and (LauraX.Clothes["bottom"] or (LauraX.seen_pussy and not LauraX.taboo)):

                    if approval_check(LauraX, 850, "L"):
                        ch_l "True. . ."
                    elif approval_check(LauraX, 500, "O"):
                        ch_l "Agreed."
                    elif approval_check(LauraX, 350, "I"):
                        ch_l "Heh."
                    else:
                        ch_l "Sure, I guess."
                else:
                    if approval_check(LauraX, 1100, "LI", taboo_modifier = 3) and LauraX.love > LauraX.inhibition:
                        ch_l "Well look, it's not about you, but. . ."
                    elif approval_check(LauraX, 700, "OI", taboo_modifier = 3) and LauraX.obedience > LauraX.inhibition:
                        ch_l "Well. . ."
                    elif approval_check(LauraX, 600, "I", taboo_modifier = 3):
                        ch_l "Hrmm. . ."
                    elif approval_check(LauraX, 1300, taboo_modifier = 3):
                        ch_l "Okay, okay."
                    else:
                        call ask_for_dress_screen (LauraX)
                        if not _return:
                            $ LauraX.change_face("surprised")
                            $ LauraX.brows = "angry"
                            if LauraX.taboo > 20:
                                ch_l "This is too public."
                            else:
                                ch_l "You're not that cute, [LauraX.player_petname]!"
                            return
                $ line = LauraX.Clothes["underwear"]
                $ LauraX.take_off("underwear")
                if not LauraX.Clothes["bottom"]:
                    "She pulls off her [line], then drops them to the ground."
                    if not renpy.showing('dress_screen'):
                        call Laura_First_Bottomless
                elif approval_check(LauraX, 1200, taboo_modifier=4):
                    $ temp_bottom = LauraX.Clothes["bottom"]
                    $ LauraX.Outfit.remove_Clothing(["pants", "skirt"])
                    pause 0.5
                    $ LauraX.Clothes["bottom"] = temp_bottom
                    "She pulls off her [LauraX.Clothes[bottom]] and [line], then pulls the [LauraX.Clothes[bottom].name] back on."
                    call Laura_First_Bottomless (1)
                elif LauraX.Clothes["bottom"] == "skirt":
                    "She reaches under her skirt and pulls her [line] off."
                else:
                    $ LauraX.blushing = "_blush1"
                    "She steps away a moment and then comes back."
                    $ LauraX.blushing = ""
                $ line = 0

            "Why don't you wear the black panties instead?" if LauraX.Clothes["underwear"] and LauraX.Clothes["underwear"] != "leather_panties" and LauraX.Clothes["underwear"] != "leather_panties":
                if approval_check(LauraX, 1100, taboo_modifier = 3):
                    ch_l "Ok."
                    $ LauraX.Clothes["underwear"] = "leather_panties"
                else:
                    call ask_for_dress_screen (LauraX)
                    if not _return:
                        ch_l "That's none of your busines."
                    else:
                        $ LauraX.Clothes["underwear"] = "leather_panties"

            "Why don't you wear the wolverine panties instead?" if "wolvie_panties" in LauraX.inventory and LauraX.Clothes["underwear"] and LauraX.Clothes["underwear"] != "wolvie_panties":
                if approval_check(LauraX, 1000, taboo_modifier = 3):
                    ch_l "I guess."
                    $ LauraX.Clothes["underwear"] = "wolvie_panties"
                else:
                    call ask_for_dress_screen (LauraX)
                    if not _return:
                        ch_l "That's none of your busines."
                    else:
                        $ LauraX.Clothes["underwear"] = "wolvie_panties"

            "Why don't you wear the lace panties instead?" if "lace_panties" in LauraX.inventory and LauraX.Clothes["underwear"] and LauraX.Clothes["underwear"] != "lace_panties":
                if approval_check(LauraX, 1300, taboo_modifier = 3):
                    ch_l "I guess."
                    $ LauraX.Clothes["underwear"] = "lace_panties"
                else:
                    call ask_for_dress_screen (LauraX)
                    if not _return:
                        ch_l "That's none of your busines."
                    else:
                        $ LauraX.Clothes["underwear"] = "lace_panties"

            "I like those bikini bottoms." if "bikini_bottoms" in LauraX.inventory and LauraX.Clothes["underwear"] != "bikini_bottoms":
                if Player.location == "bg_pool":
                    ch_l "K."
                    $ LauraX.Clothes["underwear"] = "bikini_bottoms"
                else:
                    if approval_check(LauraX, 1000, taboo_modifier=2):
                        ch_l "K."
                        $ LauraX.Clothes["underwear"] = "bikini_bottoms"
                    else:
                        call ask_for_dress_screen (LauraX)
                        if not _return:
                            ch_l "This is not really a \"bikini\" sort of place. . ."
                        else:
                            $ LauraX.Clothes["underwear"] = "bikini_bottoms"

            "You know, you could wear some panties with that. . ." if not LauraX.Clothes["underwear"]:
                $ LauraX.change_face("bemused", 1)
                if LauraX.Clothes["bottom"] and (LauraX.love+LauraX.obedience) <= (2*LauraX.inhibition):
                    $ LauraX.mouth = "smile"
                    ch_l "I don't know about that."
                    menu:
                        "Fine by me":
                            return
                        "I insist, put some on.":
                            if (LauraX.love+LauraX.obedience) <= (1.5*LauraX.inhibition):
                                $ LauraX.change_face("angry", eyes = "side")
                                ch_l "Well I insist otherwise."
                                return
                            else:
                                $ LauraX.change_face("sadside")
                                ch_l "Oh, fine."
                else:
                    ch_l "I guess. . ."
                menu:
                    extend ""
                    "How about the black ones?":
                        ch_l "Sure, ok."
                        $ LauraX.Clothes["underwear"] = "leather_panties"
                    "How about the wolvie ones?" if "wolvie_panties" in LauraX.inventory:
                        ch_l "Sure."
                        $ LauraX.Clothes["underwear"]  = "wolvie_panties"
                    "How about the lace ones?" if "lace_panties" in LauraX.inventory:
                        ch_l "Alright."
                        $ LauraX.Clothes["underwear"]  = "lace_panties"
            "Never mind":
                pass
        return
    "Never mind":
        pass
return




menu Laura_Clothes_Misc:

    "Dry Hair" if LauraX.Clothes["hair"] == "wet":
        ch_p "Maybe dry out your hair."
        if approval_check(LauraX, 600):
            ch_l "Ok."
            $ LauraX.Clothes["hair"] = "long"
        else:
            ch_l "I don't know, it's fine like this."

    "Wet Hair style" if LauraX.Clothes["hair"] != "wet":
        ch_p "You should go for that wet look with your hair."
        if approval_check(LauraX, 800):
            ch_l "Hmm?"
            $ LauraX.Clothes["hair"] = "wet"
            "She wanders off for a minute and comes back."
            ch_l "Like this?"
        else:
            ch_l "Ugh, too much work."

    "Grow pubes" if not LauraX.pubes:
        ch_p "You know, I like some nice hair down there. Maybe grow it out."
        if "pubes" in LauraX.to_do:
            $ LauraX.change_face("bemused", 1)
            ch_l "Even I can't grow it out instantly."
        else:
            $ LauraX.change_face("bemused", 1)
            if approval_check(LauraX, 1000, taboo_modifier=0):
                ch_l "Sure, that's easier. . ."
            else:
                $ LauraX.change_face("surprised")
                $ LauraX.brows = "angry"
                ch_l "I think I'll do what I want down there."
                return
            $ LauraX.to_do.append("pubes")
            $ LauraX.pubes_counter = 6
    "Shave pubes" if LauraX.pubes == "_hairy":
        ch_p "I like it waxed clean down there."
        $ LauraX.change_face("bemused", 1)
        if "shave" in LauraX.to_do:
            ch_l "Yeah, I know, I'll get to it."
        else:
            if approval_check(LauraX, 1100, taboo_modifier=0):
                ch_l "Really? I guess I could give it a shave. . ."
            else:
                $ LauraX.change_face("surprised")
                $ LauraX.brows = "angry"
                ch_l "I think I'll do what I want down there."
                return
            $ LauraX.to_do.append("shave")

    "Piercings. [[See what she looks like without them first] (locked)" if not LauraX.seen_pussy and not LauraX.seen_breasts:
        pass

    "Add ring piercings" if LauraX.Clothes["piercings"] != "ring" and (LauraX.seen_pussy or LauraX.seen_breasts):
        ch_p "You know, you'd look really nice with some ring body piercings."
        if "ring" in LauraX.to_do:
            ch_l "Yeah, I know, I'll get to it."
        else:
            $ LauraX.change_face("bemused", 1)
            $ approval = approval_check(LauraX, 1150, taboo_modifier=0)
            if approval_check(LauraX, 900, "L", taboo_modifier=0) or (approval and LauraX.love > 2* LauraX.obedience):
                ch_l "You think I'd look good with them?"
            elif approval_check(LauraX, 600, "I", taboo_modifier=0) or (approval and LauraX.inhibition > LauraX.obedience):
                ch_l "I've been thinking about that for a while."
            elif approval_check(LauraX, 500, "O", taboo_modifier=0) or approval:
                ch_l "Yes, [LauraX.player_petname]."
            else:
                $ LauraX.change_face("surprised")
                $ LauraX.brows = "angry"
                ch_l "Not interested, [LauraX.player_petname]."
                return
            $ LauraX.to_do.append("ring")

    "Add barbell piercings" if LauraX.Clothes["piercings"] != "barbell" and (LauraX.seen_pussy or LauraX.seen_breasts):
        ch_p "You know, you'd look really nice with some barbell body piercings."
        if "barbell" in LauraX.to_do:
            ch_l "Yeah, I know, I'll get to it."
        else:
            $ LauraX.change_face("bemused", 1)
            $ approval = approval_check(LauraX, 1150, taboo_modifier=0)
            if approval_check(LauraX, 900, "L", taboo_modifier=0) or (approval and LauraX.love > 2*LauraX.obedience):
                ch_l "You think I'd look good with them?"
            elif approval_check(LauraX, 600, "I", taboo_modifier=0) or (approval and LauraX.inhibition > LauraX.obedience):
                ch_l "I've been thinking about that for a while."
            elif approval_check(LauraX, 500, "O", taboo_modifier=0) or approval:
                ch_l "Yes, [LauraX.player_petname]."
            else:
                $ LauraX.change_face("surprised")
                $ LauraX.brows = "angry"
                ch_l "Not interested, [LauraX.player_petname]."
                return
            $ LauraX.to_do.append("barbell")

    "Remove piercings" if LauraX.Clothes["piercings"]:
        ch_p "You know, you'd look better without those piercings."
        $ LauraX.change_face("bemused", 1)
        $ approval = approval_check(LauraX, 1350, taboo_modifier=0)
        if approval_check(LauraX, 950, "L", taboo_modifier=0) or (approval and LauraX.love > LauraX.obedience):
            ch_l "Make up your mind . ."
        elif approval_check(LauraX, 700, "I", taboo_modifier=0) or (approval and LauraX.inhibition > LauraX.obedience):
            ch_l "In, out, snickt."
        elif approval_check(LauraX, 600, "O", taboo_modifier=0) or approval:
            ch_l "Fine."
        else:
            $ LauraX.change_face("surprised")
            $ LauraX.brows = "angry"
            ch_l "I've sort of grown attached."
            return
        $ LauraX.take_off("piercings")

    "Medallion_choker" if LauraX.Clothes["neck"] != "leash_choker":
        ch_p "Why don't you try on that medallion choker?"
        ch_l "Ok. . ."
        $ LauraX.Clothes["neck"] = "leash_choker"
    "Remove Necklace" if LauraX.Clothes["neck"]:
        ch_p "Maybe go without a necklace."
        ch_l "Ok. . ."
        $ LauraX.take_off("neck")

    "Add Suspenders" if LauraX.Clothes["suspenders"] != "suspenders" and LauraX.Clothes["suspenders"] != "suspenders2" and "halloween" in LauraX.history:
        $ LauraX.Clothes["suspenders"] = "suspenders"
    "Remove Suspenders" if LauraX.Clothes["suspenders"] == "suspenders" or LauraX.Clothes["suspenders"] == "suspenders2":
        $ LauraX.take_off("suspenders")

    "Shift Suspenders" if LauraX.Clothes["suspenders"] == "suspenders" or LauraX.Clothes["suspenders"] == "suspenders2":
        $ LauraX.Clothes["suspenders"] = "suspenders" if LauraX.Clothes["suspenders"] == "suspenders2" else "suspenders2"
    "Toggle Wristbands":

        if LauraX.Clothes["gloves"] != "wrists":
            ch_p "Why don't you put those wristbands on."
        else:
            ch_p "Maybe go without the wristbands."
        ch_l "Ok. . ."
        $ LauraX.Clothes["gloves"] = "wrists" if LauraX.Clothes["gloves"] != "wrists" else 0
    "Toggle Gloves" if "halloween" in LauraX.history:
        if LauraX.Clothes["gloves"] != "gloves":
            ch_p "Why don't you put those long gloves on."
        else:
            ch_p "Maybe go without the gloves."
        ch_l "Ok. . ."
        $ LauraX.Clothes["gloves"] = "gloves" if LauraX.Clothes["gloves"] != "gloves" else 0
    "Never mind":

        pass
return
