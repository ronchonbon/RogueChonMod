transform rotate_white(x):
    rotate -int(3.6*x)

transform rotate_red(x):
    rotate -int(3.6*x - 180)

transform tiny_button:
    zoom 0.5

screen inventory_button:
    imagebutton:
        auto "images/UI_Backpack_%s.png"
        action Show("Inventory_screen")
        pos (0.81, 0.015)
        focus_mask True
        
screen status_screen:
    default tt = Tooltip(" ")

    add "images/BarBackdrop_" + Player.focused_Girl.tag + ".png"
    frame:
        style_group "stat_bar"
        pos (0.0, 0.0)
        background None
        has vbox

        hbox:
            imagebutton idle "images/iconlove.png" hover "images/iconlove.png" action NullAction() hovered tt.Action("Love: [Player.focused_Girl.love]")
            bar range 100 value (Player.focused_Girl.love/10) xmaximum 200 ymaximum 40 left_bar "images/barfull.png" right_bar "images/barempty.png"

        hbox:
            imagebutton idle "images/iconlust.png" hover "images/iconlust.png" action NullAction() hovered tt.Action("Lust: [Player.focused_Girl.lust]")
            bar range 100 value Player.focused_Girl.lust xmaximum 200 ymaximum 40 left_bar "images/barfull.png" right_bar "images/barempty.png"

    frame:
        pos (0.15, 0.0)
        background None
        has vbox

        hbox:
            imagebutton idle "images/iconobed.png" hover "images/iconobed.png" action NullAction() hovered tt.Action("Obedience: [Player.focused_Girl.obedience]")
            bar range 100 value (Player.focused_Girl.obedience/10) xmaximum 200 ymaximum 40 left_bar "images/barfullO.png" right_bar "images/barempty.png"

        hbox:
            imagebutton idle "images/iconaddict.png" hover "images/iconaddict.png" action NullAction() hovered tt.Action("Addiction: [Player.focused_Girl.addiction]")
            bar range 100 value Player.focused_Girl.addiction xmaximum 200 ymaximum 40 left_bar "images/barfull.png" right_bar "images/barempty.png"

    frame:
        pos (0.3, 0.0)
        background None
        has vbox

        hbox:
            imagebutton idle "images/iconinbt.png" hover "images/iconinbt.png" action NullAction() hovered tt.Action("Inhibitions: [Player.focused_Girl.inhibition]")
            bar range 100 value (Player.focused_Girl.inhibition/10) xmaximum 200 ymaximum 40 left_bar "images/barfulli.png" right_bar "images/barempty.png"

        hbox:
            imagebutton idle "images/iconaddictrate.png" hover "images/iconaddictrate.png" action NullAction() hovered tt.Action("Addiction Rate: [Player.focused_Girl.addiction_rate]")
            bar range 100 value (Player.focused_Girl.addiction_rate*10) xmaximum 200 ymaximum 40 left_bar "images/barfull.png" right_bar "images/barempty.png"

    showif not Player.primary_Action.type:
        imagebutton auto "images/Button_" + Player.focused_Girl.tag + "_%s.png" action ShowTransient("Focus_Map") pos (0.71, 0.016) focus_mask True

    showif config.developer:
        imagebutton auto "images/Button_" + Player.focused_Girl.tag + "_%s.png" action Call("cheat_menu", Player.focused_Girl) pos (0.755, 0.016) focus

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
            text "[Player.focused_Girl.tag] Level: [Player.focused_Girl.level]" size 18

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
            imagebutton auto "images/Button_Rogue_%s.png" action Call("text_menu", RogueX) focus_mask True

            if KittyX in active_Girls:
                imagebutton auto "images/Button_Kitty_%s.png" action Call("text_menu", KittyX) focus_mask True

        vbox:
            if EmmaX in active_Girls:
                imagebutton auto "images/Button_Emma_%s.png" action Call("text_menu", EmmaX) focus_mask True

            if LauraX in active_Girls:
                imagebutton auto "images/Button_Laura_%s.png" action Call("text_menu", LauraX) focus_mask True

        vbox:
            if JeanX in active_Girls:
                imagebutton auto "images/Button_Jean_%s.png" action Call("text_menu", JeanX) focus_mask True

            if StormX in active_Girls:
                imagebutton auto "images/Button_Storm_%s.png" action Call("text_menu", StormX) focus_mask True

        vbox:
            if JubesX in active_Girls:
                imagebutton auto "images/Button_Jubes_%s.png" action Call("text_menu", JubesX) focus_mask True

            if MystiqueX in active_Girls:
                imagebutton auto "images/Button_Mystique_%s.png" action Call("text_menu", MystiqueX) focus_mask True

screen Inventory_screen:
    frame:
        minimum (300, 0) pos (0.83, 0.125)
        has vbox

        text "Inventory:" size 20
        showif "Xavier's photo" in Player.inventory:
            text "Xavier's Photo" size 15
        showif "Xavier's files" in Player.inventory:
            text "Xavier's Files" size 15

        showif "dildo" in Player.inventory:
            $ inventory_count = Player.inventory.count("dildo")
            text "Dildos: [inventory_count]" size 15
        showif "vibrator" in Player.inventory:
            $ inventory_count = Player.inventory.count("vibrator")
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

            textbutton "Mandrill Cologne: [inventory_count] doses" action Call("mandrill_screen") text_size 15
        showif "Purple Rain Cologne" in Player.inventory:
            $ inventory_count = Player.inventory.count("Purple Rain Cologne")

            textbutton "Purple Rain Cologne: [inventory_count] doses" action Call("purplerain_screen") text_size 15
        showif "Corruption Cologne" in Player.inventory:
            $ inventory_count = Player.inventory.count("Corruption Cologne")

            textbutton "Corruption Cologne: [inventory_count] doses" action Call("corruption_screen") text_size 15

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
