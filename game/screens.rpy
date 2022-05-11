# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.


##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False, CountWords = 0): #CountWords is just a counter used with the gag

    # Decide if we want to use the one-window or two-window variant.

    if who == "N":
            $ who = Ch_Focus.Name

    if not two_window:
        # The one window variant. Used for caption boxes
        window:
#            xpos 0.0
#            xanchor 0.0

            pos (0.0,0.1) #(0.3,0.1)
            anchor (0.0,0.0)

            style "textbox"

            id "textbox"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what" color "#000000" font "CRIMFBRG.ttf"
            #text what id "what"
    else:
        # The two window variant. Used for character dialog
        # start gag code
        if who == "Rogue" and RogueX.Gag:
            $ CountWords = 1
        elif who == "Kitty" and KittyX.Gag:
            $ CountWords = 1
        if CountWords == 1:
            $ CountWords = what.count(" ") if what.count(" ") <= 10 else 10
            $ CountWords = CountWords - what.count(".")
            $ what = ""
            python:
                while CountWords >= 0:
                    CountWords -= 1
                    what = what + renpy.random.choice(["Mrph",
                                                    "Hrgaph",
                                                    "Rhgn",
                                                    "Phar",
                                                    "Geghs",
                                                    "Paha",
                                                    "Grde",
                                                    "Phraph",
                                                    "Ugh"])
                    if CountWords:
                        what = what + " "
                    else:
                        what = what + "."
        # End gag code

        vbox:
            #Main chat text window
            pos (0.0,0.1) #(0.7,0.1)
            anchor (0.0,0.0)#(1.0,0.0)

            style "say_two_window_vbox"

            window:    #rkeljs
                    if who == GwenName: #new code. . .
                        style "say_balloon" background Frame("images/WordballoonG.png", 50, 50)
                    else:
                        style "say_balloon"

#                    has vbox:
#                            style "say_balloon"

                    text what id "what" color "#000000" font "CRIMFBRG.ttf" text_align 0.5

            if who == RogueX.Name: #"Rogue":              #rkeljsv
                    if RogueX.Loc != bg_current or RogueX.sprite_location == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    elif RogueX.sprite_location == StageRight or RogueX.sprite_location == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                    else: #RogueX.sprite_location == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8
            elif who == KittyX.Name:
                    if KittyX.Loc != bg_current or KittyX.sprite_location == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    elif KittyX.sprite_location == StageRight or KittyX.sprite_location == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                    else: #KittyX.sprite_location == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8
            elif who == EmmaX.Name:
                    if EmmaX.Loc != bg_current or EmmaX.sprite_location == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    elif EmmaX.sprite_location == StageRight or EmmaX.sprite_location == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                    else: #EmmaX.sprite_location == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8
            elif who == LauraX.Name:
                    if LauraX.Loc != bg_current or LauraX.sprite_location == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    elif LauraX.sprite_location == StageRight or LauraX.sprite_location == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                    else: #LauraX.sprite_location == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8
            elif who == JeanX.Name:
                    if JeanX.Loc != bg_current or JeanX.sprite_location == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    elif JeanX.sprite_location == StageRight or JeanX.sprite_location == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                    else: #JeanX.sprite_location == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8
            elif who == StormX.Name:
                    if StormX.Loc != bg_current or StormX.sprite_location == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    elif StormX.sprite_location == StageRight or StormX.sprite_location == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                    else: #StormX.sprite_location == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8
            elif who == JubesX.Name:
                    if JubesX.Loc != bg_current or JubesX.sprite_location == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    elif JubesX.sprite_location == StageRight or JubesX.sprite_location == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                    else: #JubesX.sprite_location == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8
            elif who == GwenName:
                        add "arrowG" xalign 0.15   # xalign 0.8
            elif who == Player.Name or who == "Danger Room": #elif who == Playername or who == "Danger Room":
                    pass
            elif who == "Professor X":
                    add "arrow" xalign 0.8
            elif who:
                    add "arrow" xalign 0.8

        if who:
            # this block is the name tag
            window:
                    pos (0.1,0.07) #(0.65,0.07)
                    anchor (0.5,0)#(0.5,0.5)
                    style "say_who_window"
#                    background Frame("images/WordballoonG.png", 50, 50)

                    text who:
                        size 15
                        id "who"
                        font "CRIMFBRG.ttf"

    # Use the quick menu.
    use quick_menu


image side arrow = "arrow"

image arrow:
    "images/Arrow.png"
    ypos -17
    xalign 0.5 #0.9
    zoom 1
    rotate 0

image arrowG:
    "images/ArrowG.png"
    ypos -17
    xalign 0.5 #0.9
    zoom 1
    rotate 0

##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xpos 20
        ypos 0.3
        yanchor 0.0

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:
                    if " (locked)" in caption:
                        $ caption = caption.replace(" (locked)", "")
                        button:
                            action None
                            style "menu_choice_button"
                            background "#424242"
                            text caption style "menu_choice" color "#6E6E6E"



                    else:               #to fix, just make this the default of "if action"
                        button:
                            action action
                            style "menu_choice_button"

                            text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True
    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.30) #* 0.45)
        xmaximum int(config.screen_width * 0.30)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt" color "#000000" size 20
        input id "input" style "input_text" color "#6E6E6E" size 25

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"
    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Start Game") action Start()
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Help") action Help()
        textbutton _("Disclaimer") action Show("Disclaimer_screen")
        textbutton _("Patreon") action OpenURL("http://www.patreon.com/OniArtist")
        textbutton _("Quit") action Quit(confirm=False)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox
                label _("There is no Audio")

#                label _("Music Volume")
#                bar value Preference("music volume")

#            frame:
#                style_group "pref"
#                has vbox

#                label _("Sound Volume")
#                bar value Preference("sound volume")

#                if config.sample_sound:
#                    textbutton _("Test"):
#                        action Play("sound", config.sample_sound)
#                        style "soundtest_button"

#            if config.has_voice:
#                frame:
#                    style_group "pref"
#                    has vbox

#                    label _("Voice Volume")
#                    bar value Preference("voice volume")

#                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
#                    if config.sample_voice:
#                        textbutton _("Test"):
#                            action Play("voice", config.sample_voice)
#                            style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"

##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"


##############################################################################
# My Bullshit
#
# This is the random crap I've added
#

#begin Roguebutton
screen roguebutton:
    imagebutton:
        auto "images/Button_Rogue_%s.png"
        action ui.callsinnewcontext("RogueWardrobe")
        xpos 690
        ypos 5
        focus_mask True

#end roguebutton

#begin Statbutton
screen statbutton:
#    if True: #"Rogue" in Party or R_Loc == bg_current:
    imagebutton:
        auto "images/Button_Rogue_%s.png"
        action ui.calls("RogueStats") #works action ui.callsinnewcontext("RogueStats") #works
        xpos 730
        ypos 5
        focus_mask True

#end statbutton

#begin Inventory Button
screen Inventorybutton:
    imagebutton:
        auto "images/UI_Backpack_%s.png"
        action Show("Inventory_screen")
        xpos 780
        ypos 5
        focus_mask True

#end Inventory Button

#Begin Status screen:

image Alt_Screen_Mask:
    # giant green mask for the second girl's menu
    contains:
        Solid("#159457", xysize=(800,150))
        alpha .5
        pos (0,-20)

screen Status_Screen:

    default tt = Tooltip(" ")

    #Under bar
    if Partner in TotalGirls:
        frame:
            background None
            pos (-100,30)
#            add "Alt_Screen_Mask"
            add  AlphaMask("images/BarBackdrop_"+Partner.Tag+".png", "Alt_Screen_Mask")
            frame:
                style_group "stat_bar"
                pos (100,25)
                background None
                has vbox
                hbox:
                    imagebutton idle "images/iconlust.png" hover "images/iconlust.png" action NullAction() hovered tt.Action("Lust: [Partner.Lust]")
                    bar range 100 value Partner.Lust xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0

                    imagebutton idle "images/iconlove.png" hover "images/iconlove.png" action NullAction() hovered tt.Action("Love: [Partner.Love]")
                    bar range 100 value (Partner.Love/10) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0

                    imagebutton idle "images/iconobed.png" hover "images/iconobed.png" action NullAction() hovered tt.Action("Obedience: [Partner.Obed]") #action NullAction("none")?
                    bar range 100 value (Partner.Obed/10) xmaximum 100 left_bar "images/barfullO.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0

                    imagebutton idle "images/iconinbt.png" hover "images/iconinbt.png" action NullAction() hovered tt.Action("Inhibitions: [Partner.Inbt]")
                    bar range 100 value (Partner.Inbt/10) xmaximum 100 left_bar "images/barfulli.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0

    #end Under bar

    #Primary bar
    #Kitty's stats

    if Ch_Focus in TotalGirls:
        add "images/BarBackdrop_"+Ch_Focus.Tag+".png"
        frame:
            style_group "stat_bar"
            xminimum 130
            background None
            has vbox
            hbox:
                imagebutton idle "images/iconlove.png" hover "images/iconlove.png" action NullAction() hovered tt.Action("Love: [Ch_Focus.Love]")
                bar range 100 value (Ch_Focus.Love/10) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
            hbox:
                imagebutton idle "images/iconlust.png" hover "images/iconlust.png" action NullAction() hovered tt.Action("Lust: [Ch_Focus.Lust]")
                bar range 100 value Ch_Focus.Lust xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
        frame:
            xminimum 130
            xpos 130
            background None
            has vbox
            hbox:
                imagebutton idle "images/iconobed.png" hover "images/iconobed.png" action NullAction() hovered tt.Action("Obedience: [Ch_Focus.Obed]")
                bar range 100 value (Ch_Focus.Obed/10) xmaximum 100 left_bar "images/barfullO.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
            hbox:
                imagebutton idle "images/iconaddict.png" hover "images/iconaddict.png" action NullAction() hovered tt.Action("Addiction: [Ch_Focus.Addict]")
                bar range 100 value Ch_Focus.Addict xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 6 thumb None thumb_offset 0
        frame:
            xminimum 130
            xpos 260
            background None
            has vbox
            hbox:
                imagebutton idle "images/iconinbt.png" hover "images/iconinbt.png" action NullAction() hovered tt.Action("Inhibitions: [Ch_Focus.Inbt]")
                bar range 100 value (Ch_Focus.Inbt/10) xmaximum 100 left_bar "images/barfulli.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
            hbox:
                imagebutton idle "images/iconaddictrate.png" hover "images/iconaddictrate.png" action NullAction() hovered tt.Action("Addiction Rate: [Ch_Focus.Addictionrate]")
                bar range 100 value (Ch_Focus.Addictionrate*10) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
        showif not Trigger:
    #            imagebutton auto "images/Button_Emma_%s.png" action ui.callsinnewcontext("Shift_Focus", "Emma") xpos 690 ypos 5 focus_mask True
            imagebutton auto "images/Button_"+Ch_Focus.Tag+"_%s.png" action ShowTransient("Focus_Map") xpos 690 ypos 5 focus_mask True #xpos 690 ypos 5
        showif config.developer:
            imagebutton auto "images/Button_"+Ch_Focus.Tag+"_%s.png" action ui.callsinnewcontext("StatHacks",Ch_Focus) xpos 730 ypos 5 focus



    frame:
        #Focus meter (dick)
        xminimum 130
        xpos 390
        background None
        has vbox
        hbox:
            bar range 100 value Player.Focus xmaximum 100 left_bar "images/barfullP.png" right_bar "images/baremptyP.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
        hbox:
            bar range 100 value (Player.Semen*20) xmaximum 100 left_bar "images/barfullS.png" right_bar "images/baremptyS.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
        imagebutton auto "images/Button_Emma_%s.png" action ui.callsinnewcontext("StatHacks",EmmaX) xpos 730 ypos 5 focus

    frame:
        # Money and level
        xminimum 75
        xpos 500
        background None
        has vbox
        hbox:
            text "Money: $[Player.Cash]" size 12
        hbox:
            text "Level: [Player.Lvl]" size 12
        hbox:
            text "[Ch_Focus.Tag] Level: [Ch_Focus.Lvl]" size 12
        # this block is the name tag
        window:
            pos (90,-40)#(-15,-8)
            anchor (0,0)
            style "say_who_window"
            text "[Ch_Focus.Name]" size 12 font "CRIMFBRG.ttf" color "#000000" #id "Ch_Focus"

    frame:
        #Clock
        xpos 900
        ypos 20
        background None

        add "images/Clockbase.png":
            anchor (0.5,0.5)
            yzoom -1
            subpixel True

        if Round < 50:
            add "images/Clockred.png" at rotate_red(Round):
                anchor (0.5,0.5)
                subpixel True
        else:
            add "images/Clockwhite.png" at rotate_white(Round):
                anchor (0.5,0.5)
                subpixel True

#        add "images/Clockface.png":
#            anchor (0.5,0.5)
        imagebutton idle "images/Clockface.png" hover "images/Clockface.png" action NullAction() hovered tt.Action("Time Left: [Round]%") anchor (0.5,0.5)

    frame:
        # Date and time
        xminimum 130
        xpos 920
        background None
        has vbox
        hbox:
            text "Day: [Day] [DayofWeek]" size 12
        hbox:
            text "Time: [Current_Time]" size 12
    frame:
        #displays small icons for nearby characters
        xpos 920
        ypos 30
        background None
        vbox:
            hbox: #rkeljsv
                if RogueX in Nearby:
                        imagebutton auto "images/Button_Rogue_%s.png" action NullAction() hovered tt.Action(RogueX.Name) at TinyButtons
                if KittyX in Nearby:
                        imagebutton auto "images/Button_Kitty_%s.png" action NullAction() hovered tt.Action(KittyX.Name) at TinyButtons
                if EmmaX in Nearby:
                        imagebutton auto "images/Button_Emma_%s.png" action NullAction() hovered tt.Action(EmmaX.Name) at TinyButtons
                if LauraX in Nearby:
                        imagebutton auto "images/Button_Laura_%s.png" action NullAction() hovered tt.Action(LauraX.Name) at TinyButtons
                if JeanX in Nearby:
                        imagebutton auto "images/Button_Jean_%s.png" action NullAction() hovered tt.Action(JeanX.Name) at TinyButtons
                if StormX in Nearby:
                        imagebutton auto "images/Button_Storm_%s.png" action NullAction() hovered tt.Action(StormX.Name) at TinyButtons
                if JubesX in Nearby:
                        imagebutton auto "images/Button_Jubes_%s.png" action NullAction() hovered tt.Action(JubesX.Name) at TinyButtons


    if tt.value != " ":
        # Pop-up mouse-over labels
        frame :
            xpos 500 ypos 60
            has vbox:
                text tt.value

transform TinyButtons:
    zoom .5

screen Focus_Map: #rkeljsv
    #changes focal character with dropdown box
    imagebutton auto "images/Button_X_%s.png" action Hide("Focus_Map") xpos 690 ypos 5 focus_mask True
    frame:
        xpos 684
        ypos 44
        hbox:
            vbox:
                imagebutton auto "images/Button_Rogue_%s.png" action ui.callsinnewcontext("Shift_Focus", RogueX) focus_mask True
                if "met" in KittyX.History:
                        imagebutton auto "images/Button_Kitty_%s.png" action ui.callsinnewcontext("Shift_Focus", KittyX) focus_mask True
                        # old way. . . imagebutton auto "images/Button_Kitty_%s.png" action ui.callsinnewcontext("Shift_Focus", "Kitty") focus_mask True
            vbox:
                if "met" in EmmaX.History:
                        imagebutton auto "images/Button_Emma_%s.png" action ui.callsinnewcontext("Shift_Focus", EmmaX) focus_mask True
                if "met" in LauraX.History:
                        imagebutton auto "images/Button_Laura_%s.png" action ui.callsinnewcontext("Shift_Focus", LauraX) focus_mask True
            vbox:
                if "met" in JeanX.History:
                        imagebutton auto "images/Button_Jean_%s.png" action ui.callsinnewcontext("Shift_Focus", JeanX) focus_mask True
                if "met" in StormX.History:
                        imagebutton auto "images/Button_Storm_%s.png" action ui.callsinnewcontext("Shift_Focus", StormX) focus_mask True
            vbox:
                if "met" in JubesX.History:
                        imagebutton auto "images/Button_Jubes_%s.png" action ui.callsinnewcontext("Shift_Focus", JubesX) focus_mask True

transform rotate_white(x):
    rotate -(int(x *3.6))

transform rotate_red(x):
    rotate -(int(x *3.6-180))

#end wardrobe



screen Inventory_screen: #rkeljsv
    frame:
        xminimum 200
        xpos 700
        ypos 75
        has vbox

#        hbox:
        text "Inventory:" size 20
        showif "dildo" in Player.Inventory:
                $ Inventory_Count = Player.Inventory.count("dildo")
                text "Dildos: [Inventory_Count]" size 15
        showif "vibrator" in Player.Inventory:
                $ Inventory_Count = Player.Inventory.count("vibrator")
                text "Vibrators: [Inventory_Count]" size 15
        showif "Dazzler and Longshot" in Player.Inventory:
                $ Inventory_Count = Player.Inventory.count("Dazzler and Longshot")
                text "Dazzler and Longshot: [Inventory_Count]" size 15
        showif "256 Shades of Grey" in Player.Inventory:
                $ Inventory_Count = Player.Inventory.count("256 Shades of Grey")
                text "256 Shades of Grey: [Inventory_Count]" size 15
        showif "Avengers Tower Penthouse" in Player.Inventory:
                $ Inventory_Count = Player.Inventory.count("Avengers Tower Penthouse")
                text "Avengers Tower Penthouse: [Inventory_Count]" size 15
        showif "Xavier's photo" in Player.Inventory:
                text "Xavier's Photo" size 15
        showif "Xavier's files" in Player.Inventory:
                text "Xavier's Files" size 15
        #Rogue
        showif "Rogue nighty" in Player.Inventory:
                text "Rogue's Green Nighty" size 15
        showif "Rogue lace bra" in Player.Inventory:
                text "Rogue's Lace Bra" size 15
        showif "Rogue lace panties" in Player.Inventory:
                text "Rogue's Lace Panties" size 15
        showif "Rogue bikini top" in Player.Inventory:
                text "Rogue's Bikini Top" size 15
        showif "Rogue bikini bottoms" in Player.Inventory:
                text "Rogue's Bikini Bottoms" size 15
        #Kitty
        showif "Kitty lace bra" in Player.Inventory:
                text "Kitty's Lace Bra" size 15
        showif "Kitty lace panties" in Player.Inventory:
                text "Kitty's Lace Panties" size 15
        showif "Kitty knee stockings" in Player.Inventory:
                text "Kitty's knee stockings" size 15
        showif "Kitty pantyhose" in Player.Inventory:
                text "Kitty's Pantyhose" size 15
        showif "Kitty bikini top" in Player.Inventory:
                text "Kitty's Bikini Top" size 15
        showif "Kitty bikini bottoms" in Player.Inventory:
                text "Kitty's Bikini Bottoms" size 15
        showif "Kitty blue skirt" in Player.Inventory:
                text "Kitty's Blue Skirt" size 15
        #Emma
        showif "Emma lace bra" in Player.Inventory:
                text "Emma's Lace Bra" size 15
        showif "Emma lace panties" in Player.Inventory:
                text "Emma's Lace Panties" size 15
        showif "Emma pantyhose" in Player.Inventory:
                text "Emma's Pantyhose" size 15
        showif "Emma bikini top" in Player.Inventory:
                text "Emma's Bikini Top" size 15
        showif "Emma bikini bottoms" in Player.Inventory:
                text "Emma's Bikini Bottoms" size 15
        #Laura
        showif "Laura corset" in Player.Inventory:
                text "Laura's Red Corset" size 15
        showif "Laura lace corset" in Player.Inventory:
                text "Laura's Lace Corset" size 15
        showif "Laura lace panties" in Player.Inventory:
                text "Laura's Lace Panties" size 15
        showif "Laura bikini top" in Player.Inventory:
                text "Laura's Bikini Top" size 15
        showif "Laura bikini bottoms" in Player.Inventory:
                text "Laura's Bikini Bottoms" size 15
        #Jean
        showif "Jean corset" in Player.Inventory:
                text "Jean's Black Corset" size 15
        showif "Jean lace corset" in Player.Inventory:
                text "Jean's Lace Corset" size 15
        showif "Jean lace bra" in Player.Inventory:
                text "Jean's Lace Bra" size 15
        showif "Jean lace panties" in Player.Inventory:
                text "Jean's Lace Panties" size 15
        showif "Jean bikini top" in Player.Inventory:
                text "Jean's Bikini Top" size 15
        showif "Jean bikini bottoms" in Player.Inventory:
                text "Jean's Bikini Bottoms" size 15
        #Storm
        showif "Storm lace bra" in Player.Inventory:
                text "Storm's Lace Bra" size 15
        showif "Storm lace panties" in Player.Inventory:
                text "Storm's Lace Panties" size 15
        showif "Storm pantyhose" in Player.Inventory:
                text "Storm's Pantyhose" size 15
        showif "Storm bikini top" in Player.Inventory:
                text "Storm's Bikini Top" size 15
        showif "Storm bikini bottoms" in Player.Inventory:
                text "Storm's Bikini Bottoms" size 15
        showif "stockings and garterbelt" in Player.Inventory:
                text "stockings and garterbelt" size 15
        #Jubes
        showif "Jubes lace bra" in Player.Inventory:
                text "Jubilees's Lace Bra" size 15
        showif "Jubes lace panties" in Player.Inventory:
                text "Jubilees's Lace Panties" size 15
        showif "Jubes bikini top" in Player.Inventory:
                text "Jubilees's Bikini Top" size 15
        showif "Jubes bikini bottoms" in Player.Inventory:
                text "Jubilees's Bikini Bottoms" size 15
        showif "socks" in Player.Inventory:
                text "Jubilees's Tall Socks" size 15

        #rkeljsv
        #colognes
        showif "Mandrill Cologne" in Player.Inventory:
                $ Inventory_Count = Player.Inventory.count("Mandrill Cologne")
                textbutton "Mandrill Cologne: [Inventory_Count] doses" action ui.callsinnewcontext("MandrillScreen") text_size 15
        showif "Purple Rain Cologne" in Player.Inventory:
                $ Inventory_Count = Player.Inventory.count("Purple Rain Cologne")
                textbutton "Purple Rain Cologne: [Inventory_Count] doses" action ui.callsinnewcontext("PurpleRainScreen") text_size 15
        showif "Corruption Cologne" in Player.Inventory:
                $ Inventory_Count = Player.Inventory.count("Corruption Cologne")
                textbutton "Corruption Cologne: [Inventory_Count] doses" action ui.callsinnewcontext("CorruptionScreen") text_size 15
        showif "Xavier" in Keys:
                text "Xavier's Key" size 15
        showif RogueX in Keys:
                text "Rogue's Key" size 15
        showif KittyX in Keys:
                text "Kitty's Key" size 15
        showif EmmaX in Keys:
                text "Emma's Key" size 15
        showif LauraX in Keys:
                text "Laura's Key" size 15
        showif JeanX in Keys:
                text "Jean's Key" size 15
        showif StormX in Keys:
                text "Storm's Key" size 15
        showif JubesX in Keys:
                text "Jubes's Key" size 15
        #rkeljsv


    imagebutton:
        auto "images/UI_Backpack_%s.png"
        action Hide("Inventory_screen")
        xpos 780
        ypos 5
        focus_mask True


label MandrillScreen:
    if "mandrill" in Player.Traits:
            "You already have this on."
            return
    if "purple" in Player.Traits or "corruption" in Player.Traits:
            "You'll confuse the scent you already have on."
            return
#    $ Inventory_Count = Inventory_Check("Mandrill Cologne")
    $ Inventory_Count = Player.Inventory.count("Mandrill Cologne")
    "This cologne is guaranteed to make women love you more [[+Love]. You have [Inventory_Count] doses left."
    "Product warning, any love gained while under the effects may be lost when this wears off, if the limits are reached."
    menu:
        "Use it now?"
        "Yes":
            $ Player.Traits.append("mandrill")
            $ Player.Inventory.remove("Mandrill Cologne")
        "No":
            pass

    return

label PurpleRainScreen:
    if "purple" in Player.Traits:
        "You already have this on."
        return
    if "mandrill" in Player.Traits or "corruption" in Player.Traits:
        "You'll confuse the scent you already have on."
        return
#    $ Inventory_Count = Inventory_Check("Purple Rain Cologne")
    $ Inventory_Count = Player.Inventory.count("Purple Rain Cologne")
    "This cologne is guaranteed to make women more suggestible to your orders until tomorrow [[+Obedience]. You have [Inventory_Count] doses left."
    "Product warning, any obedience gained whie under the effects may be lost when this wears off, if the limits are reached."
    menu:
        "Use it now?"
        "Yes":
            $ Player.Traits.append("purple")
            $ Player.Inventory.remove("Purple Rain Cologne")
        "No":
            pass
    return

label CorruptionScreen:
    if "corruption" in Player.Traits:
        "You already have this on."
        return
    if "purple" in Player.Traits or "mandrill" in Player.Traits:
        "You'll confuse the scent you already have on."
        return
#    $ Inventory_Count = Inventory_Check("Corruption Cologne")
    $ Inventory_Count = Player.Inventory.count("Corruption Cologne")
    "This cologne is guaranteed to make women let loose their wild side [[-Inhibition]. You have [Inventory_Count] doses left."
    "Product warning, any Inhibition lost whie under the effects may be regained when this wears off, if the limits are reached."
    menu:
        "Use it now?"
        "Yes":
            $ Player.Traits.append("corruption")
            $ Player.Inventory.remove("Corruption Cologne")
        "No":
            pass
    return
#Begin Disclaimer screen:

screen Disclaimer_screen:
    window:
        style "gm_root"
    frame:
        xalign .5
        ypos 100
        xmaximum 800
        has vbox
        text "This is a work of parody fiction. It is intended to be distributed through Oniartist's Patreon page, please do not redistribute through other sources."
        text " "
        text "As is noted in the game, this story takes place several years after the last episode of the TV series it is based on, and all characters involved are over the age of 18.The game references events of the TV series, but is not beholden to the canon of the series, and characters will behave differently or have different backstories."
        text " "
        text "I would like to thank Akabur for his help getting started with all this (definitely check out his games too), and the various documentation on the Renpy site for pointing me in the right directions. I've had a lot of fun coding this game, and look forward to continually improving on it. If you'd like to support my efforts, please sign up under my name at Hentai United, or join on to my Patreon page. I have some huge ambitions for where this project will end up."
        text " "
        text "{a=http://www.patreon.com/OniArtist}http://www.patreon.com/OniArtist{/a}"

    frame:
        xalign 0.5
        yalign 0.95
        has hbox
        #textbutton "Return" action Return()
        textbutton "Return" action Hide("Disclaimer_screen")

#label Disclaimer_screen_label:
#    call screen Disclaimer_screen
#    return
#end Disclaimer
