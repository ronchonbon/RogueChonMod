style phone is default

style phone_frame:
    background "phone_background"
    foreground "phone_foreground"

    ysize 815
    xsize 495

style phone_viewport:
    xfill True
    yfill True

    yoffset -20

style phone_vbox:
    xfill True

    spacing 10

transform message_appear(direction):
    xoffset 50*direction alpha 0.0
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

transform message_appear_icon:
    zoom 0.0
    easein_back 0.5 zoom 1.0

screen texting(dialogue, items = None):
    style_prefix "phone"

    frame anchor (0.5, 0.5) pos (0.5, 0.5):
        viewport:
            draggable True
            mousewheel True

            yinitial 1.0

            vbox:
                null height 20
                use nvl_phonetext(dialogue)
                null height 20

                for caption, action, chosen in items:
                    button xalign 0.5:
                        background Frame("images/UI/phone/phone_send_frame.png", 23, 23, 23, 23)

                        padding (20, 20)
                        xsize 350

                        action action
                        text caption

screen nvl_phonetext(dialogue):
    style_prefix None

    $ previous_d_who = None

    for id_d, d in enumerate(dialogue):
        if d.who == Player.name:
            $ message_frame = "images/UI/phone/phone_send_frame.png"
        else:
            $ message_frame = "images/UI/phone/phone_received_frame.png"

        hbox:
            spacing 10

            if d.who == Player.name:
                box_reverse True

            if previous_d_who != d.who:
                if d.who == Player.name:
                    $ message_icon = "images/UI/phone/phone_send_icon.png"
                else:
                    $ message_icon = f"{Player.focused_Girl.tag}_hover"

                add message_icon:
                    if d.current:
                        at message_appear_icon()

            else:
                null width 107

            vbox:
                yalign 1.0

                if d.who != Player.name and previous_d_who != d.who:
                    text d.who

                frame:
                    background Frame(message_frame, 23, 23, 23, 23)

                    padding (20, 20)
                    xsize 350

                    if d.current:
                        if d.who == Player.name:
                            at message_appear(1)
                        else:
                            at message_appear(-1)

                    text d.what:
                        pos (0, 0)
                        xsize 350
                        slow_cps False

                        if d.who == Player.name :
                            color "#FFF"
                            text_align 1.0
                        else:
                            color "#000"

                        id d.what_id

        $ previous_d_who = d.who
