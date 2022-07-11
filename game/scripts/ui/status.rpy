transform rotate_white(x):
    rotate -int(3.6*x)

transform rotate_red(x):
    rotate -int(3.6*x - 180)

transform tiny_button:
    zoom 0.5

screen status():
    add "images/UI/backdrops/[Player.focused_Girl.tag]_backdrop.png"

    vbox pos (0.005, 0.005):
        spacing 5

        hbox:
            spacing 5

            add "images/UI/icons/love_icon.png"
            bar range 1000 value Player.focused_Girl.love xmaximum 200 ymaximum 40 left_bar At("full_bar", love_color) right_bar "empty_bar" thumb None yalign 1.0

        hbox:
            spacing 5

            add "images/UI/icons/lust_icon.png"
            bar range 100 value Player.focused_Girl.lust xmaximum 200 ymaximum 40 left_bar At("full_bar", lust_color) right_bar "empty_bar" thumb None yalign 1.0

    vbox pos (0.155, 0.005):
        spacing 5

        hbox:
            spacing 5

            add "images/UI/icons/obedience_icon.png"
            bar range 1000 value Player.focused_Girl.obedience xmaximum 200 ymaximum 40 left_bar At("full_bar", obedience_color) right_bar "empty_bar" thumb None yalign 1.0

        hbox:
            spacing 5

            add "images/UI/icons/addiction_icon.png"
            bar range 100 value Player.focused_Girl.addiction xmaximum 200 ymaximum 40 left_bar "full_bar" right_bar "empty_bar" thumb None yalign 1.0

    vbox pos (0.305, 0.005):
        spacing 5

        hbox:
            spacing 5

            add "images/UI/icons/inhibition_icon.png"
            bar range 1000 value Player.focused_Girl.inhibition xmaximum 200 ymaximum 40 left_bar At("full_bar", inhibition_color) right_bar "empty_bar" thumb None yalign 1.0

        hbox:
            spacing 5

            add "images/UI/icons/addiction_rate_icon.png"
            bar range 100 value 10*Player.focused_Girl.addiction_rate xmaximum 200 ymaximum 40 left_bar "full_bar" right_bar "empty_bar" thumb None yalign 1.0

    vbox pos (0.455, 0.005):
        spacing 5

        hbox:
            spacing 5

            null height 50
            bar range 100 value Player.climax xmaximum 200 ymaximum 40 left_bar "full_bar" right_bar "empty_bar" thumb None yalign 1.0

        hbox:
            spacing 5

            null height 50
            bar range 100 value 20*Player.semen xmaximum 200 ymaximum 40 left_bar "full_bar" right_bar "empty_bar" thumb None yalign 1.0

    imagebutton pos (0.71, 0.016) :
        auto f"{Player.focused_Girl.tag}_%s"
        action ShowTransient("focus_map")
        focus_mask True

    showif config.developer:
        imagebutton pos (0.755, 0.016):
            auto f"{Player.focused_Girl.tag}_%s"
            action Call("cheat_menu", Player.focused_Girl)
            focus_mask True

    imagebutton pos (0.8, 0.01):
        auto "inventory_%s"
        action Show("inventory")
        focus_mask True

    frame pos (0.58, 0.015):
        minimum (200, 0)
        background None

        has vbox

        hbox:
            text "Money: $[Player.cash]" size 18

        hbox:
            text "Level: [Player.level]" size 18

        hbox:
            text "[Player.focused_Girl.tag] Level: [Player.focused_Girl.level]" size 18

    frame pos (0.905, 0.047):
        background None

        add "images/UI/icons/clock_base.png":
            anchor (0.5, 0.5) yzoom -1.0

        if round < 50:
            add "images/UI/icons/clock_red.png" at rotate_red(round):
                anchor (0.5, 0.5)
        else:
            add "images/UI/icons/clock_white.png" at rotate_white(round):
                anchor (0.5, 0.5)

        add "images/UI/icons/clock_face.png":
            anchor (0.5, 0.5)

    frame pos (0.93, 0.018):
        minimum (200, 0)
        background None

        has vbox

        hbox:
            text "Day: [day] [day_of_week]" size 18

        hbox:
            text "Time: [current_time]" size 16

        hbox:
            text "Stack depth: [stack_depth]" size 14

    vpgrid pos (0.905, 0.1):
        cols 4

        for G in Nearby:
            add f"{G.tag}_hover" at tiny_button

screen focus_map():
    imagebutton auto "exit_%s" action Hide("focus_map") pos (0.71, 0.016) focus_mask True

    vpgrid pos (0.71, 0.09):
        cols 4

        for G in active_Girls:
            if G.location != Player.location:
                imagebutton auto f"{G.tag}_%s" action Call("text_menu", G) focus_mask True
            else:
                imagebutton auto f"{G.tag}_%s" action NullAction() focus_mask True

screen inventory():
    vbox pos (0.83, 0.125):
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

    imagebutton pos (0.8, 0.01):
        auto "inventory_%s"
        action Hide("inventory")
        focus_mask True
