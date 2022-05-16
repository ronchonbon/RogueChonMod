












screen say(who, what, side_image=None, two_window=False, CountWords=0):



    if who == "N":
        $ who = focused_Girl.name

    if not two_window:

        window:



            pos (0.0,0.1)
            anchor (0.0,0.0)

            style "textbox"

            id "textbox"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what" color "#000000" font "CRIMFBRG.ttf"

    else:


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


        vbox:

            pos (0.0,0.1)
            anchor (0.0,0.0)

            style "say_two_window_vbox"

            window:
                if who == Gwenname:
                    style "say_balloon" background Frame("images/WordballoonG.png", 50, 50)
                else:
                    style "say_balloon"




                text what id "what" color "#000000" font "CRIMFBRG.ttf" text_align 0.5

            if who == RogueX.name:
                if RogueX.location != bg_current or RogueX.sprite_location == stage_far_left:
                    add "arrow" xalign 0.1
                elif RogueX.sprite_location == stage_right or RogueX.sprite_location == stage_far_right:
                    add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                else:
                    add "arrow" xalign 0.8
            elif who == KittyX.name:
                if KittyX.location != bg_current or KittyX.sprite_location == stage_far_left:
                    add "arrow" xalign 0.1
                elif KittyX.sprite_location == stage_right or KittyX.sprite_location == stage_far_right:
                    add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                else:
                    add "arrow" xalign 0.8
            elif who == EmmaX.name:
                if EmmaX.location != bg_current or EmmaX.sprite_location == stage_far_left:
                    add "arrow" xalign 0.1
                elif EmmaX.sprite_location == stage_right or EmmaX.sprite_location == stage_far_right:
                    add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                else:
                    add "arrow" xalign 0.8
            elif who == LauraX.name:
                if LauraX.location != bg_current or LauraX.sprite_location == stage_far_left:
                    add "arrow" xalign 0.1
                elif LauraX.sprite_location == stage_right or LauraX.sprite_location == stage_far_right:
                    add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                else:
                    add "arrow" xalign 0.8
            elif who == JeanX.name:
                if JeanX.location != bg_current or JeanX.sprite_location == stage_far_left:
                    add "arrow" xalign 0.1
                elif JeanX.sprite_location == stage_right or JeanX.sprite_location == stage_far_right:
                    add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                else:
                    add "arrow" xalign 0.8
            elif who == StormX.name:
                if StormX.location != bg_current or StormX.sprite_location == stage_far_left:
                    add "arrow" xalign 0.1
                elif StormX.sprite_location == stage_right or StormX.sprite_location == stage_far_right:
                    add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                else:
                    add "arrow" xalign 0.8
            elif who == JubesX.name:
                if JubesX.location != bg_current or JubesX.sprite_location == stage_far_left:
                    add "arrow" xalign 0.1
                elif JubesX.sprite_location == stage_right or JubesX.sprite_location == stage_far_right:
                    add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                else:
                    add "arrow" xalign 0.8
            elif who == Gwenname:
                add "arrowG" xalign 0.15
            elif who == Player.name or who == "Danger Room":
                pass
            elif who == "Professor X":
                add "arrow" xalign 0.8
            elif who:
                add "arrow" xalign 0.8

        if who:

            window:
                pos (0.1,0.07)
                anchor (0.5,0)
                style "say_who_window"


                text who:
                    size 15
                    id "who"
                    font "CRIMFBRG.ttf"


    use quick_menu


image side arrow = "arrow"

image arrow:
    "images/Arrow.png"
    ypos -17
    xalign 0.5
    zoom 1
    rotate 0

image arrowG:
    "images/ArrowG.png"
    ypos -17
    xalign 0.5
    zoom 1
    rotate 0







screen choice(items):

    window:
        style "menu_window"
        xpos 20
        ypos 0.3
        yanchor 0.0

        has vbox:
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



                else:
                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

            else:
                text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True
    style menu_window is default

    style menu_choice is button_text clear


    style menu_choice_button is button:
        xminimum int(config.screen_width*0.30)
        xmaximum int(config.screen_width*0.30)








screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt" color "#000000" size 20
        input id "input" style "input_text" color "#6E6E6E" size 25

    use quick_menu







screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"


        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id


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







screen main_menu():
    tag menu




    window:
        style "mm_root"

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


    style mm_button:
        size_group "mm"









screen navigation():


    window:
        style "gm_root"


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


    style gm_nav_button:
        size_group "gm_nav"













screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox



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


        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"


            for i in range(1, columns*rows + 1):


                button:
                    action FileAction(i)
                    xfill True

                    has hbox


                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns*rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():
    tag menu



    use navigation
    use file_picker

screen load():
    tag menu



    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text








screen preferences():
    tag menu



    use navigation


    grid 3 1:
        style_group "prefs"
        xfill True


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

                label _("Text action_speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick..") action Preference("joystick")


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


    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"






screen quick_menu():


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
    style quick_button is default:

        background None
        xpadding 5

    style quick_button_text is default:

        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"









screen roguebutton:
    imagebutton:
        auto "images/Button_Rogue_%s.png"
        action ui.callsinnewcontext("RogueWardrobe")
        xpos 690
        ypos 5
        focus_mask True




screen statbutton:

    imagebutton:
        auto "images/Button_Rogue_%s.png"
        action ui.calls("RogueStats")
        xpos 730
        ypos 5
        focus_mask True




screen Inventorybutton:
    imagebutton:
        auto "images/UI_Backpack_%s.png"
        action Show("Inventory_screen")
        xpos 780
        ypos 5
        focus_mask True





image Alt_Screen_Mask:

    contains:
        Solid("#159457", xysize=(800,150))
        alpha .5
        pos (0,-20)

screen Status_Screen:

    default tt = Tooltip(" ")


    if Partner in all_Girls:
        frame:
            background None
            pos (-100,30)

            add AlphaMask("images/BarBackdrop_"+Partner.Tag+".png", "Alt_Screen_Mask")
            frame:
                style_group "stat_bar"
                pos (100,25)
                background None
                has vbox
                hbox:
                    imagebutton idle "images/iconlust.png" hover "images/iconlust.png" action NullAction() hovered tt.Action("Lust: [Partner.lust]")
                    bar range 100 value Partner.lust xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0

                    imagebutton idle "images/iconlove.png" hover "images/iconlove.png" action NullAction() hovered tt.Action("Love: [Partner.love]")
                    bar range 100 value (Partner.love/10) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0

                    imagebutton idle "images/iconobed.png" hover "images/iconobed.png" action NullAction() hovered tt.Action("Obedience: [Partner.obedience]")
                    bar range 100 value (Partner.obedience/10) xmaximum 100 left_bar "images/barfullO.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0

                    imagebutton idle "images/iconinbt.png" hover "images/iconinbt.png" action NullAction() hovered tt.Action("Inhibitions: [Partner.inhibition]")
                    bar range 100 value (Partner.inhibition/10) xmaximum 100 left_bar "images/barfulli.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0






    if focused_Girl in all_Girls:
        add "images/BarBackdrop_"+focused_Girl.Tag+".png"
        frame:
            style_group "stat_bar"
            xminimum 130
            background None
            has vbox
            hbox:
                imagebutton idle "images/iconlove.png" hover "images/iconlove.png" action NullAction() hovered tt.Action("Love: [focused_Girl.love]")
                bar range 100 value (focused_Girl.love/10) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
            hbox:
                imagebutton idle "images/iconlust.png" hover "images/iconlust.png" action NullAction() hovered tt.Action("Lust: [focused_Girl.lust]")
                bar range 100 value focused_Girl.lust xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
        frame:
            xminimum 130
            xpos 130
            background None
            has vbox
            hbox:
                imagebutton idle "images/iconobed.png" hover "images/iconobed.png" action NullAction() hovered tt.Action("Obedience: [focused_Girl.obedience]")
                bar range 100 value (focused_Girl.obedience/10) xmaximum 100 left_bar "images/barfullO.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
            hbox:
                imagebutton idle "images/iconaddict.png" hover "images/iconaddict.png" action NullAction() hovered tt.Action("Addiction: [focused_Girl.addiction]")
                bar range 100 value focused_Girl.addiction xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 6 thumb None thumb_offset 0
        frame:
            xminimum 130
            xpos 260
            background None
            has vbox
            hbox:
                imagebutton idle "images/iconinbt.png" hover "images/iconinbt.png" action NullAction() hovered tt.Action("Inhibitions: [focused_Girl.inhibition]")
                bar range 100 value (focused_Girl.inhibition/10) xmaximum 100 left_bar "images/barfulli.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
            hbox:
                imagebutton idle "images/iconaddictrate.png" hover "images/iconaddictrate.png" action NullAction() hovered tt.Action("Addiction Rate: [focused_Girl.addiction_rate]")
                bar range 100 value (focused_Girl.addiction_rate*10) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
        showif not primary_action:

            imagebutton auto "images/Button_"+focused_Girl.Tag+"_%s.png" action ShowTransient("Focus_Map") xpos 690 ypos 5 focus_mask True
        showif config.developer:
            imagebutton auto "images/Button_"+focused_Girl.Tag+"_%s.png" action ui.callsinnewcontext("StatHacks",focused_Girl) xpos 730 ypos 5 focus



    frame:

        xminimum 130
        xpos 390
        background None
        has vbox
        hbox:
            bar range 100 value Player.focus xmaximum 100 left_bar "images/barfullP.png" right_bar "images/baremptyP.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
        hbox:
            bar range 100 value (Player.semen*20) xmaximum 100 left_bar "images/barfullS.png" right_bar "images/baremptyS.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
        imagebutton auto "images/Button_Emma_%s.png" action ui.callsinnewcontext("StatHacks",EmmaX) xpos 730 ypos 5 focus

    frame:

        xminimum 75
        xpos 500
        background None
        has vbox
        hbox:
            text "Money: $[Player.Cash]" size 12
        hbox:
            text "Level: [Player.Lvl]" size 12
        hbox:
            text "[focused_Girl.Tag] Level: [focused_Girl.Lvl]" size 12

        window:
            pos (90,-40)
            anchor (0,0)
            style "say_who_window"
            text "[focused_Girl.name]" size 12 font "CRIMFBRG.ttf" color "#000000"

    frame:

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



        imagebutton idle "images/Clockface.png" hover "images/Clockface.png" action NullAction() hovered tt.Action("Time Left: [Round]%") anchor (0.5,0.5)

    frame:

        xminimum 130
        xpos 920
        background None
        has vbox
        hbox:
            text "Day: [Day] [DayofWeek]" size 12
        hbox:
            text "Time: [Current_Time]" size 12
    frame:

        xpos 920
        ypos 30
        background None
        has vbox
        hbox:
            if RogueX in Nearby:
                imagebutton auto "images/Button_Rogue_%s.png" action NullAction() hovered tt.Action(RogueX.name) at TinyButtons
            if KittyX in Nearby:
                imagebutton auto "images/Button_Kitty_%s.png" action NullAction() hovered tt.Action(KittyX.name) at TinyButtons
            if EmmaX in Nearby:
                imagebutton auto "images/Button_Emma_%s.png" action NullAction() hovered tt.Action(EmmaX.name) at TinyButtons
            if LauraX in Nearby:
                imagebutton auto "images/Button_Laura_%s.png" action NullAction() hovered tt.Action(LauraX.name) at TinyButtons
            if JeanX in Nearby:
                imagebutton auto "images/Button_Jean_%s.png" action NullAction() hovered tt.Action(JeanX.name) at TinyButtons
            if StormX in Nearby:
                imagebutton auto "images/Button_Storm_%s.png" action NullAction() hovered tt.Action(StormX.name) at TinyButtons
            if JubesX in Nearby:
                imagebutton auto "images/Button_Jubes_%s.png" action NullAction() hovered tt.Action(JubesX.name) at TinyButtons


    if tt.value != " ":

        frame:
            xpos 500 ypos 60
            has vbox
            text tt.value

transform TinyButtons:
    zoom .5

screen Focus_Map:

    imagebutton auto "images/Button_X_%s.png" action Hide("Focus_Map") xpos 690 ypos 5 focus_mask True
    frame:
        xpos 684
        ypos 44
        has hbox
        vbox:
            imagebutton auto "images/Button_Rogue_%s.png" action ui.callsinnewcontext("shift_focus", RogueX) focus_mask True
            if "met" in KittyX.history:
                imagebutton auto "images/Button_Kitty_%s.png" action ui.callsinnewcontext("shift_focus", KittyX) focus_mask True

        vbox:
            if "met" in EmmaX.history:
                imagebutton auto "images/Button_Emma_%s.png" action ui.callsinnewcontext("shift_focus", EmmaX) focus_mask True
            if "met" in LauraX.history:
                imagebutton auto "images/Button_Laura_%s.png" action ui.callsinnewcontext("shift_focus", LauraX) focus_mask True
        vbox:
            if "met" in JeanX.history:
                imagebutton auto "images/Button_Jean_%s.png" action ui.callsinnewcontext("shift_focus", JeanX) focus_mask True
            if "met" in StormX.history:
                imagebutton auto "images/Button_Storm_%s.png" action ui.callsinnewcontext("shift_focus", StormX) focus_mask True
        vbox:
            if "met" in JubesX.history:
                imagebutton auto "images/Button_Jubes_%s.png" action ui.callsinnewcontext("shift_focus", JubesX) focus_mask True

transform rotate_white(x):
    rotate -(int(x *3.6))

transform rotate_red(x):
    rotate -(int(x *3.6-180))





screen Inventory_screen:
    frame:
        xminimum 200
        xpos 700
        ypos 75
        has vbox


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

        showif "Rogue nighty" in Player.Inventory:
            text "Rogue's Green Nighty" size 15
        showif "Rogue lace_bra" in Player.Inventory:
            text "Rogue's Lace Bra" size 15
        showif "Rogue lace_panties" in Player.Inventory:
            text "Rogue's Lace Panties" size 15
        showif "Rogue bikini_top" in Player.Inventory:
            text "Rogue's Bikini Top" size 15
        showif "Rogue bikini_bottoms" in Player.Inventory:
            text "Rogue's Bikini Bottoms" size 15

        showif "Kitty lace_bra" in Player.Inventory:
            text "Kitty's Lace Bra" size 15
        showif "Kitty lace_panties" in Player.Inventory:
            text "Kitty's Lace Panties" size 15
        showif "Kitty knee stockings" in Player.Inventory:
            text "Kitty's knee stockings" size 15
        showif "Kitty_pantyhose" in Player.Inventory:
            text "Kitty's Pantyhose" size 15
        showif "Kitty bikini_top" in Player.Inventory:
            text "Kitty's Bikini Top" size 15
        showif "Kitty bikini_bottoms" in Player.Inventory:
            text "Kitty's Bikini Bottoms" size 15
        showif "Kitty blue_skirt" in Player.Inventory:
            text "Kitty's Blue Skirt" size 15

        showif "Emma lace_bra" in Player.Inventory:
            text "Emma's Lace Bra" size 15
        showif "Emma lace_panties" in Player.Inventory:
            text "Emma's Lace Panties" size 15
        showif "Emma_pantyhose" in Player.Inventory:
            text "Emma's Pantyhose" size 15
        showif "Emma bikini_top" in Player.Inventory:
            text "Emma's Bikini Top" size 15
        showif "Emma bikini_bottoms" in Player.Inventory:
            text "Emma's Bikini Bottoms" size 15

        showif "Laura corset" in Player.Inventory:
            text "Laura's Red Corset" size 15
        showif "Laura lace corset" in Player.Inventory:
            text "Laura's Lace Corset" size 15
        showif "Laura lace_panties" in Player.Inventory:
            text "Laura's Lace Panties" size 15
        showif "Laura bikini_top" in Player.Inventory:
            text "Laura's Bikini Top" size 15
        showif "Laura bikini_bottoms" in Player.Inventory:
            text "Laura's Bikini Bottoms" size 15

        showif "Jean corset" in Player.Inventory:
            text "Jean's Black Corset" size 15
        showif "Jean lace corset" in Player.Inventory:
            text "Jean's Lace Corset" size 15
        showif "Jean lace_bra" in Player.Inventory:
            text "Jean's Lace Bra" size 15
        showif "Jean lace_panties" in Player.Inventory:
            text "Jean's Lace Panties" size 15
        showif "Jean bikini_top" in Player.Inventory:
            text "Jean's Bikini Top" size 15
        showif "Jean bikini_bottoms" in Player.Inventory:
            text "Jean's Bikini Bottoms" size 15

        showif "Storm lace_bra" in Player.Inventory:
            text "Storm's Lace Bra" size 15
        showif "Storm lace_panties" in Player.Inventory:
            text "Storm's Lace Panties" size 15
        showif "Storm_pantyhose" in Player.Inventory:
            text "Storm's Pantyhose" size 15
        showif "Storm bikini_top" in Player.Inventory:
            text "Storm's Bikini Top" size 15
        showif "Storm bikini_bottoms" in Player.Inventory:
            text "Storm's Bikini Bottoms" size 15
        showif "stockings_and_garterbelt" in Player.Inventory:
            text "stockings_and_garterbelt" size 15

        showif "Jubes lace_bra" in Player.Inventory:
            text "Jubilees's Lace Bra" size 15
        showif "Jubes lace_panties" in Player.Inventory:
            text "Jubilees's Lace Panties" size 15
        showif "Jubes bikini_top" in Player.Inventory:
            text "Jubilees's Bikini Top" size 15
        showif "Jubes bikini_bottoms" in Player.Inventory:
            text "Jubilees's Bikini Bottoms" size 15
        showif "socks" in Player.Inventory:
            text "Jubilees's Tall Socks" size 15



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

        textbutton "Return" action Hide("Disclaimer_screen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
