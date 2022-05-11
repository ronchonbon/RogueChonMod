# Start Chat menus / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Halloween_Chat(Girl=0):  #rkeljs

        show blackscreen onlayer black
        if Girl == RogueX and renpy.showing("Rogue_Sprite"):
                pass
        elif Girl == KittyX and renpy.showing("Kitty_Sprite"):
                pass
        elif Girl == EmmaX and renpy.showing("Emma_Sprite"):
                pass
        elif Girl == LauraX and renpy.showing("Laura_Sprite"):
                pass
        elif Girl == JeanX and renpy.showing("Jean_Sprite"):
                pass
        elif Girl == StormX and renpy.showing("Storm_Sprite"):
                pass
        else:
            "You approach [Girl.Name]"
            call AllHide(1) #removes all girls
            while Present:
                    # Removes all girls from Present to Nearby
                    $ Nearby.append(Present[0])
                    $ Present[0].Loc = "nearby"
                    $ Present.remove(Present[0])
            #Makes the current focus girl presant and at the party location.
            $ Nearby.remove(Girl)
            $ Present.append(Girl)
            $ Girl.Loc = "HW Party"

            call Display_Girl(Girl)
        hide blackscreen onlayer black

        if Girl == EmmaX and "classcaught" not in EmmaX.History:
                jump Emma_HWChat_Minimal

        if Girl == RogueX:
                ch_r "So what did you want to talk about, [Girl.Petname]?"
        elif Girl == KittyX:
                ch_k "So[Girl.like]what did you want to talk about, [Girl.Petname]?"
        elif Girl == EmmaX:
                ch_e "What was it you wanted to discuss, [Girl.Petname]?"
        elif Girl == LauraX:
                ch_l "Yeah?"
        elif Girl == JeanX:
                ch_j "What is it?"
        elif Girl == StormX:
                ch_s "What can I do for you, [Girl.Petname]?"

        call Halloween_Chat_Menu
        return

# Start Main Chat menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Halloween_Chat_Menu: #rkeljs
        $ Girl = GirlCheck(Girl)
        $ Girl.FaceChange()
        call Shift_Focus(Girl)

        if "angry" in Girl.RecentActions:
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
#                        "Flirt with her (locked)":
#                                    pass
                        "Flirt with her":
                                    call Flirt(Girl)
                                    return

                        "Sex Menu (locked)" if Girl.Loc != bg_current:
                                    pass
                        "Sex Menu" if Girl.Loc == bg_current:
                                    if Girl.Love >= Girl.Obed:
                                            ch_p "Did you want to fool around?"
                                    else:
                                            ch_p "I'd like to get naughty."
                                    if "angry" in Girl.RecentActions:
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
                                    elif ApprovalCheck(Girl, 800):
                                            $ Girl.FaceChange("sexy")
                                            if Girl == RogueX:
                                                    ch_r "Heh, maybe after the party, [Girl.Petname]?"
                                            elif Girl == KittyX:
                                                    ch_k "Ha! I wouldn't wanna to ruin the party [Girl.Petname]."
                                            elif Girl == EmmaX:
                                                    ch_e "Oh, and get grass stains on this dress?"
                                            elif Girl == LauraX:
                                                    ch_l "Heh, maybe later."
                                            elif Girl == JeanX:
                                                    ch_j "I'm kinda busy with the party right now."
                                            elif Girl == StormX:
                                                    ch_s "Perhaps later, [Girl.Petname]"
                                    else:
                                            if Girl == RogueX:
                                                    ch_r "I'm not really interested, [Girl.Petname]."
                                            elif Girl == KittyX:
                                                    ch_k "No thanks, [Girl.Petname]."
                                            elif Girl == EmmaX:
                                                    ch_e "No thank you, [Girl.Petname]."
                                            elif Girl == LauraX:
                                                    ch_l "No thanks, [Girl.Petname]."
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
                                    call expression Girl.Tag + "_Chitchat" #call Rogue_Chitchat
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
                                        "How do you feel about [RogueX.Name]?" if Girl != RogueX:
                                                call expression Girl.Tag + "_About" pass (RogueX)
                                        "How do you feel about [KittyX.Name]?" if Girl != KittyX and "met" in KittyX.History:
                                                call expression Girl.Tag + "_About" pass (KittyX)
                                        "How do you feel about [EmmaX.Name]?" if Girl != EmmaX and "met" in EmmaX.History:
                                                call expression Girl.Tag + "_About" pass (EmmaX)
                                        "How do you feel about [LauraX.Name]?" if Girl != LauraX and "met" in LauraX.History:
                                                call expression Girl.Tag + "_About" pass (LauraX)
                                        "How do you feel about [JeanX.Name]?" if Girl != JeanX and "met" in JeanX.History:
                                                call expression Girl.Tag + "_About" pass (JeanX)
                                        "How do you feel about [StormX.Name]?" if Girl != StormX and "met" in StormX.History:
                                                call expression Girl.Tag + "_About" pass (StormX)
                                        "About hooking up with other girls. . .":
                                                call expression Girl.Tag + "_Monogamy" #call Rogue_Monogamy
                                        "Never mind.":
                                                pass

                        "Back":
                                    pass

            "Change her":
                        call Girl_Settings

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
        jump Halloween_Chat_Menu
# End Main Chat menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Emma_HWChat_Minimal:
    $ EmmaX.FaceChange()
    call Shift_Focus(EmmaX)
    menu:
        ch_e "What was it you wished to discuss, [EmmaX.Petname]?"
        "Romance her":
                menu:
                    "Flirt with her (locked)" if EmmaX.Chat[5]:
                                pass
                    "Flirt with her" if not EmmaX.Chat[5]:
                                call Emma_Flirt_Minimal
                    "Sex Menu":
                                ch_p "Did you want to fool around?"
                                ch_e "With a student? You should know better than that, [EmmaX.Petname]."
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
        "Change [EmmaX.Name]":
                    ch_p "Let's talk about you."
                    ch_e "I doubt that's any of your business."
        "Never mind.":
                    $ EmmaX.FaceChange("bemused",2)
                    ch_e "Very well. . ."
                    ch_e "I have some. . . business to attend to."
                    return
    jump Emma_HWChat_Minimal


label HWStatup(Girl=0,HWType=0,HWCheck=0,HWValue=0,HWStore=0):
        # to $ Girl.Statup("Love", 90, 1)
        # call HWStatup(RogueX,"Love", 90, 1)
        #used for applying stats only if this is the first time through.
        if Girl not in TotalGirls:
                return
        $ HWStore = getattr(Girl,HWType) #saves original value
        $ Girl.Statup(HWType,HWCheck,HWValue)
        if "halloween" in Girl.History:
                $ setattr(Girl, HWType, HWStore) #restores original value if they've done this before
        return


label Halloween_Party_Entry(HWEvents=[],HWParty=[],Costume=0,HWLine=[]):
        # HWEvents is a list of events that get cycled through
        # HW Party is the girls currently at the party
        # Costume is the number of the costume you picked, one, pirate, ninja, and fireman
        # HWLine is used to play lines related to your costume
        #add introductory scene-setting here
        $ bg_current = "HW Party"
        call Remove_Girl("All")
        call display_background
        $ Party = []
        $ Present = []
        $ Nearby = []
        "You enter the university square, where the party seems to be in full swing."
        "The various students are wandering around in costume, there seems to be a lot of dancing going on, and some food tables set up."

        #Start Rogue Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        "[RogueX.Name] walks up to you."

        #display Rogue here in costume
#        call AllHide(1) #removes all girls
        $ Present.append(RogueX)
        $ RogueX.Loc = "HW Party"
        $ RogueX.AddWord(1,0,RogueX.Hair,0,"halloween")#adds "hair style" to Daily #adds "halloween" to History
        $ RogueX.OutfitDay = "costume"
        $ RogueX.Outfit = RogueX.OutfitDay
        $ RogueX.OutfitChange(Changed=1)
#        call Display_Girl(RogueX)
        call Shift_Focus(RogueX)
        show Rogue_Sprite at sprite_location(1200,50):
                offset (0,0)
                anchor (0.5, 0.0)
                pos (1200,50)
                ease 0.8 pos (StageCenter,50)
        pause 0.8

        $ RogueX.FaceChange("smile")
        ch_r "Hey, [RogueX.Petname], nice to see ya made it."
        $ RogueX.FaceChange("smile",Eyes="down")
        ch_r "Looks like you're dressed as. . ."
        $ RogueX.FaceChange("smile")
        menu:
            extend ""
            "A pirate":
                call HWStatup(RogueX,"Love", 90, 2)
                call HWStatup(RogueX,"Inbt", 50, 1)
                call HWStatup(RogueX,"Inbt", 80, 1)
                call HWStatup(RogueX,"Lust", 50, 2)
                $ Costume = 1
            "A ninja":
                call HWStatup(RogueX,"Love", 70, 1)
                call HWStatup(RogueX,"Love", 80, 1)
                $ Costume = 2
            "A fireman":
                call HWStatup(RogueX,"Love", 70, 1)
                call HWStatup(RogueX,"Love", 80, 1)
                call HWStatup(RogueX,"Lust", 50, 1)
                $ Costume = 3
            "No costume":
                call HWStatup(RogueX,"Love", 80, -2)
                call HWStatup(RogueX,"Obed", 50, 1)
                call HWStatup(RogueX,"Inbt", 50, 1)
                $ RogueX.FaceChange("confused")

        $ HWLine = ["Oh. . . that's sorta what I figured. . .","Well \"Ahoy\" to you then.","Oooh, dangerous. . .","Well I've certainly got a fire for you to put out. . ."]
        $ HWLine = HWLine[Costume]
        ch_r "[HWLine]"
        if not Costume:
                $ RogueX.FaceChange("smile")
                ch_r "Still, welcome to the party, I suppose. . ."
        ch_r "Can ya guess what I'm going as?"
        menu:
            extend ""
            "Ada?":
                    $ RogueX.FaceChange("confused")
                    call HWStatup(RogueX,"Love", 80, -2)
                    ch_r "Well, close, you got the game right at least."
                    $ RogueX.FaceChange("normal")
                    call HWStatup(RogueX,"Inbt", 50, 3)
                    call HWStatup(RogueX,"Inbt", 70, 2)
                    ch_r "But no, it's Jill, actually."
            "Jill?":
                    call HWStatup(RogueX,"Love", 80, 2)
                    call HWStatup(RogueX,"Love", 90, 2)
                    call HWStatup(RogueX,"Inbt", 50, 1)
                    $ RogueX.FaceChange("smile",Eyes="surprised")
                    pause 0.4
                    $ RogueX.FaceChange("smile")
                    ch_r "Sure'nuff, [RogueX.Petname]. You know your characters."
            "Some sort of hooker?":
                    if ApprovalCheck(RogueX, 1600) or ApprovalCheck(RogueX, 700, "O"):
                            $ RogueX.FaceChange("perplexed",2)
                            call HWStatup(RogueX,"Love", 90, -1)
                            ch_r "Wha. . . "
                            call HWStatup(RogueX,"Obed", 90, 2)
                            ch_r ". . ."
                            $ RogueX.FaceChange("sexy",1)
                            call HWStatup(RogueX,"Love", 90, 1)
                            call HWStatup(RogueX,"Lust", 50, 2)
                            ch_r "I suppose if that's what you like to see. . ."
                    elif ApprovalCheck(RogueX, 1300):
                            $ RogueX.FaceChange("angry",Eyes="side")
                            call HWStatup(RogueX,"Love", 70, -2)
                            call HWStatup(RogueX,"Love", 90, -2)
                            call HWStatup(RogueX,"Obed", 50, 1)
                            ch_r "I'm gonna pretend I didn't hear that. . ."
                            call HWStatup(RogueX,"Obed", 70, 1)
                            call HWStatup(RogueX,"Inbt", 50, -2)
                    else:
                            $ RogueX.FaceChange("angry")
                            call HWStatup(RogueX,"Love", 70, -2)
                            call HWStatup(RogueX,"Love", 90, -2)
                            ch_r "You are really pushing your luck [RogueX.Petname]. . ."
                            call HWStatup(RogueX,"Obed", 50, 1)
                            call HWStatup(RogueX,"Obed", 50, 1)
                    ch_r "Anyway, it's actually Jill, from that zombie game."
            "No clue.":
                    call HWStatup(RogueX,"Love", 80, -2)
                    call HWStatup(RogueX,"Love", 90, -1)
                    call HWStatup(RogueX,"Inbt", 50, 1)
                    ch_r "Well. . . it's Jill, from that zombie game."
            "Skip the intros." if "halloween" in Player.History:
                    menu:
                        "Are you sure you want to skip the remaining inros and go straight to the party?"
                        "Yes":
                            jump Halloween_Skip
                        "Never mind":
                            ch_p "Sorry, I spaced out there."
        menu:
            extend ""
            "Looks nice.":
                    $ RogueX.FaceChange("smile")
                    call HWStatup(RogueX,"Love", 80, 1)
                    call HWStatup(RogueX,"Love", 90, 2)
                    ch_r "Well thank 'ya kindly, [RogueX.Petname]."
                    call HWStatup(RogueX,"Inbt", 50, 2)
                    call HWStatup(RogueX,"Inbt", 60, 1)
            "Looks sexy.":
                    $ RogueX.FaceChange("sexy",1)
                    call HWStatup(RogueX,"Love", 80, 3)
                    call HWStatup(RogueX,"Obed", 80, 2)
                    call HWStatup(RogueX,"Lust", 60, 2)
                    ch_r "Oooh, glad ya enjoy it. . ."
                    call HWStatup(RogueX,"Inbt", 60, 3)
            "Love the hair.":
                    $ RogueX.FaceChange("smile",1)
                    call HWStatup(RogueX,"Love", 80, 2)
                    call HWStatup(RogueX,"Love", 90, 2)
                    call HWStatup(RogueX,"Inbt", 50, 2)
                    ch_r "Aw, thanks [RogueX.Petname]."
                    call HWStatup(RogueX,"Inbt", 70, 2)
                    ch_r "I like it too."
            "Ok, so have you seen [KittyX.Name]?" if "met" in KittyX.History:
                    $ RogueX.FaceChange("angry",Brows="confused")
                    call HWStatup(RogueX,"Love", 80, -2)
                    call HWStatup(RogueX,"Lust", 50, -2)
                    ch_r ". . ."
                    call HWStatup(RogueX,"Obed", 70, 2)
                    call HWStatup(RogueX,"Obed", 90, 1)
                    call HWStatup(RogueX,"Inbt", 70, 2)
                    ch_r "Yeah. I seen'er."
                    $ RogueX.FaceChange("angry",Eyes="side")
                    ch_r "You'll find her over there."
        ch_r "Anyway, I gotta get moving, I'll see you later. . ."
        $ RogueX.FaceChange("smile")
        $ Present.remove(RogueX)
        $ Nearby.append(RogueX)
        $ RogueX.Loc = "nearby"
        show Rogue_Sprite:
                ease 0.8 pos (-200,50)
        pause 0.8
        "[RogueX.Name] heads over to mingle some more."
        call AllHide(1) #removes all girls
#End Rogue Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

        if "met" not in KittyX.History:
                jump Halloween_Party

#Start Kitty Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        #hide Rogue here

        #display Kitty here in costume
        $ Present.append(KittyX)
        $ KittyX.Loc = "HW Party"
        $ KittyX.AddWord(1,0,KittyX.Hair,0,"halloween") #adds "halloween" to History
        $ KittyX.OutfitDay = "costume"
        $ KittyX.Outfit = KittyX.OutfitDay
        $ KittyX.OutfitChange(Changed=1)
#        call Display_Girl(KittyX)
        call Shift_Focus(KittyX)
        show Kitty_Sprite at sprite_location(1200,50):
                offset (0,0)
                anchor (0.5, 0.0)
                pos (1200,50)
                ease 0.8 pos (StageCenter,50)
        pause 0.8

        $ KittyX.FaceChange("confused",Eyes="down")
        "Over by the snack table, you find [KittyX.Name], looking through the chips."
        $ KittyX.FaceChange("smile")
        ch_k "Oh, hey!"
        $ KittyX.FaceChange("smile",Eyes="down")
        ch_k "Lemme guess who you are. . ."
        $ KittyX.FaceChange("smile")
        $ HWLine = [Player.Name+" Right?","A mysterious sailor. . .","Oooh, dangerous assassin. . .","A noble hero."]
        $ HWLine = HWLine[Costume]
        ch_k "[HWLine]"
        menu:
            extend ""
            "Yup.":
                    call HWStatup(KittyX,"Love", 80, 1)
                    call HWStatup(KittyX,"Love", 90, 1)
                    ch_k "Got it in one."
            "Good guess.":
                    call HWStatup(KittyX,"Love", 80, 2)
                    call HWStatup(KittyX,"Love", 90, 1)
                    call HWStatup(KittyX,"Inbt", 50, 1)
                    ch_k "Aw, thanks."
            "No, it's [Player.Name].":
                    $ KittyX.FaceChange("confused")
                    call HWStatup(KittyX,"Love", 70, -1)
                    call HWStatup(KittyX,"Obed", 50, -1)
                    if not Costume:
                        ch_k ". . . riiight?"
                    else:
                        ch_k "No[KittyX.like]I know what your name is, I meant. . ."
                    ch_k "Whatever."
            "Skip the intros." if "halloween" in Player.History:
                    menu:
                        "Are you sure you want to skip the remaining inros and go straight to the party?"
                        "Yes":
                            jump Halloween_Skip
                        "Never mind":
                            ch_p "Sorry, I spaced out there."
        $ KittyX.FaceChange("smile")
        ch_k "Anyway, can ya guess what I am?"
        menu:
            extend""
            "Aerith":
                    call HWStatup(KittyX,"Love", 60, 4)
                    call HWStatup(KittyX,"Love", 80, 2)
                    call HWStatup(KittyX,"Love", 200, 2)
                    ch_k "You got it!"
            "Little House on the Prarie?":
                    $ KittyX.FaceChange("confused",Eyes="side")
                    call HWStatup(KittyX,"Love", 70, -1)
                    call HWStatup(KittyX,"Inbt", 50, -1)
                    ch_k "Huh? I guess it is a little. . . \"farmy.\""
                    $ KittyX.FaceChange("sad")
                    ch_k "But no, it's Aerith."
            "Kitty.":
                    $ KittyX.FaceChange("confused")
                    call HWStatup(KittyX,"Love", 80, -1)
                    call HWStatup(KittyX,"Obed", 30, -1)
                    ch_k "I. . . Yes[KittyX.like]I am Kitty, but this is a costume I'm in."
                    ch_k "You know. . . Halloween?"
                    $ KittyX.FaceChange("confused",Eyes="stunned")
                    call HWStatup(KittyX,"Inbt", 50, 3)
                    call HWStatup(KittyX,"Inbt", 70, 3)
                    ch_k "Geeze."
                    $ KittyX.FaceChange("angry")
                    ch_k "I'm dressed as Aerith!"
                    $ KittyX.FaceChange("normal")
            "No?":
                    $ KittyX.FaceChange("sad")
                    call HWStatup(KittyX,"Love", 70, -1)
                    call HWStatup(KittyX,"Obed", 50, 1)
                    call HWStatup(KittyX,"Obed", 60, 1)
                    ch_k "Booo, you could at least try."
                    $ KittyX.FaceChange("normal")
                    ch_k "I'm dressed as Aerith!"
        menu:
            extend ""
            "Looks nice.":
                    $ KittyX.FaceChange("smile")
                    call HWStatup(KittyX,"Love", 80, 2)
                    call HWStatup(KittyX,"Love", 90, 1)
                    call HWStatup(KittyX,"Obed", 50, 1)
                    ch_k "Ah, thank you, [KittyX.Petname]."
                    call HWStatup(KittyX,"Inbt", 50, 2)
            "Looks sexy.":
                    $ KittyX.FaceChange("smile",2)
                    call HWStatup(KittyX,"Love", 80, 1)
                    call HWStatup(KittyX,"Inbt", 50, 2)
                    ch_k "I thought it might be kinda plain. . ."
                    $ KittyX.FaceChange("smile",1,Eyes="side")
                    call HWStatup(KittyX,"Love", 90, 1)
                    call HWStatup(KittyX,"Obed", 50, 1)
                    ch_k "Next to some of the others, at least. . ."
                    menu:
                        extend ""
                        "I'm curious what's underneath it.":
                                $ KittyX.FaceChange("sexy",2)
                                call HWStatup(KittyX,"Love", 60, -1)
                                call HWStatup(KittyX,"Love", 90, 1)
                                call HWStatup(KittyX,"Lust", 60, 3)
                                ch_k "Well, play your cards right. . ."
                                $ KittyX.Blush = 1
                                call HWStatup(KittyX,"Obed", 60, 1)
                                call HWStatup(KittyX,"Obed", 80, 2)
                                call HWStatup(KittyX,"Inbt", 70, 1)
                        "Yeah, I guess you're right about that.":
                                $ KittyX.FaceChange("sad")
                                call HWStatup(KittyX,"Love", 80, -1)
                                call HWStatup(KittyX,"Love", 90, -1)
                                ch_k ". . . oh."
                                $ KittyX.FaceChange("sadside")
                                call HWStatup(KittyX,"Obed", 50, 1)
                                call HWStatup(KittyX,"Obed", 80, 1)
                                ch_k ". . ."
                                call HWStatup(KittyX,"Inbt", 50, 1)
                                ch_k "Well, I still like it."
                                $ KittyX.FaceChange("normal")
            "Love the hair.":
                    $ KittyX.FaceChange("confused")
                    call HWStatup(KittyX,"Love", 70, -1)
                    call HWStatup(KittyX,"Love", 90, -1)
                    ch_k "What? . . but I. . . Didn't do anything with my hair. . ."
                    $ KittyX.FaceChange("normal")
            "Ok, so have you seen any of the other girls?" if "met" in EmmaX.History:
                    $ KittyX.FaceChange("confused")
                    call HWStatup(KittyX,"Love", 80, -1)
                    call HWStatup(KittyX,"Obed", 50, 1)
                    call HWStatup(KittyX,"Obed", 60, 1)
                    ch_k "Well. . ."
                    $ KittyX.FaceChange("normal",Eyes="leftside")
                    if "met" in LauraX.History:
                            ch_k "Yeah, [LauraX.Name]'s right over there."
                            ch_k "Hey [LauraX.Name]?!"
                    else:
                            ch_k "[KittyX.Like]not really?"
                    $ KittyX.FaceChange("normal")



        if "met" not in LauraX.History:
                ch_k "Anyway, I was were[KittyX.like]going to check out the scene over there for a second."
                ch_k "Maybe I'll see you later, [KittyX.Petname]."
                call AllHide(1) #removes all girls
                $ Present.remove(KittyX)
                $ Nearby.append(KittyX)
                $ KittyX.Loc = "nearby"
                jump Halloween_Emma

#Start Laura Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        "[LauraX.Name] looks up from the punch bowl and sees the two of you."
        show Kitty_Sprite:
                ease 0.8 pos (1200,50)
        pause 0.8

        #display Laura here in costume
        $ Present.append(LauraX)
        $ LauraX.Loc = "HW Party"
        $ LauraX.AddWord(1,0,LauraX.Hair,0,"halloween") #adds "halloween" to History
        $ LauraX.OutfitDay = "costume"
        $ LauraX.Outfit = LauraX.OutfitDay
        $ LauraX.OutfitChange(Changed=1)
#        call Display_Girl(LauraX)
        call Shift_Focus(LauraX)
        show Laura_Sprite at sprite_location(1200,50):
                offset (0,0)
                anchor (0.5, 0.0)
                pos (1200,50)
                ease 0.8 pos (StageCenter,50)
        show Kitty_Sprite:
                ease 0.8 pos (StageFarRight,50)
        pause 0.8
        "She wanders over"

        $ LauraX.FaceChange("normal")
        ch_l "Oh, hey, [KittyX.Name], [Player.Name]."
        $ HWLine = ["Like the look.","Homeless person?","Hand ninja?","Lumberjack?"]
        $ HWLine = HWLine[Costume]
        ch_l "[HWLine]"
        if Costume:
            menu:
                extend ""
                "Yeah.":
                        call HWStatup(LauraX,"Love", 80, 1)
                        ch_l "Cool. Cool."
                "Nope.":
                        $ LauraX.FaceChange("confused")
                        call HWStatup(LauraX,"Obed", 50, 1)
                        ch_l "Oh."
                        if Costume == 2:
                            call HWStatup(LauraX,"Love", 80, -1)
                            call HWStatup(LauraX,"Inbt", 60, 1)
                            ch_l "Definitely looks like a Hand ninja."
                        $ LauraX.FaceChange("normal")
                "Way off.":
                        $ LauraX.FaceChange("confused")
                        call HWStatup(LauraX,"Love", 80, -1)
                        call HWStatup(LauraX,"Obed", 70, 2)
                        ch_l "Oh."
                        if Costume == 2:
                            call HWStatup(LauraX,"Love", 80, -2)
                            call HWStatup(LauraX,"Inbt", 60, 2)
                            ch_l "It -definitely- looks like a Hand ninja though."
        $ KittyX.FaceChange("smile",Eyes="side")
        $ HWLine = ["Right?","He's a pirate, silly!","Yeah, I guess he could be. . .","It's a fireman, silly!"]
        $ HWLine = HWLine[Costume]
        ch_k "[HWLine]"
        $ KittyX.FaceChange("smile")
        ch_k "Now guess what [LauraX.Name]'s going as!"
        menu:
            extend ""
            "A Boxer?":
                $ LauraX.FaceChange("normal",Eyes="down")
                ch_l ". . ."
                $ LauraX.FaceChange("normal")
                call HWStatup(LauraX,"Love", 80, 1)
                ch_l "No."
                $ KittyX.FaceChange("angry")
                call HWStatup(KittyX,"Love", 70, -2)
                call HWStatup(KittyX,"Love", 90, 2)
                call HWStatup(KittyX,"Inbt", 50, 2)
                ch_k "She's Tifa!"
                $ KittyX.FaceChange("smile")
            "A prostitute?":
                $ LauraX.FaceChange("sad",2)
                if ApprovalCheck(LauraX, 1600) or ApprovalCheck(LauraX, 700, "O"):
                        #she accepts this, but doesn't like it
                        call HWStatup(LauraX,"Love", 80, -2)
                        call HWStatup(LauraX,"Love", 90, -3)
                        ch_l "That is. . . hurtful. . ."
                        call HWStatup(LauraX,"Obed", 80, 3)
                        call HWStatup(LauraX,"Obed", 200, 1)
                else:
                        call Punch
                        if "partyfix" in LauraX.History:
                                call HWStatup(LauraX,"Love", 80, -2)
                                call HWStatup(LauraX,"Love", 90, -3)
                                ch_l "Not this shit again!"
                                call HWStatup(LauraX,"Obed", 80, 3)
                                call HWStatup(LauraX,"Obed", 200, 1)
                        elif "lover" in LauraX.Petnames:
                                #you should know this
                                call HWStatup(LauraX,"Love", 80, -2)
                                call HWStatup(LauraX,"Love", 90, -3)
                                ch_l "You know better than that. . ."
                                call HWStatup(LauraX,"Obed", 80, 3)
                                call HWStatup(LauraX,"Obed", 200, 1)
                                $ LauraX.AddWord(1,0,0,0,"partyfoul") #adds "partyfoul" to History
                        else:
                                #maybe you just don't know
                                call HWStatup(LauraX,"Love", 80, -2)
                                call HWStatup(LauraX,"Love", 90, -3)
                                ch_l ". . ."
                                ch_l "If you knew. . ."
                                $ LauraX.AddWord(1,0,0,0,"partyfoul") #adds "partyfoul" to History
                        $ LauraX.FaceChange("angry")

                        $ LauraX.AddWord(1,"angry","angry",0,0) #adds "angry" to recent/daily

                        #you pissed her off and she leaves
                        ch_l "I don't have time for this."
                        show Laura_Sprite:
                                ease 0.8 pos (1200,50)
                        pause 0.8
                        "[LauraX.Name] stalks out of the party for the night."
                        call Remove_Girl(LauraX)

                        $ KittyX.FaceChange("angry")
                        call HWStatup(KittyX,"Love", 70, 2)
                        call HWStatup(KittyX,"Love", 90, 2)
                        ch_k "Well that was rude!"
                        ch_k "I think I'm[KittyX.like]going to check out the scene over there for a second."
                        show Kitty_Sprite:
                                ease 0.8 pos (1200,50)
                        pause 0.8
                        "[KittyX.Name] heads off to the side."
                        $ KittyX.FaceChange("normal")
                        call AllHide(1) #removes all girls
                        $ Present.remove(KittyX)
                        $ Nearby.append(KittyX)
                        $ KittyX.Loc = "nearby"
                        jump Halloween_Jean

            "Tifa?":
                $ KittyX.FaceChange("smile")
                $ LauraX.FaceChange("smile")
                call HWStatup(KittyX,"Love", 60, 2)
                call HWStatup(KittyX,"Love", 90, 1)
                call HWStatup(LauraX,"Love", 90, 1)
                call HWStatup(LauraX,"Inbt", 50, 1)
                ch_l "Yes, apparently."
            "How should I know?":
                call HWStatup(LauraX,"Love", 90, 1)
                call HWStatup(LauraX,"Obed", 50, 1)
                call HWStatup(LauraX,"Inbt", 50, 1)
                call HWStatup(LauraX,"Inbt", 70, 1)
                ch_l "Yeah, right?"
                $ KittyX.FaceChange("surprised")
                call HWStatup(KittyX,"Love", 70, -1)
                call HWStatup(KittyX,"Love", 90, -2)
                ch_k "She's Tifa!"
                $ KittyX.FaceChange("smile")
            "Skip the intros." if "halloween" in Player.History:
                    menu:
                        "Are you sure you want to skip the remaining inros and go straight to the party?"
                        "Yes":
                            jump Halloween_Skip
                        "Never mind":
                            ch_p "Sorry, I spaced out there."

        #you didn't piss her off. . .
        ch_k "We're wearing buddy costumes!"
        ch_l ". . . yeah."
        ch_l "Apparently."
        menu:
            extend ""
            "It looks great!":
                    $ LauraX.FaceChange("smile")
                    call HWStatup(LauraX,"Love", 70, 1)
                    call HWStatup(LauraX,"Love", 90, 1)
                    call HWStatup(LauraX,"Inbt", 60, 2)
                    ch_l "Yeah, I guess so."
            "Love the suspenders.":
                    $ LauraX.FaceChange("normal",Eyes="down")
                    call HWStatup(LauraX,"Love", 70, 1)
                    call HWStatup(LauraX,"Love", 90, 1)
                    ch_l "Oh?"
                    $ LauraX.FaceChange("smile")
                    $ LauraX.Acc = "suspenders2"
                    call HWStatup(LauraX,"Inbt", 50, 1)
                    call HWStatup(LauraX,"Inbt", 60, 1)
                    ch_l "Yeah. . ."
                    $ LauraX.Acc = "suspenders"
            "How is that different from your normal look?":
                    $ LauraX.FaceChange("normal",Eyes="down")
                    call HWStatup(LauraX,"Love", 80, -1)
                    call HWStatup(LauraX,"Obed", 50, 1)
                    ch_l ". . ."
                    call HWStatup(LauraX,"Inbt", 50, -1)
                    ch_l "Well. . . the top is white now. And the skirt doesn't have buckles."
                    $ LauraX.FaceChange("normal")
                    call HWStatup(LauraX,"Love", 80, -1)
                    call HWStatup(LauraX,"Inbt", 50, -1)
                    ch_l "Also the suspenders."
        ch_k "Anyway, we were[KittyX.like]going to check out the scene over there for a second."
        $ LauraX.FaceChange("normal",Eyes="leftside")
        ch_l "We were?"
        ch_k "Yes. Come on."
        ch_k "Later, [KittyX.Petname]!"
        show Kitty_Sprite:
                ease 0.8 pos (1200,50)
        show Laura_Sprite:
                ease 0.8 pos (1200,50)
        pause 0.8
        "[KittyX.Name] tugs [LauraX.Name] off to the side."
        $ LauraX.FaceChange("normal")

        call AllHide(1) #removes all girls
        $ Present.remove(KittyX)
        $ Nearby.append(KittyX)
        $ KittyX.Loc = "nearby"
        $ Present.remove(LauraX)
        $ Nearby.append(LauraX)
        $ LauraX.Loc = "nearby"

#End LauraPortion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Halloween_Jean:
        #Start Jean Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        if "met" not in JeanX.History:
                "Well that seemed a bit rushed."
                jump Halloween_Emma
        "You can see [JeanX.Name] heading toward the table."
        "Oooooooooh. . . ok."
        "She appears to be shouting back at someone in a baseball cap, Rusty, maybe?"
        ch_j "I don't -care- that you \"gotta catch'em all,\" you're still not in my league!"

        #add Jean arriving
        $ Present.append(JeanX)
        $ JeanX.Loc = "HW Party"
        $ JeanX.AddWord(1,0,JeanX.Hair,0,"halloween") #adds "halloween" to History
        $ JeanX.OutfitDay = "costume"
        $ JeanX.Outfit = JeanX.OutfitDay
        $ JeanX.OutfitChange(Changed=1)
#        call Display_Girl(JeanX)
        call Shift_Focus(JeanX)
        show Jean_Sprite at sprite_location(1200,50):
                offset (0,0)
                anchor (0.5, 0.0)
                pos (1200,50)
                ease 0.8 pos (StageCenter,50)
        pause 0.8

        $ JeanX.FaceChange("angry",Eyes="side")
        ch_j ". . ."
        $ JeanX.FaceChange("normal",Brows="angry")
        ch_j "Oh, hey. . . you look familiar."
        $ Line = JeanX.Petname
        menu:
            extend ""
            "It's me, [Player.Name].":
                $ JeanX.FaceChange("normal")
                call HWStatup(JeanX,"Love", 90, 1)
                call HWStatup(JeanX,"Inbt", 50, 1)
                ch_j "Oh. Yeah. Hello, [JeanX.Petname]."
                ch_j "I almost didn't recognize you."
            "It's me, [Player.Name], I'm a pirate." if Costume == 1:
                $ JeanX.FaceChange("normal")
                call HWStatup(JeanX,"Love", 90, 1)
                call HWStatup(JeanX,"Inbt", 50, 1)
                ch_j "Oh, ok. Hello \"Pirate.\""
                $ JeanX.Petname = "Pirate"
            "A pirate." if Costume == 1:
                $ JeanX.FaceChange("normal")
                call HWStatup(JeanX,"Inbt", 50, 1)
                ch_j "Oh. Yeah. Hello, [JeanX.Petname]."
                ch_j "I thought you were a drag queen."
            "It's me, [Player.Name], I'm a ninja." if Costume == 2:
                $ JeanX.FaceChange("normal")
                call HWStatup(JeanX,"Love", 90, 1)
                call HWStatup(JeanX,"Inbt", 50, 1)
                ch_j "Oh. Yeah. Hello, [JeanX.Petname]."
                ch_j "I thought you were a stage hand."
            "A ninja." if Costume == 2:
                $ JeanX.FaceChange("normal")
                call HWStatup(JeanX,"Inbt", 50, 1)
                ch_j "Oh, ok. Hello \"Ninja.\""
                $ JeanX.Petname = "Ninja"
            "It's me, [Player.Name], I'm a fireman." if Costume == 3:
                $ JeanX.FaceChange("normal")
                call HWStatup(JeanX,"Love", 90, 1)
                call HWStatup(JeanX,"Inbt", 50, 1)
                ch_j "Oh. Yeah. Hello, [JeanX.Petname]."
                $ JeanX.FaceChange("normal",Brows="angry")
                ch_j ". . ."
                $ JeanX.FaceChange("confused")
                ch_j "I thought you had \"power cancelling\" powers."
                ch_j "It's fire now?"
                $ JeanX.AddWord(1,"fire",0) #adds "fire" to Recent
            "A fireman." if Costume == 3:
                call HWStatup(JeanX,"Love", 90, 1)
                call HWStatup(JeanX,"Obed", 50, 1)
                call HWStatup(JeanX,"Inbt", 50, 1)
                ch_j "Oh, ok. Hello \"Fire Man.\""
                $ JeanX.Petname = "Fire Man"
                $ JeanX.AddWord(1,"fire",0) #adds "fire" to Recent
            "Skip the intros." if "halloween" in Player.History:
                    menu:
                        "Are you sure you want to skip the remaining inros and go straight to the party?"
                        "Yes":
                            jump Halloween_Skip
                        "Never mind":
                            ch_p "Sorry, I spaced out there."
        if "fire" in JeanX.RecentActions:
            menu:
                extend ""
                "No, I'm dressed like someone who puts -out- fires.":
                        $ JeanX.FaceChange("surprised")
                        call HWStatup(JeanX,"Love", 90, -1)
                        call HWStatup(JeanX,"Obed", 50, 2)
                        ch_j ". . ."
                        $ JeanX.FaceChange("normal")
                        call HWStatup(JeanX,"Obed", 90, 1)
                        ch_j ". . . of course you are."
                        $ JeanX.FaceChange("smile")
                        call HWStatup(JeanX,"Inbt", 80, -1)
                        ch_j "I was kidding."
                "Yes. Yes, I totally have fire powers now.":
                        $ JeanX.FaceChange("normal")
                        call HWStatup(JeanX,"Obed", 30, 1)
                        call HWStatup(JeanX,"Obed", 70, 1)
                        ch_j "Wild."
                        call HWStatup(JeanX,"Love", 70, 2)
                        call HWStatup(JeanX,"Love", 90, 1)
                        call HWStatup(JeanX,"Lust", 50, 1)
                        ch_j "I had fire powers once."
                        $ JeanX.FaceChange("angry",Eyes="side")
                        ch_j "It didn't go well."
                        ch_j "Small minded fools."

        if JeanX.Petname in ("Pirate","Ninja","Fire Man"):
                menu:
                    extend ""
                    "And my name's [Player.Name], remember?":
                            $ JeanX.FaceChange("normal")
                            call HWStatup(JeanX,"Love", 90, 1)
                            call HWStatup(JeanX,"Obed", 50, 1)
                            call HWStatup(JeanX,"Obed", 70, 1)
                            ch_j "Oh. Right. [Line]."
                            $ JeanX.Petname = Line
                            $ Line = 0
                    "And you call me [Line], remember?" if Line != Player.Name:
                            $ JeanX.FaceChange("normal")
                            call HWStatup(JeanX,"Love", 70, 1)
                            call HWStatup(JeanX,"Love", 90, 1)
                            call HWStatup(JeanX,"Obed", 70, 1)
                            ch_j "Oh. Right. [Line]."
                            $ JeanX.Petname = Line
                            $ Line = 0
                    "Leave it":
                            $ JeanX.FaceChange("normal")
                            call HWStatup(JeanX,"Inbt", 50, 1)
        "You look her costume up and down."
        menu:
            "You look her costume up and down."
            "So what's that look?":
                    $ JeanX.FaceChange("smile",Eyes="side")
                    call HWStatup(JeanX,"Love", 70, 1)
                    ch_j "Oh. . . I whammied some nerd to make me a costume with red hair."
                    $ JeanX.FaceChange("normal")
                    ch_j "I don't know what it's from, but I guess it's fine."
                    menu:
                        extend ""
                        "Yeah, I don't know either.":
                                call HWStatup(JeanX,"Love", 90, 1)
                                call HWStatup(JeanX,"Obed", 50, 1)
                                call HWStatup(JeanX,"Obed", 70, 1)
                        "It's Misty.":
                                call HWStatup(JeanX,"Love", 90, -1)
                                call HWStatup(JeanX,"Obed", 30, -1)
                                call HWStatup(JeanX,"Inbt", 50, 2)
                                ch_j "Oh, ok nerd."
            "Is that supposed to be Misty?":
                    $ JeanX.FaceChange("confused")
                    call HWStatup(JeanX,"Love", 90, -1)
                    call HWStatup(JeanX,"Obed", 30, -1)
                    call HWStatup(JeanX,"Inbt", 50, 2)
                    ch_j "Who's \"Misty?\""
                    $ JeanX.FaceChange("angry",Eyes="side")
                    ch_j "Is that the girl with the water powers?"
                    $ JeanX.FaceChange("angry",Mouth="surprised")
                    ch_j "Wait, -do- we have a girl with water powers?"
                    $ JeanX.FaceChange("normal")
                    ch_j "Anyway. . . I whammied some nerd to make me a costume with red hair."
                    ch_j "Is this her?"
                    menu:
                        extend ""
                        "Yeah, I don't know either.":
                                call HWStatup(JeanX,"Love", 90, 1)
                                call HWStatup(JeanX,"Obed", 50, 1)
                                call HWStatup(JeanX,"Obed", 70, 1)
                        "It's Misty.":
                                call HWStatup(JeanX,"Love", 90, -1)
                                call HWStatup(JeanX,"Obed", 30, -1)
                                call HWStatup(JeanX,"Inbt", 50, 2)
                                ch_j "Oh, ok nerd."
            ". . . [[don't even ask]":
                    pass

        menu:
            extend ""
            "You look great.":
                    $ JeanX.FaceChange("smile")
                    call HWStatup(JeanX,"Love", 70, 2)
                    call HWStatup(JeanX,"Love", 90, 1)
                    call HWStatup(JeanX,"Obed", 70, 1)
                    ch_j "Yeah? That's not a shocker."
                    call HWStatup(JeanX,"Inbt", 50, 1)
                    ch_j "I make anything look good."
            "I like the hair style.":
                    $ JeanX.FaceChange("smile")
                    call HWStatup(JeanX,"Love", 70, 1)
                    call HWStatup(JeanX,"Love", 90, 1)
                    call HWStatup(JeanX,"Obed", 70, 1)
                    ch_j "Big surprise."
                    call HWStatup(JeanX,"Inbt", 50, 2)
                    ch_j "I can even make a side-pony work."
            "Why didn't you go as \"Jessie?\"":
                    $ JeanX.FaceChange("normal",Mouth="kiss")
                    call HWStatup(JeanX,"Obed", 50, 1)
                    ch_j ". . ."
                    ch_j "Who's \"Jessie?!\""
                    $ JeanX.FaceChange("angry",Eyes="side")
                    "She looks around and locks eyes with one of the other students."
                    $ JeanX.FaceChange("angry",Eyes="psychic")
                    ch_j "Who's \"Jessie?\""
                    $ JeanX.FaceChange("normal",Eyes="psychic")
                    ch_j ". . ."
                    $ JeanX.FaceChange("surprised")
                    call HWStatup(JeanX,"Inbt", 50, 1)
                    ch_j "Oh. . . she looks pretty bad ass."
                    $ JeanX.FaceChange("angry",Eyes="side")
                    call HWStatup(JeanX,"Inbt", 50, 1)
                    ch_j "I probably should have gone as her."
                    $ JeanX.FaceChange("normal",Eyes="psychic")
                    call HWStatup(JeanX,"Obed", 70, 1)
                    call HWStatup(JeanX,"Inbt", 70, 1)
                    ch_j "Everyone just picture me as \"Jessie\" for the rest of the party."
                    $ JeanX.FaceChange("smile",Eyes="surprised")
                    call HWStatup(JeanX,"Inbt", 70, 2)
                    "You hear mumbles of \"yes, Jessie\". . ."
                    $ JeanX.AddWord(1,"jessie",0) #adds "jessie" to Recent
        $ JeanX.FaceChange("smile")
        show Jean_Sprite:
                ease 1 pos (300,50)
        pause 1
        "[JeanX.Name] starts to wander off."
        menu:
            extend ""
            "Jean?":
                call HWStatup(JeanX,"Love", 90, 1)
                call HWStatup(JeanX,"Obed", 70, 1)
                $ JeanX.FaceChange("confused")
                ch_j "Oh. Yes, you're still here."
                $ JeanX.FaceChange("confused",Eyes="side")
                ch_j "I was going to check in on the music situation real quick."
                $ JeanX.FaceChange("smile",Eyes="side")
                ch_j "I might be back later."
            "Let her go":
                pass
        show Jean_Sprite:
                ease 0.8 pos (-200,50)
        pause 0.8
        "She wanders into the crowd."

        call AllHide(1) #removes all girls
        $ Present.remove(JeanX)
        $ Nearby.append(JeanX)
        $ JeanX.Loc = "nearby"
        $ JeanX.FaceChange("normal")

        #End Jean Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


        #Start Storm Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

        if "met" not in StormX.History:
                jump Halloween_Party
        "You see a form out on the dance floor, and she notices you watching."
        "She dances her way over."
        #display Storm
        $ Present.append(StormX)
        $ StormX.FaceChange("smile")
        $ StormX.Loc = "HW Party"
        $ StormX.AddWord(1,0,StormX.Hair,0,"halloween") #adds "halloween" to History
        $ StormX.OutfitDay = "costume"
        $ StormX.Outfit = StormX.OutfitDay
        $ StormX.OutfitChange(Changed=1)
#        call Display_Girl(StormX)
        call Shift_Focus(StormX)
        show Storm_Sprite at sprite_location(1200,50):
                offset (0,0)
                anchor (0.5, 0.0)
                pos (1200,50)
                ease 0.8 pos (StageCenter,50)
        pause 0.8

        ch_s "Merry Halloween, [Player.Name]!"
        ch_s "Permit me to guess. . ."
        $ StormX.FaceChange("smile",Eyes="down")
        "She looks you up and down."
        $ StormX.FaceChange("smile")
        $ HWLine = ["Some form of vagabond? Yes?","You are a dashing swashbuckler!","You are a deadly Hand ninja.",". . . Ah! You are a valiant fire fighter!"]
        $ HWLine = HWLine[Costume]
        ch_s "[HWLine]"
        menu:
            extend ""
            "Yeah, you got it.":
                    call HWStatup(StormX,"Love", 90, 1)
                    ch_s "Excellent, it is a wonderful costume."
            "No, I just went casual." if not Costume:
                    $ StormX.FaceChange("surprised",Eyes="normal")
                    ch_s "Oh."
                    $ StormX.FaceChange("smile")
                    ch_s "Well, I could hardly tell."
                    ch_s "We do perhaps need to take you out shopping some time. . ."
                    ch_s "I do have a friend that could help us with that. . ."
            "No, this is just how I dress now." if Costume:
                    $ StormX.FaceChange("smile",Eyes="side")
                    call HWStatup(StormX,"Obed", 40, 1)
                    ch_s "Oh."
                    $ StormX.FaceChange("smile")
                    ch_s "Well, you do make some interesting choices."
                    call HWStatup(StormX,"Inbt", 50, 1)
                    $ StormX.FaceChange("normal",Eyes="down")
                    pause 0.4
                    $ StormX.FaceChange("smile")
                    ch_s "I suppose that I do as well."
                    $ StormX.FaceChange("smile")
            "Skip the intros." if "halloween" in Player.History:
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
                    $ StormX.FaceChange("surprised",Mouth="smile")
                    call HWStatup(StormX,"Love", 80, 1)
                    call HWStatup(StormX,"Love", 90, 1)
                    ch_s "Yes! you guessed it!"
                    $ StormX.FaceChange("smile")
                    ch_s "I was told that she was a popular video game character."
                    $ StormX.FaceChange("smile",Eyes="stunned")
                    ch_s "And we had similar hair."
                    $ StormX.FaceChange("smile")
            "Is it clothes from your homeland?":
                    $ StormX.FaceChange("surprised",2,Mouth="open")
                    call HWStatup(StormX,"Love", 90, 1)
                    call HWStatup(StormX,"Obed", 50, 1)
                    ch_s "Oh, no, that it not the look that I was going for."
                    $ StormX.FaceChange("normal",1)
                    ch_s "But I can understand the error."
                    $ StormX.FaceChange("smile",Eyes="down")
                    ch_s "I did wear something like this back in Kenya. . ."
                    $ StormX.FaceChange("sly")
                    call HWStatup(StormX,"Love", 90, 1)
                    ch_s "It did not have the top, however."
            "A ring toss?":
                    $ StormX.FaceChange("angry",2,Mouth="open")
                    call HWStatup(StormX,"Love", 90, -2)
                    call HWStatup(StormX,"Obed", 50, 1)
                    ch_s "How very rude of you!"
                    $ StormX.FaceChange("angry",1,Mouth="open")
                    ch_s "I shall have you know that these are the cultural ornaments of my people!"
                    menu:
                        extend ""
                        "Sorry!":
                            $ StormX.FaceChange("angry")
                            ch_s "Oh, are you. . ."
                            call HWStatup(StormX,"Love", 70, 1)
                            call HWStatup(StormX,"Love", 90, 1)
                        "They look really sexy though.":
                            $ StormX.FaceChange("sexy")
                            ch_s "Oh, they do, do they?"
                            call HWStatup(StormX,"Love", 80, 1)
                            call HWStatup(StormX,"Obed", 60, 1)
                            call HWStatup(StormX,"Inbt", 80, 1)
                        "Oh, ok.":
                            $ StormX.FaceChange("angry",Eyes="side")
                            call HWStatup(StormX,"Love", 90, -1)
                            call HWStatup(StormX,"Obed", 60, 1)
                            ch_s ". . ."
                    $ StormX.FaceChange("smile")
                    call HWStatup(StormX,"Love", 90, 2)
                    ch_s "I am only joking!"
                    ch_s "This is a video game character."
                    ch_s "I believe that the rings were drawn up by someone in Japan."
        menu:
            extend ""
            "You look great!":
                    call HWStatup(StormX,"Love", 80, 1)
                    call HWStatup(StormX,"Love", 90, 1)
                    ch_s "Oh, well thank you."
                    ch_s "That is sweet of you to say."
                    ch_s "I am glad that the costume was a hit."
            "I love the new hair.":
                    call HWStatup(StormX,"Love", 80, 1)
                    call HWStatup(StormX,"Love", 90, 1)
                    call HWStatup(StormX,"Inbt", 70, 1)
                    ch_s "Yes, it certainly is low maintenance."
                    ch_s "I may keep it after."
            "Very sexy.":
                    $ StormX.FaceChange("smile",Mouth="kiss")
                    call HWStatup(StormX,"Love", 80, 1)
                    call HWStatup(StormX,"Obed", 50, 1)
                    call HWStatup(StormX,"Inbt", 50, 1)
                    ch_s "Oh!"
                    $ StormX.FaceChange("sexy")
                    call HWStatup(StormX,"Inbt", 70, 1)
                    call HWStatup(StormX,"Lust", 60, 1)
                    ch_s "Well, I suppose that it is that too. . ."
            "So have you seen [EmmaX.Name] around?":
                    $ StormX.FaceChange("smile",Brows="confused")
                    call HWStatup(StormX,"Love", 90, -1)
                    call HWStatup(StormX,"Obed", 50, 1)
                    call HWStatup(StormX,"Obed", 70, 1)
                    ch_s "Tired of my company so soon?"
                    $ StormX.FaceChange("smile",Eyes="side")
                    ch_s "Yes, I believe that I did see her under that tree earlier."
                    ch_s "Send her my regards."
        $ StormX.FaceChange("smile")
        ch_s "In any case, I still have to \"get my groove on.\""
        ch_s "Perhaps I will see you later."
        show Storm_Sprite:
                ease 0.8 pos (1200,50)
        pause 0.8
        "[StormX.Name] glides back onto the dance floor, and you head over toward the treeline."

        call AllHide(1) #removes all girls
        $ Present.remove(StormX)
        $ Nearby.append(StormX)
        $ StormX.Loc = "nearby"

        #End Storm Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Halloween_Emma:
        #Start Emma Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

        if "met" not in EmmaX.History:
                jump Halloween_Party
        "You see [EmmaX.Name] standng under the trees, talking to one of the other students."

        #display Emma here in costume
        $ Present.append(EmmaX)
        $ EmmaX.Loc = "HW Party"
        $ EmmaX.FaceChange("smile")
        $ EmmaX.AddWord(1,0,EmmaX.Hair,0,"halloween") #adds "halloween" to History
        $ EmmaX.OutfitDay = "costume"
        $ EmmaX.Outfit = EmmaX.OutfitDay
        $ EmmaX.OutfitChange(Changed=1)
#        call Display_Girl(EmmaX)
        call Shift_Focus(EmmaX)
        show Emma_Sprite at sprite_location(-200,50):
                offset (0,0)
                anchor (0.5, 0.0)
                pos (-200,50)
                ease 0.8 pos (StageCenter,50)
        pause 0.8

        ch_e "Oh, [EmmaX.Petname], lovely evening, isn't it?"
        menu:
            extend ""
            "Yeah.":
                    pass
            "Let me guess, Lady D?":
                    $ EmmaX.FaceChange("confused")
                    call HWStatup(EmmaX,"Love", 90, -1)
                    call HWStatup(EmmaX,"Obed", 50, 1)
                    ch_e "Princess Diana?"
                    ch_e "No, I have no idea what you mean, I am [EmmaX.Name]."
                    ch_e "[EmmaX.Name]."
                    menu:
                        extend ""
                        "Oh. . . ok.":
                                call HWStatup(EmmaX,"Love", 90, 1)
                                call HWStatup(EmmaX,"Obed", 50, 1)
                                call HWStatup(EmmaX,"Inbt", 50, 1)
                                call HWStatup(EmmaX,"Lust", 50, 1)
                                ch_e "That young Ms. Grey hasn't been tampering with your mind, has she? . ."
                        "I knew that!":
                                call HWStatup(EmmaX,"Love", 90, 1)
                                call HWStatup(EmmaX,"Obed", 50, 1)
                                call HWStatup(EmmaX,"Inbt", 50, 1)
                                call HWStatup(EmmaX,"Lust", 50, 1)
                                ch_e "I'm sure you did. . ."
                        "I meant the giant vampire lady!":
                                $ EmmaX.FaceChange("confused",2,Eyes="surprised")
                                $ EmmaX.AddWord(1,"vampire",0) #adds "vampire" to Recent
            "Let me guess, that giant vampire lady?":
                    $ EmmaX.FaceChange("confused",2)
                    $ EmmaX.AddWord(1,"vampire","vampire") #adds "vampire" to Recent and Daily
            "Skip the intros." if "halloween" in Player.History:
                    menu:
                        "Are you sure you want to skip the remaining inros and go straight to the party?"
                        "Yes":
                            jump Halloween_Skip
                        "Never mind":
                            ch_p "Sorry, I spaced out there."


        if "vampire" in EmmaX.RecentActions:
                call HWStatup(EmmaX,"Love", 70, -2)
                call HWStatup(EmmaX,"Love", 90, -1)
                call HWStatup(EmmaX,"Obed", 50, 1)
                #you implied that she was giant
                $ EmmaX.FaceChange("angry",1,Eyes="side")
                ch_e "Well I'm not sure how offended I'm meant to be by that."
                ch_e "It's not often that someone refers to me as \"giant.\""
                menu:
                    extend ""
                    "Your costume! I meant the giant vampire lady from the game!":
                            $ EmmaX.FaceChange("surprised",1)
                            call HWStatup(EmmaX,"Love", 90, -1)
                            ch_e "Costume?"
                            $ EmmaX.FaceChange("confused")
                            ch_e "What costume?"
                            $ EmmaX.DrainWord("vampire",1,0,0)
                    "Well, I just meant. . . in certain areas.":
                            $ EmmaX.FaceChange("angry")
                            call HWStatup(EmmaX,"Obed", 50, 1)
                            call HWStatup(EmmaX,"Obed", 70, 1)
                            call HWStatup(EmmaX,"Inbt", 50, 1)
                            if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 400, "O"):
                                    ch_e ". . ."
                                    $ EmmaX.FaceChange("sexy")
                                    call HWStatup(EmmaX,"Love", 90, 1)
                                    call HWStatup(EmmaX,"Inbt", 50, 1)
                                    call HWStatup(EmmaX,"Lust", 50, 1)
                                    ch_e "I will let you off the hook for that one."
                            else:
                                    call HWStatup(EmmaX,"Obed", 50, 1)
                                    ch_e "That is still an entirely inappropriate way to talk to a lady."
                    "You do have some giant tits.":
                            $ EmmaX.FaceChange("angry")
                            call HWStatup(EmmaX,"Obed", 50, 1)
                            call HWStatup(EmmaX,"Obed", 70, 1)
                            call HWStatup(EmmaX,"Inbt", 70, 1)
                            if ApprovalCheck(EmmaX, 1300) or ApprovalCheck(EmmaX, 500, "O"):
                                    ch_e ". . ."
                                    $ EmmaX.FaceChange("sexy")
                                    call HWStatup(EmmaX,"Love", 90, 1)
                                    call HWStatup(EmmaX,"Inbt", 50, 1)
                                    call HWStatup(EmmaX,"Lust", 50, 1)
                                    call HWStatup(EmmaX,"Lust", 60, 1)
                                    ch_e "I suppose that I can't disagree."
                            else:
                                    call HWStatup(EmmaX,"Love", 90, -1)
                                    call HWStatup(EmmaX,"Inbt", 50, 1)
                                    call HWStatup(EmmaX,"Lust", 50, 1)
                                    ch_e "And -you- need to remove your mind from the gutter."
                    "Sorry, never mind. . .":
                            $ EmmaX.FaceChange("angry",Eyes="side")
                            call HWStatup(EmmaX,"Love", 90, 1)
                            call HWStatup(EmmaX,"Inbt", 50, 1)
                            ch_e "Well. . . I suppose I can allow that to slide."
                            $ EmmaX.FaceChange("normal")
                            ch_e "Still, a very unusual direction for your mind to wander."
        if "vampire" in EmmaX.RecentActions:
                $ EmmaX.FaceChange("normal",Brows="confused")
                ch_e "And why \"vampire?\""
                ch_e "Do you think that I'm spending too much time with Miss Lee?"
                menu:
                    extend ""
                    "Um, yeah, that must be it.":
                            $ EmmaX.FaceChange("normal",Eyes="side")
                            call HWStatup(EmmaX,"Love", 90, 2)
                            ch_e "Well, certainly not enough to contract her. . . affliction"
                    "What? Oh, never mind.":
                            $ EmmaX.FaceChange("normal")
                            call HWStatup(EmmaX,"Love", 90, 1)
                            call HWStatup(EmmaX,"Obed", 50, 1)
                            ch_e "Well, whatever. . ."
                    "Your costume! I meant the giant vampire lady from the game!":
                            $ EmmaX.FaceChange("surprised",1)
                            call HWStatup(EmmaX,"Love", 90, -1)
                            call HWStatup(EmmaX,"Obed", 50, 1)
                            ch_e "Costume?"
                            $ EmmaX.FaceChange("confused")
                            ch_e "What costume?"
                            $ EmmaX.DrainWord("vampire",1,0,0)
        $ EmmaX.FaceChange("normal",Eyes="down")
        ch_e "I'd heard this would be a \"fancy dress\" party, so I just dressed for the occasion."
        $ EmmaX.FaceChange("angry",Eyes="side")
        ch_e "Now that you mention it, the other students are a bit. . . flamboyantly attired."
        $ EmmaX.FaceChange("angry",Eyes="down")
        ch_e "Does that explain why you're dressed as some sort of. . ."
        $ HWLine = ["Well, I suppose that's how you always look.","Rogue seaman?","Sneakthief?","Fireman?"]
        $ EmmaX.FaceChange("normal",Brows="confused")
        $ HWLine = HWLine[Costume]
        ch_e "[HWLine]"
        if Costume == 1:
            menu:
                extend ""
                "That's me, definitely \"rogue semen.\"":
                        $ EmmaX.FaceChange("smile",Brows="surprised")
                        call HWStatup(EmmaX,"Obed", 50, 1)
                        call HWStatup(EmmaX,"Inbt", 50, 1)
                        call HWStatup(EmmaX,"Inbt", 70, 1)
                        call HWStatup(EmmaX,"Lust", 50, 2)
                        ch_e "Ha! you have a filthy mind."
                        $ EmmaX.FaceChange("sly")
                        ch_e "We'd better put that to good use. . ."
                "A pirate, actually. . .":
                        $ EmmaX.FaceChange("smile")
                        call HWStatup(EmmaX,"Love", 90, 1)
                        call HWStatup(EmmaX,"Obed", 50, 1)
                        ch_e "Oh, yes! Quite the marauder you make."
        elif Costume == 2:
            menu:
                extend ""
                "I guess I could pocket a few things. . .":
                        $ EmmaX.FaceChange("smile",Brows="confused")
                        call HWStatup(EmmaX,"Obed", 50, 1)
                        call HWStatup(EmmaX,"Inbt", 50, 1)
                        ch_e "Probably best that you don't. . ."
                "A ninja, actually.":
                        $ EmmaX.FaceChange("smile")
                        call HWStatup(EmmaX,"Obed", 50, 1)
                        call HWStatup(EmmaX,"Inbt", 50, 1)
                        ch_e "Ah!, I thought you looked a bit like a Hand Ninja."
            $ EmmaX.FaceChange("smile")
        elif Costume == 3:
            menu:
                extend ""
                "No, I'm a. . . oh, yeah, a fireman.":
                        $ EmmaX.FaceChange("smile")
                        call HWStatup(EmmaX,"Love", 90, 1)
                        call HWStatup(EmmaX,"Obed", 60, 1)
                        call HWStatup(EmmaX,"Inbt", 60, 1)
                        ch_e "I knew it. . ."
                "You guessed it!":
                        $ EmmaX.FaceChange("smile")
                        call HWStatup(EmmaX,"Love", 90, 1)
                        call HWStatup(EmmaX,"Inbt", 50, 1)
                        call HWStatup(EmmaX,"Inbt", 70, 1)
                        ch_e "Of course!"
            $ EmmaX.FaceChange("sly")
            call HWStatup(EmmaX,"Lust", 50, 2)
            call HWStatup(EmmaX,"Lust", 70, 1)
            ch_e "I do have a bit of experience with firemen. . ."
        else:
            menu:
                extend ""
                "Oh, yeah?":
                        $ EmmaX.FaceChange("sad")
                        call HWStatup(EmmaX,"Love", 90, -1)
                        call HWStatup(EmmaX,"Obed", 50, 1)
                        ch_e "No, it's. . . fine."
                "I didn't feel like dressing up.":
                        call HWStatup(EmmaX,"Love", 90, -1)
                        call HWStatup(EmmaX,"Obed", 50, 1)
                        call HWStatup(EmmaX,"Obed", 70, 1)
                        ch_e "No, I. . . can see that. . ."
            $ EmmaX.FaceChange("angry", Eyes="side")
            ch_e "We might have to take you shopping at some point though. . ."
        $ EmmaX.FaceChange("normal",Brows="sad")
        ch_e "And do you have anything to say about mine?"
        menu:
            extend ""
            "No, not really.":
                    if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 400, "O"):
                            $ EmmaX.FaceChange("sadside")
                            call HWStatup(EmmaX,"Love", 90, -1)
                            call HWStatup(EmmaX,"Obed", 70, 2)
                            call HWStatup(EmmaX,"Obed", 90, 1)
                            ch_e "Oh. . ."
                            ch_e "Pity."
                    else:
                            $ EmmaX.FaceChange("angry")
                            call HWStatup(EmmaX,"Love", 80, -2)
                            call HWStatup(EmmaX,"Love", 90, -1)
                            call HWStatup(EmmaX,"Obed", 50, 1)
                            ch_e "Well!"
                            ch_e "I suppose that I shouldn't have asked in the first place."

            "Oh, it's very nice.":
                    $ EmmaX.FaceChange("smile")
                    call HWStatup(EmmaX,"Love", 70, 2)
                    call HWStatup(EmmaX,"Love", 90, 1)
                    call HWStatup(EmmaX,"Inbt", 50, 1)
                    ch_e "I'm glad you can appreciate fine things."
            "Love the hat.":
                    $ EmmaX.FaceChange("smile",Eyes="stunned")
                    call HWStatup(EmmaX,"Love", 80, 1)
                    call HWStatup(EmmaX,"Love", 90, 2)
                    call HWStatup(EmmaX,"Obed", 70, 1)
                    call HWStatup(EmmaX,"Inbt", 70, 1)
                    ch_e "Oh, yes, I saw it in a shop in town and thought that I must have that. . ."
                    $ EmmaX.FaceChange("smile")
            "Definitely looks like the vampire lady.":
                    if "vampire" in EmmaX.RecentActions:
                            $ EmmaX.FaceChange("angry",2,Eyes="surprised")
                            call HWStatup(EmmaX,"Love", 80, -1)
                            call HWStatup(EmmaX,"Obed", 50, 1)
                            ch_e "I have no idea what you're talking about!"
                    else:
                            $ EmmaX.FaceChange("angry",2)
                            call HWStatup(EmmaX,"Obed", 50, 1)
                            call HWStatup(EmmaX,"Obed", 70, 1)
                            ch_e "Well I'm certain that any resemblance is -purely- coincidental."
                            $ EmmaX.FaceChange("angry",1)
                            ch_e "Are we -clear?-"
                    $ EmmaX.FaceChange("normal",1)
        ch_e "In any case. . ."
        ch_e "It is nice to have a little soiree. . . I do hope to see you later in the evening."
        ch_e "For the moment, I'll need to excuse myself."
        show Emma_Sprite:
                ease 0.8 pos (-200,50)
        pause 0.8
        "[EmmaX.Name] heads over to the refreshments."

        call AllHide(1) #removes all girls
        $ Present.remove(EmmaX)
        $ Nearby.append(EmmaX)
        $ EmmaX.Loc = "nearby"

        #End Emma Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

        jump Halloween_Party

        return

label Halloween_Skip:
        call AllHide(1) #removes all girls
        $ Options = ActiveGirls[:]  #loads up all local girls
        if LauraX in Options and "angry" in LauraX.RecentActions:
                #if you pissed her off, leave her out of it.
                $ Options.remove(LauraX)
        while Options:
                while Options[0] in Present:
                        $ Present.remove(Options[0])
                if Options[0] not in Nearby:
                        $ Nearby.append(Options[0])
                $ Options[0].Loc = "HW Party"
                $ Options[0].OutfitDay = "costume"
                $ Options[0].Outfit = EmmaX.OutfitDay
                $ Options[0].OutfitChange(Changed=1)
                $ Options[0].AddWord(1,0,0,0,"halloween") #adds "halloween" to History

                $ Options.remove(Options[0])


label Halloween_Party:
        #the looping portion of the party
        call Halloween_Events #spits out a randomized description of the party.
        if Round <= 10:
            call Halloween_Ending
        menu:
            "You are at the Halloween Party. What would you like to do?"
            "Talk to [RogueX.Name]." if RogueX.Loc == "HW Party" or RogueX.Loc == "nearby":
                        call Halloween_Chat(RogueX)
            "Talk to [KittyX.Name]." if KittyX.Loc == "HW Party" or KittyX.Loc == "nearby":
                        call Halloween_Chat(KittyX)
            "Talk to [EmmaX.Name]." if EmmaX.Loc == "HW Party" or EmmaX.Loc == "nearby":
                        call Halloween_Chat(EmmaX)
            "Talk to [LauraX.Name]." if LauraX.Loc == "HW Party" or LauraX.Loc == "nearby":
                        call Halloween_Chat(LauraX)
            "Talk to [JeanX.Name]." if JeanX.Loc == "HW Party" or JeanX.Loc == "nearby":
                        call Halloween_Chat(JeanX)
            "Talk to [StormX.Name]." if StormX.Loc == "HW Party" or StormX.Loc == "nearby":
                        call Halloween_Chat(StormX)
            "Leave the party":
                        call Halloween_Ending
        jump Halloween_Party


label Halloween_Events:
        if not HWEvents:
                #first time through for the night
                $ Round -= 15
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
                $ Player.AddWord(1,"halloween","halloween",0,"halloween") #adds "halloween" to History
                "Introductions out of the way, you take a look around the party in progress."
        "[HWEvents[0]]"
        $ Round -= 5
        $ HWEvents.remove(HWEvents[0])
        return

label Halloween_Ending(Girl=0):
        "As the evening comes to a close, did you want to meet up with anyone in particular?"
        menu:
            "Talk to [RogueX.Name]." if RogueX.Loc == "HW Party" or RogueX.Loc == "nearby":
                            $ Girl = RogueX
            "Talk to [KittyX.Name]." if KittyX.Loc == "HW Party" or KittyX.Loc == "nearby":
                            $ Girl = KittyX
            "Talk to [EmmaX.Name]." if EmmaX.Loc == "HW Party" or EmmaX.Loc == "nearby":
                    if "classcaught" in EmmaX.History:
                            $ Girl = EmmaX
                    else:
                            ch_e "I really had a lovely time tonight, but I have to call it an evening."
                            ch_e "I hope to see you tomorrow. . ."
                            $ EmmaX.Loc = "bg emma"
                            call Halloween_Ending
            "Talk to [LauraX.Name]." if LauraX.Loc == "HW Party" or LauraX.Loc == "nearby":
                            $ Girl = LauraX
            "Talk to [JeanX.Name]." if JeanX.Loc == "HW Party" or JeanX.Loc == "nearby":
                            $ Girl = JeanX
            "Talk to [StormX.Name]." if StormX.Loc == "HW Party" or StormX.Loc == "nearby":
                            $ Girl = StormX
            "No thanks.":
                            $ Girl = 0

        $ bg_current = "bg player"
        call Wait
        call Girls_Location
        if Girl:
            $ Girl.Loc = "bg player"
            #put girl in costume
            call Set_The_Scene(Quiet=1)
            $ Girl.FaceChange("smile",1)
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
        jump Misplaced
        return
