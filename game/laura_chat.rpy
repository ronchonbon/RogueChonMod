# star Laura chat interface
#Laura Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

label Laura_Relationship: #rkelj
    while True:
        menu:
            ch_l "What did you want to talk about?"
            "Do you want to be my girlfriend?" if LauraX not in Player.Harem and "ex" not in LauraX.Traits:
                    $ LauraX.DailyActions.append("relationship")
                    if "asked boyfriend" in LauraX.DailyActions and "angry" in LauraX.DailyActions:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Like I said, not interested."
                            return
                    elif "asked boyfriend" in LauraX.DailyActions:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Still a no."
                            return
                    elif LauraX.Break[0]:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "I'm not looking for a pack."
                            if Player.Harem:
                                    $ LauraX.DailyActions.append("asked boyfriend")
                                    return
                            else:
                                    ch_p "I'm not anymore."

                    $ LauraX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "LauraYes" not in Player.Traits:
                        if len(Player.Harem) >= 2:
                            ch_l "You'd need to clear it with the others first, [LauraX.Petname]."
                        else:
                            ch_l "You'd need to clear it with [Player.Harem[0].Name] first, [LauraX.Petname]."
                        return

                    if LauraX.Event[5]:
                            $ LauraX.FaceChange("bemused", 1)
                            ch_l "I asked, you said \"no\". . ."
                    else:
                            $ LauraX.FaceChange("surprised", 2)
                            ch_l "Huh? . ."
                            $ LauraX.FaceChange("smile", 1)

                    call Laura_OtherWoman

                    if LauraX.Love >= 800:
                            $ LauraX.FaceChange("surprised", 1)
                            $ LauraX.Mouth = "smile"
                            $ LauraX.Statup("Love", 200, 40)
                            ch_l "Sure!"
                            if "boyfriend" not in LauraX.Petnames:
                                    $ LauraX.Petnames.append("boyfriend")
                            if "LauraYes" in Player.Traits:
                                    $ Player.Traits.remove("LauraYes")
                            $ Player.Harem.append(LauraX)
                            call Harem_Initiation
                            "[LauraX.Name] tackles you and kisses you deeply."
                            $ LauraX.FaceChange("kiss", 1)
                            $ LauraX.Kissed += 1
                    elif LauraX.Obed >= 500:
                            $ LauraX.FaceChange("perplexed")
                            ch_l "I don't know, \"dating\". . ."
                    elif LauraX.Inbt >= 500:
                            $ LauraX.FaceChange("smile")
                            ch_l "Nah, this is more fun."
                    else:
                            $ LauraX.FaceChange("perplexed", 1)
                            ch_l "Whoa, slow down, [LauraX.Petname]."

            "Do you want to get back together?" if "ex" in LauraX.Traits:
                    $ LauraX.DailyActions.append("relationship")
                    if "asked boyfriend" in LauraX.DailyActions and "angry" in LauraX.DailyActions:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Like I said, not interested."
                            return
                    elif "asked boyfriend" in LauraX.DailyActions:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Still a no."
                            return

                    $ LauraX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "LauraYes" not in Player.Traits:
                            if len(Player.Harem) >= 2:
                                ch_l "You'd need to clear it with the others first, [LauraX.Petname]."
                            else:
                                ch_l "You'd need to clear it with [Player.Harem[0].Name] first, [LauraX.Petname]."
                            return

                    $ Cnt = 0
                    call Laura_OtherWoman

                    if LauraX.Love >= 800:
                            $ LauraX.FaceChange("surprised", 1)
                            $ LauraX.Mouth = "smile"
                            $ LauraX.Statup("Love", 90, 5)
                            ch_l "Ok, you've earned another shot!"
                            if "boyfriend" not in LauraX.Petnames:
                                        $ LauraX.Petnames.append("boyfriend")
                            $ LauraX.Traits.remove("ex")
                            if "LauraYes" in Player.Traits:
                                    $ Player.Traits.remove("LauraYes")
                            $ Player.Harem.append(LauraX)
                            call Harem_Initiation
                            "[LauraX.Name] pulls you in and kisses you deeply."
                            $ LauraX.FaceChange("kiss", 1)
                            $ LauraX.Kissed += 1
                    elif LauraX.Love >= 600 and ApprovalCheck(LauraX, 1500):
                            $ LauraX.FaceChange("smile", 1)
                            $ LauraX.Statup("Love", 90, 5)
                            ch_l "Um, ok, I guess."
                            if "boyfriend" not in LauraX.Petnames:
                                $ LauraX.Petnames.append("boyfriend")
                            $ LauraX.Traits.remove("ex")
                            if "LauraYes" in Player.Traits:
                                    $ Player.Traits.remove("LauraYes")
                            $ Player.Harem.append(LauraX)
                            call Harem_Initiation
                            $ LauraX.FaceChange("kiss", 1)
                            "[LauraX.Name] gives you a quick kiss."
                            $ LauraX.FaceChange("sly", 1)
                            $ LauraX.Kissed += 1
                    elif LauraX.Obed >= 500:
                            $ LauraX.FaceChange("sad")
                            ch_l "I think it's best we keep things simple."
                    elif LauraX.Inbt >= 500:
                            $ LauraX.FaceChange("perplexed")
                            ch_l "That ruined the fun."
                    else:
                            $ LauraX.FaceChange("perplexed", 1)
                            ch_l "I can't trust you like that."

                    # End Back Together

            "I wanted to ask about [[another girl]" if LauraX in Player.Harem:
                            call AskDateOther

            "I think we should break up." if LauraX in Player.Harem:
                            if "breakup talk" in LauraX.RecentActions:
                                    ch_l "Are you joking? We just had this conversation."
                            elif "breakup talk" in LauraX.DailyActions:
                                    ch_l "That bored of me?"
                                    ch_l "Not today, [LauraX.Petname]."
                            else:
                                    call Breakup(LauraX)

            "About that talk we had before. . .":
                menu:
                    "When you said you loved me. . ." if "lover" not in LauraX.Traits and LauraX.Event[6] >= 20 and LauraX.Event[6] != 23:
                            call Laura_Love_Redux

                    "When you were telling me all that stuff about yourself. . ." if "lover" not in LauraX.Traits and LauraX.Event[6] == 23:
                            call Laura_Love_Redux

                    "You said you wanted me to be more in control?" if "sir" not in LauraX.Petnames and "sir" in LauraX.History:
                            if "asked sub" in LauraX.RecentActions:
                                    ch_l "We just had this conversation."
                            elif "asked sub" in LauraX.DailyActions:
                                    ch_l "Enough of that talk for one day. . ."
                            else:
                                    call Laura_Sub_Asked
                    "You said you wanted me to be your Master?" if "master" not in LauraX.Petnames and "master" in LauraX.History:
                            if "asked sub" in LauraX.RecentActions:
                                    ch_l "We just had this conversation."
                            elif "asked sub" in LauraX.DailyActions:
                                    ch_l "Enough of that talk for one day. . ."
                            else:
                                    call Laura_Sub_Asked
                    "Never mind":
                            pass

            "Never Mind":
                return

    return

label Laura_OtherWoman(Cnt = 0):
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return
    $ Cnt = int((LauraX.GirlLikeCheck(Player.Harem[0]) - 500)/2)

    $ LauraX.FaceChange("perplexed")
    if len(Player.Harem) >= 2:
        ch_l "But you're with [Player.Harem[0].Name] right now, and you've got a whole pack going."
    else:
        ch_l "But you're with [Player.Harem[0].Name], aren't you?"
    menu:
        extend ""
        "She said I can be with you too." if "LauraYes" in Player.Traits:
                if ApprovalCheck(LauraX, 1800, Bonus = Cnt):
                    $ LauraX.FaceChange("smile", 1)
                    if LauraX.Love >= LauraX.Obed:
                            ch_l "I guess I can share you."
                    elif LauraX.Obed >= LauraX.Inbt:
                            ch_l "If that's what you want."
                    else:
                            ch_l "Fine."
                else:
                    $ LauraX.FaceChange("angry", 1)
                    ch_l "Yeah, I imagine she would, but I'm not sharing."
                    $ renpy.pop_call()
                    #This causes it to jump past the previous menu on the return

        "I could ask if she'd be ok with me dating you both." if "LauraYes" not in Player.Traits:
                if ApprovalCheck(LauraX, 1800, Bonus = Cnt):
                        $ LauraX.FaceChange("smile", 1)
                        if LauraX.Love >= LauraX.Obed:
                            ch_l "I guess I can share you."
                        elif LauraX.Obed >= LauraX.Inbt:
                            ch_l "If that's what you want."
                        else:
                            ch_l "Fine."
                        ch_l "Well ask her and tell me in the morning."
                else:
                        $ LauraX.FaceChange("angry", 1)
                        ch_l "Yeah, I imagine she would, but I'm not sharing."
                $ renpy.pop_call()

        "What she doesn't know won't hurt her.":
                if not ApprovalCheck(LauraX, 1800, Bonus = -Cnt): #checks if Laura likes you more than the other girl
                        $ LauraX.FaceChange("angry", 1)
                        if not ApprovalCheck(LauraX, 1800):
                                ch_l "Well it'd hurt me."
                        else:
                                ch_l "I don't like the sound of that."
                        $ renpy.pop_call()
                else:
                        $ LauraX.FaceChange("smile", 1)
                        if LauraX.Love >= LauraX.Obed:
                                ch_l "I guess I could. . ."
                        elif LauraX.Obed >= LauraX.Inbt:
                                ch_l "If that's what you want."
                        else:
                                ch_l "Fine."
                        $ LauraX.Traits.append("downlow")

        "I can break it off with her.":
                    $ LauraX.FaceChange("sad")
                    ch_l "Get back to me after."
                    $ renpy.pop_call()

        "You're right, I was dumb to ask.":
                    $ LauraX.FaceChange("sad")
                    ch_l "Yup."
                    $ renpy.pop_call()

    return


label Laura_About(Check=0): #rkeljsv
    if Check not in TotalGirls:
            ch_l "Who?"
            return
    ch_l "What do I think about her? Well. . ."
    if Check == RogueX:
            if "poly Rogue" in LauraX.Traits:
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
            if "poly Kitty" in LauraX.Traits:
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
            if "poly Emma" in LauraX.Traits:
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
            if "poly Jean" in LauraX.Traits:
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
            if "poly Storm" in LauraX.Traits:
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
            if "poly Jubes" in LauraX.Traits:
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
#End Laura_AboutEmma

label Laura_Monogamy:
        #called from Laura_Settings to ask her not to hook up with other girls
        menu:
            "Could you not hook up with other girls?" if "mono" not in LauraX.Traits:
                    if LauraX.Thirst >= 60 and not ApprovalCheck(LauraX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ LauraX.FaceChange("sly",1)
                            if "mono" not in LauraX.DailyActions:
                                    $ LauraX.Statup("Obed", 90, -2)
                            ch_l "I would, but you aren't around enough. . ."
                            return
                    elif ApprovalCheck(LauraX, 1200, "LO", TabM=0) and LauraX.Love >= LauraX.Obed:
                            #she cares
                            $ LauraX.FaceChange("sly",1)
                            if "mono" not in LauraX.DailyActions:
                                    $ LauraX.Statup("Love", 90, 1)
                            ch_l "I didn't take you for the jealous type."
                            ch_l "Fine, no side pussy. . ."
                    elif ApprovalCheck(LauraX, 700, "O", TabM=0):
                            #she is obedient
                            $ LauraX.FaceChange("sly",1,Eyes="side")
                            ch_l "Affirmative."
                    else:
                            #she doesn't care
                            $ LauraX.FaceChange("sly",1)
                            ch_l "Oh, you wouldn't want to see me when I'm thirsty."
                            return
                    if "mono" not in LauraX.DailyActions:
                            $ LauraX.Statup("Obed", 90, 3)
                    $ LauraX.AddWord(1,0,"mono") #Daily
                    $ LauraX.Traits.append("mono")
            "Don't hook up with other girls." if "mono" not in LauraX.Traits:
                    if ApprovalCheck(LauraX, 900, "O", TabM=0):
                            #she is obedient
                            $ LauraX.FaceChange("sly",1,Eyes="side")
                            ch_l "Ok."
                    elif LauraX.Thirst >= 60 and not ApprovalCheck(LauraX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ LauraX.FaceChange("sly",1)
                            if "mono" not in LauraX.DailyActions:
                                    $ LauraX.Statup("Obed", 90, -2)
                            ch_l "I would, but you aren't around enough. . ."
                            return
                    elif ApprovalCheck(LauraX, 600, "O", TabM=0):
                            #she is obedient
                            $ LauraX.FaceChange("sly",1,Eyes="side")
                            ch_l "Hey, fine, your call."
                    elif ApprovalCheck(LauraX, 1400, "LO", TabM=0):
                            #she cares
                            $ LauraX.FaceChange("sly",1)
                            ch_l "I wouldn't come at me like that, but fine."
                    else:
                            #she doesn't care
                            $ LauraX.FaceChange("sly",1,Brows="confused")
                            ch_l "Oh, you wouldn't want to see me when I'm thirsty."
                            return
                    if "mono" not in LauraX.DailyActions:
                            $ LauraX.Statup("Obed", 90, 3)
                    $ LauraX.AddWord(1,0,"mono") #Daily
                    $ LauraX.Traits.append("mono")
            "It's ok if you hook up with other girls." if "mono" in LauraX.Traits:
                    if ApprovalCheck(LauraX, 700, "O", TabM=0):
                            $ LauraX.FaceChange("sly",1,Eyes="side")
                            ch_l "Affirmative."
                    elif ApprovalCheck(LauraX, 800, "L", TabM=0):
                            $ LauraX.FaceChange("sly",1)
                            ch_l "You'd better not leave me hangin. . ."
                    else:
                            $ LauraX.FaceChange("sly",1,Brows="confused")
                            if "mono" not in LauraX.DailyActions:
                                    $ LauraX.Statup("Love", 90, -2)
                            ch_l "Well call out the ladies, I've just been given permission!"
                    if "mono" not in LauraX.DailyActions:
                            $ LauraX.Statup("Obed", 90, 3)
                    if "mono" in LauraX.Traits:
                            $ LauraX.Traits.remove("mono")
                    $ LauraX.AddWord(1,0,"mono") #Daily
            "Never mind.":
                pass
        return

# end Laura monogamy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Laura_Jumped:
        #called from Laura_Settings to ask her not to jump you
        ch_p "Hey, Remember that time you threw yourself at me?"
        $ LauraX.FaceChange("sly",1,Brows="confused")
        menu:
            ch_l "Yeah?"
            "Could you maybe just ask instead?" if "chill" not in LauraX.Traits:
                    if LauraX.Thirst >= 60 and not ApprovalCheck(LauraX, 1500, "LO", TabM=0):
                            #she's too thirsty
                            $ LauraX.FaceChange("sly",1)
                            if "chill" not in LauraX.DailyActions:
                                    $ LauraX.Statup("Obed", 90, -2)
                            ch_l "Not if you're going to keep dodging me. . ."
                            return
                    elif ApprovalCheck(LauraX, 1000, "LO", TabM=0) and LauraX.Love >= LauraX.Obed:
                            #she cares
                            $ LauraX.FaceChange("surprised",1)
                            if "chill" not in LauraX.DailyActions:
                                    $ LauraX.Statup("Love", 90, 1)
                            ch_l "Sorry, I was just horny. . ."
                            $ LauraX.FaceChange("sly",1,Eyes="side")
                            ch_l "I'll try to hold back. . ."
                    elif ApprovalCheck(LauraX, 500, "O", TabM=0):
                            #she is obedient
                            $ LauraX.FaceChange("sly",1,Eyes="side")
                            ch_l "Sorry. . ."
                    else:
                            #she doesn't care
                            $ LauraX.FaceChange("sly",1)
                            ch_l "Only if I can't find you."
                            return
                    if "chill" not in LauraX.DailyActions:
                            $ LauraX.Statup("Obed", 90, 3)
                    $ LauraX.AddWord(1,0,"chill") #Daily
                    $ LauraX.Traits.append("chill")
            "Don't bother me like that." if "chill" not in LauraX.Traits:
                    if ApprovalCheck(LauraX, 800, "O", TabM=0):
                            #she is obedient
                            $ LauraX.FaceChange("sly",1,Eyes="side")
                            ch_l "Ok."
                    elif LauraX.Thirst >= 60 and not ApprovalCheck(LauraX, 500, "O", TabM=0):
                            #she's too thirsty
                            $ LauraX.FaceChange("sly",1)
                            if "chill" not in LauraX.DailyActions:
                                    $ LauraX.Statup("Obed", 90, -2)
                            ch_l "Then don't keep dodging me. . ."
                            return
                    elif ApprovalCheck(LauraX, 400, "O", TabM=0):
                            #she is obedient
                            $ LauraX.FaceChange("sly",1,Eyes="side")
                            ch_l "Affirmative. . ."
                    elif ApprovalCheck(LauraX, 500, "LO", TabM=0) and not ApprovalCheck(LauraX, 500, "I", TabM=0):
                            #she cares
                            $ LauraX.FaceChange("sly",1)
                            ch_l "Don't boss me around like that."
                            ch_l "Still, I'll try to control myself. . ."
                    else:
                            #she doesn't care
                            $ LauraX.FaceChange("sly",1)
                            ch_l "Only if I can't find you."
                            return
                    if "chill" not in LauraX.DailyActions:
                            $ LauraX.Statup("Obed", 90, 3)
                    $ LauraX.AddWord(1,0,"chill") #Daily
                    $ LauraX.Traits.append("chill")
            "Knock yourself out.":
                    if ApprovalCheck(LauraX, 800, "L", TabM=0):
                            $ LauraX.FaceChange("sly",1)
                            ch_l "Oh, I think we'll both enjoy that. . ."
                    elif ApprovalCheck(LauraX, 700, "O", TabM=0):
                            $ LauraX.FaceChange("sly",1,Eyes="side")
                            ch_l "Oh yes sir."
                    else:
                            $ LauraX.FaceChange("sly",1,Brows="confused")
                            if "chill" not in LauraX.DailyActions:
                                    $ LauraX.Statup("Love", 90, -2)
                            ch_l "If I'm horny, sure."
                    if "chill" not in LauraX.DailyActions:
                            $ LauraX.Statup("Obed", 90, 3)
                    if "chill" in LauraX.Traits:
                            $ LauraX.Traits.remove("chill")
                    $ LauraX.AddWord(1,0,"chill") #Daily
            "Um, never mind.":
                pass
        return

# end Laura jumped <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# start laura hungry //////////////////////////////////////////////////////////
label Laura_Hungry:
    if LauraX.Chat[3]:
        ch_l "[[licks her lips] I'm a little thirsty. . ."
    elif LauraX.Chat[2]:
        ch_l "I really enjoy that serum you whipped up."
    else:
        ch_l "[[licks her lips] I'm a little thirsty. . ."
    $ LauraX.Traits.append("hungry")
return


# end laura hungry //////////////////////////////////////////////////////////

# Laura Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Laura_SexChat:
    $ Line = "Yeah, what did you want to talk about?" if not Line else Line
    while True:
            menu:
                ch_l "[Line]"
                "My favorite thing to do is. . .":
                    if "setfav" in LauraX.DailyActions:
                        ch_l "I remember."
                    else:
                        menu:
                            "Sex.":
                                        $ LauraX.FaceChange("sly")
                                        if LauraX.PlayerFav == "sex":
                                            $ LauraX.Statup("Lust", 80, 5)
                                            ch_l "Yeah, I know that. . ."
                                        elif LauraX.Favorite == "sex":
                                            $ LauraX.Statup("Love", 90, 5)
                                            $ LauraX.Statup("Lust", 80, 10)
                                            ch_l "I really like it too!"
                                        elif LauraX.Sex >= 5:
                                            ch_l "Well I don't mind that."
                                        elif not LauraX.Sex:
                                            $ LauraX.FaceChange("perplexed")
                                            ch_l "Who's fucking you?"
                                        else:
                                            $ LauraX.FaceChange("bemused")
                                            ch_l "Heh, um, yeah, it's nice. . ."
                                        $ LauraX.PlayerFav = "sex"

                            "Anal.":
                                        $ LauraX.FaceChange("sly")
                                        if LauraX.PlayerFav == "anal":
                                            $ LauraX.Statup("Lust", 80, 5)
                                            ch_l "So you've said. . ."
                                        elif LauraX.Favorite == "anal":
                                            $ LauraX.Statup("Love", 90, 5)
                                            $ LauraX.Statup("Lust", 80, 10)
                                            ch_l "I love it too!"
                                        elif LauraX.Anal >= 10:
                                            ch_l "Yeah, it's. . . nice. . ."
                                        elif not LauraX.Anal:
                                            $ LauraX.FaceChange("perplexed")
                                            ch_l "Who's fucking you?"
                                        else:
                                            $ LauraX.FaceChange("bemused",Eyes="side")
                                            ch_l "Heh, heh, yeah, um, it's ok. . ."
                                        $ LauraX.PlayerFav = "anal"

                            "Blowjobs.":
                                        $ LauraX.FaceChange("sly")
                                        if LauraX.PlayerFav == "blow":
                                            $ LauraX.Statup("Lust", 80, 3)
                                            ch_l "Yeah, I know."
                                        elif LauraX.Favorite == "blow":
                                            $ LauraX.Statup("Love", 90, 5)
                                            $ LauraX.Statup("Lust", 80, 5)
                                            ch_l "I love your dick!"
                                        elif LauraX.Blow >= 10:
                                            ch_l "Yeah, you're pretty tasty."
                                        elif not LauraX.Blow:
                                            $ LauraX.FaceChange("perplexed")
                                            ch_l "Who's sucking your dick?!"
                                        else:
                                            $ LauraX.FaceChange("bemused")
                                            ch_l "I'm. . . getting used to the taste. . ."
                                        $ LauraX.PlayerFav = "blow"

                            "Titjobs.":
                                        $ LauraX.FaceChange("sly")
                                        if LauraX.PlayerFav == "titjob":
                                            $ LauraX.Statup("Lust", 80, 5)
                                            ch_l "Yeah, you've said that before. . ."
                                        elif LauraX.Favorite == "titjob":
                                            $ LauraX.Statup("Love", 90, 5)
                                            $ LauraX.Statup("Lust", 80, 7)
                                            ch_l "Yeah, I enjoy that too. . ."
                                        elif LauraX.Tit >= 10:
                                            ch_l "It's certainly an interesting experience . . ."
                                        elif not LauraX.Tit:
                                            $ LauraX.FaceChange("perplexed")
                                            ch_l "Who's titfucking you?"
                                        else:
                                            $ LauraX.FaceChange("bemused")
                                            ch_l "That's nice of you to say. . ."
                                            $ LauraX.Statup("Love", 80, 5)
                                            $ LauraX.Statup("Inbt", 50, 10)
                                        $ LauraX.PlayerFav = "titjob"

                            "Footjobs.":
                                        $ LauraX.FaceChange("sly")
                                        if LauraX.PlayerFav == "foot":
                                            $ LauraX.Statup("Lust", 80, 5)
                                            ch_l "Yeah, you've said that. . ."
                                        elif LauraX.Favorite == "foot":
                                            $ LauraX.Statup("Love", 90, 5)
                                            $ LauraX.Statup("Lust", 80, 7)
                                            ch_l "I do like using my feet. . ."
                                        elif LauraX.Foot >= 10:
                                            ch_l "I like it too . . ."
                                        elif not LauraX.Foot:
                                            $ LauraX.FaceChange("perplexed")
                                            ch_l "Who's playing footsie with you?"
                                        else:
                                            $ LauraX.FaceChange("bemused")
                                            ch_l "Yeah, it's nice. . ."
                                        $ LauraX.PlayerFav = "foot"

                            "Handjobs.":
                                        $ LauraX.FaceChange("sly")
                                        if LauraX.PlayerFav == "hand":
                                            $ LauraX.Statup("Lust", 80, 5)
                                            ch_l "Yeah, you've said that. . ."
                                        elif LauraX.Favorite == "hand":
                                            $ LauraX.Statup("Love", 90, 5)
                                            $ LauraX.Statup("Lust", 80, 7)
                                            ch_l "You do feel pretty comfy. . ."
                                        elif LauraX.Hand >= 10:
                                            ch_l "I like it too . . ."
                                        elif not LauraX.Hand:
                                            $ LauraX.FaceChange("perplexed")
                                            ch_l "Who's jerking you off?"
                                        else:
                                            $ LauraX.FaceChange("bemused")
                                            ch_l "Yeah, it's nice. . ."
                                        $ LauraX.PlayerFav = "hand"

                            "Feeling you up.":
                                        $ Cnt = LauraX.FondleB + LauraX.FondleT + LauraX.SuckB + LauraX.Hotdog
                                        $ LauraX.FaceChange("sly")
                                        if LauraX.PlayerFav == "fondle":
                                            $ LauraX.Statup("Lust", 80, 3)
                                            ch_l "Yeah, I think we're clear on that. . ."
                                        elif LauraX.Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            $ LauraX.Statup("Love", 90, 5)
                                            $ LauraX.Statup("Lust", 80, 5)
                                            ch_l "I love when you touch me. . ."
                                        elif Cnt >= 10:
                                            ch_l "Yeah, it's really nice . . ."
                                        elif not Cnt:
                                            $ LauraX.FaceChange("perplexed")
                                            ch_l "Who's letting you feel her up?"
                                        else:
                                            $ LauraX.FaceChange("bemused")
                                            ch_l "I do like how that feels. . ."
                                        $ LauraX.PlayerFav = "fondle"
                                        $ Cnt = 0

                            "Kissing you.":
                                        $ LauraX.FaceChange("sly")
                                        if LauraX.PlayerFav == "kiss you":
                                            $ LauraX.Statup("Love", 90, 3)
                                            ch_l "Such a romantic. . ."
                                        elif LauraX.Favorite == "kiss you":
                                            $ LauraX.Statup("Love", 90, 5)
                                            $ LauraX.Statup("Lust", 80, 5)
                                            ch_l "Hmm, the taste of you on my lips. . ."
                                        elif LauraX.Kissed >= 10:
                                            ch_l "I love kissing you too . . ."
                                        elif not LauraX.Kissed:
                                            $ LauraX.FaceChange("perplexed")
                                            ch_l "Who are you kissing?"
                                        else:
                                            $ LauraX.FaceChange("bemused")
                                            ch_l "I like kissing you too. . ."
                                        $ LauraX.PlayerFav = "kiss you"

                        $ LauraX.DailyActions.append("setfav")

                "What's your favorite thing to do?":
                                if not ApprovalCheck(LauraX, 800):
                                        $ LauraX.FaceChange("perplexed")
                                        ch_l ". . ."
                                else:
                                        if LauraX.SEXP >= 50:
                                            $ LauraX.FaceChange("sly")
                                            ch_l "You should know. . ."
                                        else:
                                            $ LauraX.FaceChange("bemused")
                                            $ LauraX.Eyes = "side"
                                            ch_l "Hmm. . ."


                                        if not LauraX.Favorite or LauraX.Favorite == "kiss":
                                            ch_l "Kissing?"
                                        elif LauraX.Favorite == "anal":
                                                ch_l "Probably anal."
                                        elif LauraX.Favorite == "lick ass":
                                                ch_l "When you lick my ass."
                                        elif LauraX.Favorite == "insert ass":
                                                ch_l "Fingering my asshole, probably."
                                        elif LauraX.Favorite == "sex":
                                                ch_l "Just the usual pounding."
                                        elif LauraX.Favorite == "lick pussy":
                                                ch_l "When you lick my pussy."
                                        elif LauraX.Favorite == "fondle pussy":
                                                ch_l "When you finger me."
                                        elif LauraX.Favorite == "blow":
                                                ch_l "I like how your cock tastes."
                                        elif LauraX.Favorite == "tit":
                                                ch_l "When I use my tits."
                                        elif LauraX.Favorite == "foot":
                                                ch_l "Footjobs are pretty fun."
                                        elif LauraX.Favorite == "hand":
                                                ch_l "I like jerking you off."
                                        elif LauraX.Favorite == "hotdog":
                                                ch_l "When you grind against me."
                                        elif LauraX.Favorite == "suck breasts":
                                                ch_l "When you suck my tits."
                                        elif LauraX.Favorite == "fondle breasts":
                                                ch_l "When you grab my tits."
                                        elif LauraX.Favorite == "fondle thighs":
                                                ch_l "When you rub my thighs."
                                        else:
                                                ch_l "How should I know?"

                                # End Laura's favorite things.

                "Don't talk as much during sex." if "vocal" in LauraX.Traits:
                        if "setvocal" in LauraX.DailyActions:
                            $ LauraX.FaceChange("perplexed")
                            ch_l "Make up your mind."
                        else:
                            if ApprovalCheck(LauraX, 1000) and LauraX.Obed <= LauraX.Love:
                                $ LauraX.FaceChange("bemused")
                                $ LauraX.Statup("Obed", 90, 1)
                                ch_l "Stay quiet, got it."
                                $ LauraX.Traits.remove("vocal")
                            elif ApprovalCheck(LauraX, 700, "O"):
                                $ LauraX.FaceChange("sadside")
                                $ LauraX.Statup("Obed", 90, 1)
                                ch_l ". . ."
                                $ LauraX.Traits.remove("vocal")
                            elif ApprovalCheck(LauraX, 600):
                                $ LauraX.FaceChange("sly")
                                $ LauraX.Statup("Love", 90, -3)
                                $ LauraX.Statup("Obed", 50, -1)
                                $ LauraX.Statup("Inbt", 90, 5)
                                ch_l "Don't push it, [LauraX.Petname]."
                            else:
                                $ LauraX.FaceChange("angry")
                                $ LauraX.Statup("Love", 90, -5)
                                $ LauraX.Statup("Obed", 60, -3)
                                $ LauraX.Statup("Inbt", 90, 10)
                                ch_l "I don't take orders from you, [LauraX.Petname]."

                            $ LauraX.DailyActions.append("setvocal")
                "Talk dirty to me during sex." if "vocal" not in LauraX.Traits:
                        if "setvocal" in LauraX.DailyActions:
                            $ LauraX.FaceChange("perplexed")
                            ch_l "I heard you the first time."
                        else:
                            if ApprovalCheck(LauraX, 1000) and LauraX.Obed <= LauraX.Love:
                                $ LauraX.FaceChange("sly")
                                $ LauraX.Statup("Obed", 90, 2)
                                ch_l "Louder? Ok. . ."
                                $ LauraX.Traits.append("vocal")
                            elif ApprovalCheck(LauraX, 700, "O"):
                                $ LauraX.FaceChange("sadside")
                                $ LauraX.Statup("Obed", 90, 2)
                                ch_l "If you want, [LauraX.Petname]."
                                $ LauraX.Traits.append("vocal")
                            elif ApprovalCheck(LauraX, 600):
                                $ LauraX.FaceChange("sly")
                                $ LauraX.Statup("Obed", 90, 3)
                                ch_l "I guess?"
                                $ LauraX.Traits.append("vocal")
                            else:
                                $ LauraX.FaceChange("angry")
                                $ LauraX.Statup("Inbt", 90, 5)
                                ch_l ". . ."

                            $ LauraX.DailyActions.append("setvocal")
                        # End Laura Dirty Talk

                "Don't do your own thing as much during sex." if "passive" not in LauraX.Traits:
                        if "initiative" in LauraX.DailyActions:
                            $ LauraX.FaceChange("perplexed")
                            ch_l "I heard you the first time."
                        else:
                            if ApprovalCheck(LauraX, 1200) and LauraX.Obed <= LauraX.Love:
                                $ LauraX.FaceChange("bemused")
                                $ LauraX.Statup("Obed", 90, 1)
                                ch_l "Passive, eh?"
                                $ LauraX.Traits.append("passive")
                            elif ApprovalCheck(LauraX, 700, "O"):
                                $ LauraX.FaceChange("sadside")
                                $ LauraX.Statup("Obed", 90, 1)
                                ch_l "I'll try to hold back."
                                $ LauraX.Traits.append("passive")
                            elif ApprovalCheck(LauraX, 600):
                                $ LauraX.FaceChange("sly")
                                $ LauraX.Statup("Love", 90, -3)
                                $ LauraX.Statup("Obed", 50, -1)
                                $ LauraX.Statup("Inbt", 90, 5)
                                ch_l "Hm, no."
                            else:
                                $ LauraX.FaceChange("angry")
                                $ LauraX.Statup("Love", 90, -5)
                                $ LauraX.Statup("Obed", 60, -3)
                                $ LauraX.Statup("Inbt", 90, 10)
                                ch_l "We'll see."

                            $ LauraX.DailyActions.append("initiative")
                "Take more initiative during sex." if "passive" in LauraX.Traits:
                        if "initiative" in LauraX.DailyActions:
                                $ LauraX.FaceChange("perplexed")
                                ch_l "I heard you the first time."
                        else:
                            if ApprovalCheck(LauraX, 1000) and LauraX.Obed <= LauraX.Love:
                                $ LauraX.FaceChange("bemused")
                                $ LauraX.Statup("Obed", 90, 1)
                                ch_l "More active, got it."
                                $ LauraX.Traits.remove("passive")
                            elif ApprovalCheck(LauraX, 700, "O"):
                                $ LauraX.FaceChange("sadside")
                                $ LauraX.Statup("Obed", 90, 1)
                                ch_l "If you insist."
                                $ LauraX.Traits.remove("passive")
                            elif ApprovalCheck(LauraX, 600):
                                $ LauraX.FaceChange("sly")
                                $ LauraX.Statup("Obed", 90, 3)
                                ch_l "We'll see."
                                $ LauraX.Traits.remove("passive")
                            else:
                                $ LauraX.FaceChange("angry")
                                $ LauraX.Statup("Inbt", 90, 5)
                                ch_l "Too much work."

                            $ LauraX.DailyActions.append("initiative")

                "About getting Jumped" if "jumped" in LauraX.History:
                        call Laura_Jumped
                "About when you masturbate":
                    call NoFap(LauraX)

                "Never Mind" if Line == "Yeah, what did you want to talk about?":
                        return
                "That's all." if Line != "Yeah, what did you want to talk about?":
                        return
            if Line == "Yeah, what did you want to talk about?":
                $ Line = "Anything else?"
    return
# End Laura Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


## Laura Chitchat /////////////////// #Work in progress
label Laura_Chitchat(O=0, Options = ["default","default","default"]):
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:

        if LauraX not in Digits:
                if ApprovalCheck(LauraX, 500, "L") or ApprovalCheck(LauraX, 250, "I"):
                    ch_l "Oh, here's my number, in case you need back-up."
                    $ Digits.append(LauraX)
                    return
                elif ApprovalCheck(LauraX, 250, "O"):
                    ch_l "If you need to contact me, here's my number."
                    $ Digits.append(LauraX)
                    return

        if "hungry" not in LauraX.Traits and (LauraX.Swallow + LauraX.Chat[2]) >= 10 and LauraX.Loc == bg_current:  #She's swallowed a lot
                    call Laura_Hungry
                    return

        if "partyfoul" in LauraX.History and "partyfix" not in LauraX.History:
                    call Laura_Foul
                    return

        if bg_current != "bg restaurant" and bg_current != "HW Party" and (not Taboo or ApprovalCheck(LauraX, 800, "I")):
                    if LauraX.Loc == bg_current and LauraX.Thirst >= 30 and "refused" not in LauraX.DailyActions and "quicksex" not in LauraX.DailyActions:
                            $ LauraX.FaceChange("sly",1)
                            ch_l "Hey, wanna bone?"
                            call Quick_Sex(LauraX)
                            return
#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
#        if PunishmentX and "caught chat" not in LauraX.DailyActions:
#            $ Options.append("caught")
        if LauraX.Event[0] and "key" not in LauraX.Chat:
            $ Options.append("key")

        if "mandrill" in Player.Traits and "cologne chat" not in LauraX.DailyActions:
            $ Options.append("mandrill")
        if "purple" in Player.Traits and "cologne chat" not in LauraX.DailyActions:
            $ Options.append("purple")
        if "corruption" in Player.Traits and "cologne chat" not in LauraX.DailyActions:
            $ Options.append("corruption")

        if "Laura" not in LauraX.Names:
            $ Options.append("laura")

        if LauraX.Date >= 1 and bg_current != "bg restaurant":
            #if you've dated before
            $ Options.append("dated")
#        if "cheek" in LauraX.DailyActions and "cheek" not in LauraX.Chat:
#            #If you've touched her cheek today
#            $ Options.append("cheek")
        if LauraX.Kissed >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")
        if "dangerroom" in Player.DailyActions:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
        if "showered" in LauraX.DailyActions:
            #If you've caught Laura showering today
            $ Options.append("showercaught")
        if "fondle breasts" in LauraX.DailyActions or "fondle pussy" in LauraX.DailyActions or "fondle ass" in LauraX.DailyActions:
            #If you've fondled Laura today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in LauraX.Inventory and "256 Shades of Grey" in LauraX.Inventory and "Avengers Tower Penthouse" in LauraX.Inventory:
            #If you've given Laura the books
            if "book" not in LauraX.Chat:
                $ Options.append("booked")
        if "lace bra" in LauraX.Inventory or "lace panties" in LauraX.Inventory:
            #If you've given Laura the lingerie
            if "lingerie" not in LauraX.Chat:
                $ Options.append("lingerie")
        if LauraX.Hand:
            #If Laura's given a handjob
            $ Options.append("handy")
        if LauraX.Swallow:
            #If Laura's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in LauraX.DailyActions or "painted" in LauraX.DailyActions:
            #If Laura's been facialed
            $ Options.append("facial")
        if LauraX.Sleep:
            #If Laura's slept over
            $ Options.append("sleep")
        if LauraX.CreamP or LauraX.CreamA:
            #If Laura's been creampied
            $ Options.append("creampie")
        if LauraX.Sex or LauraX.Anal:
            #If Laura's been sexed
            $ Options.append("sexed")
        if LauraX.Anal:
            #If Laura's been analed
            $ Options.append("anal")

        if "seenpeen" in LauraX.History:
            $ Options.append("seenpeen")
        if "topless" in LauraX.History:
            $ Options.append("topless")
        if "bottomless" in LauraX.History:
            $ Options.append("bottomless")

#        if not LauraX.Chat[0] and LauraX.Sex:
#            $ Options.append("virgin")

#        if (bg_current == "bg laura" or bg_current == "bg player") and "relationship" not in LauraX.DailyActions:
#            if "lover" not in LauraX.Petnames and ApprovalCheck(LauraX, 900, "L"): # LauraX.Event[6]
#                $ Options.append("lover?")
#            elif "sir" not in LauraX.Petnames and ApprovalCheck(LauraX, 500, "O"): # LauraX.Event[7]
#                $ Options.append("sir?")
#            elif "daddy" not in LauraX.Petnames and ApprovalCheck(LauraX, 750, "L") and ApprovalCheck(LauraX, 500, "O") and ApprovalCheck(LauraX, 500, "I"): # LauraX.Event[5]
#                $ Options.append("daddy?")
#            elif "master" not in LauraX.Petnames and ApprovalCheck(LauraX, 900, "O"): # LauraX.Event[8]
#                $ Options.append("master?")
#            elif "sex friend" not in LauraX.Petnames and ApprovalCheck(LauraX, 500, "I"): # LauraX.Event[9]
#                $ Options.append("sexfriend?")
#            elif "fuck buddy" not in LauraX.Petnames and ApprovalCheck(LauraX, 900, "I"): # LauraX.Event[10]
#                $ Options.append("fuckbuddy?")


        if not ApprovalCheck(LauraX, 300):            #She dislikes you
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one

    if Options[0] == "mandrill":
        $ LauraX.DailyActions.append("cologne chat")
        $ LauraX.FaceChange("confused")
        ch_l "(sniff, sniff). . . smells like. . . ape . . ."
        $ LauraX.FaceChange("sexy", 2)
        ch_l ". . . did you want to do something later?"
    elif Options[0] == "purple":
        $ LauraX.DailyActions.append("cologne chat")
        $ LauraX.FaceChange("sly",1)
        ch_l "(sniff, sniff). . . what is that? . ."
        $ LauraX.FaceChange("normal",0)
        ch_l ". . . what was it you wanted?"
    elif Options[0] == "corruption":
        $ LauraX.DailyActions.append("cologne chat")
        $ LauraX.FaceChange("confused")
        ch_l "(sniff, sniff). . . that's a strong scent. . ."
        $ LauraX.FaceChange("angry")
        ch_l ". . . a dangerous scent. . ."
        $ LauraX.FaceChange("sly")

    elif Options[0] == "caught": # Xavier's caught you
            if "caught chat" in LauraX.Chat:
                    ch_l "We should be more careful about getting caught."
                    if not ApprovalCheck(LauraX, 500, "I"):
                         ch_l "Unless. . ."
            else:
                    ch_l "Sorry we got dragged into the Professor's office like that."
                    if not ApprovalCheck(LauraX, 500, "I"):
                        ch_l "I guess you wouldn't want to get it on in public anymore."
                    else:
                        ch_l "I kind of enjoyed it though. . ."
                    $ LauraX.Chat.append("caught chat")
    elif Options[0] == "key": # you have her key
            if LauraX.SEXP <= 15:
                ch_l "I gave you the key for convenience, don't abuse it . ."
            else:
                ch_l "I gave you a key, but you don't visit. . ."
            $ LauraX.Chat.append("key")

#    elif Options[0] == "cheek":
#            #Laura's response to having her cheek touched.
#            ch_l "So,[LauraX.Petname]. . .y'know how you[LauraX.like]kinda just brushed my cheek before?"
#            ch_p "Yeah?  Was that okay?"
#            $ LauraX.FaceChange("smile",1)
#            ch_l "More than just {i}okay{/i}."
#            $ LauraX.Chat.append("cheek")


    elif Options[0] == "laura":
            #if she never told you her name. . .
            ch_l "Oh, by the way, I also go by \"Laura.\" Laura Kinney."
            $ LauraX.Names.append("Laura")
            menu:
                "Oh, that's nice, I think I'll call you that.":
                        $ LauraX.Statup("Love", 70, 5) # Love
                        $ LauraX.Name = "Laura"
                "Ok, but X-23 sounds cooler.":
                        $ LauraX.Statup("Love", 70, -2) # Love
                        $ LauraX.Statup("Obed", 70, 5) # Obed
                        $ LauraX.Name = "X-23"

    elif Options[0] == "dated":
            #Laura's response to having gone on a date with the Player.
            ch_l "That was fun last night, we should do that again some time."

    elif Options[0] == "kissed":
            #Laura's response to having been kissed by the Player.
            $ LauraX.FaceChange("normal",1)
            ch_l "You're pretty good at kissing, [LauraX.Petname]."
            menu:
                extend ""
                "Hey. . .I'm the best there is at what I do.":
                        $ LauraX.FaceChange("smile",1)
                        ch_l "You'll have to back that claim up."
                "No. You think?":
                        ch_l "Do I look like a kidder?"

    elif Options[0] == "dangerroom":
            #Laura's response to Player working out in the Danger Room while Laura is present
            $ LauraX.FaceChange("sly",1)
            ch_l "Hey,[LauraX.Petname].  I saw you in the Danger Room, earlier."
            ch_l "You should probably keep your left up, you were taking too many shots to the head."

    elif Options[0] == "showercaught":
            #Laura's response to being caught in the shower.
            if "shower" in LauraX.Chat:
                ch_l "You saw me taking a shower again. . ."
            else:
                ch_l "Do you make a habit of bursting into the showers?"
                $ LauraX.Chat.append("shower")
                menu:
                    extend ""
                    "It was a total accident!  I promise!":
                            $ LauraX.Statup("Love", 50, 5)
                            $ LauraX.Statup("Love", 90, 2)
                            if ApprovalCheck(LauraX, 1200):
                                $ LauraX.FaceChange("sly",1)
                                ch_l "I didn't mind."
                            $ LauraX.FaceChange("smile")
                            ch_l "We all make mistakes."
                    "Just with you.":
                            $ LauraX.Statup("Obed", 40, 5)
                            if ApprovalCheck(LauraX, 1000) or ApprovalCheck(LauraX, 700, "L"):
                                    $ LauraX.Statup("Love", 90, 3)
                                    $ LauraX.FaceChange("sly",1)
                                    ch_l "Hmm, I guess that's a compliment."
                            else:
                                    $ LauraX.Statup("Love", 70, -5)
                                    $ LauraX.FaceChange("angry")
                                    ch_l "I think I should be insulted."
                    "Totally on purpose. I regret nothing.":
                            if ApprovalCheck(LauraX, 1200):
                                    $ LauraX.Statup("Love", 90, 3)
                                    $ LauraX.Statup("Obed", 70, 10)
                                    $ LauraX.Statup("Inbt", 50, 5)
                                    $ LauraX.FaceChange("sly",1)
                                    ch_l "You seem to know what you want."
                            elif ApprovalCheck(LauraX, 800):
                                    $ LauraX.Statup("Obed", 60, 5)
                                    $ LauraX.Statup("Inbt", 50, 5)
                                    $ LauraX.FaceChange("perplexed",2)
                                    ch_l "I guess you show initiative."
                                    $ LauraX.Blush = 1
                            else:
                                    $ LauraX.Statup("Love", 50, -10)
                                    $ LauraX.Statup("Love", 80, -10)
                                    $ LauraX.Statup("Obed", 50, 10)
                                    $ LauraX.FaceChange("angry")
                                    ch_l "That's a bit disturbing."

    elif Options[0] == "fondled":
            #Laura's response to being felt up.
            if LauraX.FondleB + LauraX.FondleP + LauraX.FondleA >= 15:
                ch_l "I need your hands on me."
            else:
                ch_l "You could feel me up, if you wanted."

    elif Options[0] == "booked":
            #Laura's response after a Player gives her the books from the shop.
            ch_l "Hey, I read those books you gave me."
            menu:
                extend ""
                "Yeah?  Did you like them?":
                        $ LauraX.FaceChange("sly",2)
                        ch_l "They were. . .{i}interesting{/i}."
                "Good.  You looked like you could use to learn a thing or two from them.":
                        $ LauraX.Statup("Love", 90, -3)
                        $ LauraX.Statup("Obed", 70, 5)
                        $ LauraX.Statup("Inbt", 50, 5)
                        $ LauraX.FaceChange("angry")
                        ch_l "I don't see how."
            $ LauraX.Blush = 1
            $ LauraX.Chat.append("book")

    elif Options[0] == "lingerie":
            #Laura's response to being given lingerie.
            $ LauraX.FaceChange("sly",2)
            ch_l "That underwear you got me was kind of uncomfortable, but I do like the look."
            $ LauraX.Blush = 1
            $ LauraX.Chat.append("lingerie")

    elif Options[0] == "handy":
            #Laura's response after giving the Player a handjob.
            $ LauraX.FaceChange("sly",1)
            ch_l "I was thinking about having your cock in my hand the other day. . ."
            ch_l "You seemed to enjoy it."
            $ LauraX.Blush = 0

    elif Options[0] == "blow":
            if "blow" not in LauraX.Chat:
                    #Laura's response after giving the Player a blowjob.
                    $ LauraX.FaceChange("sly",2)
                    ch_l "Hey, so did you like that blowjob?"
                    menu:
                        extend ""
                        "You were totally amazing.":
                                    $ LauraX.Statup("Love", 90, 5)
                                    $ LauraX.Statup("Inbt", 60, 10)
                                    $ LauraX.FaceChange("normal",1)
                                    ch_l "Cool. Cool. . . "
                                    $ LauraX.FaceChange("sexy",1)
                                    ch_l "I'd like another taste sometime."
                        "Honestly? It was good. . .but you could use a little practice, I think.":
                                if ApprovalCheck(LauraX, 300, "I") or not ApprovalCheck(LauraX, 800):
                                    $ LauraX.Statup("Love", 90, -5)
                                    $ LauraX.Statup("Obed", 60, 10)
                                    $ LauraX.Statup("Inbt", 50, 10)
                                    $ LauraX.FaceChange("perplexed",1)
                                    ch_l "Yeah? Sorry to disappoint."
                                else:
                                    $ LauraX.Statup("Obed", 70, 15)
                                    $ LauraX.Statup("Inbt", 50, 5)
                                    $ LauraX.FaceChange("sexy",1)
                                    ch_l "Yeah? I suppose we could keep trying until I get it right."
                        "I guess. If you're into weird sounds and too much teeth. Spoiler, I'm not.":
                                $ LauraX.Statup("Love", 90, -10)
                                $ LauraX.Statup("Obed", 60, 10)
                                $ LauraX.FaceChange("angry",2)
                                ch_l "Well, good luck with that then."
                    $ LauraX.Blush = 1
                    $ LauraX.Chat.append("blow")
            else:
                    $ Line = renpy.random.choice(["I gotta tell you, your dick tastes great.",
                            "I think I nearly dislocated my jaw last time.",
                            "Let me know if you'd like another blowjob sometime.",
                            "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
                    ch_l "[Line]"

    elif Options[0] == "swallowed":
            #Laura's response after swallowing the Player's cum.
            if "swallow" in LauraX.Chat:
                ch_l "Hey, I wouldn't mind another taste of you some time."
            else:
                ch_l "So. . . the other day. . ."
                ch_l "That was the first time I'd really enjoyed the taste of jiz."
                $ LauraX.FaceChange("sly",1)
                ch_l "Good job!"
                $ LauraX.Chat.append("swallow")

    elif Options[0] == "facial":
            #Laura's response after taking a facial from the Player.
            ch_l "Hey. . .I know this is kind of odd. . ."
            $ LauraX.FaceChange("sexy",2)
            ch_l "I feel so {i}good{/i} with your jiz on my face."
            $ LauraX.Blush = 1

    elif Options[0] == "sleepover":
            #Laura's response after sleeping with the Player.
            ch_l "I really enjoyed the other night."
            ch_l "It felt so safe sleeping next to someone else."

    elif Options[0] == "creampie":
            #Another of Laura's responses after having sex with the Player.
            "[LauraX.Name] draws close to you so she can whisper into your ear."
            ch_l "I can still feel you. . .running down the inside of my thigh."

    elif Options[0] == "sexed":
            #A final response from Laura after having sex with the Player.
            ch_l "So. . . you should know. . ."
            $ LauraX.FaceChange("sexy",2)
            ch_l ". . .lately when I've been flicking the bean. . ."
            ch_l "I've been thinking about you inside of me."
            $ LauraX.Blush = 1

    elif Options[0] == "anal":
            #Laura's response after getting anal from the Player.
            $ LauraX.FaceChange("sly")
            ch_l "I did't really enjoy anal much."
            $ LauraX.FaceChange("sexy",1)
            ch_l "Until you, at least."

    elif Options[0] == "seenpeen": # first seen peen skipped
            $ LauraX.FaceChange("sly",1, Eyes="down")
            ch_l "I forgot to tell you, you've got a pretty nice cock down there. . ."
            $ LauraX.FaceChange("bemused",1)
            $ LauraX.Statup("Love", 50, 5)
            $ LauraX.History.remove("seenpeen")
    elif Options[0] == "topless": # first seen breasts skipped
            ch_l "Hey,what'd you think of my tits?"
            ch_l "Did you like what you saw?"
            call Laura_First_TMenu
            $ LauraX.History.remove("topless")
    elif Options[0] == "bottomless": # first seen pussy skipped
            ch_l "Hey, what'd you think when you saw my pussy earlier?"
            call Laura_First_BMenu
            $ LauraX.History.remove("bottomless")

#    elif Options[0] == "boyfriend?":
#        call Laura_BF
#    elif Options[0] == "lover?":
#        call Laura_Love
#    elif Options[0] == "sir?":
#        call Laura_Sub
#    elif Options[0] == "master?":
#        call Laura_Master
#    elif Options[0] == "sexfriend?":
#        call Laura_Sexfriend
#    elif Options[0] == "fuckbuddy?":
#        call Laura_Fuckbuddy
#    elif Options[0] == "daddy?":
#        call Laura_Daddy

    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["Get away from me.",
                "I don't want to smell you near me.",
                "Back off.",
                "Buzz off."])
        ch_l "[Line]"

    else: #all else fell through. . .
            $ D20 = renpy.random.randint(1, 21)
            if D20 == 1:
                    $ LauraX.FaceChange("smile")
                    ch_l "I got a good grade on that bio test."
            elif D20 == 2:
                    $ LauraX.FaceChange("annoyed")
                    ch_l "If I have to hear him say \"I'm the best there is\" one more time, I swear I'm going ..."
            elif D20 == 3:
                    $ LauraX.FaceChange("surprised")
                    ch_l "Huh? Oh, sorry. I sort of spaced out. That's not like me."
            elif D20 == 4:
                    $ LauraX.FaceChange("sad")
                    ch_l "Oh, [LauraX.Petname]. I was just remembering something. Don't worry about it."
            elif D20 == 5:
                    $ LauraX.FaceChange("smile")
                    ch_l "I had a good nap. It's nice to be somewhere I can just doze off without worry."
            elif D20 == 6:
                    $ LauraX.FaceChange("perplexed")
                    ch_l "Oh, [LauraX.Petname]. I think I just saw Emma Frost staring at Cyclops. That's... wierd."
            elif D20 == 7:
                    $ LauraX.FaceChange("smile")
                    ch_l "I just got a new personal best time in the Danger Room."
            elif D20 == 8:
                    $ LauraX.FaceChange("sad")
                    ch_l "I like being here, but sometimes there's just so much noise..."
            elif D20 == 9:
                    $ LauraX.FaceChange("confused")
                    ch_l "I'm still trying to figure out what the mystery meat in the cafeteria was today."
                    ch_l "I have enhanced senses, this shouldn't be so difficult!"
            elif D20 == 10:
                    $ LauraX.FaceChange("smile")
                    ch_l "Kitty, Rogue and some of the others asked me if I wanted to go grab some ice cream with them tomorrow."
            elif D20 == 11:
                    $ LauraX.FaceChange("smile")
                    ch_l "I tried out a dance class like Kitty said. Apparently I'm good at it."
            elif D20 == 12:
                    $ LauraX.FaceChange("sad")
                    ch_l "I like talking to Kitty and the others. It makes me feel, I don't know. . ."
                    ch_l "{i}not{/i} like a really dangerous mutant who could kill everyone around me if I flipped out."
            elif D20 == 13:
                    $ LauraX.FaceChange("smile")
                    ch_l "Kitty and Rogue dared me to call Logan \"Dad\". I think we might've given him a heart attack."
            elif D20 == 14:
                    $ LauraX.FaceChange("sad")
                    ch_l "I like going out on missions, but catching up with what's been going on while I'm gone is always a pain."
            elif D20 == 15:
                    $ LauraX.FaceChange("perplexed")
                    ch_l "So they're called the \"Avengers\", but do they ever do any avenging?"
                    ch_l "At least the Fantastic Four really do things that are strange and fantastic."
            elif D20 == 16:
                    $ LauraX.FaceChange("perplexed")
                    ch_l "Have you ever been to New York? Sometimes I'm surprised anyone still wants to live there."
            elif D20 == 17:
                    $ LauraX.FaceChange("perplexed")
                    ch_l "Logan just walked up and told me that if I ever meet someone called. . ."
                    ch_l "\"Dead...Poole?\"...I should just go ahead and stab him in the face."
                    ch_l "What's up with that?"
            elif D20 == 18:
                    $ LauraX.FaceChange("smile")
                    ch_l "Don't tell anyone this, but I think Cyclops is kind of wound up tight."
            elif D20 == 19:
                    $ LauraX.FaceChange("confused")
                    ch_l "Do you smell something? Is that... nachos and... chocolate syrup?!"
            elif D20 == 20:
                    $ LauraX.FaceChange("smile")
                    ch_l "I like being able to just talk about nothing in particular. It's... nice."
            else:
                    $ LauraX.FaceChange("smile")
                    ch_l "You're fun to hang with."

    $ Line = 0
    return

# start Laura_Names//////////////////////////////////////////////////////////
label Laura_Names:
    menu:
        ch_l "Oh? What would you like me to call you?"
        "My initial's fine.":
            $ LauraX.Petname = Player.Name[:1]  #fix test this
            ch_l "You got it, [LauraX.Petname]."
        "Call me by my name.":
            $ LauraX.Petname = Player.Name
            ch_l "If you'd rather, [LauraX.Petname]."
        "Call me \"boyfriend\"." if "boyfriend" in LauraX.Petnames:
            $ LauraX.Petname = "boyfriend"
            ch_l "Sure thing, [LauraX.Petname]."
        "Call me \"lover\"." if "lover" in LauraX.Petnames:
            $ LauraX.Petname = "lover"
            ch_l "Oooh, love to, [LauraX.Petname]."
        "Call me \"sir\"." if "sir" in LauraX.Petnames:
            $ LauraX.Petname = "sir"
            ch_l "Yes, [LauraX.Petname]."
        "Call me \"master\"." if "master" in LauraX.Petnames:
            $ LauraX.Petname = "master"
            ch_l "As you wish, [LauraX.Petname]."
        "Call me \"sex friend\"." if "sex friend" in LauraX.Petnames:
            $ LauraX.Petname = "sex friend"
            ch_l "Heh, very cheeky, [LauraX.Petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in LauraX.Petnames:
            $ LauraX.Petname = "fuck buddy"
            ch_l "I'm game if you are, [LauraX.Petname]."
        "Call me \"daddy\"." if "daddy" in LauraX.Petnames:
            $ LauraX.Petname = "daddy"
            ch_l "Oh! You bet, [LauraX.Petname]."
        "Bub works.":
            $ LauraX.Petname = "bub"
            ch_l "You got it, bub."
        "Nevermind.":
            return
    return
# end Laura_Names//////////////////////////////////////////////////////////

label Laura_Pet:
    while 1:
        menu:
            extend ""
            "Polite":
                menu:
                    "I think I'll call you. . ."
                    "Laura.":
                        $ LauraX.Pet = "Laura"
                        ch_l "I don't see why not, [LauraX.Petname]."

                    "X-23.":
                        $ LauraX.Pet = "X-23"
                        if ApprovalCheck(LauraX, 700, "L") and not ApprovalCheck(LauraX, 500, "O"):
                                ch_l "Oh, if you say so, [LauraX.Petname]."
                        else:
                                ch_l "I don't see why not, [LauraX.Petname]."

                    "\"girl\".":
                        $ LauraX.Pet = "girl"
                        if "boyfriend" in LauraX.Petnames or ApprovalCheck(LauraX, 600, "L"):
                            $ LauraX.FaceChange("sexy", 1)
                            ch_l "I'm totally your girl, [LauraX.Petname]."
                        else:
                            $ LauraX.FaceChange("angry")
                            ch_l "I'm NOT your girl, [LauraX.Petname]."

                    "\"boo\".":
                        $ LauraX.Pet = "boo"
                        if "boyfriend" in LauraX.Petnames or ApprovalCheck(LauraX, 700, "L"):
                            $ LauraX.FaceChange("sexy", 1)
                            ch_l "I am your boo, [LauraX.Petname]."
                        else:
                            $ LauraX.FaceChange("angry")
                            ch_l "I'm NOT your boo,  [LauraX.Petname]."

                    "\"bae\".":
                        $ LauraX.Pet = "bae"
                        if "boyfriend" in LauraX.Petnames or ApprovalCheck(LauraX, 600, "L"):
                            $ LauraX.FaceChange("sexy", 1)
                            ch_l "I am your bae, [LauraX.Petname]."
                        else:
                            $ LauraX.FaceChange("angry")
                            ch_l "I'm NOT your bae,  [LauraX.Petname]."

                    "\"baby\".":
                        $ LauraX.Pet = "baby"
                        if "boyfriend" in LauraX.Petnames or ApprovalCheck(LauraX, 500, "L"):
                            $ LauraX.FaceChange("sexy", 1)
                            ch_l "Cute, [LauraX.Petname]."
                        else:
                            $ LauraX.FaceChange("angry")
                            ch_l "I am not a baby."


                    "\"sweetie\".":
                        $ LauraX.Pet = "sweetie"
                        if "boyfriend" in LauraX.Petnames or ApprovalCheck(LauraX, 600, "L"):
                            ch_l "Aw, that's sweet, [LauraX.Petname]."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Too sweet, [LauraX.Petname]."

                    "\"sexy\".":
                        $ LauraX.Pet = "sexy"
                        if "lover" in LauraX.Petnames or ApprovalCheck(LauraX, 800):
                            $ LauraX.FaceChange("sexy", 1)
                            ch_l "You know it, [LauraX.Petname]."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Pushing a line there, [LauraX.Petname]."

                    "\"lover\".":
                        $ LauraX.Pet = "lover"
                        if "lover" in LauraX.Petnames or ApprovalCheck(LauraX, 1200):
                            $ LauraX.FaceChange("sexy", 1)
                            ch_l "I know."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "I don't think so, [LauraX.Petname]."

                    "\"Wolvie\".":
                        $ LauraX.Pet = "Wolvie"
                        if ApprovalCheck(LauraX, 500, "I"):
                            $ LauraX.FaceChange("sexy", 1)
                            ch_l "Heh, ok, [LauraX.Petname]."
                        else:
                            $ LauraX.FaceChange("angry")
                            ch_l "Not really that cute, [LauraX.Petname]"

                    "Back":
                        pass

            "Risky":
                menu:
                    "I think I'll call you. . ."
                    "\"slave\".":
                        $ LauraX.Pet = "slave"
                        if "master" in LauraX.Petnames or ApprovalCheck(LauraX, 800, "O"):
                            $ LauraX.FaceChange("bemused", 1)
                            ch_l "As you wish, [LauraX.Petname]."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "I am not your slave, [LauraX.Petname]."

                    "\"pet\".":
                        $ LauraX.Pet = "pet"
                        if "master" in LauraX.Petnames or ApprovalCheck(LauraX, 650, "O"):
                            $ LauraX.FaceChange("bemused", 1)
                            ch_l "You can pet me if you want, [LauraX.Petname]."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "I am no one's pet, [LauraX.Petname]."

                    "\"slut\".":
                        $ LauraX.Pet = "slut"
                        if "sex friend" in LauraX.Petnames or ApprovalCheck(LauraX, 900, "OI"):
                            $ LauraX.FaceChange("sexy")
                            ch_l "Fair enough."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            $ LauraX.Mouth = "surprised"
                            ch_l "I'd like to see you try it with a busted jaw."

                    "\"whore\".":
                        $ LauraX.Pet = "whore"
                        if "fuckbuddy" in LauraX.Petnames or ApprovalCheck(LauraX, 1000, "OI"):
                            $ LauraX.FaceChange("sly")
                            ch_l "I mean. . ."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "If either of us is going to be turning tricks. . ."

                    "\"sugartits\".":
                        $ LauraX.Pet = "sugartits"
                        if "sex friend" in LauraX.Petnames or ApprovalCheck(LauraX, 1400):
                            $ LauraX.FaceChange("sly", 1)
                            ch_l "That doesn't even make sense."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Not cool."

                    "\"sex friend\".":
                        $ LauraX.Pet = "sex friend"
                        if "sex friend" in LauraX.Petnames or ApprovalCheck(LauraX, 600, "I"):
                            $ LauraX.FaceChange("sly")
                            ch_l "Yeah. . ."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Keep it down, [LauraX.Petname]."

                    "\"fuckbuddy\".":
                        $ LauraX.Pet = "fuckbuddy"
                        if "fuckbuddy" in LauraX.Petnames or ApprovalCheck(LauraX, 700, "I"):
                            $ LauraX.FaceChange("sly")
                            ch_l "Yup."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            $ LauraX.Mouth = "surprised"
                            ch_l "Don't even joke, [LauraX.Petname]."

                    "\"baby girl\".":
                        $ LauraX.Pet = "baby girl"
                        if "daddy" in LauraX.Petnames or ApprovalCheck(LauraX, 1200):
                            $ LauraX.FaceChange("smile", 1)
                            ch_l "I guess?"
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Weirdo."

                    "Back":
                        pass

            "Nevermind.":
                return
    return

#label Laura_Namecheck(LauraX.Pet = LauraX.Pet, Cnt = 0, Ugh = 0): #replaced with $ Girl.NameCheck() #checks reaction to petname


# start Laura_Rename//////////////////////////////////////////////////////////
label Laura_Rename:
        #Sets alternate names from Laura
        $ LauraX.Mouth = "smile"
        ch_l "Yeah?"
        menu:
            extend ""
            "I think \"Laura's\" a pretty name." if LauraX.Name != "Laura" and "Laura" in LauraX.Names:
                    $ LauraX.Name = "Laura"
                    ch_l "Sounds good."
            "I thought \"X-23\" sounded cool." if LauraX.Name != "X-23" and "X-23" in LauraX.Names:
                    if not ApprovalCheck(LauraX, 500, "O") and not ApprovalCheck(LauraX, 800, "L"):
                            ch_l "I've put that name behind me, I'd rather not. . ."
                    else:
                            if not ApprovalCheck(LauraX, 500, "O"):
                                    $ LauraX.FaceChange("sadside", 0,Brows="normal")
                            if "namechange" not in LauraX.DailyActions:
                                    $ LauraX.Statup("Love", 70, -2)
                                    $ LauraX.Statup("Obed", 70, 5)
                            $ LauraX.Name = "X-23"
                            ch_l "Oh, sure. . . I could go by that again. . ."
            "I liked the sound of \"Wolverine.\"" if LauraX.Name != "Wolverine" and "Wolverine" in LauraX.Names:
                    $ LauraX.FaceChange("confused", 1)
                    if ApprovalCheck(LauraX, 500, "O") or ApprovalCheck(LauraX, 500, "I"):
                            $ LauraX.Name = "Wolverine"
                            $ LauraX.FaceChange("confused", 1)
                            if "namechange" not in LauraX.DailyActions:
                                    $ LauraX.Statup("Obed", 70, 2)
                                    $ LauraX.Statup("Inbt", 50, 2)
                            ch_l "I guess I could give that one a go. . ."
                    else:
                            $ LauraX.Blush = 2
                            ch_l "I. . . really don't think that would work for me. . ."
                    $ LauraX.FaceChange()
            "Nevermind.":
                    pass
        $ LauraX.AddWord(1,0,"namechange")
        return
# end Laura_Rename//////////////////////////////////////////////////////////


# start Laura_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Laura_Personality(Cnt = 0):
    if not LauraX.Chat[4] or Cnt:
        "Since you're doing well in one area, you can convince Laura to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_l "Yeah? What's up?"
        "More Obedient. [[Love to Obedience]" if LauraX.Love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_l "If you really care about that, sure."
            $ LauraX.Chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if LauraX.Love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_l "I could always be a bit more wild if that's what you want."
            $ LauraX.Chat[4] = 2

        "Less Inhibited. [[Obedience to Inhibition]" if LauraX.Obed > 900:
            ch_p "I want you to be less inhibited."
            ch_l "I guess I could go all-out."
            $ LauraX.Chat[4] = 3
        "More Loving. [[Obedience to Love]" if LauraX.Obed > 900:
            ch_p "I'd like you to learn to love me."
            ch_l "I can try."
            $ LauraX.Chat[4] = 4

        "More Obedient. [[Inhibition to Obedience]" if LauraX.Inbt > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_l "I can give it a shot. . ."
            $ LauraX.Chat[4] = 5

        "More Loving. [[Inhibition to Love]" if LauraX.Inbt > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_l "If that's something you need out of this. . ."
            $ LauraX.Chat[4] = 6

        "I guess just do what you like. . .[[reset]" if LauraX.Chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_l "Um, ok."
            $ LauraX.Chat[4] = 0
        "Repeat the rules":
            call Laura_Personality(1)
            return
        "Nevermind.":
            return
    return
    
label Laura_Clothes:
    if LauraX.Taboo:
            if "exhibitionist" in LauraX.Traits:
                ch_l "Yes? . ."
            elif ApprovalCheck(LauraX, 900, TabM=4) or ApprovalCheck(LauraX, 400, "I", TabM=3):
                ch_l "I don't think I'm supposed to undress around here. . ."
            else:
                ch_l "I don't think I'm supposed to undress around here. . ."
                ch_l "Can we talk about this in our rooms?"
                return
    elif ApprovalCheck(LauraX, 900, TabM=4) or ApprovalCheck(LauraX, 600, "L") or ApprovalCheck(LauraX, 300, "O"):
                ch_l "Oh? What about them?"
    else:
                ch_l "I don't think about my clothes much."
                ch_l "You shouldn't either."
                return

    if Girl != LauraX or Line == "Giftstore":
            #This culls returns if sent from another girl
            $ renpy.pop_call()
    $ Line = 0
    $ Girl = LauraX
    call Shift_Focus(Girl)

label Laura_Wardrobe_Menu:
    $ LauraX.FaceChange()
    $ Trigger = 1 # to prevent Focus swapping. . .
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
                        call Clothes_Schedule(LauraX)

            "Could I get a look at it?" if LauraX.Loc != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(LauraX,0,2)
                    if _return:
                        show PhoneSex zorder 150
                        ch_l "Ok, that good?"
                    hide PhoneSex
            "Could I get a look at it?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(LauraX,0,2)
                    if _return:
                        hide DressScreen
            "Would you be more comfortable behind a screen? (locked)" if LauraX.Taboo:
                    pass
            "Would you be more comfortable behind a screen?" if LauraX.Loc == bg_current and not LauraX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    if ApprovalCheck(LauraX, 1500) or (LauraX.SeenChest and LauraX.SeenPussy):
                            ch_l "Probably won't need it, thanks."
                    else:
                            show DressScreen zorder 150
                            ch_l "Yeah, this is better, thanks."

            "Gift for you (locked)" if Girl.Loc != bg_current:
                            pass
            "Gift for you" if Girl.Loc == bg_current:
                            ch_p "I'd like to give you something."
                            call Gifts #(Girl)

            "Switch to. . .":
                    if renpy.showing('DressScreen'):
                            call OutfitShame(LauraX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ LauraX.OutfitChange()
                    $ LauraX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ Trigger = 0
                    call Switch_Chat
                    if Girl != LauraX:
                            ch_p "I wanted to talk about your clothes."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = LauraX
                    call Shift_Focus(Girl)

            "Never mind, you look good like that.":
                    if "wardrobe" not in LauraX.RecentActions:
                            #Apply stat boosts only if it's the first time this turn
                            if LauraX.Chat[1] <= 1:
                                    $ LauraX.Statup("Love", 70, 15)
                                    $ LauraX.Statup("Obed", 40, 20)
                                    ch_l "Oh! Thank you."
                            elif LauraX.Chat[1] <= 10:
                                    $ LauraX.Statup("Love", 70, 5)
                                    $ LauraX.Statup("Obed", 40, 7)
                                    ch_l "Right?"
                            elif LauraX.Chat[1] <= 50:
                                    $ LauraX.Statup("Love", 70, 1)
                                    $ LauraX.Statup("Obed", 40, 1)
                                    ch_l "Uh-huh."
                            else:
                                    ch_l "Sure."
                            $ LauraX.RecentActions.append("wardrobe")
                    if renpy.showing('DressScreen'):
                            call OutfitShame(LauraX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ LauraX.OutfitChange()
                    $ LauraX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ LauraX.Chat[1] += 1
                    $ Trigger = 0
                    return

        #Loops back up
        #return #jump Laura_Clothes
        #End of Laura Wardrobe Main Menu

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Laura_Clothes_Outfits:
        # Outfits
        "You should remember that one. [[Set Custom]":
                menu:
                    "Which slot would you like this saved in?"
                    "Custom 1":
                                call OutfitShame(LauraX,3,1)
                    "Custom 2":
                                call OutfitShame(LauraX,5,1)
                    "Custom 3":
                                call OutfitShame(LauraX,6,1)
                    "Gym Clothes":
                                call OutfitShame(LauraX,4,1)
                    "Sleepwear":
                                call OutfitShame(LauraX,7,1)
                    "Swimwear":
                                call OutfitShame(LauraX,10,1)
                    #8 is Emma's teaching clothes,
                    "Never mind":
                                pass

        "Leather combat outfit":
                $ LauraX.OutfitChange("casual1")
                menu:
                    "You should wear this one out. [[set current outfit]":
                            $ LauraX.Outfit = "casual1"
                            $ LauraX.Shame = 0
                            ch_l "Yeah, I love wearing this one in the field."
                    "Let's try something else though.":
                            ch_l "Ok."

        "Leather jacket and skirt combo":
                $ LauraX.OutfitChange("casual2")
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
                $ Cnt = 0
                while 1:
                    menu:
                        "Throw on Custom 1 (locked)" if not LauraX.Custom1[0]:
                                pass
                        "Throw on Custom 1" if LauraX.Custom1[0]:
                                $ LauraX.OutfitChange("custom1")
                                $ Cnt = 3
                        "Throw on Custom 2 (locked)" if not LauraX.Custom2[0]:
                                pass
                        "Throw on Custom 2" if LauraX.Custom2[0]:
                                $ LauraX.OutfitChange("custom2")
                                $ Cnt = 5
                        "Throw on Custom 3 (locked)" if not LauraX.Custom3[0]:
                                pass
                        "Throw on Custom 3" if LauraX.Custom3[0]:
                                $ LauraX.OutfitChange("custom3")
                                $ Cnt = 6

                        "You should wear this one in private. (locked)" if not Cnt:
                                pass
                        "You should wear this one in private." if Cnt:
                                if Cnt == 5:
                                    $ LauraX.Clothing[9] = "custom2"
                                elif Cnt == 6:
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

                        "You should wear this one out. [[choose outfit first](locked)" if not Cnt:
                                pass
                        "You should wear this one out." if Cnt:
                                call Custom_Out(LauraX,Cnt)
                        "Ok, back to what we were talking about. . .":
                                $ Cnt = 0
                                return #jump Laura_Clothes

        "Gym Clothes?" if not LauraX.Taboo or bg_current == "bg dangerroom":
                $ LauraX.OutfitChange("gym")

        "Sleepwear?" if not LauraX.Taboo:
                if ApprovalCheck(LauraX, 1200):
                        $ LauraX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(LauraX)
                        if _return:
                            $ LauraX.OutfitChange("sleep")

        "Swimwear? (locked)" if (LauraX.Taboo and bg_current != "bg pool") or not LauraX.Swim[0]:
                $ LauraX.OutfitChange("swimwear")
        "Swimwear?" if (not LauraX.Taboo or bg_current == "bg pool") and LauraX.Swim[0]:
                $ LauraX.OutfitChange("swimwear")

        "Halloween Costume?" if "halloween" in LauraX.History:
                ch_l "Ok."
                $ LauraX.OutfitChange("costume")

        "Your birthday suit looks really great. . .":
                #Nude
                $ LauraX.FaceChange("sexy", 1)
                $ Line = 0
                if not LauraX.Chest and not LauraX.Panties and not LauraX.Over and not LauraX.Legs and not LauraX.Hose:
                    ch_l "Yeah. . . wait, how would you know?"
                elif LauraX.SeenChest and LauraX.SeenPussy and ApprovalCheck(LauraX, 1200, TabM=4):
                    ch_l "You know it. . ."
                    $ Line = 1
                elif ApprovalCheck(LauraX, 2000, TabM=4):
                    ch_l "Skipping straight to that?"
                    $ Line = 1
                elif LauraX.SeenChest and LauraX.SeenPussy and ApprovalCheck(LauraX, 1200, TabM=0):
                    ch_l "Maybe, but not here. . ."
                elif ApprovalCheck(LauraX, 2000, TabM=0):
                    ch_l "Maybe, but not here. . ."
                elif ApprovalCheck(LauraX, 1000, TabM=0):
                    $ LauraX.FaceChange("confused", 1,Mouth="smirk")
                    ch_l "Yeah, but I'm not exactly showing it off."
                    $ LauraX.FaceChange("bemused", 0)
                else:
                    $ LauraX.FaceChange("angry", 1)
                    ch_l "What's it to you?"

                if Line:
                    #If she got nude. . .
                    $ LauraX.OutfitChange("nude")
                    "She throws her clothes off at her feet."
                    call Laura_First_Topless
                    call Laura_First_Bottomless(1)
                    $ LauraX.FaceChange("sexy")
                    menu:
                        "You know, you should wear this one out. [[set current outfit]":
                            if "exhibitionist" in LauraX.Traits:
                                ch_l "mmmm. . ."
                                $ LauraX.Outfit = "nude"
                                $ LauraX.Statup("Lust", 50, 10)
                                $ LauraX.Statup("Lust", 70, 5)
                                $ LauraX.Shame = 50
                            elif ApprovalCheck(LauraX, 800, "I") or ApprovalCheck(LauraX, 2800, TabM=0):
                                ch_l "Exciting. . ."
                                $ LauraX.Outfit = "nude"
                                $ LauraX.Shame = 50
                            else:
                                $ LauraX.FaceChange("sexy", 1)
                                $ LauraX.Eyes = "surprised"
                                ch_l "I probably shouldn't. Sorry."

                        "Let's try something else though.":
                            if "exhibitionist" in LauraX.Traits:
                                ch_l "Are you sure?"
                            elif ApprovalCheck(LauraX, 800, "I") or ApprovalCheck(LauraX, 2800, TabM=0):
                                $ LauraX.FaceChange("bemused", 1)
                                ch_l "I was worried you expected me to go out like this."
                                ch_l ". . ."
                            else:
                                $ LauraX.FaceChange("confused", 1)
                                ch_l "I don't mind you seeing my body, but. . ."
                $ Line = 0

        "Never mind":
            return #jump Laura_Clothes

    return #jump Laura_Clothes
    #End of Laura Outfits

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Laura_Clothes_Over:
        # Overshirts
        "Why don't you go with no [LauraX.Over]?" if LauraX.Over:
                $ LauraX.FaceChange("bemused", 1)
                if ApprovalCheck(LauraX, 800, TabM=3) and (LauraX.Chest or LauraX.SeenChest):
                    ch_l "Ok."
                elif ApprovalCheck(LauraX, 600, TabM=0):
                    call Laura_NoBra
                    if not _return:
                        if not ApprovalCheck(LauraX, 1200):
                            call Display_DressScreen(LauraX)
                            if not _return:
                                return #jump Laura_Clothes
                        else:
                                return #jump Laura_Clothes
                else:
                    call Display_DressScreen(LauraX)
                    if not _return:
                            ch_l "Not right now."
                            if not LauraX.Chest:
                                ch_l "I don't have anything under this. . ."
                            return #jump Laura_Clothes
                $ Line = LauraX.Over
                $ LauraX.Over = 0
                "She throws her [Line] at her feet."
                if not LauraX.Chest and not renpy.showing('DressScreen'):
                        call Laura_First_Topless

        "Try on that leather jacket." if LauraX.Over != "jacket":
                $ LauraX.FaceChange("bemused")
                if not LauraX.Over or LauraX.Chest == "leather bra":
                    #if she's not already wearing a top, or has the leather bra on
                    ch_l "Sure."
                elif ApprovalCheck(LauraX, 800, TabM=0):
                    ch_l "Yeah, ok."
                else:
                    call Display_DressScreen(LauraX)
                    if not _return:
                            $ LauraX.FaceChange("bemused", 1)
                            ch_l "I don't really want to take this [LauraX.Over] off at the moment."
                            return #jump Laura_Clothes
                $ LauraX.Over = "jacket"

        "Maybe just throw on a towel?" if LauraX.Over != "towel":
                $ LauraX.FaceChange("bemused", 1)
                if LauraX.Chest or LauraX.SeenChest:
                    ch_l "Weird."
                elif ApprovalCheck(LauraX, 1000, TabM=0):
                    $ LauraX.FaceChange("perplexed", 1)
                    ch_l "Huh, ok . ."
                else:
                    call Display_DressScreen(LauraX)
                    if not _return:
                            ch_l "That wouldn't look right."
                            return #jump Laura_Clothes
                $ LauraX.Over = "towel"

        "Never mind":
            pass
    return #jump Laura_Clothes
    #End of Laura Top

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Laura_NoBra:
        menu:
            ch_l "I don't exactly have anything on under this. . ."
            "Then you could slip something on under it. . .":
                        if LauraX.SeenChest and ApprovalCheck(LauraX, 1000, TabM=3):
                                $ LauraX.Blush = 1
                                ch_l "-I didn't say that I minded. . ."
                                $ LauraX.Blush = 0
                        elif ApprovalCheck(LauraX, 1200, TabM=4):
                                $ LauraX.Blush = 1
                                ch_l "-I didn't say that I minded. . ."
                                $ LauraX.Blush = 0
                        elif ApprovalCheck(LauraX, 900, TabM=2) and "lace corset" in LauraX.Inventory:
                                ch_l "I guess I could find something."
                                $ LauraX.Chest  = "lace corset"
                                "She pulls out her lace corset and slips it under her [LauraX.Over]."
                        elif ApprovalCheck(LauraX, 700, TabM=2) and "corset" in LauraX.Inventory:
                                ch_l "I guess I could find something."
                                $ LauraX.Chest  = "corset"
                                "She pulls out her corset and slips it under her [LauraX.Over]."
                        elif ApprovalCheck(LauraX, 600, TabM=2):
                                ch_l "Yeah, I guess."
                                $ LauraX.Chest = "leather bra"
                                "She pulls out her leather bra and slips it on under her [LauraX.Over]."
                        else:
                                ch_l "Yeah, I don't think so."
                                return 0

            "You could always just wear nothing at all. . .":
                        if ApprovalCheck(LauraX, 1100, "LI", TabM=2) and LauraX.Love > LauraX.Inbt:
                                ch_l "For you? I guess. . ."
                        elif ApprovalCheck(LauraX, 700, "OI", TabM=2) and LauraX.Obed > LauraX.Inbt:
                                ch_l "Sure. . ."
                        elif ApprovalCheck(LauraX, 600, "I", TabM=2):
                                ch_l "Yeah. . ."
                        elif ApprovalCheck(LauraX, 1300, TabM=2):
                                ch_l "Okay, fine."
                        else:
                                $ LauraX.FaceChange("surprised")
                                $ LauraX.Brows = "angry"
                                if LauraX.Taboo > 20:
                                    ch_l "Not in public, I won't!"
                                else:
                                    ch_l "You're not that cute, [LauraX.Petname]!"
                                return 0
            "Never mind.":
                        ch_l "Ok. . ."
                        return 0
        return 1
        #End of Laura bra check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Laura_Clothes_Legs:
        # Leggings
        "Maybe go without the [LauraX.Legs]." if LauraX.Legs:
                $ LauraX.FaceChange("sexy", 1)
                if LauraX.SeenPanties and LauraX.Panties and ApprovalCheck(LauraX, 500, TabM=5):
                    ch_l "Ok, sure."
                elif LauraX.SeenPussy and ApprovalCheck(LauraX, 900, TabM=4):
                    ch_l "Yeah, ok."
                elif ApprovalCheck(LauraX, 1300, TabM=2) and LauraX.Panties:
                    ch_l "For you, fine. . ."
                elif ApprovalCheck(LauraX, 700) and not LauraX.Panties:
                    call Laura_NoPantiesOn
                    if not _return and not LauraX.Panties:
                        if not ApprovalCheck(LauraX, 1500):
                            call Display_DressScreen(LauraX)
                            if not _return:
                                return #jump Laura_Clothes
                        else:
                                return #jump Laura_Clothes
                else:
                    call Display_DressScreen(LauraX)
                    if not _return:
                        ch_l "Um, not with you around."
                        if not LauraX.Panties:
                                ch_l "I'm going commando today. . ."
                        return #jump Laura_Clothes

                if LauraX.Legs == "leather pants" or LauraX.Legs == "mesh pants":
                        $ LauraX.Legs = 0
                        "She tugs her pants off and drops them to the ground."
                else:
                        $ LauraX.Legs = 0
                        "She tugs her skirt off and drops it to the ground."
                if renpy.showing('DressScreen'):
                    pass
                elif LauraX.Panties:
                    $ LauraX.SeenPanties = 1
                else:
                    call Laura_First_Bottomless

        "Add leather pants" if LauraX.Legs != "leather pants":
                ch_p "You look great in those leather pants"
                ch_l "Yeah, ok."
                $ LauraX.Legs = "leather pants"

        "Add mesh pants." if LauraX.Legs != "mesh pants" and "mesh pants" in LauraX.Inventory:
                ch_p "You look great in those mesh pants."
                if ApprovalCheck(LauraX, 1000, TabM=4):
                        ch_l "Yeah, ok."
                        $ LauraX.Legs = "mesh pants"
                else:
                    call Display_DressScreen(LauraX)
                    if not _return:
                        ch_l "Sorry, those are kind of. . . breezy."
                    else:
                        $ LauraX.Legs = "mesh pants"

        "Add belty skirt" if LauraX.Legs != "skirt":
                ch_p "What about wearing your leather skirt? With the belts?"
                ch_l "Sure, why not."
                $ LauraX.Legs = "skirt"

        "Add leather skirt" if LauraX.Legs != "other skirt" and "halloween" in LauraX.History:
                ch_p "What about wearing your leather skirt?"
                ch_l "Sure, why not."
                $ LauraX.Legs = "other skirt"

        "Never mind":
                pass
    return #jump Laura_Clothes
    #End of Laura Pants

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Laura_NoPantiesOn:
        menu:
            ch_l "I'm going commando today."
            "Then you could slip on a pair of panties. . .":
                        if LauraX.SeenPussy and ApprovalCheck(LauraX, 1100, TabM=4):
                                $ LauraX.Blush = 1
                                ch_l "No, commando's fine. . ."
                                $ LauraX.Blush = 0
                        elif ApprovalCheck(LauraX, 1500, TabM=4):
                                $ LauraX.Blush = 1
                                ch_l "No, commando's fine. . ."
                                $ LauraX.Blush = 0
                        elif ApprovalCheck(LauraX, 700, TabM=4):
                                ch_l "Yeah, I guess."
                                if "lace panties" in LauraX.Inventory:
                                        ch_l "I like how you think."
                                        $ LauraX.Panties  = "lace panties"
                                else:
                                        $ LauraX.Panties = "black panties"
                                if ApprovalCheck(LauraX, 1200, TabM=4):
                                    $ Line = LauraX.Legs
                                    $ LauraX.Legs = 0
                                    "She pulls off her [Line] and slips on the [LauraX.Panties]."
                                elif LauraX.Legs == "skirt":
                                    "She pulls out her [LauraX.Panties] and pulls them up under her skirt."
                                    $ LauraX.Legs = 0
                                    "Then she drops the skirt to the floor."
                                else:
                                    $ Line = LauraX.Legs
                                    $ LauraX.Legs = 0
                                    "She steps away a moment and then comes back wearing only the [LauraX.Panties]."
                                return #jump Laura_Clothes
                        else:
                                ch_l "Nope."
                                return 0

            "You could always just wear nothing at all. . .":
                        if ApprovalCheck(LauraX, 1100, "LI", TabM=3) and LauraX.Love > LauraX.Inbt:
                                ch_l "True. . ."
                        elif ApprovalCheck(LauraX, 700, "OI", TabM=3) and LauraX.Obed > LauraX.Inbt:
                                ch_l "Yes. . ."
                        elif ApprovalCheck(LauraX, 600, "I", TabM=3):
                                ch_l "Hrmm. . ."
                        elif ApprovalCheck(LauraX, 1300, TabM=3):
                                ch_l "Fine."
                        else:
                                $ LauraX.FaceChange("surprised")
                                $ LauraX.Brows = "angry"
                                if LauraX.Taboo > 20:
                                    ch_l "Yeah, but not in public, [LauraX.Petname]!"
                                else:
                                    ch_l "You aren't that cute, [LauraX.Petname]!"
                                return 0

            "Never mind.":
                ch_l "Ok. . ."
                return 0
        return 1
        #End of Laura Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Laura_Clothes_Under:
        "Tops":
            menu:
                "How about you lose the [LauraX.Chest]?" if LauraX.Chest:
                        $ LauraX.FaceChange("bemused", 1)
                        if LauraX.SeenChest and ApprovalCheck(LauraX, 900, TabM=2.7):
                            ch_l "Ok."
                        elif ApprovalCheck(LauraX, 1100, TabM=2):
                            if LauraX.Taboo:
                                ch_l "I don't know, here. . ."
                            else:
                                ch_l "Maybe. . ."
                        elif LauraX.Over == "jacket" and ApprovalCheck(LauraX, 600, TabM=2):
                            ch_l "This jacket is a bit revealing. . ."
                        elif LauraX.Over and ApprovalCheck(LauraX, 500, TabM=2):
                            ch_l "I guess I could. . ."
                        elif not LauraX.Over:
                            call Display_DressScreen(LauraX)
                            if not _return:
                                ch_l "Not without some other top."
                                return #jump Laura_Clothes
                        else:
                            call Display_DressScreen(LauraX)
                            if not _return:
                                ch_l "Nah."
                                return #jump Laura_Clothes
                        $ Line = LauraX.Chest
                        $ LauraX.Chest = 0
                        if LauraX.Over:
                            "She reaches under her [LauraX.Over] grabs her [Line], and pulls it off, dropping it to the ground."
                        else:
                            "She pulls off her [Line] and drops it to the ground."
                            if not renpy.showing('DressScreen'):
                                call Laura_First_Topless


                "Add leather bra" if LauraX.Chest != "leather bra":
                        ch_p "Try on that leather bra."
                        ch_l "Ok."
                        $ LauraX.Chest = "leather bra"

                "Add white tanktop" if LauraX.Chest != "white tank" and "halloween" in LauraX.History:
                        ch_p "Try on that white tanktop."
                        ch_l "Ok."
                        $ LauraX.Chest = "white tank"

                "Add red corset." if LauraX.Chest != "corset" and "corset" in LauraX.Inventory:
                        ch_p "I like that red corset."
                        if LauraX.SeenChest or ApprovalCheck(LauraX, 1000, TabM=1):
                            ch_l "K."
                            $ LauraX.Chest = "corset"
                        else:
                            call Display_DressScreen(LauraX)
                            if not _return:
                                ch_l "It's a bit revealing. . ."
                            else:
                                $ LauraX.Chest = "corset"

                "Add lace corset" if LauraX.Chest != "lace corset" and "lace corset" in LauraX.Inventory:
                        ch_p "I like that lace corset."
                        if LauraX.SeenChest or ApprovalCheck(LauraX, 1300, TabM=2):
                            ch_l "K."
                            $ LauraX.Chest = "lace corset"
                        else:
                            call Display_DressScreen(LauraX)
                            if not _return:
                                ch_l "It's a bit transparent. . ."
                            else:
                                $ LauraX.Chest = "lace corset"

                "Add wolverine tanktop" if LauraX.Chest != "wolvie top" and "wolvie top" in LauraX.Inventory:
                        ch_p "I like that wolverine tanktop."
                        if LauraX.SeenChest or ApprovalCheck(LauraX, 1000, TabM=2):
                            ch_l "K."
                            $ LauraX.Chest = "wolvie top"
                        else:
                            call Display_DressScreen(LauraX)
                            if not _return:
                                ch_l "It's a {i}little{/i} embarrassing. . ."
                            else:
                                $ LauraX.Chest = "wolvie top"

                "Add bikini top" if LauraX.Chest != "bikini top" and "bikini top" in LauraX.Inventory:
                        ch_p "I like that bikini top."
                        if bg_current == "bg pool":
                                ch_l "K."
                                $ LauraX.Chest = "bikini top"
                        else:
                                if LauraX.SeenChest or ApprovalCheck(LauraX, 1000, TabM=2):
                                    ch_l "K."
                                    $ LauraX.Chest = "bikini top"
                                else:
                                    call Display_DressScreen(LauraX)
                                    if not _return:
                                            ch_l "This is not really a \"bikini\" sort of place. . ."
                                    else:
                                            $ LauraX.Chest = "bikini top"
                "Never mind":
                        pass
            return #jump Laura_Clothes_Under

        "Hose and stockings options":
            menu:
                "You could lose the hose." if LauraX.Hose and LauraX.Hose != 'ripped tights' and LauraX.Hose != 'tights':
                                $ LauraX.Hose = 0
                "The thigh-high hose would look good with that." if LauraX.Hose != "stockings":
                                $ LauraX.Hose = "stockings"
                "The black stockings would look good with that." if LauraX.Hose != "black stockings" and "halloween" in LauraX.History:
                                $ LauraX.Hose = "black stockings"
                "The stockings and garterbelt would look good with that." if LauraX.Hose != "stockings and garterbelt" and "stockings and garterbelt" in LauraX.Inventory:
                                $ LauraX.Hose = "stockings and garterbelt"
                "Just the garterbelt would look good with that." if LauraX.Hose != "garterbelt" and "stockings and garterbelt" in LauraX.Inventory:
                                $ LauraX.Hose = "garterbelt"
                "Never mind":
                        pass
            return #jump Laura_Clothes_Under

        #Panties
        "Panties":
            menu:
                "You could lose those panties. . ." if LauraX.Panties:
                        $ LauraX.FaceChange("bemused", 1)
                        if ApprovalCheck(LauraX, 900) and (LauraX.Legs or (LauraX.SeenPussy and not LauraX.Taboo)):
                                #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                                if ApprovalCheck(LauraX, 850, "L"):
                                        ch_l "True. . ."
                                elif ApprovalCheck(LauraX, 500, "O"):
                                        ch_l "Agreed."
                                elif ApprovalCheck(LauraX, 350, "I"):
                                        ch_l "Heh."
                                else:
                                        ch_l "Sure, I guess."
                        else:                       #low approval or not wearing pants or in public
                                if ApprovalCheck(LauraX, 1100, "LI", TabM=3) and LauraX.Love > LauraX.Inbt:
                                        ch_l "Well look, it's not about you, but. . ."
                                elif ApprovalCheck(LauraX, 700, "OI", TabM=3) and LauraX.Obed > LauraX.Inbt:
                                        ch_l "Well. . ."
                                elif ApprovalCheck(LauraX, 600, "I", TabM=3):
                                        ch_l "Hrmm. . ."
                                elif ApprovalCheck(LauraX, 1300, TabM=3):
                                        ch_l "Okay, okay."
                                else:
                                        call Display_DressScreen(LauraX)
                                        if not _return:
                                            $ LauraX.FaceChange("surprised")
                                            $ LauraX.Brows = "angry"
                                            if LauraX.Taboo > 20:
                                                ch_l "This is too public."
                                            else:
                                                ch_l "You're not that cute, [LauraX.Petname]!"
                                            return #jump Laura_Clothes
                        $ Line = LauraX.Panties
                        $ LauraX.Panties = 0
                        if not LauraX.Legs:
                            "She pulls off her [Line], then drops them to the ground."
                            if not renpy.showing('DressScreen'):
                                    call Laura_First_Bottomless
                        elif ApprovalCheck(LauraX, 1200, TabM=4):
                            $ Trigger = LauraX.Legs
                            $ LauraX.Legs = 0
                            pause 0.5
                            $ LauraX.Legs = Trigger
                            "She pulls off her [LauraX.Legs] and [Line], then pulls the [LauraX.Legs] back on."
                            $ Trigger = 1
                            call Laura_First_Bottomless(1)
                        elif LauraX.Legs == "skirt":
                            "She reaches under her skirt and pulls her [Line] off."
                        else:
                            $ LauraX.Blush = 1
                            "She steps away a moment and then comes back."
                            $ LauraX.Blush = 0
                        $ Line = 0

                "Why don't you wear the black panties instead?" if LauraX.Panties and LauraX.Panties != "black panties" and LauraX.Panties != "leather panties":
                        if ApprovalCheck(LauraX, 1100, TabM=3):
                                ch_l "Ok."
                                $ LauraX.Panties = "black panties"
                        else:
                                call Display_DressScreen(LauraX)
                                if not _return:
                                        ch_l "That's none of your busines."
                                else:
                                        $ LauraX.Panties = "black panties"

                "Why don't you wear the wolverine panties instead?" if "wolvie panties" in LauraX.Inventory and LauraX.Panties and LauraX.Panties != "wolvie panties":
                        if ApprovalCheck(LauraX, 1000, TabM=3):
                                ch_l "I guess."
                                $ LauraX.Panties = "wolvie panties"
                        else:
                                call Display_DressScreen(LauraX)
                                if not _return:
                                        ch_l "That's none of your busines."
                                else:
                                        $ LauraX.Panties = "wolvie panties"

                "Why don't you wear the lace panties instead?" if "lace panties" in LauraX.Inventory and LauraX.Panties and LauraX.Panties != "lace panties":
                        if ApprovalCheck(LauraX, 1300, TabM=3):
                                ch_l "I guess."
                                $ LauraX.Panties = "lace panties"
                        else:
                                call Display_DressScreen(LauraX)
                                if not _return:
                                        ch_l "That's none of your busines."
                                else:
                                        $ LauraX.Panties = "lace panties"

                "I like those bikini bottoms." if "bikini bottoms" in LauraX.Inventory and LauraX.Panties != "bikini bottoms":
                        if bg_current == "bg pool":
                                ch_l "K."
                                $ LauraX.Panties = "bikini bottoms"
                        else:
                                if ApprovalCheck(LauraX, 1000, TabM=2):
                                    ch_l "K."
                                    $ LauraX.Panties = "bikini bottoms"
                                else:
                                    call Display_DressScreen(LauraX)
                                    if not _return:
                                            ch_l "This is not really a \"bikini\" sort of place. . ."
                                    else:
                                            $ LauraX.Panties = "bikini bottoms"

                "You know, you could wear some panties with that. . ." if not LauraX.Panties:
                        $ LauraX.FaceChange("bemused", 1)
                        if LauraX.Legs and (LauraX.Love+LauraX.Obed) <= (2 * LauraX.Inbt):
                            $ LauraX.Mouth = "smile"
                            ch_l "I don't know about that."
                            menu:
                                "Fine by me":
                                    return #jump Laura_Clothes
                                "I insist, put some on.":
                                    if (LauraX.Love+LauraX.Obed) <= (1.5 * LauraX.Inbt):
                                        $ LauraX.FaceChange("angry", Eyes="side")
                                        ch_l "Well I insist otherwise."
                                        return #jump Laura_Clothes
                                    else:
                                        $ LauraX.FaceChange("sadside")
                                        ch_l "Oh, fine."
                        else:
                            ch_l "I guess. . ."
                        menu:
                            extend ""
                            "How about the black ones?":
                                    ch_l "Sure, ok."
                                    $ LauraX.Panties = "black panties"
                            "How about the wolvie ones?" if "wolvie panties" in LauraX.Inventory:
                                    ch_l "Sure."
                                    $ LauraX.Panties  = "wolvie panties"
                            "How about the lace ones?" if "lace panties" in LauraX.Inventory:
                                    ch_l "Alright."
                                    $ LauraX.Panties  = "lace panties"
                "Never mind":
                    pass
            return #jump Laura_Clothes_Under
        "Never mind":
            pass
    return #jump Laura_Clothes
    #End of Laura Underwear

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Laura_Clothes_Misc:
        #Misc
        "Dry Hair" if LauraX.Hair == "wet":
                ch_p "Maybe dry out your hair."
                if ApprovalCheck(LauraX, 600):
                    ch_l "Ok."
                    $ LauraX.Hair = "long"
                else:
                    ch_l "I don't know, it's fine like this."

        "Wet Hair style" if LauraX.Hair != "wet":
                ch_p "You should go for that wet look with your hair."
                if ApprovalCheck(LauraX, 800):
                    ch_l "Hmm?"
                    $ LauraX.Hair = "wet"
                    "She wanders off for a minute and comes back."
                    ch_l "Like this?"
                else:
                    ch_l "Ugh, too much work."

        "Grow pubes" if not LauraX.Pubes:
                ch_p "You know, I like some nice hair down there. Maybe grow it out."
                if "pubes" in LauraX.Todo:
                        $ LauraX.FaceChange("bemused", 1)
                        ch_l "Even I can't grow it out instantly."
                else:
                        $ LauraX.FaceChange("bemused", 1)
                        if ApprovalCheck(LauraX, 1000, TabM=0):
                            ch_l "Sure, that's easier. . ."
                        else:
                            $ LauraX.FaceChange("surprised")
                            $ LauraX.Brows = "angry"
                            ch_l "I think I'll do what I want down there."
                            return #jump Laura_Clothes
                        $ LauraX.Todo.append("pubes")
                        $ LauraX.PubeC = 6
        "Shave pubes" if LauraX.Pubes == 1:
                ch_p "I like it waxed clean down there."
                $ LauraX.FaceChange("bemused", 1)
                if "shave" in LauraX.Todo:
                    ch_l "Yeah, I know, I'll get to it."
                else:
                    if ApprovalCheck(LauraX, 1100, TabM=0):
                        ch_l "Really? I guess I could give it a shave. . ."
                    else:
                        $ LauraX.FaceChange("surprised")
                        $ LauraX.Brows = "angry"
                        ch_l "I think I'll do what I want down there."
                        return #jump Laura_Clothes
                    $ LauraX.Todo.append("shave")

        "Piercings. [[See what she looks like without them first] (locked)" if not LauraX.SeenPussy and not LauraX.SeenChest:
            pass

        "Add ring piercings" if LauraX.Pierce != "ring" and (LauraX.SeenPussy or LauraX.SeenChest):
                ch_p "You know, you'd look really nice with some ring body piercings."
                if "ring" in LauraX.Todo:
                    ch_l "Yeah, I know, I'll get to it."
                else:
                    $ LauraX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(LauraX, 1150, TabM=0)
                    if ApprovalCheck(LauraX, 900, "L", TabM=0) or (Approval and LauraX.Love > 2* LauraX.Obed):
                        ch_l "You think I'd look good with them?"
                    elif ApprovalCheck(LauraX, 600, "I", TabM=0) or (Approval and LauraX.Inbt > LauraX.Obed):
                        ch_l "I've been thinking about that for a while."
                    elif ApprovalCheck(LauraX, 500, "O", TabM=0) or Approval:
                        ch_l "Yes, [LauraX.Petname]."
                    else:
                        $ LauraX.FaceChange("surprised")
                        $ LauraX.Brows = "angry"
                        ch_l "Not interested, [LauraX.Petname]."
                        return #jump Laura_Clothes
                    $ LauraX.Todo.append("ring")

        "Add barbell piercings" if LauraX.Pierce != "barbell" and (LauraX.SeenPussy or LauraX.SeenChest):
                ch_p "You know, you'd look really nice with some barbell body piercings."
                if "barbell" in LauraX.Todo:
                    ch_l "Yeah, I know, I'll get to it."
                else:
                    $ LauraX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(LauraX, 1150, TabM=0)
                    if ApprovalCheck(LauraX, 900, "L", TabM=0) or (Approval and LauraX.Love > 2 * LauraX.Obed):
                        ch_l "You think I'd look good with them?"
                    elif ApprovalCheck(LauraX, 600, "I", TabM=0) or (Approval and LauraX.Inbt > LauraX.Obed):
                        ch_l "I've been thinking about that for a while."
                    elif ApprovalCheck(LauraX, 500, "O", TabM=0) or Approval:
                        ch_l "Yes, [LauraX.Petname]."
                    else:
                        $ LauraX.FaceChange("surprised")
                        $ LauraX.Brows = "angry"
                        ch_l "Not interested, [LauraX.Petname]."
                        return #jump Laura_Clothes
                    $ LauraX.Todo.append("barbell")

        "Remove piercings" if LauraX.Pierce:
                ch_p "You know, you'd look better without those piercings."
                $ LauraX.FaceChange("bemused", 1)
                $ Approval = ApprovalCheck(LauraX, 1350, TabM=0)
                if ApprovalCheck(LauraX, 950, "L", TabM=0) or (Approval and LauraX.Love > LauraX.Obed):
                    ch_l "Make up your mind . ."
                elif ApprovalCheck(LauraX, 700, "I", TabM=0) or (Approval and LauraX.Inbt > LauraX.Obed):
                    ch_l "In, out, snickt."
                elif ApprovalCheck(LauraX, 600, "O", TabM=0) or Approval:
                    ch_l "Fine."
                else:
                    $ LauraX.FaceChange("surprised")
                    $ LauraX.Brows = "angry"
                    ch_l "I've sort of grown attached."
                    return #jump Laura_Clothes
                $ LauraX.Pierce = 0

        "Medallion choker" if LauraX.Neck != "leash choker":
                ch_p "Why don't you try on that medallion choker?"
                ch_l "Ok. . ."
                $ LauraX.Neck = "leash choker"
        "Remove Necklace" if LauraX.Neck:
                ch_p "Maybe go without a necklace."
                ch_l "Ok. . ."
                $ LauraX.Neck = 0

        "Add Suspenders" if LauraX.Acc != "suspenders" and LauraX.Acc != "suspenders2" and "halloween" in LauraX.History:
                $ LauraX.Acc = "suspenders"
        "Remove Suspenders" if LauraX.Acc == "suspenders" or LauraX.Acc == "suspenders2":
                $ LauraX.Acc = 0

        "Shift Suspenders" if LauraX.Acc == "suspenders" or LauraX.Acc == "suspenders2":
                $ LauraX.Acc = "suspenders" if LauraX.Acc == "suspenders2" else "suspenders2"

        "Toggle Wristbands":
                if LauraX.Arms != "wrists":
                        ch_p "Why don't you put those wristbands on."
                else:
                        ch_p "Maybe go without the wristbands."
                ch_l "Ok. . ."
                $ LauraX.Arms = "wrists" if LauraX.Arms != "wrists" else 0
        "Toggle Gloves" if "halloween" in LauraX.History:
                if LauraX.Arms != "gloves":
                        ch_p "Why don't you put those long gloves on."
                else:
                        ch_p "Maybe go without the gloves."
                ch_l "Ok. . ."
                $ LauraX.Arms = "gloves" if LauraX.Arms != "gloves" else 0

        "Never mind":
            pass
    return #jump Laura_Clothes
    #End of Laura Misc Wardrobe

return
#End Laura Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


## Start Laura first Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#label Laura_First_Les(Silent = 0, Undress = 0, GirlsNum = 0): #checked when she engages in a les scene  ## call Laura_First_Les(0,1)
#    if LauraX.Les:
#        return

#    $ LauraX.Les += 1
#    $ LauraX.RecentActions.append("lesbian")
#    $ LauraX.Statup("Inbt", 30, 2)
#    $ LauraX.Statup("Inbt", 90, 1)

#    if not Silent:
#        #example previous line: Line + " and cups " + Primary + "'s breasts in her delicate hands"
#        "Laura's head jerks up and she looks at what [Partner] is doing. [Partner] pauses and glances up at her with a mischievous grin."
#        ch_l "I, um, I haven't done that sort of thing before."
#        if Partner == "Rogue":
#                if R_Les:
#                    ch_r "Neither have I Sugar, but it seemed like fun."
#                else:
#                    ch_r "It's all right Sugar, I'll take care of you."
#        if LauraX.LikeRogue >= 60 and ApprovalCheck(LauraX, (1500-(10*LauraX.Les)-(10*(LauraX.LikeRogue-60)))): #If she likes both of you a lot, threeway
#                $ State = "threeway"
#        elif ApprovalCheck(LauraX, 1000): #If she likes you well enough, Hetero
#                $ State = "hetero"
#        elif LauraX.LikeRogue >= 70: #if she doesn't like you but likes Rogue, lesbian
#                $ State = "lesbian"





#        if "cockout" in Player.RecentActions:
#                $ LauraX.FaceChange("down", 2)
#                if GirlsNum:
#                    "Laura also glances down at your cock"
#                else:
#                    "Laura glances down at your exposed cock"
#        elif Undress:
#                "You strip nude."
#        else:
#                "You whip your cock out."
#        $ Player.RecentActions.append("cockout")

#        if Taboo and not ApprovalCheck(LauraX, 1500):
#                $ LauraX.FaceChange("surprised", 2)
#                ch_l "Um, you should[LauraX.like]put that away in public."
#                $ LauraX.FaceChange("bemused", 1)
#                if LauraX.SeenPeen == 1:
#                    ch_l "Or[LauraX.like]maybe. . ."
#                    $ LauraX.Statup("Love", 90, 15)
#                    $ LauraX.Statup("Obed", 50, 20)
#                    $ LauraX.Statup("Inbt", 60, 35)

#        elif LauraX.SeenPeen > 10:
#                return
#        elif ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 500, "L"):
#                $ LauraX.FaceChange("sly",1)
#                if LauraX.SeenPeen == 1:
#                    $ LauraX.FaceChange("surprised",2)
#                    ch_l "That's. . . impressive."
#                    $ LauraX.FaceChange("bemused",1)
#                    $ LauraX.Statup("Love", 90, 3)
#                elif LauraX.SeenPeen == 2:
#                    ch_l "I can't get over that."
#                    $ LauraX.Statup("Obed", 50, 7)
#                elif LauraX.SeenPeen == 5:
#                    ch_l "There it is."
#                    $ LauraX.Statup("Inbt", 60, 5)
#                elif LauraX.SeenPeen == 10:
#                    ch_l "So beautiful."
#                    $ LauraX.Statup("Obed", 80, 10)
#                    $ LauraX.Statup("Inbt", 60, 3)
#        else:
#                $ LauraX.FaceChange("sad",1)
#                if LauraX.SeenPeen == 1:
#                    $ LauraX.FaceChange("perplexed",1 )
#                    ch_l "Well that happened. . ."
#                    $ LauraX.Statup("Obed", 50, 7)
#                    $ LauraX.Statup("Inbt", 60, 3)
#                elif LauraX.SeenPeen < 5:
#                    $ LauraX.FaceChange("sad",0)
#                    ch_l "Huh."
#                    $ LauraX.Statup("Inbt", 60, 2)
#                elif LauraX.SeenPeen == 10:
#                    ch_l "[LauraX.Like]put that away."
#                    $ LauraX.Statup("Obed", 50, 7)
#                    $ LauraX.Statup("Inbt", 60, 3)

#    else: #Silent mode
#                $ Player.RecentActions.append("cockout")
#                if LauraX.SeenPeen > 10:
#                    return
#                elif ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 500, "L"):
#                        if LauraX.SeenPeen == 1:
#                            $ LauraX.Statup("Love", 90, 3)
#                        elif LauraX.SeenPeen == 2:
#                            $ LauraX.Statup("Obed", 50, 7)
#                        elif LauraX.SeenPeen == 5:
#                            $ LauraX.Statup("Inbt", 60, 5)
#                        elif LauraX.SeenPeen == 10:
#                            $ LauraX.Statup("Love", 90, 10)
#                else:
#                        if LauraX.SeenPeen == 1:
#                            $ LauraX.Statup("Obed", 50, 7)
#                            $ LauraX.Statup("Inbt", 60, 3)
#                        elif LauraX.SeenPeen < 5:
#                            $ LauraX.Statup("Inbt", 60, 2)
#                        elif LauraX.SeenPeen == 10:
#                            $ LauraX.Statup("Obed", 50, 7)
#                            $ LauraX.Statup("Inbt", 60, 3)

#    if LauraX.SeenPeen == 1:
#        $ LauraX.Statup("Love", 90, 10)
#        $ LauraX.Statup("Obed", 90, 25)
#        $ LauraX.Statup("Inbt", 60, 20)
#        $ LauraX.Statup("Lust", 200, 5)

#    return
## End Laura first Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
