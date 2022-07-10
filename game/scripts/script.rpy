define ch_p = Character("[name]", color = "#87CEEB")
define ch_p_nvl = Character("[name]", kind = nvl)

define ch_r = Character("[RogueX.name]", color = "#85bb65", image = "Rogue_sprite")
define ch_r_nvl = Character("[RogueX.name]", kind = nvl)
define ch_k = Character("[KittyX.name]", color = "#F5A9D0", image = "Kitty_sprite")
define ch_k_nvl = Character("[KittyX.name]", kind = nvl)
define ch_e = Character("[EmmaX.name]", color = "#98bee7", image = "Emma_sprite")
define ch_e_nvl = Character("[EmmaX.name]", kind = nvl)
define ch_l = Character("[LauraX.name]", color = "#d8b600", image = "Laura_sprite")
define ch_l_nvl = Character("[LauraX.name]", kind = nvl)
define ch_j = Character("[JeanX.name]", color = "#b2d950", image = "Jean_sprite")
define ch_j_nvl = Character("[JeanX.name]", kind = nvl)
define ch_s = Character("[StormX.name]", color = "#b2d950", image = "Storm_sprite")
define ch_s_nvl = Character("[StormX.name]", kind = nvl)
define ch_v = Character("[JubesX.name]", color = "#b2d950", image = "Jubes_sprite")
define ch_v_nvl = Character("[JubesX.name]", kind = nvl)
define ch_m = Character("[MystiqueX.name]", color = "b2d950", image = "Mystique_sprite")
define ch_m_nvl = Character("[MystiqueX.name]", kind = nvl)

define ch_x = Character("[Xavier.name]", color = "#a09400", image = "Xavier_sprite")
define ch_b = Character("Dr. McCoy", color = "#1033b2")

define ch_u = Character("???", color = "#85bb65")

label splashscreen:
    return

label start:
    python:
        renpy.start_predict("images/backgrounds/*.*")

        for G in all_Girls:
            renpy.start_predict("images/" + G.tag + "_standing/*.*")

        name = renpy.input("What is your name?", default = "Zero", length = 10)
        name = name.strip()

        if not name:
            name  = "Zero"

    menu:
        "What is your skin color?"
        "Green":
            $ color = "green"
        "White":
            $ color = "white"
        "Black":
            $ color = "black"

    $ Player = PlayerClass(name, color)

    $ RogueX = GirlClass("Rogue", 500, 0, 0, 10)
    $ KittyX = GirlClass("Kitty", 400, 100, 0, 10)
    $ EmmaX = GirlClass("Emma", 300, 0, 200, 15)
    $ LauraX = GirlClass("Laura", 400, 0, 200, 10)
    $ JeanX = GirlClass("Jean", 0, 0, 1000, 10)
    $ StormX = GirlClass("Storm", 500, 0, 100, 10)
    $ JubesX = GirlClass("Jubes", 500, 50, 50, 10)
    $ MystiqueX = GirlClass("Mystique", 0, 0, 0, 15)

    $ Xavier = NPCClass("Professor X")

    $ Player.cash = 100000

    $ Event_registry()
    
    jump prologue

return
