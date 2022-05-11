# Start You Cumming //////////////////////////////////////////////////////////////////////////////////

label Player_Cumming(Girl=0,temp_modifier = temp_modifier): #rkeljsv
    if "phonesex" in Player.RecentActions:
            $ Player.Semen -= 1
            $ Player.Focus = 0
            "You spray jizz across the room."
            return

    $ Girl = GirlCheck(Girl)

    call Shift_Focus(Girl)
    if Trigger == "blow":
            $ temp_modifier += 5

    if Girl.Addict > 75:
            $ temp_modifier += 20
    elif Girl.Addict > 50:
            $ temp_modifier += 5

    if Girl.Swallow >= 10:
            $ temp_modifier += 15
    elif Girl.Swallow >= 3:
            $ temp_modifier += 5

    if (Girl.CreamP + Girl.CreamA) >= 10:
            $ temp_modifier += 15 
    elif (Girl.CreamP + Girl.CreamA) >= 3:
            $ temp_modifier += 5

    $ D20 = renpy.random.randint(1, 20)

# intro lines
    if Situation == "swap":
            #if you swapped to the partner
            $ Line = "So what would you like "+Girl.Name+" to do?"
    elif Trigger == "hand":
            $ Line = "As she strokes, you're about ready to come. . ."
    elif Trigger == "blow":
            $ Line = "As she sucks at you, you start to feel about to come. . ."
    elif Trigger == "titjob":
            $ Line = "As you rub into her cleavage, you start to feel about to come. . ."
    elif Trigger == "sex" or Trigger == "anal":
            $ Line = "As you thrust into her, you feel about to blow. . ."
    elif Trigger == "hotdog":
            $ Line = "As you grind into her, you feel about to blow. . ."
    else:
            $ Line = "You start to feel about to come. . ."

    $ Girl.FaceChange("sexy")

    menu:
        "[Line]"
        "Warn her":
                $ Situation = "warn"
                jump Girl_Warn_Her

        "Ask to cum in her mouth":
                $ Situation = "asked"
                jump Girl_In_Mouth
        "Cum in her mouth without asking" if Trigger == "blow" or Trigger == "hand" or Trigger == "titjob" and Situation != "swap":
                $ Situation = "auto"
                jump Girl_In_Mouth

        "Ask to cum inside her" if Trigger == "sex" and Situation != "swap":
                $ Situation = "asked"
                jump Girl_Creampie_P
        "Ask to cum inside her" if Trigger == "anal" and Situation != "swap":
                $ Situation = "asked"
                jump Girl_Creampie_A

        "Cum inside her" if Trigger == "sex" and Situation != "swap":
                $ Situation = "auto"
                jump Girl_Creampie_P
        "Cum inside her" if Trigger == "anal" and Situation != "swap":
                $ Situation = "auto"
                jump Girl_Creampie_A
        "Cum Outside":
            menu:
                "Cum on her face":
                        jump Girl_Facial
                "Cum on her tits":
                        jump Girl_TitSpunk
                "Cum on her ass": #if (Girl == RogueX or Girl == JeanX)and (Trigger == "sex" or Trigger == "anal" or Trigger == "hotdog" or Trigger == "foot"):
                        $ Girl.Pose = "doggy"
                        jump Girl_Cum_Outside
                "Cum on her belly": #if (Girl != RogueX and Girl != JeanX) and (Trigger == "sex" or Trigger == "anal" or Trigger == "hotdog" or Trigger == "foot" or Trigger == "psy"):
                        $ Girl.Pose = "sex"
                        jump Girl_Cum_Outside

        "Actually, let [Partner.Name] take it." if Partner in TotalGirls and Situation != "swap":
                $ Situation = "swap"
                $ temp_modifier = 0
                call Shift_Focus(Partner) #makes the partner the lead and the lead the partner
                call AllReset(Partner) #resets the position of the orignal lead
                call Player_Cumming(Ch_Focus,temp_modifier = 0) #Does the cumshot focused on the original Partner

                call Shift_Focus(Partner) #makes the original partner the partner again
                call AllReset(Partner)  #resets the position of the partner

                $ Situation = 0
                "[Girl.Name] Steps back in."

                call AllReset(Girl) #resets the position of the orignal lead
                return

        "Just fire away" if Trigger2 == "jackin":
                if "cockout" not in Player.RecentActions:
                        $ Player.Spunk = "in"
                        "You cum in your pants."
                else:
                        "You spray jizz across the room."
                jump Girl_Orgasm_After
        "Pull back" if Trigger != "psy" and Girl.Loc == bg_current and Situation != "swap":
            if renpy.showing(Girl.Tag+"_BJ_Animation"): #if renpy.showing("Rogue_BJ_Animation"):
                    if Girl.Addict >= 60 and ApprovalCheck(Girl, 1000, "I", Bonus = ((Girl.Addict*10)- Girl.Obed)) and Girl.Swallow:
                            jump Manic_Suck
                    call expression Girl.Tag+"_BJ_Reset"
            elif renpy.showing(Girl.Tag+"_HJ_Animation"): #if renpy.showing("Rogue_HJ_Animation"):
                    call expression Girl.Tag+"_HJ_Reset"
            elif renpy.showing(Girl.Tag+"_Doggy_Animation"): #if renpy.showing("Rogue_Doggy_Animation"):
                    call expression Girl.Tag+"_Doggy_Reset"
            elif renpy.showing(Girl.Tag+"_SexSprite"): #fix
                    call expression Girl.Tag+"_Sex_Reset"
            if ApprovalCheck(Girl, 500, "I", Bonus = ((Girl.Addict*10)- Girl.Obed)) and Girl.Addict > 50 and Girl.Swallow: #If addict + Inbt is > obedience + 50. . .
                    $ Girl.Eyes = "manic"
                    $ Girl.Mouth = "kiss"
                    $ Speed = 0
                    "Her eyes widen in panic."
                    if Girl == RogueX:
                            ch_r "Are you sure you won't reconsider, [Girl.Petname]?"
                    elif Girl == KittyX:
                            ch_k "You[Girl.like]sure about that?"
                    elif Girl == EmmaX:
                            ch_e "You wouldn't reconsider, [Girl.Petname]?"
                    elif Girl == LauraX:
                            ch_l "You sure?"
                    elif Girl == JeanX:
                            ch_j "Where do you think you're going?"
                    elif Girl == StormX:
                            ch_s "Wait. . ."
                    elif Girl == JubesX:
                            ch_v "Wait, you're letting it go to waste?"
                    $ Girl.Blush = 2
                    menu:
                        extend ""
                        "Ok, if you'll swallow it.":
                                        if not renpy.showing(Girl.Tag+"_BJ_Animation"): #if not renpy.showing("Rogue_BJ_Animation"):
                                            call expression Girl.Tag+"_BJ_Launch" pass ("cum")
                                        $ Girl.FaceChange("sucking")
                                        $ Speed = 2
                                        "She nods and puts the tip into her mouth. As you release she gulps it down hungrily."
                                        $ Girl.FaceChange("sexy")
                                        $ Girl.Mouth = "sucking"
                                        $ Girl.Spunk.append("mouth")
                                        ". . ."
                                        $ Speed = 0
                                        $ Girl.FaceChange("sad")
                                        $ Girl.Mouth = "lipbite"
                                        if Girl == RogueX:
                                                ch_r "That would have been such a waste otherwise."
                                        elif Girl == KittyX:
                                                ch_k "You know I like my milk."
                                        elif Girl == EmmaX:
                                                ch_e "Waste not, want not."
                                        elif Girl == LauraX:
                                                ch_l "Yum."
                                        elif Girl == JeanX:
                                                ch_j "Mmm."
                                        elif Girl == StormX:
                                                ch_s "Mmmm. . ."
                                        elif Girl == JubesX:
                                                ch_v "Well duh!"
                                        $ Girl.Statup("Obed", 50, 2,Alt=[[JeanX],800,4]) #+4 for Jean)
                                        $ Girl.Statup("Obed", 70, 1)
                                        $ Girl.Statup("Inbt", 30, 2)
                                        $ Girl.Statup("Inbt", 50, 3)
                                        jump Girl_Swallowed
                        "No, we're done for now.": #If addict is > obedience + 50. . .
                                if ApprovalCheck(Girl, 250, "I", Bonus = ((Girl.Addict*10)- Girl.Obed)) or Girl.Addict > 75:
                                        $ Girl.Statup("Obed", 50, -1)
                                        $ Girl.Statup("Obed", 70, -2)
                                        $ Girl.Statup("Inbt", 30, 2)
                                        $ Girl.Statup("Inbt", 70, 3)
                                        if not renpy.showing(Girl.Tag+"_BJ_Animation"): #if not renpy.showing("Rogue_BJ_Animation"):
                                            call expression Girl.Tag+"_BJ_Launch" pass ("cum")
                                            $ Speed = 4
                                        "She dives down on you and you can't resist filling her throat."
                                        $ Speed = 0
                                        if Girl == RogueX:
                                                ch_r "I. . . just can't pass this up."
                                        elif Girl == KittyX:
                                                ch_k "It's. . . compelling."
                                        elif Girl == EmmaX:
                                                ch_e "Well, I'm afraid I wasn't."
                                        elif Girl == LauraX:
                                                ch_l "Now we are."
                                        elif Girl == JeanX:
                                                ch_j "Fine, we're done."
                                        elif Girl == StormX:
                                                ch_s "Now we are done. . ."
                                        elif Girl == JubesX:
                                                ch_v "Ok, -now- we're done."
                                        jump Girl_Swallowed
                                else:
                                        $ Girl.Statup("Obed", 30, 3,Alt=[[JeanX],800,3]) #+3 for Jean
                                        $ Girl.Statup("Obed", 70, 5)
                                        $ Girl.FaceChange("sad")
                                        $ Girl.Brows = "confused"
                                        if Girl == RogueX:
                                                ch_r "ok. . ."
                                        elif Girl == KittyX:
                                                ch_k "Whatever."
                                        elif Girl == EmmaX:
                                                ch_e "If you insist."
                                        elif Girl == LauraX:
                                                ch_l "Dick."
                                        elif Girl == JeanX:
                                                ch_j "Whatever."
                                        elif Girl == StormX:
                                                ch_s ". . ."
                                        elif Girl == JubesX:
                                                ch_v "Well. . . I still think that was a waste."
                                        $ Line = 0
                                        $ Player.Focus -= 5
                                        return
            #manic, wanted to swallow
            $ Girl.FaceChange("sexy", 1)
            $ Girl.Statup("Obed", 50, 2)
            "You pull pull back away from her. She looks up at you and licks her lips."

            if Girl == RogueX:
                    ch_r "Well [Girl.Petname], what next then?"
            elif Girl == KittyX:
                    ch_k "Oh? So what did you want to do?"
            elif Girl == EmmaX:
                    ch_e "Well [Girl.Petname], what next then?"
            elif Girl == LauraX:
                    ch_l "So now what?"
            elif Girl == JeanX:
                    ch_j "Fine, what now?"
            elif Girl == StormX:
                    ch_s "So what did you have in mind then?"
            elif Girl == JubesX:
                    ch_v "Ok, so what'd you want?"
            $ Line = 0
            $ Player.Focus = 95
            return
            #end "pull back"
#End Main orgasm menu

label Manic_Suck: #rkeljsv
        $ Girl.Eyes = "manic"
        $ Speed = 0
        "You pull out of her mouth with a pop, and her eyes widen in surprise."
        $ Girl.Mouth = "sucking"
        $ Girl.Spunk.append("mouth")
        $ Speed = 4
        "She leaps at your cock and sucks it deep, draining your fluids hungrily."
        $ Speed = 0
        $ Girl.Mouth = "lipbite"
        "When she finishes, she licks her lips."
        $ Girl.FaceChange("bemused")
        if Girl == EmmaX:
                ch_e "I'm sorry, [Girl.Petname], but that would have been a waste."
        elif Girl == JeanX:
                $ Girl.FaceChange("sly",2,Mouth="lipbite")
                ch_j ". . ."
        elif Girl == StormX:
                ch_s "That would have been wasteful. . ."
        else:
                call AnyLine(Girl,"Sorry, [Girl.Petname], I just couldn't let that go to waste.")
        $ Girl.Statup("Obed", 200, -5,Alt=[[JeanX],800,5]) #+5 for Jean
        $ Girl.Statup("Inbt", 200, 10)
        jump Girl_Swallowed

#Warn her start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Warn_Her:  #rkeljsv
        "You let her know that you're going to come."
        $ Girl.Statup("Love", 90, 3,Alt=[[JeanX],900,5]) #+5 for Jean
        if Girl.Obed >= 500:
                $ Girl.Statup("Obed", 80, 5)
        if ("hungry" in Girl.Traits and D20 >= 5):# or Girl == JubesX:
                if renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"): #if renpy.showing("Rogue_Doggy"):
                    call expression Girl.Tag+"_HJ_Launch" pass ("cum")
                    "She grins and pulls out with a pop, and begins to stroke you off."
                $ Speed = 2
                $ Girl.FaceChange("sucking")
                ". . ."
                $ Speed = 0
                $ Girl.Spunk.append("mouth")
                $ Girl.Spunk.append("chin")
                if not renpy.showing(Girl.Tag+"_BJ_Animation"): #if not renpy.showing("Rogue_BJ_Animation"):
                    "She smiles and then puts your tip in her mouth. When you finish filling her mouth, she quickly gulps it down and wipes her lips."
                else:
                    "She makes a little humming sound, but keeps sucking. When you finish filling her mouth, she quickly gulps it down and wipes her lips."
                $ Girl.FaceChange("sexy")
                $ Girl.Mouth = "smile"
                call Sex_Basic_Dialog(Girl,"swallowgood") #"That was real sweet, [Girl.Petname], thanks for the head's up."
                call Sex_Basic_Dialog(Girl,"warned") #"That was real sweet, [Girl.Petname], thanks for the head's up."
                jump Girl_Swallowed
        #End Hungy take-over

        if Trigger == "sex" and Girl.CreamP >= 5:
                # She's Creampied a few times
                $ Girl.FaceChange("sexy")
                $ Player.Cock = "in"
                $ Girl.Spunk.append("in")
                $ Player.Spunk = "in"
                $ Speed = 0
                "She smiles and speeds up her actions, causing you to erupt inside her."
                if Girl.Lust >= 85:
                        call Girl_Cumming(Girl)
                jump Girl_Creampied

        elif Trigger == "sex" and Girl.CreamP and D20 >= 10:
                # She's Creampied at least once
                $ Girl.FaceChange("sexy")
                $ Player.Cock = "in"
                $ Girl.Spunk.append("in")
                $ Player.Spunk = "in"
                $ Speed = 0
                "She gets a michevious look and speeds up, you burst inside her."
                if Girl.Lust >= 85:
                        call Girl_Cumming(Girl)
                jump Girl_Creampied

        elif Trigger == "anal" and Girl.CreamA >= 5:
                # She's Anal Creampied a few times
                $ Girl.FaceChange("sexy")
                $ Player.Cock = "anal"
                $ Girl.Spunk.append("anal")
                $ Player.Spunk = "anal"
                $ Speed = 0
                "She smiles and speeds up her actions, causing you to erupt inside her."
                if Girl.Lust >= 85:
                        call Girl_Cumming(Girl)
                jump Girl_Creampied

        elif Trigger == "anal" and Girl.CreamA and D20 >= 10:
                # She's Anal Creampied at least once
                $ Girl.FaceChange("sexy")
                $ Player.Cock = "anal"
                $ Girl.Spunk.append("anal")
                $ Player.Spunk = "anal"
                $ Speed = 0
                "She gets a michevious look and speeds up, you burst inside her."
                if Girl.Lust >= 85:
                        call Girl_Cumming(Girl)
                jump Girl_Creampied

        elif Trigger != "anal" and Girl.Swallow >= 5:
                #If she's swallowed a lot
                if renpy.showing(Girl.Tag+"_BJ_Animation"): #if renpy.showing("Rogue_BJ_Animation"):
                        $ Girl.FaceChange("sucking")
                        $ Girl.Spunk.append("mouth")
                        "She makes a little humming sound, but keeps sucking."
                else:
                        if renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"): #if renpy.showing("Rogue_Doggy"):
                            call expression Girl.Tag+"_BJ_Launch" pass ("cum")
                            $ Speed = 2
                        $ Girl.FaceChange("sucking")
                        $ Girl.Spunk.append("mouth")
                        "She smiles and then puts your tip in her mouth."
                $ Girl.Spunk.append("chin")
                "When you finish filling her mouth, she quickly gulps it down and wipes her lips."
                $ Speed = 0
                $ Girl.FaceChange("sexy")
                $ Girl.Mouth = "smile"
                call Sex_Basic_Dialog(Girl,"swallowgood") #"That was real sweet, [Girl.Petname], thanks for the head's up."
                call Sex_Basic_Dialog(Girl,"warned") #"That was real sweet, [Girl.Petname], thanks for the head's up."
                jump Girl_Swallowed

        elif Girl.Swallow and D20 >= 10:
                #She's swallowed before, but not a lot
                if renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"): #if renpy.showing("Rogue_Doggy"):
                    call expression Girl.Tag+"_HJ_Launch" pass ("cum")
                    "She grins and pulls out with a pop, and begins to stroke you off."
                $ Speed = 2
                if renpy.showing(Girl.Tag+"_BJ_Animation"): #if renpy.showing("Rogue_BJ_Animation"):
                        #if she's blowing
                        $ Girl.FaceChange("sucking")
                        $ Girl.Spunk.append("mouth")
                        "She makes a little humming sound, but keeps sucking."
                        "When you finish filling her mouth, she gags a little, but manages to swallow it."
                        $ Speed = 0
                        $ Girl.FaceChange("sexy")
                        $ Girl.Mouth = "smile"
                        $ Girl.Spunk.append("chin")
                        if Girl.Addict > 50:
                                $ Girl.Eyes = "manic"
                                "She gulps it down hungrily and licks her lips."
                        $ Girl.FaceChange("bemused")
                        call Sex_Basic_Dialog(Girl,"swallow2") #"I'm still starting to get used to that, thanks for the head's up."
                        call Sex_Basic_Dialog(Girl,"warned") #"I'm still starting to get used to that, thanks for the head's up."
                        jump Girl_Swallowed
                        #fix, add titjob option here.
                else:
                        #If she's handying
                        jump Girl_Handy_Finish
        #end if she's swallowed

        elif ApprovalCheck(Girl, 1000):
                #warned but likes you and experienced
                if Girl.SEXP > 20 and (renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite")): #renpy.showing("Rogue_Doggy"):
                        "She gently pushes you back off of her."
                        jump Girl_Cum_Outside
                elif Girl.SEXP > 20:
                        jump Girl_Facial

                if renpy.showing(Girl.Tag+"_HJ_Animation") and Girl.Hand:
                        jump Girl_Handy_Finish
                elif renpy.showing(Girl.Tag+"_BJ_Animation") and Girl.Blow:
                        jump Girl_Handy_Finish
                elif renpy.showing(Girl.Tag+"_TJ_Animation") and Girl.Tit:
                        jump Girl_Facial
                elif (renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite")) and Girl.Sex and Trigger == "sex":
                        "She gently pushes you back off of her."
                        jump Girl_Cum_Outside
                elif (renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite")) and Girl.Anal and Trigger == "anal":
                        "She gently pushes you back off of her."
                        jump Girl_Cum_Outside


        # Else. . . not experienced or she's not a huge fan,
        if renpy.showing(Girl.Tag+"_BJ_Animation"): #if renpy.showing("Rogue_BJ_Animation"):
                jump Girl_In_Mouth
        elif Trigger == "sex" or Trigger == "anal":
                call expression Girl.Tag+"_Doggy_Reset"
                call expression Girl.Tag+"_Sex_Reset"
                "She pulls off of you and grabs your cock in her hand."
                jump Girl_Handy_Finish
        elif renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"): #if renpy.showing("Rogue_Doggy"):#hotdogging
                "She smiles and starts rubbing against you a bit faster."
                jump Girl_Cum_Outside
        jump Girl_Facial
    #End "Warn her" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#Cum in mouth start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_In_Mouth: #rkeljsv
    if Trigger == "anal":
            $ temp_modifier -= 15
    if "hungry" not in Girl.Traits and Girl.Addict <= 50 and "full" in Girl.RecentActions:
            $ temp_modifier -= 15

#    if renpy.showing(Girl.Tag+"_PJ_Animation"): #if renpy.showing("Rogue_PJ_Animation"):
#                call expression Girl.Tag + "_Kissing_Launch" pass (Trigger,0)
    $ Player.Cock = "out"
    if Situation == "auto" or Situation == "warn":
                $ Situation = 0
                if not renpy.showing(Girl.Tag+"_BJ_Animation"): #if not renpy.showing("Rogue_BJ_Animation"):
                        call expression Girl.Tag+"_BJ_Launch" pass ("cum")
                $ Speed = 2
                if Situation == "warn":
                    "She doesn't seem sure what to do about that, as you cum in her mouth."
                else:
                    "You grab her head and cum in her mouth"
                $ Girl.Eyes = "closed"
                call Punch
                $ Player.Spunk = 1
                if "full" in Girl.RecentActions:
                        #if she's had enough
                        $ Girl.FaceChange("bemused")
                        $ Girl.Spunk.append("mouth")
                        $ Speed = 0
                        $ Girl.Spunk.append("chin")
                        "She gags a little, but manages to swallow it."
                        $ Girl.Spunk.remove("mouth")
                        if Girl == RogueX:
                                ch_r "Um, I. . . I think I've had enough for now, could we maybe. . ."
                                ch_r ". . . put that stuff someplace else?"
                        elif Girl == KittyX:
                                ch_k "I'm[Girl.like]totally stuffed here. . ."
                                ch_k ". . . is there anywhere else we could put this?"
                        elif Girl == EmmaX:
                                ch_e "Hmm. . . that, may be a bit much for right now. . ."
                                ch_e "Perhaps we could find someplace else for you to. . . release. . ."
                        elif Girl == LauraX:
                                ch_l "Hmm. . . I'm kinda full. . ."
                                ch_l "Maybe keep it outside. . ."
                        elif Girl == JeanX:
                                ch_j "I'm kinda full at the moment."
                        elif Girl == StormX:
                                ch_s "I am afraid that I am rather full at the moment. . ."
                        elif Girl == JubesX:
                                ch_v "I, um. . . I think I'm actually stuffed. . ."
                elif Girl.Swallow >= 5 or "hungry" in Girl.Traits:
                        #if she likes to swallow
                        $ Girl.FaceChange("sexy")
                        $ Girl.Mouth = "smile"
                        $ Girl.Spunk.append("mouth")
                        $ Girl.Spunk.append("chin")
                        "She quickly gulps it down and wipes her mouth."
                        $ Girl.Spunk.remove("mouth")
                        $ Speed = 0
                        call Sex_Basic_Dialog(Girl,"swallowgood") # "That was real sweet, [Girl.Petname]."
                        $ Girl.FaceChange()
                elif Girl.Swallow:
                        $ Girl.FaceChange("bemused")
                        $ Girl.Spunk.append("mouth")
                        $ Girl.Spunk.append("chin")
                        $ Speed = 0
                        "She gags a little, but manages to swallow it."
                        $ Girl.Spunk.remove("mouth")
                        call Sex_Basic_Dialog(Girl,"swallow2") #"I'm starting to get used to that"
                        if Situation != "warn":
                                call Sex_Basic_Dialog(Girl,"notwarned") #" warn me next time?"
                        $ Girl.FaceChange()
                elif Girl.Addict >= 50 and Girl.Inbt < 400 and Girl.Blow < 10 and Girl != JubesX:
                        $ Girl.FaceChange("bemused", 1)
                        $ Girl.Spunk.append("mouth")
                        call AnyLine(Girl,". . .")
                        $ Girl.Spunk.remove("mouth")
                        $ Girl.Spunk.append("chin")
                        $ Girl.Spunk.append("hand")
                        $ Speed = 0
                        "She gags and spits it into her palm. Then she licks her lips, looks down at her dripping hand, blushes, and quickly wipes it off."
                        $ Girl.Spunk.remove("hand")
                        if Girl == RogueX:
                                ch_r "I. . . don't really like the taste of that."
                        elif Girl == KittyX:
                                ch_k "I'm not into that taste."
                        elif Girl == EmmaX:
                                ch_e "That certainly is. . . rich. . ."
                        elif Girl == LauraX:
                                ch_l "That certainly is. . . intense. . ."
                        elif Girl == JeanX:
                                ch_j "Well that was new. . ."
                        elif Girl == StormX:
                                ch_s "An uncommon flavor. . ."
                        #elif Girl == JubesX:
                        $ Girl.Addictionrate += 1
                        if "addictive" in Player.Traits:
                            $ Girl.Addictionrate += 1
                        $ Girl.FaceChange()
                        jump Girl_Orgasm_After
                elif (Girl.Addict >= 50 and Situation != "warn") or Girl == JubesX:
                        $ Girl.FaceChange("sexy")
                        $ Girl.Mouth = "tongue"
                        $ Girl.Spunk.append("mouth")
                        call AnyLine(Girl,". . .")
                        $ Girl.Spunk.remove("mouth")
                        $ Girl.Spunk.append("chin")
                        $ Girl.Spunk.append("hand")
                        $ Speed = 0
                        "She gags and spits it into her palm. Then she licks her lips, looks down, and drinks up what's in her palm."
                        $ Girl.Spunk.remove("hand")
                        if Girl == RogueX:
                                ch_r "I would be mad, but you taste so sweet, [Girl.Petname]."
                        elif Girl == KittyX:
                                ch_k "You coulda warned me."
                        elif Girl == EmmaX:
                                ch_e "I shouldn't reward such rude behavior. . . but it was nourishing."
                        elif Girl == LauraX:
                                ch_l "I should be mad, but. . ."
                        elif Girl == JeanX:
                                ch_j "Well that was new. . ."
                        elif Girl == StormX:
                                ch_s "An uncommon flavor. . ."
                        elif Girl == JubesX:
                                $ Girl.Eyes = "closed"
                                ch_v "Mmmmmmmm. . ."
                                $ Girl.Eyes = "surprised"
                                ch_v "Wow! . . that's. . . incredible. . ."
                                $ Girl.Eyes = "squint"
                                ch_v "Ok. . ."
                        $ Girl.FaceChange()
                        $ Girl.Statup("Inbt", 30, 2)
                        $ Girl.Statup("Inbt", 50, 2)
                else:
                        #hasn't swallowed before
                        if ApprovalCheck(Girl, 800, "LI") and ApprovalCheck(Girl, 400, "OI"):
                                $ Girl.FaceChange("angry")
                                $ Girl.Spunk.append("mouth")
                        else:
                                $ Girl.FaceChange("bemused")
                                $ Girl.Mouth = "tongue"
                                $ Girl.Spunk.append("mouth")
                        $ Girl.Spunk.append("chin")
                        call AnyLine(Girl,". . .")
                        $ Girl.Spunk.append("hand")
                        $ Speed = 0
                        "She gags and spits it into her palm."
                        if Situation != "warn":
                                if Girl == RogueX:
                                        ch_r "Hey, who said you could come in my mouth, [Girl.Petname]?"
                                elif Girl == KittyX:
                                        ch_k "Hey[Girl.like]what gives?"
                                elif Girl == EmmaX:
                                        ch_e "Did I say you could come in my mouth, [Girl.Petname]?"
                                elif Girl == LauraX:
                                        ch_l "What's the deal just cumming in my mouth like that?"
                                elif Girl == JeanX:
                                        ch_j "Hey! Gimme a warning next time!"
                                elif Girl == StormX:
                                        ch_s "[Girl.Petname], it is inconsiderate to not warn a girl. . ."
                        else:
                                call AnyLine(Girl,"Wha?")
                        menu:
                            extend ""
                            "Sorry about that.":
                                    $ Girl.Statup("Love", 80, 1)
                                    $ Girl.Addictionrate += 1
                                    if "addictive" in Player.Traits:
                                            $ Girl.Addictionrate += 1
                                    $ Girl.FaceChange("smile", 1)
                                    if Situation != "warn":
                                            if Girl == RogueX:
                                                    ch_r "Aw, well a little warning wouldn't hurt, [Girl.Petname]."
                                            elif Girl == KittyX:
                                                    ch_k "Well, just[Girl.like]now I know, I guess?"
                                            elif Girl == EmmaX:
                                                    ch_e "Very well. . ."
                                                    ch_e "Just warn me next time. . ."
                                            elif Girl == LauraX:
                                                    ch_l "Fine. . ."
                                                    ch_l "Just warn me next time. . ."
                                            elif Girl == JeanX:
                                                    ch_j "Ok then."
                                                    ch_j "Don't let it happen again."
                                            elif Girl == StormX:
                                                    ch_s "Just do better next time. . ."
                                    else:
                                            call AnyLine(Girl,". . . fine.")
                                    jump Girl_Orgasm_After
                            # end "sorry"
                            "Why don't you try swallowing it?":
                                    if ApprovalCheck(Girl, 1200):
                                            "She tentatively licks her hand, and then gulps it down."
                                            $ Girl.Spunk.remove("hand")
                                            $ Girl.FaceChange("sexy", 1)
                                            $ Girl.Spunk.append("mouth")
                                            $ Girl.Spunk.append("chin")
                                            if Girl == RogueX:
                                                    ch_r "Hmm, that really wasn't half bad, [Girl.Petname]."
                                            elif Girl == KittyX:
                                                    ch_k "Hmm. . . creamy? . ."
                                            elif Girl == EmmaX:
                                                    ch_e "Well, that was a bit of an acquired taste. . ."
                                            elif Girl == LauraX:
                                                    ch_l "Wasn't that bad. . ."
                                            elif Girl == JeanX:
                                                    ch_j "Hmmm. . . robust. . ."
                                            elif Girl == StormX:
                                                    ch_s "That is. . . uncommon. . ."
                                            $ Girl.Statup("Obed", 50, 10,Alt=[[JeanX],900,10]) #+10 for Jean
                                            $ Girl.Spunk.remove("mouth")
                                    elif ApprovalCheck(Girl, 1200, "OI", Bonus = (Girl.Addict*10)):
                                            $ Girl.FaceChange("bemused", 1)
                                            $ Girl.Brows = "normal"
                                            $ Girl.Mouth = "sad"
                                            $ Girl.Spunk.remove("hand")
                                            $ Girl.Spunk.append("mouth")
                                            $ Girl.Spunk.append("chin")
                                            "She scowls a bit, but licks her hand clean as she does so, and swallows it down."
                                            $ Girl.Spunk.remove("mouth")
                                            if Girl == RogueX:
                                                    ch_r "I'm not really a fan of that, [Girl.Petname]."
                                            elif Girl == KittyX:
                                                    ch_k "It's. . . not terrible."
                                            elif Girl == EmmaX:
                                                    ch_e "I can't say that it would be my favorite flavor. . ."
                                            elif Girl == LauraX:
                                                    ch_l "Not my favorite flavor. . ."
                                            elif Girl == JeanX:
                                                    ch_j "Eh. . . could be worse."
                                            elif Girl == StormX:
                                                    ch_s "That was. . . fine. . ."
                                            $ Girl.Statup("Obed", 50, 10,Alt=[[JeanX],900,10]) #+10 for Jean
                                    else:
                                            $ Girl.Spunk.remove("hand")
                                            "She scowls at you and wipes her hand off. Then she licks her lips."
                                            jump Girl_Orgasm_After
                            #end "why not swallow"
                            "Swallow it, now.":
                                    $ Girl.Statup("Love", 30, -1, 1)
                                    $ Girl.Statup("Love", 50, -1, 1)
                                    $ Girl.Statup("Love", 80, -1, 1)
                                    if ApprovalCheck(Girl, 1200, "OI") or Girl.Addict >= 50:
                                            $ Girl.FaceChange("sad", 1)
                                            $ Girl.Spunk.append("mouth")
                                            $ Girl.Spunk.append("chin")
                                            $ Girl.Spunk.remove("hand")
                                            "She scowls a bit, but licks her hand clean as she does so, and swallows it down."
                                            $ Girl.Spunk.remove("mouth")
                                            if Girl == RogueX:
                                                    ch_r "I'm not really a fan of that, [Girl.Petname]."
                                            elif Girl == KittyX:
                                                    ch_k "That's. . . not awful."
                                            elif Girl == EmmaX:
                                                    ch_e "I can't say that it would be my favorite flavor. . ."
                                            elif Girl == LauraX:
                                                    ch_l "Not my favorite flavor. . ."
                                            elif Girl == JeanX:
                                                    ch_j "Eh. . . could be worse."
                                            elif Girl == StormX:
                                                    ch_s "That is. . . fine. . ."
                                            $ Girl.Statup("Obed", 50, 10,Alt=[[JeanX],900,10]) #+10 for Jean
                                    else:
                                            $ Girl.Spunk.remove("hand")
                                            "She scowls at you and wipes her hand off. Then she licks her lips."
                                            jump Girl_Orgasm_After

                jump Girl_Swallowed
                #end if not asked/auto / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

    $ Situation = 0
    "You ask if you can cum in her mouth."
    if renpy.showing(Girl.Tag+"_PJ_Animation"): #if renpy.showing("Rogue_PJ_Animation"):
                call expression Girl.Tag + "_Kissing_Launch" pass (Trigger,0)
    elif renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"): #if renpy.showing("Rogue_Doggy"):
            call expression Girl.Tag+"_HJ_Launch" pass ("cum")

    if "full" in Girl.RecentActions:
            pass

    elif Girl.Swallow >= 5 or "hungry" in Girl.Traits:
            # If she's swallowed 5 times,
            $ Girl.FaceChange("sucking")
            if not renpy.showing(Girl.Tag+"_BJ_Animation"): #if not renpy.showing("Rogue_BJ_Animation"):
                call expression Girl.Tag+"_BJ_Launch" pass ("cum")
                $ Speed = 2
                "She nods and bends down to put the tip between her lips."
            else:
                $ Speed = 2
                "She nods and hums a \"yes\" sound."
            $ Player.Spunk = 1
            $ Girl.Spunk.append("mouth")
            $ Girl.Spunk.append("chin")
            call AnyLine(Girl,". . .")
            "After you cum, she quickly gulps it down and wipes her mouth."
            $ Girl.FaceChange("sexy")
            $ Speed = 0
            call Sex_Basic_Dialog(Girl,"swallowgood") #"That was real sweet, [Girl.Petname], thanks for the head's up."
            $ Girl.Spunk.remove("mouth")
            jump Girl_Swallowed

    elif Girl.Addict >= 80 and Girl.Swallow:
            #addicted
            $ Girl.Brows = "confused"
            $ Girl.Eyes = "manic"
            if not renpy.showing(Girl.Tag+"_BJ_Animation"): #if not renpy.showing("Rogue_BJ_Animation"):
                call expression Girl.Tag+"_BJ_Launch" pass ("cum")
                $ Speed = 2
                "She looks a bit quizzical, but gently puts the tip to her lips, just as you blow."
            else:
                $ Speed = 2
                "She nods and hums a \"yes\" sound."
            $ Girl.Mouth = "sucking"
            $ Player.Spunk = 1
            $ Girl.Spunk.append("mouth")
            call AnyLine(Girl,". . .")
            $ Speed = 0
            "She gags a little, but quickly swallows it."
            $ Girl.FaceChange("sexy")
            $ Girl.Mouth = "smile"
            call Sex_Basic_Dialog(Girl,"swallow2") #"I'm starting to get used to that."
            call Sex_Basic_Dialog(Girl,"notwarned") #"I could use a warning next time. . ."
            $ Girl.Spunk.remove("mouth")
            $ Girl.Statup("Inbt", 200, 5)
            jump Girl_Swallowed

    elif Girl.Swallow:
            if ApprovalCheck(Girl, 900):
                $ Girl.Brows = "confused"
                if renpy.showing(Girl.Tag+"_TJ_Animation"): #if renpy.showing("Rogue_TJ_Animation"):
                    $ Girl.FaceChange("kiss")
                    $ Speed = 5
                    "She looks a bit confused, but gently puts the tip to her lips."
                elif not renpy.showing(Girl.Tag+"_BJ_Animation"): #if not renpy.showing("Rogue_BJ_Animation"):
                    call expression Girl.Tag+"_BJ_Launch" pass ("cum")
                    $ Speed = 2
                    "She looks a bit quizzical, but gently puts the tip to her lips, just as you blow."
                else:
                    $ Speed = 2
                    if Girl == KittyX:
                            ch_k "[[mumbled] Huh?"
                    else:
                            "She tilts her head and hums a \"huh?\" sound."
                $ Girl.Mouth = "sucking"
                $ Girl.Spunk.append("chin")
                $ Girl.Spunk.append("mouth")
                $ Girl.Brows = "normal"
                $ Girl.Eyes = "sexy"
                $ Player.Spunk = 1
                $ Girl.Spunk.append("mouth")
                call AnyLine(Girl,". . .")
                "She gags a little, but quickly swallows it."
                $ Speed = 0
                $ Girl.FaceChange("sexy")
                call Sex_Basic_Dialog(Girl,"swallow2") #"I'm starting to get used to that."
                $ Girl.Spunk.remove("mouth")
                jump Girl_Swallowed

    #If she hasn't swallowed or doesn't automatically want to. . .

    if  ApprovalCheck(Girl, 300, "LI") or ApprovalCheck(Girl, 300, "OI"):
        $ Girl.FaceChange("bemused")
        $ Girl.Eyes = "sexy"
    else:
        $ Girl.FaceChange("angry")

    $ Speed = 0

    if Girl == RogueX:
            if "full" in Girl.RecentActions:
                    ch_r "I'm feeling a bit. . . \"full\" right now, [Girl.Petname]. . ."
            else:
                    ch_r "What makes you think I'd want that, [Girl.Petname]?"
    elif Girl == KittyX:
            if "full" in Girl.RecentActions:
                ch_k "I've kinda had enough for now? . ."
            else:
                ch_k "That doesn't sound too appetizing. . ."
    elif Girl == EmmaX:
            if "full" in Girl.RecentActions:
                    ch_e "I couldn't finish another drop, [Girl.Petname]. . ."
            else:
                    ch_e "I can't imagine why I would. . ."
    elif Girl == LauraX:
            if "full" in Girl.RecentActions:
                    ch_l "I'm stuffed, [Girl.Petname]. . ."
            else:
                    ch_l "I don't know why. . ."
    elif Girl == JeanX:
            if "full" in Girl.RecentActions:
                    ch_j "I'm a bit full, [Girl.Petname]. . ."
            else:
                    ch_j "As if. . ."
    elif Girl == StormX:
            if "full" in Girl.RecentActions:
                    ch_s "I could not take any more, [Girl.Petname]. . ."
            else:
                    ch_s "I do not see why I would. . ."
    elif Girl == JubesX:
            if "full" in Girl.RecentActions:
                    ch_v "Even I'm filled up already, [Girl.Petname]. . ."
            else:
                    ch_v "I don't think I would want to. . ."
    menu:
        extend ""
        "Sorry about that.":
                $ Girl.Statup("Love", 80, 3)
                $ Girl.Addictionrate += 1
                if "addictive" in Player.Traits:
                        $ Girl.Addictionrate += 1
                $ Girl.FaceChange("smile", 1)
                if Girl == RogueX:
                        ch_r "Well, maybe it would taste as sweet as your words, [Girl.Petname]."
                elif Girl == KittyX:
                        ch_k "Can't hurt to ask, right?"
                elif Girl == EmmaX:
                        ch_e "It is a tempting offer. . ."
                elif Girl == LauraX:
                        ch_l "Hmm. . ."
                elif Girl == JeanX:
                        ch_j "Uh-huh. . ."
                elif Girl == StormX:
                        ch_s "I appreciate you asking. . ."
                elif Girl == JubesX:
                        ch_v "Well, doesn't hurt to ask. . ."
                if ApprovalCheck(Girl, 1200, TabM=1) and "full" not in Girl.RecentActions:
                        $ Girl.Statup("Inbt", 30, 3)
                        $ Girl.Statup("Inbt", 70, 2)
                        $ Girl.FaceChange("sexy", 1)
                        if Girl == RogueX:
                                ch_r "Maybe it is worth a try. . ."
                        elif Girl == KittyX:
                                ch_k "It's[Girl.like]worth a shot."
                        elif Girl == EmmaX:
                                ch_e "Perhaps a little bit. . ."
                        elif Girl == LauraX:
                                ch_l "Maybe a little. . ."
                        elif Girl == JeanX:
                                ch_j "I guess I could. . ."
                        elif Girl == StormX:
                                ch_s "I can try."
                        elif Girl == JubesX:
                                ch_v "Well, why not, you only live once. . ."
                else:
                        jump Girl_Handy_Finish

        "Give it a try, you might like it." if "full" not in Girl.RecentActions:
                if ApprovalCheck(Girl, 1200, TabM=1):
                        $ Girl.Statup("Obed", 50, 5)
                        $ Girl.Statup("Obed", 70, 3)
                        $ Girl.Brows = "confused"
                        $ Girl.Eyes = "sexy"
                        if Girl == RogueX:
                                ch_r "If you say so. . ."
                        elif Girl == KittyX:
                                ch_k "I guess. . ."
                        elif Girl == EmmaX:
                                ch_e "If you insist. . ."
                        elif Girl == LauraX:
                                ch_l "If you insist. . ."
                        elif Girl == JeanX:
                                ch_j "I don't know about that. . ."
                        elif Girl == StormX:
                                ch_s "I am unsure. . ."
                        elif Girl == JubesX:
                                ch_v "I, um. . . Maybe? . ."
                else:
                        $ Girl.Addictionrate += 1
                        if "addictive" in Player.Traits:
                            $ Girl.Addictionrate += 1
                        $ Girl.Blush = 1
                        if Girl == RogueX:
                                ch_r "You wish, [Girl.Petname]."
                        elif Girl == KittyX:
                                ch_k "You wish, [Girl.Petname]."
                        elif Girl == EmmaX:
                                ch_e "I highly doubt that, [Girl.Petname]."
                        elif Girl == LauraX:
                                ch_l "You think I don't have a nose, [Girl.Petname]?"
                        elif Girl == JeanX:
                                ch_j "Yeah, haven't heard that one before. . ."
                        elif Girl == StormX:
                                ch_s "That is. . . unlikely. . ."
                        elif Girl == JubesX:
                                ch_v "I, um. . . kinda doubt that. . ."
                        jump Girl_Handy_Finish

        "Seriously, put it in your mouth.":
                if ApprovalCheck(Girl, 1500, "LI", TabM=1) or ApprovalCheck(Girl, 1200, "OI", TabM=1):
                        $ Girl.FaceChange("sucking", 1)
                elif ApprovalCheck(Girl, 1000, "OI", Bonus = (Girl.Addict*10)): #Mild addiction included
                        $ Girl.FaceChange("angry", 1)
                else:
                        #You insisted, she refused.
                        $ Girl.FaceChange("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        call expression Girl.Tag+"_HJ_Launch" pass ("cum")
                        call expression Girl.Tag+"_HJ_Reset"
                        $ Girl.Statup("Love", 50, -3, 1)
                        $ Girl.Statup("Love", 80, -4, 1)
                        if Girl == RogueX:
                                ch_r "Well if that's your attitude you can handle your own business."
                        elif Girl == KittyX:
                                ch_k "You can handle it yourself then."
                        elif Girl == EmmaX:
                                ch_e "I think you overestimate your charms."
                        elif Girl == LauraX:
                                ch_l "Seriously, you eat a dick."
                        elif Girl == JeanX:
                                ch_j "Fuck off."
                        elif Girl == StormX:
                                ch_s "No."
                        elif Girl == JubesX:
                                ch_v "I don't need this. . ."
                        $ Girl.Statup("Obed", 30, -1, 1,Alt=[[JeanX],900,3]) #+3 for Jean
                        $ Girl.Statup("Obed", 50, -1, 1)
                        $ Girl.RecentActions.append("angry")
                        $ Girl.DailyActions.append("angry")
                        $ Line = 0
                        return
                $ Girl.Statup("Obed", 50, 10,Alt=[[JeanX],900,10]) #+10 for Jean
                $ Girl.Statup("Obed", 70, 5)

    if not renpy.showing(Girl.Tag+"_BJ_Animation"): #if not renpy.showing("Rogue_BJ_Animation"):
        call expression Girl.Tag+"_BJ_Launch" pass ("cum")
    $ Speed = 2
    if ApprovalCheck(Girl, 1200):
            "She gently puts the tip to her lips, just as you blow."
    else:
            "She tentatively places the tip in her mouth, and you blast inside it."
            $ Girl.FaceChange("sexy")
            $ Girl.Statup("Love", 50, -3, 1)
            $ Girl.Statup("Love", 80, -4, 1)
    $ Girl.Mouth = "sucking"
    $ Player.Spunk = 1
    $ Girl.Spunk.append("chin")
    $ Girl.Spunk.append("mouth")
    call AnyLine(Girl,". . .")
    "She gags a little, but quickly swallows it."
    $ Speed = 0
    $ Girl.FaceChange("sexy")

    if ApprovalCheck(Girl, 1000) and Girl.Swallow >= 3:
            call Sex_Basic_Dialog(Girl,"swallow2") #"I'm starting to get used to that."
    elif ApprovalCheck(Girl, 800):
            call Sex_Basic_Dialog(Girl,"swallowfirst") #"I'm not really a fan of that, [Girl.Petname]."
    else:
            $ Girl.FaceChange("sad")
            call Sex_Basic_Dialog(Girl,"swallowfirst") #"I'm not really a fan of that, [Girl.Petname]."
    $ Girl.Statup("Inbt", 30, 3)
    $ Girl.Statup("Inbt", 50, 2)
    $ Girl.Blow += 1
    jump Girl_Swallowed
    #end Cum in mouth  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Creampie  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Creampie_P: #rkeljsv
        if Trigger == "sex" and Situation == "auto":
                $ Player.Cock = "in"
                $ Girl.Spunk.append("in")
                $ Player.Spunk = "in"
                $ Speed = 0
                if ApprovalCheck(Girl, 1300) or Girl.CreamP:
                        $ Girl.FaceChange("surprised")
                        "You come in her pussy. Her eyes widen in surprise, but she takes it in stride."
                        $ Girl.FaceChange("sexy")
                        if Girl.Lust >= 85:
                                call Girl_Cumming(Girl)
                else:
                        if Girl.Lust >= 85:
                                "You come in her pussy. Her eyes widen in surprise and she shakes a bit."
                                call Girl_Cumming(Girl)
                        else:
                                "You come in her pussy. Her eyes widen in surprise and she pulls out."
                        $ Player.Cock = "out"
                        $ Girl.FaceChange("angry")
                        if Girl == RogueX:
                                ch_r "Hey, a little warning next time, huh?"
                                $ Girl.FaceChange("bemused")
                                ch_r "Still, that didn't feel {i}so{/i} bad. . ."
                        elif Girl == KittyX:
                                ch_k "You coulda[Girl.like]warned me or something!"
                                $ Girl.FaceChange("bemused")
                                ch_k "It was pretty warm though. . ."
                        elif Girl == EmmaX:
                                ch_e "Perhaps some warning next time?"
                                $ Girl.FaceChange("bemused")
                                ch_e "Not that it didn't feel good at the time. . ."
                        elif Girl == LauraX:
                                ch_l "Hey, maybe a heads up?"
                                $ Girl.FaceChange("bemused")
                                ch_l "Not that it didn't feel good. . ."
                        elif Girl == JeanX:
                                ch_j "Hey! What was that!"
                                ch_j ". . ."
                                $ Girl.FaceChange("bemused")
                                ch_j "But it did feel kinda good. . ."
                        elif Girl == StormX:
                                ch_s "You could have warned me you would do that. . ."
                                $ Girl.FaceChange("bemused")
                                ch_s "It did feel amazing though. . ."
                        elif Girl == JubesX:
                                ch_v "I coulda used a little warning there!"
                                $ Girl.FaceChange("bemused")
                                ch_v "So warm inside. . ."
                jump Girl_Creampied

        #else (You ask her if it's ok):
        if ApprovalCheck(Girl, 1200) or Girl.CreamP:
                $ Girl.FaceChange("sexy")
                if Girl.CreamP >= 3:
                        "She smiles and speeds up her actions, causing you to erupt inside her."
                elif Girl.CreamP:
                        "She gets a michevious look and speeds up, you burst inside her."
                else:
                        "As you continue to pound her, she nods her head."
                $ Player.Cock = "in"
                $ Girl.Spunk.append("in")
                $ Player.Spunk = "in"
                $ Speed = 0
                if Girl.Lust >= 85:
                        call Girl_Cumming(Girl)
                $ Girl.Statup("Love", 90, 1)
                if Girl == RogueX:
                        ch_r "Hmm, you know how to fill me up {i}right.{/i}"
                elif Girl == KittyX:
                        ch_k "Hmm, cozy. . ."
                elif Girl == EmmaX:
                        ch_e "How very. . . filling."
                elif Girl == LauraX:
                        ch_l "Very. . . filling."
                elif Girl == JeanX:
                        ch_j "Very. . . warm."
                elif Girl == StormX:
                        ch_s "So pleasantly warm. . ."
                elif Girl == JubesX:
                        ch_v "So warm inside. . ."
                jump Girl_Creampied
        else:
                $ Girl.FaceChange("sexy")
                $ Girl.Statup("Love", 80, 2)
                $ Girl.Statup("Love", 90, 2)
                if Girl == RogueX:
                        ch_r "Thanks for the heads up *grunt* [Girl.Petname], but I'd rather you didn't."
                elif Girl == KittyX:
                        ch_k "Thanks for the warning, but maybe not this time?"
                elif Girl == EmmaX:
                        ch_e "Thanks for warning me *grunt* [Girl.Petname], but perhaps not."
                elif Girl == LauraX:
                        ch_l "Thanks for the heads up *grunt* [Girl.Petname], but let's not."
                elif Girl == JeanX:
                        ch_j "Yeah, let's not, time to pull out."
                elif Girl == StormX:
                        ch_s "Thank you, [Girl.Petname], but no. . ."
                elif Girl == JubesX:
                        ch_v "It could be nice, but no thanks. . ."
        jump Girl_Cum_Outside

#Start Anal Creampie  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Creampie_A:      #rkeljsv
        # These need conditionals added
        if Trigger == "anal" and Situation == "auto":
                $ Player.Cock = "anal"
                $ Girl.Spunk.append("anal")
                $ Player.Spunk = "anal"
                $ Speed = 0
                if ApprovalCheck(Girl, 1200) or Girl.CreamP:
                        $ Girl.FaceChange("surprised", 1)
                        "You come in her ass. Her eyes widen in surprise, but she takes it in stride."
                        $ Girl.FaceChange("sexy")
                        if Girl.Lust >= 85:
                                call Girl_Cumming(Girl)
                else:
                        if Girl.Lust >= 85:
                                "You come in her ass. Her eyes widen in surprise and she shakes a bit."
                                call Girl_Cumming(Girl)
                        else:
                                "You come in her ass. Her eyes widen in surprise and she pulls out."
                        $ Player.Cock = "out"
                        $ Girl.FaceChange("angry")
                        if Girl == RogueX:
                                ch_r "Hey, warn a girl, huh?"
                                $ Girl.FaceChange("bemused")
                                ch_r "but. . . I guess it did feel pretty good. . ."
                        elif Girl == KittyX:
                                ch_k "Maybe a little warning next time?"
                                $ Girl.FaceChange("bemused")
                                ch_k "that was pretty warm though. . ."
                        elif Girl == EmmaX:
                                ch_e "No advanced warning, [Girl.Petname]?"
                                $ Girl.FaceChange("bemused")
                                ch_e "I suppose it was rather. . . filling though."
                        elif Girl == LauraX:
                                ch_l "No advanced warning, [Girl.Petname]?"
                                $ Girl.FaceChange("bemused")
                                ch_l "That was pretty filling. . ."
                        elif Girl == JeanX:
                                ch_j "Hey! What was that!"
                                ch_j ". . ."
                                $ Girl.FaceChange("bemused")
                                ch_j "But it did feel kinda good. . ."
                        elif Girl == StormX:
                                ch_s "You could have warned me you would do that. . ."
                                $ Girl.FaceChange("bemused")
                                ch_s "It did feel amazing though. . ."
                        elif Girl == JubesX:
                                ch_v "I coulda used a little warning there!"
                                $ Girl.FaceChange("bemused")
                                ch_v "So warm inside. . ."
                jump Girl_Creampied

        #else (You ask her if it's ok):
        if ApprovalCheck(Girl, 1200) or Girl.CreamP:
                $ Girl.FaceChange("sexy")
                if Girl.CreamP >= 3:
                        "She smiles and speeds up her actions, causing you to erupt inside her."
                elif Girl.CreamP:
                        "She gets a michevious look and speeds up, you burst inside her."
                else:
                        "As you continue to pound her, she nods her head."
                $ Player.Cock = "anal"
                $ Girl.Spunk.append("anal")
                $ Player.Spunk = "anal"
                $ Speed = 0
                if Girl.Lust >= 85:
                        call Girl_Cumming(Girl)
                $ Girl.Statup("Love", 90, 1)
                if Girl == RogueX:
                        ch_r "Hmm, I feel so full. . ."
                elif Girl == KittyX:
                        ch_k "Wow, I feel so full. . ."
                elif Girl == EmmaX:
                        ch_e "Mmmm, I feel so full. . ."
                elif Girl == LauraX:
                        ch_l "Mmmm, so full. . ."
                elif Girl == JeanX:
                        ch_j "Very. . . warm."
                elif Girl == StormX:
                        ch_s "So pleasantly warm. . ."
                elif Girl == JubesX:
                        ch_v "So warm inside. . ."
                jump Girl_Creampied
        else:
                $ Girl.FaceChange("sexy")
                $ Girl.Statup("Love", 80, 2)
                if Girl == RogueX:
                        ch_r "Thanks for the heads up *grunt* [Girl.Petname], but I'd rather you didn't."
                elif Girl == KittyX:
                        ch_k "Thanks for the warning, but maybe not this time?"
                elif Girl == EmmaX:
                        ch_e "Thanks for warning me *grunt* [Girl.Petname], but perhaps not."
                elif Girl == LauraX:
                        ch_l "Thanks for warning me *grunt* [Girl.Petname], but I don't think so."
                elif Girl == JeanX:
                        ch_j "Yeah, let's not, time to pull out."
                elif Girl == StormX:
                        ch_s "Thank you, [Girl.Petname], but no. . ."
                elif Girl == JubesX:
                        ch_v "It could be nice, but no thanks. . ."
        jump Girl_Cum_Outside

#Start Facial  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Facial:  #rkeljsj
        if renpy.showing(Girl.Tag+"_BJ_Animation"): #if renpy.showing("Rogue_BJ_Animation"):
                if Girl.Addict >= 60 and ApprovalCheck(Girl, 1000, "I", Bonus = ((Girl.Addict*10)- Girl.Obed)) and Girl.Swallow:
                        jump Manic_Suck
                call expression Girl.Tag+"_HJ_Launch" pass ("cum")
                $ Speed = 2
                if "hair" in Girl.Spunk:
                        pass
                elif "facial" in Girl.Spunk:
                        $ Girl.Spunk.append("hair")
                else:
                        $ Girl.Spunk.append("facial")
                "You pull out of her mouth with a pop, and she strokes you off. You spray all over her face."
                $ Speed = 0

        elif renpy.showing(Girl.Tag+"_TJ_Animation"): #if renpy.showing("Rogue_TJ_Animation"):
                if "hair" in Girl.Spunk:
                        pass
                elif "facial" in Girl.Spunk:
                        $ Girl.Spunk.append("hair")
                else:
                        $ Girl.Spunk.append("facial")
                if not Girl.Tit:
                        "She glances up but continues to rub her breasts up and down on your cock. When you come, you spray all over her face."
                else:
                        "As you're about to finish, you aim squarely at her face, and spray all over it."
                $ Speed = 0

        elif renpy.showing(Girl.Tag+"_HJ_Animation"): #if renpy.showing("Rogue_HJ_Animation"):
                if "hair" in Girl.Spunk:
                        pass
                elif "facial" in Girl.Spunk:
                        $ Girl.Spunk.append("hair")
                else:
                        $ Girl.Spunk.append("facial")
                if not Girl.Hand:
                        "She looks a bit confused but continues to stroke while staring at it like a live snake. When you finish, you spray all over her face."
                else:
                        "As you're about to finish, you aim squarely at her face, and spray all over it."
                $ Speed = 0
        elif renpy.showing(Girl.Tag+"_PJ_Animation"): #if renpy.showing("Rogue_PJ_Animation"):
                call expression Girl.Tag + "_Breasts_Launch" pass (Trigger,0)
                if "hair" in Girl.Spunk:
                        pass
                elif "facial" in Girl.Spunk:
                        $ Girl.Spunk.append("hair")
                else:
                        $ Girl.Spunk.append("facial")
                "As you're about to finish, you aim squarely at her face, and spray all over it."
                $ Speed = 0
        else:
                call expression Girl.Tag+"_HJ_Launch" pass ("cum")
                $ Speed = 2
                if "hair" in Girl.Spunk:
                        pass
                elif "facial" in Girl.Spunk:
                        $ Girl.Spunk.append("hair")
                else:
                        $ Girl.Spunk.append("facial")
                "As you're about to finish, you pull out, aim squarely at her face, and spray all over it."
                $ Speed = 0
        if Girl == RogueX:
                if Situation == "warn":
                    ch_r "Thanks for the warning, [Girl.Petname]. Such a mess though. . ."
                else:
                    ch_r "What a mess, you could have warned me."
        elif Girl == KittyX:
                if Situation == "warn":
                    ch_k "Whew, thanks for the head's up."
                else:
                    ch_k "Huh, nice warning there, [Girl.Petname]."
        elif Girl == EmmaX:
                if Situation == "warn":
                    ch_e "I appreciate the warning. . . perhaps not the mess though. . ."
                else:
                    ch_e "What a mess, a warning would have been appreciated."
        elif Girl == LauraX:
                if Situation == "warn":
                    ch_l "Thanks for the warning. . . maybe not the mess though. . ."
                else:
                    ch_l "What a mess, maybe a heads up next time?"
        elif Girl == JeanX:
                if Situation == "warn":
                    ch_j "Wow, you really made a mess there. . ."
                else:
                    ch_j "Hey, a little warning?"
        elif Girl == StormX:
                if Situation == "warn":
                    ch_s "Thank you for the warning, for what little good it did. . ."
                else:
                    ch_s "Well this is a fine mess you have gotten me into."
        elif Girl == JubesX:
                if Situation == "warn":
                    ch_v "Ugh, I've been slimed. . ."
                else:
                    ch_v "Ugh, I've been slimed. . . warn me next time, uh?"
        $ Player.Cock = "out"
        jump Girl_Orgasm_After

#Start titjob spunk  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_TitSpunk:  #rkeljsv
        if renpy.showing(Girl.Tag+"_BJ_Animation"): #if renpy.showing("Rogue_BJ_Animation"):
                if Girl.Addict >= 60 and ApprovalCheck(Girl, 1000, "I", Bonus = ((Girl.Addict*10)- Girl.Obed)) and Girl.Swallow:
                            jump Manic_Suck

        #if not renpy.showing("Rogue_TJ_Animation") and not renpy.showing("Rogue_HJ_Animation") and not renpy.showing("Rogue_BJ_Animation"):
        if renpy.showing(Girl.Tag+"_PJ_Animation"): #if renpy.showing("Rogue_PJ_Animation"):
                call expression Girl.Tag + "_Breasts_Launch" pass (Trigger,0)
        elif not renpy.showing(Girl.Tag+"_TJ_Animation") and not renpy.showing(Girl.Tag+"_HJ_Animation") and not renpy.showing(Girl.Tag+"_BJ_Animation"):
                call expression Girl.Tag+"_HJ_Launch" pass ("cum")
        $ Girl.Spunk.append("tits")
        $ Speed = 0
        "As you're about to finish, you speed up and spray all over her chest."
        if Girl == RogueX:
                if Situation == "warn":
                    ch_r "Thanks for the warning, [Girl.Petname]. Such a mess though. . ."
                else:
                    ch_r "What a mess, you could have warned me."
        elif Girl == KittyX:
                if Situation == "warn":
                    ch_k "Whew, thanks for the head's up."
                else:
                    ch_k "Huh, nice warning there, [Girl.Petname]."
        elif Girl == EmmaX:
                if Situation == "warn":
                    ch_e "I appreciate the warning. . . perhaps not the mess though. . ."
                else:
                    ch_e "What a mess, a warning would have been appreciated."
        elif Girl == LauraX:
                if Situation == "warn":
                    ch_l "Thanks for the warning. . . maybe not the mess though. . ."
                else:
                    ch_l "What a mess, maybe a heads up next time?"
        elif Girl == JeanX:
                if Situation == "warn":
                    ch_j "Wow, you really made a mess there. . ."
                else:
                    ch_j "Hey, a little warning?"
        elif Girl == StormX:
                if Situation == "warn":
                    ch_s "Thank you for the warning, for what little good it did. . ."
                else:
                    ch_s "Well this is a fine mess you have gotten me into."
        elif Girl == JubesX:
                if Situation == "warn":
                    ch_v "Ugh, I've been slimed. . ."
                else:
                    ch_v "Ugh, I've been slimed. . . warn me next time, uh?"
        jump Girl_Orgasm_After

# Start Spunk back  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Cum_Outside:  #rkeljsv
        if Trigger != "foot":
            if renpy.showing(Girl.Tag+"_PJ_Animation"): #if renpy.showing("Rogue_PJ_Animation"):
                call expression Girl.Tag + "_Middle_Launch" pass (Trigger,0)

            elif Girl.Pose != "doggy" and (Girl == JeanX or Girl == StormX): # temporary until these girls get a front pose
                call expression Girl.Tag + "_Middle_Launch" pass (Trigger,0)
#            elif Girl.Pose == "doggy" and (Girl == EmmaX):  # temporary until these girls get a rear pose
#                pass

            else:
                call expression Girl.Tag+"_Sex_Launch" pass ("hotdog") #call Rogue_Doggy_Launch("hotdog")
        $ Speed = 0
        if Girl.Addict >= 60 and ApprovalCheck(Girl, 1000, "I", Bonus = ((Girl.Addict*10)- Girl.Obed))  and Girl.Swallow:
                $ Girl.Eyes = "manic"
                $ Girl.Blush = 1
                call expression Girl.Tag+"_BJ_Launch" pass ("cum")
                if Trigger == "sex":
                    "You pull out of her pussy with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
                elif Trigger == "anal":
                    "You pull out of her ass with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
                $ Girl.Mouth = "lipbite"
                $ Girl.Spunk.append("mouth")
                "When she finishes, she licks her lips."
                $ Girl.FaceChange("bemused")
                $ Girl.Spunk.remove("mouth")
                if Girl == RogueX:
                        ch_r "Well, [Girl.Petname], I just couldn't let that go to waste."
                elif Girl == KittyX:
                        ch_k "Sorry, that's just[Girl.like]sooooo good."
                elif Girl == EmmaX:
                        ch_e "Well, [Girl.Petname], I just couldn't let that go to waste."
                elif Girl == LauraX:
                        ch_l "I couldn't let that go to waste."
                elif Girl == JeanX:
                        ch_j "Mmm. . ."
                elif Girl == StormX:
                        ch_s "That would have been wasteful. . ."
                elif Girl == JubesX:
                        ch_v "Wouldn't want to let all that go to waste. . ."
                $ Girl.Statup("Obed", 80, -5)
                $ Girl.Statup("Inbt", 200, 10)
                jump Girl_Swallowed
        if Trigger != "foot":
            $ Player.Cock = "out"
        if Girl.Pose == "doggy":
                $ Girl.Spunk.append("back")
                if Trigger == "sex":
                        "You pull out of her pussy with a pop and spray all over her backside."
                elif Trigger == "anal":
                        "You pull out of her ass with a pop and spray all over her backside."
                else:
                        "You pick up the pace and with a grunt you spray all over her backside."
        else:
                $ Girl.Spunk.append("belly")
                if Trigger == "sex":
                        "You pull out of her pussy with a pop and spray all over her stomach."
                elif Trigger == "anal":
                        "You pull out of her ass with a pop and spray all over her stomach."
                else:
                        "You pick up the pace and with a grunt you spray all over her stomach."


        if Girl.Addict >= 60 and ApprovalCheck(Girl, 800, "I", Bonus = ((Girl.Addict*10)- Girl.Obed)) and Girl.Swallow:
                    #if she's manic and has swallowed
                    $ Girl.Eyes = "manic"
                    $ Girl.Blush = 1
                    "[Girl.Name]'s eyes widen with desire, and she quickly wipes a bit off with her hand, then licks her fingers clean."
                    $ Girl.FaceChange("manic", 1)
                    $ Girl.Spunk.append("mouth")
                    $ Girl.Mouth = "smile"
                    if Girl == RogueX:
                            ch_r "Well, [Girl.Petname], I just couldn't let that go to waste."
                    elif Girl == KittyX:
                            ch_k "Sorry, that's just[Girl.like]sooooo good."
                    elif Girl == EmmaX:
                            ch_e "Well, [Girl.Petname], I just couldn't let that go to waste."
                    elif Girl == LauraX:
                            ch_l "I couldn't let that go to waste."
                    elif Girl == JeanX:
                            ch_j "Mmm. . ."
                    elif Girl == StormX:
                            ch_s "That would have been wasteful. . ."
                    elif Girl == JubesX:
                            ch_v "Wouldn't want to let all that go to waste. . ."
                    $ Girl.Spunk.remove("mouth")
                    $ Girl.Statup("Inbt", 50, 3)
                    jump Girl_Swallowed
        #end manic suck

        #else . . .
        $ Girl.FaceChange("sexy", 1)
        if Girl == RogueX:
                ch_r "What a mess. . ."
        elif Girl == KittyX:
                ch_k "Mmmm, all over the place. . ."
        elif Girl == EmmaX:
                ch_e "Hmm. . . you do make a mess. . ."
        elif Girl == LauraX:
                ch_l "Hmm. . . what a mess. . ."
        elif Girl == JeanX:
                ch_j "Ick. . ."
        elif Girl == StormX:
                ch_s "Well this is a fine mess you have gotten me into."
        elif Girl == JubesX:
                ch_v "Ugh, I've been slimed. . ."
#        call expression Girl.Tag+"_Doggy_Reset"
        jump Girl_Orgasm_After

   # Start Spunk back  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
#label Girl_SpunkBelly: #dead?
#        if Trigger != "foot":
#            $ Girl.Pose = "sex"
#            call expression Girl.Tag+"_Sex_Launch" pass ("hotdog") #call Rogue_Doggy_Launch("hotdog")
#        $ Speed = 0
#        if Girl.Addict >= 60 and ApprovalCheck(Girl, 1000, "I", Bonus = ((Girl.Addict*10)- Girl.Obed))  and Girl.Swallow:
#                $ Girl.Eyes = "manic"
#                $ Girl.Blush = 1
#                call expression Girl.Tag+"_BJ_Launch" pass ("cum")
#                if Trigger == "sex":
#                    "You pull out of her pussy with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
#                elif Trigger == "anal":
#                    "You pull out of her ass with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
#                $ Girl.Mouth = "lipbite"
#                $ Girl.Spunk.append("mouth")
#                "When she finishes, she licks her lips."
#                $ Girl.FaceChange("bemused")
#                $ Girl.Spunk.remove("mouth")
#                if Girl == RogueX:
#                        ch_r "Well, [Girl.Petname], I just couldn't let that go to waste."
#                elif Girl == KittyX:
#                        ch_k "Sorry, that's just[Girl.like]sooooo good."
#                elif Girl == EmmaX:
#                        ch_e "Well, [Girl.Petname], I just couldn't let that go to waste."
#                elif Girl == LauraX:
#                        ch_l "I couldn't let that go to waste."
#                elif Girl == JeanX:
#                        ch_j "Mmm. . ."
#                elif Girl == StormX:
#                        ch_s "That would have been wasteful. . ."
#                $ Girl.Statup("Obed", 80, -5)
#                $ Girl.Statup("Inbt", 200, 10)
#                jump Girl_Swallowed
#        if Trigger != "foot":
#            $ Player.Cock = "out"
#        $ Girl.Spunk.append("back")
#        if Trigger == "sex":
#                "You pull out of her pussy with a pop and spray all over her stomach."
#        elif Trigger == "anal":
#                "You pull out of her ass with a pop and spray all over her stomach."
#        else:
#                "You pick up the pace and with a grunt you spray all over her stomach."

#        if Girl.Addict >= 60 and ApprovalCheck(Girl, 800, "I", Bonus = ((Girl.Addict*10)- Girl.Obed)) and Girl.Swallow:
#                    #if she's manic and has swallowed
#                    $ Girl.Eyes = "manic"
#                    $ Girl.Blush = 1
#                    "[Girl.Name]'s eyes widen with desire, and she quickly wipes a bit off with her hand, then licks her fingers clean."
#                    $ Girl.FaceChange("manic", 1)
#                    $ Girl.Spunk.append("mouth")
#                    $ Girl.Mouth = "smile"
#                    if Girl == RogueX:
#                            ch_r "Well, [Girl.Petname], I just couldn't let that go to waste."
#                    elif Girl == KittyX:
#                            ch_k "Sorry, that's just[Girl.like]sooooo good."
#                    elif Girl == EmmaX:
#                            ch_e "Well, [Girl.Petname], I just couldn't let that go to waste."
#                    elif Girl == LauraX:
#                            ch_l "I couldn't let that go to waste."
#                    elif Girl == JeanX:
#                            ch_j "Mmm. . ."
#                    elif Girl == StormX:
#                            ch_s "That would have been wasteful. . ."
#                    $ Girl.Spunk.remove("mouth")
#                    $ Girl.Statup("Inbt", 50, 3)
#                    jump Girl_Swallowed
#        #end manic suck

#        #else . . .
#        $ Girl.FaceChange("sexy", 1)
#        if Girl == RogueX:
#                ch_r "What a mess. . ."
#        elif Girl == KittyX:
#                ch_k "Mmmm, all over the place. . ."
#        elif Girl == EmmaX:
#                ch_e "Hmm. . . you do make a mess. . ."
#        elif Girl == LauraX:
#                ch_l "Hmm. . . what a mess. . ."
#        elif Girl == JeanX:
#                ch_j "Ick. . ."
#        jump Girl_Orgasm_After

#Start Handy finish  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Handy_Finish: #rkeljsv
        if renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"): #if renpy.showing("Rogue_Doggy"):
                call expression Girl.Tag+"_Doggy_Reset"
                call expression Girl.Tag+"_Sex_Reset"
                if Trigger == "hotdog":
                    "She bends down and begins to stroke you off."
                else:
                    "She grins and pulls out with a pop, and begins to stroke you off."
                $ Speed = 2
        elif renpy.showing(Girl.Tag+"_BJ_Animation"): #if renpy.showing("Rogue_BJ_Animation"):
                call expression Girl.Tag+"_HJ_Launch" pass ("cum")
                $ Speed = 2
                "She slides her lips off your cock, and begins to stroke you off."
        elif renpy.showing(Girl.Tag+"_PJ_Animation"): #if renpy.showing("Rogue_PJ_Animation"):
                call expression Girl.Tag + "_Breasts_Launch" pass (Trigger,0)
        else:
                call expression Girl.Tag+"_HJ_Launch" pass ("cum")
                $ Speed = 2
        $ Girl.Spunk.append("hand")
        "She grins and speeds up her efforts, placing her left hand over your tip. You burst all over her hands."
        $ Speed = 0

        if Girl.Addict > 80 or "hungry" in Girl.Traits:
                $ Girl.Eyes = "manic"
                $ Girl.Spunk.remove("hand")
                $ Girl.Spunk.append("mouth")
                $ Girl.Mouth = "smile"
                "She licks her hands off with a satisfied grin."
                $ Girl.Spunk.remove("mouth")
                call AnyLine(Girl,"Hmmm. . .")
        else:
                $ Girl.FaceChange("bemused")
                $ Girl.Spunk.remove("hand")
                "She wipes her hands off, but takes a quick sniff when she's done and smiles."
                call Sex_Basic_Dialog(Girl,"warned") #"Thanks for the head's up."
                jump Girl_Orgasm_After


#Start Swallowed  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Swallowed:  #rkeljsv
        $ Girl.Swallow += 1
        $ Girl.Statup("Inbt", 50, 3)
        $ Girl.Addict -= 20
        if "mouth" in Girl.Spunk:
                $ Girl.Spunk.remove("mouth")
        if "full" not in Girl.RecentActions and Girl.RecentActions.count("swallowed") >= 5:
                $ Girl.RecentActions.append("full")
                $ Girl.FaceChange("surprised", 1)
                if Girl == RogueX:
                        ch_r "-buurp-"
                        $ Girl.FaceChange("sexy", 1)
                        ch_r "S'cuse me [Girl.Petname], must have been something I ate."
                elif Girl == KittyX:
                        ch_k "-buurp-"
                        $ Girl.FaceChange("sexy", 1)
                        ch_k "I. . . might have to cut back a bit."
                elif Girl == EmmaX:
                        ch_e "-ehem-"
                        $ Girl.FaceChange("sexy", 1)
                        ch_e "Excuse me [Girl.Petname], I had a full lunch."
                elif Girl == LauraX:
                        ch_l "-buurp-"
                        $ Girl.FaceChange("sexy", 1)
                        ch_l "Oof [Girl.Petname],  must'a been something I ate."
                elif Girl == JeanX:
                        $ Girl.Blush = 2
                        ch_j "-buurp-"
                        if ApprovalCheck(Girl, 600, "L"):
                                $ Girl.FaceChange("sexy", 1)
                                ch_j "Heh. . . kinda full. . ."
                        else:
                                $ Girl.FaceChange("bemused", 1,Eyes="side")
                                $ Girl.Statup("Obed", 200, 3)
                                ch_j "Um, you didn't hear that. . ."
                elif Girl == StormX:
                        ch_s "-buurp-"
                        $ Girl.FaceChange("sexy", 1)
                        ch_s "Oh, [Girl.Petname], I must have had enough. . ."
                elif Girl == JubesX:
                        ch_v "-cough-"
                        $ Girl.FaceChange("sexy", 1)
                        ch_v "Whew, I think maybe I've had more than I can take. . ."
        $ Girl.RecentActions.append("swallowed")
        $ Girl.DailyActions.append("swallowed")
        $ Girl.Addictionrate += 2
        if "addictive" in Player.Traits:
                $ Girl.Addictionrate += 2
        if Trigger == "anal":
                $ Girl.Statup("Obed", 50, 2)
                $ Girl.Statup("Obed", 200, 2)
        if Girl.Swallow == 1:
                $ Girl.SEXP += 12
                $ Girl.Statup("Inbt", 70, 5)
        jump Girl_Orgasm_After

#Start Creampied  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Creampied:
        if Trigger == "sex":
                $ Girl.CreamP += 1
                $ Girl.Statup("Lust", 200, 10)
                $ Girl.RecentActions.append("creampie sex")
                $ Girl.DailyActions.append("creampie sex")
        elif Trigger == "anal":
                $ Girl.CreamA += 1
                $ Girl.Statup("Lust", 200, 5)
                $ Girl.RecentActions.append("creampie anal")
                $ Girl.DailyActions.append("creampie anal")
        $ Girl.Statup("Inbt", 50, 3)
        $ Girl.Addict -= 30
        $ Girl.Addictionrate += 2
        if "addictive" in Player.Traits:
                $ Girl.Addictionrate += 3
        if Girl.CreamP == 1:
                $Girl.SEXP += 10
                $ Girl.Statup("Inbt", 70, 5)

# Clean-up / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Girl_Orgasm_After:
        $ Line = "What next?"
        if not renpy.showing(Girl.Tag+"_HJ_Animation"):
                $ Girl.ArmPose = 1
        $ Player.Semen -= 1
        $ Player.Focus = 0
        $ Speed = 0
        $ Girl.Thirst -= 10 if Girl.Thirst > 50 else 5
        menu:
                "Want [Girl.Name] to clean you off?"
                "Yes":
                        call Girl_CleanCock
                "Actually, let [Partner.Name] do it." if Partner in TotalGirls:
                        call Shift_Focus(Partner) #makes the partner the lead and the lead the partner
                        call AllReset(Partner) #resets the position of the orignal lead
                        call Girl_CleanCock(Ch_Focus) #Does the cleanup focused on the original Partner

                        call Shift_Focus(Partner) #makes the original partner the partner again
                        call AllReset(Partner)  #resets the position of the partner

                        "[Partner.Name] Steps back."

                        call AllReset(Girl) #resets the position of the orignal lead
                "No":
                        pass
        if Girl.Spunk:
                        call Girl_Cleanup(Girl)
        $ Situation = 0
        return

label Girl_CleanCock(Girl=0):
        $ Girl = GirlCheck(Girl)
        $ Line = "What next?"
        if not renpy.showing(Girl.Tag+"_HJ_Animation"):
                $ Girl.ArmPose = 1
        $ Player.Cock = "out"
        $ Speed = 0
        if Trigger == "anal" and not ApprovalCheck(Girl, 1600, TabM=1) and not Girl.Addict >= 80:
                if Girl == JeanX:
                        $ Girl.FaceChange("sly", 1,Eyes="psychic")
                        "You feel a slight breeze and the juices swirl off your cock and onto the floor."
                        $ Girl.FaceChange("sly", 0)
                else:
                        "She wipes your cock clean."
        elif Girl.Blow > 3 or Girl.Swallow:
                if ApprovalCheck(Girl, 1200, TabM=1) or Girl.Addict >= 60:
                        call expression Girl.Tag+"_BJ_Launch" pass ("cum")
                        $ Speed = 1
                        $ Girl.FaceChange("sucking", 1)
                        if ApprovalCheck(Girl, 1500, TabM=1):
                            if Partner and ApprovalCheck(Partner, 1500, TabM=1):
                                    "Both girls look up at you as they lick your cock clean."
                            elif Girl.Love > Girl.Inbt and Girl.Love > Girl.Obed:
                                    "She looks up at you lovingly as she licks your cock clean."
                            elif Girl.Obed > Girl.Inbt:
                                    $ Girl.Eyes = "side"
                                    "She dutifully licks your cock clean with lowered eyes."
                                    $ Girl.Statup("Obed", 80, 3)
                            else:
                                    "She happily licks your cock clean."
                        elif Girl.Addict >= 60:
                                    "She hungrily and thoroughly licks your cock clean."
                        else:
                                    "She licks you cock clean."
                        $ Girl.FaceChange("sexy")
                else:
                        if not renpy.showing(Girl.Tag+"_HJ_Animation"):
                                call expression Girl.Tag+"_HJ_Launch" pass ("cum")
                        if Partner and ApprovalCheck(Partner, 1000, TabM=1):
                                "Both girls reach down and wipe your cock clean."
                        else:
                                "She wipes your cock clean."
        else:
                        if renpy.showing(Girl.Tag+"_PJ_Animation"): #if renpy.showing("Rogue_PJ_Animation"):
                                pass
                        elif not renpy.showing(Girl.Tag+"_HJ_Animation"):
                                call expression Girl.Tag+"_HJ_Launch" pass ("cum")
                        if Partner and ApprovalCheck(Partner, 1000, TabM=1):
                                "Both girls reach down and wipe your cock clean."
                        else:
                                "She wipes your cock clean."
        $ Player.Spunk = 0
        $ Girl.FaceChange("sexy")
        if Trigger in ("fondle breast","suck breast"):
                call ViewShift(Girl,"breasts")
        elif Trigger in ("fondle pussy","lick pussy","fondle ass","insert ass","lick ass","fondle thighs"):
                call ViewShift(Girl,"pussy")
        return

# End You Cumming //////////////////////////////////////////////////////////////////////////////////


#  Girl's Orgasms / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Girl_Cumming(Girl=0,Quick=0,BO=[]): #rename from Girl_Cumming  #rkeljsv
    # call Girl_Cumming(Girl,0)
    if Girl not in TotalGirls: #should remove "character don't exist" errors
            return

    $ Girl.DrainWord("gonnafap",1,1,0)  #removes these flags when you've had sex
    $ Girl.DrainWord("wannafap",1,1,0)

    if Girl.Loc == "bg teacher" and bg_current == "bg classroom":
            pass
    elif Girl.Loc != bg_current and "phonesex" not in Player.RecentActions:
            #if she's not even in the room. . .
            $ Girl.Lust = 25
            return
    $ Girl.Eyes = "surprised"
    $ Girl.Brows = "sad"
    if Girl in (EmmaX,LauraX):
            $ Girl.Mouth = "tongue"
    else:
            $ Girl.Mouth = "sucking"
    $ Girl.Blush = 1

    call AnyLine(Girl,". . . !")
    $ Speed = 0

    call Punch

    $ Speed = 1
    $ Line = renpy.random.choice([Girl.Name + " is suddenly rocked with spasms, holding back a muffled scream.",
                Girl.Name + " grabs on tightly as her body shakes with pleasure.",
                Girl.Name + " stiffens and lets out a low moan.",
                Girl.Name + "'s body quivers and suddenly goes still."])
    "[Line]"
    $ Girl.Thirst = int(Girl.Thirst/2)
    $ Girl.Thirst -= 5

    $ Girl.OCount += 1
    $ Girl.Org += 1
    $ Girl.Lust = 30 if "hotblooded" in Girl.Traits else 0
    $ Girl.Lust += (Girl.OCount * 5)
    $ Girl.Lust = 60 if Girl.Lust >= 60 else Girl.Lust
    $ Girl.Statup("Inbt", 50, 1)
    $ Girl.Statup("Inbt", 70, 1)

    if Quick:
            $ Girl.FaceChange("sexy", 2)
            return

    $ Girl.Eyes = "closed"
    $ Girl.Brows = "sad"
    $ Girl.Mouth = "tongue"
    if Girl == RogueX:
            $ Line = renpy.random.choice(["Wow. . .  just, wow.",
                "I don't know what came over me. . .",
                "Hmmmm. . . .",
                "That, felt good. Thatfeltrealgood."])
    elif Girl == KittyX:
            $ Line = renpy.random.choice(["Wow. . .  just, wow.",
                "That was amazing!",
                "Hmmmm. . . .",
                "I loved that!"])
    elif Girl == EmmaX:
            $ Line = renpy.random.choice(["Oooooh. . . lovely.",
                "I really enjoyed that one. . .",
                "Hmmmm. . . .",
                "That was. . . greaaaaat. . ."])
    elif Girl == LauraX:
            $ Line = renpy.random.choice(["Oooooh. . .",
                "That was a good one. . .",
                "Hmmmm. . . .",
                "That was. . ."])
    elif Girl == JeanX:
            $ Line = renpy.random.choice(["Oooooh. . .",
                "Ah, I needed that. . .",
                "Hmmmm. . . .",
                "Woo, nice. . ."])
    elif Girl == StormX:
            $ Line = renpy.random.choice(["Oooooh. . .",
                "Nnnnmmmmaaaaahhh. . .",
                "Hmmmm. . . .",
                "That was. . . amaaazing. . ."])
    elif Girl == JubesX:
            $ Line = renpy.random.choice(["Oooooh. . .",
                "Wooooww. . .",
                "Hmmmm. . . .",
                "Wonderful. . ."])
    call AnyLine(Girl,Line)

    if "unsatisfied" in Girl.RecentActions:  #If she had been unsatisfied, you satisfied her. . .
            $ Girl.Statup("Love", 70, 2)
            $ Girl.Statup("Love", 90, 1)
            if "unsatisfied" in Girl.DailyActions:
                    if Girl == RogueX:
                            ch_r "I guess that makes up for earlier, [Girl.Petname]."
                    elif Girl == KittyX:
                            ch_k "You know how to take care of me."
                    elif Girl == EmmaX:
                            ch_e "Making up for past mistakes, [Girl.Petname]?"
                    elif Girl == LauraX:
                            ch_l "Thanks for evening the score, [Girl.Petname]?"
                    elif Girl == JeanX:
                            $ Girl.Statup("Obed", 50, 6)
                            $ Girl.Statup("Obed", 80, 2)
                            $ Girl.Statup("Obed", 90, 2)
                            ch_j "-Finally.-"
                    elif Girl == StormX:
                            ch_s "I think that brings us even, [Girl.Petname]."
                    elif Girl == JubesX:
                            ch_v "So you -do- know how to make a girl feel good."
            $ Girl.DrainWord("unsatisfied")
    $ Line = 0

    if Trigger != "masturbation":
            if Girl.OCount == 1:
                    # if she's angry, but not too angry, then reduce that on the first O of the time block.
                    $ Girl.ForcedCount -= 1 if 5 > Girl.ForcedCount > 0 else 0
            $ Girl.Statup("Lust", 40, 1)
            $ Girl.Statup("Love", 70, 1)
            $ Girl.Statup("Love", 90, 1)
            $ Girl.Statup("Obed", 50, 2,Alt=[[JeanX],900,5]) #+5 for Jean
            $ Girl.Statup("Obed", 70, 2)

            #checks to check reaction of other girls
            $ BO = TotalGirls[:]
            $ BO.remove(Girl)
            while BO:
                    if BO[0].Loc == bg_current and "noticed "+Girl.Tag in BO[0].RecentActions:
                            $ BO[0].Lust += 15 if BO[0].GirlLikeCheck(Girl) >= 500 else 10
                            $ BO[0].Lust += 5 if BO[0].Les >= 5 else 0
                    if BO[0].Lust >= 100:
                            call Girl_Cumming(BO[0],1) #calls quick version
                    $ BO.remove(BO[0])

            #Orgasm count
            if (Trigger == "blow" or Trigger == "hand") and not Trigger2:
                pass
            elif Partner != Girl:
                if Girl.OCount == 2:
                        $ Girl.Brows = "confused"
                        if Girl == RogueX:
                                ch_r "Wow. . . that was amazing. . ."
                        elif Girl == KittyX:
                                ch_k "Hmm. . . so. . . good."
                        elif Girl == EmmaX:
                                ch_e "Excellent job, [Girl.Petname]. . ."
                        elif Girl == LauraX:
                                ch_l "Hey, good job, [Girl.Petname]. . ."
                        elif Girl == JeanX:
                                ch_j "I like that attitude. . ."
                        elif Girl == StormX:
                                ch_s "Excellent job, [Girl.Petname]."
                        elif Girl == JubesX:
                                ch_v "Oh, that hit where it needed to. . ."
                        $ Girl.Statup("Love", 50, 1)
                        $ Girl.Statup("Love", 80, 2)
                        $ Girl.Statup("Obed", 50, 1)
                        $ Girl.Statup("Obed", 60, 1)
                elif Girl.OCount == 3: #5
                        $ Girl.Brows = "confused"
                        if Girl == RogueX:
                                ch_r "You. . . can. . . really. . . keep. . . it. . . up. . . huh?"
                        elif Girl == KittyX:
                                ch_k "You're. . .wearing. . .me. . .out. . ."
                        elif Girl == EmmaX:
                                ch_e "You . . .certainly. . . have some. . . stamina. . ."
                        elif Girl == LauraX:
                                ch_l "You can. . . definitely. . . keep up. . ."
                        elif Girl == JeanX:
                                $ Girl.Statup("Love", 90, 3)
                                ch_j "Hey. . . really good job. . ."
                        elif Girl == StormX:
                                ch_s "Very. . . dedicated. . . [Girl.Petname]."
                        elif Girl == JubesX:
                                ch_v "You, uh, just keep'em coming, uh?"
                        $ Girl.Statup("Love", 50, 2)
                        $ Girl.Statup("Love", 80, 2)
                        $ Girl.Statup("Obed", 30, 1)
                        $ Girl.Statup("Obed", 50, 1)
                elif Girl.OCount == 5 and Partner != Girl: #10
                    $ Girl.Mouth = "tongue"
                    if Girl == RogueX:
                            ch_r "I'm . . .really. . . getting. . . worn. . . out . . ."
                            ch_r "could. . . we. . . cool. . . off?"
                    elif Girl == KittyX:
                            ch_k "I'm . . .really. . . getting. . . tired. . . here. . ."
                            ch_k "could. . . we. . . take. . . a. . .break?"
                    elif Girl == EmmaX:
                            ch_e "You're . . .practically. . . exhausting. . ."
                            ch_e "would. . . you. . . mind. . . a break?"
                    elif Girl == LauraX:
                            ch_l "I don't. . . usually. . . wear out. . . this easy. . ."
                            ch_l "could. . . we. . . take. . . a break?"
                    elif Girl == JeanX:
                            $ Girl.Statup("Love", 50, 5)
                            ch_j "Uh. . . I'm a little. . ."
                            $ Girl.Statup("Love", 90, 3)
                            ch_j "Maybe that's. . . enough for now?"
                    elif Girl == StormX:
                            ch_s "Perhaps. . . this would be. . . enough for now. . . [Girl.Petname]?"
                    elif Girl == JubesX:
                            ch_v "I. . . uh. . . love what you're. . . doing here. . ."
                            ch_v "But. . . uh. . . maybe you could. . . let me. . . catch my breath?"
                    menu:
                        extend ""
                        "Finish up." if Player.FocusX:
                            "You release your concentration. . ."
                            $ Player.FocusX = 0
                            $ Player.Focus += 15
                        "Let's try something else." if MultiAction:
                            $ Situation = "shift"
                        "No, I'm not done yet.":
                            if Trigger == "sex" or Trigger == "anal":
                                if ApprovalCheck(Girl, 1000, TabM=1) or ApprovalCheck(Girl, 400, "O", TabM=1):
                                    $ Girl.Statup("Love", 200, -5)
                                    $ Girl.Statup("Obed", 50, 2,Alt=[[JeanX],900,5]) #+5 for Jean
                                    $ Girl.Statup("Obed", 80, 3)
                                    $ Girl.Eyes = "stunned"
                                    "She drifts off into incoherent moans."
                                else:
                                    $ Girl.FaceChange("angry", 1)
                                    "She scowls at you, pulls out with a pop, and wipes herself off."
                                    if Girl == RogueX:
                                            ch_r "Well if that's your attitude you can handle your own business."
                                    elif Girl == KittyX:
                                            ch_k "Looks like you're going to have to. . ."
                                    elif Girl == EmmaX:
                                            ch_e "Learn to take a hint. . ."
                                    elif Girl == LauraX:
                                            ch_l "Well, I am. . ."
                                    elif Girl == JeanX:
                                            ch_j ". . ."
                                            ch_j "I just don't have the time right now."
                                    elif Girl == StormX:
                                            ch_s "I wish I could manage it, [Girl.Petname]."
                                    elif Girl == JubesX:
                                            ch_v "Well, uh. . . I am."
                                    $ Girl.Statup("Love", 50, -3, 1)
                                    $ Girl.Statup("Love", 80, -4, 1)
                                    $ Girl.Statup("Obed", 30, -1, 1,Alt=[[JeanX],300,5]) #+5 for Jean
                                    $ Girl.Statup("Obed", 50, -1, 1,Alt=[[JeanX],900,5]) #+5 for Jean
                                    $ Girl.RecentActions.append("angry")
                                    $ Girl.DailyActions.append("angry")
                            else:
                                    $ Girl.Statup("Obed", 50, 3,Alt=[[JeanX],900,5]) #+5 for Jean
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Eyes = "stunned"
                                    "She drifts off into incoherent moans."
                #end Ocount stuff
    if Trigger == "strip":
            call AllReset(Girl)
            if Girl == RogueX:
                        show Rogue_Sprite at Girl_Dance1(RogueX)
            elif Girl == KittyX:
                        show Kitty_Sprite at Girl_Dance1(KittyX)
            elif Girl == EmmaX:
                        show Emma_Sprite at Girl_Dance1(EmmaX)
            elif Girl == LauraX:
                        show Laura_Sprite at Girl_Dance1(LauraX)
            elif Girl == JeanX:
                        show Jean_Sprite at Girl_Dance1(JeanX)
            elif Girl == StormX:
                        show Storm_Sprite at Girl_Dance1(StormX)
            elif Girl == JubesX:
                        show Jubes_Sprite at Girl_Dance1(JubesX)
            "[Girl.Name] begins to dance again."
    return

# End Girl's Orgasm /////////////////////////////////////////////////////////////////////////////////////


# Start Girl Clean-Up /////////////////////////////////////////////////////////////////////////////////////
label Girl_Cleanup(Girl=0,Choice = "random",Options=[],Cnt=0,Cleaned=0,Original=0): #rkeljsv
    if Girl not in TotalGirls or ("painted" in Girl.RecentActions and Choice != "ask"): #should remove "character don't exist" errors
            return
    if Choice == "after":
            # This is at the end of a session
            if not Girl.Spunk:
                $ Girl.Wet = 0
                return
            $ Cnt = 1
            $ temp_modifier = 0

    if Girl.Addict > 80 and Girl.Swallow:
            #if she likes cum, she prefers to eat it.
            $ Choice = "eat"
            $ Girl.Eyes = "manic"
            $ Girl.Mouth = "smile"
    elif Girl == EmmaX and "taboo" not in EmmaX.History and Cnt:
            #Emma won't go around like this unless past her barrier
            $ Choice = "clean"
    elif Choice == "ask":
            pass
    elif "painted" in Girl.RecentActions and ApprovalCheck(Girl, 1000, "OI"):
            return
    elif ApprovalCheck(Girl, 1200, "LO"):
            $ Choice = "ask"
    elif not ApprovalCheck(Girl, 400, "I"):
            $ Girl.FaceChange("bemused")
            $ Choice = "clean"
    elif not Cnt:
            $ Choice = "random"
    else:
            $ Choice = "ask"

    $ Cleaned = 1 if "cleaned" in Girl.DailyActions else 0
    $ Girl.RecentActions.append("cleaned")
    $ Girl.DailyActions.append("cleaned")

    if Ch_Focus != Girl:
            # if Girl isn't the lead, swap to her.
            if Original in TotalGirls:
                    $ Original = Partner
            else:
                    $ Original = Girl
            call Shift_Focus(Girl)

    if Choice == "ask":
            $ Choice = "random"
            "[Girl.Name] looks down at the spunk covering her."
            menu:
                "What do you suggest [Girl.Name] do about cleaning up?"
                "You should leave it where it is.":
                        if not Cnt:
                            # If this isn't the end of the session
                            $ Girl.FaceChange("sly")
                            if ApprovalCheck(Girl, 300, "I") or ApprovalCheck(Girl, 1000):
                                    $ Girl.Statup("Obed", 70, 1)
                                    $ Girl.Statup("Inbt", 50, 1)
                                    $ Girl.Statup("Lust", 90, 2)
                                    $ Choice = "leave"
                                    if Girl == RogueX:
                                            ch_r "Heh, ok, [Girl.Petname]."
                                    elif Girl == KittyX:
                                            ch_k "Oh, ok.."
                                    elif Girl == EmmaX:
                                            ch_e "Hmm. . ."
                                    elif Girl == LauraX:
                                            ch_l "Hmm. . ."
                                    elif Girl == JeanX:
                                            ch_j "Ok, sure. . ."
                                    elif Girl == StormX:
                                            ch_s "Oh, I suppose that I could, [Girl.Petname]."
                                    elif Girl == JubesX:
                                            $ Girl.Statup("Love", 80, -2)
                                            $ Girl.FaceChange("sad")
                                            ch_v "Well, uh. . . I guess. . ."
                            else:
                                    if Girl == RogueX:
                                            ch_r "Ugh, too messy."
                                    elif Girl == KittyX:
                                            ch_k "Hm, no."
                                    elif Girl == EmmaX:
                                            ch_e "Too undignified, [Girl.Petname]."
                                    elif Girl == LauraX:
                                            ch_l "Eh, I'm not a fan of mess, [Girl.Petname]."
                                    elif Girl == JeanX:
                                            ch_j "Not in the mood, [Girl.Petname]."
                                    elif Girl == StormX:
                                            ch_s "That would be a bit messy, [Girl.Petname]."
                                    elif Girl == JubesX:
                                            $ Girl.FaceChange("sad")
                                            ch_v "I, uh. . . wouldn't want to leave it a mess. . ."

                        #This is the end of session. . .
                        elif ApprovalCheck(Girl, 900, "I") or "exhibitionist" in Girl.Traits:
                                    $ Girl.Statup("Obed", 70, 2)
                                    $ Girl.Statup("Obed", 90, 1)
                                    $ Girl.Statup("Lust", 90, 5)
                                    $ Choice = "leave"
                                    $ Girl.FaceChange("sly")
                                    if Girl == RogueX:
                                            ch_r "Ooh, I like where your head is at. . "
                                    elif Girl == KittyX:
                                            ch_k "Ooh, I like where your head is at. . "
                                    elif Girl == EmmaX:
                                            ch_e "Hmm. . . I suppose I could use some accessories. . "
                                    elif Girl == LauraX:
                                            ch_l "Hmm. . . I do like the glow it gives me. . "
                                    elif Girl == JeanX:
                                            ch_j "Hmm. . . ok."
                                    elif Girl == StormX:
                                            ch_s "Something to wear out, [Girl.Petname]. . ."
                                    elif Girl == JubesX:
                                            $ Girl.Statup("Love", 80, -2)
                                            $ Girl.FaceChange("sad")
                                            ch_v "Oh, uh. . . I guess I could. . ."
                        elif ApprovalCheck(Girl, 600, "I") and ApprovalCheck(Girl, 1200, "LO",Alt=[[JubesX],1500]):
                                    $ Girl.Statup("Obed", 90, 1)
                                    $ Girl.Statup("Inbt", 80, 1)
                                    $ Girl.Statup("Lust", 90, 5)
                                    $ Choice = "leave"
                                    $ Girl.FaceChange("surprised",2)
                                    if Girl == RogueX:
                                            ch_r "Well, I guess I could. . ."
                                    elif Girl == KittyX:
                                            ch_k "Well, maybe. . ."
                                    elif Girl == EmmaX:
                                            ch_e "Hmm. . . if you insist. . ."
                                    elif Girl == LauraX:
                                            ch_l "Hmm. . . if you insist. . ."
                                    elif Girl == JeanX:
                                            ch_j "Hmm. . . ok."
                                    elif Girl == StormX:
                                            ch_s ". . . Fine."
                                    elif Girl == JubesX:
                                            $ Girl.FaceChange("sad")
                                            ch_v "Oh, uh. . . I guess I could. . ."
                                    $ Girl.FaceChange("sly",1)
                        else:
                            #leave it on, permanently
                            $ Girl.FaceChange("angry")
                            if Girl == RogueX:
                                    ch_r "Now you're just being ridiculous!"
                            elif Girl == KittyX:
                                    $ Girl.Brows = "confused"
                                    ch_k "Now you're just being silly!"
                            elif Girl == EmmaX:
                                    ch_e "Excuse me?"
                            elif Girl == LauraX:
                                    ch_l "Excuse me?"
                            elif Girl == JeanX:
                                    ch_j "What?"
                            elif Girl == StormX:
                                    ch_s "That would be a bit much, [Girl.Petname]."
                            elif Girl == JubesX:
                                    $ Girl.FaceChange("sad")
                                    ch_v "Well. . . that would be. . . messy. . . yeah."
                            menu:
                                extend ""
                                "Please?":
                                    if ApprovalCheck(Girl, 1800,Alt=[[JubesX],2200]):
                                            $ Girl.Statup("Love", 85, 1)
                                            $ Girl.Statup("Obed", 50, 2)
                                            $ Girl.Statup("Obed", 80, 1)
                                            $ Girl.Statup("Inbt", 40, 3)
                                            $ Girl.Statup("Inbt", 80, 1)
                                            if Girl == RogueX:
                                                    ch_r "Oh, fine!"
                                            elif Girl == KittyX:
                                                    ch_k "Oh, fine!"
                                            elif Girl == EmmaX:
                                                    ch_e "Well. Ok."
                                            elif Girl == LauraX:
                                                    ch_l "Fine."
                                            elif Girl == JeanX:
                                                    ch_j "Hmm. . . ok."
                                            elif Girl == StormX:
                                                    ch_s ". . . Fine."
                                            elif Girl == JubesX:
                                                    $ Girl.Statup("Love", 80, -2)
                                                    ch_v ". . . fine. . ."
                                            $ Choice = "leave"
                                    elif Cleaned:
                                            $ Girl.FaceChange("angry")
                                            if Girl == RogueX:
                                                    ch_r "Seriously, stop bugging me about this."
                                            elif Girl == KittyX:
                                                    ch_k "Seriously, quit bugging me about this."
                                            elif Girl == EmmaX:
                                                    ch_e "I believe I've made myself clear."
                                            elif Girl == LauraX:
                                                    ch_l "I'm in no mood for this."
                                            elif Girl == JeanX:
                                                    ch_j "Cut it out, [Girl.Petname]."
                                            elif Girl == StormX:
                                                    ch_s "I cannot."
                                            elif Girl == JubesX:
                                                    ch_v "I don't wanna!"
                                    elif ApprovalCheck(Girl, 800):
                                            $ Girl.Statup("Inbt", 50, 1)
                                            if Girl == RogueX:
                                                    ch_r "You're persistant, but no way."
                                            elif Girl == KittyX:
                                                    ch_k "You're persistant, but no way."
                                            elif Girl == EmmaX:
                                                    ch_e "You're persistant, but no."
                                            elif Girl == LauraX:
                                                    ch_l "You're certainly persistant, but no."
                                            elif Girl == JeanX:
                                                    ch_j "Cut it out."
                                            elif Girl == StormX:
                                                    ch_s "Be serious, [Girl.Petname]."
                                            elif Girl == JubesX:
                                                    ch_v "No!"
                                    else:
                                            $ Girl.Statup("Love", 75, -5)
                                            $ Girl.Statup("Love", 40, -10)
                                            $ Girl.Statup("Obed", 90, 2)
                                            $ Girl.FaceChange("angry")
                                            if Girl == RogueX:
                                                    ch_r "Don't be an asshole."
                                            elif Girl == KittyX:
                                                    ch_k "Don't be a dick."
                                            elif Girl == EmmaX:
                                                    ch_e "Of course not."
                                            elif Girl == LauraX:
                                                    ch_l "You've gotta be joking."
                                            elif Girl == JeanX:
                                                    ch_j "Fuck off."
                                            elif Girl == StormX:
                                                    ch_s "No."
                                            elif Girl == JubesX:
                                                    ch_v "No way! Mine!"
                                "I insist.":
                                    $ Girl.FaceChange("sad")
                                    if ApprovalCheck(Girl, 400, "I") and ApprovalCheck(Girl, 1200, "LO",Alt=[[JubesX],1500]):
                                            $ Girl.Statup("Obed", 40, 3)
                                            $ Girl.Statup("Obed", 90, 2)
                                            if Girl == RogueX:
                                                    ch_r "Alright, fine."
                                            elif Girl == KittyX:
                                                    ch_k "Fine, whatever."
                                            elif Girl == EmmaX:
                                                    ch_e "Well then."
                                            elif Girl == LauraX:
                                                    ch_l "Fine."
                                            elif Girl == JeanX:
                                                    ch_j "Well good for you."
                                            elif Girl == StormX:
                                                    ch_s ". . . I suppose."
                                            elif Girl == JubesX:
                                                    $ Girl.Statup("Love", 80, -2)
                                                    ch_v ". . . fine."
                                            $ Choice = "leave"
                                    elif ApprovalCheck(Girl, 800, "O"):
                                            $ Girl.Statup("Love", 50, -10)
                                            $ Girl.Statup("Love", 200, -5)
                                            $ Girl.Statup("Obed", 90, 10)
                                            $ Girl.Statup("Obed", 200, 5)
                                            if Girl == RogueX:
                                                    ch_r "If you have to insist."
                                            elif Girl == KittyX:
                                                    ch_k "Fine."
                                            elif Girl == EmmaX:
                                                    ch_e "If I must."
                                            elif Girl == LauraX:
                                                    ch_l "If you insist."
                                            elif Girl == JeanX:
                                                    ch_j "Huh. . . ok."
                                            elif Girl == StormX:
                                                    ch_s ". . . Fine."
                                            elif Girl == JubesX:
                                                    ch_v ". . . fine."
                                            $ Choice = "leave"
                                    elif Cleaned:
                                            $ Girl.Statup("Love", 50, -5)
                                            $ Girl.Statup("Love", 200, -1)
                                            $ Girl.FaceChange("angry")
                                            if Girl == RogueX:
                                                    ch_r "Seriously, stop bugging me about this."
                                            elif Girl == KittyX:
                                                    ch_k "Seriously, stop bugging me about this."
                                            elif Girl == EmmaX:
                                                    ch_e "That's enough of that."
                                            elif Girl == LauraX:
                                                    ch_l "Enough out of you."
                                            elif Girl == JeanX:
                                                    ch_j "Cut it out."
                                            elif Girl == StormX:
                                                    ch_s "That is enough, [Girl.Petname]."
                                            elif Girl == JubesX:
                                                    ch_v "I don't wanna!"
                                    elif ApprovalCheck(Girl, 800):
                                            $ Girl.Statup("Love", 50, -3)
                                            $ Girl.Statup("Love", 200, -1)
                                            $ Girl.FaceChange("sad")
                                            if Girl == RogueX:
                                                    ch_r "Sorry, that's just a bridge too far."
                                            elif Girl == KittyX:
                                                    ch_k "That's a bit much."
                                            elif Girl == EmmaX:
                                                    ch_e "Don't push me."
                                            elif Girl == LauraX:
                                                    ch_l "Don't push it."
                                            elif Girl == JeanX:
                                                    ch_j "Cool it."
                                            elif Girl == StormX:
                                                    ch_s "No."
                                            elif Girl == JubesX:
                                                    ch_v "No!"
                                    else:
                                            $ Girl.Statup("Love", 50, -10)
                                            $ Girl.Statup("Love", 200, -5)
                                            $ Girl.FaceChange("angry")
                                            if Girl == RogueX:
                                                    ch_r "Well {i}I{/i} insist you don't know how to talk to a lady!"
                                            elif Girl == KittyX:
                                                    ch_k "Well that's too bad!"
                                            elif Girl == EmmaX:
                                                    ch_e "Obviously not."
                                            elif Girl == LauraX:
                                                    ch_l "Hell no."
                                            elif Girl == JeanX:
                                                    ch_j "Good for you."
                                            elif Girl == StormX:
                                                    ch_s "Do not push me, [Girl.Petname]."
                                            elif Girl == JubesX:
                                                    ch_v "No way!"
                                "Never mind then.":
                                            if Girl == RogueX:
                                                    ch_r "Alright then. . ."
                                            elif Girl == KittyX:
                                                    ch_k "Right. . ."
                                            elif Girl == EmmaX:
                                                    ch_e "Ok. . ."
                                            elif Girl == LauraX:
                                                    ch_l "Ok. . ."
                                            elif Girl == JeanX:
                                                    ch_j "Right. . ."
                                            elif Girl == StormX:
                                                    ch_s "Very well."
                                            elif Girl == JubesX:
                                                    ch_v "Good."
                        #end "leave it"

                "You should just eat it.":
                        $ Girl.FaceChange("sly")
                        if "hungry" in Girl.Traits or (Girl.Swallow >= 5 and ApprovalCheck(Girl, 800)):
                                #lots of swallows
                                $ Girl.Statup("Obed", 90, 1)
                                $ Girl.Statup("Inbt", 50, 3)
                                $ Girl.Statup("Inbt", 80, 1)
                                $ Girl.Statup("Lust", 90, 5)
                                $ Choice = "eat"
                                if Girl == RogueX:
                                        ch_r "I am a bit peckish. . ."
                                elif Girl == KittyX:
                                        ch_k "Mmmmm, maybe . ."
                                elif Girl == EmmaX:
                                        ch_e "Well, I suppose I could. . ."
                                elif Girl == LauraX:
                                        "She licks her lips. . ."
                                elif Girl == JeanX:
                                        ch_j "Hmm. . . ok."
                                elif Girl == StormX:
                                        ch_s "Thank you. . ."
                                elif Girl == JubesX:
                                        $ Girl.FaceChange("smile")
                                        ch_v "Sweet!"
                        elif Girl.Swallow and ApprovalCheck(Girl, 800):
                                #few swallows
                                $ Girl.Statup("Obed", 50, 1)
                                $ Girl.Statup("Obed", 90, 1)
                                $ Girl.Statup("Inbt", 50, 2)
                                $ Girl.Statup("Inbt", 80, 1)
                                $ Girl.Statup("Lust", 90, 5)
                                $ Choice = "eat"
                                if Girl == RogueX:
                                        ch_r "I guess it wasn't so bad last time. . ."
                                elif Girl == KittyX:
                                        ch_k "It's not that bad. . ."
                                elif Girl == EmmaX:
                                        ch_e "You do have a unique flavor. . ."
                                elif Girl == LauraX:
                                        ch_l "You do taste pretty good. . ."
                                elif Girl == JeanX:
                                        ch_j "Mmmm. . . ok."
                                elif Girl == StormX:
                                        ch_s "Very interesting. . ."
                                elif Girl == JubesX:
                                        $ Girl.FaceChange("smile")
                                        ch_v "Sweet!"
                        elif ApprovalCheck(Girl, 1200) or Girl == JubesX:
                                #no swallows, but likes you
                                $ Girl.Statup("Obed", 50, 1)
                                $ Girl.Statup("Obed", 90, 1)
                                $ Girl.Statup("Inbt", 50, 3)
                                $ Girl.Statup("Inbt", 80, 1)
                                $ Choice = "eat"
                                if Girl == RogueX:
                                        ch_r "I suppose I could give it a go. . ."
                                elif Girl == KittyX:
                                        ch_k "Huh, I guess. . ."
                                elif Girl == EmmaX:
                                        ch_e "I have been a bit curious. . ."
                                elif Girl == LauraX:
                                        ch_l "I have been thinking about it. . ."
                                elif Girl == JeanX:
                                        ch_j "Hmm. . . ok."
                                elif Girl == StormX:
                                        ch_s "I could try it, [Girl.Petname]."
                                elif Girl == JubesX:
                                        $ Girl.FaceChange("smile")
                                        ch_v "Thanks!"
                        elif ApprovalCheck(Girl, 400):
                                #Likes you well enough, but won't
                                $ Girl.FaceChange("sad")
                                if Girl == RogueX:
                                        ch_r "Sorry, I just don't think I could."
                                elif Girl == KittyX:
                                        ch_k "Yeah, not really."
                                elif Girl == EmmaX:
                                        ch_e "I doubt that."
                                elif Girl == LauraX:
                                        ch_l "Yeah, but I won't. . ."
                                elif Girl == JeanX:
                                        ch_j "Hmm. . . nah."
                                elif Girl == StormX:
                                        ch_s "I would rather not."
                                #elif Girl == JubesX:
                        else:
                                #doesn't like you.
                                $ Girl.Statup("Love", 50, -5)
                                $ Girl.Statup("Love", 200, -3)
                                $ Girl.FaceChange("angry")
                                if Girl == RogueX:
                                        ch_r "No."
                                elif Girl == KittyX:
                                        ch_k "Nah."
                                elif Girl == EmmaX:
                                        ch_e "No."
                                elif Girl == LauraX:
                                        ch_l "Nope."
                                elif Girl == JeanX:
                                        ch_j "Ha. . . no way."
                                elif Girl == StormX:
                                        ch_s "Thank you, but no."
                                #elif Girl == JubesX:
                        #end eat it

                "You should just clean it up.":
                        if ApprovalCheck(Girl, 600, "I") and not ApprovalCheck(Girl, 1500, "LO") and Girl != JubesX: #rebellious
                                $ Girl.FaceChange("sly")
                                $ Girl.Statup("Obed", 50, -3)
                                $ Girl.Statup("Inbt", 70, 10)
                                $ Girl.Statup("Inbt", 200, 5)
                                $ Girl.Statup("Lust", 60, 5)
                                if Girl == RogueX:
                                        ch_r "I don't know, [Girl.Petname], I kind of like it where it is. . ."
                                elif Girl == KittyX:
                                        ch_k "I don't know, [Girl.Petname], it doesn't look so bad. . ."
                                elif Girl == EmmaX:
                                        ch_e "Hmmm. . . don't I look good like this? . ."
                                elif Girl == LauraX:
                                        ch_l "I could. . ."
                                        ch_l "-but I don't want to. . ."
                                elif Girl == JeanX:
                                        ch_j "Hmm. . . nah. I like it like this. . ."
                                elif Girl == StormX:
                                        ch_s "I might like to keep it like this. . ."
                                $ Choice = "leave"
                                menu:
                                    extend ""
                                    "Ok, fine.":
                                                $ Girl.FaceChange("smile")
                                                $ Girl.Statup("Love", 70, 5)
                                                $ Girl.Statup("Obed", 50, 3)
                                    "No, clean it up.":
                                        if ApprovalCheck(Girl, 600, "O"):
                                                $ Girl.FaceChange("sad")
                                                $ Girl.Statup("Obed", 50, 10)
                                                if Girl == RogueX:
                                                        ch_r "If that's what you really want. . ."
                                                elif Girl == KittyX:
                                                        ch_k "Oh, fine. . ."
                                                elif Girl == EmmaX:
                                                        ch_e "Oh, if I must. . ."
                                                elif Girl == LauraX:
                                                        ch_l "Oh, fine. . ."
                                                elif Girl == JeanX:
                                                        ch_j "Hmm. . . whatever."
                                                elif Girl == StormX:
                                                        ch_s ". . . Fine."
                                                elif Girl == JubesX:
                                                        ch_v "Sweet!"
                                                $ Choice = "clean"
                                        elif ApprovalCheck(Girl, 1200, "LO"):
                                                $ Girl.FaceChange("sad")
                                                $ Girl.Statup("Love", 70, -3)
                                                $ Girl.Statup("Obed", 50, 3)
                                                if Girl == RogueX:
                                                        ch_r "You take the fun out of this. . ."
                                                elif Girl == KittyX:
                                                        ch_k "Boooo. . ."
                                                elif Girl == EmmaX:
                                                        ch_e "Spoilsport. . ."
                                                elif Girl == LauraX:
                                                        ch_l "Booo. . ."
                                                elif Girl == JeanX:
                                                        ch_j ". . . whatever."
                                                elif Girl == StormX:
                                                        ch_s ". . . Fine."
                                                $ Choice = "clean"
                                        else:
                                                $ Girl.Statup("Love", 70, -5)
                                                $ Girl.Statup("Obed", 50, -5)
                                                if Girl == RogueX:
                                                        ch_r "I {i}said{/i} it's stay'in."
                                                elif Girl == KittyX:
                                                        ch_k "No! I like it this way."
                                                elif Girl == EmmaX:
                                                        ch_e "I'm afraid you don't have any say in the matter."
                                                elif Girl == LauraX:
                                                        ch_l "Too bad."
                                                elif Girl == JeanX:
                                                        ch_j "Hmm. . . whatever."
                                                elif Girl == StormX:
                                                        ch_s ". . . no."
                        else: #agrees
                                    $ Girl.FaceChange("bemused")
                                    $ Choice = "clean"
                                    if Girl == RogueX:
                                            ch_r "Ok, I guess. . ."
                                    elif Girl == KittyX:
                                            ch_k "Ok, fine. . ."
                                    elif Girl == EmmaX:
                                            ch_e "If I must. . ."
                                    elif Girl == LauraX:
                                            ch_l "Whatever. . ."
                                    elif Girl == JeanX:
                                            ch_j "Hmm. . . whatever."
                                    elif Girl == StormX:
                                            ch_s ". . . Fine."
                                    elif Girl == JubesX:
                                            ch_v "Not a problem!"
                        #end clean it up

                "Hey [Partner.Name], you eat it off her." if Partner:
                            $ Choice = "partner lick"
                "Hey [Partner.Name], you wipe it off her." if Partner:
                            $ Choice = "partner wipe"


                "Say nothing. [[leave it to her]":
                    $ Choice = "random"
            #end "asked"

    if Choice == "partner wipe" or Choice == "partner lick":
            #resets to "random" if she refuses
            call Partner_Cleanup_Check(Girl)

    if Choice == "random":
            $ Options = ["clean"]
            if Girl.Swallow and ApprovalCheck(Girl, 800):
                    $ Options.append("eat")
                    if Girl.Swallow >=5:
                        $ Options.append("eat")
                    if "hungry" in Girl.Traits:
                        $ Options.append("eat")
            if ApprovalCheck(Girl, 300, "I"):
                    #Cnt means it's the end of a session
                    if not Cnt:
                        $ Options.append("leave")
                    if not Cnt or ApprovalCheck(Girl, 600, "I"):
                        $ Options.append("leave")
                    if not Cnt or ApprovalCheck(Girl, 800, "I"):
                        $ Options.append("leave")
                    if "exhibitionist" in Girl.Traits:
                        $ Options.append("leave")

            $ renpy.random.shuffle(Options)

            $ Choice = Options[0]
            #end "random"
    if Girl == JubesX:
            $ Options = ["eat"]

    if Girl.Spunk and Choice != "leave":
            call Self_Cleanup(Girl)

    if Choice == "leave":
            $ Girl.Statup("Inbt", 80, 2)
            $ Girl.Statup("Inbt", 200, 1)
            "She leaves the jiz right where it is and gives you a wink."
            if "hand" in Girl.Spunk:
                    $ Girl.Spunk.remove("hand")
                    if Girl.Swallow:
                        "She does lick off her hand though."
                    else:
                        "She does wipe her hand off though."
            if "mouth" in Girl.Spunk:
                    $ Girl.Spunk.remove("mouth")
            if Cnt:
                    # if this is final clean-up and left the jiz on
                    $ Girl.RecentActions.append("painted")
                    $ Girl.DailyActions.append("painted")

    if Original in TotalGirls and Ch_Focus != Original:
            # if Girl wasn't the lead, swap that one back
            call Shift_Focus(Original)
    return

# End Girl Clean-Up /////////////////////////////////////////////////////////////////////////////////////


# Start Clean-up  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Start Self Clean-Up / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Self_Cleanup(Girl=0):         #rkeljsv
    $ Cnt = 0
    if Girl == JeanX and not ApprovalCheck(Girl, 600, "LO"):
            #if she has no interest in you. . .
            $ Girl.Wet = 0
            $ del Girl.Spunk[:]
            $ Girl.FaceChange("sly", 1,Eyes="psychic")
            "[JeanX.Name] concentrates and the juices swirl off of her, raining to the floor."
            $ Girl.FaceChange("sly", 0)
            return
    if "mouth" in Girl.Spunk and Choice != "eat":
            $ Girl.Spunk.remove("mouth")
            "[Girl.Name] spits out the spunk in her mouth and it dribbles down her chin,"
            $ Cnt += 1
            if "chin" not in Girl.Spunk:
                $ Girl.Spunk.append("chin")
    if Girl.Spunk:
            $ Girl.Spunk.append("hand")
    if "chin" in Girl.Spunk:
            $ Girl.Spunk.remove("chin")
            if Cnt:
                "then she wipes the spunk off her chin,"
            else:
                "[Girl.Name] wipes the spunk off her chin,"
            $ Cnt += 1
    if "hair" in Girl.Spunk:
            $ Girl.Spunk.remove("hair")
            if Cnt:
                "then she wipes the spunk out of her hair,"
            else:
                "[Girl.Name] wipes the spunk out of her hair,"
            $ Cnt += 1
    if "facial" in Girl.Spunk:
            $ Girl.Spunk.remove("facial")
            if Cnt:
                "then she wipes the spunk off of her face,"
            else:
                "[Girl.Name] wipes the spunk off of her face,"
            $ Cnt += 1
    if "tits" in Girl.Spunk:
            $ Girl.Spunk.remove("tits")
            $ Player.Statup("Focus",80,2)
            if Cnt:
                "then she wipes the spunk off of her chest,"
            else:
                "[Girl.Name] wipes the spunk off of her chest,"
            $ Cnt += 1
    if "belly" in Girl.Spunk:
            $ Girl.Spunk.remove("belly")
            if Cnt:
                "then she wipes the spunk off of her belly,"
            else:
                "[Girl.Name] wipes the spunk off her belly,"
            $ Cnt += 1
    if "back" in Girl.Spunk:
            $ Girl.Spunk.remove("back")
            if Cnt:
                "then she wipes the spunk off of her lower back,"
            else:
                "[Girl.Name] wipes the spunk off her lower back,"
            $ Cnt += 1
    if "in" in Girl.Spunk:
            $ Girl.Spunk.remove("in")
            $ Player.Statup("Focus",80,3)
            if Cnt:
                "then she wipes the spunk inside her pussy,"
            else:
                "[Girl.Name] wipes the spunk inside her pussy,"
            $ Cnt += 1
    if "anal" in Girl.Spunk and (ApprovalCheck(Girl, 800, "I") or Choice != "eat"):
            while "anal" in Girl.Spunk:
                $ Girl.Spunk.remove("anal")
            $ Player.Statup("Focus",80,2)
            if Cnt:
                "then she wipes the spunk dripping out of her ass,"
            else:
                "[Girl.Name] wipes the spunk dripping our of her ass,"
            $ Cnt += 1
    if "hand" in Girl.Spunk:
            $ Girl.Spunk.remove("hand")
            if Choice == "eat":
                    $ Girl.Spunk.append("mouth")
                    $ Player.Statup("Focus",80,3)
                    if Cnt and "anal" in Girl.Spunk:
                        "then licks her hands off with a satisfied grin,"
                    if Cnt:
                        "and finally she licks her hands off with a satisfied grin."
                    else:
                        "[Girl.Name] licks her hands off with a satisfied grin."

                    $ Girl.Statup("Inbt", 80, 2)
                    $ Girl.Spunk.remove("mouth")
                    $ Girl.Swallow += 1
                    $ Girl.Addict -= (10*Cnt)
                    if Girl.Swallow == 1:
                        $ Girl.SEXP += 12
                    $ Girl.RecentActions.append("swallowed")
                    $ Girl.DailyActions.append("swallowed")
            #end hand if swallowing
            else:
                    if Cnt:
                        "and finally, she wipes her hands off with a nearby tissue."
                    else:
                        "[Girl.Name] wipes her hands off with a nearby tissue."
            $ Cnt += 1
            #end hand
    if "anal" in Girl.Spunk:
            $ Girl.Spunk.remove("anal")
            if Cnt:
                "Afterward, she wipes the spunk dripping our of her ass."
            else:
                "[Girl.Name] wipes the spunk dripping out of her ass."

    $ Girl.Wet = 0
    $ del Girl.Spunk[:]
    if Cnt >= 5:
            $ Girl.Eyes = "surprised"
            if Girl == RogueX:
                    ch_r "Wow, you really painted me white!"
            elif Girl == KittyX:
                    ch_k "Wow, you really drenched me!"
            elif Girl == EmmaX:
                    if "White Queen" not in EmmaX.Names:
                            ch_e "I really was the \"white queen\" there."
                            $ EmmaX.Names.append("White Queen")
                    else:
                            ch_e "Well that was a lot of work."
            elif Girl == LauraX:
                    ch_l "There was a lot more to that than I'd noticed. . ."
            elif Girl == JeanX:
                    ch_j "Ugh, you really made a mess there. . ."
            elif Girl == StormX:
                    ch_s ". . . is there any in my hair? So hard to tell. . ."
            elif Girl == JubesX:
                    ch_v "You really coated me, huh?"
            $ Girl.Eyes = "sexy"
    elif Cnt >=3:
            if Girl == RogueX:
                    ch_r "That was a real mess you left me to clean up."
            elif Girl == KittyX:
                    ch_k "Well that was a fine mess you got me into."
            elif Girl == EmmaX:
                    ch_e "I really was the \"white queen\" there."
                    if "White Queen" not in EmmaX.Names:
                            $ EmmaX.Names.append("White Queen")
            elif Girl == LauraX:
                    ch_l "You made a real mess there."
            elif Girl == JeanX:
                    ch_j "Maybe be more careful with your aim. . ."
            elif Girl == StormX:
                    ch_s "Perhaps next time take better care where you fire."
            elif Girl == JubesX:
                    ch_v "Whew, that was a lot."
    if Choice == "eat" and Girl.Swallow >= 5:
            if Girl == RogueX:
                    ch_r "That was delicious."
            elif Girl == KittyX:
                    ch_k "Yum."
            elif Girl == EmmaX:
                    ch_e "Mmmm, now I'm hungry for more."
            elif Girl == LauraX:
                    ch_l "Mmmm, got any more?"
            elif Girl == JeanX:
                    ch_j "Mmm. . ."
            elif Girl == StormX:
                    ch_s "Mmmm. . ."
            elif Girl == JubesX:
                    ch_v "That was amazing. . ."
    return
# End Self Clean-Up / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Partner_Cleanup_Check(Girl=0,B=0): #rkeljsv
        #girl is the lead, B is a bonus check based on if she's good with the other girl
        #resets to "random" if she refuses
        if Partner == JubesX:
                        $ B = 100
        elif Choice == "partner lick":
                if (Partner in Player.Harem and Girl in Player.Harem) or "poly " + Partner.Tag in Girl.Traits:
                        $ B = 0
                else:
                        $ B = -100
        else:
                        $ B = 0


        if Partner == JeanX and not ApprovalCheck(Partner, 600, "LO") and Partner.GirlLikeCheck(Girl) < (500-2*B):
                #if you asdk Jean to clean other girl and she has no interest in either of you. . .
                ch_j "Hm? Clean [Girl.Name] off?"
                ch_j "I guess she is a mess. . ."
                $ Girl.Wet = 0
                $ del Girl.Spunk[:]
                $ Partner.FaceChange("sly", 1,Eyes="psychic")
                "[JeanX.Name] concentrates and the juices swirl off of [Girl.Name], raining to the floor."
                if Girl == JubesX:
                        $ Girl.FaceChange("sad", 1,Eyes="down")
                        ch_v "Aw."
                $ Partner.FaceChange("sly", 0)
                ch_j "There."
                return

        if not ApprovalCheck(Partner, 1400, Bonus=3*B) or Partner.GirlLikeCheck(Girl) < (500-2*B):
                #if she's not super obedient or doesn't like the other girl
                $ Partner.FaceChange("sly")
                $ Partner.Statup("Obed", 50, -3)
                $ Partner.Statup("Inbt", 70, 10)
                $ Partner.Statup("Inbt", 200, 5)
                $ Partner.Statup("Lust", 60, 5)
                call Partner_CGLine(2) #"You want me ta clean up your mess?"
                menu:
                    extend ""
                    "Fine, never mind.":
                                $ Partner.FaceChange("smile")
                                $ Partner.Statup("Love", 70, 5)
                                $ Partner.Statup("Obed", 50, 3)
                                $ Choice = "random"
                    "Yeah, go ahead.":
                        if ApprovalCheck(Partner, 600,"O", Bonus=3*B):
                                # She's obedient. . .
                                $ Partner.FaceChange("sad")
                                $ Partner.Statup("Obed", 50, 10)
                                call Partner_CGLine(3) #"If you say so."
                        elif Partner.GirlLikeCheck(Girl) >= 800:
                                # She likes the other girl. . .
                                $ Partner.FaceChange("sly")
                                $ Partner.Statup("Love", 70, -3)
                                $ Partner.Statup("Obed", 50, 3)
                                call Partner_CGLine(4) #"I guess I don't mind if she doesn't."
                        elif ApprovalCheck(Partner, 1200, Bonus=3*B):
                                # She's likes you enough to listen. . .
                                $ Partner.FaceChange("normal")
                                $ Partner.Statup("Love", 70, -3)
                                $ Partner.Statup("Obed", 50, 3)
                                call Partner_CGLine(5) #"I guess I could. . ."
                        elif Choice == "partner lick" and ApprovalCheck(Partner, 1200) and Partner.GirlLikeCheck(Girl) >= 600:
                                # She's likes you enough to wipe, but not lick. . .
                                $ Partner.FaceChange("normal")
                                $ Partner.Statup("Love", 70, -3)
                                $ Partner.Statup("Obed", 50, 3)
                                call Partner_CGLine(6)  #"I can wipe her off, I guess, but that's it. . ."
                                $ Choice = "partner wipe"
                        else:
                                # She's obedient. . .
                                $ Partner.Statup("Love", 70, -5)
                                $ Partner.Statup("Obed", 50, -5)
                                $ Girl.GLG(Partner,900,-2,1)
                                call Partner_CGLine(7)  #"No way."
                                $ Choice = "random"
        else:           # She just agrees. . .
                                $ Girl.FaceChange("bemused")
                                if not Choice:
                                        $ Choice = "partner wipe"
                                $ Girl.GLG(Partner,900,3,1)
                                call Partner_CGLine(1) #"I'd better get to work, I guess."
        #end Partner wipe off partner check


        if Choice != "random":
            $ Girl.Statup("Lust", 60, 5)
            if not ApprovalCheck(Girl, 1400, Bonus=3*B) or Girl.GirlLikeCheck(Partner) < (500-2*B):
                #if Rogue doesn't like the other girl or isn't super obedient
                if Girl.GirlLikeCheck(Partner) >= 800:
                        $ Girl.Statup("Inbt", 90, 5)
                        $ Partner.GLG(Girl,900,5,1)
                        call Partner_CGLine(8,Girl)   #"I'll allow it, since she seems so excited by it. . ."
                elif ApprovalCheck(Girl, 1200, Bonus=3*B):
                        $ Girl.Statup("Obed", 50, 3)
                        $ Girl.Statup("Obed", 80, 2)
                        $ Girl.Statup("Inbt", 70, 3)
                        call Partner_CGLine(9,Girl)    #"If that's what turns you on. . ."
                elif ApprovalCheck(Girl, 1000, Bonus=3*B) and Girl.GirlLikeCheck(Partner) >= (600-B):
                        $ Girl.Statup("Love", 70, 1)
                        $ Girl.Statup("Obed", 50, 3)
                        $ Girl.Statup("Obed", 80, 3)
                        $ Girl.Statup("Inbt", 70, 5)
                        $ Partner.GLG(Girl,900,3,1)
                        call Partner_CGLine(10,Girl) #"Kinda ganging up on me here. . ."
                else:
                        $ Girl.Statup("Obed", 70, -3)
                        $ Girl.Statup("Inbt", 70, 2)
                        call Partner_CGLine(11,Girl)   # "Kinda gross, no."
                        $ Choice = "random"
            else:
                        $ Girl.Statup("Obed", 50, 3)
                        $ Girl.Statup("Inbt", 70, 3)
                        call Partner_CGLine(12,Girl) #"Oh, very well. . ."

        if Choice != "random":
                #calls the partner clean-up if that option is chosen
                call Les_Launch(Girl)

                call Partner_Clean_Girl(Girl)

                if Girl.Swallow >=5:
                        $ Options.append("eat")
                call AllReset(Partner)
                call AllReset(Ch_Focus)
                if Choice == "partner lick":
                        $ Girl.GLG(Partner,900,10,1)
                        call Partner_CGLine(13,Girl) #"Well that was a treat. . ."
                else:
                        $ Girl.GLG(Partner,900,3,1)
                        call Partner_CGLine(14,Girl)   #"That was easy."
        #end Partner wipe off
        return

label Partner_CGLine(LineNum=1,Girl=0): #rkeljsv
        #call Partner_CGLine(4)
        if not Partner or not LineNum:
            return
        if LineNum == 1:
                # She just agrees. . .
                if Partner == RogueX:
                        ch_r "Sure, why not?"
                elif Partner == KittyX:
                        ch_k "You[KittyX.like]really did a job on her."
                        ch_k "I'll get on it."
                elif Partner == EmmaX:
                        ch_e "I suppose it wouldn't be so bad."
                elif Partner == LauraX:
                        ch_l "I'd better get to work, I guess."
                elif Partner == JeanX:
                        ch_j "I guess. . ."
                elif Partner == StormX:
                        ch_s "I suppose I would not mind. . ."
                elif Partner == JubesX:
                        ch_v "Cool. . ."
        elif LineNum == 2:
                # She questions whether she should. . .
                if Partner == RogueX:
                        ch_r "You want me ta clean up your mess?"
                elif Partner == KittyX:
                        ch_k "You[KittyX.like]really did a job on her."
                        ch_k "I'm supposed to deal with that?"
                elif Partner == EmmaX:
                        ch_e "You expect me to stoop to clean-up duty?"
                elif Partner == LauraX:
                        ch_l "Real mess you left me there."
                elif Partner == JeanX:
                        ch_j "So I'm your maid now?"
                elif Partner == StormX:
                        ch_s "You would like me to clean her off?"
                elif Partner == JubesX:
                        ch_v "Could I? . ."
        elif LineNum == 3:
                # She's obedient. . .
                if Partner == RogueX:
                        ch_r "If you say so."
                elif Partner == KittyX:
                        ch_k "Whatever."
                elif Partner == EmmaX:
                        ch_e "Lovely."
                elif Partner == LauraX:
                        ch_l "On it."
                elif Partner == JeanX:
                        ch_j "Sure. . ."
                elif Partner == StormX:
                        ch_s ". . . Fine."
                elif Partner == JubesX:
                        ch_v "Sure. . ."
        elif LineNum == 4:
                # She likes the other girl. . .
                if Partner == RogueX:
                        ch_r "Well, if she doesn't mind. . ."
                elif Partner == KittyX:
                        ch_k "I guess I don't mind if she doesn't."
                elif Partner == EmmaX:
                        ch_e "Very well, come over here, dear."
                elif Partner == LauraX:
                        ch_l "She is a bit messy. . ."
                elif Partner == JeanX:
                        ch_j "Well, if I must. . ."
                elif Partner == StormX:
                        ch_s "Very well, come here."
                elif Partner == JubesX:
                        ch_v "Cool. . ."
        elif LineNum == 5:
                # She's likes you enough to listen. . .
                if Partner == RogueX:
                        ch_r "I s'pose so. . ."
                elif Partner == KittyX:
                        ch_k "I guess I could. . ."
                elif Partner == EmmaX:
                        ch_e "I suppose she'd do the same for me."
                elif Partner == LauraX:
                        ch_l "I guess someone has to."
                elif Partner == JeanX:
                        ch_j "Fine, whatever."
                elif Partner == StormX:
                        ch_s "I suppose that I could. . ."
                elif Partner == JubesX:
                        ch_v "Sure. . ."
        elif LineNum == 6:
                # She's likes you enough to wipe, not lick. . .
                if Partner == RogueX:
                        ch_r "I can wipe her off, I guess, but that's it. . ."
                elif Partner == KittyX:
                        ch_k "I'm not {i}that{/i} catlike. . ."
                elif Partner == EmmaX:
                        ch_e "I'll just use my hands, if you don't mind."
                elif Partner == LauraX:
                        ch_l "I don't know, I'll just use my hands."
                elif Partner == JeanX:
                        ch_j "I'm not doing that, but I guess I can clean her off."
                elif Partner == StormX:
                        ch_s "I will wipe her clean, but not. . . with my tongue."
                elif Partner == JubesX:
                        ch_v "I guess I could just wipe her off. . ."
        elif LineNum == 7:
                # She's obedient. . .
                if Partner == RogueX:
                        ch_r "Well, that's y'all's business. . ."
                elif Partner == KittyX:
                        ch_k "No way."
                elif Partner == EmmaX:
                        ch_e "I'm afraid not, [EmmaX.Petname]."
                elif Partner == LauraX:
                        ch_l "I'd rather not."
                elif Partner == JeanX:
                        ch_j "I don't think so. . ."
                elif Partner == StormX:
                        ch_s ". . . I will not."
                elif Partner == JubesX:
                        ch_v "Sure. . ."
        if not Girl:
                return
        #from the response portion. . .
        elif LineNum == 8:
                # She's into the other girl. . .
                if Girl == RogueX:
                        ch_r "Well, how could I turn down such an attractive offer. . ."
                elif Girl == KittyX:
                        ch_k "I mean[KittyX.like]she seems so into it. . ."
                elif Girl == EmmaX:
                        ch_e "I'll allow it, since she seems so excited by it. . ."
                elif Girl == LauraX:
                        ch_l "I could do worse than her."
                elif Girl == JeanX:
                        ch_j "Well. . . if we have to. . ."
                elif Girl == StormX:
                        ch_s "That would be lovely, [Partner.Name]."
                elif Partner == JubesX:
                        ch_v "Cool. . ."
        elif LineNum == 9:
                # She's into you enough. . .
                if Girl == RogueX:
                    ch_r "If that's what turns you on. . ."
                elif Girl == KittyX:
                    ch_k "I guess if you wanna. . ."
                elif Girl == EmmaX:
                    ch_e "I'll allow it, if you're that interested. . ."
                elif Girl == LauraX:
                    ch_l "Sure, if you're into that."
                elif Girl == JeanX:
                    ch_j "Oh, is that what you like? . ."
                elif Girl == StormX:
                        ch_s "I could do that."
                elif Partner == JubesX:
                        ch_v "Sure. . ."
        elif LineNum == 10:
                # She's into both of you a little. . .
                if Girl == RogueX:
                        ch_r "Kinda ganging up on me here. . ."
                elif Girl == KittyX:
                        ch_k "I feel totally targetted."
                elif Girl == EmmaX:
                        ch_e "Oh, fine, don't the both of you look at me like that."
                elif Girl == LauraX:
                        ch_l "More the merrier."
                elif Girl == JeanX:
                        ch_j "Sure. . ."
                elif Girl == StormX:
                        ch_s "That might be. . . nice."
                elif Partner == JubesX:
                        ch_v "Cool. . ."
        elif LineNum == 11:
                # She's not into it. . .
                if Girl == RogueX:
                        ch_r "I'm just not that kinda girl. . ."
                elif Girl == KittyX:
                        ch_k "Kinda gross, no."
                elif Girl == EmmaX:
                        ch_e "I just can't be party to that."
                elif Girl == LauraX:
                        ch_l "Hm. . . nah."
                elif Girl == JeanX:
                        ch_j "No thanks."
                elif Girl == StormX:
                        ch_s ". . . I would rather not."
                elif Partner == JubesX:
                        ch_v "Um. . ."
        elif LineNum == 12:
                # She's fine with it. . .
                if Girl == RogueX:
                        ch_r "I wouldn't mind some help. . ."
                elif Girl == KittyX:
                        ch_k "How could I say no?"
                elif Girl == EmmaX:
                        ch_e "Oh, very well. . ."
                elif Girl == LauraX:
                        ch_l "If you're offering. . ."
                elif Girl == JeanX:
                        ch_j "Well. . . if I have to. . ."
                elif Girl == StormX:
                        ch_s ". . . Fine."
                elif Partner == JubesX:
                        ch_v "Cool. . ."
        elif LineNum == 13:
                # After the other girl licked her down. . .
                if Girl == RogueX:
                        ch_r "Well that was a treat. . ."
                elif Girl == KittyX:
                        ch_k "That was. . . real nice."
                elif Girl == EmmaX:
                        ch_e "Mmmm, I might need to have you over more often."
                elif Girl == LauraX:
                        ch_l "You're really good at that."
                elif Girl == JeanX:
                        ch_j "Good job. . ."
                elif Girl == StormX:
                        ch_s "Well. . . thank you. . . [Partner.Name]."
                elif Partner == JubesX:
                        ch_v "Oh, um, thanks, I guess. . ."
        elif LineNum == 14:
                # After the other girl wiped her down. . .
                if Girl == RogueX:
                        ch_r "Piece of cake, heh. . ."
                elif Girl == KittyX:
                        ch_k "Um, thanks."
                elif Girl == EmmaX:
                        ch_e "Thank you, dear, I hope that wasn't too much bother."
                elif Girl == LauraX:
                        ch_l "That was easy."
                elif Girl == JeanX:
                        ch_j "I guess that was. . . thorough. . ."
                elif Girl == StormX:
                        ch_s "Well. . . thank you. . . [Partner.Name]."
                elif Partner == JubesX:
                        ch_v "Oh, um, thanks, I guess. . ."
        return

label Partner_Clean_Girl(Girl=0): #rkeljsv
    #either "partner wipe" or Choice == "partner lick"

    if Choice != "partner wipe" and Choice != "partner lick":
        return

    if Choice == "partner lick":
            $ Partner.FaceChange("tongue")
    else:
            $ Partner.Spunk.append("hand")
    $ Cnt = 0
    if "chin" in Girl.Spunk or "mouth" in Girl.Spunk:
            while "chin" in Girl.Spunk:
                    $ Girl.Spunk.remove("chin")
            $ Girl.GLG(Partner,900,2,1)
            $ Partner.GLG(Girl,900,2,1)
            if Choice == "partner lick":
                    if "mouth" not in Partner.Spunk:
                            $ Partner.Spunk.append("mouth")
                    if "chin" not in Partner.Spunk:
                            $ Partner.Spunk.append("chin")
                    $ Partner.Statup("Lust", 80, 3)
                    $ Girl.Statup("Lust", 80, 4)
                    $ Player.Statup("Focus",80,3)
                    "[Partner.Name] licks her way up [Girl.Name]'s chin, before deeply kissing her."
            else:
                    $ Girl.Statup("Lust", 80, 2)
                    "[Partner.Name] wipes her thumb across [Girl.Name]'s chin,"
            $ Cnt += 1
    if "mouth" in Girl.Spunk and Cnt:
            $ Girl.Spunk.remove("mouth")
            "you can see a line of jiz stretching between their mouths."
            $ Cnt += 1
    if "hair" in Girl.Spunk:
            $ Girl.Spunk.remove("hair")
            if Cnt:
                "then she wipes the spunk out of [Girl.Name]'s hair,"
            else:
                "[Partner.Name] wipes the spunk out of [Girl.Name]'s hair,"
            $ Cnt += 1
    if "facial" in Girl.Spunk:
            $ Girl.Spunk.remove("facial")
            if Choice == "partner lick":
                    if "mouth" not in Partner.Spunk:
                            $ Partner.Spunk.append("mouth")
                    if "chin" not in Partner.Spunk:
                            $ Partner.Spunk.append("chin")
                    $ Partner.Statup("Lust", 80, 2)
                    $ Girl.Statup("Lust", 80, 4)
                    $ Player.Statup("Focus",80,3)
                    if Cnt:
                        "then she licks the spunk off of [Girl.Name]'s face,"
                    else:
                        "[Partner.Name] licks the spunk off of [Girl.Name]'s face,"
            else:
                    $ Girl.Statup("Lust", 80, 1)
                    if Cnt:
                        "then she wipes the spunk off of [Girl.Name]'s face,"
                    else:
                        "[Partner.Name] wipes the spunk off of [Girl.Name]'s face,"
            $ Cnt += 1
    if "tits" in Girl.Spunk:
            $ Girl.Spunk.remove("tits")
            $ Girl.GLG(Partner,900,2,1)
            if Choice == "partner lick":
                    if "mouth" not in Partner.Spunk:
                            $ Partner.Spunk.append("mouth")
                    if "chin" not in Partner.Spunk:
                            $ Partner.Spunk.append("chin")
                    $ Partner.Statup("Lust", 80, 2)
                    $ Girl.Statup("Lust", 200, 4)
                    $ Player.Statup("Focus",80,4)
                    if Cnt:
                        "then she licks her way across [Girl.Name]'s chest,"
                    else:
                        "[Partner.Name] licks her way across [Girl.Name]'s chest,"
            else:
                    $ Partner.Statup("Lust", 80, 2)
                    $ Girl.Statup("Lust", 80, 2)
                    $ Player.Statup("Focus",80,2)
                    if Cnt:
                        "then she wipes the spunk off of [Girl.Name]'s chest,"
                    else:
                        "[Partner.Name] wipes the spunk off of [Girl.Name]'s chest,"
            $ Cnt += 1
    if "belly" in Girl.Spunk:
            $ Girl.Spunk.remove("belly")
            if Choice == "partner lick":
                    if "mouth" not in Partner.Spunk:
                            $ Partner.Spunk.append("mouth")
                    if "chin" not in Partner.Spunk:
                            $ Partner.Spunk.append("chin")
                    $ Partner.Statup("Lust", 80, 2)
                    $ Girl.Statup("Lust", 80, 3)
                    $ Player.Statup("Focus",80,1)
                    if Cnt:
                        "then she licks her way down [Girl.Name]'s belly,"
                    else:
                        "[Partner.Name] licks her way down [Girl.Name]'s belly,"
            else:
                    $ Partner.Statup("Lust", 80, 1)
                    $ Girl.Statup("Lust", 80, 1)
                    if Cnt:
                        "then she wipes the spunk off of [Girl.Name]'s belly,"
                    else:
                        "[Partner.Name] wipes the spunk off [Girl.Name]'s belly,"
            $ Cnt += 1
    if "back" in Girl.Spunk:
            $ Girl.Spunk.remove("back")
            if Choice == "partner lick":
                    if "mouth" not in Partner.Spunk:
                            $ Partner.Spunk.append("mouth")
                    if "chin" not in Partner.Spunk:
                            $ Partner.Spunk.append("chin")
                    $ Girl.Statup("Lust", 80, 2)
                    if Cnt:
                        "then she licks her way up [Girl.Name]'s lower back,"
                    else:
                        "[Partner.Name] licks her way up [Girl.Name]'s lower back,"
            else:
                    $ Girl.Statup("Lust", 80, 1)
                    if Cnt:
                        "then she wipes the spunk off of [Girl.Name]'s lower back,"
                    else:
                        "[Partner.Name] wipes the spunk off [Girl.Name]'s lower back,"
            $ Cnt += 1
    if "in" in Girl.Spunk:
            $ Girl.Spunk.remove("in")
            $ Girl.GLG(Partner,900,5,1)
            if Choice == "partner lick":
                    if "mouth" not in Partner.Spunk:
                            $ Partner.Spunk.append("mouth")
                    if "chin" not in Partner.Spunk:
                            $ Partner.Spunk.append("chin")
                    $ Partner.Statup("Lust", 80, 4)
                    $ Girl.Statup("Lust", 200, 6)
                    $ Player.Statup("Focus",80,6)
                    if Cnt:
                        "then she sucks gently at [Girl.Name]'s pussy,"
                    else:
                        "[Partner.Name] bends down and sucks gently at [Girl.Name]'s pussy,"
            else:
                    $ Partner.Statup("Lust", 80, 2)
                    $ Girl.Statup("Lust", 200, 4)
                    $ Player.Statup("Focus",80,4)
                    if Cnt:
                        "then she strokes along [Girl.Name]'s pussy, wiping the spunk clean,"
                    else:
                        "[Partner.Name] strokes along [Girl.Name]'s pussy, wiping the spunk clean,"
            $ Cnt += 1
    if "anal" in Girl.Spunk:
            $ Girl.Spunk.remove("anal")
            $ Girl.GLG(Partner,900,5,1)
            if Choice == "partner lick" and ApprovalCheck(Partner, 800, "I"):
                    if "mouth" not in Partner.Spunk:
                            $ Partner.Spunk.append("mouth")
                    if "chin" not in Partner.Spunk:
                            $ Partner.Spunk.append("chin")
                    $ Partner.Statup("Lust", 80, 2)
                    $ Girl.Statup("Lust", 200, 6)
                    $ Player.Statup("Focus",80,5)
                    if Cnt:
                        "then she licks up the spunk dripping out of [Girl.Name]'s ass,"
                    else:
                        "[Partner.Name] licks up the spunk dripping our of [Girl.Name]'s ass,"
            else:
                    $ Partner.Statup("Lust", 80, 2)
                    $ Girl.Statup("Lust", 200, 6)
                    $ Player.Statup("Focus",80,3)
                    if Cnt:
                        "then she wipes the spunk dripping out of [Girl.Name]'s ass, discarding it,"
                    else:
                        "[Partner.Name] wipes the spunk dripping our of [Girl.Name]'s ass, discarding it,"
            $ Cnt += 1

    $ Partner.FaceChange("sly")
    if "hand" in Girl.Spunk:
            $ Girl.Spunk.remove("hand")
            if Choice == "partner lick":
                    if "mouth" not in Partner.Spunk:
                            $ Partner.Spunk.append("mouth")
                    if "chin" not in Partner.Spunk:
                            $ Partner.Spunk.append("chin")
                    $ Girl.Statup("Lust", 80, 3)
                    $ Player.Statup("Focus",80,3)
                    if Cnt:
                        "and finally she licks [Girl.Name]'s hands off with a satisfied grin."
                    else:
                        "[Partner.Name] licks [Girl.Name]'s fingertips with a satisfied grin."
            else:
                    if Cnt:
                        "and finally she wipes [Girl.Name]'s hands clean."
                    else:
                        "[Partner.Name] wipes [Girl.Name]'s hands off with a satisfied grin."

            if Choice == "partner lick" or ApprovalCheck(Partner, 1000):
                    #if the partner swallows
                    while "mouth" in Partner.Spunk:
                            $ Partner.Spunk.remove("mouth")
                    while "chin" in Partner.Spunk:
                            $ Partner.Spunk.remove("chin")
                    $ Girl.Statup("Inbt", 80, 2)
                    $ Player.Statup("Focus",80,3)
                    "Then [Partner.Name] swallows and wipes her mouth."
                    $ Partner.Swallow += 1
                    $ Partner.Addict -= (10*Cnt)
                    if Partner.Swallow == 1:
                        $ Partner.SEXP += 12
                    $ Partner.RecentActions.append("swallowed")
                    $ Partner.DailyActions.append("swallowed")
            else:
                #if the Partner won't swallow
                if Cnt:
                    "and finally, she wipes her own hands off with a nearby tissue."
                else:
                    "[Partner.Name] wipes her own hands off with a nearby tissue."
            $ Cnt += 1
    $ Girl.Spunk = []
    $ Partner.Spunk = []
    return

# End Clean-up  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
