label MindFuck_Screen:

    if bg_current in personal_rooms:
        call RoomMask




















    elif bg_current == "bg_classroom":
        show bg_classmask onlayer black:
            alpha .2
    elif bg_current == "bg_dangerroom":
        show bg_danger onlayer black:
            alpha .2
    elif bg_current == "bg_showerroom":
        show bg_shower onlayer black:
            alpha .2
    elif bg_current == "bg_study":
        show bg_study onlayer black:
            alpha .2
    elif bg_current == "bg_movies":
        show bg_movies onlayer black:
            alpha .2
    elif bg_current == "bg_restaurant":
        show bg_rest onlayer black:
            alpha .2
    elif bg_current == "bg_pool":
        show bg_pool onlayer black:
            alpha .2
    else:
        show bg_campus onlayer black:
            alpha .2
    return

label psychicFlash(Face="_sly", TempLoc=0):
    call MindFuck_Screen
    $ line = Girl.location
    $ Girl.location = bg_current
    call set_the_scene (1, 0, 0, 0, 1)
    if Face:
        $ Girl.change_face(Face)
    $ Girl.arm_pose = 2
    $ Girl.top_pulled_up = 1
    $ Girl.upskirt = 1
    $ Girl.underwear_pulled_down = 1
    ". . . {w=0.3}{nw}"
    if Girl == EmmaX:
        hide Emma_sprite with fade
    elif Girl == JeanX:
        hide Jean_sprite with fade
    $ Girl.change_outfit("today")
    scene onlayer black
    $ Girl.arm_pose = 1
    $ line = 0
    Girl.voice ". . ."


label MindFuck(TempLoc=0):

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
            $ TempLoc = Girl.location
            $ Girl.location = bg_current
            $ Girl.change_face("_sly")

            call set_the_scene (1, 0, 0, 0, 1)
            Girl.voice "There. . ."

            $ Player.add_word(1,"MindFuck","MindFuck", 0,"MindFuck")
            call shift_focus(Girl)
            call enter_main_sex_menu(Girl)

            $ Girl.location = TempLoc
            if Girl == EmmaX:
                ch_e "That'll be all for now. . ."
                ch_e "I'll see you in your dreams. . ."
            elif Girl == JeanX:
                ch_j "Ok, that'll do it. . ."
                ch_j "Be thinking about me. . ."

            $ Girl.change_outfit("today")

            python:
                for key in Girl.spunk.keys():
                    Girl.spunk[key] = False

            if Girl == EmmaX:
                hide Emma_sprite with fade
            elif Girl == JeanX:
                hide Jean_sprite with fade
            scene onlayer black
            jump reset_location
        "What is that?" if "mfuck?" not in Player.recent_history and "MindFuck" not in Player.history:
            if Girl == EmmaX:
                ch_e "Well, if you open your mind a bit, I could project into it."
                ch_e "Then we could have. . . all sorts of fun. . ."
            elif Girl == JeanX:
                ch_j "You know, like if you let your guards down a little. . ."
                ch_j "I could work my way in there and we could have some fun. . ."
            $ Player.add_word(1,"mfuck?")
            jump MindFuck_Menu
        "Nah, over the phone is fine.":
            if Girl == EmmaX:
                ch_e "Fine, be boring. . ."
            elif Girl == JeanX:
                ch_j "Lame. . ."
            return
    return
