# star Jubes chat interface
#Jubes Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

label Jubes_Relationship: #rkeljsv
    while True:
        menu:
            ch_v "What did you want to talk about?"
            "Do you want to be my girlfriend?" if JubesX not in Player.Harem and "ex" not in JubesX.Traits:
                    $ JubesX.daily_history.append("relationship")
                    if "asked boyfriend" in JubesX.daily_history and "angry" in JubesX.daily_history:
                            $ JubesX.change_face("angry", 1)
                            ch_v "Like I said, not interested."
                            return
                    elif "asked boyfriend" in JubesX.daily_history:
                            $ JubesX.change_face("angry", 1)
                            ch_v "Still a no."
                            return
                    elif JubesX.Break[0]:
                            $ JubesX.change_face("angry", 1)
                            ch_v "I don't want to be with you."
                            if Player.Harem:
                                    $ JubesX.daily_history.append("asked boyfriend")
                                    return
                            else:
                                    ch_p "Not anymore, at least. . ."

                    $ JubesX.daily_history.append("asked boyfriend")

                    if Player.Harem and "JubesYes" not in Player.Traits:
                        if len(Player.Harem) >= 2:
                            ch_v "Well, you need to check in with the others first, [JubesX.Petname]."
                        else:
                            ch_v "Well, you need to check in with [Player.Harem[0].name] first, [JubesX.Petname]."
                        return

                    if JubesX.Event[5]:
                            $ JubesX.change_face("bemused", 1)
                            ch_v "You were the one that turned me down. . ."
                    else:
                            $ JubesX.change_face("surprised", 2)
                            ch_v "What? . ."
                            $ JubesX.change_face("smile", 1)

                    call Jubes_OtherWoman

                    if JubesX.love >= 800:
                            $ JubesX.change_face("surprised", 1)
                            $ JubesX.Mouth = "smile"
                            $ JubesX.change_stat("love", 200, 40)
                            ch_v "Sure!"
                            if "boyfriend" not in JubesX.Petnames:
                                    $ JubesX.Petnames.append("boyfriend")
                            if "JubesYes" in Player.Traits:
                                    $ Player.Traits.remove("JubesYes")
                            $ Player.Harem.append(JubesX)
                            call Harem_Initiation
                            "[JubesX.name] tackles you and kisses you deeply."
                            $ JubesX.change_face("kiss", 1)
                            $ JubesX.Kissed += 1
                    elif JubesX.obedience >= 500:
                            $ JubesX.change_face("perplexed")
                            ch_v "I don't know if I want to -date- you. . ."
                    elif JubesX.inhibition >= 500:
                            $ JubesX.change_face("smile")
                            ch_v "I just wanna have fun, ya know?"
                    else:
                            $ JubesX.change_face("perplexed", 1)
                            ch_v "Whoa, slow your roll, [JubesX.Petname]."

            "Do you want to get back together?" if "ex" in JubesX.Traits:
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

                    if Player.Harem and "JubesYes" not in Player.Traits:
                            if len(Player.Harem) >= 2:
                                ch_v "Well, you need to check in with the others first, [JubesX.Petname]."
                            else:
                                ch_v "Well, you need to check in with [Player.Harem[0].name] first, [JubesX.Petname]."
                            return

                    $ counter = 0
                    call Jubes_OtherWoman

                    if JubesX.love >= 800:
                            $ JubesX.change_face("surprised", 1)
                            $ JubesX.Mouth = "smile"
                            $ JubesX.change_stat("love", 90, 5)
                            ch_v "Ok, fine, we can give it a try."
                            if "boyfriend" not in JubesX.Petnames:
                                        $ JubesX.Petnames.append("boyfriend")
                            $ JubesX.Traits.remove("ex")
                            if "JubesYes" in Player.Traits:
                                    $ Player.Traits.remove("JubesYes")
                            $ Player.Harem.append(JubesX)
                            call Harem_Initiation
                            "[JubesX.name] pulls you in and kisses you deeply."
                            $ JubesX.change_face("kiss", 1)
                            $ JubesX.Kissed += 1
                    elif JubesX.love >= 600 and ApprovalCheck(JubesX, 1500):
                            $ JubesX.change_face("smile", 1)
                            $ JubesX.change_stat("love", 90, 5)
                            ch_v "Sure, I guess we can try it."
                            if "boyfriend" not in JubesX.Petnames:
                                $ JubesX.Petnames.append("boyfriend")
                            $ JubesX.Traits.remove("ex")
                            if "JubesYes" in Player.Traits:
                                    $ Player.Traits.remove("JubesYes")
                            $ Player.Harem.append(JubesX)
                            call Harem_Initiation
                            $ JubesX.change_face("kiss", 1)
                            "[JubesX.name] gives you a quick kiss."
                            $ JubesX.change_face("sly", 1)
                            $ JubesX.Kissed += 1
                    elif JubesX.obedience >= 500:
                            $ JubesX.change_face("sad")
                            ch_v "Nah, we gave it a shot."
                    elif JubesX.inhibition >= 500:
                            $ JubesX.change_face("perplexed")
                            ch_v "Nah, let's just keep it loose."
                    else:
                            $ JubesX.change_face("perplexed", 1)
                            ch_v "Nope, you blew it."

                    # End Back Together

            "I wanted to ask about [[another girl]" if JubesX in Player.Harem:
                            call AskDateOther

            "I think we should break up." if JubesX in Player.Harem:
                            if "breakup talk" in JubesX.daily_history:
                                    ch_v "Are you having a stroke?"
                            else:
                                    call Breakup(JubesX)

            "About that talk we had before. . .":
                menu:
                    "When you said you loved me. . ." if "lover" not in JubesX.Traits and JubesX.Event[6] >= 20 and JubesX.Event[6] != 23:
                            call Jubes_love_Redux

                    "When you were telling me all that stuff about yourself. . ." if "lover" not in JubesX.Traits and JubesX.Event[6] == 23:
                            call Jubes_love_Redux

                    "You said you wanted me to be more in control?" if "sir" not in JubesX.Petnames and "sir" in JubesX.History:
                            if "asked sub" in JubesX.daily_history:
                                    ch_v "We should give that a rest for today. . ."
                            else:
                                    call Jubes_Sub_Asked
                    "You said you wanted me to be your Master?" if "master" not in JubesX.Petnames and "master" in JubesX.History:
                            if "asked sub" in JubesX.daily_history:
                                    ch_v "We should give that a rest for today. . ."
                            else:
                                    call Jubes_Sub_Asked
                    "Never mind":
                            pass

            "Never Mind":
                return

    return

label Jubes_OtherWoman(counter = 0):
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return
    $ counter = int((JubesX.GirlLikeCheck(Player.Harem[0]) - 500)/2)

    $ JubesX.change_face("perplexed")
    if len(Player.Harem) >= 2:
        ch_v "You're with [Player.Harem[0].name] though, right? And a bunch of others too!"
    else:
        ch_v "You're with [Player.Harem[0].name] though, right?"
    menu:
        extend ""
        "She said I can be with you too." if "JubesYes" in Player.Traits:
                if ApprovalCheck(JubesX, 1800, Bonus = counter):
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
                    #This causes it to jump past the previous menu on the return

        "I could ask if she'd be ok with me dating you both." if "JubesYes" not in Player.Traits:
                if ApprovalCheck(JubesX, 1800, Bonus = counter):
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
                if not ApprovalCheck(JubesX, 1800, Bonus = -counter): #checks if Jubes likes you more than the other girl
                        $ JubesX.change_face("angry", 1)
                        if not ApprovalCheck(JubesX, 1800):
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
                        $ JubesX.Traits.append("downlow")

        "I can break it off with her.":
                    $ JubesX.change_face("sad")
                    ch_v "Do that, and get back to me."
                    $ renpy.pop_call()

        "You're right, I was dumb to ask.":
                    $ JubesX.change_face("sad")
                    ch_v "Ya'think?"
                    $ renpy.pop_call()

    return


label Jubes_About(Check=0): #rkeljsv
    if Check not in all_Girls:
            ch_v "Who?"
            return
    ch_v "What do I think about her? Well. . ."
    if Check == RogueX:
            if "poly Rogue" in JubesX.Traits:
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
            if "poly Kitty" in JubesX.Traits:
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
            if "poly Emma" in JubesX.Traits:
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
            if "poly Laura" in JubesX.Traits:
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
            if "poly Jean" in JubesX.Traits:
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
            if "poly Storm" in JubesX.Traits:
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
#End Jubes_AboutEmma

label Jubes_Monogamy:
        #called from Jubes_Settings to ask her not to hook up with other girls
        menu:
            "Could you not hook up with other girls?" if "mono" not in JubesX.Traits:
                    if JubesX.Thirst >= 60 and not ApprovalCheck(JubesX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ JubesX.change_face("sly",1)
                            if "mono" not in JubesX.daily_history:
                                    $ JubesX.change_stat("obedience", 90, -2)
                            ch_v "I could, but where would the fun in that be?"
                            return
                    elif ApprovalCheck(JubesX, 1200, "LO", TabM=0) and JubesX.love >= JubesX.obedience:
                            #she cares
                            $ JubesX.change_face("sly",1)
                            if "mono" not in JubesX.daily_history:
                                    $ JubesX.change_stat("love", 90, 1)
                            ch_v "Oh. . . want me for yourself?."
                            ch_v "Fine, I'll be more careful. . ."
                    elif ApprovalCheck(JubesX, 700, "O", TabM=0):
                            #she is obedient
                            $ JubesX.change_face("sly",1,Eyes="side")
                            ch_v "Sure."
                    else:
                            #she doesn't care
                            $ JubesX.change_face("sly",1)
                            ch_v "Nah."
                            return
                    if "mono" not in JubesX.daily_history:
                            $ JubesX.change_stat("obedience", 90, 3)
                    $ JubesX.AddWord(1,0,"mono") #Daily
                    $ JubesX.Traits.append("mono")
            "Don't hook up with other girls." if "mono" not in JubesX.Traits:
                    if ApprovalCheck(JubesX, 900, "O", TabM=0):
                            #she is obedient
                            $ JubesX.change_face("sly",1,Eyes="side")
                            ch_v "Fine."
                    elif JubesX.Thirst >= 60 and not ApprovalCheck(JubesX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ JubesX.change_face("sly",1)
                            if "mono" not in JubesX.daily_history:
                                    $ JubesX.change_stat("obedience", 90, -2)
                            ch_v "I could, but where would the fun in that be?"
                            return
                    elif ApprovalCheck(JubesX, 600, "O", TabM=0):
                            #she is obedient
                            $ JubesX.change_face("sly",1,Eyes="side")
                            ch_v "If you insist."
                    elif ApprovalCheck(JubesX, 1400, "LO", TabM=0):
                            #she cares
                            $ JubesX.change_face("sly",1)
                            ch_v "Yeah, ok, but ask nicely next time."
                    else:
                            #she doesn't care
                            $ JubesX.change_face("sly",1,Brows="confused")
                            ch_v "Nah."
                            return
                    if "mono" not in JubesX.daily_history:
                            $ JubesX.change_stat("obedience", 90, 3)
                    $ JubesX.AddWord(1,0,"mono") #Daily
                    $ JubesX.Traits.append("mono")
            "It's ok if you hook up with other girls." if "mono" in JubesX.Traits:
                    if ApprovalCheck(JubesX, 700, "O", TabM=0):
                            $ JubesX.change_face("sly",1,Eyes="side")
                            ch_v "Cool, cool."
                    elif ApprovalCheck(JubesX, 800, "L", TabM=0):
                            $ JubesX.change_face("sly",1)
                            ch_v "Ok, but make sure you make it up to me. . ."
                    else:
                            $ JubesX.change_face("sly",1,Brows="confused")
                            if "mono" not in JubesX.daily_history:
                                    $ JubesX.change_stat("love", 90, -2)
                            ch_v "Nice. . ."
                    if "mono" not in JubesX.daily_history:
                            $ JubesX.change_stat("obedience", 90, 3)
                    if "mono" in JubesX.Traits:
                            $ JubesX.Traits.remove("mono")
                    $ JubesX.AddWord(1,0,"mono") #Daily
            "Never mind.":
                pass
        return

# end Jubes monogamy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Jubes_Jumped:
        #called from Jubes_Settings to ask her not to jump you
        ch_p "Hey, Remember that time you threw yourself at me?"
        $ JubesX.change_face("sly",1,Brows="confused")
        menu:
            ch_v "Yeah?"
            "Could you maybe just ask instead?" if "chill" not in JubesX.Traits:
                    if JubesX.Thirst >= 60 and not ApprovalCheck(JubesX, 1500, "LO", TabM=0):
                            #she's too thirsty
                            $ JubesX.change_face("sly",1)
                            if "chill" not in JubesX.daily_history:
                                    $ JubesX.change_stat("obedience", 90, -2)
                            ch_v "Hey, better you than one of these other bloodbags. . ."
                            return
                    elif ApprovalCheck(JubesX, 1000, "LO", TabM=0) and JubesX.love >= JubesX.obedience:
                            #she cares
                            $ JubesX.change_face("surprised",1)
                            if "chill" not in JubesX.daily_history:
                                    $ JubesX.change_stat("love", 90, 1)
                            ch_v "Sorry, I. . . have needs. . ."
                            $ JubesX.change_face("sly",1,Eyes="side")
                            ch_v "I'll do better. . ."
                    elif ApprovalCheck(JubesX, 500, "O", TabM=0):
                            #she is obedient
                            $ JubesX.change_face("sly",1,Eyes="side")
                            ch_v "Sorry. . ."
                    else:
                            #she doesn't care
                            $ JubesX.change_face("sly",1)
                            ch_v "We'll see. . ."
                            return
                    if "chill" not in JubesX.daily_history:
                            $ JubesX.change_stat("obedience", 90, 3)
                    $ JubesX.AddWord(1,0,"chill") #Daily
                    $ JubesX.Traits.append("chill")
            "Don't bother me like that." if "chill" not in JubesX.Traits:
                    if ApprovalCheck(JubesX, 800, "O", TabM=0):
                            #she is obedient
                            $ JubesX.change_face("sly",1,Eyes="side")
                            ch_v "Fine."
                    elif JubesX.Thirst >= 60 and not ApprovalCheck(JubesX, 500, "O", TabM=0):
                            #she's too thirsty
                            $ JubesX.change_face("sly",1)
                            if "chill" not in JubesX.daily_history:
                                    $ JubesX.change_stat("obedience", 90, -2)
                            ch_v "Sorry, I. . . have needs. . ."
                            return
                    elif ApprovalCheck(JubesX, 400, "O", TabM=0):
                            #she is obedient
                            $ JubesX.change_face("sly",1,Eyes="side")
                            ch_v "Sure. . ."
                    elif ApprovalCheck(JubesX, 500, "LO", TabM=0) and not ApprovalCheck(JubesX, 500, "I", TabM=0):
                            #she cares
                            $ JubesX.change_face("sly",1)
                            ch_v "Hey, don't come at me like that."
                            ch_v "I can try though. . ."
                    else:
                            #she doesn't care
                            $ JubesX.change_face("sly",1)
                            ch_v "We'll see. . ."
                            return
                    if "chill" not in JubesX.daily_history:
                            $ JubesX.change_stat("obedience", 90, 3)
                    $ JubesX.AddWord(1,0,"chill") #Daily
                    $ JubesX.Traits.append("chill")
            "Knock yourself out.":
                    if ApprovalCheck(JubesX, 800, "L", TabM=0):
                            $ JubesX.change_face("sly",1)
                            ch_v "Game on. . ."
                    elif ApprovalCheck(JubesX, 700, "O", TabM=0):
                            $ JubesX.change_face("sly",1,Eyes="side")
                            ch_v "You got it!"
                    else:
                            $ JubesX.change_face("sly",1,Brows="confused")
                            if "chill" not in JubesX.daily_history:
                                    $ JubesX.change_stat("love", 90, -2)
                            ch_v "Yeah, we'll see. . ."
                    if "chill" not in JubesX.daily_history:
                            $ JubesX.change_stat("obedience", 90, 3)
                    if "chill" in JubesX.Traits:
                            $ JubesX.Traits.remove("chill")
                    $ JubesX.AddWord(1,0,"chill") #Daily
            "Um, never mind.":
                pass
        return

# end Jubes jumped <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# start jubilee hungry //////////////////////////////////////////////////////////
label Jubes_Hungry:
    if JubesX.Chat[3]:
        ch_v "[[licks her lips] I'm a little thirsty. . ."
    elif JubesX.Chat[2]:
        ch_v "I really love that serum you whipped up."
    else:
        ch_v "[[licks her lips] I'm a little thirsty. . ."
    $ JubesX.Traits.append("hungry")
return


# end jubilee hungry //////////////////////////////////////////////////////////

# Jubes Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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
                                        if JubesX.PlayerFav == "sex":
                                            $ JubesX.change_stat("lust", 80, 5)
                                            ch_v "Yeah, I know that. . ."
                                        elif JubesX.Favorite == "sex":
                                            $ JubesX.change_stat("love", 90, 5)
                                            $ JubesX.change_stat("lust", 80, 10)
                                            ch_v "I really like it too!"
                                        elif JubesX.Sex >= 5:
                                            ch_v "Well I don't mind that."
                                        elif not JubesX.Sex:
                                            $ JubesX.change_face("perplexed")
                                            ch_v "Who's fucking you?"
                                        else:
                                            $ JubesX.change_face("bemused")
                                            ch_v "Heh, um, yeah, it's nice. . ."
                                        $ JubesX.PlayerFav = "sex"

                            "Anal.":
                                        $ JubesX.change_face("sly")
                                        if JubesX.PlayerFav == "anal":
                                            $ JubesX.change_stat("lust", 80, 5)
                                            ch_v "So you've said. . ."
                                        elif JubesX.Favorite == "anal":
                                            $ JubesX.change_stat("love", 90, 5)
                                            $ JubesX.change_stat("lust", 80, 10)
                                            ch_v "I love it too!"
                                        elif JubesX.Anal >= 10:
                                            ch_v "Yeah, it's. . . nice. . ."
                                        elif not JubesX.Anal:
                                            $ JubesX.change_face("perplexed")
                                            ch_v "Who's fucking you?"
                                        else:
                                            $ JubesX.change_face("bemused",Eyes="side")
                                            ch_v "Heh, heh, yeah, um, it's ok. . ."
                                        $ JubesX.PlayerFav = "anal"

                            "Blowjobs.":
                                        $ JubesX.change_face("sly")
                                        if JubesX.PlayerFav == "blow":
                                            $ JubesX.change_stat("lust", 80, 3)
                                            ch_v "Definitely."
                                        elif JubesX.Favorite == "blow":
                                            $ JubesX.change_stat("love", 90, 5)
                                            $ JubesX.change_stat("lust", 80, 5)
                                            ch_v "Me too!"
                                        elif JubesX.Blow >= 10:
                                            ch_v "Yeah, you're delicious."
                                        elif not JubesX.Blow:
                                            $ JubesX.change_face("perplexed")
                                            ch_v "Who's sucking your dick?!"
                                        else:
                                            $ JubesX.change_face("bemused")
                                            ch_v "I'm. . . it's really good. . ."
                                        $ JubesX.PlayerFav = "blow"

                            "Titjobs.":
                                        $ JubesX.change_face("sly")
                                        if JubesX.PlayerFav == "titjob":
                                            $ JubesX.change_stat("lust", 80, 5)
                                            ch_v "Yeah, you've said that before. . ."
                                        elif JubesX.Favorite == "titjob":
                                            $ JubesX.change_stat("love", 90, 5)
                                            $ JubesX.change_stat("lust", 80, 7)
                                            ch_v "Yeah, I enjoy that too. . ."
                                        elif JubesX.Tit >= 10:
                                            ch_v "It's certainly an interesting experience . . ."
                                        elif not JubesX.Tit:
                                            $ JubesX.change_face("perplexed")
                                            ch_v "Who's titfucking you?"
                                        else:
                                            $ JubesX.change_face("bemused")
                                            ch_v "That's nice of you to say. . ."
                                            $ JubesX.change_stat("love", 80, 5)
                                            $ JubesX.change_stat("inhibition", 50, 10)
                                        $ JubesX.PlayerFav = "titjob"

                            "Footjobs.":
                                        $ JubesX.change_face("sly")
                                        if JubesX.PlayerFav == "foot":
                                            $ JubesX.change_stat("lust", 80, 5)
                                            ch_v "Yeah, you've said that. . ."
                                        elif JubesX.Favorite == "foot":
                                            $ JubesX.change_stat("love", 90, 5)
                                            $ JubesX.change_stat("lust", 80, 7)
                                            ch_v "I do like using my feet. . ."
                                        elif JubesX.Foot >= 10:
                                            ch_v "I like it too . . ."
                                        elif not JubesX.Foot:
                                            $ JubesX.change_face("perplexed")
                                            ch_v "Who's playing footsie with you?"
                                        else:
                                            $ JubesX.change_face("bemused")
                                            ch_v "Yeah, it's nice. . ."
                                        $ JubesX.PlayerFav = "foot"

                            "Handjobs.":
                                        $ JubesX.change_face("sly")
                                        if JubesX.PlayerFav == "hand":
                                            $ JubesX.change_stat("lust", 80, 5)
                                            ch_v "Yeah, you've said that. . ."
                                        elif JubesX.Favorite == "hand":
                                            $ JubesX.change_stat("love", 90, 5)
                                            $ JubesX.change_stat("lust", 80, 7)
                                            ch_v "You do feel pretty comfy. . ."
                                        elif JubesX.Hand >= 10:
                                            ch_v "I like it too . . ."
                                        elif not JubesX.Hand:
                                            $ JubesX.change_face("perplexed")
                                            ch_v "Who's jerking you off?"
                                        else:
                                            $ JubesX.change_face("bemused")
                                            ch_v "Yeah, it's nice. . ."
                                        $ JubesX.PlayerFav = "hand"

                            "Feeling you up.":
                                        $ counter = JubesX.FondleB + JubesX.FondleT + JubesX.SuckB + JubesX.Hotdog
                                        $ JubesX.change_face("sly")
                                        if JubesX.PlayerFav == "fondle":
                                            $ JubesX.change_stat("lust", 80, 3)
                                            ch_v "Yeah, I think we're clear on that. . ."
                                        elif JubesX.Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            $ JubesX.change_stat("love", 90, 5)
                                            $ JubesX.change_stat("lust", 80, 5)
                                            ch_v "I love when you touch me. . ."
                                        elif counter >= 10:
                                            ch_v "Yeah, it's really nice . . ."
                                        elif not counter:
                                            $ JubesX.change_face("perplexed")
                                            ch_v "Who's letting you feel her up?"
                                        else:
                                            $ JubesX.change_face("bemused")
                                            ch_v "I do like how that feels. . ."
                                        $ JubesX.PlayerFav = "fondle"
                                        $ counter = 0

                            "Kissing you.":
                                        $ JubesX.change_face("sly")
                                        if JubesX.PlayerFav == "kiss you":
                                            $ JubesX.change_stat("love", 90, 3)
                                            ch_v "Mmmmm. . ."
                                        elif JubesX.Favorite == "kiss you":
                                            $ JubesX.change_stat("love", 90, 5)
                                            $ JubesX.change_stat("lust", 80, 5)
                                            ch_v "Hmm, the taste of you on my lips. . ."
                                        elif JubesX.Kissed >= 10:
                                            ch_v "I love kissing you too . . ."
                                        elif not JubesX.Kissed:
                                            $ JubesX.change_face("perplexed")
                                            ch_v "Who are you kissing?"
                                        else:
                                            $ JubesX.change_face("bemused")
                                            ch_v "I love kissing you too. . ."
                                        $ JubesX.PlayerFav = "kiss you"

                        $ JubesX.daily_history.append("setfav")

                "What's your favorite thing to do?":
                                if not ApprovalCheck(JubesX, 800):
                                        $ JubesX.change_face("perplexed")
                                        ch_v ". . ."
                                else:
                                        if JubesX.SEXP >= 50:
                                            $ JubesX.change_face("sly")
                                            ch_v "You should know. . ."
                                        else:
                                            $ JubesX.change_face("bemused")
                                            $ JubesX.Eyes = "side"
                                            ch_v "Hmm. . ."


                                        if not JubesX.Favorite or JubesX.Favorite == "kiss":
                                                ch_v "Kissing?"
                                        elif JubesX.Favorite == "anal":
                                                ch_v "Probably anal."
                                        elif JubesX.Favorite == "lick ass":
                                                ch_v "When you lick my ass."
                                        elif JubesX.Favorite == "insert ass":
                                                ch_v "Fingering my asshole, probably."
                                        elif JubesX.Favorite == "sex":
                                                ch_v "Just the usual pounding."
                                        elif JubesX.Favorite == "lick pussy":
                                                ch_v "When you lick my pussy."
                                        elif JubesX.Favorite == "fondle pussy":
                                                ch_v "When you finger me."
                                        elif JubesX.Favorite == "blow":
                                                ch_v "I -love- how your cock tastes."
                                        elif JubesX.Favorite == "tit":
                                                ch_v "When I use my tits."
                                        elif JubesX.Favorite == "foot":
                                                ch_v "Footjobs are pretty fun."
                                        elif JubesX.Favorite == "hand":
                                                ch_v "I like jerking you off."
                                        elif JubesX.Favorite == "hotdog":
                                                ch_v "When you grind against me."
                                        elif JubesX.Favorite == "suck breasts":
                                                ch_v "When you suck my tits."
                                        elif JubesX.Favorite == "fondle breasts":
                                                ch_v "When you grab my tits."
                                        elif JubesX.Favorite == "fondle thighs":
                                                ch_v "When you rub my thighs."
                                        else:
                                                ch_v "How should I know?"

                                # End Jubes's favorite things.

                "Don't talk as much during sex." if "vocal" in JubesX.Traits:
                        if "setvocal" in JubesX.daily_history:
                                $ JubesX.change_face("perplexed")
                                ch_v "Make up your mind."
                        else:
                            if ApprovalCheck(JubesX, 1000) and JubesX.obedience <= JubesX.love:
                                $ JubesX.change_face("bemused")
                                $ JubesX.change_stat("obedience", 90, 1)
                                ch_v "Keep quiet, fine."
                                $ JubesX.Traits.remove("vocal")
                            elif ApprovalCheck(JubesX, 700, "O"):
                                $ JubesX.change_face("sadside")
                                $ JubesX.change_stat("obedience", 90, 1)
                                ch_v ". . ."
                                $ JubesX.Traits.remove("vocal")
                            elif ApprovalCheck(JubesX, 600):
                                $ JubesX.change_face("sly")
                                $ JubesX.change_stat("love", 90, -3)
                                $ JubesX.change_stat("obedience", 50, -1)
                                $ JubesX.change_stat("inhibition", 90, 5)
                                ch_v "Don't push it, [JubesX.Petname]."
                            else:
                                $ JubesX.change_face("angry")
                                $ JubesX.change_stat("love", 90, -5)
                                $ JubesX.change_stat("obedience", 60, -3)
                                $ JubesX.change_stat("inhibition", 90, 10)
                                ch_v "Nah."

                            $ JubesX.daily_history.append("setvocal")
                "Talk dirty to me during sex." if "vocal" not in JubesX.Traits:
                        if "setvocal" in JubesX.daily_history:
                                $ JubesX.change_face("perplexed")
                                ch_v "Heard you the first time."
                        else:
                            if ApprovalCheck(JubesX, 1000) and JubesX.obedience <= JubesX.love:
                                $ JubesX.change_face("sly")
                                $ JubesX.change_stat("obedience", 90, 2)
                                ch_v "Louder? I can do loud. . ."
                                $ JubesX.Traits.append("vocal")
                            elif ApprovalCheck(JubesX, 700, "O"):
                                $ JubesX.change_face("sadside")
                                $ JubesX.change_stat("obedience", 90, 2)
                                ch_v "If 'ya want, [JubesX.Petname]."
                                $ JubesX.Traits.append("vocal")
                            elif ApprovalCheck(JubesX, 600):
                                $ JubesX.change_face("sly")
                                $ JubesX.change_stat("obedience", 90, 3)
                                ch_v "Sure?"
                                $ JubesX.Traits.append("vocal")
                            else:
                                $ JubesX.change_face("angry")
                                $ JubesX.change_stat("inhibition", 90, 5)
                                ch_v ". . ."

                            $ JubesX.daily_history.append("setvocal")
                        # End Jubes Dirty Talk

                "Don't do your own thing as much during sex." if "passive" not in JubesX.Traits:
                        if "initiative" in JubesX.daily_history:
                                $ JubesX.change_face("perplexed")
                                ch_v "Heard you the first time."
                        else:
                            if ApprovalCheck(JubesX, 1200) and JubesX.obedience <= JubesX.love:
                                $ JubesX.change_face("bemused")
                                $ JubesX.change_stat("obedience", 90, 1)
                                ch_v "Ok, you can take the lead. . ."
                                $ JubesX.Traits.append("passive")
                            elif ApprovalCheck(JubesX, 700, "O"):
                                $ JubesX.change_face("sadside")
                                $ JubesX.change_stat("obedience", 90, 1)
                                ch_v "I'll try to restrain myself. . ."
                                $ JubesX.Traits.append("passive")
                            elif ApprovalCheck(JubesX, 600):
                                $ JubesX.change_face("sly")
                                $ JubesX.change_stat("love", 90, -3)
                                $ JubesX.change_stat("obedience", 50, -1)
                                $ JubesX.change_stat("inhibition", 90, 5)
                                ch_v "Hm, no."
                            else:
                                $ JubesX.change_face("angry")
                                $ JubesX.change_stat("love", 90, -5)
                                $ JubesX.change_stat("obedience", 60, -3)
                                $ JubesX.change_stat("inhibition", 90, 10)
                                ch_v "Uh-huh. . ."

                            $ JubesX.daily_history.append("initiative")
                "Take more initiative during sex." if "passive" in JubesX.Traits:
                        if "initiative" in JubesX.daily_history:
                                $ JubesX.change_face("perplexed")
                                ch_v "Heard you the first time."
                        else:
                            if ApprovalCheck(JubesX, 1000) and JubesX.obedience <= JubesX.love:
                                $ JubesX.change_face("bemused")
                                $ JubesX.change_stat("obedience", 90, 1)
                                ch_v "I can take the lead. . ."
                                $ JubesX.Traits.remove("passive")
                            elif ApprovalCheck(JubesX, 700, "O"):
                                $ JubesX.change_face("sadside")
                                $ JubesX.change_stat("obedience", 90, 1)
                                ch_v "Sure, no problem."
                                $ JubesX.Traits.remove("passive")
                            elif ApprovalCheck(JubesX, 600):
                                $ JubesX.change_face("sly")
                                $ JubesX.change_stat("obedience", 90, 3)
                                ch_v "We'll see."
                                $ JubesX.Traits.remove("passive")
                            else:
                                $ JubesX.change_face("angry")
                                $ JubesX.change_stat("inhibition", 90, 5)
                                ch_v "Meh."

                            $ JubesX.daily_history.append("initiative")

                "About getting Jumped" if "jumped" in JubesX.History:
                            call Jubes_Jumped
                "About when you masturbate":
                            call NoFap(JubesX)

                "Never Mind" if line == "Yeah, what did you want to talk about?":
                            return
                "That's all." if line != "Yeah, what did you want to talk about?":
                            return
            if line == "Yeah, what did you want to talk about?":
                $ line = "Anything else?"
    return
# End Jubes Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


## Jubes Chitchat /////////////////// #Work in progress
label Jubes_Chitchat(O=0, Options = ["default","default","default"]):
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:

        if JubesX not in Digits:
                if ApprovalCheck(JubesX, 500, "L") or ApprovalCheck(JubesX, 250, "I"):
                    ch_v "Oh, here's my number, call me maybe."
                    $ Digits.append(JubesX)
                    return
                elif ApprovalCheck(JubesX, 250, "O"):
                    ch_v "If you need to call me, here's my number."
                    $ Digits.append(JubesX)
                    return

        if "hungry" not in JubesX.Traits and JubesX.Swallow >= 3 and JubesX.Loc == bg_current:  #She's swallowed a lot
                    call Jubes_Hungry
                    return

        if bg_current != "bg_restaurant" and bg_current != "HW Party" and (not Taboo or ApprovalCheck(JubesX, 800, "I")):
                    if JubesX.Loc == bg_current and JubesX.Thirst >= 30 and "refused" not in JubesX.daily_history and "quicksex" not in JubesX.daily_history:
                            $ JubesX.change_face("sly",1)
                            ch_v "Hey, did you. . . wanna do something?"
                            call Quick_Sex(JubesX)
                            return
#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
#        if PunishmentX and "caught chat" not in JubesX.daily_history:
#            $ Options.append("caught")
        if JubesX.Event[0] and "key" not in JubesX.Chat:
            $ Options.append("key")

        if "mandrill" in Player.Traits and "cologne chat" not in JubesX.daily_history:
            $ Options.append("mandrill")
        if "purple" in Player.Traits and "cologne chat" not in JubesX.daily_history:
            $ Options.append("purple")
        if "corruption" in Player.Traits and "cologne chat" not in JubesX.daily_history:
            $ Options.append("corruption")

        if "Jubes" not in JubesX.names:
            $ Options.append("jubes")

        if JubesX.Date >= 1 and bg_current != "bg_restaurant":
            #if you've dated before
            $ Options.append("dated")
#        if "cheek" in JubesX.daily_history and "cheek" not in JubesX.Chat:
#            #If you've touched her cheek today
#            $ Options.append("cheek")
        if JubesX.Kissed >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")

        if "vamp" in "contagious" not in JubesX.History:
            $ Options.append("contagious")
        if "dangerroom" in Player.daily_history:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
        if "showered" in JubesX.daily_history:
            #If you've caught Jubes showering today
            $ Options.append("showercaught")
        if "fondle breasts" in JubesX.daily_history or "fondle pussy" in JubesX.daily_history or "fondle ass" in JubesX.daily_history:
            #If you've fondled Jubes today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in JubesX.Inventory and "256 Shades of Grey" in JubesX.Inventory and "Avengers Tower Penthouse" in JubesX.Inventory:
            #If you've given Jubes the books
            if "book" not in JubesX.Chat:
                $ Options.append("booked")
        if "lace bra" in JubesX.Inventory or "lace panties" in JubesX.Inventory:
            #If you've given Jubes the lingerie
            if "lingerie" not in JubesX.Chat:
                $ Options.append("lingerie")
        if JubesX.Hand:
            #If Jubes's given a handjob
            $ Options.append("handy")
        if JubesX.Swallow:
            #If Jubes's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in JubesX.daily_history or "painted" in JubesX.daily_history:
            #If Jubes's been facialed
            $ Options.append("facial")
        if JubesX.Sleep:
            #If Jubes's slept over
            $ Options.append("sleep")
        if JubesX.CreamP or JubesX.CreamA:
            #If Jubes's been creampied
            $ Options.append("creampie")
        if JubesX.Sex or JubesX.Anal:
            #If Jubes's been sexed
            $ Options.append("sexed")
        if JubesX.Anal:
            #If Jubes's been analed
            $ Options.append("anal")

        if "seenpeen" in JubesX.History:
            $ Options.append("seenpeen")
        if "topless" in JubesX.History:
            $ Options.append("topless")
        if "bottomless" in JubesX.History:
            $ Options.append("bottomless")

#        if not JubesX.Chat[0] and JubesX.Sex:
#            $ Options.append("virgin")

#        if (bg_current == "bg_jubes" or bg_current == "bg_player") and "relationship" not in JubesX.daily_history:
#            if "lover" not in JubesX.Petnames and ApprovalCheck(JubesX, 900, "L"): # JubesX.Event[6]
#                $ Options.append("lover?")
#            elif "sir" not in JubesX.Petnames and ApprovalCheck(JubesX, 500, "O"): # JubesX.Event[7]
#                $ Options.append("sir?")
#            elif "daddy" not in JubesX.Petnames and ApprovalCheck(JubesX, 750, "L") and ApprovalCheck(JubesX, 500, "O") and ApprovalCheck(JubesX, 500, "I"): # JubesX.Event[5]
#                $ Options.append("daddy?")
#            elif "master" not in JubesX.Petnames and ApprovalCheck(JubesX, 900, "O"): # JubesX.Event[8]
#                $ Options.append("master?")
#            elif "sex friend" not in JubesX.Petnames and ApprovalCheck(JubesX, 500, "I"): # JubesX.Event[9]
#                $ Options.append("sexfriend?")
#            elif "fuck buddy" not in JubesX.Petnames and ApprovalCheck(JubesX, 900, "I"): # JubesX.Event[10]
#                $ Options.append("fuckbuddy?")


        if not ApprovalCheck(JubesX, 300):            #She dislikes you
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one

    if Options[0] == "mandrill":
        $ JubesX.daily_history.append("cologne chat")
        $ JubesX.change_face("confused")
        ch_v "(sniff, sniff). . . you smell like monkey butt . . ."
        ch_v ". . . why is that turning me on?"
        $ JubesX.change_face("sexy", 2)
    elif Options[0] == "purple":
        $ JubesX.daily_history.append("cologne chat")
        $ JubesX.change_face("sly",1)
        ch_v "(sniff, sniff). . . that's an unusual scent. . ."
        $ JubesX.change_face("normal",0)
        ch_v ". . . did you want something?"
    elif Options[0] == "corruption":
        $ JubesX.daily_history.append("cologne chat")
        $ JubesX.change_face("confused")
        ch_v "(sniff, sniff). . . that's. . . um, overpowering. . ."
        $ JubesX.change_face("angry")
        ch_v ". . . dangerous. . ."
        $ JubesX.change_face("sly")

    elif Options[0] == "caught": # Xavier's caught you
            if "caught chat" in JubesX.Chat:
                    ch_v "We should try not to get caught like that."
                    if not ApprovalCheck(JubesX, 500, "I"):
                         ch_v "Unless. . ."
            else:
                    ch_v "Sorry we got dragged into the Professor's office like that."
                    if not ApprovalCheck(JubesX, 500, "I"):
                        ch_v "I guess you wouldn't want to be so public anymore."
                    else:
                        ch_v "I kinda had fun though. . ."
                    $ JubesX.Chat.append("caught chat")
    elif Options[0] == "key": # you have her key
            if JubesX.SEXP <= 15:
                ch_v "Be careful when you use that key . ."
            else:
                ch_v "I gave you a key, but you don't visit. . ."
            $ JubesX.Chat.append("key")

#    elif Options[0] == "cheek":
#            #Jubes's response to having her cheek touched.
#            ch_v "So,[JubesX.Petname]. . .y'know how you[JubesX.like]kinda just brushed my cheek before?"
#            ch_p "Yeah?  Was that okay?"
#            $ JubesX.change_face("smile",1)
#            ch_v "More than just {i}okay{/i}."
#            $ JubesX.Chat.append("cheek")


    elif Options[0] == "contagious":
                        $ JubesX.change_face("sadside",2)
                        ch_v "Just so you know, the vampire thing. . ."
                        ch_v "It's not contagious. . ."
                        $ JubesX.change_face("sadside",1)
                        ch_v "It was, but Dr. Strange was able to cast a spell or something."
                        ch_v "So you don't need to worry about it spreading to you or anything."
                        $ JubesX.change_face("sad",1)
                        $ JubesX.AddWord(1,0,0,0,"contagious") #adds "word" tag to History

    elif Options[0] == "jubes":
            #if she never told you her name. . .
            ch_v "Oh, by the way, I also go by \"Jubes.\""
            ch_v "Thought you might wanna know that."
            $ JubesX.names.append("Jubes")
            $ JubesX.Pets.append("Jubes")
            menu:
                "Oh, that's cool, I think I'll call you that.":
                        $ JubesX.change_stat("love", 70, 5) # love
                        $ JubesX.name = "Jubes"
                "Ok, but I like [JubesX.name].":
                        $ JubesX.change_stat("love", 70, 2) # love
                        $ JubesX.change_stat("obedience", 70, 2) # obedience
                        $ JubesX.change_face("smile",1)
                        ch_v "Oh, ok."

    elif Options[0] == "dated":
            #Jubes's response to having gone on a date with the Player.
            ch_v "I liked going out, haven't had too many chances at that lately."

    elif Options[0] == "kissed":
            #Jubes's response to having been kissed by the Player.
            $ JubesX.change_face("sly",1)
            ch_v "You're a great kisser, [JubesX.Petname]."
            menu:
                extend ""
                "Hey. . .I'm the best there is at what I do.":
                        $ JubesX.change_face("smile",1)
                        ch_v "Well. . . maybe."
                        ch_v "We'll have to test that one out."
                "No. You think?":
                        ch_v "Would I have said it otherwise?"

    elif Options[0] == "dangerroom":
            #Jubes's response to Player working out in the Danger Room while Jubes is present
            $ JubesX.change_face("sly",1)
            ch_v "Hey,[JubesX.Petname]. I saw you in the Danger Room, earlier."
            ch_v "You're surprisingly good at this, considering you lack the ability to pewpew."

    elif Options[0] == "showercaught":
            #Jubes's response to being caught in the shower.
            if "shower" in JubesX.Chat:
                ch_v "You saw me showering again. . ."
            else:
                ch_v "hey. don't you check before entering the showers?"
                $ JubesX.Chat.append("shower")
                menu:
                    extend ""
                    "It was a total accident!  I promise!":
                            $ JubesX.change_stat("love", 50, 5)
                            $ JubesX.change_stat("love", 90, 2)
                            if ApprovalCheck(JubesX, 1200):
                                $ JubesX.change_face("sly",1)
                                ch_v "I didn't say I minded. . ."
                            $ JubesX.change_face("smile")
                            ch_v "Ok, sure, it's cool."
                    "Just with you.":
                            $ JubesX.change_stat("obedience", 40, 5)
                            if ApprovalCheck(JubesX, 1000) or ApprovalCheck(JubesX, 700, "L"):
                                    $ JubesX.change_stat("love", 90, 3)
                                    $ JubesX.change_face("sly",1)
                                    ch_v "Well I guess that's kinda sweet. . ."
                            else:
                                    $ JubesX.change_stat("love", 70, -5)
                                    $ JubesX.change_face("angry")
                                    ch_v "Well, cut it out!"
                    "Totally on purpose. I regret nothing.":
                            if ApprovalCheck(JubesX, 1200):
                                    $ JubesX.change_stat("love", 90, 3)
                                    $ JubesX.change_stat("obedience", 70, 10)
                                    $ JubesX.change_stat("inhibition", 50, 5)
                                    $ JubesX.change_face("sly",1)
                                    ch_v "Fair."
                            elif ApprovalCheck(JubesX, 800):
                                    $ JubesX.change_stat("obedience", 60, 5)
                                    $ JubesX.change_stat("inhibition", 50, 5)
                                    $ JubesX.change_face("perplexed",2)
                                    ch_v "Well, I guess I can't blame you. . ."
                                    $ JubesX.Blush = 1
                            else:
                                    $ JubesX.change_stat("love", 50, -10)
                                    $ JubesX.change_stat("love", 80, -10)
                                    $ JubesX.change_stat("obedience", 50, 10)
                                    $ JubesX.change_face("angry")
                                    ch_v "That's. . . off-putting. . ."

    elif Options[0] == "fondled":
            #Jubes's response to being felt up.
            ch_v "Hey, um, could you feel me up a little?"

    elif Options[0] == "booked":
            #Jubes's response after a Player gives her the books from the shop.
            ch_v "Hey, I read those books you gave me."
            menu:
                extend ""
                "Yeah?  Did you like them?":
                        $ JubesX.change_face("sly",2)
                        ch_v "Well. . . yeah, I guess. . ."
                "Good.  You looked like you could use to learn a thing or two from them.":
                        $ JubesX.change_stat("love", 90, -3)
                        $ JubesX.change_stat("obedience", 70, 5)
                        $ JubesX.change_stat("inhibition", 50, 5)
                        $ JubesX.change_face("sad")
                        ch_v "Well. . . I guess I could."
            $ JubesX.Blush = 1
            $ JubesX.Chat.append("book")

    elif Options[0] == "lingerie":
            #Jubes's response to being given lingerie.
            $ JubesX.change_face("sly",2)
            ch_v "That underwear you got me was pretty nice. . . thanks."
            $ JubesX.Blush = 1
            $ JubesX.Chat.append("lingerie")

    elif Options[0] == "handy":
            #Jubes's response after giving the Player a handjob.
            $ JubesX.change_face("sly",1)
            ch_v "I was daydreaming about having your cock in my hand. . ."
            ch_v "Maybe I should take it out of the dream. . ."
            $ JubesX.Blush = 0

    elif Options[0] == "blow":
            if "blow" not in JubesX.Chat:
                    #Jubes's response after giving the Player a blowjob.
                    $ JubesX.change_face("sly",2)
                    ch_v "Hey, I didn't bite or anything, did I?"
                    menu:
                        extend ""
                        "You were totally amazing.":
                                    $ JubesX.change_stat("love", 90, 5)
                                    $ JubesX.change_stat("inhibition", 60, 10)
                                    $ JubesX.change_face("normal",1)
                                    ch_v "Cool. Cool. . . "
                                    $ JubesX.change_face("sexy",1)
                                    ch_v "I'd like another taste sometime."
                        "Honestly? It was good. . .but you could use a little practice, I think.":
                                if ApprovalCheck(JubesX, 300, "I") or not ApprovalCheck(JubesX, 800):
                                    $ JubesX.change_stat("love", 90, -5)
                                    $ JubesX.change_stat("obedience", 60, 10)
                                    $ JubesX.change_stat("inhibition", 50, 10)
                                    $ JubesX.change_face("perplexed",1)
                                    ch_v "Oh! Sorry!."
                                else:
                                    $ JubesX.change_stat("obedience", 70, 15)
                                    $ JubesX.change_stat("inhibition", 50, 5)
                                    $ JubesX.change_face("sexy",1)
                                    ch_v "Yeah? Well, practice makes perfect. . ."
                        "I guess. If you're into weird sounds and too much teeth. Spoiler, I'm not.":
                                    $ JubesX.change_stat("love", 90, -5)
                                    $ JubesX.change_stat("obedience", 60, 5)
                                    $ JubesX.change_face("sad",2)
                                    ch_v "Well. . . sorry about that. . ."
                    $ JubesX.Blush = 1
                    $ JubesX.Chat.append("blow")
            else:
                    $ line = renpy.random.choice(["You know, your dick tastes great.",
                            "I think I nearly dislocated my jaw last time.",
                            "Lemme know if you want another blowjob sometime.",
                            "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
                    ch_v "[line]"

    elif Options[0] == "swallowed":
            #Jubes's response after swallowing the Player's cum.
            if "swallow" in JubesX.Chat:
                ch_v "I wouldn't mind another taste of your. . ."
            else:
                ch_v "So. . . the other day. . ."
                ch_v "I really got a charge out of drinking your. . ."
                $ JubesX.change_face("sly",1)
                ch_v "I wouldn't mind that again some time."
                $ JubesX.Chat.append("swallow")

    elif Options[0] == "facial":
            #Jubes's response after taking a facial from the Player.
            ch_v "Hey. . .I know this is kind of odd. . ."
            $ JubesX.change_face("sexy",2)
            ch_v "It does feel nice to wear your. . . jiz, but. . ."
            ch_v "Also kinda a waste?"
            $ JubesX.Blush = 1

    elif Options[0] == "sleepover":
            #Jubes's response after sleeping with the Player.
            ch_v "I really enjoyed the other night."
            ch_v "It felt nice spending the night with someone again."

    elif Options[0] == "creampie":
            #Another of Jubes's responses after having sex with the Player.
            "[JubesX.name] draws close to you so she can whisper into your ear."
            ch_v "I loved the feeling of having you cum inside me. . ."

    elif Options[0] == "sexed":
            #A final response from Jubes after having sex with the Player.
            ch_v "Hey, um. . ."
            $ JubesX.change_face("sexy",2)
            ch_v ". . .when I've been. . . enjoying myself. . ."
            ch_v "I've been thinking about you."
            $ JubesX.Blush = 1

    elif Options[0] == "anal":
            #Jubes's response after getting anal from the Player.
            $ JubesX.change_face("sly")
            ch_v "I hadn't really done much anal before. . ."
            $ JubesX.change_face("sexy",1)
            ch_v "Until you, at least."

    elif Options[0] == "seenpeen": # first seen peen skipped
            $ JubesX.change_face("sly",1, Eyes="down")
            ch_v "Oh, hey, you're swinging some real meat down there, huh?"
            $ JubesX.change_face("bemused",1)
            $ JubesX.change_stat("love", 50, 5)
            $ JubesX.History.remove("seenpeen")
    elif Options[0] == "topless": # first seen breasts skipped
            ch_v "Hey, so did you like my tits, or what?"
            call Jubes_First_TMenu
            $ JubesX.History.remove("topless")
    elif Options[0] == "bottomless": # first seen pussy skipped
            ch_v "Hey, so what'd you think when you first saw my. . . um. . ."
            ch_v "-my pussy. . ."
            call Jubes_First_BMenu
            $ JubesX.History.remove("bottomless")

#    elif Options[0] == "boyfriend?":
#        call Jubes_BF
#    elif Options[0] == "lover?":
#        call Jubes_love
#    elif Options[0] == "sir?":
#        call Jubes_Sub
#    elif Options[0] == "master?":
#        call Jubes_Master
#    elif Options[0] == "sexfriend?":
#        call Jubes_Sexfriend
#    elif Options[0] == "fuckbuddy?":
#        call Jubes_Fuckbuddy
#    elif Options[0] == "daddy?":
#        call Jubes_Daddy

    elif Options[0] == "hate": # trinty lower then 50:
        $ line = renpy.random.choice(["Get away from me.",
                "I don't want you anywhere near me.",
                "Back off.",
                "Fuck off."])
        ch_v "[line]"

    else: #all else fell through. . .
            $ D20 = renpy.random.randint(1, 21)
            if D20 == 1:
                    $ JubesX.change_face("smile")
                    ch_v "It's nice being able to get out more. . ."
#            elif D20 == 2:
#                    $ JubesX.change_face("annoyed")
#                    ch_v "If I have to hear him say \"I'm the best there is\" one more time, I swear I'm going ..."
#            elif D20 == 3:
#                    $ JubesX.change_face("surprised")
#                    ch_v "Huh? Oh, sorry. I sort of spaced out. That's not like me."
#            elif D20 == 4:
#                    $ JubesX.change_face("sad")
#                    ch_v "Oh, [JubesX.Petname]. I was just remembering something. Don't worry about it."
#            elif D20 == 5:
#                    $ JubesX.change_face("smile")
#                    ch_v "I had a good nap. It's nice to be somewhere I can just doze off without worry."
#            elif D20 == 6:
#                    $ JubesX.change_face("perplexed")
#                    ch_v "Oh, [JubesX.Petname]. I think I just saw Emma Frost staring at Cyclops. That's... wierd."
#            elif D20 == 7:
#                    $ JubesX.change_face("smile")
#                    ch_v "I just got a new personal best time in the Danger Room."
#            elif D20 == 8:
#                    $ JubesX.change_face("sad")
#                    ch_v "I like being here, but sometimes there's just so much noise..."
#            elif D20 == 9:
#                    $ JubesX.change_face("confused")
#                    ch_v "I'm still trying to figure out what the mystery meat in the cafeteria was today."
#                    ch_v "I have enhanced senses, this shouldn't be so difficult!"
#            elif D20 == 10:
#                    $ JubesX.change_face("smile")
#                    ch_v "Kitty, Rogue and some of the others asked me if I wanted to go grab some ice cream with them tomorrow."
#            elif D20 == 11:
#                    $ JubesX.change_face("smile")
#                    ch_v "I tried out a dance class like Kitty said. Apparently I'm good at it."
#            elif D20 == 12:
#                    $ JubesX.change_face("sad")
#                    ch_v "I like talking to Kitty and the others. It makes me feel, I don't know. . ."
#                    ch_v "{i}not{/i} like a really dangerous mutant who could kill everyone around me if I flipped out."
#            elif D20 == 13:
#                    $ JubesX.change_face("smile")
#                    ch_v "Kitty and Rogue dared me to call Logan \"Dad\". I think we might've given him a heart attack."
#            elif D20 == 14:
#                    $ JubesX.change_face("sad")
#                    ch_v "I like going out on missions, but catching up with what's been going on while I'm gone is always a pain."
#            elif D20 == 15:
#                    $ JubesX.change_face("perplexed")
#                    ch_v "So they're called the \"Avengers\", but do they ever do any avenging?"
#                    ch_v "At least the Fantastic Four really do things that are strange and fantastic."
#            elif D20 == 16:
#                    $ JubesX.change_face("perplexed")
#                    ch_v "Have you ever been to New York? Sometimes I'm surprised anyone still wants to live there."
#            elif D20 == 17:
#                    $ JubesX.change_face("perplexed")
#                    ch_v "Logan just walked up and told me that if I ever meet someone called. . ."
#                    ch_v "\"Dead...Poole?\"...I should just go ahead and stab him in the face."
#                    ch_v "What's up with that?"
#            elif D20 == 18:
#                    $ JubesX.change_face("smile")
#                    ch_v "Don't tell anyone this, but I think Cyclops is kind of wound up tight."
#            elif D20 == 19:
#                    $ JubesX.change_face("confused")
#                    ch_v "Do you smell something? Is that... nachos and... chocolate syrup?!"
#            elif D20 == 20:
#                    $ JubesX.change_face("smile")
#                    ch_v "I like being able to just talk about nothing in particular. It's... nice."
            else:
                    $ JubesX.change_face("smile")
                    ch_v "I like hanging with you."

    $ line = 0
    return

# start Jubes_Names//////////////////////////////////////////////////////////
label Jubes_Names:
    menu:
        ch_v "Oh? What would you like me to call you?"
        "My initial's fine.":
            $ JubesX.Petname = Player.name[:1]  #fix test this
            ch_v "You got it, [JubesX.Petname]."
        "Call me by my name.":
            $ JubesX.Petname = Player.name
            ch_v "If you want, [JubesX.Petname]."
        "Call me \"boyfriend\"." if "boyfriend" in JubesX.Petnames:
            $ JubesX.Petname = "boyfriend"
            ch_v "Sure thing, [JubesX.Petname]."
        "Call me \"lover\"." if "lover" in JubesX.Petnames:
            $ JubesX.Petname = "lover"
            ch_v "Oooh, love to, [JubesX.Petname]."
        "Call me \"sir\"." if "sir" in JubesX.Petnames:
            $ JubesX.Petname = "sir"
            ch_v "Yes, [JubesX.Petname]."
        "Call me \"master\"." if "master" in JubesX.Petnames:
            $ JubesX.Petname = "master"
            ch_v "As you wish, [JubesX.Petname]."
        "Call me \"sex friend\"." if "sex friend" in JubesX.Petnames:
            $ JubesX.Petname = "sex friend"
            ch_v "Heh, very fun, [JubesX.Petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in JubesX.Petnames:
            $ JubesX.Petname = "fuck buddy"
            ch_v "I'm game if you are, [JubesX.Petname]."
        "Call me \"daddy\"." if "daddy" in JubesX.Petnames:
            $ JubesX.Petname = "daddy"
            ch_v "Oh! You bet, [JubesX.Petname]."
        "Dude works.":
            $ JubesX.Petname = "dude"
            ch_v "You got it, dude."
        "Bro works." if "bro" in JubesX.Petnames:
            $ JubesX.Petname = "bro"
            ch_v "You got it, bro."
        "Nevermind.":
            return
    return
# end Jubes_Names//////////////////////////////////////////////////////////

label Jubes_Pet:
    while 1:
        menu:
            extend ""
            "Polite":
                menu:
                    "I think I'll call you. . ."
                    "Jubes.":
                        $ JubesX.Pet = "Jubes"
                        ch_v "I don't see why not, [JubesX.Petname]."

                    "Jubilee.":
                        $ JubesX.Pet = "Jubilee"
                        ch_v "I don't see why not, [JubesX.Petname]."

                    "Jubilation.":
                        $ JubesX.Pet = "Jubilation"
                        ch_v "I don't see why not, [JubesX.Petname]."

                    "\"girl\".":
                        $ JubesX.Pet = "girl"
                        if "boyfriend" in JubesX.Petnames or ApprovalCheck(JubesX, 600, "L"):
                            $ JubesX.change_face("sexy", 1)
                            ch_v "I'm totally your girl, [JubesX.Petname]."
                        else:
                            $ JubesX.change_face("angry")
                            ch_v "I am NOT your girl, [JubesX.Petname]."

                    "\"boo\".":
                        $ JubesX.Pet = "boo"
                        if "boyfriend" in JubesX.Petnames or ApprovalCheck(JubesX, 700, "L"):
                            $ JubesX.change_face("sexy", 1)
                            ch_v "I am your boo, [JubesX.Petname]."
                        else:
                            $ JubesX.change_face("angry")
                            ch_v "I'm NOT your boo,  [JubesX.Petname]."

                    "\"bae\".":
                        $ JubesX.Pet = "bae"
                        if "boyfriend" in JubesX.Petnames or ApprovalCheck(JubesX, 600, "L"):
                            $ JubesX.change_face("sexy", 1)
                            ch_v "I am your bae, [JubesX.Petname]."
                        else:
                            $ JubesX.change_face("angry")
                            ch_v "I'm NOT your bae,  [JubesX.Petname]."

                    "\"baby\".":
                        $ JubesX.Pet = "baby"
                        if "boyfriend" in JubesX.Petnames or ApprovalCheck(JubesX, 500, "L"):
                            $ JubesX.change_face("sexy", 1)
                            ch_v "Cute, [JubesX.Petname]."
                        else:
                            $ JubesX.change_face("angry")
                            ch_v "I am not your baby."


                    "\"sweetie\".":
                        $ JubesX.Pet = "sweetie"
                        if "boyfriend" in JubesX.Petnames or ApprovalCheck(JubesX, 600, "L"):
                            ch_v "Aw, that's sweet, [JubesX.Petname]."
                        else:
                            $ JubesX.change_face("angry", 1)
                            ch_v "Too sweet, [JubesX.Petname]."

                    "\"sexy\".":
                        $ JubesX.Pet = "sexy"
                        if "lover" in JubesX.Petnames or ApprovalCheck(JubesX, 800):
                            $ JubesX.change_face("sexy", 1)
                            ch_v "You know it, [JubesX.Petname]."
                        else:
                            $ JubesX.change_face("angry", 1)
                            ch_v "I don't know, [JubesX.Petname]."

                    "\"lover\".":
                        $ JubesX.Pet = "lover"
                        if "lover" in JubesX.Petnames or ApprovalCheck(JubesX, 1200):
                            $ JubesX.change_face("sexy", 1)
                            ch_v "I know."
                        else:
                            $ JubesX.change_face("angry", 1)
                            ch_v "I don't think so, [JubesX.Petname]."

                    "Back":
                        pass

            "Risky":
                menu:
                    "I think I'll call you. . ."
                    "\"slave\".":
                        $ JubesX.Pet = "slave"
                        if "master" in JubesX.Petnames or ApprovalCheck(JubesX, 800, "O"):
                            $ JubesX.change_face("bemused", 1)
                            ch_v "As you wish, [JubesX.Petname]."
                        else:
                            $ JubesX.change_face("angry", 1)
                            ch_v "I am not your slave, [JubesX.Petname]."

                    "\"pet\".":
                        $ JubesX.Pet = "pet"
                        if "master" in JubesX.Petnames or ApprovalCheck(JubesX, 650, "O"):
                            $ JubesX.change_face("bemused", 1)
                            ch_v "You can pet me if you want, [JubesX.Petname]."
                        else:
                            $ JubesX.change_face("angry", 1)
                            ch_v "I am no one's pet, [JubesX.Petname]."

                    "\"slut\".":
                        $ JubesX.Pet = "slut"
                        if "sex friend" in JubesX.Petnames or ApprovalCheck(JubesX, 900, "OI"):
                            $ JubesX.change_face("sexy")
                            ch_v "Fair enough."
                        else:
                            $ JubesX.change_face("angry", 1)
                            $ JubesX.Mouth = "surprised"
                            ch_v "Not with that mouth you don't."

                    "\"whore\".":
                        $ JubesX.Pet = "whore"
                        if "fuckbuddy" in JubesX.Petnames or ApprovalCheck(JubesX, 1000, "OI"):
                            $ JubesX.change_face("sly")
                            ch_v "Ouch. . ."
                        else:
                            $ JubesX.change_face("angry", 1)
                            ch_v "If either of us is going to be turning tricks. . ."

                    "\"sugartits\".":
                        $ JubesX.Pet = "sugartits"
                        if "sex friend" in JubesX.Petnames or ApprovalCheck(JubesX, 1400):
                            $ JubesX.change_face("sly", 1)
                            ch_v "Huh?"
                        else:
                            $ JubesX.change_face("angry", 1)
                            ch_v "Not cool."

                    "\"sex friend\".":
                        $ JubesX.Pet = "sex friend"
                        if "sex friend" in JubesX.Petnames or ApprovalCheck(JubesX, 600, "I"):
                            $ JubesX.change_face("sly")
                            ch_v "Yeah. . ."
                        else:
                            $ JubesX.change_face("angry", 1)
                            ch_v "Keep it down, [JubesX.Petname]."

                    "\"fuckbuddy\".":
                        $ JubesX.Pet = "fuckbuddy"
                        if "fuckbuddy" in JubesX.Petnames or ApprovalCheck(JubesX, 700, "I"):
                            $ JubesX.change_face("sly")
                            ch_v "Yup."
                        else:
                            $ JubesX.change_face("angry", 1)
                            $ JubesX.Mouth = "surprised"
                            ch_v "Not even, [JubesX.Petname]."

                    "\"baby girl\".":
                        $ JubesX.Pet = "baby girl"
                        if "daddy" in JubesX.Petnames or ApprovalCheck(JubesX, 1200):
                            $ JubesX.change_face("smile", 1)
                            ch_v "I guess?"
                        else:
                            $ JubesX.change_face("angry", 1)
                            ch_v "Weirdo."

                    "\"Miss Lee\"." if "Miss Lee" in JubesX.names:
                        $ JubesX.Pet = "Miss Lee"
                        if ApprovalCheck(JubesX, 900):
                            $ JubesX.change_face("bemused", 1)
                            ch_v "Ok, if that's what you're into, [JubesX.Petname]."
                        else:
                            $ JubesX.change_face("sad", 1)
                            ch_v "That's kinda. . . formal, [JubesX.Petname]."

                    "Back":
                        pass

            "Nevermind.":
                return
    return

#label Jubes_Namecheck(JubesX.Pet = JubesX.Pet, counter = 0, Ugh = 0): #replaced with $ Girl.nameCheck() #checks reaction to petname


# start Jubes_Rename//////////////////////////////////////////////////////////
label Jubes_Rename:
        #Sets alternate names from Jubes
        $ JubesX.Mouth = "smile"
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
                    if ApprovalCheck(JubesX, 900):
                        $ JubesX.change_face("bemused", 1)
                        ch_v "Ok, if that's what you're into, [JubesX.Petname]."
                    else:
                        $ JubesX.change_face("sad", 1)
                        ch_v "That's kinda. . . formal, [JubesX.Petname]."
            "Nevermind.":
                    pass
        $ JubesX.AddWord(1,0,"namechange")
        return
# end Jubes_Rename//////////////////////////////////////////////////////////


# start Jubes_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Jubes_Personality(counter = 0):
    if not JubesX.Chat[4] or counter:
        "Since you're doing well in one area, you can convince Jubes to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_v "Yeah? What's up?"
        "More obedienceient. [[love to obedienceience]" if JubesX.love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_v "If you really care about that, sure."
            $ JubesX.Chat[4] = 1
        "Less Inhibited. [[love to Inhibition]" if JubesX.love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_v "I could always be a bit more wild if that's what you want."
            $ JubesX.Chat[4] = 2

        "Less Inhibited. [[obedienceience to Inhibition]" if JubesX.obedience > 900:
            ch_p "I want you to be less inhibited."
            ch_v "I guess I could go all-out."
            $ JubesX.Chat[4] = 3
        "More Loving. [[obedienceience to love]" if JubesX.obedience > 900:
            ch_p "I'd like you to learn to love me."
            ch_v "I can try."
            $ JubesX.Chat[4] = 4

        "More obedienceient. [[Inhibition to obedienceience]" if JubesX.inhibition > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_v "I can give it a shot. . ."
            $ JubesX.Chat[4] = 5

        "More Loving. [[Inhibition to love]" if JubesX.inhibition > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_v "If that's something you need out of this. . ."
            $ JubesX.Chat[4] = 6

        "I guess just do what you like. . .[[reset]" if JubesX.Chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_v "Um, ok."
            $ JubesX.Chat[4] = 0
        "Repeat the rules":
            call Jubes_Personality(1)
            return
        "Nevermind.":
            return
    return
# end Jubes_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Jubes_Summon / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jubes_Summon(temp_modifier=temp_modifier):
    $ JubesX.OutfitChange()
    if "no summon" in JubesX.recent_history:
                if "angry" in JubesX.recent_history:
                    ch_v "Grrrrrrrrr."
                elif JubesX.recent_history.count("no summon") > 1:
                    ch_v "Back off!"
                    $ JubesX.recent_history.append("angry")
#                elif Current_Time == "Night":
#                    ch_v "Like I said, it's too late for that."
                else:
                    ch_v "Like I said, I'm busy."
                $ JubesX.recent_history.append("no summon")
                return

    $ D20 = renpy.random.randint(1, 20)
    $ line = 0
    if JubesX.Loc == "bg_classroom": #fix change these if changed function
        $ temp_modifier = -10
    elif JubesX.Loc == "bg_dangerroom":
        $ temp_modifier = -10
    elif JubesX.Loc == "bg_showerroom":
        $ temp_modifier = -30

    if D20 <= 3:
        #unlucky refusal
        $ line = "no"
#    if Current_Time == "Night":
#                if ApprovalCheck(JubesX, 500, "L") or ApprovalCheck(JubesX, 400, "O"):
#                        #It's night time but she likes you.
#                        ch_v "You're up too? Sure, we can hang."
#                        $ JubesX.Loc = bg_current
#                        call set_the_scene
#                else:
#                        #It's night time and she isn't into you
#                        ch_v "Nah."
#                        $ JubesX.recent_history.append("no summon")
#                return
    if "les" in JubesX.recent_history:
            #if she's with another girl. . .
            if ApprovalCheck(JubesX, 2000):
                    ch_v "I have another guest here right now, but I guess you can drop by. . ."
                    menu:
                        extend ""
                        "Sure":
                            $ line = "go to"
                        "No thanks.":
                            ch_v "Heh, your call."
                            return
            else:
                    ch_v "Oh, um, I kinda have a guest."
                    ch_v "I'll see you later, though?"
                    $ JubesX.recent_history.append("no summon")
                    return
    elif not ApprovalCheck(JubesX, 700, "L") or not ApprovalCheck(JubesX, 600, "O"):
        #It's not night time, but she's busy
        if not ApprovalCheck(JubesX, 300):
                ch_v "I'm kinda busy, [JubesX.Petname]."
                $ JubesX.recent_history.append("no summon")
                return


        if "summoned" in JubesX.recent_history:
                pass
        elif "goto" in JubesX.recent_history:
                ch_v "You just left!"
        elif JubesX.Loc == "bg_classroom":
                ch_v "I'm in class, did you want to come too?"
        elif JubesX.Loc == "bg_dangerroom":
                ch_v "I'm in the Danger Room, [JubesX.Petname], want in?"
        elif JubesX.Loc == "bg_campus":
                ch_v "I'm just enjoying the sun, want to come?"
        elif JubesX.Loc == "bg_jubes":
                ch_v "I'm in my room, [JubesX.Petname], did you wanna drop by?"
        elif JubesX.Loc == "bg_player":
                ch_v "I'm in your room, [JubesX.Petname], are you coming back?"
        elif JubesX.Loc == "bg_showerroom":
            if ApprovalCheck(JubesX, 1600):
                ch_v "I'm in the shower right now. Join me?"
            else:
                ch_v "I'm in the shower right now, [JubesX.Petname]. We can hang later."
                $ JubesX.recent_history.append("no summon")
                return
        elif JubesX.Loc == "hold":
                ch_v "I'm a little busy right now. Sorry?"
                $ JubesX.recent_history.append("no summon")
                return
        else:
                ch_v "Why don't you come to me?"

        if "summoned" in JubesX.recent_history:
                ch_v "Oh, you want me back so soon?"
                $ line = "yes"
        elif "goto" in JubesX.recent_history:
            menu:
                extend ""
                "You're right, be right back.":
                                ch_v "Cool, see you then."
                                $ line = "go to"
                "Nah, it's better here.":
                                ch_v "Ok, later then."
                "But I'd {i}really{/i} like to see you over here.":
                        if ApprovalCheck(JubesX, 600, "L") or ApprovalCheck(JubesX, 1400):
                                $ line = "lonely"
                        else:
                                $ line = "no"
                "I said come over here.":
                        if ApprovalCheck(JubesX, 600, "O"):
                                #she is obedient
                                $ line = "command"
                        elif D20 >= 7 and ApprovalCheck(JubesX, 1400):
                                #she is generally favorable
                                ch_v "Fine."
                                $ line = "yes"
                        elif ApprovalCheck(JubesX, 200, "O"):
                                #she is not obedient
                                ch_v "Whatever."
                                ch_v "I'll be here if you change your mind."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ line = "no"
        else:
            menu:
                extend ""
                "Sure, I'll be right there.":
                    $ JubesX.change_stat("love", 55, 1)
                    $ JubesX.change_stat("inhibition", 30, 1)
                    ch_v "Cool, see you then."
                    $ line = "go to"

                "Nah, we can talk later.":
                    $ JubesX.change_stat("obedience", 50, 1)
                    $ JubesX.change_stat("obedience", 30, 2)
                    ch_v "Ok. Later then."

                "Could you please come visit me? I'm lonely.":
                    if ApprovalCheck(JubesX, 650, "L") or ApprovalCheck(JubesX, 1500):
                        $ JubesX.change_stat("love", 70, 1)
                        $ JubesX.change_stat("obedience", 50, 1)
                        $ line = "lonely"
                    else:
                        $ JubesX.change_stat("inhibition", 30, 1)
                        $ line = "no"
                        ch_v "Aw, how could I say \"no\"?"

                "Come on, it'll be fun.":
                    if ApprovalCheck(JubesX, 400, "L") and ApprovalCheck(JubesX, 800):
                        $ JubesX.change_stat("love", 70, 1)
                        $ JubesX.change_stat("obedience", 50, 1)
                        $ line = "fun"
                    else:
                        $ JubesX.change_stat("inhibition", 30, 1)
                        $ line = "no"

                "I said come over here.":
                    if ApprovalCheck(JubesX, 600, "O"):
                        #she is obedient
                        $ JubesX.change_stat("love", 50, 1, 1)
                        $ JubesX.change_stat("love", 40, -1)
                        $ JubesX.change_stat("obedience", 90, 1)
                        $ line = "command"

                    elif D20 >= 7 and ApprovalCheck(JubesX, 1500):
                        #she is generally favorable
                        $ JubesX.change_stat("love", 70, -2)
                        $ JubesX.change_stat("love", 90, -1)
                        $ JubesX.change_stat("obedience", 50, 2)
                        $ JubesX.change_stat("obedience", 90, 1)
                        ch_v "Ok, fine."
                        $ line = "yes"

                    elif ApprovalCheck(JubesX, 200, "O"):
                        #she is not obedient
                        $ JubesX.change_stat("love", 60, -4)
                        $ JubesX.change_stat("love", 90, -3)
                        ch_v "No way."
                        $ JubesX.change_stat("inhibition", 40, 2)
                        $ JubesX.change_stat("inhibition", 60, 1)
                        $ JubesX.change_stat("obedience", 70, -3)
                        ch_v "I'm staying here."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ JubesX.change_stat("inhibition", 30, 1)
                        $ JubesX.change_stat("inhibition", 50, 1)
                        $ JubesX.change_stat("love", 50, -1, 1)
                        $ JubesX.change_stat("obedience", 70, -1)
                        $ line = "no"
                    #end "ordered"
    else:
        #automatic acceptance
        if JubesX.love > JubesX.obedience:
            ch_v "Sure!"
        else:
            ch_v "Cool, on my way."
        $ line = "yes"

    $ temp_modifier = 0

    if not line:
            #You end the dialog neutrally
            $ JubesX.recent_history.append("no summon")
            return

    if line == "no":
            # She's refused, context based dialog
            if JubesX.Loc == "bg_classroom":
                ch_v "I can't skip this lecture."
            elif JubesX.Loc == "bg_dangerroom":
                ch_v "I'm just getting into it."
            else:
                ch_v "Sorry, [JubesX.Petname], I'm kinda busy."
            $ JubesX.recent_history.append("no summon")
            return

    elif line == "go to":
            #You agreed to go to her instead
            $ renpy.pop_call()
            $ JubesX.recent_history.append("goto")
            $ Player.recent_history.append("goto")
            $ line = 0
            if JubesX.Loc == "bg_classroom":
                    ch_v "K, there's room next to me."
                    jump Class_Room
            elif JubesX.Loc == "bg_dangerroom":
                    ch_v "Don't be long. . ."
                    jump Danger_Room
            elif JubesX.Loc == "bg_jubes":
                    ch_v "I'll. . . get ready."
                    jump Jubes_Room
            elif JubesX.Loc == "bg_player":
                    ch_v "I'll be waiting."
                    jump Player_Room
            elif JubesX.Loc == "bg_showerroom":
                    ch_v "I'll leave you some hot water."
                    jump Shower_Room
            elif JubesX.Loc == "bg_campus":
                    ch_v "I'm still in the shade a bit. . ."
                    jump Campus
            elif JubesX.Loc in PersonalRooms:
                    ch_v "Yeah, see you."
                    $ bg_current = JubesX.Loc
                    jump Misplaced
            else:
                    ch_v "Um, I'll just meet you in my room."
                    $ JubesX.Loc = "bg_jubes"
                    jump Jubes_Room

    #She's agreed to come over
    elif line == "lonely":
            ch_v "Aw, well I can help with that!"
    elif line == "command":
            ch_v "Ok, [JubesX.Petname]."

    if bg_current not in PersonalRooms:
            call Jubes_Sunshock
            if _return:
                    #if she couldn't go out and refused, then head back.
                    $ JubesX.recent_history.append("no summon")
                    return

    $ JubesX.recent_history.append("summoned")
    $ line = 0
    if "locked" in Player.Traits:
            call Locked_Door(JubesX)
            return
    $ JubesX.Loc = bg_current
    call Taboo_Level(0)
    $ JubesX.OutfitChange()
    call set_the_scene
    return

label Jubes_Clothes:
    if JubesX.Taboo:
            if "exhibitionist" in JubesX.Traits:
                ch_v "Yes? . ."
            elif ApprovalCheck(JubesX, 900, TabM=4) or ApprovalCheck(JubesX, 400, "I", TabM=3):
                ch_v "It's pretty public here, I don't think so. . ."
            else:
                ch_v "It's pretty public here, I don't think so. . ."
                ch_v "Can't we talk about this in our rooms?"
                return
    elif ApprovalCheck(JubesX, 900, TabM=4) or ApprovalCheck(JubesX, 600, "L") or ApprovalCheck(JubesX, 300, "O"):
                ch_v "Oh, what were you thinking? . ."
    else:
                ch_v "I don't think I really need your fashion advice."
                return

    if Girl != JubesX or line == "Giftstore":
            #This culls returns if sent from another girl
            $ renpy.pop_call()
    $ line = 0
    $ Girl = JubesX
    call Shift_Focus(Girl)

label Jubes_Wardrobe_Menu:
    $ JubesX.change_face()
    $ primary_action = 1 # to prevent Focus swapping. . .
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
                        call Clothes_Schedule(JubesX)

            "Could I get a look at it?" if JubesX.Loc != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(JubesX,0,2)
                    if _return:
                        show PhoneSex zorder 150
                        ch_v "Ok, that good?"
                    hide PhoneSex
            "Could I get a look at it?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(JubesX,0,2)
                    if _return:
                        hide DressScreen
            "Would you be more comfortable behind a screen? (locked)" if JubesX.Taboo:
                    pass
            "Would you be more comfortable behind a screen?" if JubesX.Loc == bg_current and not JubesX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    if ApprovalCheck(JubesX, 1500) or (JubesX.SeenChest and JubesX.SeenPussy):
                            ch_v "I think I'm fine. . ."
                    else:
                            show DressScreen zorder 150
                            ch_v "Yeah, this is better, thanks."

            "Gift for you (locked)" if Girl.Loc != bg_current:
                            pass
            "Gift for you" if Girl.Loc == bg_current:
                            ch_p "I'd like to give you something."
                            call Gifts #(Girl)

            "Switch to. . .":
                    if renpy.showing('DressScreen'):
                            call OutfitShame(JubesX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ JubesX.OutfitChange()
                    $ JubesX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ primary_action = 0
                    call Switch_Chat
                    if Girl != JubesX:
                            ch_p "I wanted to talk about your clothes."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = JubesX
                    call Shift_Focus(Girl)

            "Never mind, you look good like that.":
                    if "wardrobe" not in JubesX.recent_history:
                            #Apply stat boosts only if it's the first time this turn
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
                            call OutfitShame(JubesX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ JubesX.OutfitChange()
                    $ JubesX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ JubesX.Chat[1] += 1
                    $ primary_action = 0
                    return

        #Loops back up
        #return #jump Jubes_Clothes
        #End of Jubes Wardrobe Main Menu

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Jubes_Clothes_Outfits:
        # Outfits
        "You should remember that one. [[Set Custom]":
                menu:
                    "Which slot would you like this saved in?"
                    "Custom 1":
                                call OutfitShame(JubesX,3,1)
                    "Custom 2":
                                call OutfitShame(JubesX,5,1)
                    "Custom 3":
                                call OutfitShame(JubesX,6,1)
                    "Gym Clothes":
                                call OutfitShame(JubesX,4,1)
                    "Sleepwear":
                                call OutfitShame(JubesX,7,1)
                    "Swimwear":
                                call OutfitShame(JubesX,10,1)
                    #8 is Emma's teaching clothes,
                    "Never mind":
                                pass

        "Red and blue outfit":
                $ JubesX.OutfitChange("casual1")
                menu:
                    "You should wear this one out. [[set current outfit]":
                            $ JubesX.Outfit = "casual1"
                            $ JubesX.Shame = 0
                            ch_v "Yeah, this one's a classic, right?"
                    "Let's try something else though.":
                            ch_v "Ok."

        "Black Leather combo":
                $ JubesX.OutfitChange("casual2")
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
                                $ JubesX.OutfitChange("custom1")
                                $ counter = 3
                        "Throw on Custom 2 (locked)" if not JubesX.Custom2[0]:
                                pass
                        "Throw on Custom 2" if JubesX.Custom2[0]:
                                $ JubesX.OutfitChange("custom2")
                                $ counter = 5
                        "Throw on Custom 3 (locked)" if not JubesX.Custom3[0]:
                                pass
                        "Throw on Custom 3" if JubesX.Custom3[0]:
                                $ JubesX.OutfitChange("custom3")
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
                                call Custom_Out(JubesX,counter)
                        "Ok, back to what we were talking about. . .":
                                $ counter = 0
                                return #jump Jubes_Clothes

        "Gym Clothes?" if not JubesX.Taboo or bg_current == "bg_dangerroom":
                $ JubesX.OutfitChange("gym")

        "Sleepwear?" if not JubesX.Taboo:
                if ApprovalCheck(JubesX, 1200):
                        $ JubesX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(JubesX)
                        if _return:
                            $ JubesX.OutfitChange("sleep")

        "Swimwear? (locked)" if (JubesX.Taboo and bg_current != "bg_pool") or not JubesX.Swim[0]:
                $ JubesX.OutfitChange("swimwear")
        "Swimwear?" if (not JubesX.Taboo or bg_current == "bg_pool") and JubesX.Swim[0]:
                $ JubesX.OutfitChange("swimwear")

        "Halloween Costume?" if "halloween" in JubesX.History:
                ch_v "Ok."
                $ JubesX.OutfitChange("costume")

        "Your birthday suit looks really great. . .":
                #Nude
                $ JubesX.change_face("sexy", 1)
                $ line = 0
                if not JubesX.Chest and not JubesX.Panties and not JubesX.Over and not JubesX.Legs and not JubesX.Hose:
                    ch_v "Uh-huh. . . wait, how would you know?!"
                elif JubesX.SeenChest and JubesX.SeenPussy and ApprovalCheck(JubesX, 1200, TabM=4):
                    ch_v ". . . yeah?"
                    $ line = 1
                elif ApprovalCheck(JubesX, 2000, TabM=4):
                    ch_v "Well you get to the point!"
                    $ line = 1
                elif JubesX.SeenChest and JubesX.SeenPussy and ApprovalCheck(JubesX, 1200, TabM=0):
                    ch_v "Maaaybe, but not here. . ."
                elif ApprovalCheck(JubesX, 2000, TabM=0):
                    ch_v "Maaaybe, but not here. . ."
                elif ApprovalCheck(JubesX, 1000, TabM=0):
                    $ JubesX.change_face("confused", 1,Mouth="smirk")
                    ch_v "Yeah, but you'll just have to keep guessing. . ."
                    $ JubesX.change_face("bemused", 0)
                else:
                    $ JubesX.change_face("angry", 1)
                    ch_v "That's not really any of your business!"

                if line:
                    #If she got nude. . .
                    $ JubesX.OutfitChange("nude")
                    "She throws her clothes off at her feet."
                    call Jubes_First_Topless
                    call Jubes_First_Bottomless(1)
                    $ JubesX.change_face("sexy")
                    menu:
                        "You know, you should wear this one out. [[set current outfit]":
                            if "exhibitionist" in JubesX.Traits:
                                ch_v "mmmm. . ."
                                $ JubesX.Outfit = "nude"
                                $ JubesX.change_stat("lust", 50, 10)
                                $ JubesX.change_stat("lust", 70, 5)
                                $ JubesX.Shame = 50
                            elif ApprovalCheck(JubesX, 800, "I") or ApprovalCheck(JubesX, 2800, TabM=0):
                                ch_v "Fun. . ."
                                $ JubesX.Outfit = "nude"
                                $ JubesX.Shame = 50
                            else:
                                $ JubesX.change_face("sexy", 1)
                                $ JubesX.Eyes = "surprised"
                                ch_v "I really won't."

                        "Let's try something else though.":
                            if "exhibitionist" in JubesX.Traits:
                                ch_v "Really?"
                            elif ApprovalCheck(JubesX, 800, "I") or ApprovalCheck(JubesX, 2800, TabM=0):
                                $ JubesX.change_face("bemused", 1)
                                ch_v "Oh! i thought you wanted me to wear this out. . ."
                                ch_v ". . ."
                            else:
                                $ JubesX.change_face("confused", 1)
                                ch_v "Yeah, I mean, I wouldn't. . ."
                $ line = 0

        "Never mind":
            return #jump Jubes_Clothes

    return #jump Jubes_Clothes
    #End of Jubes Outfits

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Jubes_Clothes_Over:
        # Overshirts
        "Why don't you go with no jacket?" if JubesX.Acc:
                $ JubesX.change_face("bemused", 1)
                if JubesX.Over or (ApprovalCheck(JubesX, 800, TabM=3) and (JubesX.Chest or JubesX.SeenChest)):
                    #if she has a shirt on, or a bra and is a bit loose about it
                    ch_v "Sure."
                elif ApprovalCheck(JubesX, 600, TabM=0):
                    call Jubes_NoBra
                    if not _return:
                        if not ApprovalCheck(JubesX, 1200):
                            call Display_DressScreen(JubesX)
                            if not _return:
                                return #jump Jubes_Clothes
                        else:
                                return #jump Jubes_Clothes
                else:
                    call Display_DressScreen(JubesX)
                    if not _return:
                            ch_v "Not right now."
                            if not JubesX.Chest:
                                ch_v "I don't have anything under this. . ."
                            return #jump Jubes_Clothes
                $ JubesX.Acc = 0
                "She throws her Jacket at her feet."
                if not renpy.showing('DressScreen'):
                        call Jubes_First_Topless

        "Why don't you go with no [JubesX.Over]?" if JubesX.Over:
                $ JubesX.change_face("bemused", 1)
                if ApprovalCheck(JubesX, 800, TabM=3) and (JubesX.Chest or JubesX.SeenChest):
                    ch_v "Sure."
                elif ApprovalCheck(JubesX, 600, TabM=0):
                    call Jubes_NoBra
                    if not _return:
                        if not ApprovalCheck(JubesX, 1200):
                            call Display_DressScreen(JubesX)
                            if not _return:
                                return #jump Jubes_Clothes
                        else:
                                return #jump Jubes_Clothes
                else:
                    call Display_DressScreen(JubesX)
                    if not _return:
                            ch_v "Not right now."
                            if not JubesX.Chest:
                                ch_v "I don't have anything under this. . ."
                            return #jump Jubes_Clothes
                $ line = JubesX.Over
                $ JubesX.Over = 0
                "She throws her [line] at her feet."
                if not JubesX.Chest and not renpy.showing('DressScreen'):
                        call Jubes_First_Topless

        "Try on that yellow jacket." if not JubesX.Acc:
                $ JubesX.change_face("bemused")
                ch_v "Sure."
                $ JubesX.Acc = "jacket"

        "Maybe open the jacket more?" if JubesX.Acc and JubesX.Acc != "open jacket":
                $ JubesX.change_face("bemused")
                if JubesX.Over or (ApprovalCheck(JubesX, 800, TabM=3) and (JubesX.Chest or JubesX.SeenChest)):
                    #if she has a shirt on, or a bra and is a bit loose about it
                    ch_v "Sure."
                elif ApprovalCheck(JubesX, 600, TabM=0):
                    call Jubes_NoBra
                    if not _return:
                        if not ApprovalCheck(JubesX, 1200):
                            call Display_DressScreen(JubesX)
                            if not _return:
                                return #jump Jubes_Clothes
                        else:
                                return #jump Jubes_Clothes
                else:
                    call Display_DressScreen(JubesX)
                    if not _return:
                            ch_v "Not right now."
                            if not JubesX.Chest:
                                ch_v "I don't have anything under this. . ."
                            return #jump Jubes_Clothes
                $ JubesX.Acc = "open jacket"
                if not renpy.showing('DressScreen'):
                        call Jubes_First_Topless

        "Maybe just leave the jacket loose?" if JubesX.Acc and JubesX.Acc != "jacket":
                $ JubesX.change_face("bemused")
                if JubesX.Over or (ApprovalCheck(JubesX, 800, TabM=3) and (JubesX.Chest or JubesX.SeenChest)):
                    #if she has a shirt on, or a bra and is a bit loose about it
                    ch_v "Sure."
                elif ApprovalCheck(JubesX, 600, TabM=0):
                    call Jubes_NoBra
                    if not _return:
                        if not ApprovalCheck(JubesX, 1200):
                            call Display_DressScreen(JubesX)
                            if not _return:
                                return #jump Jubes_Clothes
                        else:
                                return #jump Jubes_Clothes
                else:
                    call Display_DressScreen(JubesX)
                    if not _return:
                            ch_v "Not right now."
                            if not JubesX.Chest:
                                ch_v "I don't have anything under this. . ."
                            return #jump Jubes_Clothes
                $ JubesX.Acc = "jacket"
                if not renpy.showing('DressScreen'):
                        call Jubes_First_Topless

        "Maybe zip the jacket closed?" if JubesX.Acc and JubesX.Acc != "shut jacket":
                $ JubesX.change_face("bemused")
                ch_v "Sure."
                $ JubesX.Acc = "shut jacket"

        "Try on that red shirt." if JubesX.Over != "red shirt":
                $ JubesX.change_face("bemused")
                if not JubesX.Over:
                    #if she's not already wearing a top
                    ch_v "Sure."
                elif ApprovalCheck(JubesX, 800, TabM=0):
                    ch_v "Yeah, ok."
                else:
                    call Display_DressScreen(JubesX)
                    if not _return:
                            $ JubesX.change_face("bemused", 1)
                            ch_v "I don't really want to take this [JubesX.Over] off at the moment."
                            return #jump Jubes_Clothes
                $ JubesX.Over = "red shirt"

        "Try on that leather shirt." if JubesX.Over != "black shirt":
                $ JubesX.change_face("bemused")
                if not JubesX.Over:
                    #if she's not already wearing a top
                    ch_v "Sure."
                elif ApprovalCheck(JubesX, 800, TabM=0):
                    ch_v "Yeah, ok."
                else:
                    call Display_DressScreen(JubesX)
                    if not _return:
                            $ JubesX.change_face("bemused", 1)
                            ch_v "I don't really want to take this [JubesX.Over] off at the moment."
                            return #jump Jubes_Clothes
                $ JubesX.Over = "black shirt"

        "Try on that pink tubetop." if JubesX.Over != "tube top":
                $ JubesX.change_face("bemused")
                if not JubesX.Over:
                    #if she's not already wearing a top
                    ch_v "Sure."
                elif ApprovalCheck(JubesX, 800, TabM=0):
                    ch_v "Yeah, ok."
                else:
                    call Display_DressScreen(JubesX)
                    if not _return:
                            $ JubesX.change_face("bemused", 1)
                            ch_v "I don't really want to take this [JubesX.Over] off at the moment."
                            return #jump Jubes_Clothes
                $ JubesX.Over = "tube top"

        "Maybe just throw on a towel?" if JubesX.Over != "towel":
                $ JubesX.change_face("bemused", 1)
                if JubesX.Chest or JubesX.SeenChest:
                    ch_v "Odd."
                elif ApprovalCheck(JubesX, 1000, TabM=0):
                    $ JubesX.change_face("perplexed", 1)
                    ch_v "Huh, sure . ."
                else:
                    call Display_DressScreen(JubesX)
                    if not _return:
                            ch_v "Nah."
                            return #jump Jubes_Clothes
                $ JubesX.Over = "towel"

        "Never mind":
            pass
    return #jump Jubes_Clothes
    #End of Jubes Top

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Jubes_NoBra:
        menu:
            ch_v "I don't exactly have anything on under this. . ."
            "Then you could slip something on under it. . .":
                        if JubesX.SeenChest and ApprovalCheck(JubesX, 1000, TabM=3):
                                $ JubesX.Blush = 1
                                ch_v "Oh, I was just warning -you-. . ."
                                $ JubesX.Blush = 0
                        elif ApprovalCheck(JubesX, 1200, TabM=4):
                                $ JubesX.Blush = 1
                                ch_v "Oh, I was just warning -you-. . ."
                                $ JubesX.Blush = 0
                        elif ApprovalCheck(JubesX, 900, TabM=2) and "lace bra" in JubesX.Inventory:
                                ch_v "Well, I do have something I could throw on. . ."
                                $ JubesX.Chest  = "lace bra"
                                "She pulls out her lace bra and slips it under her [JubesX.Over]."
                        elif ApprovalCheck(JubesX, 600, TabM=2):
                                ch_v "Well, I do have something I could throw on. . ."
                                $ JubesX.Chest = "sports bra"
                                "She pulls out her sports bra and slips it on under her [JubesX.Over]."
                        else:
                                ch_v "Yeah, that wouldn't help."
                                return 0

            "You could always just wear nothing at all. . .":
                        if ApprovalCheck(JubesX, 1100, "LI", TabM=2) and JubesX.love > JubesX.inhibition:
                                ch_v "For you? sure. . ."
                        elif ApprovalCheck(JubesX, 700, "OI", TabM=2) and JubesX.obedience > JubesX.inhibition:
                                ch_v "Sure. . ."
                        elif ApprovalCheck(JubesX, 600, "I", TabM=2):
                                ch_v "Yeah. . ."
                        elif ApprovalCheck(JubesX, 1300, TabM=2):
                                ch_v "Okay, fine."
                        else:
                                $ JubesX.change_face("surprised")
                                $ JubesX.Brows = "angry"
                                if JubesX.Taboo > 20:
                                    ch_v "Not in public, I won't!"
                                else:
                                    ch_v "Nah."
                                return 0
            "Never mind.":
                        ch_v "Ok. . ."
                        return 0
        return 1
        #End of Jubes bra check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Jubes_Clothes_Legs:
        # Leggings
        "Maybe go without the [JubesX.Legs]." if JubesX.Legs:
                $ JubesX.change_face("sexy", 1)
                if JubesX.SeenPanties and JubesX.Panties and ApprovalCheck(JubesX, 500, TabM=5):
                    ch_v "Ok, sure."
                elif JubesX.SeenPussy and ApprovalCheck(JubesX, 900, TabM=4):
                    ch_v "Yeah, ok."
                elif ApprovalCheck(JubesX, 1300, TabM=2) and JubesX.Panties:
                    ch_v "For you, fine. . ."
                elif ApprovalCheck(JubesX, 700) and not JubesX.Panties:
                    call Jubes_NoPantiesOn
                    if not _return and not JubesX.Panties:
                        if not ApprovalCheck(JubesX, 1500):
                            call Display_DressScreen(JubesX)
                            if not _return:
                                return #jump Jubes_Clothes
                        else:
                                return #jump Jubes_Clothes
                else:
                    call Display_DressScreen(JubesX)
                    if not _return:
                        ch_v "Um, not with you around."
                        if not JubesX.Panties:
                                ch_v "I'm not actually wearing any. . ."
                        return #jump Jubes_Clothes

                $ line = JubesX.Legs
                $ JubesX.Legs = 0
                "She tugs her [line] off and drops them to the ground."
                $ line = 0

                if renpy.showing('DressScreen'):
                    pass
                elif JubesX.Panties:
                    $ JubesX.SeenPanties = 1
                else:
                    call Jubes_First_Bottomless

        "Add leather pants" if JubesX.Legs != "pants":
                ch_p "You look great in those leather pants"
                ch_v "Yeah, ok."
                $ JubesX.Legs = "pants"

        "Add jeans shorts" if JubesX.Legs != "shorts":
                ch_p "What about wearing your jeans shorts?"
                ch_v "Sure, why not."
                $ JubesX.Legs = "shorts"

#        "Add leather skirt" if JubesX.Legs != "other skirt" and "halloween" in JubesX.History:
#                ch_p "What about wearing your leather skirt?"
#                ch_v "Sure, why not."
#                $ JubesX.Legs = "other skirt"

        "Never mind":
                pass
    return #jump Jubes_Clothes
    #End of Jubes Pants

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Jubes_NoPantiesOn:
        menu:
            ch_v "I'm actually not wearing any?"
            "Then you could slip on a pair of panties. . .":
                        if JubesX.SeenPussy and ApprovalCheck(JubesX, 1100, TabM=4):
                                $ JubesX.Blush = 1
                                ch_v "No, no, it's fine like this. . ."
                                $ JubesX.Blush = 0
                        elif ApprovalCheck(JubesX, 1500, TabM=4):
                                $ JubesX.Blush = 1
                                ch_v "No, no, it's fine like this. . ."
                                $ JubesX.Blush = 0
                        elif ApprovalCheck(JubesX, 700, TabM=4):
                                ch_v "I could, I guess. . ."
                                if "lace panties" in JubesX.Inventory:
                                        $ JubesX.Panties  = "lace panties"
                                else:
                                        $ JubesX.Panties = "blue panties"
                                if ApprovalCheck(JubesX, 1200, TabM=4):
                                        $ line = JubesX.Legs
                                        $ JubesX.Legs = 0
                                        "She pulls off her [line] and slips on the [JubesX.Panties]."
                                elif JubesX.Legs == "skirt":
                                        "She pulls out her [JubesX.Panties] and pulls them up under her skirt."
                                        $ JubesX.Legs = 0
                                        "Then she drops the skirt to the floor."
                                else:
                                        $ line = JubesX.Legs
                                        $ JubesX.Legs = 0
                                        "She steps away a moment and then comes back wearing only the [JubesX.Panties]."
                                return #jump Jubes_Clothes
                        else:
                                ch_v "Nope."
                                return 0

            "You could always just wear nothing at all. . .":
                        if ApprovalCheck(JubesX, 1100, "LI", TabM=3) and JubesX.love > JubesX.inhibition:
                                ch_v "True. . ."
                        elif ApprovalCheck(JubesX, 700, "OI", TabM=3) and JubesX.obedience > JubesX.inhibition:
                                ch_v "Sure. . ."
                        elif ApprovalCheck(JubesX, 600, "I", TabM=3):
                                ch_v "Hrmm. . ."
                        elif ApprovalCheck(JubesX, 1300, TabM=3):
                                ch_v "Fine."
                        else:
                                $ JubesX.change_face("surprised")
                                $ JubesX.Brows = "angry"
                                if JubesX.Taboo > 20:
                                    ch_v "Yeah, but not in public, [JubesX.Petname]!"
                                else:
                                    ch_v "Nah."
                                return 0

            "Never mind.":
                ch_v "Ok. . ."
                return 0
        return 1
        #End of Jubes Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Jubes_Clothes_Under:
        "Tops":
            menu:
                "How about you lose the [JubesX.Chest]?" if JubesX.Chest:
                        $ JubesX.change_face("bemused", 1)
                        if JubesX.SeenChest and ApprovalCheck(JubesX, 900, TabM=2.7):
                            ch_v "Sure."
                        elif ApprovalCheck(JubesX, 1100, TabM=2):
                            if JubesX.Taboo:
                                ch_v "I don't know, here. . ."
                            else:
                                ch_v "Maaaybe. . ."
                        elif JubesX.Acc == "jacket" and ApprovalCheck(JubesX, 600, TabM=2):
                            ch_v "This jacket is a bit revealing. . ."
                        elif JubesX.Over and ApprovalCheck(JubesX, 500, TabM=2):
                            ch_v "I guess I could. . ."
                        elif not JubesX.Over:
                            call Display_DressScreen(JubesX)
                            if not _return:
                                ch_v "Not without something over it. . ."
                                return #jump Jubes_Clothes
                        else:
                            call Display_DressScreen(JubesX)
                            if not _return:
                                ch_v "Nah."
                                return #jump Jubes_Clothes
                        $ line = JubesX.Chest
                        $ JubesX.Chest = 0
                        if JubesX.Acc:
                            "She reaches under her jacket grabs her [line], and pulls it off, dropping it to the ground."
                        elif JubesX.Over:
                            "She reaches under her [JubesX.Over] grabs her [line], and pulls it off, dropping it to the ground."
                        else:
                            "She pulls off her [line] and drops it to the ground."
                            if not renpy.showing('DressScreen'):
                                call Jubes_First_Topless

                "Add sports bra" if JubesX.Chest != "sports bra":
                        ch_p "Try on that sports bra."
                        ch_v "Ok."
                        $ JubesX.Chest = "sports bra"

                "Add lace bra" if JubesX.Chest != "lace bra" and "lace bra" in JubesX.Inventory:
                        ch_p "I like that bra corset."
                        if JubesX.SeenChest or ApprovalCheck(JubesX, 1300, TabM=2):
                            ch_v "K."
                            $ JubesX.Chest = "lace bra"
                        else:
                            call Display_DressScreen(JubesX)
                            if not _return:
                                ch_v "It's kinda revealing. . ."
                            else:
                                $ JubesX.Chest = "lace bra"

                "Add bikini top" if JubesX.Chest != "bikini top" and "bikini top" in JubesX.Inventory:
                        ch_p "I like that bikini top."
                        if bg_current == "bg_pool":
                                ch_v "K."
                                $ JubesX.Chest = "bikini top"
                        else:
                                if JubesX.SeenChest or ApprovalCheck(JubesX, 1000, TabM=2):
                                    ch_v "K."
                                    $ JubesX.Chest = "bikini top"
                                else:
                                    call Display_DressScreen(JubesX)
                                    if not _return:
                                            ch_v "This is not really a \"bikini\" sort of place. . ."
                                    else:
                                            $ JubesX.Chest = "bikini top"
                "Never mind":
                        pass
            return #jump Jubes_Clothes_Under

        "Hose and stockings options":
            menu:
                "You could lose the hose." if JubesX.Hose and JubesX.Hose != 'ripped tights' and JubesX.Hose != 'tights':
                                $ JubesX.Hose = 0
                "The thigh-high hose would look good with that." if JubesX.Hose != "stockings":
                                $ JubesX.Hose = "stockings"
                "The pantyhose would look good with that." if JubesX.Hose != "pantyhose" and "pantyhose" in JubesX.Inventory:
                                $ JubesX.Hose = "pantyhose"
                "The ripped pantyhose would look good with that." if JubesX.Hose != "ripped pantyhose" and "ripped pantyhose" in JubesX.Inventory:
                                $ JubesX.Hose = "ripped pantyhose"
                "The tall socks would look good with that." if JubesX.Hose != "socks" and "socks" in JubesX.Inventory:
                                $ JubesX.Hose = "socks"
                "The stockings and garterbelt would look good with that." if JubesX.Hose != "stockings and garterbelt" and "stockings and garterbelt" in JubesX.Inventory:
                                $ JubesX.Hose = "stockings and garterbelt"
                "Just the garterbelt would look good with that." if JubesX.Hose != "garterbelt" and "stockings and garterbelt" in JubesX.Inventory:
                                $ JubesX.Hose = "garterbelt"
                "Never mind":
                        pass
            return #jump Jubes_Clothes_Under

        #Panties
        "Panties":
            menu:
                "You could lose those panties. . ." if JubesX.Panties:
                        $ JubesX.change_face("bemused", 1)
                        if ApprovalCheck(JubesX, 900) and (JubesX.Legs or (JubesX.SeenPussy and not JubesX.Taboo)):
                                #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                                if ApprovalCheck(JubesX, 850, "L"):
                                        ch_v "True. . ."
                                elif ApprovalCheck(JubesX, 500, "O"):
                                        ch_v "Right. . ."
                                elif ApprovalCheck(JubesX, 350, "I"):
                                        ch_v "Heh."
                                else:
                                        ch_v "Sure, I guess."
                        else:                       #low approval or not wearing pants or in public
                                if ApprovalCheck(JubesX, 1100, "LI", TabM=3) and JubesX.love > JubesX.inhibition:
                                        ch_v "I don't know, it's kinda public here. . ."
                                elif ApprovalCheck(JubesX, 700, "OI", TabM=3) and JubesX.obedience > JubesX.inhibition:
                                        ch_v "Well. . ."
                                elif ApprovalCheck(JubesX, 600, "I", TabM=3):
                                        ch_v "Hrmm. . ."
                                elif ApprovalCheck(JubesX, 1300, TabM=3):
                                        ch_v "Okay, fine."
                                else:
                                        call Display_DressScreen(JubesX)
                                        if not _return:
                                            $ JubesX.change_face("surprised")
                                            $ JubesX.Brows = "angry"
                                            if JubesX.Taboo > 20:
                                                ch_v "This is just too public."
                                            else:
                                                ch_v "Nah."
                                            return #jump Jubes_Clothes
                        $ line = JubesX.Panties
                        $ JubesX.Panties = 0
                        if not JubesX.Legs:
                            "She pulls off her [line], then drops them to the ground."
                            if not renpy.showing('DressScreen'):
                                    call Jubes_First_Bottomless
                        elif ApprovalCheck(JubesX, 1200, TabM=4):
                            $ primary_action = JubesX.Legs
                            $ JubesX.Legs = 0
                            pause 0.5
                            $ JubesX.Legs = primary_action
                            "She pulls off her [JubesX.Legs] and [line], then pulls the [JubesX.Legs] back on."
                            $ primary_action = 1
                            call Jubes_First_Bottomless(1)
                        elif JubesX.Legs == "skirt":
                            "She reaches under her skirt and pulls her [line] off."
                        else:
                            $ JubesX.Blush = 1
                            "She steps away a moment and then comes back."
                            $ JubesX.Blush = 0
                        $ line = 0

                "Why don't you wear the blue panties instead?" if JubesX.Panties and JubesX.Panties != "blue panties":
                        if ApprovalCheck(JubesX, 1100, TabM=3):
                                ch_v "Ok."
                                $ JubesX.Panties = "blue panties"
                        else:
                                call Display_DressScreen(JubesX)
                                if not _return:
                                        ch_v "That's none of your busines."
                                else:
                                        $ JubesX.Panties = "blue panties"

                "Why don't you wear the lace panties instead?" if "lace panties" in JubesX.Inventory and JubesX.Panties and JubesX.Panties != "lace panties":
                        if ApprovalCheck(JubesX, 1300, TabM=3):
                                ch_v "I guess."
                                $ JubesX.Panties = "lace panties"
                        else:
                                call Display_DressScreen(JubesX)
                                if not _return:
                                        ch_v "That's none of your busines."
                                else:
                                        $ JubesX.Panties = "lace panties"

                "Why don't you wear the tiger panties instead?" if "tiger panties" in JubesX.Inventory and JubesX.Panties and JubesX.Panties != "tiger panties":
                        if ApprovalCheck(JubesX, 1300, TabM=3):
                                ch_v "I guess."
                                $ JubesX.Panties = "tiger panties"
                        else:
                                call Display_DressScreen(JubesX)
                                if not _return:
                                        ch_v "That's none of your busines."
                                else:
                                        $ JubesX.Panties = "tiger panties"

                "I like those bikini bottoms." if "bikini bottoms" in JubesX.Inventory and JubesX.Panties != "bikini bottoms":
                        if bg_current == "bg_pool":
                                ch_v "K."
                                $ JubesX.Panties = "bikini bottoms"
                        else:
                                if ApprovalCheck(JubesX, 1000, TabM=2):
                                    ch_v "K."
                                    $ JubesX.Panties = "bikini bottoms"
                                else:
                                    call Display_DressScreen(JubesX)
                                    if not _return:
                                            ch_v "This is not really a \"bikini\" sort of place. . ."
                                    else:
                                            $ JubesX.Panties = "bikini bottoms"

                "You know, you could wear some panties with that. . ." if not JubesX.Panties:
                        $ JubesX.change_face("bemused", 1)
                        if JubesX.Legs and (JubesX.love+JubesX.obedience) <= (2 * JubesX.inhibition):
                            $ JubesX.Mouth = "smile"
                            ch_v "I don't know about that."
                            menu:
                                "Fine by me":
                                    return #jump Jubes_Clothes
                                "I insist, put some on.":
                                    if (JubesX.love+JubesX.obedience) <= (1.5 * JubesX.inhibition):
                                        $ JubesX.change_face("angry", Eyes="side")
                                        ch_v "Well too bad."
                                        return #jump Jubes_Clothes
                                    else:
                                        $ JubesX.change_face("sadside")
                                        ch_v "Oh, fine."
                        else:
                            ch_v "I guess. . ."
                        menu:
                            extend ""
                            "How about the blue ones?":
                                    ch_v "Sure, ok."
                                    $ JubesX.Panties = "blue panties"
                            "How about the lace ones?" if "lace panties" in JubesX.Inventory:
                                    ch_v "Alright."
                                    $ JubesX.Panties  = "lace panties"
                            "How about the tiger ones?" if "tiger panties" in JubesX.Inventory:
                                    ch_v "Alright."
                                    $ JubesX.Panties  = "tiger panties"
                            "How about the bikini bottoms?" if "bikini bottoms" in JubesX.Inventory:
                                    ch_v "Alright."
                                    $ JubesX.Panties  = "bikini bottoms"
                "Never mind":
                    pass
            return #jump Jubes_Clothes_Under
        "Never mind":
            pass
    return #jump Jubes_Clothes
    #End of Jubes Underwear

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Jubes_Clothes_Misc:
        #Misc
        "Shades in her hair" if JubesX.Hair != "shades":
                ch_p "You're missing those signature shades!"
                if ApprovalCheck(JubesX, 600):
                    ch_v "Oh yeah!"
                    $ JubesX.Hair = "shades"
                else:
                    ch_v "I don't know, it's fine like this."

        "Shades out of her hair" if JubesX.Hair == "shades":
                ch_p "You should try without the shades."
                if ApprovalCheck(JubesX, 600):
                    ch_v "Ok. . "
                    $ JubesX.Hair = "short"
                else:
                    ch_v "I don't know, it's fine like this."

        "Dry Hair" if JubesX.Hair == "wet":
                ch_p "Maybe dry out your hair."
                if ApprovalCheck(JubesX, 600):
                    ch_v "Ok."
                    $ JubesX.Hair = "short"
                else:
                    ch_v "I don't know, it's fine like this."

        "Wet Hair style" if JubesX.Hair != "wet":
                ch_p "You should go for that wet look with your hair."
                if ApprovalCheck(JubesX, 800):
                    ch_v "Hmm?"
                    $ JubesX.Hair = "wet"
                    "She wanders off for a minute and comes back."
                    ch_v "Like this?"
                else:
                    ch_v "Ugh, too much work."


        "Grow pubes" if not JubesX.Pubes:
                ch_p "You know, I like some nice hair down there. Maybe grow it out."
                if "pubes" in JubesX.Todo:
                        $ JubesX.change_face("bemused", 1)
                        ch_v "It doesn't grow out over night!"
                else:
                        $ JubesX.change_face("bemused", 1)
                        if ApprovalCheck(JubesX, 1000, TabM=0):
                            ch_v "I guess I could. . ."
                        else:
                            $ JubesX.change_face("surprised")
                            $ JubesX.Brows = "angry"
                            ch_v "That's none of your business!"
                            return #jump Jubes_Clothes
                        $ JubesX.Todo.append("pubes")
                        $ JubesX.PubeC = 6
        "Shave pubes" if JubesX.Pubes == 1:
                ch_p "I like it waxed clean down there."
                $ JubesX.change_face("bemused", 1)
                if "shave" in JubesX.Todo:
                    ch_v "I heard you, I'll get around to it."
                else:
                    if ApprovalCheck(JubesX, 1100, TabM=0):
                        ch_v "That's how you like it then? . ."
                    else:
                        $ JubesX.change_face("surprised")
                        $ JubesX.Brows = "angry"
                        ch_v "That's none of your business!"
                        return #jump Jubes_Clothes
                    $ JubesX.Todo.append("shave")

        "Piercings. [[See what she looks like without them first] (locked)" if not JubesX.SeenPussy and not JubesX.SeenChest:
            pass

        "Add ring piercings" if JubesX.Pierce != "ring" and (JubesX.SeenPussy or JubesX.SeenChest):
                ch_p "You know, you'd look really nice with some ring body piercings."
                if "ring" in JubesX.Todo:
                    ch_v "I heard you, I'll get around to it."
                else:
                    $ JubesX.change_face("bemused", 1)
                    $ Approval = ApprovalCheck(JubesX, 1150, TabM=0)
                    if ApprovalCheck(JubesX, 900, "L", TabM=0) or (Approval and JubesX.love > 2* JubesX.obedience):
                        ch_v "You think they'd look good on me?"
                    elif ApprovalCheck(JubesX, 600, "I", TabM=0) or (Approval and JubesX.inhibition > JubesX.obedience):
                        ch_v "I've been thinking about that for a while."
                    elif ApprovalCheck(JubesX, 500, "O", TabM=0) or Approval:
                        ch_v "Yes, [JubesX.Petname]."
                    else:
                        $ JubesX.change_face("surprised")
                        $ JubesX.Brows = "angry"
                        ch_v "Not into it, [JubesX.Petname]."
                        return #jump Jubes_Clothes
                    $ JubesX.Todo.append("ring")

        "Add barbell piercings" if JubesX.Pierce != "barbell" and (JubesX.SeenPussy or JubesX.SeenChest):
                ch_p "You know, you'd look really nice with some barbell body piercings."
                if "barbell" in JubesX.Todo:
                    ch_v "I heard you, I'll get around to it."
                else:
                    $ JubesX.change_face("bemused", 1)
                    $ Approval = ApprovalCheck(JubesX, 1150, TabM=0)
                    if ApprovalCheck(JubesX, 900, "L", TabM=0) or (Approval and JubesX.love > 2 * JubesX.obedience):
                        ch_v "You think they'd look good on me?"
                    elif ApprovalCheck(JubesX, 600, "I", TabM=0) or (Approval and JubesX.inhibition > JubesX.obedience):
                        ch_v "I've been thinking about that for a while."
                    elif ApprovalCheck(JubesX, 500, "O", TabM=0) or Approval:
                        ch_v "Yes, [JubesX.Petname]."
                    else:
                        $ JubesX.change_face("surprised")
                        $ JubesX.Brows = "angry"
                        ch_v "Not into it, [JubesX.Petname]."
                        return #jump Jubes_Clothes
                    $ JubesX.Todo.append("barbell")

        "Remove piercings" if JubesX.Pierce:
                ch_p "You know, you'd look better without those piercings."
                $ JubesX.change_face("bemused", 1)
                $ Approval = ApprovalCheck(JubesX, 1350, TabM=0)
                if ApprovalCheck(JubesX, 950, "L", TabM=0) or (Approval and JubesX.love > JubesX.obedience):
                    ch_v "Make up your mind . ."
                elif ApprovalCheck(JubesX, 700, "I", TabM=0) or (Approval and JubesX.inhibition > JubesX.obedience):
                    ch_v "Well, this is annoying. . ."
                elif ApprovalCheck(JubesX, 600, "O", TabM=0) or Approval:
                    ch_v "Fine."
                else:
                    $ JubesX.change_face("surprised")
                    $ JubesX.Brows = "angry"
                    ch_v "I really like them though!"
                    return #jump Jubes_Clothes
                $ JubesX.Pierce = 0

        "Never mind":
            pass
    return #jump Jubes_Clothes
    #End of Jubes Misc Wardrobe

return
#End Jubes Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
