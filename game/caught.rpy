

#start girls caught lesing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girls_Caught_Lesing(Girl=0,Girl2=0,BO=[]): #rkeljsv
        #called by room entry dialog if the girls were lesing

        $ BO = ActiveGirls[:]
        if Girl in TotalGirls:
                $ BO.remove(Girl)
        while BO and not Girl:
                if BO[0] not in Party and BO[0].Loc == bg_current and "les" in BO[0].RecentActions:
                        # if this girl is not already the focal girl, is at the current location but not in a party,
                        # and was queued for a les action, set her up as girl 1.
                        $ Girl = BO[0]
                        $ BO = [1]
                $ BO.remove(BO[0])
        if Girl and not Girl2:
                #if a Girl was either offered or produced by first loop. . .
                $ BO = ActiveGirls[:]
                $ BO.remove(Girl)
                while BO:
                        if BO[0] not in Party and BO[0].Loc == bg_current and "les" in BO[0].RecentActions:
                                # if this girl is not already the focal girl, is at the current location but not in a party,
                                # and was queued for a les action, set her up as girl 2.
                                $ Girl2 = BO[0]
                                $ BO = [1]
                        $ BO.remove(BO[0])

        if not Girl or not Girl2:
                return 1

        $ Girl.DrainWord("les",1,0) #removes general "les" tag from recent actions
        $ Girl2.DrainWord("les",1,0) #removes general "les" tag from recent actions

        $ Girl.AddWord(0,"lesbian","lesbian")  #adds "lesbian" tag to recent and daily actions
        $ Girl2.AddWord(0,"lesbian","lesbian")  #adds "lesbian" tag to recent and daily actions
        $ Girl.AddWord(1,0,0,0,"les "+Girl2.Tag)  #adds "les Rogue" tag to recent actions
        $ Girl2.AddWord(1,0,0,0,"les "+Girl.Tag)  #adds "les Kitty" tag to recent actions

        "As you approach her room, you hear soft moans from inside, and notice that the door is slightly ajar."
        $ Line = 0
        while not Line:
            menu:
                extend ""
                "Knock politely":
                        "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                        "After several seconds and some more shuffling of clothing, [Girl.Name] comes to the door."
                        $ Girl.FaceChange("confused",2,Eyes = "surprised",Mouth = "smile")
                        $ Girl2.FaceChange("confused",2,Eyes = "surprised",Mouth = "smile")
                        $ Trigger = 0
                        $ Trigger3 = 0
                        $ Trigger4 = 0
                        $ Trigger5 = 0
                        call Set_The_Scene
                        if Girl == RogueX:
                                ch_r "Sorry about that [Girl.Petname], we were, um. . . working out."
                        elif Girl == KittyX:
                                ch_k "Oh, hey, [Girl.Petname], hi, we were. . . never mind."
                        elif Girl == EmmaX:
                                ch_e "Well, I hope you have a good reason for interrupting us."
                                ch_e "I was. . . teaching her a few things. . ."
                        elif Girl == LauraX:
                                ch_l "Um, hey [Girl.Petname], we were a bit busy."
                        elif Girl == JeanX:
                                ch_j "Hey [Girl.Petname], we were just giving [Girl2.Name]'s tongue a workout."
                        elif Girl == StormX:
                                ch_s "Ah, hello, [Girl.Petname] . . I was having a. . . chat with [Girl2.Name]. . ."
                        elif Girl == JubesX:
                                ch_v "Oh, hey. . . me and [Girl2.Name] were just. . . having some fun."
                        $ Girl.FaceChange("smile",1)
                        $ Girl2.FaceChange("smile",1)
                        $ temp_modifier += 10
                        $ Line = 1
                "Peek inside":
                        call Set_The_Scene
                        $ Girl.FaceChange("kiss",1,Eyes = "closed")
                        $ Girl2.FaceChange("kiss",1,Eyes = "closed")
                        $ Trigger = "lesbian"
                        $ Trigger3 = "fondle pussy"
                        $ Trigger4 = "fondle pussy"
                        "You see [Girl.Name] and [Girl2.Name], eyes closed and stroking each other vigorously."
                "Enter quietly":
                        call Set_The_Scene(Quiet=1)
                        $ Girl.FaceChange("kiss",1,Eyes = "closed")
                        $ Girl2.FaceChange("kiss",1,Eyes = "closed")
                        $ Trigger = "lesbian"
                        $ Trigger3 = "fondle pussy"
                        $ Trigger4 = "fondle pussy"
                        $ Girl.AddWord(1,"unseen","unseen")
                        $ Girl2.AddWord(1,"unseen","unseen")
                        $ Partner = Girl2
                        $ Line = 0
                        call expression Girl.Tag + "_SexAct" pass ("lesbian") #call Rogue_SexAct("lesbian")
                "Leave quietly":
                        "You leave the girls to their business and slip out."
                        $ Girl.Thirst -= 30
                        $ Girl.Lust = 20
                        $ Girl2.Thirst -= 30
                        $ Girl2.Lust = 20
                        $ renpy.pop_call()
                        jump Campus_Map
        $ Line = 0
        return

#end Girls caught lesing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start girls caught showering / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Caught_Shower(Girl=0): #rkeljsv
        if Girl not in TotalGirls:
                return
        call Shift_Focus(Girl)

        $ Options = []
        $ Girl.AddWord(1,"showered","showered",0,0)
        call Remove_Girl("All")

        $ Girl.OutfitChange("nude")
        $ Girl.FaceChange("smile",1)

        $ Girl.Loc = "bg showerroom"
        $ Girl.Water = 1
        $ Girl.Wet = 2

        if "gonnafap" in Girl.DailyActions:
                "As you approach the showers, you hear some shallow moans from inside."
        else:
                "As you approach the showers, you hear some humming noises from inside."
        menu:
                "What do you do?"
                "Enter":
                    pass
                "Knock":
                    $ Line = "knock"
                "Come back later":
                    call Remove_Girl(Girl)
                    $ Girl.OutfitChange(6) #dresses her
                    $ Girl.DrainWord("gonnafap",0,1) #removes "gonnafap" tag from daily
                    $ Girl.Lust = 25
                    $ Girl.Thirst -= int(Girl.Thirst/2) if Girl.Thirst >= 50 else int(Girl.Thirst/4)
                    $ bg_current = "bg campus"
                    jump Misplaced

        if Line == "knock":
                #You knock
                "You knock on the door. You hear some shuffling inside"
                $ Girl.Over = "towel"
                if "gonnafap" in Girl.DailyActions:
                        #Girl caught fapping
                        "You hear a sharp shuffling sound and the water gets cut off."
                        "After several seconds and some more shuffling, [Girl.Name] comes to the door."
                        $ Girl.FaceChange("perplexed",2,Mouth="normal")
                        call Set_The_Scene(Dress=0)
                        if Girl == RogueX:
                                ch_r "Sorry about that [Girl.Petname], I was. . . just wrapping up my shower."
                        elif Girl == KittyX:
                                ch_k "Oh, hey, [Girl.Petname]. I was just. . . showering. Yeah."
                        elif Girl == EmmaX:
                                ch_e "Oh, hello [Girl.Petname]. I was. . . taking care of some personal business."
                        elif Girl == LauraX:
                                ch_l "Oh, hey [Girl.Petname]. I was just. . . working off some stress."
                        elif Girl == JeanX:
                                ch_j "Oh, [Girl.Petname]. I was. . . never mind."
                        elif Girl == StormX:
                                ch_s "Ah, hello, [Girl.Petname]. . . I was. . . cleaning myself."
                        elif Girl == JubesX:
                                ch_v "Oh, hey, [Girl.Petname]. . . I was. . . what did you hear?"
                        $ Girl.Statup("Lust", 90, 5)
                        $ temp_modifier += 10
                else:
                        #Laura caught showering
                        "You hear the rustling of a towel and some knocking around, but after a few seconds [Girl.Name] comes to the door."
                        call Set_The_Scene(Dress=0)
                        if Girl == RogueX:
                                ch_r "Sorry about that [Girl.Petname], I was just wrapping up my shower."
                        elif Girl == KittyX:
                                ch_k "Oh, hey, [Girl.Petname]. I was just[KittyX.like]showering."
                        elif Girl == EmmaX:
                                ch_e "Oh, hello [Girl.Petname]. I was just finishing my shower."
                        elif Girl == LauraX:
                                ch_l "Oh, hey [Girl.Petname]. I was just finishing up."
                        elif Girl == JeanX:
                                ch_j "Oh, [Girl.Petname]. I'm about done here."
                        elif Girl == StormX:
                                ch_s "Ah, hello, [Girl.Petname] . . I am about finished here if you want some water. . ."
                        elif Girl == JubesX:
                                ch_v "Oh, hey, [Girl.Petname]. I was wrapping up here. . ."
                #end "knocked"
        else:
            #You don't knock
            if "gonnafap" in Girl.DailyActions:
                    #Caught masturbating in the shower.
                    $ Girl.DrainWord("gonnafap",0,1) #removes "gonnafap" tag from daily
                    $ Girl.FaceChange("sexy",Eyes="closed")
                    $ Girl.AddWord(1,"unseen","unseen",0,0)
                    call Set_The_Scene(Dress=0)
                    $ Count = 0
                    $ Trigger = "masturbation"
                    $ Trigger3 = "fondle pussy"
                    "You see [Girl.Name] under the shower, feeling herself up."
                    call expression Girl.Tag + "_SexAct" pass ("masturbate") #call Laura_SexAct("masturbate")
                    $ bg_current = "bg showerroom"
                    jump Misplaced

            elif D20 >= 15:
                    #She's just showering and naked
                    call Set_The_Scene(Dress=0)
                    $ Girl.FaceChange("surprised", 1)
                    "As you enter the showers, you see [Girl.Name] washing up."
                    call expression Girl.Tag + "_First_Bottomless" pass (1)
                    call first_topless(Girl, silent = 1)
                    if not ApprovalCheck(Girl, 1200) or not Girl.SeenPussy or not Girl.SeenChest:
                            $ Girl.Brows="angry"
                            $ Girl.Over = "towel"
                            "She grabs a towel and covers up."
                            $ Girl.FaceChange("angry", 1)
                            $ Girl.Statup("Love", 80, -5)
                    else:
                            if "exhibitionist" in Girl.Traits:
                                $ Girl.Statup("Lust", 90, (2*D20))
                            else:
                                $ Girl.Statup("Lust", 80, D20)
                            $ Girl.Brows="confused"

                    $ Girl.Statup("Inbt", 70, 3)
                    if Girl == RogueX:
                            ch_r "Hey! Learn to knock maybe?!"
                    elif Girl == KittyX:
                            ch_k "Did you[KittyX.like]get a good look?"
                    elif Girl == EmmaX:
                            ch_e "Hello. Haven't you learned to knock before entering?"
                    elif Girl == LauraX:
                            ch_l "Um, hey? Don't knock much?"
                    elif Girl == JeanX:
                            ch_j "Forget to knock, [JeanX.Petname]?"
                    elif Girl == StormX:
                            ch_s "Oh, hello, [Girl.Petname]."
                    elif Girl == JubesX:
                            ch_v "Hey, knock maybe?"
                    menu:
                            extend ""
                            "Sorry, I should have knocked.":
                                    $ Girl.Statup("Love", 50, 2)
                                    if Girl != StormX:
                                            $ Girl.Statup("Love", 80, 4)
                            "And miss the view?":
                                    $ Girl.Statup("Obed", 50, 2)
                                    if Girl != StormX:
                                            $ Girl.Statup("Obed", 80, 2)
                                            $ Girl.Statup("Inbt", 60, 1)
                            "Why, would it have made a difference?":
                                    if not ApprovalCheck(Girl, 500,"I"):
                                            $ Girl.Statup("Love", 50, -3)
                                            $ Girl.Statup("Obed", 50, 2)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 2)
                            "It's not as if you're leaving that much to the imagination. . ." if Girl == EmmaX:
                                    $ EmmaX.Statup("Obed", 50, 2)
                                    $ EmmaX.Statup("Obed", 80, 2)
                                    $ EmmaX.Statup("Inbt", 60, 2)
                    #end caught showering naked

            else:
                    #She's done showering and in a towel
                    $ Girl.Over = "towel"
                    call Set_The_Scene(Dress=0)
                    "As you enter the showers, you see [Girl.Name] putting on a towel."
                    if not ApprovalCheck(Girl, 1100) and (not Girl.SeenPussy or not Girl.SeenChest):
                            $ Girl.FaceChange("angry",Brows="confused")
                            $ Girl.Statup("Love", 80, -5)
                    else:
                            $ Girl.FaceChange("sexy",Brows="confused")
                    $ Girl.Statup("Inbt", 50, 3)
                    if Girl == RogueX:
                            ch_r "Well hello there, [RogueX.Petname]. Hoping to see something more?"
                    elif Girl == KittyX:
                            ch_k "Oh, hey. Were you hoping I'd be naaaaaked?"
                    elif Girl == EmmaX:
                            ch_e "Oh, hello, [EmmaX.Petname]. Sorry you didn't get here sooner?"
                    elif Girl == LauraX:
                            ch_l "Oh, hey [LauraX.Petname]. Trying to slip in unnoticed?"
                    elif Girl == JeanX:
                            ch_j "Oh, [JeanX.Petname], just sneaking in?"
                    elif Girl == StormX:
                            ch_s "Oh, hello, [Girl.Petname]."
                    elif Girl == JubesX:
                            ch_v "Well you're being sneaky. . ."
                    menu:
                            extend ""
                            "Sorry, I should have knocked.":
                                    $ Girl.Statup("Love", 50, 2)
                                    if Girl != StormX:
                                            $ Girl.Statup("Love", 80, 2)
                            "Well, to be honest. . .":
                                    $ Girl.Statup("Love", 50, -2)
                                    $ Girl.Statup("Obed", 50, 2)
                                    if Girl != StormX:
                                            $ Girl.Statup("Obed", 80, 2)
                                            $ Girl.Statup("Inbt", 60, 1)
                            "I still like the view. . ." if Girl != EmmaX:
                                if ApprovalCheck(Girl, 500,"I"):
                                    $ Girl.Statup("Love", 80, 1)
                                else:
                                    $ Girl.Statup("Love", 50, -1)
                                    $ Girl.Statup("Obed", 50, 2)
                                $ Girl.Statup("Obed", 80, 2)
                                $ Girl.Statup("Inbt", 60, 3)
                            "It's not as if you're leaving that much to the imagination. . ." if Girl == EmmaX:
                                $ EmmaX.Statup("Obed", 50, 2)
                                $ EmmaX.Statup("Obed", 80, 2)
                                $ EmmaX.Statup("Inbt", 60, 2)
                    #end caught in towel

            $ Girl.FaceChange("sexy")
            if Girl == StormX:
                            ch_s "Oh, that's fine, [Girl.Petname]."
                            ch_s "You might want to be careful with the other girls though."
            elif not ApprovalCheck(Girl, 1000) or not Girl.SeenPussy or not Girl.SeenChest:
                    if Girl == RogueX:
                            ch_r "Well, it happens, just be careful next time."
                    elif Girl == KittyX:
                            ch_k "Well, it's not like I totally mind. . ."
                    elif Girl == EmmaX:
                            ch_e "Hmm. Yes, a likely excuse."
                    elif Girl == LauraX:
                            ch_l "Well, just keep an eye on your own bits."
                            ch_l "Wouldn't want them going missing."
                    elif Girl == JeanX:
                            ch_j "Well, just. . . be more careful."
                    elif Girl == JubesX:
                            ch_v "Gimme some warning next time."
            elif not ApprovalCheck(Girl, 1300):
                    if Girl == RogueX:
                            ch_r "Well, it happens, just be careful next time."
                    elif Girl == KittyX:
                            ch_k "Well too bad."
                    elif Girl == EmmaX:
                            ch_e "Hmm. Yes, a likely excuse."
                    elif Girl == LauraX:
                            ch_l "Uh-huh."
                    elif Girl == JeanX:
                            ch_j "Sure. . ."
                    elif Girl == JubesX:
                            ch_v "Uh-huh. . ."
            else:
                    if Girl == RogueX:
                            ch_r "You could have just asked, [Girl.Petname]."
                    elif Girl == KittyX:
                            ch_k "Well, it's not like it's totally off the table. . ."
                    elif Girl == EmmaX:
                            ch_e "Well, it's not that I mind. . ."
                    elif Girl == LauraX:
                            ch_l "Nah, I don't mind much. . ."
                    elif Girl == JeanX:
                            ch_j "How could I resist an audience?"
                    elif Girl == JubesX:
                            ch_v "Gimme some warning next time."
                    elif Girl == JubesX:
                            ch_v "You just have to ask. . ."

                    if Girl.Over == "towel":
                            #if she's wearing a towel. . .
                            $ Girl.Over = 0 #removes towel
                            pause 0.5
                            $ Girl.Over = "towel"
                            "She flashes you real quick."
                            $ Girl.Over = "towel"
                            call expression Girl.Tag + "_First_Bottomless" pass (1)
                            call first_topless(Girl, silent = 1) #same as "call Rogue_First_Topless(1)"

                            if Girl == LauraX:
                                    ch_l "Heh!"

            #end didn't knock

        if Girl == RogueX:
                ch_r "Well, I should probably get going. . ."
        elif Girl == KittyX:
                ch_k "I'm done here, see you later?"
        elif Girl == EmmaX:
                ch_e "I should probably be leaving. . ."
        elif Girl == LauraX:
                ch_l "I should get going. . ."
        elif Girl == JeanX:
                ch_j "Ok, I'm headed out."
        elif Girl == StormX:
                ch_s "Ok, I am finished here, [Girl.Petname]."
        elif Girl == JubesX:
                ch_v "Well, I'm done here. . ."
        menu:
            extend ""
            "Sure, see you later then.":
                    call Remove_Girl(Girl)
            "Actually, could you stick around a minute?":
                if ApprovalCheck(Girl, 900) or Girl == StormX:
                    if Girl == RogueX:
                            ch_r "Sure, what's up?"
                    elif Girl == KittyX:
                            ch_k "Yeah?"
                    elif Girl == EmmaX:
                            ch_e "Very well, what did you need?"
                    elif Girl == LauraX:
                            $ LauraX.Loc = "bg showerroom"
                            ch_l "Huh? Ok, what's up?"
                    elif Girl == JeanX:
                            ch_j "What? Why?"
                    elif Girl == StormX:
                            ch_s "I suppose so, what did you need?"
                    elif Girl == JubesX:
                            ch_v "Oh? Why?"
                else:

                    if Girl == RogueX:
                            ch_r "Um, actually, I'm not really comfortable being so. . . exposed?"
                            ch_r "I'll just see you around later."
                    elif Girl == KittyX:
                            ch_k "I'm[KittyX.like]totally exposed here?"
                            ch_k "I'm just going to head out."
                    elif Girl == EmmaX:
                            ch_e "I really shouldn't be \"hanging out\" in such a state."
                            ch_e "We can talk later."
                    elif Girl == LauraX:
                            ch_l "I probably shouldn't hang out like this."
                            ch_l "We'll talk later."
                    elif Girl == JeanX:
                            ch_j "I'd rather not."
                    elif Girl == JubesX:
                            ch_v "Um. . . nah. . ."
                    call Remove_Girl(Girl)

        if Line == "leaving":
                $ Girl.OutfitChange(6)
        $ Line = 0
        return 0
# End Girl Caught Shower / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



label Girls_Caught(Girl=0,TotalCaught=0,Shame=0,Count=0,T_Pet=0,BO=[]): #rkeljsv
    call Shift_Focus(Girl)
    call Checkout
    call AnyLine(Girl,"!!!")
    $ Line = Trigger
    call Trig_Reset
    $ Girl.OutfitChange()
    $ BO = TotalGirls[:]
    while BO:
            if BO[0].Loc == bg_current:
                    $ BO[0].Loc = "bg study"
            $ TotalCaught += BO[0].Caught
            $ BO.remove(BO[0])
    $ bg_current = "bg study"
    call Set_The_Scene(0)
    show Professor at sprite_location(StageLeft)

    if Girl == RogueX:
            show Rogue_Sprite at sprite_location(StageRight) with ease
    elif Girl == KittyX:
            show Kitty_Sprite at sprite_location(StageRight) with ease
    elif Girl == EmmaX:
            show Emma_Sprite at sprite_location(StageRight) with ease
    elif Girl == LauraX:
            show Laura_Sprite at sprite_location(StageRight) with ease
    elif Girl == JeanX:
            show Jean_Sprite at sprite_location(StageRight) with ease
    elif Girl == StormX:
            show Storm_Sprite at sprite_location(StageRight) with ease
    elif Girl == JubesX:
            show Jubes_Sprite at sprite_location(StageRight) with ease
    call OutfitShame(Girl,20)

    $ Count = Girl.Caught

    if Partner == RogueX:
            show Rogue_Sprite at sprite_location(StageFarRight) with ease
    elif Partner == KittyX:
            show Kitty_Sprite at sprite_location(StageFarRight) with ease
    elif Partner == EmmaX:
            show Emma_Sprite at sprite_location(StageFarRight) with ease
    elif Partner == LauraX:
            show Laura_Sprite at sprite_location(StageFarRight) with ease
    elif Partner == JeanX:
            show Jean_Sprite at sprite_location(StageFarRight) with ease
    elif Partner == StormX:
            show Storm_Sprite at sprite_location(StageFarRight) with ease
    elif Partner == JubesX:
            show Jubes_Sprite at sprite_location(StageFarRight) with ease

    call XavierFace("shocked")
    $ Girl.FaceChange("sad")
    if (Girl == EmmaX or Partner == EmmaX) and (Girl == StormX or Partner == StormX):
            ch_x "I'm very disappointed in the both of you!."
            ch_x "You should BOTH know better than this!"
    elif Girl == StormX or Partner == StormX:
            ch_x "I'm very disappointed in your behavior, particularly yours, Ororo."
    elif Girl == EmmaX or Partner == EmmaX:
            ch_x "I'm very disappointed in your behavior, particularly yours, Emma."
    else:
            ch_x "I'm very disappointed in your behavior, the both of you."

    if Line == "fondle thighs" or Line == "fondle breasts" or Line == "fondle pussy" or Line == "hotdog" or Line == "hand":
        ch_x "The two of you, feeling each other up like animals!"
    elif Line == "dildo pussy" or Line == "dildo anal":
        ch_x "Using those. . . devices on each other, unsanitary!"
    elif Line == "lick pussy":
        ch_x "Engaging in. . . cunnilingus. . . dripping everywhere. . ."
    elif Line == "blow":
        ch_x "Right there in public with his {i}penis{/i} in your mouth. . ."
    else:
        ch_x "Having sexual relations in such a public location, it shows very poor character of you!"

    if Girl.Shame >= 40:
            ch_x "[Girl.Name], my dear, you're practically naked! At least throw a towel on!"
            "He throws [Girl.Name] the towel."
            show blackscreen onlayer black
            $ BO = TotalGirls[:]
            while BO:
                    if BO[0].Loc == bg_current and (not BO[0].Over and not BO[0].Chest):
                            $ BO[0].Over = "towel"
                    $ BO.remove(BO[0])
            hide blackscreen onlayer black
            if (Girl == StormX or Partner == StormX) and StormX.Over == "towel":
                    ch_x ". . ."
                    ch_x "Ororo, for Christ's sake. . ."
                    ch_x "Put on some actual clothes!"
                    show blackscreen onlayer black
                    $ StormX.Over = "white shirt"
                    $ StormX.Legs = "skirt"
                    hide blackscreen onlayer black
                    ch_x ". . . fine."

    elif Girl.Shame >= 20:
            ch_x "[Girl.Name], my dear, that attire is positively scandalous."

    if Girl.Caught:
            #if Caught for Girl > 0
            "And this isn't even the first time this has happened!"

    if Partner:
            $ Partner.FaceChange("surprised",2)
            if Partner in Rules:
                    if Partner == KittyX:
                        "Xavier glances over at [KittyX.Name], who just waggles her phone. . ."
                    elif Partner == LauraX:
                        $ Laura_Arms = 2
                        "Xavier glances over at [LauraX.Name], who raises her fist and shakes it. . ."
                        $ Laura_Arms = 1
                    ch_x "And. . .hm, I could have sworn there was someone else. . ."
            else:
                    ch_x "And [Partner.Name], you were just watching this occur!"
            $ Partner.FaceChange("bemused",1, Eyes="side")

    if EmmaX.Loc == bg_current and EmmaX not in Rules:
        if not EmmaX.Caught:
                ch_x "Emma, you are entrusted as a teacher here, I can't have you fraternizing with the students."
                ch_x "This is especially true in the school's public spaces!"
                ch_x "What sort of message does that send?"
                ch_x "How appropriate would it be if I were to just wander the halls with Miss Grey on my lap?"
                call XavierFace("hypno")
                ch_x "Just. . . running my hands along her firm little body without a care in the world. . ."
                call XavierFace("happy")
                if JeanX.Loc == bg_current:
                        "You glance over at [JeanX.Name], she shrugs."
                ch_x ". . ."
                call XavierFace("shocked")
                ch_x "Yes, well, as I was saying! . ."
        else:
                ch_x "Emma, I don't believe this is the first time we've had this talk."
                ch_x "I should hope it will be the last."
    if StormX.Loc == bg_current and StormX not in Rules:
        if not StormX.Caught:
                if EmmaX.Loc == bg_current and EmmaX not in Rules:
                        ch_x "And Ororo! You also know better than to be fraternizing with the students!"
                else:
                        ch_x "Ororo, you are entrusted as a teacher here, I can't have you fraternizing with the students."
                ch_x "I'm well aware of your Bohemian tendencies in private, but you must comport yourself while in public."
                ch_x "What sort of message does that send?"
                ch_x "Do you think it would be appropriate for me to engage in such escapades?"
                call XavierFace("hypno")
                ch_x "Just. . . rolling down the halls with my balls flowing freely in the wind. . ."
                call XavierFace("happy")
                ch_x ". . ."
                call XavierFace("shocked")
                ch_x "Do not distract me! . ."
        else:
                if EmmaX.Loc == bg_current and EmmaX not in Rules:
                        ch_x "And Ororo! We've also been over this before."
                else:
                        ch_x "Ororo, I don't believe this is the first time we've had this talk."
                ch_x "I should hope it will be the last."

    $ Line = 0
    menu:
        ch_x "Well what have you to say for yourselves?"
        "Sorry sir, won't do it again.":
                if RogueX.Loc == bg_current and RogueX.Caught < 3:
                            $ RogueX.Statup("Love", 70, 20)
                            $ RogueX.Statup("Inbt", 50, -15)
                            $ RogueX.Statup("Love", 90, 5)
                if KittyX.Loc == bg_current and KittyX.Caught < 3:
                            $ KittyX.Statup("Love", 70, 10)
                            $ KittyX.Statup("Inbt", 30, -25)
                            $ KittyX.Statup("Inbt", 50, -10)
                if EmmaX.Loc == bg_current and EmmaX.Caught < 3:
                            $ EmmaX.Statup("Love", 70, 5)
                            $ EmmaX.Statup("Inbt", 30, -15)
                if LauraX.Loc == bg_current and LauraX.Caught < 3:
                            $ LauraX.Statup("Inbt", 30, -20)
                            $ LauraX.Statup("Inbt", 50, -10)
                if JeanX.Loc == bg_current and JeanX.Caught < 3:
                            $ JeanX.Statup("Obed", 30, -20)
                            $ JeanX.Statup("Obed", 50, -10)
                if StormX.Loc == bg_current and StormX.Caught < 3:
                            $ StormX.Statup("Love", 70, 5)
                            $ StormX.Statup("Inbt", 30, -5)
                if JubesX.Loc == bg_current and JubesX.Caught < 3:
                            $ JubesX.Statup("Love", 70, 10)
                            $ JubesX.Statup("Obed", 70, 5)
                            $ JubesX.Statup("Inbt", 30, -10)
                            $ JubesX.Statup("Inbt", 50, -5)
                $ Girl.Statup("Obed", 50, -5)

                call XavierFace("happy")
                if Girl.Caught:
                    ch_x "But you know you've done this before. . . at least [Girl.Caught] times. . ."
                elif Girl == EmmaX and TotalCaught:
                    ch_x "Not with Ms. Frost, perhaps, but you know you've done this before. . ."
                    ch_x "at least [TotalCaught] times. . ."
                    $ Girl.FaceChange("sexy",Brows="confused")
                elif Girl == StormX and TotalCaught:
                    ch_x "Not with Ms. Munroe, perhaps, but you know you've done this before. . ."
                    ch_x "at least [TotalCaught] times. . ."
                    $ Girl.FaceChange("sexy",Brows="confused")
                elif TotalCaught:
                    ch_x "Not with this young lady, perhaps, but you know you've done this before. . ."
                    ch_x "at least [TotalCaught] times. . ."
                else:
                    ch_x "Very well, just don't let it happen again. "
                $ Count += 5
                if PunishmentX:
                    ch_x "I'm extending your punishment by [Count] days."
                else:
                    ch_x "I'm halving your daily stipend for [Count] days."
                ch_x "Now return to your rooms and reflect on what you've done."
        #End "sorry"

        "Just having a little fun, right [Girl.Pet]?":
                $ Girl.NameCheck() #checks reaction to petname
                $ Girl.FaceChange("bemused")
                $ Girl.Statup("Lust", 90, 5)
                if RogueX.Loc == bg_current and RogueX.Caught < 5:
                        $ RogueX.Statup("Love", 70, 20)
                        $ RogueX.Statup("Love", 90, 10)
                if KittyX.Loc == bg_current and KittyX.Caught < 5:
                        $ KittyX.Statup("Inbt", 90, 10)
                        $ KittyX.Statup("Love", 90, 10)
                if EmmaX.Loc == bg_current and EmmaX.Caught < 5:
                        $ EmmaX.Statup("Inbt", 90, 10)
                        $ EmmaX.Statup("Love", 90, 10)
                if LauraX.Loc == bg_current and LauraX.Caught < 5:
                        $ LauraX.Statup("Inbt", 90, 10)
                        $ LauraX.Statup("Obed", 90, 5)
                        $ LauraX.Statup("Love", 90, 5)
                if JeanX.Loc == bg_current and JeanX.Caught < 5:
                        $ JeanX.Statup("Inbt", 200, 10)
                        $ JeanX.Statup("Obed", 50, 5)
                        $ JeanX.Statup("Obed", 90, 5)
                        $ JeanX.Statup("Love", 90, 5)
                if StormX.Loc == bg_current and StormX.Caught < 5:
                        $ StormX.Statup("Inbt", 90, 15)
                        $ StormX.Statup("Obed", 50, 5)
                        $ StormX.Statup("Love", 90, 5)
                if JubesX.Loc == bg_current and JubesX.Caught < 5:
                        $ JubesX.Statup("Inbt", 90, 5)
                        $ JubesX.Statup("Obed", 80, 5)
                        $ JubesX.Statup("Love", 90, 10)

                call XavierFace("angry")
                $ Count += 10
                ch_x "If that's your attitude, harsher methods might be necessary."
                if PunishmentX:
                    ch_x "I'm extending your punishment by [Count] days."
                else:
                    ch_x "I'm halving your daily stipend for [Count] days."

                if RogueX.Loc == bg_current and RogueX.Caught < 3:
                        $ RogueX.Statup("Obed", 50, 20)
                        $ RogueX.Statup("Obed", 90, 20)
                        $ RogueX.Statup("Inbt", 30, -20)
                        $ RogueX.Statup("Inbt", 50, -10)
                if KittyX.Loc == bg_current and KittyX.Caught < 3:
                        $ KittyX.Statup("Obed", 50, 20)
                        $ KittyX.Statup("Obed", 90, 20)
                        $ KittyX.Statup("Inbt", 30, -20)
                if EmmaX.Loc == bg_current and EmmaX.Caught < 3:
                        $ EmmaX.Statup("Obed", 50, 20)
                        $ EmmaX.Statup("Obed", 90, 20)
                        $ EmmaX.Statup("Inbt", 30, -20)
                if LauraX.Loc == bg_current and LauraX.Caught < 3:
                        $ LauraX.Statup("Obed", 50, 20)
                        $ LauraX.Statup("Obed", 90, 20)
                        $ LauraX.Statup("Inbt", 30, -20)
                if JeanX.Loc == bg_current and JeanX.Caught < 3:
                        $ JeanX.Statup("Obed", 50, 20)
                        $ JeanX.Statup("Obed", 90, 20)
                if StormX.Loc == bg_current and StormX.Caught < 3:
                        $ StormX.Statup("Obed", 50, 20)
                        $ StormX.Statup("Inbt", 30, -10)
                if JubesX.Loc == bg_current and JubesX.Caught < 3:
                        $ JubesX.Statup("Obed", 70, 10)
                        $ JubesX.Statup("Inbt", 30, -10)

                ch_x "I've had enough of you, begone."
        #End "Little fun"

        "Just this. . . Plan Omega, [RogueX.Name]." if Girl == RogueX and Player.Lvl >= 5:
                $ Line = "Omega"
        "Just this. . . Plan Kappa, [KittyX.Name]!" if Girl == KittyX and Player.Lvl >= 5:
                $ Line = "Kappa"
        "Just this. . . Plan Psi, [EmmaX.Name]!" if Girl == EmmaX and Player.Lvl >= 5:
                $ Line = "Psi"
        "Just this. . . Plan Chi, [LauraX.Name]!" if Girl == LauraX and Player.Lvl >= 5:
                $ Line = "Chi"
        "Just this. . . Plan Alpha, [JeanX.Name]!" if Girl == JeanX and Player.Lvl >= 5:
                $ Line = "Alpha"
        "Just this. . . Plan Rho, [StormX.Name]!" if Girl == StormX and Player.Lvl >= 5:
                $ Line = "Rho"
        "Just this. . . Plan Zeta, [JubesX.Name]!" if Girl == JubesX and Player.Lvl >= 5:
                $ Line = "Zeta"
        #End "Plan X"


        "You can suck it, old man.":
                $ Girl.FaceChange("surprised")
                $ Girl.Statup("Lust", 90, 10)
                if RogueX.Loc == bg_current and RogueX.Caught < 3:
                        $ RogueX.Statup("Obed", 50, 20)
                        $ RogueX.Statup("Obed", 90, 40)
                if KittyX.Loc == bg_current and KittyX.Caught < 3:
                        $ KittyX.Statup("Obed", 50, 25)
                        $ KittyX.Statup("Obed", 90, 40)
                if EmmaX.Loc == bg_current and EmmaX.Caught < 3:
                        $ EmmaX.Statup("Love", 90, 5)
                        $ EmmaX.Statup("Obed", 50, 20)
                        $ EmmaX.Statup("Obed", 90, 30)
                if LauraX.Loc == bg_current and LauraX.Caught < 3:
                        $ LauraX.Statup("Love", 90, 5)
                        $ LauraX.Statup("Obed", 50, 25)
                        $ LauraX.Statup("Obed", 90, 30)
                if JeanX.Loc == bg_current and JeanX.Caught < 3:
                        $ JeanX.Statup("Love", 50, 5)
                        $ JeanX.Statup("Love", 90, 10)
                        $ JeanX.Statup("Obed", 50, 25)
                        $ JeanX.Statup("Obed", 90, 30)
                if StormX.Loc == bg_current and StormX.Caught < 3:
                        $ StormX.Statup("Love", 90, -5)
                        $ StormX.Statup("Obed", 50, 20)
                        $ StormX.Statup("Obed", 90, 30)
                if JubesX.Loc == bg_current and JubesX.Caught < 3:
                        $ JubesX.Statup("Love", 80, 10)
                        $ JubesX.Statup("Obed", 50, 25)
                        $ JubesX.Statup("Obed", 90, 30)

                call XavierFace("angry")
                $ Count += 20
                ch_x "If that's your attitude, harsher methods might be necessary."
                if PunishmentX:
                    ch_x "I'm extending your punishment by [Count] days!"
                else:
                    ch_x "I'm halving your daily stipend for [Count] days!"

                if RogueX.Loc == bg_current and RogueX.Caught < 3:
                        if RogueX.Inbt > 500:
                            $ RogueX.Statup("Inbt", 90, 15)
                        $ RogueX.Statup("Inbt", 30, -20)
                        $ RogueX.Statup("Inbt", 50, -10)
                if KittyX.Loc == bg_current and KittyX.Caught < 3:
                        if KittyX.Inbt > 500:
                            $ KittyX.Statup("Inbt", 90, 15)
                        $ KittyX.Statup("Inbt", 30, -20)
                        $ KittyX.Statup("Inbt", 50, -10)
                if EmmaX.Loc == bg_current and EmmaX.Caught < 3:
                        if EmmaX.Inbt > 500:
                            $ EmmaX.Statup("Inbt", 90, 15)
                        $ EmmaX.Statup("Inbt", 30, -20)
                        $ EmmaX.Statup("Inbt", 50, -10)
                if LauraX.Loc == bg_current and LauraX.Caught < 3:
                        if LauraX.Inbt > 500:
                            $ LauraX.Statup("Inbt", 90, 15)
                        $ LauraX.Statup("Inbt", 30, -15)
                        $ LauraX.Statup("Inbt", 50, -10)
                if JeanX.Loc == bg_current and JeanX.Caught < 3:
                        $ JeanX.Statup("Inbt", 90, 15)
                if StormX.Loc == bg_current and StormX.Caught < 3:
                        if StormX.Inbt > 500:
                            $ StormX.Statup("Inbt", 90, 5)
                        $ StormX.Statup("Inbt", 30, -10)
                        $ StormX.Statup("Inbt", 50, -5)
                if JubesX.Loc == bg_current and JubesX.Caught < 3:
                        if JubesX.Inbt > 500:
                            $ JubesX.Statup("Inbt", 90, 15)
                        $ JubesX.Statup("Inbt", 30, -15)
                        $ JubesX.Statup("Inbt", 50, -10)

                ch_x "Now get out of my sight."
        #End "suck it"

    if Line:
            if Line == "Omega":
                    if ApprovalCheck(RogueX, 1500, TabM=1, Loc="No"):
                            call Xavier_Plan(RogueX) #Plan_OmegaPlan_Alpha
                            return
                    elif ApprovalCheck(RogueX, 1000, TabM=1, Loc="No"):
                            $ Girl.FaceChange("perplexed",Brows = "sad")
                            ch_r "I'm not comfortable with something that extreme, [RogueX.Petname]. . ."
                            menu:
                                "Dammit [RogueX.Name]. . .":
                                        $ Girl.FaceChange("angry")
                                        $ RogueX.Statup("Obed", 50, 5)
                                        $ RogueX.Statup("Love", 90, -5)
                                "Yeah, I guess you're right. . .":
                                        $ Girl.FaceChange("bemused")
                    else:
                            $ Girl.FaceChange("confused")
                            ch_r "What nonsense are you talking now?"
                            ch_p "Plan {i}Omega!{/i} . . you know. . ."
                            ch_r "Sounds like gibberish."
                            ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                            $ Girl.FaceChange("bemused")
                    #End "Plan Omega"
            elif Line == "Kappa":
                    if "Xavier's photo" in Player.Inventory and ApprovalCheck(KittyX, 1500, TabM=1, Loc="No"):
                            call Xavier_Plan(KittyX) #Plan_KappaPlan_Alpha
                            return
                    elif ApprovalCheck(KittyX, 1000, TabM=1, Loc="No"):
                            $ Girl.FaceChange("perplexed",Brows = "sad")
                            if "Xavier's photo" in Player.Inventory:
                                    ch_k "You know. . . I really don't think that's a good idea. . ."
                            elif "kappa" in Player.History:
                                    ch_k "Maybe if we came back later we could find something. . ."
                            else:
                                    ch_k "We don't really have any way to pull that off atm. . ."
                                    $ Player.History.append("kappa")
                            menu:
                                "Dammit [KittyX.Name]. . .":
                                        $ Girl.FaceChange("angry")
                                        $ KittyX.Statup("Obed", 50, 5)
                                        $ KittyX.Statup("Love", 90, -5)
                                "Yeah, I guess you're right. . .":
                                        $ Girl.FaceChange("bemused")
                                        $ KittyX.Statup("Love", 90, 5)
                    else:
                            $ Girl.FaceChange("confused")
                            ch_k "Wait, Plan what??"
                            ch_p "Plan {i}Kappa!{/i} . . you know. . ."
                            ch_k "I have no {i}idea{/i} what you're talking about."
                            ch_p "oh, yeah, I guess I haven't mentioned that. . ."
                            $ Girl.FaceChange("bemused")
                    #End "Plan Kappa"
            elif Line == "Psi":
                    if ApprovalCheck(EmmaX, 1500, TabM=1, Loc="No"):
                            call Xavier_Plan(EmmaX) #Plan_PsiPlan_Alpha
                            return
                    elif ApprovalCheck(EmmaX, 1000, TabM=1, Loc="No"):
                            $ Girl.FaceChange("perplexed",Brows = "sad")
                            ch_e "Um, I don't believe we're quite at that point yet, [EmmaX.Petname]. . ."
                            menu:
                                "Dammit [EmmaX.Name]. . .":
                                        $ Girl.FaceChange("angry")
                                        $ EmmaX.Statup("Obed", 50, 5)
                                        $ EmmaX.Statup("Love", 90, -5)
                                "Yeah, I guess you're right. . .":
                                        $ Girl.FaceChange("bemused")
                    else:
                            $ Girl.FaceChange("confused")
                            ch_e "Lord child, what are you talking about now?"
                            ch_p "Plan {i}Psi!{/i} . . you know. . ."
                            ch_e "I wish that I did."
                            ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                            $ Girl.FaceChange("bemused")
                    #End "Plan Psi"
            elif Line == "Chi":
                    if LauraX.Lvl >= 2 and ApprovalCheck(LauraX, 1500, TabM=1, Loc="No") and ApprovalCheck(LauraX, 750, "I"):
                            call Xavier_Plan(LauraX) #Plan_ChiPlan_Alpha
                            return
                    elif ApprovalCheck(LauraX, 1000, TabM=1, Loc="No"):
                            $ Girl.FaceChange("angry",Eyes="side",Brows = "angry")
                            ch_l "I told you that was a stupid idea. . ."
                            menu:
                                "Dammit [LauraX.Name]. . .":
                                        $ Girl.FaceChange("angry")
                                        $ LauraX.Statup("Obed", 50, 5)
                                        $ LauraX.Statup("Love", 90, -5)
                                "Yeah, I guess you're right. . .":
                                        $ Girl.FaceChange("bemused")
                                        $ LauraX.Statup("Love", 90, 5)
                    else:
                            $ Girl.FaceChange("confused")
                            ch_l "Yeah!"
                            ch_l ". . ."
                            ch_l "Wait, plan \"key,\" what??"
                            ch_p "Plan {i}Chi!{/i} . . you know. . ."
                            ch_l "Um. No?"
                            ch_p "oh, yeah, I guess I haven't mentioned that. . ."
                            $ Girl.FaceChange("bemused")
                    #End "Plan Chi"
            elif Line == "Alpha":
                    if ApprovalCheck(JeanX, 1500, TabM=1, Loc="No"):
                            call Xavier_Plan(JeanX) #Plan_Alpha
                            return
                    elif ApprovalCheck(JeanX, 1000, TabM=1, Loc="No"):
                            $ Girl.FaceChange("perplexed",Brows = "sad")
                            ch_j "Look, this is your mess, I'm not going to clean it up, [JeanX.Petname]. . ."
                            menu:
                                "Dammit [JeanX.Name]. . .":
                                        $ Girl.FaceChange("angry")
                                        $ JeanX.Statup("Obed", 50, 5)
                                        $ JeanX.Statup("Love", 90, -5)
                                "Yeah, I guess you're right. . .":
                                        $ Girl.FaceChange("bemused")
                    else:
                            $ Girl.FaceChange("confused")
                            ch_j "Huh? What are you talking about?"
                            ch_p "Plan {i}Alpha!{/i} . . you know. . ."
                            ch_j "Drawing a blank here. . ."
                            ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                            $ Girl.FaceChange("bemused")
                    #End "Plan Alpha"
            elif Line == "Rho":
                    if "Xavier's files" in Player.Inventory and ApprovalCheck(StormX, 1500, TabM=1, Loc="No"):
                            call Xavier_Plan(StormX)
                            return
                    elif ApprovalCheck(StormX, 1000, TabM=1, Loc="No"):
                            $ Girl.FaceChange("perplexed",Brows = "sad")
                            if "Xavier's files" in Player.Inventory:
                                    ch_s "I really doubt that we should attempt that. . ."
                            elif "rho" in Player.History:
                                    ch_s "Perhaps if we had some leverage on the situation. . ."
                            else:
                                    ch_s "I'm not sure what you think we could do here. . ."
                                    $ Player.History.append("rho")
                            menu:
                                "Dammit [StormX.Name]. . .":
                                        $ Girl.FaceChange("angry")
                                        $ StormX.Statup("Obed", 50, 5)
                                        $ StormX.Statup("Love", 90, -5)
                                "Yeah, I guess you're right. . .":
                                        $ Girl.FaceChange("bemused")
                    else:
                            $ Girl.FaceChange("confused")
                            ch_s "'Ro? You were speaking to me?"
                            ch_p "Yes! Plan {i}Rho!{/i} . . you know. . ."
                            ch_s "Yes, this is 'Ro. What plan?"
                            ch_p "What's on second! I don't know!"
                            $ Girl.FaceChange("smile")
                            ch_s "Ah! \"Third base!\""
                            $ Girl.FaceChange("bemused")
                    #End "Plan Rho"
            elif Line == "Zeta":
                    if ApprovalCheck(JubesX, 1500, TabM=1, Loc="No"):
                            call Xavier_Plan(JubesX) #Plan_PsiPlan_Alpha
                            return
                    elif ApprovalCheck(JubesX, 1000, TabM=1, Loc="No"):
                            $ Girl.FaceChange("perplexed",Brows = "sad")
                            ch_v "What?! Um, no, let's not."
                            menu:
                                "Dammit [JubesX.Name]. . .":
                                        $ Girl.FaceChange("angry")
                                        $ JubesX.Statup("Obed", 50, 5)
                                        $ JubesX.Statup("Love", 90, -5)
                                "Yeah, I guess you're right. . .":
                                        $ Girl.FaceChange("bemused")
                    else:
                            $ Girl.FaceChange("confused")
                            ch_v "Huh?"
                            ch_p "Plan {i}Zeta!{/i} . . you know. . ."
                            ch_v "Is this a \"Gundam\" thing?"
                            ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                            $ Girl.FaceChange("bemused")
                    #End "Plan Zeta"

            # if the plan falls through. . .
            call XavierFace("angry")
            $ Count += 10
            ch_x "I have no idea what that was about, but it sounds like you haven't learned."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."

                if RogueX.Loc == bg_current and RogueX.Caught < 3:
                        $ RogueX.Statup("Obed", 50, 10)
                        $ RogueX.Statup("Obed", 90, 10)
                        $ RogueX.Statup("Inbt", 30, -10)
                        $ RogueX.Statup("Inbt", 50, -5)
                if KittyX.Loc == bg_current and KittyX.Caught < 3:
                        $ KittyX.Statup("Obed", 50, 10)
                        $ KittyX.Statup("Obed", 90, 10)
                        $ KittyX.Statup("Inbt", 30, -10)
                        $ KittyX.Statup("Inbt", 50, -5)
                if EmmaX.Loc == bg_current and EmmaX.Caught < 3:
                        $ EmmaX.Statup("Obed", 50, 10)
                        $ EmmaX.Statup("Inbt", 50, -5)
                if LauraX.Loc == bg_current and LauraX.Caught < 3:
                        $ LauraX.Statup("Obed", 50, 10)
                        $ LauraX.Statup("Obed", 90, 10)
                        $ LauraX.Statup("Inbt", 30, -10)
                        $ LauraX.Statup("Inbt", 50, -5)
                if JeanX.Loc == bg_current and JeanX.Caught < 3:
                        $ JeanX.Statup("Obed", 50, -10)
                if StormX.Loc == bg_current and StormX.Caught < 3:
                        $ StormX.Statup("Obed", 50, 10)
                        $ StormX.Statup("Inbt", 50, -5)
                if JubesX.Loc == bg_current and JubesX.Caught < 3:
                        $ JubesX.Statup("Obed", 50, 5)
                        $ JubesX.Statup("Obed", 90, 5)
                        $ JubesX.Statup("Inbt", 30, -8)
                        $ JubesX.Statup("Inbt", 50, -2)
            ch_x "I've had enough of you, begone."
    #End "evil plans"

    $ PunishmentX += Count

    $ Girl.Caught += 1
    if Partner in TotalGirls:
            $ Partner.Caught += 1
    $ Girl.AddWord(0,"caught","caught") #recent and daily

    if Girl == KittyX and KittyX not in Rules and "Xavier's photo" not in Player.Inventory:
            "It would probably be a good idea to find some way to get Xavier to leave you alone."
            if KittyX.Caught > 1:
                "Maybe I should try searching the office when he's not around."
            if KittyX.Caught > 2:
                "I bet [KittyX.Name] could help me get in."
            if KittyX.Caught > 3:
                "I bet there's something in that lefthand drawer. . ."
    elif Girl == JeanX and "nowhammy" not in JeanX.Traits and JeanX.Caught > 1:
            ch_x "Oh, and Jean, dear, I'd like a word?"
            $ Girl.FaceChange("bemused")
            ch_j "What is it?"
            ch_x "I understand that you've been using your abilities to. . ."
            ch_x "cover up for some of your. . . transgressions."
            $ Girl.FaceChange("bemused",Eyes="up")
            ch_j "Oh, you mean how I mindwipe the \"NPCs\" that get too nosy?"
            call XavierFace("angry")
            ch_x "If by \"NPCs\" you mean your fellow students. . ."
            ch_x ". . . and by \"get too nosy,\" you mean \"notice you having sex in public\". . ."
            ch_x ". . . then yes, that is exactly what I mean."
            $ Girl.FaceChange("bemused",Eyes="side")
            ch_j "Ok, yeah."
            ch_x "I would like you to cease this activity at once!"
            ch_x "It is a total abuse of your abilities and of those students' autonomy!"
            $ Girl.FaceChange("angry",1)
            ch_j "Who cares."
            call XavierFace("shocked")
            ch_x "!!!"
            ch_x "I do!"
            call XavierFace("angry")
            ch_x "That is it, young lady. Until further notice, you're forbidden from. . . whammying your fellow students!"
            $ Girl.FaceChange("angry",1,Mouth="surprised")
            ch_j "Bullshit!"
            $ Girl.FaceChange("angry",0,Eyes="psychic")
            ch_x "Ugh. . ."
            call XavierFace("psychic")
            ch_x "[Player.Name]. . . this may take a while. . ."
            ch_x "You may as well leave. . ."
            $ JeanX.Traits.append("nowhammy")
            $ Girl.FaceChange("normal")

    if EmmaX.Loc == bg_current and EmmaX not in Rules:
            ch_x "Emma, I'd like you to stay after for a brief discussion about \"boundaries\". . ."
            if EmmaX.Caught:
                    $ EmmaX.Statup("Love", 90, -5)
                    $ Girl.FaceChange("angry",Eyes="closed")
                    ch_e "Not again. . ."
    if StormX.Loc == bg_current and StormX not in Rules:
            if EmmaX.Loc == bg_current and EmmaX not in Rules:
                    ch_x "And Ororo, I'm afraid we will have to have words as well. . ."
            else:
                    ch_x "Ororo, I'd like you to stay after for a brief discussion about \"boundaries\". . ."
            if StormX.Caught:
                    $ StormX.Statup("Love", 90, -5)
                    $ Girl.FaceChange("angry",Eyes="closed")
                    ch_s "Again? . ."
            if StormX not in Rules and "Xavier's files" not in Player.Inventory:
                    "It would probably be a good idea to find some way to get Xavier to leave you alone."
                    if StormX.Caught > 1:
                        "Maybe I should try searching the office when he's not around."
                    if StormX.Caught > 2:
                        "I bet [StormX.Name] could help me get in."
                    if StormX.Caught > 3:
                        "I bet there's something in that righthand drawer. . ."

    call Remove_Girl("All")
    "You return to your room"
    hide Professor
    $ bg_current = "bg player"
    jump Misplaced
#End Caught / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Xavier_Plan(GirlX=0): #rkeljsv
    if "Xavier" in Player.DailyActions:
            "The Professor seems pretty out of it."
            "You don't think you'll be able to get anything more out of him today."
            "You leave him to it."
            $ bg_current = "bg player"
            jump Misplaced

    #$ GirlX = GirlCheck(GirlX)
    call Shift_Focus(GirlX)
    $ GirlX.FaceChange("sly")
    "As you say this, a sly grin crosses [GirlX.Name]'s face."
    "You quickly approach Xavier and place your hands on his head."
    call XavierFace("psychic")
    ch_x ". . ."
    call XavierFace("shocked")
    "Xavier realizes with a shock that with your powers, his telepathy is useless."

    if Partner:
            if Partner == RogueX and "Omega" not in Player.Traits:
                    $ Line = "first"
            elif Partner == KittyX and "Kappa" not in Player.Traits:
                    $ Line = "first"
            elif Partner == EmmaX and "Psi" not in Player.Traits:
                    $ Line = "first"
            elif Partner == LauraX and "Chi" not in Player.Traits:
                    $ Line = "first"
            elif Partner == JeanX and "Alpha" not in Player.Traits:
                    $ Line = "first"
            elif Partner == StormX and "Rho" not in Player.Traits:
                    $ Line = "first"
            elif Partner == JubesX and "Zeta" not in Player.Traits:
                    $ Line = "first"

            if Line == "first":
                #if the Partner has never done this. . .
                if ApprovalCheck(Partner, 1000) or Partner == JeanX:
                        #if she's cool with it.
                        $ Partner.FaceChange("surprised")
                        "[Partner.Name] looks a bit caught off guard, but goes along with the idea."
                        $ Partner.FaceChange("sly")
                else:
                        $ Partner.FaceChange("surprised")
                        "[Partner.Name] looks a bit uncomfortable with what's happening and takes off."
                        call Remove_Girl(Partner)

            else:
                        $ Partner.FaceChange("sly")
                        "[Partner.Name] understands what's going on here."
    #end partner response

    call XavierFace("angry")
    if GirlX == RogueX:
            $ RogueX.Arms = 0
            $ RogueX.ArmPose = 2
            show Rogue_Sprite at sprite_location(StageLeft+100,85) zorder 24 with ease
            "[RogueX.Name] moves in and also grabs his head, duplicating his powers as he watches helplessly."
            "Now that she posesses his full power, while his are negated, he has no defenses."
            call XavierFace("hypno")
            if "Omega" in Player.Traits:
                    ch_x "Oh, not again."
                    ch_x "What is it you want this time?"
                    $ RogueX.Statup("Obed", 80, 3)
                    $ RogueX.Statup("Inbt", 70, 1)
            else:
                    $ RogueX.Statup("Obed", 50, 40)
                    $ RogueX.Statup("Inbt", 70, 20)
            ch_r "Well, [RogueX.Petname], what would you like to do with this opportunity?"
            ch_r "I think we'll only get three tries at this. . ."
    elif GirlX == KittyX:
            $ KittyX.ArmPose = 2
            show Kitty_Sprite at sprite_location(StageLeft+100,150) with ease
            $ KittyX.sprite_location = StageCenter
            "[KittyX.Name] moves in sits on his lap, pinning his arms to the chair."
            if "Kappa" in Player.Traits:
                    ch_x "Oh, not again."
                    ch_x "What is it you want this time?"
                    $ KittyX.Statup("Obed", 80, 3)
                    $ KittyX.Statup("Inbt", 70, 1)
            else:
                    ch_x "What is the meaning of this? Unhand me!"
                    "You pull out the photo you found earlier in his study."
                    $ KittyX.Statup("Obed", 50, 40)
                    $ KittyX.Statup("Inbt", 70, 30)
                    ch_p "I have here a rather. . . compromising photo of you and Mystique."
                    ch_p "I was thinking maybe you could cut me a little slack around here."
                    ch_x "And if I do not?"
                    ch_p "[KittyX.Name] here's set it to distribute to every computer in school, every day."
                    ch_p "And only I know the password."
                    ch_x "Very well. . . I'll forget about your punishment."
                    ch_p "Oh, I think we can do a bit better than that. . ."
                    $ KittyX.Statup("Obed", 200, 30)
                    $ KittyX.Statup("Inbt", 200, 10)
            ch_k "Well, [KittyX.Petname], what should we ask for?"
    elif GirlX == EmmaX or GirlX == JeanX:
            if GirlX == EmmaX:
                    show Emma_Sprite at sprite_location(StageLeft+100,85) zorder 24 with ease
            elif GirlX == JeanX:
                    show Jean_Sprite at sprite_location(StageLeft+100,85) zorder 24 with ease
            "[GirlX.Name] moves behind Xavier and activates her own telepathy."
            call XavierFace("angry")
            if (GirlX == EmmaX and "Psi" in Player.Traits) or (GirlX == JeanX and "Alpha" in Player.Traits):
                    ch_x "Oh, not again. . ."
                    $ GirlX.Statup("Obed", 80, 3)
                    $ GirlX.Statup("Inbt", 80, 1)
            else:
                    $ GirlX.Statup("Obed", 50, 40)
                    $ GirlX.Statup("Inbt", 70, 30)
                    $ GirlX.Statup("Obed", 200, 30)
                    $ GirlX.Statup("Inbt", 200, 10)
            call AnyLine(GirlX,"Well, "+GirlX.Petname+", what should we ask for?")
    elif GirlX == LauraX:
            $ LauraX.ArmPose = 2
            if "Chi" in Player.Traits:
                    ch_x "Oh, not again."
                    $ LauraX.Claws = 1
                    ch_x "What is it you want this time?"
                    $ LauraX.Statup("Obed", 80, 3)
                    $ LauraX.Statup("Inbt", 80, 1)
            else:
                    ch_x "What is the meaning of this? Unhand me!"
                    ch_p "[LauraX.Name] and I were talking, and it seems like neither of us appreciates you bothering us."
                    ch_x "And if I continue?"
                    ch_p "My little [LauraX.Pet] here has a very particular set of skills, you know. . ."
                    $ GirlX.NameCheck() #checks reaction to petname
                    $ LauraX.Claws = 1
                    $ GirlX.FaceChange("sly")
                    ch_p "She could cause a lot of trouble if she keeps getting called down here. . ."
                    "[LauraX.Name] draws her claws along the arm of the Professor's chair, tracing fine lines into the metal."
                    ch_x "Very well. . . I'll forget about your punishment."
                    ch_p "Oh, I think we can do a bit better than that. . ."
                    $ LauraX.Statup("Obed", 50, 40)
                    $ LauraX.Statup("Inbt", 80, 30)
                    $ LauraX.Statup("Obed", 200, 30)
                    $ LauraX.Statup("Inbt", 200, 10)
            ch_l "Well, [LauraX.Petname], what should we ask for?"
    elif GirlX == StormX:
            $ StormX.ArmPose = 1
            show Storm_Sprite at sprite_location(StageLeft+100,150) with ease
            $ StormX.sprite_location = StageCenter
            "[StormX.Name] moves in sits on his lap, pinning his arms to the chair."
            if "Rho" in Player.Traits:
                    ch_x "Oh, not this again."
                    ch_x "What is it you want this time?"
                    $ StormX.Statup("Obed", 80, 3)
                    $ StormX.Statup("Inbt", 70, 1)
            else:
                    ch_x "What is the meaning of this? Unhand me!"
                    "You pull out the files you found earlier in his study."
                    $ StormX.Statup("Obed", 50, 40)
                    $ StormX.Statup("Inbt", 70, 30)
                    ch_p "I have here some rather. . . questionable \"medical\" files."
                    ch_p "I was thinking maybe you could cut me a little slack around here."
                    ch_x "And if I do not?"
                    ch_p "We've made sure that -all- the girls in these files will find out."
                    ch_x "Very well. . . I'll forget about your punishment."
                    ch_p "Oh, I think we can do a bit better than that. . ."
                    $ StormX.Statup("Obed", 200, 30)
                    $ StormX.Statup("Inbt", 200, 10)
            ch_s "Well, [StormX.Petname], what should we ask for?"
    elif GirlX == JubesX:
            $ JubesX.ArmPose = 2
            show Jubes_Sprite at sprite_location(StageLeft+100,150) with ease
            $ JubesX.sprite_location = StageCenter
            "[JubesX.Name] moves in and sits on his lap, pinning his arms to the chair."  #fix, change this when doggy pose is available
            "She turns to look at him."
            if "Zeta" in Player.Traits:
                    ch_x "Oh, not again."
                    ch_x "What is it you want this time?"
                    $ JubesX.Statup("Obed", 80, 3)
                    $ JubesX.Statup("Inbt", 70, 1)
            else:
                    ch_x "What is the meaning of this? Unhand me!"
                    $ JubesX.Statup("Inbt", 70, 30)
                    ch_v "Look into my eyes. . ."
                    $ JubesX.Statup("Obed", 50, 40)
                    $ JubesX.Statup("Inbt", 200, 10)
                    ch_v "see the sparks dancing around them? . . ."
                    $ JubesX.Statup("Obed", 200, 30)
                    "She slowly mesmerizes him into a trance, using a combination of her vampiric abilties and fireworks. . ."
            ch_v "Well, [JubesX.Petname], what should we ask for?"

    $ Count = 3
    $ PunishmentX = 0
    while Count > 0:
        $ Count -= 1
        menu:
            ch_x "What do you want?"
            "Don't bother us anymore when we're having fun." if GirlX not in Rules:
                    ch_x "Very well. . . I could offer you some. . . discretion. . ."
                    $ Rules.append(GirlX)
            "You know, it's kinda fun dodging you, catch us if you can." if GirlX in Rules:
                    ch_x "If you. . . want me to, I suppose. . ."
                    $ Rules.remove(GirlX)

            "You know, [JeanX.Name] should be able to \"whammy\" people again." if JeanX in TotalGirls and "nowhammy" in JeanX.Traits:
                    ch_x "I could remove her mind-wiping ban. . ."
                    $ JeanX.Traits.remove("nowhammy")
                    $ JeanX.Traits.append("whammy")
                    if JeanX.Loc == bg_current:
                            $ JeanX.Statup("Obed", 50, 5)
                            $ JeanX.Statup("Love", 50, 5)
                            $ JeanX.Statup("Love", 70, 5)
                            $ JeanX.Statup("Love", 90, 5)
                            $ GirlX.FaceChange("sly",1)
                            ch_j "Nice. . ."
            "You know, I did like it when [JeanX.Name] couldn't use her \"whammy.\"" if JeanX in TotalGirls and "whammy" in JeanX.Traits:
                    ch_x "I could reinstate her mind-wiping ban. . ."
                    $ JeanX.Traits.append("nowhammy")
                    $ JeanX.Traits.remove("whammy")
                    if JeanX.Loc == bg_current:
                            $ JeanX.Statup("Obed", 50, 5)
                            $ JeanX.Statup("Obed", 80, 5)
                            $ JeanX.Statup("Love", 70, -5)
                            $ JeanX.Statup("Love", 90, -5)
                            $ GirlX.FaceChange("angry",1,Mouth="surprised")
                            ch_j "Hey!"
                            $ GirlX.FaceChange("angry",1)

            "Raise my stipend." if Player.Income < 30:
                    if GirlX == RogueX and "Omega" not in Player.Traits:
                            ch_x "Very well. . . but I can only raise it by so much. . ."
                            $ Player.Income += 2
                    elif GirlX == KittyX and "Kappa" not in Player.Traits:
                            ch_x "Very well. . . but I can only raise it by so much. . ."
                            $ Player.Income += 2
                    elif GirlX == EmmaX and "Psi" not in Player.Traits:
                            ch_x "Very well. . . but I can only raise it by so much. . ."
                            $ Player.Income += 2
                    elif GirlX == LauraX and "Chi" not in Player.Traits:
                            ch_x "Very well. . . but I can only raise it by so much. . ."
                            $ Player.Income += 2
                    elif GirlX == JeanX and "Alpha" not in Player.Traits:
                            ch_x "Very well. . . but I can only raise it by so much. . ."
                            $ Player.Income += 2
                    elif GirlX == StormX and "Rho" not in Player.Traits:
                            ch_x "Very well. . . but I can only raise it by so much. . ."
                            $ Player.Income += 2
                    elif GirlX == JubesX and "Zeta" not in Player.Traits:
                            ch_x "Very well. . . but I can only raise it by so much. . ."
                            $ Player.Income += 2
                    else:
                            ch_x "I'm afraid I can't manage any more than I have. . ."
                            $ Count += 1
            "Raise my stipend. [[Used](locked)" if Player.Income >= 30:
                    pass

            "There's this girl that's been bothering me. . .":
                    "This will send a girl away, temporarily removing her from the game."
                    "You can always ask to bring her back later."
                    $ Line = 0
                    menu:
                        ch_p "Could you get rid of. . ."
                        "[RogueX.Name]" if RogueX in ActiveGirls:
                                $ Line = RogueX
                        "[KittyX.Name]" if KittyX in ActiveGirls and "met" in KittyX.History:
                                $ Line = KittyX
                        "[EmmaX.Name]" if EmmaX in ActiveGirls and "met" in EmmaX.History:
                                $ Line = EmmaX
                        "[LauraX.Name]" if LauraX in ActiveGirls and "met" in LauraX.History and "dress0" not in LauraX.History:
                                $ Line = LauraX
                        "[JeanX.Name]" if JeanX in ActiveGirls and "met" in JeanX.History:
                                $ Line = JeanX
                        "[StormX.Name]" if StormX in ActiveGirls and "met" in StormX.History:
                                $ Line = StormX
                        "[JubesX.Name]" if JubesX in ActiveGirls and "met" in JubesX.History:
                                $ Line = JubesX
                        "Never mind. . .":
                                $ Count += 1
                    if Line:
                            #if you picked someone. . .
                            ch_x "Very well, I suppose I can keep her occupied with various tasks around the campus. . ."
                            ch_x "She should be out of your hair for the time being."
                            if Line.Loc == bg_current:
                                    #if she's in the room
                                    $ Line.Statup("Love", 90, -10)
                                    $ Line.Statup("Obed", 50, 3)
                                    if Line == RogueX:
                                            ch_r "What do you mean, I'm \"bothering\" you?"
                                    elif Line == KittyX:
                                            ch_k "Hey, what gives?!"
                                    elif Line == EmmaX:
                                            ch_e "Excuse me? I must not have heard that right."
                                    elif Line == LauraX:
                                            ch_l "Explain."
                                    elif Line == JeanX:
                                            ch_j "Are you kidding me?!"
                                    elif Line == StormX:
                                            ch_s "I do not understand this."
                                    elif Line == JubesX:
                                            ch_v "Seriously?!"
                                    menu:
                                        extend ""
                                        "Oh, sorry, never mind.":
                                                $ Line = 0
                                                if ApprovalCheck(Line, 2000):
                                                        #if she accepts it
                                                        $ Line.FaceChange("confused")
                                                        $ Line.Statup("Love", 90, 3)
                                                        $ Line.Statup("Obed", 50, 2)
                                                        if Line == RogueX:
                                                                ch_r "Right. . ."
                                                        elif Line == KittyX:
                                                                ch_k "Uh-huh?"
                                                        elif Line == EmmaX:
                                                                ch_e ". . . right. . ."
                                                        elif Line == LauraX:
                                                                ch_l "If you say so."
                                                        elif Line == JeanX:
                                                                ch_j "We will have words. . ."
                                                        elif Line == StormX:
                                                                ch_s "I will remember this. . ."
                                                        elif Line == JubesX:
                                                                ch_v "Riiight."
                                                else:
                                                        #if she's mad
                                                        $ Line.FaceChange("angry")
                                                        $ Line.Statup("Obed", 50, -2)
                                                        $ Line.Statup("Inbt", 60, 3)
                                                        if Line == RogueX:
                                                                ch_r "Damned right you are."
                                                        elif Line == KittyX:
                                                                ch_k "Yeah, right."
                                                        elif Line == EmmaX:
                                                                ch_e "I don't know what you were thinking."
                                                        elif Line == LauraX:
                                                                ch_l "Uh. . . huh."
                                                        elif Line == JeanX:
                                                                ch_j "We will have words. . ."
                                                        elif Line == StormX:
                                                                ch_s "I will remember this. . ."
                                                        elif Line == JubesX:
                                                                ch_v "We will have words."
                                        "Sorry, but I just need some \"me\" time.":
                                                $ ActiveGirls.remove(Line)
                                                $ Line.Statup("Obed", 50, 5)
                                                $ Line.Statup("Obed", 90, 2)
                                                $ Line.Statup("Inbt", 60, 2)
                                                if ApprovalCheck(Line, 900, "L") or ApprovalCheck(Line, 2000):
                                                        #if she accepts it
                                                        $ Line.FaceChange("sadside")
                                                        if Line == RogueX:
                                                                ch_r "I suppose if you do, I can give you some space."
                                                        elif Line == KittyX:
                                                                ch_k "I guess we both could. . ."
                                                        elif Line == EmmaX:
                                                                ch_e "I wouldn't want to be a bother. . ."
                                                        elif Line == LauraX:
                                                                ch_l "I can make myself scarce. . ."
                                                        elif Line == JeanX:
                                                                ch_j "Well, I guess I could find someone else to occupy my time with. . ."
                                                        elif Line == StormX:
                                                                ch_s ". . . fine, I can understand that. . ."
                                                        elif Line == JubesX:
                                                                ch_v "Ok, whatever, I have things to do."
                                                else:
                                                        #if she's mad
                                                        $ Line.Statup("Love", 90, -5)
                                                        $ Line.FaceChange("angry")
                                                        $ Line.AddWord(1,"angry","angry")
                                                        if Line == RogueX:
                                                                ch_r "Oh, I think you'll be getting it."
                                                        elif Line == KittyX:
                                                                ch_k "Yeah, \"me\" too, I guess!"
                                                        elif Line == EmmaX:
                                                                ch_e "I do have other things with which to occupy myself."
                                                        elif Line == LauraX:
                                                                ch_l "I'm busy too."
                                                        elif Line == StormX:
                                                                ch_s "Oh, you shall get it. . ."
                                                        elif Line == JubesX:
                                                                ch_v "We will have words."
                                        "You heard me.":
                                                $ ActiveGirls.remove(Line)
                                                $ Line.Statup("Love", 80, -5)
                                                $ Line.Statup("Love", 90, -5)
                                                $ Line.Statup("Obed", 80, 5)
                                                if ApprovalCheck(Line, 850, "O") or ApprovalCheck(Line, 1500, "LO"):
                                                        #if she accepts it
                                                        $ Line.FaceChange("sadside")
                                                        $ Line.Statup("Obed", 200, 10)
                                                else:
                                                        #if she's mad
                                                        $ Line.FaceChange("angry")
                                                        $ Line.Statup("Love", 90, -5)
                                                        $ Line.Statup("Inbt", 60, 5)
                                                        $ Line.AddWord(1,"angry","angry")
                                                if Line == RogueX:
                                                        ch_r "Loud and clear."
                                                elif Line == KittyX:
                                                        ch_k ". . ."
                                                elif Line == EmmaX:
                                                        ch_e "I suppose I did."
                                                elif Line == LauraX:
                                                        ch_l "If you say so."
                                                elif Line == JeanX:
                                                        ch_j "Noted. . ."
                                                elif Line == StormX:
                                                        ch_s "Like thunder. . ."
                                                elif Line == JubesX:
                                                        ch_v "We will have words."
                                    #end "picked same girl
                            else:
                                    #if she is not in the room
                                    $ ActiveGirls.remove(Line)
                    if Line == GirlX:
                        call AnyLine(GirlX,"Did you forget that I'm your escape plan?")
                        menu:
                            "Oh. . .":
                                    ch_x "I'll forget you asked."
                                    $ Count = 0
                    $ Line = 0
            #end "remove girl"

            "I wanted to bring a girl back in. . ." if len(TotalGirls) > len (ActiveGirls):
                    "This will bring the girl back into active play."
                    "You can always ask to send her away again later."
                    $ Line = 0
                    menu:
                        ch_p "Could you bring back. . ."
                        "[RogueX.Name]" if RogueX not in ActiveGirls and RogueX in TotalGirl:
                                $ Line = RogueX
                        "[KittyX.Name]" if KittyX not in ActiveGirls and KittyX in TotalGirls and "met" in KittyX.History:
                                $ Line = KittyX
                        "[EmmaX.Name]" if EmmaX not in ActiveGirls and EmmaX in TotalGirls and "met" in EmmaX.History:
                                $ Line = EmmaX
                        "[LauraX.Name]" if LauraX not in ActiveGirls and LauraX in TotalGirls and "met" in LauraX.History and "dress0" not in LauraX.History:
                                #Laura has a special condition because of her introduction story
                                $ Line = LauraX
                        "[JeanX.Name]" if JeanX not in ActiveGirls and JeanX in TotalGirls and "met" in JeanX.History:
                                $ Line = JeanX
                        "[StormX.Name]" if StormX not in ActiveGirls and StormX in TotalGirls and "met" in StormX.History:
                                $ Line = StormX
                        "[JubesX.Name]" if JubesX not in ActiveGirls and JubesX in TotalGirls and "met" in JubesX.History:
                                $ Line = JubesX
                        "Never mind. . .":
                                $ Count += 1
                    if Line:
                            #if you picked someone. . .
                            ch_x "Certainly. I've kept her busy, but I can let her off the hook. . ."
                            ch_x "She should have more free time now. . ."
                            $ ActiveGirls.append(Line)
                    $ Line = 0
            "In was interested in a key. . . ":
                menu:
                    "Give me the key to your study." if "Xavier" not in Keys:
                            ch_x "Fine, take it. . ."
                            $ Keys.append("Xavier")
                    "Give me the key to your study.[[Owned] (locked)" if "Xavier" in Keys:
                            pass

                    "Give me the key to [GirlX.Name]'s room." if GirlX not in Keys:
                            ch_x "I. . . suppose I could do that. . ."
                            $ Keys.append(GirlX)
                    "Give me the key to [GirlX.Name]'s room.[[Owned] (locked)" if GirlX in Keys:
                            pass

                    "Never mind the keys.":
                            $ Count += 1
            "That should do it.":
                $ Count = 0

    ch_x "Very well, that should conclude our business. Please leave."
    if GirlX == RogueX:
            if "Omega" not in Player.Traits:
                    $ GirlX.Statup("Lust", 90, 10)
                    $ GirlX.Statup("Love", 70, 30)
                    $ GirlX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Omega")
            ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here."
            $ GirlX.Arms = "gloves"
            $ GirlX.ArmPose = 1
    elif GirlX == KittyX:
            if "Kappa" not in Player.Traits:
                    $ GirlX.Statup("Lust", 90, 10)
                    $ GirlX.Statup("Inbt", 80, 10)
                    $ GirlX.Statup("Love", 70, 10)
                    $ GirlX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Kappa")
            $ GirlX.ArmPose = 0
    elif GirlX == EmmaX:
            ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here."
            if "Psi" not in Player.Traits:
                    $ GirlX.Statup("Lust", 90, 10)
                    $ GirlX.Statup("Inbt", 80, 10)
                    $ GirlX.Statup("Love", 70, 10)
                    $ GirlX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Psi")
    elif GirlX == LauraX:
            if "Chi" not in Player.Traits:
                    $ GirlX.Statup("Lust", 90, 10)
                    $ GirlX.Statup("Inbt", 80, 10)
                    $ GirlX.Statup("Love", 70, 10)
                    $ GirlX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Chi")
            $ GirlX.ArmPose = 1
            $ GirlX.Claws = 0
    elif GirlX == JeanX:
            ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here."
            if "Alpha" not in Player.Traits:
                    $ GirlX.Statup("Lust", 70, 20)
                    $ GirlX.Statup("Lust", 90, 10)
                    $ GirlX.Statup("Inbt", 80, 10)
                    $ GirlX.Statup("Obed", 70, 10)
                    $ GirlX.Statup("Obed", 200, 20)
                    $ GirlX.Statup("Love", 70, 10)
                    $ GirlX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Alpha")
    elif GirlX == StormX:
            if "Rho" not in Player.Traits:
                    $ GirlX.Statup("Lust", 90, 10)
                    $ GirlX.Statup("Inbt", 80, 10)
                    $ GirlX.Statup("Love", 70, 10)
                    $ GirlX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Rho")
    elif GirlX == JubesX:
            if "Zeta" not in Player.Traits:
                    $ GirlX.Statup("Lust", 90, 10)
                    $ GirlX.Statup("Inbt", 80, 10)
                    $ GirlX.Statup("Love", 70, 10)
                    $ GirlX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Zeta")
            $ GirlX.ArmPose = 0

    $ Player.DailyActions.append("Xavier")
    call Remove_Girl("All")
    hide Professor
    $ bg_current = "bg player"
    call Set_The_Scene
    "You return to your room"
    jump Misplaced

# end Caught / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Start Caught Changing/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Caught_Changing(Girl=0): #rkeljsv
        if Girl not in TotalGirls:
                return
        call Shift_Focus(Girl)
        $ D20 = renpy.random.randint(1, 20)

        $ Girl.FaceChange("surprised", 1,Mouth="kiss")
        call Remove_Girl("All")

        if D20 > 17:
                #She's naked
                $ Girl.OutfitChange("nude")
        else:
                #restore base outfit
                $ Girl.OutfitChange(6)
                if D20 >15:
                        #She's bottomless
                        $ Girl.Legs = 0 #Legs
                        $ Girl.Hose = 0 #Hose
                        $ Girl.Panties = 0 #Panties
                elif D20 >14:
                        #She's Topless
                        $ Girl.Chest = 0 #Over
                        $ Girl.Over = 0 #Chest
                elif D20 >10:
                        #She's in her underwear
                        $ Girl.Over = 0 #Over
                        $ Girl.Legs = 0 #Legs
                elif D20 >5:
                        #She's wearing pants/skirt but no shirt
                        $ Girl.Over = 0 #Over
        #else: #fully dressed
        $ Girl.Loc = bg_current
        call Set_The_Scene(Dress=0)
        if D20 > 17:
                #She's naked
                "As you enter the room, you see [Girl.Name] is naked, and seems to be getting dressed."
        elif D20 >14:
                #She's Topless
                "As you enter the room, you see [Girl.Name] is practically naked, and seems to be getting dressed."
        elif D20 >10:
                #She's in her underwear
                "As you enter the room, you see [Girl.Name] is in her underwear, and seems to be getting dressed."
        elif D20 >5:
                #She's wearing pants/skirt
                "As you enter the room, you see [Girl.Name] has her top off, and seems to be getting dressed."
        else:
                #She's done
                "As you enter the room, you see [Girl.Name] has just pulled her top on, and seems to have been getting dressed."

        if Girl == StormX:
                ch_s "Oh, hello, [Girl.Petname]."
        elif ApprovalCheck(Girl, 1400):
                if Girl == RogueX:
                        ch_r "Oh, hey."
                elif Girl == KittyX:
                        ch_k "Hey, [Girl.Petname]."
                elif Girl == EmmaX:
                        ch_e "Oh, here for the view?"
                elif Girl == LauraX:
                        ch_l "Hey."
                elif Girl == JeanX:
                        ch_j "Oh, [Girl.Petname]?"
                elif Girl == JubesX:
                        ch_v "Yo."
        else:
                if D20 > 5:
                        if not ApprovalCheck(Girl, (D20 *70)) and (not Girl.SeenPussy or not Girl.SeenChest):
                                # if D20*70 is less than her approval, and this is the first you've seen of her bits. . .
                                $ Girl.FaceChange("surprised",Brows="angry")
                                $ Girl.Statup("Love", 80, -50)

                                if not Girl.OverNum() or (Girl.OverNum()+Girl.ChestNum() <5) or (Girl.PantsNum() < 5 and Girl.HoseNum() < 10):
                                    # if either she is mostly topless or mostly bottomless)

                                    call expression Girl.Tag + "_First_Bottomless" pass (1)
                                    call first_topless(Girl, silent = 1)
                                    $ Girl.Over = "towel"
                                    "She grabs a towel and covers up."
                        else:
                                #She's cool with it, but confused.
                                $ Girl.FaceChange("surprised", 1,Brows = "confused")
                                if "exhibitionist" in Girl.Traits:
                                    $ Girl.Statup("Lust", 200, (2*D20))
                                else:
                                    $ Girl.Statup("Lust", 200, D20)
                                if D20 > 17:
                                        call expression Girl.Tag + "_First_Bottomless"
                                        call first_topless(Girl, silent = 1)
                                elif D20 > 15:
                                        call expression Girl.Tag + "_First_Bottomless"
                                elif D20 > 14:
                                        call first_topless(Girl)
                        $ Girl.Statup("Inbt", 70, 20)


                        if Girl == RogueX:
                                ch_r "Hey! Learn to knock maybe?!"
                        elif Girl == KittyX:
                                ch_k "Why didn't you knock?!"
                        elif Girl == EmmaX:
                                ch_e "Did you consider knocking?"
                        elif Girl == LauraX:
                                ch_l "Didn't think about knocking?"
                        elif Girl == JeanX:
                                ch_j "Forget to knock, [JeanX.Petname]?"
                        elif Girl == JubesX:
                                ch_v "Hey, knock maybe?"
                        menu:
                            extend ""
                            "Sorry, I should have knocked.":
                                    $ Girl.Statup("Love", 50, 2)
                                    $ Girl.Statup("Love", 80, 4)
                            "And miss the view?":
                                    $ Girl.Statup("Obed", 50, 2)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 1)
                        #end if she's partially nude
                else:
                        #She's fully dressed
                        if not ApprovalCheck(Girl, 800) and (not Girl.SeenPussy or not Girl.SeenChest):
                                $ Girl.FaceChange("angry",Brows="confused")
                                $ Girl.Statup("Love", 80, -5)
                        else:
                                $ Girl.FaceChange("sexy",Brows="confused")
                        $ Girl.Statup("Inbt", 50, 3)

                        if Girl == RogueX:
                                ch_r "Well hello there, [Girl.Petname]. Hoping to see something more?"
                        elif Girl == KittyX:
                                ch_k "Hey, [Girl.Petname]. . . {i}you{/i} were hoping I'd be naaaked."
                        elif Girl == EmmaX:
                                ch_e "Were you hoping to catch me in a compromising position?."
                        elif Girl == LauraX:
                                ch_l "Hey, [Girl.Petname]. Trying to catch a peek?"
                        elif Girl == JeanX:
                                ch_j "Oh, [Girl.Petname]. Hoping to catch me dressing again?"
                        elif Girl == JubesX:
                                ch_v "Hey, [Girl.Petname]. Hoping to catch me naked again?"

                        menu:
                            extend ""
                            "Sorry, I should have knocked.":
                                    $ Girl.Statup("Love", 50, 2)
                                    $ Girl.Statup("Love", 80, 2)
                            "Well, to be honest. . .":
                                    $ Girl.Statup("Love", 50, -2)
                                    $ Girl.Statup("Obed", 50, 2)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 1)
                $ Girl.FaceChange("sexy")
                if ApprovalCheck(Girl, 1000):
                        #she flashes you
                        if Girl == RogueX:
                                ch_r "You could have just asked, [RogueX.Petname]."
                        elif Girl == KittyX:
                                ch_k "I didn't say that I {i}minded{/i}. . ."
                        elif Girl == EmmaX:
                                ch_e "That does show initiative. . ."
                        elif Girl == LauraX:
                                ch_l "I don't mind."
                        elif Girl == JeanX:
                                ch_j "Well, give the audience what it wants. . ."
                        elif Girl == JubesX:
                                ch_v "You just have to ask. . ."

                        $ Girl.Uptop = 1 #Uptop up
                        $ Girl.Upskirt = 1 #Upskirt up
                        pause 1
                        call first_topless(Girl, silent = 1)
                        call expression Girl.Tag + "_First_Bottomless" pass (1)
                        $ Girl.Uptop = 0 #Uptop up
                        $ Girl.Upskirt = 0 #Upskirt up
                        "She flashes you real quick."
                else:
                        #if she doesn't flash you
                        if Girl == RogueX:
                                ch_r "Well, it happens, just be careful next time."
                        elif Girl == KittyX:
                                ch_k "Yeah. . . we wouldn't want any accidents. . ."
                        elif Girl == EmmaX:
                                ch_e "Hmm, show a bit more care next time. . ."
                        elif Girl == LauraX:
                                ch_l "Uh-huh . . ."
                        elif Girl == JeanX:
                                ch_j "Sure, perv."
                        elif Girl == JubesX:
                                ch_v "Don't be sneaking around."
                #end "if she isn't into you."
        if Girl == RogueX:
                ch_r "Well, are you planning to stick around?"
        elif Girl == KittyX:
                ch_k "So were you planning on staying?"
        elif Girl == EmmaX:
                ch_e "Did you have business with me?"
        elif Girl == LauraX:
                ch_l "So did you plan to stay?"
        elif Girl == JeanX:
                ch_j "So, what did you want?"
        elif Girl == StormX:
                ch_s "Was there something I could help you with?"
        elif Girl == JubesX:
                ch_v "Did you want something?"
        menu:
                extend ""
                "Sure, for a bit.":
                        pass

                "Actually, I should get going. . .":
                        $ Girl.OutfitChange(6,Changed=0)
                        $ renpy.pop_call()
                        call Worldmap

        if Girl == StormX and D20 >5:
            #she's at least partly nude
            ch_s "Ok, then let me finish getting dressed. . ."
            menu:
                "Ok.":
                                "She finishes getting changed."
                                $ Girl.OutfitChange(6,Changed=0)
                "Actually, you could leave them off.":
                        if ApprovalCheck(Girl, 350+(10*D20)): #400-550
                                $ Girl.Statup("Love", 70, 3)
                                $ Girl.Statup("Obed", 50, 1)
                                $ Girl.Statup("Obed", 80, 2)
                                $ Girl.Statup("Inbt", 60, 2)
                                $ Girl.FaceChange("sexy")
                                ch_s "I suppose that could not hurt. . ."
                                $ Girl.Set_Temp_Outfit() #sets current outfit as temporary
                        else:
                                $ Girl.Statup("Inbt", 60, 2)
                                $ Girl.FaceChange("smile")
                                ch_s "Ha! I would not want to be too much of a distraction."
                                $ Girl.OutfitChange(6,Changed=0)
                "Why not lose the rest too?":
                        $ Girl.FaceChange("sexy")
                        if ApprovalCheck(Girl, 700):
                                $ Girl.Statup("Love", 50, 1)
                                $ Girl.Statup("Love", 70, 1)
                                $ Girl.Statup("Obed", 50, 1)
                                $ Girl.Statup("Obed", 80, 1)
                                $ Girl.Statup("Inbt", 70, 1)
                                ch_s "Oh, you are a naughty one. . ."
                                $ Girl.OutfitChange("nude")
                                $ Girl.Set_Temp_Outfit() #sets current outfit as temporary
                        elif ApprovalCheck(Girl, 350+(10*D20)): #400-550
                                $ Girl.Statup("Love", 80, 1)
                                $ Girl.Statup("Obed", 50, 1)
                                $ Girl.Statup("Obed", 80, 1)
                                $ Girl.Statup("Inbt", 70, 2)
                                ch_s "I could at least. . . pause for a moment?"
                                $ Girl.Set_Temp_Outfit() #sets current outfit as temporary
                        else:
                                $ Girl.Statup("Love", 60, 1)
                                $ Girl.Statup("Obed", 50, 2)
                                $ Girl.Statup("Inbt", 70, 1)
                                ch_s "You are joking, [Girl.Petname]."
                                $ Girl.OutfitChange(6,Changed=0)
                "Don't, stay like that.":
                        $ Girl.Statup("Obed", 80, 2)
                        if ApprovalCheck(Girl,1100):
                                $ Girl.Statup("Obed", 50, 2)
                                $ Girl.Statup("Inbt", 60, 1)
                                $ Girl.FaceChange("sexy")
                                ch_s "If you want. . ."
                                $ Girl.Set_Temp_Outfit() #sets current outfit as temporary
                        elif ApprovalCheck(Girl, 350+(10*D20)) and ApprovalCheck(Girl, 400, "O"):
                                $ Girl.Statup("Love", 50, -2)
                                $ Girl.Statup("Love", 80, -1)
                                $ Girl.Statup("Obed", 50, 2)
                                $ Girl.FaceChange("sexy",Eyes="side")
                                ch_s ". . . Very well."
                                $ Girl.Set_Temp_Outfit() #sets current outfit as temporary
                        else:
                                $ Girl.Statup("Love", 80, -2)
                                $ Girl.Statup("Obed", 50, -1)
                                $ Girl.FaceChange("angry")
                                ch_s "You do not decide that, [Girl.Petname]."
                                $ Girl.OutfitChange(6,Changed=0)
                "Lose the rest of it.":
                        $ Girl.Statup("Obed", 80, 2)
                        if ApprovalCheck(Girl,1300):
                                $ Girl.Statup("Obed", 50, 2)
                                $ Girl.Statup("Inbt", 60, 1)
                                $ Girl.FaceChange("sexy")
                                ch_s "Fine. . ."
                                $ Girl.OutfitChange("nude")
                                $ Girl.Set_Temp_Outfit() #sets current outfit as temporary
                        elif ApprovalCheck(Girl,800) and ApprovalCheck(Girl, 500, "O"):
                                $ Girl.Statup("Love", 50, -2)
                                $ Girl.Statup("Love", 80, -2)
                                $ Girl.Statup("Obed", 50, 2)
                                $ Girl.Statup("Obed", 80, 1)
                                $ Girl.FaceChange("sexy",Eyes="side")
                                ch_s ". . . Fine."
                                $ Girl.OutfitChange("nude")
                                $ Girl.Set_Temp_Outfit() #sets current outfit as temporary
                        else:
                                $ Girl.Statup("Love", 50, -2)
                                $ Girl.Statup("Love", 80, -2)
                                $ Girl.Statup("Obed", 50, -2)
                                $ Girl.Statup("Obed", 80, 2)
                                $ Girl.FaceChange("angry")
                                ch_s "I do not think that I will, [Girl.Petname]."
                                $ Girl.OutfitChange(6,Changed=0)
        return
#End Girl Caught Changing


label Girl_Caught_Mastubating(Girl=0): #rkeljsv
        #called by room entry dialog if the girl was masturbating
        if Girl not in TotalGirls:
            return
        $ Girl.DrainWord("gonnafap")
        call Remove_Girl("All")
        $ Girl.Loc = bg_current
        "As you approach her room, you hear soft moans from inside, and notice that the door is slightly ajar."
        menu:
            extend ""
            "Knock politely":
                $ Line = "knock"
            "Peek inside":
                call Set_The_Scene
                $ Girl.FaceChange("kiss",1,Eyes = "closed")
                $ Trigger = "masturbation"
                $ Trigger3 = "fondle pussy"
                "You see [Girl.Name], eyes closed and stroking herself vigorously."
                menu:
                    extend ""
                    "Enter Quietly":
                            $ Line = "enter"
                    "Pull back and knock":
                            $ Line = "knock"
                    "Leave quietly":
                            $ Line = "leave"
            "Enter quietly":
                    $ Line = "enter"
                    "You hear some odd noises coming from [Girl.Name]'s room as you enter."
            "Leave quietly":
                    $ Line = "leave"

        if Line == "leave":
                $ Girl.Statup("Lust", 80, 20)
                "You leave [Girl.Name] to her business and slip out."
                $ renpy.pop_call()
                jump Campus_Map
        elif Line == "knock":
                "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                "After several seconds and some more shuffling of clothing, [Girl.Name] comes to the door."
                $ Girl.FaceChange("confused",1,Eyes = "surprised",Mouth = "smile")
                $ Trigger = 0
                $ Trigger3 = 0
                call Set_The_Scene
                if Girl == RogueX:
                        ch_r "Sorry about that [RogueX.Petname], I was. . . working out."
                elif Girl == KittyX:
                        ch_k "Oh, hey, [KittyX.Petname], I was. . . never mind."
                elif Girl == EmmaX:
                        ch_e "Well, I suppose you could tell I was a bit. . . occupied."
                elif Girl == LauraX:
                        ch_l "Um, hey [LauraX.Petname], just working off some stress."
                elif Girl == JeanX:
                        ch_j "Oh, [JeanX.Petname]. I was. . . never mind."
                elif Girl == StormX:
                        ch_s "Oh, um, [StormX.Petname]. I was just. . . stretching."
                elif Girl == JubesX:
                        ch_v "Oh, hey, [Girl.Petname]. . . I was. . ."
                $ temp_modifier += 10
        elif Line == "enter":
                call Shift_Focus(Girl)
                show blackscreen onlayer black
                $ Girl.Upskirt = 1
                $ Girl.PantiesDown = 1
                $ Girl.Loc = bg_current
                #call CleartheRoom(Girl,1,1)
                call Set_The_Scene
                $ Girl.FaceChange("sexy")
                $ Girl.Eyes = "closed"
                $ Girl.ArmPose = 2
                $ Count = 0
                $ Trigger = "masturbation"
                hide blackscreen onlayer black
                $ Girl.DailyActions.append("unseen")
                $ Girl.RecentActions.append("unseen")
                call expression Girl.Tag + "_SexAct" pass ("masturbate")
                if "angry" in Girl.RecentActions:
                        return

                #After caught masturbating. . .
                $ Girl.FaceChange("sexy",Brows="confused")
                if Girl.Mast == 1:
                        if Girl == RogueX:
                                ch_r "Well that was a bit unexpected. . ."
                                $ Girl.FaceChange("bemused",Eyes="side")
                                ch_r "but not exactly unpleasant. . ."
                                $ Girl.FaceChange("sexy")
                                ch_r "Maybe next time I'll give you a heads up first."
                        elif Girl == KittyX:
                                ch_k "So[KittyX.like]I wasn't expecting company. . ."
                                $ Girl.FaceChange("bemused",Eyes="side")
                                ch_k "but I didn't exactly mind it either. . ."
                                $ Girl.FaceChange("sexy")
                                ch_k "Maybe knock next time?"
                        elif Girl == EmmaX:
                                ch_e "I wasn't expecting visitors. . ."
                                $ Girl.FaceChange("bemused",Eyes="side")
                                ch_e "although for you I could make an exception. . ."
                                $ Girl.FaceChange("sexy")
                                ch_e "Perhaps next time you could knock?"
                        elif Girl == LauraX:
                                ch_l "So what are you doing here? . ."
                                $ Girl.FaceChange("bemused",Eyes="side")
                                ch_l "not that I mind the company. . ."
                                $ Girl.FaceChange("sexy")
                                ch_l "But you know, give me a heads up first."
                        elif Girl == JeanX:
                                $ Girl.FaceChange("bemused",Eyes="side")
                                ch_j "Well that was fun. . ."
                                $ Girl.FaceChange("sexy")
                                ch_j "So what brings you here? . ."
                        elif Girl == StormX:
                                ch_s "That was an interesting experience. . ."
                                $ Girl.FaceChange("bemused",Eyes="side")
                                ch_s "I certainly didn't mnd the attention. . ."
                                $ Girl.FaceChange("sexy")
                                ch_s "You might want to knock in future though."
                        elif Girl == JubesX:
                                ch_v "I don't usually get unexpected visitors . ."
                                $ Girl.FaceChange("bemused",Eyes="side")
                                ch_v "but I didn't mind the company. . ."
                                $ Girl.FaceChange("sexy")
                                ch_v "Maybe knock next time?"
                else:
                        if Girl == RogueX:
                                ch_r "Fancy seeing you here again, [Girl.Petname]. Almost like it was intentional. . ."
                        elif Girl == KittyX:
                                ch_k "You seem to be making a habit of dropping in."
                        elif Girl == EmmaX:
                                ch_e "I notice you make a habit of dropping in."
                        elif Girl == LauraX:
                                ch_l "You're around a lot. . ."
                        elif Girl == JeanX:
                                ch_j "You have a habit of dropping by. . ."
                        elif Girl == StormX:
                                ch_s "You come up here fairly often. . ."
                        elif Girl == JubesX:
                                ch_v "You stop by alot. . ."

                $ Girl.ArmPose = 1
                $ Girl.OutfitChange(Changed=0)
                #end "if you entered"
        return

#end girls caught masturbating / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
