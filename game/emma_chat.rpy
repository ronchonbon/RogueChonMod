# star Emma chat interface

label Emma_Chat_Minimal:
    $ EmmaX.change_face()
    call shift_focus(EmmaX)
    if EmmaX.location != bg_current:
                show Cellphone at sprite_location(EmmaX.sprite_location)
    else:
                hide Cellphone
    if "caught" in EmmaX.recent_history:
                ch_e "I don't think we should be seen together, if you don't mind."
                return
    if "angry" in EmmaX.recent_history:
                ch_e "I would not press my luck if I were you."
                return
    menu:
        ch_e "What was it you wished to discuss, [EmmaX.Petname]?"
        "Come on over." if EmmaX.location != bg_current:
                    ch_e "I don't think I should be visiting students at their whim."
                    ch_e "You know my office hours."
        "Ask [EmmaX.name] to leave" if EmmaX.location == bg_current:
                    ch_e "I'll come and go as I see fit, thank you."
        "Romance her":
                menu:
                    "Flirt with her (locked)" if not EmmaX.can_flirt:
                                pass
                    "Flirt with her" if EmmaX.can_flirt:
                                call Emma_Flirt_Minimal
                    "Sex Menu" if EmmaX.location == bg_current:
                                ch_p "Did you want to fool around?"
                                ch_e "With a student? You should know better than that, [EmmaX.Petname]."
                    "Date":
                                ch_p "Do you want to go on a date tonight?"
                                ch_e "Well that certainly doesn't seem appropriate."
                    "Gifts" if EmmaX.location == bg_current:
                                ch_p "I'd like to give you something."
                                ch_e "I'm not sure that would be appropriate at the moment."
                    "Back":
                                pass
        "Talk to her":
                menu:
                    "I just wanted to talk. . .":
                                call Emma_Chitchat
                    "Relationship status":
                                ch_p "Could we talk about us?"
                                ch_e "I'm not sure that's an appropriate discussion at the moment."
                    "Could I get your number?" if EmmaX not in Digits:
                                if Approvalcheck(EmmaX, 800, "LI"):
                                    ch_e "I don't see why not."
                                    $ Digits.append(EmmaX)
                                elif Approvalcheck(EmmaX, 500, "OI"):
                                    ch_e "Hmm. . . fine, hand me your phone."
                                    $ Digits.append(EmmaX)
                                else:
                                    ch_e "I don't think it's appropriate to give my number out to a student like that."
                    "Back":
                                pass
        "Change [EmmaX.name]":
                    ch_p "Let's talk about you."
                    ch_e "I doubt that's any of your business."
        "Party up" if EmmaX not in Party and EmmaX.location == bg_current:
                    ch_p "Could you follow me for a bit?"
                    ch_e "I don't think I should."
        "Disband party" if EmmaX in Party:
                    ch_p "Ok, you can leave if you prefer."
                    $ Party.remove(EmmaX)
        "Never mind.":
                    if time_index == 2: #evening time
                            ch_e "Now if that will be all, please clear out of here."
                            $ EmmaX.change_face("bemused",2)
                            ch_e "I have some. . . business to attend to."
                    else:
                            "She seems a bit reserved. Maybe you need something to break the ice."
                            "Maybe you should check in on her after classes are over and the students leave."
                    return
    jump Emma_Chat_Minimal

label Emma_Flirt_Minimal:
        menu:
            "Compliment her":
                        call Compliment(Girl)
            "Say you love her":
                        if EmmaX.love >= 500:
                                $ EmmaX.change_stat("love", 90, 2)
                        $ EmmaX.change_stat("obedience", 40, 1)
                        ch_e "Don't even joke, [EmmaX.Petname]."
            "Touch her cheek":
                        "You begin to approach her, but she cuts you off with a firm hand out."
                        ch_e "Don't get too close to me, [EmmaX.Petname]."
            "Hold hands":
                        "You begin to approach her, but she cuts you off with a firm hand out."
                        ch_e "Don't get too close to me, [EmmaX.Petname]."
            "Pat her head":
                        "You begin to approach her, but she cuts you off with a firm hand out."
                        ch_e "Don't get too close to me, [EmmaX.Petname]."
            "Kiss her cheek":
                        "You begin to approach her, but she cuts you off with a firm hand out."
                        ch_e "Don't get too close to me, [EmmaX.Petname]."
            "Hug her":
                        "You begin to approach her, but she cuts you off with a firm hand out."
                        ch_e "Don't get too close to me, [EmmaX.Petname]."
            "Slap her ass":
                        "You begin to approach her, but she cuts you off with a firm hand out."
                        ch_e "Don't get too close to me, [EmmaX.Petname]."
            "Pinch her ass":
                        "You begin to approach her, but she cuts you off with a firm hand out."
                        ch_e "Don't get too close to me, [EmmaX.Petname]."
            "Grab her tit":
                        "You begin to approach her, but she cuts you off with a firm hand out."
                        ch_e "Don't get too close to me, [EmmaX.Petname]."
            "Rub her shoulders":
                        "You begin to approach her, but she cuts you off with a firm hand out."
                        ch_e "Don't get too close to me, [EmmaX.Petname]."
            "Never mind":
                return

        $ EmmaX.can_flirt = False
        return
#Emma Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

label Emma_Relationship: #rkelj
    while True:
        menu:
            ch_e "What did you want to talk about?"
            "Do you want to be my girlfriend?" if EmmaX not in Player.Harem and "ex" not in EmmaX.Traits:
                    $ EmmaX.daily_history.append("relationship")
                    if "asked boyfriend" in EmmaX.daily_history and "angry" in EmmaX.daily_history:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "Pest."
                            return
                    elif "asked boyfriend" in EmmaX.daily_history:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "Not today, little fly."
                            return
                    elif EmmaX.Break[0]:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "I don't share."
                            if Player.Harem:
                                    $ EmmaX.daily_history.append("asked boyfriend")
                                    return
                            else:
                                    ch_p "I'm not anymore."

                    $ EmmaX.daily_history.append("asked boyfriend")

                    if Player.Harem and "EmmaYes" not in Player.Traits:
                        if len(Player.Harem) >= 2:
                            ch_e "I doubt they would understand, [EmmaX.Petname]."
                        else:
                            ch_e "I doubt [Player.Harem[0].name] would understand, [EmmaX.Petname]."
                        return

                    if EmmaX.Event[5]:
                            $ EmmaX.change_face("bemused", 1)
                            ch_e "I believe I asked you first."
                    else:
                            $ EmmaX.change_face("surprised", 2)
                            ch_e "Don't you think that might be inappropriate, [EmmaX.Petname]. . ."
                            $ EmmaX.change_face("smile", 1)

                    call Emma_OtherWoman

                    if EmmaX.love >= 800:
                            $ EmmaX.change_face("surprised", 1)
                            $ EmmaX.Mouth = "smile"
                            $ EmmaX.change_stat("love", 200, 40)
                            ch_e "I suppose I've become accustomed to you. . ."
                            if "boyfriend" not in EmmaX.Petnames:
                                    $ EmmaX.Petnames.append("boyfriend")
                            if "EmmaYes" in Player.Traits:
                                    $ Player.Traits.remove("EmmaYes")
                            $ Player.Harem.append(EmmaX)
                            call Harem_Initiation
                            "[EmmaX.name] draws you in and kisses you deeply."
                            $ EmmaX.change_face("kiss", 1)
                            $ EmmaX.Kissed += 1
                    elif EmmaX.obedience >= 500:
                            $ EmmaX.change_face("perplexed")
                            ch_e "I don't believe \"dating\" would be the right term for it."
                    elif EmmaX.inhibition >= 500:
                            $ EmmaX.change_face("smile")
                            ch_e "I don't think we should be \"exclusive.\""
                    else:
                            $ EmmaX.change_face("perplexed", 1)
                            ch_e "I really couldn't get serious about a student, [EmmaX.Petname]."

            "Do you want to get back together?" if "ex" in EmmaX.Traits:
                    $ EmmaX.daily_history.append("relationship")
                    if "asked boyfriend" in EmmaX.daily_history and "angry" in EmmaX.daily_history:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "Do I have to demonstrate how unlikely that is?"
                            return
                    elif "asked boyfriend" in EmmaX.daily_history:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "Now you're just embarrassing yourself."
                            return

                    $ EmmaX.daily_history.append("asked boyfriend")

                    if Player.Harem and "EmmaYes" not in Player.Traits:
                            if len(Player.Harem) >= 2:
                                ch_e "I doubt they would understand, [EmmaX.Petname]."
                            else:
                                ch_e "I doubt [Player.Harem[0].name] would understand, [EmmaX.Petname]."
                            return

                    $ counter = 0
                    call Emma_OtherWoman

                    if EmmaX.love >= 800:
                            $ EmmaX.change_face("sly", 1)
                            $ EmmaX.change_stat("love", 90, 5)
                            ch_e "Try as I might, I can't stay mad at you."
                            if "boyfriend" not in EmmaX.Petnames:
                                    $ EmmaX.Petnames.append("boyfriend")
                            $ EmmaX.Traits.remove("ex")
                            if "EmmaYes" in Player.Traits:
                                    $ Player.Traits.remove("EmmaYes")
                            $ Player.Harem.append(EmmaX)
                            call Harem_Initiation
                            "[EmmaX.name] leans in and kisses you deeply."
                            $ EmmaX.change_face("kiss", 1)
                            $ EmmaX.Kissed += 1
                    elif EmmaX.love >= 600 and Approvalcheck(EmmaX, 1500):
                            $ EmmaX.change_face("smile", 1)
                            $ EmmaX.change_stat("love", 90, 5)
                            ch_e "Hrm, very well."
                            if "boyfriend" not in EmmaX.Petnames:
                                    $ EmmaX.Petnames.append("boyfriend")
                            $ EmmaX.Traits.remove("ex")
                            if "EmmaYes" in Player.Traits:
                                    $ Player.Traits.remove("EmmaYes")
                            $ Player.Harem.append(EmmaX)
                            call Harem_Initiation
                            $ EmmaX.change_face("kiss", 1)
                            "[EmmaX.name] gives you a quick kiss."
                            $ EmmaX.change_face("sly", 1)
                            $ EmmaX.Kissed += 1
                    elif EmmaX.obedience >= 500:
                            $ EmmaX.change_face("sad")
                            ch_e "Let's keep things as they are, for now."
                    elif EmmaX.inhibition >= 500:
                            $ EmmaX.change_face("perplexed")
                            ch_e "No, \"casual\" works better for the time being."
                    else:
                            $ EmmaX.change_face("perplexed", 1)
                            ch_e "I can't be bothered with second chances."

                    # End Back Together

            "I wanted to ask about [[another girl]" if EmmaX in Player.Harem:
                            call AskDateOther

            "I think we should break up." if EmmaX in Player.Harem:
                        if "breakup talk" in EmmaX.daily_history:
                                ch_e "You must be joking. Again?"
                        else:
                                call Breakup(EmmaX)

            "About that talk we had before. . .":
                menu:
                    "When you said you loved me. . ." if "lover" not in EmmaX.Traits and EmmaX.Event[6] >= 20:
                            call Emma_love_Redux
                    "You said you wanted me to be more in control?" if "sir" not in EmmaX.Petnames and "sir" in EmmaX.History:
                            if "asked sub" in EmmaX.daily_history:
                                    ch_e "I did, you didn't."
                            else:
                                    call Emma_Sub_Asked
                    "You said you wanted me to be your Master?" if "master" not in EmmaX.Petnames and "master" in EmmaX.History:
                            if "asked sub" in EmmaX.daily_history:
                                    ch_e "I seem to recall something about that. . ."
                            else:
                                    call Emma_Sub_Asked
                    "Never Mind":
                            pass
            "Never Mind":
                return

    return

label Emma_OtherWoman(counter = 0):
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return
    $ counter = int((EmmaX.GirlLikecheck(Player.Harem[0]) - 500)/2)

    $ EmmaX.change_face("perplexed")
    if len(Player.Harem) >= 2:
        ch_e "But you're with [Player.Harem[0].name] right now, among others, apparently."
    else:
        ch_e "But you're with [Player.Harem[0].name] right now."
    menu:
        extend ""
        "She said I can be with you too." if "EmmaYes" in Player.Traits:
                if Approvalcheck(EmmaX, 1800, Bonus = counter):
                    $ EmmaX.change_face("smile", 1)
                    if EmmaX.love >= EmmaX.obedience:
                            ch_e "I suppose you're worth sharing."
                    elif EmmaX.obedience >= EmmaX.inhibition:
                            ch_e "If she can share then I can."
                    else:
                            ch_e "Sure, why not."
                else:
                    $ EmmaX.change_face("angry", 1)
                    ch_e "I really don't care what that little slut does."
                    $ renpy.pop_call()
                    #This causes it to jump past the previous menu on the return

        "I could ask if she'd be ok with me dating you both." if "EmmaYes" not in Player.Traits:
                if Approvalcheck(EmmaX, 1800, Bonus = counter):
                        $ EmmaX.change_face("smile", 1)
                        if EmmaX.love >= EmmaX.obedience:
                            ch_e "I suppose you're worth sharing."
                        elif EmmaX.obedience >= EmmaX.inhibition:
                            ch_e "If she can share then I can."
                        else:
                            ch_e "Sure, why not."
                        ch_e "Go ask her, give me the night to think about it, and then come back tomorrow with her answer."
                else:
                        $ EmmaX.change_face("angry", 1)
                        ch_e "I really don't care what that little slut does."
                $ renpy.pop_call()

        "What she doesn't know won't hurt her.":
                if not Approvalcheck(EmmaX, 1800, Bonus = -counter): #checks if Emma likes you more than Rogue
                        $ EmmaX.change_face("angry", 1)
                        if not Approvalcheck(EmmaX, 1800):
                                ch_e "I don't want you either."
                        else:
                                ch_e "I don't want to share you."
                        $ renpy.pop_call()
                else:
                        $ EmmaX.change_face("smile", 1)
                        if EmmaX.love >= EmmaX.obedience:
                                ch_e "I suppose we could arrange something."
                        elif EmmaX.obedience >= EmmaX.inhibition:
                                ch_e "If you insist."
                        else:
                                ch_e "I don't see why not."
                        $ EmmaX.Traits.append("downlow")

        "I can break it off with her.":
                    $ EmmaX.change_face("sad")
                    ch_e "Then we can talk after you have."
                    $ renpy.pop_call()

        "You're right, I was dumb to ask.":
                    $ EmmaX.change_face("sad")
                    ch_e "Obviously. . ."
                    $ renpy.pop_call()
    return


label Emma_About(check=0): #rkeljsv
    if check not in all_Girls:
            ch_e "Who?"
            return
    ch_e "What do I think about her? Well. . ."
    if check == RogueX:
            if "poly Rogue" in EmmaX.Traits:
                ch_e "As you're aware, we've shared a great deal. . ."
            elif EmmaX.LikeRogue >= 900:
                ch_e "I do find her rather mesmerizing. . ."
            elif EmmaX.LikeRogue >= 800:
                ch_e "That accent certainly did grow on me. . ."
            elif EmmaX.LikeRogue >= 700:
                ch_e "We've become quite close."
            elif EmmaX.LikeRogue >= 600:
                ch_e "I'm rather fond of her."
            elif EmmaX.LikeRogue >= 500:
                ch_e "She's an adequate student."
            elif EmmaX.LikeRogue >= 400:
                ch_e "She can be a bit of a handful."
            elif EmmaX.LikeRogue >= 300:
                ch_e "I can barely tollerate her disrespectful nature."
            else:
                ch_e "That swamp rat? What about her?"
    elif check == KittyX:
            if "poly Kitty" in EmmaX.Traits:
                ch_e "As you're aware, we do get along quite well. . ."
            elif EmmaX.LikeKitty >= 900:
                ch_e "She is rather. . . flexible. . ."
            elif EmmaX.LikeKitty >= 800:
                ch_e "She is rather adorable. . ."
            elif EmmaX.LikeKitty >= 700:
                ch_e "She's something of a friend at this point."
            elif EmmaX.LikeKitty >= 600:
                ch_e "Once you get to know her, she's not bad."
            elif EmmaX.LikeKitty >= 500:
                ch_e "She's an adequate student."
            elif EmmaX.LikeKitty >= 400:
                ch_e "She can be a bit of a know it all."
            elif EmmaX.LikeKitty >= 300:
                ch_e "I can't stand her constant questions."
            else:
                ch_e "That little bitch?"
    elif check == LauraX:
            if "poly Laura" in EmmaX.Traits:
                ch_e "She is quite. . . energetic. . ."
            elif EmmaX.LikeLaura >= 900:
                ch_e "She's very durable. . ."
            elif EmmaX.LikeLaura >= 800:
                ch_e "She has a rough quality that is quite exciting. . ."
            elif EmmaX.LikeLaura >= 700:
                ch_e "She's something of a friend at this point."
            elif EmmaX.LikeLaura >= 600:
                ch_e "Once you get to know her, she's not bad."
            elif EmmaX.LikeLaura >= 500:
                ch_e "She's an adequate student."
            elif EmmaX.LikeLaura >= 400:
                ch_e "She is a bit rough around the edges."
            elif EmmaX.LikeLaura >= 300:
                ch_e "Yes, a bit feral, that one."
            else:
                ch_e "I'd put her down myself if I didn't have responsibilites."
    elif check == JeanX:
            if "poly Jean" in EmmaX.Traits:
                ch_e "As you're aware, we've shared a great deal. . ."
            elif EmmaX.LikeJean >= 900:
                ch_e "I do find her rather mesmerizing. . ."
            elif EmmaX.LikeJean >= 800:
                ch_e "She really is lovely, when you give her a chance. . ."
            elif EmmaX.LikeJean >= 700:
                ch_e "I have grown to like her. . ."
            elif EmmaX.LikeJean >= 600:
                ch_e "I'm rather fond of her."
            elif EmmaX.LikeJean >= 500:
                ch_e "She's an adequate student."
            elif EmmaX.LikeJean >= 400:
                ch_e "She can be a bit of a pill."
            elif EmmaX.LikeJean >= 300:
                ch_e "I can barely tollerate her arrogance."
            else:
                ch_e "That bitch? What about her?"
    elif check == StormX:
            if "poly Storm" in EmmaX.Traits:
                ch_e "She is marvelously experienced. . ."
            elif EmmaX.LikeStorm >= 900:
                ch_e "She complements me well. . ."
            elif EmmaX.LikeStorm >= 800:
                ch_e "She has a lovely figure. . ."
            elif EmmaX.LikeStorm >= 700:
                ch_e "She's something of a friend.."
            elif EmmaX.LikeStorm >= 600:
                ch_e "She's an excellent colleague."
            elif EmmaX.LikeStorm >= 500:
                ch_e "She's an adequate colleague."
            elif EmmaX.LikeStorm >= 400:
                ch_e "She is a bit rough around the edges"
            elif EmmaX.LikeStorm >= 300:
                ch_e "The carpet matches the drapes, you know. Of course you would."
            else:
                ch_e "I wish I could convince Charles to fire her."
    elif check == JubesX:
            if "poly Jubes" in EmmaX.Traits:
                ch_e "As you're aware, we do get along quite well. . ."
            elif EmmaX.LikeJubes >= 900:
                ch_e "She is rather. . . flexible. . ."
            elif EmmaX.LikeJubes >= 800:
                ch_e "She is rather lovely. . ."
            elif EmmaX.LikeJubes >= 700:
                ch_e "She's something of a friend at this point."
            elif EmmaX.LikeJubes >= 600:
                ch_e "Once you get to know her, she's not bad."
            elif EmmaX.LikeJubes >= 500:
                ch_e "She's an adequate student."
            elif EmmaX.LikeJubes >= 400:
                ch_e "She can be a bit of a biter"
            elif EmmaX.LikeJubes >= 300:
                ch_e "She is very disruptive."
            else:
                ch_e "That little bitch?"
    return
#End Emma_AboutRogue

label Emma_Monogamy:
        #called from Emma_Settings to ask her not to hook up wiht other girls
        menu:
            "Could you not hook up with other girls?" if "mono" not in EmmaX.Traits:
                    if EmmaX.Thirst >= 50 and not Approvalcheck(EmmaX, 1800, "LO", TabM=0):
                            #she's too thirsty
                            $ EmmaX.change_face("sly",1)
                            if "mono" not in EmmaX.daily_history:
                                    $ EmmaX.change_stat("obedience", 90, -2)
                            ch_e "You know, it's not like you leave me any alternatives. . ."
                            return
                    elif Approvalcheck(EmmaX, 1300, "LO", TabM=0) and EmmaX.love >= EmmaX.obedience:
                            #she cares
                            $ EmmaX.change_face("sly",1)
                            if "mono" not in EmmaX.daily_history:
                                    $ EmmaX.change_stat("love", 90, 1)
                            ch_e "Jealousy is an adorable look on you. . ."
                            ch_e "I suppose I could restain myself. . ."
                    elif Approvalcheck(EmmaX, 750, "O", TabM=0):
                            #she is obedient
                            $ EmmaX.change_face("sly",1,Eyes="side")
                            ch_e "If you insist. . ."
                    else:
                            #she doesn't care
                            $ EmmaX.change_face("sly",1,Brows="confused")
                            ch_e "I'm afraid my affairs are my own business."
                            ch_e "Don't leave me wanting. . ."
                            return
                    if "mono" not in EmmaX.daily_history:
                            $ EmmaX.change_stat("obedience", 90, 3)
                    $ EmmaX.AddWord(1,0,"mono") #Daily
                    $ EmmaX.Traits.append("mono")
            "Don't hook up with other girls." if "mono" not in EmmaX.Traits:
                    if Approvalcheck(EmmaX, 900, "O", TabM=0):
                            #she is obedient
                            $ EmmaX.change_face("sly",1,Eyes="side")
                            ch_e "Oh very well."
                    elif EmmaX.Thirst >= 60 and not Approvalcheck(EmmaX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ EmmaX.change_face("sly",1)
                            if "mono" not in EmmaX.daily_history:
                                    $ EmmaX.change_stat("obedience", 90, -2)
                            ch_e "You know, it's not like you leave me any alternatives. . ."
                            return
                    elif Approvalcheck(EmmaX, 600, "O", TabM=0):
                            #she is obedient
                            $ EmmaX.change_face("sly",1,Eyes="side")
                            ch_e "If I must. . ."
                    elif Approvalcheck(EmmaX, 1500, "LO", TabM=0):
                            #she cares
                            $ EmmaX.change_face("sly",1)
                            ch_e "You shouldn't take that tone with me."
                            ch_e "But I suppose I could let it slide. . ."
                    else:
                            #she doesn't care
                            $ EmmaX.change_face("sly",1,Brows="confused")
                            ch_e "My affairs are my own business."
                            return
                    if "mono" not in EmmaX.daily_history:
                            $ EmmaX.change_stat("obedience", 90, 3)
                    $ EmmaX.AddWord(1,0,"mono") #Daily
                    $ EmmaX.Traits.append("mono")
            "It's ok if you hook up with other girls." if "mono" in EmmaX.Traits:
                    if Approvalcheck(EmmaX, 700, "O", TabM=0):
                            $ EmmaX.change_face("sly",1,Eyes="side")
                            ch_e "Of course."
                    elif Approvalcheck(EmmaX, 800, "L", TabM=0):
                            $ EmmaX.change_face("sly",1)
                            ch_e "Only if I find myself. . . available. . ."
                    else:
                            $ EmmaX.change_face("sly",1,Brows="confused")
                            if "mono" not in EmmaX.daily_history:
                                    $ EmmaX.change_stat("love", 90, -2)
                            ch_e "I wasn't aware that I needed your permission."
                    if "mono" not in EmmaX.daily_history:
                            $ EmmaX.change_stat("obedience", 90, 3)
                    if "mono" in EmmaX.Traits:
                            $ EmmaX.Traits.remove("mono")
                    $ EmmaX.AddWord(1,0,"mono") #Daily
            "Never mind.":
                pass
        return

# end Emma monogamy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Emma_Jumped:
        #called from Emma_Settings to ask her not to jump you
        ch_p "Hey, Remember that time you threw yourself at me?"
        $ EmmaX.change_face("sly",1,Brows="confused")
        ch_e "I believe I recall something like that."
        menu:
            ch_e "What of it?"
            "Could you maybe just ask instead?" if "chill" not in EmmaX.Traits:
                    if EmmaX.Thirst >= 60 and not Approvalcheck(EmmaX, 1600, "LO", TabM=0):
                            #she's too thirsty
                            $ EmmaX.change_face("sly",1)
                            if "chill" not in EmmaX.daily_history:
                                    $ EmmaX.change_stat("obedience", 90, -2)
                            ch_e "I do have certain. . . needs that must be met."
                            ch_e "Stay on your toes."
                            return
                    elif Approvalcheck(EmmaX, 1100, "LO", TabM=0) and EmmaX.love >= EmmaX.obedience:
                            #she cares
                            $ EmmaX.change_face("sly",1)
                            if "chill" not in EmmaX.daily_history:
                                    $ EmmaX.change_stat("love", 90, 1)
                            ch_e "I didn't intend to upset you, [EmmaX.Petname]. . ."
                            ch_e "I'll try to keep control. . ."
                    elif Approvalcheck(EmmaX, 600, "O", TabM=0):
                            #she is obedient
                            $ EmmaX.change_face("sly",1,Eyes="side")
                            ch_e "If that's what would make you comfortable. . ."
                    else:
                            #she doesn't care
                            $ EmmaX.change_face("sly",1,Brows="confused")
                            ch_e "I'll see what I can do about that."
                            ch_e "Stay on your toes."
                            return
                    if "chill" not in EmmaX.daily_history:
                            $ EmmaX.change_stat("obedience", 90, 3)
                    $ EmmaX.AddWord(1,0,"chill") #Daily
                    $ EmmaX.Traits.append("chill")
            "Don't bother me like that." if "chill" not in EmmaX.Traits:
                    if Approvalcheck(EmmaX, 900, "O", TabM=0):
                            #she is obedient
                            $ EmmaX.change_face("sly",1,Eyes="side")
                            ch_e "Oh, very well."
                    elif EmmaX.Thirst >= 60 and not Approvalcheck(EmmaX, 600, "O", TabM=0):
                            #she's too thirsty
                            $ EmmaX.change_face("sly",1)
                            if "chill" not in EmmaX.daily_history:
                                    $ EmmaX.change_stat("obedience", 90, -2)
                            ch_e "I do have certain. . . needs that must be met."
                            ch_e "Stay on your toes."
                            return
                    elif Approvalcheck(EmmaX, 450, "O", TabM=0):
                            #she is obedient
                            $ EmmaX.change_face("sly",1,Eyes="side")
                            ch_e "Well, I wouldn't want to be a \"bother\". . ."
                    elif Approvalcheck(EmmaX, 500, "LO", TabM=0) and not Approvalcheck(EmmaX, 500, "I", TabM=0):
                            #she cares
                            $ EmmaX.change_face("sly",1)
                            ch_e "Don't press your luck, [EmmaX.Petname]."
                            ch_e "I will try to give you some space, however. . ."
                    else:
                            #she doesn't care
                            $ EmmaX.change_face("sly",1,Brows="confused")
                            ch_e "I'll see what I can do about that."
                            ch_e "Stay on your toes."
                            return
                    if "chill" not in EmmaX.daily_history:
                            $ EmmaX.change_stat("obedience", 90, 3)
                    $ EmmaX.AddWord(1,0,"chill") #Daily
                    $ EmmaX.Traits.append("chill")
            "Knock yourself out.":
                    if Approvalcheck(EmmaX, 800, "L", TabM=0):
                            $ EmmaX.change_face("sly",1)
                            ch_e "You can count on it. . ."
                    elif Approvalcheck(EmmaX, 700, "O", TabM=0):
                            $ EmmaX.change_face("sly",1,Eyes="side")
                            ch_e "Very well."
                    else:
                            $ EmmaX.change_face("sly",1,Brows="confused")
                            if "chill" not in EmmaX.daily_history:
                                    $ EmmaX.change_stat("love", 90, -2)
                            ch_e "We'll see. . ."
                    if "chill" not in EmmaX.daily_history:
                            $ EmmaX.change_stat("obedience", 90, 3)
                    if "chill" in EmmaX.Traits:
                            $ EmmaX.Traits.remove("chill")
                    $ EmmaX.AddWord(1,0,"chill") #Daily
            "Um, never mind.":
                pass
        return

# end Emma jumped  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# start emma hungry  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_Hungry:
    if EmmaX.Chat[3]:
        ch_e "I do enjoy your taste. . ."
    elif EmmaX.Chat[2]:
        ch_e "You know, that serum of yours has a rather. . . familiar taste to it."
    else:
        ch_e "I do enjoy your taste. . ."
    $ EmmaX.Traits.append("hungry")
    return


# end emma hungry / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Emma Sexchat / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_SexChat:
    $ line = "Hmm? What did you want to talk about?" if not line else line
    while True:
            menu:
                ch_e "[line]"
                "My favorite thing to do is. . .":
                    if "setfav" in EmmaX.daily_history:
                        ch_e "I'm aware. You just told me earlier."
                    else:
                        menu:
                            "Sex.":
                                        $ EmmaX.change_face("sly")
                                        if EmmaX.PlayerFav == "sex":
                                            $ EmmaX.change_stat("lust", 80, 5)
                                            ch_e "I'm well aware. . ."
                                        elif EmmaX.Favorite == "sex":
                                            $ EmmaX.change_stat("love", 90, 5)
                                            $ EmmaX.change_stat("lust", 80, 10)
                                            ch_e "Oh. . . as chance would have it. . ."
                                        elif EmmaX.Sex:
                                            ch_e "I can see why."
                                        else:
                                            $ EmmaX.change_face("perplexed")
                                            ch_e "And exactly {i}who{/i} are you having sex {i}with?{/i}"
                                        $ EmmaX.PlayerFav = "sex"

                            "Anal.":
                                        $ EmmaX.change_face("sly")
                                        if EmmaX.PlayerFav == "anal":
                                            $ EmmaX.change_stat("lust", 80, 5)
                                            ch_e "So you've told me. . ."
                                        elif EmmaX.Favorite == "anal":
                                            $ EmmaX.change_stat("love", 90, 5)
                                            $ EmmaX.change_stat("lust", 80, 10)
                                            ch_e "{i}Mine too{/i}. . ."
                                        elif EmmaX.Anal >= 10:
                                            ch_e "It certainly is a workout. . ."
                                        elif not EmmaX.Anal:
                                            $ EmmaX.change_face("perplexed")
                                            ch_e "Who's ass {i}are{/i} you fucking?"
                                        else:
                                            $ EmmaX.change_face("bemused")
                                            ch_e "Yes, you did seem enthusiastic. . ."
                                        $ EmmaX.PlayerFav = "anal"

                            "Blowjobs.":
                                        $ EmmaX.change_face("sly")
                                        if EmmaX.PlayerFav == "blowjob":
                                            $ EmmaX.change_stat("lust", 80, 3)
                                            ch_e "Yes, so you've said. . ."
                                        elif EmmaX.Favorite == "blowjob":
                                            $ EmmaX.change_stat("love", 90, 5)
                                            $ EmmaX.change_stat("lust", 80, 5)
                                            ch_e "Hmm, you are delicious. . ."
                                        elif EmmaX.Blow >= 10:
                                            ch_e "I certainly can't complain . . ."
                                        elif not EmmaX.Blow:
                                            $ EmmaX.change_face("perplexed")
                                            ch_e "Oh? Is some little whore sucking you off?"
                                        else:
                                            $ EmmaX.change_face("bemused")
                                            ch_e "Yes, I enjoy it as well. . . ."
                                        $ EmmaX.PlayerFav = "blowjob"

                            "Titjobs.":
                                        $ EmmaX.change_face("sly")
                                        if EmmaX.PlayerFav == "titjob":
                                            $ EmmaX.change_stat("lust", 80, 5)
                                            ch_e "So you're said. . ."
                                        elif EmmaX.Favorite == "titjob":
                                            $ EmmaX.change_stat("love", 90, 5)
                                            $ EmmaX.change_stat("lust", 80, 7)
                                            ch_e "I really enjoy it too. . ."
                                        elif EmmaX.Tit >= 10:
                                            ch_e "I can't imagine why . . ."
                                        elif not EmmaX.Tit:
                                            $ EmmaX.change_face("perplexed")
                                            ch_e "Oh, is someone else providing that service?"
                                        else:
                                            $ EmmaX.change_face("bemused")
                                            ch_e "I can understand why. . ."
                                        $ EmmaX.PlayerFav = "titjob"

                            "Footjobs.":
                                        $ EmmaX.change_face("sly")
                                        if EmmaX.PlayerFav == "footjob":
                                            $ EmmaX.change_stat("lust", 80, 5)
                                            ch_e "Yes, so you've said. . ."
                                        elif EmmaX.Favorite == "footjob":
                                            $ EmmaX.change_stat("love", 90, 5)
                                            $ EmmaX.change_stat("lust", 80, 7)
                                            ch_e "It certainly is a diversion. . ."
                                        elif EmmaX.Foot >= 10:
                                            ch_e "Yes, it certainly is a workout . . ."
                                        elif not EmmaX.Foot:
                                            $ EmmaX.change_face("perplexed")
                                            ch_e "Oh, is some little skank offering footsies now?"
                                        else:
                                            $ EmmaX.change_face("bemused")
                                            ch_e "It certainly is a diversion. . ."
                                        $ EmmaX.PlayerFav = "footjob"

                            "Handjobs.":
                                        $ EmmaX.change_face("sly")
                                        if EmmaX.PlayerFav == "handjob":
                                            $ EmmaX.change_stat("lust", 80, 5)
                                            ch_e "Yes, so you've said. . ."
                                        if EmmaX.Favorite == "handjob":
                                            $ EmmaX.change_stat("love", 90, 5)
                                            $ EmmaX.change_stat("lust", 80, 7)
                                            ch_e "It certainly is a diversion. . ."
                                        elif EmmaX.Hand >= 10:
                                            ch_e "Yes, it certainly is a workout . . ."
                                        elif not EmmaX.Hand:
                                            $ EmmaX.change_face("perplexed")
                                            ch_e "Oh, is some little skank offering handies now?"
                                        else:
                                            $ EmmaX.change_face("bemused")
                                            ch_e "It certainly is a diversion. . ."
                                        $ EmmaX.PlayerFav = "handjob"

                            "Feeling you up.":
                                        $ counter = EmmaX.FondleB + EmmaX.FondleT + EmmaX.SuckB + EmmaX.Hotdog
                                        $ EmmaX.change_face("sly")
                                        if EmmaX.PlayerFav == "fondle":
                                            $ EmmaX.change_stat("lust", 80, 3)
                                            ch_e "I've heard that before. . ."
                                        elif EmmaX.Favorite in ("hotdog","suck_breasts","fondle_breasts","fondle_thighs"):
                                            $ EmmaX.change_stat("love", 90, 5)
                                            $ EmmaX.change_stat("lust", 80, 5)
                                            ch_e "You do have a way with my body . ."
                                        elif not counter:
                                            $ EmmaX.change_face("perplexed")
                                            ch_e "I can't imagine who youre feeling up. Yet."
                                        else:
                                            $ EmmaX.change_face("bemused")
                                            ch_e "You have a very deft hand . . ."
                                        $ EmmaX.PlayerFav = "fondle"
                                        $ counter = 0

                            "Kissing you.":
                                        $ EmmaX.change_face("sly")
                                        if EmmaX.PlayerFav == "kiss you":
                                            $ EmmaX.change_stat("love", 90, 3)
                                            ch_e "I'm well aware. . ."
                                        elif EmmaX.Favorite == "kiss you":
                                            $ EmmaX.change_stat("love", 90, 5)
                                            $ EmmaX.change_stat("lust", 80, 5)
                                            ch_e "For some reason, the romantic in me agrees. . ."
                                        elif EmmaX.Kissed >= 10:
                                            ch_e "I love kissing you too . . ."
                                        elif not EmmaX.Kissed:
                                            $ EmmaX.change_face("perplexed")
                                            ch_e "Who {i}are{/i} you kissing, [EmmaX.Petname]?"
                                        else:
                                            $ EmmaX.change_face("bemused")
                                            ch_e "How romantic."
                                        $ EmmaX.PlayerFav = "kiss you"

                        $ EmmaX.daily_history.append("setfav")

                "What's your favorite thing to do?":
                                if not Approvalcheck(EmmaX, 800):
                                        $ EmmaX.change_face("perplexed")
                                        ch_e "I don't believe that's an appropriate question. . ."
                                else:
                                        if EmmaX.SEXP >= 50:
                                            $ EmmaX.change_face("sly")
                                            ch_e "You really should know already . ."
                                        else:
                                            $ EmmaX.change_face("bemused")
                                            $ EmmaX.Eyes = "side"
                                            ch_e "Hmm, I suppose I could tell you. . ."


                                        if not EmmaX.Favorite or EmmaX.Favorite == "kiss":
                                            ch_e "Call me a romantic, but I enjoy kissing you. . ."
                                        elif EmmaX.Favorite == "anal":
                                                ch_e "I really enjoy anal."
                                        elif EmmaX.Favorite == "eat_ass":
                                                ch_e "I enjoy it when you lick my asshole."
                                        elif EmmaX.Favorite == "finger_ass":
                                                ch_e "I enjoy it when you stick a finger in my ass."
                                        elif EmmaX.Favorite == "sex":
                                                ch_e "I like when you fuck me hard."
                                        elif EmmaX.Favorite == "eat_pussy":
                                                ch_e "I like when you lick my pussy."
                                        elif EmmaX.Favorite == "fondle_pussy":
                                                ch_e "I like when you finger me."
                                        elif EmmaX.Favorite == "blowjob":
                                                ch_e "I quite enjoy sucking you, is that a problem?"
                                        elif EmmaX.Favorite == "titjob":
                                                ch_e "I enjoy using my tits."
                                        elif EmmaX.Favorite == "footjob":
                                                ch_e "I do enjoy using my feet."
                                        elif EmmaX.Favorite == "handjob":
                                                ch_e "I enjoy stroking you off."
                                        elif EmmaX.Favorite == "hotdog":
                                                ch_e "I enjoy it when you grind against me."
                                        elif EmmaX.Favorite == "suck_breasts":
                                                ch_e "You are good at sucking my tits."
                                        elif EmmaX.Favorite == "fondle_breasts":
                                                ch_e "You are good at fondling my tits."
                                        elif EmmaX.Favorite == "fondle_thighs":
                                                ch_e "I enjoy when you massage my thighs."
                                        else:
                                                ch_e "I'm really not sure. . ."

                                # End Emma's favorite things.

                "Don't talk as much during sex." if "vocal" in EmmaX.Traits:
                        if "setvocal" in EmmaX.daily_history:
                            $ EmmaX.change_face("perplexed")
                            ch_e "You've made yourself clear on the matter."
                        else:
                            if Approvalcheck(EmmaX, 1000) and EmmaX.obedience <= EmmaX.love:
                                $ EmmaX.change_face("bemused")
                                $ EmmaX.change_stat("obedience", 90, 1)
                                ch_e "Oh, very well. . ."
                                $ EmmaX.Traits.remove("vocal")
                            elif Approvalcheck(EmmaX, 700, "O"):
                                $ EmmaX.change_face("sadside")
                                $ EmmaX.change_stat("obedience", 90, 1)
                                ch_e "I suppose I could, [EmmaX.Petname]."
                                $ EmmaX.Traits.remove("vocal")
                            elif Approvalcheck(EmmaX, 600):
                                $ EmmaX.change_face("sly")
                                $ EmmaX.change_stat("love", 90, -3)
                                $ EmmaX.change_stat("obedience", 50, -1)
                                $ EmmaX.change_stat("inhibition", 90, 5)
                                ch_e "Don't presume to tell me what to say, [EmmaX.Petname]."
                            else:
                                $ EmmaX.change_face("angry")
                                $ EmmaX.change_stat("love", 90, -5)
                                $ EmmaX.change_stat("obedience", 60, -3)
                                $ EmmaX.change_stat("inhibition", 90, 10)
                                ch_e "I'll say what I wish, and you'll enjoy it."

                            $ EmmaX.daily_history.append("setvocal")
                "Talk dirty to me during sex." if "vocal" not in EmmaX.Traits:
                        if "setvocal" in EmmaX.daily_history:
                            $ EmmaX.change_face("perplexed")
                            ch_e "We've discussed this already."
                        else:
                            if Approvalcheck(EmmaX, 1000) and EmmaX.obedience <= EmmaX.love:
                                $ EmmaX.change_face("sly")
                                $ EmmaX.change_stat("obedience", 90, 2)
                                ch_e "Mmmm, I believe I can do that. . ."
                                $ EmmaX.Traits.append("vocal")
                            elif Approvalcheck(EmmaX, 700, "O"):
                                $ EmmaX.change_face("sadside")
                                $ EmmaX.change_stat("obedience", 90, 2)
                                ch_e "If that's what you wish, [EmmaX.Petname]."
                                $ EmmaX.Traits.append("vocal")
                            elif Approvalcheck(EmmaX, 600):
                                $ EmmaX.change_face("sly")
                                $ EmmaX.change_stat("obedience", 90, 3)
                                ch_e "I suppose I could, [EmmaX.Petname]."
                                $ EmmaX.Traits.append("vocal")
                            else:
                                $ EmmaX.change_face("angry")
                                $ EmmaX.change_stat("inhibition", 90, 5)
                                ch_e "If I feel like it."

                            $ EmmaX.daily_history.append("setvocal")
                        # End Emma Dirty Talk

                "Don't do your own thing as much during sex." if "passive" not in EmmaX.Traits:
                        if "initiative" in EmmaX.daily_history:
                            $ EmmaX.change_face("perplexed")
                            ch_e "I believe we've discussed this."
                        else:
                            if Approvalcheck(EmmaX, 1000) and EmmaX.obedience <= EmmaX.love:
                                $ EmmaX.change_face("bemused")
                                $ EmmaX.change_stat("obedience", 90, 1)
                                ch_e "Oh, so you want to take charge? . ."
                                $ EmmaX.Traits.append("passive")
                            elif Approvalcheck(EmmaX, 700, "O"):
                                $ EmmaX.change_face("sadside")
                                $ EmmaX.change_stat("obedience", 90, 1)
                                ch_e "I'll await your instruction, [EmmaX.Petname]."
                                $ EmmaX.Traits.append("passive")
                            elif Approvalcheck(EmmaX, 600):
                                $ EmmaX.change_face("sly")
                                $ EmmaX.change_stat("love", 90, -3)
                                $ EmmaX.change_stat("obedience", 50, -1)
                                $ EmmaX.change_stat("inhibition", 90, 5)
                                ch_e "Oh, you don't mean that, [EmmaX.Petname]."
                            else:
                                $ EmmaX.change_face("angry")
                                $ EmmaX.change_stat("love", 90, -5)
                                $ EmmaX.change_stat("obedience", 60, -3)
                                $ EmmaX.change_stat("inhibition", 90, 10)
                                ch_e "You wish."

                            $ EmmaX.daily_history.append("initiative")
                "Take more initiative during sex." if "passive" in EmmaX.Traits:
                        if "initiative" in EmmaX.daily_history:
                                $ EmmaX.change_face("perplexed")
                                ch_e "I believe we've discussed this."
                        else:
                            if Approvalcheck(EmmaX, 1000) and EmmaX.obedience <= EmmaX.love:
                                $ EmmaX.change_face("bemused")
                                $ EmmaX.change_stat("obedience", 90, 1)
                                ch_e "Oh, you know that I will. . ."
                                $ EmmaX.Traits.remove("passive")
                            elif Approvalcheck(EmmaX, 700, "O"):
                                $ EmmaX.change_face("sadside")
                                $ EmmaX.change_stat("obedience", 90, 1)
                                ch_e "I can do that, [EmmaX.Petname]."
                                $ EmmaX.Traits.remove("passive")
                            elif Approvalcheck(EmmaX, 600):
                                $ EmmaX.change_face("sly")
                                $ EmmaX.change_stat("obedience", 90, 3)
                                ch_e "I suppose I might, [EmmaX.Petname]."
                                $ EmmaX.Traits.remove("passive")
                            else:
                                $ EmmaX.change_face("angry")
                                $ EmmaX.change_stat("inhibition", 90, 5)
                                ch_e "We'll see."

                            $ EmmaX.daily_history.append("initiative")


                "About getting Jumped" if "jumped" in EmmaX.History:
                        call Emma_Jumped

                "About that \"mind screen\"" if "screen" in EmmaX.Traits or "noscreen" in EmmaX.Traits:
                        ch_e "You mean how I can make Charles ignore us sometimes?"
                        menu:
                            extend ""
                            "Yeah, do that." if "noscreen" in EmmaX.Traits:
                                ch_e "lovely. . ."
                                $ EmmaX.Traits.append("screen")
                            "Don't do that anymore, I want him to know." if "screen" in EmmaX.Traits:
                                ch_e "Oh, you are a naughty one."
                                if Approvalcheck(EmmaX, 900, "OI"):
                                        $ EmmaX.change_face("sad")
                                        ch_e "Very well, we won't do that."
                                        $ EmmaX.change_face("bemused")
                                        $ EmmaX.Traits.append("noscreen")
                                else:
                                        ch_e "However, I still don't appreciate his interference."
                                        ch_e "I'll use the screen anyway."
                            "Never mind.":
                                pass

                "About when you masturbate":
                        call NoFap(EmmaX)

                "Have you considered maybe having some fun in public?" if "taboocheck" not in EmmaX.History and "taboo" not in EmmaX.History:
                        call Emma_Taboo_Talk
                "We talked about maybe having some fun in public?" if "taboocheck" in EmmaX.History and "taboo" not in EmmaX.History:
                        call Emma_Taboo_Talk

                "Have you considered maybe having a threesome?" if "threecheck" not in EmmaX.History and "three" not in EmmaX.History:
                        call Emma_Threecheck
                "We talked about maybe having a threesome?" if "threecheck" in EmmaX.History and "three" not in EmmaX.History:
                        call Emma_Threecheck

                "Never Mind" if line == "Hmm? What did you want to talk about?":
                        return
                "That's all." if line != "Hmm? What did you want to talk about?":
                        return
            if line == "Yeah, what did you want to talk about?":
                $ line = "Anything else?"
    return
# End Emma Sexchat / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

## Emma Chitchat / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_Chitchat(O=0, Options = ["default","default","default"]):
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:
        if EmmaX not in Digits:
                if Approvalcheck(EmmaX, 850, "LI"):
                    ch_e "If you'd like to reach me. . . after hours, here's my number."
                    $ Digits.append(EmmaX)
                    return
                elif Approvalcheck(EmmaX, 500, "OI"):
                    ch_e "I should let you know how to contact me."
                    $ Digits.append(EmmaX)
                    return

        if "hungry" not in EmmaX.Traits and (EmmaX.Swallow + EmmaX.Chat[2]) >= 10 and EmmaX.location == bg_current:  #She's swallowed a lot
                    call Emma_Hungry
                    return
        if bg_current != "bg_restaurant" and bg_current != "HW Party" and (not Taboo or Approvalcheck(EmmaX, 800, "I")):
                    if EmmaX.location == bg_current and EmmaX.Thirst >= 30 and "refused" not in EmmaX.daily_history and "quicksex" not in EmmaX.daily_history:
                            $ Girl.change_face("sly",1,Eyes="down")
                            ch_e "I've got an itch. . . "
                            "[EmmaX.name] draws her hand down her body and grazes her pussy."
                            $ Girl.change_face("sly",1)
                            ch_e ". . think you can scratch it?"
                            call Quick_Sex(EmmaX)
                            return

#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
        if "classcaught" in EmmaX.Traits:
            if "caught" in EmmaX.daily_history and "caught chat" not in EmmaX.daily_history:
                $ Options.append("caught")
            if "screen" not in EmmaX.Traits and "noscreen" not in EmmaX.Traits and "screen" in JeanX.Traits:
                $ Options.append("screen")
            if EmmaX.Event[0] and "key" not in EmmaX.Chat:
                $ Options.append("key")
            if "lover" in EmmaX.Petnames and Approvalcheck(EmmaX, 900, "L"): # luvy dovey
                $ Options.append("luv")

            if Player.cologne and "cologne_chat" not in EmmaX.daily_history:
                $ Options.append(Player.cologne)

            if EmmaX.Date >= 1 and bg_current != "bg_restaurant":
                #if you've dated before
                $ Options.append("dated")
            if "cheek" in EmmaX.daily_history and "cheek" not in EmmaX.Chat:
                #If you've touched her cheek today
                $ Options.append("cheek")
            if EmmaX.Kissed >= 5:
                #if you've kissed a few times
                $ Options.append("kissed")
            if "dangerroom" in Player.daily_history:
                #If you've been in the danger room today
                $ Options.append("dangerroom")
            if "showered" in EmmaX.daily_history:
                #If you've caught Emma showering today
                $ Options.append("showercaught")
            if "fondle_breasts" in EmmaX.daily_history or "fondle_pussy" in EmmaX.daily_history or "fondle_ass" in EmmaX.daily_history:
                #If you've fondled Emma today
                $ Options.append("fondled")
            if "Dazzler and Longshot" in EmmaX.Inventory and "256 Shades of Grey" in EmmaX.Inventory and "Avengers Tower Penthouse" in EmmaX.Inventory:
                #If you've given Emma the books
                if "book" not in EmmaX.Chat:
                    $ Options.append("booked")
            if "lace bra" in EmmaX.Inventory or "lace panties" in EmmaX.Inventory:
                #If you've given Emma the lingerie
                if "lingerie" not in EmmaX.Chat:
                    $ Options.append("lingerie")

            if "seenpeen" in EmmaX.History:
                $ Options.append("seenpeen")
            if "topless" in EmmaX.History:
                $ Options.append("topless")
            if "bottomless" in EmmaX.History:
                $ Options.append("bottomless")

            if EmmaX.Hand:
                #If Emma's given a handjob
                $ Options.append("handjob")
            if EmmaX.Swallow:
                #If Emma's swallowed before
                $ Options.append("swallowed")
            if "cleaned" in EmmaX.daily_history or "painted" in EmmaX.daily_history:
                #If Emma's been facialed
                $ Options.append("facial")
            if EmmaX.Sleep:
                #If Emma's slept over
                $ Options.append("sleep")
            if EmmaX.CreamP or EmmaX.CreamA:
                #If Emma's been creampied
                $ Options.append("creampie")
            if EmmaX.Sex or EmmaX.Anal:
                #If Emma's been sexed
                $ Options.append("sexed")
            if EmmaX.Anal:
                #If Emma's been analed
                $ Options.append("anal")
            if "public" in EmmaX.History and "public" not in EmmaX.Chat:
                $ Options.append("public")

            if (bg_current == "bg_emma" or bg_current == "bg_player") and "relationship" not in EmmaX.daily_history:
                if "lover" not in EmmaX.Petnames and EmmaX.love >= 950 and EmmaX.Event[6] != 20: # EmmaX.Event[6]
                    $ Options.append("lover?")
                elif "sir" not in EmmaX.History and EmmaX.obedience >= 500: # EmmaX.Event[7]
                    $ Options.append("sir?")
                elif "daddy" not in EmmaX.Petnames and Approvalcheck(EmmaX, 750, "L") and Approvalcheck(EmmaX, 500, "O") and Approvalcheck(EmmaX, 500, "I"): # EmmaX.Event[5]
                    $ Options.append("daddy?")
                elif "master" not in EmmaX.History and EmmaX.obedience >= 800 and "sir" in EmmaX.Petnames: # EmmaX.Event[8]
                    $ Options.append("master?")
                elif "sex friend" not in EmmaX.Petnames and EmmaX.inhibition >= 500 and bg_current == "bg_classroom" and time_index == 2: # EmmaX.Event[9]
                    $ Options.append("sexfriend?")
                elif "fuck buddy" not in EmmaX.Petnames and EmmaX.inhibition >= 800 and bg_current != EmmaX.location: # EmmaX.Event[10]
                    $ Options.append("fuckbuddy?")


        if not Approvalcheck(EmmaX, 300):            #She dislikes you
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one

    if Options[0] == "mandrill":
        $ EmmaX.daily_history.append("cologne_chat")
        $ EmmaX.change_face("confused")
        ch_e "(sniff, sniff). . . you aren't using that cheap baboon musk, are you? . ."
        $ EmmaX.change_face("perplexed", 1)
        ch_e ". . . though I suppose. . . he wasn't that bad. . ."
    elif Options[0] == "purple":
        $ EmmaX.daily_history.append("cologne_chat")
        $ EmmaX.change_face("sly",1)
        ch_e "(sniff, sniff). . . huh, what's that smell? . ."
        ch_e ". . . was there anything I could do for you?"
    elif Options[0] == "corruption":
        $ EmmaX.daily_history.append("cologne_chat")
        $ EmmaX.change_face("confused")
        ch_e "(sniff, sniff). . . that's. . . ripe. . ."
        $ EmmaX.change_face("sly")
        ch_e ". . . I may have some. . . purpose for you later. . ."

    elif Options[0] == "caught": # Xavier's caught you
            $ EmmaX.change_face("angry", Eyes="side")
            if "caught chat" in EmmaX.Chat:
                    ch_e "I'm getting rather tired of getting dragged into Charles' office."
                    ch_e "Perhaps we ought to be more. . . discrete."
                    if not Approvalcheck(EmmaX, 500, "I"):
                        $ EmmaX.change_face("sly", Eyes="side")
                        ch_e "Sometimes. . ."
            else:
                    ch_e "Well that was certainly unpleasant."
                    ch_e "Xavier talked my ear off for at least an hour."
                    ch_e "Some nonsense about \"the responsibilities of an educator.\""
                    ch_e "I'll have you know, I take my responsibilities to my students. . ."
                    $ EmmaX.change_face("sly")
                    ch_e "{i}very{/i} seriously. . ."
                    if not Approvalcheck(EmmaX, 500, "I"):
                        ch_e "I don't thing we should be so forward in public anymore."
                    else:
                        ch_e "I did enjoy seeing the old buzzard so worked up though. . ."
                    $ EmmaX.Chat.append("caught chat")

    elif Options[0] == "screen": # Xavier's caught you
            $ EmmaX.change_face("angry")
            ch_e "Charles!"
            ch_e "I'm tired of him interfering in our business!"
            $ EmmaX.change_face("surprised")
            ch_e "Oh!"
            $ EmmaX.change_face("sly")
            ch_e "I've had an idea."
            ch_e "I -could- use my own powers to neutralize his, make it more likely that he'll ignore us."
            menu:
                "Sure, that sounds good.":
                    ch_e "lovely. . ."
                    $ EmmaX.Traits.append("screen")
                "Nah, I want him to know.":
                    ch_e "Oh, you are a naughty one."
                    if Approvalcheck(EmmaX, 900, "OI"):
                            $ EmmaX.change_face("sad")
                            ch_e "Very well, we won't do that."
                            $ EmmaX.change_face("bemused")
                            $ EmmaX.Traits.append("noscreen")
                    else:
                            ch_e "Even so, I don't appreciate his interference."
                            ch_e "I'll use the screen anyway."
                            $ EmmaX.Traits.append("screen")
    elif Options[0] == "key": # you have her key
            if EmmaX.SEXP <= 15:
                ch_e "Now just because I gave you my room key, doesn't mean you shouldn't knock. . ."
            else:
                ch_e "I gave you that key for a reason, you might want to use it sometime. . ."
            $ EmmaX.Chat.append("key")

    elif Options[0] == "cheek":
            #Emma's response to having her cheek touched.
            ch_e "Earlier, you brushed my cheek. . ."
            ch_p "Yeah?  Was that okay?"
            if Approvalcheck(EmmaX, 600, "L"):
                    $ EmmaX.change_face("smile",1)
                    ch_e "Yes, it was. . . intimate."
                    $ EmmaX.Chat.append("cheek")
            elif Approvalcheck(EmmaX, 800):
                    $ EmmaX.change_face("normal",1,Eyes="side")
                    ch_e "I. . . suppose so, [EmmaX.Petname]."
            else:
                    $ EmmaX.change_face("confused",1,Eyes="side")
                    ch_e "I just found it to be a bit. . . forward."


    elif Options[0] == "dated":
            #Emma's response to having gone on a date with the Player.
            ch_e "You should know, I enjoyed our last date.  We should do that again sometime."

    elif Options[0] == "kissed":
            #Emma's response to having been kissed by the Player.
            $ EmmaX.change_face("sly",1)
            ch_e "You have some remarkably skilled lips, [EmmaX.Petname]."
            menu:
                extend ""
                "Hey. . .when you're good, you're good.":
                        $ EmmaX.change_face("smile",1)
                        ch_e "Oh, don't let it get to your head."
                        ch_e "-unless you're interested in sharing."
                "No. You think?":
                        ch_e "Oh, learn to take a compliment, [EmmaX.Petname]."

    elif Options[0] == "dangerroom":
            #Emma's response to Player working out in the Danger Room while Emma is present
            $ EmmaX.change_face("sly",1)
            ch_e "I caught your last Danger Room session,[EmmaX.Petname]."
            ch_e "You certainly do. . . fill out that uniform."

    elif Options[0] == "showercaught":
            #Emma's response to being caught in the shower.
            if "shower" in EmmaX.Chat:
                ch_e "Enjoy the show earlier?"
            else:
                ch_e "I do hope that my appearance in the shower earlier wasn't too distracting."
                $ EmmaX.Chat.append("shower")
                menu:
                    extend ""
                    "It was a total accident!  I promise!":
                            $ EmmaX.change_stat("love", 50, 5)
                            $ EmmaX.change_stat("love", 90, 2)
                            if Approvalcheck(EmmaX, 1000):
                                $ EmmaX.change_face("sly",1)
                                ch_e "Oh? so I can't count on a repeat performance?"
                            else:
                                $ EmmaX.change_face("smile")
                                ch_e "It happens, just don't make a habit of it."
                    "I only have eyes for you.":
                            $ EmmaX.change_stat("obedience", 40, 5)
                            if Approvalcheck(EmmaX, 1000) or Approvalcheck(EmmaX, 700, "L"):
                                    $ EmmaX.change_stat("love", 90, 3)
                                    $ EmmaX.change_face("sly",1)
                                    ch_e "Oh, I'm sure that's true. . ."
                                    ch_e "It is nice to hear though."
                            else:
                                    $ EmmaX.change_stat("love", 70, -5)
                                    $ EmmaX.change_face("angry", Eyes="side")
                                    ch_e "I suppose it's better than being stalked by one-eye over there."
                    "Totally on purpose. I regret nothing.":
                            if Approvalcheck(EmmaX, 1200):
                                    $ EmmaX.change_stat("love", 90, 3)
                                    $ EmmaX.change_stat("obedience", 70, 10)
                                    $ EmmaX.change_stat("inhibition", 50, 5)
                                    $ EmmaX.change_face("sly",1)
                                    ch_e "Welll. . . I suppose I can appreciate your honesty."
                                    $ EmmaX.change_face("sly",1, Eyes="side")
                                    ch_e ". . .if not for your lack of follow-through."
                            elif Approvalcheck(EmmaX, 800):
                                    $ EmmaX.change_stat("obedience", 60, 5)
                                    $ EmmaX.change_stat("inhibition", 50, 5)
                                    $ EmmaX.change_face("perplexed",2)
                                    ch_e "Hmm? I suppose I can't blame you for that."
                            else:
                                    $ EmmaX.change_stat("love", 50, -10)
                                    $ EmmaX.change_stat("love", 80, -10)
                                    $ EmmaX.change_stat("obedience", 50, 10)
                                    $ EmmaX.change_face("angry")
                                    ch_e "Unexpectedly honest, but still unacceptable."

    elif Options[0] == "fondled":
            #Emma's response to being felt up.
            if EmmaX.FondleB + EmmaX.FondleP + EmmaX.FondleA >= 10:
                ch_e "I'll need a helping hand later."
            else:
                ch_e "You've displayed some rather significant talents in. . . massage."
                ch_e "We may need to explore that further. . ."

    elif Options[0] == "booked":
            #Emma's response after a Player gives her the books from the shop.
            ch_e "I read the. . . books you gave me."
            menu:
                extend ""
                "Yeah? Did you like them?":
                        $ EmmaX.change_face("sly",2)
                        ch_e "They were a bit simplistic, but certainly inspirational."
                "Good. You looked like you could use to learn a thing or two from them.":
                        $ EmmaX.change_stat("love", 90, 3)
                        $ EmmaX.change_stat("inhibition", 50, 10)
                        $ EmmaX.change_face("sly")
                        ch_e "Oh, [EmmaX.Petname], the things I could teach those authors would leave them in the hospital."
            $ EmmaX.Blush = 1
            $ EmmaX.Chat.append("book")

    elif Options[0] == "lingerie":
            #Emma's response to being given lingerie.
            $ EmmaX.change_face("sly")
            ch_e "[EmmaX.Petname], I wanted to thank you again for the. . .{i}clothing{/i} you bought me."
            ch_e "They look wonderful."
            $ EmmaX.Chat.append("lingerie")

    elif Options[0] == "handjob":
            #Emma's response after giving the Player a handjob.
            $ EmmaX.change_face("sly", Eyes="side")
            ch_e "You know, I was thinking about my hand,"
            $ EmmaX.change_face("sly")
            ch_e "on your cock. . ."
            ch_e "Oh, that expression is priceless. . ."
            ch_e "I suppose I'll have to repeat that service sometime. . ."

    elif Options[0] == "blowjob":
            if "blowjob" not in EmmaX.Chat:
                    #Emma's response after giving the Player a blowjob.
                    $ EmmaX.change_face("sly",2)
                    ch_e "You know, [EmmaX.Petname], you have a very unique flavor to you."
                    ch_p "Oh?"
                    ch_e "Your cock, I mean."
                    ch_e "Very. . . satisfying."
                    menu:
                        extend ""
                        "Well, there's always more where that came from.":
                                    $ EmmaX.change_stat("love", 90, 5)
                                    $ EmmaX.change_stat("inhibition", 60, 10)
                                    $ EmmaX.change_face("sly")
                                    ch_e "I'll have to take you up on that."
                        "I'm glad it measured up to all those other guys.":
                                if Approvalcheck(EmmaX, 300, "I") or not Approvalcheck(EmmaX, 800):
                                    $ EmmaX.change_stat("obedience", 60, 10)
                                    $ EmmaX.change_stat("inhibition", 50, 10)
                                    $ EmmaX.change_face("smile",1)
                                    ch_e "Oh, it certainly managed that."
                                else:
                                    $ EmmaX.change_stat("love", 80, -2)
                                    $ EmmaX.change_stat("obedience", 70, 10)
                                    $ EmmaX.change_stat("inhibition", 50, 5)
                                    $ EmmaX.change_face("sly")
                                    ch_e "Are you trying to imply something about my. . . experience?"
                    $ EmmaX.Blush = 1
                    $ EmmaX.Chat.append("blowjob")
            else:
                    $ line = renpy.random.choice(["You've a taste that's easy to acquire.",
                            "My jaw is a bit sore lately.",
                            "If you need some. . . attention, let me know.",
                            "Mmmm. . . [she mimes her tongue knocking against her cheek.]"])
                    ch_e "[line]"

    elif Options[0] == "swallowed":
            #Emma's response after swallowing the Player's cum.
            if "swallow" in EmmaX.Chat:
                ch_e "I think I'd like another taste of your. . . essence."
            else:
                ch_e "You certainly have a unique flavor to your semen, [EmmaX.Petname]."
                $ EmmaX.change_face("sly",1)
                ch_e "Very. . . envigorating. . ."
                $ EmmaX.Chat.append("swallow")

    elif Options[0] == "facial":
            #Emma's response after taking a facial from the Player.
            $ EmmaX.change_face("sexy")
            ch_e "You know, perhaps you could try to keep it away from my eyes next time?"

    elif Options[0] == "sleepover":
            #Emma's response after sleeping with the Player.
            ch_e "You're so restless in your sleep, it gives me. . . ideas."

    elif Options[0] == "creampie":
            #Another of Emma's responses after having sex with the Player.
            "[EmmaX.name] draws close to you so she can whisper into your ear."
            ch_e "I can still feel you. . .running down the inside of my thigh."

    elif Options[0] == "sexed":
            #A final response from Emma after having sex with the Player.
            $ EmmaX.change_face("sexy",2)
            ch_e "Since being with you, I have a lot more to think about, after class. . ."

    elif Options[0] == "anal":
            #Emma's response after getting anal from the Player.
            $ EmmaX.change_face("sly",1)
            ch_e "It's been a while since I've had anyone use the back door."
            $ EmmaX.change_face("sexy")
            ch_e "I'm glad you \"went there.\""

    elif Options[0] == "seenpeen": # first seen peen skipped
            $ EmmaX.change_face("sly",1)
            ch_e "Perhaps I should have mentioned it earlier,"
            $ EmmaX.change_face("sly",1, Eyes="down")
            ch_e "That cock you've got is certainly an interesting specimen."
            $ EmmaX.change_face("bemused",1)
            $ EmmaX.change_stat("love", 50, 5)
            $ EmmaX.change_stat("love", 90, 10)
            $ EmmaX.History.remove("seenpeen")
    elif Options[0] == "topless": # first seen breasts skipped
            $ EmmaX.change_face("sly",1)
            ch_e "Out of curiosity, when you saw my breasts earlier. . ."
            ch_e "Was it everything you dreamed?"
            call Emma_First_TMenu
            $ EmmaX.History.remove("topless")
    elif Options[0] == "bottomless": # first seen pussy skipped
            $ EmmaX.change_face("sly",1)
            ch_e "I was wondering, when you saw me bottomless before. . ."
            ch_e "What did you think?"
            call Emma_First_BMenu
            $ EmmaX.History.remove("bottomless")

    elif Options[0] == "boyfriend?":
        call Emma_BF
    elif Options[0] == "lover?":
        call Emma_love
    elif Options[0] == "sir?":
        call Emma_Sub
    elif Options[0] == "master?":
        call Emma_Master
    elif Options[0] == "sexfriend?":
        call Emma_Sexfriend
    elif Options[0] == "fuckbuddy?":
        call Emma_Fuckbuddy
    elif Options[0] == "daddy?":
        call Emma_Daddy

    elif Options[0] == "public": # You had sex in public
                $ EmmaX.change_face("sly")
                ch_e "Hmm, well I suppose the cat's out of the bag now."
                $ EmmaX.change_face("sly", Eyes="side",Brows="angry")
                if "spotted" in EmmaX.daily_history:
                    ch_e "With that show we put on earlier, I doubt we can keep rumors from spreading."
                else:
                    ch_e "With that show we put on the other day, I doubt we can keep rumors from spreading."
                ch_e ". . ."
                $ EmmaX.change_face("sly")
                $ EmmaX.change_stat("obedience", 70, 10)
                $ EmmaX.change_stat("inhibition", 60, 10)
                $ EmmaX.change_stat("inhibition", 90, 10)
                ch_e "I suppose we'll just have to spread some more. . ."
                $ EmmaX.Chat.append("public")

    elif Options[0] == "hate": # trinty lower then 50:
        $ line = renpy.random.choice(["I'd rather keep this professional.",
                "If you have something to say, put it in writing.",
                "Back off.",
                "Leave me alone."])
        ch_e "[line]"

    else: #all else fell through. . .
            $ D20 = renpy.random.randint(1, 15)
            if D20 == 1:
                    $ EmmaX.change_face("smile")
                    ch_e "You did  lovely job on the quiz the other day."
            elif D20 == 2:
                    $ EmmaX.change_face("sad")
                    ch_e "I've had a miserable amount of paperwork lately."
                    $ EmmaX.change_face("bemused")
                    ch_e "Perhaps come by after class to help?"
            elif D20 == 3:
                    $ EmmaX.change_face("surprised")
                    ch_e "You should have seen what Miss Pryde was wearing earlier!"
            elif D20 == 4:
                    $ EmmaX.change_face("sad")
                    ch_e "Preparing for next week's test has been exhausting!"
            elif D20 == 5:
                    $ EmmaX.change_face("smile")
                    ch_e "It really is a lovely day for a walk. . ."
            elif D20 == 6:
                    $ EmmaX.change_face("startled")
                    ch_e "There have been some serious issues lately with Sentinel attacks."
            elif D20 == 7:
                    $ EmmaX.change_face("smile")
                    ch_e "I've just had a positive progress report on my work so far."
            elif D20 == 8:
                    $ EmmaX.change_face("sad")
                    ch_e "This is a lovely school, but I do miss the amenities of the big city."
            elif D20 == 9:
                    $ EmmaX.change_face("confused")
                    ch_e "Do you pick up that weird humming of Xavier's in your head, or is that just me?"
            elif D20 == 10:
                    $ EmmaX.change_face("smile")
                    ch_e "I think the class is picking up the recent study sessions."
            elif D20 == 11:
                    $ EmmaX.change_face("smile")
                    ch_e "I've been looking forward to my next workout session."
            elif D20 == 12:
                    $ EmmaX.change_face("sad")
                    ch_e "I'm not sure what to do with Rogue's grades, they're starting to slip."
            elif D20 == 13:
                    $ EmmaX.change_face("smile")
                    ch_e "Not that I'm a lush or anything, but I could really do for a drink."
            elif D20 == 14:
                    $ EmmaX.change_face("sad")
                    ch_e "There's been another attack on the news, deplorable."
            elif D20 == 15:
                    $ EmmaX.change_face("sadside")
                    ch_e "I think I must have pulled something during my workout yesterday."
                    $ EmmaX.change_face("sly",Mouth="normal")
                    ch_e "Perhaps you could work it out for me?"
            else:
                    $ EmmaX.change_face("startled")
                    ch_e "As students go, you're not intollerable."

    $ line = 0
    return

# start Emma_Names / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_Names(TempName=0):
    call LastNamer
    $ TempName = _return
    menu:
        ch_e "Oh? What would you like me to call you?"
        "[TempName]'s fine.":
            # ie "Mr. Zero"
            $ EmmaX.Petname = TempName
            ch_e "I assumed it was, [EmmaX.Petname]."
        "Call me by my name.":
            $ EmmaX.Petname = Player.name
            ch_e "If you'd rather, [EmmaX.Petname]."
        "Call me \"dear\"." if "dear" in EmmaX.Petnames:
            $ EmmaX.Petname = "dear"
            ch_e "Certainly, [EmmaX.Petname]."
        "Call me \"darling\"." if "darling" in EmmaX.Petnames:
            $ EmmaX.Petname = "darling"
            ch_e "Certainly, [EmmaX.Petname]."
        "Call me \"boyfriend\"." if "boyfriend" in EmmaX.Petnames:
            $ EmmaX.Petname = "boyfriend"
            ch_e "How pedestrian, but fine, [EmmaX.Petname]."
        "Call me \"lover\"." if "lover" in EmmaX.Petnames:
            $ EmmaX.Petname = "lover"
            ch_e "Certainly, [EmmaX.Petname]."
        "Call me \"sir\"." if "sir" in EmmaX.Petnames:
            $ EmmaX.Petname = "sir"
            ch_e "Yes, [EmmaX.Petname]."
        "Call me \"master\"." if "master" in EmmaX.Petnames:
            $ EmmaX.Petname = "master"
            ch_e "As you wish, [EmmaX.Petname]."
        "Call me \"sex friend\"." if "sex friend" in EmmaX.Petnames:
            $ EmmaX.Petname = "sex friend"
            ch_e "You naughty boy. Very well, [EmmaX.Petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in EmmaX.Petnames:
            $ EmmaX.Petname = "fuck buddy"
            ch_e "How nasty, \"[EmmaX.Petname]\"."
        "Call me \"daddy\"." if "daddy" in EmmaX.Petnames:
            $ EmmaX.Petname = "daddy"
            ch_e "Mmm, ok, [EmmaX.Petname]."
        "Nevermind.":
            return
    return
# end Emma_Names//////////////////////////////////////////////////////////

label Emma_Pet:
    while 1:
        menu:
            extend ""
            "Polite":
                menu:
                    extend ""
                    "I think I'll just call you Ms. Frost.":
                        $ EmmaX.Pet = "Ms. Frost"
                        $ EmmaX.name = "Ms. Frost"
                        ch_e "I don't see why not, [EmmaX.Petname]."

                    "I think I'll just call you Emma.":
                        if Approvalcheck(EmmaX, 700) or "classcaught" in EmmaX.History:
                            ch_e "I don't see why not, [EmmaX.Petname]."
                            $ EmmaX.Pet = "Emma"
                            $ EmmaX.name = "Emma"
                        else:
                            ch_e "I'd rather you didn't, [EmmaX.Petname]."

                    "I think I'll call you \"girl\".":
                        $ EmmaX.Pet = "girl"
                        if "boyfriend" in EmmaX.Petnames or Approvalcheck(EmmaX, 600, "L"):
                            $ EmmaX.change_face("sexy", 1)
                            ch_e "How droll, [EmmaX.Petname]."
                        else:
                            $ EmmaX.change_face("angry")
                            ch_e "I wouldn't, [EmmaX.Petname]."

                    "I think I'll call you \"boo\".":
                        $ EmmaX.Pet = "boo"
                        if "boyfriend" in EmmaX.Petnames or Approvalcheck(EmmaX, 800, "L"):
                            $ EmmaX.change_face("bemused", 1)
                            ch_e "How adorable, [EmmaX.Petname]."
                        else:
                            $ EmmaX.change_face("angry")
                            ch_e "I'm no such thing,  [EmmaX.Petname]."

                    "I think I'll call you \"bae\".":
                        $ EmmaX.Pet = "bae"
                        if "boyfriend" in EmmaX.Petnames or Approvalcheck(EmmaX, 800, "L"):
                            $ EmmaX.change_face("sexy", 1)
                            ch_e "I suppose I am your. . . \"bae?\""
                        else:
                            $ EmmaX.change_face("angry")
                            ch_e "What does that even mean?."

                    "I think I'll call you \"baby\".":
                        $ EmmaX.Pet = "baby"
                        if "boyfriend" in EmmaX.Petnames or Approvalcheck(EmmaX, 500, "L"):
                            $ EmmaX.change_face("sexy", 1)
                            ch_e "How precious."
                        else:
                            $ EmmaX.change_face("angry")
                            ch_e "I think I'm a bit. . . mature for that."

                    "I think I'll call you \"darling\".":
                        $ EmmaX.Pet = "darling"
                        if "boyfriend" in EmmaX.Petnames or Approvalcheck(EmmaX, 600, "L"):
                            ch_e "I do adore you, [EmmaX.Petname]."
                        else:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "A bit premature, [EmmaX.Petname]."

                    "I think I'll call you \"sweetie\".":
                        $ EmmaX.Pet = "sweetie"
                        if "boyfriend" in EmmaX.Petnames or Approvalcheck(EmmaX, 500, "L"):
                            ch_e "Really, [EmmaX.Petname]?"
                        else:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "Too saccharine, [EmmaX.Petname]."

                    "I think I'll call you \"sexy\".":
                        $ EmmaX.Pet = "sexy"
                        if "lover" in EmmaX.Petnames or Approvalcheck(EmmaX, 900):
                            $ EmmaX.change_face("sexy", 1)
                            ch_e "I can't argue there, [EmmaX.Petname]."
                        else:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "That may be a bit much, [EmmaX.Petname]."

                    "I think I'll call you \"lover\".":
                        $ EmmaX.Pet = "lover"
                        if "lover" in EmmaX.Petnames or Approvalcheck(EmmaX, 900, "L"):
                            $ EmmaX.change_face("sexy", 1)
                            ch_e "I do love you, [EmmaX.Petname]!"
                        else:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "Not in this lifetime, [EmmaX.Petname]."

                    "Back":
                        pass

            "Risky":
                menu:
                    "I think I'll call you \"slave\".":
                        $ EmmaX.Pet = "slave"
                        if "master" in EmmaX.Petnames or Approvalcheck(EmmaX, 900, "O"):
                            $ EmmaX.change_face("bemused", 1)
                            ch_e "As you wish, [EmmaX.Petname]."
                        else:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "I'm no man's slave, [EmmaX.Petname]."

                    "I think I'll call you \"pet\".":
                        $ EmmaX.Pet = "pet"
                        if "master" in EmmaX.Petnames or Approvalcheck(EmmaX, 600, "O"):
                            $ EmmaX.change_face("bemused", 1)
                            ch_e "So long as you make sure to pet me, [EmmaX.Petname]."
                        else:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "I doubt you'd want me for a pet, [EmmaX.Petname]."

                    "I think I'll call you \"slut\".":
                        $ EmmaX.Pet = "slut"
                        if "sex friend" in EmmaX.Petnames or Approvalcheck(EmmaX, 1000, "OI"):
                            $ EmmaX.change_face("sexy")
                            ch_e "I cant exactly disagree, [EmmaX.Petname]."
                        else:
                            $ EmmaX.change_face("angry", 1)
                            $ EmmaX.Mouth = "surprised"
                            ch_e "I would strongly reconsider that."

                    "I think I'll call you \"whore\".":
                        $ EmmaX.Pet = "whore"
                        if "fuckbuddy" in EmmaX.Petnames or Approvalcheck(EmmaX, 1100, "OI"):
                            $ EmmaX.change_face("sly")
                            ch_e "Only for you though. . ."
                        else:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "The last man to call me that no longer remembers his own name."

                    "I think I'll call you \"sugartits\".":
                        $ EmmaX.Pet = "sugartits"
                        if "sex friend" in EmmaX.Petnames or Approvalcheck(EmmaX, 1400):
                            $ EmmaX.change_face("sly", 1)
                            ch_e "They certainly are sweet. . ."
                        else:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "I expect you're better than that, [EmmaX.Petname]."

                    "I think I'll call you \"sex friend\".":
                        $ EmmaX.Pet = "sex friend"
                        if "sex friend" in EmmaX.Petnames or Approvalcheck(EmmaX, 600, "I"):
                            $ EmmaX.change_face("sly")
                            ch_e "Hm?"
                        else:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "Hopefully not in public, [EmmaX.Petname]."

                    "I think I'll call you \"fuckbuddy\".":
                        $ EmmaX.Pet = "fuckbuddy"
                        if "fuckbuddy" in EmmaX.Petnames or Approvalcheck(EmmaX, 700, "I"):
                            $ EmmaX.change_face("bemused")
                            ch_e "Well. . . alright."
                        else:
                            $ EmmaX.change_face("angry", 1)
                            $ EmmaX.Mouth = "surprised"
                            ch_e "How crass."

                    "I think I'll call you \"baby girl\".":
                        $ EmmaX.Pet = "baby girl"
                        if "daddy" in EmmaX.Petnames or Approvalcheck(EmmaX, 1200):
                            $ EmmaX.change_face("smile", 1)
                            ch_e "Adorable."
                        else:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "A bit inappropriate."

                    "I think I'll call you \"mommy\".":
                        $ EmmaX.Pet = "mommy"
                        if "mommy" in EmmaX.Pets or Approvalcheck(EmmaX, 1500):
                            $ EmmaX.change_face("sly", 1, Mouth="kiss")
                            ch_e "Oooh, [EmmaX.Petname]."
                        else:
                            $ EmmaX.change_face("angry")
                            ch_e "That's a bit much, [EmmaX.Petname]"

                    "Back":
                        pass

            "Nevermind.":
                return
    return

#label Emma_Namecheck(EmmaX.Pet = EmmaX.Pet, counter = 0, Ugh = 0):#$ Girl.namecheck() #checks reaction to petname

# start Emma_Rename//////////////////////////////////////////////////////////
label Emma_Rename:
        #Sets alternate names from Emma
        $ EmmaX.Mouth = "smile"
        ch_e "Yes, and?"
        menu:
            extend ""
            "I think \"Emma's\" a pretty name." if EmmaX.name != "Emma" and "Emma" in EmmaX.names:
                    $ EmmaX.name = "Emma"
                    ch_e "I've always been fond of it. . ."
            "I thought \"Ms. Frost\" sounded cool." if EmmaX.name != "Ms. Frost" and "Ms. Frost" in EmmaX.names:
                    $ EmmaX.name = "Ms. Frost"
                    if Approvalcheck(EmmaX, 1000, "LI"):
                            $ EmmaX.change_face("sly", 1)
                            if "namechange" not in EmmaX.daily_history:
                                    $ EmmaX.change_stat("obedience", 70, 2)
                                    $ EmmaX.change_stat("inhibition", 70, 3)
                            ch_e "Naughty boy. . ."
                    else:
                            ch_e "I suppose we could keep things professional. . ."
            "I liked the sound of \"White Queen.\"" if EmmaX.name != "White Queen" and "White Queen" in EmmaX.names:
                    $ EmmaX.name = "White Queen"
                    if not Approvalcheck(EmmaX, 500, "I"):
                            $ EmmaX.change_face("confused")
                            ch_e "Where have you heard that-"
                            $ EmmaX.change_face("sly", 2)
                            if "namechange" not in EmmaX.daily_history:
                                    $ EmmaX.change_stat("love", 80, 2)
                                    $ EmmaX.change_stat("obedience", 70, 2)
                                    $ EmmaX.change_stat("inhibition", 80, 3)
                            ch_e "Oh, you dirty, dirty boy. . ."
                    else:
                            $ EmmaX.change_face("confused")
                            ch_e "Oh, well, I suppose. . ."
                    $ EmmaX.change_face()
            "Nevermind.":
                    pass
        $ EmmaX.AddWord(1,0,"namechange")
        return
# end Emma_Rename//////////////////////////////////////////////////////////

# start Emma_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_Personality(counter = 0):
    if not EmmaX.Chat[4] or counter:
        "Since you're doing well in one area, you can convince Emma to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_e "Sure, what's up?"
        "More obedienceient. [[love to obedience]" if EmmaX.love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_e "Anything to humor you, [EmmaX.Petname]."
            $ EmmaX.Chat[4] = 1
        "Less Inhibited. [[love to Inhibition]" if EmmaX.love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_e "I don't see how I could be {i}less{/i} inhibited, but I can certainly try."
            $ EmmaX.Chat[4] = 2

        "Less Inhibited. [[obedience to Inhibition]" if EmmaX.obedience > 900:
            ch_p "I want you to be less inhibited."
            ch_e "If you say so."
            $ EmmaX.Chat[4] = 3
        "More Loving. [[obedience to love]" if EmmaX.obedience > 900:
            ch_p "I'd like you to learn to love me."
            ch_e "I'll try to."
            $ EmmaX.Chat[4] = 4

        "More obedienceient. [[Inhibition to obedience]" if EmmaX.inhibition > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_e "Does that get you off?"
            $ EmmaX.Chat[4] = 5

        "More Loving. [[Inhibition to love]" if EmmaX.inhibition > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_e "We do have fun. . ."
            $ EmmaX.Chat[4] = 6

        "I guess just do what you like. . .[[reset]" if EmmaX.Chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_e "As if I ever do anything else?"
            $ EmmaX.Chat[4] = 0
        "Repeat the rules":
            call Emma_Personality(1)
            return
        "Nevermind.":
            return
    return
# end Emma_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


## Emma's Clothes // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // //
label Emma_Clothes(Public=0,Bonus=0):
    if EmmaX.Taboo:
            if "exhibitionist" in EmmaX.Traits:
                ch_e "Mmmmm. . ."
            elif Approvalcheck(EmmaX, 900, TabM=4) or Approvalcheck(EmmaX, 400, "I", TabM=3):
                ch_e "This isn't really the appropriate place for it, however. . ."
                return #alter to be conditional
            else:
                ch_e "I'd rather discuss that in private."
                return
    elif Approvalcheck(EmmaX, 900, TabM=4) or Approvalcheck(EmmaX, 600, "L") or Approvalcheck(EmmaX, 300, "O"):
        ch_e "What about my style?"
    else:
        ch_e "I'll let you know when I care what you think."
        return

    if Girl != EmmaX or line == "Giftstore":
            #This culls returns if sent from another girl
            $ renpy.pop_call()
    $ line = 0
    $ Girl = EmmaX
    call shift_focus(Girl)

    $ Public = 0
    if "exhibitionist" in EmmaX.Traits:
            $ Public += 1
    if EmmaX.Rep <= 200:
            $ Public += 2
    elif EmmaX.Rep <= 400:
            $ Public += 1
    if "public" in EmmaX.History:
            $ Public += 2
    #This is a trait for if she's open to being sexy in public

label Emma_Wardrobe_Menu:
    $ primary_action = 1 # to prevent Focus swapping. . .
    $ EmmaX.change_face()
    while True:
        menu:
            ch_e "You wanted to discuss my clothing choices?"
            "Overshirts":
                        call Emma_Clothes_Over
            "Legwear":
                        call Emma_Clothes_Legs
            "Underwear":
                        call Emma_Clothes_Under
            "Accessories":
                        call Emma_Clothes_Misc
            "Outfits":
                        call Emma_Clothes_Outfits
            "Let's talk about what you wear around.":
                        call Clothes_Schedule(EmmaX)

            "Could I get a look at it?" if EmmaX.location != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(EmmaX,0,2)
                    if _return:
                        show PhoneSex zorder 150
                        ch_e "Ok, a quick shot for you. . ."
                    hide PhoneSex

            "Could I get a look at it?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(EmmaX,0,2)
                    if _return:
                        hide DressScreen
            "Would you be more comfortable behind a screen? (locked)" if EmmaX.Taboo:
                    pass
            "Would you be more comfortable behind a screen?" if EmmaX.location == bg_current and not EmmaX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    if Approvalcheck(EmmaX, 1500) or (EmmaX.SeenChest and EmmaX.SeenPussy):
                            ch_e "Oh, I think we can handle this."
                    else:
                            show DressScreen zorder 150
                            ch_e "Yes, this will be more comfortable."

            "Gift for you (locked)" if Girl.location != bg_current:
                            pass
            "Gift for you" if Girl.location == bg_current:
                            ch_p "I'd like to give you something."
                            call Gifts #(Girl)

            "Switch to. . .":
                    if renpy.showing('DressScreen'):
                            call OutfitShame(EmmaX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ EmmaX.OutfitChange()
                    $ EmmaX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ primary_action = 0
                    call Switch_Chat
                    if Girl != EmmaX:
                            ch_p "I wanted to talk about your clothes."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = EmmaX
                    call shift_focus(Girl)
            "Never mind, you look good like that.":
                    if "wardrobe" not in EmmaX.recent_history:
                            #Apply stat boosts only if it's the first time this turn
                            if EmmaX.Chat[1] <= 1:
                                    $ EmmaX.change_stat("love", 70, 15)
                                    $ EmmaX.change_stat("obedience", 40, 20)
                                    ch_e "I thought so as well."
                            elif EmmaX.Chat[1] <= 10:
                                    $ EmmaX.change_stat("love", 70, 5)
                                    $ EmmaX.change_stat("obedience", 40, 7)
                                    ch_e "Isn't it?"
                            elif EmmaX.Chat[1] <= 50:
                                    $ EmmaX.change_stat("love", 70, 1)
                                    $ EmmaX.change_stat("obedience", 40, 1)
                            $ EmmaX.recent_history.append("wardrobe")
                    if renpy.showing('DressScreen'):
                            call OutfitShame(EmmaX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ EmmaX.OutfitChange()
                    $ EmmaX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ EmmaX.Chat[1] += 1
                    $ primary_action = 0
                    return

        #Loops back up
        #return #jump Emma_Clothes
        #End of Emma Wardrobe Main Menu

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Emma_Clothes_Outfits:
        # Outfits
        "You should remember that one. [[Set Custom]":
                menu:
                    "Which slot would you like this saved in?"
                    "Custom 1":
                                call OutfitShame(EmmaX,3,1)
                    "Custom 2":
                                call OutfitShame(EmmaX,5,1)
                    "Custom 3":
                                call OutfitShame(EmmaX,6,1)
                    "Gym Clothes":
                                call OutfitShame(EmmaX,4,1)
                    "Sleepwear":
                                call OutfitShame(EmmaX,7,1)
                    "Swimwear":
                                call OutfitShame(EmmaX,10,1)
                    "Never mind":
                                pass
        "I really like that teacher's look you wear.":
                $ EmmaX.OutfitChange("casual1")
                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ EmmaX.Outfit = "casual1"
                        $ EmmaX.Shame = 0
                        ch_e "Yes, a very tasteful look."
                    "Let's try something else though.":
                        ch_e "Very well."

        "That combat uniform you have looks really nice on you.":
                $ EmmaX.OutfitChange("casual2")
                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ EmmaX.Outfit = "casual2"
                        $ EmmaX.Shame = 0
                        ch_e "I really enjoyed wearing that one."
                    "Let's try something else though.":
                        ch_e "Very well."

        "Remember that outfit we put together? [[Set a custom outfit] (locked)" if not EmmaX.Custom1[0] and not EmmaX.Custom2[0] and not EmmaX.Custom3[0]:
                        pass

        "Remember that outfit we put together?" if EmmaX.Custom1[0] or EmmaX.Custom2[0] or EmmaX.Custom3[0]:
                $ counter = 0
                while 1:
                    menu:
                        "Throw on Custom 1 (locked)" if not EmmaX.Custom1[0]:
                                pass
                        "Throw on Custom 1" if EmmaX.Custom1[0]:
                                $ EmmaX.OutfitChange("custom1")
                                $ counter = 3
                        "Throw on Custom 2 (locked)" if not EmmaX.Custom2[0]:
                                pass
                        "Throw on Custom 2" if EmmaX.Custom2[0]:
                                $ EmmaX.OutfitChange("custom2")
                                $ counter = 5
                        "Throw on Custom 3 (locked)" if not EmmaX.Custom3[0]:
                                pass
                        "Throw on Custom 3" if EmmaX.Custom3[0]:
                                $ EmmaX.OutfitChange("custom3")
                                $ counter = 6

                        "You should wear this one in private. (locked)" if not counter:
                                pass
                        "You should wear this one in private." if counter:
                                if counter == 5:
                                    $ EmmaX.Clothing[9] = "custom2"
                                elif counter == 6:
                                    $ EmmaX.Clothing[9] = "custom3"
                                else:
                                    $ EmmaX.Clothing[9] = "custom1"
                                ch_e "Ok, sure."

                        "On second thought, forget about that one outfit. . .":
                                menu:
                                    "Custom 1 [[clear custom 1]" if EmmaX.Custom1[0]:
                                        ch_e "Very well."
                                        $ EmmaX.Custom1[0] = 0
                                    "Custom 1 [[clear custom 1] (locked)" if not EmmaX.Custom1[0]:
                                        pass
                                    "Custom 2 [[clear custom 2]" if EmmaX.Custom2[0]:
                                        ch_e "Very well."
                                        $ EmmaX.Custom2[0] = 0
                                    "Custom 2 [[clear custom 2] (locked)" if not EmmaX.Custom2[0]:
                                        pass
                                    "Custom 3 [[clear custom 3]" if EmmaX.Custom3[0]:
                                        ch_e "Very well."
                                        $ EmmaX.Custom3[0] = 0
                                    "Custom 3 [[clear custom 3] (locked)" if not EmmaX.Custom3[0]:
                                        pass
                                    "Never mind, [[back].":
                                        pass

                        "You should wear this one out. [[choose outfit first](locked)" if not counter:
                                pass
                        "You should wear this one out." if counter:
                                call Custom_Out(EmmaX,counter)
                        "Ok, back to what we were talking about. . .":
                                $ counter = 0
                                return #jump Emma_Clothes

        "Gym Clothes?" if not EmmaX.Taboo or bg_current == "bg_dangerroom":
                $ EmmaX.OutfitChange("gym")


        "Sleepwear?" if not EmmaX.Taboo:
                if Approvalcheck(EmmaX, 1200):
                        $ EmmaX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(EmmaX)
                        if _return:
                            $ EmmaX.OutfitChange("sleep")

        "Swimwear? (locked)" if (EmmaX.Taboo and bg_current != "bg_pool") or not EmmaX.Swim[0]:
                $ EmmaX.OutfitChange("swimwear")
        "Swimwear?" if (not EmmaX.Taboo or bg_current == "bg_pool") and EmmaX.Swim[0]:
                $ EmmaX.OutfitChange("swimwear")

        "Halloween Costume?" if "halloween" in EmmaX.History:
                ch_e "Very well. . ."
                $ EmmaX.OutfitChange("costume")

        "Your birthday suit looks really great. . .":
                #Nude
                $ EmmaX.change_face("sly", 1)
                $ line = 0
                if not EmmaX.Chest and not EmmaX.Panties and not EmmaX.Over and not EmmaX.Legs and not EmmaX.Hose:
                    # if already naked (yes)
                    ch_e "Apparently so. . ."
                elif EmmaX.SeenChest and EmmaX.SeenPussy and Approvalcheck(EmmaX, 1200, TabM=(5-Public)):
                    #if you've seen it all and she likes you well enough (yes)
                    ch_e "I'll take that as an invitation. . ."
                    $ line = 1
                elif Approvalcheck(EmmaX, 2000, TabM=(5-Public)):
                    #if you haven't seen everything but she really likes you (yes)
                    ch_e "I suppose you've earned it. . ."
                    $ line = 1
                elif EmmaX.SeenChest and EmmaX.SeenPussy and Approvalcheck(EmmaX, 1200, TabM=0):
                    # if you've seen it but it's in public (no)
                    ch_e "As you're well aware, but this isn't the appropriate venue. . ."
                elif Approvalcheck(EmmaX, 2000, TabM=0):
                    #if you haven't seen everything but she really likes you and it's public (no)
                    ch_e "I assure you it is, but this isn't the appropriate venue. . ."
                elif Approvalcheck(EmmaX, 1000, TabM=0):
                    #if you haven't seen everything and she kinda likes you but it's public (no)
                    $ EmmaX.change_face("surprised", 1)
                    ch_e "I assure you that it is, but that's not the way to ask."
                    $ EmmaX.Blush = 0
                else:
                    # if she refuses. (no)
                    $ EmmaX.change_face("angry", 1)
                    ch_e "Not the worst line I've heard."
                    ch_e ". . . but close."

                if line:                                                            #If she got nude. . .
                    $ EmmaX.OutfitChange("nude")
                    "She strips down."
                    call Emma_First_Topless
                    call Emma_First_Bottomless(1)
                    $ EmmaX.change_face("sexy")
                    menu:
                        "You know, you should wear this one out. [[set current outfit]":
                            if "exhibitionist" in EmmaX.Traits:
                                $ EmmaX.change_face("sexy",2,Eyes="down")
                                ch_e "Mmmmm. . ."
                                $ EmmaX.Outfit = "nude"
                                $ EmmaX.change_stat("lust", 50, 10)
                                $ EmmaX.change_stat("lust", 70, 5)
                                $ EmmaX.Shame = 50
                                $ EmmaX.change_face("sexy",1)
                            elif Approvalcheck(EmmaX, 800, "I") or Approvalcheck(EmmaX, 2800, TabM=0):
                                ch_e "Oooh, that would cause quite a stir. . ."
                                $ EmmaX.Outfit = "nude"
                                $ EmmaX.Shame = 50
                            elif Approvalcheck(EmmaX, 400, "I") and Approvalcheck(EmmaX, 1200, TabM=0):
                                $ EmmaX.change_face("bemused", 1,Eyes="side")
                                ch_e "You shouldn't suggest such things. . ."
                            else:
                                $ EmmaX.change_face("sexy", 1,Eyes="surprised")
                                ch_e "Impossible."

                        "Let's try something else though.":
                            if "exhibitionist" in EmmaX.Traits:
                                ch_e "Too much for you to handle?"
                            elif Approvalcheck(EmmaX, 800, "I") or Approvalcheck(EmmaX, 2800, TabM=0):
                                $ EmmaX.change_face("bemused", 1)
                                ch_e "Because obviously I couldn't go around like this. . ."
                            else:
                                $ EmmaX.change_face("confused", 1)
                                ch_e "So long as it's just the two of us, I don't mind this."
                $ line = 0

        "Never mind":
            return #jump Emma_Clothes

    return #jump Emma_Clothes
    #End of Emma Outfits

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Emma_Clothes_Over:
        # Overshirts
        "Why don't you go with no [EmmaX.Over]?" if EmmaX.Over:
                $ EmmaX.change_face("bemused", 1)
                if Approvalcheck(EmmaX, 800, TabM=(3-Public)) and (EmmaX.Chest or EmmaX.SeenChest):
                    ch_e "Certainly."
                elif Approvalcheck(EmmaX, 600, TabM=0):
                    call Emma_NoBra
                    if not _return:
                        if not Approvalcheck(EmmaX, 1200):
                            call Display_DressScreen(EmmaX)
                            if not _return:
                                return #jump Emma_Clothes
                        else:
                                return #jump Emma_Clothes
                else:
                    call Display_DressScreen(EmmaX)
                    if not _return:
                            ch_e "I'm afraid not."
                            if not EmmaX.Chest:
                                ch_e "I'm indecent under this. . ."
                            return #jump Emma_Clothes
                $ line = EmmaX.Over
                $ EmmaX.Over = 0
                "She shrugs off her [line]."
                if not EmmaX.Chest and not renpy.showing('DressScreen'):
                        call Emma_First_Topless

        "Try on that white jacket you have." if EmmaX.Over != "jacket":
                $ EmmaX.change_face("bemused")
                if EmmaX.Chest or EmmaX.SeenChest or Approvalcheck(EmmaX, 500, TabM=(3-Public)):
                    ch_e "Yeah, ok."
                else:
                    call Display_DressScreen(EmmaX)
                    if not _return:
                            $ EmmaX.change_face("bemused", 1)
                            ch_e "I'm not sure this is appropriate without something more substantial underneath."
                            return #jump Emma_Clothes
                $ EmmaX.Over = "jacket"

        "Try on that white dress you have." if EmmaX.Over != "dress" and "halloween" in EmmaX.History:
                $ EmmaX.change_face("bemused")
                if EmmaX.Chest or EmmaX.SeenChest or Approvalcheck(EmmaX, 500, TabM=(3-Public)):
                    ch_e "Yeah, ok."
                else:
                    call Display_DressScreen(EmmaX)
                    if not _return:
                            $ EmmaX.change_face("bemused", 1)
                            ch_e "I'm not sure this is appropriate without something more substantial underneath."
                            return #jump Emma_Clothes
                menu:
                    ch_e "The whole thing, or just the top?"
                    "The whole dress.":
                            $ EmmaX.Legs = "dress"
                    "Just the top.":
                            pass
                $ EmmaX.Over = "dress"

        "Try on that lace nighty." if EmmaX.Over != "nighty":
                $ EmmaX.change_face("bemused")
                if EmmaX.Chest or EmmaX.SeenChest or Approvalcheck(EmmaX, 500, TabM=(3-Public)):
                    ch_e "Yeah, ok."
                else:
                    call Display_DressScreen(EmmaX)
                    if not _return:
                            $ EmmaX.change_face("bemused", 1)
                            ch_e "This is a bit shear for this top."
                            return #jump Emma_Clothes
                $ EmmaX.Over = "nighty"

        "Maybe just throw on a towel?" if EmmaX.Over != "towel":
                $ EmmaX.change_face("bemused", 1)
                $ Bonus = 5 if bg_current == "bg_showerroom" else 0
                if EmmaX.Chest or (EmmaX.SeenChest and Approvalcheck(EmmaX, 500, TabM=(3-Public-Bonus))):
                    ch_e "Oh, you like this?"
                elif Approvalcheck(EmmaX, 1000, TabM=(3-Public-Bonus)):
                    $ EmmaX.change_face("perplexed", 1)
                    ch_e "Fine."
                else:
                    call Display_DressScreen(EmmaX)
                    if not _return:
                            $ EmmaX.change_face("bemused", 1)
                            ch_e "This wouldn't leave much to the imagination."
                            return #jump Emma_Clothes
                call Emma_NoBra
                if not _return:
                    return #jump Emma_Clothes
                $ EmmaX.Over = "towel"

        "Never mind":
                pass
    return #jump Emma_Clothes
    #End of Emma Top

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Emma_NoBra: #fix test this
        menu:
            ch_e "I'm not wearing much of anything under this. . ."
            "Then you could slip something on under it. . .":
                        if (EmmaX.SeenChest and Approvalcheck(EmmaX, 1000, TabM=(4-Public))) or Approvalcheck(EmmaX, 1200, TabM=(5-Public)):
                                ch_e "-not that I'm overly concerned about it. . ."
                        elif Approvalcheck(EmmaX, 900, TabM=(3-Public)) and "lace bra" in EmmaX.Inventory:
                                ch_e "I suppose I could."
                                $ EmmaX.Chest  = "lace bra"
                                "She pulls out her lace bra and slips it on under her [EmmaX.Over]."
#                        elif Approvalcheck(EmmaX, 800, TabM=(3-Public)):
#                                ch_e "I suppose I could."
#                                $ EmmaX.Chest = "bra"
#                                "She pulls out her bra and slips it on under her [EmmaX.Over]."
                        elif Approvalcheck(EmmaX, 700, TabM=(3-Public)):
                                ch_e "I suppose I could."
                                $ EmmaX.Chest = "corset"
                                "She pulls out her corset and slips it on under her [EmmaX.Over]."
                        elif Approvalcheck(EmmaX, 600, TabM=(3-Public)):
                                ch_e "I suppose I could."
                                $ EmmaX.Chest = "sports bra"
                                "She pulls out her sports bra and slips it on under her [EmmaX.Over]."
                        else:
                                ch_e "Yes, but I'd rather not."
                                return 0

            "You could always just wear nothing at all. . .":
                        if Approvalcheck(EmmaX, 1100, "LI", TabM=(3-Public)) and EmmaX.love > EmmaX.inhibition:
                                ch_e "The things I do for you. . ."
                        elif Approvalcheck(EmmaX, 700, "OI", TabM=(3-Public)) and EmmaX.obedience > EmmaX.inhibition:
                                ch_e "If that's what you insist. . ."
                        elif Approvalcheck(EmmaX, 600, "I", TabM=(3-Public)):
                                ch_e "I suppose I could. . ."
                        elif Approvalcheck(EmmaX, 1300, TabM=(3-Public)):
                                ch_e "Very well."
                        else:
                                $ EmmaX.change_face("surprised")
                                $ EmmaX.Brows = "angry"
                                if EmmaX.Taboo > 20:
                                    ch_e "I'm afraid I couldn't do that in public."
                                else:
                                    ch_e "I could, but I wouldn't."
                                return 0


            "Never mind.":
                        return 0
        return 1
        #End of Emma bra check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Emma_Clothes_Legs:
        # Leggings
        "Maybe go without the [EmmaX.Legs]." if EmmaX.Legs:
                $ EmmaX.change_face("sexy", 1)
                if EmmaX.SeenPanties and EmmaX.Panties and Approvalcheck(EmmaX, 500, TabM=(6-Public)):
                    ch_e "Fine."
                elif EmmaX.SeenPussy and Approvalcheck(EmmaX, 900, TabM=(5-Public)):
                    ch_e "Fine."
                elif Approvalcheck(EmmaX, 1300, TabM=(2-Public)) and EmmaX.Panties:
                    ch_e "It's not like I haven't worn this look before. . ."
                elif Approvalcheck(EmmaX, 700) and not EmmaX.Panties:
                    call Emma_NoPantiesOn
                    if not _return and not EmmaX.Panties:
                        if not Approvalcheck(EmmaX, 1500):
                            call Display_DressScreen(EmmaX)
                            if not _return:
                                return #jump Emma_Clothes
                        else:
                                return #jump Emma_Clothes
                else:
                    call Display_DressScreen(EmmaX)
                    if not _return:
                        ch_e "I'm afraid not."
                        if not EmmaX.Panties:
                            ch_e "You understand, it could get. . . drafty. . ."
                        return #jump Emma_Clothes
                $ line = EmmaX.Legs
                $ EmmaX.Legs = 0
                "She peels her [line] off."
                $ line = 0
                if renpy.showing('DressScreen'):
                    pass
                elif EmmaX.Panties:
                    $ EmmaX.SeenPanties = 1
                else:
                    call Emma_First_Bottomless

        "You look great in those white pants." if EmmaX.Legs != "pants":
                ch_e "I know."
                $ EmmaX.Legs = "pants"

        "You look great in that little skirt." if EmmaX.Legs != "skirt":
                ch_e "I agree."
                $ EmmaX.Legs = "skirt"

        "Try on that white dress you have." if EmmaX.Legs != "dress" and "halloween" in EmmaX.History:
                $ EmmaX.change_face("bemused")
                menu:
                    ch_e "The whole thing, or just the skirt?"
                    "The whole dress.":
                            $ EmmaX.Over = "dress"
                    "Just the skirt.":
                            pass
                $ EmmaX.Legs = "dress"

        "You look great in boots." if EmmaX.Acc != "thigh boots":
                ch_e "They do look nice on me."
                $ EmmaX.Acc = "thigh boots"
        "Maybe lose the boots." if EmmaX.Acc == "thigh boots":
                ch_e "I suppose."
                $ EmmaX.Acc = 0

        "You look great in yoga pants." if EmmaX.Legs != "yoga pants":
                ch_e "Yeah, ok."
                $ EmmaX.Legs = "yoga pants"

        "Never mind":
                pass
    return #jump Emma_Clothes
    #End of Emma Pants

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Emma_NoPantiesOn: #fix test this
        $ EmmaX.change_face("sexy",Eyes="side")
        ch_e "You should be aware. . ."
        $ EmmaX.change_face("sly")
        menu:
            ch_e "I'm not wearing any panties at the moment. . ."
            "Then you could slip on a pair. . .":
                        if (EmmaX.SeenPussy and Approvalcheck(EmmaX, 1100, TabM=(5-Public))) or Approvalcheck(EmmaX, 1500, TabM=(5-Public)):
                                $ EmmaX.Blush = 1
                                ch_e "I didn't say that bothered me. . ."
                                $ EmmaX.Blush = 0
                        elif Approvalcheck(EmmaX, 700, TabM=5):
                                ch_e "I suppose that I could. . ."
                                if "lace panties" in EmmaX.Inventory:
                                        $ EmmaX.Panties  = "lace panties"
                                else:
                                        $ EmmaX.Panties = "green panties"
                                if Approvalcheck(EmmaX, 1200, TabM=4):
                                    $ line = EmmaX.Legs
                                    $ EmmaX.Legs = 0
                                    "She pulls off her [line] and slips on the [EmmaX.Panties]."
                                elif EmmaX.Legs == "skirt":
                                    "She pulls out her [EmmaX.Panties] and pulls them up under her skirt."
                                    $ EmmaX.Legs = 0
                                    "Then she drops the skirt to the floor."
                                else:
                                    $ line = EmmaX.Legs
                                    $ EmmaX.Legs = 0
                                    "She steps away a moment and then comes back wearing only the [EmmaX.Panties]."
                                return #jump Emma_Clothes
                        elif EmmaX.Taboo and Approvalcheck(EmmaX, 800, TabM=0):
                                ch_e "I like how you think, but not in public like this."
                                return 0
                        else:
                                ch_e "I could, but I'd rather not."
                                return 0

            "You could always just wear nothing at all. . .":
                        if Approvalcheck(EmmaX, 1100, "LI", TabM=(5-Public)) and EmmaX.love > EmmaX.inhibition:
                                ch_e "I suppose I could. . ."
                        elif Approvalcheck(EmmaX, 700, "OI", TabM=(5-Public)) and EmmaX.obedience > EmmaX.inhibition:
                                ch_e "If you'd like. . ."
                        elif Approvalcheck(EmmaX, 600, "I", TabM=(5-Public)):
                                ch_e "I certainly could. . ."
                        elif Approvalcheck(EmmaX, 1300, TabM=(5-Public)):
                                ch_e "Very well."
                        else:
                                $ EmmaX.change_face("surprised")
                                $ EmmaX.Brows = "angry"
                                if EmmaX.Taboo > 20:
                                    ch_e "I'm afraid not out here, [EmmaX.Petname]!"
                                else:
                                    ch_e "You wish, [EmmaX.Petname]!"
                                return 0

            "Never mind.":
                ch_e "Ok. . ."
                return 0
        return 1
        #End of Emma Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Emma_Clothes_Under:
        "Tops":
            menu:
                "How about you lose the [EmmaX.Chest]?" if EmmaX.Chest:
                    $ EmmaX.change_face("bemused", 1)
                    if EmmaX.SeenChest and Approvalcheck(EmmaX, 900, TabM=(4-Public)):
                        ch_e "Of course."
                    elif Approvalcheck(EmmaX, 1100, TabM=2):
                        if EmmaX.Taboo:
                            ch_e "I'd rather not out here. . ."
                        else:
                            ch_e "I suppose for you. . ."
                    elif EmmaX.Over == "jacket" and Approvalcheck(EmmaX, 700, TabM=(3-Public)):
                        ch_e "This is a bit daring without anything under it. . ."
                    elif not EmmaX.Over:
                        call Display_DressScreen(EmmaX)
                        if not _return:
                            ch_e "I don't think that would be appropriate."
                            return #jump Emma_Clothes
                    else:
                        call Display_DressScreen(EmmaX)
                        if not _return:
                            ch_e "I'm afraid not, [EmmaX.Petname]."
                            return #jump Emma_Clothes
                    $ line = EmmaX.Chest
                    $ EmmaX.Chest = 0
                    if EmmaX.Over:
                        "She reaches under her [EmmaX.Over] grabs her [line], and pulls it out, dropping it to the ground."
                    else:
                        "She lets her [line] fall to the ground."
                        if not renpy.showing('DressScreen'):
                            call Emma_First_Topless

                "I like that corset you have." if EmmaX.Chest != "corset":
                    if EmmaX.SeenChest or Approvalcheck(EmmaX, 1000, TabM=(3-Public)):
                        ch_e "So do I."
                        $ EmmaX.Chest = "corset"
                        $ EmmaX.TitsUp = 1
                    else:
                        call Display_DressScreen(EmmaX)
                        if not _return:
                            ch_e "I don't think that would be appropriate. . ."
                        else:
                            $ EmmaX.Chest = "corset"

                "I like that lace bra." if "lace bra" in EmmaX.Inventory and EmmaX.Chest != "lace bra":
                    if EmmaX.SeenChest or Approvalcheck(EmmaX, 1300, TabM=(3-Public)):
                        ch_e "Fine."
                        $ EmmaX.Chest = "lace bra"
                    else:
                        call Display_DressScreen(EmmaX)
                        if not _return:
                            ch_e "It's a bit revealing. . ."
                        else:
                            $ EmmaX.Chest = "lace bra"

                "I like that sports bra." if EmmaX.Chest != "sports bra":
                    if EmmaX.SeenChest or Approvalcheck(EmmaX, 1000, TabM=(3-Public)):
                        ch_e "Fine."
                        $ EmmaX.Chest = "sports bra"
                    else:
                        call Display_DressScreen(EmmaX)
                        if not _return:
                            ch_e "I'm not sure about that. . ."
                        else:
                            $ EmmaX.Chest = "sports bra"

                "I like that bikini top." if EmmaX.Chest != "bikini top" and "bikini top" in EmmaX.Inventory:
                    if bg_current == "bg_pool":
                            ch_e "Fine."
                            $ EmmaX.Chest = "bikini top"
                    else:
                            if EmmaX.SeenChest or Approvalcheck(EmmaX, 800, TabM=2):
                                ch_e "Fine."
                                $ EmmaX.Chest = "bikini top"
                            else:
                                call Display_DressScreen(EmmaX)
                                if not _return:
                                    ch_e "I don't know about wearing that here. . ."
                                else:
                                    $ EmmaX.Chest = "bikini top"
                "Never mind":
                    pass
            return #jump Emma_Clothes_Under


        "Hose and stockings options":
            menu:
                "You could lose the hose." if EmmaX.Hose:
                                $ EmmaX.Hose = 0
                "The thigh-high hose would look good with that." if EmmaX.Hose != "stockings" and "stockings and garterbelt" in EmmaX.Inventory:
                                $ EmmaX.Hose = "stockings"
                "The pantyhose would look good with that." if EmmaX.Hose != "pantyhose" and "pantyhose" in EmmaX.Inventory:
                                $ EmmaX.Hose = "pantyhose"
                "The ripped pantyhose would look good with that." if EmmaX.Hose != "ripped pantyhose" and "ripped pantyhose" in EmmaX.Inventory:
                                $ EmmaX.Hose = "ripped pantyhose"
                "The stockings and garterbelt would look good with that." if EmmaX.Hose != "stockings and garterbelt" and "stockings and garterbelt" in EmmaX.Inventory:
                                $ EmmaX.Hose = "stockings and garterbelt"
                "Maybe just the garterbelt?" if EmmaX.Hose != "garterbelt" and "stockings and garterbelt" in EmmaX.Inventory:
                                $ EmmaX.Hose = "garterbelt"
                "Never mind":
                        pass
            return #jump Emma_Clothes_Under

        #Panties
        "Panties":
            menu:
                "You could lose those panties. . ." if EmmaX.Panties:
                        $ EmmaX.change_face("bemused", 1)
                        if (Approvalcheck(EmmaX, 900) or EmmaX.SeenPussy) and not EmmaX.Taboo:
                            #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public

                            if Approvalcheck(EmmaX, 850, "L"):
                                    ch_e "You like the view?"
                            elif Approvalcheck(EmmaX, 500, "O"):
                                    ch_e "If you'd like."
                            elif Approvalcheck(EmmaX, 350, "I"):
                                    ch_e "I do enjoy going without them. . ."
                            else:
                                    ch_e "Very well."
                        else:
                            #low approval or not wearing pants or in public
                            if Approvalcheck(EmmaX, 1100, "LI", TabM=(4-Public)) and EmmaX.love > EmmaX.inhibition:
                                    ch_e "I don't exactly mind you seeing. . ."
                            elif Approvalcheck(EmmaX, 700, "OI", TabM=(4-Public)) and EmmaX.obedience > EmmaX.inhibition:
                                    ch_e "I suppose I could. . ."
                            elif Approvalcheck(EmmaX, 600, "I", TabM=(4-Public)):
                                    ch_e "Why not."
                            elif Approvalcheck(EmmaX, 1300, TabM=(4-Public)):
                                    ch_e "Fine."
                            else:
                                call Display_DressScreen(EmmaX)
                                if not _return:
                                    $ EmmaX.change_face("surprised")
                                    $ EmmaX.Brows = "angry"
                                    if EmmaX.Taboo > 20:
                                        ch_e "I don't think I could out here, [EmmaX.Petname]!"
                                    else:
                                        ch_e "I could, but I won't, [EmmaX.Petname]!"
                                    return #jump Emma_Clothes
                        $ line = EmmaX.Panties
                        $ EmmaX.Panties = 0
                        if not EmmaX.Legs:
                            "She pulls off her [line], then drops them to the ground."
                            if not renpy.showing('DressScreen'):
                                    call Emma_First_Bottomless
                        elif Approvalcheck(EmmaX, 1200, TabM=4):
                            $ temp = EmmaX.Legs
                            $ EmmaX.Legs = 0
                            pause 0.5
                            $ EmmaX.Legs = temp
                            "She pulls off her [EmmaX.Legs] and [line], then pulls the [EmmaX.Legs] back on."
                            $ primary_action = 1
                            call Emma_First_Bottomless(1)
                        elif EmmaX.Legs == "skirt":
                            "She reaches under her skirt and pulls her [line] off."
                        else:
                            $ EmmaX.Blush = 1
                            "She steps away a moment and then comes back."
                            $ EmmaX.Blush = 0
                        $ line = 0

                "Why don't you wear the white panties instead?" if EmmaX.Panties and EmmaX.Panties != "white panties":
                        if Approvalcheck(EmmaX, 1100, TabM=(4-Public)):
                                ch_e "Ok."
                                $ EmmaX.Panties = "white panties"
                        else:
                            call Display_DressScreen(EmmaX)
                            if not _return:
                                ch_e "I really don't see how that's any of your concern."
                            else:
                                $ EmmaX.Panties = "white panties"

                "Why don't you wear the sporty panties instead?" if EmmaX.Panties and EmmaX.Panties != "sports panties":
                        if Approvalcheck(EmmaX, 1200, TabM=(4-Public)):
                                ch_e "Fine."
                                $ EmmaX.Panties = "sports panties"
                        else:
                            call Display_DressScreen(EmmaX)
                            if not _return:
                                ch_e "I really don't see how that's any of your concern."
                            else:
                                $ EmmaX.Panties = "sports panties"

                "Why don't you wear the lace panties instead?" if "lace panties" in EmmaX.Inventory and EmmaX.Panties and EmmaX.Panties != "lace panties":
                        if Approvalcheck(EmmaX, 1300, TabM=(4-Public)):
                                ch_e "Fine."
                                $ EmmaX.Panties = "lace panties"
                        else:
                            call Display_DressScreen(EmmaX)
                            if not _return:
                                ch_e "I really don't see how that's any of your concern."
                            else:
                                $ EmmaX.Panties = "lace panties"

                "I like those bikini bottoms." if EmmaX.Panties != "bikini bottoms" and "bikini bottoms" in EmmaX.Inventory:
                        if bg_current == "bg_pool":
                                ch_e "Fine."
                                $ EmmaX.Panties = "bikini bottoms"
                        else:
                                if Approvalcheck(EmmaX, 800, TabM=2):
                                    ch_e "Fine."
                                    $ EmmaX.Panties = "bikini bottoms"
                                else:
                                    call Display_DressScreen(EmmaX)
                                    if not _return:
                                        ch_e "I don't know about wearing those here. . ."
                                    else:
                                        $ EmmaX.Panties = "bikini bottoms"

                "You know, you could wear some panties with that. . ." if not EmmaX.Panties:
                        $ EmmaX.change_face("bemused", 1)
                        if EmmaX.Legs and (EmmaX.love+EmmaX.obedience) <= (2* EmmaX.inhibition):
                            $ EmmaX.Mouth = "smile"
                            ch_e "I could, but won't."
                            menu:
                                "Fine by me":
                                    return #jump Emma_Clothes
                                "I insist, put some on.":
                                    if (EmmaX.love+EmmaX.obedience) <= EmmaX.inhibition:
                                        $ EmmaX.change_face("angry", Eyes="side")
                                        ch_e "How disappointing that must be for you."
                                        return #jump Emma_Clothes
                                    else:
                                        $ EmmaX.change_face("sadside")
                                        ch_e "If you insist."
                        menu:
                            ch_e "If you insist. . ."
                            "How about the white ones?":
                                ch_e "Fine."
                                $ EmmaX.Panties = "white panties"
                            "How about the sporty ones?":
                                ch_e "Fine."
                                $ EmmaX.Panties = "sports panties"
                            "How about the lace ones?" if "lace panties" in EmmaX.Inventory:
                                ch_e "Fine."
                                $ EmmaX.Panties  = "lace panties"
                "Never mind":
                    pass
            return #jump Emma_Clothes_Under
        "Never mind":
            pass
    return #jump Emma_Clothes
    #End of Emma Underwear

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Emma_Clothes_Misc:
        #Misc
        "You look good with your hair flowing." if EmmaX.Hair != "wave" and EmmaX.Hair != "hat":
                if Approvalcheck(EmmaX, 600):
                    if EmmaX.Hair == "hat wet":
                            $ EmmaX.Hair = "hat"
                    else:
                            $ EmmaX.Hair = "wave"
                    ch_e "Like this?"
                else:
                    ch_e "Yes, I do."

        "Maybe keep your hair straight." if EmmaX.Hair != "wet"and EmmaX.Hair != "hat wet":
                if Approvalcheck(EmmaX, 600):
                    if EmmaX.Hair == "hat":
                            $ EmmaX.Hair = "hat wet"
                    else:
                            $ EmmaX.Hair = "wet"
                    ch_e "You think?"
                else:
                    ch_e "I tend to prefer it a bit more loose."

        "Add hat" if EmmaX.Hair != "hat" and EmmaX.Hair != "hat wet" and "halloween" in EmmaX.History:
                ch_p "That hat you wore to the party was nice."
                if EmmaX.Hair == "wet":
                        $ EmmaX.Hair = "hat wet"
                else:
                        $ EmmaX.Hair = "hat"
        "Remove hat" if EmmaX.Hair == "hat" or EmmaX.Hair == "hat wet":
                ch_p "You could probably lose the hat."
                if EmmaX.Hair == "hat wet":
                        $ EmmaX.Hair = "wet"
                else:
                        $ EmmaX.Hair = "wave"

        "Grow Pubes." if not EmmaX.Pubes and "pubes" not in EmmaX.Todo:
                ch_p "You know, I like some nice hair down there. Maybe grow it out."
                if "pubes" in EmmaX.Todo:
                    $ EmmaX.change_face("bemused", 1)
                    ch_e "Rome wasn't built in a day. . ."
                else:
                    $ EmmaX.change_face("bemused", 1)
                    $ Approval = Approvalcheck(EmmaX, 1150, TabM=0)
                    if Approvalcheck(EmmaX, 850, "L", TabM=0) or (Approval and EmmaX.love > 2 * EmmaX.obedience):
                        ch_e "If you like that sort of thing. . ."
                    elif Approvalcheck(EmmaX, 500, "I", TabM=0) or (Approval and EmmaX.inhibition > EmmaX.obedience):
                        ch_e "I could go a bit more. . . wild."
                    elif Approvalcheck(EmmaX, 400, "O", TabM=0) or Approval:
                        ch_e "If you insist. . ."
                    else:
                        $ EmmaX.change_face("surprised")
                        $ EmmaX.Brows = "angry"
                        ch_e "I don't see how that's your concern, [EmmaX.Petname]."
                        return #jump Emma_Clothes
                    $ EmmaX.Todo.append("pubes")
                    $ EmmaX.PubeC = 6

        "Shave pubes" if EmmaX.Pubes == 1:
                ch_p "I like it waxed clean down there."
                $ EmmaX.change_face("bemused", 1)
                if "shave" in EmmaX.Todo:
                    ch_e "Yes, yes, it's on my schedule."
                else:
                    $ Approval = Approvalcheck(EmmaX, 1150, TabM=0)

                    if Approvalcheck(EmmaX, 850, "L", TabM=0) or (Approval and EmmaX.love > 2 * EmmaX.obedience):
                        ch_e "I know you love it."
                    elif Approvalcheck(EmmaX, 500, "I", TabM=0) or (Approval and EmmaX.inhibition > EmmaX.obedience):
                        ch_e "I like it kept tidy."
                    elif Approvalcheck(EmmaX, 400, "O", TabM=0) or Approval:
                        ch_e "If you insist."
                    else:
                        $ EmmaX.change_face("surprised")
                        $ EmmaX.Brows = "angry"
                        ch_e "I don't see how that's your concern, [EmmaX.Petname]."
                        return #jump Emma_Clothes
                    $ EmmaX.Todo.append("shave")
        "Piercings. [[See what she looks like without them first] (locked)" if not EmmaX.SeenPussy and not EmmaX.SeenChest:
                pass

        "Add ring piercings" if EmmaX.Pierce != "ring" and (EmmaX.SeenPussy or EmmaX.SeenChest):
                ch_p "You know, you'd look really nice with some ring body piercings."
                if "ring" in EmmaX.Todo:
                        ch_e "Yes, yes, it's on my schedule."
                else:
                        $ EmmaX.change_face("bemused", 1)
                        $ Approval = Approvalcheck(EmmaX, 1350, TabM=0)
                        if Approvalcheck(EmmaX, 900, "L", TabM=0) or (Approval and EmmaX.love > 2* EmmaX.obedience):
                                ch_e "A little handhold, I assume?"
                        elif Approvalcheck(EmmaX, 600, "I", TabM=0) or (Approval and EmmaX.inhibition > EmmaX.obedience):
                                ch_e "I do like a nice ring. . ."
                        elif Approvalcheck(EmmaX, 500, "O", TabM=0) or Approval:
                                ch_e "I didn't know you were into that sort of thing."
                        else:
                                $ EmmaX.change_face("surprised")
                                $ EmmaX.Brows = "angry"
                                ch_e "Well, I'm just not ready for that sort of thing, [EmmaX.Petname]."
                                return #jump Emma_Clothes
                        $ EmmaX.Todo.append("ring")

        "Add barbell piercings." if EmmaX.Pierce != "barbell" and (EmmaX.SeenPussy or EmmaX.SeenChest):
                ch_p "You know, you'd look really nice with some barbell body piercings."
                if "barbell" in EmmaX.Todo:
                        ch_e "Yes, yes, it's on my schedule."
                else:
                        $ EmmaX.change_face("bemused", 1)
                        $ Approval = Approvalcheck(EmmaX, 1350, TabM=0)
                        if Approvalcheck(EmmaX, 900, "L", TabM=0) or (Approval and EmmaX.love > 2 * EmmaX.obedience):
                            ch_e "A little handhold, I assume?"
                        elif Approvalcheck(EmmaX, 600, "I", TabM=0) or (Approval and EmmaX.inhibition > EmmaX.obedience):
                            ch_e "They might look nice on these. . ."
                        elif Approvalcheck(EmmaX, 500, "O", TabM=0) or Approval:
                            ch_e "I didn't know you were into that sort of thing."
                        else:
                            $ EmmaX.change_face("surprised")
                            $ EmmaX.Brows = "angry"
                            ch_e "Well, I'm just not ready for that sort of thing, [EmmaX.Petname]."
                            return #jump Emma_Clothes
                        $ EmmaX.Todo.append("barbell")
                        $ EmmaX.Pierce = "barbell"

        "Remove piercings" if EmmaX.Pierce:
                ch_p "You know, you'd look better without those piercings."
                $ EmmaX.change_face("bemused", 1)
                $ Approval = Approvalcheck(EmmaX, 1350, TabM=0)
                if Approvalcheck(EmmaX, 950, "L", TabM=0) or (Approval and EmmaX.love > EmmaX.obedience):
                    ch_e "If they aren't working for you. . ."
                elif Approvalcheck(EmmaX, 700, "I", TabM=0) or (Approval and EmmaX.inhibition > EmmaX.obedience):
                    ch_e "They were being a nuisance."
                elif Approvalcheck(EmmaX, 600, "O", TabM=0) or Approval:
                    ch_e "I'll remove them then."
                else:
                    $ EmmaX.change_face("surprised")
                    $ EmmaX.Brows = "angry"
                    ch_e "Well {i}I{/i} enjoy them."
                    return #jump Emma_Clothes
                $ EmmaX.Pierce = 0

        "Add choker" if EmmaX.Neck != "choker":
                ch_e "Why don't you try on that white choker."
                ch_e "Ok. . ."
                $ EmmaX.Neck = "choker"
        "Remove choker" if EmmaX.Neck:
                ch_e "WMaybe go without a collar."
                ch_e "Ok. . ."
                $ EmmaX.Neck = 0

        "Maybe lose the gloves." if EmmaX.Arms:
                $ EmmaX.Arms = 0
                ch_e "Ok."
        "Put your gloves on." if not EmmaX.Arms:
                $ EmmaX.Arms = "gloves"
                ch_e "Ok."
        "Never mind":
                pass
    return #jump Emma_Clothes
    #End of Emma Misc Wardrobe

return
#End Emma Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


## Start Emma first Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#label Emma_First_Les(Silent = 0, Undress = 0, GirlsNum = 0): #checked when she engages in a les scene  ## call Emma_First_Les(0,1)
#    if EmmaX.Les:
#        return

#    $ EmmaX.Les += 1
#    $ EmmaX.recent_history.append("lesbian")
#    $ EmmaX.change_stat("inhibition", 30, 2)
#    $ EmmaX.change_stat("inhibition", 90, 1)

#    if not Silent:
#        #example previous line: line + " and cups " + Primary + "'s breasts in her delicate hands"
#        "Emma's head jerks up and she looks at what [Partner] is doing. [Partner] pauses and glances up at her with a mischievous grin."
#        ch_e "I, um, I haven't done that sort of thing before."
#        if Partner == "Rogue":
#                if R_Les:
#                    ch_r "Neither have I Sugar, but it seemed like fun."
#                else:
#                    ch_r "It's all right Sugar, I'll take care of you."
#        if EmmaX.LikeRogue >= 60 and Approvalcheck(EmmaX, (1500-(10*EmmaX.Les)-(10*(EmmaX.LikeRogue-60)))): #If she likes both of you a lot, threeway
#                $ State = "threeway"
#        elif Approvalcheck(EmmaX, 1000): #If she likes you well enough, Hetero
#                $ State = "hetero"
#        elif EmmaX.LikeRogue >= 70: #if she doesn't like you but likes Rogue, lesbian
#                $ State = "lesbian"





#        if "cockout" in Player.recent_history:
#                $ EmmaX.change_face("down", 2)
#                if GirlsNum:
#                    "Emma also glances down at your cock"
#                else:
#                    "Emma glances down at your exposed cock"
#        elif Undress:
#                "You strip nude."
#        else:
#                "You whip your cock out."
#        $ Player.recent_history.append("cockout")

#        if Taboo and not Approvalcheck(EmmaX, 1500):
#                $ EmmaX.change_face("surprised", 2)
#                ch_e "Um, you should[EmmaX.like]put that away in public."
#                $ EmmaX.change_face("bemused", 1)
#                if EmmaX.SeenPeen == 1:
#                    ch_e "Or[EmmaX.like]maybe. . ."
#                    $ EmmaX.change_stat("love", 90, 15)
#                    $ EmmaX.change_stat("obedience", 50, 20)
#                    $ EmmaX.change_stat("inhibition", 60, 35)

#        elif EmmaX.SeenPeen > 10:
#                return
#        elif Approvalcheck(EmmaX, 1200) or Approvalcheck(EmmaX, 500, "L"):
#                $ EmmaX.change_face("sly",1)
#                if EmmaX.SeenPeen == 1:
#                    $ EmmaX.change_face("surprised",2)
#                    ch_e "That's. . . impressive."
#                    $ EmmaX.change_face("bemused",1)
#                    $ EmmaX.change_stat("love", 90, 3)
#                elif EmmaX.SeenPeen == 2:
#                    ch_e "I can't get over that."
#                    $ EmmaX.change_stat("obedience", 50, 7)
#                elif EmmaX.SeenPeen == 5:
#                    ch_e "There it is."
#                    $ EmmaX.change_stat("inhibition", 60, 5)
#                elif EmmaX.SeenPeen == 10:
#                    ch_e "So beautiful."
#                    $ EmmaX.change_stat("obedience", 80, 10)
#                    $ EmmaX.change_stat("inhibition", 60, 3)
#        else:
#                $ EmmaX.change_face("sad",1)
#                if EmmaX.SeenPeen == 1:
#                    $ EmmaX.change_face("perplexed",1 )
#                    ch_e "Well that happened. . ."
#                    $ EmmaX.change_stat("obedience", 50, 7)
#                    $ EmmaX.change_stat("inhibition", 60, 3)
#                elif EmmaX.SeenPeen < 5:
#                    $ EmmaX.change_face("sad",0)
#                    ch_e "Huh."
#                    $ EmmaX.change_stat("inhibition", 60, 2)
#                elif EmmaX.SeenPeen == 10:
#                    ch_e "[EmmaX.Like]put that away."
#                    $ EmmaX.change_stat("obedience", 50, 7)
#                    $ EmmaX.change_stat("inhibition", 60, 3)

#    else: #Silent mode
#                $ Player.recent_history.append("cockout")
#                if EmmaX.SeenPeen > 10:
#                    return
#                elif Approvalcheck(EmmaX, 1200) or Approvalcheck(EmmaX, 500, "L"):
#                        if EmmaX.SeenPeen == 1:
#                            $ EmmaX.change_stat("love", 90, 3)
#                        elif EmmaX.SeenPeen == 2:
#                            $ EmmaX.change_stat("obedience", 50, 7)
#                        elif EmmaX.SeenPeen == 5:
#                            $ EmmaX.change_stat("inhibition", 60, 5)
#                        elif EmmaX.SeenPeen == 10:
#                            $ EmmaX.change_stat("love", 90, 10)
#                else:
#                        if EmmaX.SeenPeen == 1:
#                            $ EmmaX.change_stat("obedience", 50, 7)
#                            $ EmmaX.change_stat("inhibition", 60, 3)
#                        elif EmmaX.SeenPeen < 5:
#                            $ EmmaX.change_stat("inhibition", 60, 2)
#                        elif EmmaX.SeenPeen == 10:
#                            $ EmmaX.change_stat("obedience", 50, 7)
#                            $ EmmaX.change_stat("inhibition", 60, 3)

#    if EmmaX.SeenPeen == 1:
#        $ EmmaX.change_stat("love", 90, 10)
#        $ EmmaX.change_stat("obedience", 90, 25)
#        $ EmmaX.change_stat("inhibition", 60, 20)
#        $ EmmaX.change_stat("lust", 200, 5)

#    return
## End Emma first Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

##label Emma_Tits_Up:
