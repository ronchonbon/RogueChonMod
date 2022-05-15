label Breakup(Girl=0,Other=0,Anger = 0,Girls=[]): #rkeljsv
        # call Breakup(RogueX) from Chat
        # Repeats is number of times you've broken up, Other is a potential other woman, Anger is a meter that ends things at 4+

        $ Girl.AddWord(1,"breakup talk","breakup talk",0,0)

        if Girl.Break[1] > 3:
                $ Girl.change_face("angry")
                $ Girl.change_stat("love", 50, -5, 1)
                $ Girl.change_stat("love", 80, -10, 1)
                $ Girl.change_stat("obedience", 30, -5, 1)
                $ Girl.change_stat("obedience", 50, -10, 1)
                $ Girl.change_stat("inhibition", 50, 3)
                $ Girl.change_stat("inhibition", 80, 1)
                call Anyline(Girl,"This is getting old.")
                $ Anger -= 1
        elif Girl.Break[1]:
                $ Girl.change_face("surprised")
                $ Girl.change_stat("love", 50, -5, 1)
                $ Girl.change_stat("obedience", 30, -5, 1)
                $ Girl.change_stat("inhibition", 80, 1)
                call Anyline(Girl,"What, again?")
                $ Girl.change_face("angry")
                $ Anger += 1
        else:
                $ Girl.change_face("surprised")
                call Anyline(Girl,"What?! Why?")

        $ line = 0
        menu:
            "It's not you, it's me.":
                    $ Girl.change_stat("love", 200, -5)
                    $ Girl.change_stat("obedience", 80, -5)
                    $ Girl.change_stat("inhibition", 50, 3)
                    $ Girl.change_stat("inhibition", 70, 1)
                    $ Girl.change_face("confused")

            "I just think we need a break.":
                    $ Girl.change_stat("love", 200, -5)
                    $ Girl.change_face("sad")

            "I've found someone else.":
                    $ Anger += 1
                    $ Girl.change_stat("love", 200, -10)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 80, 3)
                    $ Girl.change_stat("inhibition", 50, -5)
                    $ Girl.change_face("angry")
                    call Anyline(Girl,"Who is it?")
                    menu:
                        extend ""
                        "[RogueX.name]" if Girl != RogueX:
                                $ Other = RogueX
                        "[KittyX.name]" if Girl != KittyX and "met" in KittyX.History:
                                $ Other = KittyX
                        "[EmmaX.name]" if Girl != EmmaX and "met" in EmmaX.History:
                                $ Other = EmmaX
                        "[LauraX.name]" if Girl != LauraX and "met" in LauraX.History:
                                $ Other = LauraX
                        "[JeanX.name]" if Girl != JeanX and "met" in JeanX.History:
                                $ Other = JeanX
                        "[StormX.name]" if Girl != StormX and "met" in StormX.History:
                                $ Other = StormX
                        "[JubesX.name]" if Girl != JubesX and "met" in JubesX.History:
                                $ Other = JubesX
                        "I won't say.":
                                $ Girl.change_stat("love", 200, -5)
                                $ Girls = active_Girls[:]
                                $ Girls.remove(Girl)
                                $ Count = 0
                                while Girls:
                                        if Girls[0].SEXP > Count:
                                                # if you've boned this girl more than the last, she's the boss
                                                $ Other = Girls[0]
                                                $ Count = Girls[0].SEXP
                                        $ Girls.remove(Girls[0])
                                $ Count = 0
                                if not Other:
                                        call Anyline(Girl,"Well it's got to be someone. . .")
                                else:
                                        call Anyline(Girl,"It's "+Other.name+", isn't it.")
                        "I was kidding.":
                                $ Girl.change_stat("love", 200, -5)
                                $ Girl.change_stat("obedience", 50, 3)
                                $ Girl.change_face("angry")
                                if Girl == RogueX:
                                        ch_r "That was a pretty rude way to deflect there."
                                elif Girl == KittyX:
                                        ch_k "I'll[KittyX.like]kid you!"
                                elif Girl == EmmaX:
                                        ch_e "Oh, you do *not* want to \"kid\" me about that."
                                elif Girl == LauraX:
                                        ch_l ". . ."
                                elif Girl == JeanX:
                                        ch_j "The last time I heard a joke like that, someone lost a 7th birthday."
                                elif Girl == StormX:
                                        ch_s "You should not \"kid\" about such things, [Girl.Petname]."
                                elif Girl == JubesX:
                                        ch_v "Right. . ."
                                $ Girl.change_face("normal")
                                $ Anger += 1

            "I'm just done with you.":
                    $ Girl.change_face("angry")
                    $ Girl.change_stat("love", 50, 3)
                    $ Girl.change_stat("love", 200, -15)
                    $ Girl.change_stat("obedience", 50, 5)
                    $ Girl.change_stat("obedience", 80, 5)
                    $ Girl.change_stat("obedience", 200,5)
                    $ Girl.change_stat("inhibition", 50, -5)
                    $ Anger += 1
        #end first question

        if not Other:
                #"denial":
                $ Girl.change_face("sad")
                if Approvalcheck(Girl, 900, "O"):
                        #high obedience
                        call Anyline(Girl,"If that's really what you want. . .")
                elif Approvalcheck(Girl, 900, "L"):
                        #high love
                        call Anyline(Girl,"But I love you so much!")
                elif Approvalcheck(Girl, 900, "I") or Girl == JeanX:
                        #super casual
                        call Anyline(Girl,"If that's how you feel. . .")
                elif Approvalcheck(Girl, 1500):
                        #general mix
                        call Anyline(Girl,"But we mean so much to each other!")
                else:
                        #doesn't care too much
                        call Anyline(Girl,"Are you sure this is what you want?")
                $ line = "bargaining"

        else:
            #if there's another girl. . .
            #GirlLikecheck(RogueX,KittyX) if Rogue is the girl talking and Kitty is the "other girl"
            $ counter = int((Girl.GirlLikecheck(Other) - 500)/2)

            if Girl.GirlLikecheck(Other) >= 800:
                    $ Girl.change_stat("lust", 70, 5)
                    $ Girl.change_stat("obedience", 50, 5)
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("inhibition", 50, 1)
                    $ Girl.change_stat("inhibition", 200, 5)
                    $ Girl.change_face(5,2) #blush2
                    call Anyline(Girl,"Well, you have good tastes, at least.")
                    $ Girl.change_face(5,1) #blush1
            elif Girl.GirlLikecheck(Other) >= 600:
                    $ Girl.change_stat("love", 50, -5, 1)
                    $ Girl.change_stat("love", 80, -10, 1)
                    $ Girl.change_stat("obedience", 50, 5)
                    $ Girl.change_stat("obedience", 200, 3)
                    if Other == EmmaX and Girl != StormX:
                            call Anyline(Girl,"With our teacher?!")
                    if Other == StormX and Girl != EmmaX:
                            call Anyline(Girl,"With our teacher?!")
                    elif Girl == EmmaX and Other != StormX:
                            ch_e "And I always did like her in class. . ."
                    elif Girl == StormX and Other == EmmaX:
                            ch_s "And she seemed so respectable. . ."
                    elif Girl in (EmmaX,StormX) and Other in (EmmaX,StormX):
                            call Anyline(Girl,"You have a thing for teachers?")
                    elif Girl == LauraX:
                            ch_l "I do kinda like her."
                    elif Girl == JeanX:
                            ch_j "Well, she's not a complete bitch."
                    else:
                            call Anyline(Girl,"With one of my friends?!")
                    $ Girl.change_face("normal")
                    $ Anger += 1
            elif Girl.GirlLikecheck(Other) >= 400:
                    $ Girl.change_stat("love", 50, -3, 1)
                    $ Girl.change_stat("love", 80, -5, 1)
                    $ Girl.change_stat("obedience", 80, 5)
                    $ Girl.change_stat("inhibition", 50, 1)
                    $ Girl.change_stat("inhibition", 80, 3)
                    call Anyline(Girl,"You know you can do better.")
            else: #Girl.GirlLikecheck(Other) < 400
                    $ Girl.change_stat("love", 50, -5, 1)
                    $ Girl.change_stat("obedience", 80, 3)
                    $ Girl.change_stat("inhibition", 50, 2)
                    $ Girl.change_stat("inhibition", 80, 5)
                    $ Girl.change_face("angry")
                    call Anyline(Girl,"With that skank?!")
                    $ Anger += 2

            if Approvalcheck(Girl, 2000, Bonus = counter):
                    $ Girl.change_stat("lust", 70, 5)
                    $ Girl.change_face("sexy")
                    call Anyline(Girl,"Why not both of us?")
                    $ line = "threeway"
            else:
                    $ Girl.change_face("sad")
                    call Anyline(Girl,"You would rather be with her than with me?")
                    menu:
                        extend ""
                        "Yes, I would.":
                                $ Girl.change_stat("love", 50, -3, 1)
                                $ Girl.change_stat("love", 80, -5, 1)
                                $ Girl.change_stat("obedience", 30, 1)
                                $ Girl.change_stat("obedience", 50, 1)
                                $ Anger += 1
                                $ line = "bargaining"
                                if Girl == RogueX:
                                        ch_r "Well then I don't think I can help you."
                                elif Girl == KittyX:
                                        ch_k "!!!"
                                elif Girl == EmmaX:
                                        ch_e "I suppose you've made your choice then."
                                elif Girl == LauraX:
                                        ch_l "Your loss."
                                elif Girl == JeanX:
                                        ch_j "Nonsense."
                                elif Girl == StormX:
                                        ch_s "Then I understand."
                                        $ line = "threeway"
                                elif Girl == JubesX:
                                        ch_v "Rough. . ."

                        "I'd rather be with both of you.":
                                $ line = "threeway"

                        "No, I'm sorry, never mind that.":
                                $ Girl.change_stat("love", 50, -3, 1)
                                $ Girl.change_stat("obedience", 80, -5)
                                call Anyline(Girl,"Not doing yourself any favors there. . .")
                                $ line = "bargaining"
        #end "if there's another" or not

        if line == "threeway" and Anger < 4:
                if Girl == StormX:
                        ch_s "So would she be fine with you dating us both?"
                else:
                        call Anyline(Girl,"Date us both at once? What does she think about that?")
                menu Breakup_Threeway_Offer:
                        extend ""
                        "She said it would be ok with her." if "poly "+ Girl.Tag in Other.Traits or Girl.Tag+"Yes" in Player.Traits:
                                #"poly Rogue" in KittyX.Traits, or "KittyYes" in Player.Traits
                                if Approvalcheck(Girl, 1800, Bonus = counter):
                                        $ Girl.change_face("smile", 1)
                                        $ Girl.change_stat("lust", 70, 5)
                                        $ Girl.change_stat("obedience", 50, 5)
                                        $ Girl.change_stat("obedience", 80, 3)
                                        $ Girl.change_stat("inhibition", 50, 3)
                                        $ Girl.change_stat("inhibition", 80, 1)
                                        if Girl.GirlLikecheck(Other) < 400:
                                                $ Girl.change_face("angry")
                                                if Girl == RogueX:
                                                        ch_r "I can't stand that bitch, but for you I'll put up with her."
                                                elif Girl == KittyX:
                                                        ch_k "That bitch! Fine, I'll put up with her."
                                                elif Girl == EmmaX:
                                                        ch_e "I suppose I can be the better woman here. . ."
                                                        ch_e "Not that it's hard to accomplish."
                                                elif Girl == LauraX:
                                                        ch_l "I can keep my claws in. . . for you."
                                                elif Girl == JeanX:
                                                        ch_j "Well. .. I guess I can find -some- use for her."
                                                elif Girl == StormX:
                                                        ch_s "I dislike her, but I will put up with her."
                                                elif Girl == JubesX:
                                                        ch_v "Well, this is not cool. . . but I can deal. . ."
                                        elif Girl == StormX:
                                                ch_s "Then that is all I need to know."
                                        elif Girl.GirlLikecheck(Other) >= 700 or Girl == JeanX:
                                                $ Girl.change_face("sexy")
                                                call Anyline(Girl,"I have to say I've kind of been thinking about it myself.")
                                        elif Girl.love >= Girl.obedience:
                                                $ Girl.change_face("sad")
                                                call Anyline(Girl,"Just so long as we can be together, I can share.")
                                        else:
                                                #inhibition highest
                                                call Anyline(Girl,"If she's in, I am.")

                                        $ Girl.AddWord(1,0,0,"poly "+Other.Tag,0) #adds "poly Other" to traits
                                else:
                                        $ Anger += 2
                                        $ Girl.change_stat("love", 50, -10, 1)
                                        $ Girl.change_stat("love", 80, -15, 1)
                                        $ Girl.change_stat("obedience", 50, 3)
                                        $ Girl.change_stat("obedience", 80, 3)
                                        $ Girl.change_stat("inhibition", 50, 5)
                                        $ Girl.change_stat("inhibition", 80, 3)
                                        $ Girl.change_face("angry", 1)
                                        call Anyline(Girl,"Well maybe she did, but I don't want to share." )
                                        $ line = "bargaining"
                                        if Girl == StormX:
                                                $ line = "breakup"
                        #End "she said it'd be ok.

                        "I have no idea.": #if not KittyX.Break[0]:
                                $ line = "ask " + Other.Tag #"ask Kitty"

                        "She's not into it.": #if KittyX.Break[0]:
                                if Girl.GirlLikecheck(Other) >= 700:
                                        $ Girl.change_stat("love", 200, -5)
                                elif Girl.GirlLikecheck(Other) <= 400:
                                        $ Girl.change_stat("love", 90, 5)
                                call Anyline(Girl,"Well then why even bring it up?")


                        "Well, even if she doesn't agree. . .":
                                $ line = "ask " + Other.Tag #"ask Kitty"
                                if Girl.GirlLikecheck(Other) >= 700:
                                        $ Girl.change_face("angry")
                                        $ Girl.change_stat("love", 200, -5)
                                elif Girl.GirlLikecheck(Other) <= 400:
                                        $ Girl.change_stat("love", 90, 5)

                if line == "ask " + Other.Tag and Girl.GirlLikecheck(Other) >= 700:
                                #if previous responses had her wanting to ask the other girl about it
                                call Anyline(Girl,"You want me to ask her for you?")
                                menu:
                                    extend ""
                                    "Yes, that'd be a good idea.":
                                            $ Girl.change_stat("love", 90, 5)
                                            $ Girl.change_stat("obedience", 70, 1)
                                            $ Girl.change_stat("inhibition", 80, 5)
                                            $ Girl.change_face("sexy")
                                            call Anyline(Girl,"I guess I could.")
                                            $ Girl.AddWord(1,0,0,"ask "+Other.Tag,0) #adds "ask Other" to traits
                                            $ Girl.AddWord(1,0,0,"poly "+Other.Tag,0) #adds "poly Other" to traits
                                    "No, let's just keep it under cover.":
                                            $ Girl.change_stat("love", 50, -5, 1)
                                            $ Girl.change_stat("love", 80, -5, 1)
                                            $ Girl.change_stat("obedience", 80, 5)
                                            $ Girl.change_stat("inhibition", 50, 3)
                                            call Anyline(Girl,"I don't know. . .")

                if line == "breakup":
                        pass
                elif line != "bargaining" and "poly "+ Other.Tag not in Girl.Traits:
                        #if the answer is not "bargaining," but also the girl has not agreed yet. . .
                        #"poly Kitty" not in RogueX.Traits:
                        if "ask "+ Other.Tag not in Girl.Traits and not Approvalcheck(Girl, 1800, Bonus = -(int((Girl.GirlLikecheck(Other) - 600)/2))):
                                #"ask Kitty" not in RogueX.Traits
                                #checks if Girl likes you more than Other
                                $ Girl.change_stat("love", 50, -5, 1)
                                $ Girl.change_stat("obedience", 80, -10, 1)
                                $ Girl.change_stat("inhibition", 50, 5)
                                $ Girl.change_face("angry", 1)
                                if not Approvalcheck(Girl, 1800):
                                        call Anyline(Girl,"Maybe I don't like you that much either.")
                                else:
                                        $ Girl.change_stat("love", 80, -10, 1)
                                        $ Girl.change_stat("obedience", 50, -5, 1)
                                        if Girl == EmmaX and Other != StormX:
                                                ch_e "I'd rather not be dallying with another teacher's boyfriend. . ."
                                        elif Girl == EmmaX:
                                                ch_e "I'd rather not be dallying with a student's boyfriend. . ."
                                        elif Girl == StormX:
                                                ch_s "I would rather not creep around like that."
                                        elif Girl == JeanX:
                                                ch_j "I don't know, shes a little boring. . ."
                                        elif Other == EmmaX:
                                                call Anyline(Girl,"I don't want to get caught with the teacher's boyfriend!")
                                        else:
                                                call Anyline(Girl,"I'm not really cool with that, "+Other.name+"'s a friend of mine." )
                                $ Anger += 1
                                if Girl != StormX:
                                        $ line = "bargaining"
                        else:
                                #if she agrees to polygamy
                                $ Girl.change_stat("obedience", 30, 5)
                                $ Girl.change_stat("obedience", 50, 3)
                                $ Girl.change_stat("inhibition", 50, 5)
                                $ Girl.change_stat("inhibition", 80, 1)
                                $ Girl.change_face("sad")
                                if Girl.GirlLikecheck(Other) < 400:
                                        $ Girl.change_face("angry")
                                        if Girl == RogueX:
                                                ch_r "I can't stand that bitch, but for you I'll put up with her."
                                        elif Girl == KittyX:
                                                ch_k "That bitch! Fine, I'll put up with her."
                                        elif Girl == EmmaX:
                                                ch_e "I suppose I can be the better woman here. . ."
                                                ch_e "Not that it's hard to accomplish."
                                        elif Girl == LauraX:
                                                ch_l "I can keep my claws in. . . for you."
                                        elif Girl == JeanX:
                                                ch_j "Well. .. I guess I can find -some- use for her."
                                        elif Girl == StormX:
                                                ch_s "I dislike her, but I will put up with her."
                                        elif Girl == JubesX:
                                                ch_v "Well, this is not cool. . . but I can deal. . ."
                                elif Girl.GirlLikecheck(Other) >= 700:
                                        $ Girl.change_face("sexy")
                                        call Anyline(Girl,"I have to say I've kind of been thinking about it myself.")
                                elif Girl.love >= Girl.obedience:
                                        #RogueX.love >= RogueX.obedience:
                                        $ Girl.change_face("sad")
                                        call Anyline(Girl,"Just so long as we can be together, I can share.")
                                else:
                                        #inhibition highest
                                        call Anyline(Girl,"If she's in, I am.")
                                $ Girl.AddWord(1,0,0,"poly "+Other.Tag,0) #adds "poly Other" to traits
                                if "ask "+ Other.Tag in Girl.Traits:
                                        #"ask Kitty" in RogueX.Traits:
                                        call Anyline(Girl,"I'll talk to "+Other.name+" about it.")
                                else:
                                        $ Girl.change_face("sad")
                                        $ Girl.AddWord(1,0,0,"downlow",0) #adds "downlow" to traits
                                        if Girl == RogueX:
                                                ch_r "I guess we can keep this on the downlow, for now at least."
                                        elif Girl == KittyX:
                                                ch_k "Oooh, our little secret. . ."
                                        elif Girl == EmmaX:
                                                ch_e "I suppose I can be discreet."
                                        elif Girl == LauraX:
                                                ch_l "I can keep a secret."
                                        elif Girl == JeanX:
                                                ch_j "Sure, that works."
                                        elif Girl == StormX:
                                                ch_s "I can keep my secrets."
                                        elif Girl == JubesX:
                                                ch_v "I can keep to myself. . ."

                                        if Girl.GirlLikecheck(Other) >= 800 and Girl != JeanX:
                                                call Anyline(Girl, "Please talk to "+Other.name+" about sharing you openly though.")
                                        elif Girl.GirlLikecheck(Other) >= 500 and Girl != JeanX:
                                                call Anyline(Girl,"I really don't like going behind "+Other.name+"'s back though.")
                                        else:
                                                call Anyline(Girl,"Might be fun, sneaking around behind her back.")
                #End Threeway

        if line == "bargaining" and Anger < 4:
                $ Girl.change_face("sad")
                call Anyline(Girl,"You're sure there's no way I could convince you to stay?")
                menu Breakup_Bargaining:
                    extend ""
                    "Sorry, I've changed my mind.":
                            $ Girl.change_stat("obedience", 80, 5)
                            if Approvalcheck(Girl, 1500):
                                    $ line = "makeup"
                                    $ Girl.change_stat("love", 80, 5)
                                    if Girl == RogueX:
                                            ch_r "That's wonderful!"
                                    elif Girl == KittyX:
                                            ch_k "Ok!"
                                    elif Girl == EmmaX:
                                            ch_e "I can accept that as an apology. . ."
                                    elif Girl == LauraX:
                                            ch_l "Huh? Ok. . ."
                                    elif Girl == JeanX:
                                            ch_j "Finally, you've come to your senses."
                                    elif Girl == StormX:
                                            ch_s "Then you can stay."
                                    elif Girl == JubesX:
                                            ch_v "Cool. . ."
                            else:
                                    $ line = "breakup"
                                    $ Girl.change_stat("love", 90, -5)
                                    $ Girl.change_stat("obedience", 80, -5)
                                    $ Girl.change_stat("inhibition", 80, 10)
                                    if Girl == RogueX:
                                            ch_r "You know what? Save it. We're done."
                                    elif Girl == KittyX:
                                            ch_k "Too little, too late. . ."
                                    elif Girl == EmmaX:
                                            ch_e "I'm afraid it's too late for apologies."
                                    elif Girl == LauraX:
                                            ch_l "Uh-huh. Too late for that."
                                    elif Girl == JeanX:
                                            ch_j "You know what? Too late."
                                    elif Girl == StormX:
                                            ch_s "I am not interested in your games."
                                    elif Girl == JubesX:
                                            ch_v "Too late. . ."
                    "My mind's made up.":
                            $ Girl.change_stat("obedience", 80, 5)
                            $ line = "breakup"
                    "Well, you could do something for me. . .[[sex menu]":
                            $ Girl.AddWord(1,"bargainsex",0,0,0) #adds "bargainsex" to recent
                            $ Girl.change_stat("obedience", 80, 3)
                            $ temp_modifier = 50
                            $ multi_action = 0
                            call expression Girl.Tag + "_SMenu" #call Rogue_SexMenu
                            $ multi_action = 1
                            menu:
                                "Ok, I guess we can give it another shot.":
                                        $ Girl.change_stat("love", 80, 3)
                                        $ Girl.change_stat("obedience", 80, 5)
                                        $ line = "makeup"
                                        $ Girl.change_face("smile")

                                "That was nice, but we're still over.":
                                        $ Girl.change_face("angry")
                                        $ Girl.change_stat("love", 50, -5, 1)
                                        $ Girl.change_stat("love", 80, -10, 1)
                                        $ Girl.change_stat("obedience", 50, 15)
                                        $ Girl.change_stat("obedience", 80, 10)
                                        $ line = "breakup"
                                        $ Anger += 4

                    "Maybe if we brought someone else into this relationship?" if not Other and "bargainthreeway" not in Girl.recent_history:
                            # if you haven't just tried this
                            $ Girl.AddWord(1,"bargainthreeway",0,0,0) #adds "bargainthreeway" to recent
                            call Anyline(Girl,"Who?")
                            menu:
                                extend ""
                                "[RogueX.name]?" if Girl != RogueX:
                                        $ Other = RogueX
                                "[KittyX.name]?" if Girl != KittyX and "met" in KittyX.History:
                                        $ Other = KittyX
                                "[EmmaX.name]?" if Girl != EmmaX and "met" in EmmaX.History:
                                        $ Other = EmmaX
                                "[LauraX.name]?" if Girl != LauraX and "met" in LauraX.History:
                                        $ Other = LauraX
                                "[JeanX.name]?" if Girl != JeanX and "met" in JeanX.History:
                                        $ Other = JeanX
                                "[StormX.name]?" if Girl != StormX and "met" in StormX.History:
                                        $ Other = StormX
                                "[JubesX.name]?" if Girl != JubesX and "met" in JubesX.History:
                                        $ Other = JubesX

                                "Up to you?":
                                        $ Girl.change_face("confused")
                                        #picks her favorite girl. . .
                                        $ Girls = active_Girls[:]
                                        $ Girls.remove(Girl)
                                        $ Count = 0
                                        while Girls:
                                                if Girl.GirlLikecheck(Girls[0]) > Count:
                                                        # if she likes this girl more than the last, she's the pick
                                                        $ Other = Girls[0]
                                                        $ Count = Girl.GirlLikecheck(Girls[0])
                                                $ Girls.remove(Girls[0])
                                        $ Count = 0
                                        call Anyline(Girl,Other.name+"?")

                                "Never mind, silly question.":
                                        $ Girl.change_stat("love", 200, -10)
                                        $ Girl.change_stat("obedience", 50, -10, 1)
                                        $ Anger += 1
                                        $ Girl.change_face("angry")
                                        jump Breakup_Bargaining

                            if Other:
                                    $ Girl.change_face("confused")
                                    jump Breakup_Threeway_Offer

                if Anger < 3 and line != "breakup" and line != "makeup":
                        #if no decision and she's not pissed yet, loop
                        if Girl == StormX:
                                $ line = "breakup"
                        else:
                                jump Breakup_Bargaining
        # End Bargaining



        if line == "breakup" or Anger >= 4:
                if Anger >= 4:
                        #if she's pissed
                        $ Girl.change_face("angry")
                        $ Girl.change_stat("love", 60, -10, 1)
                        $ Girl.change_stat("obedience", 50, -5)
                        $ Girl.change_stat("inhibition", 70, 5)
                        if Girl == RogueX:
                                ch_r "Well fuck you then!"
                        elif Girl == KittyX:
                                ch_k "Jerk!!"
                        elif Girl == EmmaX:
                                ch_e "Scum."
                        elif Girl == LauraX:
                                ch_l "You're gonna want to back up a few steps."
                        elif Girl == JeanX:
                                ch_j "Ok, that's it, I'm pulling the plug on this one!"
                        elif Girl == StormX:
                                ch_s "I am afraid that you have overstayed your welcome."
                        elif Girl == JubesX:
                                ch_v "Fuck off then!"
                else:
                        #if she's just sad
                        $ Girl.change_stat("inhibition", 70, 5)
                        $ Girl.change_face("sad")

                        if Girl.love >= Girl.obedience:
                                #RogueX.love >= RogueX.obedience:
                                if Girl == RogueX:
                                        ch_r "I'll really miss you."
                                elif Girl == KittyX:
                                        ch_k "I was[KittyX.like]totally all-in on this!"
                                elif Girl == EmmaX:
                                        ch_e "I'll be devastated."
                                        ch_e "For at least five minutes."
                                elif Girl == LauraX:
                                        ch_l ". . ."
                                elif Girl == JeanX:
                                        ch_j "You know what. . . forget it."
                                elif Girl == StormX:
                                        ch_s "I will miss you."
                                elif Girl == JubesX:
                                        ch_v "I'll miss you. . ."
                                $ Girl.AddWord(1,0,0,"ex",0) #adds "ex" to traits
                        elif Girl.obedience >= Girl.inhibition:
                                #RogueX.obedience >= RogueX.inhibition:
                                $ Girl.change_stat("obedience", 200, -10)
                                if Girl == RogueX:
                                        ch_r "You're abandoning me."
                                elif Girl == KittyX:
                                        ch_k "I'm[KittyX.like]not sure what to do next."
                                elif Girl == EmmaX:
                                        ch_e "I suppose I'll have to make do."
                                elif Girl == LauraX:
                                        ch_l "I'll need some new options."
                                elif Girl == JeanX:
                                        ch_j "Ok, never mind then."
                                elif Girl == StormX:
                                        ch_s "I am sorry it has come to this."
                                elif Girl == JubesX:
                                        ch_v "I needed this. . ."
                                $ Girl.AddWord(1,0,0,"ex",0) #adds "ex" to traits
                        else:
                                #inbt highest
                                if Girl == RogueX:
                                        ch_r "Now who'll I fuck?"
                                elif Girl == KittyX:
                                        ch_k "I guess I'll[KittyX.like]have to find someone else to bang?"
                                elif Girl == EmmaX:
                                        ch_e "I suppose I'll have other options."
                                elif Girl == LauraX:
                                        ch_l "Ok, later."
                                elif Girl == JeanX:
                                        ch_j "Ok, that's cool."
                                elif Girl == StormX:
                                        ch_s "Well, I will find a way to move on."
                                elif Girl == JubesX:
                                        ch_v "This was fun. . ."
                                #does not add "ex" to traits because she doesn't care that much

                if Girl in Player.Harem:
                        $ Player.Harem.remove(Girl)

                $ Girl.Break[0] = 5 + Girl.Break[1] + Girl.Cheated
                $ Girl.Break[1] += 1
        #end "if you break up"


        else: #Stay together.
                $ Girl.change_face("smile")
                call Anyline(Girl,"I'm glad we could work things out. . .")
                if Girl.love >= Girl.obedience:
                        #RogueX.love >= RogueX.obedience:
                        $ Girl.change_stat("love", 200, 3)
                        if Girl == RogueX:
                                ch_r "I'd really miss you."
                        elif Girl == KittyX:
                                ch_k "I'd[KittyX.like]totes miss you!"
                        elif Girl == EmmaX:
                                ch_e "I'm in too deep, [EmmaX.Petname]."
                        elif Girl == LauraX:
                                ch_l "I. . . care about you."
                        elif Girl == JeanX:
                                ch_j "You've really grown on me."
                                $ Girl.change_face("sly")
                                ch_j "Like a one of those teacup pigs. . ."
                        elif Girl == StormX:
                                ch_s "I would miss you very much."
                        elif Girl == JubesX:
                                ch_v "I woulda missed you. . ."
                elif Girl.obedience >= Girl.inhibition:
                        #RogueX.obedience >= RogueX.inhibition:
                        if Girl == RogueX:
                                ch_r "I need you with me."
                        elif Girl == KittyX:
                                ch_k "I'm[KittyX.like]totally all-in on this."
                        elif Girl == EmmaX:
                                ch_e "I don't think I could do without you."
                        elif Girl == LauraX:
                                ch_l "I need you too much."
                        elif Girl == JeanX:
                                ch_j "I was really starting to enjoy this. . ."
                        elif Girl == StormX:
                                ch_s "I would miss you very much."
                        elif Girl == JubesX:
                                ch_v "I need this. . ."
                else:
                        #inbt highest, still a break-up, but friendly
                        if Girl == RogueX:
                                ch_r "We have fun together. Let's keep it at that."
                        elif Girl == KittyX:
                                ch_k "You[KittyX.like]really dodged a bullet on that one."
                        elif Girl == EmmaX:
                                ch_e "It's too much trouble finding another toy."
                        elif Girl == LauraX:
                                ch_l "Ok, fine."
                        elif Girl == JeanX:
                                ch_j "Yeah. . . ok."
                        elif Girl == StormX:
                                ch_s "I suppose so."
                        elif Girl == JubesX:
                                ch_v "This is fun, right?"
        $ line = 0
        return
        #End Break-up
