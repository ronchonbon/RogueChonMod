init -2:

    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text clear:
        size 24

    style menu_choice_button is button:
        xminimum int(config.screen_width*0.25)
        xmaximum int(config.screen_width*0.25)

    style mm_button:
        size_group "mm"

    style gm_nav_button:
        size_group "gm_nav"

    style file_picker_

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

    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"

    style quick_button is default:
        background None
        xpadding 5

    style quick_button_text is default:
        size 20
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

transform rotate_white(x):
    rotate -int(3.6*x)

transform rotate_red(x):
    rotate -int(3.6*x - 180)

transform tiny_button:
    zoom 0.5

screen say(who, what, two_window = False):
    if not two_window:
        window:
            anchor (0.5, 0.0) pos (0.15, 0.18)

            style "textbox"
            id "textbox"

            has vbox:
                style "say_vbox"

            if who:
                text who:
                    size 20
                    id "who"
                    font "CRIMFBRG.ttf"

            text what:
                size 20
                id "what"
                color "#000000"
                font "CRIMFBRG.ttf"
                text_align 0.5
    else:
        vbox:
            anchor (0.5, 0.0) pos (0.15, 0.18)

            style "say_two_window_vbox"

            window:
                anchor (0.5, 0.0) pos (0.5, 0.0)

                style "say_balloon"

                text what:
                    size 20
                    id "what"
                    color "#000000"
                    font "CRIMFBRG.ttf"
                    text_align 0.5

        if who:
            window:
                anchor (0.5, 0.0) pos (0.15, 0.13)

                style "say_who_window"

                text who:
                    size 20
                    id "who"
                    font "CRIMFBRG.ttf"

    use quick_menu

screen choice(items):
    window:
        anchor (0.5, 0.0) pos (0.15, 0.35)

        style "menu_window"

        fixed anchor (0.5, 0.0) pos (0.5, 0.0) xysize (480, 500):
            viewport:
                mousewheel True
                draggable True

                side_yfill True

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
                                text caption:
                                    style "menu_choice"
                                    color "#6E6E6E"
                        else:
                            button:
                                action action
                                style "menu_choice_button"
                                text caption:
                                    style "menu_choice"
                    else:
                        text caption:
                            style "menu_caption"

screen input(prompt):
    window:
        anchor (0.5, 1.0) pos (0.5, 0.9)

        style "input_window"

        has vbox

        text prompt:
            size 20
            style "input_prompt"
            color "#000000"

        input:
            size 25
            id "input"
            style "input_text"
            color "#6E6E6E"

    use quick_menu

screen main_menu():
    tag menu

    window:
        style "mm_root"

    frame:
        style_group "mm"
        align (0.98, 0.98)

        has vbox

        textbutton _("Start Game") action Start()
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Quit") action Quit(confirm = False)

screen navigation():
    window:
        style "gm_root"

    frame:
        style_group "gm_nav"
        align (0.98, 0.98)

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Quit") action Quit()

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
                textbutton _("all") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
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
                    textbutton _("Wait for Voice") action Preference("Wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox
                label _("There is no Audio")

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

screen inventory_button:
    imagebutton:
        auto "images/UI_Backpack_%s.png"
        action Show("Inventory_screen")
        pos (0.81, 0.015)
        focus_mask True

image Alt_Screen_Mask:
    contains:
        Solid("#159457", xysize = (800, 150))
        alpha .5
        pos (0.0, 0.0)

screen status_screen:
    default tt = Tooltip(" ")

    if Partner in all_Girls:
        frame:
            background None
            pos (0.0, 0.3)

            add AlphaMask("images/BarBackdrop_" + Partner.tag + ".png", "Alt_Screen_Mask")

            frame:
                style_group "stat_bar"
                pos (0.0, 0.2)
                background None
                has vbox

                hbox:
                    imagebutton idle "images/iconlust.png" hover "images/iconlust.png" action NullAction() hovered tt.Action("Lust: [Partner.lust]")
                    bar range 100 value Partner.lust xmaximum 200 ymaximum 40 left_bar "images/barfull.png" right_bar "images/barempty.png"

                    imagebutton idle "images/iconlove.png" hover "images/iconlove.png" action NullAction() hovered tt.Action("Love: [Partner.love]")
                    bar range 100 value (Partner.love/10) xmaximum 200 ymaximum 40 left_bar "images/barfull.png" right_bar "images/barempty.png"

                    imagebutton idle "images/iconobed.png" hover "images/iconobed.png" action NullAction() hovered tt.Action("Obedience: [Partner.obedience]")
                    bar range 100 value (Partner.obedience/10) xmaximum 200 ymaximum 40 left_bar "images/barfullO.png" right_bar "images/barempty.png"

                    imagebutton idle "images/iconinbt.png" hover "images/iconinbt.png" action NullAction() hovered tt.Action("Inhibitions: [Partner.inhibition]")
                    bar range 100 value (Partner.inhibition/10) xmaximum 200 ymaximum 40 left_bar "images/barfulli.png" right_bar "images/barempty.png"

    add "images/BarBackdrop_" + focused_Girl.tag + ".png"
    frame:
        style_group "stat_bar"
        pos (0.0, 0.0)
        background None
        has vbox

        hbox:
            imagebutton idle "images/iconlove.png" hover "images/iconlove.png" action NullAction() hovered tt.Action("Love: [focused_Girl.love]")
            bar range 100 value (focused_Girl.love/10) xmaximum 200 ymaximum 40 left_bar "images/barfull.png" right_bar "images/barempty.png"

        hbox:
            imagebutton idle "images/iconlust.png" hover "images/iconlust.png" action NullAction() hovered tt.Action("Lust: [focused_Girl.lust]")
            bar range 100 value focused_Girl.lust xmaximum 200 ymaximum 40 left_bar "images/barfull.png" right_bar "images/barempty.png"

    frame:
        pos (0.15, 0.0)
        background None
        has vbox

        hbox:
            imagebutton idle "images/iconobed.png" hover "images/iconobed.png" action NullAction() hovered tt.Action("Obedience: [focused_Girl.obedience]")
            bar range 100 value (focused_Girl.obedience/10) xmaximum 200 ymaximum 40 left_bar "images/barfullO.png" right_bar "images/barempty.png"

        hbox:
            imagebutton idle "images/iconaddict.png" hover "images/iconaddict.png" action NullAction() hovered tt.Action("Addiction: [focused_Girl.addiction]")
            bar range 100 value focused_Girl.addiction xmaximum 200 ymaximum 40 left_bar "images/barfull.png" right_bar "images/barempty.png"

    frame:
        pos (0.3, 0.0)
        background None
        has vbox

        hbox:
            imagebutton idle "images/iconinbt.png" hover "images/iconinbt.png" action NullAction() hovered tt.Action("Inhibitions: [focused_Girl.inhibition]")
            bar range 100 value (focused_Girl.inhibition/10) xmaximum 200 ymaximum 40 left_bar "images/barfulli.png" right_bar "images/barempty.png"

        hbox:
            imagebutton idle "images/iconaddictrate.png" hover "images/iconaddictrate.png" action NullAction() hovered tt.Action("Addiction Rate: [focused_Girl.addiction_rate]")
            bar range 100 value (focused_Girl.addiction_rate*10) xmaximum 200 ymaximum 40 left_bar "images/barfull.png" right_bar "images/barempty.png"

    showif not Player.primary_action:
        imagebutton auto "images/Button_" + focused_Girl.tag + "_%s.png" action ShowTransient("Focus_Map") pos (0.71, 0.016) focus_mask True

    showif config.developer:
        imagebutton auto "images/Button_" + focused_Girl.tag + "_%s.png" action ui.callsinnewcontext("cheat_editor",focused_Girl) pos (0.755, 0.016) focus

    frame:
        pos (0.45, 0.0085)
        background None
        has vbox

        hbox:
            bar range 100 value Player.focus xmaximum 200 ymaximum 40 left_bar "images/barfullP.png" right_bar "images/baremptyP.png"

        hbox:
            bar range 100 value (Player.semen*20) xmaximum 200 ymaximum 40 left_bar "images/barfullS.png" right_bar "images/baremptyS.png"

    frame:
        minimum (200, 0) pos (0.58, 0.015)
        background None
        has vbox
        hbox:
            text "Money: $[Player.cash]" size 18
        hbox:
            text "Level: [Player.level]" size 18
        hbox:
            text "[focused_Girl.tag] Level: [focused_Girl.level]" size 18

    frame:
        pos (0.905, 0.047)
        background None

        add "images/Clockbase.png":
            anchor (0.5, 0.5)
            yzoom -1
            subpixel True

        if round < 50:
            add "images/Clockred.png" at rotate_red(round):
                anchor (0.5, 0.5)
                subpixel True
        else:
            add "images/Clockwhite.png" at rotate_white(round):
                anchor (0.5, 0.5)
                subpixel True

        imagebutton idle "images/Clockface.png" hover "images/Clockface.png" action NullAction() hovered tt.Action("Time Left: [round]%") anchor (0.5, 0.5)

    frame:
        minimum (200, 0) pos (0.93, 0.018)
        background None
        has vbox
        hbox:
            text "Day: [day] [day_of_week]" size 18
        hbox:
            text "Time: [current_time]" size 16
        hbox:
            text "Stack depth: [stack_depth]" size 14

    frame:
        pos (0.905, 0.1)
        background None
        has vbox
        hbox:
            if RogueX in Nearby:
                imagebutton auto "images/Button_Rogue_%s.png" action NullAction() hovered tt.Action(RogueX.name) at tiny_button
            if KittyX in Nearby:
                imagebutton auto "images/Button_Kitty_%s.png" action NullAction() hovered tt.Action(KittyX.name) at tiny_button
            if EmmaX in Nearby:
                imagebutton auto "images/Button_Emma_%s.png" action NullAction() hovered tt.Action(EmmaX.name) at tiny_button
            if LauraX in Nearby:
                imagebutton auto "images/Button_Laura_%s.png" action NullAction() hovered tt.Action(LauraX.name) at tiny_button
            if JeanX in Nearby:
                imagebutton auto "images/Button_Jean_%s.png" action NullAction() hovered tt.Action(JeanX.name) at tiny_button
            if StormX in Nearby:
                imagebutton auto "images/Button_Storm_%s.png" action NullAction() hovered tt.Action(StormX.name) at tiny_button
            if JubesX in Nearby:
                imagebutton auto "images/Button_Jubes_%s.png" action NullAction() hovered tt.Action(JubesX.name) at tiny_button

    if tt.value != " ":
        frame:
            pos (0.9, 0.12)
            has vbox
            text tt.value

screen Focus_Map:
    imagebutton auto "images/Button_X_%s.png" action Hide("Focus_Map") pos (0.71, 0.016) focus_mask True

    frame:
        pos (0.71, 0.09)
        has hbox

        vbox:
            imagebutton auto "images/Button_Rogue_%s.png" action ui.callsinnewcontext("shift_focus", RogueX) focus_mask True

            if KittyX in active_Girls:
                imagebutton auto "images/Button_Kitty_%s.png" action ui.callsinnewcontext("shift_focus", KittyX) focus_mask True

        vbox:
            if EmmaX in active_Girls:
                imagebutton auto "images/Button_Emma_%s.png" action ui.callsinnewcontext("shift_focus", EmmaX) focus_mask True

            if LauraX in active_Girls:
                imagebutton auto "images/Button_Laura_%s.png" action ui.callsinnewcontext("shift_focus", LauraX) focus_mask True

        vbox:
            if JeanX in active_Girls:
                imagebutton auto "images/Button_Jean_%s.png" action ui.callsinnewcontext("shift_focus", JeanX) focus_mask True

            if StormX in active_Girls:
                imagebutton auto "images/Button_Storm_%s.png" action ui.callsinnewcontext("shift_focus", StormX) focus_mask True

        vbox:
            if JubesX in active_Girls:
                imagebutton auto "images/Button_Jubes_%s.png" action ui.callsinnewcontext("shift_focus", JubesX) focus_mask True

screen Inventory_screen:
    frame:
        minimum (300, 0) pos (0.83, 0.125)
        has vbox

        text "Inventory:" size 20
        showif "Xavier's photo" in Player.inventory:
            text "Xavier's Photo" size 15
        showif "Xavier's files" in Player.inventory:
            text "Xavier's Files" size 15

        showif "_dildo" in Player.inventory:
            $ inventory_count = Player.inventory.count("_dildo")
            text "Dildos: [inventory_count]" size 15
        showif "_vibrator" in Player.inventory:
            $ inventory_count = Player.inventory.count("_vibrator")
            text "Vibrators: [inventory_count]" size 15

        showif "Dazzler and Longshot" in Player.inventory:
            $ inventory_count = Player.inventory.count("Dazzler and Longshot")
            text "Dazzler and Longshot: [inventory_count]" size 15
        showif "256 Shades of Grey" in Player.inventory:
            $ inventory_count = Player.inventory.count("256 Shades of Grey")
            text "256 Shades of Grey: [inventory_count]" size 15
        showif "Avengers Tower Penthouse" in Player.inventory:
            $ inventory_count = Player.inventory.count("Avengers Tower Penthouse")
            text "Avengers Tower Penthouse: [inventory_count]" size 15

        showif "Mandrill Cologne" in Player.inventory:
            $ inventory_count = Player.inventory.count("Mandrill Cologne")

            textbutton "Mandrill Cologne: [inventory_count] doses" action ui.callsinnewcontext("mandrill_screen") text_size 15
        showif "Purple Rain Cologne" in Player.inventory:
            $ inventory_count = Player.inventory.count("Purple Rain Cologne")

            textbutton "Purple Rain Cologne: [inventory_count] doses" action ui.callsinnewcontext("purplerain_screen") text_size 15
        showif "Corruption Cologne" in Player.inventory:
            $ inventory_count = Player.inventory.count("Corruption Cologne")

            textbutton "Corruption Cologne: [inventory_count] doses" action ui.callsinnewcontext("corruption_screen") text_size 15

        showif "Xavier" in Player.Keys:
            text "Xavier's Key" size 15
        showif RogueX in Player.Keys:
            text "Rogue's Key" size 15
        showif KittyX in Player.Keys:
            text "Kitty's Key" size 15
        showif EmmaX in Player.Keys:
            text "Emma's Key" size 15
        showif LauraX in Player.Keys:
            text "Laura's Key" size 15
        showif JeanX in Player.Keys:
            text "Jean's Key" size 15
        showif StormX in Player.Keys:
            text "Storm's Key" size 15
        showif JubesX in Player.Keys:
            text "Jubes's Key" size 15

    imagebutton:
        auto "images/UI_Backpack_%s.png"
        action Hide("Inventory_screen")
        pos (0.81, 0.015)
        focus_mask True

label mandrill_screen:
    if "mandrill" in Player.traits:
        "You already have this on."

        return

    if "purple" in Player.traits or "corruption" in Player.traits:
        "You'll confuse the scent you already have on."

        return

    $ inventory_count = Player.inventory.count("Mandrill Cologne")

    "This cologne is guaranteed to make women love you more [[+Love]. You have [inventory_count] doses left."
    "Product warning, any love gained while under the effects may be lost when this wears off, if the limits are reached."

    menu:
        "Use it now?"
        "Yes":
            $ Player.traits.append("mandrill")
            $ Player.inventory.remove("Mandrill Cologne")
        "No":
            pass

    return

label purplerain_screen:
    if "purple" in Player.traits:
        "You already have this on."
        return

    if "mandrill" in Player.traits or "corruption" in Player.traits:
        "You'll confuse the scent you already have on."
        return

    $ inventory_count = Player.inventory.count("Purple Rain Cologne")

    "This cologne is guaranteed to make women more suggestible to your orders until tomorrow [[+Obedience]. You have [inventory_count] doses left."
    "Product warning, any obedience gained whie under the effects may be lost when this wears off, if the limits are reached."

    menu:
        "Use it now?"
        "Yes":
            $ Player.traits.append("purple")
            $ Player.inventory.remove("Purple Rain Cologne")
        "No":
            pass

    return

label corruption_screen:
    if "corruption" in Player.traits:
        "You already have this on."

        return

    if "purple" in Player.traits or "mandrill" in Player.traits:
        "You'll confuse the scent you already have on."

        return

    $ inventory_count = Player.inventory.count("Corruption cologne")

    "This cologne is guaranteed to make women let loose their wild side [[-Inhibition]. You have [inventory_count] doses left."
    "Product warning, any Inhibition lost whie under the effects may be regained when this wears off, if the limits are reached."

    menu:
        "Use it now?"
        "Yes":
            $ Player.traits.append("corruption")
            $ Player.inventory.remove("Corruption cologne")
        "No":
            pass

    return
