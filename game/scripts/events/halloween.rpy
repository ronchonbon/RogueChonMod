
label Halloween_chat(Girl=0):

    show black_screen onlayer black
    if Girl == RogueX and renpy.showing("Rogue_sprite standing"):
        pass
    elif Girl == KittyX and renpy.showing("Kitty_sprite standing"):
        pass
    elif Girl == EmmaX and renpy.showing("Emma_sprite standing"):
        pass
    elif Girl == LauraX and renpy.showing("Laura_sprite standing"):
        pass
    elif Girl == JeanX and renpy.showing("Jean_sprite standing"):
        pass
    elif Girl == StormX and renpy.showing("Storm_sprite standing"):
        pass
    else:
        "You approach [Girl.name]"
        call hide_all
        while Present:

            $ Nearby.append(Present[0])
            $ Present[0].location = "nearby"
            $ Present.remove(Present[0])

        $ Nearby.remove(Girl)
        $ Present.append(Girl)

        call add_Girls(Girl)
    hide black_screen onlayer black

    if Girl == EmmaX and "classcaught" not in EmmaX.history:
        jump Emma_HWchat_Minimal

    if Girl == RogueX:
        ch_r "So what did you want to talk about, [Girl.player_petname]?"
    elif Girl == KittyX:
        ch_k "So[Girl.like]what did you want to talk about, [Girl.player_petname]?"
    elif Girl == EmmaX:
        ch_e "What was it you wanted to discuss, [Girl.player_petname]?"
    elif Girl == LauraX:
        ch_l "Yeah?"
    elif Girl == JeanX:
        ch_j "What is it?"
    elif Girl == StormX:
        ch_s "What can I do for you, [Girl.player_petname]?"

    call Halloween_chat_Menu
    return



label Halloween_chat_Menu:
    $ Girl = check_girl(Girl)
    $ Girl.change_face()
    $ shift_focus (Girl)

    if "angry" in Girl.recent_history:
        if Girl == RogueX:
            ch_r "I really don't want to talk to you right now."
        elif Girl == KittyX:
            ch_k "I'm[Girl.like]so mad at you right now!"
        elif Girl == EmmaX:
            ch_e "I would not press my luck if I were you."
        elif Girl == LauraX:
            ch_l "You don't want to be around me right now."
        elif Girl == JeanX:
            ch_j "Get away from me."
        elif Girl == StormX:
            ch_s "You do not want to tangle with me right now."
        return

    menu:
        "Romance her":
            menu:
                "Flirt with her":


                    call Flirt (Girl)
                    return

                "Sex Menu (locked)" if Girl.location != Player.location:
                    pass
                "Sex Menu" if Girl.location == Player.location:
                    if Girl.love >= Girl.obedience:
                        ch_p "Did you want to fool around?"
                    else:
                        ch_p "I'd like to get naughty."
                    if "angry" in Girl.recent_history:
                        if Girl == RogueX:
                            ch_r "I don't want to deal with you right now."
                        elif Girl == KittyX:
                            ch_k "Not even!"
                        elif Girl == EmmaX:
                            ch_e "You should know better than that."
                        elif Girl == LauraX:
                            ch_l "Bad idea right now."
                        elif Girl == JeanX:
                            ch_j "-So- not interested."
                        elif Girl == StormX:
                            ch_s "I am uninterested."
                    elif approval_check(Girl, 800):
                        $ Girl.change_face("sexy")
                        if Girl == RogueX:
                            ch_r "Heh, maybe after the party, [Girl.player_petname]?"
                        elif Girl == KittyX:
                            ch_k "Ha! I wouldn't wanna to ruin the party [Girl.player_petname]."
                        elif Girl == EmmaX:
                            ch_e "Oh, and get grass stains on this dress?"
                        elif Girl == LauraX:
                            ch_l "Heh, maybe later."
                        elif Girl == JeanX:
                            ch_j "I'm kinda busy with the party right now."
                        elif Girl == StormX:
                            ch_s "Perhaps later, [Girl.player_petname]"
                    else:
                        if Girl == RogueX:
                            ch_r "I'm not really interested, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k "No thanks, [Girl.player_petname]."
                        elif Girl == EmmaX:
                            ch_e "No thank you, [Girl.player_petname]."
                        elif Girl == LauraX:
                            ch_l "No thanks, [Girl.player_petname]."
                        elif Girl == JeanX:
                            ch_j "Not interested."
                        elif Girl == StormX:
                            ch_s "I am uninterested."
                    return
                "Dirty Talk (locked)":

                    pass
                "Date (locked)":
                    pass
                "Gifts (locked)":

                    pass
                "Back":
                    pass
        "Talk with her":

            menu:
                "I just wanted to talk. . .":
                    call expression Girl.tag + "_Chitchat"
                    return
                "Relationship status":
                    ch_p "Could we talk about us?"
                    if Girl == RogueX:
                        ch_r "That sounds like it might be a little heavy for a party."
                        ch_r "Maybe later?"
                    elif Girl == KittyX:
                        ch_k "That seems like something we'd want to do after the party."
                        ch_k "Maybe later?"
                    elif Girl == EmmaX:
                        ch_e "This seems a bit serious to discuss during a party."
                        ch_e "Later, perhaps."
                    elif Girl == LauraX:
                        ch_l "Sounds heavy."
                        ch_l "Maybe later?"
                    elif Girl == JeanX:
                        ch_j "That sounds like a conversation to have when we're -not- at a party?"
                    elif Girl == StormX:
                        ch_s "That seems like a conversation that we should not have at a party."
                        ch_s "Perhaps at a later date."
                    return
                "Other girls":

                    menu:
                        "How do you feel about [RogueX.name]?" if Girl != RogueX:
                            call expression Girl.tag + "_About" pass (RogueX)
                        "How do you feel about [KittyX.name]?" if Girl != KittyX and "met" in KittyX.history:
                            call expression Girl.tag + "_About" pass (KittyX)
                        "How do you feel about [EmmaX.name]?" if Girl != EmmaX and "met" in EmmaX.history:
                            call expression Girl.tag + "_About" pass (EmmaX)
                        "How do you feel about [LauraX.name]?" if Girl != LauraX and "met" in LauraX.history:
                            call expression Girl.tag + "_About" pass (LauraX)
                        "How do you feel about [JeanX.name]?" if Girl != JeanX and "met" in JeanX.history:
                            call expression Girl.tag + "_About" pass (JeanX)
                        "How do you feel about [StormX.name]?" if Girl != StormX and "met" in StormX.history:
                            call expression Girl.tag + "_About" pass (StormX)
                        "About hooking up with other girls. . .":
                            call expression Girl.tag + "_Monogamy"
                        "Never mind.":
                            pass
                "Back":

                    pass
        "Change her":

            call change_girl(Girl)
        "Never mind.":

            if Girl == RogueX:
                ch_r "Ok, later then."
            elif Girl == KittyX:
                ch_k "Ok, bye."
            elif Girl == EmmaX:
                ch_e "We'll talk later then."
            elif Girl == LauraX:
                ch_l "Ok."
            elif Girl == JeanX:
                ch_j "Ok?"
            elif Girl == StormX:
                ch_s "Very well then."
            return
    jump Halloween_chat_Menu


label Emma_HWchat_Minimal:
    $ EmmaX.change_face()
    $ shift_focus (EmmaX)
    menu:
        ch_e "What was it you wished to discuss, [EmmaX.player_petname]?"
        "Romance her":
            menu:
                "Flirt with her (locked)" if EmmaX.had_chat[5]:
                    pass
                "Flirt with her" if not EmmaX.had_chat[5]:
                    call Emma_Flirt_Minimal
                "Sex Menu":
                    ch_p "Did you want to fool around?"
                    ch_e "With a student? You should know better than that, [EmmaX.player_petname]."
                "Back":
                    pass
        "Talk to her":
            menu:
                "I just wanted to talk. . .":
                    call Emma_Chitchat
                "Relationship status":
                    ch_p "Could we talk about us?"
                    ch_e "I'm not sure that's an appropriate discussion at the moment."
                "Back":
                    pass
        "Change [EmmaX.name]":
            ch_p "Let's talk about you."
            ch_e "I doubt that's any of your business."
        "Never mind.":
            $ EmmaX.change_face("bemused", 2)
            ch_e "Very well. . ."
            ch_e "I have some. . . business to attend to."
            return
    jump Emma_HWchat_Minimal


label HWchange_stat(Girl=0, HWType=0, HWCheck=0, HWvalue=0, HWStore=0):



    if Girl not in all_Girls:
        return
    $ HWStore = getattr(Girl,HWType)
    call change_Girl_stat(Girl, HWType,HWCheck,HWvalue)
    if "halloween" in Girl.history:
        $ setattr(Girl, HWType, HWStore)
    return


label Halloween_Party_entry(HWEvents = [], halloween_costume=0, HWline = []):





    $ Player.location = "bg_halloween"
    call remove_all

    $ Player.Party = []
    $ Present = []
    $ Nearby = []
    "You enter the university square, where the party seems to be in full swing."
    "The various students are wandering around in costume, there seems to be a lot of dancing going on, and some food tables set up."


    "[RogueX.name] walks up to you."



    $ Present.append(RogueX)
    $ RogueX.location = "bg_halloween"
    $ RogueX.add_word(1, 0,RogueX.Clothes["hair"], 0, "halloween")
    $ RogueX.outfitday = "costume"
    $ RogueX.outfit_name = RogueX.outfitday
    $ RogueX.change_Outfit()

    $ shift_focus (RogueX)
    show Rogue_sprite standing at sprite_location(1200, 50):
        offset (0, 0)
        anchor (0.5, 0.0)
        pos (1200, 50)
        ease 0.8 pos (stage_center, 50)
    pause 0.8

    $ RogueX.change_face("smile")
    ch_r "Hey, [RogueX.player_petname], nice to see ya made it."
    $ RogueX.change_face("smile", eyes = "down")
    ch_r "Looks like you're dressed as. . ."
    $ RogueX.change_face("smile")
    menu:
        extend ""
        "A pirate":
            call HWchange_stat (RogueX, "love", 90, 2)
            call HWchange_stat (RogueX, "inhibition", 50, 1)
            call HWchange_stat (RogueX, "inhibition", 80, 1)
            call HWchange_stat (RogueX, "lust", 50, 2)
            $ halloween_costume = 1
        "A ninja":
            call HWchange_stat (RogueX, "love", 70, 1)
            call HWchange_stat (RogueX, "love", 80, 1)
            $ halloween_costume = 2
        "A fireman":
            call HWchange_stat (RogueX, "love", 70, 1)
            call HWchange_stat (RogueX, "love", 80, 1)
            call HWchange_stat (RogueX, "lust", 50, 1)
            $ halloween_costume = 3
        "No costume":
            call HWchange_stat (RogueX, "love", 80, -2)
            call HWchange_stat (RogueX, "obedience", 50, 1)
            call HWchange_stat (RogueX, "inhibition", 50, 1)
            $ RogueX.change_face("confused")

    $ HWline = ["Oh. . . that's sorta what I figured. . .", "Well \"Ahoy\" to you then.", "Oooh, dangerous. . .", "Well I've certainly got a fire for you to put out. . ."]
    $ HWline = HWline[halloween_costume]
    ch_r "[HWline]"
    if not halloween_costume:
        $ RogueX.change_face("smile")
        ch_r "Still, welcome to the party, I suppose. . ."
    ch_r "Can ya guess what I'm going as?"
    menu:
        extend ""
        "Ada?":
            $ RogueX.change_face("confused")
            call HWchange_stat (RogueX, "love", 80, -2)
            ch_r "Well, close, you got the game right at least."
            $ RogueX.change_face("normal")
            call HWchange_stat (RogueX, "inhibition", 50, 3)
            call HWchange_stat (RogueX, "inhibition", 70, 2)
            ch_r "But no, it's Jill, actually."
        "Jill?":
            call HWchange_stat (RogueX, "love", 80, 2)
            call HWchange_stat (RogueX, "love", 90, 2)
            call HWchange_stat (RogueX, "inhibition", 50, 1)
            $ RogueX.change_face("smile", eyes = "surprised")
            pause 0.4
            $ RogueX.change_face("smile")
            ch_r "Sure'nuff, [RogueX.player_petname]. You know your characters."
        "Some sort of hooker?":
            if approval_check(RogueX, 1600) or approval_check(RogueX, 700, "O"):
                $ RogueX.change_face("perplexed", 2)
                call HWchange_stat (RogueX, "love", 90, -1)
                ch_r "Wha. . . "
                call HWchange_stat (RogueX, "obedience", 90, 2)
                ch_r ". . ."
                $ RogueX.change_face("sexy", 1)
                call HWchange_stat (RogueX, "love", 90, 1)
                call HWchange_stat (RogueX, "lust", 50, 2)
                ch_r "I suppose if that's what you like to see. . ."
            elif approval_check(RogueX, 1300):
                $ RogueX.change_face("angry", eyes = "side")
                call HWchange_stat (RogueX, "love", 70, -2)
                call HWchange_stat (RogueX, "love", 90, -2)
                call HWchange_stat (RogueX, "obedience", 50, 1)
                ch_r "I'm gonna pretend I didn't hear that. . ."
                call HWchange_stat (RogueX, "obedience", 70, 1)
                call HWchange_stat (RogueX, "inhibition", 50, -2)
            else:
                $ RogueX.change_face("angry")
                call HWchange_stat (RogueX, "love", 70, -2)
                call HWchange_stat (RogueX, "love", 90, -2)
                ch_r "You are really pushing your luck [RogueX.player_petname]. . ."
                call HWchange_stat (RogueX, "obedience", 50, 1)
                call HWchange_stat (RogueX, "obedience", 50, 1)
            ch_r "Anyway, it's actually Jill, from that zombie game."
        "No clue.":
            call HWchange_stat (RogueX, "love", 80, -2)
            call HWchange_stat (RogueX, "love", 90, -1)
            call HWchange_stat (RogueX, "inhibition", 50, 1)
            ch_r "Well. . . it's Jill, from that zombie game."
        "Skip the intros." if "halloween" in Player.history:
            menu:
                "Are you sure you want to skip the remaining inros and go straight to the party?"
                "Yes":
                    jump Halloween_Skip
                "Never mind":
                    ch_p "Sorry, I spaced out there."
    menu:
        extend ""
        "Looks nice.":
            $ RogueX.change_face("smile")
            call HWchange_stat (RogueX, "love", 80, 1)
            call HWchange_stat (RogueX, "love", 90, 2)
            ch_r "Well thank 'ya kindly, [RogueX.player_petname]."
            call HWchange_stat (RogueX, "inhibition", 50, 2)
            call HWchange_stat (RogueX, "inhibition", 60, 1)
        "Looks sexy.":
            $ RogueX.change_face("sexy", 1)
            call HWchange_stat (RogueX, "love", 80, 3)
            call HWchange_stat (RogueX, "obedience", 80, 2)
            call HWchange_stat (RogueX, "lust", 60, 2)
            ch_r "Oooh, glad ya enjoy it. . ."
            call HWchange_stat (RogueX, "inhibition", 60, 3)
        "Love the hair.":
            $ RogueX.change_face("smile", 1)
            call HWchange_stat (RogueX, "love", 80, 2)
            call HWchange_stat (RogueX, "love", 90, 2)
            call HWchange_stat (RogueX, "inhibition", 50, 2)
            ch_r "Aw, thanks [RogueX.player_petname]."
            call HWchange_stat (RogueX, "inhibition", 70, 2)
            ch_r "I like it too."
        "Ok, so have you seen [KittyX.name]?" if "met" in KittyX.history:
            $ RogueX.change_face("angry", brows = "confused")
            call HWchange_stat (RogueX, "love", 80, -2)
            call HWchange_stat (RogueX, "lust", 50, -2)
            ch_r ". . ."
            call HWchange_stat (RogueX, "obedience", 70, 2)
            call HWchange_stat (RogueX, "obedience", 90, 1)
            call HWchange_stat (RogueX, "inhibition", 70, 2)
            ch_r "Yeah. I seen'er."
            $ RogueX.change_face("angry", eyes = "side")
            ch_r "You'll find her over there."
    ch_r "Anyway, I gotta get moving, I'll see you later. . ."
    $ RogueX.change_face("smile")
    $ Present.remove(RogueX)
    $ Nearby.append(RogueX)
    $ RogueX.location = "nearby"
    show Rogue_sprite standing:
        ease 0.8 pos (-200, 50)
    pause 0.8
    "[RogueX.name] heads over to mingle some more."
    call hide_all


    if "met" not in KittyX.history:
        jump Halloween_Party





    $ Present.append(KittyX)
    $ KittyX.location = "bg_halloween"
    $ KittyX.add_word(1, 0, KittyX.Clothes["hair"], 0, "halloween")
    $ KittyX.outfitday = "costume"
    $ KittyX.outfit_name = KittyX.outfitday
    $ KittyX.change_Outfit()

    $ shift_focus (KittyX)
    show Kitty_sprite standing at sprite_location(1200, 50):
        offset (0, 0)
        anchor (0.5, 0.0)
        pos (1200, 50)
        ease 0.8 pos (stage_center, 50)
    pause 0.8

    $ KittyX.change_face("confused", eyes = "down")
    "Over by the snack table, you find [KittyX.name], looking through the chips."
    $ KittyX.change_face("smile")
    ch_k "Oh, hey!"
    $ KittyX.change_face("smile", eyes = "down")
    ch_k "Lemme guess who you are. . ."
    $ KittyX.change_face("smile")
    $ HWline = [Player.name + " Right?", "A mysterious sailor. . .", "Oooh, dangerous assassin. . .", "A noble hero."]
    $ HWline = HWline[halloween_costume]
    ch_k "[HWline]"
    menu:
        extend ""
        "Yup.":
            call HWchange_stat (KittyX, "love", 80, 1)
            call HWchange_stat (KittyX, "love", 90, 1)
            ch_k "Got it in one."
        "Good guess.":
            call HWchange_stat (KittyX, "love", 80, 2)
            call HWchange_stat (KittyX, "love", 90, 1)
            call HWchange_stat (KittyX, "inhibition", 50, 1)
            ch_k "Aw, thanks."
        "No, it's [Player.name].":
            $ KittyX.change_face("confused")
            call HWchange_stat (KittyX, "love", 70, -1)
            call HWchange_stat (KittyX, "obedience", 50, -1)
            if not halloween_costume:
                ch_k ". . . riiight?"
            else:
                ch_k "No[KittyX.like]I know what your name is, I meant. . ."
            ch_k "Whatever."
        "Skip the intros." if "halloween" in Player.history:
            menu:
                "Are you sure you want to skip the remaining inros and go straight to the party?"
                "Yes":
                    jump Halloween_Skip
                "Never mind":
                    ch_p "Sorry, I spaced out there."
    $ KittyX.change_face("smile")
    ch_k "Anyway, can ya guess what I am?"
    menu:
        extend ""
        "Aerith":
            call HWchange_stat (KittyX, "love", 60, 4)
            call HWchange_stat (KittyX, "love", 80, 2)
            call HWchange_stat (KittyX, "love", 200, 2)
            ch_k "You got it!"
        "Little House on the Prarie?":
            $ KittyX.change_face("confused", eyes = "side")
            call HWchange_stat (KittyX, "love", 70, -1)
            call HWchange_stat (KittyX, "inhibition", 50, -1)
            ch_k "Huh? I guess it is a little. . . \"farmy.\""
            $ KittyX.change_face("sad")
            ch_k "But no, it's Aerith."
        "Kitty.":
            $ KittyX.change_face("confused")
            call HWchange_stat (KittyX, "love", 80, -1)
            call HWchange_stat (KittyX, "obedience", 30, -1)
            ch_k "I. . . Yes[KittyX.like]I am Kitty, but this is a costume I'm in."
            ch_k "You know. . . Halloween?"
            $ KittyX.change_face("confused", eyes = "stunned")
            call HWchange_stat (KittyX, "inhibition", 50, 3)
            call HWchange_stat (KittyX, "inhibition", 70, 3)
            ch_k "Geeze."
            $ KittyX.change_face("angry")
            ch_k "I'm dressed as Aerith!"
            $ KittyX.change_face("normal")
        "No?":
            $ KittyX.change_face("sad")
            call HWchange_stat (KittyX, "love", 70, -1)
            call HWchange_stat (KittyX, "obedience", 50, 1)
            call HWchange_stat (KittyX, "obedience", 60, 1)
            ch_k "Booo, you could at least try."
            $ KittyX.change_face("normal")
            ch_k "I'm dressed as Aerith!"
    menu:
        extend ""
        "Looks nice.":
            $ KittyX.change_face("smile")
            call HWchange_stat (KittyX, "love", 80, 2)
            call HWchange_stat (KittyX, "love", 90, 1)
            call HWchange_stat (KittyX, "obedience", 50, 1)
            ch_k "Ah, thank you, [KittyX.player_petname]."
            call HWchange_stat (KittyX, "inhibition", 50, 2)
        "Looks sexy.":
            $ KittyX.change_face("smile", 2)
            call HWchange_stat (KittyX, "love", 80, 1)
            call HWchange_stat (KittyX, "inhibition", 50, 2)
            ch_k "I thought it might be kinda plain. . ."
            $ KittyX.change_face("smile", 1, eyes = "side")
            call HWchange_stat (KittyX, "love", 90, 1)
            call HWchange_stat (KittyX, "obedience", 50, 1)
            ch_k "Next to some of the others, at least. . ."
            menu:
                extend ""
                "I'm curious what's underneath it.":
                    $ KittyX.change_face("sexy", 2)
                    call HWchange_stat (KittyX, "love", 60, -1)
                    call HWchange_stat (KittyX, "love", 90, 1)
                    call HWchange_stat (KittyX, "lust", 60, 3)
                    ch_k "Well, play your cards right. . ."
                    $ KittyX.blushing = "_blush1"
                    call HWchange_stat (KittyX, "obedience", 60, 1)
                    call HWchange_stat (KittyX, "obedience", 80, 2)
                    call HWchange_stat (KittyX, "inhibition", 70, 1)
                "Yeah, I guess you're right about that.":
                    $ KittyX.change_face("sad")
                    call HWchange_stat (KittyX, "love", 80, -1)
                    call HWchange_stat (KittyX, "love", 90, -1)
                    ch_k ". . . oh."
                    $ KittyX.change_face("sadside")
                    call HWchange_stat (KittyX, "obedience", 50, 1)
                    call HWchange_stat (KittyX, "obedience", 80, 1)
                    ch_k ". . ."
                    call HWchange_stat (KittyX, "inhibition", 50, 1)
                    ch_k "Well, I still like it."
                    $ KittyX.change_face("normal")
        "Love the hair.":
            $ KittyX.change_face("confused")
            call HWchange_stat (KittyX, "love", 70, -1)
            call HWchange_stat (KittyX, "love", 90, -1)
            ch_k "What? . . but I. . . Didn't do anything with my hair. . ."
            $ KittyX.change_face("normal")
        "Ok, so have you seen any of the other girls?" if "met" in EmmaX.history:
            $ KittyX.change_face("confused")
            call HWchange_stat (KittyX, "love", 80, -1)
            call HWchange_stat (KittyX, "obedience", 50, 1)
            call HWchange_stat (KittyX, "obedience", 60, 1)
            ch_k "Well. . ."
            $ KittyX.change_face("normal", eyes = "leftside")
            if "met" in LauraX.history:
                ch_k "Yeah, [LauraX.name]'s right over there."
                ch_k "Hey [LauraX.name]?!"
            else:
                ch_k "[KittyX.Like]not really?"
            $ KittyX.change_face("normal")



    if "met" not in LauraX.history:
        ch_k "Anyway, I was were[KittyX.like]going to check out the scene over there for a second."
        ch_k "Maybe I'll see you later, [KittyX.player_petname]."
        call hide_all
        $ Present.remove(KittyX)
        $ Nearby.append(KittyX)
        $ KittyX.location = "nearby"
        jump Halloween_Emma


    "[LauraX.name] looks up from the punch bowl and sees the two of you."
    show Kitty_sprite standing:
        ease 0.8 pos (1200, 50)
    pause 0.8


    $ Present.append(LauraX)
    $ LauraX.location = "bg_halloween"
    $ LauraX.add_word(1, 0,LauraX.Clothes["hair"], 0, "halloween")
    $ LauraX.outfitday = "costume"
    $ LauraX.outfit_name = LauraX.outfitday
    $ LauraX.change_Outfit()

    $ shift_focus (LauraX)
    show Laura_sprite standing at sprite_location(1200, 50):
        offset (0, 0)
        anchor (0.5, 0.0)
        pos (1200, 50)
        ease 0.8 pos (stage_center, 50)
    show Kitty_sprite standing:
        ease 0.8 pos (stage_far_right, 50)
    pause 0.8
    "She wanders over"

    $ LauraX.change_face("normal")
    ch_l "Oh, hey, [KittyX.name], [Player.name]."
    $ HWline = ["Like the look.", "Homeless person?", "Hand ninja?", "Lumberjack?"]
    $ HWline = HWline[halloween_costume]
    ch_l "[HWline]"
    if halloween_costume:
        menu:
            extend ""
            "Yeah.":
                call HWchange_stat (LauraX, "love", 80, 1)
                ch_l "Cool. Cool."
            "Nope.":
                $ LauraX.change_face("confused")
                call HWchange_stat (LauraX, "obedience", 50, 1)
                ch_l "Oh."
                if halloween_costume == 2:
                    call HWchange_stat (LauraX, "love", 80, -1)
                    call HWchange_stat (LauraX, "inhibition", 60, 1)
                    ch_l "Definitely looks like a Hand ninja."
                $ LauraX.change_face("normal")
            "Way off.":
                $ LauraX.change_face("confused")
                call HWchange_stat (LauraX, "love", 80, -1)
                call HWchange_stat (LauraX, "obedience", 70, 2)
                ch_l "Oh."
                if halloween_costume == 2:
                    call HWchange_stat (LauraX, "love", 80, -2)
                    call HWchange_stat (LauraX, "inhibition", 60, 2)
                    ch_l "It -definitely- looks like a Hand ninja though."
    $ KittyX.change_face("smile", eyes = "side")
    $ HWline = ["Right?", "He's a pirate, silly!", "Yeah, I guess he could be. . .", "It's a fireman, silly!"]
    $ HWline = HWline[halloween_costume]
    ch_k "[HWline]"
    $ KittyX.change_face("smile")
    ch_k "Now guess what [LauraX.name]'s going as!"
    menu:
        extend ""
        "A Boxer?":
            $ LauraX.change_face("normal", eyes = "down")
            ch_l ". . ."
            $ LauraX.change_face("normal")
            call HWchange_stat (LauraX, "love", 80, 1)
            ch_l "No."
            $ KittyX.change_face("angry")
            call HWchange_stat (KittyX, "love", 70, -2)
            call HWchange_stat (KittyX, "love", 90, 2)
            call HWchange_stat (KittyX, "inhibition", 50, 2)
            ch_k "She's Tifa!"
            $ KittyX.change_face("smile")
        "A prostitute?":
            $ LauraX.change_face("sad", 2)
            if approval_check(LauraX, 1600) or approval_check(LauraX, 700, "O"):

                call HWchange_stat (LauraX, "love", 80, -2)
                call HWchange_stat (LauraX, "love", 90, -3)
                ch_l "That is. . . hurtful. . ."
                call HWchange_stat (LauraX, "obedience", 80, 3)
                call HWchange_stat (LauraX, "obedience", 200, 1)
            else:
                call punch
                if "partyfix" in LauraX.history:
                    call HWchange_stat (LauraX, "love", 80, -2)
                    call HWchange_stat (LauraX, "love", 90, -3)
                    ch_l "Not this shit again!"
                    call HWchange_stat (LauraX, "obedience", 80, 3)
                    call HWchange_stat (LauraX, "obedience", 200, 1)
                elif "lover" in LauraX.player_petnames:

                    call HWchange_stat (LauraX, "love", 80, -2)
                    call HWchange_stat (LauraX, "love", 90, -3)
                    ch_l "You know better than that. . ."
                    call HWchange_stat (LauraX, "obedience", 80, 3)
                    call HWchange_stat (LauraX, "obedience", 200, 1)
                    $ LauraX.add_word(1, 0, 0, 0, "partyfoul")
                else:

                    call HWchange_stat (LauraX, "love", 80, -2)
                    call HWchange_stat (LauraX, "love", 90, -3)
                    ch_l ". . ."
                    ch_l "If you knew. . ."
                    $ LauraX.add_word(1, 0, 0, 0, "partyfoul")
                $ LauraX.change_face("angry")

                $ LauraX.add_word(1, "angry", "angry", 0, 0)


                ch_l "I don't have time for this."
                show Laura_sprite standing:
                    ease 0.8 pos (1200, 50)
                pause 0.8
                "[LauraX.name] stalks out of the party for the night."
                call remove_Girl(LauraX)

                $ KittyX.change_face("angry")
                call HWchange_stat (KittyX, "love", 70, 2)
                call HWchange_stat (KittyX, "love", 90, 2)
                ch_k "Well that was rude!"
                ch_k "I think I'm[KittyX.like]going to check out the scene over there for a second."
                show Kitty_sprite standing:
                    ease 0.8 pos (1200, 50)
                pause 0.8
                "[KittyX.name] heads off to the side."
                $ KittyX.change_face("normal")
                call hide_all
                $ Present.remove(KittyX)
                $ Nearby.append(KittyX)
                $ KittyX.location = "nearby"
                jump Halloween_Jean
        "Tifa?":

            $ KittyX.change_face("smile")
            $ LauraX.change_face("smile")
            call HWchange_stat (KittyX, "love", 60, 2)
            call HWchange_stat (KittyX, "love", 90, 1)
            call HWchange_stat (LauraX, "love", 90, 1)
            call HWchange_stat (LauraX, "inhibition", 50, 1)
            ch_l "Yes, apparently."
        "How should I know?":
            call HWchange_stat (LauraX, "love", 90, 1)
            call HWchange_stat (LauraX, "obedience", 50, 1)
            call HWchange_stat (LauraX, "inhibition", 50, 1)
            call HWchange_stat (LauraX, "inhibition", 70, 1)
            ch_l "Yeah, right?"
            $ KittyX.change_face("surprised")
            call HWchange_stat (KittyX, "love", 70, -1)
            call HWchange_stat (KittyX, "love", 90, -2)
            ch_k "She's Tifa!"
            $ KittyX.change_face("smile")
        "Skip the intros." if "halloween" in Player.history:
            menu:
                "Are you sure you want to skip the remaining inros and go straight to the party?"
                "Yes":
                    jump Halloween_Skip
                "Never mind":
                    ch_p "Sorry, I spaced out there."


    ch_k "We're wearing buddy costumes!"
    ch_l ". . . yeah."
    ch_l "Apparently."
    menu:
        extend ""
        "It looks great!":
            $ LauraX.change_face("smile")
            call HWchange_stat (LauraX, "love", 70, 1)
            call HWchange_stat (LauraX, "love", 90, 1)
            call HWchange_stat (LauraX, "inhibition", 60, 2)
            ch_l "Yeah, I guess so."
        "Love the suspenders.":
            $ LauraX.change_face("normal", eyes = "down")
            call HWchange_stat (LauraX, "love", 70, 1)
            call HWchange_stat (LauraX, "love", 90, 1)
            ch_l "Oh?"
            $ LauraX.change_face("smile")
            $ LauraX.Clothes["suspenders"] = "suspenders2"
            call HWchange_stat (LauraX, "inhibition", 50, 1)
            call HWchange_stat (LauraX, "inhibition", 60, 1)
            ch_l "Yeah. . ."
            $ LauraX.Clothes["suspenders"] = "suspenders"
        "How is that different from your normal look?":
            $ LauraX.change_face("normal", eyes = "down")
            call HWchange_stat (LauraX, "love", 80, -1)
            call HWchange_stat (LauraX, "obedience", 50, 1)
            ch_l ". . ."
            call HWchange_stat (LauraX, "inhibition", 50, -1)
            ch_l "Well. . . the top is white now. And the skirt doesn't have buckles."
            $ LauraX.change_face("normal")
            call HWchange_stat (LauraX, "love", 80, -1)
            call HWchange_stat (LauraX, "inhibition", 50, -1)
            ch_l "Also the suspenders."
    ch_k "Anyway, we were[KittyX.like]going to check out the scene over there for a second."
    $ LauraX.change_face("normal", eyes = "leftside")
    ch_l "We were?"
    ch_k "Yes. Come on."
    ch_k "Later, [KittyX.player_petname]!"
    show Kitty_sprite standing:
        ease 0.8 pos (1200, 50)
    show Laura_sprite standing:
        ease 0.8 pos (1200, 50)
    pause 0.8
    "[KittyX.name] tugs [LauraX.name] off to the side."
    $ LauraX.change_face("normal")

    call hide_all
    $ Present.remove(KittyX)
    $ Nearby.append(KittyX)
    $ KittyX.location = "nearby"
    $ Present.remove(LauraX)
    $ Nearby.append(LauraX)
    $ LauraX.location = "nearby"



label Halloween_Jean:

    if "met" not in JeanX.history:
        "Well that seemed a bit rushed."
        jump Halloween_Emma
    "You can see [JeanX.name] heading toward the table."
    "Oooooooooh. . . ok."
    "She appears to be shouting back at someone in a baseball cap, Rusty, maybe?"
    ch_j "I don't -care- that you \"gotta catch'em all,\" you're still not in my league!"


    $ Present.append(JeanX)
    $ JeanX.location = "bg_halloween"
    $ JeanX.add_word(1, 0,JeanX.Clothes["hair"], 0, "halloween")
    $ JeanX.outfitday = "costume"
    $ JeanX.outfit_name = JeanX.outfitday
    $ JeanX.change_Outfit()

    $ shift_focus (JeanX)
    show Jean_sprite standing at sprite_location(1200, 50):
        offset (0, 0)
        anchor (0.5, 0.0)
        pos (1200, 50)
        ease 0.8 pos (stage_center, 50)
    pause 0.8

    $ JeanX.change_face("angry", eyes = "side")
    ch_j ". . ."
    $ JeanX.change_face("normal", brows = "angry")
    ch_j "Oh, hey. . . you look familiar."
    $ line = JeanX.player_petname
    menu:
        extend ""
        "It's me, [Player.name].":
            $ JeanX.change_face("normal")
            call HWchange_stat (JeanX, "love", 90, 1)
            call HWchange_stat (JeanX, "inhibition", 50, 1)
            ch_j "Oh. Yeah. Hello, [JeanX.player_petname]."
            ch_j "I almost didn't recognize you."
        "It's me, [Player.name], I'm a pirate." if halloween_costume == 1:
            $ JeanX.change_face("normal")
            call HWchange_stat (JeanX, "love", 90, 1)
            call HWchange_stat (JeanX, "inhibition", 50, 1)
            ch_j "Oh, ok. Hello \"Pirate.\""
            $ JeanX.player_petname = "Pirate"
        "A pirate." if halloween_costume == 1:
            $ JeanX.change_face("normal")
            call HWchange_stat (JeanX, "inhibition", 50, 1)
            ch_j "Oh. Yeah. Hello, [JeanX.player_petname]."
            ch_j "I thought you were a drag queen."
        "It's me, [Player.name], I'm a ninja." if halloween_costume == 2:
            $ JeanX.change_face("normal")
            call HWchange_stat (JeanX, "love", 90, 1)
            call HWchange_stat (JeanX, "inhibition", 50, 1)
            ch_j "Oh. Yeah. Hello, [JeanX.player_petname]."
            ch_j "I thought you were a stage hand."
        "A ninja." if halloween_costume == 2:
            $ JeanX.change_face("normal")
            call HWchange_stat (JeanX, "inhibition", 50, 1)
            ch_j "Oh, ok. Hello \"Ninja.\""
            $ JeanX.player_petname = "Ninja"
        "It's me, [Player.name], I'm a fireman." if halloween_costume == 3:
            $ JeanX.change_face("normal")
            call HWchange_stat (JeanX, "love", 90, 1)
            call HWchange_stat (JeanX, "inhibition", 50, 1)
            ch_j "Oh. Yeah. Hello, [JeanX.player_petname]."
            $ JeanX.change_face("normal", brows = "angry")
            ch_j ". . ."
            $ JeanX.change_face("confused")
            ch_j "I thought you had \"power cancelling\" powers."
            ch_j "It's fire now?"
            $ JeanX.add_word(1, "fire", 0)
        "A fireman." if halloween_costume == 3:
            call HWchange_stat (JeanX, "love", 90, 1)
            call HWchange_stat (JeanX, "obedience", 50, 1)
            call HWchange_stat (JeanX, "inhibition", 50, 1)
            ch_j "Oh, ok. Hello \"Fire Man.\""
            $ JeanX.player_petname = "Fire Man"
            $ JeanX.add_word(1, "fire", 0)
        "Skip the intros." if "halloween" in Player.history:
            menu:
                "Are you sure you want to skip the remaining inros and go straight to the party?"
                "Yes":
                    jump Halloween_Skip
                "Never mind":
                    ch_p "Sorry, I spaced out there."
    if "fire" in JeanX.recent_history:
        menu:
            extend ""
            "No, I'm dressed like someone who puts -out- fires.":
                $ JeanX.change_face("surprised")
                call HWchange_stat (JeanX, "love", 90, -1)
                call HWchange_stat (JeanX, "obedience", 50, 2)
                ch_j ". . ."
                $ JeanX.change_face("normal")
                call HWchange_stat (JeanX, "obedience", 90, 1)
                ch_j ". . . of course you are."
                $ JeanX.change_face("smile")
                call HWchange_stat (JeanX, "inhibition", 80, -1)
                ch_j "I was kidding."
            "Yes. Yes, I totally have fire powers now.":
                $ JeanX.change_face("normal")
                call HWchange_stat (JeanX, "obedience", 30, 1)
                call HWchange_stat (JeanX, "obedience", 70, 1)
                ch_j "Wild."
                call HWchange_stat (JeanX, "love", 70, 2)
                call HWchange_stat (JeanX, "love", 90, 1)
                call HWchange_stat (JeanX, "lust", 50, 1)
                ch_j "I had fire powers once."
                $ JeanX.change_face("angry", eyes = "side")
                ch_j "It didn't go well."
                ch_j "Small minded fools."

    if JeanX.player_petname in ("Pirate", "Ninja", "Fire Man"):
        menu:
            extend ""
            "And my name's [Player.name], remember?":
                $ JeanX.change_face("normal")
                call HWchange_stat (JeanX, "love", 90, 1)
                call HWchange_stat (JeanX, "obedience", 50, 1)
                call HWchange_stat (JeanX, "obedience", 70, 1)
                ch_j "Oh. Right. [line]."
                $ JeanX.player_petname = line
                $ line = 0
            "And you call me [line], remember?" if line != Player.name:
                $ JeanX.change_face("normal")
                call HWchange_stat (JeanX, "love", 70, 1)
                call HWchange_stat (JeanX, "love", 90, 1)
                call HWchange_stat (JeanX, "obedience", 70, 1)
                ch_j "Oh. Right. [line]."
                $ JeanX.player_petname = line
                $ line = 0
            "Leave it":
                $ JeanX.change_face("normal")
                call HWchange_stat (JeanX, "inhibition", 50, 1)
    "You look her costume up and down."
    menu:
        "You look her costume up and down."
        "So what's that look?":
            $ JeanX.change_face("smile", eyes = "side")
            call HWchange_stat (JeanX, "love", 70, 1)
            ch_j "Oh. . . I whammied some nerd to make me a costume with red hair."
            $ JeanX.change_face("normal")
            ch_j "I don't know what it's from, but I guess it's fine."
            menu:
                extend ""
                "Yeah, I don't know either.":
                    call HWchange_stat (JeanX, "love", 90, 1)
                    call HWchange_stat (JeanX, "obedience", 50, 1)
                    call HWchange_stat (JeanX, "obedience", 70, 1)
                "It's Misty.":
                    call HWchange_stat (JeanX, "love", 90, -1)
                    call HWchange_stat (JeanX, "obedience", 30, -1)
                    call HWchange_stat (JeanX, "inhibition", 50, 2)
                    ch_j "Oh, ok nerd."
        "Is that supposed to be Misty?":
            $ JeanX.change_face("confused")
            call HWchange_stat (JeanX, "love", 90, -1)
            call HWchange_stat (JeanX, "obedience", 30, -1)
            call HWchange_stat (JeanX, "inhibition", 50, 2)
            ch_j "Who's \"Misty?\""
            $ JeanX.change_face("angry", eyes = "side")
            ch_j "Is that the girl with the water powers?"
            $ JeanX.change_face("angry", mouth = "surprised")
            ch_j "Wait, -do- we have a girl with water powers?"
            $ JeanX.change_face("normal")
            ch_j "Anyway. . . I whammied some nerd to make me a costume with red hair."
            ch_j "Is this her?"
            menu:
                extend ""
                "Yeah, I don't know either.":
                    call HWchange_stat (JeanX, "love", 90, 1)
                    call HWchange_stat (JeanX, "obedience", 50, 1)
                    call HWchange_stat (JeanX, "obedience", 70, 1)
                "It's Misty.":
                    call HWchange_stat (JeanX, "love", 90, -1)
                    call HWchange_stat (JeanX, "obedience", 30, -1)
                    call HWchange_stat (JeanX, "inhibition", 50, 2)
                    ch_j "Oh, ok nerd."
        ". . . [[don't even ask]":
            pass

    menu:
        extend ""
        "You look great.":
            $ JeanX.change_face("smile")
            call HWchange_stat (JeanX, "love", 70, 2)
            call HWchange_stat (JeanX, "love", 90, 1)
            call HWchange_stat (JeanX, "obedience", 70, 1)
            ch_j "Yeah? That's not a shocker."
            call HWchange_stat (JeanX, "inhibition", 50, 1)
            ch_j "I make anything look good."
        "I like the hair style.":
            $ JeanX.change_face("smile")
            call HWchange_stat (JeanX, "love", 70, 1)
            call HWchange_stat (JeanX, "love", 90, 1)
            call HWchange_stat (JeanX, "obedience", 70, 1)
            ch_j "Big surprise."
            call HWchange_stat (JeanX, "inhibition", 50, 2)
            ch_j "I can even make a side-pony work."
        "Why didn't you go as \"Jessie?\"":
            $ JeanX.change_face("normal", mouth = "kiss")
            call HWchange_stat (JeanX, "obedience", 50, 1)
            ch_j ". . ."
            ch_j "Who's \"Jessie?!\""
            $ JeanX.change_face("angry", eyes = "side")
            "She looks around and locks eyes with one of the other students."
            $ JeanX.change_face("angry", eyes = "psychic")
            ch_j "Who's \"Jessie?\""
            $ JeanX.change_face("normal", eyes = "psychic")
            ch_j ". . ."
            $ JeanX.change_face("surprised")
            call HWchange_stat (JeanX, "inhibition", 50, 1)
            ch_j "Oh. . . she looks pretty bad ass."
            $ JeanX.change_face("angry", eyes = "side")
            call HWchange_stat (JeanX, "inhibition", 50, 1)
            ch_j "I probably should have gone as her."
            $ JeanX.change_face("normal", eyes = "psychic")
            call HWchange_stat (JeanX, "obedience", 70, 1)
            call HWchange_stat (JeanX, "inhibition", 70, 1)
            ch_j "Everyone just picture me as \"Jessie\" for the rest of the party."
            $ JeanX.change_face("smile", eyes = "surprised")
            call HWchange_stat (JeanX, "inhibition", 70, 2)
            "You hear mumbles of \"yes, Jessie\". . ."
            $ JeanX.add_word(1, "jessie", 0)
    $ JeanX.change_face("smile")
    show Jean_sprite standing:
        ease 1 pos (300, 50)
    pause 1
    "[JeanX.name] starts to wander off."
    menu:
        extend ""
        "Jean?":
            call HWchange_stat (JeanX, "love", 90, 1)
            call HWchange_stat (JeanX, "obedience", 70, 1)
            $ JeanX.change_face("confused")
            ch_j "Oh. Yes, you're still here."
            $ JeanX.change_face("confused", eyes = "side")
            ch_j "I was going to check in on the music situation real quick."
            $ JeanX.change_face("smile", eyes = "side")
            ch_j "I might be back later."
        "Let her go":
            pass
    show Jean_sprite standing:
        ease 0.8 pos (-200, 50)
    pause 0.8
    "She wanders into the crowd."

    call hide_all
    $ Present.remove(JeanX)
    $ Nearby.append(JeanX)
    $ JeanX.location = "nearby"
    $ JeanX.change_face("normal")






    if "met" not in StormX.history:
        jump Halloween_Party

    "You see a form out on the dance floor, and she notices you watching."
    "She dances her way over."

    $ Present.append(StormX)
    $ StormX.change_face("smile")
    $ StormX.location = "bg_halloween"
    $ StormX.add_word(1, 0, StormX.Clothes["hair"], 0, "halloween")
    $ StormX.outfitday = "costume"
    $ StormX.outfit_name = StormX.outfitday
    $ StormX.change_Outfit()

    $ shift_focus (StormX)
    show Storm_sprite standing at sprite_location(1200, 50):
        offset (0, 0)
        anchor (0.5, 0.0)
        pos (1200, 50)
        ease 0.8 pos (stage_center, 50)
    pause 0.8

    ch_s "Merry Halloween, [Player.name]!"
    ch_s "Permit me to guess. . ."
    $ StormX.change_face("smile", eyes = "down")
    "She looks you up and down."
    $ StormX.change_face("smile")
    $ HWline = ["Some form of vagabond? Yes?", "You are a dashing swashbuckler!", "You are a deadly Hand ninja.", ". . . Ah! You are a valiant fire fighter!"]
    $ HWline = HWline[halloween_costume]
    ch_s "[HWline]"
    menu:
        extend ""
        "Yeah, you got it.":
            call HWchange_stat (StormX, "love", 90, 1)
            ch_s "Excellent, it is a wonderful costume."
        "No, I just went casual." if not halloween_costume:
            $ StormX.change_face("surprised", eyes = "normal")
            ch_s "Oh."
            $ StormX.change_face("smile")
            ch_s "Well, I could hardly tell."
            ch_s "We do perhaps need to take you out shopping some time. . ."
            ch_s "I do have a friend that could help us with that. . ."
        "No, this is just how I dress now." if halloween_costume:
            $ StormX.change_face("smile", eyes = "side")
            call HWchange_stat (StormX, "obedience", 40, 1)
            ch_s "Oh."
            $ StormX.change_face("smile")
            ch_s "Well, you do make some interesting choices."
            call HWchange_stat (StormX, "inhibition", 50, 1)
            $ StormX.change_face("normal", eyes = "down")
            pause 0.4
            $ StormX.change_face("smile")
            ch_s "I suppose that I do as well."
            $ StormX.change_face("smile")
        "Skip the intros." if "halloween" in Player.history:
            menu:
                "Are you sure you want to skip the remaining inros and go straight to the party?"
                "Yes":
                    jump Halloween_Skip
                "Never mind":
                    ch_p "Sorry, I spaced out there."
    ch_s "So can you guess mine?"
    menu:
        extend ""
        "Is it Elena?":
            $ StormX.change_face("surprised", mouth = "smile")
            call HWchange_stat (StormX, "love", 80, 1)
            call HWchange_stat (StormX, "love", 90, 1)
            ch_s "Yes! you guessed it!"
            $ StormX.change_face("smile")
            ch_s "I was told that she was a popular video game character."
            $ StormX.change_face("smile", eyes = "stunned")
            ch_s "And we had similar hair."
            $ StormX.change_face("smile")
        "Is it clothes from your homeland?":
            $ StormX.change_face("surprised", 2, mouth = "open")
            call HWchange_stat (StormX, "love", 90, 1)
            call HWchange_stat (StormX, "obedience", 50, 1)
            ch_s "Oh, no, that it not the look that I was going for."
            $ StormX.change_face("normal", 1)
            ch_s "But I can understand the error."
            $ StormX.change_face("smile", eyes = "down")
            ch_s "I did wear something like this back in Kenya. . ."
            $ StormX.change_face("sly")
            call HWchange_stat (StormX, "love", 90, 1)
            ch_s "It did not have the top, however."
        "A ring toss?":
            $ StormX.change_face("angry", 2, mouth = "open")
            call HWchange_stat (StormX, "love", 90, -2)
            call HWchange_stat (StormX, "obedience", 50, 1)
            ch_s "How very rude of you!"
            $ StormX.change_face("angry", 1, mouth = "open")
            ch_s "I shall have you know that these are the cultural ornaments of my people!"
            menu:
                extend ""
                "Sorry!":
                    $ StormX.change_face("angry")
                    ch_s "Oh, are you. . ."
                    call HWchange_stat (StormX, "love", 70, 1)
                    call HWchange_stat (StormX, "love", 90, 1)
                "They look really sexy though.":
                    $ StormX.change_face("sexy")
                    ch_s "Oh, they do, do they?"
                    call HWchange_stat (StormX, "love", 80, 1)
                    call HWchange_stat (StormX, "obedience", 60, 1)
                    call HWchange_stat (StormX, "inhibition", 80, 1)
                "Oh, ok.":
                    $ StormX.change_face("angry", eyes = "side")
                    call HWchange_stat (StormX, "love", 90, -1)
                    call HWchange_stat (StormX, "obedience", 60, 1)
                    ch_s ". . ."
            $ StormX.change_face("smile")
            call HWchange_stat (StormX, "love", 90, 2)
            ch_s "I am only joking!"
            ch_s "This is a video game character."
            ch_s "I believe that the rings were drawn up by someone in Japan."
    menu:
        extend ""
        "You look great!":
            call HWchange_stat (StormX, "love", 80, 1)
            call HWchange_stat (StormX, "love", 90, 1)
            ch_s "Oh, well thank you."
            ch_s "That is sweet of you to say."
            ch_s "I am glad that the costume was a hit."
        "I love the new hair.":
            call HWchange_stat (StormX, "love", 80, 1)
            call HWchange_stat (StormX, "love", 90, 1)
            call HWchange_stat (StormX, "inhibition", 70, 1)
            ch_s "Yes, it certainly is low maintenance."
            ch_s "I may keep it after."
        "Very sexy.":
            $ StormX.change_face("smile", mouth = "kiss")
            call HWchange_stat (StormX, "love", 80, 1)
            call HWchange_stat (StormX, "obedience", 50, 1)
            call HWchange_stat (StormX, "inhibition", 50, 1)
            ch_s "Oh!"
            $ StormX.change_face("sexy")
            call HWchange_stat (StormX, "inhibition", 70, 1)
            call HWchange_stat (StormX, "lust", 60, 1)
            ch_s "Well, I suppose that it is that too. . ."
        "So have you seen [EmmaX.name] around?":
            $ StormX.change_face("smile", brows = "confused")
            call HWchange_stat (StormX, "love", 90, -1)
            call HWchange_stat (StormX, "obedience", 50, 1)
            call HWchange_stat (StormX, "obedience", 70, 1)
            ch_s "Tired of my company so soon?"
            $ StormX.change_face("smile", eyes = "side")
            ch_s "Yes, I believe that I did see her under that tree earlier."
            ch_s "Send her my regards."
    $ StormX.change_face("smile")
    ch_s "In any case, I still have to \"get my groove on.\""
    ch_s "Perhaps I will see you later."
    show Storm_sprite standing:
        ease 0.8 pos (1200, 50)
    pause 0.8
    "[StormX.name] glides back onto the dance floor, and you head over toward the treeline."

    call hide_all
    $ Present.remove(StormX)
    $ Nearby.append(StormX)
    $ StormX.location = "nearby"




label Halloween_Emma:


    if "met" not in EmmaX.history:
        jump Halloween_Party
    "You see [EmmaX.name] standng under the trees, talking to one of the other students."


    $ Present.append(EmmaX)
    $ EmmaX.location = "bg_halloween"
    $ EmmaX.change_face("smile")
    $ EmmaX.add_word(1, 0,EmmaX.Clothes["hair"], 0, "halloween")
    $ EmmaX.outfitday = "costume"
    $ EmmaX.outfit_name = EmmaX.outfitday
    $ EmmaX.change_Outfit()

    $ shift_focus (EmmaX)
    show Emma_sprite standing at sprite_location(-200, 50):
        offset (0, 0)
        anchor (0.5, 0.0)
        pos (-200, 50)
        ease 0.8 pos (stage_center, 50)
    pause 0.8

    ch_e "Oh, [EmmaX.player_petname], lovely evening, isn't it?"
    menu:
        extend ""
        "Yeah.":
            pass
        "Let me guess, Lady D?":
            $ EmmaX.change_face("confused")
            call HWchange_stat (EmmaX, "love", 90, -1)
            call HWchange_stat (EmmaX, "obedience", 50, 1)
            ch_e "Princess Diana?"
            ch_e "No, I have no idea what you mean, I am [EmmaX.name]."
            ch_e "[EmmaX.name]."
            menu:
                extend ""
                "Oh. . . ok.":
                    call HWchange_stat (EmmaX, "love", 90, 1)
                    call HWchange_stat (EmmaX, "obedience", 50, 1)
                    call HWchange_stat (EmmaX, "inhibition", 50, 1)
                    call HWchange_stat (EmmaX, "lust", 50, 1)
                    ch_e "That young Ms. Grey hasn't been tampering with your mind, has she? . ."
                "I knew that!":
                    call HWchange_stat (EmmaX, "love", 90, 1)
                    call HWchange_stat (EmmaX, "obedience", 50, 1)
                    call HWchange_stat (EmmaX, "inhibition", 50, 1)
                    call HWchange_stat (EmmaX, "lust", 50, 1)
                    ch_e "I'm sure you did. . ."
                "I meant the giant vampire lady!":
                    $ EmmaX.change_face("confused", 2, eyes = "surprised")
                    $ EmmaX.add_word(1, "vampire", 0)
        "Let me guess, that giant vampire lady?":
            $ EmmaX.change_face("confused", 2)
            $ EmmaX.add_word(1, "vampire", "vampire")
        "Skip the intros." if "halloween" in Player.history:
            menu:
                "Are you sure you want to skip the remaining inros and go straight to the party?"
                "Yes":
                    jump Halloween_Skip
                "Never mind":
                    ch_p "Sorry, I spaced out there."


    if "vampire" in EmmaX.recent_history:
        call HWchange_stat (EmmaX, "love", 70, -2)
        call HWchange_stat (EmmaX, "love", 90, -1)
        call HWchange_stat (EmmaX, "obedience", 50, 1)

        $ EmmaX.change_face("angry", 1, eyes = "side")
        ch_e "Well I'm not sure how offended I'm meant to be by that."
        ch_e "It's not often that someone refers to me as \"giant.\""
        menu:
            extend ""
            "Your costume! I meant the giant vampire lady from the game!":
                $ EmmaX.change_face("surprised", 1)
                call HWchange_stat (EmmaX, "love", 90, -1)
                ch_e "Costume?"
                $ EmmaX.change_face("confused")
                ch_e "What costume?"
                $ EmmaX.drain_word("vampire", 1, 0, 0)
            "Well, I just meant. . . in certain areas.":
                $ EmmaX.change_face("angry")
                call HWchange_stat (EmmaX, "obedience", 50, 1)
                call HWchange_stat (EmmaX, "obedience", 70, 1)
                call HWchange_stat (EmmaX, "inhibition", 50, 1)
                if approval_check(EmmaX, 1200) or approval_check(EmmaX, 400, "O"):
                    ch_e ". . ."
                    $ EmmaX.change_face("sexy")
                    call HWchange_stat (EmmaX, "love", 90, 1)
                    call HWchange_stat (EmmaX, "inhibition", 50, 1)
                    call HWchange_stat (EmmaX, "lust", 50, 1)
                    ch_e "I will let you off the hook for that one."
                else:
                    call HWchange_stat (EmmaX, "obedience", 50, 1)
                    ch_e "That is still an entirely inappropriate way to talk to a lady."
            "You do have some giant tits.":
                $ EmmaX.change_face("angry")
                call HWchange_stat (EmmaX, "obedience", 50, 1)
                call HWchange_stat (EmmaX, "obedience", 70, 1)
                call HWchange_stat (EmmaX, "inhibition", 70, 1)
                if approval_check(EmmaX, 1300) or approval_check(EmmaX, 500, "O"):
                    ch_e ". . ."
                    $ EmmaX.change_face("sexy")
                    call HWchange_stat (EmmaX, "love", 90, 1)
                    call HWchange_stat (EmmaX, "inhibition", 50, 1)
                    call HWchange_stat (EmmaX, "lust", 50, 1)
                    call HWchange_stat (EmmaX, "lust", 60, 1)
                    ch_e "I suppose that I can't disagree."
                else:
                    call HWchange_stat (EmmaX, "love", 90, -1)
                    call HWchange_stat (EmmaX, "inhibition", 50, 1)
                    call HWchange_stat (EmmaX, "lust", 50, 1)
                    ch_e "And -you- need to remove your mind from the gutter."
            "Sorry, never mind. . .":
                $ EmmaX.change_face("angry", eyes = "side")
                call HWchange_stat (EmmaX, "love", 90, 1)
                call HWchange_stat (EmmaX, "inhibition", 50, 1)
                ch_e "Well. . . I suppose I can allow that to slide."
                $ EmmaX.change_face("normal")
                ch_e "Still, a very unusual direction for your mind to wander."
    if "vampire" in EmmaX.recent_history:
        $ EmmaX.change_face("normal", brows = "confused")
        ch_e "And why \"vampire?\""
        ch_e "Do you think that I'm spending too much time with Miss Lee?"
        menu:
            extend ""
            "Um, yeah, that must be it.":
                $ EmmaX.change_face("normal", eyes = "side")
                call HWchange_stat (EmmaX, "love", 90, 2)
                ch_e "Well, certainly not enough to contract her. . . affliction"
            "What? Oh, never mind.":
                $ EmmaX.change_face("normal")
                call HWchange_stat (EmmaX, "love", 90, 1)
                call HWchange_stat (EmmaX, "obedience", 50, 1)
                ch_e "Well, whatever. . ."
            "Your costume! I meant the giant vampire lady from the game!":
                $ EmmaX.change_face("surprised", 1)
                call HWchange_stat (EmmaX, "love", 90, -1)
                call HWchange_stat (EmmaX, "obedience", 50, 1)
                ch_e "Costume?"
                $ EmmaX.change_face("confused")
                ch_e "What costume?"
                $ EmmaX.drain_word("vampire", 1, 0, 0)
    $ EmmaX.change_face("normal", eyes = "down")
    ch_e "I'd heard this would be a \"fancy dress\" party, so I just dressed for the occasion."
    $ EmmaX.change_face("angry", eyes = "side")
    ch_e "Now that you mention it, the other students are a bit. . . flamboyantly attired."
    $ EmmaX.change_face("angry", eyes = "down")
    ch_e "Does that explain why you're dressed as some sort of. . ."
    $ HWline = ["Well, I suppose that's how you always look.", "Rogue seaman?", "Sneakthief?", "Fireman?"]
    $ EmmaX.change_face("normal", brows = "confused")
    $ HWline = HWline[halloween_costume]
    ch_e "[HWline]"
    if halloween_costume == 1:
        menu:
            extend ""
            "That's me, definitely \"rogue semen.\"":
                $ EmmaX.change_face("smile", brows = "surprised")
                call HWchange_stat (EmmaX, "obedience", 50, 1)
                call HWchange_stat (EmmaX, "inhibition", 50, 1)
                call HWchange_stat (EmmaX, "inhibition", 70, 1)
                call HWchange_stat (EmmaX, "lust", 50, 2)
                ch_e "Ha! you have a filthy mind."
                $ EmmaX.change_face("sly")
                ch_e "We'd better put that to good use. . ."
            "A pirate, actually. . .":
                $ EmmaX.change_face("smile")
                call HWchange_stat (EmmaX, "love", 90, 1)
                call HWchange_stat (EmmaX, "obedience", 50, 1)
                ch_e "Oh, yes! Quite the marauder you make."
    elif halloween_costume == 2:
        menu:
            extend ""
            "I guess I could pocket a few things. . .":
                $ EmmaX.change_face("smile", brows = "confused")
                call HWchange_stat (EmmaX, "obedience", 50, 1)
                call HWchange_stat (EmmaX, "inhibition", 50, 1)
                ch_e "Probably best that you don't. . ."
            "A ninja, actually.":
                $ EmmaX.change_face("smile")
                call HWchange_stat (EmmaX, "obedience", 50, 1)
                call HWchange_stat (EmmaX, "inhibition", 50, 1)
                ch_e "Ah!, I thought you looked a bit like a Hand Ninja."
        $ EmmaX.change_face("smile")
    elif halloween_costume == 3:
        menu:
            extend ""
            "No, I'm a. . . oh, yeah, a fireman.":
                $ EmmaX.change_face("smile")
                call HWchange_stat (EmmaX, "love", 90, 1)
                call HWchange_stat (EmmaX, "obedience", 60, 1)
                call HWchange_stat (EmmaX, "inhibition", 60, 1)
                ch_e "I knew it. . ."
            "You guessed it!":
                $ EmmaX.change_face("smile")
                call HWchange_stat (EmmaX, "love", 90, 1)
                call HWchange_stat (EmmaX, "inhibition", 50, 1)
                call HWchange_stat (EmmaX, "inhibition", 70, 1)
                ch_e "Of course!"
        $ EmmaX.change_face("sly")
        call HWchange_stat (EmmaX, "lust", 50, 2)
        call HWchange_stat (EmmaX, "lust", 70, 1)
        ch_e "I do have a bit of experience with firemen. . ."
    else:
        menu:
            extend ""
            "Oh, yeah?":
                $ EmmaX.change_face("sad")
                call HWchange_stat (EmmaX, "love", 90, -1)
                call HWchange_stat (EmmaX, "obedience", 50, 1)
                ch_e "No, it's. . . fine."
            "I didn't feel like dressing up.":
                call HWchange_stat (EmmaX, "love", 90, -1)
                call HWchange_stat (EmmaX, "obedience", 50, 1)
                call HWchange_stat (EmmaX, "obedience", 70, 1)
                ch_e "No, I. . . can see that. . ."
        $ EmmaX.change_face("angry", eyes = "side")
        ch_e "We might have to take you shopping at some point though. . ."
    $ EmmaX.change_face("normal", brows = "sad")
    ch_e "And do you have anything to say about mine?"
    menu:
        extend ""
        "No, not really.":
            if approval_check(EmmaX, 1200) or approval_check(EmmaX, 400, "O"):
                $ EmmaX.change_face("sadside")
                call HWchange_stat (EmmaX, "love", 90, -1)
                call HWchange_stat (EmmaX, "obedience", 70, 2)
                call HWchange_stat (EmmaX, "obedience", 90, 1)
                ch_e "Oh. . ."
                ch_e "Pity."
            else:
                $ EmmaX.change_face("angry")
                call HWchange_stat (EmmaX, "love", 80, -2)
                call HWchange_stat (EmmaX, "love", 90, -1)
                call HWchange_stat (EmmaX, "obedience", 50, 1)
                ch_e "Well!"
                ch_e "I suppose that I shouldn't have asked in the first place."
        "Oh, it's very nice.":

            $ EmmaX.change_face("smile")
            call HWchange_stat (EmmaX, "love", 70, 2)
            call HWchange_stat (EmmaX, "love", 90, 1)
            call HWchange_stat (EmmaX, "inhibition", 50, 1)
            ch_e "I'm glad you can appreciate fine things."
        "Love the hat.":
            $ EmmaX.change_face("smile", eyes = "stunned")
            call HWchange_stat (EmmaX, "love", 80, 1)
            call HWchange_stat (EmmaX, "love", 90, 2)
            call HWchange_stat (EmmaX, "obedience", 70, 1)
            call HWchange_stat (EmmaX, "inhibition", 70, 1)
            ch_e "Oh, yes, I saw it in a shop in town and thought that I must have that. . ."
            $ EmmaX.change_face("smile")
        "Definitely looks like the vampire lady.":
            if "vampire" in EmmaX.recent_history:
                $ EmmaX.change_face("angry", 2, eyes = "surprised")
                call HWchange_stat (EmmaX, "love", 80, -1)
                call HWchange_stat (EmmaX, "obedience", 50, 1)
                ch_e "I have no idea what you're talking about!"
            else:
                $ EmmaX.change_face("angry", 2)
                call HWchange_stat (EmmaX, "obedience", 50, 1)
                call HWchange_stat (EmmaX, "obedience", 70, 1)
                ch_e "Well I'm certain that any resemblance is -purely- coincidental."
                $ EmmaX.change_face("angry", 1)
                ch_e "Are we -clear?-"
            $ EmmaX.change_face("normal", 1)
    ch_e "In any case. . ."
    ch_e "It is nice to have a little soiree. . . I do hope to see you later in the evening."
    ch_e "For the moment, I'll need to excuse myself."
    show Emma_sprite standing:
        ease 0.8 pos (-200, 50)
    pause 0.8
    "[EmmaX.name] heads over to the refreshments."

    call hide_all
    $ Present.remove(EmmaX)
    $ Nearby.append(EmmaX)
    $ EmmaX.location = "nearby"



    jump Halloween_Party

    return

label Halloween_Skip:
    call hide_all
    $ Options = active_Girls[:]
    if LauraX in Options and "angry" in LauraX.recent_history:

        $ Options.remove(LauraX)
    while Options:
        while Options[0] in Present:
            $ Present.remove(Options[0])
        if Options[0] not in Nearby:
            $ Nearby.append(Options[0])
        $ Options[0].location = "bg_halloween"
        $ Options[0].outfitday = "costume"
        $ Options[0].outfit_name = EmmaX.outfitday
        $ Options[0].change_Outfit()
        $ Options[0].add_word(1, 0, 0, 0, "halloween")

        $ Options.remove(Options[0])


label Halloween_Party:

    call Halloween_Events
    if round <= 10:
        call Halloween_Ending
    menu:
        "You are at the Halloween Player.Party. What would you like to do?"
        "Talk to [RogueX.name]." if RogueX.location == "bg_halloween" or RogueX.location == "nearby":
            call Halloween_chat (RogueX)
        "Talk to [KittyX.name]." if KittyX.location == "bg_halloween" or KittyX.location == "nearby":
            call Halloween_chat (KittyX)
        "Talk to [EmmaX.name]." if EmmaX.location == "bg_halloween" or EmmaX.location == "nearby":
            call Halloween_chat (EmmaX)
        "Talk to [LauraX.name]." if LauraX.location == "bg_halloween" or LauraX.location == "nearby":
            call Halloween_chat (LauraX)
        "Talk to [JeanX.name]." if JeanX.location == "bg_halloween" or JeanX.location == "nearby":
            call Halloween_chat (JeanX)
        "Talk to [StormX.name]." if StormX.location == "bg_halloween" or StormX.location == "nearby":
            call Halloween_chat (StormX)
        "Leave the party":
            call Halloween_Ending
    jump Halloween_Party


label Halloween_Events:
    if not HWEvents:

        $ round -= 15
        $ HWEvents = ["Scott is dressed like Ryu. He tries to do a Hadouken, but with his eyes.",
                            "Kurt is dressed like Sasuke. He keeps teleporting around and dropping logs everywhere.",
                            "Bobby is dressed like Sub Zero. He keeps yelling \"get over here!\", but everyone looks confused.",
                            "Professor McCoy is swinging from one of the trees. He's dyed his fur green, with an orange mane.",
                            "Hisako is lumbering around with cardboard boxes over her armor, so she looks like a mech.",

                            "Lin seems to be wearing a Chopper costume over her antlers.",
                            "Treavor has stuck a bunch of eyestalk tentacles to his body and painted himself purple.",
                            "Iara has managed to crush the apple bobbing contest, but then she can stay down there forever.",
                            "Herman has dyed himself teal, somehow, and is wearing a pair of pants that look like a giant wolf.",
                            "Doug is dressed as a shiny gold droid. Fluent in over 6 million languages, I bet.",

                            "Ernst is dressed in a black witch's costume with a giant hat. Martha has little cat ears on.",
                            "Cessily has some various metal bits added on so that she looks like something off a Heavy Metal cover.",
                            "Aaaaaaand apparently Tabby's dropped a bomb in the apple bobbing tub. Apple sauce everywhere.",
                            "Pietro is eating- no, he's dancin- no, wait, he's playing vide- no. . . oh, whatever. He's at the party.",
                            "It looks like Warren is a Mercy main. That's a pretty decent rule 63 costume.",

                            ]
        $ renpy.random.shuffle(HWEvents)
        $ Player.add_word(1, "halloween", "halloween", 0, "halloween")
        "Introductions out of the way, you take a look around the party in progress."
    "[HWEvents[0]]"
    $ round -= 5
    $ HWEvents.remove(HWEvents[0])
    return

label Halloween_Ending(Girl=0):
    "As the evening comes to a close, did you want to meet up with anyone in particular?"
    menu:
        "Talk to [RogueX.name]." if RogueX.location == "bg_halloween" or RogueX.location == "nearby":
            $ Girl = RogueX
        "Talk to [KittyX.name]." if KittyX.location == "bg_halloween" or KittyX.location == "nearby":
            $ Girl = KittyX
        "Talk to [EmmaX.name]." if EmmaX.location == "bg_halloween" or EmmaX.location == "nearby":
            if "classcaught" in EmmaX.history:
                $ Girl = EmmaX
            else:
                ch_e "I really had a lovely time tonight, but I have to call it an evening."
                ch_e "I hope to see you tomorrow. . ."
                $ EmmaX.location = "bg_emma"
                call Halloween_Ending
        "Talk to [LauraX.name]." if LauraX.location == "bg_halloween" or LauraX.location == "nearby":
            $ Girl = LauraX
        "Talk to [JeanX.name]." if JeanX.location == "bg_halloween" or JeanX.location == "nearby":
            $ Girl = JeanX
        "Talk to [StormX.name]." if StormX.location == "bg_halloween" or StormX.location == "nearby":
            $ Girl = StormX
        "No thanks.":
            $ Girl = 0

    $ Player.location = "bg_player"
    call wait
    call set_Girls_locations
    if Girl:
        $ Girl.location = "bg_player"

        call set_the_scene (silent = True)
        $ Girl.change_face("smile", 1)
        if Girl == RogueX:
            ch_r "Well that was an awful fun shindig."
            ch_r "Now what did you have in mind. . ."
        elif Girl == KittyX:
            ch_k "I[Girl.like]totally enjoyed that party!"
            ch_k "So why'd you bring me back here. . ."
        elif Girl == EmmaX:
            ch_e "I really had a lovely time tonight, I hope you had something. . . more in mind."
        elif Girl == LauraX:
            ch_l "Hey, you liked the costume that much?"
        elif Girl == JeanX:
            ch_j "Hey, so what did you want to talk about?"
        elif Girl == StormX:
            ch_s "Whew. . . I quite enjoyed that party. . ."
            ch_s "What was it that you wished to discuss?"
    jump reset_location
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
