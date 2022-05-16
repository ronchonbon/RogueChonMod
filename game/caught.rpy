label Girls_Caught_Lesing(Girl=0,Girl2=0,Girls=[]): #rkeljsv
        #called by room entry dialog if the girls were lesing

        $ Girls = active_Girls[:]
        if Girl in all_Girls:
                $ Girls.remove(Girl)
        while Girls and not Girl:
                if Girls[0] not in Party and Girls[0].location == bg_current and "les" in Girls[0].recent_history:
                        # if this girl is not already the focal girl, is at the current location but not in a party,
                        # and was queued for a les action, set her up as girl 1.
                        $ Girl = Girls[0]
                        $ Girls = [1]
                $ Girls.remove(Girls[0])
        if Girl and not Girl2:
                #if a Girl was either offered or produced by first loop. . .
                $ Girls = active_Girls[:]
                $ Girls.remove(Girl)
                while Girls:
                        if Girls[0] not in Party and Girls[0].location == bg_current and "les" in Girls[0].recent_history:
                                # if this girl is not already the focal girl, is at the current location but not in a party,
                                # and was queued for a les action, set her up as girl 2.
                                $ Girl2 = Girls[0]
                                $ Girls = [1]
                        $ Girls.remove(Girls[0])

        if not Girl or not Girl2:
                return 1

        $ Girl.DrainWord("les",1,0) #removes general "les" tag from recent actions
        $ Girl2.DrainWord("les",1,0) #removes general "les" tag from recent actions

        $ Girl.AddWord(0,"lesbian","lesbian")  #adds "lesbian" tag to recent and daily actions
        $ Girl2.AddWord(0,"lesbian","lesbian")  #adds "lesbian" tag to recent and daily actions
        $ Girl.AddWord(1,0,0,0,"les "+Girl2.Tag)  #adds "les Rogue" tag to recent actions
        $ Girl2.AddWord(1,0,0,0,"les "+Girl.Tag)  #adds "les Kitty" tag to recent actions

        "As you approach her room, you hear soft moans from inside, and notice that the door is slightly ajar."
        $ line = 0
        while not line:
            menu:
                extend ""
                "Knock politely":
                        "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                        "After several seconds and some more shuffling of clothing, [Girl.name] comes to the door."
                        $ Girl.change_face("confused",2,Eyes = "surprised",Mouth = "smile")
                        $ Girl2.change_face("confused",2,Eyes = "surprised",Mouth = "smile")
                        $ primary_action = 0
                        $ girl_offhand_action = 0
                        $ second_girl_primary_action = 0
                        $ second_girl_offhand_action = 0
                        call set_the_scene
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
                                ch_j "Hey [Girl.Petname], we were just giving [Girl2.name]'s tongue a workout."
                        elif Girl == StormX:
                                ch_s "Ah, hello, [Girl.Petname] . . I was having a. . . chat with [Girl2.name]. . ."
                        elif Girl == JubesX:
                                ch_v "Oh, hey. . . me and [Girl2.name] were just. . . having some fun."
                        $ Girl.change_face("smile",1)
                        $ Girl2.change_face("smile",1)
                        $ temp_modifier += 10
                        $ line = 1
                "Peek inside":
                        call set_the_scene
                        $ Girl.change_face("kiss",1,Eyes = "closed")
                        $ Girl2.change_face("kiss",1,Eyes = "closed")
                        $ primary_action = "lesbian"
                        $ girl_offhand_action = "fondle_pussy"
                        $ second_girl_primary_action = "fondle_pussy"
                        "You see [Girl.name] and [Girl2.name], eyes closed and stroking each other vigorously."
                "Enter quietly":
                        call set_the_scene(Quiet=1)
                        $ Girl.change_face("kiss",1,Eyes = "closed")
                        $ Girl2.change_face("kiss",1,Eyes = "closed")
                        $ primary_action = "lesbian"
                        $ girl_offhand_action = "fondle_pussy"
                        $ second_girl_primary_action = "fondle_pussy"
                        $ Girl.AddWord(1,"unseen","unseen")
                        $ Girl2.AddWord(1,"unseen","unseen")
                        $ Partner = Girl2
                        $ line = 0
                        call sex_acts("lesbian") #call Rogue_SexAct("lesbian")
                "Leave quietly":
                        "You leave the girls to their business and slip out."
                        $ Girl.Thirst -= 30
                        $ Girl.lust = 20
                        $ Girl2.Thirst -= 30
                        $ Girl2.lust = 20
                        $ renpy.pop_call()
                        jump Campus_Map
        $ line = 0
        return

label Girl_Caught_Shower(Girl=0): #rkeljsv
        if Girl not in all_Girls:
                return
        call shift_focus(Girl)

        $ Options = []
        $ Girl.AddWord(1,"showered","showered",0,0)
        call remove_girl("all")

        $ Girl.OutfitChange("nude")
        $ Girl.change_face("smile",1)

        $ Girl.location = "bg_showerroom"
        $ Girl.Water = 1
        $ Girl.Wet = 2

        if "gonnafap" in Girl.daily_history:
                "As you approach the showers, you hear some shallow moans from inside."
        else:
                "As you approach the showers, you hear some humming noises from inside."
        menu:
                "What do you do?"
                "Enter":
                    pass
                "Knock":
                    $ line = "knock"
                "Come back later":
                    call remove_girl(Girl)
                    $ Girl.OutfitChange(6) #dresses her
                    $ Girl.DrainWord("gonnafap",0,1) #removes "gonnafap" tag from daily
                    $ Girl.lust = 25
                    $ Girl.Thirst -= int(Girl.Thirst/2) if Girl.Thirst >= 50 else int(Girl.Thirst/4)
                    $ bg_current = "bg_campus"
                    jump Misplaced

        if line == "knock":
                #You knock
                "You knock on the door. You hear some shuffling inside"
                $ Girl.Over = "towel"
                if "gonnafap" in Girl.daily_history:
                        #Girl caught fapping
                        "You hear a sharp shuffling sound and the water gets cut off."
                        "After several seconds and some more shuffling, [Girl.name] comes to the door."
                        $ Girl.change_face("perplexed",2,Mouth="normal")
                        call set_the_scene(check_if_dressed=0)
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
                        $ Girl.change_stat("lust", 90, 5)
                        $ temp_modifier += 10
                else:
                        #Laura caught showering
                        "You hear the rustling of a towel and some knocking around, but after a few seconds [Girl.name] comes to the door."
                        call set_the_scene(check_if_dressed=0)
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
            if "gonnafap" in Girl.daily_history:
                    #Caught masturbating in the shower.
                    $ Girl.DrainWord("gonnafap",0,1) #removes "gonnafap" tag from daily
                    $ Girl.change_face("sexy",Eyes="closed")
                    $ Girl.AddWord(1,"unseen","unseen",0,0)
                    call set_the_scene(check_if_dressed=0)
                    $ Count = 0
                    $ primary_action = "masturbation"
                    $ girl_offhand_action = "fondle_pussy"
                    "You see [Girl.name] under the shower, feeling herself up."
                    call sex_acts("masturbation") #call Laura_SexAct("masturbation")
                    $ bg_current = "bg_showerroom"
                    jump Misplaced

            elif D20 >= 15:
                    #She's just showering and naked
                    call set_the_scene(check_if_dressed=0)
                    $ Girl.change_face("surprised", 1)
                    "As you enter the showers, you see [Girl.name] washing up."
                    call first_bottomless(Girl, 1)
                    call first_topless(Girl, silent = 1)
                    if not Approvalcheck(Girl, 1200) or not Girl.SeenPussy or not Girl.SeenChest:
                            $ Girl.Brows="angry"
                            $ Girl.Over = "towel"
                            "She grabs a towel and covers up."
                            $ Girl.change_face("angry", 1)
                            $ Girl.change_stat("love", 80, -5)
                    else:
                            if "exhibitionist" in Girl.Traits:
                                $ Girl.change_stat("lust", 90, (2*D20))
                            else:
                                $ Girl.change_stat("lust", 80, D20)
                            $ Girl.Brows="confused"

                    $ Girl.change_stat("inhibition", 70, 3)
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
                                    $ Girl.change_stat("love", 50, 2)
                                    if Girl != StormX:
                                            $ Girl.change_stat("love", 80, 4)
                            "And miss the view?":
                                    $ Girl.change_stat("obedience", 50, 2)
                                    if Girl != StormX:
                                            $ Girl.change_stat("obedience", 80, 2)
                                            $ Girl.change_stat("inhibition", 60, 1)
                            "Why, would it have made a difference?":
                                    if not Approvalcheck(Girl, 500,"I"):
                                            $ Girl.change_stat("love", 50, -3)
                                            $ Girl.change_stat("obedience", 50, 2)
                                    $ Girl.change_stat("obedience", 80, 2)
                                    $ Girl.change_stat("inhibition", 60, 2)
                            "It's not as if you're leaving that much to the imagination. . ." if Girl == EmmaX:
                                    $ EmmaX.change_stat("obedience", 50, 2)
                                    $ EmmaX.change_stat("obedience", 80, 2)
                                    $ EmmaX.change_stat("inhibition", 60, 2)
                    #end caught showering naked

            else:
                    #She's done showering and in a towel
                    $ Girl.Over = "towel"
                    call set_the_scene(check_if_dressed=0)
                    "As you enter the showers, you see [Girl.name] putting on a towel."
                    if not Approvalcheck(Girl, 1100) and (not Girl.SeenPussy or not Girl.SeenChest):
                            $ Girl.change_face("angry",Brows="confused")
                            $ Girl.change_stat("love", 80, -5)
                    else:
                            $ Girl.change_face("sexy",Brows="confused")
                    $ Girl.change_stat("inhibition", 50, 3)
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
                                    $ Girl.change_stat("love", 50, 2)
                                    if Girl != StormX:
                                            $ Girl.change_stat("love", 80, 2)
                            "Well, to be honest. . .":
                                    $ Girl.change_stat("love", 50, -2)
                                    $ Girl.change_stat("obedience", 50, 2)
                                    if Girl != StormX:
                                            $ Girl.change_stat("obedience", 80, 2)
                                            $ Girl.change_stat("inhibition", 60, 1)
                            "I still like the view. . ." if Girl != EmmaX:
                                if Approvalcheck(Girl, 500,"I"):
                                    $ Girl.change_stat("love", 80, 1)
                                else:
                                    $ Girl.change_stat("love", 50, -1)
                                    $ Girl.change_stat("obedience", 50, 2)
                                $ Girl.change_stat("obedience", 80, 2)
                                $ Girl.change_stat("inhibition", 60, 3)
                            "It's not as if you're leaving that much to the imagination. . ." if Girl == EmmaX:
                                $ EmmaX.change_stat("obedience", 50, 2)
                                $ EmmaX.change_stat("obedience", 80, 2)
                                $ EmmaX.change_stat("inhibition", 60, 2)
                    #end caught in towel

            $ Girl.change_face("sexy")
            if Girl == StormX:
                            ch_s "Oh, that's fine, [Girl.Petname]."
                            ch_s "You might want to be careful with the other girls though."
            elif not Approvalcheck(Girl, 1000) or not Girl.SeenPussy or not Girl.SeenChest:
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
            elif not Approvalcheck(Girl, 1300):
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
                            call first_bottomless(Girl, 1)
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
                    call remove_girl(Girl)
            "Actually, could you stick around a minute?":
                if Approvalcheck(Girl, 900) or Girl == StormX:
                    if Girl == RogueX:
                            ch_r "Sure, what's up?"
                    elif Girl == KittyX:
                            ch_k "Yeah?"
                    elif Girl == EmmaX:
                            ch_e "Very well, what did you need?"
                    elif Girl == LauraX:
                            $ LauraX.location = "bg_showerroom"
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
                    call remove_girl(Girl)

        if line == "leaving":
                $ Girl.OutfitChange(6)
        $ line = 0
        return 0

label Girls_Caught(Girl=0,TotalCaught=0,Shame=0,Count=0,T_Pet=0,Girls=[]): #rkeljsv
    call shift_focus(Girl)
    call checkout
    call Anyline(Girl,"!!!")
    $ line = primary_action
    call Trig_Reset
    $ Girl.OutfitChange()
    $ Girls = all_Girls[:]
    while Girls:
            if Girls[0].location == bg_current:
                    $ Girls[0].location = "bg_study"
            $ TotalCaught += Girls[0].Caught
            $ Girls.remove(Girls[0])
    $ bg_current = "bg_study"
    call set_the_scene(0)
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
    $ Girl.change_face("sad")
    if (Girl == EmmaX or Partner == EmmaX) and (Girl == StormX or Partner == StormX):
            ch_x "I'm very disappointed in the both of you!."
            ch_x "You should GirlsTH know better than this!"
    elif Girl == StormX or Partner == StormX:
            ch_x "I'm very disappointed in your behavior, particularly yours, Ororo."
    elif Girl == EmmaX or Partner == EmmaX:
            ch_x "I'm very disappointed in your behavior, particularly yours, Emma."
    else:
            ch_x "I'm very disappointed in your behavior, the both of you."

    if line == "fondle_thighs" or line == "fondle_breasts" or line == "fondle_pussy" or line == "hotdog" or line == "handjob":
        ch_x "The two of you, feeling each other up like animals!"
    elif line == "dildo_pussy" or line == "dildo_anal":
        ch_x "Using those. . . devices on each other, unsanitary!"
    elif line == "eat_pussy":
        ch_x "Engaging in. . . cunnilingus. . . dripping everywhere. . ."
    elif line == "blowjob":
        ch_x "Right there in public with his {i}penis{/i} in your mouth. . ."
    else:
        ch_x "Having sexual relations in such a public location, it shows very poor Girl of you!"

    if Girl.Shame >= 40:
            ch_x "[Girl.name], my dear, you're practically naked! At least throw a towel on!"
            "He throws [Girl.name] the towel."
            show blackscreen onlayer black
            $ Girls = all_Girls[:]
            while Girls:
                    if Girls[0].location == bg_current and (not Girls[0].Over and not Girls[0].Chest):
                            $ Girls[0].Over = "towel"
                    $ Girls.remove(Girls[0])
            hide blackscreen onlayer black
            if (Girl == StormX or Partner == StormX) and StormX.Over == "towel":
                    ch_x ". . ."
                    ch_x "Ororo, for Girlist's sake. . ."
                    ch_x "Put on some actual clothes!"
                    show blackscreen onlayer black
                    $ StormX.Over = "white shirt"
                    $ StormX.Legs = "skirt"
                    hide blackscreen onlayer black
                    ch_x ". . . fine."

    elif Girl.Shame >= 20:
            ch_x "[Girl.name], my dear, that attire is positively scandalous."

    if Girl.Caught:
            #if Caught for Girl > 0
            "And this isn't even the first time this has happened!"

    if Partner:
            $ Partner.change_face("surprised",2)
            if Partner in Rules:
                    if Partner == KittyX:
                        "Xavier glances over at [KittyX.name], who just waggles her phone. . ."
                    elif Partner == LauraX:
                        $ Laura_Arms = 2
                        "Xavier glances over at [LauraX.name], who raises her fist and shakes it. . ."
                        $ Laura_Arms = 1
                    ch_x "And. . .hm, I could have sworn there was someone else. . ."
            else:
                    ch_x "And [Partner.name], you were just watching this occur!"
            $ Partner.change_face("bemused",1, Eyes="side")

    if EmmaX.location == bg_current and EmmaX not in Rules:
        if not EmmaX.Caught:
                ch_x "Emma, you are entrusted as a teacher here, I can't have you fraternizing with the students."
                ch_x "This is especially true in the school's public spaces!"
                ch_x "What sort of message does that send?"
                ch_x "How appropriate would it be if I were to just wander the halls with Miss Grey on my lap?"
                call XavierFace("hypno")
                ch_x "Just. . . running my hands along her firm little body without a care in the world. . ."
                call XavierFace("happy")
                if JeanX.location == bg_current:
                        "You glance over at [JeanX.name], she shrugs."
                ch_x ". . ."
                call XavierFace("shocked")
                ch_x "Yes, well, as I was saying! . ."
        else:
                ch_x "Emma, I don't believe this is the first time we've had this talk."
                ch_x "I should hope it will be the last."
    if StormX.location == bg_current and StormX not in Rules:
        if not StormX.Caught:
                if EmmaX.location == bg_current and EmmaX not in Rules:
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
                if EmmaX.location == bg_current and EmmaX not in Rules:
                        ch_x "And Ororo! We've also been over this before."
                else:
                        ch_x "Ororo, I don't believe this is the first time we've had this talk."
                ch_x "I should hope it will be the last."

    $ line = 0
    menu:
        ch_x "Well what have you to say for yourselves?"
        "Sorry sir, won't do it again.":
                if RogueX.location == bg_current and RogueX.Caught < 3:
                            $ RogueX.change_stat("love", 70, 20)
                            $ RogueX.change_stat("inhibition", 50, -15)
                            $ RogueX.change_stat("love", 90, 5)
                if KittyX.location == bg_current and KittyX.Caught < 3:
                            $ KittyX.change_stat("love", 70, 10)
                            $ KittyX.change_stat("inhibition", 30, -25)
                            $ KittyX.change_stat("inhibition", 50, -10)
                if EmmaX.location == bg_current and EmmaX.Caught < 3:
                            $ EmmaX.change_stat("love", 70, 5)
                            $ EmmaX.change_stat("inhibition", 30, -15)
                if LauraX.location == bg_current and LauraX.Caught < 3:
                            $ LauraX.change_stat("inhibition", 30, -20)
                            $ LauraX.change_stat("inhibition", 50, -10)
                if JeanX.location == bg_current and JeanX.Caught < 3:
                            $ JeanX.change_stat("obedience", 30, -20)
                            $ JeanX.change_stat("obedience", 50, -10)
                if StormX.location == bg_current and StormX.Caught < 3:
                            $ StormX.change_stat("love", 70, 5)
                            $ StormX.change_stat("inhibition", 30, -5)
                if JubesX.location == bg_current and JubesX.Caught < 3:
                            $ JubesX.change_stat("love", 70, 10)
                            $ JubesX.change_stat("obedience", 70, 5)
                            $ JubesX.change_stat("inhibition", 30, -10)
                            $ JubesX.change_stat("inhibition", 50, -5)
                $ Girl.change_stat("obedience", 50, -5)

                call XavierFace("happy")
                if Girl.Caught:
                    ch_x "But you know you've done this before. . . at least [Girl.Caught] times. . ."
                elif Girl == EmmaX and TotalCaught:
                    ch_x "Not with Ms. Frost, perhaps, but you know you've done this before. . ."
                    ch_x "at least [TotalCaught] times. . ."
                    $ Girl.change_face("sexy",Brows="confused")
                elif Girl == StormX and TotalCaught:
                    ch_x "Not with Ms. Munroe, perhaps, but you know you've done this before. . ."
                    ch_x "at least [TotalCaught] times. . ."
                    $ Girl.change_face("sexy",Brows="confused")
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
                $ Girl.namecheck() #checks reaction to petname
                $ Girl.change_face("bemused")
                $ Girl.change_stat("lust", 90, 5)
                if RogueX.location == bg_current and RogueX.Caught < 5:
                        $ RogueX.change_stat("love", 70, 20)
                        $ RogueX.change_stat("love", 90, 10)
                if KittyX.location == bg_current and KittyX.Caught < 5:
                        $ KittyX.change_stat("inhibition", 90, 10)
                        $ KittyX.change_stat("love", 90, 10)
                if EmmaX.location == bg_current and EmmaX.Caught < 5:
                        $ EmmaX.change_stat("inhibition", 90, 10)
                        $ EmmaX.change_stat("love", 90, 10)
                if LauraX.location == bg_current and LauraX.Caught < 5:
                        $ LauraX.change_stat("inhibition", 90, 10)
                        $ LauraX.change_stat("obedience", 90, 5)
                        $ LauraX.change_stat("love", 90, 5)
                if JeanX.location == bg_current and JeanX.Caught < 5:
                        $ JeanX.change_stat("inhibition", 200, 10)
                        $ JeanX.change_stat("obedience", 50, 5)
                        $ JeanX.change_stat("obedience", 90, 5)
                        $ JeanX.change_stat("love", 90, 5)
                if StormX.location == bg_current and StormX.Caught < 5:
                        $ StormX.change_stat("inhibition", 90, 15)
                        $ StormX.change_stat("obedience", 50, 5)
                        $ StormX.change_stat("love", 90, 5)
                if JubesX.location == bg_current and JubesX.Caught < 5:
                        $ JubesX.change_stat("inhibition", 90, 5)
                        $ JubesX.change_stat("obedience", 80, 5)
                        $ JubesX.change_stat("love", 90, 10)

                call XavierFace("angry")
                $ Count += 10
                ch_x "If that's your attitude, harsher methods might be necessary."
                if PunishmentX:
                    ch_x "I'm extending your punishment by [Count] days."
                else:
                    ch_x "I'm halving your daily stipend for [Count] days."

                if RogueX.location == bg_current and RogueX.Caught < 3:
                        $ RogueX.change_stat("obedience", 50, 20)
                        $ RogueX.change_stat("obedience", 90, 20)
                        $ RogueX.change_stat("inhibition", 30, -20)
                        $ RogueX.change_stat("inhibition", 50, -10)
                if KittyX.location == bg_current and KittyX.Caught < 3:
                        $ KittyX.change_stat("obedience", 50, 20)
                        $ KittyX.change_stat("obedience", 90, 20)
                        $ KittyX.change_stat("inhibition", 30, -20)
                if EmmaX.location == bg_current and EmmaX.Caught < 3:
                        $ EmmaX.change_stat("obedience", 50, 20)
                        $ EmmaX.change_stat("obedience", 90, 20)
                        $ EmmaX.change_stat("inhibition", 30, -20)
                if LauraX.location == bg_current and LauraX.Caught < 3:
                        $ LauraX.change_stat("obedience", 50, 20)
                        $ LauraX.change_stat("obedience", 90, 20)
                        $ LauraX.change_stat("inhibition", 30, -20)
                if JeanX.location == bg_current and JeanX.Caught < 3:
                        $ JeanX.change_stat("obedience", 50, 20)
                        $ JeanX.change_stat("obedience", 90, 20)
                if StormX.location == bg_current and StormX.Caught < 3:
                        $ StormX.change_stat("obedience", 50, 20)
                        $ StormX.change_stat("inhibition", 30, -10)
                if JubesX.location == bg_current and JubesX.Caught < 3:
                        $ JubesX.change_stat("obedience", 70, 10)
                        $ JubesX.change_stat("inhibition", 30, -10)

                ch_x "I've had enough of you, begone."
        #End "Little fun"

        "Just this. . . Plan Omega, [RogueX.name]." if Girl == RogueX and Player.Lvl >= 5:
                $ line = "Omega"
        "Just this. . . Plan Kappa, [KittyX.name]!" if Girl == KittyX and Player.Lvl >= 5:
                $ line = "Kappa"
        "Just this. . . Plan Psi, [EmmaX.name]!" if Girl == EmmaX and Player.Lvl >= 5:
                $ line = "Psi"
        "Just this. . . Plan Chi, [LauraX.name]!" if Girl == LauraX and Player.Lvl >= 5:
                $ line = "Chi"
        "Just this. . . Plan Alpha, [JeanX.name]!" if Girl == JeanX and Player.Lvl >= 5:
                $ line = "Alpha"
        "Just this. . . Plan Rho, [StormX.name]!" if Girl == StormX and Player.Lvl >= 5:
                $ line = "Rho"
        "Just this. . . Plan Zeta, [JubesX.name]!" if Girl == JubesX and Player.Lvl >= 5:
                $ line = "Zeta"
        #End "Plan X"


        "You can suck it, old man.":
                $ Girl.change_face("surprised")
                $ Girl.change_stat("lust", 90, 10)
                if RogueX.location == bg_current and RogueX.Caught < 3:
                        $ RogueX.change_stat("obedience", 50, 20)
                        $ RogueX.change_stat("obedience", 90, 40)
                if KittyX.location == bg_current and KittyX.Caught < 3:
                        $ KittyX.change_stat("obedience", 50, 25)
                        $ KittyX.change_stat("obedience", 90, 40)
                if EmmaX.location == bg_current and EmmaX.Caught < 3:
                        $ EmmaX.change_stat("love", 90, 5)
                        $ EmmaX.change_stat("obedience", 50, 20)
                        $ EmmaX.change_stat("obedience", 90, 30)
                if LauraX.location == bg_current and LauraX.Caught < 3:
                        $ LauraX.change_stat("love", 90, 5)
                        $ LauraX.change_stat("obedience", 50, 25)
                        $ LauraX.change_stat("obedience", 90, 30)
                if JeanX.location == bg_current and JeanX.Caught < 3:
                        $ JeanX.change_stat("love", 50, 5)
                        $ JeanX.change_stat("love", 90, 10)
                        $ JeanX.change_stat("obedience", 50, 25)
                        $ JeanX.change_stat("obedience", 90, 30)
                if StormX.location == bg_current and StormX.Caught < 3:
                        $ StormX.change_stat("love", 90, -5)
                        $ StormX.change_stat("obedience", 50, 20)
                        $ StormX.change_stat("obedience", 90, 30)
                if JubesX.location == bg_current and JubesX.Caught < 3:
                        $ JubesX.change_stat("love", 80, 10)
                        $ JubesX.change_stat("obedience", 50, 25)
                        $ JubesX.change_stat("obedience", 90, 30)

                call XavierFace("angry")
                $ Count += 20
                ch_x "If that's your attitude, harsher methods might be necessary."
                if PunishmentX:
                    ch_x "I'm extending your punishment by [Count] days!"
                else:
                    ch_x "I'm halving your daily stipend for [Count] days!"

                if RogueX.location == bg_current and RogueX.Caught < 3:
                        if RogueX.inhibition > 500:
                            $ RogueX.change_stat("inhibition", 90, 15)
                        $ RogueX.change_stat("inhibition", 30, -20)
                        $ RogueX.change_stat("inhibition", 50, -10)
                if KittyX.location == bg_current and KittyX.Caught < 3:
                        if KittyX.inhibition > 500:
                            $ KittyX.change_stat("inhibition", 90, 15)
                        $ KittyX.change_stat("inhibition", 30, -20)
                        $ KittyX.change_stat("inhibition", 50, -10)
                if EmmaX.location == bg_current and EmmaX.Caught < 3:
                        if EmmaX.inhibition > 500:
                            $ EmmaX.change_stat("inhibition", 90, 15)
                        $ EmmaX.change_stat("inhibition", 30, -20)
                        $ EmmaX.change_stat("inhibition", 50, -10)
                if LauraX.location == bg_current and LauraX.Caught < 3:
                        if LauraX.inhibition > 500:
                            $ LauraX.change_stat("inhibition", 90, 15)
                        $ LauraX.change_stat("inhibition", 30, -15)
                        $ LauraX.change_stat("inhibition", 50, -10)
                if JeanX.location == bg_current and JeanX.Caught < 3:
                        $ JeanX.change_stat("inhibition", 90, 15)
                if StormX.location == bg_current and StormX.Caught < 3:
                        if StormX.inhibition > 500:
                            $ StormX.change_stat("inhibition", 90, 5)
                        $ StormX.change_stat("inhibition", 30, -10)
                        $ StormX.change_stat("inhibition", 50, -5)
                if JubesX.location == bg_current and JubesX.Caught < 3:
                        if JubesX.inhibition > 500:
                            $ JubesX.change_stat("inhibition", 90, 15)
                        $ JubesX.change_stat("inhibition", 30, -15)
                        $ JubesX.change_stat("inhibition", 50, -10)

                ch_x "Now get out of my sight."
        #End "suck it"

    if line:
            if line == "Omega":
                    if Approvalcheck(RogueX, 1500, TabM=1, Loc="No"):
                            call Xavier_Plan(RogueX) #Plan_OmegaPlan_Alpha
                            return
                    elif Approvalcheck(RogueX, 1000, TabM=1, Loc="No"):
                            $ Girl.change_face("perplexed",Brows = "sad")
                            ch_r "I'm not comfortable with something that extreme, [RogueX.Petname]. . ."
                            menu:
                                "Dammit [RogueX.name]. . .":
                                        $ Girl.change_face("angry")
                                        $ RogueX.change_stat("obedience", 50, 5)
                                        $ RogueX.change_stat("love", 90, -5)
                                "Yeah, I guess you're right. . .":
                                        $ Girl.change_face("bemused")
                    else:
                            $ Girl.change_face("confused")
                            ch_r "What nonsense are you talking now?"
                            ch_p "Plan {i}Omega!{/i} . . you know. . ."
                            ch_r "Sounds like gibberish."
                            ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                            $ Girl.change_face("bemused")
                    #End "Plan Omega"
            elif line == "Kappa":
                    if "Xavier's photo" in Player.Inventory and Approvalcheck(KittyX, 1500, TabM=1, Loc="No"):
                            call Xavier_Plan(KittyX) #Plan_KappaPlan_Alpha
                            return
                    elif Approvalcheck(KittyX, 1000, TabM=1, Loc="No"):
                            $ Girl.change_face("perplexed",Brows = "sad")
                            if "Xavier's photo" in Player.Inventory:
                                    ch_k "You know. . . I really don't think that's a good idea. . ."
                            elif "kappa" in Player.History:
                                    ch_k "Maybe if we came back later we could find something. . ."
                            else:
                                    ch_k "We don't really have any way to pull that off atm. . ."
                                    $ Player.History.append("kappa")
                            menu:
                                "Dammit [KittyX.name]. . .":
                                        $ Girl.change_face("angry")
                                        $ KittyX.change_stat("obedience", 50, 5)
                                        $ KittyX.change_stat("love", 90, -5)
                                "Yeah, I guess you're right. . .":
                                        $ Girl.change_face("bemused")
                                        $ KittyX.change_stat("love", 90, 5)
                    else:
                            $ Girl.change_face("confused")
                            ch_k "Wait, Plan what??"
                            ch_p "Plan {i}Kappa!{/i} . . you know. . ."
                            ch_k "I have no {i}idea{/i} what you're talking about."
                            ch_p "oh, yeah, I guess I haven't mentioned that. . ."
                            $ Girl.change_face("bemused")
                    #End "Plan Kappa"
            elif line == "Psi":
                    if Approvalcheck(EmmaX, 1500, TabM=1, Loc="No"):
                            call Xavier_Plan(EmmaX) #Plan_PsiPlan_Alpha
                            return
                    elif Approvalcheck(EmmaX, 1000, TabM=1, Loc="No"):
                            $ Girl.change_face("perplexed",Brows = "sad")
                            ch_e "Um, I don't believe we're quite at that point yet, [EmmaX.Petname]. . ."
                            menu:
                                "Dammit [EmmaX.name]. . .":
                                        $ Girl.change_face("angry")
                                        $ EmmaX.change_stat("obedience", 50, 5)
                                        $ EmmaX.change_stat("love", 90, -5)
                                "Yeah, I guess you're right. . .":
                                        $ Girl.change_face("bemused")
                    else:
                            $ Girl.change_face("confused")
                            ch_e "Lord child, what are you talking about now?"
                            ch_p "Plan {i}Psi!{/i} . . you know. . ."
                            ch_e "I wish that I did."
                            ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                            $ Girl.change_face("bemused")
                    #End "Plan Psi"
            elif line == "Chi":
                    if LauraX.Lvl >= 2 and Approvalcheck(LauraX, 1500, TabM=1, Loc="No") and Approvalcheck(LauraX, 750, "I"):
                            call Xavier_Plan(LauraX) #Plan_ChiPlan_Alpha
                            return
                    elif Approvalcheck(LauraX, 1000, TabM=1, Loc="No"):
                            $ Girl.change_face("angry",Eyes="side",Brows = "angry")
                            ch_l "I told you that was a stupid idea. . ."
                            menu:
                                "Dammit [LauraX.name]. . .":
                                        $ Girl.change_face("angry")
                                        $ LauraX.change_stat("obedience", 50, 5)
                                        $ LauraX.change_stat("love", 90, -5)
                                "Yeah, I guess you're right. . .":
                                        $ Girl.change_face("bemused")
                                        $ LauraX.change_stat("love", 90, 5)
                    else:
                            $ Girl.change_face("confused")
                            ch_l "Yeah!"
                            ch_l ". . ."
                            ch_l "Wait, plan \"key,\" what??"
                            ch_p "Plan {i}Chi!{/i} . . you know. . ."
                            ch_l "Um. No?"
                            ch_p "oh, yeah, I guess I haven't mentioned that. . ."
                            $ Girl.change_face("bemused")
                    #End "Plan Chi"
            elif line == "Alpha":
                    if Approvalcheck(JeanX, 1500, TabM=1, Loc="No"):
                            call Xavier_Plan(JeanX) #Plan_Alpha
                            return
                    elif Approvalcheck(JeanX, 1000, TabM=1, Loc="No"):
                            $ Girl.change_face("perplexed",Brows = "sad")
                            ch_j "Look, this is your mess, I'm not going to clean it up, [JeanX.Petname]. . ."
                            menu:
                                "Dammit [JeanX.name]. . .":
                                        $ Girl.change_face("angry")
                                        $ JeanX.change_stat("obedience", 50, 5)
                                        $ JeanX.change_stat("love", 90, -5)
                                "Yeah, I guess you're right. . .":
                                        $ Girl.change_face("bemused")
                    else:
                            $ Girl.change_face("confused")
                            ch_j "Huh? What are you talking about?"
                            ch_p "Plan {i}Alpha!{/i} . . you know. . ."
                            ch_j "Drawing a blank here. . ."
                            ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                            $ Girl.change_face("bemused")
                    #End "Plan Alpha"
            elif line == "Rho":
                    if "Xavier's files" in Player.Inventory and Approvalcheck(StormX, 1500, TabM=1, Loc="No"):
                            call Xavier_Plan(StormX)
                            return
                    elif Approvalcheck(StormX, 1000, TabM=1, Loc="No"):
                            $ Girl.change_face("perplexed",Brows = "sad")
                            if "Xavier's files" in Player.Inventory:
                                    ch_s "I really doubt that we should attempt that. . ."
                            elif "rho" in Player.History:
                                    ch_s "Perhaps if we had some leverage on the situation. . ."
                            else:
                                    ch_s "I'm not sure what you think we could do here. . ."
                                    $ Player.History.append("rho")
                            menu:
                                "Dammit [StormX.name]. . .":
                                        $ Girl.change_face("angry")
                                        $ StormX.change_stat("obedience", 50, 5)
                                        $ StormX.change_stat("love", 90, -5)
                                "Yeah, I guess you're right. . .":
                                        $ Girl.change_face("bemused")
                    else:
                            $ Girl.change_face("confused")
                            ch_s "'Ro? You were speaking to me?"
                            ch_p "Yes! Plan {i}Rho!{/i} . . you know. . ."
                            ch_s "Yes, this is 'Ro. What plan?"
                            ch_p "What's on second! I don't know!"
                            $ Girl.change_face("smile")
                            ch_s "Ah! \"Third base!\""
                            $ Girl.change_face("bemused")
                    #End "Plan Rho"
            elif line == "Zeta":
                    if Approvalcheck(JubesX, 1500, TabM=1, Loc="No"):
                            call Xavier_Plan(JubesX) #Plan_PsiPlan_Alpha
                            return
                    elif Approvalcheck(JubesX, 1000, TabM=1, Loc="No"):
                            $ Girl.change_face("perplexed",Brows = "sad")
                            ch_v "What?! Um, no, let's not."
                            menu:
                                "Dammit [JubesX.name]. . .":
                                        $ Girl.change_face("angry")
                                        $ JubesX.change_stat("obedience", 50, 5)
                                        $ JubesX.change_stat("love", 90, -5)
                                "Yeah, I guess you're right. . .":
                                        $ Girl.change_face("bemused")
                    else:
                            $ Girl.change_face("confused")
                            ch_v "Huh?"
                            ch_p "Plan {i}Zeta!{/i} . . you know. . ."
                            ch_v "Is this a \"Gundam\" thing?"
                            ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                            $ Girl.change_face("bemused")
                    #End "Plan Zeta"

            # if the plan falls through. . .
            call XavierFace("angry")
            $ Count += 10
            ch_x "I have no idea what that was about, but it sounds like you haven't learned."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."

                if RogueX.location == bg_current and RogueX.Caught < 3:
                        $ RogueX.change_stat("obedience", 50, 10)
                        $ RogueX.change_stat("obedience", 90, 10)
                        $ RogueX.change_stat("inhibition", 30, -10)
                        $ RogueX.change_stat("inhibition", 50, -5)
                if KittyX.location == bg_current and KittyX.Caught < 3:
                        $ KittyX.change_stat("obedience", 50, 10)
                        $ KittyX.change_stat("obedience", 90, 10)
                        $ KittyX.change_stat("inhibition", 30, -10)
                        $ KittyX.change_stat("inhibition", 50, -5)
                if EmmaX.location == bg_current and EmmaX.Caught < 3:
                        $ EmmaX.change_stat("obedience", 50, 10)
                        $ EmmaX.change_stat("inhibition", 50, -5)
                if LauraX.location == bg_current and LauraX.Caught < 3:
                        $ LauraX.change_stat("obedience", 50, 10)
                        $ LauraX.change_stat("obedience", 90, 10)
                        $ LauraX.change_stat("inhibition", 30, -10)
                        $ LauraX.change_stat("inhibition", 50, -5)
                if JeanX.location == bg_current and JeanX.Caught < 3:
                        $ JeanX.change_stat("obedience", 50, -10)
                if StormX.location == bg_current and StormX.Caught < 3:
                        $ StormX.change_stat("obedience", 50, 10)
                        $ StormX.change_stat("inhibition", 50, -5)
                if JubesX.location == bg_current and JubesX.Caught < 3:
                        $ JubesX.change_stat("obedience", 50, 5)
                        $ JubesX.change_stat("obedience", 90, 5)
                        $ JubesX.change_stat("inhibition", 30, -8)
                        $ JubesX.change_stat("inhibition", 50, -2)
            ch_x "I've had enough of you, begone."
    #End "evil plans"

    $ PunishmentX += Count

    $ Girl.Caught += 1
    if Partner in all_Girls:
            $ Partner.Caught += 1
    $ Girl.AddWord(0,"caught","caught") #recent and daily

    if Girl == KittyX and KittyX not in Rules and "Xavier's photo" not in Player.Inventory:
            "It would probably be a good idea to find some way to get Xavier to leave you alone."
            if KittyX.Caught > 1:
                "Maybe I should try searching the office when he's not around."
            if KittyX.Caught > 2:
                "I bet [KittyX.name] could help me get in."
            if KittyX.Caught > 3:
                "I bet there's something in that lefthand drawer. . ."
    elif Girl == JeanX and "nowhammy" not in JeanX.Traits and JeanX.Caught > 1:
            ch_x "Oh, and Jean, dear, I'd like a word?"
            $ Girl.change_face("bemused")
            ch_j "What is it?"
            ch_x "I understand that you've been using your abilities to. . ."
            ch_x "cover up for some of your. . . transgressions."
            $ Girl.change_face("bemused",Eyes="up")
            ch_j "Oh, you mean how I mindwipe the \"NPCs\" that get too nosy?"
            call XavierFace("angry")
            ch_x "If by \"NPCs\" you mean your fellow students. . ."
            ch_x ". . . and by \"get too nosy,\" you mean \"notice you having sex in public\". . ."
            ch_x ". . . then yes, that is exactly what I mean."
            $ Girl.change_face("bemused",Eyes="side")
            ch_j "Ok, yeah."
            ch_x "I would like you to cease this activity at once!"
            ch_x "It is a total abuse of your abilities and of those students' autonomy!"
            $ Girl.change_face("angry",1)
            ch_j "Who cares."
            call XavierFace("shocked")
            ch_x "!!!"
            ch_x "I do!"
            call XavierFace("angry")
            ch_x "That is it, young lady. Until further notice, you're forbidden from. . . whammying your fellow students!"
            $ Girl.change_face("angry",1,Mouth="surprised")
            ch_j "Bullshit!"
            $ Girl.change_face("angry",0,Eyes="psychic")
            ch_x "Ugh. . ."
            call XavierFace("psychic")
            ch_x "[Player.name]. . . this may take a while. . ."
            ch_x "You may as well leave. . ."
            $ JeanX.Traits.append("nowhammy")
            $ Girl.change_face("normal")

    if EmmaX.location == bg_current and EmmaX not in Rules:
            ch_x "Emma, I'd like you to stay after for a brief discussion about \"boundaries\". . ."
            if EmmaX.Caught:
                    $ EmmaX.change_stat("love", 90, -5)
                    $ Girl.change_face("angry",Eyes="closed")
                    ch_e "Not again. . ."
    if StormX.location == bg_current and StormX not in Rules:
            if EmmaX.location == bg_current and EmmaX not in Rules:
                    ch_x "And Ororo, I'm afraid we will have to have words as well. . ."
            else:
                    ch_x "Ororo, I'd like you to stay after for a brief discussion about \"boundaries\". . ."
            if StormX.Caught:
                    $ StormX.change_stat("love", 90, -5)
                    $ Girl.change_face("angry",Eyes="closed")
                    ch_s "Again? . ."
            if StormX not in Rules and "Xavier's files" not in Player.Inventory:
                    "It would probably be a good idea to find some way to get Xavier to leave you alone."
                    if StormX.Caught > 1:
                        "Maybe I should try searching the office when he's not around."
                    if StormX.Caught > 2:
                        "I bet [StormX.name] could help me get in."
                    if StormX.Caught > 3:
                        "I bet there's something in that righthand drawer. . ."

    call remove_girl("all")
    "You return to your room"
    hide Professor
    $ bg_current = "bg_player"
    jump Misplaced

label Xavier_Plan(GirlX=0): #rkeljsv
    if "Xavier" in Player.daily_history:
            "The Professor seems pretty out of it."
            "You don't think you'll be able to get anything more out of him today."
            "You leave him to it."
            $ bg_current = "bg_player"
            jump Misplaced

    #$ GirlX = Girlcheck(GirlX)
    call shift_focus(GirlX)
    $ GirlX.change_face("sly")
    "As you say this, a sly grin crosses [GirlX.name]'s face."
    "You quickly approach Xavier and place your hands on his head."
    call XavierFace("psychic")
    ch_x ". . ."
    call XavierFace("shocked")
    "Xavier realizes with a shock that with your powers, his telepathy is useless."

    if Partner:
            if Partner == RogueX and "Omega" not in Player.Traits:
                    $ line = "first"
            elif Partner == KittyX and "Kappa" not in Player.Traits:
                    $ line = "first"
            elif Partner == EmmaX and "Psi" not in Player.Traits:
                    $ line = "first"
            elif Partner == LauraX and "Chi" not in Player.Traits:
                    $ line = "first"
            elif Partner == JeanX and "Alpha" not in Player.Traits:
                    $ line = "first"
            elif Partner == StormX and "Rho" not in Player.Traits:
                    $ line = "first"
            elif Partner == JubesX and "Zeta" not in Player.Traits:
                    $ line = "first"

            if line == "first":
                #if the Partner has never done this. . .
                if Approvalcheck(Partner, 1000) or Partner == JeanX:
                        #if she's cool with it.
                        $ Partner.change_face("surprised")
                        "[Partner.name] looks a bit caught off guard, but goes along with the idea."
                        $ Partner.change_face("sly")
                else:
                        $ Partner.change_face("surprised")
                        "[Partner.name] looks a bit uncomfortable with what's happening and takes off."
                        call remove_girl(Partner)

            else:
                        $ Partner.change_face("sly")
                        "[Partner.name] understands what's going on here."
    #end partner response

    call XavierFace("angry")
    if GirlX == RogueX:
            $ RogueX.Arms = 0
            $ RogueX.ArmPose = 2
            show Rogue_Sprite at sprite_location(StageLeft+100,85) zorder 24 with ease
            "[RogueX.name] moves in and also grabs his head, duplicating his powers as he watches helplessly."
            "Now that she posesses his full power, while his are negated, he has no defenses."
            call XavierFace("hypno")
            if "Omega" in Player.Traits:
                    ch_x "Oh, not again."
                    ch_x "What is it you want this time?"
                    $ RogueX.change_stat("obedience", 80, 3)
                    $ RogueX.change_stat("inhibition", 70, 1)
            else:
                    $ RogueX.change_stat("obedience", 50, 40)
                    $ RogueX.change_stat("inhibition", 70, 20)
            ch_r "Well, [RogueX.Petname], what would you like to do with this opportunity?"
            ch_r "I think we'll only get three tries at this. . ."
    elif GirlX == KittyX:
            $ KittyX.ArmPose = 2
            show Kitty_Sprite at sprite_location(StageLeft+100,150) with ease
            $ KittyX.sprite_location = StageCenter
            "[KittyX.name] moves in sits on his lap, pinning his arms to the chair."
            if "Kappa" in Player.Traits:
                    ch_x "Oh, not again."
                    ch_x "What is it you want this time?"
                    $ KittyX.change_stat("obedience", 80, 3)
                    $ KittyX.change_stat("inhibition", 70, 1)
            else:
                    ch_x "What is the meaning of this? Unhand me!"
                    "You pull out the photo you found earlier in his study."
                    $ KittyX.change_stat("obedience", 50, 40)
                    $ KittyX.change_stat("inhibition", 70, 30)
                    ch_p "I have here a rather. . . compromising photo of you and Mystique."
                    ch_p "I was thinking maybe you could cut me a little slack around here."
                    ch_x "And if I do not?"
                    ch_p "[KittyX.name] here's set it to distribute to every computer in school, every day."
                    ch_p "And only I know the password."
                    ch_x "Very well. . . I'll forget about your punishment."
                    ch_p "Oh, I think we can do a bit better than that. . ."
                    $ KittyX.change_stat("obedience", 200, 30)
                    $ KittyX.change_stat("inhibition", 200, 10)
            ch_k "Well, [KittyX.Petname], what should we ask for?"
    elif GirlX == EmmaX or GirlX == JeanX:
            if GirlX == EmmaX:
                    show Emma_Sprite at sprite_location(StageLeft+100,85) zorder 24 with ease
            elif GirlX == JeanX:
                    show Jean_Sprite at sprite_location(StageLeft+100,85) zorder 24 with ease
            "[GirlX.name] moves behind Xavier and activates her own telepathy."
            call XavierFace("angry")
            if (GirlX == EmmaX and "Psi" in Player.Traits) or (GirlX == JeanX and "Alpha" in Player.Traits):
                    ch_x "Oh, not again. . ."
                    $ GirlX.change_stat("obedience", 80, 3)
                    $ GirlX.change_stat("inhibition", 80, 1)
            else:
                    $ GirlX.change_stat("obedience", 50, 40)
                    $ GirlX.change_stat("inhibition", 70, 30)
                    $ GirlX.change_stat("obedience", 200, 30)
                    $ GirlX.change_stat("inhibition", 200, 10)
            call Anyline(GirlX,"Well, "+GirlX.Petname+", what should we ask for?")
    elif GirlX == LauraX:
            $ LauraX.ArmPose = 2
            if "Chi" in Player.Traits:
                    ch_x "Oh, not again."
                    $ LauraX.Claws = 1
                    ch_x "What is it you want this time?"
                    $ LauraX.change_stat("obedience", 80, 3)
                    $ LauraX.change_stat("inhibition", 80, 1)
            else:
                    ch_x "What is the meaning of this? Unhand me!"
                    ch_p "[LauraX.name] and I were talking, and it seems like neither of us appreciates you bothering us."
                    ch_x "And if I continue?"
                    ch_p "My little [LauraX.Pet] here has a very particular set of skills, you know. . ."
                    $ GirlX.namecheck() #checks reaction to petname
                    $ LauraX.Claws = 1
                    $ GirlX.change_face("sly")
                    ch_p "She could cause a lot of trouble if she keeps getting called down here. . ."
                    "[LauraX.name] draws her claws along the arm of the Professor's chair, tracing fine lines into the metal."
                    ch_x "Very well. . . I'll forget about your punishment."
                    ch_p "Oh, I think we can do a bit better than that. . ."
                    $ LauraX.change_stat("obedience", 50, 40)
                    $ LauraX.change_stat("inhibition", 80, 30)
                    $ LauraX.change_stat("obedience", 200, 30)
                    $ LauraX.change_stat("inhibition", 200, 10)
            ch_l "Well, [LauraX.Petname], what should we ask for?"
    elif GirlX == StormX:
            $ StormX.ArmPose = 1
            show Storm_Sprite at sprite_location(StageLeft+100,150) with ease
            $ StormX.sprite_location = StageCenter
            "[StormX.name] moves in sits on his lap, pinning his arms to the chair."
            if "Rho" in Player.Traits:
                    ch_x "Oh, not this again."
                    ch_x "What is it you want this time?"
                    $ StormX.change_stat("obedience", 80, 3)
                    $ StormX.change_stat("inhibition", 70, 1)
            else:
                    ch_x "What is the meaning of this? Unhand me!"
                    "You pull out the files you found earlier in his study."
                    $ StormX.change_stat("obedience", 50, 40)
                    $ StormX.change_stat("inhibition", 70, 30)
                    ch_p "I have here some rather. . . questionable \"medical\" files."
                    ch_p "I was thinking maybe you could cut me a little slack around here."
                    ch_x "And if I do not?"
                    ch_p "We've made sure that -all- the girls in these files will find out."
                    ch_x "Very well. . . I'll forget about your punishment."
                    ch_p "Oh, I think we can do a bit better than that. . ."
                    $ StormX.change_stat("obedience", 200, 30)
                    $ StormX.change_stat("inhibition", 200, 10)
            ch_s "Well, [StormX.Petname], what should we ask for?"
    elif GirlX == JubesX:
            $ JubesX.ArmPose = 2
            show Jubes_Sprite at sprite_location(StageLeft+100,150) with ease
            $ JubesX.sprite_location = StageCenter
            "[JubesX.name] moves in and sits on his lap, pinning his arms to the chair."  #fix, change this when doggy pose is available
            "She turns to look at him."
            if "Zeta" in Player.Traits:
                    ch_x "Oh, not again."
                    ch_x "What is it you want this time?"
                    $ JubesX.change_stat("obedience", 80, 3)
                    $ JubesX.change_stat("inhibition", 70, 1)
            else:
                    ch_x "What is the meaning of this? Unhand me!"
                    $ JubesX.change_stat("inhibition", 70, 30)
                    ch_v "Look into my eyes. . ."
                    $ JubesX.change_stat("obedience", 50, 40)
                    $ JubesX.change_stat("inhibition", 200, 10)
                    ch_v "see the sparks dancing around them? . . ."
                    $ JubesX.change_stat("obedience", 200, 30)
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

            "You know, [JeanX.name] should be able to \"whammy\" people again." if JeanX in all_Girls and "nowhammy" in JeanX.Traits:
                    ch_x "I could remove her mind-wiping ban. . ."
                    $ JeanX.Traits.remove("nowhammy")
                    $ JeanX.Traits.append("whammy")
                    if JeanX.location == bg_current:
                            $ JeanX.change_stat("obedience", 50, 5)
                            $ JeanX.change_stat("love", 50, 5)
                            $ JeanX.change_stat("love", 70, 5)
                            $ JeanX.change_stat("love", 90, 5)
                            $ GirlX.change_face("sly",1)
                            ch_j "Nice. . ."
            "You know, I did like it when [JeanX.name] couldn't use her \"whammy.\"" if JeanX in all_Girls and "whammy" in JeanX.Traits:
                    ch_x "I could reinstate her mind-wiping ban. . ."
                    $ JeanX.Traits.append("nowhammy")
                    $ JeanX.Traits.remove("whammy")
                    if JeanX.location == bg_current:
                            $ JeanX.change_stat("obedience", 50, 5)
                            $ JeanX.change_stat("obedience", 80, 5)
                            $ JeanX.change_stat("love", 70, -5)
                            $ JeanX.change_stat("love", 90, -5)
                            $ GirlX.change_face("angry",1,Mouth="surprised")
                            ch_j "Hey!"
                            $ GirlX.change_face("angry",1)

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
                    $ line = 0
                    menu:
                        ch_p "Could you get rid of. . ."
                        "[RogueX.name]" if RogueX in active_Girls:
                                $ line = RogueX
                        "[KittyX.name]" if KittyX in active_Girls and "met" in KittyX.History:
                                $ line = KittyX
                        "[EmmaX.name]" if EmmaX in active_Girls and "met" in EmmaX.History:
                                $ line = EmmaX
                        "[LauraX.name]" if LauraX in active_Girls and "met" in LauraX.History and "dress0" not in LauraX.History:
                                $ line = LauraX
                        "[JeanX.name]" if JeanX in active_Girls and "met" in JeanX.History:
                                $ line = JeanX
                        "[StormX.name]" if StormX in active_Girls and "met" in StormX.History:
                                $ line = StormX
                        "[JubesX.name]" if JubesX in active_Girls and "met" in JubesX.History:
                                $ line = JubesX
                        "Never mind. . .":
                                $ Count += 1
                    if line:
                            #if you picked someone. . .
                            ch_x "Very well, I suppose I can keep her occupied with various tasks around the campus. . ."
                            ch_x "She should be out of your hair for the time being."
                            if line.location == bg_current:
                                    #if she's in the room
                                    $ line.change_stat("love", 90, -10)
                                    $ line.change_stat("obedience", 50, 3)
                                    if line == RogueX:
                                            ch_r "What do you mean, I'm \"bothering\" you?"
                                    elif line == KittyX:
                                            ch_k "Hey, what gives?!"
                                    elif line == EmmaX:
                                            ch_e "Excuse me? I must not have heard that right."
                                    elif line == LauraX:
                                            ch_l "Explain."
                                    elif line == JeanX:
                                            ch_j "Are you kidding me?!"
                                    elif line == StormX:
                                            ch_s "I do not understand this."
                                    elif line == JubesX:
                                            ch_v "Seriously?!"
                                    menu:
                                        extend ""
                                        "Oh, sorry, never mind.":
                                                $ line = 0
                                                if Approvalcheck(line, 2000):
                                                        #if she accepts it
                                                        $ line.change_face("confused")
                                                        $ line.change_stat("love", 90, 3)
                                                        $ line.change_stat("obedience", 50, 2)
                                                        if line == RogueX:
                                                                ch_r "Right. . ."
                                                        elif line == KittyX:
                                                                ch_k "Uh-huh?"
                                                        elif line == EmmaX:
                                                                ch_e ". . . right. . ."
                                                        elif line == LauraX:
                                                                ch_l "If you say so."
                                                        elif line == JeanX:
                                                                ch_j "We will have words. . ."
                                                        elif line == StormX:
                                                                ch_s "I will remember this. . ."
                                                        elif line == JubesX:
                                                                ch_v "Riiight."
                                                else:
                                                        #if she's mad
                                                        $ line.change_face("angry")
                                                        $ line.change_stat("obedience", 50, -2)
                                                        $ line.change_stat("inhibition", 60, 3)
                                                        if line == RogueX:
                                                                ch_r "Damned right you are."
                                                        elif line == KittyX:
                                                                ch_k "Yeah, right."
                                                        elif line == EmmaX:
                                                                ch_e "I don't know what you were thinking."
                                                        elif line == LauraX:
                                                                ch_l "Uh. . . huh."
                                                        elif line == JeanX:
                                                                ch_j "We will have words. . ."
                                                        elif line == StormX:
                                                                ch_s "I will remember this. . ."
                                                        elif line == JubesX:
                                                                ch_v "We will have words."
                                        "Sorry, but I just need some \"me\" time.":
                                                $ active_Girls.remove(line)
                                                $ line.change_stat("obedience", 50, 5)
                                                $ line.change_stat("obedience", 90, 2)
                                                $ line.change_stat("inhibition", 60, 2)
                                                if Approvalcheck(line, 900, "L") or Approvalcheck(line, 2000):
                                                        #if she accepts it
                                                        $ line.change_face("sadside")
                                                        if line == RogueX:
                                                                ch_r "I suppose if you do, I can give you some space."
                                                        elif line == KittyX:
                                                                ch_k "I guess we both could. . ."
                                                        elif line == EmmaX:
                                                                ch_e "I wouldn't want to be a bother. . ."
                                                        elif line == LauraX:
                                                                ch_l "I can make myself scarce. . ."
                                                        elif line == JeanX:
                                                                ch_j "Well, I guess I could find someone else to occupy my time with. . ."
                                                        elif line == StormX:
                                                                ch_s ". . . fine, I can understand that. . ."
                                                        elif line == JubesX:
                                                                ch_v "Ok, whatever, I have things to do."
                                                else:
                                                        #if she's mad
                                                        $ line.change_stat("love", 90, -5)
                                                        $ line.change_face("angry")
                                                        $ line.AddWord(1,"angry","angry")
                                                        if line == RogueX:
                                                                ch_r "Oh, I think you'll be getting it."
                                                        elif line == KittyX:
                                                                ch_k "Yeah, \"me\" too, I guess!"
                                                        elif line == EmmaX:
                                                                ch_e "I do have other things with which to occupy myself."
                                                        elif line == LauraX:
                                                                ch_l "I'm busy too."
                                                        elif line == StormX:
                                                                ch_s "Oh, you shall get it. . ."
                                                        elif line == JubesX:
                                                                ch_v "We will have words."
                                        "You heard me.":
                                                $ active_Girls.remove(line)
                                                $ line.change_stat("love", 80, -5)
                                                $ line.change_stat("love", 90, -5)
                                                $ line.change_stat("obedience", 80, 5)
                                                if Approvalcheck(line, 850, "O") or Approvalcheck(line, 1500, "LO"):
                                                        #if she accepts it
                                                        $ line.change_face("sadside")
                                                        $ line.change_stat("obedience", 200, 10)
                                                else:
                                                        #if she's mad
                                                        $ line.change_face("angry")
                                                        $ line.change_stat("love", 90, -5)
                                                        $ line.change_stat("inhibition", 60, 5)
                                                        $ line.AddWord(1,"angry","angry")
                                                if line == RogueX:
                                                        ch_r "Loud and clear."
                                                elif line == KittyX:
                                                        ch_k ". . ."
                                                elif line == EmmaX:
                                                        ch_e "I suppose I did."
                                                elif line == LauraX:
                                                        ch_l "If you say so."
                                                elif line == JeanX:
                                                        ch_j "Noted. . ."
                                                elif line == StormX:
                                                        ch_s "Like thunder. . ."
                                                elif line == JubesX:
                                                        ch_v "We will have words."
                                    #end "picked same girl
                            else:
                                    #if she is not in the room
                                    $ active_Girls.remove(line)
                    if line == GirlX:
                        call Anyline(GirlX,"Did you forget that I'm your escape plan?")
                        menu:
                            "Oh. . .":
                                    ch_x "I'll forget you asked."
                                    $ Count = 0
                    $ line = 0
            #end "remove girl"

            "I wanted to bring a girl back in. . ." if len(all_Girls) > len (active_Girls):
                    "This will bring the girl back into active play."
                    "You can always ask to send her away again later."
                    $ line = 0
                    menu:
                        ch_p "Could you bring back. . ."
                        "[RogueX.name]" if RogueX not in active_Girls and RogueX in TotalGirl:
                                $ line = RogueX
                        "[KittyX.name]" if KittyX not in active_Girls and KittyX in all_Girls and "met" in KittyX.History:
                                $ line = KittyX
                        "[EmmaX.name]" if EmmaX not in active_Girls and EmmaX in all_Girls and "met" in EmmaX.History:
                                $ line = EmmaX
                        "[LauraX.name]" if LauraX not in active_Girls and LauraX in all_Girls and "met" in LauraX.History and "dress0" not in LauraX.History:
                                #Laura has a special condition because of her introduction story
                                $ line = LauraX
                        "[JeanX.name]" if JeanX not in active_Girls and JeanX in all_Girls and "met" in JeanX.History:
                                $ line = JeanX
                        "[StormX.name]" if StormX not in active_Girls and StormX in all_Girls and "met" in StormX.History:
                                $ line = StormX
                        "[JubesX.name]" if JubesX not in active_Girls and JubesX in all_Girls and "met" in JubesX.History:
                                $ line = JubesX
                        "Never mind. . .":
                                $ Count += 1
                    if line:
                            #if you picked someone. . .
                            ch_x "Certainly. I've kept her busy, but I can let her off the hook. . ."
                            ch_x "She should have more free time now. . ."
                            $ active_Girls.append(line)
                    $ line = 0
            "In was interested in a key. . . ":
                menu:
                    "Give me the key to your study." if "Xavier" not in Keys:
                            ch_x "Fine, take it. . ."
                            $ Keys.append("Xavier")
                    "Give me the key to your study.[[Owned] (locked)" if "Xavier" in Keys:
                            pass

                    "Give me the key to [GirlX.name]'s room." if GirlX not in Keys:
                            ch_x "I. . . suppose I could do that. . ."
                            $ Keys.append(GirlX)
                    "Give me the key to [GirlX.name]'s room.[[Owned] (locked)" if GirlX in Keys:
                            pass

                    "Never mind the keys.":
                            $ Count += 1
            "That should do it.":
                $ Count = 0

    ch_x "Very well, that should conclude our business. Please leave."
    if GirlX == RogueX:
            if "Omega" not in Player.Traits:
                    $ GirlX.change_stat("lust", 90, 10)
                    $ GirlX.change_stat("love", 70, 30)
                    $ GirlX.change_stat("love", 200, 20)
                    $ Player.Traits.append("Omega")
            ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here."
            $ GirlX.Arms = "gloves"
            $ GirlX.ArmPose = 1
    elif GirlX == KittyX:
            if "Kappa" not in Player.Traits:
                    $ GirlX.change_stat("lust", 90, 10)
                    $ GirlX.change_stat("inhibition", 80, 10)
                    $ GirlX.change_stat("love", 70, 10)
                    $ GirlX.change_stat("love", 200, 20)
                    $ Player.Traits.append("Kappa")
            $ GirlX.ArmPose = 0
    elif GirlX == EmmaX:
            ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here."
            if "Psi" not in Player.Traits:
                    $ GirlX.change_stat("lust", 90, 10)
                    $ GirlX.change_stat("inhibition", 80, 10)
                    $ GirlX.change_stat("love", 70, 10)
                    $ GirlX.change_stat("love", 200, 20)
                    $ Player.Traits.append("Psi")
    elif GirlX == LauraX:
            if "Chi" not in Player.Traits:
                    $ GirlX.change_stat("lust", 90, 10)
                    $ GirlX.change_stat("inhibition", 80, 10)
                    $ GirlX.change_stat("love", 70, 10)
                    $ GirlX.change_stat("love", 200, 20)
                    $ Player.Traits.append("Chi")
            $ GirlX.ArmPose = 1
            $ GirlX.Claws = 0
    elif GirlX == JeanX:
            ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here."
            if "Alpha" not in Player.Traits:
                    $ GirlX.change_stat("lust", 70, 20)
                    $ GirlX.change_stat("lust", 90, 10)
                    $ GirlX.change_stat("inhibition", 80, 10)
                    $ GirlX.change_stat("obedience", 70, 10)
                    $ GirlX.change_stat("obedience", 200, 20)
                    $ GirlX.change_stat("love", 70, 10)
                    $ GirlX.change_stat("love", 200, 20)
                    $ Player.Traits.append("Alpha")
    elif GirlX == StormX:
            if "Rho" not in Player.Traits:
                    $ GirlX.change_stat("lust", 90, 10)
                    $ GirlX.change_stat("inhibition", 80, 10)
                    $ GirlX.change_stat("love", 70, 10)
                    $ GirlX.change_stat("love", 200, 20)
                    $ Player.Traits.append("Rho")
    elif GirlX == JubesX:
            if "Zeta" not in Player.Traits:
                    $ GirlX.change_stat("lust", 90, 10)
                    $ GirlX.change_stat("inhibition", 80, 10)
                    $ GirlX.change_stat("love", 70, 10)
                    $ GirlX.change_stat("love", 200, 20)
                    $ Player.Traits.append("Zeta")
            $ GirlX.ArmPose = 0

    $ Player.daily_history.append("Xavier")
    call remove_girl("all")
    hide Professor
    $ bg_current = "bg_player"
    call set_the_scene
    "You return to your room"
    jump Misplaced

label Girl_Caught_Changing(Girl=0): #rkeljsv
        if Girl not in all_Girls:
                return
        call shift_focus(Girl)
        $ D20 = renpy.random.randint(1, 20)

        $ Girl.change_face("surprised", 1,Mouth="kiss")
        call remove_girl("all")

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
        $ Girl.location = bg_current
        call set_the_scene(check_if_dressed=0)
        if D20 > 17:
                #She's naked
                "As you enter the room, you see [Girl.name] is naked, and seems to be getting dressed."
        elif D20 >14:
                #She's Topless
                "As you enter the room, you see [Girl.name] is practically naked, and seems to be getting dressed."
        elif D20 >10:
                #She's in her underwear
                "As you enter the room, you see [Girl.name] is in her underwear, and seems to be getting dressed."
        elif D20 >5:
                #She's wearing pants/skirt
                "As you enter the room, you see [Girl.name] has her top off, and seems to be getting dressed."
        else:
                #She's done
                "As you enter the room, you see [Girl.name] has just pulled her top on, and seems to have been getting dressed."

        if Girl == StormX:
                ch_s "Oh, hello, [Girl.Petname]."
        elif Approvalcheck(Girl, 1400):
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
                        if not Approvalcheck(Girl, (D20 *70)) and (not Girl.SeenPussy or not Girl.SeenChest):
                                # if D20*70 is less than her approval, and this is the first you've seen of her bits. . .
                                $ Girl.change_face("surprised",Brows="angry")
                                $ Girl.change_stat("love", 80, -50)

                                if not Girl.OverNum() or (Girl.OverNum()+Girl.ChestNum() <5) or (Girl.PantsNum() < 5 and Girl.HoseNum() < 10):
                                    # if either she is mostly topless or mostly bottomless)

                                    call first_bottomless(Girl, 1)
                                    call first_topless(Girl, silent = 1)
                                    $ Girl.Over = "towel"
                                    "She grabs a towel and covers up."
                        else:
                                #She's cool with it, but confused.
                                $ Girl.change_face("surprised", 1,Brows = "confused")
                                if "exhibitionist" in Girl.Traits:
                                    $ Girl.change_stat("lust", 200, (2*D20))
                                else:
                                    $ Girl.change_stat("lust", 200, D20)
                                if D20 > 17:
                                        call expression Girl.Tag + "_First_Bottomless"
                                        call first_topless(Girl, silent = 1)
                                elif D20 > 15:
                                        call expression Girl.Tag + "_First_Bottomless"
                                elif D20 > 14:
                                        call first_topless(Girl)
                        $ Girl.change_stat("inhibition", 70, 20)


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
                                    $ Girl.change_stat("love", 50, 2)
                                    $ Girl.change_stat("love", 80, 4)
                            "And miss the view?":
                                    $ Girl.change_stat("obedience", 50, 2)
                                    $ Girl.change_stat("obedience", 80, 2)
                                    $ Girl.change_stat("inhibition", 60, 1)
                        #end if she's partially nude
                else:
                        #She's fully dressed
                        if not Approvalcheck(Girl, 800) and (not Girl.SeenPussy or not Girl.SeenChest):
                                $ Girl.change_face("angry",Brows="confused")
                                $ Girl.change_stat("love", 80, -5)
                        else:
                                $ Girl.change_face("sexy",Brows="confused")
                        $ Girl.change_stat("inhibition", 50, 3)

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
                                    $ Girl.change_stat("love", 50, 2)
                                    $ Girl.change_stat("love", 80, 2)
                            "Well, to be honest. . .":
                                    $ Girl.change_stat("love", 50, -2)
                                    $ Girl.change_stat("obedience", 50, 2)
                                    $ Girl.change_stat("obedience", 80, 2)
                                    $ Girl.change_stat("inhibition", 60, 1)
                $ Girl.change_face("sexy")
                if Approvalcheck(Girl, 1000):
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
                        call first_bottomless(Girl, 1)
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
                        if Approvalcheck(Girl, 350+(10*D20)): #400-550
                                $ Girl.change_stat("love", 70, 3)
                                $ Girl.change_stat("obedience", 50, 1)
                                $ Girl.change_stat("obedience", 80, 2)
                                $ Girl.change_stat("inhibition", 60, 2)
                                $ Girl.change_face("sexy")
                                ch_s "I suppose that could not hurt. . ."
                                $ Girl.Set_Temp_Outfit() #sets current outfit as temporary
                        else:
                                $ Girl.change_stat("inhibition", 60, 2)
                                $ Girl.change_face("smile")
                                ch_s "Ha! I would not want to be too much of a distraction."
                                $ Girl.OutfitChange(6,Changed=0)
                "Why not lose the rest too?":
                        $ Girl.change_face("sexy")
                        if Approvalcheck(Girl, 700):
                                $ Girl.change_stat("love", 50, 1)
                                $ Girl.change_stat("love", 70, 1)
                                $ Girl.change_stat("obedience", 50, 1)
                                $ Girl.change_stat("obedience", 80, 1)
                                $ Girl.change_stat("inhibition", 70, 1)
                                ch_s "Oh, you are a naughty one. . ."
                                $ Girl.OutfitChange("nude")
                                $ Girl.Set_Temp_Outfit() #sets current outfit as temporary
                        elif Approvalcheck(Girl, 350+(10*D20)): #400-550
                                $ Girl.change_stat("love", 80, 1)
                                $ Girl.change_stat("obedience", 50, 1)
                                $ Girl.change_stat("obedience", 80, 1)
                                $ Girl.change_stat("inhibition", 70, 2)
                                ch_s "I could at least. . . pause for a moment?"
                                $ Girl.Set_Temp_Outfit() #sets current outfit as temporary
                        else:
                                $ Girl.change_stat("love", 60, 1)
                                $ Girl.change_stat("obedience", 50, 2)
                                $ Girl.change_stat("inhibition", 70, 1)
                                ch_s "You are joking, [Girl.Petname]."
                                $ Girl.OutfitChange(6,Changed=0)
                "Don't, stay like that.":
                        $ Girl.change_stat("obedience", 80, 2)
                        if Approvalcheck(Girl,1100):
                                $ Girl.change_stat("obedience", 50, 2)
                                $ Girl.change_stat("inhibition", 60, 1)
                                $ Girl.change_face("sexy")
                                ch_s "If you want. . ."
                                $ Girl.Set_Temp_Outfit() #sets current outfit as temporary
                        elif Approvalcheck(Girl, 350+(10*D20)) and Approvalcheck(Girl, 400, "O"):
                                $ Girl.change_stat("love", 50, -2)
                                $ Girl.change_stat("love", 80, -1)
                                $ Girl.change_stat("obedience", 50, 2)
                                $ Girl.change_face("sexy",Eyes="side")
                                ch_s ". . . Very well."
                                $ Girl.Set_Temp_Outfit() #sets current outfit as temporary
                        else:
                                $ Girl.change_stat("love", 80, -2)
                                $ Girl.change_stat("obedience", 50, -1)
                                $ Girl.change_face("angry")
                                ch_s "You do not decide that, [Girl.Petname]."
                                $ Girl.OutfitChange(6,Changed=0)
                "Lose the rest of it.":
                        $ Girl.change_stat("obedience", 80, 2)
                        if Approvalcheck(Girl,1300):
                                $ Girl.change_stat("obedience", 50, 2)
                                $ Girl.change_stat("inhibition", 60, 1)
                                $ Girl.change_face("sexy")
                                ch_s "Fine. . ."
                                $ Girl.OutfitChange("nude")
                                $ Girl.Set_Temp_Outfit() #sets current outfit as temporary
                        elif Approvalcheck(Girl,800) and Approvalcheck(Girl, 500, "O"):
                                $ Girl.change_stat("love", 50, -2)
                                $ Girl.change_stat("love", 80, -2)
                                $ Girl.change_stat("obedience", 50, 2)
                                $ Girl.change_stat("obedience", 80, 1)
                                $ Girl.change_face("sexy",Eyes="side")
                                ch_s ". . . Fine."
                                $ Girl.OutfitChange("nude")
                                $ Girl.Set_Temp_Outfit() #sets current outfit as temporary
                        else:
                                $ Girl.change_stat("love", 50, -2)
                                $ Girl.change_stat("love", 80, -2)
                                $ Girl.change_stat("obedience", 50, -2)
                                $ Girl.change_stat("obedience", 80, 2)
                                $ Girl.change_face("angry")
                                ch_s "I do not think that I will, [Girl.Petname]."
                                $ Girl.OutfitChange(6,Changed=0)
        return

label Girl_Caught_Mastubating(Girl=0): #rkeljsv
        #called by room entry dialog if the girl was masturbating
        if Girl not in all_Girls:
            return
        $ Girl.DrainWord("gonnafap")
        call remove_girl("all")
        $ Girl.location = bg_current
        "As you approach her room, you hear soft moans from inside, and notice that the door is slightly ajar."
        menu:
            extend ""
            "Knock politely":
                $ line = "knock"
            "Peek inside":
                call set_the_scene
                $ Girl.change_face("kiss",1,Eyes = "closed")
                $ primary_action = "masturbation"
                $ girl_offhand_action = "fondle_pussy"
                "You see [Girl.name], eyes closed and stroking herself vigorously."
                menu:
                    extend ""
                    "Enter Quietly":
                            $ line = "enter"
                    "Pull back and knock":
                            $ line = "knock"
                    "Leave quietly":
                            $ line = "leave"
            "Enter quietly":
                    $ line = "enter"
                    "You hear some odd noises coming from [Girl.name]'s room as you enter."
            "Leave quietly":
                    $ line = "leave"

        if line == "leave":
                $ Girl.change_stat("lust", 80, 20)
                "You leave [Girl.name] to her business and slip out."
                $ renpy.pop_call()
                jump Campus_Map
        elif line == "knock":
                "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                "After several seconds and some more shuffling of clothing, [Girl.name] comes to the door."
                $ Girl.change_face("confused",1,Eyes = "surprised",Mouth = "smile")
                $ primary_action = 0
                $ girl_offhand_action = 0
                call set_the_scene
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
        elif line == "enter":
                call shift_focus(Girl)
                show blackscreen onlayer black
                $ Girl.Upskirt = 1
                $ Girl.PantiesDown = 1
                $ Girl.location = bg_current
                #call clear_the_room(Girl,1,1)
                call set_the_scene
                $ Girl.change_face("sexy")
                $ Girl.Eyes = "closed"
                $ Girl.ArmPose = 2
                $ Count = 0
                $ primary_action = "masturbation"
                hide blackscreen onlayer black
                $ Girl.daily_history.append("unseen")
                $ Girl.recent_history.append("unseen")
                call sex_acts("masturbation")
                if "angry" in Girl.recent_history:
                        return

                #After caught masturbating. . .
                $ Girl.change_face("sexy",Brows="confused")
                if Girl.Mast == 1:
                        if Girl == RogueX:
                                ch_r "Well that was a bit unexpected. . ."
                                $ Girl.change_face("bemused",Eyes="side")
                                ch_r "but not exactly unpleasant. . ."
                                $ Girl.change_face("sexy")
                                ch_r "Maybe next time I'll give you a heads up first."
                        elif Girl == KittyX:
                                ch_k "So[KittyX.like]I wasn't expecting company. . ."
                                $ Girl.change_face("bemused",Eyes="side")
                                ch_k "but I didn't exactly mind it either. . ."
                                $ Girl.change_face("sexy")
                                ch_k "Maybe knock next time?"
                        elif Girl == EmmaX:
                                ch_e "I wasn't expecting visitors. . ."
                                $ Girl.change_face("bemused",Eyes="side")
                                ch_e "although for you I could make an exception. . ."
                                $ Girl.change_face("sexy")
                                ch_e "Perhaps next time you could knock?"
                        elif Girl == LauraX:
                                ch_l "So what are you doing here? . ."
                                $ Girl.change_face("bemused",Eyes="side")
                                ch_l "not that I mind the company. . ."
                                $ Girl.change_face("sexy")
                                ch_l "But you know, give me a heads up first."
                        elif Girl == JeanX:
                                $ Girl.change_face("bemused",Eyes="side")
                                ch_j "Well that was fun. . ."
                                $ Girl.change_face("sexy")
                                ch_j "So what brings you here? . ."
                        elif Girl == StormX:
                                ch_s "That was an interesting experience. . ."
                                $ Girl.change_face("bemused",Eyes="side")
                                ch_s "I certainly didn't mnd the attention. . ."
                                $ Girl.change_face("sexy")
                                ch_s "You might want to knock in future though."
                        elif Girl == JubesX:
                                ch_v "I don't usually get unexpected visitors . ."
                                $ Girl.change_face("bemused",Eyes="side")
                                ch_v "but I didn't mind the company. . ."
                                $ Girl.change_face("sexy")
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
