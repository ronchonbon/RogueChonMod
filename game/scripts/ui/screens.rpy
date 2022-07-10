init -3:

    style choice_menu is default

    style choice_menu_window is window:
        background None

    style choice_menu_text is button_text clear:
        size 24

    style choice_menu_button is button:
        xminimum int(config.screen_width*0.25)
        xmaximum int(config.screen_width*0.25)

    style mm_button:
        size_group "mm"

    style gm_nav_button:
        size_group "gm_nav"

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

screen say(who, what, two_window = False):
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
    style_prefix "choice_menu"

    window:
        anchor (0.5, 0.0) pos (0.15, 0.35)

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
                                background "#424242"
                                action None
                                text caption:
                                    color "#6E6E6E"
                        else:
                            button:
                                action action
                                text caption
                    else:
                        text caption

screen nvl(dialogue, items = None):
    use texting(dialogue, items)

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

        vbox:
            frame:
                style_group "pref"
                has vbox
                label _("There is no audio")

screen confirm(message, yes_action, no_action):
    modal True

    window:
        style "gm_root"

    frame:
        style_prefix "confirm"

        xfill True
        xmargin 50
        ypadding 25
        yalign 0.25

        vbox:
            xfill True
            spacing 25

            text _(message):
                text_align 0.5
                xalign 0.5

            hbox:
                spacing 100
                xalign 0.5
                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

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
