label Date_Ask(Girl=0): #rkeljsv
        #From the chat menu, you ask Rogue to meet you
        $ Girl = Girlcheck(Girl)
        call shift_focus(Girl)
        if "yesdate" in Girl.daily_history:
                $ Girl.change_face("bemused")
                if Girl == RogueX:
                        ch_r "Come on, I already said \"yes.\""
                elif Girl == KittyX:
                        ch_k "Lol, I already said \"yes.\""
                elif Girl == EmmaX:
                        ch_e "Learn to take \"yes\" for an answer, [Girl.Petname]."
                elif Girl == LauraX:
                        ch_l "I already told you \"ok.\""
                elif Girl == JeanX:
                        ch_j "Are you still here?"
                elif Girl == StormX:
                        ch_s "I have already agreed, [Girl.Petname]."
                elif Girl == JubesX:
                        ch_v "Yeah, I mean we already agreed on that. . ."
                return
        if "askeddate" in Girl.daily_history:
                $ Girl.change_face("angry")
                if Girl == RogueX:
                        ch_r "I think you got your answer already."
                elif Girl == KittyX:
                        ch_k "Geez, stop bothering me already!"
                elif Girl == EmmaX:
                        ch_e "Persistance will not be rewarded, [Girl.Petname]."
                elif Girl == LauraX:
                        ch_l "Back off."
                elif Girl == JeanX:
                        ch_j "Are you still here?"
                elif Girl == StormX:
                        ch_s "I have already said \"no,\" [Girl.Petname]."
                elif Girl == JubesX:
                        ch_v "Yeah, I mean I already said \"no\". . ."
                return
        if "stoodup" in Girl.Traits:
                call Date_Stood_Up(Girl)
                #$ Girl.AddWord(1,"askeddate","askeddate")#recent and daily
                return
        $ Girl.AddWord(1,"askeddate","askeddate")  #recent and daily

        if Girl == EmmaX:
                if "classcaught" not in EmmaX.History:
                        #if you haven't caught her yet
                        ch_e "I don't really think it would be appropriate for the two of us to be seen together."
                        return
                if "taboo" not in EmmaX.History:
                        #if she hasn't agreed to go public yet
                        call Emma_Taboo_Talk
                        if "taboo" not in EmmaX.History:
                            return
        if Girl.Break[0] and "ex" in Girl.Traits:
                $ Girl.change_face("angry")
                if Girl == RogueX:
                        ch_r "Seriously? You're asking me that after what you just did?"
                elif Girl == KittyX:
                        ch_k "You can't just pretend that nothing happened!"
                elif Girl == EmmaX:
                        ch_e "I think you have some work to do before you're ready to ask that question."
                elif Girl == LauraX:
                        ch_l "You don't want to be hassling me right now."
                elif Girl == JeanX:
                        ch_j "If it weren't for your power, you wouldn't even remember what you did."
                        ch_j "But I -would-."
                elif Girl == StormX:
                        ch_s "I am afraid not. You have burned that bridge."
                elif Girl == JubesX:
                        ch_v "I'm kinda still pissed at you right now?"
                return
        if "ex" in Girl.Traits:
            if Approvalcheck(Girl, 1200):
                    $ Girl.change_face("bemused",Brows = "sad" )
                    if Girl == RogueX:
                            ch_r "We had some fun, I guess we could go out, as friends maybe."
                    elif Girl == KittyX:
                            ch_k "I don't know, we used to have fun. Maybe. . ."
                    elif Girl == EmmaX:
                            ch_e "You were an entertaining date, I suppose, this once."
                    elif Girl == LauraX:
                            ch_l "Well, we did have some fun. . ."
                    elif Girl == JeanX:
                            ch_j "Who are you again?"
                    elif Girl == StormX:
                            ch_s "I suppose we could go out as friends, [Girl.Petname]."
                    elif Girl == JubesX:
                            ch_v "Yeah, I mean we could go as friends or whatever. . ."
            else:
                    $ Girl.change_face("angry",Eyes = "side")
                    if Girl == RogueX:
                            ch_r "I don't think we really worked out, [Girl.Petname]."
                    elif Girl == KittyX:
                            ch_k "I[Girl.like]don't think so."
                    elif Girl == EmmaX:
                            ch_e "I don't think we really worked out, [Girl.Petname]."
                    elif Girl == LauraX:
                            ch_l "Nah, pass."
                    elif Girl == JeanX:
                            ch_j "Who are you again?"
                    elif Girl == StormX:
                            ch_s "We made for a poor match, [Girl.Petname]."
                    elif Girl == JubesX:
                            ch_v "I don't really think that would make any sense. . ."
                    return

        if "stoodup" in Girl.History or "deadbeat" in Girl.History:
            if "stoodup" in Girl.History:
                    $ Girl.change_face("angry",Eyes = "side")
                    if Girl == RogueX:
                            ch_r "Don't you be leav'in me behind this time."
                    elif Girl == KittyX:
                            ch_k "I don't want to be left in the quad again."
                    elif Girl == EmmaX:
                            ch_e "I believe you know better than to leave me waiting again."
                    elif Girl == LauraX:
                            ch_l "Just don't keep me waiting again."
                    elif Girl == JeanX:
                            ch_j "I don't give first chances, and definitely not second ones."
                    elif Girl == StormX:
                            ch_s "Make certain to keep your promises this time, [Girl.Petname]."
                    elif Girl == JubesX:
                            ch_v "Just make sure you actually show this time. . ."
            if "deadbeat" in Girl.History:
                    $ Girl.change_face("angry")
                    if Girl == RogueX:
                            if "stoodup" in Girl.History:
                                ch_r "And last time, you even made me pay for your broke ass?"
                            else:
                                ch_r "Remember last time, when you made me pay for your broke ass?"
                    elif Girl == KittyX:
                            if "stoodup" in Girl.History:
                                ch_k "And last time we went out, you[Girl.like]left me with the check!"
                            else:
                                ch_k "Last time we went out, you[Girl.like]left me with the check!"
                    elif Girl == EmmaX:
                            if "stoodup" in Girl.History:
                                ch_e "Nor do I expect to be picking up the check again."
                            else:
                                ch_e "I don't I expect to be picking up the check again."
                    elif Girl == LauraX:
                            if "stoodup" in Girl.History:
                                ch_l "And last time you just ditched me with the check."
                            else:
                                ch_l "Last time you just ditched me with the check."
                    elif Girl == JeanX:
                            if "stoodup" in Girl.History:
                                ch_j "and -especially- not for deadbeats."
                            else:
                                ch_j "You forgot the \"paying for me\" part last time. . ."
                    elif Girl == StormX:
                            if "stoodup" in Girl.History:
                                ch_s "And I won't be picking up the tab this time either."
                            else:
                                ch_s "And I won't be picking up the tab this time."
                    elif Girl == JubesX:
                            if "stoodup" in Girl.History:
                                ch_v "-and last time, you just left me with the check!"
                            else:
                                ch_v "Last time, you just left me with the check!"
            menu:
                extend ""
                "Sorry about that, I'll take care of it this time.":
                        if Approvalcheck(Girl, 650):
                                $ Girl.change_face("sad")
                                if Girl == RogueX:
                                        ch_r "Ok, [Girl.Petname], you'd better."
                                elif Girl == KittyX:
                                        ch_k "Well, I guess I can give you another chance, just don't disappoint me again."
                                elif Girl == EmmaX:
                                        ch_e "I'll take you at your word, [Girl.Petname]."
                                elif Girl == LauraX:
                                        ch_l "Ok, you get another shot, don't screw it up."
                                elif Girl == JeanX:
                                        ch_j "Oh, you will? You'd better."
                                elif Girl == StormX:
                                        ch_s "As well you should, [Girl.Petname]."
                                elif Girl == JubesX:
                                        ch_v "Well that's what I expected last time. . ."
                        else:
                                $ Girl.change_face("angry")
                                if Girl == RogueX:
                                        ch_r "Yeah, I'aint buy'in that hogwash, [Girl.Petname]."
                                elif Girl == KittyX:
                                        ch_k "Yeah[Girl.like]fool me once. . . no thanks, [Girl.Petname]."
                                elif Girl == EmmaX:
                                        ch_e "A likely story."
                                elif Girl == LauraX:
                                        ch_l "You had your chance, you blew it."
                                elif Girl == JeanX:
                                        ch_j "I don't buy it."
                                elif Girl == StormX:
                                        ch_s "Well, perhaps eventually that will be enough."
                                elif Girl == JubesX:
                                        ch_v "Well that's what I expected last time. . ."
                                return
                "Yeah, so?":
                        if Approvalcheck(Girl, 1400,Alt=[[EmmaX],1500]):
                                $ Girl.change_face("angry", Mouth = "grimace")
                                if Girl == RogueX:
                                        ch_r "It's a good thing you're so pretty."
                                elif Girl == KittyX:
                                        ch_k "Why do I[Girl.like]put up with you?"
                                elif Girl == EmmaX:
                                        ch_e "I suppose I can appreciate confidence."
                                        $ EmmaX.change_face("bemused")
                                        ch_e "Just don't get {i}too{/i} confident."
                                elif Girl == LauraX:
                                        ch_l "Hmm. Ok."
                                elif Girl == JeanX:
                                        ch_j "Bold move."
                                        ch_j "I can repect that."
                                elif Girl == StormX:
                                        ch_s "A bold play, [Girl.Petname]."
                                elif Girl == JubesX:
                                        ch_v "So?! Well. . . so. . ."
                                        ch_v "Whatever."
                                $ Girl.change_face("bemused")
                        elif Approvalcheck(Girl, 500, "O",Alt=[[EmmaX],700]):
                                $ Girl.change_face("surprised")
                                call Anyline(Girl,". . .")
                                $ Girl.change_face("sad")
                                $ Girl.change_stat("obedience", 80, 3)
                                if Girl == RogueX:
                                        ch_r "I. . . guess I can give you another shot. . ."
                                elif Girl == KittyX:
                                        ch_k "Well, I guess we can still have fun. . ."
                                elif Girl == EmmaX:
                                        ch_e "Well, I suppose I could join you for a bit. . ."
                                elif Girl == LauraX:
                                        ch_l "If you insist. . ."
                                elif Girl == JeanX:
                                        ch_j "Hmm. . . Ok. . ."
                                elif Girl == StormX:
                                        ch_s ". . . I can give you another chance."
                                elif Girl == JubesX:
                                        ch_v "I guess we could try it. . ."
                        elif Approvalcheck(Girl, 650):
                                $ Girl.change_face("angry")
                                $ Girl.change_stat("love", 80, -5)
                                $ Girl.change_stat("inhibition", 60, 2)
                                if Girl == RogueX:
                                        ch_r "\"So\" it looks like we won't be going out again."
                                elif Girl == KittyX:
                                        ch_k "Yeah[Girl.like]I'm going out with {i}you,{/i} dick."
                                elif Girl == EmmaX:
                                        ch_e "Then I believe you can figure out the answer to your own question."
                                elif Girl == LauraX:
                                        ch_l "So I'm not going out with you again."
                                elif Girl == JeanX:
                                        ch_j "\"So,\" I'll get someone -else- to pay for dinner."
                                elif Girl == StormX:
                                        ch_s "You should have no trouble paying for yor own meal."
                                elif Girl == JubesX:
                                        ch_v "So do better. . ."
                                return
                        else:
                                $ Girl.change_face("angry")
                                $ Girl.change_stat("love", 80, -10)
                                $ Girl.change_stat("obedience", 80, -3)
                                $ Girl.change_stat("inhibition", 60, 2)
                                if Girl == RogueX:
                                        ch_r "Fuck off."
                                elif Girl == KittyX:
                                        ch_k "Asshole."
                                elif Girl == EmmaX:
                                        ch_e "You don't want to stick around."
                                elif Girl == LauraX:
                                        ch_l "Dick."
                                elif Girl == JeanX:
                                        $ Girl.change_face("angry",1,Eyes="psychic")
                                        ch_j ". . ."
                                        $ Girl.change_face("angry",1)
                                elif Girl == StormX:
                                        ch_s "So you shall eat alone, [Girl.Petname]."
                                elif Girl == JubesX:
                                        ch_v "Nah. . ."
                                return
            $ Girl.change_stat("obedience", 30, 3)
            $ Girl.change_stat("obedience", 80, 2)
        #end "if stoodup or deadbeat". . .
        elif Approvalcheck(Girl, 650):
                $ Girl.change_face("smile")
                if Girl == RogueX:
                        ch_r "Yeah, sounds good. See ya in a bit, [Girl.Petname]."
                elif Girl == KittyX:
                        ch_k "Sure, see you then."
                elif Girl == EmmaX:
                        ch_e "Sounds lovely, I'll see you later then, [Girl.Petname]."
                elif Girl == LauraX:
                        ch_l "Sure, see you there."
                elif Girl == JeanX:
                        ch_j "Ok, don't be late."
                elif Girl == StormX:
                        ch_s "I will see you then, [Girl.Petname]."
                elif Girl == JubesX:
                        ch_v "Ok, so see you then. . ."
        elif Approvalcheck(Girl, 400):
                $ Girl.change_face("angry",Eyes = "side")
                if Girl == RogueX:
                        ch_r "I think I'm washing my hair tonight. . ."
                elif Girl == KittyX:
                        ch_k "I've[Girl.like]got better things to do. . ."
                elif Girl == EmmaX:
                        ch_e "I have some papers to take care of tonight. . ."
                elif Girl == LauraX:
                        ch_l "I've got some other stuff to do. . ."
                elif Girl == JeanX:
                        ch_j "I have plans that don't include you."
                elif Girl == StormX:
                        ch_s "I will be busy, I am afraid."
                elif Girl == JubesX:
                        ch_v "I think I'll be busy with something?"
                return
        else:
                $ Girl.change_face("angry")
                if Girl == RogueX:
                        ch_r "Yeah, you wish."
                elif Girl == KittyX:
                        ch_k "[Girl.Like]no way."
                elif Girl == EmmaX:
                        ch_e "I can't imagine why I would."
                elif Girl == LauraX:
                        ch_l "Nah."
                elif Girl == JeanX:
                        ch_j "Ha! Yeah right."
                elif Girl == StormX:
                        ch_s "I do not think so."
                elif Girl == JubesX:
                        ch_v "No way."
                return

        $ Count = 0
        #She mostly agreed, do you ask for a double date?
        menu:
            "Good, I'll meet you in the campus square." if bg_current != "bg_campus" or time_index < 2: #pre-evening time
                            $ Girl.change_face("smile")
            "Good, let's get going then." if bg_current == "bg_campus" and time_index == 2: #evening time
                            $ Girl.change_face("smile")
            "And I was thinking of asking. . .":
                        menu:
                            ch_p "And I was thinking of asking. . ."
                            "[RogueX.name] along too." if Girl != RogueX:
                                        $ Count = Girl.LikeRogue
                            "[KittyX.name] along too." if Girl != KittyX and "met" in KittyX.History:
                                        $ Count = Girl.LikeKitty
                            "[EmmaX.name] along too." if Girl != EmmaX and "met" in EmmaX.History:
                                        $ Count = Girl.LikeEmma
                            "[LauraX.name] along too." if Girl != LauraX and "met" in LauraX.History:
                                        $ Count = Girl.LikeLaura
                            "[JeanX.name] along too." if Girl != JeanX and "met" in JeanX.History:
                                        $ Count = Girl.LikeJean
                            "[StormX.name] along too." if Girl != StormX and "met" in StormX.History:
                                        $ Count = Girl.LikeStorm
                            "[JubesX.name] along too." if Girl != JubesX and "met" in JubesX.History:
                                        $ Count = Girl.LikeJubes
                            "Never mind, probably a bad idea.":
                                        $ Girl.change_face("confused")
                                        if Girl == RogueX:
                                                ch_r "Okay. . ."
                                        elif Girl == KittyX:
                                                ch_k "Um. . ."
                                        elif Girl == EmmaX:
                                                ch_e "I see. . ."
                                        elif Girl == LauraX:
                                                ch_l "Um. . ."
                                        elif Girl == JeanX:
                                                ch_j "Uh. . . huh. . ."
                                        elif Girl == StormX:
                                                ch_s "Oh, very well."
                                        elif Girl == JubesX:
                                                ch_v ". . . right. . ."
                                        if bg_current != "bg_campus":
                                                ch_p "I'll meet you in the campus square then."
        if Count:
            #If you asked about another girl. . .
            if Count >= 600 and Approvalcheck(Girl, 800, "OI"): #Count is "Girl.LikeX"
                    $ Girl.change_face("smile")
                    if Girl == RogueX:
                            ch_r "Oh, yeah, sounds good."
                    elif Girl == KittyX:
                            ch_k "Sure, sounds fun."
                    elif Girl == EmmaX:
                            ch_e "She'd be lovely company."
                    elif Girl == LauraX:
                            ch_l "Sure, more's the merrier, I guess."
                    elif Girl == JeanX:
                            ch_j "I guess? Whatever."
                    elif Girl == StormX:
                            ch_s "That could be entertaining."
                    elif Girl == JubesX:
                            ch_v "Ok, sounds fun."
            elif Count >= 750:
                    $ Girl.change_face("bemused")
                    if Girl == RogueX:
                            ch_r "Oh, nice. . ."
                    elif Girl == KittyX:
                            ch_k "Hm, yeah. . ."
                    elif Girl == EmmaX:
                            ch_e "Hmmm, you have good taste. . ."
                    elif Girl == LauraX:
                            ch_l "Ok. . ."
                    elif Girl == JeanX:
                            ch_j "Oh, double our pleasure?"
                    elif Girl == StormX:
                            ch_s "That could be. . . distracting."
                    elif Girl == JubesX:
                            ch_v "Well, ok. . ."
            elif Approvalcheck(Girl, 1300, "LO"):
                    $ Girl.change_face("sad")
                    if Girl == RogueX:
                            ch_r "If that's what you're into. . ."
                    elif Girl == KittyX:
                            ch_k "I guess if that's what you want. . ."
                    elif Girl == EmmaX:
                            ch_e "Oh, if that's what you'd like. . ."
                    elif Girl == LauraX:
                            ch_l "If you insist. . ."
                    elif Girl == JeanX:
                            ch_j "Why not?"
                    elif Girl == StormX:
                            ch_s "I cannot think of a reason why not."
                    elif Girl == JubesX:
                            ch_v ". . . I guess?"
            else:
                    $ Girl.change_face("angry")
                    if Girl == RogueX:
                            ch_r "Keep tryin, polecat."
                    elif Girl == KittyX:
                            ch_k "You wish, player!"
                    elif Girl == EmmaX:
                            ch_e "No, I don't think I would be up for that."
                    elif Girl == LauraX:
                            ch_l "I'm out."
                    elif Girl == JeanX:
                            ch_j "You don't want that."
                            $ Girl.daily_history.append("yesdate")
                    elif Girl == StormX:
                            ch_s "I am not fine with that."
                    elif Girl == JubesX:
                            ch_v ". . . that's not ok with me."
                    $ Count = 0
                    return
            $ Girl.daily_history.append("yesdouble")
            if bg_current != "bg_campus":
                    ch_p "I'll meet you in the campus square then."
            $ Count = 0

        if bg_current != "bg_campus" or time_index < 2: #evening time
                if Girl == RogueX:
                        ch_r "Yeah, see you then!"
                elif Girl == KittyX:
                        ch_k "K', see you then!"
                elif Girl == EmmaX:
                        ch_e "Yes, see you then."
                elif Girl == LauraX:
                        ch_l "Right."
                elif Girl == JeanX:
                        ch_j "Sure."
                elif Girl == StormX:
                        ch_s "Later."
                elif Girl == JubesX:
                        ch_v "See you then!"
        $ Girl.daily_history.append("yesdate")
        $ Player.daily_history.append("yesdate")
        return

label Date_Stood_Up(Girl=0): #rkeljsv
    # if "stoodup" in Girl.Traits
    if Girl.location != bg_current:
            "[Girl.name] storms into the room."
            $ Girl.location = bg_current
            call Display_Girl(Girl)
    else:
            "[Girl.name] turns to you."
    $ Girl.change_face("confused")
    $ Girl.change_stat("love", 80, -10)
    if Girl == RogueX:
            ch_r "What're you thinkin not showin up for our date?"
    elif Girl == KittyX:
            ch_k "Hey, what gives? You didn't show up for our date!"
    elif Girl == EmmaX:
            ch_e "Can you explain where you were the other night?"
    elif Girl == LauraX:
            ch_l "We had plans, you didn't show."
    elif Girl == JeanX:
            ch_j "You forgot to show up."
    elif Girl == StormX:
            ch_s "You did not show for our prior engagement."
    elif Girl == JubesX:
            ch_v "Did you forget our date?"
    if "stoodup" in Girl.History:
            $ Girl.change_face("angry")
            $ Girl.change_stat("love", 80, -5)
            if Girl == RogueX:
                    ch_r "Again!"
            elif Girl == KittyX:
                    ch_k "Again!"
            elif Girl == EmmaX:
                    ch_e "And not for the first time!"
            elif Girl == LauraX:
                    ch_l "Again!"
            elif Girl == JeanX:
                    ch_j "I think I remember a pattern here."
            elif Girl == StormX:
                    ch_s "This is not the first time."
            elif Girl == JubesX:
                    ch_v "This isn't even the first time!"
    menu:
            extend ""
            "Oh, sorry about that, slipped my mind.":
                if Approvalcheck(Girl, 800, "LO") or Approvalcheck(Girl, 1200):
                        $ Girl.change_face("angry")
                        $ Girl.change_stat("love", 80, 5)
                        if Girl == RogueX:
                                ch_r "Well, 'least you own up ta your mistakes."
                        elif Girl == KittyX:
                                ch_k "I guess it can happen, but don't make a habit of it."
                        elif Girl == EmmaX:
                                ch_e "Hmph. Well at least you can be honest."
                        elif Girl == LauraX:
                                ch_l "I'll cut you a break, but don't make me cut you."
                        elif Girl == JeanX:
                                ch_j "You should be glad I can't make your name slip your mind."
                        elif Girl == StormX:
                                ch_s "An apology is a good start."
                        elif Girl == JubesX:
                                ch_v "Well. . . ok. . ."
                        if "stoodup" in Girl.History:
                                $ Girl.change_face("sad",Eyes="side")
                                $ Girl.change_stat("obedience", 80, 5)
                                if Girl == RogueX:
                                        ch_r "You need'ta shape up."
                                elif Girl == KittyX:
                                        ch_k "You really need to get your priorities in order."
                                elif Girl == EmmaX:
                                        ch_e "You need to do better than that, however."
                                elif Girl == LauraX:
                                        ch_l "Sort out your plans."
                                elif Girl == StormX:
                                        ch_s "Do better though."
                                elif Girl == JubesX:
                                        ch_v "Just stop letting this happen."
                elif "stoodup" in Girl.History:
                        $ Girl.change_face("sad",Eyes="side")
                        $ Girl.change_stat("love", 80, -5)
                        $ Girl.change_stat("obedience", 80, 5)
                        if Girl == RogueX:
                                ch_r "You need ta shape up!"
                        elif Girl == KittyX:
                                ch_k "You really need to get your priorities in order."
                        elif Girl == EmmaX:
                                ch_e "Well you need to stop slipping up."
                        elif Girl == LauraX:
                                ch_l "Sort out your plans."
                        elif Girl == JeanX:
                                ch_j "Sort of a habit with you. . ."
                        elif Girl == StormX:
                                ch_s "This is a habit you should correct."
                        elif Girl == JubesX:
                                ch_v "You need to stop letting this happen."
                else:
                        $ Girl.change_face("angry")
                        $ Girl.change_stat("obedience", 80, -2)
                        $ Girl.change_stat("inhibition", 60, 2)
                        if Girl == RogueX:
                                ch_r "\"Sorry\" ain't gonna cut it next time."
                        elif Girl == KittyX:
                                ch_k "You'll really have to make it up to me next time."
                        elif Girl == EmmaX:
                                ch_e "The next time, an apology may not be enough."
                                ch_e "If there is a next time."
                        elif Girl == LauraX:
                                ch_l "You're in the hole on this one."
                        elif Girl == JeanX:
                                ch_j "Wasn't me!"
                        elif Girl == StormX:
                                ch_s "If there is a next time, you will owe me."
                        elif Girl == JubesX:
                                ch_v "You need to do better next time."
            # end "sorry"

            "I can't imagine that happening, maybe you got the date wrong?":
                if "stoodup" in Girl.History and Approvalcheck(Girl, 800, "O",Alt=[[EmmaX],900]):
                        $ Girl.change_face("confused")
                        $ Girl.change_stat("obedience", 90, 15)
                        if Girl == RogueX:
                                ch_r "What? . . No, we definitely. . ."
                                $ Girl.change_face("confused",Eyes="side")
                                ch_r "Hm."
                        elif Girl == KittyX:
                                ch_k "Are you. . . I was sure that I. . ."
                                $ Girl.change_face("confused",Eyes="side")
                                ch_k "Huh."
                        elif Girl == EmmaX:
                                ch_e "What? . . No, we definitely. . ."
                                $ Girl.change_face("confused",Eyes="side")
                                ch_e "Hm."
                        elif Girl == LauraX:
                                ch_l "I don't think. . . I pretty sure. . ."
                                $ Girl.change_face("confused",Eyes="side")
                                ch_l "Eh."
                        elif Girl == JeanX:
                                $ Girl.change_face("confused")
                                ch_j "Hmm. . ."
                                $ Girl.change_face("sly")
                                ch_j "Nope, not possible."
                                ch_j "If I think it, it is."
                        elif Girl == StormX:
                                ch_s "What? . . that is. . . unlikely. . ."
                                $ Girl.change_face("confused",Eyes="side")
                                ch_s "Hm."
                        elif Girl == JubesX:
                                ch_v "Huh? . . . well. . ."
                                $ Girl.change_face("confused",Eyes="side")
                                ch_v ". . . maybe. . ."
                elif Approvalcheck(Girl, 700, "O",Alt=[[EmmaX],800]):
                        $ Girl.change_face("angry")
                        $ Girl.change_stat("obedience", 80, 5)
                        $ Girl.change_stat("obedience", 90, 10)
                        if Girl == RogueX:
                                ch_r "No. . . we definitely. . ."
                        elif Girl == KittyX:
                                ch_k "Um. . . I don't think so, but I guess it's possible. . ."
                        elif Girl == EmmaX:
                                ch_e "No. . . we definitely. . ."
                        elif Girl == LauraX:
                                ch_l ". . . I don't think so, but it's possible. . ."
                        elif Girl == JeanX:
                                ch_j "Nice try!"
                        elif Girl == StormX:
                                ch_s "Do not attempt to confuse me."
                        elif Girl == JubesX:
                                ch_v "That won't work on me!"
                elif Girl == EmmaX and not Approvalcheck(Girl, 700, "L"):
                        $ Girl.change_face("angry")
                        $ Girl.recent_history.append("angry")
                        $ Girl.daily_history.append("angry")
                        $ Girl.change_stat("love", 80, -10)
                        $ Girl.change_stat("obedience", 80, -5)
                        $ Girl.change_stat("inhibition", 70, 10)
                        ch_e "Don't even try that nonsense on me, [Girl.Petname]!"
                        ch_e "I INVENTED gaslighting."
                elif Girl != EmmaX and Approvalcheck(Girl, 500, "I"):
                        $ Girl.change_face("angry")
                        $ Girl.recent_history.append("angry")
                        $ Girl.daily_history.append("angry")
                        $ Girl.change_stat("love", 80, -10)
                        $ Girl.change_stat("inhibition", 70, 10)
                        if Girl == RogueX:
                                ch_r "Don't you try and twist that around on me!"
                        elif Girl == KittyX:
                                ch_k "Pull the other one, jerk."
                        elif Girl == LauraX:
                                ch_l "Yeah right."
                        elif Girl == JeanX:
                                ch_j "Nice Try!"
                        elif Girl == StormX:
                                ch_s "You can lie better than that."
                        elif Girl == JubesX:
                                ch_v "Don't even."
                else:
                        $ Girl.change_face("sad",Eyes="side")
                        $ Girl.recent_history.append("angry")
                        $ Girl.daily_history.append("angry")
                        $ Girl.change_stat("love", 80, -5)
                        $ Girl.change_stat("obedience", 80, -5)
                        $ Girl.change_stat("inhibition", 60, 5)
                        if Girl == RogueX:
                                ch_r "Doubt it, maybe think about a better apology."
                        elif Girl == KittyX:
                                ch_k "Well. . . I don't think so, stop bothering me."
                        elif Girl == EmmaX:
                                ch_e "Oh, [Girl.Petname], surely you can do better than that."
                        elif Girl == LauraX:
                                ch_l "Nope, not buying it."
                        elif Girl == JeanX:
                                ch_j "Nooooope."
                        elif Girl == StormX:
                                ch_s "Do not."
                        elif Girl == JubesX:
                                ch_v "Nope."
            #end "gaslight"

            "Yeah, I found something better to do.":
                if Approvalcheck(Girl, 1200, "LO"):
                        $ Girl.change_face("sad",Eyes="side")
                        $ Girl.change_stat("love", 80, -5)
                        $ Girl.change_stat("obedience", 80, 5)
                        if Girl == RogueX:
                                if "stoodup" in Girl.History:
                                        ch_r "Oh. . . "
                                        ch_r "Well, I guess you have your way. . ."
                                else:
                                        $ Girl.change_stat("obedience", 80, 10)
                                        ch_r "Oh. . . "
                                        ch_r "just, don't do it again."
                        elif Girl == KittyX:
                                if "stoodup" in Girl.History:
                                        ch_k "Yeah. . . "
                                        ch_k "You always seem to. . ."
                                else:
                                        $ Girl.change_stat("obedience", 80, 10)
                                        ch_k "Well. . . "
                                        ch_k "well don't let it happen again."
                        elif Girl == EmmaX:
                                if "stoodup" in Girl.History:
                                        ch_e "Oh. . . "
                                        ch_e "This independent streaks of yours is growing tiresome. . ."
                                else:
                                        $ Girl.change_stat("obedience", 80, 10)
                                        ch_e "Oh. . . "
                                        ch_e "don't push your luck."
                        elif Girl == LauraX:
                                if "stoodup" in Girl.History:
                                        ch_l "Yeah. . . "
                                        ch_l "That sounds like you. . ."
                                else:
                                        $ Girl.change_stat("obedience", 80, 10)
                                        ch_l "Huh. . . "
                                        ch_l "well don't do it again."
                        elif Girl == JeanX:
                                ch_j "We both know that's not possible."
                                if "stoodup" not in Girl.History:
                                        $ Girl.change_stat("obedience", 80, 10)
                                        ch_j "Just don't do it again."
                        elif Girl == StormX:
                                if "stoodup" in Girl.History:
                                        ch_s "That seems to be a habit for you. . ."
                                else:
                                        ch_s "I cannot imagine what that might be."
                        elif Girl == JubesX:
                                if "stoodup" in Girl.History:
                                        ch_v "Yeah, well. . . "
                                        ch_v "I also do things. . ."
                                else:
                                        ch_v "Yeah, well. . . "
                                        ch_v ". . . don't do it again!"
                elif Approvalcheck(Girl, 800, "LO"):
                        $ Girl.change_face("angry",Eyes="side")
                        $ Girl.change_stat("love", 80, -10)
                        $ Girl.change_stat("obedience", 80, 20)
                        if Girl == RogueX:
                                ch_r "You can do better than that."
                        elif Girl == KittyX:
                                ch_k "Well that's rude."
                        elif Girl == EmmaX:
                                ch_e "Surely you can do better than that."
                        elif Girl == LauraX:
                                ch_l "Maybe I did too."
                        elif Girl == JeanX:
                                $ Girl.change_face("confused",Eyes="side")
                                ch_j "That can't be it. . ."
                                ch_j "Maybe I did? . ."
                                $ Girl.change_face("sly",Eyes="side")
                                ch_j "Yeah, I guess that's it."
                        elif Girl == StormX:
                                ch_s "That is no excuse."
                        elif Girl == JubesX:
                                ch_v "Who cares?!"
                else:
                        $ Girl.change_face("angry")
                        $ Girl.change_stat("love", 80, -15)
                        $ Girl.change_stat("inhibition", 60, 5)
                        if Girl == RogueX:
                                ch_r "Oh, fuck off."
                        elif Girl == KittyX:
                                ch_k "Asshole."
                        elif Girl == EmmaX:
                                ch_e "Well then I suppose I have as well."
                        elif Girl == LauraX:
                                ch_l "Asshole."
                        elif Girl == JeanX:
                                ch_j "Not possible."
                        elif Girl == StormX:
                                ch_s "Do not attempt that."
                        elif Girl == JubesX:
                                ch_v "Don't even."
                        $ Girl.recent_history.append("angry")
                        $ Girl.daily_history.append("angry")
            #end "something better to do"

    $ Girl.Traits.remove("stoodup")
    if "stoodup" not in Girl.History:
            $ Girl.History.append("stoodup")

    return

label Readytogo(Girl=0,R=0,Girls=[]):  #rkeljsv
    #checks to see if you want to go on a date
    if Girl in all_Girls and "yesdate" in Girl.daily_history:
            #if a girl was sent and she has a date
            $ R = Girl
    else:
            $ Girls = all_Girls[:]
            while Girls:
                    if Girls[0].location == bg_current and "yesdate" in Girls[0].daily_history:
                            $ R = Girls[0]
                            $ Girls = [1]
                    $ Girls.remove(Girls[0])
    if R not in all_Girls:
            #if nobody was found. . .
            return

    if R.location != bg_current:
            # if the girl you have a date with isn't the one you're talking to. . .
            "You should probably head for that date."
    elif R == RogueX:
            ch_r "Ready to head out?"
    elif R == KittyX:
            ch_k "Wanna get going?"
    elif R == EmmaX:
            ch_e "We should be off."
    elif R == LauraX:
            ch_l "Ready?"
    elif R == JeanX:
            ch_j "Let's get going."
    elif R == StormX:
            ch_s "Shall we then?"
    elif R == JubesX:
            ch_v "Ready to go?"
    else:
            "Head out on your date?"
    menu:
        extend ""
        "Yes":
                $ renpy.pop_call() #removes call to ReadytoGo
                $ renpy.pop_call() #removes call to Chat
                jump Campus_Entry
        "Not yet":
                if R == RogueX:
                        ch_r "Ok, it's getting late though."
                elif R == KittyX:
                        ch_k "Fine."
                elif R == EmmaX:
                        ch_e "Fine, but we don't want to be late."
                elif R == LauraX:
                        ch_l "Ok, but we need to get going."
                elif R == JeanX:
                        ch_j "I'll give you a minute."
                elif R == StormX:
                        ch_s "Don't be long then."
                elif R == JubesX:
                        ch_v "Ok, just let me know."
                else:
                        "Suit yourself."
        "Let's cancel that date, just hang out.[[Room is full] (locked)" if R and R.location != bg_current and Room_Full():
                pass
        "Let's cancel that date, just hang out." if R and not Room_Full():
                #won't work if the room is full.
                if R == RogueX:  #checks if Rogue is in
                        ch_r "Yeah, ok, that's fine."
                elif R == KittyX:   #checks if Kitty is in
                        ch_k "Yeah, ok."
                elif R == EmmaX:   #checks if Emma is in
                        ch_e "Suit yourself."
                elif R == LauraX:   #checks if Laura is in
                        ch_l "Ok, whatever."
                elif R == JeanX:    #checks if Jean is in
                        ch_j "What?"
                        ch_j "Ok?"
                elif R == StormX:
                        ch_s ". . . Fine."
                elif R == JubesX:
                        ch_v "Well. . . ok?"
                $ R.daily_history.remove("yesdate")

                if R.location != bg_current:
                        # brings her if she wasn't already there
                        $ R.recent_history.append("summoned")
                        $ line = 0
                        if door_locked:
                                call Locked_Door(R)
                                return
                        $ R.location = bg_current
                        call Taboo_Level(0)
                        $ R.OutfitChange()
                        call set_the_scene
    return

label DateNight(Date_Bonus=[0,0],Play_Cost=0,Date_Cost=[0,0],Girls=[]):  #rkeljsv
    #(nee Prime_Bonus=0,Second_Bonus=0,Play_Cost=0,Prime_Cost=0,Second_Cost=0,Girls=[]):
    # Called from the event menu
    # Party[0] is the lead girl Party[1] the other.
    # Primary_Bonus and Secondary_Bonus track the girl's love bonuses, Cost is cost of the date

    $ Party = [] #clears Party if there is one

    $ Girls = active_Girls[:]
    while Girls:
        if "yesdate" in Girls[0].daily_history:  #checks if which girls are in
                $ Party.append(Girls[0])
                $ Girls[0].daily_history.remove("yesdate")
        $ Girls.remove(Girls[0])

    if not Party:
            "Nobody showed up, weird."
            return

    $ renpy.random.shuffle(Party)

    while len(Party) > 2:
            # If two or more members in the party
            #Culls down party size to two
            $ Party.remove(Party[2])


    # This portion sets the girls' clothing and mood for the date

    $ Girls = Party[:]
    while Girls:
            if "stoodup" in Girls[0].History:
                        $ Girls[0].History.remove("stoodup")
            call Date_Prep(Girls[0])#Rogue_Date_Prep
            $ Girls.remove(Girls[0])

    $ bg_current = "date"
    $ Player.AddWord(1,"date") #recent
    call shift_focus(Party[0])
    call set_the_scene

    if len(Party) >= 2:
        "As you arrive, you see [Party[0].name] and [Party[1].name] waiting for you."
        call Date_Crossed
        if not Party:
                # both left
                return
        elif len(Party) < 2:
                # One stayed, but not both
                ch_p "Ok then, I guess we're ready to get going. . ."
    else:
                "As you arrive, you see [Party[0].name] waiting for you."
    if Round <= 60:
            #kept waiting
            $ Party[0].change_stat("love", 90, -3)
            $ Party[0].change_stat("obedience", 50, 2)
            $ Party[0].change_stat("obedience", 70, 1)
            $ Party[0].change_face("angry")
            if len(Party) >= 2:
                    $ Party[1].change_stat("love", 90, -3)
                    $ Party[1].change_stat("obedience", 50, 2)
                    $ Party[1].change_stat("obedience", 70, 1)
                    $ Party[1].change_face("angry")
            if Party[0] == RogueX:
                    ch_r "You really kept me waiting, [Party[0].Petname]!"
            elif Party[0] == KittyX:
                    ch_k "So[KittyX.like]you really kept me waiting around. . ."
            elif Party[0] == EmmaX:
                    ch_e "Do you not think I have better things to do with my time than to wait for you?"
            elif Party[0] == LauraX:
                    ch_l "What took you so long?"
            elif Party[0] == JeanX:
                    $ Party[0].change_stat("obedience", 70, 2)
                    ch_j "You were supposed to be here hours ago!"
            elif Party[0] == StormX:
                    ch_s "If you were going to be late, you should have told me."
            elif Party[0] == JubesX:
                    ch_v "Hey, what was the hold-up?"
            menu:
                "Sorry, I got held up!":
                        $ Party[0].change_stat("love", 70, 1)
                        $ Party[0].change_stat("love", 90, 1)
                        $ Party[0].change_face("normal")
                        if len(Party) >= 2:
                                $ Party[1].change_stat("love", 70, 1)
                                $ Party[1].change_stat("love", 90, 1)
                                $ Party[1].change_face("normal")
                        call Anyline(Party[0],"Don't let it happen again.")
                "I lost track of time.":
                        $ Party[0].change_stat("love", 70, -1)
                        $ Party[0].change_stat("love", 90, -1)
                        $ Party[0].change_stat("obedience", 50, 1)
                        if len(Party) >= 2:
                                $ Party[1].change_stat("love", 70, -1)
                                $ Party[1].change_stat("love", 90, -1)
                                $ Party[1].change_stat("obedience", 50, 1)
                        call Anyline(Party[0],"Well spend your time better!")
                "I had stuff to take care of.":
                        $ Party[0].change_stat("love", 70, -1)
                        $ Party[0].change_stat("love", 90, -2)
                        $ Party[0].change_stat("obedience", 50, 1)
                        $ Party[0].change_stat("obedience", 70, 1)
                        if len(Party) >= 2:
                                $ Party[1].change_stat("love", 70, -1)
                                $ Party[1].change_stat("love", 90, -2)
                                $ Party[1].change_stat("obedience", 50, 1)
                                $ Party[1].change_stat("obedience", 70, 1)
                        call Anyline(Party[0],"That's not an excuse!")
    # end if Round <= 60:

    if Round <= 25:
            #no time
            $ Party[0].change_stat("love", 90, -3)
            $ Party[0].change_stat("obedience", 50, 1)
            $ Party[0].change_face("angry")
            if len(Party) >= 2:
                    $ Party[1].change_stat("love", 90, -3)
                    $ Party[1].change_stat("obedience", 50, 1)
                    $ Party[1].change_face("angry")
            call Anyline(Party[0],"It looks like there's no time to actually do anything tonight!")
            if Party[0] == RogueX:
                    ch_r "Well why even bother cleaning up?"
            elif Party[0] == KittyX:
                    ch_k "So[KittyX.like]is this how dates usually go with you?"
            elif Party[0] == EmmaX:
                    ch_e "This was a waste."
            elif Party[0] == LauraX:
                    ch_l "Huh."
            elif Party[0] == JeanX:
                    $ Party[0].change_stat("obedience", 70, 2)
                    ch_j "Did you just waste my time?"
            elif Party[0] == StormX:
                    ch_s "I do not appreciate you wasting my time."
            elif Party[0] == JubesX:
                    ch_v "Well that was pointless. . ."
            if len(Party) >= 2:
                    "The girls storm off."
            else:
                    "[Party[0].Tag] storms off."
            call remove_girl("all")
            $ bg_current = "bg_campus"
            $ Player.DrainWord("date") #recent
            $ Player.DrainWord("yesdate") #recent
            return
    #end if Round <= 25:

    $ line = 0
    if JeanX in Party and "dinner" not in Player.recent_history:
        ch_j "We're going to dinner now."
        menu:
            "Fine.":
                    $ line = "dinner"

            "And then a movie?":
                    $ line = "dinner"
                    if Approvalcheck(JeanX, 500, "LO"):
                            ch_j "Sure, movie after, whatever."
                    else:
                            ch_j "I don't want this to take all night."

            "No, we're going shopping." if "mall" in Player.History:
                    if Approvalcheck(JeanX, 700, "LO"):
                            ch_j "Ok, fine, shopping, whatever."
                            $ line = "shopping"
                    else:
                            ch_j "Well that was a short date."
                            call Girl_Date_Over(JeanX)
                            #if only girl, quit?

            "No, we're just going to a movie.":
                    if Approvalcheck(JeanX, 700, "LO"):
                            ch_j "Ok, fine, movie, whatever."
                            $ line = "movie"
                    else:
                            ch_j "Well that was a short date."
                            call Girl_Date_Over(JeanX)
                            #if only girl, quit?

    if line:
            #if Jean picked
            pass
    else:
            #if Jean didn't pick
            if Party[0] == RogueX:
                    ch_r "Where are we going?"
            elif Party[0] == KittyX:
                    ch_k "So[KittyX.like]where would you like to go?"
            elif Party[0] == EmmaX:
                    ch_e "Did you have a place in mind?"
            elif Party[0] == LauraX:
                    ch_l "Where we headed?"
            elif Party[0] == JeanX:
                    ch_j "So, where to?"
            elif Party[0] == StormX:
                    ch_s "Where should we go then?"
            elif Party[0] == JubesX:
                    ch_v "Ok, where to?"

            menu Date_Location:
                extend ""
                "To a restaurant." if "dinner" not in Player.recent_history and Round >= 20:
                        $ line = "dinner"
                "To a restaurant. (locked)" if "dinner" in Player.recent_history or Round <=20:
                        $ line = "dinner"

                "Let's shop." if "shopping" not in Player.recent_history and Round >= 20 and "mall" in Player.History:
                        $ line = "shopping"
                "Let's shop. (locked)" if ("shopping" in Player.recent_history or Round < 20) and "mall" in Player.History:
                        $ line = "shopping"

                "To the movies." if "movie" not in Player.recent_history and Round >= 60:
                        $ line = "movie"
                "To the movies [[No time]. (locked)" if "movie" in Player.recent_history or Round < 60:
                        $ line = "movie"

                "Let's head back.":
                        if "movie" in Player.recent_history or "dinner" in Player.recent_history or "shopping" in Player.recent_history:
                                #if you did anything at all. . .
                                show blackscreen onlayer black with dissolve
                                "It's getting late, you head back to the dorms. . ."
                        else:
                                $ Party[0].change_stat("love", 90, -3)
                                $ Party[0].change_stat("obedience", 50, 1)
                                if len(Party) >= 2:
                                        $ Party[1].change_stat("love", 90, -3)
                                        $ Party[1].change_stat("obedience", 50, 1)
                                if Party[0] == RogueX:
                                        ch_r "Well why even bother cleaning up?"
                                elif Party[0] == KittyX:
                                        ch_k "So[KittyX.like]is this how dates usually go with you?"
                                elif Party[0] == EmmaX:
                                        ch_e "This was a waste."
                                elif Party[0] == LauraX:
                                        ch_l "Huh."
                                elif Party[0] == JeanX:
                                        $ Party[0].change_stat("obedience", 70, 2)
                                        ch_j "Did you just waste my time?"
                                elif Party[0] == StormX:
                                        ch_s "I do not appreciate you wasting my time."
                                elif Party[0] == JubesX:
                                        ch_v "Well that was pointless. . ."
                                show blackscreen onlayer black with dissolve
                        $ line = 0
                        jump Date_End


    if len(Party) >= 2 and JeanX not in Party:
            if Party[1] == RogueX:
                    ch_r "Sounds fun."
            elif Party[1] == KittyX:
                    ch_k "K, let's get going then."
            elif Party[1] == EmmaX:
                    ch_e "Oh, lovely, shall we?"
            elif Party[1] == LauraX:
                    ch_l "Cool."
            elif Party[1] == StormX:
                    ch_s "That sounds lovely."
            elif Party[1] == JubesX:
                    ch_v "Ok, cool."
    else:
            if RogueX in Party:
                    ch_r "Sounds fun."
            elif KittyX in Party:
                    ch_k "K, let's get going then."
            elif EmmaX in Party:
                    ch_e "Oh, lovely, shall we?"
            elif LauraX in Party:
                    ch_l "Cool."
            elif StormX in Party:
                    ch_s "That sounds lovely."
            elif JubesX in Party:
                    ch_v "Ok, cool."

    show blackscreen onlayer black with dissolve

    if line == "dinner":
            "You go to one of the nicer restaurants in town. The food is quality but reasonably affordable."
            jump Date_Dinner
    elif line == "movie":
            "You head to the local theater and check out the film listings."
            jump Date_Movies
    elif line == "shopping":
            "You wander the mall, checking out some of the nicer boutiques."
            call Shopping_Mall
            jump Misplaced
    else:
            #somehow didn't pick a location?
            $ bg_current = "bg_campus"
            jump Misplaced

label Date_Crossed(Girls=[],check=0,Count=0,counter=0): #rkeljsv
    #this checks to make sure both girls are on the same page.
    #"girls" is the girls that are not cool with a double date.

    if Party[0] == RogueX and "yesdouble" not in RogueX.daily_history:
            ch_r "What's [Party[1].name] doing here?"
            $ Girls.append(RogueX)
    elif Party[0] == KittyX and "yesdouble" not in KittyX.daily_history:
            ch_k "Huh? What's [Party[1].name] doing here?"
            $ Girls.append(KittyX)
    elif Party[0] == EmmaX and "yesdouble" not in EmmaX.daily_history:
            ch_e "Oh, hello, why is [Party[1].name] here?"
            $ Girls.append(EmmaX)
    elif Party[0] == LauraX and "yesdouble" not in LauraX.daily_history:
            ch_l "Hey."
            ch_l "Why's [Party[1].name] here?"
            $ Girls.append(LauraX)
    elif Party[0] == JeanX and "yesdouble" not in JeanX.daily_history:
            ch_j "I don't remember inviting [Party[1].name]."
            $ Girls.append(JeanX)
    elif Party[0] == StormX and "yesdouble" not in StormX.daily_history:
            ch_s "Hello? What is [Party[1].name] doing here?"
            $ Girls.append(StormX)
    elif Party[0] == JubesX and "yesdouble" not in JubesX.daily_history:
            ch_v "What? Why's [Party[1].name] here?"
            $ Girls.append(JubesX)

    if Party[1] == RogueX and "yesdouble" not in RogueX.daily_history:
            if Girls:
                ch_r "Yeah, why's [Party[0].name] here?"
            else:
                ch_r "What's [Party[0].name] doing here?"
            $ Girls.append(RogueX)
    elif Party[1] == KittyX and "yesdouble" not in KittyX.daily_history:
            if Girls:
                ch_k "Yeah, what gives?"
            else:
                ch_k "Huh? What's [Party[0].name] doing here?"
            $ Girls.append(KittyX)
    elif Party[1] == EmmaX and "yesdouble" not in EmmaX.daily_history:
            if Girls:
                ch_e "Yes, care to explain?"
            else:
                ch_e "Oh, hello, why is [Party[0].name] here?"
            $ Girls.append(EmmaX)
    elif Party[1] == LauraX and "yesdouble" not in LauraX.daily_history:
            if Girls:
                ch_l "Yeah, what's up?"
            else:
                ch_l "Hey."
                ch_l "Why's [Party[0].name] here?"
            $ Girls.append(LauraX)
    elif Party[1] == JeanX and "yesdouble" not in JeanX.daily_history:
            if Girls:
                ch_j "Yeah, I don't remember inviting [Party[0].name]."
            else:
                ch_j "I don't remember inviting [Party[0].name]."
            $ Girls.append(JeanX)
    elif Party[1] == StormX and "yesdouble" not in StormX.daily_history:
            if Girls:
                ch_s "Yes, I would like to know this as well."
            else:
                ch_s "Hello? What is [Party[1].name] doing here?"
            $ Girls.append(StormX)
    elif Party[1] == JubesX and "yesdouble" not in JubesX.daily_history:
            if Girls:
                ch_v "Yeah, what's the deal?"
            else:
                ch_v "Hey, Why's [Party[0].name] here?"
            $ Girls.append(JubesX)

    if not Girls:
            #if both are fine with it, just return
            return

    menu:
        "I thought we could have fun together.":
                $ check = "fun"
        "Oh, I forgot to tell you?":
                $ check = "cute"
        "You're both coming with me.":
                $ check = "order"

        "Never mind [[ditch one or both]":
                menu:
                    "[RogueX.name], you can go" if RogueX in Party:
                            if Approvalcheck(RogueX, 1400, "LO"):
                                    $ RogueX.change_face("sad", 1)
                                    ch_r "Oh, ok, I guess. Later then?"
                                    "[RogueX.name] heads off."
                                    call Girl_Date_Over(RogueX,0)
                            else:
                                    call Girl_Date_Over(RogueX)
                    "[KittyX.name], you can go" if KittyX in Party:
                            if Approvalcheck(KittyX, 1400, "LO"):
                                    $ KittyX.change_face("sad", 1)
                                    ch_k "Huh? Well, ok, I guess?"
                                    "[KittyX.name] heads off."
                                    call Girl_Date_Over(KittyX,0)
                            else:
                                    call Girl_Date_Over(KittyX)
                    "[EmmaX.name], you can go" if EmmaX in Party:
                            if Approvalcheck(EmmaX, 1500, "LO"):
                                    $ EmmaX.change_face("sad", 1)
                                    ch_e "Hm. You'll have to make this up to me later."
                                    "[EmmaX.name] walks off."
                                    call Girl_Date_Over(EmmaX,0)
                            else:
                                    call Girl_Date_Over(EmmaX)
                    "[LauraX.name], you can go" if LauraX in Party:
                            if Approvalcheck(LauraX, 1500, "LO"):
                                    $ LauraX.change_face("sad", 1)
                                    ch_l "This choice will have consequences."
                                    "[LauraX.name] walks off."
                                    call Girl_Date_Over(LauraX,0)
                            else:
                                    call Girl_Date_Over(LauraX)
                    "[JeanX.name], you can go" if JeanX in Party:
                            if Approvalcheck(JeanX, 800, "LO"):
                                    $ JeanX.change_face("normal", 1,Eyes="side")
                                    if JeanX == Party[0]:
                                            ch_j "You heard him, get going [Party[1].name]."
                                            "[JeanX.name] apparently ignored you. . . and [Party[1].name] walks off."
                                            call Girl_Date_Over(Party[1],0)
                                    else:
                                            ch_j "You heard him, get going [Party[0].name]."
                                            "[JeanX.name] apparently ignored you. . . and [Party[0].name] walks off."
                                            call Girl_Date_Over(Party[0],0)
                            else:
                                    ch_j "I don't have time for this."
                                    call Girl_Date_Over(JeanX)
                    "[StormX.name], you can go" if StormX in Party:
                            if Approvalcheck(StormX, 1400, "LO"):
                                    $ StormX.change_face("sad", 1)
                                    ch_s "You will have much to explain later."
                                    "[StormX.name] walks off."
                                    call Girl_Date_Over(StormX,0)
                            else:
                                    call Girl_Date_Over(StormX)
                    "[JubesX.name], you can go" if JubesX in Party:
                            if Approvalcheck(JubesX, 1400, "LO"):
                                    $ JubesX.change_face("sad", 1)
                                    ch_v "What? Ok, fine. . ."
                                    "[JubesX.name] heads off."
                                    call Girl_Date_Over(JubesX,0)
                            else:
                                    call Girl_Date_Over(JubesX)


                    "Never mind. [[Go home]":
                            if RogueX in Party:
                                    if Approvalcheck(RogueX, 1400, "LO"):
                                        $ RogueX.change_face("sad", 1)
                                        ch_r "Oh, ok, I guess. Later then?"
                                        call Girl_Date_Over(RogueX,0)
                                    else:
                                        call Girl_Date_Over(RogueX)
                            if KittyX in Party:
                                    if Approvalcheck(KittyX, 1400, "LO"):
                                        $ KittyX.change_face("sad", 1)
                                        ch_k "Huh? Well, ok, I guess?"
                                        call Girl_Date_Over(KittyX,0)
                                    else:
                                        call Girl_Date_Over(KittyX)
                            if EmmaX in Party:
                                    if Approvalcheck(EmmaX, 1500, "LO"):
                                        $ EmmaX.change_face("sad", 1)
                                        ch_e "Hm. You'll have to make this up to me later."
                                        call Girl_Date_Over(EmmaX,0)
                                    else:
                                        call Girl_Date_Over(EmmaX)
                            if LauraX in Party:
                                    if Approvalcheck(LauraX, 1500, "LO"):
                                        $ LauraX.change_face("sad", 1)
                                        ch_l "This choice will have consequences."
                                        call Girl_Date_Over(LauraX,0)
                                    else:
                                        call Girl_Date_Over(LauraX)
                            if JeanX in Party:
                                    if Approvalcheck(JeanX, 1500, "LO"):
                                        $ JeanX.change_face("sad", 1)
                                        ch_j "Don't waste my time."
                                        call Girl_Date_Over(JeanX,0)
                                    else:
                                        call Girl_Date_Over(JeanX)
                            if StormX in Party:
                                    if Approvalcheck(StormX, 1500, "LO"):
                                        $ StormX.change_face("sad", 1)
                                        ch_s "You will have much to explain later."
                                        call Girl_Date_Over(StormX,0)
                                    else:
                                        call Girl_Date_Over(StormX)
                            if JubesX in Party:
                                    if Approvalcheck(JubesX, 1400, "LO"):
                                        $ JubesX.change_face("sad", 1)
                                        ch_v "What? Ok, fine. . ."
                                        call Girl_Date_Over(JubesX,0)
                                    else:
                                        call Girl_Date_Over(JubesX)

                            "You head back to your room."
                            if "yesdate" in Player.daily_history:
                                    $ Player.daily_history.remove("yesdate")
                            $ bg_current = "bg_player"
                            jump Misplaced
                return
    #end question menu

    $ counter = 2
    while counter:
            #checks to see whether each girls stays or goes
            #assumes that this process starts with two girls, Party[0] and [1]
            $ counter -= 1 #first time through is 1, second time through is 0, then out
            if len(Party) < 2:
                    #if the other girl's dropped out
                    if not Approvalcheck(Party[0], 1000,Alt=[[EmmaX,LauraX],800]):
                            #if the remaining girl isn't interested, this quits out.
                            if Party[0] == RogueX:
                                    ch_r "So. . . I'm going to get going too?"
                            elif Party[0] == KittyX:
                                    ch_k "Yeah, this is kind of a weird scene, maybe I'll see you later?"
                            elif Party[0] == EmmaX:
                                    ch_e "Unprofessional, but I do give you points for trying."
                            elif Party[0] == LauraX:
                                    ch_l "You need to plan better."
                                    ch_l "Almost seems like you did that on purpose."
                            elif Party[0] == JeanX:
                                    ch_j "I feel like you don't have your shit together."
                                    ch_j "You really need to get it together."
                            elif Party[0] == StormX:
                                    ch_s "[StormX.Petname], you really do need to plan with more care."
                            elif Party[0] == JubesX:
                                    ch_v "I don't know, [JubesX.Petname], I think I should just head back."
                            call Girl_Date_Over(Party[0],0)
                    return

            if check == "fun":
                    if Approvalcheck(Party[counter],1000):
                        $ check = 0
                    else:
                        $ check = -200
            elif check == "cute":
                    if Approvalcheck(Party[counter],1000,"LI"):
                        $ check = 200
                    else:
                        $ check = -100
            elif check == "order":
                    if Approvalcheck(Party[counter],1200,"LO"):
                        $ check = 100
                    else:
                        $ check = -300
            else:
                        $ check = 0

            if counter == 1:
                    $ Count = 0
            else:
                    $ Count = 1

            if Party[counter] == JeanX:
                    ch_j "Fine, let's get going. . ."
            elif Approvalcheck(Party[counter], 800, "OI", Bonus = check) and Party[counter].GirlLikecheck(Party[Count]) >= 600:
                    # If they like you well enough and get along with the other girl
                    # if the current iteration is 1, then it's Party[1].LikesParty[0]
                    # if the current iteration is 0, then it's Party[0].LikesParty[1]
                    $ Party[counter].change_face("smile")
                    if Party[counter] == RogueX:
                            ch_r "Sure, why not."
                    elif Party[counter] == KittyX:
                            ch_k "Sure, sounds fun."
                    elif Party[counter] == EmmaX:
                            ch_e "Alright, I'm in"
                    elif Party[counter] == LauraX:
                            ch_l "This could be fun. . ."
                    elif Party[counter] == StormX:
                            ch_s "I do not mind her company."
                    elif Party[counter] == JubesX:
                            ch_v "Sure, she's great."
            elif Party[counter].GirlLikecheck(Party[Count]) >= 750:
                    # if they really like the other girl
                    $ Party[counter].change_face("bemused")
                    if Party[counter] == RogueX:
                            ch_r "Oh, I guess. . ."
                    elif Party[counter] == KittyX:
                            ch_k "Hm, yeah. . ."
                    elif Party[counter] == EmmaX:
                            ch_e "This could be interesting. . ."
                    elif Party[counter] == LauraX:
                            ch_l "Nice"
                    elif Party[counter] == StormX:
                            ch_s "I do not mind her company."
                    elif Party[counter] == JubesX:
                            ch_v "K, that's cool."
            elif Approvalcheck(Party[counter], 1300, "LO", Bonus = check):
                    # if they especially like you
                    $ Party[counter].change_face("sad")
                    if Party[counter] == RogueX:
                            ch_r "If you insist. . ."
                    elif Party[counter] == KittyX:
                            ch_k "I guess if that's what you want. . ."
                    else:
                            call Anyline(Party[counter],"If you insist.")
            else:
                    $ Party[counter].change_face("angry")
                    if Party[counter] == RogueX:
                            ch_r "In your dreams!"
                    elif Party[counter] == KittyX:
                            ch_k "You wish, player!"
                    elif Party[counter] == EmmaX:
                            $ Party[counter].change_face("surprised",Mouth="smirk")
                            ch_e "Oh, you do aim high."
                            $ Party[counter].change_face("angry")
                            ch_e "Too high."
                    elif Party[counter] == LauraX:
                            $ Party[counter].change_face("surprised",Mouth="smirk")
                            ch_l "Really?"
                            $ Party[counter].change_face("angry")
                            ch_l "That's your play here."
                    elif Party[counter] == StormX:
                            ch_s "I will leave this one to the two of you."
                    elif Party[counter] == JubesX:
                            ch_v "Nah, you two have fun though. . ."
                    call Girl_Date_Over(Party[counter],0)
    #end check to see if they're cool with this. . .
    return

label Date_Prep(Girl=0):
    #This gets rthe girl Dressed and ready for Dinner, called by Date_Night
    if Girl not in all_Girls:
            "Tell Oni this girl called without a target girl."
            return
    $ Taboo = 40
    $ Girl.Taboo = 40
    if Girl.Clothing[7]:
            # if she has a date outfit set
            if Girl.Clothing[7] == 2:
                    $ Girl.Outfit = "casual2"
            elif Girl.Clothing[7] == 3:
                    $ Girl.Outfit = "custom1"
            elif Girl.Clothing[7] == 4:
                    $ Girl.Outfit = "gym"
            elif Girl.Clothing[7] == 5:
                    $ Girl.Outfit = "custom2"
            elif Girl.Clothing[7] == 6:
                    $ Girl.Outfit = "custom3"
            else:
                    $ Girl.Outfit = "casual1"
    else:
            $ Options = ["casual2", "casual1"]
            $ Options.append("custom1") if Girl.Custom1[0] == 2 else Options
            $ Options.append("custom2") if Girl.Custom2[0] == 2 else Options
            $ Options.append("custom3") if Girl.Custom3[0] == 2 else Options
            $ renpy.random.shuffle(Options)
            $ Girl.Outfit = Options[0]
            $ del Options[:]
    $ Girl.location = "date"
    $ Girl.OutfitChange(Changed=1)
    $ Girl.change_face("smile")
    return

label Date_Dinner:    #rkeljsv
    $ bg_current = "bg_restaurant"
    $ Player.recent_history.append("dinner")
    $ Player.daily_history.append("dinner")
    $ Girls = Party[:]
    while Girls:
        $ Girls[0].location = "bg_restaurant"
        $ Girls.remove(Girls[0])

    call set_the_scene

    "The waitress comes to the table."

    $ Girls = Party[:]
    while Girls:
        call expression Girls[0].Tag + "_Dinner"
        $ Girls.remove(Girls[0])
    call Player_Dinner

    "After a bit, the waitress brings you your meals."

    $ line = "You eat your " + line

    if JubesX in Party and "surfturf" in JubesX.recent_history:
            $ line = line + ", "+JubesX.name+" picks at her food but barely eats any of it."
    elif KittyX in Party and "surfturf" in KittyX.recent_history:
            $ line = line + ", "+KittyX.name+" eats the steak but pushes the lobster to the side."
    else:
            $ line = line + ", and have a pleasant conversation over the meal."

    "[line]"
    $ Player.recent_history.append("dinner")

    $ Count = 3
    while Count > 0:
            $ Count -= 1
            menu:
                "Chat with [Party[0].name]":
                        ch_p "Anything going on, [Party[0].name]?"
                        call expression Party[0].Tag + "_Chitchat"
                "Chat with [Party[1].name]" if len(Party) > 1:
                        ch_p "Anything going on, [Party[1].name]?"
                        call expression Party[1].Tag + "_Chitchat"
                "Compliment [Party[0].name]":
                        call Compliment(Party[0])
                "Compliment [Party[1].name]" if len(Party) > 1:
                        call Compliment(Party[1])
                "Just finish eating":
                        $ Count = 0

    call Dinner_Sex

    call Date_Paying("dinner")

    $ Round -= 30 if Round > 40 else (Round-10) #reduces Round to at minimum 10

    if Round < 20:
            "It's getting late, you head back to the dorms. . ."
            jump Date_End

    if not Party:
            "You decide to head back to your room."
            jump Date_Over

    "You seem to have some time left, where would you like to go next?"
    jump Date_Location #picks next stop. . .

label Player_Dinner: #rkeljsv
    # This is the player's menu choices
    menu:
        "For yourself, you order. . ."
        "Surf and turf. ($20)":
            $ Play_Cost = 20
            $ line = "steak and a juicy lobster"
        "Steak. ($15)":
            $ Play_Cost = 15
            $ line = "medium rare ribeye"
        "Chicken. ($10)":
            $ Play_Cost = 10
            $ line = "pangrilled chicken thighs"
        "Just a salad. ($5)":
            $ Play_Cost = 5
            $ line = "fresh garden salad"
    return

label Rogue_Dinner(GirlCost=0): #rkeljsv
    #Called by Date Dinner, picked Rogue's food
    menu:
        "For [RogueX.name] you order. . ."
        "Surf and turf. ($20)":
                $ RogueX.change_face("smile", Brows = "surprised")
                ch_r "Ooh, you're really pulling out the stops here."
                $ RogueX.change_face()
                $ RogueX.change_stat("love", 80, 5)
                $ RogueX.change_stat("love", 200, 2)
                $ GirlCost = 20
                $ RogueX.recent_history.append("surfturf")
        "Steak. ($15)":
                $ RogueX.change_face("smile")
                ch_r "I love a big, juicy steak."
                $ RogueX.change_stat("love", 80, 5)
                $ GirlCost = 15
                $ RogueX.recent_history.append("ribeye")
        "Chicken. ($10)":
                $ RogueX.change_face("smile")
                ch_r "I could always go for some chicken."
                $ RogueX.change_stat("love", 50, 1)
                $ RogueX.change_stat("love", 80, 3)
                $ GirlCost = 10
                $ RogueX.recent_history.append("chicken")
        "Just a salad. ($5)":
                $ RogueX.Mouth = "sad"
                $ RogueX.Eyes = "sexy"
                $ RogueX.Brows = "confused"
                ch_r "Well, I guess salad isn't that bad. . ."
                $ RogueX.change_stat("love", 60, -5)
                $ RogueX.change_stat("obedience", 50, 2)
                $ GirlCost = 5
                $ RogueX.recent_history.append("salad")
        "Why don't you choose, [RogueX.name]?":
                call Date_Bonus(RogueX,2)
                $ RogueX.change_face("smile")
                ch_r "Well thanks, [RogueX.Petname]. I think I'll have the chicken."
                $ RogueX.change_stat("love", 80, 5)
                $ RogueX.change_stat("inhibition", 50, 3)
                $ RogueX.change_stat("obedience", 50, -2)
                $ GirlCost = 10
                $ RogueX.recent_history.append("chicken")

    if Party[0] == RogueX:
            $ Date_Cost[0] = GirlCost
    else:
            $ Date_Cost[1] = GirlCost
    call Date_Bonus(RogueX,GirlCost)
    return

label Kitty_Dinner(GirlCost=0):
    #Called by Date Dinner, picked Kitty's food
    menu:
        "For [KittyX.name] you order. . ."
        "Surf and turf. ($20)":
                $ KittyX.change_face("sad",Brows = "surprised")
                ch_k "Um, I[KittyX.like]don't really eat shellfish. . ."
                $ KittyX.change_face()
                $ KittyX.change_stat("love", 80, -5)
                $ KittyX.change_stat("love", 200, -2)
                $ GirlCost = 20
                call Date_Bonus(KittyX,-11)
                $ KittyX.recent_history.append("surfturf")
        "Steak. ($15)":
                $ KittyX.change_face("smile")
                ch_k "Sounds delish."
                $ KittyX.change_stat("love", 80, 5)
                $ KittyX.change_stat("love", 200, 2)
                $ GirlCost = 15
                $ KittyX.recent_history.append("ribeye")
        "Chicken. ($10)":
                $ KittyX.change_face("smile")
                ch_k "Chicken's fine."
                $ KittyX.change_stat("love", 50, 1)
                $ KittyX.change_stat("love", 80, 3)
                $ GirlCost = 10
                $ KittyX.recent_history.append("chicken")
        "Just a salad. ($5)":
                $ KittyX.Mouth = "sad"
                $ KittyX.Eyes = "sexy"
                $ KittyX.Brows = "confused"
                ch_k "I do enjoy a nice salad."
                $ KittyX.change_stat("love", 60, -3)
                $ KittyX.change_stat("obedience", 50, 2)
                $ GirlCost = 5
                $ KittyX.recent_history.append("salad")
        "Why don't you choose, [KittyX.name]?":
                call Date_Bonus(KittyX,2)
                $ KittyX.change_face("smile")
                ch_k "Well thanks, [KittyX.Petname]. I think I'll have the steak."
                $ KittyX.change_stat("love", 80, 7)
                $ KittyX.change_stat("love", 200, 2)
                $ GirlCost = 15
                $ KittyX.recent_history.append("ribeye")
    if Party[0] == KittyX:
        $ Date_Cost[0] = GirlCost
    else:
        $ Date_Cost[1] = GirlCost
    call Date_Bonus(KittyX,GirlCost)
    return

label Emma_Dinner(GirlCost=0):
    #Called by Date Dinner, picked Emma's food
    menu:
        "For [EmmaX.name] you order. . ."
        "Surf and turf. ($20)":
                $ EmmaX.change_face("sly")
                ch_e "Hmm, a refined choice."
                $ EmmaX.change_face()
                $ EmmaX.change_stat("love", 80, 7)
                $ EmmaX.change_stat("love", 200, 3)
                $ GirlCost = 20
                $ EmmaX.recent_history.append("surfturf")
        "Steak. ($15)":
                $ EmmaX.change_face("smile")
                ch_e "I do enjoy tender meat."
                $ EmmaX.change_stat("love", 80, 5)
                $ GirlCost = 15
                $ EmmaX.recent_history.append("ribeye")
        "Chicken. ($10)":
                $ EmmaX.change_face("smile")
                ch_e "Chicken is fine."
                $ EmmaX.change_stat("love", 50, 1)
                $ EmmaX.change_stat("love", 80, 3)
                $ GirlCost = 10
                $ EmmaX.recent_history.append("chicken")
        "Just a salad. ($5)":
                $ EmmaX.Mouth = "sad"
                $ EmmaX.Eyes = "sexy"
                $ EmmaX.Brows = "confused"
                ch_e "I suppose I could go for a salad. . ."
                $ EmmaX.change_stat("love", 60, -3)
                $ EmmaX.change_stat("obedience", 50, -2)
                $ GirlCost = 5
                $ EmmaX.recent_history.append("salad")
        "Why don't you choose, [EmmaX.name]?":
                call Date_Bonus(EmmaX,2)
                $ EmmaX.change_face("smile")
                ch_e "Thank you, [EmmaX.Petname]. I believe I'll have the steak."
                $ EmmaX.change_face("sly")
                ch_e ". . .and the lobster, of course."
                $ EmmaX.change_stat("love", 80, 5)
                $ EmmaX.change_stat("inhibition", 50, 3)
                $ EmmaX.change_stat("obedience", 50, -2)
                $ GirlCost = 20
                $ EmmaX.recent_history.append("surfturf")

    if Party[0] == EmmaX:
        $ Date_Cost[0] = GirlCost
    else:
        $ Date_Cost[1] = GirlCost
    call Date_Bonus(EmmaX,GirlCost)
    return

label Laura_Dinner(GirlCost=0):
    #Called by Date Dinner, picked Laura's food
    menu:
        "For [LauraX.name] you order. . ."
        "Surf and turf. ($20)":
                $ LauraX.change_face("sad",Brows = "surprised")
                ch_l "Nice. . ."
                $ LauraX.change_face()
                $ LauraX.change_stat("love", 80, 5)
                $ LauraX.change_stat("love", 90, 2)
                $ GirlCost = 20
                $ LauraX.recent_history.append("surfturf")
        "Steak. ($15)":
                $ LauraX.change_face("smile")
                ch_l "Rare."
                $ LauraX.change_stat("love", 80, 5)
                $ LauraX.change_stat("love", 90, 2)
                $ GirlCost = 15
                $ LauraX.recent_history.append("ribeye")
        "Chicken. ($10)":
                $ LauraX.change_face("smile")
                ch_l "Yeah, ok."
                $ LauraX.change_stat("love", 50, 1)
                $ LauraX.change_stat("love", 80, 3)
                $ GirlCost = 10
                $ LauraX.recent_history.append("chicken")
        "Just a salad. ($5)":
                $ LauraX.Mouth = "sad"
                $ LauraX.Eyes = "sexy"
                $ LauraX.Brows = "confused"
                ch_l "Um. no."
                $ LauraX.change_stat("love", 60, -5)
                $ LauraX.change_stat("obedience", 50, -2)
                $ LauraX.change_stat("inhibition", 60, 2)
                ch_l "Steak, rare."
                $ GirlCost = 15
                $ LauraX.recent_history.append("ribeye")
        "Why don't you choose, [LauraX.name]?":
                call Date_Bonus(LauraX,2)
                $ LauraX.change_face("smile")
                ch_l "Thanks. I think I'll have the steak."
                $ LauraX.change_stat("love", 80, 7)
                $ LauraX.change_stat("obedience", 60, 2)
                $ LauraX.change_stat("love", 200, 2)
                $ GirlCost = 15
                $ LauraX.recent_history.append("ribeye")

    if Party[0] == LauraX:
        $ Date_Cost[0] = GirlCost
    else:
        $ Date_Cost[1] = GirlCost
    call Date_Bonus(LauraX,GirlCost)
    return

label Jean_Dinner(GirlCost=0):
    #Called by Date Dinner, picked Jean's food
    if not Approvalcheck(JeanX, 500, "O"):
            ch_j "I'll have the surf and turf."
            $ Passline = renpy.random.choice(["-but I want to substitute the steak for veal.",
                    "-but I want two lobsters.",
                    "-rare.",
                    "-well done.",
                    "-but I want crab legs instead of lobster.",
                    "-but I want to substitute the lobster for another steak.",
                    "-but I want to substitute the steak for an extra lobster."])
            ch_j "[Passline]"
            $ GirlCost = 20
            $ JeanX.recent_history.append("surfturf")
    else:
            ch_j "I'd like-"
            menu:
                "For [JeanX.name] you order. . ."
                "Surf and turf. ($20)":
                        $ JeanX.change_face("sly",Brows = "surprised")
                        ch_j "Good choice."
                        $ JeanX.change_face()
                        $ JeanX.change_stat("love", 80, 3)
                        $ JeanX.change_stat("love", 90, 2)
                        $ JeanX.change_stat("obedience", 70, 2)
                        $ GirlCost = 20
                        $ JeanX.recent_history.append("surfturf")
                "Steak. ($15)":
                        $ JeanX.change_face("smile")
                        ch_j "I guess that's fine."
                        $ JeanX.change_stat("love", 80, 2)
                        $ JeanX.change_stat("love", 90, 1)
                        $ JeanX.change_stat("obedience", 70, 2)
                        $ GirlCost = 15
                        $ JeanX.recent_history.append("ribeye")
                "Chicken. ($10)":
                        $ JeanX.change_face("smile")
                        ch_j "Yeah, whatever."
                        $ JeanX.change_stat("love", 50, 1)
                        $ JeanX.change_stat("love", 80, 3)
                        $ JeanX.change_stat("obedience", 70, 2)
                        $ GirlCost = 10
                        $ JeanX.recent_history.append("chicken")
                "Just a salad. ($5)":
                        $ JeanX.Mouth = "sad"
                        $ JeanX.Eyes = "sexy"
                        $ JeanX.Brows = "confused"
                        $ JeanX.change_stat("love", 60, -5)
                        $ JeanX.change_stat("obedience", 70, 2)
                        $ JeanX.change_stat("inhibition", 60, 2)
                        ch_j "Righ- wait, what?"
                        if Approvalcheck(JeanX, 700, "O"):
                                $ JeanX.change_stat("love", 60, 5)
                                $ JeanX.change_stat("obedience", 80, 2)
                                $ JeanX.change_stat("obedience", 90, 3)
                                $ GirlCost = 5
                                $ JeanX.recent_history.append("salad")
                        else:
                                $ JeanX.change_face("sly")
                                $ JeanX.change_stat("love", 60, -2)
                                $ JeanX.change_stat("obedience", 70, 2)
                                $ JeanX.change_stat("inhibition", 60, 2)
                                ch_j "No, Steak."
                                if Approvalcheck(JeanX, 800, "O"):
                                        $ GirlCost = 15
                                        $ JeanX.recent_history.append("ribeye")
                                else:
                                        ch_j "and lobster."
                                        $ GirlCost = 20
                                        $ JeanX.recent_history.append("surfturf")
                "Why don't you choose, [JeanX.name]?":
                        call Date_Bonus(JeanX,2)
                        $ JeanX.change_face("smile")
                        ch_j "I think I'll have the surf and turf."
                        $ JeanX.change_stat("love", 80, 3)
                        $ JeanX.change_stat("obedience", 80, 2)
                        $ GirlCost = 20
                        $ JeanX.recent_history.append("surfturf")
            #end menu

    if Party[0] == JeanX:
        $ Date_Cost[0] = GirlCost
    else:
        $ Date_Cost[1] = GirlCost
    call Date_Bonus(JeanX,GirlCost)
    return

label Storm_Dinner(GirlCost=0):
    #Called by Date Dinner, picked Storm's food
    menu:
        "For [StormX.name] you order. . ."
        "Surf and turf. ($20)":
                $ StormX.change_face("confused",Mouth="smile")
                ch_s "This is a bit heavy. . ."
                $ StormX.change_face()
                $ StormX.change_stat("love", 80, 3)
                $ GirlCost = 20
                $ StormX.recent_history.append("surfturf")
        "Steak. ($15)":
                $ StormX.change_face("smile")
                ch_s "A steak is nice, from time to time."
                $ StormX.change_stat("love", 80, 3)
                $ GirlCost = 15
                $ StormX.recent_history.append("ribeye")
        "Chicken. ($10)":
                $ StormX.change_face("smile")
                ch_s "Chicken would be delicious."
                $ StormX.change_stat("love", 50, 1)
                $ StormX.change_stat("love", 80, 2)
                $ StormX.change_stat("love", 200, 1)
                $ GirlCost = 10
                $ StormX.recent_history.append("chicken")
        "Just a salad. ($5)":
                $ StormX.change_face("smile")
                ch_s "I do enjoy a vegetarian option. . ."
                $ StormX.change_stat("love", 60, 2)
                $ StormX.change_stat("obedience", 50, 1)
                $ GirlCost = 5
                $ StormX.recent_history.append("salad")
        "Why don't you choose, [StormX.name]?":
                call Date_Bonus(StormX,2)
                $ StormX.change_face("smile")
                ch_s "Thank you, [StormX.Petname]. I'll have the chicken then."
                $ StormX.change_stat("love", 80, 5)
                $ StormX.change_stat("inhibition", 50, 3)
                $ StormX.change_stat("obedience", 50, -2)
                $ GirlCost = 20
                $ StormX.recent_history.append("chicken")

    if Party[0] == StormX:
        $ Date_Cost[0] = GirlCost
    else:
        $ Date_Cost[1] = GirlCost
    call Date_Bonus(StormX,GirlCost)
    return

label Jubes_Dinner(GirlCost=0):
    #Called by Date Dinner, picked Jubes's food
    menu:
        "For [JubesX.name] you order. . ."
        "Surf and turf. ($20)":
                $ JubesX.change_face("sad",Brows = "surprised")
                ch_v "Show-off. . ."
                $ JubesX.change_face()
                $ JubesX.change_stat("love", 80, -5)
                $ JubesX.change_stat("love", 200, -2)
                $ GirlCost = 20
                call Date_Bonus(JubesX,-11)
                $ JubesX.recent_history.append("surfturf")
        "Steak. ($15)":
                $ JubesX.change_face("smile")
                ch_v "Keep it bloody."
                if renpy.random.randint(1, 20) > 10:
                    ch_v "And when I say \"bloody\". . ."
                    ch_v "I mean that if I see a single scorch mark on that steak. . ."
                    ch_v "I'm coming after you."
                $ JubesX.change_stat("love", 80, 3)
                $ JubesX.change_stat("love", 200, 2)
                $ GirlCost = 15
                $ JubesX.recent_history.append("ribeye")
        "Chicken. ($10)":
                $ JubesX.change_face("smile")
                ch_v "Sure, whatever."
                $ JubesX.change_stat("love", 50, 1)
                $ JubesX.change_stat("love", 80, 1)
                $ GirlCost = 10
                $ JubesX.recent_history.append("chicken")
        "Just a salad. ($5)":
                $ JubesX.Mouth = "sad"
                $ JubesX.Eyes = "sexy"
                $ JubesX.Brows = "confused"
                ch_v "I wouldn't want to overspend."
                $ JubesX.change_stat("love", 60, 3)
                $ JubesX.change_stat("obedience", 50, 2)
                $ GirlCost = 5
                $ JubesX.recent_history.append("salad")
        "Why don't you choose, [JubesX.name]?":
                call Date_Bonus(JubesX,2)
                $ JubesX.change_face("smile")
                ch_v "Oh, thanks, [JubesX.Petname]. I guess I'll have the salad."
                $ JubesX.change_stat("love", 60, 3)
                $ JubesX.change_stat("love", 80, 7)
                $ JubesX.change_stat("love", 200, 2)
                $ GirlCost = 15
                $ JubesX.recent_history.append("ribeye")
    if Party[0] == JubesX:
        $ Date_Cost[0] = GirlCost
    else:
        $ Date_Cost[1] = GirlCost
    call Date_Bonus(JubesX,(int(GirlCost/2)))
    return

label Dinner_Sex(Girl=0,Previous=0,GirlBonus=0,OptionsDS=[],Girls=[]):#rkeljsv
    #Called by Dinner Sex

    $ Girls = Party[:]
    if 0 in Girls:
        $ Girls.remove(0)
    while Girls: #add option later to make Jubilee more likely here
            if Approvalcheck(Girls[0], 1000):  #checks if Girls[0] is in
                    $ OptionsDS.append(Girls[0])
                    if Party[0] == Girls[0] and Date_Bonus[0] > 10:
                            $ OptionsDS.append(Girls[0])
                    elif Girls[0] in Party and Date_Bonus[1] > 10:
                            $ OptionsDS.append(Girls[0])
            $ Girls.remove(Girls[0])

    if len(OptionsDS) == 0:
            #if nobody is in, return
            return

    $ renpy.random.shuffle(OptionsDS)

    $ Girl = OptionsDS[0]               #picks lead
    if len(Party) >= 2:
            if Girl == Party[0]:
                    $ Previous = Party[1]
            else:
                    $ Previous = Party[0]

    if Girl == Previous:
        "Tell Oni that on a date, a girl and previous were the same, [Girl.Tag], DS"

    $ OptionsDS =["nothing"]

    if Party[0] == Girl:
        $ GirlBonus = Date_Bonus[0] + Date_Cost[0]
    else:
        $ GirlBonus = Date_Bonus[1] + Date_Cost[1]

    if Girl.Anal and Approvalcheck(Girl, 1500) and GirlBonus >=15:
            $ OptionsDS.append("anal")
    if Girl.Sex and Approvalcheck(Girl, 1500) and GirlBonus >=10:
            $ OptionsDS.append("sex")
    if Girl.Blow and Approvalcheck(Girl, 1300) and GirlBonus >=10:
            $ OptionsDS.append("blowjob")
    if Girl.Hand and Approvalcheck(Girl, 1000) and GirlBonus >=10:
            $ OptionsDS.append("handjob")
    if Girl.FondleP and Approvalcheck(Girl, 1000) and GirlBonus >=10:
            $ OptionsDS.append("pussy")
    if Approvalcheck(Girl, 1000) and GirlBonus >=10:
            $ OptionsDS.append("footjob")

    $ renpy.random.shuffle(OptionsDS)

    $ Girl.change_face("sexy")
    if OptionsDS[0] == "nothing":
        pass
    elif OptionsDS[0] == "anal":
        "Halfway through the meal, [Girl.name] gets a sly look on her face."
        "She nods her head suggestively towards the restrooms, and then excuses herself."
        call Date_Sex_Break(Girl,Previous)
        if _return == 4: #you refused
                $ Girl.change_face("sadside", 2)
                "You wait a few minutes until she returns, seemingly a bit annoyed at you."
                $ Girl.change_stat("love", 90, -5)
                $ Girl.change_stat("inhibition", 80, -10)
                call Date_Bonus(Girl,-5)
        else:
                if _return == 1: #other girl is fine
                        "A few seconds later, you and [Previous.name] follow her and she drags you both inside, locking the door behind you."
                        "She spends the next several minutes taking it up the ass while [Previous.name] feels you both up."
                        $ Girl.GLG(Previous,1000,3,1)
                        $ Previous.GLG(Girl,1000,2,1)
                else:
                        "A few seconds later, you follow her and she drags you inside, locking the door behind you."
                        "She spends the next several minutes taking it up the ass."
                if _return == 3:
                        "[Previous.name] stares daggers at you both as you return to the table."
                        call Date_Bonus(Previous,-10)
                if Girl == RogueX:
                        ch_r "I hope I'll still be able to sit down later."
                elif Girl == KittyX:
                        ch_k "That was {i}so{/i} worth it."
                elif Girl == EmmaX:
                        ch_e "Thank you for helping with the stuffing, [Girl.Petname]."
                elif Girl == LauraX:
                        ch_l "Worth it."
                elif Girl == JeanX:
                        ch_j "Hmmm, thanks [Girl.Petname]."
                elif Girl == StormX:
                        ch_s "Quite. . . filling, [Girl.Petname]."
                elif Girl == JubesX:
                        ch_v "See, -that- was how you fill me up."
                $ Girl.change_stat("inhibition", 50, 9)
                $ Girl.change_stat("inhibition", 80, 3)
                $ Girl.Addict -= 20
                $ Girl.SeenPeen += 1
                $ Girl.Anal += 1
                $ Player.Semen -= 1
                $ Girl.recent_history.append("anal")
                $ Girl.recent_history.append("dinnersex")
                $ Girl.daily_history.append("anal")
    elif OptionsDS[0] == "sex":
        "Halfway through the meal, [Girl.name] gets a sly look on her face."
        "She nods her head suggestively towards the restrooms, and then excuses herself."
        call Date_Sex_Break(Girl,Previous)
        if _return == 4: #you refused
                $ Girl.change_face("sadside", 2)
                "You wait a few minutes until she returns, seemingly a bit annoyed at you."
                $ Girl.change_stat("love", 90, -5)
                $ Girl.change_stat("inhibition", 80, -10)
                call Date_Bonus(Girl,-5)
        else:
                if _return == 1: #other girl is fine
                        "A few seconds later, you and [Previous.name] follow her and she drags you both inside, locking the door behind you."
                        "She spends the next several minutes fucking you raw while [Previous.name] feels you both up."
                        $ Girl.GLG(Previous,1000,3,1)
                        $ Previous.GLG(Girl,1000,2,1)
                else:
                        "A few seconds later, you follow her and she drags you inside, locking the door behind you."
                        "She spends the next several minutes fucking you raw."
                if _return == 3:
                        "[Previous.name] stares daggers at you both as you return to the table."
                        call Date_Bonus(Previous,-10)
                if Girl == RogueX:
                        ch_r "I needed to work off that meal a bit."
                elif Girl == KittyX:
                        ch_k "That was a workout."
                elif Girl == EmmaX:
                        ch_e "A little after dinner workout never hurt."
                elif Girl == LauraX:
                        ch_l "Sorry about the scratches."
                elif Girl == JeanX:
                        ch_j "Hmmm, thanks [Girl.Petname]."
                elif Girl == StormX:
                        ch_s "Quite. . . filling, [Girl.Petname]."
                elif Girl == JubesX:
                        ch_v "See, -that- was how you stuff my belly."
                $ Girl.change_stat("inhibition", 50, 8)
                $ Girl.change_stat("inhibition", 80, 2)
                $ Girl.Addict -= 20
                $ Girl.SeenPeen += 1
                $ Girl.Sex += 1
                $ Player.Semen -= 1
                $ Girl.recent_history.append("sex")
                $ Girl.recent_history.append("dinnersex")
                $ Girl.daily_history.append("sex")
    elif OptionsDS[0] == "blowjob":
        "Halfway through the meal, [Girl.name] gets a sly look on her face, then knocks her fork off the table."
        "She ducks under the table after it, and unzips your pants."
        call Date_Sex_Break(Girl,Previous)
        if _return == 4: #you refused
                $ Girl.change_face("sadside", 2)
                "You zip them back up and shoo her away. She gets back up from under the table."
                $ Girl.change_stat("love", 90, -5)
                $ Girl.change_stat("inhibition", 80, -5)
                call Date_Bonus(Girl,-3)
                if Girl == EmmaX:
                        $ Girl.change_stat("obedience", 70, 5)
                        ch_e "Found it. . ."
        else:
                if _return == 1:
                        #other girl is fine
                        "[Previous.name] shifts closer and wraps one arm around you, the other hand caressing [Girl.name]'s cheek."
                        "[Girl.name] then procedes to blow you for several minutes until you cum."
                        $ Girl.GLG(Previous,1000,2,1)
                        $ Previous.GLG(Girl,1000,1,1)
                elif _return == 2: #other girl is fine
                        "She then procedes to blow you for several minutes until you cum, while [Previous.name] pretends to be occupied."
                else:
                        "She then procedes to blow you for several minutes until you cum."
                $ Girl.change_stat("inhibition", 50, 6)
                $ Girl.change_stat("inhibition", 80, 2)
                $ Girl.recent_history.append("blowjob")
                $ Girl.recent_history.append("dinnersex")
                $ Girl.daily_history.append("blowjob")
                if Girl.Swallow:
                    "[Girl.name] wipes her mouth as she climbs out from under the table."
                    if Girl == RogueX:
                            ch_r "I don't think we need desert, [Girl.Petname]."
                    elif Girl == KittyX:
                            ch_k "That hit the spot. . ."
                    elif Girl == EmmaX:
                            ch_e "Hmm, a creamy aperitif."
                    elif Girl == LauraX:
                            ch_l "Yum. . ."
                    elif Girl == JeanX:
                            ch_j "Mmm. . .."
                    elif Girl == StormX:
                            ch_s "I love the deserts here, don't you, [Girl.Petname]?"
                    elif Girl == JubesX:
                            ch_v "My compliments to the chef. . ."
                    $ Girl.Addict -= 20
                    $ Girl.Swallow += 1
                    $ Girl.recent_history.append("swallow")
                    $ Girl.daily_history.append("swallow")
                else:
                    "[Girl.name] grabs the napkin off your lap and uses it to collect the jiz."
                    if Girl == RogueX:
                            ch_r "I bet the cleaning crew will enjoy that."
                    elif Girl == KittyX:
                            ch_k "I feel kinda sorry for the busboys."
                    elif Girl == EmmaX:
                            ch_e "I suppose that is a bit rude to the help."
                    elif Girl == LauraX:
                            ch_l "Sorry about the mess."
                    elif Girl == JeanX:
                            ch_j "Oh waiter? Clean this up."
                    elif Girl == StormX:
                            ch_s "We should tip well, [Girl.Petname]."
                    elif Girl == JubesX:
                            "She then licks it up. . ."
                            ch_v "My compliments to the chef. . ."
                            $ Girl.Addict -= 20
                            $ Girl.Swallow += 1
                            $ Girl.recent_history.append("swallow")
                            $ Girl.daily_history.append("swallow")
                $ Girl.change_stat("inhibition", 30, 4)
                $ Girl.change_stat("inhibition", 80, 2)
                $ Girl.SeenPeen += 1
                $ Girl.Addict -= 10
                $ Girl.Blow += 1
                $ Player.Semen -= 1
                if _return == 3:
                    "[Previous.name] stares daggers at you both as [Girl.name] crawls out from under the table."
                    call Date_Bonus(Previous,-10)
    elif OptionsDS[0] == "handjob":
        "Halfway through the meal, [Girl.name] gets a sly look on her face, then shifts her chair around next to yours."
        call Date_Sex_Break(Girl,Previous)
        if _return == 4:
                #you refused
                $ Girl.change_face("sadside", 2)
                "She tries to unzip your pants under the table, but you shoo her away."
                $ Girl.change_stat("love", 90, -5)
                $ Girl.change_stat("inhibition", 80, -5)
                call Date_Bonus(Girl,-2)
        else:
                if _return == 1: #other girl is fine
                        "She unzips your pants under the table, and proceeds to caress your cock."
                        "On the other side, [Previous.name] also reaches down and gets into the action."
                        $ line = "They"
                        $ Previous.Hand += 1
                        $ Previous.recent_history.append("handjob")
                        $ Previous.daily_history.append("handjob")
                        $ Girl.GLG(Previous,600,3,1)
                        $ Previous.GLG(Girl,600,2,1)
                        $ Girl.GLG(Previous,1000,2,1)
                        $ Previous.GLG(Girl,1000,1,1)
                elif _return == 2: #other girl is fine
                        "She unzips your pants under the table, and proceeds to caress your cock, while [Previous.name] pretends to be occupied."
                        $ line = "She"
                else:
                        "She unzips your pants under the table, and proceeds to caress your cock."
                        $ line = "She"
                if Girl.Blow and (Approvalcheck(Girl, 1200) or Girl == JubesX):
                        "Just as you're about to cum, [Girl.name] ducks her head under the table and comes up with a mouth full."
                        $ Girl.SeenPeen += 1
                        $ Girl.Blow += 1
                        $ Girl.Addict -= 20
                        $ Girl.Swallow += 1
                        $ Girl.recent_history.append("swallow")
                        $ Girl.daily_history.append("swallow")
                else:
                        "[line] continues stroking it until you cum into the napkin."
                        if Girl == RogueX:
                                ch_r "I bet the cleaning crew will enjoy that."
                        elif Girl == KittyX:
                                ch_k "I feel kinda sorry for the busboys."
                        elif Girl == EmmaX:
                                ch_e "I bet the cleaning crew will enjoy that."
                        elif Girl == LauraX:
                                ch_l "Sorry about the mess."
                        elif Girl == JeanX:
                                ch_j "Oh waiter? Clean this up."
                        elif Girl == StormX:
                                ch_s "We should tip well, [Girl.Petname]."
                        elif Girl == JubesX:
                                "She then licks it up. . ."
                                ch_v "My compliments to the chef. . ."
                                $ Girl.Addict -= 20
                                $ Girl.Swallow += 1
                                $ Girl.recent_history.append("swallow")
                                $ Girl.daily_history.append("swallow")
                $ line = 0
                $ Girl.change_stat("inhibition", 30, 4)
                $ Girl.change_stat("inhibition", 80, 2)
                $ Girl.Hand += 1
                $ Player.Semen -= 1
                $ Girl.Addict -= 5
                $ Girl.recent_history.append("handjob")
                $ Girl.daily_history.append("handjob")
                if _return == 3:
                    "[Previous.name] stares daggers at you both from across the table."
                    call Date_Bonus(Previous,-5)
    elif OptionsDS[0] == "pussy":
        "Halfway through the meal, [Girl.name] gets a sly look on her face, then shifts her chair around next to yours."
        call Date_Sex_Break(Girl,Previous)
        if _return == 4:
                #you refused
                if Girl.Legs:
                    "She takes your hand and pulls it over to her crotch, shoving it under her [Girl.Legs]."
                else:
                    "She takes your hand and shoves it into her crotch."
                $ Girl.change_face("sadside", 2)
                "With a glance at [Previous.name], you jerk your hand away."
                $ Girl.change_stat("love", 90, -5)
                $ Girl.change_stat("inhibition", 80, -5)
                call Date_Bonus(Girl,-3)
        else:
                if Girl.Legs:
                        "She takes your hand and pulls it over to her crotch, shoving it under her [Girl.Legs]."
                else:
                        "She takes your hand and shoves it into her crotch."
                "You can feel that she's warm as a furnace."
                if _return == 1:
                        #other girl is in on it
                        "On the other side, [Previous.name] also reaches down and gets into the action."
                        "You both stroke her pussy for several minutes, until finally she shudders in orgasm."
                        "You slowly pulls your hands free with a sly smile."
                        $ Girl.GLG(Previous,700,6,1)
                        $ Girl.GLG(Previous,1000,6,1)
                        $ Previous.GLG(Girl,1000,2,1)
                else:
                        "You stroke her pussy for several minutes, until finally she shudders in orgasm."
                        "You slowly pulls your hand free with a sly smile."
                if _return == 3:
                    call Date_Bonus(Previous,-3)
                if Girl == RogueX:
                        ch_r "I needed to take a bit of the edge off, [Girl.Petname]."
                elif Girl == KittyX:
                        ch_k "Thanks, [Girl.Petname], I needed that."
                elif Girl == EmmaX:
                        ch_e "Ah, that was lovely, [Girl.Petname]."
                elif Girl == LauraX:
                        ch_l "Oof, that was nice."
                elif Girl == JeanX:
                        ch_j "Ok, that'll do fine."
                elif Girl == StormX:
                        ch_s "Thank you, that was lovely, [Girl.Petname]."
                elif Girl == JubesX:
                        ch_v "I needed that, [Girl.Petname]. . ."
                if _return == 1:
                        #if the other girl joined in. . .
                        if Girl == RogueX:
                                ch_r "Thanks to you too, [Previous.name]."
                        elif Girl == KittyX:
                                ch_k "You too, [Previous.name]."
                        elif Girl == EmmaX:
                                ch_e "And thank you as well, [Previous.name]."
                        elif Girl == LauraX:
                                ch_l "You too, [Previous.name]."
                        elif Girl == JeanX:
                                ch_j "love the initiative there [Previous.name]."
                        elif Girl == StormX:
                                ch_s "And you as well, [Previous.Petname]."
                        elif Girl == JubesX:
                                ch_v "And thanks for the assist, [Previous.Petname]."
                        $ Girl.Les += 1
                        $ Previous.Les += 1
                $ Girl.Addict -= 5
                $ Girl.change_stat("love", 90, 3)
                $ Girl.change_stat("inhibition", 30, 5)
                $ Girl.change_stat("inhibition", 90, 2)
                $ Girl.FondleP += 1
                $ Girl.Org += 1
                $ Girl.recent_history.append("fondle_pussy")
                $ Girl.recent_history.append("dinnersex")
                $ Girl.daily_history.append("fondle_pussy")
    elif OptionsDS[0] == "footjob":
        "Halfway through the meal, [Girl.name] gets a sly look on her face, then shifts a bit lower in her seat."
        "You suddenly feel her foot in your lap, gently caressing your cock."
        call Date_Sex_Break(Girl,Previous)
        if _return == 4: #you refused
                $ Girl.change_face("sadside", 2)
                "You shift uncomfortably and push her foot away."
                $ Girl.change_stat("love", 90, -5)
                $ Girl.change_stat("inhibition", 80, -3)
                call Date_Bonus(Girl,-1)
        else:
                $ Player.change_stat("Focus", 60, 10)
                if _return == 1: #other girl is fine
                        "[Previous.name] decides to join in the fun and adds her foot to the mix."
                        $ Player.change_stat("Focus", 60, 5)
                        $ Girl.GLG(Previous,1000,2,1)
                        $ Previous.GLG(Girl,1000,1,1)
                if _return == 3:
                        call Date_Bonus(Previous,-3)
                "After several minutes of this, she pulls back."
                if Girl == RogueX:
                        ch_r "Just a little downpayment on later, [Girl.Petname]."
                elif Girl == KittyX:
                        ch_k "Just a taste of things to come, [Girl.Petname]."
                elif Girl == EmmaX:
                        ch_e "Patience. . . [Girl.Petname]."
                elif Girl == LauraX:
                        ch_l "I've got plans for tonight, [Girl.Petname]."
                elif Girl == JeanX:
                        ch_j "Hold on to those for me?"
                elif Girl == StormX:
                        ch_s "I felt. . . constrained, [Girl.Petname]."
                elif Girl == JubesX:
                        ch_v "I hope you got the message, [Girl.Petname]. . ."
                $ Girl.change_stat("inhibition", 80, 3)
                $ Girl.recent_history.append("dinnersex")

    $ Girl.Blush = 0
    return

label Date_Movies:  #rkeljsv
    #This picks and watches a movie
    $ bg_current = "bg_movies"
    $ Player.recent_history.append("movie")
    $ Player.daily_history.append("movie")
    $ Girls = Party[:]
    while Girls:
        $ Girls[0].location = "bg_movies"
        $ Girls.remove(Girls[0])

    call set_the_scene

    menu:
        "What would you like to see?"
        "A romantic comedy.":
            $ line = "romcom"
            $ Player.recent_history.append("romcom")
        "An action movie.":
            $ line = "action"
            $ Player.recent_history.append("action")
        "A horror movie.":
            $ line = "horror"
            $ Player.recent_history.append("horror")
        "An acclaimed drama.":
            $ line = "drama"
            $ Player.recent_history.append("drama")
        "Let [RogueX.name] pick." if RogueX in Party:
            $ line = "pick"
            $ chosen_Girl= RogueX
        "Let [KittyX.name] pick." if KittyX in Party:
            $ line = "pick"
            $ chosen_Girl= KittyX
        "Let [EmmaX.name] pick." if EmmaX in Party:
            $ line = "pick"
            $ chosen_Girl= EmmaX
        "Let [LauraX.name] pick." if LauraX in Party:
            $ line = "pick"
            $ chosen_Girl= LauraX
        "Let [JeanX.name] pick." if JeanX in Party:
            $ line = "pick"
            $ chosen_Girl= JeanX
        "Let [StormX.name] pick." if StormX in Party:
            $ line = "pick"
            $ chosen_Girl= StormX
        "Let [JubesX.name] pick." if JubesX in Party:
            $ line = "pick"
            $ chosen_Girl= JubesX


    if line == "pick":
            #if you let one of the girls pick the movie
            $ temp.change_face("smile")
            if chosen_Girl== RogueX:
                    $ RogueX.change_stat("love", 80, 4)
                    $ RogueX.change_stat("obedience", 50, -2)
                    $ RogueX.change_stat("inhibition", 50, 2)
                    ch_r "How sweet, [RogueX.Petname]. Let's see the romantic comedy."
                    $ line = "romcom"
            elif chosen_Girl== KittyX:
                    $ KittyX.change_stat("love", 80, 4)
                    $ KittyX.change_stat("obedience", 50, -2)
                    $ KittyX.change_stat("inhibition", 50, 2)
                    ch_k "Aw, [KittyX.Petname]. Let's see the drama."
                    $ line = "drama"
            elif chosen_Girl== EmmaX:
                    $ EmmaX.change_stat("love", 80, 5)
                    $ EmmaX.change_stat("obedience", 50, -3)
                    $ EmmaX.change_stat("inhibition", 50, 3)
                    ch_e "Oh, lovely. Let's see the horror film."
                    $ line = "horror"
            elif chosen_Girl== LauraX:
                    $ LauraX.change_stat("love", 90, 5)
                    $ LauraX.change_stat("obedience", 50, 2)
                    $ LauraX.change_stat("inhibition", 50, 2)
                    ch_l "Cool. Let's go with some action."
                    $ line = "action"
            elif chosen_Girl== JeanX:
                    $ JeanX.change_stat("love", 60, 2)
                    $ JeanX.change_stat("love", 90, 3)
                    $ JeanX.change_stat("obedience", 50, 2)
                    $ JeanX.change_stat("inhibition", 70, 2)
                    ch_j "I guess that romcom looks fun."
                    $ line = "romcom"
            elif chosen_Girl== StormX:
                    $ StormX.change_stat("love", 80, 5)
                    $ StormX.change_stat("inhibition", 50, 3)
                    $ StormX.change_stat("inhibition", 80, 1)
                    ch_s "Then, let us watch the drama. I have heard it is excellent."
                    $ line = "drama"
            elif chosen_Girl== JubesX:
                    $ JubesX.change_stat("love", 80, 4)
                    $ JubesX.change_stat("obedience", 50, 2)
                    $ JubesX.change_stat("inhibition", 50, 2)
                    ch_v "Oh, definitely \"action.\""
                    $ line = "drama"
            $ Player.recent_history.append(line)
            call Date_Bonus(temp,20)

    if line == "romcom":
            if RogueX in Party and chosen_Girl!= RogueX:
                    $ RogueX.change_face("smile", Eyes="surprised")
                    $ RogueX.change_stat("love", 50, 2)
                    $ RogueX.change_stat("love", 95, 4)
                    $ RogueX.change_stat("inhibition", 50, 2)
                    ch_r "Oooh, I love a good rom-com, [RogueX.Petname]. This should be great!"
                    call Date_Bonus(RogueX,15)
            if KittyX in Party and chosen_Girl!= KittyX:
                    $ KittyX.change_face("smile", Eyes="surprised")
                    $ KittyX.change_stat("love", 50, 2)
                    $ KittyX.change_stat("love", 95, 3)
                    ch_k "Aw, how cuuuute!"
                    call Date_Bonus(KittyX,5)
            if EmmaX in Party and chosen_Girl!= EmmaX:
                    $ EmmaX.change_face("confused", Mouth="sad")
                    $ EmmaX.change_stat("love", 70, 2)
                    $ EmmaX.change_stat("obedience", 50, 5)
                    $ EmmaX.change_stat("inhibition", 70, -3)
                    ch_e "How. . . pedestrian."
                    call Date_Bonus(EmmaX,-5)
            if LauraX in Party and chosen_Girl!= LauraX:
                    $ LauraX.change_face("smile", 2)
                    $ LauraX.change_stat("love", 80, 3)
                    $ LauraX.change_stat("obedience", 50, 3)
                    $ LauraX.change_stat("inhibition", 60, 3)
                    ch_l "This one looks. . . ok."
                    call Date_Bonus(LauraX,10)
            if JeanX in Party and chosen_Girl!= JeanX:
                    $ JeanX.change_face("smile")
                    $ JeanX.change_stat("love", 80, 3)
                    $ JeanX.change_stat("obedience", 50, 3)
                    $ JeanX.change_stat("inhibition", 60, 3)
                    ch_j "Oh, excellent tastes."
                    call Date_Bonus(JeanX,10)
            if StormX in Party and chosen_Girl!= StormX:
                    $ StormX.change_face("smile")
                    $ StormX.change_stat("love", 70, 2)
                    $ StormX.change_stat("obedience", 50, 1)
                    ch_s "A true romantic at heart."
                    call Date_Bonus(StormX,10)
            if JubesX in Party and chosen_Girl!= JubesX:
                    $ JubesX.change_face("smile")
                    $ JubesX.change_stat("love", 50, 2)
                    $ JubesX.change_stat("love", 95, 3)
                    ch_v "Yeah, ok."
                    call Date_Bonus(JubesX,5)
    elif line == "action":
            if RogueX in Party and chosen_Girl!= RogueX:
                    $ RogueX.change_face("sexy")
                    ch_r "Hmm, you know I'm always up for some action."
                    $ RogueX.change_stat("love", 95, 3)
                    call Date_Bonus(RogueX,5)
            if KittyX in Party and chosen_Girl!= KittyX:
                    $ KittyX.change_face("sexy")
                    $ KittyX.change_stat("love", 95, 4)
                    $ KittyX.change_stat("inhibition", 50, 2)
                    ch_k "Action movies are kind of fun."
                    call Date_Bonus(KittyX,5)
            if EmmaX in Party and chosen_Girl!= EmmaX:
                    $ EmmaX.change_face("sadside", Brows="angry")
                    $ EmmaX.change_stat("love", 70, -2)
                    $ EmmaX.change_stat("obedience", 50, 5)
                    ch_e "I suppose it will at least keep me occupied."
                    # call Date_Bonus(EmmaX,0)
            if LauraX in Party and chosen_Girl!= LauraX:
                    $ LauraX.change_face("smile")
                    $ LauraX.change_stat("love", 70, 5)
                    $ LauraX.change_stat("obedience", 50, 5)
                    ch_l "This one sounds exciting!"
                    call Date_Bonus(LauraX,10)
            if JeanX in Party and chosen_Girl!= JeanX:
                    $ JeanX.change_face("smile")
                    $ JeanX.change_stat("obedience", 50, 3)
                    $ JeanX.change_stat("inhibition", 60, 2)
                    ch_j "I guess that's fine."
                    call Date_Bonus(JeanX,5)
            if StormX in Party and chosen_Girl!= StormX:
                    $ StormX.change_face("smile")
                    $ StormX.change_stat("love", 70, 2)
                    $ StormX.change_stat("obedience", 50, 1)
                    ch_s "That does get the pulse racing."
                    call Date_Bonus(StormX,5)
            if JubesX in Party and chosen_Girl!= JubesX:
                    $ JubesX.change_face("smile")
                    $ JubesX.change_stat("love", 95, 5)
                    $ JubesX.change_stat("obedience", 50, 2)
                    $ JubesX.change_stat("inhibition", 50, 2)
                    ch_v "I love to see some action!"
                    call Date_Bonus(JubesX,15)
    elif line == "horror":
            if RogueX in Party and chosen_Girl!= RogueX:
                    $ RogueX.change_face("sad", Eyes="surprised")
                    $ RogueX.change_stat("love", 90, -3)
                    $ RogueX.change_stat("obedience", 50, 3)
                    $ RogueX.change_stat("obedience", 80, 2)
                    ch_r "I'm not really into the spooky stuff, [RogueX.Petname]."
                    # call Date_Bonus(RogueX,0)
            if KittyX in Party and chosen_Girl!= KittyX:
                    $ KittyX.change_face("sad", Eyes="surprised")
                    $ KittyX.change_stat("love", 90, -5)
                    $ KittyX.change_stat("obedience", 50, 4)
                    $ KittyX.change_stat("obedience", 80, 2)
                    ch_k "It won't be {i}too{/i} scary, right?"
                    call Date_Bonus(KittyX,-5)
            if EmmaX in Party and chosen_Girl!= EmmaX:
                    $ EmmaX.change_face("sly")
                    $ EmmaX.change_stat("love", 70, 3)
                    $ EmmaX.change_stat("obedience", 50, 3)
                    $ EmmaX.change_stat("inhibition", 70, 2)
                    $ EmmaX.change_stat("lust", 60, 5)
                    ch_e "I do love to get a good chill up the spine."
                    call Date_Bonus(EmmaX,15)
            if LauraX in Party and chosen_Girl!= LauraX:
                    $ LauraX.change_face("normal")
                    $ LauraX.change_stat("obedience", 50, 3)
                    ch_l "I'm sure it'll be terrifying."
                    #call Date_Bonus(LauraX,0)
            if JeanX in Party and chosen_Girl!= JeanX:
                    $ JeanX.change_face("sadside")
                    $ JeanX.change_stat("love", 70, -1)
                    $ JeanX.change_stat("obedience", 70, 3)
                    $ JeanX.change_stat("inhibition", 60, 1)
                    ch_j "Kinda boring."
                    #call Date_Bonus(JeanX,0)
            if StormX in Party and chosen_Girl!= StormX:
                    $ StormX.change_face("sad")
                    $ StormX.change_stat("love", 70, 1)
                    $ StormX.change_stat("obedience", 50, 1)
                    $ StormX.change_stat("inhibition", 50, 1)
                    ch_s "I. . . do not prefer terror."
                    #call Date_Bonus(StormX,0)
            if JubesX in Party and chosen_Girl!= JubesX:
                    $ JubesX.change_face("sad")
                    $ JubesX.change_stat("love", 90, -5)
                    $ JubesX.change_stat("obedience", 50, 2)
                    $ JubesX.change_stat("obedience", 80, 2)
                    ch_v "I get enough of this back home. . ."
                    call Date_Bonus(JubesX,-5)
    elif line == "drama":
            if RogueX in Party and chosen_Girl!= RogueX:
                    $ RogueX.change_face("bemused")
                    $ RogueX.change_stat("love", 95, 1)
                    $ RogueX.change_stat("obedience", 50, 3)
                    ch_r "Hmmm, I have heard some good things about this one, could be interesting."
                    call Date_Bonus(RogueX,5)
            if KittyX in Party and chosen_Girl!= KittyX:
                    $ KittyX.change_face("bemused")
                    $ KittyX.change_stat("love", 95, 3)
                    $ KittyX.change_stat("obedience", 50, 2)
                    ch_k "I heard this was a good one!"
                    call Date_Bonus(KittyX,15)
            if EmmaX in Party and chosen_Girl!= EmmaX:
                    $ EmmaX.change_face("normal")
                    $ EmmaX.change_stat("love", 70, 2)
                    $ EmmaX.change_stat("obedience", 50, 3)
                    ch_e "Ah, this does sound like an interesting one."
                    call Date_Bonus(EmmaX,5)
            if LauraX in Party and chosen_Girl!= LauraX:
                    $ LauraX.change_face("normal")
                    $ LauraX.change_stat("obedience", 50, 3)
                    ch_l "Meh."
                    #call Date_Bonus(LauraX,0)
            if JeanX in Party and chosen_Girl!= JeanX:
                    $ JeanX.change_face("sad")
                    $ JeanX.change_stat("love", 60, -3)
                    $ JeanX.change_stat("love", 80, -2)
                    $ JeanX.change_stat("obedience", 50, 2)
                    $ JeanX.change_stat("obedience", 80, 2)
                    $ JeanX.change_stat("inhibition", 60, 3)
                    ch_j "Booooring."
                    call Date_Bonus(JeanX,10)
            if StormX in Party and chosen_Girl!= StormX:
                    $ StormX.change_face("smile")
                    $ StormX.change_stat("love", 50, 3)
                    $ StormX.change_stat("love", 80, 3)
                    $ StormX.change_stat("obedience", 50, 2)
                    $ StormX.change_stat("obedience", 80, 1)
                    $ StormX.change_stat("inhibition", 50, 3)
                    ch_s "Ah, an wonderful choice. I have heard it is excellent."
                    call Date_Bonus(StormX,15)
            if JubesX in Party and chosen_Girl!= JubesX:
                    $ JubesX.change_face("bemused")
                    $ JubesX.change_stat("love", 95, 1)
                    $ JubesX.change_stat("obedience", 50, 2)
                    ch_v "Yeah, ok. . ."
                    call Date_Bonus(JubesX,5)
    $ chosen_Girl= 0

    call Date_Paying("movie")

    if not Party:
            #if you're ditched,
            "You decide to watch the movie anyway, but it was pretty boring."
            "Afterwards you just head back to your room."
            jump Date_Over

    $ Player.recent_history.append("movie")
    #The movie plays.
    if len(Party) >= 2:
        "You take your seat in between the other two."
    else:
        "You take your seats in the theater."

    if "romcom" in Player.recent_history:
        $ line = renpy.random.choice(["You watch the movie, which is about an adorkable girl who can't choose between two hunky guys. She picks the other one.",
                    "You watch the movie, which is about a girl who is mercilessly stalked by some weird guy, until she eventually decides she loves him. They live hapily ever after.",
                    "In this movie, the lead goes to all her friend's weddings, but can't get it together herself. She dies alone. Just kidding, she gets married at the end.",
                    "You watch the movie, in which a bunch of college girls go on a wild adventure and have lots of random sex.",
                    "This movie is about a girl who's convinced to live in a sex dungeon, and really seems to enjoy it.",
                    "This movie is about a girl who works for a fashion house and is bullied by her boss, until they become friends."])
    elif "action" in Player.recent_history:
        $ line = renpy.random.choice(["You watch the movie, which is about an ex marine fighting aliens.",
                    "You watch the movie, which is about a girl who is mercilessly stalked by some weird guy, until she eventually decides she loves him. They live hapily ever after. There are also a lot of explosions.",
                    "In this movie, giant robots are fighting animal mash-ups, with the fate of the world in the balance.",
                    "You watch the movie, in which a team of non-mutant superhumans are apparently fighting some sort of silvery robots in Eastern Europe.",
                    "This movie is about a superhuman powerhouse that nearly wrecks a town, and yet is not arrested for it by the humans. Must be the hammer.",
                    "This movie is about 90 minutes of constant explosions and lensflares."])
    elif "horror" in Player.recent_history:
        $ line = renpy.random.choice(["You watch the movie, which is about an adorkable girl who can't choose between two hunky guys. She picks the other one. The guys are a fishman and a skeleton.",
                    "You watch the movie, which is about a girl who is mercilessly stalked by some weird guy, until she eventually gives in and marries him. Her life is an endless hell.",
                    "In this movie, a group of teens are trapped in a wilderness cabin. They have a lot of random sex as some shadowy monster kills them one by one.",
                    "In this movie, a group of teens are trapped in an abandoned motel. They have a lot of random sex as some shadowy monster kills them one by one.",
                    "This movie is about a girl who's convinced to live in a sex dungeon, and she's eventually murdered.",
                    "In this movie, a group of teens are trapped in a spaceship. They have a lot of random sex as some shadowy monster kills them one by one."])
    elif "drama" in Player.recent_history:
        $ line = renpy.random.choice(["You watch the movie, which is about a mature woman who can't choose between two eligible widowers. She picks the other one.",
                    "You watch the movie, which is a documentary about a girl who is mercilessly stalked by some weird guy, until she eventually decides to get a restraining order.",
                    "In this movie, which is a biopic about a great historical leader.",
                    "You watch the movie, in which a disabled person struggles with his various disabilities, and eventually overcomes them, and/or dies.",
                    "This movie is about a lot of yelling and crying as some very serious issues are explored by an ensemble cast."])

    "[line]" #You watch the movie. . .

    call Movie_Sex

    $ Round -= 60 if Round > 70 else (Round-10) #reduces Round to at minimum 10

    if Round < 20:
            "After you leave the theater, you notice it's getting dark, and head back to the dorms. . ."
            jump Date_End

    if not Party:
            "After the movie, you decide to head back to your room."
            jump Date_Over

    "You seem to have some time left, where would you like to go next?"
    jump Date_Location #picks next stop. . .

label Movie_Sex(Girl=0,Previous=0,GirlBonus=0, OptionsDS=[],Girls=[]):#rkeljsv
    # Called by Date_Sex
    $ Girls = Party[:]
    if 0 in Girls:
        $ Girls.remove(0)
    while Girls:
            if Approvalcheck(Girls[0], 1000):  #checks if Girls[0] is in
                    $ OptionsDS.append(Girls[0])
                    if Party[0] == Girls[0] and Date_Bonus[0] > 10:
                            $ OptionsDS.append(Girls[0])
                    elif Girls[0] in Party and Date_Bonus[1] > 10:
                            $ OptionsDS.append(Girls[0])
                    if "horror" in Player.recent_history:
                            $ OptionsDS.append(Girls[0])
                    elif "drama" in Player.recent_history:
                            $ OptionsDS.append(Girls[0])
                    elif Girls[0] == LauraX and "action" in Player.recent_history:
                            $ OptionsDS.append(Girls[0])
            $ Girls.remove(Girls[0])

    if len(OptionsDS) == 0:
            #if nobody is in, return
            return

    $ renpy.random.shuffle(OptionsDS)

    $ Girl = OptionsDS[0]
    if len(Party) >= 2:
            if Girl == Party[0]:
                    $ Previous = Party[1]
            else:
                    $ Previous = Party[0]

    if Girl == Previous:
        "Tell Oni that on a date, a girl and previous were the same, [Girl.Tag], MS"

    $ OptionsDS = ["nothing"]

    if Party[0] == Girl:
        $ GirlBonus = Date_Bonus[0] + Date_Cost[0]
    else:
        $ GirlBonus = Date_Bonus[1] + Date_Cost[1]

    if Approvalcheck(Girl, 500, Bonus=(10*GirlBonus)):
        $ Girl.change_face("kiss", 1)
        if "romcom" in Player.recent_history:
                "Halfway through the movie, inspired by the action on screen, [Girl.name] turns to you and starts to make out with you."
        elif "action" in Player.recent_history:
                "Halfway through the movie, adrenaline pumping from the action on screen, [Girl.name] turns to you and starts to make out with you."
        elif "horror" in Player.recent_history:
                if Girl == EmmaX:
                        "Halfway through the movie, slightly bored by it, [Girl.name] shrugs and starts to make out with you."
                elif Girl == LauraX:
                        "Halfway through the movie, bored by the \"tension\" on screen, [Girl.name] turns to you and starts to make out with you."
                else:
                        "Halfway through the movie, freaked out by the tension on screen, [Girl.name] huddles in your arms, and then starts to make out with you."
        elif "drama" in Player.recent_history:
                if Girl in (RogueX,EmmaX):
                        "Halfway through the movie, profoundly bored by the movie, [Girl.name] turns to you with a shrug and starts to make out with you."
                else:
                        "Halfway through the movie, [Girl.name] turns to you with a shrug and starts to make out with you."
        $ Girl.recent_history.append("kissing")
        $ Girl.recent_history.append("moviesex")
        $ Girl.daily_history.append("kissing")
        call Date_Sex_Break(Girl,Previous)
        if _return == 4:
                #the other girl stops you
                "You settle back into your seats and watch the rest of the film."
                return
        elif Previous and _return == 1:
                #the other girl joins in. . .
                "[Previous.name] also leans in and begins kissing the both of you."
        elif Previous and  _return == 3:
                #the other girl is mad. . .
                "You get back to it, [Previous.name] settles back into her seat with a glare."

        if Girl.Anal and Approvalcheck(Girl, 2000, Bonus=(10*GirlBonus)) and Girl.PantsNum() <= 5:
                $ OptionsDS.append("anal")
        if Girl.Sex and Approvalcheck(Girl, 2000, Bonus=(10*GirlBonus)) and Girl.PantsNum() <= 5:
                $ OptionsDS.append("sex")
        if Girl.Blow and Approvalcheck(Girl, 1300, Bonus=(10*GirlBonus)):
                $ OptionsDS.append("blowjob")
                if Girl == JubesX:
                    $ OptionsDS.append("blowjob")
                    $ OptionsDS.append("blowjob")
        if Girl.Hand and Approvalcheck(Girl, 1000, Bonus=(10*GirlBonus)):
                $ OptionsDS.append("handjob")
        if Girl.FondleP and Approvalcheck(Girl, 900, Bonus=(10*GirlBonus)):
                $ OptionsDS.append("pussy")
        elif Approvalcheck(Girl, 1200, Bonus=(5*GirlBonus)) and Girl.Panties:
                $ OptionsDS.append("panties")
        elif Approvalcheck(Girl, 1200, Bonus=(5*GirlBonus)):
                $ OptionsDS.append("flash")

        $ renpy.random.shuffle(OptionsDS)


        if OptionsDS[0] == "anal":
                    $ Girl.change_face("sexy", 1)
                    if Girl.Panties:
                        "As you make out, [Girl.name] reaches down and undoes your fly. She pulls her panties aside and shifts into your lap."
                    else:
                        "As you make out, [Girl.name] reaches down and undoes your fly. She hikes her skirt up a bit and shifts into your lap."
                    call Date_Sex_Break(Girl,Previous)
                    if _return == 3:
                            #the other girl stormed out. . .
                            call Sex_Basic_Dialog(Girl,"partner") #"Aw, that's a bummer. Anyway. . ."
                    "She gingerly squeezes your cock into her ass and begins to grind up and down, quietly enough that the other patrons don't seem to notice."
                    if _return == 1:
                            #the other girl joins you. . .
                            "[Previous.name] also leans over and toys with [Girl.name]'s pussy."
                            $ Girl.GLG(Previous,700,3,1)
                            $ Girl.GLG(Previous,1000,3,1)
                            $ Previous.GLG(Girl,1000,2,1)
                    if Girl.CreamA:
                            if Girl.Panties:
                                "After several minutes of this, you can't take it anymore and come inside her."
                                "She pulls her panties back up and returns to her seat."
                            else:
                                "After several minutes of this, you can't take it anymore and come inside her."
                                "She wipes off as best she can and shifts back into her seat."
                            $ Girl.CreamA += 1
                            $ Girl.recent_history.append("creampie anal")
                            $ Girl.daily_history.append("creampie anal")
                    else:
                            "After several minutes of this, she pulls out and shifts back into her seat, finishing you off with her hand."
                            if Girl.Swallow:
                                if 0 < _return < 3: #if 1 or 2
                                    "You cum into the popcorn bucket, which she and [Previous.name] then finish off together."
                                else:
                                    "You cum into the popcorn bucket, which she then finishes off."
                                $ Girl.Addict -= 20
                                $ Girl.Swallow += 1
                                $ Girl.Spunk.append("mouth")
                                $ Girl.recent_history.append("swallowed")
                                $ Girl.daily_history.append("swallowed")
                            else:
                                if Girl == KittyX:
                                    "You cum into the popcorn bucket, which she phases into the floor."
                                else:
                                    "You cum into the popcorn bucket, which she sets in the seat next to her."
                    if Girl == RogueX:
                            ch_r "This makes for a better ride than a movie."
                    elif Girl == KittyX:
                            ch_k "Talk about a \"4D\" movie."
                    elif Girl == EmmaX:
                            ch_e "Well, that was exciting."
                    elif Girl == LauraX:
                            ch_l "Hmm, I'm stuffed."
                    elif Girl == JeanX:
                            ch_j "Great job, [Girl.Petname]."
                    elif Girl == StormX:
                            ch_s "That was quite fulfilling. . ."
                    elif Girl == JubesX:
                            ch_v "A movie and a free fill-up. . ."
                    $ Girl.change_stat("inhibition", 50, 4)
                    $ Girl.change_stat("inhibition", 90, 3)
                    $ Girl.SeenPeen += 1
                    $ Girl.Anal += 1
                    $ Player.Semen -= 1
                    $ Girl.recent_history.append("anal")
                    $ Girl.daily_history.append("anal")
        elif OptionsDS[0] == "sex":
                    $ Girl.change_face("sexy", 1)
                    if Girl.Panties:
                        "As you make out, [Girl.name] reaches down and undoes your fly. She pulls her panties aside and shifts into your lap."
                    else:
                        "As you make out, [Girl.name] reaches down and undoes your fly. She hikes her skirt up a bit and shifts into your lap."
                    call Date_Sex_Break(Girl,Previous)
                    if _return == 3:
                            #the other girl stormed out. . .
                            call Sex_Basic_Dialog(Girl,"partner") #"Aw, that's a bummer. Anyway. . ."
                    "Seconds later, she's slowly rocking on your cock, quietly enough that the other patrons don't seem to notice."
                    if _return == 1:
                            #the other girl joins you. . .
                            "[Previous.name] also leans over and toys with [Girl.name]'s pussy."
                            $ Girl.GLG(Previous,700,3,1)
                            $ Girl.GLG(Previous,1000,3,1)
                            $ Previous.GLG(Girl,1000,2,1)
                    if Girl.CreamP:
                        if Girl.Panties:
                            "After several minutes of this, you can't take it anymore and come inside her."
                            "She pulls her panties up over her dripping slit and returns to her seat."
                        else:
                            "After several minutes of this, you can't take it anymore and come inside her."
                            "She wipes up as best she can and returns to her seat."
                        $ Girl.CreamP += 1
                        $ Girl.recent_history.append("creampie sex")
                        $ Girl.daily_history.append("creampie sex")
                    else:
                        "After several minutes of this, she pulls out and shifts back into her seat, finishing you off with her hand."
                        if Girl.Swallow:
                                if 0 < _return < 3: #if 1 or 2
                                    "You cum into the popcorn bucket, which she and [Previous.name] then finish off together."
                                else:
                                    "You cum into the popcorn bucket, which she then finishes off."
                                $ Girl.Spunk.append("mouth")
                                $ Girl.Addict -= 20
                                $ Girl.Swallow += 1
                                $ Girl.recent_history.append("swallowed")
                                $ Girl.daily_history.append("swallowed")
                        else:
                            if Girl == KittyX:
                                "You cum into the popcorn bucket, which she phases into the floor."
                            else:
                                "You cum into the popcorn bucket, which she sets in the seat next to her."
                    if Girl == RogueX:
                            ch_r "This makes for a better ride than a movie."
                    elif Girl == KittyX:
                            ch_k "Talk about a \"4D\" movie."
                    elif Girl == EmmaX:
                            ch_e "Well, that was exciting."
                    elif Girl == LauraX:
                            ch_l "Hmm, I'm stuffed."
                    elif Girl == JeanX:
                            ch_j "Great job, [Girl.Petname]."
                    elif Girl == StormX:
                            ch_s "I do prefer this sort of drama. . ."
                    elif Girl == JubesX:
                            ch_v "A movie and a free fill-up. . ."
                    $ Girl.change_stat("inhibition", 50, 4)
                    $ Girl.change_stat("inhibition", 90, 3)
                    $ Girl.SeenPeen += 1
                    $ Girl.Sex += 1
                    $ Player.Semen -= 1
                    $ Girl.recent_history.append("sex")
                    $ Girl.daily_history.append("sex")
        elif OptionsDS[0] == "blowjob":
                    $ Girl.change_face("sucking", 1)
                    "As you make out, [Girl.name] reaches down and undoes your fly. She then bends down and wraps her lips around it."
                    call Date_Sex_Break(Girl,Previous)
                    if _return == 3:
                            #the other girl stormed out. . .
                            call Sex_Basic_Dialog(Girl,"partner") #"Aw, that's a bummer. Anyway. . ."
                    if _return == 1:
                            #the other girl joins you. . .
                            "[Previous.name] also leans over joins [Girl.name] at licking your cock."
                            "They take turns sucking on it contentedly for several minutes before you finally cum."
                            $ Girl.GLG(Previous,1000,2,1)
                            $ Previous.GLG(Girl,1000,2,1)
                    else:
                            "She sucks on it contentedly for several minutes before you finally cum."
                    $ Girl.Spunk.append("mouth")
                    if Girl.Swallow:
                            "[Girl.name] wipes her mouth as she shifts back into her seat and washes it down with some soda."
                            $ Girl.change_face("sexy")
                            if Girl == RogueX:
                                    ch_r "Mmmm, refreshing. . ."
                            elif Girl == KittyX:
                                    ch_k "Mmmm, that hit the spot. . ."
                            elif Girl == EmmaX:
                                    ch_e "Mmmm, refreshing. . ."
                            elif Girl == LauraX:
                                    ch_l "Mmmm, that hit the spot. . ."
                            elif Girl == JeanX:
                                    ch_j "Delish, [Girl.Petname]."
                            elif Girl == StormX:
                                    ch_s "You certainly are a delicious treat. . ."
                            elif Girl == JubesX:
                                    ch_v "Now -that's- refreshing. . ."
                            $ Girl.Addict -= 20
                            $ Girl.Swallow += 1
                            $ Girl.recent_history.append("swallowed")
                            $ Girl.daily_history.append("swallowed")
                    else:
                        if Girl == KittyX:
                            "You cum into the popcorn bucket, which she phases into the floor."
                        else:
                            "You cum into the popcorn bucket, which she sets in the seat next to her."
                        if Girl == RogueX:
                                ch_r "I bet the cleaning crew will enjoy that."
                        elif Girl == KittyX:
                                ch_k "That should give archeolgists a surprise."
                        elif Girl == EmmaX:
                                ch_e "That is a bit of a mess for the help."
                        elif Girl == LauraX:
                                ch_l "Kinda left a mess there."
                        elif Girl == JeanX:
                                ch_j "Heh."
                        elif Girl == StormX:
                                ch_s "We really should not leave such a mess. . ."
                        elif Girl == JubesX:
                                ch_v "Ugh, what a mess. . ."
                    $ Girl.change_stat("inhibition", 40, 3)
                    $ Girl.change_stat("inhibition", 80, 2)
                    $ Girl.SeenPeen += 1
                    $ Girl.Blow += 1
                    $ Player.Semen -= 1
                    $ Girl.recent_history.append("blowjob")
                    $ Girl.daily_history.append("blowjob")
        elif OptionsDS[0] == "handjob":
                    $ Girl.change_face("sexy")
                    "As you make out, [Girl.name] reaches down and pulls out your cock."
                    call Date_Sex_Break(Girl,Previous)
                    if _return == 3:
                            #the other girl stormed out. . .
                            call Sex_Basic_Dialog(Girl,"partner") #"Aw, that's a bummer. Anyway. . ."
                            "She then leans over and begins to stroke your cock."
                    elif _return == 1:
                            #the other girl joins in. . .
                            "She then leans over and begins to stroke your cock."
                            "[Previous.name] leans in and joins her, and they share a smile."
                            $ Girl.GLG(Previous,1000,2,1)
                            $ Previous.GLG(Girl,1000,2,1)
                    else:
                            "She then leans over and begins to stroke it."
                    $ Girl.change_face("surprised")
                    if Girl.FondleP:
                        if _return == 1:
                                #the other girl joins in. . .
                                "You also reach down and begin stroking their pussies."
                        else:
                            if Girl.Legs:
                                    "You also lean over, reach into her [Girl.Legs], and begin to stroke her pussy."
                            elif Girl.Hose:
                                    "You also lean in, reach under her [Girl.Hose], and begin to stroke her pussy."
                            elif Girl.Panties:
                                    "You also lean in, reach under her panties, and begin to stroke her pussy."
                            else:
                                    "You also lean over, notice she isn't wearing anything down there, and begin to stroke her pussy."
                    $ Girl.change_face("sexy", 1, Eyes = "closed")
                    if Girl.FondleP:
                            if _return == 1:
                                "After several minutes of this, [Girl.name] and [Previous.name] shudder in orgasm, which sets you off as well."
                            else:
                                "After several minutes of this, she shudders in orgasm, which sets you off as well."
                            "[Girl.name] catches the jiz in the popcorn bucket."
                    $ Girl.Eyes = "sexy"
                    if Girl.Swallow:
                            if 0 < _return < 3: #if 1 or 2
                                "The girls finish off the remaining popcorn with a grin."
                            else:
                                "She finishes off the remaining popcorn with a grin."
                            $ Girl.Spunk.append("mouth")
                            if Girl == RogueX:
                                    ch_r "Best topping they got here, [Girl.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Best topping they got here, [Girl.Petname]."
                            elif Girl == EmmaX:
                                    ch_e "I do enjoy this new flavor they have, [Girl.Petname]."
                            elif Girl == LauraX:
                                    ch_l "I should order that topping next time."
                            elif Girl == JeanX:
                                    ch_j "Yum."
                            elif Girl == StormX:
                                    ch_s "That certainly was delicious. . ."
                            elif Girl == JubesX:
                                    ch_v "Now -that's- refreshing. . ."
                            $ Girl.Addict -= 20
                            $ Girl.Swallow += 1
                            $ Girl.recent_history.append("swallowed")
                            $ Girl.daily_history.append("swallowed")
                    else:
                            if Girl == KittyX:
                                "You cum into the popcorn bucket, which she phases into the floor."
                            else:
                                "You cum into the popcorn bucket, which she sets in the seat next to her."
                            if Girl == RogueX:
                                    ch_r "I bet the cleaning crew will enjoy that."
                            elif Girl == KittyX:
                                    ch_k "That should give archeolgists a surprise."
                            elif Girl == EmmaX:
                                    ch_e "That is a bit of a mess for the help."
                            elif Girl == LauraX:
                                    ch_l "Kinda left a mess there."
                            elif Girl == JeanX:
                                    ch_j "Heh."
                            elif Girl == StormX:
                                    ch_s "We really should not leave such a mess. . ."
                            elif Girl == JubesX:
                                    ch_v "Ugh, what a mess. . ."
                    $ Girl.change_stat("love", 90, 2)
                    $ Girl.change_stat("inhibition", 40, 3)
                    $ Girl.change_stat("inhibition", 80, 2)
                    $ Girl.FondleP += 1
                    $ Girl.Org += 1
                    $ Girl.Hand += 1
                    $ Player.Semen -= 1
                    $ Girl.recent_history.append("handjob")
                    $ Girl.daily_history.append("handjob")
        elif OptionsDS[0] == "pussy":
                    $ Girl.change_face("sexy")
                    if Girl.Legs:
                            "As you make out, [Girl.name] grabs your hand and shoves it down her [Girl.Legs]."
                    elif Girl.Hose:
                            "As you make out, [Girl.name] grabs your hand and shoves it down her [Girl.Hose]."
                    elif Girl.Panties:
                            "As you make out, [Girl.name] grabs your hand and shoves it down her panties."
                    else:
                            "As you make out, [Girl.name] grabs your hand and shoves it between her legs."
                    call Date_Sex_Break(Girl,Previous)
                    $ Girl.Eyes = "closed"
                    if _return == 3:
                            #the other girl stormed out. . .
                            call Sex_Basic_Dialog(Girl,"partner") #"Aw, that's a bummer. Anyway. . ."
                            "You get back to work."
                    elif _return == 1:
                            #the other girl joins in. . .
                            "[Previous.name] leans in and begins to fondle her breasts as well."
                            $ Girl.GLG(Previous,700,6,1)
                            $ Girl.GLG(Previous,1000,3,1)
                            $ Previous.GLG(Girl,1000,2,1)
                    "After several minutes of this, she shudders in orgasm and leans back with a contented sigh."
                    $ Girl.Eyes = "sexy"
                    if Girl == RogueX:
                            ch_r "Thanks [Girl.Petname]. I needed that. . . distraction."
                    elif Girl == KittyX:
                            ch_k "Hmm, that felt great, [Girl.Petname]."
                    elif Girl == EmmaX:
                            ch_e "Very. . . kind of you, [Girl.Petname]. I needed that."
                    elif Girl == LauraX:
                            ch_l "Hmm, that was great, [Girl.Petname]."
                    elif Girl == JeanX:
                            ch_j "That made the show worth it, [Girl.Petname]."
                    elif Girl == StormX:
                            ch_s "Thank you for your. . . assistance. . ."
                    elif Girl == JubesX:
                            ch_v "Ah. . . that's what I needed. . ."
                    $ Girl.change_stat("love", 90, 2)
                    $ Girl.change_stat("inhibition", 40, 2)
                    $ Girl.change_stat("inhibition", 80, 2)
                    $ Girl.FondleP += 1
                    $ Girl.Org += 1
                    $ Girl.recent_history.append("fondle_pussy")
                    $ Girl.daily_history.append("fondle_pussy")
        elif OptionsDS[0] == "panties":
                    $ Girl.change_face("sexy")
                    "After making out for a few minutes, [Girl.name] gets a sly look on her face and reaches into her pocket."
                    "After a second, she hands you a cloth lump, apparently her panties."
                    $ Girl.daily_history.append("pantyless")
                    $ Girl.change_stat("inhibition", 60, 2)
                    $ Girl.Panties = 0
                    if Girl == RogueX:
                            ch_r "Just a little downpayment on later, [Girl.Petname]."
                    elif Girl == KittyX:
                            ch_k "[Girl.Like]hold on to those for me, uh?"
                    elif Girl == EmmaX:
                            ch_e "Just a hint at later, [Girl.Petname]."
                    elif Girl == LauraX:
                            ch_l "Could you hold onto those for later?"
                    elif Girl == JeanX:
                            ch_j "Hold onto those for me, [Girl.Petname]."
                    elif Girl == StormX:
                            ch_s "I felt a bit constrained. . ."
                    elif Girl == JubesX:
                            ch_v "You can. . . uh, hold on to those. . ."
        elif OptionsDS[0] == "flash":
                    $ Girl.change_face("sexy")
                    "After making out for a few minutes, [Girl.name] gets a sly look on her face, then shifts a bit lower in her seat."
                    if Girl.PantsNum() > 6:
                        "Looking down, you notice she's pulled down her pants enough that you can see her bare pussy, lit by the movie screen."
                    elif Girl.PantsNum() == 6:
                        "Looking down, you notice she's pulled down her shorts enough that you can see her bare pussy, lit by the movie screen."
                    else:
                        "Looking down, you notice she's hiked up her skirt enough that you can see her bare pussy, lit by the movie screen."
                    $ Girl.change_stat("inhibition", 60, 2)
                    call expression Girl.Tag + "_First_Bottomless" pass (1)
                    if Girl == RogueX:
                            ch_r "Just a little downpayment on later, [Girl.Petname]."
                    elif Girl == KittyX:
                            ch_k "Just giving you a little taste. . ."
                    elif Girl == EmmaX:
                            ch_e "Just a hint at later, [Girl.Petname]."
                    elif Girl == LauraX:
                            ch_l "Just a heads up. . ."
                    elif Girl == JeanX:
                            ch_j "Eye on the prize, [Girl.Petname]."
                    elif Girl == StormX:
                            ch_s "I thought you might enjoy the view. . ."
                    elif Girl == JubesX:
                            ch_v "More fun than the movie? . ."
    #End Rogue movie sex options
    $ Girl.OutfitChange(Changed=0)
    return

label Date_Sex_Break(Girl=0,Previous=0,Repeat=0):#rkeljsv
        #Girl is the lead girl
        #Previous is the other girl
        # if it returns 0, it continues normally.
        # if it returns 1, the other girl joins in
        # if it returns 2, the other girl watches
        # if it returns 3, the other girl is mad, but it goes on
        # if it returns 4, the other girl is mad, so you cancel out
        # if Repeat, it's the second scene like this of the night.

        if Previous not in all_Girls and len(Party) >= 2:
                    if Girl == Party[0]:
                            $ Previous = Party[1]
                    else:
                            $ Previous = Party[0]

        if Previous not in all_Girls:
                return 0

        if Girl == Previous:
            "Tell Oni that on a date, a girl and previous were the same, [Girl.Tag], DSB"

        if Girl.GirlLikecheck(Previous) >= 700 and Previous.GirlLikecheck(Girl) >= 700:
                #They like each other and will share
                $ Previous.recent_history.append("noticed " + Girl.Tag)
                return 1
        elif Previous == JeanX and not Approvalcheck(Previous, 500, "L"):
                #if it's Jean and she doesn't particularly care. . .
                $ Previous.change_face("sly",1,Eyes="side")
                if bg_current == "bg_restaurant":
                        "[Previous.name] rolls her eyes, but goes back to her meal."
                elif bg_current == "bg_movie":
                        "[Previous.name] rolls her eyes, but continues to watch the movie."
                else:
                        "[Previous.name] rolls her eyes, but doesn't get involved."
                $ Previous.recent_history.append("noticed " + Girl.Tag)
                $ Girl.GLG(Previous,600,5,2)
                $ Previous.GLG(Girl,500,3)
                $ Previous.GLG(Girl,900,3)
                return 2
        elif Approvalcheck(Previous, 1400) and Previous.GirlLikecheck(Girl) >= 500:
                #girl2 likes you, and likes girl1 enough to be chill
                $ Previous.change_face("sly")
                "[Previous.name] winks at you, but doesn't move to get involved."
                $ Previous.recent_history.append("noticed " + Girl.Tag)
                $ Girl.GLG(Previous,600,5,1)
                $ Girl.GLG(Previous,900,3,1)
                $ Previous.GLG(Girl,900,2,1)
                return 2
        elif Approvalcheck(Previous, 1400) and Previous.GirlLikecheck(Girl) < 500:
                pass


        #If they asked you to stop

        #She likes you, but hates the girl
        if Repeat == 2:
                #if it's a good night kiss
                $ Previous.change_face("angry",Eyes="side")
                $ Previous.change_stat("love", 80, -5)
                $ Previous.change_stat("obedience", 80, 5)
                $ Previous.GLG(Girl,800,-3,1)
                $ Previous.AddWord(1,"annoyed") #adds to Recent
                return 3
        elif "annoyed" in Previous.recent_history:
                #if something happened earlier. . .
                $ Previous.change_face("angry")
                $ Previous.change_stat("love", 80, -15)
                $ Previous.change_stat("obedience", 80, 15)
                if Previous == RogueX:
                        ch_r "Get a room you two!"
                elif Previous == KittyX:
                        ch_k "Geeze, right in front of me?!"
                elif Previous == EmmaX:
                        ch_e "Oh do grow up, you two!"
                elif Previous == LauraX:
                        ch_l "Seriously, get a room!"
                elif Previous == JeanX:
                        ch_j "Ok, keep the hormones to a dull roar."
                elif Previous == StormX:
                        ch_s "That is enough, break it up."
                elif Previous == JubesX:
                        ch_v "Cut it out!"
                $ Previous.GLG(Girl,800,-3,1)
                call Girl_Date_Over(Previous)
                # You do it anyway
                return 3
        $ Previous.AddWord(1,"annoyed") #adds to Recent
        if Previous == RogueX:
                ch_r "I know what she's up to, cut it out."
        elif Previous == KittyX:
                ch_k "I see you there, cut it out."
        elif Previous == EmmaX:
                ch_e "Oh, I see what's going on, stop it."
        elif Previous == LauraX:
                ch_l "You think I wouldn't notice? Cut it out."
        elif Previous == JeanX:
                ch_j "I don't have to be a psychic to know what's going on there."
                ch_j "and I -am- one."
                ch_j "Cut it out."
        elif Previous == StormX:
                ch_s "I would hope that we could make it through the meal."
        elif Previous == JubesX:
                ch_v "I can -see- you, you know."
        $ Previous.GLG(Girl,800,-1,1)
        $ Girl.GLG(Previous,800,-3,1)
        menu:
            extend ""
            "Ok, I'll stop.":
                $ Previous.change_stat("love", 80, 10)
                $ Previous.change_stat("obedience", 80, -5)
                $ Previous.change_stat("inhibition", 60, 5)
                $ Girl.GLG(Previous,800,-3,1)
                if "study" not in Player.recent_history:
                        call Date_Bonus(Previous,5)
                # You stop
                return 4
            "I don't think so.":
                $ Previous.change_face("angry")
                $ Previous.change_stat("love", 80, -10)
                $ Previous.change_stat("obedience", 80, 10)
                $ Previous.change_stat("inhibition", 60, -5)
                $ Previous.GLG(Girl,800,-3,1)
                if "study" in Player.recent_history:
                        call Girl_Date_Over(Previous)
                else:
                        call Date_Bonus(Previous,-5)
                # You do it anyway
                return 3
        return 0 #Yes

label Date_Paying(Activity="dinner", Total_Cost=0):  #rkeljsv
    # Activity is which thing you're doing, total cost is the combined meal costs.
    if Activity == "dinner":
                $ Total_Cost = Play_Cost + Date_Cost[0] + Date_Cost[1]
                "The Waitress brings you the check, it comes to $[Total_Cost]."
    else:
        if len(Party) >= 2:
                $ Total_Cost = 30
                "You go to the ticket window, three tickets would be $30."
        else:
                $ Total_Cost = 20
                "You go to the ticket window, two tickets would be $20."

    menu:
        "Who's paying?"
        "I've got it." if Player.Cash >= Total_Cost:
            $ line = "you"

        "[RogueX.name], you pay." if RogueX in Party:
            $ line = RogueX
        "[KittyX.name], you pay." if KittyX in Party:
            $ line = KittyX
        "[EmmaX.name], you pay." if EmmaX in Party:
            $ line = EmmaX
        "[LauraX.name], you pay." if LauraX in Party:
            $ line = LauraX
        "[JeanX.name], you pay." if JeanX in Party:
            $ line = JeanX
        "[StormX.name], you pay." if StormX in Party:
            $ line = StormX
        "[JubesX.name], you pay." if JubesX in Party:
            $ line = JubesX

        "Let's split it." if Player.Cash >= Play_Cost:
            $ line = "split"

        "I really can't afford it. . ." if Player.Cash < Total_Cost:
            $ line = "deadbeat"

    if line == "you":
            #If you offer to cover the meal
            if RogueX in Party:
                    if "deadbeat" in RogueX.History:
                        $ RogueX.History.remove("deadbeat")
                    $ RogueX.change_face("sexy", 1)
                    ch_r "Oh, and such a gentleman."
                    $ RogueX.change_stat("love", 50, 2)
                    $ RogueX.change_stat("love", 80, 2)
                    if Total_Cost >= 15:
                        $ RogueX.change_stat("love", 200, 2)
                    call Date_Bonus(RogueX,Total_Cost)

            if KittyX in Party:
                    if "deadbeat" in KittyX.History:
                        $ KittyX.History.remove("deadbeat")
                    $ KittyX.change_face("sexy", 1)
                    ch_k "[KittyX.Like]that's really nice of you."
                    $ KittyX.change_stat("love", 50, 2)
                    $ KittyX.change_stat("love", 80, 2)
                    if Total_Cost >= 15:
                        $ KittyX.change_stat("love", 200, 2)
                    call Date_Bonus(KittyX,Total_Cost)

            if EmmaX in Party:
                    if "deadbeat" in EmmaX.History:
                        $ EmmaX.History.remove("deadbeat")
                    $ EmmaX.change_face("sly", 1)
                    ch_e "Oh, how very mature of you."
                    $ EmmaX.change_stat("obedience", 50, 3)
                    $ EmmaX.change_stat("love", 50, 2)
                    $ EmmaX.change_stat("love", 80, 2)
                    if Total_Cost >= 15:
                        $ EmmaX.change_stat("love", 200, 2)
                    call Date_Bonus(EmmaX,Total_Cost)

            if LauraX in Party:
                    if "deadbeat" in LauraX.History:
                        $ LauraX.History.remove("deadbeat")
                    $ LauraX.change_face("sly", 1)
                    ch_l "Oh, that's nice of you."
                    $ LauraX.change_stat("obedience", 50, 4)
                    $ LauraX.change_stat("love", 50, 2)
                    $ LauraX.change_stat("love", 80, 1)
                    if Total_Cost >= 15:
                        $ LauraX.change_stat("love", 90, 2)
                        $ LauraX.change_stat("obedience", 50, 1)
                    call Date_Bonus(LauraX,Total_Cost)
            if JeanX in Party:
                    if "deadbeat" in JeanX.History:
                        $ JeanX.History.remove("deadbeat")
                    $ JeanX.change_face("sly", 1)
                    $ JeanX.change_stat("obedience", 50, 4)
                    $ JeanX.change_stat("love", 50, 2)
                    $ JeanX.change_stat("love", 80, 1)
                    if Total_Cost >= 15:
                        $ JeanX.change_stat("love", 90, 2)
                        $ JeanX.change_stat("obedience", 50, 1)
                    call Date_Bonus(JeanX,Total_Cost)

            if StormX in Party:
                    if "deadbeat" in StormX.History:
                        $ StormX.History.remove("deadbeat")
                    $ StormX.change_face("sly", 1)
                    ch_s "How very gentlemanly."
                    $ StormX.change_stat("obedience", 40, 1)
                    $ StormX.change_stat("obedience", 60, 3)
                    $ StormX.change_stat("love", 50, 1)
                    $ StormX.change_stat("love", 80, 2)
                    if Total_Cost >= 15:
                        $ StormX.change_stat("love", 200, 1)
                    call Date_Bonus(StormX,Total_Cost)

            if JubesX in Party:
                    if "deadbeat" in JubesX.History:
                        $ JubesX.History.remove("deadbeat")
                    $ JubesX.change_face("sexy", 1)
                    ch_v "Oh. That's nice of you. . ."
                    $ JubesX.change_stat("love", 50, 1)
                    $ JubesX.change_stat("love", 80, 1)
                    if Total_Cost >= 15:
                        $ JubesX.change_stat("obedience", 50, 1)
                    call Date_Bonus(JubesX,Total_Cost)

            $ Player.Cash -= Total_Cost

    elif line == RogueX:
            #If you ask Rogue to pay
            $ RogueX.change_stat("love", 90, -7)
            if Total_Cost >= 15:
                    $ RogueX.change_stat("love", 200, -6)
                    if Party[0] == RogueX and Play_Cost > Date_Cost[0]:
                        $ RogueX.change_stat("love", 200, -10)
                        $ RogueX.change_stat("obedience", 80, 4)
                    elif RogueX in Party and Play_Cost > Date_Cost[1]:
                        $ RogueX.change_stat("love", 200, -10)
                        $ RogueX.change_stat("obedience", 80, 4)
            if Approvalcheck(RogueX, 1100) and len(Party) < 2:
                    $ RogueX.change_face("sad")
                    ch_r "Well, ok, I guess I can cover it this time."
                    $ RogueX.change_stat("obedience", 30, 3)
                    $ RogueX.change_stat("obedience", 80, 2)
                    if bg_current == "bg_restaurant" and "dinnersex" in RogueX.recent_history:
                            call Date_Bonus(RogueX, -Total_Cost)
            elif Approvalcheck(RogueX, 1300) and len(Party) >= 2:
                    $ RogueX.change_face("sad")
                    ch_r "Hm, ok, I guess I can cover it this time."
                    $ RogueX.change_stat("love", 80, -5)
                    $ RogueX.change_stat("obedience", 30, 4)
                    $ RogueX.change_stat("obedience", 80, 3)
                    if bg_current == "bg_restaurant" and "dinnersex" in RogueX.recent_history:
                            call Date_Bonus(RogueX, -Total_Cost)
            else:
                    $ RogueX.change_face("angry")
                    if len(Party) >= 2:
                        $ RogueX.change_stat("love", 80, -5)
                        ch_r "Oh, bullshit, I am NOT payin for her."
                    else:
                        ch_r "No way, you're coverin your own bills, [RogueX.Petname]."
                    if Player.Cash >= Play_Cost:
                        $ line = "split"
                    else:
                        $ line = "deadbeat"
            #end asked Rogue to pay

    elif line == KittyX:
            #If you ask Kitty to pay
            $ KittyX.change_stat("love", 90, -7)
            if Total_Cost >= 15:
                    $ KittyX.change_stat("love", 200, -6)
                    if Party[0] == KittyX and Play_Cost > Date_Cost[0]:
                        $ KittyX.change_stat("love", 200, -10)
                        $ KittyX.change_stat("obedience", 80, 4)
                    elif KittyX in Party and Play_Cost > Date_Cost[1]:
                        $ KittyX.change_stat("love", 200, -10)
                        $ KittyX.change_stat("obedience", 80, 4)
            if Approvalcheck(KittyX, 1000) and not len(Party) < 2:
                    $ KittyX.change_face("sad")
                    ch_k "Huh? I mean I guess I can. . ."
                    $ KittyX.change_stat("obedience", 30, 3)
                    $ KittyX.change_stat("obedience", 80, 2)
                    if bg_current == "bg_restaurant" and "dinnersex" in KittyX.recent_history:
                            call Date_Bonus(KittyX, -Total_Cost)
            elif Approvalcheck(KittyX, 1300) and len(Party) >= 2:
                    $ KittyX.change_face("sad")
                    ch_k "Huh? I mean I guess I can. . ."
                    $ KittyX.change_stat("love", 80, -5)
                    $ KittyX.change_stat("obedience", 30, 4)
                    $ KittyX.change_stat("obedience", 80, 3)
                    if bg_current == "bg_restaurant" and "dinnersex" in KittyX.recent_history:
                            call Date_Bonus(KittyX, -Total_Cost)
            else:
                    $ KittyX.change_face("angry")
                    if len(Party) >= 2:
                        $ KittyX.change_stat("love", 80, -5)
                        ch_k "You have GOT to be kidding! I'm not paying for her too!"
                    else:
                        ch_k "As if! You're paying for yourself, [KittyX.Petname]."
                    if Player.Cash >= Play_Cost:
                        $ line = "split"
                    else:
                        $ line = "deadbeat"
            #end asked Kitty to pay

    elif line == EmmaX:
            #If you ask Emma to pay
            $ EmmaX.change_stat("love", 90, -3)
            if Total_Cost >= 15:
                    $ EmmaX.change_stat("love", 200, -6)
                    if Party[0] == EmmaX and Play_Cost > Date_Cost[0]:
                        $ EmmaX.change_stat("love", 200, -5)
                        $ EmmaX.change_stat("obedience", 80, 4)
                    elif EmmaX in Party and Play_Cost > Date_Cost[1]:
                        $ EmmaX.change_stat("love", 200, -5)
                        $ EmmaX.change_stat("obedience", 80, 4)
            if Approvalcheck(EmmaX, 900) and len(Party) < 2:
                    $ EmmaX.change_face("sad")
                    ch_e "I suppose you a student, after all. . ."
                    $ EmmaX.change_stat("obedience", 30, 3)
                    $ EmmaX.change_stat("obedience", 80, 2)
                    if bg_current == "bg_restaurant" and "dinnersex" in EmmaX.recent_history:
                            call Date_Bonus(EmmaX, -Play_Cost)
            elif Approvalcheck(EmmaX, 1100) and len(Party) >= 2:
                    $ EmmaX.change_face("sad")
                    ch_e "I suppose you are students, after all. . ."
                    $ EmmaX.change_stat("love", 80, -5)
                    $ EmmaX.change_stat("obedience", 30, 4)
                    $ EmmaX.change_stat("obedience", 80, 3)
                    if bg_current == "bg_restaurant" and "dinnersex" in EmmaX.recent_history:
                            call Date_Bonus(EmmaX, -Play_Cost)
            else:
                    $ EmmaX.change_face("angry")
                    if len(Party) >= 2:
                        $ EmmaX.change_stat("love", 80, -5)
                        ch_e "I'm certainly not paying {i}her{/i} tab."
                    else:
                        ch_e "Student or not, I'm not paying your bills, [EmmaX.Petname]."
                    if Player.Cash >= Play_Cost:
                        $ line = "split"
                    else:
                        $ line = "deadbeat"
            #end asked Emma to pay


    elif line == LauraX:
            #If you ask Laura to pay
            $ LauraX.change_stat("love", 90, -2)
            if Total_Cost >= 15:
                    $ LauraX.change_stat("love", 200, -6)
                    if Party[0] == LauraX and Play_Cost > Date_Cost[0]:
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 80, 4)
                    elif LauraX in Party and Play_Cost > Date_Cost[1]:
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 80, 4)
            if Approvalcheck(LauraX, 900) and len(Party) < 2:
                    $ LauraX.change_face("sad")
                    ch_l "Down on your luck? . ."
                    $ LauraX.change_stat("obedience", 30, 3)
                    $ LauraX.change_stat("obedience", 80, 2)
                    if bg_current == "bg_restaurant" and "dinnersex" in LauraX.recent_history:
                            call Date_Bonus(LauraX, -Play_Cost)
            elif Approvalcheck(LauraX, 1100) and len(Party) >= 2:
                    $ LauraX.change_face("sad")
                    ch_l "Down on your luck? . ."
                    $ LauraX.change_stat("love", 80, -5)
                    $ LauraX.change_stat("obedience", 30, 4)
                    $ LauraX.change_stat("obedience", 80, 3)
                    if bg_current == "bg_restaurant" and "dinnersex" in LauraX.recent_history:
                            call Date_Bonus(LauraX, -Play_Cost)
            else:
                    $ LauraX.change_face("angry")
                    if len(Party) >= 2:
                        $ LauraX.change_stat("love", 80, -5)
                        ch_l "I'm not covering her though."
                    else:
                        ch_l "Too bad, I'm not covering you."
                    if Player.Cash >= Play_Cost:
                        $ line = "split"
                    else:
                        $ line = "deadbeat"
            #end asked Laura to pay
    elif line == JeanX:
            #If you ask Jean to pay
            $ JeanX.change_stat("love", 90, -2)
            if Total_Cost >= 15:
                    $ JeanX.change_stat("love", 200, -6)
                    if Party[0] == JeanX and Play_Cost > Date_Cost[0]:
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_stat("obedience", 80, 4)
                    elif JeanX in Party and Play_Cost > Date_Cost[1]:
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_stat("obedience", 80, 4)
            if Approvalcheck(JeanX, 900) and len(Party) < 2:
                    $ JeanX.change_face("confused",Mouth="smirk")
                    ch_j "Ooh, bad move . ."
                    $ JeanX.change_stat("obedience", 30, 3)
                    $ JeanX.change_stat("obedience", 80, 2)
                    if bg_current == "bg_restaurant" and "dinnersex" in JeanX.recent_history:
                            call Date_Bonus(JeanX, -Play_Cost)
            elif Approvalcheck(JeanX, 1100) and len(Party) >= 2:
                    $ JeanX.change_face("confused",Mouth="smirk")
                    ch_j "Seriously? . ."
                    $ JeanX.change_stat("love", 80, -5)
                    $ JeanX.change_stat("obedience", 30, 4)
                    $ JeanX.change_stat("obedience", 80, 3)
                    if bg_current == "bg_restaurant" and "dinnersex" in JeanX.recent_history:
                            call Date_Bonus(JeanX, -Play_Cost)
            else:
                    $ JeanX.change_face("sadside")
                    if len(Party) >= 2:
                        $ JeanX.change_stat("love", 80, -5)
                    ch_j "Ok, fine. . ."
                    $ line = "deadbeat"
            #end asked Jean to pay

    elif line == StormX:
            #If you ask Storm to pay
            $ StormX.change_stat("love", 90, -3)
            if Total_Cost >= 15:
                    $ StormX.change_stat("love", 200, -6)
                    if Party[0] == StormX and Play_Cost > Date_Cost[0]:
                        $ StormX.change_stat("love", 200, -5)
                        $ StormX.change_stat("obedience", 80, 4)
                    elif StormX in Party and Play_Cost > Date_Cost[1]:
                        $ StormX.change_stat("love", 200, -5)
                        $ StormX.change_stat("obedience", 80, 4)
            if Approvalcheck(StormX, 900) and len(Party) < 2:
                    $ StormX.change_face("sad")
                    ch_s "You are only a child, I suppose. . ."
                    $ StormX.change_stat("obedience", 30, 3)
                    $ StormX.change_stat("obedience", 80, 2)
                    if bg_current == "bg_restaurant" and "dinnersex" in StormX.recent_history:
                            call Date_Bonus(StormX, -Play_Cost)
            elif Approvalcheck(StormX, 1100) and len(Party) >= 2:
                    $ StormX.change_face("sad")
                    ch_s "You are children, I suppose. . ."
                    $ StormX.change_stat("love", 80, -5)
                    $ StormX.change_stat("obedience", 30, 4)
                    $ StormX.change_stat("obedience", 80, 3)
                    if bg_current == "bg_restaurant" and "dinnersex" in StormX.recent_history:
                            call Date_Bonus(StormX, -Play_Cost)
            else:
                    $ StormX.change_face("angry")
                    if len(Party) >= 2:
                        $ StormX.change_stat("love", 80, -4)
                        ch_s "I will not pay you her meal as well."
                    else:
                        ch_s "You may be a student, but I am not covering your costs, [StormX.Petname]."
                    if Player.Cash >= Play_Cost:
                        $ line = "split"
                    else:
                        $ line = "deadbeat"
            #end asked Storm to pay

    elif line == JubesX:
            #If you ask Jubes to pay
            $ JubesX.change_stat("love", 90, -8)
            if Total_Cost >= 15:
                    $ JubesX.change_stat("love", 200, -8)
                    if Party[0] == JubesX and Play_Cost > Date_Cost[0]:
                        $ JubesX.change_stat("love", 200, -10)
                        $ JubesX.change_stat("obedience", 80, 4)
                    elif JubesX in Party and Play_Cost > Date_Cost[1]:
                        $ JubesX.change_stat("love", 200, -10)
                        $ JubesX.change_stat("obedience", 80, 4)
            if Approvalcheck(JubesX, 1000) and not len(Party) < 2:
                    $ JubesX.change_face("sad")
                    ch_v "What? I guess I could. . ."
                    $ JubesX.change_stat("obedience", 30, 3)
                    $ JubesX.change_stat("obedience", 80, 2)
                    if bg_current == "bg_restaurant" and "dinnersex" in JubesX.recent_history:
                            call Date_Bonus(JubesX, -Total_Cost)
            elif Approvalcheck(JubesX, 1300) and len(Party) >= 2:
                    $ JubesX.change_face("sad")
                    ch_v "What?. . . I guess. . ."
                    $ JubesX.change_stat("love", 80, -5)
                    $ JubesX.change_stat("obedience", 30, 4)
                    $ JubesX.change_stat("obedience", 80, 3)
                    if bg_current == "bg_restaurant" and "dinnersex" in JubesX.recent_history:
                            call Date_Bonus(JubesX, -Total_Cost)
            else:
                    $ JubesX.change_face("angry")
                    if len(Party) >= 2:
                        $ JubesX.change_stat("love", 80, -5)
                        ch_v "What?! No I'm not paying for her too!"
                    elif bg_current == "bg_restaurant":
                        ch_v "What? No way, I barely ate anything anyway!"
                    else:
                        ch_v "What? No way am I paying, you invited me!"
                    if Player.Cash >= Play_Cost:
                        $ line = "split"
                    else:
                        $ line = "deadbeat"
            #end asked Jubes to pay

    if line == "split":
            #If you ask to split it evenly
            $ Count = len(Party)
            while Count > 0:
                    $ Count -= 1
                    if Approvalcheck(Party[Count], 600):
                        $ Party[Count].change_face("sad",Mouth="normal")
                        $ Party[Count].change_stat("obedience", 50, 2)
                        if Party[Count] == RogueX:
                                ch_r "Fine, I guess that's fair."
                        elif Party[Count] == KittyX:
                                ch_k "Yeah[KittyX.like]ok."
                        elif Party[Count] == EmmaX:
                                ch_e "I suppose you are still on a student's budget."
                        elif Party[Count] == LauraX:
                                $ LauraX.change_face("sadside")
                                $ LauraX.change_stat("love", 70, 2)
                                $ LauraX.change_stat("obedience", 50, 3)
                                ch_l "Kinda cheap."
                        elif Party[Count] == JeanX:
                                $ JeanX.change_stat("obedience", 70, 3)
                                ch_j "Oh, whatever."
                        elif Party[Count] == StormX:
                                ch_s "You cannot have much money as a student."
                        elif Party[Count] == JubesX:
                                ch_v "Yeah, that's fine."
                    else:
                        if Date_Cost[Count] >=15:
                                # if it cost more than 15, they like you less.
                                $ Party[Count].change_stat("love", 200, -5, alternates = {"Laura": {"check": 200, "value": 3}})
                        else:
                                $ Party[Count].change_stat("love", 200, -3, alternates = {"Laura": {"check": 200, "value": 0}})
                        if Party[Count] == RogueX:
                                $ RogueX.change_face("angry",Eyes="side")
                                ch_r "Tch. Cheapskate."
                        elif Party[Count] == KittyX:
                                $ KittyX.change_face("angry",Eyes="side")
                                ch_k "Jerk."
                        elif Party[Count] == EmmaX:
                                $ EmmaX.change_face("sadside")
                                ch_e "You should learn not to ask a woman out if you can't afford it."
                        elif Party[Count] == LauraX:
                                $ Party[Count].change_stat("love", 70, 2)
                                ch_l "Sure."
                        elif Party[Count] == JeanX:
                                $ JeanX.change_stat("obedience", 70, 3)
                                ch_j "Oh, whatever."
                        elif Party[Count] == StormX:
                                $ StormX.change_face("sadside")
                                ch_s "Do not bite off more than you can chew."
                        elif Party[Count] == JubesX:
                                $ JubesX.change_face("angry",Eyes="side")
                                ch_v "Kinda cheap, but. . ."
                    $ Date_Bonus[Count] -= 10 if Date_Cost[Count] >= 15 else 0
            $ Player.Cash -= Play_Cost

    if line == "deadbeat":
            #If you cannot pay.
            $ Date_Bonus[0] -= Play_Cost
            $ Date_Bonus[1] -= Play_Cost
            $ Date_Bonus[0] -= (Date_Cost[0] - 10) if Date_Cost[0] > 10 else 0
            $ Date_Bonus[1] -= (Date_Cost[1] - 10) if Date_Cost[1] > 10 else 0
            $ Count = len(Party)
            while Count > 0:
                    $ Count -= 1
                    if Total_Cost >=15:
                            $ Party[Count].change_stat("love", 200, -4)
                            if Play_Cost > Date_Cost[Count]:
                                    $ Party[Count].change_stat("love", 200, -10, alternates = {"Emma": {"check": 200, "value": -5}, "Laura": {"check": 200, "value": -5}})
                                    $ Party[Count].change_stat("obedience", 200, 0, alternates = {"Emma": {"check": 200, "value": -2}, "Laura": {"check": 200, "value": -2}})
                    if bg_current == "bg_restaurant" and "dinnersex" in Party[Count].recent_history:
                                    call Date_Bonus(Party[Count], -Total_Cost)
                    $ Party[Count].change_stat("obedience", 50, -2, alternates = {"Laura": {"check": 500, "value": -3}})
                    $ Party[Count].change_face("sad")
                    if Approvalcheck(Party[Count], 800):
                            #pity
                            if Party[Count] == RogueX:
                                    ch_r "Aw, poor baby."
                            elif Party[Count] == KittyX:
                                    ch_k "That's so[KittyX.like]sad."
                            elif Party[Count] == EmmaX:
                                    ch_e "Well that's just irresponsible."
                            elif Party[Count] == LauraX:
                                    ch_l "You gotta cover your own tab, [LauraX.Petname]."
                            elif Party[Count] == JeanX:
                                    ch_j "Pretty pathetic."
                            elif Party[Count] == StormX:
                                    ch_s "Well. That is unfortunate."
                            elif Party[Count] == JubesX:
                                    ch_v "Well that's sad. . ."
                    else:
                            #anger
                            $ Party[Count].Brows = "angry"
                            if Party[Count] == RogueX:
                                    ch_r "Well that's pretty weak, asking a girl out when you can't even afford it."
                            elif Party[Count] == KittyX:
                                    ch_k "I wouldn't have gone out with you if I'd known you were such a bum."
                            elif Party[Count] == EmmaX:
                                    ch_e "You really should learn not to shop outside your class, [EmmaX.Petname]."
                            elif Party[Count] == LauraX:
                                    ch_l "Get your act together."
                                    $ Party[Count].change_stat("love", 200, -1)
                            elif Party[Count] == JeanX:
                                    ch_j "Sad."
                            elif Party[Count] == StormX:
                                    ch_s "Do not bite off more than you can chew."
                            elif Party[Count] == JubesX:
                                    ch_v "It'd be nice if you'd told me. . ."
                            $ Party[Count].change_stat("love", 200, -3)
                            if "deadbeat" not in Party[Count].History:
                                $ Party[Count].History.append("deadbeat")
                            else:
                                call Girl_Date_Over(Party[Count])
    #end choice consequences

    if JeanX in Party and line in (JeanX,"split","deadbeat"):
            #if Jean has to pay, she whammies
            ch_j "Waiter?"
            $ JeanX.change_face("confused",Eyes="psychic")
            ch_j ". . ."
            $ JeanX.change_face("sly")
            ch_j "There, that should cover it."

    #Boosts lust based on price spent
    $ Count = int(Date_Bonus[0]/2)
    $ Count = 10 if Count >= 10 else Count

    $ Party[0].change_stat("lust", 60, Count, alternates = {"Emma": {"check": 75, "value": Count}})

    $ Count = int(Date_Bonus[1]/2)
    $ Count = 10 if Count >= 10 else Count
    if len(Party) >= 2:
            $ Party[1].change_stat("lust", 60, Count, alternates = {"Emma": {"check": 75, "value": Count}})

    $ Count = 0
    $ Play_Cost = 0
    $ Date_Cost[0] = 0
    $ Date_Cost[1] = 0
    return

label Date_Bonus(Girl=0, Amount=0):
    #This updates the prime value if the girl is prime, second if not.
    # call Date_Bonus(RogueX,5)
    if Party[0] == Girl:
                $ Date_Bonus[0] += Amount
    elif Girl in Party:
                $ Date_Bonus[1] += Amount
    return

label Date_End:#rkeljsv
    #The end of the date jumped to from any end of date
    if time_index == 2: #evening time
            #makes it night time
            if Round > 20:
                    $ bg_current = "bg_date"
                    call set_the_scene(Dress=0)
                    "You decide to walk back slowly, as the night falls around you. . ."

            call Wait(Outfit = 0)

            $ bg_current = "bg_date"
            call set_the_scene(Dress=0)
    else:
            $ bg_current = "bg_player"
            call set_the_scene(Entry=1,Dress=0)

    if len(Party) >= 2:
            #if there are two girls
            menu:
                "Who's room do you visit first?"
                "[RogueX.name]" if RogueX in Party:
                        call Girl_Date_End(RogueX)
                "[KittyX.name]" if KittyX in Party:
                        call Girl_Date_End(KittyX)
                "[EmmaX.name]" if EmmaX in Party:
                        call Girl_Date_End(EmmaX)
                "[LauraX.name]" if LauraX in Party:
                        call Girl_Date_End(LauraX)
                "[JeanX.name]" if JeanX in Party:
                        call Girl_Date_End(JeanX)
                "[StormX.name]" if StormX in Party:
                        call Girl_Date_End(StormX)
                "[JubesX.name]" if JubesX in Party:
                        call Girl_Date_End(JubesX)
                "Bring them both back to your room" if len(Party) >= 2:
                        jump Player_Date_End
                "Neither, just head home alone": #disable
                        call Date_Ditched
            jump Date_Over
    if Party and Party[0]:
            call Girl_Date_End(Party[0])
    else:
            $ Party = []
            "You head back to your room."

label Date_Over:
    if time_index == 2: #evening time
            #makes it night time
            call Wait(Outfit = 0)
    $ Player.daily_history.append("post date")
    $ bg_current = "bg_player"
    call clear_the_room("all",0,1)
    jump Misplaced

label Player_Date_End:
    #Called if you call them back to your room
    $ bg_current = "bg_player"
    $ Girls = Party[:]
    while Girls:
            $ Girls[0].location = "bg_player"
            $ Girls.remove(Girls[0])
    call set_the_scene(Dress=0)
    call Taboo_Level
    if len(Party) >= 2:
            "You bring the girls to your own door."
            menu:
                "Who do you want to talk to?"
                "[RogueX.name]" if RogueX in Party:
                        call Girl_Date_End(RogueX)
                "[KittyX.name]" if KittyX in Party:
                        call Girl_Date_End(KittyX)
                "[EmmaX.name]" if EmmaX in Party:
                        call Girl_Date_End(EmmaX)
                "[LauraX.name]" if LauraX in Party:
                        call Girl_Date_End(LauraX)
                "[JeanX.name]" if JeanX in Party:
                        call Girl_Date_End(JeanX)
                "[StormX.name]" if StormX in Party:
                        call Girl_Date_End(StormX)
                "[JubesX.name]" if JubesX in Party:
                        call Girl_Date_End(JubesX)
                "Go to Sleep":
                        pass
    elif Party and Party[0]:
            "You bring [Party[0].name] to your own door."
            call Girl_Date_End(Party[0])
    jump Player_Room

label Girl_Date_End(Girl=0): #nee R_Date_End
    #Called if you end up with girl at the end of the date
    if Girl not in all_Girls:
            $ Party = []
            jump Date_End
    if bg_current != "bg_player":
            #skips this portion if you are in the player's room already
            menu:
                "Take [Girl.name] back to her room?":
                    pass
                "Just leave and head back to yours.":
                    call Date_Ditched
                    jump Date_Over

            $ bg_current = Girl.Home
            $ Girl.location = Girl.Home
            if len(Party) >= 2 and Party[1] != Girl:
                    $ Party[1].location = Girl.Home
            call set_the_scene(Dress=0)
            call Taboo_Level

    if len(Party) >= 2 and Party[0] != Girl:
            # If you picked the secondary girl, it flips them
            $ Party.reverse()
            $ Date_Bonus.reverse()

    if bg_current != "bg_player":
            "You walk [Girl.name] back to her room."
    if Date_Bonus[0] < 0:
            #if it was a bad date, no bonus
            $ Girl.change_face("angry", 0,Eyes = "side")
            if Girl == RogueX:
                    ch_r "Well that was a waste of an evening. I'll see you around, [Player.name]."
            elif Girl == KittyX:
                    ch_k "You[Girl.like]really need to get your shit together, [Player.name]."
            elif Girl == EmmaX:
                    ch_e "It's possible I could have had a worse evening, [Player.name]."
            elif Girl == LauraX:
                    ch_l "That was a real shitshow, [Player.name]."
            elif Girl == JeanX:
                    ch_j "You -do- understand how badly that went, right [Player.name]?"
            elif Girl == StormX:
                    ch_s "Let us just consider this evening a failure, [Player.name]."
            elif Girl == JubesX:
                    ch_v "I really had an awful evening there, [Player.name]. . ."
            if bg_current == "bg_player":
                if Girl == KittyX:
                    "She phases through the wall toward her room."
                else:
                    "She storms off down the hall."
            else:
                    "She slams the door on you."
            call set_the_scene(Entry=1,Dress=0)
            $ Date_Bonus[0] = 0
            call Girl_Date_Over(Girl,0)
            jump Date_End
    else:
        if Date_Bonus[0] > 20:
            #if it was a very good date
            $ Girl.change_face("sexy", 1)
            if Girl == RogueX:
                            ch_r "Well that was a lot of fun, [Girl.Petname]. I don't want the night to end . . ."
            elif Girl == KittyX:
                    if bg_current == "bg_player":
                            ch_k "That was fun, [Girl.Petname]. Do I have to go . . ."
                    else:
                            ch_k "That was fun, [Girl.Petname]. Do you have to go . . ."
            elif Girl == EmmaX:
                    if bg_current == "bg_player":
                            ch_e "That was a lovely evening, [Girl.Petname]. Could I come in for a nightcap?"
                    else:
                            ch_e "That was a lovely evening, [Girl.Petname]. Care for a nightcap? . ."
            elif Girl == LauraX:
                    if bg_current == "bg_player":
                            ch_l "I had fun, [Girl.Petname]. We done, or. . ."
                    else:
                            ch_l "I had fun, [Girl.Petname]. We done, or . . ."
            elif Girl == JeanX:
                    if bg_current == "bg_player":
                            ch_j "That was fun, [Girl.Petname]. Invite me in."
                    else:
                            ch_j "That was fun, [Girl.Petname]. You can come inside."
                            menu:
                                "Phrasing. . .":
                                        $ Girl.change_face("confused")
                                        ch_j "???"
                                        $ Girl.change_face("sly",1)
                                ". . .":
                                        pass
            elif Girl == StormX:
                    if bg_current == "bg_player":
                            ch_s "That was a delightful evening, [Girl.Petname]. Would you mind if I came inside?"
                    else:
                            ch_s "That was a delightful evening, [Girl.Petname]. Would you like to come inside?"
                    menu:
                        "Phrasing. . .":
                                $ Girl.change_face("confused")
                                ch_s "???"
                                $ Girl.change_face("sly",1)
                        "I believe that's my line. . ." if bg_current == "bg_player":
                                $ Girl.change_face("confused")
                                ch_s "But this is your room. . ."
                                $ Girl.change_face("sly",1)
                        ". . .":
                                pass
            elif Girl == JubesX:
                    ch_v "Well, that was fun, [Girl.Petname]. . . "
                    ch_v "I guess maybe you've gotta get some sleep though? . ."
        else:
            #if it was a mediocre date
            $ Girl.change_face("smile", 1)
            if Girl == RogueX:
                    ch_r "Well that was a lot of fun, [Girl.Petname]. We'll have to do it again."
            elif Girl == KittyX:
                    ch_k "Well that was fun, [Girl.Petname]. Text me later."
            elif Girl == EmmaX:
                    ch_e "That was a lovely evening, [Girl.Petname]. We'll have to do it again."
            elif Girl == LauraX:
                    ch_l "I had fun, [Girl.Petname]. Talk to you later."
            elif Girl == JeanX:
                    ch_j "Well, that's that. 'Night."
            elif Girl == StormX:
                    ch_s "I enjoyed the evening, [Girl.Petname]. We should do this again."
            elif Girl == JubesX:
                    ch_v "Well, that was fun, [Girl.Petname]. Maybe we could do this again."
        $ Girl.Date += 1
        menu:
            extend ""
            "Could I get a good night kiss?":
                    if Approvalcheck(Girl, 600, Bonus=(10*Date_Bonus[0])):
                        $ Girl.Mouth = "smile"
                        if Girl == RogueX:
                                ch_r "Ok, [Girl.Petname]. I suppose you've earned it."
                        elif Girl == KittyX:
                                ch_k "Heh, I guess so. . ."
                        elif Girl == EmmaX:
                                ch_e "[Girl.Petname], I suppose I could indulge you."
                        elif Girl == LauraX:
                                ch_l "Well if you insist. . ."
                        elif Girl == JeanX:
                                ch_j "Oh, I don't see why not. . ."
                        elif Girl == StormX:
                                ch_s "I suppose that it would not hurt. . ."
                        elif Girl == JubesX:
                                ch_v "Sure, why not. . ."
                        call Date_Sex_Break(Girl,0,2)
                        $ multi_action = 0
                        call KissPrep(Girl)
                        $ multi_action = 1
                    if Approvalcheck(Girl, 900, Bonus=(10*Date_Bonus[0])):
                        $ Girl.change_face("sexy", 1)
                        if Girl == RogueX:
                                if bg_current == "bg_player":
                                        ch_r "That was real nice, how about I come inside for a minute. . ."
                                else:
                                        ch_r "That was real nice, how about you come inside for a minute. . ."
                        elif Girl == KittyX:
                                ch_k "Hmmm . . ."
                                if bg_current == "bg_player":
                                        ch_k "Could I. . . maybe come inside for a minute?"
                                else:
                                        ch_k "Maybe. . . come inside for a minute?"
                        elif Girl == EmmaX:
                                if bg_current == "bg_player":
                                        ch_e "Hmm, are you sure I couldn't come in? . ."
                                else:
                                        ch_e "Hmm, are you sure you couldn't come in? . ."
                        elif Girl == LauraX:
                                ch_l "Hmmm . . ."
                                ch_l "Could I. . . borrow you for a minute?"
                        elif Girl == JeanX:
                                ch_j "Hmmm . . ."
                                ch_j "I think that bought you some extra time"
                        elif Girl == StormX:
                                if bg_current == "bg_player":
                                        ch_s "Now, would you not like to come in? . ."
                                else:
                                        ch_s "Now, could I still not come in? . ."
                        elif Girl == JubesX:
                                ch_v "Hmmm . . ."
                                if bg_current == "bg_player":
                                        ch_v "Did you wanna. . . invite me in?"
                                else:
                                        ch_v "Did you wanna. . . come inside?"
                        call Date_Sex_Break(Girl)
                        if _return == 4:
                                if bg_current == "bg_player":
                                        ch_p "You should probably get going, sorry."
                                else:
                                        ch_p "I should probably get going, sorry."
                                call Girl_Date_Over(Girl,0)
                                jump Date_End
                    else:
                        $ Girl.change_face("smile", 1)
                        if Girl == RogueX:
                                ch_r "That was real nice, I'll see you later, [Girl.Petname]."
                        elif Girl == KittyX:
                                ch_k "That was nice, text you later!"
                        elif Girl == EmmaX:
                                ch_e "And now, I'll see you tomorrow, [Girl.Petname]."
                        elif Girl == LauraX:
                                ch_l "That was nice, talk to you later."
                        elif Girl == JeanX:
                                ch_j "Ok, time to go now."
                        elif Girl == StormX:
                                ch_s "I will see you tomorrow then, [Girl.Petname]."
                        elif Girl == JubesX:
                                ch_v "Ok, see you tomorrow then, [Girl.Petname]."
                        $ Date_Bonus[0] = 0
                        call Girl_Date_Over(Girl,0)
                        jump Date_End

            "Want to have a little fun first?" if bg_current != "bg_player":
                    if Approvalcheck(Girl, 800, Bonus=(10*Date_Bonus[0])):
                        $ Girl.change_face("sexy", 1)
                        if Girl == RogueX:
                                ch_r "Alright, [Girl.Petname]. I think you've earned it."
                        elif Girl == KittyX:
                                ch_k "Heh, I guess so. . ."
                        elif Girl == EmmaX:
                                ch_e "Oh, fine, [Girl.Petname]. I'll indulge you."
                        elif Girl == LauraX:
                                ch_l "I guess, sure."
                        elif Girl == JeanX:
                                ch_j "Yeah, ok."
                        elif Girl == StormX:
                                ch_s "Yes, I think that I might, [Girl.Petname]."
                        elif Girl == JubesX:
                                ch_v "Oh, sure! The night's young."
                        call Date_Sex_Break(Girl)
                        if _return == 4:
                                ch_p "I should probably get going, sorry."
                                call Girl_Date_Over(Girl,0)
                                jump Date_End
            "Could you come in for a bit?" if bg_current == "bg_player":
                    if Approvalcheck(Girl, 800, Bonus=(10*Date_Bonus[0])):
                        $ Girl.change_face("sexy", 1)
                        if Girl == RogueX:
                                ch_r "Alright, [Girl.Petname]. I think you've earned it."
                        elif Girl == KittyX:
                                ch_k "Heh, I guess so. . ."
                        elif Girl == EmmaX:
                                ch_e "Oh, fine, [Girl.Petname]. I'll indulge you."
                        elif Girl == LauraX:
                                ch_l "I guess, sure."
                        elif Girl == JeanX:
                                ch_j "Huh? Ok?"
                        elif Girl == StormX:
                                ch_s "I was hoping that you would ask. . ."
                        elif Girl == JubesX:
                                ch_v "Oh, sure! The night's young."
                        call Date_Sex_Break(Girl)
                        if _return == 4:
                                ch_p "You should probably get going, sorry."
                                call Girl_Date_Over(Girl,0)
                                jump Date_End

            "Ok, good night then.":
                    $ Girl.change_face("confused", 1)
                    if Girl == EmmaX:
                            $ Girl.Mouth = "smirk"
                            if bg_current == "bg_player":
                                    "[Girl.name] looks a little annoyed, but heads out."
                            else:
                                    "[Girl.name] looks a little annoyed, but you head out."
                    else:
                            if bg_current == "bg_player":
                                    "[Girl.name] looks a little confused, but she heads out."
                            else:
                                    "[Girl.name] looks a little confused, but you head out."
                    call Girl_Date_Over(Girl,0)
                    jump Date_End

    # Rogue lets you into her room:
    if bg_current != "bg_player":
            $ bg_current = Girl.Home
    call set_the_scene(Dress=0)
    call Taboo_Level
    $ Girl.change_face("sexy", 1)
    if Girl == RogueX:
            if len(Party) < 2:#not Party[1]:
                            ch_r "So, [Girl.Petname], you've got me all alone, what are your intentions? . ."
            else:
                    if bg_current == "bg_player":
                            ch_r "So, [Girl.Petname], we're in your room together, what are your intentions? . ."
                    else:
                            ch_r "So, [Girl.Petname], we're in my room together, what are your intentions? . ."
    elif Girl == KittyX:
                            ch_k "So[Girl.like]here we are. . . "
    elif Girl == EmmaX:
            if len(Party) < 2: #not Party[1]:
                            ch_e "Now, [Girl.Petname], we're alone together, what would you like to do next? . ."
            else:
                    if bg_current == "bg_player":
                            ch_e "Now, [Girl.Petname], we're in your room together, what would you like to do next? . ."
                    else:
                            ch_e "Now, [Girl.Petname], we're in my room together, what would you like to do next? . ."
    elif Girl == LauraX:
                            ch_l "So. . . after a date like that. . . "
    elif Girl == JeanX:
                            ch_j "So, what did you have in mind? . ."
    elif Girl == StormX:
            if len(Party) < 2: #not Party[1]:
                            ch_s "We are alone now, [Girl.Petname], did you have anything more in mind? . ."
            else:
                            ch_s "Now [Girl.Petname], did you have anything more in mind? . ."
    elif Girl == JubesX:
                            ch_v "So. . . what did you wanna do to me?"
    $ Player.daily_history.append("post date")
    call sex_menu(Girl)

    if "angry" in Girl.recent_history:
            if bg_current == "bg_player":
                if Girl == KittyX:
                    "[KittyX.name] storms off through the nearest wall."
                elif Girl in (EmmaX,StormX):
                    "[Girl.name] stalks through the door and back to her room."
                else:
                    "[Girl.name] storms off down the hall."
            else:
                    "[Girl.name] shoves you out into the hall. You head back to your room."
                    $ bg_current = "bg_player"
            call remove_girl("all")
            $ Player.daily_history.append("post date")
            jump Player_Room

    call Sleepover(Girl)
    jump Misplaced

label Date_Ditched(Girls=0):  #rkeljsv
    #if you ditch out on a date, called by Date End
    #Girls tracks the number fo people who have already answered.
    while Party:
        if Party[0] in all_Girls:

                if Party[0] == JeanX:
                        if Girls:
                                $ Party[0].change_face("confused")
                                ch_j "What? Yeah, bye."
                        else:
                                ch_j "Oh, bye then."
                elif Approvalcheck(Party[0], 1200):
                    $ Party[0].change_face("confused")
                    if Party[0] == RogueX:
                            if Girls:
                                    ch_r "Yeah, bye?"
                            else:
                                    ch_r "Huh? Ok, bye, I guess."
                    elif Party[0] == KittyX:
                            if Girls:
                                    ch_k "Yeah, um, bye?"
                            else:
                                    ch_k "Um, bye?"
                    elif Party[0] == EmmaX:
                            if Girls:
                                    ch_e "Yes, a pity."
                            else:
                                    ch_e "Oh? Pity."
                    elif Party[0] == LauraX:
                            if Girls:
                                    ch_l "Yeah, bye."
                            else:
                                    ch_l "Um, ok, bye."
                    elif Party[0] == StormX:
                            if Girls:
                                    ch_s "Oh? Well that is unfortunate."
                            else:
                                    ch_s "Well that is unfortunate."
                    elif Party[0] == JubesX:
                            if Girls:
                                    ch_v "Ok then. . . bye?"
                            else:
                                    ch_v "Um, bye?"
                elif Approvalcheck(Party[0], 400):
                    $ Party[0].change_face("smile")
                    if Party[0] == RogueX:
                            if Girls:
                                    ch_r "Yeah, see ya later."
                            else:
                                    ch_r "Oh, bye then."
                    elif Party[0] == KittyX:
                            if Girls:
                                    ch_k "Yeah, Bye!"
                            else:
                                    ch_k "Bye!"
                    elif Party[0] == EmmaX:
                            if Girls:
                                    ch_e "Oh, yes, good night."
                            else:
                                    ch_e "Good night then."
                    elif Party[0] == LauraX:
                            if Girls:
                                    ch_l "Yeah, bye."
                            else:
                                    ch_l "Um, ok, bye."
                    elif Party[0] == StormX:
                            if Girls:
                                    ch_s "Oh? Well that is unfortunate."
                            else:
                                    ch_s "Well that is unfortunate."
                    elif Party[0] == JubesX:
                            if Girls:
                                    ch_v "Ok then. . . bye?"
                            else:
                                    ch_v "Um, bye?"
                else:
                    $ Party[0].change_face("angry")
                    if Party[0] == RogueX:
                            if Girls:
                                    ch_r "Right, \"bye.\""
                            else:
                                    ch_r "Good riddance."
                    elif Party[0] == KittyX:
                            if Girls:
                                    ch_k "Yeah, later, asshole."
                            else:
                                    ch_k "Later, asshole."
                    elif Party[0] == EmmaX:
                            if Girls:
                                    ch_e "I'm not surprised."
                            else:
                                    ch_e "You're excused!"
                    elif Party[0] == LauraX:
                            if Girls:
                                    ch_l "Wow, yeah, bye."
                            else:
                                    ch_l "Screw you."
                    elif Party[0] == StormX:
                            if Girls:
                                    ch_s "Yes, I am disappointed."
                            else:
                                    ch_s "What a disaster."
                    elif Party[0] == JubesX:
                            if Girls:
                                    ch_v "Yeah, get going. . ."
                            else:
                                    ch_v "Um, bye?"
                $ Party[0].location = Party[0].Home
                $ Girls += 1
        $ Party.remove(Party[0])
    return

label Girl_Date_Over(Girl=0,Angry=1): #rkeljsv
        # Called if Girl is pissed and leaves
        if Angry:
                $ Girl.recent_history.append("angry")
                $ Girl.daily_history.append("angry")
                $ Girl.change_face("angry")
                if Girl == RogueX:
                        ch_r "I think I'm done here, [Girl.Petname]."
                elif Girl == KittyX:
                        ch_k "You know what?"
                        ch_k "[Player.name]'s a Jerk!"
                elif Girl == EmmaX:
                        ch_e "I think that's enough of that, [Girl.Petname]."
                elif Girl == LauraX:
                        ch_l "What was that?"
                        ch_l "Eat a dick."
                elif Girl == JeanX:
                        ch_j "Oooooh, you blew it."
                elif Girl == StormX:
                        ch_s "I have had enough."
                elif Girl == JubesX:
                        ch_v "Well, I'm out. . ."
                "[Girl.name] storms out."
        if "study" in Player.recent_history:
                call remove_girl(Girl)
                return
        if Party[0] == Girl:
                $ Date_Bonus[0] = Date_Bonus[1]
                $ Date_Cost[0] = Date_Cost[1]
                $ Date_Cost[1] = 0
        elif Girl in Party:
                # If this person was in the second slot, flip them.
                $ Date_Bonus.reverse
                $ Date_Cost.reverse

        $ Date_Bonus[1] = 0
        $ Date_Cost[1] = 0
        call remove_girl(Girl)
        if not Party:
                #if nobody is left, quit the date
                jump Date_End
        call shift_focus(Party[0])
        return
