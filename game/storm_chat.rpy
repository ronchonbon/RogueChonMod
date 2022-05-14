# star Storm chat interface
#Storm Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

label Storm_Relationship: #rkeljs
    while True:
        menu:
            ch_s "What did you want to talk about?"
            "Do you want to be my girlfriend?" if StormX not in Player.Harem and "ex" not in StormX.Traits and "story" not in Player.History:
                    $ StormX.daily_history.append("relationship")
                    if "asked boyfriend" in StormX.daily_history and "angry" in StormX.daily_history:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "Please stop."
                            return
                    elif "asked boyfriend" in StormX.daily_history:
                            $ StormX.FaceChange("sad", 1)
                            ch_s "Oh, [Girl.Petname], no."
                            return
                    elif StormX.Break[0]:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "I. . . do not share."
                            if Player.Harem:
                                    $ StormX.daily_history.append("asked boyfriend")
                                    return
                            else:
                                    ch_s "It. . . will not work."

                    $ StormX.daily_history.append("asked boyfriend")

                    if Player.Harem and "StormYes" not in Player.Traits:
                        if len(Player.Harem) >= 2:
                            ch_s "You'd need to clear it with the others first, [StormX.Petname]."
                        else:
                            ch_s "You'd need to clear it with [Player.Harem[0].Name] first, [StormX.Petname]."
                        return

                    if StormX.Event[5]:
                            $ StormX.FaceChange("bemused", 1)
                            ch_s "When I asked, you said \"no\". . ."
                    else:
                            $ StormX.FaceChange("surprised", 2)
                            ch_s "What? . ."
                            $ StormX.FaceChange("smile", 1)

                    call Storm_OtherWoman

                    if StormX.Love >= 800:
                            $ StormX.FaceChange("surprised", 1)
                            $ StormX.Mouth = "smile"
                            $ StormX.Statup("Love", 200, 40)
                            ch_s "I would love to!"
                            if "boyfriend" not in StormX.Petnames:
                                    $ StormX.Petnames.append("boyfriend")
                            if "StormYes" in Player.Traits:
                                    $ Player.Traits.remove("StormYes")
                            $ Player.Harem.append(StormX)
                            call Harem_Initiation
                            "[StormX.Name] moves in and kisses you deeply."
                            $ StormX.FaceChange("kiss", 1)
                            $ StormX.Kissed += 1
                    elif StormX.Obed >= 500:
                            $ StormX.FaceChange("perplexed")
                            ch_s "I'm unsure, \"dating\". . ."
                    elif StormX.Inbt >= 500:
                            $ StormX.FaceChange("smile")
                            ch_s "Can't we just keep it casual?"
                    else:
                            $ StormX.FaceChange("perplexed", 1)
                            ch_s "I don't know about that, [StormX.Petname]."

            "Do you want to get back together?" if "ex" in StormX.Traits:
                    $ StormX.daily_history.append("relationship")
                    if "asked boyfriend" in StormX.daily_history and "angry" in StormX.daily_history:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "Please stop."
                            return
                    elif "asked boyfriend" in StormX.daily_history:
                            $ StormX.FaceChange("sad", 1)
                            ch_s "Oh, [Girl.Petname], no."
                            return

                    $ StormX.daily_history.append("asked boyfriend")

                    if Player.Harem and "StormYes" not in Player.Traits:
                            if len(Player.Harem) >= 2:
                                ch_s "You'd need to clear it with the others first, [StormX.Petname]."
                            else:
                                ch_s "You'd need to clear it with [Player.Harem[0].Name] first, [StormX.Petname]."
                            return

                    $ Cnt = 0
                    call Storm_OtherWoman

                    if StormX.Love >= 800:
                            $ StormX.FaceChange("surprised", 1)
                            $ StormX.Mouth = "smile"
                            $ StormX.Statup("Love", 90, 5)
                            ch_s "I suppose I could give you another chance."
                            if "boyfriend" not in StormX.Petnames:
                                    $ StormX.Petnames.append("boyfriend")
                            $ StormX.Traits.remove("ex")
                            if "StormYes" in Player.Traits:
                                    $ Player.Traits.remove("StormYes")
                            $ Player.Harem.append(StormX)
                            call Harem_Initiation
                            "[StormX.Name] pulls you in and kisses you deeply."
                            $ StormX.FaceChange("kiss", 1)
                            $ StormX.Kissed += 1
                    elif StormX.Love >= 600 and ApprovalCheck(StormX, 1500):
                            $ StormX.FaceChange("smile", 1)
                            $ StormX.Statup("Love", 90, 5)
                            ch_s "I suppose I could give it another chance."
                            if "boyfriend" not in StormX.Petnames:
                                $ StormX.Petnames.append("boyfriend")
                            $ StormX.Traits.remove("ex")
                            if "StormYes" in Player.Traits:
                                    $ Player.Traits.remove("StormYes")
                            $ Player.Harem.append(StormX)
                            call Harem_Initiation
                            $ StormX.FaceChange("kiss", 1)
                            "[StormX.Name] gives you a quick kiss."
                            $ StormX.FaceChange("sly", 1)
                            $ StormX.Kissed += 1
                    elif StormX.Obed >= 500:
                            $ StormX.FaceChange("sad")
                            ch_s "Perhaps \"relationships\" are beyond us."
                    elif StormX.Inbt >= 500:
                            $ StormX.FaceChange("perplexed")
                            ch_s "Let's keep things casual."
                    else:
                            $ StormX.FaceChange("perplexed", 1)
                            ch_s "You've lost my trust."

                    # End Back Together

            "I wanted to ask about [[another girl]" if StormX in Player.Harem:
                            call AskDateOther

            "I think we should break up." if StormX in Player.Harem:
                            if "breakup talk" in StormX.RecentActions:
                                    ch_s "Why do you torment me?"
                            elif "breakup talk" in StormX.daily_history:
                                    ch_s "Not today, [StormX.Petname]."
                            else:
                                    call Breakup(StormX)

            "About that talk we had before. . .":
                menu:
                    "When you said you wanted to tell me a story. . ." if "story" in Player.History and StormX.Event[5] == 20:
                            $ Player.History.remove("story")
                            ch_s "Ah, yes, I did have a story to tell you. . ."
                            call Storm_BF_Story
                    "I feel you were trying to tell me something before. . ." if "lover" not in StormX.Traits and StormX.Event[6] >= 5:
                            if ApprovalCheck(StormX, 900, "L"):
                                    $ StormX.Event[6] = 3
                                    ch_s "Yes, I supposed that I did. . ."
                                    $ StormX.daily_history.append("relationship")
                                    call Storm_Love_Redux
                            else:
                                    ch_s "I do not think you understand yet. . ."


                    "You said you wanted me to be more assertive?" if "sir" not in StormX.Petnames and "sir" in StormX.History:
                            if "asked sub" in StormX.RecentActions:
                                    ch_s "That was only moments ago."
                            elif "asked sub" in StormX.daily_history:
                                    ch_s "We discussed this earlier. . ."
                            else:
                                    call Storm_Sub_Asked
                    "You said you wanted me to be your Master?" if "master" not in StormX.Petnames and "master" in StormX.History:
                            if "asked sub" in StormX.RecentActions:
                                    ch_s "That was only moments ago."
                            elif "asked sub" in StormX.daily_history:
                                    ch_s "We discussed this earlier. . ."
                            else:
                                    call Storm_Sub_Asked
                    "Never mind":
                            pass

            "Never Mind":
                return

    return

label Storm_OtherWoman(Cnt = 0): #rkeljs
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return
    $ Cnt = int((StormX.GirlLikeCheck(Player.Harem[0]) - 500)/2)

    $ StormX.FaceChange("perplexed")
    if len(Player.Harem) >= 2:
        ch_s "But you are with [Player.Harem[0].Name] right now, and others as well."
    else:
        ch_s "But you are with [Player.Harem[0].Name], are you not?"
    menu:
        extend ""
        "She said I can be with you too." if "StormYes" in Player.Traits:
                if ApprovalCheck(StormX, 1800, Bonus = Cnt):
                    $ StormX.FaceChange("smile", 1)
                    if StormX.Love >= StormX.Obed:
                            ch_s "I suppose I can share with her."
                    elif StormX.Obed >= StormX.Inbt:
                            ch_s "If that's what you want."
                    else:
                            ch_s "Fine."
                else:
                    $ StormX.FaceChange("angry", 1)
                    ch_s "Yes, I suppose that she would, but I'm unwilling to share."
                    $ renpy.pop_call()
                    #This causes it to jump past the previous menu on the return

        "I could ask if she'd be ok with me dating you both." if "StormYes" not in Player.Traits:
                if ApprovalCheck(StormX, 1800, Bonus = Cnt):
                        $ StormX.FaceChange("smile", 1)
                        if StormX.Love >= StormX.Obed:
                            ch_s "I guess I can share you."
                        elif StormX.Obed >= StormX.Inbt:
                            ch_s "If that's what you want."
                        else:
                            ch_s "Fine."
                        ch_s "Well ask her and tell me in the morning."
                else:
                        $ StormX.FaceChange("angry", 1)
                        ch_s "Yeah, I imagine she would, but I'm not sharing."
                $ renpy.pop_call()

        "What she doesn't know won't hurt her.":
                if not ApprovalCheck(StormX, 1800, Bonus = -Cnt): #checks if Storm likes you more than the other girl
                        $ StormX.FaceChange("angry", 1)
                        if not ApprovalCheck(StormX, 1800):
                                ch_s "It would hurt us both."
                        else:
                                ch_s "That sounds beneath you."
                        $ renpy.pop_call()
                else:
                        $ StormX.FaceChange("smile", 1)
                        if StormX.Love >= StormX.Obed:
                                ch_s "I suppose I could get past it. . ."
                        elif StormX.Obed >= StormX.Inbt:
                                ch_s "If that's what you want."
                        else:
                                ch_s "Fine."
                        $ StormX.Traits.append("downlow")

        "I can break it off with her.":
                    $ StormX.FaceChange("sad")
                    ch_s "Then after you do, we can discuss this again."
                    $ renpy.pop_call()

        "You're right, I was dumb to ask.":
                    $ StormX.FaceChange("sad")
                    ch_s "Very."
                    $ renpy.pop_call()

    return


label Storm_About(Check=0): #rkeljsv
    if Check not in TotalGirls:
            ch_s "Who?"
            return
    ch_s "What do I think about her? Well. . ."
    if Check == RogueX:
            if "poly Rogue" in StormX.Traits:
                ch_s "We have enjoyed each other's company. . ."
            elif StormX.LikeRogue >= 900:
                ch_s "She does have a fine figure . ."
            elif StormX.LikeRogue >= 800:
                ch_s "She is a lovely person. . ."
            elif StormX.LikeRogue >= 700:
                ch_s "She is quite a hard worker."
            elif StormX.LikeRogue >= 600:
                ch_s "She is nice."
            elif StormX.LikeRogue >= 500:
                ch_s "I have seen her around."
            elif StormX.LikeRogue >= 400:
                ch_s "I would rather not talk about it."
            elif StormX.LikeRogue >= 300:
                ch_s "I hate her."
            else:
                ch_s "Bitch."
    elif Check == KittyX:
            if "poly Kitty" in StormX.Traits:
                ch_s "We have enjoyed each other's company. . ."
            elif StormX.LikeKitty >= 900:
                ch_s "She does have a petite figure . ."
            elif StormX.LikeKitty >= 800:
                ch_s "She is a lovely person. . ."
            elif StormX.LikeKitty >= 700:
                ch_s "She is attentive in class."
            elif StormX.LikeKitty >= 600:
                ch_s "She is a hard worker."
            elif StormX.LikeKitty >= 500:
                ch_s "She is in our classes, correct?"
            elif StormX.LikeKitty >= 400:
                ch_s "I would rather not talk about it."
            elif StormX.LikeKitty >= 300:
                ch_s "I stongly dislike her."
            else:
                ch_s "Bitch."
    elif Check == EmmaX:
            if "poly Emma" in StormX.Traits:
                ch_s "We have enjoyed each other's company. . ."
            elif StormX.LikeEmma >= 900:
                ch_s "She does have a volumptuous figure . ."
            elif StormX.LikeEmma >= 800:
                ch_s "I have grown to enjoy her company. . ."
            elif StormX.LikeEmma >= 700:
                ch_s "She is an excellent educator."
            elif StormX.LikeEmma >= 600:
                ch_s "I don't mind sharing classes with her."
            elif StormX.LikeEmma >= 500:
                ch_s "She's fine."
            elif StormX.LikeEmma >= 400:
                ch_s "I could do with less of her attitude."
            elif StormX.LikeEmma >= 300:
                ch_s "She needs to stay out of my head."
            else:
                ch_s "Bitch."
    if Check == LauraX:
            if "poly Laura" in StormX.Traits:
                ch_s "We have enjoyed each other's company. . ."
            elif StormX.LikeLaura >= 900:
                ch_s "She does have a fine figure . ."
            elif StormX.LikeLaura >= 800:
                ch_s "She is a lovely person. . . eventually."
            elif StormX.LikeLaura >= 700:
                ch_s "She is quite a strong warrior."
            elif StormX.LikeLaura >= 600:
                ch_s "She is aggressive."
            elif StormX.LikeLaura >= 500:
                ch_s "I have seen her around."
            elif StormX.LikeLaura >= 400:
                ch_s "I would rather not talk about it."
            elif StormX.LikeLaura >= 300:
                ch_s "I hate her."
            else:
                ch_s "Bitch."
    elif Check == JeanX:
            if "poly Jean" in StormX.Traits:
                ch_s "We have enjoyed each other's company. . ."
            elif StormX.LikeJean >= 900:
                ch_s "She does have a fine figure . ."
            elif StormX.LikeJean >= 800:
                ch_s "She is an acquired taste. . ."
            elif StormX.LikeJean >= 700:
                ch_s "She. . . does try."
            elif StormX.LikeJean >= 600:
                ch_s "I've become accustomed to her."
            elif StormX.LikeJean >= 500:
                ch_s "She can be difficult."
            elif StormX.LikeJean >= 400:
                ch_s "She is a chore."
            elif StormX.LikeJean >= 300:
                ch_s "I seriously dislike her."
            else:
                ch_s "Bitch."
    elif Check == JubesX:
            if "poly Jubes" in StormX.Traits:
                ch_s "We have enjoyed each other's company. . ."
            elif StormX.LikeJubes >= 900:
                ch_s "She does have a wonderful figure . ."
            elif StormX.LikeJubes >= 800:
                ch_s "She is a lovely person. . ."
            elif StormX.LikeJubes >= 700:
                ch_s "She is attentive in class."
            elif StormX.LikeJubes >= 600:
                ch_s "She is a hard worker."
            elif StormX.LikeJubes >= 500:
                ch_s "She is in our classes, correct?"
            elif StormX.LikeJubes >= 400:
                ch_s "She is a bit of a biter."
            elif StormX.LikeJubes >= 300:
                ch_s "I stongly dislike her."
            else:
                ch_s "Bitch."
    return
#End Storm_AboutEmma

label Storm_Monogamy: #rkeljs
        #called from Storm_Settings to ask her not to hook up with other girls
        menu:
            "Could you not hook up with other girls?" if "mono" not in StormX.Traits:
                    if StormX.Thirst >= 60 and not ApprovalCheck(StormX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ StormX.FaceChange("sly",1)
                            if "mono" not in StormX.daily_history:
                                    $ StormX.Statup("Obed", 90, -2)
                            ch_s "I do have needs that must be met. . ."
                            return
                    elif ApprovalCheck(StormX, 1200, "LO", TabM=0) and StormX.Love >= StormX.Obed:
                            #she cares
                            $ StormX.FaceChange("sly",1)
                            if "mono" not in StormX.daily_history:
                                    $ StormX.Statup("Love", 90, 1)
                            ch_s "I did not take you for the jealous type."
                            ch_s "Very well, for now. . ."
                    elif ApprovalCheck(StormX, 700, "O", TabM=0):
                            #she is obedient
                            $ StormX.FaceChange("sly",1,Eyes="side")
                            ch_s "Fine."
                    else:
                            #she doesn't care
                            $ StormX.FaceChange("sly",1)
                            ch_s "I do have needs. No."
                            return
                    if "mono" not in StormX.daily_history:
                            $ StormX.Statup("Obed", 90, 3)
                    $ StormX.AddWord(1,0,"mono") #Daily
                    $ StormX.Traits.append("mono")
            "Don't hook up with other girls." if "mono" not in StormX.Traits:
                    if ApprovalCheck(StormX, 900, "O", TabM=0):
                            #she is obedient
                            $ StormX.FaceChange("sly",1,Eyes="side")
                            ch_s "If that is what you want."
                    elif StormX.Thirst >= 60 and not ApprovalCheck(StormX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ StormX.FaceChange("sly",1)
                            if "mono" not in StormX.daily_history:
                                    $ StormX.Statup("Obed", 90, -2)
                            ch_s "I do have needs that must be met. . ."
                            return
                    elif ApprovalCheck(StormX, 600, "O", TabM=0):
                            #she is obedient
                            $ StormX.FaceChange("sly",1,Eyes="side")
                            ch_s "Fine."
                    elif ApprovalCheck(StormX, 1400, "LO", TabM=0):
                            #she cares
                            $ StormX.FaceChange("sly",1)
                            ch_s "Take care with your words, but I will consider it."
                    else:
                            #she doesn't care
                            $ StormX.FaceChange("sly",1,Brows="confused")
                            ch_s "I would watch your tone."
                            return
                    if "mono" not in StormX.daily_history:
                            $ StormX.Statup("Obed", 90, 3)
                    $ StormX.AddWord(1,0,"mono") #Daily
                    $ StormX.Traits.append("mono")
            "It's ok if you hook up with other girls." if "mono" in StormX.Traits:
                    if ApprovalCheck(StormX, 700, "O", TabM=0):
                            $ StormX.FaceChange("sly",1,Eyes="side")
                            ch_s ". . . ok then."
                    elif ApprovalCheck(StormX, 800, "L", TabM=0):
                            $ StormX.FaceChange("sly",1)
                            ch_s "Fine. . ."
                    else:
                            $ StormX.FaceChange("sly",1,Brows="confused")
                            if "mono" not in StormX.daily_history:
                                    $ StormX.Statup("Love", 90, -2)
                            ch_s "It sounds like I have some weekend plans to make then."
                    if "mono" not in StormX.daily_history:
                            $ StormX.Statup("Obed", 90, 3)
                    if "mono" in StormX.Traits:
                            $ StormX.Traits.remove("mono")
                    $ StormX.AddWord(1,0,"mono") #Daily
            "Never mind.":
                pass
        return

# end Storm monogamy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Storm_Jumped: #rkeljs
        #called from Storm_Settings to ask her not to jump you
        ch_p "Hey, Remember that time you threw yourself at me?"
        $ StormX.FaceChange("sly",1,Brows="confused")
        menu:
            ch_s "Yeah?"
            "Could you maybe just ask instead?" if "chill" not in StormX.Traits:
                    if StormX.Thirst >= 60 and not ApprovalCheck(StormX, 1500, "LO", TabM=0):
                            #she's too thirsty
                            $ StormX.FaceChange("sly",1)
                            if "chill" not in StormX.daily_history:
                                    $ StormX.Statup("Obed", 90, -2)
                            ch_s "I would if you would come to me more often. . ."
                            return
                    elif ApprovalCheck(StormX, 1000, "LO", TabM=0) and StormX.Love >= StormX.Obed:
                            #she cares
                            $ StormX.FaceChange("surprised",1)
                            if "chill" not in StormX.daily_history:
                                    $ StormX.Statup("Love", 90, 1)
                            ch_s "I am sorry, but I have needs. . ."
                            $ StormX.FaceChange("sly",1,Eyes="side")
                            ch_s "I will -try- to keep them in check. . ."
                    elif ApprovalCheck(StormX, 500, "O", TabM=0):
                            #she is obedient
                            $ StormX.FaceChange("sly",1,Eyes="side")
                            ch_s "I am sorry about that. . ."
                    else:
                            #she doesn't care
                            $ StormX.FaceChange("sly",1)
                            ch_s "I will take what I need."
                            return
                    if "chill" not in StormX.daily_history:
                            $ StormX.Statup("Obed", 90, 3)
                    $ StormX.AddWord(1,0,"chill") #Daily
                    $ StormX.Traits.append("chill")
            "Don't bother me like that." if "chill" not in StormX.Traits:
                    if ApprovalCheck(StormX, 800, "O", TabM=0):
                            #she is obedient
                            $ StormX.FaceChange("sly",1,Eyes="side")
                            ch_s "Very well."
                    elif StormX.Thirst >= 60 and not ApprovalCheck(StormX, 500, "O", TabM=0):
                            #she's too thirsty
                            $ StormX.FaceChange("sly",1)
                            if "chill" not in StormX.daily_history:
                                    $ StormX.Statup("Obed", 90, -2)
                            ch_s "I would if you would come to me more often. . ."
                            return
                    elif ApprovalCheck(StormX, 400, "O", TabM=0):
                            #she is obedient
                            $ StormX.FaceChange("sly",1,Eyes="side")
                            ch_s "Fine. . ."
                    elif ApprovalCheck(StormX, 500, "LO", TabM=0) and not ApprovalCheck(StormX, 500, "I", TabM=0):
                            #she cares
                            $ StormX.FaceChange("sly",1)
                            ch_s "Watch your language."
                            ch_s "I will -try- to keep my needs in check. . ."
                    else:
                            #she doesn't care
                            $ StormX.FaceChange("sly",1)
                            ch_s "I will take what I need."
                            return
                    if "chill" not in StormX.daily_history:
                            $ StormX.Statup("Obed", 90, 3)
                    $ StormX.AddWord(1,0,"chill") #Daily
                    $ StormX.Traits.append("chill")
            "Knock yourself out.":
                    if ApprovalCheck(StormX, 800, "L", TabM=0):
                            $ StormX.FaceChange("sly",1)
                            ch_s "Noted. . ."
                    elif ApprovalCheck(StormX, 700, "O", TabM=0):
                            $ StormX.FaceChange("sly",1,Eyes="side")
                            ch_s "Very well. . .."
                    else:
                            $ StormX.FaceChange("sly",1,Brows="confused")
                            if "chill" not in StormX.daily_history:
                                    $ StormX.Statup("Love", 90, -2)
                            ch_s "If I find myself in need, certainly."
                    if "chill" not in StormX.daily_history:
                            $ StormX.Statup("Obed", 90, 3)
                    if "chill" in StormX.Traits:
                            $ StormX.Traits.remove("chill")
                    $ StormX.AddWord(1,0,"chill") #Daily
            "Um, never mind.":
                pass
        return

# end Storm jumped <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# start laura hungry //////////////////////////////////////////////////////////
label Storm_Hungry:#rkeljs
    if StormX.Chat[3]:
        ch_s "[[licks her lips] could use another taste. . ."
    elif StormX.Chat[2]:
        ch_s "I have really acquired a taste for that serum of yours."
    else:
        ch_s "[[licks her lips] I really love your taste. . ."
    $ StormX.Traits.append("hungry")
return


# end laura hungry //////////////////////////////////////////////////////////

# Storm Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Storm_SexChat:#rkeljs
    $ Line = "Yes? What did you want to discuss?" if not Line else Line
    while True:
            menu:
                ch_s "[Line]"
                "My favorite thing to do is. . .":
                    if "setfav" in StormX.daily_history:
                        ch_s "We've been over this."
                    else:
                        menu:
                            "Sex.":
                                        $ StormX.FaceChange("sly")
                                        if StormX.PlayerFav == "sex":
                                            $ StormX.Statup("Lust", 80, 5)
                                            ch_s "Yes, so you've said."
                                        elif StormX.Favorite == "sex":
                                            $ StormX.Statup("Love", 90, 5)
                                            $ StormX.Statup("Lust", 80, 10)
                                            ch_s "I also enjoy that. . ."
                                        elif StormX.Sex >= 5:
                                            ch_s "It certainly is enjoyable. . ."
                                        elif not StormX.Sex:
                                            $ StormX.FaceChange("perplexed")
                                            ch_s "And who is fucking you?"
                                        else:
                                            $ StormX.FaceChange("bemused")
                                            ch_s "Yes. . . um. . . it is fine. . ."
                                        $ StormX.PlayerFav = "sex"

                            "Anal.":
                                        $ StormX.FaceChange("sly")
                                        if StormX.PlayerFav == "anal":
                                            $ StormX.Statup("Lust", 80, 5)
                                            ch_s "Yes, so you've said."
                                        elif StormX.Favorite == "anal":
                                            $ StormX.Statup("Love", 90, 5)
                                            $ StormX.Statup("Lust", 80, 10)
                                            ch_s "I also enjoy that. . ."
                                        elif StormX.Anal >= 10:
                                            ch_s "It certainly is enjoyable. . ."
                                        elif not StormX.Anal:
                                            $ StormX.FaceChange("perplexed")
                                            ch_s "And who is fucking you?"
                                        else:
                                            $ StormX.FaceChange("bemused",Eyes="side")
                                            ch_s "Yes. . . um. . . it is fine. . ."
                                        $ StormX.PlayerFav = "anal"

                            "Blowjobs.":
                                        $ StormX.FaceChange("sly")
                                        if StormX.PlayerFav == "blow":
                                            $ StormX.Statup("Lust", 80, 3)
                                            ch_s "Yes, so you've said."
                                        elif StormX.Favorite == "blow":
                                            $ StormX.Statup("Love", 90, 5)
                                            $ StormX.Statup("Lust", 80, 5)
                                            ch_s "I would have to agree. . ."
                                        elif StormX.Blow >= 10:
                                            ch_s "You are quite delicious. . ."
                                        elif not StormX.Blow:
                                            $ StormX.FaceChange("perplexed")
                                            ch_s "Who's sucking your dick?!"
                                        else:
                                            $ StormX.FaceChange("bemused")
                                            ch_s "I'm. . . getting used to the taste. . ."
                                        $ StormX.PlayerFav = "blow"

                            "Titjobs.":
                                        $ StormX.FaceChange("sly")
                                        if StormX.PlayerFav == "titjob":
                                            $ StormX.Statup("Lust", 80, 5)
                                            ch_s "Yes, so you've said."
                                        elif StormX.Favorite == "titjob":
                                            $ StormX.Statup("Love", 90, 5)
                                            $ StormX.Statup("Lust", 80, 7)
                                            ch_s "I also enjoy that. . ."
                                        elif StormX.Tit >= 10:
                                            ch_s "It certainly is enjoyable. . ."
                                        elif not StormX.Tit:
                                            $ StormX.FaceChange("perplexed")
                                            ch_s "And who is titfucking you?"
                                        else:
                                            $ StormX.FaceChange("bemused")
                                            ch_s "Yes. . . um. . . it is fine. . ."
                                            $ StormX.Statup("Love", 80, 5)
                                            $ StormX.Statup("Inbt", 50, 10)
                                        $ StormX.PlayerFav = "titjob"

                            "Footjobs.":
                                        $ StormX.FaceChange("sly")
                                        if StormX.PlayerFav == "foot":
                                            $ StormX.Statup("Lust", 80, 5)
                                            ch_s "Yes, so you've said."
                                        elif StormX.Favorite == "foot":
                                            $ StormX.Statup("Love", 90, 5)
                                            $ StormX.Statup("Lust", 80, 7)
                                            ch_s "I also enjoy that. . ."
                                        elif StormX.Foot >= 10:
                                            ch_s "I like it too . . ."
                                        elif not StormX.Foot:
                                            $ StormX.FaceChange("perplexed")
                                            ch_s "And who is playing footsie with you?"
                                        else:
                                            $ StormX.FaceChange("bemused")
                                            ch_s "Yes. . . um. . . it is fine. . ."
                                        $ StormX.PlayerFav = "foot"

                            "Handjobs.":
                                        $ StormX.FaceChange("sly")
                                        if StormX.PlayerFav == "hand":
                                            $ StormX.Statup("Lust", 80, 5)
                                            ch_s "Yes, so you've said."
                                        elif StormX.Favorite == "hand":
                                            $ StormX.Statup("Love", 90, 5)
                                            $ StormX.Statup("Lust", 80, 7)
                                            ch_s "I also enjoy that. . ."
                                        elif StormX.Hand >= 10:
                                            ch_s "I like it too . . ."
                                        elif not StormX.Hand:
                                            $ StormX.FaceChange("perplexed")
                                            ch_s "And who is jerking you off?"
                                        else:
                                            $ StormX.FaceChange("bemused")
                                            ch_s "Yes. . . um. . . it is fine. . ."
                                        $ StormX.PlayerFav = "hand"

                            "Feeling you up.":
                                        $ Cnt = StormX.FondleB + StormX.FondleT + StormX.SuckB + StormX.Hotdog
                                        $ StormX.FaceChange("sly")
                                        if StormX.PlayerFav == "fondle":
                                            $ StormX.Statup("Lust", 80, 3)
                                            ch_s "Yes, so you've said."
                                        elif StormX.Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            $ StormX.Statup("Love", 90, 5)
                                            $ StormX.Statup("Lust", 80, 5)
                                            ch_s "I do not mind that myself. . ."
                                        elif Cnt >= 10:
                                            ch_s "It certainly is enjoyable. . ."
                                        elif not Cnt:
                                            $ StormX.FaceChange("perplexed")
                                            ch_s "And who is letting you feel her up?"
                                        else:
                                            $ StormX.FaceChange("bemused")
                                            ch_s "I do enjoy how that feels. . ."
                                        $ StormX.PlayerFav = "fondle"
                                        $ Cnt = 0

                            "Kissing you.":
                                        $ StormX.FaceChange("sly")
                                        if StormX.PlayerFav == "kiss you":
                                            $ StormX.Statup("Love", 90, 3)
                                            ch_s "Yes, so you've said."
                                        elif StormX.Favorite == "kiss you":
                                            $ StormX.Statup("Love", 90, 5)
                                            $ StormX.Statup("Lust", 80, 5)
                                            ch_s "I also enjoy that. . ."
                                        elif StormX.Kissed >= 10:
                                            ch_s "It certainly is enjoyable. . ."
                                        elif not StormX.Kissed:
                                            $ StormX.FaceChange("perplexed")
                                            ch_s "And who are you kissing?"
                                        else:
                                            $ StormX.FaceChange("bemused")
                                            ch_s "I enjoy kissing you as well. . ."
                                        $ StormX.PlayerFav = "kiss you"

                        $ StormX.daily_history.append("setfav")

                "What's your favorite thing to do?":
                                if not ApprovalCheck(StormX, 800):
                                        $ StormX.FaceChange("perplexed")
                                        ch_s ". . . I would rather not say."
                                else:
                                        if StormX.SEXP >= 50:
                                            $ StormX.FaceChange("sly")
                                            ch_s "You should be aware. . ."
                                        else:
                                            $ StormX.FaceChange("bemused")
                                            $ StormX.Eyes = "side"
                                            ch_s "Well. . ."


                                        if not StormX.Favorite or StormX.Favorite == "kiss":
                                                ch_s "Kissing?"
                                        elif StormX.Favorite == "anal":
                                                ch_s "Probably anal."
                                        elif StormX.Favorite == "lick ass":
                                                ch_s "When you lick my ass."
                                        elif StormX.Favorite == "insert ass":
                                                ch_s "Fingering my asshole, probably."
                                        elif StormX.Favorite == "sex":
                                                ch_s "I enjoy sex the most."
                                        elif StormX.Favorite == "lick pussy":
                                                ch_s "When you lick my pussy."
                                        elif StormX.Favorite == "fondle pussy":
                                                ch_s "When you finger me."
                                        elif StormX.Favorite == "blow":
                                                ch_s "I enjoy the taste of your cock."
                                        elif StormX.Favorite == "tit":
                                                ch_s "When I use my breasts."
                                        elif StormX.Favorite == "foot":
                                                ch_s "Footjobs are quite fun."
                                        elif StormX.Favorite == "hand":
                                                ch_s "I enjoy jerking you off."
                                        elif StormX.Favorite == "hotdog":
                                                ch_s "When you grind against me."
                                        elif StormX.Favorite == "suck breasts":
                                                ch_s "When you suck my breasts."
                                        elif StormX.Favorite == "fondle breasts":
                                                ch_s "When you grab my breasts."
                                        elif StormX.Favorite == "fondle thighs":
                                                ch_s "When you rub my thighs."
                                        else:
                                                ch_s "I'm unsure, actually."

                                # End Storm's favorite things.

                "Don't talk as much during sex." if "vocal" in StormX.Traits:
                        if "setvocal" in StormX.daily_history:
                                $ StormX.FaceChange("perplexed")
                                ch_s "I do wish you would make up your mind."
                        else:
                            if ApprovalCheck(StormX, 1000) and StormX.Obed <= StormX.Love:
                                $ StormX.FaceChange("bemused")
                                $ StormX.Statup("Obed", 90, 1)
                                ch_s "I can be silent if you wish."
                                $ StormX.Traits.remove("vocal")
                            elif ApprovalCheck(StormX, 700, "O"):
                                $ StormX.FaceChange("sadside")
                                $ StormX.Statup("Obed", 90, 1)
                                ch_s ". . ."
                                $ StormX.Traits.remove("vocal")
                            elif ApprovalCheck(StormX, 600):
                                $ StormX.FaceChange("sly")
                                $ StormX.Statup("Love", 90, -3)
                                $ StormX.Statup("Obed", 50, -1)
                                $ StormX.Statup("Inbt", 90, 5)
                                ch_s "Do not presume to control me, [StormX.Petname]."
                            else:
                                $ StormX.FaceChange("angry")
                                $ StormX.Statup("Love", 90, -5)
                                $ StormX.Statup("Obed", 60, -3)
                                $ StormX.Statup("Inbt", 90, 10)
                                ch_s "I do not take orders from you, [StormX.Petname]."

                            $ StormX.daily_history.append("setvocal")
                "Talk dirty to me during sex." if "vocal" not in StormX.Traits:
                        if "setvocal" in StormX.daily_history:
                                $ StormX.FaceChange("perplexed")
                                ch_s "I do wish you would make up your mind."
                        else:
                            if ApprovalCheck(StormX, 1000) and StormX.Obed <= StormX.Love:
                                $ StormX.FaceChange("sly")
                                $ StormX.Statup("Obed", 90, 2)
                                ch_s "I believe I can make myself known. . ."
                                $ StormX.Traits.append("vocal")
                            elif ApprovalCheck(StormX, 700, "O"):
                                $ StormX.FaceChange("sadside")
                                $ StormX.Statup("Obed", 90, 2)
                                ch_s "If that is what you want, [StormX.Petname]."
                                $ StormX.Traits.append("vocal")
                            elif ApprovalCheck(StormX, 600):
                                $ StormX.FaceChange("sly")
                                $ StormX.Statup("Obed", 90, 3)
                                ch_s "I suppose that I could. . ."
                                $ StormX.Traits.append("vocal")
                            else:
                                $ StormX.FaceChange("angry")
                                $ StormX.Statup("Inbt", 90, 5)
                                ch_s ". . . I would rather not."

                            $ StormX.daily_history.append("setvocal")
                        # End Storm Dirty Talk

                "Don't do your own thing as much during sex." if "passive" not in StormX.Traits:
                        if "initiative" in StormX.daily_history:
                                $ StormX.FaceChange("perplexed")
                                ch_s "I do wish you would make up your mind."
                        else:
                            if ApprovalCheck(StormX, 1200) and StormX.Obed <= StormX.Love:
                                $ StormX.FaceChange("bemused")
                                $ StormX.Statup("Obed", 90, 1)
                                ch_s "Allow you to take the lead? Fine."
                                $ StormX.Traits.append("passive")
                            elif ApprovalCheck(StormX, 700, "O"):
                                $ StormX.FaceChange("sadside")
                                $ StormX.Statup("Obed", 90, 1)
                                ch_s "I will try to restrain myself."
                                $ StormX.Traits.append("passive")
                            elif ApprovalCheck(StormX, 600):
                                $ StormX.FaceChange("sly")
                                $ StormX.Statup("Love", 90, -3)
                                $ StormX.Statup("Obed", 50, -1)
                                $ StormX.Statup("Inbt", 90, 5)
                                ch_s "We shall see."
                            else:
                                $ StormX.FaceChange("angry")
                                $ StormX.Statup("Love", 90, -5)
                                $ StormX.Statup("Obed", 60, -3)
                                $ StormX.Statup("Inbt", 90, 10)
                                ch_s "I don't think that I shall."

                            $ StormX.daily_history.append("initiative")
                "Take more initiative during sex." if "passive" in StormX.Traits:
                        if "initiative" in StormX.daily_history:
                                $ StormX.FaceChange("perplexed")
                                ch_s "I do wish you would make up your mind."
                        else:
                            if ApprovalCheck(StormX, 1000) and StormX.Obed <= StormX.Love:
                                $ StormX.FaceChange("bemused")
                                $ StormX.Statup("Obed", 90, 1)
                                ch_s "You would prefer I choose? Very Well."
                                $ StormX.Traits.remove("passive")
                            elif ApprovalCheck(StormX, 700, "O"):
                                $ StormX.FaceChange("sadside")
                                $ StormX.Statup("Obed", 90, 1)
                                ch_s "If you insist."
                                $ StormX.Traits.remove("passive")
                            elif ApprovalCheck(StormX, 600):
                                $ StormX.FaceChange("sly")
                                $ StormX.Statup("Obed", 90, 3)
                                ch_s "We shall see."
                                $ StormX.Traits.remove("passive")
                            else:
                                $ StormX.FaceChange("angry")
                                $ StormX.Statup("Inbt", 90, 5)
                                ch_s "I would rather not."

                            $ StormX.daily_history.append("initiative")

                "About getting Jumped" if "jumped" in StormX.History:
                            call Storm_Jumped
                "About when you masturbate":
                            call NoFap(StormX)

                "Never Mind" if Line == "Yes? What did you want to discuss?":
                        return
                "That's all." if Line != "Yes? What did you want to discuss?":
                        return
            if Line == "Yes? What did you want to discuss?":
                $ Line = "Anything else?"
    return
# End Storm Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


## Storm Chitchat /////////////////// #Work in progress
label Storm_Chitchat(O=0, Options = ["default","default","default"]): #rkeljs
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:

        if StormX not in Digits:
                if ApprovalCheck(StormX, 500, "L") or ApprovalCheck(StormX, 250, "I"):
                    ch_s "Oh, here's my number, in case you need back-up."
                    $ Digits.append(StormX)
                    return
                elif ApprovalCheck(StormX, 250, "O"):
                    ch_s "If you need to contact me, here's my number."
                    $ Digits.append(StormX)
                    return

        if "hungry" not in StormX.Traits and (StormX.Swallow + StormX.Chat[2]) >= 10 and StormX.Loc == bg_current:  #She's swallowed a lot
                    call Storm_Hungry
                    return

        if bg_current != "bg restaurant" and bg_current != "HW Party" and (not Taboo or ApprovalCheck(StormX, 800, "I")):
                    if StormX.Loc == bg_current and StormX.Thirst >= 30 and "refused" not in StormX.daily_history and "quicksex" not in StormX.daily_history:
                            $ StormX.FaceChange("sly",1)
                            ch_s "I was wondering if you wanted to. . ."
                            ch_s "\"get intimate\" with me?"
                            call Quick_Sex(StormX)
                            return
#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
#        if PunishmentX and "caught chat" not in StormX.daily_history:
#            $ Options.append("caught")
        if StormX.Event[0] and "key" not in StormX.Chat:
            $ Options.append("key")

        if "mandrill" in Player.Traits and "cologne chat" not in StormX.daily_history:
            $ Options.append("mandrill")
        if "purple" in Player.Traits and "cologne chat" not in StormX.daily_history:
            $ Options.append("purple")
        if "corruption" in Player.Traits and "cologne chat" not in StormX.daily_history:
            $ Options.append("corruption")

        if StormX.Date >= 1 and bg_current != "bg restaurant" :
            #if you've dated before
            $ Options.append("dated")
#        if "cheek" in StormX.daily_history and "cheek" not in StormX.Chat:
#            #If you've touched her cheek today
#            $ Options.append("cheek")
        if StormX.Kissed >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")
        if "dangerroom" in Player.daily_history:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
#        if "showered" in StormX.daily_history:
#            #If you've caught Storm showering today
            $ Options.append("showercaught")
        if "fondle breasts" in StormX.daily_history or "fondle pussy" in StormX.daily_history or "fondle ass" in StormX.daily_history:
            #If you've fondled Storm today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in StormX.Inventory and "256 Shades of Grey" in StormX.Inventory and "Avengers Tower Penthouse" in StormX.Inventory:
            #If you've given Storm the books
            if "book" not in StormX.Chat:
                $ Options.append("booked")
        if "lace bra" in StormX.Inventory or "lace panties" in StormX.Inventory:
            #If you've given Storm the lingerie
            if "lingerie" not in StormX.Chat:
                $ Options.append("lingerie")
        if StormX.Hand:
            #If Storm's given a handjob
            $ Options.append("handy")
        if StormX.Swallow:
            #If Storm's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in StormX.daily_history or "painted" in StormX.daily_history:
            #If Storm's been facialed
            $ Options.append("facial")
        if StormX.Sleep:
            #If Storm's slept over
            $ Options.append("sleep")
        if StormX.CreamP or StormX.CreamA:
            #If Storm's been creampied
            $ Options.append("creampie")
        if StormX.Sex or StormX.Anal:
            #If Storm's been sexed
            $ Options.append("sexed")
        if StormX.Anal:
            #If Storm's been analed
            $ Options.append("anal")

        if "seenpeen" in StormX.History:
            $ Options.append("seenpeen")
        if "nudity" not in StormX.History:
            $ Options.append("nudity")
#        if "topless" in StormX.History:
#            $ Options.append("topless")
#        if "bottomless" in StormX.History:
#            $ Options.append("bottomless")

#        if not StormX.Chat[0] and StormX.Sex:
#            $ Options.append("virgin")

#        if (bg_current == "bg laura" or bg_current == "bg player") and "relationship" not in StormX.daily_history:
#            if "lover" not in StormX.Petnames and ApprovalCheck(StormX, 900, "L"): # StormX.Event[6]
#                $ Options.append("lover?")
#            elif "sir" not in StormX.Petnames and ApprovalCheck(StormX, 500, "O"): # StormX.Event[7]
#                $ Options.append("sir?")
#            elif "daddy" not in StormX.Petnames and ApprovalCheck(StormX, 750, "L") and ApprovalCheck(StormX, 500, "O") and ApprovalCheck(StormX, 500, "I"): # StormX.Event[5]
#                $ Options.append("daddy?")
#            elif "master" not in StormX.Petnames and ApprovalCheck(StormX, 900, "O"): # StormX.Event[8]
#                $ Options.append("master?")
#            elif "sex friend" not in StormX.Petnames and ApprovalCheck(StormX, 500, "I"): # StormX.Event[9]
#                $ Options.append("sexfriend?")
#            elif "fuck buddy" not in StormX.Petnames and ApprovalCheck(StormX, 900, "I"): # StormX.Event[10]
#                $ Options.append("fuckbuddy?")


        if not ApprovalCheck(StormX, 300):            #She dislikes you
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one

    if Options[0] == "mandrill":
        $ StormX.daily_history.append("cologne chat")
        $ StormX.FaceChange("confused")
        ch_s "(sniff, sniff). . . I can smell. . . some type of ape . . ."
        $ StormX.FaceChange("sexy", 2)
        ch_s ". . . you are looking quite fetching though. . ."
    elif Options[0] == "purple":
        $ StormX.daily_history.append("cologne chat")
        $ StormX.FaceChange("sly",1)
        ch_s "(sniff, sniff). . . what is that odor? . ."
        $ StormX.FaceChange("normal",0)
        ch_s ". . . was there anything that you wanted?"
    elif Options[0] == "corruption":
        $ StormX.daily_history.append("cologne chat")
        $ StormX.FaceChange("confused")
        ch_s "(sniff, sniff). . . that's a strong odor. . ."
        $ StormX.FaceChange("angry")
        ch_s ". . . I'm feeling quite dangerous. . ."
        $ StormX.FaceChange("sly")

    elif Options[0] == "caught": # Xavier's caught you
            if "caught chat" in StormX.Chat:
                    ch_s "We should be more careful where we're seen together. . ."
                    if not ApprovalCheck(StormX, 500, "I"):
                         ch_s "Not that this should stop us. . ."
            else:
                    ch_s "I am sorry for that unforunate business with Charles."
                    if not ApprovalCheck(StormX, 500, "I"):
                        ch_s "I suppose we should avoid activities in public."
                    else:
                        ch_s "I did enjoy the thrill though. . ."
                    $ StormX.Chat.append("caught chat")
    elif Options[0] == "key": # you have her key
            if StormX.SEXP <= 15:
                ch_s "I gave you that key for convenience, do not abuse it . ."
            else:
                ch_s "I gave you a key, but you never come up to visit me. . ."
            $ StormX.Chat.append("key")

#    elif Options[0] == "cheek":
#            #Storm's response to having her cheek touched.
#            ch_s "So,[StormX.Petname]. . .y'know how you[StormX.like]kinda just brushed my cheek before?"
#            ch_p "Yeah?  Was that okay?"
#            $ StormX.FaceChange("smile",1)
#            ch_s "More than just {i}okay{/i}."
#            $ StormX.Chat.append("cheek")


    elif Options[0] == "dated":
            #Storm's response to having gone on a date with the Player.
            ch_s "I enjoyed our date, we should definitely do that again sometime."

    elif Options[0] == "kissed":
            #Storm's response to having been kissed by the Player.
            $ StormX.FaceChange("normal",1)
            ch_s "You know, [StormX.Petname], you are a quite good kisser."
            menu:
                extend ""
                "Hey. . .I'm the best there is at what I do.":
                        $ StormX.FaceChange("bemused",1,Eyes="leftside")
                        ch_s "Well, one of the best, perhaps."
                        $ StormX.FaceChange("smile",1)
                        ch_s "But we'll get you there. . ."
                "No. You think?":
                        ch_s "I'm quie certain. . ."
                        ch_s "But we could experiment. . ."

    elif Options[0] == "dangerroom":
            #Storm's response to Player working out in the Danger Room while Storm is present
            $ StormX.FaceChange("sly",1)
            ch_s "Hey,[StormX.Petname].  I saw your work in the Danger Room."
            ch_s "You might want to stay close to a \"tank\" to avoid damage. . ."
    elif Options[0] == "nudity":
            #Storm's response to Player asking about nudity.
            ch_p "I've noticed you walk around naked more than the others."
            call Storm_Nudity

#    elif Options[0] == "showercaught":
#            #Storm's response to being caught in the shower.
#            if "shower" in StormX.Chat:
#                ch_s "You saw me taking a shower again. . ."
#            else:
#                ch_s "Do you make a habit of bursting into the showers?"
#                $ StormX.Chat.append("shower")
#                menu:
#                    extend ""
#                    "It was a total accident!  I promise!":
#                            $ StormX.Statup("Love", 50, 5)
#                            $ StormX.Statup("Love", 90, 2)
#                            if ApprovalCheck(StormX, 1200):
#                                $ StormX.FaceChange("sly",1)
#                                ch_s "I didn't mind."
#                            $ StormX.FaceChange("smile")
#                            ch_s "We all make mistakes."
#                    "Just with you.":
#                            $ StormX.Statup("Obed", 40, 5)
#                            if ApprovalCheck(StormX, 1000) or ApprovalCheck(StormX, 700, "L"):
#                                    $ StormX.Statup("Love", 90, 3)
#                                    $ StormX.FaceChange("sly",1)
#                                    ch_s "Hmm, I guess that's a compliment."
#                            else:
#                                    $ StormX.Statup("Love", 70, -5)
#                                    $ StormX.FaceChange("angry")
#                                    ch_s "I think I should be insulted."
#                    "Totally on purpose. I regret nothing.":
#                            if ApprovalCheck(StormX, 1200):
#                                    $ StormX.Statup("Love", 90, 3)
#                                    $ StormX.Statup("Obed", 70, 10)
#                                    $ StormX.Statup("Inbt", 50, 5)
#                                    $ StormX.FaceChange("sly",1)
#                                    ch_s "You seem to know what you want."
#                            elif ApprovalCheck(StormX, 800):
#                                    $ StormX.Statup("Obed", 60, 5)
#                                    $ StormX.Statup("Inbt", 50, 5)
#                                    $ StormX.FaceChange("perplexed",2)
#                                    ch_s "I guess you show initiative."
#                                    $ StormX.Blush = 1
#                            else:
#                                    $ StormX.Statup("Love", 50, -10)
#                                    $ StormX.Statup("Love", 80, -10)
#                                    $ StormX.Statup("Obed", 50, 10)
#                                    $ StormX.FaceChange("angry")
#                                    ch_s "That's a bit disturbing."

    elif Options[0] == "fondled":
            #Storm's response to being felt up.
            if StormX.FondleB + StormX.FondleP + StormX.FondleA >= 15:
                ch_s "Please touch me. . . sometime. . .."
            else:
                ch_s "You know, you could touch me. . . if you wanted."

    elif Options[0] == "booked":
            #Storm's response after a Player gives her the books from the shop.
            ch_s "I read those books you gave me."
            menu:
                extend ""
                "Yeah?  Did you like them?":
                        $ StormX.FaceChange("sly",2)
                        ch_s "They were. . .{i}interesting{/i}."
                "Good.  You looked like you could use to learn a thing or two from them.":
                        $ StormX.Statup("Love", 90, -3)
                        $ StormX.Statup("Obed", 70, 5)
                        $ StormX.Statup("Inbt", 50, 5)
                        $ StormX.FaceChange("angry")
                        ch_s "Well, I cannot say they I din't learn a thing or so."
            $ StormX.Blush = 1
            $ StormX.Chat.append("book")

    elif Options[0] == "lingerie":
            #Storm's response to being given lingerie.
            $ StormX.FaceChange("sly",2)
            ch_s "I have enjoyed that lingerie you purchased for me."
            $ StormX.Blush = 1
            $ StormX.Chat.append("lingerie")

    elif Options[0] == "handy":
            #Storm's response after giving the Player a handjob.
            $ StormX.FaceChange("sly",1)
            ch_s "I was thinking about having your cock in my hand the other day. . ."
            ch_s "Were you?"
            $ StormX.Blush = 0

    elif Options[0] == "blow":
            if "blow" not in StormX.Chat:
                    #Storm's response after giving the Player a blowjob.
                    $ StormX.FaceChange("sly",2)
                    ch_s "I was curious, did you enjoy that blowjob earlier?"
                    menu:
                        extend ""
                        "You were totally amazing.":
                                    $ StormX.Statup("Love", 90, 5)
                                    $ StormX.Statup("Inbt", 60, 10)
                                    $ StormX.FaceChange("normal",1)
                                    ch_s ". . . "
                                    $ StormX.FaceChange("sexy",1)
                                    ch_s "As I had hoped. . ."
                                    ch_s "Let me know if you're like a repeat. . ."
                        "Honestly? It was good. . .but you could use a little practice, I think.":
                                if ApprovalCheck(StormX, 300, "I") or not ApprovalCheck(StormX, 800):
                                    $ StormX.Statup("Love", 90, -5)
                                    $ StormX.Statup("Obed", 60, 10)
                                    $ StormX.Statup("Inbt", 50, 10)
                                    $ StormX.FaceChange("perplexed",1)
                                    ch_s "Oh? Well I am sorry I was not up to your usual standards. . ."
                                else:
                                    $ StormX.Statup("Obed", 70, 15)
                                    $ StormX.Statup("Inbt", 50, 5)
                                    $ StormX.FaceChange("sexy",1)
                                    ch_s "Oh? I'm certain that I can improve on the experience. . ."
                        "I guess. If you're into weird sounds and too much teeth. Spoiler, I'm not.":
                                    $ StormX.Statup("Love", 90, -10)
                                    $ StormX.Statup("Obed", 60, 10)
                                    $ StormX.FaceChange("angry",2)
                                    ch_s "Oh, then I suppose you will not miss it."
                    $ StormX.Blush = 1
                    $ StormX.Chat.append("blow")
            else:
                    $ Line = renpy.random.choice(["You know, I really do enjoy the taste of your cock.",
                            "I think I nearly dislocated my jaw last time.",
                            "Let me know if you would enjoy another blowjob.",
                            "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
                    ch_s "[Line]"

    elif Options[0] == "swallowed":
            #Storm's response after swallowing the Player's cum.
            if "swallow" in StormX.Chat:
                ch_s "I would like to taste you again sometime."
            else:
                ch_s "So. . . the other day. . ."
                ch_s "I really enjoyed the taste of your semen."
                $ StormX.FaceChange("sly",1)
                ch_s "Fairly surpirsing, all things considered."
                $ StormX.Chat.append("swallow")

    elif Options[0] == "facial":
            #Storm's response after taking a facial from the Player.
            ch_s ". . .I know this is a bit unusual, but. . ."
            $ StormX.FaceChange("sexy",2)
            ch_s "I do so enjoy when you cum on my face. . ."
            $ StormX.Blush = 1

    elif Options[0] == "sleepover":
            #Storm's response after sleeping with the Player.
            ch_s "I really enjoyed the other night."
            ch_s "I don't often get to sleep with someone else around. . ."

    elif Options[0] == "creampie":
            #Another of Storm's responses after having sex with the Player.
            "[StormX.Name] draws close to you so she can whisper into your ear."
            ch_s "I can still feel you. . .running down the inside of my thigh."

    elif Options[0] == "sexed":
            #A final response from Storm after having sex with the Player.
            ch_s "So. . . you should know. . ."
            $ StormX.FaceChange("sexy",2)
            ch_s ". . .when I. . . care for my own needs. . ."
            ch_s "It is you that I imagine with me. . ."
            $ StormX.Blush = 1

    elif Options[0] == "anal":
            #Storm's response after getting anal from the Player.
            $ StormX.FaceChange("sly")
            ch_s "I never much cared for anal sex."
            $ StormX.FaceChange("sexy",1)
            ch_s ". . . but you have turned me around on the idea."

    elif Options[0] == "seenpeen": # first seen peen skipped
            $ StormX.FaceChange("sly",1, Eyes="leftside")
            ch_s "Oh, just so you are aware, I was impressed by your. . ."
            $ StormX.FaceChange("sly",2, Eyes="down")
            ch_s ". . . manhood. . ."
            $ StormX.FaceChange("bemused",1)
            $ StormX.Statup("Love", 50, 5)
            $ StormX.History.remove("seenpeen")
#    elif Options[0] == "topless": # first seen breasts skipped
#            ch_s "Hey,what'd you think of my tits?"
#            ch_s "Did you like what you saw?"
#            call Storm_First_TMenu
#            $ StormX.History.remove("topless")
#    elif Options[0] == "bottomless": # first seen pussy skipped
#            ch_s "Hey, what'd you think when you saw my pussy earlier?"
#            call Storm_First_BMenu
#            $ StormX.History.remove("bottomless")

#    elif Options[0] == "boyfriend?":
#        call Storm_BF
#    elif Options[0] == "lover?":
#        call Storm_Love
#    elif Options[0] == "sir?":
#        call Storm_Sub
#    elif Options[0] == "master?":
#        call Storm_Master
#    elif Options[0] == "sexfriend?":
#        call Storm_Sexfriend
#    elif Options[0] == "fuckbuddy?":
#        call Storm_Fuckbuddy
#    elif Options[0] == "daddy?":
#        call Storm_Daddy

    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["Get away from me.",
                "I don't want you in my sight.",
                "Stay away.",
                "Leave me."])
        ch_s "[Line]"

    else: #all else fell through. . .
#            $ D20 = renpy.random.randint(1, 15)
#            if D20 == 1:
#                    $ StormX.FaceChange("smile")
#                    ch_s "I noticed you did well on your last exam."
#            elif D20 == 2:
#                    $ StormX.FaceChange("annoyed")
#                    ch_s "If I have to hear him say \"I'm the best there is\" one more time, I swear I'm going ..."
#            elif D20 == 3:
#                    $ StormX.FaceChange("surprised")
#                    ch_s "Huh? Oh, sorry. I sort of spaced out. That's not like me."
#            elif D20 == 4:
#                    $ StormX.FaceChange("sad")
#                    ch_s "Oh, [StormX.Petname]. I was just remembering something. Don't worry about it."
#            elif D20 == 5:
#                    $ StormX.FaceChange("smile")
#                    ch_s "I had a good nap. It's nice to be somewhere I can just doze off without worry."
#            elif D20 == 6:
#                    $ StormX.FaceChange("perplexed")
#                    ch_s "Oh, [StormX.Petname]. I think I just saw Emma Frost staring at Cyclops. That's... wierd."
#            elif D20 == 7:
#                    $ StormX.FaceChange("smile")
#                    ch_s "I just got a new personal best time in the Danger Room."
#            elif D20 == 8:
#                    $ StormX.FaceChange("sad")
#                    ch_s "I like being here, but sometimes there's just so much noise..."
#            elif D20 == 9:
#                    $ StormX.FaceChange("confused")
#                    ch_s "I'm still trying to figure out what the mystery meat in the cafeteria was today."
#                    ch_s "I have enhanced senses, this shouldn't be so difficult!"
#            elif D20 == 10:
#                    $ StormX.FaceChange("smile")
#                    ch_s "Kitty, Rogue and some of the others asked me if I wanted to go grab some ice cream with them tomorrow."
#            elif D20 == 11:
#                    $ StormX.FaceChange("smile")
#                    ch_s "I tried out a dance class like Kitty said. Apparently I'm good at it."
#            elif D20 == 12:
#                    $ StormX.FaceChange("sad")
#                    ch_s "I like talking to Kitty and the others. It makes me feel, I don't know. . ."
#                    ch_s "{i}not{/i} like a really dangerous mutant who could kill everyone around me if I flipped out."
#            elif D20 == 13:
#                    $ StormX.FaceChange("smile")
#                    ch_s "Kitty and Rogue dared me to call Logan \"Dad\". I think we might've given him a heart attack."
#            elif D20 == 14:
#                    $ StormX.FaceChange("sad")
#                    ch_s "I like going out on missions, but catching up with what's been going on while I'm gone is always a pain."
#            elif D20 == 15:
#                    $ StormX.FaceChange("perplexed")
#                    ch_s "So they're called the \"Avengers\", but do they ever do any avenging?"
#                    ch_s "At least the Fantastic Four really do things that are strange and fantastic."
#            elif D20 == 16:
#                    $ StormX.FaceChange("perplexed")
#                    ch_s "Have you ever been to New York? Sometimes I'm surprised anyone still wants to live there."
#            elif D20 == 17:
#                    $ StormX.FaceChange("perplexed")
#                    ch_s "Logan just walked up and told me that if I ever meet someone called. . ."
#                    ch_s "\"Dead...Poole?\"...I should just go ahead and stab him in the face."
#                    ch_s "What's up with that?"
#            elif D20 == 18:
#                    $ StormX.FaceChange("smile")
#                    ch_s "Don't tell anyone this, but I think Cyclops is kind of wound up tight."
#            elif D20 == 19:
#                    $ StormX.FaceChange("confused")
#                    ch_s "Do you smell something? Is that... nachos and... chocolate syrup?!"
#            elif D20 == 20:
#                    $ StormX.FaceChange("smile")
#                    ch_s "I like being able to just talk about nothing in particular. It's... nice."
#            else:
                    $ StormX.FaceChange("smile")
                    ch_s "I do enjoy being with you. . ."

    $ Line = 0
    return

# start Storm_Names//////////////////////////////////////////////////////////
label Storm_Names:     #rkeljs
    menu:
        ch_s "Oh? What would you prefer I call you?"
        "My initial's fine.":
            $ StormX.Petname = Player.Name[:1]  #fix test this
            ch_s "You got it, [StormX.Petname]."
        "Call me by my name.":
            $ StormX.Petname = Player.Name
            ch_s "If you'd rather, [StormX.Petname]."
        "Call me \"boyfriend\"." if "boyfriend" in StormX.Petnames:
            $ StormX.Petname = "boyfriend"
            ch_s "Very well, [StormX.Petname]."
        "Call me \"lover\"." if "lover" in StormX.Petnames:
            $ StormX.Petname = "lover"
            ch_s "I would love to, [StormX.Petname]."
        "Call me \"beloved\"." if "lover" in StormX.Petnames:
            $ StormX.Petname = "beloved"
            ch_s "I would love to, [StormX.Petname]."
        "Call me \"sir\"." if "sir" in StormX.Petnames:
            $ StormX.Petname = "sir"
            ch_s "Yes, [StormX.Petname]."
        "Call me \"master\"." if "master" in StormX.Petnames:
            $ StormX.Petname = "master"
            ch_s "As you wish, [StormX.Petname]."
        "Call me \"sex friend\"." if "sex friend" in StormX.Petnames:
            $ StormX.Petname = "sex friend"
            ch_s "Quite cheeky, [StormX.Petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in StormX.Petnames:
            $ StormX.Petname = "fuck buddy"
            ch_s "Fine, [StormX.Petname]."
        "Call me \"daddy\"." if "daddy" in StormX.Petnames:
            $ StormX.Petname = "daddy"
            ch_s "Ok, [StormX.Petname]."
        "Nevermind.":
            return
    return
# end Storm_Names//////////////////////////////////////////////////////////

label Storm_Pet: #rkeljs
    while 1:
        menu:
            extend ""
            "Polite":
                menu:
                    "I think I'll call you. . ."
                    "Ororo.":
                        $ StormX.Pet = "Ororo"
                        ch_s "I don't see why not, [StormX.Petname]."
                    "Storm.":
                        $ StormX.Pet = "Storm"
                        ch_s "I don't see why not, [StormX.Petname]."
                    "Stormy.":
                        $ StormX.Pet = "Stormy"
                        if ApprovalCheck(StormX, 600):
                            $ StormX.FaceChange("smile", 1)
                            ch_s "I don't see why not, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("normal", 1)
                            ch_s "I would rather you weren't so familiar, [StormX.Petname]."
                    "'Ro.":
                        $ StormX.Pet = "'Ro"
                        if ApprovalCheck(StormX, 700):
                            $ StormX.FaceChange("smile", 1)
                            ch_s "I don't see why not, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("normal", 1)
                            ch_s "I would rather you weren't so familiar, [StormX.Petname]."

                    "Ms. Munroe." if "Ms. Munroe" in StormX.Names:
                        $ StormX.Pet = "Ms. Munroe"
                        if ApprovalCheck(StormX, 700):
                            $ StormX.FaceChange("bemused", 1)
                            ch_s "I don't see why not, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("normal", 1)
                            ch_s "That would be a bit much, [StormX.Petname]."


                    "\"girl\".":
                        $ StormX.Pet = "girl"
                        if "boyfriend" in StormX.Petnames or ApprovalCheck(StormX, 600, "L"):
                            $ StormX.FaceChange("sexy", 1)
                            ch_s "I can be your girl, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("angry")
                            ch_s "I'm NOT your girl, [StormX.Petname]."

                    "\"boo\".":
                        $ StormX.Pet = "boo"
                        if "boyfriend" in StormX.Petnames or ApprovalCheck(StormX, 700, "L"):
                            $ StormX.FaceChange("sexy", 1)
                            ch_s "I can be your boo, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("angry")
                            ch_s "I'm NOT your boo,  [StormX.Petname]."

                    "\"bae\".":
                        $ StormX.Pet = "bae"
                        if "boyfriend" in StormX.Petnames or ApprovalCheck(StormX, 600, "L"):
                            $ StormX.FaceChange("sexy", 1)
                            ch_s "I can be your bae, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("angry")
                            ch_s "I'm NOT your bae,  [StormX.Petname]."

                    "\"baby\".":
                        $ StormX.Pet = "baby"
                        if "boyfriend" in StormX.Petnames or ApprovalCheck(StormX, 500, "L"):
                            $ StormX.FaceChange("sexy", 1)
                            ch_s "Cute, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("angry")
                            ch_s "I am not your baby."


                    "\"sweetie\".":
                        $ StormX.Pet = "sweetie"
                        if "boyfriend" in StormX.Petnames or ApprovalCheck(StormX, 600, "L"):
                            ch_s "That is so sweet, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "Perhaps too sweet, [StormX.Petname]."

                    "\"sexy\".":
                        $ StormX.Pet = "sexy"
                        if "lover" in StormX.Petnames or ApprovalCheck(StormX, 800):
                            $ StormX.FaceChange("sexy", 1)
                            ch_s "I suppose that I am, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "Crossing a line there, [StormX.Petname]."

                    "\"lover\".":
                        $ StormX.Pet = "lover"
                        if "lover" in StormX.Petnames or ApprovalCheck(StormX, 1200):
                            $ StormX.FaceChange("sexy", 1)
                            ch_s "I am, I suppose."
                        else:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "I do not think so, [StormX.Petname]."

                    "Back":
                        pass

            "Risky":
                menu:
                    "I think I'll call you. . ."
                    "\"slave\".":
                        $ StormX.Pet = "slave"
                        if "master" in StormX.Petnames or ApprovalCheck(StormX, 850, "O"):
                            $ StormX.FaceChange("bemused", 1)
                            ch_s "As you wish, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "I am no one's slave, [StormX.Petname]."

                    "\"pet\".":
                        $ StormX.Pet = "pet"
                        if "master" in StormX.Petnames or ApprovalCheck(StormX, 700, "O"):
                            $ StormX.FaceChange("bemused", 1)
                            ch_s "You can pet me if you want, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "I am no one's pet, [StormX.Petname]."

                    "\"slut\".":
                        $ StormX.Pet = "slut"
                        if "sex friend" in StormX.Petnames or ApprovalCheck(StormX, 900, "OI"):
                            $ StormX.FaceChange("sexy")
                            ch_s "Fair enough."
                        else:
                            $ StormX.FaceChange("angry", 1)
                            $ StormX.Mouth = "surprised"
                            ch_s "You would do well to avoid that."

                    "\"whore\".":
                        $ StormX.Pet = "whore"
                        if "fuckbuddy" in StormX.Petnames or ApprovalCheck(StormX, 1000, "OI"):
                            $ StormX.FaceChange("sly")
                            ch_s ". . ."
                        else:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "Do not tempt me to harm you. . ."

                    "\"sugartits\".":
                        $ StormX.Pet = "sugartits"
                        if "sex friend" in StormX.Petnames or ApprovalCheck(StormX, 1400):
                            $ StormX.FaceChange("sly", 1)
                            ch_s "I suppose. . ."
                        else:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "Why would you even-."

                    "\"sex friend\".":
                        $ StormX.Pet = "sex friend"
                        if "sex friend" in StormX.Petnames or ApprovalCheck(StormX, 600, "I"):
                            $ StormX.FaceChange("sly")
                            ch_s "Yes. . ."
                        else:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "Keep it quiet, [StormX.Petname]."

                    "\"fuckbuddy\".":
                        $ StormX.Pet = "fuckbuddy"
                        if "fuckbuddy" in StormX.Petnames or ApprovalCheck(StormX, 700, "I"):
                            $ StormX.FaceChange("sly")
                            ch_s "Sure."
                        else:
                            $ StormX.FaceChange("angry", 1)
                            $ StormX.Mouth = "surprised"
                            ch_s "That is not even funny, [StormX.Petname]."

                    "\"baby girl\".":
                        $ StormX.Pet = "baby girl"
                        if "daddy" in StormX.Petnames or ApprovalCheck(StormX, 1200):
                            $ StormX.FaceChange("smile", 1)
                            ch_s "I suppose?"
                        else:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "How odd. . ."

                    "Back":
                        pass

            "Nevermind.":
                return
    return

#label Storm_Namecheck(StormX.Pet = StormX.Pet, Cnt = 0, Ugh = 0): #replaced with $ Girl.NameCheck() #checks reaction to petname


# start Storm_Rename//////////////////////////////////////////////////////////
label Storm_Rename:   #rkeljs
        #Sets alternate names from Storm
        $ StormX.Mouth = "smile"
        ch_s "Yeah?"
        menu:
            extend ""
            "I think \"Storm's\" a cool name." if StormX.Name != "Storm" and "Storm" in StormX.Names:
                    $ StormX.Name = "Storm"
                    ch_s "Sounds good."
            "I think \"Ororo's\" a pretty name." if StormX.Name != "Ororo" and "Ororo" in StormX.Names:
                    $ StormX.Name = "Ororo"
                    ch_s "Sounds good."
            "I think \"Ms. Munroe's\" a pretty name." if StormX.Name != "Ms. Munroe" and "Ms. Munroe" in StormX.Names:
                    $ StormX.Name = "Ms. Munroe"
                    ch_s "Sounds good."
            "Nevermind.":
                    pass
        $ StormX.AddWord(1,0,"namechange")
        return
# end Storm_Rename//////////////////////////////////////////////////////////


# start Storm_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Storm_Personality(Cnt = 0):    #rkeljs
    if not StormX.Chat[4] or Cnt:
        "Since you're doing well in one area, you can convince Storm to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_s "Yes? What was it you wanted?"
        "More Obedient. [[Love to Obedience]" if StormX.Love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_s "I suppose that I could try."
            $ StormX.Chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if StormX.Love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_s "I can try to be more open."
            $ StormX.Chat[4] = 2

        "Less Inhibited. [[Obedience to Inhibition]" if StormX.Obed > 900:
            ch_p "I want you to be less inhibited."
            ch_s "I can try to be more open."
            $ StormX.Chat[4] = 3
        "More Loving. [[Obedience to Love]" if StormX.Obed > 900:
            ch_p "I'd like you to learn to love me."
            ch_s "I can try."
            $ StormX.Chat[4] = 4

        "More Obedient. [[Inhibition to Obedience]" if StormX.Inbt > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_s "I suppose that I could try."
            $ StormX.Chat[4] = 5

        "More Loving. [[Inhibition to Love]" if StormX.Inbt > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_s "I will try."
            $ StormX.Chat[4] = 6

        "I guess just do what you like. . .[[reset]" if StormX.Chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_s ". . . very well."
            $ StormX.Chat[4] = 0
        "Repeat the rules":
            call Storm_Personality(1)
            return
        "Nevermind.":
            return
    return

label Storm_Clothes:  #rkeljs
    if StormX.Taboo and StormX not in Rules:
            if "exhibitionist" in StormX.Traits:
                ch_s "Oh, here? . ."
            elif ApprovalCheck(StormX, 900, TabM=4) or ApprovalCheck(StormX, 400, "I", TabM=3):
                ch_s "I'm not supposed to undress here. . ."
            else:
                ch_s "I'm not supposed to undress here. . ."
                ch_s "Can we talk about this in our rooms?"
                return
    elif ApprovalCheck(StormX, 900, TabM=4) or ApprovalCheck(StormX, 600, "L") or ApprovalCheck(StormX, 300, "O"):
                ch_s "Oh? What about them?"
    else:
                ch_s "I don't really need fashion advice, thank you."
                return

    if Girl != StormX or Line == "Giftstore":
            #This culls returns if sent from another girl
            $ renpy.pop_call()
    $ Line = 0
    $ Girl = StormX
    call Shift_Focus(Girl)

label Storm_Wardrobe_Menu:
    $ StormX.FaceChange()
    $ Trigger = 1 # to prevent Focus swapping. . .
    while True:
        menu:
            ch_s "What about my wardrobe?"
            "Overshirts":
                        call Storm_Clothes_Over
            "Legwear":
                        call Storm_Clothes_Legs
            "Underwear":
                        call Storm_Clothes_Under
            "Accessories":
                        call Storm_Clothes_Misc
            "Outfit Management":
                        call Storm_Clothes_Outfits
            "Let's talk about what you wear around.":
                        call Clothes_Schedule(StormX)

            "Could I get a look at it?" if StormX.Loc != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(StormX,0,2)
                    if _return:
                            show PhoneSex zorder 150
                            ch_s "What do you think?"
                    hide PhoneSex
            "Could I get a look at it?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(StormX,0,2)
                    if _return:
                        hide DressScreen
            "Would you be more comfortable behind a screen? (locked)" if StormX.Taboo:
                    pass
            "Would you be more comfortable behind a screen?" if StormX.Loc == bg_current and not StormX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    #if ApprovalCheck(StormX, 1500) or (StormX.SeenChest and StormX.SeenPussy):
                            ch_s "I won't need it, but I appreciate the offer."
                    #else:
#                            show DressScreen zorder 150
#                            ch_s "Yeah, this is better."

            "Gift for you (locked)" if Girl.Loc != bg_current:
                            pass
            "Gift for you" if Girl.Loc == bg_current:
                            ch_p "I'd like to give you something."
                            call Gifts #(Girl)

            "Switch to. . .":
                    if renpy.showing('DressScreen'):
                            call OutfitShame(StormX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ StormX.OutfitChange()
                    $ StormX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ Trigger = 0
                    call Switch_Chat
                    if Girl != StormX:
                            ch_p "I wanted to talk about your clothes."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = StormX
                    call Shift_Focus(Girl)

            "Never mind, you look good like that.":
                    if "wardrobe" not in StormX.RecentActions:
                            #Apply stat boosts only if it's the first time this turn
                            if (StormX.OverNum()+StormX.ChestNum()<4) or (StormX.PantiesNum()+StormX.PantsNum() < 5):
                                    #if she's half-naked
                                    $ StormX.FaceChange("sly",Eyes="down")
                                    ch_s "I understand why -you- would think so. . ."
                                    $ StormX.FaceChange("sly")
                            elif StormX.Chat[1] <= 1:
                                    $ StormX.Statup("Love", 70, 15)
                                    $ StormX.Statup("Obed", 40, 20)
                                    ch_s "Oh, how sweet of you to say so."
                            elif StormX.Chat[1] <= 10:
                                    $ StormX.Statup("Love", 70, 5)
                                    $ StormX.Statup("Obed", 40, 7)
                                    ch_s "I do enjoy this look."
                            elif StormX.Chat[1] <= 50:
                                    $ StormX.Statup("Love", 70, 1)
                                    $ StormX.Statup("Obed", 40, 1)
                                    ch_s "Thank you. . ."
                            else:
                                    ch_s "Certainly."
                            $ StormX.RecentActions.append("wardrobe")
                    if renpy.showing('DressScreen'):
                            call OutfitShame(StormX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ StormX.OutfitChange()
                    $ StormX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ StormX.Chat[1] += 1
                    $ Trigger = 0
                    return

        #Loops back up
        #return #jump Storm_Clothes
        #End of Storm Wardrobe Main Menu

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Storm_Clothes_Outfits:
        # Outfits
        "You should remember that one. [[Set Custom]":
                menu:
                    "Which slot would you like this saved in?"
                    "Custom 1":
                                call OutfitShame(StormX,3,1)
                    "Custom 2":
                                call OutfitShame(StormX,5,1)
                    "Custom 3":
                                call OutfitShame(StormX,6,1)
                    "Gym Clothes":
                                call OutfitShame(StormX,4,1)
                    "Sleepwear":
                                call OutfitShame(StormX,7,1)
                    "Swimwear":
                                call OutfitShame(StormX,10,1)
                    #8 is Emma's teaching clothes,
                    "Never mind":
                                pass

        "That skirt combo":
                $ StormX.OutfitChange("casual1")
                menu:
                    "You should wear this one out. [[set current outfit]":
                            $ StormX.Outfit = "casual1"
                            $ StormX.Shame = 0
                            ch_s "Yes, this is my preferred casual outfit."
                    "Let's try something else though.":
                            ch_s "Ok."

        "Leather jacket and pants combo":
                $ StormX.OutfitChange("casual2")
                menu:
                    "You should wear this one out. [[set current outfit]":
                            $ StormX.Outfit = "casual2"
                            $ StormX.Shame = 0
                            ch_s "Yes, I find this one more stylish."
                    "Let's try something else though.":
                            ch_s "Ok."

        "Remember that outfit we put together? [[Set a custom outfit] (locked)" if not StormX.Custom1[0] and not StormX.Custom2[0] and not StormX.Custom3[0]:
                        pass

        "Remember that outfit we put together?" if StormX.Custom1[0] or StormX.Custom2[0] or StormX.Custom3[0]:
                $ Cnt = 0
                while 1:
                    menu:
                        "Throw on Custom 1 (locked)" if not StormX.Custom1[0]:
                                pass
                        "Throw on Custom 1" if StormX.Custom1[0]:
                                $ StormX.OutfitChange("custom1")
                                $ Cnt = 3
                        "Throw on Custom 2 (locked)" if not StormX.Custom2[0]:
                                pass
                        "Throw on Custom 2" if StormX.Custom2[0]:
                                $ StormX.OutfitChange("custom2")
                                $ Cnt = 5
                        "Throw on Custom 3 (locked)" if not StormX.Custom3[0]:
                                pass
                        "Throw on Custom 3" if StormX.Custom3[0]:
                                $ StormX.OutfitChange("custom3")
                                $ Cnt = 6

                        "You should wear this one in private. (locked)" if not Cnt:
                                pass
                        "You should wear this one in private." if Cnt:
                                if Cnt == 5:
                                        $ StormX.Clothing[9] = "custom2"
                                elif Cnt == 6:
                                        $ StormX.Clothing[9] = "custom3"
                                else:
                                        $ StormX.Clothing[9] = "custom1"
                                ch_s "That would be fine."

                        "On second thought, forget about that one outfit. . .":
                                menu:
                                    "Custom 1 [[clear custom 1]" if StormX.Custom1[0]:
                                            ch_s "Fine."
                                            $ StormX.Custom1[0] = 0
                                    "Custom 1 [[clear custom 1] (locked)" if not StormX.Custom1[0]:
                                            pass
                                    "Custom 2 [[clear custom 2]" if StormX.Custom2[0]:
                                            ch_s "Fine."
                                            $ StormX.Custom2[0] = 0
                                    "Custom 2 [[clear custom 2] (locked)" if not StormX.Custom2[0]:
                                            pass
                                    "Custom 3 [[clear custom 3]" if StormX.Custom3[0]:
                                            ch_s "Fine."
                                            $ StormX.Custom3[0] = 0
                                    "Custom 3 [[clear custom 3] (locked)" if not StormX.Custom3[0]:
                                            pass
                                    "Never mind, [[back].":
                                            pass

                        "You should wear this one out. [[choose outfit first](locked)" if not Cnt:
                                pass
                        "You should wear this one out." if Cnt:
                                call Custom_Out(StormX,Cnt)
                        "Ok, back to what we were talking about. . .":
                                $ Cnt = 0
                                return #jump Storm_Clothes

        "Gym Clothes?" if not StormX.Taboo or bg_current == "bg dangerroom":
                $ StormX.OutfitChange("gym")

        "Sleepwear?" if not StormX.Taboo:
                if ApprovalCheck(StormX, 1200):
                        $ StormX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(StormX)
                        if _return:
                                $ StormX.OutfitChange("sleep")

        "Swimwear? (locked)" if (StormX.Taboo and bg_current != "bg pool") or not StormX.Swim[0]:
                $ StormX.OutfitChange("swimwear")
        "Swimwear?" if (not StormX.Taboo or bg_current == "bg pool") and StormX.Swim[0]:
                $ StormX.OutfitChange("swimwear")


        "Halloween Costume?" if "halloween" in StormX.History:
                if StormX.Taboo <= 20 or StormX in Rules or StormX.PantsNum() >= 5:
                        ch_s "Fine."
                        $ StormX.OutfitChange("costume")
                elif ApprovalCheck(StormX, 1100, TabM=3):
                        ch_s "Ok."
                        $ StormX.OutfitChange("costume")
                else:
                        call Display_DressScreen(StormX)
                        if not _return:
                                ch_s "I would really rather not. . ."
                        else:
                                $ StormX.OutfitChange("costume")


        "Your birthday suit looks really great. . .":
                #Nude
                $ StormX.FaceChange("sexy", 1)
                $ Line = 0
                if not StormX.Chest and not StormX.Panties and not StormX.Over and not StormX.Legs and not StormX.Hose:
                        ch_s "Thank you."
                elif ApprovalCheck(StormX, 1200, TabM=4): #and StormX.SeenChest and StormX.SeenPussy
                        ch_s "Certainly. . ."
                        $ Line = 1
                elif ApprovalCheck(StormX, 2000, TabM=4):
                        ch_s "No foreplay?"
                        $ Line = 1
                elif not ApprovalCheck(StormX, 500, TabM=0):
                        $ StormX.FaceChange("confused", 1,Mouth="smirk")
                        ch_s "I don't exactly get nude on command, you know. . ."
                        $ StormX.FaceChange("bemused", 0)
                elif StormX.Taboo and StormX not in Rules: #StormX.SeenChest and StormX.SeenPussy and ApprovalCheck(StormX, 1200, TabM=0)
                        ch_s "Maybe, but not here. . ."
                elif ApprovalCheck(StormX, 1000, TabM=0):
                        $ StormX.FaceChange("confused", 1,Mouth="smirk")
                        ch_s "Yeah, but I'm not exactly showing it off."
                        $ StormX.FaceChange("bemused", 0)
                else:
                        $ StormX.FaceChange("angry", 1)
                        ch_s "I would rather not."

                if Line:
                    #If she got nude. . .
                    $ StormX.OutfitChange("nude")
                    "She throws her clothes off at her feet."
                    call Storm_First_Topless
                    call Storm_First_Bottomless(1)
                    $ StormX.FaceChange("sexy")
                    menu:
                        "You know, you should wear this one out. [[set current outfit]":
                            if "exhibitionist" in StormX.Traits:
                                    ch_s "mmmm. . ."
                                    $ StormX.Outfit = "nude"
                                    $ StormX.Statup("Lust", 50, 10)
                                    $ StormX.Statup("Lust", 70, 5)
                                    $ StormX.Shame = 50
                            elif ApprovalCheck(StormX, 800, "I") or ApprovalCheck(StormX, 2800, TabM=0) or StormX in Rules:
                                    ch_s "You know, I might. . ."
                                    $ StormX.Outfit = "nude"
                                    $ StormX.Shame = 50
                            else:
                                    $ StormX.FaceChange("sexy", 1)
                                    $ StormX.Eyes = "surprised"
                                    ch_s "I probably shouldn't. I am sorry."

                        "Let's try something else though.":
                            if "exhibitionist" in StormX.Traits:
                                    ch_s "Are you certain?"
                            elif ApprovalCheck(StormX, 800, "I") or ApprovalCheck(StormX, 2800, TabM=0) or StormX in Rules:
                                    $ StormX.FaceChange("bemused", 1)
                                    ch_s "I expected that you wanted me to go out like this."
                                    ch_s ". . ."
                            else:
                                    $ StormX.FaceChange("confused", 1)
                                    ch_s "I don't mind you seeing my body, but Charles does have his rules. . ."
                $ Line = 0

        "Never mind":
            return #jump Storm_Clothes

    return #jump Storm_Clothes
    #End of Storm Outfits

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Storm_Clothes_Over:
        # Overshirts
        "Why don't you go with no [StormX.Over]?" if StormX.Over:
                $ StormX.FaceChange("bemused", 1)
                if ApprovalCheck(StormX, 800, TabM=3):# and (StormX.Chest or StormX.SeenChest):
                    ch_s "Fine."
                elif ApprovalCheck(StormX, 600, TabM=0):
                    call Storm_NoBra
                    if not _return:
                        if not ApprovalCheck(StormX, 1200):
                            call Display_DressScreen(StormX)
                            if not _return:
                                return #jump Storm_Clothes
                        else:
                                return #jump Storm_Clothes
                else:
                    call Display_DressScreen(StormX)
                    if not _return:
                            ch_s "I would rather not."
                            if not StormX.Chest:
                                ch_s "I don't have anything under this. . ."
                            return #jump Storm_Clothes
                $ Line = StormX.Over
                $ StormX.Over = 0
                "She throws her [Line] at her feet."
                if not StormX.Chest and not renpy.showing('DressScreen'):
                        call Storm_First_Topless

        "Try on that white shirt." if StormX.Over != "white shirt":
                $ StormX.FaceChange("bemused")
                if not StormX.Over or StormX.ChestNum() >= 5:
                    #if she's not already wearing a top, or has fair clothes on under
                    ch_s "Very well."
                elif ApprovalCheck(StormX, 800, TabM=3):
                    ch_s "Very well."
                else:
                    call Display_DressScreen(StormX)
                    if not _return:
                            $ StormX.FaceChange("bemused", 1)
                            ch_s "I cannot really take this [StormX.Over] off at the moment."
                            return #jump Storm_Clothes
                $ StormX.Over = "white shirt"

        "Try on that leather jacket." if StormX.Over != "jacket":
                $ StormX.FaceChange("bemused")
                if not StormX.Over or StormX.ChestNum() >= 5:
                    #if she's not already wearing a top, or has fair clothes on under
                    ch_s "Very well."
                elif ApprovalCheck(StormX, 800, TabM=3):
                    ch_s "Very well."
                else:
                    call Display_DressScreen(StormX)
                    if not _return:
                            $ StormX.FaceChange("bemused", 1)
                            ch_s "I cannot really take this [StormX.Over] off at the moment."
                            return #jump Storm_Clothes
                $ StormX.Over = "jacket"

        "Maybe just throw on a towel?" if StormX.Over != "towel":
                $ StormX.FaceChange("bemused", 1)
                if StormX.ChestNum() >= 5: #or StormX.SeenChest
                    ch_s "If that's what you want. . ."
                elif ApprovalCheck(StormX, 1000, TabM=3):
                    $ StormX.FaceChange("perplexed", 1)
                    ch_s "If that's what you want. . ."
                else:
                    call Display_DressScreen(StormX)
                    if not _return:
                            ch_s "I'm afraid I couldn't."
                            return #jump Storm_Clothes
                $ StormX.Over = "towel"

        "Never mind":
            pass
    return #jump Storm_Clothes
    #End of Storm Top

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Storm_NoBra:
        menu:
            ch_s "I don't have much on under this. . ."
            "Then you could slip something on under it. . .":
                        if StormX in Rules or StormX.Taboo < 20 :
                                ch_s "No, I suppose it's fine, for now at least."
                        elif StormX.SeenChest and ApprovalCheck(StormX, 1000, TabM=3):
                                $ StormX.Blush = 2
                                ch_s "I truly don't mind though. . ."
                                $ StormX.Blush = 0
#                        elif ApprovalCheck(StormX, 1200, TabM=4):
#                                $ StormX.Blush = 1
#                                ch_s "-I didn't say that I minded. . ."
#                                $ StormX.Blush = 0
                        elif ApprovalCheck(StormX, 900, TabM=2) and "lace bra" in StormX.Inventory:
                                ch_s "Fine."
                                $ StormX.Chest  = "lace bra"
                                "She pulls out her lace bra and slips it under her [StormX.Over]."
                        elif ApprovalCheck(StormX, 700, TabM=2) and "corset" in StormX.Inventory:
                                ch_s "Fine."
                                $ StormX.Chest  = "black bra"
                                "She pulls out her black bra and slips it under her [StormX.Over]."
                        elif ApprovalCheck(StormX, 600, TabM=2):
                                ch_s "Fine."
                                $ StormX.Chest = "tube top"
                                "She pulls out her tube top and slips it on under her [StormX.Over]."
                        else:
                                ch_s "I don't think it would be appropriate."
                                return 0

            "You could always just wear nothing at all. . .":
                        if StormX in Rules or not StormX.Taboo:
                                ch_s "I suppose it's fine, for now at least."
                        elif ApprovalCheck(StormX, 1100, "LI", TabM=2) and StormX.Love > StormX.Inbt:
                                ch_s "For you? I suppose. . ."
                        elif ApprovalCheck(StormX, 700, "OI", TabM=2) and StormX.Obed > StormX.Inbt:
                                ch_s "Fine. . ."
                        elif ApprovalCheck(StormX, 600, "I", TabM=2):
                                ch_s "Yes. . ."
                        elif ApprovalCheck(StormX, 1300, TabM=2):
                                ch_s "Okay, fine."
                        else:
                                $ StormX.FaceChange("sadside")
                                if StormX.Taboo > 20:
                                    ch_s "Not in public, I'm afraid"
                                else:
                                    ch_s "I'm afraid not, [StormX.Petname]!"
                                return 0
            "Never mind.":
                        ch_s "Ok. . ."
                        return 0
        return 1
        #End of Storm bra check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Storm_Clothes_Legs:
        # Leggings
        "Maybe go without the [StormX.Legs]." if StormX.Legs:
                $ StormX.FaceChange("sexy", 1)
                if StormX.Taboo <= 20 or StormX.HoseNum() >= 5 or StormX.PantiesNum() >= 5 or StormX in Rules:
                    ch_s "Fine."
#                elif StormX.SeenPanties and StormX.Panties and ApprovalCheck(StormX, 500, TabM=5):
#                    ch_s "Ok, sure."
#                elif StormX.SeenPussy and ApprovalCheck(StormX, 900, TabM=4):
#                    ch_s "Yeah, ok."
                elif ApprovalCheck(StormX, 1300, TabM=2) and StormX.Panties:
                    ch_s "For you, fine. . ."
                elif ApprovalCheck(StormX, 700) and not StormX.Panties:
                    call Storm_NoPantiesOn
                    if not _return and not StormX.Panties:
                        if not ApprovalCheck(StormX, 1500):
                            call Display_DressScreen(StormX)
                            if not _return:
                                return #jump Storm_Clothes
                        else:
                                return #jump Storm_Clothes
                else:
                    call Display_DressScreen(StormX)
                    if not _return:
#                        ch_s "Um, not with you around."
                        if not StormX.Panties:
                                ch_s "I'm not wearing panties today. . ."
                        return #jump Storm_Clothes

                if StormX.Legs == "pants" or StormX.Legs == "yoga pants":
                        $ StormX.Legs = 0
                        "She tugs her pants off and drops them to the ground."
                else:
                        $ StormX.Legs = 0
                        "She tugs her skirt off and drops it to the ground."
                if renpy.showing('DressScreen'):
                    pass
                elif StormX.Panties:
                    $ StormX.SeenPanties = 1
                else:
                    call Storm_First_Bottomless

        "You look great in those black pants." if StormX.Legs != "pants":
                ch_s "Ok, one moment. . ."
                $ StormX.Legs = "pants"

        "You look great in those yoga pants." if StormX.Legs != "yoga pants":
                ch_s "Ok, one moment. . ."
                $ StormX.Legs = "yoga pants"

        "What about wearing your purple skirt?" if StormX.Legs != "skirt":
                ch_s "Ok, one moment. . ."
                $ StormX.Legs = "skirt"

        "Never mind":
                pass
    return #jump Storm_Clothes
    #End of Storm Pants

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Storm_NoPantiesOn:
        menu:
            ch_s "I am not wearing panties today."
            "Then you could slip on a pair of panties. . .":
                        if StormX.Taboo <= 20 or StormX.HoseNum() >= 5 or StormX in Rules:
                                ch_s "No, it's fine."
                        elif StormX.SeenPussy and ApprovalCheck(StormX, 1100, TabM=4):
                                $ StormX.Blush = 1
                                ch_s "No, commando's fine. . ."
                                $ StormX.Blush = 0
#                        elif ApprovalCheck(StormX, 1500, TabM=4):
#                                $ StormX.Blush = 1
#                                ch_s "No, commando's fine. . ."
#                                $ StormX.Blush = 0
                        elif ApprovalCheck(StormX, 700, TabM=4):
                                ch_s "Fine."
                                if "lace panties" in StormX.Inventory:
                                        $ StormX.Panties  = "lace panties"
                                else:
                                        $ StormX.Panties = "black panties"
                                if ApprovalCheck(StormX, 1200, TabM=4):
                                    $ Line = StormX.Legs
                                    $ StormX.Legs = 0
                                    "She pulls off her [Line] and slips on the [StormX.Panties]."
                                elif StormX.Legs == "skirt":
                                    "She pulls out her [StormX.Panties] and pulls them up under her skirt."
                                    $ StormX.Legs = 0
                                    "Then she drops the skirt to the floor."
                                else:
                                    $ Line = StormX.Legs
                                    $ StormX.Legs = 0
                                    "She steps away a moment and then comes back wearing only the [StormX.Panties]."
                                return #jump Storm_Clothes
                        else:
                                ch_s "No, thank you."
                                return 0

            "You could always just wear nothing at all. . .":
                        if StormX.Taboo <= 20 or StormX.HoseNum() >= 5 or StormX in Rules:
                                ch_s "True."
                        elif ApprovalCheck(StormX, 1100, "LI", TabM=3) and StormX.Love > StormX.Inbt:
                                ch_s "True. . ."
                        elif ApprovalCheck(StormX, 700, "OI", TabM=3) and StormX.Obed > StormX.Inbt:
                                ch_s "Yes. . ."
                        elif ApprovalCheck(StormX, 600, "I", TabM=3):
                                ch_s "Hrmm. . ."
                        elif ApprovalCheck(StormX, 1300, TabM=3):
                                ch_s "Fine."
                        else:
                                $ StormX.FaceChange("bemused")
                                if StormX.Taboo > 20:
                                    ch_s "Obviously, but not in public, [StormX.Petname]."
                                else:
                                    ch_s "I'm afraid not, [StormX.Petname]!"
                                return 0

            "Never mind.":
                ch_s "Ok. . ."
                return 0
        return 1
        #End of Storm Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Storm_Clothes_Under:
        "Tops":
            menu:
                "How about you lose the [StormX.Chest]?" if StormX.Chest:
                        $ StormX.FaceChange("bemused", 1)

                        if StormX.Taboo <= 20 or StormX in Rules or StormX.OverNum() >= 5:
                                ch_s "Fine."
                        elif StormX.SeenChest and ApprovalCheck(StormX, 900, TabM=2.7):
                            ch_s "Fine."
#                        elif ApprovalCheck(StormX, 1100, TabM=2):
#                            if StormX.Taboo:
#                                ch_s "I don't know, here. . ."
#                            else:
#                                ch_s "Maybe. . ."
                        elif StormX.Over == "jacket" and ApprovalCheck(StormX, 600, TabM=2):
                            ch_s "This jacket is a bit revealing. . ."
#                        elif StormX.Over and ApprovalCheck(StormX, 500, TabM=2):
#                            ch_s "I guess I could. . ."
                        elif not StormX.Over:
                            call Display_DressScreen(StormX)
                            if not _return:
                                ch_s "I'd have to wear something else over it."
                                return #jump Storm_Clothes
                        else:
                            call Display_DressScreen(StormX)
                            if not _return:
                                ch_s "I'm afraid not."
                                return #jump Storm_Clothes
                        $ Line = StormX.Chest
                        $ StormX.Chest = 0
                        if StormX.Over:
                            "She reaches under her [StormX.Over] grabs her [Line], and pulls it off, dropping it to the ground."
                        else:
                            "She pulls off her [Line] and drops it to the ground."
                            if not renpy.showing('DressScreen'):
                                call Storm_First_Topless


                "Try on that tube top." if StormX.Chest != "tube top":
                        ch_s "Fine."
                        $ StormX.Chest = "tube top"

                "Try on that sports bra." if StormX.Chest != "sports bra":
                        ch_s "Fine."
                        $ StormX.Chest = "sports bra"

                "I like that black bra." if StormX.Chest != "black bra":
                        if StormX.Taboo <= 20 or StormX in Rules or StormX.OverNum() >= 5:
                            ch_s "Fine."
                            $ StormX.Chest = "black bra"
                        elif StormX.SeenChest or ApprovalCheck(StormX, 1100, TabM=2):
                            ch_s "Fine."
                            $ StormX.Chest = "black bra"
                        else:
                            call Display_DressScreen(StormX)
                            if not _return:
                                ch_s "It's a bit minimal. . ."
                            else:
                                $ StormX.Chest = "black bra"

                "I like that lace bra." if StormX.Chest != "lace bra" and "lace bra" in StormX.Inventory:
                        if StormX.Taboo <= 20 or StormX in Rules or StormX.OverNum() >= 5:
                            ch_s "Fine."
                            $ StormX.Chest = "lace bra"
                        elif StormX.SeenChest or ApprovalCheck(StormX, 1300, TabM=2):
                            ch_s "Fine."
                            $ StormX.Chest = "lace bra"
                        else:
                            call Display_DressScreen(StormX)
                            if not _return:
                                ch_s "It's a bit sheer. . ."
                            else:
                                $ StormX.Chest = "lace bra"

                "I like that bikini top." if StormX.Chest != "bikini top" and "bikini top" in StormX.Inventory:
                        if bg_current == "bg pool":
                                ch_s "Fine."
                                $ StormX.Chest = "bikini top"
                        else:
                                if StormX.Taboo <= 20 or StormX in Rules or StormX.OverNum() >= 5:
                                    ch_s "Fine."
                                    $ StormX.Chest = "bikini top"
                                elif StormX.SeenChest or ApprovalCheck(StormX, 1000, TabM=2):
                                    ch_s "Fine."
                                    $ StormX.Chest = "bikini top"
                                else:
                                    call Display_DressScreen(StormX)
                                    if not _return:
                                            ch_s "This is not really a \"bikini\" sort of place. . ."
                                    else:
                                            $ StormX.Chest = "bikini top"

                "I like that top you had at the party." if StormX.Chest != "cos bra" and "halloween" in StormX.History:
                        if StormX.Taboo <= 20 or StormX in Rules or StormX.OverNum() >= 5:
                            ch_s "Fine."
                            $ StormX.Chest = "cos bra"
                        elif StormX.SeenChest or ApprovalCheck(StormX, 1100, TabM=2):
                            ch_s "Fine."
                            $ StormX.Chest = "cos bra"
                        else:
                            call Display_DressScreen(StormX)
                            if not _return:
                                ch_s "It's a bit minimal. . ."
                            else:
                                $ StormX.Chest = "cos bra"

                "Never mind":
                        pass
            return #jump Storm_Clothes_Under

        "Hose and stockings options":
            menu:
                "You could lose the hose." if StormX.Hose and StormX.Hose != 'ripped tights' and StormX.Hose != 'tights':
                                $ StormX.Hose = 0
                "The thigh-high hose would look good with that." if StormX.Hose != "stockings":
                                $ StormX.Hose = "stockings"
                "The pantyhose would look good with that." if StormX.Hose != "pantyhose":
                                $ StormX.Hose = "pantyhose"
                "The ripped pantyhose would look good with that." if StormX.Hose != "ripped pantyhose" and "ripped pantyhose" in StormX.Inventory:
                                $ StormX.Hose = "ripped pantyhose"
                "The stockings and garterbelt would look good with that." if StormX.Hose != "stockings and garterbelt" and "stockings and garterbelt" in StormX.Inventory:
                                $ StormX.Hose = "stockings and garterbelt"
                "Just the garterbelt would look good with that." if StormX.Hose != "garterbelt" and "stockings and garterbelt" in StormX.Inventory:
                                $ StormX.Hose = "garterbelt"
                "Never mind":
                        pass
            return #jump Storm_Clothes_Under

        #Panties
        "Panties":
            menu:
                "You could lose those panties. . ." if StormX.Panties:
                        $ StormX.FaceChange("bemused", 1)
                        if StormX.Taboo <= 20 or StormX.HoseNum() >= 5 or StormX.PantsNum() >= 5 or StormX in Rules:
                                ch_s "Sure."
#                        elif ApprovalCheck(StormX, 900) and (StormX.Legs or (StormX.SeenPussy and not StormX.Taboo)):
#                                #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
#                                if ApprovalCheck(StormX, 850, "L"):
#                                        ch_s "True. . ."
#                                elif ApprovalCheck(StormX, 500, "O"):
#                                        ch_s "Agreed."
#                                elif ApprovalCheck(StormX, 350, "I"):
#                                        ch_s "Heh."
#                                else:
#                                        ch_s "Sure, I guess."
                        else:                       #low approval or not wearing pants or in public
                                if ApprovalCheck(StormX, 1100, "LI", TabM=3) and StormX.Love > StormX.Inbt:
                                        ch_s "I suppose I could, but. . ."
                                elif ApprovalCheck(StormX, 700, "OI", TabM=3) and StormX.Obed > StormX.Inbt:
                                        ch_s "Well. . ."
                                elif ApprovalCheck(StormX, 600, "I", TabM=3):
                                        ch_s "Hrmm. . ."
                                elif ApprovalCheck(StormX, 1300, TabM=3):
                                        ch_s "Okay, okay."
                                else:
                                        call Display_DressScreen(StormX)
                                        if not _return:
                                            $ StormX.FaceChange("bemused")
                                            if StormX.Taboo >= 20:
                                                ch_s "Obviously, but not in public, [StormX.Petname]."
                                            else:
                                                ch_s "I'm afraid not, [StormX.Petname]!"
                                            return #jump Storm_Clothes
                        $ Line = StormX.Panties
                        $ StormX.Panties = 0
                        if not StormX.Legs:
                            "She pulls off her [Line], then drops them to the ground."
                            if not renpy.showing('DressScreen'):
                                    call Storm_First_Bottomless
                        elif ApprovalCheck(StormX, 1200, TabM=4):
                            $ Trigger = StormX.Legs
                            $ StormX.Legs = 0
                            pause 0.5
                            $ StormX.Legs = Trigger
                            "She pulls off her [StormX.Legs] and [Line], then pulls the [StormX.Legs] back on."
                            $ Trigger = 1
                            call Storm_First_Bottomless(1)
                        elif StormX.Legs == "skirt":
                            "She reaches under her skirt and pulls her [Line] off."
                        else:
                            $ StormX.Blush = 1
                            "She steps away a moment and then comes back."
                            $ StormX.Blush = 0
                        $ Line = 0

                "Why don't you wear the white panties instead?" if StormX.Panties and StormX.Panties != "white panties":
                        if StormX.Taboo <= 20 or StormX in Rules or StormX.PantsNum() >= 5:
                                ch_s "Fine."
                                $ StormX.Panties = "white panties"
                        elif ApprovalCheck(StormX, 1100, TabM=3):
                                ch_s "Ok."
                                $ StormX.Panties = "white panties"
                        else:
                                call Display_DressScreen(StormX)
                                if not _return:
                                        ch_s "That's really none of your busines."
                                else:
                                    $ StormX.Panties = "white panties"

                "Why don't you wear the black panties instead?" if StormX.Panties and StormX.Panties != "black panties":
                        if StormX.Taboo <= 20 or StormX in Rules or StormX.PantsNum() >= 5:
                                ch_s "Fine."
                                $ StormX.Panties = "black panties"
                        elif ApprovalCheck(StormX, 1100, TabM=3):
                                ch_s "Ok."
                                $ StormX.Panties = "black panties"
                        else:
                                call Display_DressScreen(StormX)
                                if not _return:
                                        ch_s "That's really none of your busines."
                                else:
                                    $ StormX.Panties = "black panties"

                "Why don't you wear the lace panties instead?" if "lace panties" in StormX.Inventory and StormX.Panties and StormX.Panties != "lace panties":
                        if StormX.Taboo <= 20 or StormX in Rules or StormX.PantsNum() >= 5:
                                ch_s "Fine."
                                $ StormX.Panties = "lace panties"
                        elif ApprovalCheck(StormX, 1300, TabM=3):
                                ch_s "I guess."
                                $ StormX.Panties = "lace panties"
                        else:
                                call Display_DressScreen(StormX)
                                if not _return:
                                        ch_s "That's really none of your busines."
                                else:
                                    $ StormX.Panties = "lace panties"

                "I like those bikini bottoms." if "bikini bottoms" in StormX.Inventory and StormX.Panties != "bikini bottoms":
                        if bg_current == "bg pool":
                                ch_s "Fine."
                                $ StormX.Panties = "bikini bottoms"
                        else:
                                if StormX.Taboo <= 20 or StormX in Rules or StormX.PantsNum() >= 5:
                                    ch_s "Fine."
                                    $ StormX.Panties = "bikini bottoms"
                                elif ApprovalCheck(StormX, 1000, TabM=2):
                                    ch_s "Fine."
                                    $ StormX.Panties = "bikini bottoms"
                                else:
                                    call Display_DressScreen(StormX)
                                    if not _return:
                                            ch_s "This is not really a \"bikini\" sort of place. . ."
                                    else:
                                            $ StormX.Panties = "bikini bottoms"

                "Why don't you wear those panties from the party?" if StormX.Panties and "halloween" in StormX.History and StormX.Panties != "cos panties":
                        if StormX.Taboo <= 20 or StormX in Rules or StormX.PantsNum() >= 5:
                                ch_s "Fine."
                                $ StormX.Panties = "cos panties"
                        elif ApprovalCheck(StormX, 1100, TabM=3):
                                ch_s "Ok."
                                $ StormX.Panties = "cos panties"
                        else:
                                call Display_DressScreen(StormX)
                                if not _return:
                                        ch_s "That's really none of your busines."
                                else:
                                    $ StormX.Panties = "cos panties"

                "You know, you could wear some panties with that. . ." if not StormX.Panties:
                        $ StormX.FaceChange("bemused", 1)
                        if StormX.Legs and (StormX.Love+StormX.Obed) <= (2 * StormX.Inbt):
                            $ StormX.Mouth = "smile"
                            ch_s "I don't know about that."
                            menu:
                                "Fine by me":
                                    return #jump Storm_Clothes
                                "I insist, put some on.":
                                    if (StormX.Love+StormX.Obed) <= (1.5 * StormX.Inbt):
                                        $ StormX.FaceChange("angry", Eyes="side")
                                        ch_s "Well I insist otherwise."
                                        return #jump Storm_Clothes
                                    else:
                                        $ StormX.FaceChange("sadside")
                                        ch_s "Oh, fine. . ."
                        else:
                            ch_s "Which?"
                        menu:
                            extend ""
                            "How about the white ones?":
                                    ch_s "Fine."
                                    $ StormX.Panties = "white panties"
                            "How about the black ones?":
                                    ch_s "Fine."
                                    $ StormX.Panties = "black panties"
                            "How about the lace ones?" if "lace panties" in StormX.Inventory:
                                    ch_s "Fine."
                                    $ StormX.Panties  = "lace panties"
                            "How about the bikini bottoms?" if "bikini bottoms" in StormX.Inventory:
                                    ch_s "Fine."
                                    $ StormX.Panties = "bikini bottoms"
                            "How about the costume ones?" if "halloween" in StormX.History:
                                    ch_s "Fine."
                                    $ StormX.Panties = "cos panties"
                "Never mind":
                    pass
            return #jump Storm_Clothes_Under
        "Never mind":
            pass
    return #jump Storm_Clothes
    #End of Storm Underwear

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Storm_Clothes_Misc:
        #Misc
        "Long hair style" if StormX.Hair != "long" and StormX.Hair != "wet":
                ch_p "You looked good with long hair."
                if "hair" in StormX.RecentActions:
                    ch_s "I have already messed with it too much today."
                elif ApprovalCheck(StormX, 900):
                    ch_s "Oh, you did?"
                    ch_s "I suppose I could speak to Hank about that. . ."
                    show blackscreen onlayer black
                    $ Round -5 if Round >= 10 else 0
                    "She steps away for a few minutes."
                    hide blackscreen onlayer black
                    if StormX.Hair == "wethawk":
                            $ StormX.Hair = "wet"
                    else:
                            $ StormX.Hair = "long"
                    $ StormX.AddWord(1,"hair","hair",0,0)
                    ch_s "Like this?"
                else:
                    ch_s "Thank you, but I'm not interested in that style right now."

        "Mohawk hair style" if "mohawk" in StormX.History and (StormX.Hair != "mohawk" and StormX.Hair != "wethawk"):
                ch_p "You looked good with a mohawk."
                if "hair" in StormX.RecentActions:
                    ch_s "I have already messed with it too much today."
                elif ApprovalCheck(StormX, 900):
                    ch_s "You liked it?"
                    show blackscreen onlayer black
                    $ Round -5 if Round >= 10 else 0
                    "She steps away for a few minutes."
                    hide blackscreen onlayer black
                    if StormX.Hair == "wet":
                            $ StormX.Hair = "wethawk"
                    else:
                            $ StormX.Hair = "mohawk"
                    $ StormX.AddWord(1,"hair","hair",0,0)
                    ch_s "Like this?"
                else:
                    ch_s "Thank you, but I'm not interested in that style right now."

        "Short hair style" if StormX.Hair != "short" and "halloween" in StormX.History:
                ch_p "You looked good with short hair."
                if "hair" in StormX.RecentActions:
                    ch_s "I have already messed with it too much today."
                elif ApprovalCheck(StormX, 900):
                    ch_s "Oh, you did?"
                    ch_s "I suppose I could speak to Hank about that. . ."
                    show blackscreen onlayer black
                    $ Round -5 if Round >= 10 else 0
                    "She steps away for a few minutes."
                    hide blackscreen onlayer black
                    $ StormX.Hair = "short"
                    $ StormX.AddWord(1,"hair","hair",0,0)
                    ch_s "Like this?"
                else:
                    ch_s "Thank you, but I'm not interested in that style right now."

        "Wet look hairstyle" if StormX.Hair != "wet" and StormX.Hair != "wethawk":
                ch_p "You should go for that wet look with your hair."
                if ApprovalCheck(StormX, 800):
                    ch_s "Really?"
                    if StormX.Hair == "mohawk":
                            $ StormX.Hair = "wethawk"
                    else:
                            $ StormX.Hair = "wet"
                    "A concentrated hurricane swirls around her head for a moment, leaving her hair limp."
                    ch_s "Like this?"
                else:
                    ch_s "I'd rather not."

        "Dry out hair" if StormX.Hair == "wet" or StormX.Hair == "wethawk":
                ch_p "Maybe dry out your hair."
                if ApprovalCheck(StormX, 600):
                    ch_s "Fine."
                    "A gust of wind swirls around her hair."
                    if StormX.Hair == "wethawk":
                            $ StormX.Hair = "mohawk"
                    else:
                            $ StormX.Hair = "long"
                else:
                    ch_s "I'm unsure, I think this is fine."

        "Grow pubes" if not StormX.Pubes:
                ch_p "You know, I like some nice hair down there. Maybe grow it out."
                if "pubes" in StormX.Todo:
                        $ StormX.FaceChange("bemused", 1)
                        ch_s "It's not as though it grows instantly!"
                else:
                        $ StormX.FaceChange("bemused", 1)
                        if ApprovalCheck(StormX, 500, TabM=0):
                            ch_s "I do prefer it that way. . ."
                        else:
                            $ StormX.FaceChange("surprised")
                            $ StormX.Brows = "angry"
                            ch_s "I do not need your advice."
                            return #jump Storm_Clothes
                        $ StormX.Todo.append("pubes")
                        $ StormX.PubeC = 6
        "Shave pubes" if StormX.Pubes == 1:
                ch_p "I like it waxed clean down there."
                $ StormX.FaceChange("bemused", 1)
                if "shave" in StormX.Todo:
                    ch_s "Yes, I will get around to it."
                else:
                    if ApprovalCheck(StormX, 1100, TabM=0):
                        ch_s "You do? I suppose I could shave. . ."
                    else:
                        $ StormX.FaceChange("surprised")
                        $ StormX.Brows = "angry"
                        ch_s "I think I will do what I want down there."
                        return #jump Storm_Clothes
                    $ StormX.Todo.append("shave")

#        "Piercings. [[See what she looks like without them first] (locked)" if not StormX.SeenPussy and not StormX.SeenChest:
#            pass

        "Add Ring Piercings" if StormX.Pierce != "ring": #and (StormX.SeenPussy or StormX.SeenChest):
                ch_p "You know, you'd look really nice with some ring body piercings."
                if "ring" in StormX.Todo:
                    ch_s "I know, I will do it."
                else:
                    $ StormX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(StormX, 1150, TabM=0)
                    if ApprovalCheck(StormX, 900, "L", TabM=0) or (Approval and StormX.Love > 2* StormX.Obed):
                        ch_s "You like the way they'd look on me?"
                    elif ApprovalCheck(StormX, 600, "I", TabM=0) or (Approval and StormX.Inbt > StormX.Obed):
                        ch_s "I have been considering that for a while."
                    elif ApprovalCheck(StormX, 500, "O", TabM=0) or Approval:
                        ch_s "Yes, [StormX.Petname]."
                    else:
                        $ StormX.FaceChange("bemused")
                        ch_s "I would rather not, [StormX.Petname]."
                        return #jump Storm_Clothes
                    $ StormX.Todo.append("ring")

        "Add barbell piercings." if StormX.Pierce != "barbell":# and (StormX.SeenPussy or StormX.SeenChest):
                ch_p "You know, you'd look really nice with some barbell body piercings."
                if "barbell" in StormX.Todo:
                    ch_s "I know, I will do it."
                else:
                    $ StormX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(StormX, 1150, TabM=0)
                    if ApprovalCheck(StormX, 900, "L", TabM=0) or (Approval and StormX.Love > 2 * StormX.Obed):
                        ch_s "You like the way they'd look on me?"
                    elif ApprovalCheck(StormX, 600, "I", TabM=0) or (Approval and StormX.Inbt > StormX.Obed):
                        ch_s "I have been considering that for a while."
                    elif ApprovalCheck(StormX, 500, "O", TabM=0) or Approval:
                        ch_s "Yes, [StormX.Petname]."
                    else:
                        $ StormX.FaceChange("bemused")
                        ch_s "I would rather not, [StormX.Petname]."
                        return #jump Storm_Clothes
                    $ StormX.Todo.append("barbell")

        "Remove Piercings" if StormX.Pierce:
                ch_p "You know, you'd look better without those piercings."
                $ StormX.FaceChange("bemused", 1)
                $ Approval = ApprovalCheck(StormX, 1350, TabM=0)
                if ApprovalCheck(StormX, 950, "L", TabM=0) or (Approval and StormX.Love > StormX.Obed):
                    ch_s "Really? Very well . ."
                elif ApprovalCheck(StormX, 700, "I", TabM=0) or (Approval and StormX.Inbt > StormX.Obed):
                    ch_s "Oh, I was growing rather attached. . ."
                elif ApprovalCheck(StormX, 600, "O", TabM=0) or Approval:
                    ch_s "Fine."
                else:
                    $ StormX.FaceChange("surprised")
                    $ StormX.Brows = "angry"
                    ch_s "I grown rather attached."
                    return #jump Storm_Clothes
                $ StormX.Pierce = 0

        "Add gold necklace" if StormX.Neck != "gold necklace":
                ch_p "Why don't you try on that gold necklace?"
                ch_s "Ok. . ."
                $ StormX.Neck = "gold necklace"
        "Add ring necklace" if StormX.Neck != "rings" and "halloween" in StormX.History:
                ch_p "Why don't you try on that ring necklace?"
                ch_s "Ok. . ."
                $ StormX.Neck = "rings"
        "Remove Necklace" if StormX.Neck:
                ch_p "Maybe go without a necklace."
                ch_s "Ok. . ."
                $ StormX.Neck = 0

        "Add Arm and Leg hoops." if StormX.Acc != "rings" and "halloween" in StormX.History:
                ch_p "Why don't you wear those body hoops?"
                ch_s "Ok. . ."
                $ StormX.Acc = "rings"
        "Remove Arm and Leg hoops." if StormX.Acc == "rings":
                ch_p "Why don't you take off those body hoops?"
                ch_s "Ok. . ."
                $ StormX.Acc = 0

#        "Why don't you put those wristbands on." if StormX.Arms != "wrists":
#                ch_s "Ok. . ."
#                $ StormX.Arms = "wrists"
#        "Maybe go without the wristbands." if StormX.Arms:
#                ch_s "Ok. . ."
#                $ StormX.Arms = 0

        "Never mind":
            pass
    return #jump Storm_Clothes
    #End of Storm Misc Wardrobe

return
#End Storm Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
