define ch_p = Character('[Player.name]', color = "#87CEEB", show_two_window = True)

define ch_r = Character('[RogueX.name]', color = "#85bb65", image = "Rogue_sprite", show_two_window = True)
define ch_k = Character('[KittyX.name]', color = "#F5A9D0", image = "Kitty_sprite", show_two_window = True)
define ch_e = Character('[EmmaX.name]', color = "#98bee7", image = "Emma_sprite", show_two_window = True)
define ch_l = Character('[LauraX.name]', color = "#d8b600", image = "Laura_sprite", show_two_window = True)
define ch_j = Character('[JeanX.name]', color = "#b2d950", image = "Jean_sprite", show_two_window = True)
define ch_s = Character('[StormX.name]', color = "#b2d950", image = "Storm_sprite", show_two_window = True)
define ch_v = Character('[JubesX.name]', color = "#b2d950", image = "Jubes_sprite", show_two_window = True)
define ch_m = Character('[MystiqueX.name]', color = "b2d950", image = "Mystique_sprite", show_two_window = True)

define ch_x = Character('[Xavier.name]', color = "#a09400", image = "Xavier_sprite", show_two_window = True)
define ch_b = Character('Dr. McCoy', color = "#1033b2", show_two_window = True)

define ch_u = Character('???', color = "#85bb65", show_two_window = True)

label splashscreen:
    return

label start:
    python:
        renpy.start_predict("images/backgrounds/*.*")

        for G in all_Girls:
            renpy.start_predict("images/" + G.tag + "_standing/*.*")

    $ Player = PlayerClass()

    python:
        Player.name = renpy.input("What is your name?", default = "Zero", length = 10)
        Player.name = Player.name.strip()

        if not Player.name :
            Player.name  = "Zero"

    menu:
        "What is your skin color?"
        "Green":
            $ Player.color = "green"
        "White":
            $ Player.color = "white"
        "Black":
            $ Player.color = "black"

    $ RogueX = GirlClass("Rogue", 500, 0, 0, 10)
    $ KittyX = GirlClass("Kitty", 400, 100, 0, 10)
    $ EmmaX = GirlClass("Emma", 300, 0, 200, 15)
    $ LauraX = GirlClass("Laura", 400, 0, 200, 10)
    $ JeanX = GirlClass("Jean", 0, 0, 1000, 10)
    $ StormX = GirlClass("Storm", 500, 0, 100, 10)
    $ JubesX = GirlClass("Jubes", 500, 50, 50, 10)
    $ MystiqueX = GirlClass("Mystique", 0, 0, 0, 15)

    $ Xavier = NPCClass("Professor X")

    $ Player.focused_Girl = RogueX

    show screen status_screen
    show screen inventory_button

    $ Player.cash = 100000

    jump prologue

return
