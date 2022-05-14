init python:

    def ApprovalCheck(Chr = 0, T = 1000, Type = "LOI", Spread = 150, TmpM = 1, TabM = 0, C = 1, Bonus = 0, Loc = 0, Check=0, Alt=[[],0]):
            # $ Count = ApprovalCheck(Rogue,125,"L")
            # T is the value being checked against, Type is the LOI condition in play, Spread is the difference between basic approval and high approval
            # TmpM is temp_modifier multiplier, TabM is the taboo modifier, C is cologne modifiers, Bonus is a random bonus applied, and Loc is the girl's location
            #figure out a way to send a matrix variable for altering the results based on character Alt=[[RogueX,KittyX],800]

            if Chr not in TotalGirls: #should remove "character don't exist" errors
                return 0

            while Alt[0]:
                    #if there is an alternate character option. . .
                    if Chr in Alt[0]:
                            T = Alt[1] if Alt[1] else T
                    Alt[0].remove(Alt[0][0])

            L = Chr.Love
            O = Chr.Obed
            I = Chr.Inbt
            LocalTaboo = Chr.Taboo
            Loc = Chr.Loc if not Loc else Loc

            if Chr.Tag == "Jean" and (O <= 800 or JeanX.Taboo):
                    # Reduces effective value of Inhibition by 500 to a minimum of 0.
                    I = (I - JeanX.IX) #IX is a value of up to 500

            if Loc == bg_current and C:
                    #Bumps stats based on colognes
                    if Chr == LauraX:
                            if "mandrill" in Player.Traits:
                                    if L <= 400:
                                        L += 600
                                    else:
                                        L = 1200
                                    if "drugged" not in Chr.Traits:
                                            Chr.Traits.append("drugged")
                            elif "purple" in Player.Traits:
                                    if O <= 400:
                                        O += 600
                                    else:
                                        O = 1200
                                    if "drugged" not in Chr.Traits:
                                            Chr.Traits.append("drugged")
                            elif "corruption" in Player.Traits:
                                    if I <= 400:
                                        I += 600
                                    else:
                                        I = 1200
                                    if "drugged" not in Chr.Traits:
                                            Chr.Traits.append("drugged")
                    else:
                            if "mandrill" in Player.Traits:
                                    if L <= 500:
                                        L += 500
                                    else:
                                        L = 1000
                            elif "purple" in Player.Traits:
                                    if O <= 500:
                                        O += 500
                                    else:
                                        O = 1000
                            elif "corruption" in Player.Traits:
                                    if I <= 500:
                                        I += 500
                                    else:
                                        I = 1000

            if Type == "LOI":
                    LocalTaboo = LocalTaboo * 10
                    Localtemp_modifier = temp_modifier * 10

            elif Type == "LO":                      #40 -> 240
                    #culls unwanted parameters.
                    #These bits multiply everything from the 0-300 range to the 0-3000 range
                    I = 0
                    LocalTaboo = LocalTaboo * 6
                    Localtemp_modifier = temp_modifier * 6
            elif Type == "OI":
                    L = 0
                    LocalTaboo = LocalTaboo * 6
                    Localtemp_modifier = temp_modifier * 6
            elif Type == "LI":
                    O = 0
                    LocalTaboo = LocalTaboo * 6
                    Localtemp_modifier = temp_modifier * 6

            elif Type == "L":                       #40 -> 120
                    O = 0
                    I = 0
                    LocalTaboo = LocalTaboo * 3
                    Localtemp_modifier = temp_modifier * 3
            elif Type == "O":
                    L = 0
                    I = 0
                    LocalTaboo = LocalTaboo * 3
                    Localtemp_modifier = temp_modifier * 3
            elif Type == "I":
                    O = 0
                    L = 0
                    LocalTaboo = LocalTaboo * 3
                    Localtemp_modifier = temp_modifier * 3

            else:
                    LocalTaboo = LocalTaboo * 10         #40 -> 400
                    Localtemp_modifier = temp_modifier * 10

            TabM = 0 if TabM <= 0 else TabM #test this, makes sure TabM is positive

            if Check:
                    #this returns the actual value of the tested stat.
                    Check = (L + O + I + Bonus + (TmpM * Localtemp_modifier) - (TabM * LocalTaboo))
                    return Check

            if (L + O + I + Bonus + (TmpM * Localtemp_modifier) - (TabM * LocalTaboo)) >= (T + (2 * Spread)):
                    #She passes and loves it
                    return 3
            elif (L + O + I + Bonus + (TmpM * Localtemp_modifier) - (TabM * LocalTaboo)) >= (T + Spread):
                    #She passes
                    return 2
            elif (L + O + I + Bonus + (TmpM * Localtemp_modifier) - (TabM * LocalTaboo)) >= T:
                    #She doesn't really want to, but can be convinced
                    return 1
            else:
                    return 0

    def AloneCheck(Girl=0,BO=[]):
            # returns a positive value if alone
            # if Girl, it checks if she's the only one in the room
            BO = TotalGirls[:]
            if Girl and Girl in TotalGirls:
                    BO.remove(Girl)
            while BO:
                    if BO[0].Loc == bg_current:
                            return 0
                    BO.remove(BO[0])
            return 1

    def GirlCheck(Check=0,Local=0,BO=[]):
            #checks whether the indicated girl is available for this activity
            # $ Girl = GirlCheck(Girl,1)
            global Ch_Focus
            if Check in TotalGirls and (not Local or bg_current == Check.Loc):
                        #if the sent girl is valid and the game does not care about location
                        #or if the sent girl is valid and the girl is nearby
                        return Check
            elif bg_current == Ch_Focus.Loc:
                        #if this sent girl is in the room and focal, make her the choice.
                        return Ch_Focus
            else:
                #If the sent girl is invalid, and the focal girl is not local,
                #search all girls for one that is local, and make her the focal girl
                BO = TotalGirls[:]
                while BO:
                        if bg_current == BO[0].Loc:
                                #if this current girl is in the room, make her the choice.
                                #renpy.call("Shift_Focus",BO[0],from_current=True)
                                Ch_Focus = BO[0]
                                return BO[0]
                        BO.remove(BO[0])
            ch_u("Tell Oni, no appropriate character was found.", interact=True)
            return Ch_Focus

label Girl_First_Peen(Girl = 0, Silent = 0, Undress = 0, Second = 0, React = 0):  #rkeljsv
        #checked each time she sees your cock  ## call Girl_First_Peen(RogueX,0,1)
        #if Silent it doesn't say anything
        #if Undress then you get nude
        #if Secondary then this is the second girl to see it.
        # React 0 if other girl didn't comment,
        # 1 = if the other girl commented, 2 = didn't like it

        if Girl.Loc != bg_current:
                    if Partner == Girl:
                            $ Partner = 0
                    return
        if "cockout" in Player.RecentActions and "peen" in Girl.RecentActions:
                    #If the cock is already out and she's seen it, return
                    return

        if "unseen" in Girl.RecentActions:
                    #if she hasn't noticed you, she won't notice this, yet.
                    return

        $ Girl.RecentActions.append("peen")
        $ Girl.DailyActions.append("peen")
        $ Girl.SeenPeen += 1
        $ Girl.Statup("Inbt", 30, 2)
        $ Girl.Statup("Inbt", 80, 1)

        if Second:
                #If another girl commented on it first. . .
                if Girl.SeenPeen == 1:
                                $ Girl.FaceChange("surprised", 2)
                                if Girl == RogueX:
                                        ch_r "Wow, yeah, that's pretty nice. . ."
                                elif Girl == KittyX:
                                        ch_k "Oh, wow, you aren't kidding. . ."
                                elif Girl == EmmaX:
                                        $ Girl.FaceChange("smirk", 2, Eyes = "down")
                                        ch_e "My, that certainly is an impressive specimen. . ."
                                elif Girl == LauraX:
                                        $ Girl.FaceChange("smirk", 2, Eyes = "down")
                                        ch_l "Huh, that's a pretty good one you got there. . ."
                                elif Girl == JeanX:
                                        $ Girl.FaceChange("smirk", 2, Eyes = "down")
                                        ch_j "Yeah, looking good. . ."
                                elif Girl == StormX:
                                        $ Girl.FaceChange("smirk", 2, Eyes = "down")
                                        ch_s "Yes, that is impressive. . ."
                                elif Girl == JubesX:
                                        $ Girl.FaceChange("smirk", 2, Eyes = "down")
                                        ch_v "Oh, wow, yeah. . ."
                                $ Girl.FaceChange("bemused", 1)
                elif Second == 1:
                        # The other girl liked it
                        if not ApprovalCheck(Girl, 800) and not ApprovalCheck(Girl, 500, "I"):
                                $ Girl.FaceChange("sad", 1)
                                if Girl == RogueX:
                                        ch_r "If you're inta that sorta thing. . ."
                                elif Girl == KittyX:
                                        ch_k "I mean I guess. . ."
                                elif Girl == EmmaX:
                                        ch_e "I suppose you haven't had a lot of experience. . ."
                                elif Girl == LauraX:
                                        ch_l "I guess . ."
                                elif Girl == JeanX:
                                        ch_j "Yeah, it's ok. . ."
                                elif Girl == StormX:
                                        ch_s "I suppose it could be. . ."
                                elif Girl == JubesX:
                                        ch_v "I guess. . ."
                        else:
                                $ Girl.FaceChange("bemused", 1)
                                if Girl == RogueX:
                                        ch_r "Yeah, it really is a beauty. . ."
                                elif Girl == KittyX:
                                        ch_k "I know, right?!"
                                elif Girl == EmmaX:
                                        ch_e "Yes, it caught me off guard as well. . ."
                                elif Girl == LauraX:
                                        ch_l "Yeah, nice, isn't it. . ."
                                elif Girl == JeanX:
                                        ch_j "Right?"
                                elif Girl == StormX:
                                        ch_s "I thought so as well."
                                elif Girl == JubesX:
                                        ch_v "Right?"
                elif Second == 2:
                        # The other girl didn't like it
                        if not ApprovalCheck(Girl, 800) and not ApprovalCheck(Girl, 500, "I"):
                                $ Girl.FaceChange("sad", 1)
                                if Girl == RogueX:
                                        ch_r "Right, whatever. . ."
                                elif Girl == KittyX:
                                        ch_k "So over it. . ."
                                elif Girl == EmmaX:
                                        ch_e "A fine judge of quality. . ."
                                elif Girl == LauraX:
                                        ch_l "I guess. . ."
                                elif Girl == JeanX:
                                        ch_j "Yeah. . ."
                                elif Girl == StormX:
                                        ch_s "True. . ."
                                elif Girl == JubesX:
                                        ch_v "I guess. . ."
                        else:
                                $ Girl.FaceChange("confused", 1)
                                if Girl == RogueX:
                                        ch_r "Well I liked it. . ."
                                        $ Girl.FaceChange("sexy", 1)
                                elif Girl == KittyX:
                                        ch_k "Come on, it's really cute!"
                                        $ Girl.FaceChange("smile", 1)
                                elif Girl == EmmaX:
                                        ch_e "You just don't appreciate the finer things. . ."
                                        $ Girl.FaceChange("sly",0)
                                elif Girl == LauraX:
                                        ch_l "Aw, come on, it's not that bad. . ."
                                        $ Girl.FaceChange("sly",0)
                                elif Girl == JeanX:
                                        ch_j "I mean, I've seen worse. . ."
                                        $ Girl.FaceChange("sly",0)
                                elif Girl == StormX:
                                        ch_s "It's far from the worst I've seen. . ."
                                        $ Girl.FaceChange("sly",0)
                                elif Girl == JubesX:
                                        ch_v "More for me, I guess. . ."
                                        $ Girl.FaceChange("sly",0)
                $ Silent = 1

        if Undress:
                    $ Player.AddWord(1,"naked")
        if not Silent:
            if "cockout" in Player.RecentActions:
                    $ Girl.FaceChange("down", 2)
                    "[Girl.Name] glances down at your exposed cock."
            elif React:
                    #If called by a sex dialog
                    "[Girl.Name] reaches for your pants and pulls out your cock."
            elif Undress:
                    "You strip nude."
            else:
                    "You whip your cock out."
            $ Player.AddWord(1,"cockout")
            if not Girl.Forced and not React and Taboo > 20 and (not ApprovalCheck(Girl, 1500) or Girl.SEXP < 10) and bg_current != "bg showerroom" and Girl not in (JeanX,StormX):
                #if it's a semi-public space that isn't the showers, and she is not down with this. . .
                if not ApprovalCheck(Girl, 800) and not ApprovalCheck(Girl, 500, "I"):
                        #If the girl is very not into it. . .
                        if Girl == EmmaX and ("detention" in Girl.RecentActions or "classcaught" in Girl.RecentActions):
                            #special exceptions for detention and classcaught events
                            $ Girl.FaceChange("confused", Eyes="down")
                            ch_e "Mmm?"
                            $ Girl.FaceChange("surprised", Eyes="squint")
                            if Girl.SeenPeen == 1:
                                    $ Girl.Statup("Love", 30, 10)
                                    $ Girl.Statup("Love", 90, 5)
                                    $ Girl.Statup("Obed", 50, 20)
                                    $ Girl.Statup("Inbt", 60, 30)
                            else:
                                    $ Girl.Statup("Love", 90, 2)
                                    $ Girl.Statup("Obed", 50, 3)
                                    $ Girl.Statup("Inbt", 60, 5)
                            ch_e "Well I suppose I can make an exception in this case."
                            $ React = 1
                        else:
                            #If the girl is very not into it. . .
                            $ Girl.FaceChange("surprised", 2)
                            if Girl == RogueX:
                                    ch_r "What the hell?"
                            elif Girl == KittyX:
                                    ch_k "Huh?!"
                            elif Girl == EmmaX:
                                    $ Girl.Eyes = "down"
                                    ch_e "Mmm?"
                            elif Girl == LauraX:
                                    $ Girl.Eyes = "down"
                                    ch_l "Mmm?"
                            elif Girl == JubesX:
                                    $ Girl.Eyes = "down"
                                    ch_v "Hey. . ."
                                    $ Girl.Eyes = "squint"
                                    ch_v "What's that about?"
                            $ Girl.FaceChange("angry", 1)
                            $ Girl.RecentActions.append("angry")
                            $ Girl.DailyActions.append("angry")
                            $ React = 2
                            if Girl.SeenPeen == 1:
                                        $ Girl.Statup("Love", 90, -20)
                                        $ Girl.Statup("Obed", 50, 30)
                                        $ Girl.Statup("Inbt", 60, 20)
                            else:
                                #if this is the second time you've done this today. . .
                                if Girl == RogueX:
                                        ch_r "What is {i}wrong{/i} with you?"
                                elif Girl == KittyX:
                                        ch_k "Dude, seriously, you've got a problem!"
                                elif Girl == EmmaX:
                                        ch_e "[Girl.Petname]! We are going to have to work through this. . . problem of yours."
                                elif Girl == LauraX:
                                        ch_l "Dude, not cool."
                                elif Girl == JubesX:
                                        ch_v "Keep it in your pants. . ."
                                if Girl.DailyActions.count("peen") >= 2:
                                        #if she's seen more than one peen today
                                        $ Girl.Statup("Love", 90, -1)
                                        $ Girl.Statup("Obed", 50, 1)
                                        $ Girl.Statup("Inbt", 60, 2)
                                else:
                                        $ Girl.Statup("Love", 90, -5)
                                        $ Girl.Statup("Obed", 50, 10)
                                        $ Girl.Statup("Inbt", 60, 10)
                #end if bg_current != "bg showerroom" and not ApprovalCheck(Girl, 800) and not ApprovalCheck(Girl, 500, "I"):
                else:
                            #if ApprovalCheck is 800-1500 and not ApprovalCheck(Girl, 500, "I"):
                            $ Girl.FaceChange("surprised", 2)
                            if Girl == RogueX:
                                    ch_r "What are you- you should really put that thing away!"
                            elif Girl == KittyX:
                                    ch_k "Um, you should[Girl.like]put that away in public."
                            elif Girl == EmmaX:
                                    ch_e "You really should be careful where you display that thing."
                            elif Girl == LauraX:
                                    ch_l "I think there's a time and place for that sort of thing."
                            elif Girl == JubesX:
                                    ch_v "Um, maybe you should put that away?"
                            $ Girl.FaceChange("bemused", 1)
                            if Girl.SeenPeen == 1:
                                    if Girl == RogueX:
                                            ch_r "I mean. . . no, definitely put that away!"
                                    elif Girl == KittyX:
                                            ch_k "Or[Girl.like]maybe. . ."
                                    elif Girl == EmmaX:
                                            $ Girl.Eyes = "down"
                                            ch_e ". . . impressive though it may be. . ."
                                    elif Girl == LauraX:
                                            ch_l ". . . not that I mind, myself. . ."
                                    elif Girl == JubesX:
                                            ch_v "Or. . . not. . ."
                                    $ Girl.Statup("Love", 90, 20)
                                    $ Girl.Statup("Obed", 50, 20)
                                    $ Girl.Statup("Inbt", 60, 30)
                            $ React = 2

                #end if not Girl.Forced and not React and Taboo > 20 and (not ApprovalCheck(Girl, 1500) or Girl.SEXP < 10) and bg_current != "bg showerroom" and Girl != JeanX:
            elif Girl.SeenPeen > 10:
                        #if it's been more than 10 times, return
                        return 0
            elif ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "L"):
                    #She basically likes it
                    $ Girl.FaceChange("sly",1)
                    if Girl.SeenPeen == 1:
                            $ Girl.FaceChange("surprised",2)
                            if Girl == RogueX:
                                    ch_r "Whoa, I didn't know they looked so big up close."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Love", 90, 5)
                            elif Girl == KittyX:
                                    $ Girl.FaceChange("surprised",2)
                                    ch_k "That's. . . impressive."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Love", 90, 3)
                            elif Girl == EmmaX:
                                    $ Girl.FaceChange("surprised",1, Eyes="down")
                                    ch_e "Well that's certainly an interesting specimen."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Love", 50, 5)
                                    $ Girl.Statup("Love", 90, 10)
                            elif Girl == LauraX:
                                    $ Girl.FaceChange("surprised",1, Eyes="down")
                                    ch_l "Huh, that's a pretty good one you got there. . ."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Love", 50, 5)
                                    $ Girl.Statup("Love", 90, 10)
                            elif Girl == JeanX:
                                    $ Girl.FaceChange("confused",1, Eyes="down",Mouth="smile")
                                    ch_j "Well, what do we have here. . ."
                                    $ Girl.FaceChange("bemused",1)
                                    ch_j "Preeety nice there, [Girl.Petname]."
                                    $ Girl.Statup("Love", 50, 5)
                                    $ Girl.Statup("Love", 90, 10)
                                    $ Girl.Statup("Obed", 80, 3)
                            elif Girl == StormX:
                                    $ Girl.FaceChange("confused",1, Eyes="down")
                                    ch_s "Hmm. . . that is a lovely one."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Love", 50, 5)
                                    $ Girl.Statup("Love", 90, 5)
                                    $ Girl.Statup("Inbt", 60, 2)
                            elif Girl == JubesX:
                                    $ Girl.FaceChange("surprised",2, Eyes="down")
                                    ch_v "Oh. . . nice."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 80, 3)
                                    $ Girl.Statup("Obed", 80, 1)
                                    $ Girl.Statup("Inbt", 60, 4)
                    elif Girl.SeenPeen == 2:
                            if Girl == RogueX:
                                    ch_r "That thing sure is impressive."
                                    $ Girl.Statup("Obed", 50, 5)
                            elif Girl == KittyX:
                                    ch_k "I can't get over that."
                                    $ Girl.Statup("Obed", 50, 7)
                            elif Girl == EmmaX:
                                    $ Girl.Eyes = "down"
                                    ch_e "Oh, hello again."
                                    $ Girl.Statup("Inbt", 50, 5)
                            elif Girl == LauraX:
                                    $ Girl.Eyes = "down"
                                    ch_l "Oh, there it is."
                                    $ Girl.Statup("Obed", 50, 2)
                                    $ Girl.Statup("Inbt", 50, 3)
                            elif Girl == JeanX:
                                    $ Girl.Eyes = "down"
                                    ch_j "Still pretty impressive. . ."
                                    $ Girl.Statup("Love", 90, 3)
                                    $ Girl.Statup("Obed", 80, 3)
                            elif Girl == StormX:
                                    $ Girl.Eyes = "down"
                                    ch_s "Hmm. . ."
                                    $ Girl.Statup("Inbt", 50, 2)
                            elif Girl == JubesX:
                                    $ Girl.FaceChange("sly",1, Eyes="down")
                                    ch_v "Hello again."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Obed", 80, 1)
                                    $ Girl.Statup("Inbt", 60, 1)
                    elif Girl.SeenPeen == 5:
                            if Girl == RogueX:
                                    ch_r "I certainly appreciate that guy."
                                    $ Girl.Statup("Inbt", 60, 5)
                            elif Girl == KittyX:
                                    ch_k "There it is."
                                    $ Girl.Statup("Inbt", 60, 5)
                            elif Girl == EmmaX:
                                    ch_e "Yes, we've seen that before."
                                    $ Girl.Statup("Obed", 60, 7)
                            elif Girl == LauraX:
                                    ch_l "Yeah, I've seen that one."
                                    $ Girl.Statup("Obed", 60, 4)
                                    $ Girl.Statup("Inbt", 60, 3)
                            elif Girl == JeanX:
                                    $ Girl.Eyes = "down"
                                    ch_j "Nice. . ."
                                    $ Girl.Statup("Love", 90, 3)
                                    $ Girl.Statup("Obed", 80, 2)
                            elif Girl == StormX:
                                    ch_s ". . ."
                                    $ Girl.Statup("Inbt", 60, 5)
                            elif Girl == JubesX:
                                    $ Girl.FaceChange("sly",1, Eyes="down")
                                    ch_v "Hey there. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 80, 1)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 2)
                    elif Girl.SeenPeen == 10:
                            if Girl == RogueX:
                                    ch_r "I never get tired of seeing that."
                                    $ Girl.Statup("Love", 90, 10)
                            elif Girl == KittyX:
                                    ch_k "So beautiful."
                                    $ Girl.Statup("Obed", 80, 10)
                                    $ Girl.Statup("Inbt", 60, 3)
                            elif Girl == EmmaX:
                                    $ Girl.Eyes = "down"
                                    ch_e "I do appreciate some of your features."
                                    $ Girl.Statup("Obed", 80, 5)
                                    $ Girl.Statup("Inbt", 60, 10)
                            elif Girl == LauraX:
                                    $ Girl.Eyes = "down"
                                    ch_l "I don't get tired of that view."
                                    $ Girl.Statup("Obed", 80, 8)
                                    $ Girl.Statup("Inbt", 60, 7)
                            elif Girl == JeanX:
                                    $ Girl.Eyes = "down"
                                    ch_j "Thanks for that. . ."
                                    $ Girl.Statup("Love", 90, 10)
                                    $ Girl.Statup("Obed", 80, 8)
                            elif Girl == StormX:
                                    $ Girl.Eyes = "down"
                                    ch_s "Well, I do enjoy that one."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Love", 90, 5)
                                    $ Girl.Statup("Inbt", 60, 2)
                            elif Girl == JubesX:
                                    $ Girl.FaceChange("confused",1, Eyes="down")
                                    ch_v "Kinda. . . hypnotic. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 80, 1)
                                    $ Girl.Statup("Obed", 80, 3)
                                    $ Girl.Statup("Inbt", 60, 2)
                    $ React = 1
            else:
                    #she doesn't like it much
                    $ Girl.FaceChange("sad",1)
                    if Girl.SeenPeen == 1:
                            $ Girl.FaceChange("perplexed",1 )
                            $ Girl.Eyes = "down"
                            if Girl == RogueX:
                                    ch_r "Well, I guess that's impressive. What do you plan to do with it?"
                                    $ Girl.Statup("Obed", 50, 5)
                                    $ Girl.Statup("Inbt", 60, 5)
                            elif Girl == KittyX:
                                    ch_k "Well that happened. . ."
                            elif Girl == EmmaX:
                                    ch_e "Are you aware that your dick is out?"
                                    $ Girl.Statup("Obed", 50, 2)
                            elif Girl == LauraX:
                                    ch_l "Your dick is out."
                                    $ Girl.Statup("Inbt", 60, 2)
                            elif Girl == JeanX:
                                    ch_j "Hey, you're penis is out."
                                    $ Girl.Statup("Obed", 80, 4)
                                    $ Girl.Statup("Inbt", 70, 4)
                            elif Girl == StormX:
                                    ch_s "Apparently you enjoy a nice breeze as well. . ."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Inbt", 60, 5)
                            elif Girl == JubesX:
                                    ch_v "Hmm, ok. . ."
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 2)
                            $ Girl.Statup("Obed", 50, 5)
                            $ Girl.Statup("Inbt", 60, 5)
                    elif Girl.SeenPeen < 5:
                            $ Girl.FaceChange("sad",0)
                            if Girl == RogueX:
                                    ch_r "Yeah, I've seen it."
                            elif Girl == KittyX:
                                    ch_k "Huh."
                            elif Girl == EmmaX:
                                    ch_e "You might want to put that away, [Girl.Petname]."
                            elif Girl == LauraX:
                                    ch_l "Hey. . ."
                                    ch_l "You might want to put that away, [Girl.Petname]."
                            elif Girl == JeanX:
                                    ch_j "I've seen that one before."
                            elif Girl == StormX:
                                    ch_s ". . ."
                            elif Girl == JubesX:
                                    ch_v "That's. . . inappropriate. . ."
                                    $ Girl.Statup("Obed", 80, 2)
                            $ Girl.Statup("Inbt", 60, 2)
                    elif Girl.SeenPeen == 10:
                            if Girl == RogueX:
                                    ch_r "I'm getting tired of seeing that."
                                    $ Girl.Statup("Obed", 50, 5)
                                    $ Girl.Statup("Inbt", 60, 5)
                            elif Girl == KittyX:
                                    ch_k "[Girl.Like]put that away."
                                    $ Girl.Statup("Obed", 50, 7)
                                    $ Girl.Statup("Inbt", 60, 3)
                            elif Girl == EmmaX:
                                    ch_e "Yes, we've all seen that before."
                                    $ Girl.Statup("Obed", 50, 7)
                                    $ Girl.Statup("Inbt", 60, 5)
                            elif Girl == LauraX:
                                    ch_l "Yeah, yeah, waving your cock around again."
                                    $ Girl.Statup("Obed", 50, 8)
                                    $ Girl.Statup("Inbt", 60, 4)
                            elif Girl == JeanX:
                                    ch_j "Oh, Penis. So original."
                                    $ Girl.Statup("Obed", 50, 8)
                                    $ Girl.Statup("Inbt", 60, 4)
                            elif Girl == StormX:
                                    ch_s ". . ."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Obed", 50, 2)
                                    $ Girl.Statup("Inbt", 60, 4)
                            elif Girl == JubesX:
                                    ch_v ". . ."
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 2)
                    $ React = 2
        else:
                    #Silent mode
                    $ Player.RecentActions.append("cockout")
                    if Girl.SeenPeen > 10:
                        return
                    elif ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "L"):
                            if Girl.SeenPeen == 1:
                                $ Girl.Statup("Love", 90, 5)
                            elif Girl.SeenPeen == 2:
                                $ Girl.Statup("Obed", 50, 5)
                            elif Girl.SeenPeen == 5:
                                $ Girl.Statup("Inbt", 60, 5)
                            elif Girl.SeenPeen == 10:
                                $ Girl.Statup("Love", 90, 10)
                    else:
                            if Girl.SeenPeen == 1:
                                $ Girl.Statup("Obed", 50, 5)
                                $ Girl.Statup("Inbt", 60, 5)
                                $ Girl.AddWord(1,0,0,0,"seenpeen") #$ Girl.History.append("seenpeen")
                            elif Girl.SeenPeen < 5:
                                $ Girl.Statup("Inbt", 60, 2)
                            elif Girl.SeenPeen == 10:
                                $ Girl.Statup("Obed", 50, 5)
                                $ Girl.Statup("Inbt", 60, 5)
                    if Girl == JubesX:
                            $ Girl.Statup("Obed", 80, 1)
        if Girl.SeenPeen == 1:
                if Girl == JeanX:
                        $ Girl.Statup("Love", 90, 10)
                        $ Girl.Statup("Obed", 30, 20)
                        $ Girl.Statup("Obed", 50, 10)
                        $ Girl.Statup("Obed", 80, 5)
                elif Girl == JubesX:
                        $ Girl.Statup("Obed", 80, 3)
                $ Girl.Statup("Love", 90, 15)
                $ Girl.Statup("Obed", 90, 20,Alt=[[StormX],900,0])
                $ Girl.Statup("Inbt", 60, 20)
                $ Girl.Statup("Lust", 200, 5)
        $ Girl.FaceChange("sly",1)
        return React

label Girls_Taboo(Girl=0,Cnt= 1,Choice=0,D20=0):  #nee  Rogue_Taboo(Cnt= 1,Choice=0) #rkeljsv
        #Called by Sex_Dialog
        #Girl is the Primary actor, Cnt is a count of how many times you've been spotted,
        #Choice is how the girl is reacting, D20 is a randomizer
        #With Jean, Taboo should not be a factor if she can whammy people
        if Girl not in TotalGirls:
                $ Girl = Ch_Focus
        $ Player.AddWord(1,0,Girl.Tag) #$ Player.DailyActions.append(Girl.Tag)
        $ Player.AddWord(1,0,"scent") #$ Player.DailyActions.append("scent") Allows Laura to track you.

        if "uninterrupted" in Girl.RecentActions:
                return
        elif "MindFuck" in Player.RecentActions:
                return
        $ Cnt = Girl.RecentActions.count("spotted") if "spotted" in Girl.RecentActions else 1
        $ Cnt = 4 if Cnt > 4 else Cnt

        $ D20 = renpy.random.randint(1, 20)

        if "screen" in Girl.Traits or (Partner and "screen" in Partner.Traits):
                #You've told Jean/Emma to screen Xavier's perceptions
                $ D20 += 8
        if D20 < 10:
                #if you're at the point where the girls would notice you. . .
                if Taboo > 20:
                        if (Trigger == "kiss_you" and not Trigger2 and not Trigger3):
                                #if it's very innocent, skip this part
                                pass
                        elif Girl not in Rules:
                                #if Xavier is looking. . .
                                $ Girl.FaceChange("surprised", 1)
                                if Trigger == "blow" or Trigger == "hand" or Trigger == "titjob":
                                        "[Girl.Name] stops what she's doing with a startled look."
                                else:
                                        "You feel a slight buzzing in your head and stop what you're doing."
                                ch_x "Cease that behavior at once! Come to my office immediately!"
                                call AllReset(Girl)
                                call Girls_Caught(Girl) #Rogue_Caught
                                return
                        else:
                                #if you've disabled Xavier's looking
                                ch_x "Hmmm. . ."
                                $ Girl.Statup("Inbt", 90, 2)
                                $ Girl.Statup("Lust", 200, 3)
                if bg_current == "bg classroom" and EmmaX.Loc == "bg teacher" and Girl != EmmaX:
                                #If you're in class and Emma's there as a teacher. . .
                                call Emma_Teacher_Caught(Girl)
                elif bg_current == "bg classroom" and StormX.Loc == "bg teacher" and Girl != StormX:
                                #If you're in class and Storm's there as a teacher. . .
                                call Storm_Teacher_Caught(Girl)
                elif "interruption" in Player.RecentActions:
                                #skips locked door event if it's already happened lately.
                                pass
                elif D20 == 1 and AloneCheck(Girl) and Time_Count < 3:
                                #bad luck, a girl showed up out of nowhere. . .
                                $ Choice = ActiveGirls[:]
                                $ Choice.remove(Girl)
                                $ renpy.random.shuffle(Choice)
                                while Choice:
                                        if Choice[0].Loc != bg_current and "lockedout" not in Girl.Traits:
                                                $ Trigger5 = Choice[0]
                                                $ Choice = [1]
                                        $ Choice.remove(Choice[0])
                                if Trigger5:
                                        call Locked_Door(Trigger5,1,Girl)
                                # either this new girl will be allowed in and stay, or she will run away
                                $ Choice = 0
                                $ Trigger5 = 0


                #now the girls get their turn to notice. . .
                call Girls_Noticed(Girl)

        if Taboo <= 20:
                #This is a private space with others around.
                call Girls_Noticed(Girl)
                return
        elif (Trigger == "kiss_you" and not Trigger2 and not Trigger3):
                #if it's very innocent, skip this part
                pass
        elif Cnt < 4:
                #if this has happened less than 4 times within the current cycle of events

                if Girl in (EmmaX,StormX) and "public" not in Girl.History:
                        $ Girl.History.append("public")

                if "spotted" not in Girl.RecentActions:
                        "Some of the other students notice you and [Girl.Name]."
                        $ Girl.Statup("Inbt", 200, 2)
                        $ Girl.Rep -= 2
                        $ Player.Rep -= 2
                elif Cnt < 3:
                        "A few more students notice you and [Girl.Name]."
                        $ Girl.Statup("Inbt", 200, 2)
                        $ Girl.Rep -= 1
                        $ Player.Rep -= 1
                elif Cnt == 3:
                        "You've got quite an audience."
                        $ Girl.Statup("Inbt", 200, 3)
                        $ Girl.Rep -= 1
                        $ Player.Rep -= 1
                if Partner:
                        $ Partner.Rep -= 1


                if "exhibitionist" in Girl.Traits:
                        $ Girl.FaceChange("sexy", 0)
                        if "spotted" not in Girl.RecentActions:
                                if Girl == RogueX:
                                        ch_r "Let'em watch, [Girl.Petname]."
                                elif Girl == KittyX:
                                        ch_k "I think we can give'em a show, [Girl.Petname]."
                                elif Girl == EmmaX:
                                        ch_e "Hmm, perhaps they can learn a few things, [Girl.Petname]."
                                elif Girl == LauraX:
                                        ch_l "Well, let's give'em what they want."
                                elif Girl == JeanX:
                                        ch_j "Well of course they want this."
                                elif Girl == StormX:
                                        ch_s "Let them worship us. . ."
                                elif Girl == JubesX:
                                        ch_v "I'm good if you are. . ."
                        $ Girl.Statup("Lust", 200, 4)
                        $ Choice = "A"
                elif ApprovalCheck(Girl, 650, "I", TabM=Cnt):
                        #not an exhibitionist but very uninhibited
                        $ Girl.FaceChange("sexy", 1, Brows="sad")
                        if "spotted" not in Girl.RecentActions:
                                if Girl == RogueX:
                                        ch_r "Hmm, what should we do about this, [Girl.Petname]?"
                                elif Girl == KittyX:
                                        ch_k "What should we do?"
                                elif Girl == EmmaX:
                                        ch_e "Well, this is something of a situation."
                                elif Girl == LauraX:
                                        ch_l "How do you want to play this?"
                                elif Girl == JeanX:
                                        $ Girl.Statup("Obed", 80, 3)
                                        $ Girl.Statup("Inbt", 80, 3)
                                        ch_j "Looks like we have an audience. . ."
                                elif Girl == StormX:
                                        ch_s "We seem to have attracted some attention. . ."
                                elif Girl == JubesX:
                                        ch_v "Oh, um, they're looking. . ."
                        $ Girl.Statup("Lust", 200, 3)
                        $ Choice = "B"
                elif ApprovalCheck(Girl, 1000, "OI", TabM=Cnt):
                        #not an exhibitionist but obedient/uninhibited
                        $ Girl.FaceChange("surprised", 2)
                        if Girl in (EmmaX,StormX):
                                "[Girl.Name] looks a bit concerned."
                        elif Girl == LauraX:
                                "[Girl.Name] looks a bit uncomfortable."
                        else:
                                "[Girl.Name] looks a bit panicked."
                        $ Girl.Statup("Lust", 200, 3)
                        $ Choice = "C"
                else:
                        # She fails her inhibition checks
                        $ Girl.FaceChange("surprised", 2)
                        if "spotted" not in Girl.RecentActions:
                                if Girl == KittyX:
                                        "[Girl.Name] bolts up with an embarassed look. She grabs her clothes and flings herself through the nearest wall."
                                elif Girl in (EmmaX,StormX):
                                        "[Girl.Name] bolts up with an embarassed look. She grabs her clothes and stalks off."
                                else:
                                        "[Girl.Name] bolts up with an embarassed look. She runs off while putting her clothes back on."
                                $ Girl.Rep -= 3 if Girl.Rep >= 30 else Girl.Rep
                        else:
                                if Girl == KittyX:
                                        $ Girl.Statup("Love", 90, -15)
                                        "With a sudden embarrassed start, [Girl.Name] panics. She dives through the nearest wall."
                                elif Girl in (EmmaX,StormX):
                                        $ Girl.Statup("Love", 90, -15)
                                        "With a sudden embarrassed start, [Girl.Name] stop what she's doing. She grabs her clothes and stalks off."
                                else:
                                        "With a sudden embarrassed start, [Girl.Name] panics. She takes off while throwing her clothes together."
                        "You head back to your room."
                        $ Choice = "stop"

                if Choice != "stop":
                    menu:
                        "What would you like to do?"
                        "Let them watch. . ." if "spotted" not in Girl.RecentActions:
                            if Choice == "A":
                                    $ Girl.FaceChange("sexy", 0)
                                    if Girl == RogueX:
                                            ch_r "That's what I'm talking about."
                                    elif Girl == KittyX:
                                            ch_k "I'll bring my \"A\" game."
                                    elif Girl == EmmaX:
                                            ch_e "It's only fair."
                                    elif Girl == LauraX:
                                            ch_l "I can handle that."
                                    elif Girl == JeanX:
                                            ch_j "Yeeeaah."
                                    elif Girl == StormX:
                                            ch_s "Yes. . ."
                                    elif Girl == JubesX:
                                            ch_v "Let's move it!"
                            elif Choice == "B":
                                    #not an exhibitionist but very uninhibited
                                    $ Girl.FaceChange("sexy", 1,Brows="sad")
                                    if Girl == RogueX:
                                            ch_r "Uh, ok."
                                    elif Girl == KittyX:
                                            ch_k "Hehe, um, yeah."
                                    elif Girl == EmmaX:
                                            ch_e "I do suppose we can show them how it's done."
                                    elif Girl == LauraX:
                                            ch_l "Ok."
                                    elif Girl == JeanX:
                                            ch_j "Sure, whatever."
                                    elif Girl == StormX:
                                            ch_s "I suppose. . ."
                                    elif Girl == JubesX:
                                            ch_v "Um, yeah. . ."
                            elif Choice == "C":
                                    $ Girl.FaceChange("sexy",2)
                                    if Girl.Obed > Girl.Inbt:
                                        $ Girl.Eyes = "side"
                                        if Girl == RogueX:
                                                ch_r "If you say so, [Girl.Petname]."
                                        elif Girl == KittyX:
                                                ch_k "If you insist, [KittyX.Petname]."
                                        elif Girl == EmmaX:
                                                ch_e "I won't back down if you won't, [EmmaX.Petname]."
                                        elif Girl == LauraX:
                                                ch_l "I guess."
                                        elif Girl == JeanX:
                                                ch_j "I suppose we could. . ."
                                        elif Girl == StormX:
                                                ch_s "Certainly. . ."
                                        elif Girl == JubesX:
                                                ch_v ". . . Right."
                                    else:
                                        $ Girl.Mouth = "smile"
                                        $ Girl.Brows = "sad"
                                        if Girl == RogueX:
                                                ch_r "Uh, I guess. . ."
                                        elif Girl == KittyX:
                                                ch_k "Yeah[KittyX.like]sure. . ."
                                        elif Girl == EmmaX:
                                                ch_e "Not that I mind, of course."
                                        elif Girl == LauraX:
                                                ch_l "Whatever. . ."
                                        elif Girl == JeanX:
                                                $ Girl.Statup("Obed", 80, 3)
                                                $ Girl.Statup("Inbt", 80, 3)
                                                ch_j "Yeah. . ."
                                        elif Girl == StormX:
                                                ch_s "Very well. . ."
                                        elif Girl == JubesX:
                                                ch_v "I guess."
                                    $ Girl.Statup("Obed", 200, 5)
                            "You get back to it."
                            $ Girl.Blush = 1
                        "Continue" if "spotted" in Girl.RecentActions:
                            if Choice == "C":
                                    $ Girl.Statup("Obed", 200, 4)
                        "Ok, let's stop.":
                            if Choice == "A":
                                    $ Girl.FaceChange("sad")
                                    if Girl == KittyX:
                                            ch_k "Booo."
                                    elif Girl == LauraX:
                                            ch_l "Sissy."
                                    elif Girl == StormX:
                                            ch_s "Oh, if you insist. . ."
                                    else:
                                            call AnyLine(Girl,"Spoilsport.")
                            elif Choice == "B":
                                    $ Girl.FaceChange("sad")
                                    if Girl == RogueX:
                                            ch_r "Yeah, probably."
                                    elif Girl == KittyX:
                                            ch_k "Um, yeah."
                                    elif Girl == EmmaX:
                                            ch_e "I suppose."
                                    elif Girl == LauraX:
                                            ch_l "Probably a good call."
                                    elif Girl == JeanX:
                                            $ Girl.Statup("Love", 80, 3)
                                            $ Girl.Statup("Obed", 80, 3)
                                            ch_j "Yeah. . . wouldn't want to cause a riot."
                                    elif Girl == StormX:
                                            ch_s "I suppose it's for the best. . ."
                                    elif Girl == JubesX:
                                            ch_v "Yeah, I guess so. . ."
                            elif Choice == "C":
                                    $ Girl.Statup("Love", 90, 5)
                                    $ Girl.FaceChange("smile")
                                    if Girl == RogueX:
                                            ch_r "Heh, thanks [Girl.Petname]"
                                    elif Girl == KittyX:
                                            ch_k "Heh, thanks [Girl.Petname]."
                                            $ Girl.Statup("Love", 90, 5)
                                    elif Girl == EmmaX:
                                            ch_e "That probably would be for the best. . ."
                                    elif Girl == LauraX:
                                            ch_l "Yeah, thanks."
                                            $ Girl.Statup("Love", 90, 5)
                                    elif Girl == JeanX:
                                            $ Girl.Statup("Love", 80, 3)
                                            $ Girl.Statup("Obed", 80, 3)
                                            ch_j "Yeah. . ."
                                    elif Girl == StormX:
                                            ch_s "Yes, that makes sense. . ."
                                    elif Girl == JubesX:
                                            ch_v "Heh, thanks."
                            "You both run back to your rooms."
                            $ Choice = "stop"

                if Choice == "stop":
                            $ Girl.RecentActions.append("caught")
                            $ Girl.DailyActions.append("caught")
                            show blackscreen onlayer black
                            call AllReset(Girl)
                            call Remove_Girl(Girl)
                            $ Girl.OutfitChange(Changed=0)
                            hide blackscreen onlayer black
                            $ bg_current = "bg player"
                            jump Misplaced
        elif "exhibitionist" not in Girl.Traits:
                            $ Girl.FaceChange("sly")
                            if Girl == JeanX and "nowhammy" not in JeanX.Traits:
                                    #if it's Jean, this doesn't count unless she's got "nowhammy" status
                                    pass
                            else:
                                    $ Girl.Traits.append("exhibitionist")
                                    "[Girl.Name] seems to have become something of an exhibitionist."
        elif D20 > 15:
                            $ Girl.FaceChange("sexy")
                            "The crowd cheers."

        $ Girl.RecentActions.append("spotted") if Cnt < 4 else Girl.RecentActions
        $ Girl.DailyActions.append("spotted")  if "spotted" not in Girl.DailyActions else Girl.DailyActions
        return

label Activity_Check(Girl=0,Girl2=0,Silent=0,Removal=1,ClothesCheck=1,Mod=0,Approval=1,Tempshame=0,TabooM=1): #rkeljsv
        # This checks whether a girl is up for watching a given activity
        # Silent is whether it plays dialog or not, Removal is whether it auto-removes the girl on a fail,
        # ClothesCheck is whether it bothers checking clothing, 2 if skip first girl
        # Mod gets set to her Like stat -600, so 600 Like, you break even, otherwise it's a penalty
        # call Activity_Check("Rogue",0,1,0)

        if Girl == Girl2:
            "Tell oni that the activity check failed after [Trigger]."
            $ Girl.NotAStat = 5

        #if they don't know you're there, they don't run
        if "unseen" in Girl.RecentActions or "classcaught" in Girl.RecentActions:
                    return 2

        $ Mod += 200 if Girl.Forced else 0             #bonus if in the Forced state
        $ Mod += (Girl.Lust*5) if Girl.Lust >= 50 else 0  #bonus if high lust (50 = +250, 75= +375, 90 = +450)

        if Girl2 and ClothesCheck != 2:
                #if there is a second girl and it's not told to skip it
                $ Mod = int(Mod/2) if Mod > 0 else Mod
                #halves the benefits from the above mechanisms
                $ Mod = (Girl.GirlLikeCheck(Girl2)-600)
                # if 500 = -100, if 700 = +100 if 900 = +300
                if Girl in Player.Harem and Girl2 in Player.Harem: #bonus for if both in harem
                        $ Mod += 500

        if ClothesCheck and Girl2:
                #sets her shame level to be accurate to current look
                #call expression Girl2.Tag + "_OutfitShame" pass (20)
                call OutfitShame(Girl2,20)
                $ Tempshame = Girl2.Shame

                if Girl == StormX:
                        #Storm doesn't care
                                $ Approval = 2
                elif Tempshame <= 15 and (ApprovalCheck(Girl, 600,Bonus=Mod) or ApprovalCheck(Girl, 350, "I")):
                        #If the outfit is hot but she's ok
                        if ApprovalCheck(Girl, 900,Bonus=Mod) or ApprovalCheck(Girl, 450, "I"):
                                $ Approval = 2
                elif Tempshame <= 20 and (ApprovalCheck(Girl, 900,Bonus=Mod) or ApprovalCheck(Girl, 450, "I")):
                        #If the outfit is sexy but she's cool with that
                        if ApprovalCheck(Girl, 1100,Bonus=Mod) or ApprovalCheck(Girl, 550, "I"):
                                $ Approval = 2
                elif Tempshame <= 25 and (ApprovalCheck(Girl, 1100,Bonus=Mod) or ApprovalCheck(Girl, 550, "I")):
                        #If the outfit is sexy but she's cool with that
                        if ApprovalCheck(Girl, 1400,Bonus=Mod) or ApprovalCheck(Girl, 650, "I"):
                                $ Approval = 2
                elif (ApprovalCheck(Girl, 1400,Bonus=Mod) or ApprovalCheck(Girl, 650, "I")):
                        #If the outfit is very scandelous but she's ok with that
                        if ApprovalCheck(Girl, 1600,Bonus=Mod) or ApprovalCheck(Girl, 850, "I"):
                                $ Approval = 2
                else:
                                $ Approval = 0

        if "exhibitionist" in Girl.Traits or ApprovalCheck(Girl,900,"I"):
                    #this negates or reduces the taboo modifier if they are slutty
                    $ TabooM = 0
        elif ApprovalCheck(Girl,50,"X") or ApprovalCheck(Girl,800,"I"):
                    $ TabooM = .5

        if not Approval:
                    # If it fails the clothing check, skip the next part
                    pass
        elif Trigger == "strip" and Trigger2 != "jackin":
                    pass #covered by the above check
        elif not Trigger:
                    pass
        elif Trigger == "lick ass":
                    $ Approval = ApprovalCheck(Girl,1550,Bonus=Mod, TabM = (TabooM* 3 ))
        elif Trigger == "anal":
                    $ Approval = ApprovalCheck(Girl,1550,Bonus=Mod, TabM = (TabooM* 3 ))
        elif Trigger == "sex":
                    $ Approval = ApprovalCheck(Girl,1400,Bonus=Mod, TabM = (TabooM* 3 ))
        elif Trigger == "lick pussy":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = (TabooM* 2 ))
        elif Trigger2 == "jackin":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = (TabooM* 2 ))
        elif Trigger == "blow":
                    $ Approval = ApprovalCheck(Girl,1300,Bonus=Mod, TabM = (TabooM* 2 ))
        elif Trigger == "titjob":
                    $ Approval = ApprovalCheck(Girl,1200,Bonus=Mod, TabM = (TabooM* 3 ))
        elif Trigger == "hotdog":
                    $ Approval = ApprovalCheck(Girl,1000,Bonus=Mod, TabM = (TabooM* 3 ))
        elif Trigger == "hand" or Trigger3 == "hand":
                    $ Approval = ApprovalCheck(Girl,1100,Bonus=Mod, TabM = (TabooM* 2 ))
        elif Trigger == "foot":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = (TabooM* 2 ))
        elif Trigger == "dildo anal":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = (TabooM* 2 ))
        elif Trigger == "dildo pussy":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = (TabooM* 2 ))
        elif Trigger == "insert ass":
                    $ Approval = ApprovalCheck(Girl,1300,Bonus=Mod, TabM = (TabooM* 2 ))
        elif Trigger == "fondle pussy" or Trigger == "insert pussy":
                    $ Approval = ApprovalCheck(Girl,1050,Bonus=Mod, TabM = (TabooM* 2 ))
        elif Trigger == "suck breasts":
                    $ Approval = ApprovalCheck(Girl,1050,Bonus=Mod, TabM = (TabooM* 3 ))
        elif Trigger == "fondle breasts":
                    $ Approval = ApprovalCheck(Girl,950,Bonus=Mod, TabM = (TabooM* 2 ))
        elif Trigger == "fondle ass":
                    $ Approval = ApprovalCheck(Girl,850,Bonus=Mod, TabM = (TabooM* 1 ))

        elif Trigger == "masturbation":
                    $ Approval = ApprovalCheck(Girl,1200,Bonus=Mod, TabM = (TabooM* 2 ))

        elif Trigger == "kiss_you":
                    $ Approval = ApprovalCheck(Girl,500,Bonus=Mod, TabM = 0)
        elif Trigger == "fondle thighs":
                    $ Approval = ApprovalCheck(Girl,750,Bonus=Mod, TabM = 0)

        elif Trigger == "lesbian":
                    $ Approval = ApprovalCheck(Girl,1350,Bonus=Mod, TabM = (TabooM* 2 ))

        #Threesomecheck
        if not Approval:
                    # If it fails the primary trigger check, skip the next part
                    pass
        elif not Trigger4:
                    pass
        elif Trigger4 == "lick ass":
                    $ Approval = ApprovalCheck(Girl,1750,Bonus=(Mod+200), TabM = (TabooM* 3 ))
        elif Trigger4 == "lick pussy":
                    $ Approval = ApprovalCheck(Girl,1450,Bonus=(Mod+200), TabM = (TabooM* 2 ))
        elif Trigger4 == "blow":
                    $ Approval = ApprovalCheck(Girl,1300,Bonus=(Mod+200), TabM = (TabooM* 2 ))
        elif Trigger4 == "hand":
                    $ Approval = ApprovalCheck(Girl,1200,Bonus=(Mod+200), TabM = (TabooM* 2 ))
        elif Trigger4 == "insert ass":
                    $ Approval = ApprovalCheck(Girl,1500,Bonus=(Mod+200), TabM = (TabooM* 2 ))
        elif Trigger4 == "fondle pussy":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=(Mod+200), TabM = (TabooM* 2 ))
        elif Trigger4 == "suck breasts":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=(Mod+200), TabM = (TabooM* 3 ))
        elif Trigger4 == "fondle breasts":
                    $ Approval = ApprovalCheck(Girl,1150,Bonus=(Mod+200), TabM = (TabooM* 2 ))
        elif Trigger4 == "kiss girl":
                    $ Approval = ApprovalCheck(Girl,1050,Bonus=(Mod+200), TabM = 0)
        elif Trigger4 == "kiss both":
                    $ Approval = ApprovalCheck(Girl,1050,Bonus=(Mod+200), TabM = 0)
        elif Trigger4 == "fondle ass":
                    $ Approval = ApprovalCheck(Girl,1050,Bonus=(Mod+200), TabM = (TabooM* 1 ))
        elif Trigger4 == "masturbation":
                    $ Approval = ApprovalCheck(Girl,1400,Bonus=(Mod+200), TabM = (TabooM* 2 ))
        elif Trigger4 == "watch":
                    $ Approval = ApprovalCheck(Girl,1000,Bonus=(Mod+200), TabM = 0)
        elif Trigger4 == "kiss_you":
                    $ Approval = ApprovalCheck(Girl,600,Bonus=Mod, TabM = 0)

        if not Silent and not Approval and not Girl.Forced:
            $ Girl.FaceChange("sadside",1)
            if Girl == RogueX:
                    if Girl2:
                        ch_r "I don't know, with [Girl2.Name] here and all."
                    ch_r "Ain't none a this right, [Girl.Petname]."
            elif Girl == KittyX:
                    if Girl2:
                        ch_k "I don't know, with [Girl2.Name] being here."
                    ch_k "I'm[KittyX.like]not really comfortable with this?"
            elif Girl == EmmaX:
                    if Girl2:
                        ch_e "I'm unsure that I'm comfortable doing this with [Girl2.Name] here."
                    ch_e "This has become a bit too. . . scandalous for my tastes."
            elif Girl == LauraX:
                    if Girl2:
                        ch_l "[Girl2.Name]'s weirding me out."
                    else:
                        ch_l "This is getting weird."
                    ch_l "I'll see you later."
            elif Girl == JeanX:
                    if Girl2:
                        ch_j "I'd rather not be here with [Girl2.Name]."
                    ch_j "I'm gonna leave it here."
            elif Girl == StormX:
                    if Girl2:
                        ch_s "I do not want to do this with [Girl2.Name] around."
                    ch_s "This has become a bit much for me, I am sorry."
            elif Girl == JubesX:
                    if Girl2:
                        ch_v "Not around [Girl2.Name], [Girl.Petname]."
                    ch_v "This is totally not cool. Sorry."

        if Removal and not Approval and not Girl.Forced:
                call Remove_Girl(Girl,2)
                "[Girl.Name] takes off."

        return Approval

label JumperCheck(Girls=[],BO=[]): #rkeljsv
        #decides whether a girl wants to jump you unexpectedly
        if "nope" in Player.RecentActions or Party:
                #if you refused sex. . .
                return

        $ BO = ActiveGirls[:]
        while BO:
                if "les" in BO[0].RecentActions and "no les" not in Player.RecentActions and ApprovalCheck(BO[0], 1600 - BO[0].SEXP, TabM=0):
                        #if they might be into you joining their lesbian adventure. . .
                        call Call_For_Les(BO[0])

                if "locked" in Player.Traits and BO[0].Loc != bg_current:
                        #if the door's locked and she's not in the room, skip it
                        pass
                elif BO[0].Action and BO[0].Thirst >= 30 and ApprovalCheck(BO[0], 500, "I") and "refused" not in BO[0].DailyActions and "met" in BO[0].History:
                        if "chill" not in BO[0].Traits and BO[0].Tag not in Player.DailyActions and "jumped" not in BO[0].DailyActions and BO[0].Loc != "bg teacher":
                            # I rule out if she is teaching, she won't jump you. . .
                            if renpy.random.randint(0,3) > 1:
                                    $ Girls.append(BO[0])
                            if BO[0].Thirst >= 60:
                                    $ Girls.append(BO[0])
                        if BO[0].Thirst >= 90:
                                    $ Girls.append(BO[0])
                $ BO.remove(BO[0])

        if not Girls:
            return

        if len(Girls) >= 2:
            $ renpy.random.shuffle(Girls)
            while len(Girls) >= 2 and Girls[0] == Girls[1]:
                    $ Girls.remove(Girls[1])    #removes duplicates
            while len(Girls) > 2:
                    $ Girls.remove(Girls[2])    #removes any over 2

        $ Partner = 0
        if len(Girls) >= 2:
            #if there are two girls, it adds the second as a potential partner
            if Girls[0] in Player.Harem and Girls[1] in Player.Harem:
                    $ Partner = Girls[1]
            elif Girls[0].GirlLikeCheck(Girls[1]) >= 800 and Girls[1].GirlLikeCheck(Girls[0]) >= 800:
                    $ Partner = Girls[1]

        call Jumped #Launches the main event

        if "nope" in Player.RecentActions:
                #if you refused sex. . .
                while Girls:         #clears list
                        call Remove_Girl(Girls[0])
                        $ Girls.remove(Girls[0])
                jump Misplaced
        elif Girls:
                #if you had some sort of sexual encounter, it will hop you to the appropriate sex menu
                if Girls[0].Loc == bg_current:
                        call expression Girls[0].Tag + "_SexMenu" #call Rogue_SexMenu

        if bg_current == "bg player":
                #if it jumped to your room. . .
                jump Player_Room
        return

label LesCheck(Girls=[],BO=[]): #rkeljsv
        #Called by Wait, Checks if any girls will jump each other behind the scenes. . .
        # They will if they have over 500 Inbt and are thirsty

        if "three" not in EmmaX.History:
                #this addes threecheck if she's really slutty
                if EmmaX.Thirst >= 30 and ApprovalCheck(EmmaX, 800, "I"):
                        $ EmmaX.History.append("three")

        $ BO = ActiveGirls[:]
        while BO:
                #loops through and makes choices.
                if BO[0] == RogueX and "touch" not in RogueX.Traits:
                        #skip if Rogue and she doesn't have touch upgrade
                        pass
                elif BO[0] == EmmaX and "three" not in EmmaX.History:
                        #skip if it's Emma and she doesn't do threesomes
                        pass
                elif ApprovalCheck(BO[0], 500, "I",Alt=[[EmmaX,JeanX],300]) and BO[0].Thirst >= 30: #and "refused" not in R_DailyActions?
                        if ("mono" not in BO[0].Traits or BO[0].Break[0]) and BO[0] not in Party:
                            $ Girls.append(BO[0])
                            if BO[0].Thirst >= 60:
                                    $ Girls.append(BO[0])
                        if BO[0].Thirst >= 90:
                                $ Girls.append(BO[0])
                $ BO.remove(BO[0])
        if not Girls:
            return

        if Girls[0] != JeanX: #keeps Jean as lead if she's in the mix
                $ renpy.random.shuffle(Girls)

        $ Partner = 0
        while len(Girls) >= 2:
                # So long as the list has two people in it, check to see if the second girl is viable
                # if not, remove her and try again
                if Partner:
                        # if a partner's been picked, cull out the 3+ girls
                        $ Girls.remove(Girls[1]) #$ Girls.remove(Girls[2])
                elif Girls[1] == Girls[0] or Girls[1].Loc == bg_current or Girls[1] in Party:
                        # if the second girl in the list is the same as the first, remove her
                        # if the second girl is at your location, remove her too
                        $ Girls.remove(Girls[1])
                elif Girls[0] == JeanX and Girls[1].GirlLikeCheck(Girls[0]) >= 500:
                        # Jean tends to get her way. . .
                        $ Partner = Girls[1]
                elif (Girls[1] in Player.Harem and Girls[0] in Player.Harem) and Girls[0].GirlLikeCheck(Girls[1]) >= 600:
                        $ Partner = Girls[1]
                elif Girls[1].GirlLikeCheck(Girls[0]) >= 800 and Girls[0].GirlLikeCheck(Girls[1]) >= 800:
                        $ Partner = Girls[1]
                elif Girls[1].Thirst >= 90 and Girls[0].GirlLikeCheck(Girls[1]) >= 600:
                        $ Partner = Girls[1]
                else:
                        #if not picked, remove this girl from the list
                        $ Girls.remove(Girls[1])

        if not Partner:
                # if nobody is picked, then return, otherwise you should have at least two girls picked
                return

        $ Girls.append(Partner)
        $ Partner = 0
        #move both girls into the same room

        if bg_current != Girls[0].Home:
                #if you aren't in first girl's room, move both there.
                $ Girls[0].Loc = Girls[0].Home
                $ Girls[1].Loc = Girls[0].Home
        elif bg_current != Girls[1].Home:
                #if you are in the first girl's room, move both to the seconds'.
                $ Girls[0].Loc = Girls[1].Home
                $ Girls[1].Loc = Girls[1].Home

        $ Girls[0].AddWord(1,"les",0,0,0) #adds "les" to recent actions for both girls
        $ Girls[1].AddWord(1,"les",0,0,0) #adds "les" to recent actions for both girls

        $ Girls[0].GLG(Girls[1],700,15,1)         #Like +15 if under 700
        $ Girls[1].GLG(Girls[0],700,15,1)         #Like +15 if under 700

        $ Girls[0].GLG(Girls[1],900,10,1)         #Like +10 if under 900
        $ Girls[1].GLG(Girls[0],900,10,1)         #Like +10 if under 900

        $ Girls[0].GLG(Girls[1],1000,5,1)         #Like +5 if under 1000
        $ Girls[1].GLG(Girls[0],1000,5,1)         #Like +5 if under 1000

        $ Girls[0].DrainWord("arriving",1,0) #removes "arriving" from recent
        $ Girls[1].DrainWord("arriving",1,0) #removes "arriving" from recent

        $ Girls[0].Statup("Lust", 60, 20)
        $ Girls[1].Statup("Lust", 60, 20)

        $ Girls[0].Thirst -= 5
        $ Girls[1].Thirst -= 5
        return

label CheckTaboo(Girl=0,Taboo_Check=0,Girl2=[]): #rkeljsv
        #Girl is the girl being tested
        # Taboo_Check is the location she is at

        if Taboo_Check in PersonalRooms or Taboo_Check == "hold":
                            $ Girl.Taboo = 0
        elif "locked" in Player.Traits and Taboo_Check == bg_current:
                            $ Girl.Taboo = 0
        elif Taboo_Check in ("bg classroom", "bg study"):
                if Time_Count >= 3:
                            $ Girl.Taboo = 10
                elif Time_Count == 2 or Weekday >= 5:
                            $ Girl.Taboo = 30
                else:
                            $ Girl.Taboo = 40
        elif Taboo_Check == "bg dangerroom":
                if Time_Count >= 3:
                            $ Girl.Taboo = 20
                else:
                            $ Girl.Taboo = 40
        elif Taboo_Check == "bg campus" or Taboo_Check == "bg pool":
                if Time_Count >= 3:
                            $ Girl.Taboo = 20
                else:
                            $ Girl.Taboo = 40
        elif Taboo_Check == "bg showerroom":
                            $ Girl.Taboo = 20
        else:
                            $ Girl.Taboo = 40
        if Girl == Player:
                # if it's already 20+, or if we're testing the player stat, there's no point to this
                $ Taboo = Girl.Taboo
                return
        if Girl.Taboo >= 20:
                # if it's already 20+, or if we're testing the player stat, there's no point to this
                return

        $ Girl2 = TotalGirls[:]
        while Girl2:
                #compares the first girl to each of the others.
                if Girl2[0] != Girl:
                        #loops through the girls in an inner loop if they are not the same
                        if Girl.Loc == Girl2[0].Loc and Girl.GirlLikeCheck(Girl2[0]) <= 700 and not (Girl in Player.Harem and Girl2[0] in Player.Harem):
                                #if either she likes the second girl, or both are in the harem, skip
                                $ Girl.Taboo = 20
                $ Girl2.remove(Girl2[0])

        $ Taboo = Girl.Taboo if (Girl.Taboo > Taboo and bg_current == Girl.Loc) else Taboo

        return

label Present_Check(Hold=1,BO=[],TempList=[]):
        # Culls parties down to 2 max
        # call Present Check will cull inhabitants of the room down to zero

        while len(Party) > 2:
                # If two or more members in the party
                #Culls down party size to two
                $ Party.remove(Party[2])

        #If there is a party, fill the Present list with the party first
        $ Present = Party[:] if Party else []

        # checks to see which girls are present at a given location
        # If they are in the party, makes sure they are in the room
        # adds members who are not currently in the party

        $ BO = TotalGirls[:]
        $ renpy.random.shuffle(BO) #Randomizes pool
        while BO:
                #cycles through each girl possible, adds them to the local area if possible
                if BO[0] not in Present and BO[0].Loc == bg_current:
                        $ Present.append(BO[0])
                $ BO.remove(BO[0])

        while len(Present) > 2:
                #culls the Temporary Present list down to two items (or less if the party is full)
                #Removes the rest
                #Moves girls to Nearby if that's an option.
                call Remove_Girl(Present[2],Hold=Hold)

        if Present and Ch_Focus not in Present:
                $ renpy.random.shuffle(Present)
                call Shift_Focus(Present[0])

        $ BO = Present[:]
        while BO:
                #cycles through each girl possible, removes them from NEarby if they were there.
                if BO[0] in Nearby:
                        $ Nearby.remove(BO[0])
                $ BO[0].Loc = bg_current
                $ BO.remove(BO[0])
        return
