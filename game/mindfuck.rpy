
label MindFuck_Screen: #rkeljsv
        #Displays the current background as a ghost
        if bg_current in PersonalRooms:
                call RoomMask #in Rogue Animations


        elif bg_current == "bg classroom":
                    show bg_classmask onlayer black:
                        alpha .2
        elif bg_current == "bg dangerroom":
                    show bg_danger onlayer black:
                        alpha .2
        elif bg_current == "bg showerroom":
                    show bg_shower onlayer black:
                        alpha .2
        elif bg_current == "bg study":
                    show bg_study onlayer black:
                        alpha .2
        elif bg_current == "bg movies":
                    show bg_movies onlayer black:
                        alpha .2
        elif bg_current == "bg restaurant":
                    show bg_rest onlayer black:
                        alpha .2
        elif bg_current == "bg pool":
                    show bg_pool onlayer black:
                        alpha .2
        else: # if 'bg campus' or anything else
                    show bg_campus onlayer black:
                        alpha .2
        return

label PsychicFlash(Face="sly",TempLoc=0): #rkeljsv
        call MindFuck_Screen
        $ Line = Girl.Loc
        $ Girl.Loc = bg_current
        call Set_The_Scene(1,0,0,0,1)
        if Face:
                $ Girl.FaceChange(Face)
        $ Girl.ArmPose = 2
        $ Girl.Uptop = 1
        $ Girl.Upskirt = 1
        $ Girl.PantiesDown = 1
        ". . . {w=0.3}{nw}"
        if Girl == EmmaX:
                hide Emma_Sprite with fade
        elif Girl == JeanX:
                hide Jean_Sprite with fade
        $ Girl.OutfitChange(6,Changed=1)
        scene onlayer black
        $ Girl.ArmPose = 1
        $ Line = 0
        call AnyLine(Girl,". . .")


label MindFuck(TempLoc=0): #rkeljsv
        #having sex with a girl in her head
        if Girl == EmmaX:
                ch_e "Would you prefer to have some telepathic sex?"
        elif Girl == JeanX:
                ch_j "Wouldn't telepathic sex be more fun?"
        menu MindFuck_Menu:
            "Sure":
                    if Girl == EmmaX:
                            ch_e "Lovely. . ."
                            ch_e "Just let me prepare us. . ."
                    elif Girl == JeanX:
                            ch_j "Great!"
                            ch_j "Ok, looping you in. . ."

                    call MindFuck_Screen
                    $ TempLoc = Girl.Loc
                    $ Girl.Loc = bg_current
                    $ Girl.FaceChange("sly")
                    #call Display_Girl(EmmaX,0,0)
                    call Set_The_Scene(1,0,0,0,1)
                    call AnyLine(Girl,"There. . .")

                    $ Player.AddWord(1,"MindFuck","MindFuck",0,"MindFuck")
                    call expression Girl.Tag + "_SexMenu" #call Rogue_SexMenu

                    $ Girl.Loc = TempLoc
                    if Girl == EmmaX:
                            ch_e "That'll be all for now. . ."
                            ch_e "I'll see you in your dreams. . ."
                    elif Girl == JeanX:
                            ch_j "Ok, that'll do it. . ."
                            ch_j "Be thinking about me. . ."

                    $ Girl.OutfitChange(6,Changed=1)
                    $ Girl.Spunk = []
                    if Girl == EmmaX:
                            hide Emma_Sprite with fade
                    elif Girl == JeanX:
                            hide Jean_Sprite with fade
                    scene onlayer black
                    jump Misplaced
            "What is that?" if "mfuck?" not in Player.RecentActions and "MindFuck" not in Player.History:
                    if Girl == EmmaX:
                            ch_e "Well, if you open your mind a bit, I could project into it."
                            ch_e "Then we could have. . . all sorts of fun. . ."
                    elif Girl == JeanX:
                            ch_j "You know, like if you let your guards down a little. . ."
                            ch_j "I could work my way in there and we could have some fun. . ."
                    $ Player.AddWord(1,"mfuck?")
                    jump MindFuck_Menu
            "Nah, over the phone is fine.":
                    if Girl == EmmaX:
                            ch_e "Fine, be boring. . ."
                    elif Girl == JeanX:
                            ch_j "Lame. . ."
                    return
        return
