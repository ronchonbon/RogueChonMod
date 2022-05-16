
label Mall_Entry(First=0, Second=0, Girl=0, Cart=[]):
    call Jubes_Entry_Check
    $ Player.DrainWord("locked",0,0,1)
    $ bg_current = "bg_mall"
    $ Nearby = []
    call Gym_Clothes_Off
    call Taboo_Level
    $ Player.recent_history.append("traveling")
    call EventCalls

label Shopping_Mall(First=0, Second=0, Girl=0, Cart=[]):

    $ bg_current = "bg_mall"
    $ Player.recent_history.append("shopping")
    $ Player.daily_history.append("shopping")
    $ BO = Party[:]
    while BO:
        $ BO[0].location = "bg_mall"
        $ BO.remove(BO[0])

    call set_the_scene
    "You're at the Salem Centre Mall."
    if len(Party) >= 2:
        $ First = Party[0]
        $ Second = Party[1]
        "You wander the various stores with the girls, seeing what they have to offer. . ."
    elif len(Party) >= 1:
        $ First = Party[0]
        "You wander the various stores with [Party[0].name], seeing what they have to offer. . ."
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

        "Wait around a bit" if "date" not in Player.recent_history:

            "You wait around a bit."
            call Wait
            call EventCalls
            call Girls_Location
            if time_index >= 3:
                ch_u "The mall is now closing, please head to the nearest exit. . ."
                "You head back to campus."
                jump Campus_Entry

        "Head back to school" if "date" not in Player.recent_history:

            jump Campus_Entry


        "Just wander and window shop" if Party and Round > 20:

            if len(Party) >= 2:
                if renpy.random.randint(1, 20) > 10:
                    $ Party[0].change_stat("love", 80, 1)
                    $ Party[0].change_stat("obedience", 50, 1)
                    $ Party[0].change_stat("inhibition", 50, 1)
                    $ Party[1].change_stat("love", 80, 1)
                    $ Party[1].change_stat("obedience", 50, 1)
                    $ Party[1].change_stat("inhibition", 50, 1)
                "You wander around with the girls and see what they have available."
            else:
                if renpy.random.randint(1, 20) > 10:
                    $ Party[0].change_stat("love", 80, 1)
                    $ Party[0].change_stat("obedience", 50, 1)
                    $ Party[0].change_stat("inhibition", 50, 1)
                "You wander around with [Party[0].name]and see what they have available."
            $ Round -= 10

        "Do something else" if "date" in Player.recent_history and Round > 20:

            jump Date_Location

        "Head back to school" if "date" in Player.recent_history:

            if "movie" in Player.recent_history or "dinner" in Player.recent_history or Round < 30 or not Party:
                show blackscreen onlayer black with dissolve
                "It's getting late, you head back to the dorms. . ."
                jump Date_End
            else:

                if Party[0] in (EmmaX,StormX):
                    Party[0].voice "Oh, I was expecting more. . ."
                elif Party[0] in (JeanX,LauraX):
                    Party[0].voice "Is that it?"
                else:
                    Party[0].voice "Aw. . . we aren't doing anything else?"
                menu:
                    "Continue Shopping":
                        jump Mall_Menu
                    "Do something else":
                        jump Date_Location
                    "Head back to school [[seriously this time]":
                        ch_p "Yeah, let's head back."
                        Party[0].voice "Fine. . ."
                        show blackscreen onlayer black with dissolve
                        "It's getting late, you head back to the dorms. . ."
                        jump Date_End


    if time_index >= 3 or Round < 20:
        if "date" in Player.recent_history:

            show blackscreen onlayer black with dissolve
            "It's getting late, you head back to the dorms. . ."
            jump Date_End
        ch_u "The mall is now closing, please head to the nearest exit. . ."
        "You head back to campus."
        jump Campus_Entry
    jump Mall_Menu


label Sex_Shop:

    $ bg_current = "bg_shop"
    $ BO = Party[:]
    while BO:
        $ BO[0].location = "bg_shop"
        $ BO.remove(BO[0])

    call set_the_scene
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
                            $ First.change_face("sly")
                            $ First.change_stat("love", 80, 1)
                            $ First.change_stat("obedience", 50, 3)
                            $ First.change_stat("inhibition", 50, 3)
                            if First == RogueX:
                                ch_r "Oh, what's that for, [Girl.player_petname]?"
                            elif First == KittyX:
                                ch_k "Is that for. . ."
                            elif First == EmmaX:
                                ch_e "Hmm. . ."
                            elif First == LauraX:
                                ch_l ". . ."
                            elif First == JeanX:
                                pass
                            elif First == StormX:
                                ch_s "Well that's certainly interesting. . ."
                            elif First == JubesX:
                                ch_v "What're you gonna do with that. . ."
                        else:
                            $ First.change_face("confused",2)
                            $ First.change_stat("love", 60, -2)
                            $ First.change_stat("obedience", 70, 4)
                            $ First.change_stat("inhibition", 50, 2)
                            if First == RogueX:
                                ch_r "Is that. . . oh. . ."
                            elif First == KittyX:
                                ch_k "Um, what's that about. . ."
                            elif First == EmmaX:
                                ch_e "This is certainly an unusual trip. . ."
                            elif First == LauraX:
                                ch_l ". . ."
                            elif First == JeanX:
                                pass
                            elif First == StormX:
                                ch_s "Interesting choice. . ."
                            elif First == JubesX:
                                ch_v "What're you gonna do with that. . ."
                            $ First.change_face("confused",1)
                        $ First.change_stat("lust", 60, 5)
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
                            $ First.change_face("sly")
                            $ First.change_stat("love", 80, 2)
                            $ First.change_stat("obedience", 50, 2)
                            $ First.change_stat("inhibition", 50, 3)
                            if First == RogueX:
                                ch_r "Oh, what's that for, [Girl.player_petname]?"
                            elif First == KittyX:
                                ch_k "Is that for. . ."
                            elif First == EmmaX:
                                ch_e "Hmm. . ."
                            elif First == LauraX:
                                ch_l ". . ."
                            elif First == JeanX:
                                pass
                            elif First == StormX:
                                ch_s "Well that's certainly interesting. . ."
                            elif First == JubesX:
                                ch_v "What're you gonna do with that. . ."
                            $ First.change_stat("lust", 60, 5)
                        else:
                            $ First.change_face("confused",2)
                            $ First.change_stat("obedience", 70, 2)
                            $ First.change_stat("inhibition", 50, 2)
                            if First == RogueX:
                                ch_r "Is that. . . oh. . ."
                            elif First == KittyX:
                                ch_k "Um, what's that about. . ."
                            elif First == EmmaX:
                                ch_e "This is certainly an unusual trip. . ."
                            elif First == LauraX:
                                ch_l ". . ."
                            elif First == JeanX:
                                pass
                            elif First == StormX:
                                ch_s "Interesting choice. . ."
                            elif First == JubesX:
                                ch_v "What're you gonna do with that. . ."
                            $ First.change_face("confused",1)
                else:
                    "You don't have enough for that."
            "Give a gift to [First.name]." if First:
                $ Girl = First
            "Give a gift to [Second.name]." if Second:
                $ Girl = Second
            "Exit.":
                "You head back into the mall. . ."
                $ Round -= 10 if Round > 20 else (Round-10)
                $ Girl = 0
                $ bg_current = "bg_mall"
                $ BO = Party[:]
                while BO:
                    $ BO[0].location = "bg_mall"
                    $ BO.remove(BO[0])

                call set_the_scene
                return


        if Girl:
            menu:
                "Gift a Dildo" if "dildo" in Player.Inventory:

                    if "dildo" not in Girl.Inventory:
                        "You give [Girl.name] the dildo."
                        $ Girl.blushing = 1
                        $ Girl.ArmPose = 2
                        $ Girl.held_item = "dildo"
                        if ApprovalCheck(Girl, 800):
                            $ Girl.change_face("bemused")
                            $ Player.Inventory.remove("dildo")
                            $ Girl.Inventory.append("dildo")
                            $ Girl.change_stat("love", 200, 30)
                            $ Girl.change_stat("obedience", 200, 30)
                            $ Girl.change_stat("inhibition", 200, 30)
                            if Girl == RogueX:
                                ch_r "Well, I've got some ideas in mind for this. . ."
                            elif Girl == LauraX:
                                ch_l "Oh, cool, I've wanted one of these. . ."
                            else:
                                Girl.voice "I'm sure I can find some place to store it. . ."
                            $ Girl.change_stat("lust", 89, 10)
                        elif ApprovalCheck(Girl, 600):
                            $ Girl.change_face("confused")
                            $ Player.Inventory.remove("dildo")
                            $ Girl.Inventory.append("dildo")
                            if Girl != EmmaX:
                                $ Girl.change_stat("love", 200, 10)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 10)
                            if Girl == RogueX:
                                ch_r "Huh, well I guess I can find a place for it. . ."
                                $ Girl.change_stat("lust", 89, 10)
                                $ Girl.change_face("surprised")
                                ch_r "I- I mean. . . I'll just put it away."
                            elif Girl == KittyX:
                                ch_k "I don't know what. . ."
                                $ Girl.change_stat("lust", 89, 5)
                                $ Girl.change_stat("lust", 89, 10)
                                $ Girl.change_face("surprised")
                                ch_k "Oh!"
                                ch_k "Oh. . . I'll just[Girl.like]put it away."
                            elif Girl == EmmaX:
                                ch_e "This is not an appropriate gift from a student. . ."
                                $ Girl.change_stat("lust", 89, 5)
                                $ Girl.change_stat("lust", 89, 10)
                                $ Girl.change_face("sadside",1)
                                ch_e "Hm. . ."
                                $ Girl.change_stat("love", 200, 10)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 10)
                                $ Girl.change_face("sly")
                                ch_e "I suppose I can find {i}some{/i} use for it. . ."
                            elif Girl == LauraX:
                                ch_l "Huh, you're a weird gift giver."
                                $ Girl.change_stat("lust", 89, 5)
                                $ Girl.change_stat("lust", 89, 10)
                                $ Girl.change_face("smile")
                                ch_l "It's very thoughtful though."
                            elif Girl == JeanX:
                                $ Girl.change_stat("lust", 89, 5)
                                $ Girl.change_stat("lust", 89, 10)
                                ch_j "Well we know where your mind it at."
                                $ Girl.change_face("smile")
                                ch_j "I guess I should be flattered. . ."
                            elif Girl == StormX:
                                if StormX not in Rules:
                                    $ Girl.change_face("sadside",1)
                                    ch_s "I don't know that I should accept this from a student. . ."
                                $ Girl.change_stat("lust", 89, 5)
                                $ Girl.change_stat("lust", 89, 10)
                                ch_s "Hm. . ."
                                $ Girl.change_face("sly")
                                ch_s "Thank you for the thought. . ."
                            elif Girl == JubesX:
                                ch_v "I guess I have some use for it. . ."
                                $ Girl.change_stat("lust", 89, 10)
                                $ Girl.change_face("surprised")
                                ch_v "I- I mean. . . decorative."
                            $ Girl.change_face("bemused")
                        elif "offered gift" in Girl.daily_history:
                            $ Girl.change_face("angry")
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
                            $ Girl.change_face("angry")
                            $ Girl.change_stat("love", 50, -20)
                            $ Girl.change_stat("obedience", 20, 10)
                            $ Girl.change_stat("inhibition", 20, 20)
                            if Girl == RogueX:
                                ch_r "That's a pretty forward gift to be giving a lady. . ."
                            elif Girl == KittyX:
                                ch_k "I- you shouldn't be giving girls stuff like this!"
                            elif Girl == EmmaX:
                                ch_e "[Girl.player_petname], I don't believe this is an appropriate gift from a student."
                            elif Girl == LauraX:
                                ch_l "I don't think you should just be handing these out to random chicks."
                            elif Girl == JeanX:
                                ch_j "So you just go around handing out sex toys?"
                            elif Girl == StormX:
                                ch_s "I do not appreciate the implication here."
                            elif Girl == JubesX:
                                ch_v "This is an odd design for a. . . wait."
                            $ Girl.change_stat("lust", 89, 5)
                            "She hands it back to you."
                            $ Girl.daily_history.append("offered gift")
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
                            ch_r "Honestly, [Girl.player_petname], I already have enough of those."
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
                    $ Girl.held_item = 0
                    $ Girl.ArmPose = 2
                    $ Girl = 0

                "Gift a Dildo (locked)" if "dildo" not in Player.Inventory:
                    pass

                "Gift a Vibrator" if "vibrator" in Player.Inventory:

                    if "vibrator" not in Girl.Inventory:
                        "You give [Girl.name] the Shocker Vibrator."
                        $ Girl.blushing = 1
                        $ Girl.ArmPose = 2
                        $ Girl.held_item = "vibrator"
                        if ApprovalCheck(Girl, 700):
                            $ Girl.change_face("bemused")
                            $ Player.Inventory.remove("vibrator")
                            $ Girl.Inventory.append("vibrator")
                            $ Girl.change_stat("love", 200, 30)
                            $ Girl.change_stat("obedience", 200, 30)
                            $ Girl.change_stat("inhibition", 200, 30)
                            if Girl == RogueX:
                                ch_r "Well, I've got some ideas in mind for this. . ."
                            elif Girl == KittyX:
                                ch_k "Well this is. . . [[bzzzt]- "
                                ch_k "-interesting. . ."
                            elif Girl == EmmaX:
                                ch_e "How very thoughtful of you. . ."
                                $ Girl.change_stat("lust", 89, 10)
                                $ Girl.change_face("sly")
                                ch_e "I'm sure I can put this to good use. . ."
                            elif Girl == LauraX:
                                ch_l "This is. . . [[bzzzt]- "
                                $ Girl.change_stat("lust", 89, 10)
                                $ Girl.change_face("sly")
                                ch_l "-some kind of sex thing, huh. . ."
                            elif Girl == JeanX:
                                ch_j "Oh, nifty."
                            elif Girl == StormX:
                                ch_s "Oh!. . . oooohhh."
                            elif Girl == JubesX:
                                ch_v "Oh, this could be nice. . ."
                            $ Girl.change_stat("lust", 89, 10)
                        elif ApprovalCheck(Girl, 400):
                            $ Girl.change_face("confused")
                            $ Player.Inventory.remove("vibrator")
                            $ Girl.Inventory.append("vibrator")
                            $ Girl.change_stat("love", 200, 10)
                            $ Girl.change_stat("obedience", 200, 10)
                            $ Girl.change_stat("inhibition", 200, 10)
                            if Girl == RogueX:
                                ch_r "I guess I can use this to work the kinks out. . ."
                                $ Girl.change_stat("lust", 89, 10)
                                $ Girl.change_face("surprised")
                                ch_r "Muscle knots, I mean!"
                            elif Girl == KittyX:
                                ch_k "I've heard these are very relaxing. . ."
                                $ Girl.change_stat("lust", 89, 10)
                                $ Girl.change_face("surprised")
                                ch_k "-for my back!"
                            elif Girl == EmmaX:
                                ch_e "How very thoughtful of you. . ."
                                $ Girl.change_stat("lust", 89, 10)
                                $ Girl.change_face("sly")
                                ch_e "A back massager, I assume. . ."
                            elif Girl == LauraX:
                                ch_l "This is. . . [[bzzzt]- "
                                $ Girl.change_face("sly")
                                $ Girl.change_stat("lust", 89, 10)
                                ch_l "-oooh. . ."
                            elif Girl == JeanX:
                                ch_j "Huh. Ok."
                            elif Girl == StormX:
                                ch_s "Oh, something for exercise purposes. . ."
                            elif Girl == JubesX:
                                ch_v "Thanks, my, uh, back's been killing me. . ."
                            $ Girl.change_face("bemused", 1)
                        elif "offered gift" in Girl.daily_history:
                            $ Girl.change_face("angry")
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
                            $ Girl.change_face("angry")
                            $ Girl.change_stat("love", 50, -20)
                            $ Girl.change_stat("obedience", 20, 10)
                            $ Girl.change_stat("inhibition", 20, 20)
                            if Girl == RogueX:
                                ch_r "I don't think I have much use for that."
                            elif Girl == KittyX:
                                ch_k "I can't really see the point."
                            elif Girl == EmmaX:
                                ch_e "[Girl.player_petname], I don't believe this is an appropriate gift from a student."
                            elif Girl == LauraX:
                                ch_l "I don't need it."
                            elif Girl == JeanX:
                                ch_j "Huh. No, I don't need this."
                            elif Girl == StormX:
                                ch_s "I have no use for this."
                            elif Girl == JubesX:
                                ch_v "Put that away. . ."
                            $ Girl.change_stat("lust", 89, 5)
                            "She hands it back to you."
                            $ Girl.daily_history.append("offered gift")
                    else:
                        if Girl == RogueX:
                            ch_r "[Girl.player_petname], I only need the one."
                        elif Girl == EmmaX:
                            ch_e "I already have plenty."
                        else:
                            Girl.voice "I already have one of these."
                    $ Girl.held_item = 0
                    $ Girl.ArmPose = 2
                    $ Girl = 0

                "Gift a Vibrator (locked)" if "vibrator" not in Player.Inventory:
                    pass
                "Never Mind":

                    $ Girl = 0

    return



label Swim_Shop:





    $ bg_current = "bg_shop"
    $ BO = Party[:]
    while BO:
        $ BO[0].location = "bg_shop"
        $ BO.remove(BO[0])

    call set_the_scene
    $ Girl = 0
    "You head into \"The Swimsuit Issue\". . ."
    while True:
        if Round <= 20:
            "It's getting late, you head back into the mall. . ."
            $ Girl = 0
            return
        menu:
            "What did you want to do?"
            "Have [First.name] try something on." if First:
                $ Girl = First
            "Have [Second.name] try something on." if Second:

                $ Girl = Second
                $ Second = First
                $ First = Girl
            "Exit.":
                "You head back into the mall. . ."
                $ Girl = 0
                $ bg_current = "bg_mall"
                $ BO = Party[:]
                while BO:
                    $ BO[0].location = "bg_mall"
                    $ BO.remove(BO[0])

                call set_the_scene
                return


        if Girl:

            $ Girl.change_face("smile",1)
            if Girl.Swim[0]:

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


        if Girl:

            "You grab some things and head into one of the dressing rooms with [Girl.name]."
            $ bg_current = "bg_dressing"
            $ Girl.location = "bg_dressing"
            if Second:

                "Should [Second.name] come too?"
                menu:
                    "Sure":
                        "[Second.name] follows you in."
                        $ Second.location = "bg_dressing"
                    "Probably not.":
                        ch_p "[Second.name], probably hang back."
                        Second.voice "Fine. I'll just wait here then."
            if Second and Second.location == bg_current:

                call set_the_scene
            else:

                show blackscreen onlayer black
                call AllHide
                call Display_Background
                $ Girl.sprite_location = stage_center
                $ Girl.sprite_layer = 100
                call Display_Girl (Girl, 0, 0)

                hide blackscreen onlayer black
            $ Player.Traits.append("locked")
            call Taboo_Level

            while Girl:
                menu:
                    "What did you want to try on here?"
                    "Bikini Top (locked)" if Girl.bra == "bikini_top":
                        pass
                    "Bikini Top" if Girl.bra != "bikini_top":
                        if Girl.SeenChest or ApprovalCheck(Girl, 1100, TabM=2):
                            call Dressing_Strip_Bra ("bikini_top")
                        else:
                            Girl.voice "I'll need some privacy here. . ."
                            show blackscreen onlayer black
                            if Girl == JubesX:
                                $ Girl.accessory = 0
                            $ Girl.top = 0
                            $ Girl.bra = "bikini_top"
                            "You back out of the room for a moment. . ."
                            hide blackscreen onlayer black
                        if "bikini_top" in Cart:
                            pass
                        elif "bikini_top" in Girl.Inventory:
                            Girl.voice "I do already have one of these though."
                        else:
                            $ Cart.append("bikini_top")
                            if Girl == StormX and Girl.bra == "bikini_top" and Girl.underwear == "bikini_bottoms":
                                ch_s "Oh! I understand the purpose of the flap now!"



                    "Bikini Bottoms (locked)" if Girl.underwear == "bikini_bottoms":
                        pass
                    "Bikini Bottoms" if Girl.underwear != "bikini_bottoms":
                        if Girl.SeenPussy or ApprovalCheck(Girl, 1200, TabM=2):
                            call Dressing_Strip_Panties ("bikini_bottoms")
                        else:
                            Girl.voice "I'll need some privacy here. . ."
                            show blackscreen onlayer black
                            $ Girl.legs = 0
                            $ Girl.hose = 0
                            $ Girl.underwear = "bikini_bottoms"
                            "You back out of the room for a moment. . ."
                            hide blackscreen onlayer black
                        if "bikini_bottoms" in Cart:
                            pass
                        elif "bikini_bottoms" in Girl.Inventory:
                            Girl.voice "I do already have one of these though."
                        else:
                            $ Cart.append("bikini_bottoms")
                            if Girl == StormX and Girl.bra == "bikini_top" and Girl.underwear == "bikini_bottoms":
                                ch_s "Oh! I understand the purpose of the flap now!"



                    "Blue swim skirt (locked)" if Girl == KittyX and Girl.legs == "blue_skirt":
                        pass
                    "Blue swim_skirt" if Girl == KittyX and Girl.legs != "blue_skirt":
                        $ Girl.change_face("smile")
                        if (Girl.underwear and ApprovalCheck(Girl, 900, TabM=2)) or ApprovalCheck(Girl, 1200, TabM=2):
                            Girl.voice "Sure. . ."
                            $ Girl.Upskirt = 1
                            pause 0.3
                            $ Girl.legs = 0
                            call expression Girl.Tag + "_First_Bottomless"
                            pause 0.3
                            $ Girl.legs = "blue_skirt"
                            $ Girl.Upskirt = 0
                        else:
                            Girl.voice "I'll need some privacy here. . ."
                            show blackscreen onlayer black
                            $ Girl.legs = "blue_skirt"
                            "You back out of the room for a moment. . ."
                            hide blackscreen onlayer black
                        if "blue_skirt" in Cart:
                            pass
                        elif "blue_skirt" in Girl.Inventory:
                            Girl.voice "I do already have one of these though."
                        else:
                            $ Cart.append("blue_skirt")
                    "Leave Dressing Area.":

                        if Cart and Second:
                            if Second.location == bg_current and Second not in (LauraX,JeanX) and Second.GirlLikeCheck(Girl) >= 500:
                                $ Second.change_face("smile")
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

                                $ Girl.change_face("smile")
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


                        $ Girl.change_outfit(Changed=0)
                        $ Round -= 20 if Round > 30 else (Round-10)
                        $ Player.DrainWord("locked",0,0,1)
                        $ bg_current = "bg_shop"
                        $ BO = Party[:]
                        while BO:
                            $ BO[0].location = "bg_shop"
                            $ BO.remove(BO[0])

                        call Taboo_Level
                        call set_the_scene
                        if not Cart:
                            "That was fun, but since there wasn't anything she was interested in, she put it all back."
                        if Player.Cash < 50:
                            "You don't have enough cash on you, so you have to put everything back."
                            $ Girl.change_face("sad")
                            if "shopblock" not in Girl.daily_history:
                                $ Girl.change_stat("love", 50, -2)
                                $ Girl.change_stat("love", 90, -2)
                                $ Girl.change_stat("obedience", 50, 3)
                                $ Girl.change_stat("obedience", 80, 3)
                                $ Girl.AddWord(1,"shopblock","shopblock")
                            if Girl in (EmmaX,StormX):
                                Girl.voice "How disappointing."
                            elif Girl in (JeanX,LauraX):
                                pass
                            else:
                                Girl.voice "Aw. . ."
                            $ Cart = []

                        while Cart:
                            menu:
                                "So what did you want to buy?"
                                "The_top" if "bikini_top" in Cart:
                                    "You agree to buy [Girl.name] the bikini top."
                                    if Girl.Tag + " bikini_top" in Player.Inventory:
                                        "Wait, you already have one of those."
                                        "You pull out the one in your bag."
                                        $ Player.Inventory.remove(Girl.Tag + " bikini_top")
                                    elif Girl in (KittyX,EmmaX,StormX):
                                        if Player.Cash < 60:
                                            "You look at the tag, and actually, it's $60, you can't afford it."
                                            $ Cart.remove("bikini_top")
                                        else:
                                            $ Player.Cash -= 60
                                    elif Player.Cash < 50:
                                        "You look at the tag, and actually, it's $50, you can't afford it."
                                        $ Cart.remove("bikini_top")
                                    else:
                                        $ Player.Cash -= 50
                                    if "bikini_top" in Cart:

                                        $ Cart.remove("bikini_top")
                                        $ Girl.change_face("bemused",1)
                                        $ Girl.Inventory.append("bikini_top")
                                        $ Player.AddWord(1,"purchased")
                                        $ Girl.change_stat("love", 200, 20)
                                        $ Girl.change_stat("obedience", 200, 10)
                                        $ Girl.change_stat("inhibition", 200, 5)
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


                                "The_bottoms" if "bikini_bottoms" in Cart:
                                    "You agree to buy [Girl.name] the bikini bottoms."
                                    if Girl.Tag + " bikini_bottoms" in Player.Inventory:
                                        "Wait, you already have those."
                                        "You pull out the pair in your bag."
                                        $ Player.Inventory.remove(Girl.Tag + " bikini_bottoms")
                                    elif Girl in (KittyX,EmmaX,StormX):
                                        if Player.Cash < 60:
                                            "You look at the tag, and actually, it's $60, you can't afford it."
                                            $ Cart.remove("bikini_bottoms")
                                        else:
                                            $ Player.Cash -= 60
                                    elif Player.Cash < 50:
                                        "You look at the tag, and actually, it's $50, you can't afford it."
                                        $ Cart.remove("bikini_bottoms")
                                    else:
                                        $ Player.Cash -= 50
                                    if "bikini_bottoms" in Cart:

                                        $ Cart.remove("bikini_bottoms")
                                        $ Girl.change_face("bemused",1)
                                        $ Girl.Inventory.append("bikini_bottoms")
                                        $ Player.AddWord(1,"purchased")
                                        $ Girl.change_stat("love", 200, 20)
                                        $ Girl.change_stat("obedience", 200, 10)
                                        $ Girl.change_stat("inhibition", 200, 5)
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


                                "The_skirt" if "blue_skirt" in Cart:
                                    "You agree to buy [Girl.name] the blue skirt."
                                    if Girl.Tag + " blue_skirt" in Player.Inventory:
                                        "Wait, you already have one of those."
                                        "You pull out the one in your bag."
                                        $ Player.Inventory.remove(Girl.Tag + " blue_skirt")
                                    if Player.Cash < 50:
                                        "You look at the tag, and actually, it's $50, you can't afford it."
                                        $ Cart.remove("blue_skirt")
                                    else:
                                        $ Player.Cash -= 50
                                    if "blue_skirt" in Cart:

                                        $ Cart.remove("blue_skirt")
                                        $ Girl.change_face("bemused",1)
                                        $ Girl.Inventory.append("blue_skirt")
                                        $ Player.AddWord(1,"purchased")
                                        $ Girl.change_stat("love", 200, 20)
                                        $ Girl.change_stat("obedience", 200, 10)
                                        $ Girl.change_stat("inhibition", 200, 5)
                                        ch_k "This is a cute skirt. . ."


                                "Nothing" if "purchased" not in Player.recent_history:
                                    $ Girl.change_face("sad")
                                    if "shopblock" not in Girl.daily_history:
                                        $ Girl.change_stat("love", 50, -2)
                                        $ Girl.change_stat("love", 90, -2)
                                        $ Girl.change_stat("obedience", 50, 3)
                                        $ Girl.change_stat("obedience", 80, 3)
                                        $ Girl.AddWord(1,"shopblock","shopblock")
                                    "You put all the stuff back."
                                    if Girl in (EmmaX,StormX):
                                        Girl.voice "How disappointing."
                                    elif Girl in (JeanX,LauraX):
                                        pass
                                    else:
                                        Girl.voice "Aw. . ."
                                    $ Cart = []
                                "Nothing else" if "purchased" in Player.recent_history:
                                    $ Girl.change_face("sad")
                                    if "shopblock" not in Girl.daily_history:
                                        $ Girl.change_stat("love", 50, -1)
                                        $ Girl.change_stat("obedience", 50, 3)
                                        $ Girl.change_stat("obedience", 90, 2)
                                    "You put all the remaining stuff back."
                                    $ Cart = []



                        $ Player.DrainWord("purchased")
                        if Girl == KittyX and ("blue_skirt" in Girl.Inventory or Girl.inhibition >= 400) and "bikini_top" in Girl.Inventory and "bikini_bottoms" in Girl.Inventory:
                            $ Girl.Swim[0] = 1
                        elif "bikini_top" in Girl.Inventory and "bikini_bottoms" in Girl.Inventory:
                            $ Girl.Swim[0] = 1
                        $ Girl = 0



    return



label Lingerie_Shop:





    $ bg_current = "bg_shop"
    $ BO = Party[:]
    while BO:
        $ BO[0].location = "bg_shop"
        $ BO.remove(BO[0])

    call set_the_scene
    $ Girl = 0
    "You head into \"Stacy's\". . ."
    while True:
        if Round <= 20:
            "It's getting late, you head back into the mall. . ."
            $ Girl = 0
            return
        menu:
            "What did you want to do?"
            "Have [First.name] try something on." if First:
                $ Girl = First
            "Have [Second.name] try something on." if Second:

                $ Girl = Second
                $ Second = First
                $ First = Girl
            "Exit.":
                "You head back into the mall. . ."
                $ Girl = 0
                $ bg_current = "bg_mall"
                $ BO = Party[:]
                while BO:
                    $ BO[0].location = "bg_mall"
                    $ BO.remove(BO[0])
                call set_the_scene
                return


        if Girl:

            $ Girl.change_face("smile",1)
            if ApprovalCheck(Girl, 800) or ApprovalCheck(Girl, 600, "L") or ApprovalCheck(Girl, 300, "O"):

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


        if Girl:

            "You grab some things and head into one of the dressing rooms with [Girl.name]."
            $ bg_current = "bg_dressing"
            $ Girl.location = "bg_dressing"
            if Second:

                "Should [Second.name] come too?"
                menu:
                    "Sure":
                        "[Second.name] follows you in."
                        $ Second.location = "bg_dressing"
                    "Probably not.":
                        ch_p "[Second.name], probably hang back."
                        Second.voice "Fine. I'll just wait here then."
            if Second and Second.location == bg_current:

                call set_the_scene
            else:

                show blackscreen onlayer black
                call AllHide
                call Display_Background
                $ Girl.sprite_location = stage_center
                $ Girl.sprite_layer = 100
                call Display_Girl (Girl, 0, 0)

                hide blackscreen onlayer black
            $ Player.Traits.append("locked")
            call Taboo_Level

            while Girl:
                menu:
                    "What did you want to try on here?"
                    "Lace Bra (locked)" if Girl.bra == "lace_bra":
                        pass
                    "Lace Bra" if Girl.bra != "lace_bra" and Girl != LauraX:
                        if "no_gift_bra" in Girl.recent_history:
                            Girl.voice "I said no. . ."
                        elif not Girl.SeenChest and not ApprovalCheck(Girl, 900):
                            $ Girl.change_face("angry",2)
                            if Girl in (EmmaX,StormX):
                                Girl.voice "I don't think that would be appropriate."
                            elif Girl in (JeanX,LauraX):
                                Girl.voice "No thanks. . ."
                            else:
                                Girl.voice "Um, no, definitely not. . ."
                            $ Girl.change_face("angry",1)
                            $ Girl.recent_history.append("no_gift_bra")
                        else:
                            if Girl.SeenChest or ApprovalCheck(Girl, 1000, TabM=2):
                                call Dressing_Strip_Bra ("lace_bra")
                            else:
                                Girl.voice "I'll need some privacy here. . ."
                                show blackscreen onlayer black
                                if Girl == JubesX:
                                    $ Girl.accessory = 0
                                $ Girl.top = 0
                                $ Girl.bra = "lace_bra"
                                "You back out of the room for a moment. . ."
                                hide blackscreen onlayer black
                            if "lace_bra" in Cart:
                                pass
                            elif "lace_bra" in Girl.Inventory:
                                Girl.voice "I do already have one of these though."
                            else:
                                $ Cart.append("lace_bra")


                    "Corset (locked)" if Girl.bra == "corset":
                        pass
                    "Corset" if Girl.bra != "corset" and Girl in (LauraX,JeanX):
                        if "no_gift_bra" in Girl.recent_history:
                            Girl.voice "I said no. . ."
                        elif not Girl.SeenChest and not ApprovalCheck(Girl, 900):
                            $ Girl.change_face("angry",2)
                            if Girl in (EmmaX,StormX):
                                Girl.voice "I don't think that would be appropriate."
                            elif Girl in (JeanX,LauraX):
                                Girl.voice "No thanks. . ."
                            else:
                                Girl.voice "Um, no, definitely not. . ."
                            $ Girl.change_face("angry",1)
                            $ Girl.recent_history.append("no_gift_bra")
                        else:
                            if Girl.SeenChest or ApprovalCheck(Girl, 1000, TabM=2):
                                call Dressing_Strip_Bra ("corset")
                            else:
                                Girl.voice "I'll need some privacy here. . ."
                                show blackscreen onlayer black
                                if Girl == JubesX:
                                    $ Girl.accessory = 0
                                $ Girl.top = 0
                                $ Girl.bra = "corset"
                                "You back out of the room for a moment. . ."
                                hide blackscreen onlayer black
                            if "corset" in Cart:
                                pass
                            elif "corset" in Girl.Inventory:
                                Girl.voice "I do already have one of these though."
                            else:
                                $ Cart.append("corset")


                    "Lace Corset (locked)" if Girl.bra == "lace corset":
                        pass
                    "Lace Corset" if Girl.bra != "lace corset" and Girl == LauraX:
                        if "no_gift_bra" in Girl.recent_history:
                            Girl.voice "I said no. . ."
                        elif not Girl.SeenChest and not ApprovalCheck(Girl, 900):
                            $ Girl.change_face("angry",2)
                            if Girl in (EmmaX,StormX):
                                Girl.voice "I don't think that would be appropriate."
                            elif Girl in (JeanX,LauraX):
                                Girl.voice "No thanks. . ."
                            else:
                                Girl.voice "Um, no, definitely not. . ."
                            $ Girl.change_face("angry",1)
                            $ Girl.recent_history.append("no_gift_bra")
                        else:
                            if Girl.SeenChest or ApprovalCheck(Girl, 1000, TabM=2):
                                call Dressing_Strip_Bra ("lace corset")
                            else:
                                Girl.voice "I'll need some privacy here. . ."
                                show blackscreen onlayer black
                                if Girl == JubesX:
                                    $ Girl.accessory = 0
                                $ Girl.top = 0
                                $ Girl.bra = "lace corset"
                                "You back out of the room for a moment. . ."
                                hide blackscreen onlayer black
                            if "lace corset" in Cart:
                                pass
                            elif "lace corset" in Girl.Inventory:
                                Girl.voice "I do already have one of these though."
                            else:
                                $ Cart.append("lace corset")

                    "Lace Panties (locked)" if Girl.underwear == "lace_panties":
                        pass
                    "Lace Panties" if Girl.underwear != "lace_panties":
                        if "no_gift_panties" in Girl.recent_history:
                            Girl.voice "I said no. . ."
                        elif not Girl.SeenPussy and not ApprovalCheck(Girl, 1000):
                            $ Girl.change_face("angry",2)
                            if Girl in (EmmaX,StormX):
                                Girl.voice "I don't think that would be appropriate."
                            elif Girl in (JeanX,LauraX):
                                Girl.voice "No thanks. . ."
                            else:
                                Girl.voice "Um, no, definitely not. . ."
                            $ Girl.change_face("angry",1)
                            $ Girl.recent_history.append("no_gift_panties")
                        else:
                            if Girl.SeenPussy or ApprovalCheck(Girl, 1200, TabM=2):
                                call Dressing_Strip_Panties ("lace_panties")
                            else:
                                Girl.voice "I'll need some privacy here. . ."
                                show blackscreen onlayer black
                                $ Girl.legs = 0
                                $ Girl.hose = 0
                                $ Girl.underwear = "lace_panties"
                                "You back out of the room for a moment. . ."
                                hide blackscreen onlayer black
                            if "lace_panties" in Cart:
                                pass
                            elif "lace_panties" in Girl.Inventory:
                                Girl.voice "I do already have these though."
                            else:
                                $ Cart.append("lace_panties")


                    "Tiger-Striped Panties (locked)" if Girl.underwear == "tiger_panties":
                        pass
                    "Tiger-Striped Panties" if Girl.underwear != "tiger_panties" and Girl == JubesX:
                        if "no_gift_panties" in Girl.recent_history:
                            Girl.voice "I said no. . ."
                        elif not Girl.SeenPussy and not ApprovalCheck(Girl, 1000):
                            $ Girl.change_face("angry",2)
                            Girl.voice "Um, no, not really interested. . ."
                            $ Girl.change_face("angry",1)
                            $ Girl.recent_history.append("no_gift_panties")
                        else:
                            if Girl.SeenPussy or ApprovalCheck(Girl, 1200, TabM=2):
                                call Dressing_Strip_Panties ("tiger_panties")
                            else:
                                Girl.voice "I'll need some privacy here. . ."
                                show blackscreen onlayer black
                                $ Girl.legs = 0
                                $ Girl.hose = 0
                                $ Girl.underwear = "tiger_panties"
                                "You back out of the room for a moment. . ."
                                hide blackscreen onlayer black
                            if "tiger_panties" in Cart:
                                pass
                            elif "tiger_panties" in Girl.Inventory:
                                Girl.voice "I do already have these though."
                            else:
                                $ Cart.append("tiger_panties")


                    "Stockings and Garterbelt (locked)" if Girl.hose == "stockings_and_garterbelt":
                        pass
                    "Stockings and Garterbelt" if Girl.hose != "stockings_and_garterbelt":
                        if Girl.SeenPussy or ApprovalCheck(Girl, 900, TabM=2):
                            $ Girl.change_face("sexy")
                            Girl.voice "Sure. . ."
                            $ Girl.Upskirt = 1
                            pause 0.3
                            $ Girl.legs = 0
                            pause 0.3
                            $ Girl.hose = 0
                            call expression Girl.Tag + "_First_Bottomless"
                            pause 0.3
                            $ Girl.hose = "stockings_and_garterbelt"
                            $ Girl.underwearDown = 0
                            $ Girl.Upskirt = 0
                            if Second and "stockings_and_garterbelt" not in Cart:
                                $ Girl.GirlLikeUp(Second,1)
                                $ Second.GirlLikeUp(Girl,2)
                        else:
                            Girl.voice "I'll need some privacy here. . ."
                            show blackscreen onlayer black
                            $ Girl.hose = "stockings_and_garterbelt"
                            "You back out of the room for a moment. . ."
                            hide blackscreen onlayer black
                        if "stockings_and_garterbelt" in Cart:
                            pass
                        elif "stockings_and_garterbelt" in Girl.Inventory:
                            Girl.voice "I do already have these though."
                        else:
                            $ Cart.append("stockings_and_garterbelt")


                    "Knee Stockings (locked)" if Girl.hose == "knee stockings":
                        pass
                    "Knee Stockings" if Girl.hose != "knee stockings" and Girl == KittyX:
                        $ Girl.change_face("sexy")
                        Girl.voice "Sure. . ."
                        $ Girl.hose = 0
                        pause 0.3
                        $ Girl.hose = "knee stockings"
                        if "knee stockings" in Cart:
                            pass
                        elif "knee stockings" in Girl.Inventory:
                            Girl.voice "I do already have these though."
                        else:
                            $ Cart.append("knee stockings")


                    "High Socks (locked)" if Girl.hose == "socks":
                        pass
                    "High Socks" if Girl.hose != "socks" and Girl == JubesX:
                        $ Girl.change_face("sexy")
                        Girl.voice "Sure. . ."
                        $ Girl.hose = 0
                        pause 0.3
                        $ Girl.hose = "socks"
                        if "socks" in Cart:
                            pass
                        elif "socks" in Girl.Inventory:
                            Girl.voice "I do already have these though."
                        else:
                            $ Cart.append("socks")


                    "Pantyhose (locked)" if Girl.hose == "pantyhose":
                        pass
                    "Pantyhose" if Girl.hose != "pantyhose" and Girl != LauraX:
                        if Girl.SeenPussy or ApprovalCheck(Girl, 900, TabM=2):
                            $ Girl.change_face("sexy")
                            Girl.voice "Sure. . ."
                            $ Girl.Upskirt = 1
                            pause 0.3
                            $ Girl.legs = 0
                            pause 0.3
                            $ Girl.hose = 0
                            call expression Girl.Tag + "_First_Bottomless"
                            pause 0.3
                            $ Girl.hose = "pantyhose"
                            $ Girl.underwearDown = 0
                            $ Girl.Upskirt = 0
                            if Second and "pantyhose" not in Cart:
                                $ Girl.GirlLikeUp(Second,1)
                                $ Second.GirlLikeUp(Girl,2)
                        else:
                            Girl.voice "I'll need some privacy here. . ."
                            show blackscreen onlayer black
                            $ Girl.hose = "pantyhose"
                            "You back out of the room for a moment. . ."
                            hide blackscreen onlayer black
                        if "pantyhose" in Cart:
                            pass
                        elif "pantyhose" in Girl.Inventory:
                            Girl.voice "I do already have these though."
                        else:
                            $ Cart.append("pantyhose")


                    "Lose the [Girl.hose]" if Girl.hose:
                        if Girl.HoseNum() < 10 or ApprovalCheck(Girl, 900, TabM=2):
                            if Girl in (EmmaX,StormX):
                                Girl.voice "I suppose. . ."
                            else:
                                Girl.voice "Ok. . ."
                            $ Girl.hose = 0
                            call expression Girl.Tag + "_First_Bottomless"
                        else:
                            if Girl in (EmmaX,StormX):
                                Girl.voice "I do not think so. . ."
                            else:
                                Girl.voice "No thanks. . ."

                    "Nighty (locked)" if Girl.top == "nighty":
                        pass
                    "Nighty" if Girl.top != "nighty" and Girl == RogueX:
                        if "no_gift_bra" in Girl.recent_history:
                            Girl.voice "I said no. . ."
                        elif not Girl.SeenChest and not ApprovalCheck(Girl, 900):
                            $ Girl.change_face("angry",2)
                            if Girl in (EmmaX,StormX):
                                Girl.voice "I don't think that would be appropriate."
                            elif Girl in (JeanX,LauraX):
                                Girl.voice "No thanks. . ."
                            else:
                                Girl.voice "Um, no, definitely not. . ."
                            $ Girl.change_face("angry",1)
                            $ Girl.recent_history.append("no_gift_bra")
                        else:
                            if Girl.SeenChest or ApprovalCheck(Girl, 900, TabM=2):
                                $ Girl.change_face("sexy")
                                Girl.voice "Sure. . ."
                                if Girl == JubesX:
                                    $ Girl.accessory = 0
                                    pause 0.3                                                    
                                $ Girl.top = 0
                                call expression Girl.Tag + "_First_Topless"
                                call expression Girl.Tag + "_First_Bottomless" pass (1)
                                pause 0.3
                                $ Girl.top = "nighty"
                                pause 0.3
                                $ Girl.Uptop = 0
                                if Second and "nighty" not in Cart:
                                    $ Girl.GirlLikeUp(Second,1)
                                    $ Second.GirlLikeUp(Girl,3)
                            else:
                                Girl.voice "I'll need some privacy here. . ."
                                show blackscreen onlayer black
                                if Girl == JubesX:
                                    $ Girl.accessory = 0
                                $ Girl.top = "nighty"
                                "You back out of the room for a moment. . ."
                                hide blackscreen onlayer black
                            if "nighty" in Cart:
                                pass
                            elif "nighty" in Girl.Inventory:
                                Girl.voice "I do already have one of these though."
                            else:
                                $ Cart.append("nighty")
                    "Leave Dressing Area.":


                        if Cart and Second:
                            if Second.location == bg_current and Second not in (LauraX,JeanX) and Second.GirlLikeCheck(Girl) >= 500:
                                $ Second.change_face("sexy")
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

                                $ Girl.change_face("sexy")
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

                        $ Round -= 20 if Round > 30 else (Round-10)
                        $ Player.DrainWord("locked",0,0,1)
                        $ bg_current = "bg_shop"
                        $ BO = Party[:]
                        while BO:
                            $ BO[0].location = "bg_shop"
                            $ BO.remove(BO[0])

                        call Taboo_Level
                        call set_the_scene

                        $ Girl.change_outfit(Changed=0)
                        if not Cart:
                            "That was fun, but since there wasn't anything she was interested in, she put it all back."
                        if Player.Cash < 50:
                            "You don't have enough cash on you, so you have to put everything back."
                            $ Girl.change_face("sad")
                            if "shopblock" not in Girl.daily_history:
                                $ Girl.change_stat("love", 50, -2)
                                $ Girl.change_stat("love", 90, -2)
                                $ Girl.change_stat("obedience", 50, 3)
                                $ Girl.change_stat("obedience", 80, 3)
                                $ Girl.AddWord(1,"shopblock","shopblock")
                            if Girl in (EmmaX,StormX):
                                Girl.voice "How disappointing."
                            elif Girl in (JeanX,LauraX):
                                pass
                            else:
                                Girl.voice "Aw. . ."
                            $ Cart = []

                        while Cart:
                            menu:
                                "So what did you want to buy?"
                                "The lace_bra" if "lace_bra" in Cart:
                                    "You agree to buy [Girl.name] the lace bra."
                                    if Girl.Tag + " lace_bra" in Player.Inventory:
                                        "Wait, you already have one of those."
                                        "You pull out the one in your bag."
                                        $ Player.Inventory.remove(Girl.Tag + " lace_bra")
                                    elif Player.Cash < 90:
                                        "You look at the tag, and actually, it's $90, you can't afford it."
                                        $ Cart.remove("lace_bra")
                                    else:
                                        $ Player.Cash -= 90
                                    if "lace_bra" in Cart:

                                        $ Cart.remove("lace_bra")
                                        $ Girl.change_face("bemused",1)
                                        $ Girl.Inventory.append("lace_bra")
                                        $ Player.AddWord(1,"purchased")
                                        $ Girl.change_stat("love", 200, 25)
                                        $ Girl.change_stat("obedience", 200, 20)
                                        $ Girl.change_stat("inhibition", 200, 20)
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


                                "The corset" if "corset" in Cart:
                                    "You agree to buy [Girl.name] the corset."
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

                                        $ Cart.remove("corset")
                                        $ Girl.change_face("bemused",1)
                                        $ Girl.Inventory.append("corset")
                                        $ Player.AddWord(1,"purchased")
                                        $ Girl.change_stat("love", 200, 15)
                                        $ Girl.change_stat("obedience", 200, 20)
                                        $ Girl.change_stat("inhibition", 200, 10)
                                        if Girl == LauraX:
                                            ch_l "This is. . . kinda cool. . ."
                                        elif Girl == JeanX:
                                            ch_j "Thanks?"


                                "The lace corset" if "lace corset" in Cart:
                                    "You agree to buy [Girl.name] the lace corset."
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

                                        $ Cart.remove("lace corset")
                                        $ Girl.change_face("bemused",1)
                                        $ Girl.Inventory.append("lace corset")
                                        $ Player.AddWord(1,"purchased")
                                        $ Girl.change_stat("love", 200, 25)
                                        $ Girl.change_stat("obedience", 200, 30)
                                        $ Girl.change_stat("inhibition", 200, 20)
                                        ch_l "You think this'd look good on me?"


                                "The lace_panties" if "lace_panties" in Cart:
                                    "You agree to buy [Girl.name] the lace panties."
                                    if Girl.Tag + " lace_panties" in Player.Inventory:
                                        "Wait, you already have one of those."
                                        "You pull out the ones in your bag."
                                        $ Player.Inventory.remove(Girl.Tag + " lace_panties")
                                    elif Player.Cash < 110:
                                        "You look at the tag, and actually, they're $110, you can't afford them."
                                        $ Cart.remove("lace_panties")
                                    else:
                                        $ Player.Cash -= 110
                                    if "lace_panties" in Cart:

                                        $ Cart.remove("lace_panties")
                                        $ Girl.change_face("bemused",1)
                                        $ Girl.Inventory.append("lace_panties")
                                        $ Player.AddWord(1,"purchased")
                                        $ Girl.change_stat("love", 200, 25)
                                        $ Girl.change_stat("obedience", 200, 20)
                                        $ Girl.change_stat("inhibition", 200, 20)
                                        if Girl == RogueX:
                                            ch_r "These are a bit flimsy. . ."
                                        elif Girl == KittyX:
                                            ch_k "These don't leave much to the imagination. . ."
                                        elif Girl == EmmaX:
                                            ch_e "This is an. . . unsual gift."
                                            $ EmmaX.change_face("sly",1)
                                            ch_e "But I'll hold on to them. . ."
                                        elif Girl == LauraX:
                                            ch_l "These are pretty hot. . ."
                                        elif Girl == JeanX:
                                            ch_j "Oh, these are nice. . ."
                                        elif Girl == StormX:
                                            ch_s "I suppose I could always use another pair. . ."
                                        elif Girl == JubesX:
                                            ch_v "A little. . . intimate. . ."


                                "The tiger-striped_panties" if "tiger_panties" in Cart:
                                    "You agree to buy [Girl.name] the tiger panties."
                                    if Girl.Tag + " tiger_panties" in Player.Inventory:
                                        "Wait, you already have one of those."
                                        "You pull out the ones in your bag."
                                        $ Player.Inventory.remove(Girl.Tag + " tiger_panties")
                                    elif Player.Cash < 100:
                                        "You look at the tag, and actually, they're $100, you can't afford them."
                                        $ Cart.remove("tiger_panties")
                                    else:
                                        $ Player.Cash -= 100
                                    if "tiger_panties" in Cart:

                                        $ Cart.remove("tiger_panties")
                                        $ Girl.change_face("bemused",1)
                                        $ Girl.Inventory.append("tiger_panties")
                                        $ Player.AddWord(1,"purchased")
                                        $ Girl.change_stat("love", 200, 25)
                                        $ Girl.change_stat("obedience", 200, 20)
                                        $ Girl.change_stat("inhibition", 200, 20)
                                        ch_v "These are stink'in cute. . ."



                                "The stockings and garterbelt" if "stockings_and_garterbelt" in Cart:
                                    "You agree to buy [Girl.name] the stockings and garterbelt."
                                    if Girl.Tag + " stockings and garterbelt" in Player.Inventory:
                                        "Wait, you already have those."
                                        "You pull out the ones in your bag."
                                        $ Player.Inventory.remove(Girl.Tag + " stockings and garterbelt")
                                    elif Player.Cash < 100:
                                        "You look at the tag, and actually, they're $100, you can't afford them."
                                        $ Cart.remove("stockings_and_garterbelt")
                                    else:
                                        $ Player.Cash -= 100
                                    if "stockings_and_garterbelt" in Cart:

                                        $ Cart.remove("stockings_and_garterbelt")
                                        $ Girl.change_face("bemused",1)
                                        $ Girl.Inventory.append("stockings_and_garterbelt")
                                        $ Player.AddWord(1,"purchased")
                                        $ Girl.change_stat("love", 200, 5)
                                        $ Girl.change_stat("obedience", 200, 5)
                                        $ Girl.change_stat("inhibition", 200, 5)
                                        if Girl == EmmaX:
                                            ch_e "These are lovely. . ."
                                        elif Girl == StormX:
                                            ch_s "You think I could pull these off?"
                                        else:
                                            Girl.voice "These are pretty nice. . ."


                                "The knee stockings" if "knee stockings" in Cart:
                                    "You agree to buy [Girl.name] the knee stockings."
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

                                        $ Cart.remove("knee stockings")
                                        $ Girl.change_face("bemused",1)
                                        $ Girl.Inventory.append("knee stockings")
                                        $ Player.AddWord(1,"purchased")
                                        $ Girl.change_stat("love", 200, 5)
                                        $ Girl.change_stat("obedience", 200, 5)
                                        $ Girl.change_stat("inhibition", 200, 5)
                                        Girl.voice "These are pretty nice. . ."


                                "The high socks" if "socks" in Cart:
                                    "You agree to buy [Girl.name] the socks."
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

                                        $ Cart.remove("socks")
                                        $ Girl.change_face("bemused",1)
                                        $ Girl.Inventory.append("socks")
                                        $ Player.AddWord(1,"purchased")
                                        $ Girl.change_stat("love", 200, 5)
                                        $ Girl.change_stat("obedience", 200, 5)
                                        $ Girl.change_stat("inhibition", 200, 5)
                                        Girl.voice "These are pretty nice. . ."


                                "The_pantyhose" if "pantyhose" in Cart:
                                    "You agree to buy [Girl.name] the pantyhose."
                                    if Girl.Tag + "_pantyhose" in Player.Inventory:
                                        "Wait, you already have one of those."
                                        "You pull out the ones in your bag."
                                        $ Player.Inventory.remove(Girl.Tag + "_pantyhose")
                                    elif Player.Cash < 50:
                                        "You look at the tag, and actually, they're $50, you can't afford them."
                                        $ Cart.remove("pantyhose")
                                    else:
                                        $ Player.Cash -= 50
                                    if "pantyhose" in Cart:

                                        $ Cart.remove("pantyhose")
                                        $ Girl.change_face("bemused",1)
                                        $ Girl.Inventory.append("pantyhose")
                                        $ Player.AddWord(1,"purchased")
                                        $ Girl.change_stat("love", 200, 5)
                                        $ Girl.change_stat("obedience", 200, 5)
                                        $ Girl.change_stat("inhibition", 200, 5)
                                        Girl.voice "These are lovely. . ."


                                "The nighty" if "nighty" in Cart:
                                    "You agree to buy [Girl.name] the nighty."
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

                                        $ Cart.remove("nighty")
                                        $ Girl.change_face("bemused",1)
                                        $ Girl.Inventory.append("nighty")
                                        $ Player.AddWord(1,"purchased")
                                        $ Girl.change_stat("love", 200, 40)
                                        $ Girl.change_stat("obedience", 200, 20)
                                        $ Girl.change_stat("inhibition", 200, 30)
                                        ch_r "Well, it's a little revealing, but still pretty cute."
                                        $ Girl.change_stat("lust", 89, 10)


                                "Nothing" if "purchased" not in Player.recent_history:
                                    $ Girl.change_face("sad")
                                    if "shopblock" not in Girl.daily_history:
                                        $ Girl.change_stat("love", 50, -2)
                                        $ Girl.change_stat("love", 90, -2)
                                        $ Girl.change_stat("obedience", 50, 3)
                                        $ Girl.change_stat("obedience", 80, 3)
                                        $ Girl.AddWord(1,"shopblock","shopblock")
                                    "You put all the stuff back."
                                    if Girl in (EmmaX,StormX):
                                        Girl.voice "How disappointing."
                                    elif Girl in (JeanX,LauraX):
                                        pass
                                    else:
                                        Girl.voice "Aw. . ."
                                    $ Cart = []
                                "Nothing else" if "purchased" in Player.recent_history:
                                    $ Girl.change_face("sad")
                                    if "shopblock" not in Girl.daily_history:
                                        $ Girl.change_stat("love", 50, -1)
                                        $ Girl.change_stat("obedience", 50, 3)
                                        $ Girl.change_stat("obedience", 90, 2)
                                    "You put all the remaining stuff back."
                                    $ Cart = []



                        $ Player.DrainWord("purchased")
                        $ Girl = 0


    return



label Dressing_Strip_Bra(Item=0):


    if not Item:
        return
    $ Girl.change_face("sexy")
    Girl.voice "Sure. . ."
    if Girl.top or Girl.bra:
        $ Girl.Uptop = 1
        pause 0.3
    if Girl == JubesX and Girl.accessory:
        $ Girl.accessory = 0
        pause 0.3 
    if Girl.top:
        $ Girl.top = 0
        pause 0.3
    if Girl.bra:
        $ Girl.bra = 0
    call expression Girl.Tag + "_First_Topless"
    pause 0.3
    $ Girl.bra = Item
    pause 0.3
    $ Girl.Uptop = 0
    if Second and Item not in Cart:
        $ Girl.GirlLikeUp(Second,2)
        $ Second.GirlLikeUp(Girl,5)
    Girl.voice ". . ."
    return

label Dressing_Strip_Panties(Item=0):


    if not Item:
        return
    $ Girl.change_face("sexy")
    Girl.voice "Sure. . ."
    if Girl.legs:
        $ Girl.Upskirt = 1
        pause 0.3
        $ Girl.legs = 0
        pause 0.3
    if Girl.hose:
        $ Girl.hose = 0
        pause 0.3
    if Girl.underwear:
        $ Girl.underwearDown = 1
        pause 0.2
        $ Girl.underwear = 0
    call expression Girl.Tag + "_First_Bottomless"
    pause 0.3
    $ Girl.underwear = Item
    $ Girl.underwearDown = 0
    $ Girl.Upskirt = 0
    if Second and Item not in Cart:
        $ Girl.GirlLikeUp(Second,3)
        $ Second.GirlLikeUp(Girl,5)
    Girl.voice ". . ."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
