style Action_menu is default

style Action_menu_window is window:
    background None

style Action_menu_text is button_text clear:
    size 24

screen Action_menu():
    style_prefix "Action_menu"

    window:
        anchor (0.5, 0.0) pos (0.15, 0.35)
