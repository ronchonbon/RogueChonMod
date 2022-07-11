init python:

    def approval_check(Girl, threshold = None, flavor = "LOI", spread = 150, alternate_thresholds = {}):
        if Girl in alternate_thresholds.keys():
            threshold = alternate_thresholds[Girl]

        if "L" in flavor:
            L = Girl.love
        else:
            L = 0

        if "O" in flavor:
            O = Girl.obedience
        else:
            O = 0

        if "I" in flavor:
            I = Girl.inhibition
        else:
            I = 0

        if not threshold:
            return L + O + I

        if L + O + I >= threshold + 2*spread:
            return 3
        elif L + O + I >= threshold + spread:
            return 2
        elif L + O + I >= threshold:
            return 1
        else:
            return 0

    def check_if_alone(Girl):
        for G in all_Girls:
            if G != Girl and G.location == Player.location:
                return False

        return True

label check_who_is_present(location = None):
    python:
        Present = Player.Party[:] if Player.Party else []

        if not location:
            location = Player.location

        for G in all_Girls:
            if G not in Player.Party:
                if G not in Present and G.location == location:
                    Present.append(G)
                elif G in Present and G.location != location:
                    Present.remove(G)

        for G in Present:
            if G in Nearby:
                Nearby.remove(G)

        if Present and Player.focused_Girl not in Present:
            renpy.random.shuffle(Present)

            shift_focus(Present[0])

    return

label dildo_check(Girl):
    if "dildo" in Player.inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in Girl.inventory:
        "You ask [Girl.name] to get out her favorite dildo."
    else:
        "You don't have one of those on you."

        return "not_found"

    return "found"

label vibrator_check(Girl):
    if "vibrator" in Player.inventory:
        "You pull out the \"Shocker\" vibrator, handy."
    elif "vibrator" in Girl.inventory:
        "You ask [Girl.name] to get out her vibrator."
    else:
        "You don't have one of those on you."

        return "not_found"

    return "found"
