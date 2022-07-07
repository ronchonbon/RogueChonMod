screen Girl_picker():
    for Girl in all_Girls:
        if renpy.showing(Girl.tag + "_sprite"):
            button:
                background None
                anchor (0.5, 0.5) pos (Girl.sprite_location + 0.02, 0.6) xysize (250, 900)
                action Call("chat_menu", Girl)

screen Clothing_picker(Girl):
    window:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        style "menu_window"

        window anchor (0.5, 0.5) pos (0.5, 0.5) xysize (int(4.2*256), 600):
            vpgrid:
                cols 4
                spacing 0

                mousewheel True
                draggable True

                side_yfill True

                imagebutton:
                    anchor (0.5, 0.5) pos (0.5, 0.5) xysize (256, 256)
                    auto "images/Button_X_%s.png"
                    action Return("quit")

                for Clothing in Girl.Wardrobe.Clothes.values():
                    # $ img = f"images/menu_images/{Girl.tag}/{Clothing.string}.png"
                    $ img = f"images/Button_{Girl.tag}_hover.png"

                    imagebutton:
                        anchor (0.5, 0.5) pos (0.5, 0.5) xysize (256, 256)
                        idle img
                        hover img
                        action Return(Clothing.name)
