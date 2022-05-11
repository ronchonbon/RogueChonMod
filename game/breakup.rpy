

label Breakup(Girl=0,Other=0,Anger = 0,BO=[]): #rkeljsv
        # call Breakup(RogueX) from Chat
        # Repeats is number of times you've broken up, Other is a potential other woman, Anger is a meter that ends things at 4+

        $ Girl.AddWord(1,"breakup talk","breakup talk",0,0)

        if Girl.Break[1] > 3:
                $ Girl.FaceChange("angry")
                $ Girl.Statup("Love", 50, -5, 1)
                $ Girl.Statup("Love", 80, -10, 1)
                $ Girl.Statup("Obed", 30, -5, 1)
                $ Girl.Statup("Obed", 50, -10, 1)
                $ Girl.Statup("Inbt", 50, 3)
                $ Girl.Statup("Inbt", 80, 1)
                call AnyLine(Girl,"This is getting old.")
                $ Anger -= 1
        elif Girl.Break[1]:
                $ Girl.FaceChange("surprised")
                $ Girl.Statup("Love", 50, -5, 1)
                $ Girl.Statup("Obed", 30, -5, 1)
                $ Girl.Statup("Inbt", 80, 1)
                call AnyLine(Girl,"What, again?")
                $ Girl.FaceChange("angry")
                $ Anger += 1
        else:
                $ Girl.FaceChange("surprised")
                call AnyLine(Girl,"What?! Why?")

        $ Line = 0
        menu:
            "It's not you, it's me.":
                    $ Girl.Statup("Love", 200, -5)
                    $ Girl.Statup("Obed", 80, -5)
                    $ Girl.Statup("Inbt", 50, 3)
                    $ Girl.Statup("Inbt", 70, 1)
                    $ Girl.FaceChange("confused")

            "I just think we need a break.":
                    $ Girl.Statup("Love", 200, -5)
                    $ Girl.FaceChange("sad")

            "I've found someone else.":
                    $ Anger += 1
                    $ Girl.Statup("Love", 200, -10)
                    $ Girl.Statup("Obed", 50, 3)
                    $ Girl.Statup("Obed", 80, 3)
                    $ Girl.Statup("Inbt", 50, -5)
                    $ Girl.FaceChange("angry")
                    call AnyLine(Girl,"Who is it?")
                    menu:
                        extend ""
                        "[RogueX.Name]" if Girl != RogueX:
                                $ Other = RogueX
                        "[KittyX.Name]" if Girl != KittyX and "met" in KittyX.History:
                                $ Other = KittyX
                        "[EmmaX.Name]" if Girl != EmmaX and "met" in EmmaX.History:
                                $ Other = EmmaX
                        "[LauraX.Name]" if Girl != LauraX and "met" in LauraX.History:
                                $ Other = LauraX
                        "[JeanX.Name]" if Girl != JeanX and "met" in JeanX.History:
                                $ Other = JeanX
                        "[StormX.Name]" if Girl != StormX and "met" in StormX.History:
                                $ Other = StormX
                        "[JubesX.Name]" if Girl != JubesX and "met" in JubesX.History:
                                $ Other = JubesX
                        "I won't say.":
                                $ Girl.Statup("Love", 200, -5)
                                $ BO = ActiveGirls[:]
                                $ BO.remove(Girl)
                                $ Count = 0
                                while BO:
                                        if BO[0].SEXP > Count:
                                                # if you've boned this girl more than the last, she's the boss
                                                $ Other = BO[0]
                                                $ Count = BO[0].SEXP
                                        $ BO.remove(BO[0])
                                $ Count = 0
                                if not Other:
                                        call AnyLine(Girl,"Well it's got to be someone. . .")
                                else:
                                        call AnyLine(Girl,"It's "+Other.Name+", isn't it.")
                        "I was kidding.":
                                $ Girl.Statup("Love", 200, -5)
                                $ Girl.Statup("Obed", 50, 3)
                                $ Girl.FaceChange("angry")
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
                                $ Girl.FaceChange("normal")
                                $ Anger += 1

            "I'm just done with you.":
                    $ Girl.FaceChange("angry")
                    $ Girl.Statup("Love", 50, 3)
                    $ Girl.Statup("Love", 200, -15)
                    $ Girl.Statup("Obed", 50, 5)
                    $ Girl.Statup("Obed", 80, 5)
                    $ Girl.Statup("Obed", 200,5)
                    $ Girl.Statup("Inbt", 50, -5)
                    $ Anger += 1
        #end first question

        if not Other:
                #"denial":
                $ Girl.FaceChange("sad")
                if ApprovalCheck(Girl, 900, "O"):
                        #high obedience
                        call AnyLine(Girl,"If that's really what you want. . .")
                elif ApprovalCheck(Girl, 900, "L"):
                        #high love
                        call AnyLine(Girl,"But I love you so much!")
                elif ApprovalCheck(Girl, 900, "I") or Girl == JeanX:
                        #super casual
                        call AnyLine(Girl,"If that's how you feel. . .")
                elif ApprovalCheck(Girl, 1500):
                        #general mix
                        call AnyLine(Girl,"But we mean so much to each other!")
                else:
                        #doesn't care too much
                        call AnyLine(Girl,"Are you sure this is what you want?")
                $ Line = "bargaining"

        else:
            #if there's another girl. . .
            #GirlLikeCheck(RogueX,KittyX) if Rogue is the girl talking and Kitty is the "other girl"
            $ Cnt = int((Girl.GirlLikeCheck(Other) - 500)/2)

            if Girl.GirlLikeCheck(Other) >= 800:
                    $ Girl.Statup("Lust", 70, 5)
                    $ Girl.Statup("Obed", 50, 5)
                    $ Girl.Statup("Obed", 200, 5)
                    $ Girl.Statup("Inbt", 50, 1)
                    $ Girl.Statup("Inbt", 200, 5)
                    $ Girl.FaceChange(5,2) #blush2
                    call AnyLine(Girl,"Well, you have good tastes, at least.")
                    $ Girl.FaceChange(5,1) #blush1
            elif Girl.GirlLikeCheck(Other) >= 600:
                    $ Girl.Statup("Love", 50, -5, 1)
                    $ Girl.Statup("Love", 80, -10, 1)
                    $ Girl.Statup("Obed", 50, 5)
                    $ Girl.Statup("Obed", 200, 3)
                    if Other == EmmaX and Girl != StormX:
                            call AnyLine(Girl,"With our teacher?!")
                    if Other == StormX and Girl != EmmaX:
                            call AnyLine(Girl,"With our teacher?!")
                    elif Girl == EmmaX and Other != StormX:
                            ch_e "And I always did like her in class. . ."
                    elif Girl == StormX and Other == EmmaX:
                            ch_s "And she seemed so respectable. . ."
                    elif Girl in (EmmaX,StormX) and Other in (EmmaX,StormX):
                            call AnyLine(Girl,"You have a thing for teachers?")
                    elif Girl == LauraX:
                            ch_l "I do kinda like her."
                    elif Girl == JeanX:
                            ch_j "Well, she's not a complete bitch."
                    else:
                            call AnyLine(Girl,"With one of my friends?!")
                    $ Girl.FaceChange("normal")
                    $ Anger += 1
            elif Girl.GirlLikeCheck(Other) >= 400:
                    $ Girl.Statup("Love", 50, -3, 1)
                    $ Girl.Statup("Love", 80, -5, 1)
                    $ Girl.Statup("Obed", 80, 5)
                    $ Girl.Statup("Inbt", 50, 1)
                    $ Girl.Statup("Inbt", 80, 3)
                    call AnyLine(Girl,"You know you can do better.")
            else: #Girl.GirlLikeCheck(Other) < 400
                    $ Girl.Statup("Love", 50, -5, 1)
                    $ Girl.Statup("Obed", 80, 3)
                    $ Girl.Statup("Inbt", 50, 2)
                    $ Girl.Statup("Inbt", 80, 5)
                    $ Girl.FaceChange("angry")
                    call AnyLine(Girl,"With that skank?!")
                    $ Anger += 2

            if ApprovalCheck(Girl, 2000, Bonus = Cnt):
                    $ Girl.Statup("Lust", 70, 5)
                    $ Girl.FaceChange("sexy")
                    call AnyLine(Girl,"Why not both of us?")
                    $ Line = "threeway"
            else:
                    $ Girl.FaceChange("sad")
                    call AnyLine(Girl,"You would rather be with her than with me?")
                    menu:
                        extend ""
                        "Yes, I would.":
                                $ Girl.Statup("Love", 50, -3, 1)
                                $ Girl.Statup("Love", 80, -5, 1)
                                $ Girl.Statup("Obed", 30, 1)
                                $ Girl.Statup("Obed", 50, 1)
                                $ Anger += 1
                                $ Line = "bargaining"
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
                                        $ Line = "threeway"
                                elif Girl == JubesX:
                                        ch_v "Rough. . ."

                        "I'd rather be with both of you.":
                                $ Line = "threeway"

                        "No, I'm sorry, never mind that.":
                                $ Girl.Statup("Love", 50, -3, 1)
                                $ Girl.Statup("Obed", 80, -5)
                                call AnyLine(Girl,"Not doing yourself any favors there. . .")
                                $ Line = "bargaining"
        #end "if there's another" or not

        if Line == "threeway" and Anger < 4:
                if Girl == StormX:
                        ch_s "So would she be fine with you dating us both?"
                else:
                        call AnyLine(Girl,"Date us both at once? What does she think about that?")
                menu Breakup_Threeway_Offer:
                        extend ""
                        "She said it would be ok with her." if "poly "+ Girl.Tag in Other.Traits or Girl.Tag+"Yes" in Player.Traits:
                                #"poly Rogue" in KittyX.Traits, or "KittyYes" in Player.Traits
                                if ApprovalCheck(Girl, 1800, Bonus = Cnt):
                                        $ Girl.FaceChange("smile", 1)
                                        $ Girl.Statup("Lust", 70, 5)
                                        $ Girl.Statup("Obed", 50, 5)
                                        $ Girl.Statup("Obed", 80, 3)
                                        $ Girl.Statup("Inbt", 50, 3)
                                        $ Girl.Statup("Inbt", 80, 1)
                                        if Girl.GirlLikeCheck(Other) < 400:
                                                $ Girl.FaceChange("angry")
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
                                        elif Girl.GirlLikeCheck(Other) >= 700 or Girl == JeanX:
                                                $ Girl.FaceChange("sexy")
                                                call AnyLine(Girl,"I have to say I've kind of been thinking about it myself.")
                                        elif Girl.Love >= Girl.Obed:
                                                $ Girl.FaceChange("sad")
                                                call AnyLine(Girl,"Just so long as we can be together, I can share.")
                                        else:
                                                #Inbt highest
                                                call AnyLine(Girl,"If she's in, I am.")

                                        $ Girl.AddWord(1,0,0,"poly "+Other.Tag,0) #adds "poly Other" to traits
                                else:
                                        $ Anger += 2
                                        $ Girl.Statup("Love", 50, -10, 1)
                                        $ Girl.Statup("Love", 80, -15, 1)
                                        $ Girl.Statup("Obed", 50, 3)
                                        $ Girl.Statup("Obed", 80, 3)
                                        $ Girl.Statup("Inbt", 50, 5)
                                        $ Girl.Statup("Inbt", 80, 3)
                                        $ Girl.FaceChange("angry", 1)
                                        call AnyLine(Girl,"Well maybe she did, but I don't want to share." )
                                        $ Line = "bargaining"
                                        if Girl == StormX:
                                                $ Line = "breakup"
                        #End "she said it'd be ok.

                        "I have no idea.": #if not KittyX.Break[0]:
                                $ Line = "ask " + Other.Tag #"ask Kitty"

                        "She's not into it.": #if KittyX.Break[0]:
                                if Girl.GirlLikeCheck(Other) >= 700:
                                        $ Girl.Statup("Love", 200, -5)
                                elif Girl.GirlLikeCheck(Other) <= 400:
                                        $ Girl.Statup("Love", 90, 5)
                                call AnyLine(Girl,"Well then why even bring it up?")


                        "Well, even if she doesn't agree. . .":
                                $ Line = "ask " + Other.Tag #"ask Kitty"
                                if Girl.GirlLikeCheck(Other) >= 700:
                                        $ Girl.FaceChange("angry")
                                        $ Girl.Statup("Love", 200, -5)
                                elif Girl.GirlLikeCheck(Other) <= 400:
                                        $ Girl.Statup("Love", 90, 5)

                if Line == "ask " + Other.Tag and Girl.GirlLikeCheck(Other) >= 700:
                                #if previous responses had her wanting to ask the other girl about it
                                call AnyLine(Girl,"You want me to ask her for you?")
                                menu:
                                    extend ""
                                    "Yes, that'd be a good idea.":
                                            $ Girl.Statup("Love", 90, 5)
                                            $ Girl.Statup("Obed", 70, 1)
                                            $ Girl.Statup("Inbt", 80, 5)
                                            $ Girl.FaceChange("sexy")
                                            call AnyLine(Girl,"I guess I could.")
                                            $ Girl.AddWord(1,0,0,"ask "+Other.Tag,0) #adds "ask Other" to traits
                                            $ Girl.AddWord(1,0,0,"poly "+Other.Tag,0) #adds "poly Other" to traits
                                    "No, let's just keep it under cover.":
                                            $ Girl.Statup("Love", 50, -5, 1)
                                            $ Girl.Statup("Love", 80, -5, 1)
                                            $ Girl.Statup("Obed", 80, 5)
                                            $ Girl.Statup("Inbt", 50, 3)
                                            call AnyLine(Girl,"I don't know. . .")

                if Line == "breakup":
                        pass
                elif Line != "bargaining" and "poly "+ Other.Tag not in Girl.Traits:
                        #if the answer is not "bargaining," but also the girl has not agreed yet. . .
                        #"poly Kitty" not in RogueX.Traits:
                        if "ask "+ Other.Tag not in Girl.Traits and not ApprovalCheck(Girl, 1800, Bonus = -(int((Girl.GirlLikeCheck(Other) - 600)/2))):
                                #"ask Kitty" not in RogueX.Traits
                                #checks if Girl likes you more than Other
                                $ Girl.Statup("Love", 50, -5, 1)
                                $ Girl.Statup("Obed", 80, -10, 1)
                                $ Girl.Statup("Inbt", 50, 5)
                                $ Girl.FaceChange("angry", 1)
                                if not ApprovalCheck(Girl, 1800):
                                        call AnyLine(Girl,"Maybe I don't like you that much either.")
                                else:
                                        $ Girl.Statup("Love", 80, -10, 1)
                                        $ Girl.Statup("Obed", 50, -5, 1)
                                        if Girl == EmmaX and Other != StormX:
                                                ch_e "I'd rather not be dallying with another teacher's boyfriend. . ."
                                        elif Girl == EmmaX:
                                                ch_e "I'd rather not be dallying with a student's boyfriend. . ."
                                        elif Girl == StormX:
                                                ch_s "I would rather not creep around like that."
                                        elif Girl == JeanX:
                                                ch_j "I don't know, shes a little boring. . ."
                                        elif Other == EmmaX:
                                                call AnyLine(Girl,"I don't want to get caught with the teacher's boyfriend!")
                                        else:
                                                call AnyLine(Girl,"I'm not really cool with that, "+Other.Name+"'s a friend of mine." )
                                $ Anger += 1
                                if Girl != StormX:
                                        $ Line = "bargaining"
                        else:
                                #if she agrees to polygamy
                                $ Girl.Statup("Obed", 30, 5)
                                $ Girl.Statup("Obed", 50, 3)
                                $ Girl.Statup("Inbt", 50, 5)
                                $ Girl.Statup("Inbt", 80, 1)
                                $ Girl.FaceChange("sad")
                                if Girl.GirlLikeCheck(Other) < 400:
                                        $ Girl.FaceChange("angry")
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
                                elif Girl.GirlLikeCheck(Other) >= 700:
                                        $ Girl.FaceChange("sexy")
                                        call AnyLine(Girl,"I have to say I've kind of been thinking about it myself.")
                                elif Girl.Love >= Girl.Obed:
                                        #RogueX.Love >= RogueX.Obed:
                                        $ Girl.FaceChange("sad")
                                        call AnyLine(Girl,"Just so long as we can be together, I can share.")
                                else:
                                        #Inbt highest
                                        call AnyLine(Girl,"If she's in, I am.")
                                $ Girl.AddWord(1,0,0,"poly "+Other.Tag,0) #adds "poly Other" to traits
                                if "ask "+ Other.Tag in Girl.Traits:
                                        #"ask Kitty" in RogueX.Traits:
                                        call AnyLine(Girl,"I'll talk to "+Other.Name+" about it.")
                                else:
                                        $ Girl.FaceChange("sad")
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

                                        if Girl.GirlLikeCheck(Other) >= 800 and Girl != JeanX:
                                                call AnyLine(Girl, "Please talk to "+Other.Name+" about sharing you openly though.")
                                        elif Girl.GirlLikeCheck(Other) >= 500 and Girl != JeanX:
                                                call AnyLine(Girl,"I really don't like going behind "+Other.Name+"'s back though.")
                                        else:
                                                call AnyLine(Girl,"Might be fun, sneaking around behind her back.")
                #End Threeway

        if Line == "bargaining" and Anger < 4:
                $ Girl.FaceChange("sad")
                call AnyLine(Girl,"You're sure there's no way I could convince you to stay?")
                menu Breakup_Bargaining:
                    extend ""
                    "Sorry, I've changed my mind.":
                            $ Girl.Statup("Obed", 80, 5)
                            if ApprovalCheck(Girl, 1500):
                                    $ Line = "makeup"
                                    $ Girl.Statup("Love", 80, 5)
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
                                    $ Line = "breakup"
                                    $ Girl.Statup("Love", 90, -5)
                                    $ Girl.Statup("Obed", 80, -5)
                                    $ Girl.Statup("Inbt", 80, 10)
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
                            $ Girl.Statup("Obed", 80, 5)
                            $ Line = "breakup"
                    "Well, you could do something for me. . .[[sex menu]":
                            $ Girl.AddWord(1,"bargainsex",0,0,0) #adds "bargainsex" to recent
                            $ Girl.Statup("Obed", 80, 3)
                            $ temp_modifier = 50
                            $ MultiAction = 0
                            call expression Girl.Tag + "_SMenu" #call Rogue_SexMenu
                            $ MultiAction = 1
                            menu:
                                "Ok, I guess we can give it another shot.":
                                        $ Girl.Statup("Love", 80, 3)
                                        $ Girl.Statup("Obed", 80, 5)
                                        $ Line = "makeup"
                                        $ Girl.FaceChange("smile")

                                "That was nice, but we're still over.":
                                        $ Girl.FaceChange("angry")
                                        $ Girl.Statup("Love", 50, -5, 1)
                                        $ Girl.Statup("Love", 80, -10, 1)
                                        $ Girl.Statup("Obed", 50, 15)
                                        $ Girl.Statup("Obed", 80, 10)
                                        $ Line = "breakup"
                                        $ Anger += 4

                    "Maybe if we brought someone else into this relationship?" if not Other and "bargainthreeway" not in Girl.RecentActions:
                            # if you haven't just tried this
                            $ Girl.AddWord(1,"bargainthreeway",0,0,0) #adds "bargainthreeway" to recent
                            call AnyLine(Girl,"Who?")
                            menu:
                                extend ""
                                "[RogueX.Name]?" if Girl != RogueX:
                                        $ Other = RogueX
                                "[KittyX.Name]?" if Girl != KittyX and "met" in KittyX.History:
                                        $ Other = KittyX
                                "[EmmaX.Name]?" if Girl != EmmaX and "met" in EmmaX.History:
                                        $ Other = EmmaX
                                "[LauraX.Name]?" if Girl != LauraX and "met" in LauraX.History:
                                        $ Other = LauraX
                                "[JeanX.Name]?" if Girl != JeanX and "met" in JeanX.History:
                                        $ Other = JeanX
                                "[StormX.Name]?" if Girl != StormX and "met" in StormX.History:
                                        $ Other = StormX
                                "[JubesX.Name]?" if Girl != JubesX and "met" in JubesX.History:
                                        $ Other = JubesX

                                "Up to you?":
                                        $ Girl.FaceChange("confused")
                                        #picks her favorite girl. . .
                                        $ BO = ActiveGirls[:]
                                        $ BO.remove(Girl)
                                        $ Count = 0
                                        while BO:
                                                if Girl.GirlLikeCheck(BO[0]) > Count:
                                                        # if she likes this girl more than the last, she's the pick
                                                        $ Other = BO[0]
                                                        $ Count = Girl.GirlLikeCheck(BO[0])
                                                $ BO.remove(BO[0])
                                        $ Count = 0
                                        call AnyLine(Girl,Other.Name+"?")

                                "Never mind, silly question.":
                                        $ Girl.Statup("Love", 200, -10)
                                        $ Girl.Statup("Obed", 50, -10, 1)
                                        $ Anger += 1
                                        $ Girl.FaceChange("angry")
                                        jump Breakup_Bargaining

                            if Other:
                                    $ Girl.FaceChange("confused")
                                    jump Breakup_Threeway_Offer

                if Anger < 3 and Line != "breakup" and Line != "makeup":
                        #if no decision and she's not pissed yet, loop
                        if Girl == StormX:
                                $ Line = "breakup"
                        else:
                                jump Breakup_Bargaining
        # End Bargaining



        if Line == "breakup" or Anger >= 4:
                if Anger >= 4:
                        #if she's pissed
                        $ Girl.FaceChange("angry")
                        $ Girl.Statup("Love", 60, -10, 1)
                        $ Girl.Statup("Obed", 50, -5)
                        $ Girl.Statup("Inbt", 70, 5)
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
                        $ Girl.Statup("Inbt", 70, 5)
                        $ Girl.FaceChange("sad")

                        if Girl.Love >= Girl.Obed:
                                #RogueX.Love >= RogueX.Obed:
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
                        elif Girl.Obed >= Girl.Inbt:
                                #RogueX.Obed >= RogueX.Inbt:
                                $ Girl.Statup("Obed", 200, -10)
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
                $ Girl.FaceChange("smile")
                call AnyLine(Girl,"I'm glad we could work things out. . .")
                if Girl.Love >= Girl.Obed:
                        #RogueX.Love >= RogueX.Obed:
                        $ Girl.Statup("Love", 200, 3)
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
                                $ Girl.FaceChange("sly")
                                ch_j "Like a one of those teacup pigs. . ."
                        elif Girl == StormX:
                                ch_s "I would miss you very much."
                        elif Girl == JubesX:
                                ch_v "I woulda missed you. . ."
                elif Girl.Obed >= Girl.Inbt:
                        #RogueX.Obed >= RogueX.Inbt:
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
        $ Line = 0
        return
        #End Break-up
