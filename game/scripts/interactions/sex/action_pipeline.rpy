label start_Action(Girl, Action_type, context = None):
    while True:
        call before_Action(Girl, Action_type, context)

        if _return == "continue":
            call Action_cycle(Girl, Action_type)

            if _return[1] == "switch":
                call after_Action(Girl, Action_type, "switch")
                call stop_all_Actions

                return "switch"
            elif _return[1] == "stop":
                call after_Action(Girl, Action_type, "stop")
                call stop_all_Actions

                return "stop"
            else:
                $ Action_type = _return[0]
                $ context = _return[1]
        elif _return == "stop":
            call stop_all_Actions

            return "stop"

label before_Action(Girl, Action_type, context = None):
    $ Girl.change_face("sexy")

    if Action_type in active_Action_types:
        $ Actor = Player

        $ Target = Girl
    elif Action_type in passive_Action_types:
        $ Actor = Girl

        $ Target = Player

    $ Actor.primary_Action = ActionClass(Action_type, Target = Target)

    if Action_type == "kiss":
        if Girl == RogueX and not Girl.permanent_History["kiss"]:
            call first_kiss

            return "stop"
        else:
            call kiss_launch(Girl)
    elif Action_type in job_Action_types:
        $ Player.sprite = True

        if Action_type == "handjob":
            call show_handjob(Girl)
        elif Action_type == "footjob":
            call show_sex(Girl)
        elif Action_type == "titjob":
            call show_titjob(Girl)
        elif Action_type == "blowjob":
            call show_blowjob(Girl)
        elif Action_type in dildo_Action_types:
            call pussy_launch(Girl)
    elif Action_type in sex_Action_types:
        $ Player.sprite = True

        call show_sex(Girl)

    return "continue"

label Action_cycle(Girl, Action_type):
    while round > 0:
        $ stack_depth = renpy.call_stack_depth()

        if Player.climax < 100:
            if Action_type == "kiss":
                call kiss_menu(Girl)
            elif Action_type in fondle_Action_types:
                call fondle_menu(Girl, Action_type)
            elif Action_type in job_Action_types:
                call handjob_menu(Girl, Action_type)
            elif Action_type in sex_Action_types:
                call sex_menu(Girl, Action_type)

            if _return[1] == "switch":
                return [None, "switch"]
            elif _return[1] == "stop":
                return [None, "stop"]
            elif _return[1] != "continue":
                $ Action_type = _return[0]
                $ context = _return[1]

                return [Action_type, context]

        $ counter += 1
        $ round -= 1

        if (Action_type in ["blowjob"] and Girl.primary_Action.speed) or (Action_type in ["sex", "anal"] and Player.primary_Action.speed):
            $ Player.cock_wet = True
            $ Player.spunk = False if (Player.spunk and not Girl.spunk["pussy"]) else Player.spunk

        call end_of_Action_round(Girl, Action_type)

        if _return[1] == "switch":
            return [None, "switch"]
        elif _return[1] == "stop":
            return [None, "stop"]
        elif _return[1] != "continue":
            $ Action_type = _return[0]
            $ context = _return[1]

            return [Action_type, context]

    call end_of_Action_reaction(Girl, Action_type)

    return [None, "stop"]

label after_Action(Girl, Action_type, context = None):
    $ Girl.change_face("sexy")
    $ Girl.permanent_History[Action_type] += 1
    $ Girl.remaining_Actions -= 1

    $ Player.sprite = False

    $ checkout()

    return
