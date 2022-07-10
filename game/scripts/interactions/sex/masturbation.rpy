label masturbate(Girl, context = None):
    while True:
        call before_masturbation(Girl)
        call masturbation_cycle(Girl)

        if _return == "interrupt":
            call after_masturbation(Girl, "interrupt")

            if _return == "switch":
                return "switch"
            elif _return == "stop":
                return "stop"
        elif _return == "switch":
            call after_masturbation(Girl, "switch")
            call stop_all_Actions

            return "switch"
        elif _return == "stop":
            call after_masturbation(Girl, "stop")
            call stop_all_Actions

            return "stop"

label before_masturbation(Girl):
    $ Girl.primary_Action = ActionClass("fondle_pussy", Target = Girl)

    return

label masturbation_cycle(Girl):
    while round > 0:
        $ stack_depth = renpy.call_stack_depth()

        if Player.climax < 100:
            call masturbation_menu(Girl)

            if _return != "continue":
                $ context = _return

                return context

        $ counter += 1
        $ round -= 1

        $ Player.climax = 50 if not Player.semen and Player.climax >= 50 else Player.focus

        if Player.climax >= 100 or Girl.lust >= 100:
            $ orgasmed = False

            if Player.climax >= 100:
                $ orgasmed = True

            if orgasmed:
                if not Player.semen:
                    "You're emptied out, you should probably take a break."

        if round == 10:
            call ten_rounds_left_lines(Girl, "masturbation")
        elif round == 5:
            call five_rounds_left_lines(Girl, "masturbation")

    return "stop"

label after_masturbation(Girl, context):
    $ Girl.remaining_Actions -= 1
    $ Girl.permanent_History["masturbation"] += 1

    $ checkout()

    return "stop"
