#Start Date_Shopping   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Mall_Entry(First=0,Second=0,Girl=0,Cart=[]):
        call Jubes_Entry_Check
        $ Player.DrainWord("locked",0,0,1)
        $ bg_current = "bg mall"
        $ Nearby = []
        call Gym_Clothes_Off #call Gym_Clothes
        call Taboo_Level
        $ Player.RecentActions.append("traveling")
        call EventCalls

label Shopping_Mall(First=0,Second=0,Girl=0,Cart=[]):
        #this is the mall
        $ bg_current = "bg mall"
        $ Player.RecentActions.append("shopping")
        $ Player.DailyActions.append("shopping")
        $ BO = Party[:]
        while BO:
            $ BO[0].Loc = "bg mall"
            $ BO.remove(BO[0])

        call Set_The_Scene
        "You're at the Salem Centre Mall."
        if len(Party) >= 2:
                $ First = Party[0]
                $ Second = Party[1]
                "You wander the various stores with the girls, seeing what they have to offer. . ."
        elif len(Party) >= 1:
                $ First = Party[0]
                "You wander the various stores with [Party[0].Name], seeing what they have to offer. . ."
        else:
                "You wander the various stores, seeing what they have to offer. . ."
        menu Mall_Menu:
            "Where would you like to go?"
            "Enter the Sex Shop" if Round > 20:
                    call Sex_Shop

            "Enter Lingerie Shop" if Round > 20:
                    call Lingerie_Shop

            "Enter Swimwear Shop" if Round > 20:
                    call Swim_Shop

            "Wait around a bit" if "date" not in Player.RecentActions:
                    #set to not during date
                    "You wait around a bit."
                    call Wait
                    call EventCalls
                    call Girls_Location
                    if Time_Count >= 3: #night time
                        ch_u "The mall is now closing, please head to the nearest exit. . ."
                        "You head back to campus."
                        jump Campus_Entry

            "Head back to school" if "date" not in Player.RecentActions:
                    #set to not during date
                    jump Campus_Entry

            #special dating options
            "Just wander and window shop" if Party and Round > 20:
                    #only during date
                    if len(Party) >= 2:
                            if renpy.random.randint(1, 20) > 10:
                                    $ Party[0].Statup("Love", 80, 1)
                                    $ Party[0].Statup("Obed", 50, 1)
                                    $ Party[0].Statup("Inbt", 50, 1)
                                    $ Party[1].Statup("Love", 80, 1)
                                    $ Party[1].Statup("Obed", 50, 1)
                                    $ Party[1].Statup("Inbt", 50, 1)
                            "You wander around with the girls and see what they have available."
                    else:
                            if renpy.random.randint(1, 20) > 10:
                                    $ Party[0].Statup("Love", 80, 1)
                                    $ Party[0].Statup("Obed", 50, 1)
                                    $ Party[0].Statup("Inbt", 50, 1)
                            "You wander around with [Party[0].Name]and see what they have available."
                    $ Round -= 10

            "Do something else" if "date" in Player.RecentActions and Round > 20:
                    #only during date
                    jump Date_Location

            "Head back to school" if "date" in Player.RecentActions:
                    #only during date
                    if "movie" in Player.RecentActions or "dinner" in Player.RecentActions or Round < 30 or not Party:
                            show blackscreen onlayer black with dissolve
                            "It's getting late, you head back to the dorms. . ."
                            jump Date_End
                    else:
                            #if there's still time and not much has happened. . .
                            if Party[0] in (EmmaX,StormX):
                                    call AnyLine(Party[0],"Oh, I was expecting more. . .")
                            elif Party[0] in (JeanX,LauraX):
                                    call AnyLine(Party[0],"Is that it?")
                            else:
                                    call AnyLine(Party[0],"Aw. . . we aren't doing anything else?")
                            menu:
                                "Continue Shopping":
                                        jump Mall_Menu
                                "Do something else":
                                        jump Date_Location
                                "Head back to school [[seriously this time]":
                                        ch_p "Yeah, let's head back."
                                        call AnyLine(Party[0],"Fine. . .")
                                        show blackscreen onlayer black with dissolve
                                        "It's getting late, you head back to the dorms. . ."
                                        jump Date_End


        if Time_Count >= 3 or Round < 20:
                if "date" in Player.RecentActions:
                         #if on a date
                        show blackscreen onlayer black with dissolve
                        "It's getting late, you head back to the dorms. . ."
                        jump Date_End
                ch_u "The mall is now closing, please head to the nearest exit. . ."
                "You head back to campus."
                jump Campus_Entry
        jump Mall_Menu


label Sex_Shop:
        # jumped to from Mall Menu
        $ bg_current = "bg shop"
        $ BO = Party[:]
        while BO:
            $ BO[0].Loc = "bg shop"
            $ BO.remove(BO[0])

        call Set_The_Scene
        $ Girl = 0
        "You head into Spiral's Body Shoppe. . ."
        while True:
                if Round <= 20:
                    "It's getting late, you head back into the mall. . ."
                    $ Girl = 0
                    return
                menu:
                    "What did you want to purchase?"
                    "Buy dildo for $20.":
                            if Player.Inventory.count("dildo") >= 10:
                                "You already have way more dildos than you need. 2, 4, 6. . . yes, way too many."
                            elif Player.Cash >= 20:
                                "You purchase one dildo."
                                $ Player.Inventory.append("dildo")
                                $ Player.Cash -= 20
                                if First:
                                    if ApprovalCheck(Girl, 800):
                                        $ First.FaceChange("sly")
                                        $ First.Statup("Love", 80, 1)
                                        $ First.Statup("Obed", 50, 3)
                                        $ First.Statup("Inbt", 50, 3)
                                        if First == RogueX:
                                                ch_r "Oh, what's that for, [Girl.Petname]?"
                                        elif First == KittyX:
                                                ch_k "Is that for. . ."
                                        elif First == EmmaX:
                                                ch_e "Hmm. . ."
                                        elif First == LauraX:
                                                ch_l ". . ."
                                        elif First == JeanX:
                                                pass #ch_j "Eye on the prize, [Girl.Petname]."
                                        elif First == StormX:
                                                ch_s "Well that's certainly interesting. . ."
                                        elif First == JubesX:
                                                ch_v "What're you gonna do with that. . ."
                                    else:
                                        $ First.FaceChange("confused",2)
                                        $ First.Statup("Love", 60, -2)
                                        $ First.Statup("Obed", 70, 4)
                                        $ First.Statup("Inbt", 50, 2)
                                        if First == RogueX:
                                                ch_r "Is that. . . oh. . ."
                                        elif First == KittyX:
                                                ch_k "Um, what's that about. . ."
                                        elif First == EmmaX:
                                                ch_e "This is certainly an unusual trip. . ."
                                        elif First == LauraX:
                                                ch_l ". . ."
                                        elif First == JeanX:
                                                pass #ch_j "Eye on the prize, [Girl.Petname]."
                                        elif First == StormX:
                                                ch_s "Interesting choice. . ."
                                        elif First == JubesX:
                                                ch_v "What're you gonna do with that. . ."
                                        $ First.FaceChange("confused",1)
                                    $ First.Statup("Lust", 60, 5)
                            else:
                                "You don't have enough for that."

                    "Buy \"Shocker\" vibrator for $25.":
                            if Player.Inventory.count("vibrator") >= 10:
                                "If you bought one more vibrator, you would risk a geological event."
                            elif Player.Cash >= 25:
                                "You purchase one vibrator."
                                $ Player.Inventory.append("vibrator")
                                $ Player.Cash -= 25
                                if First:
                                    if ApprovalCheck(Girl, 800):
                                        $ First.FaceChange("sly")
                                        $ First.Statup("Love", 80, 2)
                                        $ First.Statup("Obed", 50, 2)
                                        $ First.Statup("Inbt", 50, 3)
                                        if First == RogueX:
                                                ch_r "Oh, what's that for, [Girl.Petname]?"
                                        elif First == KittyX:
                                                ch_k "Is that for. . ."
                                        elif First == EmmaX:
                                                ch_e "Hmm. . ."
                                        elif First == LauraX:
                                                ch_l ". . ."
                                        elif First == JeanX:
                                                pass #ch_j "Eye on the prize, [Girl.Petname]."
                                        elif First == StormX:
                                                ch_s "Well that's certainly interesting. . ."
                                        elif First == JubesX:
                                                ch_v "What're you gonna do with that. . ."
                                        $ First.Statup("Lust", 60, 5)
                                    else:
                                        $ First.FaceChange("confused",2)
                                        $ First.Statup("Obed", 70, 2)
                                        $ First.Statup("Inbt", 50, 2)
                                        if First == RogueX:
                                                ch_r "Is that. . . oh. . ."
                                        elif First == KittyX:
                                                ch_k "Um, what's that about. . ."
                                        elif First == EmmaX:
                                                ch_e "This is certainly an unusual trip. . ."
                                        elif First == LauraX:
                                                ch_l ". . ."
                                        elif First == JeanX:
                                                pass #ch_j "Eye on the prize, [Girl.Petname]."
                                        elif First == StormX:
                                                ch_s "Interesting choice. . ."
                                        elif First == JubesX:
                                                ch_v "What're you gonna do with that. . ."
                                        $ First.FaceChange("confused",1)
                            else:
                                "You don't have enough for that."
                    "Give a gift to [First.Name]." if First:
                            $ Girl = First
                    "Give a gift to [Second.Name]." if Second:
                            $ Girl = Second
                    "Exit.":
                            "You head back into the mall. . ."
                            $ Round -= 10 if Round > 20 else (Round-10) #reduces Round to at minimum 10
                            $ Girl = 0
                            $ bg_current = "bg mall"
                            $ BO = Party[:]
                            while BO:
                                $ BO[0].Loc = "bg mall"
                                $ BO.remove(BO[0])

                            call Set_The_Scene
                            return

                #End shop menu
                if Girl:
                    menu:
                        "Gift a Dildo" if "dildo" in Player.Inventory:
                            #If you have a Dildo, you'll give it.
                            if "dildo" not in Girl.Inventory:
                                    "You give [Girl.Name] the dildo."
                                    $ Girl.Blush = 1
                                    $ Girl.ArmPose = 2
                                    $ Girl.Held = "dildo"
                                    if ApprovalCheck(Girl, 800):
                                            $ Girl.FaceChange("bemused")
                                            $ Player.Inventory.remove("dildo")
                                            $ Girl.Inventory.append("dildo")
                                            $ Girl.Statup("Love", 200, 30)
                                            $ Girl.Statup("Obed", 200, 30)
                                            $ Girl.Statup("Inbt", 200, 30)
                                            if Girl == RogueX:
                                                    ch_r "Well, I've got some ideas in mind for this. . ."
                                            elif Girl == LauraX:
                                                    ch_l "Oh, cool, I've wanted one of these. . ."
                                            else:
                                                    call AnyLine(Girl,"I'm sure I can find some place to store it. . .")
                                            $ Girl.Statup("Lust", 89, 10)
                                    elif ApprovalCheck(Girl, 600):
                                            $ Girl.FaceChange("confused")
                                            $ Player.Inventory.remove("dildo")
                                            $ Girl.Inventory.append("dildo")
                                            if Girl != EmmaX:
                                                    $ Girl.Statup("Love", 200, 10)
                                                    $ Girl.Statup("Obed", 200, 10)
                                                    $ Girl.Statup("Inbt", 200, 10)
                                            if Girl == RogueX:
                                                    ch_r "Huh, well I guess I can find a place for it. . ."
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    $ Girl.FaceChange("surprised")
                                                    ch_r "I- I mean. . . I'll just put it away."
                                            elif Girl == KittyX:
                                                    ch_k "I don't know what. . ."
                                                    $ Girl.Statup("Lust", 89, 5)
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    $ Girl.FaceChange("surprised")
                                                    ch_k "Oh!"
                                                    ch_k "Oh. . . I'll just[Girl.like]put it away."
                                            elif Girl == EmmaX:
                                                    ch_e "This is not an appropriate gift from a student. . ."
                                                    $ Girl.Statup("Lust", 89, 5)
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    $ Girl.FaceChange("sadside",1)
                                                    ch_e "Hm. . ."
                                                    $ Girl.Statup("Love", 200, 10)
                                                    $ Girl.Statup("Obed", 200, 10)
                                                    $ Girl.Statup("Inbt", 200, 10)
                                                    $ Girl.FaceChange("sly")
                                                    ch_e "I suppose I can find {i}some{/i} use for it. . ."
                                            elif Girl == LauraX:
                                                    ch_l "Huh, you're a weird gift giver."
                                                    $ Girl.Statup("Lust", 89, 5)
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    $ Girl.FaceChange("smile")
                                                    ch_l "It's very thoughtful though."
                                            elif Girl == JeanX:
                                                    $ Girl.Statup("Lust", 89, 5)
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    ch_j "Well we know where your mind it at."
                                                    $ Girl.FaceChange("smile")
                                                    ch_j "I guess I should be flattered. . ."
                                            elif Girl == StormX:
                                                    if StormX not in Rules:
                                                            $ Girl.FaceChange("sadside",1)
                                                            ch_s "I don't know that I should accept this from a student. . ."
                                                    $ Girl.Statup("Lust", 89, 5)
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    ch_s "Hm. . ."
                                                    $ Girl.FaceChange("sly")
                                                    ch_s "Thank you for the thought. . ."
                                            elif Girl == JubesX:
                                                    ch_v "I guess I have some use for it. . ."
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    $ Girl.FaceChange("surprised")
                                                    ch_v "I- I mean. . . decorative."
                                            $ Girl.FaceChange("bemused")
                                    elif "offered gift" in Girl.DailyActions:
                                            $ Girl.FaceChange("angry")
                                            "She hands it back to you."
                                            if Girl == RogueX:
                                                    ch_r "Look, maybe you should just rethink your gift-giving choices?"
                                            elif Girl == KittyX:
                                                    ch_k "I think I[Girl.like]made myself clear about inappropriate gifts?"
                                            elif Girl == EmmaX:
                                                    ch_e "I think I have made myself clear about inappropriate gifts?"
                                            elif Girl == LauraX:
                                                    ch_l "I said I can't take something like this."
                                            elif Girl == JeanX:
                                                    ch_j "I really don't need this."
                                            elif Girl == StormX:
                                                    ch_s "I repeat, this is not something I need."
                                            elif Girl == JubesX:
                                                    ch_v "This really isn't something I need. . ."
                                    else:
                                            $ Girl.FaceChange("angry")
                                            $ Girl.Statup("Love", 50, -20)
                                            $ Girl.Statup("Obed", 20, 10)
                                            $ Girl.Statup("Inbt", 20, 20)
                                            if Girl == RogueX:
                                                    ch_r "That's a pretty forward gift to be giving a lady. . ."
                                            elif Girl == KittyX:
                                                    ch_k "I- you shouldn't be giving girls stuff like this!"
                                            elif Girl == EmmaX:
                                                    ch_e "[Girl.Petname], I don't believe this is an appropriate gift from a student."
                                            elif Girl == LauraX:
                                                    ch_l "I don't think you should just be handing these out to random chicks."
                                            elif Girl == JeanX:
                                                    ch_j "So you just go around handing out sex toys?"
                                            elif Girl == StormX:
                                                    ch_s "I do not appreciate the implication here."
                                            elif Girl == JubesX:
                                                    ch_v "This is an odd design for a. . . wait."
                                            $ Girl.Statup("Lust", 89, 5)
                                            "She hands it back to you."
                                            $ Girl.DailyActions.append("offered gift")
                            elif Girl.Inventory.count("dildo") == 1:
                                    $ Player.Inventory.remove("dildo")
                                    $ Girl.Inventory.append("dildo")
                                    if Girl == RogueX:
                                            ch_r "Well, I suppose I could always use another. . ."
                                    elif Girl == KittyX:
                                            ch_k "Why stop with one. . ."
                                    elif Girl == EmmaX:
                                            ch_e "I suppose I always have room for one more. . ."
                                    elif Girl == LauraX:
                                            ch_l "I don't know if I need another. . ."
                                    elif Girl == JeanX:
                                            ch_j "Oh look, another rubber cock. . ."
                                    elif Girl == StormX:
                                            ch_s "Oh, another one. . ."
                                    elif Girl == JubesX:
                                            ch_v "I don't need more. . ."
                            else:
                                    if Girl == RogueX:
                                            ch_r "Honestly, [Girl.Petname], I already have enough of those."
                                    elif Girl == KittyX:
                                            ch_k "I only have so many places to store these."
                                    elif Girl == EmmaX:
                                            ch_e "How many places do you think I could put these?"
                                    elif Girl == LauraX:
                                            ch_l "I'm running out of space at this point."
                                    elif Girl == JeanX:
                                            ch_j "How many holes do you think a girl has?"
                                    elif Girl == StormX:
                                            ch_s "I doubt I can find a place for this one."
                                    elif Girl == JubesX:
                                            ch_v "This is way too many. . ."
                            $ Girl.Held = 0
                            $ Girl.ArmPose = 2
                            $ Girl = 0
                        # end "Gift a Dildo"
                        "Gift a Dildo (locked)" if "dildo" not in Player.Inventory:
                            pass

                        "Gift a Vibrator" if "vibrator" in Player.Inventory:
                            #If you have a vibrator, you'll give it.
                            if "vibrator" not in Girl.Inventory:
                                "You give [Girl.Name] the Shocker Vibrator."
                                $ Girl.Blush = 1
                                $ Girl.ArmPose = 2
                                $ Girl.Held = "vibrator"
                                if ApprovalCheck(Girl, 700):
                                        $ Girl.FaceChange("bemused")
                                        $ Player.Inventory.remove("vibrator")
                                        $ Girl.Inventory.append("vibrator")
                                        $ Girl.Statup("Love", 200, 30)
                                        $ Girl.Statup("Obed", 200, 30)
                                        $ Girl.Statup("Inbt", 200, 30)
                                        if Girl == RogueX:
                                                ch_r "Well, I've got some ideas in mind for this. . ."
                                        elif Girl == KittyX:
                                                ch_k "Well this is. . . [[bzzzt]- "
                                                ch_k "-interesting. . ."
                                        elif Girl == EmmaX:
                                                ch_e "How very thoughtful of you. . ."
                                                $ Girl.Statup("Lust", 89, 10)
                                                $ Girl.FaceChange("sly")
                                                ch_e "I'm sure I can put this to good use. . ."
                                        elif Girl == LauraX:
                                                ch_l "This is. . . [[bzzzt]- "
                                                $ Girl.Statup("Lust", 89, 10)
                                                $ Girl.FaceChange("sly")
                                                ch_l "-some kind of sex thing, huh. . ."
                                        elif Girl == JeanX:
                                                ch_j "Oh, nifty."
                                        elif Girl == StormX:
                                                ch_s "Oh!. . . oooohhh."
                                        elif Girl == JubesX:
                                                ch_v "Oh, this could be nice. . ."
                                        $ Girl.Statup("Lust", 89, 10)
                                elif ApprovalCheck(Girl, 400):
                                        $ Girl.FaceChange("confused")
                                        $ Player.Inventory.remove("vibrator")
                                        $ Girl.Inventory.append("vibrator")
                                        $ Girl.Statup("Love", 200, 10)
                                        $ Girl.Statup("Obed", 200, 10)
                                        $ Girl.Statup("Inbt", 200, 10)
                                        if Girl == RogueX:
                                                ch_r "I guess I can use this to work the kinks out. . ."
                                                $ Girl.Statup("Lust", 89, 10)
                                                $ Girl.FaceChange("surprised")
                                                ch_r "Muscle knots, I mean!"
                                        elif Girl == KittyX:
                                                ch_k "I've heard these are very relaxing. . ."
                                                $ Girl.Statup("Lust", 89, 10)
                                                $ Girl.FaceChange("surprised")
                                                ch_k "-for my back!"
                                        elif Girl == EmmaX:
                                                ch_e "How very thoughtful of you. . ."
                                                $ Girl.Statup("Lust", 89, 10)
                                                $ Girl.FaceChange("sly")
                                                ch_e "A back massager, I assume. . ."
                                        elif Girl == LauraX:
                                                ch_l "This is. . . [[bzzzt]- "
                                                $ Girl.FaceChange("sly")
                                                $ Girl.Statup("Lust", 89, 10)
                                                ch_l "-oooh. . ."
                                        elif Girl == JeanX:
                                                ch_j "Huh. Ok."
                                        elif Girl == StormX:
                                                ch_s "Oh, something for exercise purposes. . ."
                                        elif Girl == JubesX:
                                                ch_v "Thanks, my, uh, back's been killing me. . ."
                                        $ Girl.FaceChange("bemused", 1)
                                elif "offered gift" in Girl.DailyActions:
                                        $ Girl.FaceChange("angry")
                                        "She hands it back to you."
                                        if Girl == RogueX:
                                                ch_r "Look, maybe you should just rethink your gift-giving choices?"
                                        elif Girl == KittyX:
                                                ch_k "I think I[Girl.like]made myself clear about inappropriate gifts?"
                                        elif Girl == EmmaX:
                                                ch_e "I think I have made myself clear about inappropriate gifts?"
                                        elif Girl == LauraX:
                                                ch_l "I don't want it."
                                        elif Girl == JeanX:
                                                ch_j "I really don't need this."
                                        elif Girl == StormX:
                                                ch_s "I repeat, this is not something I need."
                                        elif Girl == JubesX:
                                                ch_v "I don't need this. . ."
                                else:
                                        $ Girl.FaceChange("angry")
                                        $ Girl.Statup("Love", 50, -20)
                                        $ Girl.Statup("Obed", 20, 10)
                                        $ Girl.Statup("Inbt", 20, 20)
                                        if Girl == RogueX:
                                                ch_r "I don't think I have much use for that."
                                        elif Girl == KittyX:
                                                ch_k "I can't really see the point."
                                        elif Girl == EmmaX:
                                                ch_e "[Girl.Petname], I don't believe this is an appropriate gift from a student."
                                        elif Girl == LauraX:
                                                ch_l "I don't need it."
                                        elif Girl == JeanX:
                                                ch_j "Huh. No, I don't need this."
                                        elif Girl == StormX:
                                                ch_s "I have no use for this."
                                        elif Girl == JubesX:
                                                ch_v "Put that away. . ."
                                        $ Girl.Statup("Lust", 89, 5)
                                        "She hands it back to you."
                                        $ Girl.DailyActions.append("offered gift")
                            else:
                                        if Girl == RogueX:
                                            ch_r "[Girl.Petname], I only need the one."
                                        elif Girl == EmmaX:
                                            ch_e "I already have plenty."
                                        else:
                                            call AnyLine(Girl,"I already have one of these.")
                            $ Girl.Held = 0
                            $ Girl.ArmPose = 2
                            $ Girl = 0
                        #end "Gift a Vibrator"
                        "Gift a Vibrator (locked)" if "vibrator" not in Player.Inventory:
                            pass

                        "Never Mind":
                            $ Girl = 0
        # end Body Shoppe while loop
        return

#End Sex Shop   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Swim_Shop:
        #this one will loop the "try something on menu" until you leave,
        #if you pick a girl, it sees if she's willing to try stuff on.
        #if she is, it loops the "dressing room" area until you try to leave
        #then it loops the "empty cart" menu until it's empty.

        $ bg_current = "bg shop"
        $ BO = Party[:]
        while BO:
            $ BO[0].Loc = "bg shop"
            $ BO.remove(BO[0])

        call Set_The_Scene
        $ Girl = 0
        "You head into \"The Swimsuit Issue\". . ."
        while True:
                if Round <= 20:
                    "It's getting late, you head back into the mall. . ."
                    $ Girl = 0
                    return
                menu:
                    "What did you want to do?"
                    "Have [First.Name] try something on." if First:
                            $ Girl = First
                    "Have [Second.Name] try something on." if Second:
                            #swaps first and second
                            $ Girl = Second
                            $ Second = First
                            $ First = Girl
                    "Exit.":
                            "You head back into the mall. . ."
                            $ Girl = 0
                            $ bg_current = "bg mall"
                            $ BO = Party[:]
                            while BO:
                                $ BO[0].Loc = "bg mall"
                                $ BO.remove(BO[0])

                            call Set_The_Scene
                            return
                #End shop menu

                if Girl:
                        #checks if they are ok with shopping for bikinis with you, kicks out if not
                        $ Girl.FaceChange("smile",1)
                        if Girl.Swim[0]:
                            #if she already has a suit. . .
                            if Girl == RogueX:
                                    ch_r "I'm already set on that. . ."
                            elif Girl == KittyX:
                                    ch_k "I[KittyX.like]don't think I really need -another- one. . ."
                            elif Girl == EmmaX:
                                    ch_e "I don't really need more of those. . ."
                            elif Girl == LauraX:
                                    ch_l "I already have a suit. . ."
                            elif Girl == JeanX:
                                    ch_j "Oh, I don't need one of those."
                            elif Girl == StormX:
                                    ch_s "I have plenty of those. . ."
                            elif Girl == JubesX:
                                    ch_v "I already got one!"
                        elif ApprovalCheck(Girl, 800) or ApprovalCheck(Girl, 600, "L") or ApprovalCheck(Girl, 300, "O"):
                            #if she agrees. . .
                            if Girl == RogueX:
                                    ch_r "Oh, we're looking for a nice suit?"
                            elif Girl == KittyX:
                                    ch_k "Oh, um, I guess we could shop for suits. . ."
                            elif Girl == EmmaX:
                                    ch_e "I suppose we could pick something out. . ."
                            elif Girl == LauraX:
                                    ch_l "Oh, I guess I do need a suit. . ."
                            elif Girl == JeanX:
                                    ch_j "Oh, what're you getting?"
                            elif Girl == StormX:
                                    ch_s "I suppose I should get something for the pool area. . ."
                            elif Girl == JubesX:
                                    ch_v "I guess I do need a new suit now. . ."
                        else:
                            if Girl == RogueX:
                                    ch_r "Oh, no thank you."
                            elif Girl == KittyX:
                                    ch_k "Oh, um, I don't really need one. . ."
                            elif Girl == EmmaX:
                                    ch_e "I think that's a bit inappropriate. . ."
                            elif Girl == LauraX:
                                    ch_l "Not interested. . ."
                            elif Girl == JeanX:
                                    ch_j "No, I'm good."
                            elif Girl == StormX:
                                    ch_s "I don't think that I should. . ."
                            elif Girl == JubesX:
                                    ch_v "I don't really want to shop for that. . ."
                            $ Girl = 0
                #end checks if they are ok with shopping for bikinis with you, kicks out if not

                if Girl:
                    #if she agreed to shop for a suit. . .
                    "You grab some things and head into one of the dressing rooms with [Girl.Name]."
                    $ bg_current = "bg dressing"
                    $ Girl.Loc = "bg dressing"
                    if Second:
                        #if there is a second girl
                        "Should [Second.Name] come too?"
                        menu:
                            "Sure":
                                    "[Second.Name] follows you in."
                                    $ Second.Loc = "bg dressing"
                            "Probably not.":
                                    ch_p "[Second.Name], probably hang back."
                                    call AnyLine(Second,"Fine. I'll just wait here then.")
                    if Second and Second.Loc == bg_current:
                            #if the other girl agreed to come along
                            call Set_The_Scene
                    else:
                            #if the other girl didn't agree to come along
                            show blackscreen onlayer black
                            call AllHide
                            call display_background
                            $ Girl.sprite_location = StageCenter
                            $ Girl.Layer = 100
                            call Display_Girl(Girl,0,0)

                            hide blackscreen onlayer black
                    $ Player.Traits.append("locked")
                    call Taboo_Level

                    while Girl:
                        menu:
                            "What did you want to try on here?"
                            "Bikini Top (locked)" if Girl.Chest == "bikini top":
                                            pass
                            "Bikini Top" if Girl.Chest != "bikini top":
                                            if Girl.SeenChest or ApprovalCheck(Girl, 1100, TabM=2):
                                                call Dressing_Strip_Bra("bikini top")
                                            else:
                                                call AnyLine(Girl,"I'll need some privacy here. . .")
                                                show blackscreen onlayer black
                                                if Girl == JubesX: #removes coat
                                                        $ Girl.Acc = 0
                                                $ Girl.Over = 0
                                                $ Girl.Chest = "bikini top"
                                                "You back out of the room for a moment. . ."
                                                hide blackscreen onlayer black
                                            if "bikini top" in Cart:
                                                pass
                                            elif "bikini top" in Girl.Inventory:
                                                call AnyLine(Girl,"I do already have one of these though.")
                                            else:
                                                $ Cart.append("bikini top")
                                                if Girl == StormX and Girl.Chest == "bikini top" and Girl.Panties == "bikini bottoms":
                                                        ch_s "Oh! I understand the purpose of the flap now!"
                            #End bikini top


                            "Bikini Bottoms (locked)" if Girl.Panties == "bikini bottoms":
                                            pass
                            "Bikini Bottoms" if Girl.Panties != "bikini bottoms":
                                            if Girl.SeenPussy or ApprovalCheck(Girl, 1200, TabM=2):
                                                call Dressing_Strip_Panties("bikini bottoms")
                                            else:
                                                call AnyLine(Girl,"I'll need some privacy here. . .")
                                                show blackscreen onlayer black
                                                $ Girl.Legs = 0
                                                $ Girl.Hose = 0
                                                $ Girl.Panties = "bikini bottoms"
                                                "You back out of the room for a moment. . ."
                                                hide blackscreen onlayer black
                                            if "bikini bottoms" in Cart:
                                                pass
                                            elif "bikini bottoms" in Girl.Inventory:
                                                call AnyLine(Girl,"I do already have one of these though.")
                                            else:
                                                $ Cart.append("bikini bottoms")
                                                if Girl == StormX and Girl.Chest == "bikini top" and Girl.Panties == "bikini bottoms":
                                                        ch_s "Oh! I understand the purpose of the flap now!"
                            #End bikini bottoms


                            "Blue swim skirt (locked)" if Girl == KittyX and Girl.Legs == "blue skirt":
                                            pass
                            "Blue swim skirt" if Girl == KittyX and Girl.Legs != "blue skirt":
                                            $ Girl.FaceChange("smile")
                                            if (Girl.Panties and ApprovalCheck(Girl, 900, TabM=2)) or ApprovalCheck(Girl, 1200, TabM=2):
                                                call AnyLine(Girl,"Sure. . .")
                                                $ Girl.Upskirt = 1
                                                pause 0.3
                                                $ Girl.Legs = 0
                                                call expression Girl.Tag + "_First_Bottomless"
                                                pause 0.3
                                                $ Girl.Legs = "blue skirt"
                                                $ Girl.Upskirt = 0
                                            else:
                                                call AnyLine(Girl,"I'll need some privacy here. . .")
                                                show blackscreen onlayer black
                                                $ Girl.Legs = "blue skirt"
                                                "You back out of the room for a moment. . ."
                                                hide blackscreen onlayer black
                                            if "blue skirt" in Cart:
                                                pass
                                            elif "blue skirt" in Girl.Inventory:
                                                call AnyLine(Girl,"I do already have one of these though.")
                                            else:
                                                $ Cart.append("blue skirt")

                            "Leave Dressing Area.":
                                    if Cart and Second:
                                        if Second.Loc == bg_current and Second not in (LauraX,JeanX) and Second.GirlLikeCheck(Girl) >= 500:
                                            $ Second.FaceChange("smile")
                                            if Second == RogueX:
                                                    ch_r "Look'in good there. . ."
                                            elif Second == KittyX:
                                                    ch_k "Oh, that looks cute on you!"
                                            elif Second == EmmaX:
                                                    ch_e "You really do wear that well. . ."
                                            elif Second == StormX:
                                                    ch_s "That really does suit you. . ."
                                            elif Second == JubesX:
                                                    ch_v "So cute!"

                                            $ Girl.FaceChange("smile")
                                            if Girl == RogueX:
                                                    ch_r "Aw, thanks. . ."
                                            elif Girl == KittyX:
                                                    ch_k "Right?"
                                            elif Girl == EmmaX:
                                                    ch_e "Obviously. . ."
                                            elif Girl == LauraX:
                                                    ch_l "Ok, cool. . ."
                                            elif Girl == JeanX:
                                                    ch_j "Of course it does. . ."
                                            elif Girl == StormX:
                                                    ch_s "Oh, thank you. . ."
                                            elif Girl == JubesX:
                                                    ch_v "I know, right?"
                                            $ Girl.GirlLikeUp(Second,5)
                                            $ Second.GirlLikeUp(Girl,3)


                                    $ Girl.OutfitChange(Changed=0) #puts clothes back on
                                    $ Round -= 20 if Round > 30 else (Round-10) #reduces Round to at minimum 10
                                    $ Player.DrainWord("locked",0,0,1)
                                    $ bg_current = "bg shop"
                                    $ BO = Party[:]
                                    while BO:
                                        $ BO[0].Loc = "bg shop"
                                        $ BO.remove(BO[0])

                                    call Taboo_Level
                                    call Set_The_Scene
                                    if not Cart:
                                            "That was fun, but since there wasn't anything she was interested in, she put it all back."
                                    if Player.Cash < 50:
                                        "You don't have enough cash on you, so you have to put everything back."
                                        $ Girl.FaceChange("sad")
                                        if "shopblock" not in Girl.DailyActions:
                                                $ Girl.Statup("Love", 50, -2)
                                                $ Girl.Statup("Love", 90, -2)
                                                $ Girl.Statup("Obed", 50, 3)
                                                $ Girl.Statup("Obed", 80, 3)
                                                $ Girl.AddWord(1,"shopblock","shopblock") #recent and daily
                                        if Girl in (EmmaX,StormX):
                                                call AnyLine(Girl,"How disappointing.")
                                        elif Girl in (JeanX,LauraX):
                                                pass
                                        else:
                                                call AnyLine(Girl,"Aw. . .")
                                        $ Cart = []

                                    while Cart:
                                        menu:
                                            "So what did you want to buy?"
                                            "The top" if "bikini top" in Cart:
                                                    "You agree to buy [Girl.Name] the bikini top."
                                                    if Girl.Tag + " bikini top" in Player.Inventory:
                                                            "Wait, you already have one of those."
                                                            "You pull out the one in your bag."
                                                            $ Player.Inventory.remove(Girl.Tag + " bikini top")
                                                    elif Girl in (KittyX,EmmaX,StormX):
                                                        if Player.Cash < 60:
                                                            "You look at the tag, and actually, it's $60, you can't afford it."
                                                            $ Cart.remove("bikini top")
                                                        else:
                                                            $ Player.Cash -= 60
                                                    elif Player.Cash < 50:
                                                            "You look at the tag, and actually, it's $50, you can't afford it."
                                                            $ Cart.remove("bikini top")
                                                    else:
                                                            $ Player.Cash -= 50
                                                    if "bikini top" in Cart:
                                                            #if you successsfully got it for her. . .
                                                            $ Cart.remove("bikini top")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("bikini top")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 20)
                                                            $ Girl.Statup("Obed", 200, 10)
                                                            $ Girl.Statup("Inbt", 200, 5)
                                                            if Girl == RogueX:
                                                                    ch_r "A little skimpy. . ."
                                                            elif Girl == KittyX:
                                                                    ch_k "Aw, a cute Kitty. . . hole. . ."
                                                            elif Girl == EmmaX:
                                                                    ch_e "This does show off my assets, doesn't it. . ."
                                                            elif Girl == LauraX:
                                                                    ch_l "\"X\", cute. . ."
                                                            elif Girl == JeanX:
                                                                    ch_j "Yeah, this'll work. . ."
                                                            elif Girl == StormX:
                                                                    ch_s "I think I can recognize the design. . ."
                                                            elif Girl == JubesX:
                                                                    ch_v "Ooo, so Cal. . ."
                                            #end buy bikini top

                                            "The bottoms" if "bikini bottoms" in Cart:
                                                    "You agree to buy [Girl.Name] the bikini bottoms."
                                                    if Girl.Tag + " bikini bottoms" in Player.Inventory:
                                                            "Wait, you already have those."
                                                            "You pull out the pair in your bag."
                                                            $ Player.Inventory.remove(Girl.Tag + " bikini bottoms")
                                                    elif Girl in (KittyX,EmmaX,StormX):
                                                        if Player.Cash < 60:
                                                            "You look at the tag, and actually, it's $60, you can't afford it."
                                                            $ Cart.remove("bikini bottoms")
                                                        else:
                                                            $ Player.Cash -= 60
                                                    elif Player.Cash < 50:
                                                            "You look at the tag, and actually, it's $50, you can't afford it."
                                                            $ Cart.remove("bikini bottoms")
                                                    else:
                                                            $ Player.Cash -= 50
                                                    if "bikini bottoms" in Cart:
                                                            #if you successsfully got it for her. . .
                                                            $ Cart.remove("bikini bottoms")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("bikini bottoms")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 20)
                                                            $ Girl.Statup("Obed", 200, 10)
                                                            $ Girl.Statup("Inbt", 200, 5)
                                                            if Girl == RogueX:
                                                                    ch_r "I was thinking about a tan. . ."
                                                            elif Girl == KittyX:
                                                                    ch_k "A little snug, maybe. . ."
                                                            elif Girl == EmmaX:
                                                                    ch_e "I don't know that a student should be buying me swimwear. . ."
                                                            elif Girl == LauraX:
                                                                    ch_l "Ok, cool. . ."
                                                            elif Girl == JeanX:
                                                                    ch_j "Ooo, these are nice. . ."
                                                            elif Girl == StormX:
                                                                    ch_s "Where have I seen this cut before. . ."
                                                            elif Girl == JubesX:
                                                                    ch_v "Maybe a little small. . ."
                                            #end buy bikini bottoms

                                            "The skirt" if "blue skirt" in Cart:
                                                    "You agree to buy [Girl.Name] the blue skirt."
                                                    if Girl.Tag + " blue skirt" in Player.Inventory:
                                                            "Wait, you already have one of those."
                                                            "You pull out the one in your bag."
                                                            $ Player.Inventory.remove(Girl.Tag + " blue skirt")
                                                    if Player.Cash < 50:
                                                            "You look at the tag, and actually, it's $50, you can't afford it."
                                                            $ Cart.remove("blue skirt")
                                                    else:
                                                            $ Player.Cash -= 50
                                                    if "blue skirt" in Cart:
                                                            #if you successsfully got it for her. . .
                                                            $ Cart.remove("blue skirt")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("blue skirt")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 20)
                                                            $ Girl.Statup("Obed", 200, 10)
                                                            $ Girl.Statup("Inbt", 200, 5)
                                                            ch_k "This is a cute skirt. . ."
                                            #end buy blue skirt

                                            "Nothing" if "purchased" not in Player.RecentActions:
                                                    $ Girl.FaceChange("sad")
                                                    if "shopblock" not in Girl.DailyActions:
                                                            $ Girl.Statup("Love", 50, -2)
                                                            $ Girl.Statup("Love", 90, -2)
                                                            $ Girl.Statup("Obed", 50, 3)
                                                            $ Girl.Statup("Obed", 80, 3)
                                                            $ Girl.AddWord(1,"shopblock","shopblock") #recent and daily
                                                    "You put all the stuff back."
                                                    if Girl in (EmmaX,StormX):
                                                            call AnyLine(Girl,"How disappointing.")
                                                    elif Girl in (JeanX,LauraX):
                                                            pass
                                                    else:
                                                            call AnyLine(Girl,"Aw. . .")
                                                    $ Cart = []
                                            "Nothing else" if "purchased" in Player.RecentActions:
                                                    $ Girl.FaceChange("sad")
                                                    if "shopblock" not in Girl.DailyActions:
                                                            $ Girl.Statup("Love", 50, -1)
                                                            $ Girl.Statup("Obed", 50, 3)
                                                            $ Girl.Statup("Obed", 90, 2)
                                                    "You put all the remaining stuff back."
                                                    $ Cart = []
                                    #End while Cart: loop


                                    $ Player.DrainWord("purchased") #removes purchased token
                                    if Girl == KittyX and ("blue skirt" in Girl.Inventory or Girl.Inbt >= 400) and "bikini top" in Girl.Inventory and "bikini bottoms" in Girl.Inventory:
                                                $ Girl.Swim[0] = 1
                                    elif "bikini top" in Girl.Inventory and "bikini bottoms" in Girl.Inventory:
                                                $ Girl.Swim[0] = 1
                                    $ Girl = 0
                    #end Dressing room loop"

                # End Swimwear while loop
        return

#End Swim Shop   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Lingerie_Shop:
        #this one will loop the "try something on menu" until you leave,
        #if you pick a girl, it sees if she's willing to try stuff on.
        #if she is, it loops the "dressing room" area until you try to leave
        #then it loops the "empty cart" menu until it's empty.

        $ bg_current = "bg shop"
        $ BO = Party[:]
        while BO:
            $ BO[0].Loc = "bg shop"
            $ BO.remove(BO[0])

        call Set_The_Scene
        $ Girl = 0
        "You head into \"Stacy's\". . ."
        while True:
                if Round <= 20:
                    "It's getting late, you head back into the mall. . ."
                    $ Girl = 0
                    return
                menu:
                    "What did you want to do?"
                    "Have [First.Name] try something on." if First:
                            $ Girl = First
                    "Have [Second.Name] try something on." if Second:
                            #swaps first and second
                            $ Girl = Second
                            $ Second = First
                            $ First = Girl
                    "Exit.":
                            "You head back into the mall. . ."
                            $ Girl = 0
                            $ bg_current = "bg mall"
                            $ BO = Party[:]
                            while BO:
                                $ BO[0].Loc = "bg mall"
                                $ BO.remove(BO[0])
                            call Set_The_Scene
                            return
                #End shop menu

                if Girl:
                        #checks if they are ok with shopping for bikinis with you, kicks out if not
                        $ Girl.FaceChange("smile",1)
                        if ApprovalCheck(Girl, 800) or ApprovalCheck(Girl, 600, "L") or ApprovalCheck(Girl, 300, "O"):
                            #if she agrees. . .
                            if Girl == RogueX:
                                    ch_r "Oh, this looks spicy. . ."
                            elif Girl == KittyX:
                                    ch_k "Um, I don't know. . ."
                            elif Girl == EmmaX:
                                    ch_e "I'm not sure where this is heading. . ."
                            elif Girl == LauraX:
                                    ch_l "Oh?"
                            elif Girl == JeanX:
                                    ch_j "Oh, what're you getting?"
                            elif Girl == StormX:
                                    ch_s "I will see where you are heading with this. . ."
                            elif Girl == JubesX:
                                    ch_v "Ok, interesting play here. . ."
                        else:
                            if Girl == RogueX:
                                    ch_r "Oh, no thank you."
                            elif Girl == KittyX:
                                    ch_k "Oh, um, I don't really need anything from here. . ."
                            elif Girl == EmmaX:
                                    ch_e "I think that's a bit inappropriate. . ."
                            elif Girl == LauraX:
                                    ch_l "Not interested. . ."
                            elif Girl == JeanX:
                                    ch_j "No, I'm good."
                            elif Girl == StormX:
                                    ch_s "I don't think that I should. . ."
                            elif Girl == JubesX:
                                    ch_v "I don't really want to shop for that. . ."
                            $ Girl = 0
                #end checks if they are ok with shopping for bikinis with you, kicks out if not

                if Girl:
                    #if she agreed to shop for a suit. . .
                    "You grab some things and head into one of the dressing rooms with [Girl.Name]."
                    $ bg_current = "bg dressing"
                    $ Girl.Loc = "bg dressing"
                    if Second:
                        #if there is a second girl
                        "Should [Second.Name] come too?"
                        menu:
                            "Sure":
                                    "[Second.Name] follows you in."
                                    $ Second.Loc = "bg dressing"
                            "Probably not.":
                                    ch_p "[Second.Name], probably hang back."
                                    call AnyLine(Second,"Fine. I'll just wait here then.")
                    if Second and Second.Loc == bg_current:
                            #if the other girl agreed to come along
                            call Set_The_Scene
                    else:
                            #if the other girl didn't agree to come along
                            show blackscreen onlayer black
                            call AllHide
                            call display_background
                            $ Girl.sprite_location = StageCenter
                            $ Girl.Layer = 100
                            call Display_Girl(Girl,0,0)

                            hide blackscreen onlayer black
                    $ Player.Traits.append("locked")
                    call Taboo_Level

                    while Girl:
                        menu:
                            "What did you want to try on here?"
                            "Lace Bra (locked)" if Girl.Chest == "lace bra":
                                            pass
                            "Lace Bra" if Girl.Chest != "lace bra" and Girl != LauraX:
                                    if "no gift bra" in Girl.RecentActions:
                                            call AnyLine(Girl,"I said no. . .")
                                    elif not Girl.SeenChest and not ApprovalCheck(Girl, 900):
                                            $ Girl.FaceChange("angry",2)
                                            if Girl in (EmmaX,StormX):
                                                    call AnyLine(Girl,"I don't think that would be appropriate.")
                                            elif Girl in (JeanX,LauraX):
                                                    call AnyLine(Girl,"No thanks. . .")
                                            else:
                                                    call AnyLine(Girl,"Um, no, definitely not. . .")
                                            $ Girl.FaceChange("angry",1)
                                            $ Girl.RecentActions.append("no gift bra")
                                    else:
                                            if Girl.SeenChest or ApprovalCheck(Girl, 1000, TabM=2):
                                                call Dressing_Strip_Bra("lace bra")
                                            else:
                                                call AnyLine(Girl,"I'll need some privacy here. . .")
                                                show blackscreen onlayer black
                                                if Girl == JubesX: #removes coat
                                                        $ Girl.Acc = 0
                                                $ Girl.Over = 0
                                                $ Girl.Chest = "lace bra"
                                                "You back out of the room for a moment. . ."
                                                hide blackscreen onlayer black
                                            if "lace bra" in Cart:
                                                pass
                                            elif "lace bra" in Girl.Inventory:
                                                call AnyLine(Girl,"I do already have one of these though.")
                                            else:
                                                $ Cart.append("lace bra")
                            #End lace bra

                            "Corset (locked)" if Girl.Chest == "corset":
                                            pass
                            "Corset" if Girl.Chest != "corset" and Girl in (LauraX,JeanX):
                                    if "no gift bra" in Girl.RecentActions:
                                            call AnyLine(Girl,"I said no. . .")
                                    elif not Girl.SeenChest and not ApprovalCheck(Girl, 900):
                                            $ Girl.FaceChange("angry",2)
                                            if Girl in (EmmaX,StormX):
                                                    call AnyLine(Girl,"I don't think that would be appropriate.")
                                            elif Girl in (JeanX,LauraX):
                                                    call AnyLine(Girl,"No thanks. . .")
                                            else:
                                                    call AnyLine(Girl,"Um, no, definitely not. . .")
                                            $ Girl.FaceChange("angry",1)
                                            $ Girl.RecentActions.append("no gift bra")
                                    else:
                                            if Girl.SeenChest or ApprovalCheck(Girl, 1000, TabM=2):
                                                call Dressing_Strip_Bra("corset")
                                            else:
                                                call AnyLine(Girl,"I'll need some privacy here. . .")
                                                show blackscreen onlayer black
                                                if Girl == JubesX: #removes coat
                                                        $ Girl.Acc = 0
                                                $ Girl.Over = 0
                                                $ Girl.Chest = "corset"
                                                "You back out of the room for a moment. . ."
                                                hide blackscreen onlayer black
                                            if "corset" in Cart:
                                                pass
                                            elif "corset" in Girl.Inventory:
                                                call AnyLine(Girl,"I do already have one of these though.")
                                            else:
                                                $ Cart.append("corset")
                            #End corset

                            "Lace Corset (locked)" if Girl.Chest == "lace corset":
                                            pass
                            "Lace Corset" if Girl.Chest != "lace corset" and Girl == LauraX:
                                    if "no gift bra" in Girl.RecentActions:
                                            call AnyLine(Girl,"I said no. . .")
                                    elif not Girl.SeenChest and not ApprovalCheck(Girl, 900):
                                            $ Girl.FaceChange("angry",2)
                                            if Girl in (EmmaX,StormX):
                                                    call AnyLine(Girl,"I don't think that would be appropriate.")
                                            elif Girl in (JeanX,LauraX):
                                                    call AnyLine(Girl,"No thanks. . .")
                                            else:
                                                    call AnyLine(Girl,"Um, no, definitely not. . .")
                                            $ Girl.FaceChange("angry",1)
                                            $ Girl.RecentActions.append("no gift bra")
                                    else:
                                            if Girl.SeenChest or ApprovalCheck(Girl, 1000, TabM=2):
                                                call Dressing_Strip_Bra("lace corset")
                                            else:
                                                call AnyLine(Girl,"I'll need some privacy here. . .")
                                                show blackscreen onlayer black
                                                if Girl == JubesX: #removes coat
                                                        $ Girl.Acc = 0
                                                $ Girl.Over = 0
                                                $ Girl.Chest = "lace corset"
                                                "You back out of the room for a moment. . ."
                                                hide blackscreen onlayer black
                                            if "lace corset" in Cart:
                                                pass
                                            elif "lace corset" in Girl.Inventory:
                                                call AnyLine(Girl,"I do already have one of these though.")
                                            else:
                                                $ Cart.append("lace corset")
                            #End lace corset
                            "Lace Panties (locked)" if Girl.Panties == "lace panties":
                                            pass
                            "Lace Panties" if Girl.Panties != "lace panties":
                                    if "no gift panties" in Girl.RecentActions:
                                            call AnyLine(Girl,"I said no. . .")
                                    elif not Girl.SeenPussy and not ApprovalCheck(Girl, 1000):
                                            $ Girl.FaceChange("angry",2)
                                            if Girl in (EmmaX,StormX):
                                                    call AnyLine(Girl,"I don't think that would be appropriate.")
                                            elif Girl in (JeanX,LauraX):
                                                    call AnyLine(Girl,"No thanks. . .")
                                            else:
                                                    call AnyLine(Girl,"Um, no, definitely not. . .")
                                            $ Girl.FaceChange("angry",1)
                                            $ Girl.RecentActions.append("no gift panties")
                                    else:
                                            if Girl.SeenPussy or ApprovalCheck(Girl, 1200, TabM=2):
                                                call Dressing_Strip_Panties("lace panties")
                                            else:
                                                call AnyLine(Girl,"I'll need some privacy here. . .")
                                                show blackscreen onlayer black
                                                $ Girl.Legs = 0
                                                $ Girl.Hose = 0
                                                $ Girl.Panties = "lace panties"
                                                "You back out of the room for a moment. . ."
                                                hide blackscreen onlayer black
                                            if "lace panties" in Cart:
                                                pass
                                            elif "lace panties" in Girl.Inventory:
                                                call AnyLine(Girl,"I do already have these though.")
                                            else:
                                                $ Cart.append("lace panties")
                            #End lace panties

                            "Tiger-Striped Panties (locked)" if Girl.Panties == "tiger panties":
                                            pass
                            "Tiger-Striped Panties" if Girl.Panties != "tiger panties" and Girl == JubesX:
                                    if "no gift panties" in Girl.RecentActions:
                                            call AnyLine(Girl,"I said no. . .")
                                    elif not Girl.SeenPussy and not ApprovalCheck(Girl, 1000):
                                            $ Girl.FaceChange("angry",2)
                                            call AnyLine(Girl,"Um, no, not really interested. . .")
                                            $ Girl.FaceChange("angry",1)
                                            $ Girl.RecentActions.append("no gift panties")
                                    else:
                                            if Girl.SeenPussy or ApprovalCheck(Girl, 1200, TabM=2):
                                                call Dressing_Strip_Panties("tiger panties")
                                            else:
                                                call AnyLine(Girl,"I'll need some privacy here. . .")
                                                show blackscreen onlayer black
                                                $ Girl.Legs = 0
                                                $ Girl.Hose = 0
                                                $ Girl.Panties = "tiger panties"
                                                "You back out of the room for a moment. . ."
                                                hide blackscreen onlayer black
                                            if "tiger panties" in Cart:
                                                pass
                                            elif "tiger panties" in Girl.Inventory:
                                                call AnyLine(Girl,"I do already have these though.")
                                            else:
                                                $ Cart.append("tiger panties")
                            #End tiger panties

                            "Stockings and Garterbelt (locked)" if Girl.Hose == "stockings and garterbelt":
                                            pass
                            "Stockings and Garterbelt" if Girl.Hose != "stockings and garterbelt":
                                            if Girl.SeenPussy or ApprovalCheck(Girl, 900, TabM=2):
                                                $ Girl.FaceChange("sexy")
                                                call AnyLine(Girl,"Sure. . .")
                                                $ Girl.Upskirt = 1
                                                pause 0.3
                                                $ Girl.Legs = 0
                                                pause 0.3
                                                $ Girl.Hose = 0
                                                call expression Girl.Tag + "_First_Bottomless"
                                                pause 0.3
                                                $ Girl.Hose = "stockings and garterbelt"
                                                $ Girl.PantiesDown = 0
                                                $ Girl.Upskirt = 0
                                                if Second and "stockings and garterbelt" not in Cart:
                                                    $ Girl.GirlLikeUp(Second,1)
                                                    $ Second.GirlLikeUp(Girl,2)
                                            else:
                                                call AnyLine(Girl,"I'll need some privacy here. . .")
                                                show blackscreen onlayer black
                                                $ Girl.Hose = "stockings and garterbelt"
                                                "You back out of the room for a moment. . ."
                                                hide blackscreen onlayer black
                                            if "stockings and garterbelt" in Cart:
                                                pass
                                            elif "stockings and garterbelt" in Girl.Inventory:
                                                call AnyLine(Girl,"I do already have these though.")
                                            else:
                                                $ Cart.append("stockings and garterbelt")
                            #End Stockings and Garterbelt

                            "Knee Stockings (locked)" if Girl.Hose == "knee stockings":
                                            pass
                            "Knee Stockings" if Girl.Hose != "knee stockings" and Girl == KittyX:
                                            $ Girl.FaceChange("sexy")
                                            call AnyLine(Girl,"Sure. . .")
                                            $ Girl.Hose = 0
                                            pause 0.3
                                            $ Girl.Hose = "knee stockings"
                                            if "knee stockings" in Cart:
                                                pass
                                            elif "knee stockings" in Girl.Inventory:
                                                call AnyLine(Girl,"I do already have these though.")
                                            else:
                                                $ Cart.append("knee stockings")
                            #End Knee Stockings

                            "High Socks (locked)" if Girl.Hose == "socks":
                                            pass
                            "High Socks" if Girl.Hose != "socks" and Girl == JubesX:
                                            $ Girl.FaceChange("sexy")
                                            call AnyLine(Girl,"Sure. . .")
                                            $ Girl.Hose = 0
                                            pause 0.3
                                            $ Girl.Hose = "socks"
                                            if "socks" in Cart:
                                                pass
                                            elif "socks" in Girl.Inventory:
                                                call AnyLine(Girl,"I do already have these though.")
                                            else:
                                                $ Cart.append("socks")
                            #End Knee Stockings

                            "Pantyhose (locked)" if Girl.Hose == "pantyhose":
                                            pass
                            "Pantyhose" if Girl.Hose != "pantyhose" and Girl != LauraX:
                                            if Girl.SeenPussy or ApprovalCheck(Girl, 900, TabM=2):
                                                $ Girl.FaceChange("sexy")
                                                call AnyLine(Girl,"Sure. . .")
                                                $ Girl.Upskirt = 1
                                                pause 0.3
                                                $ Girl.Legs = 0
                                                pause 0.3
                                                $ Girl.Hose = 0
                                                call expression Girl.Tag + "_First_Bottomless"
                                                pause 0.3
                                                $ Girl.Hose = "pantyhose"
                                                $ Girl.PantiesDown = 0
                                                $ Girl.Upskirt = 0
                                                if Second and "pantyhose" not in Cart:
                                                    $ Girl.GirlLikeUp(Second,1)
                                                    $ Second.GirlLikeUp(Girl,2)
                                            else:
                                                call AnyLine(Girl,"I'll need some privacy here. . .")
                                                show blackscreen onlayer black
                                                $ Girl.Hose = "pantyhose"
                                                "You back out of the room for a moment. . ."
                                                hide blackscreen onlayer black
                                            if "pantyhose" in Cart:
                                                pass
                                            elif "pantyhose" in Girl.Inventory:
                                                call AnyLine(Girl,"I do already have these though.")
                                            else:
                                                $ Cart.append("pantyhose")
                            #End Pantyhose

                            "Lose the [Girl.Hose]" if Girl.Hose:
                                            if Girl.HoseNum() < 10 or ApprovalCheck(Girl, 900, TabM=2):
                                                if Girl in (EmmaX,StormX):
                                                        call AnyLine(Girl,"I suppose. . .")
                                                else:
                                                        call AnyLine(Girl,"Ok. . .")
                                                $ Girl.Hose = 0
                                                call expression Girl.Tag + "_First_Bottomless"
                                            else:
                                                if Girl in (EmmaX,StormX):
                                                        call AnyLine(Girl,"I do not think so. . .")
                                                else:
                                                        call AnyLine(Girl,"No thanks. . .")

                            "Nighty (locked)" if Girl.Over == "nighty":
                                            pass
                            "Nighty" if Girl.Over != "nighty" and Girl == RogueX:
                                    if "no gift bra" in Girl.RecentActions:
                                            call AnyLine(Girl,"I said no. . .")
                                    elif not Girl.SeenChest and not ApprovalCheck(Girl, 900):
                                            $ Girl.FaceChange("angry",2)
                                            if Girl in (EmmaX,StormX):
                                                    call AnyLine(Girl,"I don't think that would be appropriate.")
                                            elif Girl in (JeanX,LauraX):
                                                    call AnyLine(Girl,"No thanks. . .")
                                            else:
                                                    call AnyLine(Girl,"Um, no, definitely not. . .")
                                            $ Girl.FaceChange("angry",1)
                                            $ Girl.RecentActions.append("no gift bra")
                                    else:
                                            if Girl.SeenChest or ApprovalCheck(Girl, 900, TabM=2):
                                                $ Girl.FaceChange("sexy")
                                                call AnyLine(Girl,"Sure. . .")
                                                if Girl == JubesX: #removes coat
                                                        $ Girl.Acc = 0
                                                        pause 0.3
                                                $ Girl.Over = 0
                                                call first_topless(Girl)
                                                call expression Girl.Tag + "_First_Bottomless" pass (1)
                                                pause 0.3
                                                $ Girl.Over = "nighty"
                                                pause 0.3
                                                $ Girl.Uptop = 0
                                                if Second and "nighty" not in Cart:
                                                    $ Girl.GirlLikeUp(Second,1)
                                                    $ Second.GirlLikeUp(Girl,3)
                                            else:
                                                call AnyLine(Girl,"I'll need some privacy here. . .")
                                                show blackscreen onlayer black
                                                if Girl == JubesX: #removes coat
                                                        $ Girl.Acc = 0
                                                $ Girl.Over = "nighty"
                                                "You back out of the room for a moment. . ."
                                                hide blackscreen onlayer black
                                            if "nighty" in Cart:
                                                pass
                                            elif "nighty" in Girl.Inventory:
                                                call AnyLine(Girl,"I do already have one of these though.")
                                            else:
                                                $ Cart.append("nighty")
                            #End nighty

                            "Leave Dressing Area.":
                                    if Cart and Second:
                                        if Second.Loc == bg_current and Second not in (LauraX,JeanX) and Second.GirlLikeCheck(Girl) >= 500:
                                            $ Second.FaceChange("sexy")
                                            if Second == RogueX:
                                                    ch_r "Look'in good there. . ."
                                            elif Second == KittyX:
                                                    ch_k "Oh, that looks cute on you!"
                                            elif Second == EmmaX:
                                                    ch_e "You really do wear that well. . ."
                                            elif Second == StormX:
                                                    ch_s "That really does suit you. . ."
                                            elif Second == JubesX:
                                                    ch_v "So cute!"

                                            $ Girl.FaceChange("sexy")
                                            if Girl == RogueX:
                                                    ch_r "Aw, thanks. . ."
                                            elif Girl == KittyX:
                                                    ch_k "Right?"
                                            elif Girl == EmmaX:
                                                    ch_e "Obviously. . ."
                                            elif Girl == LauraX:
                                                    ch_l "Ok, cool. . ."
                                            elif Girl == JeanX:
                                                    ch_j "Of course it does. . ."
                                            elif Girl == StormX:
                                                    ch_s "Oh, thank you. . ."
                                            elif Girl == JubesX:
                                                    ch_v "I know, right?"
                                            $ Girl.GirlLikeUp(Second,5)
                                            $ Second.GirlLikeUp(Girl,3)

                                    $ Round -= 20 if Round > 30 else (Round-10) #reduces Round to at minimum 10
                                    $ Player.DrainWord("locked",0,0,1)
                                    $ bg_current = "bg shop"
                                    $ BO = Party[:]
                                    while BO:
                                        $ BO[0].Loc = "bg shop"
                                        $ BO.remove(BO[0])

                                    call Taboo_Level
                                    call Set_The_Scene

                                    $ Girl.OutfitChange(Changed=0) #puts clothes back on
                                    if not Cart:
                                            "That was fun, but since there wasn't anything she was interested in, she put it all back."
                                    if Player.Cash < 50:
                                        "You don't have enough cash on you, so you have to put everything back."
                                        $ Girl.FaceChange("sad")
                                        if "shopblock" not in Girl.DailyActions:
                                                $ Girl.Statup("Love", 50, -2)
                                                $ Girl.Statup("Love", 90, -2)
                                                $ Girl.Statup("Obed", 50, 3)
                                                $ Girl.Statup("Obed", 80, 3)
                                                $ Girl.AddWord(1,"shopblock","shopblock") #recent and daily
                                        if Girl in (EmmaX,StormX):
                                                call AnyLine(Girl,"How disappointing.")
                                        elif Girl in (JeanX,LauraX):
                                                pass
                                        else:
                                                call AnyLine(Girl,"Aw. . .")
                                        $ Cart = []

                                    while Cart:
                                        menu:
                                            "So what did you want to buy?"
                                            "The lace bra" if "lace bra" in Cart:
                                                    "You agree to buy [Girl.Name] the lace bra."
                                                    if Girl.Tag + " lace bra" in Player.Inventory:
                                                            "Wait, you already have one of those."
                                                            "You pull out the one in your bag."
                                                            $ Player.Inventory.remove(Girl.Tag + " lace bra")
                                                    elif Player.Cash < 90:
                                                            "You look at the tag, and actually, it's $90, you can't afford it."
                                                            $ Cart.remove("lace bra")
                                                    else:
                                                            $ Player.Cash -= 90
                                                    if "lace bra" in Cart:
                                                            #if you successsfully got it for her. . .
                                                            $ Cart.remove("lace bra")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("lace bra")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 25)
                                                            $ Girl.Statup("Obed", 200, 20)
                                                            $ Girl.Statup("Inbt", 200, 20)
                                                            if Girl == RogueX:
                                                                    ch_r "I don't know that I'd wear this out, but maybe in private."
                                                            elif Girl == KittyX:
                                                                ch_k "At least you appreciate what I've got."
                                                            elif Girl == EmmaX:
                                                                    ch_e "I'm not exactly running low on this sort of thing. . ."
                                                            elif Girl == StormX:
                                                                    ch_s "It is not that I do not appreciate it, but. . ."
                                                            elif Girl == JeanX:
                                                                    ch_j "Good tastes. . ."
                                                            elif Girl == JubesX:
                                                                    ch_v "It's not my usual style. . ."
                                            #end lace bra

                                            "The corset" if "corset" in Cart:
                                                    "You agree to buy [Girl.Name] the corset."
                                                    if Girl.Tag + " corset" in Player.Inventory:
                                                            "Wait, you already have one of those."
                                                            "You pull out the one in your bag."
                                                            $ Player.Inventory.remove(Girl.Tag + " corset")
                                                    elif Player.Cash < 70:
                                                            "You look at the tag, and actually, it's $70, you can't afford it."
                                                            $ Player.Inventory.remove(Girl.Tag + " corset")
                                                    else:
                                                            $ Player.Cash -= 70
                                                    if "corset" in Cart:
                                                            #if you successsfully got it for her. . .
                                                            $ Cart.remove("corset")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("corset")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 15)
                                                            $ Girl.Statup("Obed", 200, 20)
                                                            $ Girl.Statup("Inbt", 200, 10)
                                                            if Girl == LauraX:
                                                                    ch_l "This is. . . kinda cool. . ."
                                                            elif Girl == JeanX:
                                                                    ch_j "Thanks?"
                                            #end lace corset

                                            "The lace corset" if "lace corset" in Cart:
                                                    "You agree to buy [Girl.Name] the lace corset."
                                                    if Girl.Tag + " lace corset" in Player.Inventory:
                                                            "Wait, you already have one of those."
                                                            "You pull out the one in your bag."
                                                            $ Player.Inventory.remove(Girl.Tag + " lace corset")
                                                    elif Player.Cash < 90:
                                                            "You look at the tag, and actually, it's $90, you can't afford it."
                                                            $ Cart.remove("lace corset")
                                                    else:
                                                            $ Player.Cash -= 90
                                                    if "lace corset" in Cart:
                                                            #if you successsfully got it for her. . .
                                                            $ Cart.remove("lace corset")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("lace corset")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 25)
                                                            $ Girl.Statup("Obed", 200, 30)
                                                            $ Girl.Statup("Inbt", 200, 20)
                                                            ch_l "You think this'd look good on me?"
                                            #end lace corset

                                            "The lace panties" if "lace panties" in Cart:
                                                    "You agree to buy [Girl.Name] the lace panties."
                                                    if Girl.Tag + " lace panties" in Player.Inventory:
                                                            "Wait, you already have one of those."
                                                            "You pull out the ones in your bag."
                                                            $ Player.Inventory.remove(Girl.Tag + " lace panties")
                                                    elif Player.Cash < 110:
                                                            "You look at the tag, and actually, they're $110, you can't afford them."
                                                            $ Cart.remove("lace panties")
                                                    else:
                                                            $ Player.Cash -= 110
                                                    if "lace panties" in Cart:
                                                            #if you successsfully got it for her. . .
                                                            $ Cart.remove("lace panties")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("lace panties")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 25)
                                                            $ Girl.Statup("Obed", 200, 20)
                                                            $ Girl.Statup("Inbt", 200, 20)
                                                            if Girl == RogueX:
                                                                    ch_r "These are a bit flimsy. . ."
                                                            elif Girl == KittyX:
                                                                    ch_k "These don't leave much to the imagination. . ."
                                                            elif Girl == EmmaX:
                                                                    ch_e "This is an. . . unsual gift."
                                                                    $ EmmaX.FaceChange("sly",1)
                                                                    ch_e "But I'll hold on to them. . ."
                                                            elif Girl == LauraX:
                                                                    ch_l "These are pretty hot. . ."
                                                            elif Girl == JeanX:
                                                                    ch_j "Oh, these are nice. . ."
                                                            elif Girl == StormX:
                                                                    ch_s "I suppose I could always use another pair. . ."
                                                            elif Girl == JubesX:
                                                                    ch_v "A little. . . intimate. . ."
                                            #end lace panties

                                            "The tiger-striped panties" if "tiger panties" in Cart:
                                                    "You agree to buy [Girl.Name] the tiger panties."
                                                    if Girl.Tag + " tiger panties" in Player.Inventory:
                                                            "Wait, you already have one of those."
                                                            "You pull out the ones in your bag."
                                                            $ Player.Inventory.remove(Girl.Tag + " tiger panties")
                                                    elif Player.Cash < 100:
                                                            "You look at the tag, and actually, they're $100, you can't afford them."
                                                            $ Cart.remove("tiger panties")
                                                    else:
                                                            $ Player.Cash -= 100
                                                    if "tiger panties" in Cart:
                                                            #if you successsfully got it for her. . .
                                                            $ Cart.remove("tiger panties")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("tiger panties")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 25)
                                                            $ Girl.Statup("Obed", 200, 20)
                                                            $ Girl.Statup("Inbt", 200, 20)
                                                            ch_v "These are stink'in cute. . ."
                                            #end tiger panties


                                            "The stockings and garterbelt" if "stockings and garterbelt" in Cart:
                                                    "You agree to buy [Girl.Name] the stockings and garterbelt."
                                                    if Girl.Tag + " stockings and garterbelt" in Player.Inventory:
                                                            "Wait, you already have those."
                                                            "You pull out the ones in your bag."
                                                            $ Player.Inventory.remove(Girl.Tag + " stockings and garterbelt")
                                                    elif Player.Cash < 100:
                                                            "You look at the tag, and actually, they're $100, you can't afford them."
                                                            $ Cart.remove("stockings and garterbelt")
                                                    else:
                                                            $ Player.Cash -= 100
                                                    if "stockings and garterbelt" in Cart:
                                                            #if you successsfully got it for her. . .
                                                            $ Cart.remove("stockings and garterbelt")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("stockings and garterbelt")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 5)
                                                            $ Girl.Statup("Obed", 200, 5)
                                                            $ Girl.Statup("Inbt", 200, 5)
                                                            if Girl == EmmaX:
                                                                    ch_e "These are lovely. . ."
                                                            elif Girl == StormX:
                                                                    ch_s "You think I could pull these off?"
                                                            else:
                                                                    call AnyLine(Girl,"These are pretty nice. . .")
                                            #end buy S&G

                                            "The knee stockings" if "knee stockings" in Cart:
                                                    "You agree to buy [Girl.Name] the knee stockings."
                                                    if Girl.Tag + " knee stockings" in Player.Inventory:
                                                            "Wait, you already have some of those."
                                                            "You pull out the ones in your bag."
                                                            $ Player.Inventory.remove(Girl.Tag + " knee stockings")
                                                    elif Player.Cash < 50:
                                                            "You look at the tag, and actually, they're $50, you can't afford them."
                                                            $ Cart.remove("knee stockings")
                                                    else:
                                                            $ Player.Cash -= 50
                                                    if "knee stockings" in Cart:
                                                            #if you successsfully got it for her. . .
                                                            $ Cart.remove("knee stockings")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("knee stockings")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 5)
                                                            $ Girl.Statup("Obed", 200, 5)
                                                            $ Girl.Statup("Inbt", 200, 5)
                                                            call AnyLine(Girl,"These are pretty nice. . .")
                                            #end buy knee stockings

                                            "The high socks" if "socks" in Cart:
                                                    "You agree to buy [Girl.Name] the socks."
                                                    if Girl.Tag + " socks" in Player.Inventory:
                                                            "Wait, you already have one of those."
                                                            "You pull out the ones in your bag."
                                                            $ Player.Inventory.remove(Girl.Tag + " socks")
                                                    elif Player.Cash < 50:
                                                            "You look at the tag, and actually, they're $50, you can't afford them."
                                                            $ Cart.remove("socks")
                                                    else:
                                                            $ Player.Cash -= 50
                                                    if "socks" in Cart:
                                                            #if you successsfully got it for her. . .
                                                            $ Cart.remove("socks")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("socks")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 5)
                                                            $ Girl.Statup("Obed", 200, 5)
                                                            $ Girl.Statup("Inbt", 200, 5)
                                                            call AnyLine(Girl,"These are pretty nice. . .")
                                            #end buy socks

                                            "The pantyhose" if "pantyhose" in Cart:
                                                    "You agree to buy [Girl.Name] the pantyhose."
                                                    if Girl.Tag + " pantyhose" in Player.Inventory:
                                                            "Wait, you already have one of those."
                                                            "You pull out the ones in your bag."
                                                            $ Player.Inventory.remove(Girl.Tag + " pantyhose")
                                                    elif Player.Cash < 50:
                                                            "You look at the tag, and actually, they're $50, you can't afford them."
                                                            $ Cart.remove("pantyhose")
                                                    else:
                                                            $ Player.Cash -= 50
                                                    if "pantyhose" in Cart:
                                                            #if you successsfully got it for her. . .
                                                            $ Cart.remove("pantyhose")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("pantyhose")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 5)
                                                            $ Girl.Statup("Obed", 200, 5)
                                                            $ Girl.Statup("Inbt", 200, 5)
                                                            call AnyLine(Girl,"These are lovely. . .")
                                            #end buy pantyhose

                                            "The nighty" if "nighty" in Cart:
                                                    "You agree to buy [Girl.Name] the nighty."
                                                    if Girl.Tag + " nighty" in Player.Inventory:
                                                            "Wait, you already have one of those."
                                                            "You pull out the one in your bag."
                                                            $ Player.Inventory.remove(Girl.Tag + " nighty")
                                                    elif Player.Cash < 75:
                                                        "You look at the tag, and actually, it's $75, you can't afford it."
                                                        $ Cart.remove("nighty")
                                                    else:
                                                        $ Player.Cash -= 75
                                                    if "nighty" in Cart:
                                                            #if you successsfully got it for her. . .
                                                            $ Cart.remove("nighty")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("nighty")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 40)
                                                            $ Girl.Statup("Obed", 200, 20)
                                                            $ Girl.Statup("Inbt", 200, 30)
                                                            ch_r "Well, it's a little revealing, but still pretty cute."
                                                            $ Girl.Statup("Lust", 89, 10)
                                            #end buy nighty

                                            "Nothing" if "purchased" not in Player.RecentActions:
                                                    $ Girl.FaceChange("sad")
                                                    if "shopblock" not in Girl.DailyActions:
                                                            $ Girl.Statup("Love", 50, -2)
                                                            $ Girl.Statup("Love", 90, -2)
                                                            $ Girl.Statup("Obed", 50, 3)
                                                            $ Girl.Statup("Obed", 80, 3)
                                                            $ Girl.AddWord(1,"shopblock","shopblock") #recent and daily
                                                    "You put all the stuff back."
                                                    if Girl in (EmmaX,StormX):
                                                            call AnyLine(Girl,"How disappointing.")
                                                    elif Girl in (JeanX,LauraX):
                                                            pass
                                                    else:
                                                            call AnyLine(Girl,"Aw. . .")
                                                    $ Cart = []
                                            "Nothing else" if "purchased" in Player.RecentActions:
                                                    $ Girl.FaceChange("sad")
                                                    if "shopblock" not in Girl.DailyActions:
                                                            $ Girl.Statup("Love", 50, -1)
                                                            $ Girl.Statup("Obed", 50, 3)
                                                            $ Girl.Statup("Obed", 90, 2)
                                                    "You put all the remaining stuff back."
                                                    $ Cart = []
                                    #End while Cart: loop


                                    $ Player.DrainWord("purchased") #removes purchased token
                                    $ Girl = 0
                    #end Dressing room loop"
                # End Lingerie while loop
        return
#End Lingerie shop   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Dressing_Strip_Bra(Item=0):
        #called if girl decides to strip panties in shops
        # call Dressing_Strip_Bra("lace bra")
        if not Item:
                return
        $ Girl.FaceChange("sexy")
        call AnyLine(Girl,"Sure. . .")
        if Girl.Over or Girl.Chest:
                $ Girl.Uptop = 1
                pause 0.3
        if Girl == JubesX and Girl.Acc: #removes coat
                $ Girl.Acc = 0
                pause 0.3
        if Girl.Over:
                $ Girl.Over = 0
                pause 0.3
        if Girl.Chest:
                $ Girl.Chest = 0
        call first_topless(Girl)
        pause 0.3
        $ Girl.Chest = Item
        pause 0.3
        $ Girl.Uptop = 0
        if Second and Item not in Cart:
                $ Girl.GirlLikeUp(Second,2)
                $ Second.GirlLikeUp(Girl,5)
        call AnyLine(Girl,". . .")
        return

label Dressing_Strip_Panties(Item=0):
        #called if girl decides to strip panties in shops
        # call Dressing_Strip_Panties("lace panties")
        if not Item:
                return
        $ Girl.FaceChange("sexy")
        call AnyLine(Girl,"Sure. . .")
        if Girl.Legs:
                $ Girl.Upskirt = 1
                pause 0.3
                $ Girl.Legs = 0
                pause 0.3
        if Girl.Hose:
                $ Girl.Hose = 0
                pause 0.3
        if Girl.Panties:
                $ Girl.PantiesDown = 1
                pause 0.2
                $ Girl.Panties = 0
        call expression Girl.Tag + "_First_Bottomless"
        pause 0.3
        $ Girl.Panties = Item
        $ Girl.PantiesDown = 0
        $ Girl.Upskirt = 0
        if Second and Item not in Cart:
            $ Girl.GirlLikeUp(Second,3)
            $ Second.GirlLikeUp(Girl,5)
        call AnyLine(Girl,". . .")
        return


#End Date_Shopping   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
