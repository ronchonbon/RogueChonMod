label Sex_Dialog(Primary, Secondary):
    $ TempFocus=0
    $ PrimaryLust=0
    $ SecondaryLust=0
    $ line2=0
    $ line3=0
    $ line4=0
    $ D20S=0




    $ D20S = renpy.random.randint(1, 20) if not D20S else D20S
    $ line = 0







    call Girls_taboo (Primary)

    call Primary_SexDialog
    $ line1 = line



    if Player.secondary_Action and D20S <= 15:

        $ line = ""
        call Offhand_Dialog
        $ line1 = line1 + line



    if D20S >= 7 and Player.primary_Action not in ("masturbation", "lesbian"):

        $ line = 0
        call Girl_Self_lines (Primary, "T3", Primary.secondary_Action, D20X=D20S)
        if line:
            $ line3 = line + "_."



    if Secondary and (not second_Girl_main_action or 7 <= D20S <= 17 or second_Girl_main_action == "watch"):

        $ line = 0
        call SexDialog_Threeway
        if line:
            $ line4 = line + "_."



    call change_Player_stat("focus", 200, TempFocus)


    call change_Girl_stat(Primary, "lust", PrimaryLust)
    $ Primary.lust_face()


    if Secondary:
        $ SecondaryLust += (int(PrimaryLust/10)) if Secondary.likes[Primary.tag] >= 700 else 0
        call change_Girl_stat(Secondary, "lust", SecondaryLust)
        $ Secondary.lust_face()


    "[line1]"
    if line3:

        call Seen_First_Peen (Primary, Secondary, Passive = 3)
        "[line3]"
    if line4:


        call Seen_First_Peen (Primary, Secondary, Passive=4)
        "[line4]"
        if second_Girl_main_action == "suck_breasts" or second_Girl_main_action == "fondle_breasts":

            if approval_check(Primary, 500, "I",taboo_modifier=2) and Primary.lust >= 50 and (Primary.Clothes["bra"] or Primary.top_number() > 1):

                $ Primary.top_pulled_up = 1
                "[Primary.name] seems frustrated and pulls her top open."

    call Activity_check (Primary, Secondary, 0)
    if not _return:

        if Primary.forced:


            return
        if Secondary and Secondary.location == Player.location:
            $ Partner = None
            $ second_Girl_main_action = None
            $ second_Girl_secondary_Action = None
        else:



            call stop_all_Actions
        jump reset_location

    call Dirty_Talk

    return



label Primary_SexDialog(GirlA=Primary, Templine=0, TempLust=0, TempLust2=0):
    if Player.primary_Action == "handjob":
        $ line = GirlA.name + " continues stroke your cock. "

        if not action_speed:
            $ line = GirlA.name + " holds your cock in her hand. "
            if GirlA.permanent_History["handjob"] > 2:
                $ line = line + "_She just seems to be enjoying the feel of it"
                $ TempLust += 2 if GirlA.lust < 60 else 0
            else:
                $ line = line + "_She just seems to be looking it over"
                $ TempLust += 2 if GirlA.lust < 40 else 0
                $ TempFocus += -3 if Player.climax > 50 else 2
            $ GirlA.addiction -= 1 if D20S > 10 else 2
            return
        if GirlA in (EmmaX,LauraX, StormX):

            if action_speed <= 1:

                $ line = line + renpy.random.choice(["Her movements have become masterful, her slightest touch starts you twitching",
                                    "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here",
                                    "She slowly caresses you in a way that makes your blood boil, then pulls back at the last second",
                                    "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                    "You can't tell where she is at any moment, all you know is that it works"])
                $ TempFocus += 20 if Player.climax < 60 else 7
            else:

                $ line = line + renpy.random.choice(["Her movements have become masterful, her slightest touch starts you twitching",
                                    "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here",
                                    "Her expert strokes will have you boiling over in seconds",
                                    "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, you can tell she's had plenty of practice",
                                    "You can't tell where she is at any moment, all you know is that it works"])
                $ TempFocus += 20 if Player.climax > 70 else 7
        elif GirlA.permanent_History["handjob"] > 4:

            if action_speed <= 1:

                $ line = line + renpy.random.choice(["Her movements have become almost masterful, her slightest touch starts you twitching",
                                    "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here",
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She slowly caresses you in a way that makes your blood boil, then pulls back at the last second",
                                    "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                    "You can't tell where she is at any moment, all you know is that it works"])
                $ TempFocus += 20 if Player.climax < 40 else 5
            else:

                $ line = line + renpy.random.choice(["Her movements have become almost masterful, her slightest touch starts you twitching",
                                    "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here",
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "Her expert strokes will have you boiling over in seconds",
                                    "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                    "You can't tell where she is at any moment, all you know is that it works"])
                $ TempFocus += 20 if Player.climax > 70 else 5
        elif 2 < GirlA.permanent_History["handjob"] <= 4:

            if action_speed <= 1:

                $ line = line + renpy.random.choice(["She's begining to figure things out, her fingers cause tingles as they caress the shaft",
                                    "She's still learning, but learning fast. Her hands sure are smooth",
                                    "She has a smooth motion going now, gentle and precise",
                                    "Her lessons are paying off, she's really becoming very talented at this",
                                    "She gently caresses the shaft, and cups the balls in her other hand, giving them a warm massage"])
                $ TempFocus += 15 if Player.climax < 60 else 7
            else:

                $ line = line + renpy.random.choice(["She's begining to figure things out, her fingers cause tingles as they caress the shaft",
                                    "She's still learning, but learning fast. Her hands sure are smooth",
                                    "Her hands glide smoothly across your cock",
                                    "She has a smooth motion going now, gentle and precise",
                                    "Her lessons are paying off, she's really becoming very talented at this",
                                    "She quickly strokes your cock, with a very deft pressure"])
                $ TempFocus += 15 if Player.climax > 60 else 5
        else:

            if action_speed <= 1:

                $ line = line + renpy.random.choice(["She makes up for her inexperience with determination, carefully stroking your cock",
                                "She moves her hands up and down the shaft. She's a little rough at this, but at least she tries",
                                "She strokes you gently. She isn't quite sure what to make of the balls",
                                "Her fingers fumble with your shaft a bit",
                                "She squeezes one of your balls too tightly, but stops when you wince",
                                "She has a firm grip, and she's not letting go. This may take a few tries"])
                $ TempFocus += 12 if Player.climax > 60 else 5
            else:

                $ line = line + renpy.random.choice(["She really wasn't prepared for speeding up, and your cock often slips out of her hand",
                                "She rapidly moves her hands up and down the shaft. She's a little rough at this, but at least she tries",
                                "She strokes you a bit too quickly, the friction is a bit uncomfortable",
                                "Her fingers fumble with your shaft a bit",
                                "She squeezes one of your balls too tightly, but stops when you wince",
                                "She has a firm grip, and she's not letting go. This train is out of control"])
                $ TempFocus += 10 if Player.climax > 60 else 2

        $ TempLust += 2 if GirlA.lust < 60 else 0
        $ TempLust += 2 if GirlA.permanent_History["handjob"] > 2 else 0
        $ GirlA.addiction -= 1 if D20S > 10 else 2




    elif Player.primary_Action == "titjob":


        if not action_speed:
            if GirlA == KittyX:
                $ line = GirlA.name + " begins to rub her chest against you"
            elif GirlA.permanent_History["titjob"] > 2:
                $ line = GirlA.name + " begins to bounce her breasts up and down"
            else:
                $ line = GirlA.name + " squeezes her breasts together and slowly moves them along your shaft"
            $ action_speed = 1
            $ TempFocus += 12 if Player.climax < 60 else 6
            $ TempLust += 6 if GirlA.lust > 60 else 3
            return

        if GirlA in (EmmaX, StormX) or (GirlA.permanent_History["titjob"] > 4 and GirlA.permanent_History["blowjob"]):

            if action_speed <= 1:

                $ line = renpy.random.choice([GirlA.name + " rocks her breasts up and down around your cock",
                                    GirlA.name + " lightly licks the head as it pops up between her tits",
                                    GirlA.name + " has a smooth motion going now, gentle and precise",
                                    GirlA.name + " pauses to rub her nipples across the shaft",
                                    "In between strokes " + GirlA.name + " gently sucks on the head",
                                    GirlA.name + " drips some spittle down to make sure you're properly lubed",
                                    GirlA.name + " gently caresses the shaft between her tits"])

                $ TempFocus += 15 if Player.climax < 70 else 5
                $ TempLust += 7 if GirlA.lust > 60 else 4
            else:

                $ line = renpy.random.choice([GirlA.name + " rapidly rocks her breasts up and down around your cock",
                                    GirlA.name + " licks away at the head every time it pops up between her tits",
                                    GirlA.name + " has a smooth motion going now, quick by efficient",
                                    GirlA.name + " dances her nipples across the shaft",
                                    "In as she strokes faster and faster, " + GirlA.name + " bends down to suck on the head",
                                    GirlA.name + " covers her tits with drool to keep them well lubed",
                                    GirlA.name + " rapidly caresses the shaft between her tits"])

                $ TempFocus += 20 if Player.climax > 40 else 5
                $ TempLust += 6 if GirlA.lust > 70 else 4


        elif GirlA.permanent_History["titjob"] > 1:

            if action_speed <= 1:

                $ line = renpy.random.choice([GirlA.name + " juggles her breasts up and down around your cock",
                                GirlA.name + " lightly strokes the head as it pops up between her tits",
                                GirlA.name + " has a smooth motion going now, gentle and precise",
                                GirlA.name + " pauses to rub her nipples across the shaft",
                                GirlA.name + " gently caresses the shaft between her tits"])

                $ TempFocus += 15 if Player.climax < 60 else 5
                $ TempLust += 6 if GirlA.lust > 60 else 3
            else:

                $ line = renpy.random.choice([GirlA.name + " rapidly juggles her breasts up and down around your cock",
                            GirlA.name + " lightly brushes the head with her chin as it pops up between her tits",
                            GirlA.name + " moves them up and down in a fluid rocking motion",
                            GirlA.name + " bounces her whole body up and down",
                            GirlA.name + " rapidly slides the shaft between her tits"])

                $ TempFocus += 15 if Player.climax > 50 else 7
                $ TempLust += 6 if GirlA.lust > 60 else 4
        else:


            if action_speed <= 1:

                $ line = renpy.random.choice([GirlA.name + " sort of squishes her breasts back and forth around your cock",
                            GirlA.name + " slides the cock up and down between her cleavage",
                            GirlA.name + " kind of bounces her tits around your cock",
                            GirlA.name + " smooshes her cleavage as tight as she can and rubs up and down"])

                $ TempFocus += 12 if Player.climax < 60 else 6
                $ TempLust += 6 if GirlA.lust > 60 else 3
            else:


                $ line = renpy.random.choice([GirlA.name + " sort of bounces her breasts off your cock",
                            GirlA.name + " tries to quickly slide the cock up and down between her cleavage, but it tends to slide out",
                            GirlA.name + " slaps her tits against your dick",
                            GirlA.name + " smooshes her cleavage as tight as she can and rubs up and down quite quickly"])

                $ TempFocus += 8 if Player.climax > 70 else 4
                $ TempLust += 5 if GirlA.lust > 60 else 3

        if GirlA == KittyX:
            $ TempFocus -= 2
        elif GirlA in (EmmaX, StormX):
            $ TempFocus += 1

        $ GirlA.addiction -= 2



    elif Player.primary_Action == "blowjob":
        if not action_speed:

            if "hungry" in GirlA.traits:
                $ GirlA.change_face("sly")
                $ line = GirlA.name + " stares at your cock. She licks her lips in anticipation"
                $ TempLust += 3 if GirlA.lust < 40 else 1
            elif GirlA.permanent_History["blowjob"] > 2:
                $ GirlA.change_face("sly")
                $ line = GirlA.name + " stares at your cock. She seems pretty excited about it"
                $ TempLust += 2 if GirlA.lust < 60 else 0
            elif GirlA == EmmaX:
                $ GirlA.change_face("sly")
                $ line = GirlA.name + " stares at your cock. She seems pretty intrigued by it"
                $ TempLust += 2 if GirlA.lust < 60 else 0
            else:
                $ GirlA.change_face("perplexed")
                $ line = GirlA.name + " stares at your cock with trepidation"
                $ TempLust += 2 if GirlA.lust < 40 else 0

            if GirlA.permanent_History["blowjob"] <= 1 or (GirlA.obedience >= 500 and GirlA.obedience > GirlA.inhibition):
                $ TempLust += 2 if GirlA.lust > 60 else 0
                $ line = line + "_, but she seems to be waiting for some instruction"
            else:
                $ line = line + "_, and then she gets started licking your cock"
                $ action_speed = 1
            return

        elif action_speed < 2:
            $ line = GirlA.name + " continues to lick your cock. "
        else:

            $ line = GirlA.name + " continues to suck your cock. "


        if action_speed == 1:

            if GirlA.permanent_History["blowjob"] > 4 or GirlA in (EmmaX,LauraX, StormX):

                $ line = line + renpy.random.choice(["Her deft licks are masterful, your cock twitches with each stroke",
                                    "She gently blows across the head as she covers your cock in smooth licks",
                                    "How many licks to the center of your cock? No way you're finding out",
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She's really getting good at this, alternating between deep suction and gentle licks",
                                    "She moves very smoothly, tongue dancing casually and very gently, like she's been doing this for years",
                                    "She puts the tip into her mouth and her tounge dances around it"])
                $ TempFocus += 20 if Player.climax < 70 else 15
                $ TempLust += 2 if GirlA.lust > 80 else 1

            elif GirlA.permanent_History["blowjob"] > 1:

                $ line = line + renpy.random.choice(["She's begining to figure things out, her tongue makes your hair stand on end",
                                    "She's still learning, but learning fast. She seems eager to use her mouth for more than talk",
                                    "She's settled into a gentle licking pace that washes over you like a warm bath",
                                    "She licks gently up and down the shaft. She's a little rough at this, but at least she tries",
                                    "Her tongue moves carefully along the shaft",
                                    "She's really starting to learn some clever tricks to making you feel good",
                                    "She licks her way down the shaft, and gently teases the balls"])
                $ TempFocus += 20 if Player.climax > 60 else 10
                $ TempLust += 2 if GirlA.lust > 80 else 1
            else:


                $ line = line + renpy.random.choice([GirlA.name + " makes up for her inexperience with determination, carefully licking your cock",
                                    "She takes a small lick and grimaces at the taste",
                                    "She tentatively kisses around the head a bit",
                                    "She nibbles one of your balls, but stops when you wince",
                                    "She licks all over your dick, but she doesn't really have a handle on it"])
                $ TempFocus += 15 if Player.climax > 60 else 5
            $ GirlA.addiction -= 2

        elif action_speed == 2:

            if GirlA.permanent_History["blowjob"] > 4 or GirlA in (EmmaX,LauraX, StormX):

                $ line = line + renpy.random.choice(["She masterfully bobs on your cock, and it twitches with each stroke",
                                    "She rapidly bobs up and down on your cock, a frenzy of motion",
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She's really getting good at this, alternating between deep suction and quick licks across the head",
                                    "She moves very smoothly, bobbing in and out like she's been doing this for years",
                                    "She puts the tip into her mouth and her tounge swirls rapidly around it"])
                $ TempFocus += 20 if Player.climax < 80 else 10
                $ TempLust += 2 if GirlA.lust > 70 else 1

            elif GirlA.permanent_History["blowjob"] > 1:

                $ line = line + renpy.random.choice(["She's begining to figure things out, she bobs carefully up and down the head",
                                    "She's still learning, but learning fast. She keeps her teeth well clear, aside from a playful nip",
                                    "Her lips envelope you like a warm bath as she bobs in and out",
                                    "She's really starting to learn some clever tricks to making you feel good",
                                    "She rapidly licks her way around the head",
                                    "Her mouth envelopes the head, then she quickly draws it in and draws back with a pop"])
                $ TempFocus += 15 if Player.climax > 80 else 10
                $ TempLust += 1 if GirlA.lust > 60 else 0
            else:


                $ line = line + renpy.random.choice(["She really wasn't prepared for speeding up, and your cock often pops out of her mouth",
                                    "She puts the tip in her mouth and starts to actually suck in as hard as she can. She's a little rough at this, but at least she tries",
                                    "Her head bobs rapidly, until she goes a bit too deep and starts to gag",
                                    "She lets her teeth get a bit too much action",
                                    "She bobs quickly on your cock, but clamps down a bit too tight for comfort"])
                $ TempFocus += 9 if Player.climax > 80 else 3
            $ GirlA.addiction -= 2

        elif action_speed == 3:

            if GirlA.permanent_History["blowjob"] > 4 or GirlA in (EmmaX,LauraX, StormX):

                $ line = line + renpy.random.choice(["She masterfully bobs on your cock, and it twitches with each stroke",
                                    "She smoothly bobs up and down on your cock, a frenzy of motion",
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She gobbles you up all the way to the base, then quickly draws out and plunges back in",
                                    "She's really getting good at this, alternating between deep suction and quick licks across the head",
                                    "She moves very smoothly, bobbing in and out like she's been doing this for years",
                                    "She puts the shaft into her mouth and her tounge swirls rapidly around it"])
                $ TempFocus += 22 if Player.climax > 40 else 10
                $ TempLust += 3 if GirlA.lust > 60 else 1

            elif GirlA.permanent_History["blowjob"] > 1:

                $ line = line + renpy.random.choice(["She's begining to figure things out, she bobs carefully up and down the shaft",
                                    "She's still learning, but learning fast. She keeps her teeth well clear, aside from a playful nip",
                                    "Her lips envelope you like a warm bath as she bobs in and out",
                                    "She slowly draws you in to the base of your cock, then pulls back at the last second",
                                    "She's really starting to learn some clever tricks to making you feel good",
                                    "She rapidly licks her way up and down the shaft as her mouth envelopes you",
                                    "Her mouth envelopes the shaft, then she quickly draws it in and draws back with a pop"])
                $ TempFocus += 15 if Player.climax > 50 else 5
            else:


                $ line = line + renpy.random.choice(["She really wasn't prepared for putting it all the way in, and grimaces at the taste",
                                    "She puts the tip in her mouth and starts to actually suck in as hard as she can. She's a little rough at this, but at least she tries",
                                    "She sucks up and down your cock very quickly, but gets a bit dizzy and has to slow down",
                                    "Her head bobs rapidly, until she goes a bit too deep and starts to gag",
                                    "She lets her teeth get a bit too much action",
                                    "She bobs quickly on your cock, but clamps down a bit too tight for comfort"])
                $ TempFocus += 6 if Player.climax < 50 else 3
            $ GirlA.addiction -= 2 if D20S > 10 else 3
        else:



            if GirlA.permanent_History["blowjob"] > 4 or GirlA in (EmmaX,LauraX, StormX):

                $ line = line + renpy.random.choice(["She masterfully bobs on your cock, and it twitches with each stroke",
                                    "She rapidly bobs to the base of your cock, a frenzy of motion",
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She gobbles you up all the way to the base, then quickly draws out and plunges back in",
                                    "She's really getting good at this, alternating between deep suction and quick licks across the head",
                                    "She moves very smoothly, bobbing in and out like she's been doing this for years",
                                    "She puts the entire shaft into her mouth and her tounge swirls rapidly around it"])
                $ TempFocus += 25 if Player.climax > 40 else 8
                $ TempLust += 3 if GirlA.lust > 60 else 2

            elif GirlA.permanent_History["blowjob"] > 1:

                $ line = line + renpy.random.choice(["She's begining to figure things out, she bobs carefully up and down the shaft",
                                    "She's still learning, but learning fast. She keeps her teeth well clear, aside from a playful nip",
                                    "Her lips envelope you like a warm bath as she bobs in and out",
                                    "She slowly draws you in to the base of your cock, then pulls back at the last second",
                                    "She's really starting to learn some clever tricks to making you feel good",
                                    "She completely envelops the shaft with her throat.",
                                    "Her mouth envelopes the head, then she quickly draws it all the way in and draws back with a pop"])
                $ TempFocus += 20 if Player.climax > 40 else 5
                $ TempLust += -3 if GirlA.lust < 60 else -1
                $ TempLust += 5 if GirlA.obedience > 500 else 0
            else:


                $ line = line + renpy.random.choice(["She really wasn't prepared for going so deep, and gags a bit",
                                    "She puts the whole shaft in her mouth and starts to actually suck in as hard as she can. She's a little rough at this, but at least she tries",
                                    "She draws your cock into her mouth very qucikly, but gets a bit dizzy and has to slow down",
                                    "Her head bobs rapidly, until she goes a bit too deep and starts to gag",
                                    "She lets her teeth get a bit too much action",
                                    "She bobs quickly on your cock, but clamps down a bit too tight for comfort"])
                $ TempFocus += 15 if Player.climax > 80 else 5
                $ TempLust += -5 if GirlA.lust < 60 else -2
                $ TempLust += 7 if GirlA.obedience > 500 else 0
            $ GirlA.addiction -= 3
        $ GirlA.addiction -= 3 if GirlA == JubesX else 0



    elif Player.primary_Action == "sex":


        if not action_speed:

            $ line = "She seems to be waiting for you to do something. . "
            return

        elif action_speed < 2:
            $ line = "You continue to pound " + GirlA.name + "_. "
        else:

            $ line = "You continue to slowly drive into " + GirlA.name + "_. "


        if GirlA.permanent_History["sex"] > 4 or GirlA in (EmmaX,LauraX, StormX):
            if action_speed > 1:

                $ line = line + renpy.random.choice(["She bounces rapidly against your cock",
                            "You thrust into her and she squeaks a bit",
                            "You quickly grind back and forth inside her",
                            "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                            "You pound away at her",
                            "She grinds furiously back and forth along your cock"])
                $ TempFocus += 18 if Player.climax > 50 else 12
                $ TempLust += 16 if GirlA.lust > 70 else 10
            else:

                $ line = line + renpy.random.choice(["She bumps slowly against your cock",
                            "You thrust into her and she coos a bit",
                            "You slowly grind back and forth inside her",
                            "You alternate between long and slow thrusts, and the occasional quick one",
                            "You slowly slide back and forth near the entrance",
                            "She slides slowly back and forth along your cock, teasing you"])
                $ TempFocus += 14 if Player.climax < 60 else 12
                $ TempLust += 12 if 40 > GirlA.lust > 90 else 10

        elif GirlA.permanent_History["sex"] > 1:
            if action_speed > 1:

                $ line = line + renpy.random.choice(["She bounces rapidly against your cock",
                        "You thrust into her and she squeaks a bit",
                        "You quickly grind back and forth inside her",
                        "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                        "You pound away at her",
                        "She grinds furiously back and forth along your cock"])
                $ TempFocus += 12 if Player.climax > 50 else 9
                $ TempLust += 14 if GirlA.lust > 80 else 10
            else:

                $ line = line + renpy.random.choice(["she bumps slowly against your cock",
                        "You thrust into her and she squeaks a bit",
                        "You slowly grind back and forth inside her",
                        "You alternate between long and slow thrusts, and the occasional quick one",
                        "You slowly slide back and forth near the entrance",
                        "She slides slowly back and forth along your cock"])
                $ TempFocus += 12 if Player.climax < 70 else 7
                $ TempLust += 10 if 50 > GirlA.lust > 90 else 8
        else:

            if action_speed > 1:

                $ line = line + renpy.random.choice(["She bounces rapidly against your cock",
                        "You thrust into her and she squeaks in pain",
                        "You quickly grind back and forth inside her but she doesn't seem to have the rhythm down",
                        "She bounces rapidly against your cock, occasionally popping out and having to stick it back in",
                        "You pound away at her",
                        "She moves rapidly back and forth along your cock, but seems a bit uncomfortable"])
                $ TempFocus += 10 if Player.climax > 60 else 9
                $ TempLust += 10 if GirlA.lust > 80 else 6
            else:

                $ line = line + renpy.random.choice(["She bumps slowly against your cock",
                        "You thrust into her and she squeaks a bit",
                        "You slowly grind back and forth inside her",
                        "You alternate between long and slow thrusts, and the occasional quick one",
                        "You slowly slide back and forth near the entrance",
                        "She slides slowly back and forth along your cock"])
                $ TempFocus += 10 if Player.climax < 70 else 9
                $ TempLust += 8 if 60 > GirlA.lust > 90 else 6

        $ GirlA.addiction -= 2



    elif Player.primary_Action == "hotdog":


        $ TempLust2 = 2
        if GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"].state:

            $ TempLust2 -= 1
        if GirlA.hose_number() >= 6:

            $ TempLust2 -= 1
        if GirlA.Clothes["bottom"] and not GirlA.upskirt:

            $ TempLust2 -= 2 if TempLust2 <= 2 else TempLust2

        if not action_speed:
            $ line = "She seems to be waiting for you to do something. . "
            return
        elif action_speed < 2:
            $ line = "You continue to hotdog " + GirlA.name + "_. "
        else:
            $ line = "You continue to grind against " + GirlA.name + "_. "

        if GirlA.permanent_History["hotdog"] >= 2:
            if action_speed > 1:

                $ line = line + renpy.random.choice(["She bounces rapidly against your cock",
                        "You thrust against her and she squeaks a bit",
                        "You quickly grind back and forth along her crack",
                        "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                        "You grind away at her",
                        "She grinds furiously back and forth along your cock"])
                $ TempFocus += (TempLust2 + 8) if Player.climax < 60 else (TempLust2 + 4)
                $ TempLust += (TempLust2 + 8) if 50 > GirlA.lust > 80 else (TempLust2 + 2)

            elif action_speed:

                $ line = line + renpy.random.choice(["She grinds slowly against your cock",
                        "You thrust against her and she coos a bit",
                        "You slowly rub the tip across her pussy",
                        "You alternate between long and slow thrusts, and the occasional rapid ones",
                        "You slowly slide back and forth near her rim",
                        "She slides slowly back and forth along your cock, teasing you"])
                $ TempFocus += (TempLust2 + 8) if Player.climax < 60 else (TempLust2 + 3)
                $ TempLust += (TempLust2 + 7) if 30 > GirlA.lust > 70 else (TempLust2 + 3)
        else:


            if action_speed > 1:

                $ line = line + renpy.random.choice(["She bounces rapidly against your cock",
                        "You thrust against her and she squeaks in surprise",
                        "You quickly grind back and forth against her but she doesn't seem to have the rhythm down",
                        "She bounces rapidly against your cock",
                        "You pound away at her",
                        "She slides rapidly back and forth along your cock, but seems a bit uncomfortable"])
                $ TempFocus += (TempLust2 + 5) if Player.climax < 60 else (TempLust2 + 3)
                $ TempLust += (TempLust2 + 4) if 50 > GirlA.lust > 80 else (TempLust2 + 2)

            elif action_speed:

                $ line = line + renpy.random.choice(["She grinds slowly against your cock",
                        "You thrust into her crack and she squeaks a bit",
                        "You slowly grind back and forth across her rear",
                        "You slowly slide back and forth near her rim",
                        "She slides slowly back and forth along your cock"])
                $ TempFocus += (TempLust2 + 5) if Player.climax < 60 else (TempLust2 + 3)
                $ TempLust += (TempLust2 + 5) if 50 > GirlA.lust > 70 else (TempLust2 + 2)

        if TempLust2:
            $ GirlA.addiction -= 1
            $ TempLust2 = 0




    elif Player.primary_Action == "anal":


        if not action_speed:
            $ line = "She seems to be waiting for you to do something. . "
            return

        elif action_speed < 2:
            $ line = "You continue to pound into " + GirlA.name + "_'s ass. "
        else:
            $ line = "You continue to push into " + GirlA.name + "_'s ass. "


        if GirlA.permanent_History["anal"] >= 5:
            if action_speed > 1:

                $ line = line + renpy.random.choice(["She bounces rapidly against your cock",
                                "You thrust into her and she squeaks a bit",
                                "You quickly grind back and forth inside her",
                                "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                                "You pound away at her",
                                "She grinds furiously back and forth along your cock"])
                $ TempFocus += 18 if Player.climax > 60 else 12
                $ TempLust += 14 if GirlA.lust > 80 else 9
            else:


                $ line = line + renpy.random.choice(["She bumps slowly against your cock",
                                "You thrust into her and she coos a bit",
                                "You slowly grind back and forth inside her",
                                "You alternate between long and slow thrusts, and the occasional quick one",
                                "You slowly slide back and forth near the rim",
                                "She slides slowly back and forth along your cock, teasing you"])
                $ TempFocus += 12 if Player.climax > 60 else 9
                $ TempLust += 12 if 50 < GirlA.lust < 90 else 8

        elif GirlA.used_to_anal:

            if action_speed > 1:

                $ line = line + renpy.random.choice(["She bounces rapidly against your cock",
                                "You thrust into her and she squeaks a bit",
                                "You quickly grind back and forth inside her",
                                "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                                "You pound away at her",
                                "She grinds furiously back and forth along your cock"])
                $ TempFocus += 12 if Player.climax > 60 else 8
                $ TempLust += 12 if GirlA.lust > 80 else 6

            elif action_speed:

                $ line = line + renpy.random.choice(["She bumps slowly against your cock",
                                "You thrust into her and she squeaks a bit",
                                "You slowly grind back and forth inside her",
                                "You alternate between long and slow thrusts, and the occasional quick one",
                                "You slowly slide back and forth near the rim",
                                "She slides slowly back and forth along your cock"])
                $ TempFocus += 13 if Player.climax > 60 else 8
                $ TempLust += 8 if 70 > GirlA.lust > 90 else 4
        else:


            if action_speed > 1:

                $ line = line + renpy.random.choice(["She bounces rapidly against your cock but seems to be in pain",
                                "You thrust into her and she squeaks in pain",
                                "You quickly grind back and forth inside her but she doesn't seem to have the rhythm down",
                                "She bounces rapidly against your cock, occasionally popping out and having to stick it back in",
                                "You pound away at her",
                                "She moves rapidly back and forth along your cock, but seems a bit uncomfortable"])
                $ TempFocus += 10 if Player.climax > 60 else 8
                $ TempLust += 2 if GirlA.lust > 80 else -3

            elif action_speed:

                $ line = line + renpy.random.choice(["She grits her teeth and slides slowly against your cock",
                                "You thrust into her and she squeaks a bit",
                                "You slowly grind back and forth inside her",
                                "You slowly slide back and forth near the rim",
                                "She slides slowly back and forth along your cock"])
                $ TempFocus += 10 if Player.climax > 60 else 6
                $ TempLust += 4 if GirlA.lust > 60 else -1

        if GirlA.used_to_anal > 1:

            $ TempLust += 1

        $ GirlA.addiction -= 3
        $ TempLust = 0 if (GirlA.lust - TempLust) < 0 else TempLust



    elif Player.primary_Action == "fondle_breasts":
        $ line = "You continue to fondle " + GirlA.name + "_. "
        if not GirlA.top_pulled_up and GirlA.Clothes["top"] and GirlA.Clothes["bra"]:

            $ line = line + renpy.random.choice(["You reach under her layers of clothing and massage her breasts",
                                    "You pass your hands gently over her warm breasts",
                                    "Her firm nipples catch on the fabric of her top as you grasp her warm flesh",
                                    "She gasps as you grasp her under her_top"])
            $ TempFocus += 2 if Player.climax < 40 else 1
            $ TempLust += 4 if GirlA.lust > 50 else 2
        elif not GirlA.top_pulled_up and GirlA.Clothes["top"]:

            $ line = line + renpy.random.choice(["You reach under her top and massage her breasts",
                                    "You pass your hands gently over her warm breasts",
                                    "Her nipples catch on the fabric of her top as you grasp her warm flesh, you can see them stiffen",
                                    "She gasps as you grasp her under her " + GirlA.Clothes[top].name])
            $ TempFocus += 2 if Player.climax < 50 else 1
            $ TempLust += 4 if GirlA.lust > 50 else 2
        elif not GirlA.top_pulled_up and GirlA.Clothes["bra"]:

            $ line = line + renpy.random.choice(["You reach under her " + GirlA.Clothes["bra"] + " and massage her breasts",
                                    "You pass your hands gently over her warm breasts",
                                    "Her nipples catch on the fabric of her " + GirlA.Clothes["bra"] + " as you grasp her warm flesh, you can see them stiffen",
                                    "She gasps as you grasp her under her " + GirlA.Clothes[bra].name])
            $ TempFocus += 3 if Player.climax < 60 else 2
            $ TempLust += 5 if GirlA.lust > 50 else 2
        elif GirlA.Clothes["piercings"]:

            $ line = line + renpy.random.choice(["You reach out and massage her glorious breasts",
                                    "You pass your hands gently over her warm breasts, and blow across her pierced nipples",
                                    "Her piercings catch lightly on your fingers as you grasp her warm flesh, you can see the nipples stiffen",
                                    "She gasps as you lightly thumb across her pierced nipples"])
            $ TempFocus += 4 if Player.climax < 70 else 2
            $ TempLust += 6 if GirlA.lust > 40 else 4
        else:
            $ line = line + renpy.random.choice(["You reach out and massage her glorious breasts",
                                    "You pass your hands gently over her warm breasts, and blow across her nipples",
                                    "Her nipples catch lightly on your fingers as you grasp her warm flesh, you can see them stiffen",
                                    "She gasps as you lightly thumb her rigid nipples"])
            $ TempFocus += 4 if Player.climax < 60 else 2
            $ TempLust += 6 if GirlA.lust > 50 else 3
        if D20S > 18:
            if GirlA == KittyX:
                $ line = "You continue to fondle " + GirlA.name + "_. They fit comfortably into your palms."
            elif GirlA in (EmmaX, StormX):
                $ line = "You continue to fondle " + GirlA.name + "_. You can barely wrap your hands around them."
        $ GirlA.addiction -= 2


    elif Player.primary_Action == "suck_breasts":
        $ line = "You continue to suck on " + GirlA.name + "_'s breasts. "
        if not GirlA.top_pulled_up and GirlA.Clothes["top"] and GirlA.Clothes["bra"]:

            $ line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                        "You gently nibble at her nipples as you suck on them through the layered tops",
                                        "You  place a nipple between your lips, and give it a quick tug through the " + GirlA.Clothes["top"],
                                        "She gasps as you gently nibble her rigid nipples poking through her tops"])
            $ TempFocus += 2 if Player.climax < 50 else 1
            $ TempLust += 2 if GirlA.lust < 30 else 1
        elif not GirlA.top_pulled_up and GirlA.Clothes["top"]:

            $ line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                        "You gently nibble at her nipples as you suck on them through the " + GirlA.Clothes["top"],
                                        "You tease her nipples with your tongue through the fabric",
                                        "You slowly lick her nipples through her moist_top",
                                        "You gently place a nipple between your lips, and draw it out until it releases with a *pop*",
                                        "She gasps as you lightly lick her rigid nipples, poking through her_top"])
            $ TempFocus += 2 if Player.climax < 50 else 1
            $ TempLust += 5 if GirlA.lust > 50 else 3
        elif not GirlA.top_pulled_up and GirlA.Clothes["bra"]:

            $ line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                        "You tease her nipples with your tongue through her " + GirlA.Clothes["bra"],
                                        "You slowly lick her nipples through her moist " + GirlA.Clothes["bra"],
                                        "You gently place a nipple between your lips, and draw it out until it releases with a *pop*",
                                        "She gasps as you lightly lick her rigid nipples, poking through her " + GirlA.Clothes[bra].name])
            $ TempFocus += 4 if Player.climax < 60 else 3
            $ TempLust += 5 if GirlA.lust > 50 else 2
        elif GirlA.Clothes["piercings"]:

            $ line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                    "You gently nibble at her nipples as you suck on them",
                                    "You tease her piercings with your tongue",
                                    "You slowly lick around, and then blow across her nipples",
                                    "You gently place a pierced nipple between your lips, and draw it out until it releases with a *pop*",
                                    "She gasps as you lightly lick her rigid nipples"])
            $ TempFocus += 5 if Player.climax < 70 else 4
            $ TempLust += 10 if GirlA.lust > 40 else 7
            $ GirlA.addiction -= 2
        else:
            $ line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                    "You gently nibble at her nipples as you suck on them",
                                    "You tease her nipples with your tongue",
                                    "You slowly lick around, and then blow across her nipples",
                                    "You gently place a nipple between your lips, and draw it out until it releases with a *pop*",
                                    "She gasps as you lightly lick her rigid nipples"])
            $ TempFocus += 5 if Player.climax < 60 else 3
            $ TempLust += 10 if GirlA.lust > 50 else 7
            $ GirlA.addiction -= 2



    elif Player.primary_Action == "fondle_thighs":
        $ line = "You continue to massage " + GirlA.name + "_'s thighs. "

        if GirlA.wearing_pants and not GirlA.upskirt:

            $ line = renpy.random.choice(["Her legs twitch a bit in her pants as you caress them",
                                        "She gasps as you stroke her warm thighs through the_pants",
                                        "You draw your hand from her knee to mid-thigh, and she gasps a little",
                                        "You slide a hand up her inner thigh, to just below her . . ."])
            $ TempFocus += 1 if Player.climax < 50 else 0
            $ TempLust += 1 if GirlA.lust < 50 else 0
        elif GirlA.wearing_skirt and GirlA.Clothes["hose"] in ["tights", "pantyhose"]:

            $ line = renpy.random.choice(["You reach under skirt and stroke her thighs",
                                        "You lift her skirt a bit and feel her firm thighs",
                                        "Her legs twitch a bit beneath her_skirt",
                                        "She gasps as you stroke her lightly covered thighs",
                                        "You slide a hand up her inner thigh, to just below her . . "])
            $ TempFocus += 2 if Player.climax < 40 else 0
            $ TempLust += 2 if GirlA.lust < 40 else 0
            $ GirlA.addiction -= 1 if D20S > 10 else 0
        elif GirlA.wearing_skirt and GirlA.Clothes["hose"]:

            $ line = renpy.random.choice(["You reach under skirt and stroke her thighs",
                                        "You lift her skirt a bit and feel her firm thighs",
                                        "Her legs twitch a bit beneath her_skirt",
                                        "She gasps as you stroke her warm thighs",
                                        "You slide a hand up her inner thigh, to just above the hose"])
            $ TempFocus += 2 if Player.climax < 50 else 0
            $ TempLust += 2 if GirlA.lust < 50 else 0
            $ GirlA.addiction -= 1 if D20S > 10 else 0
        elif GirlA.wearing_skirt:

            $ line = renpy.random.choice(["You reach under skirt and stroke her thighs",
                                        "You lift her skirt a bit and feel her firm thighs",
                                        "Her legs twitch a bit beneath her_skirt",
                                        "She gasps as you stroke her warm thighs",
                                        "You draw your hand from her knee to mid-thigh, and she gasps a little",
                                        "You slide a hand up her inner thigh, to just her_skirt"])
            $ TempFocus += 2 if Player.climax < 50 else 0
            $ TempLust += 2 if GirlA.lust < 50 else 0
            $ GirlA.addiction -= 2 if D20S > 10 else 1
        elif GirlA.Clothes["hose"] in ["tights", "pantyhose"]:

            $ line = renpy.random.choice(["You reach out and stroke her lightly covered thighs",
                                        "You lift her leg a bit and feel her firm thighs",
                                        "Her legs twitch a bit beneath your hands",
                                        "She gasps as you stroke her warm thighs",
                                        "You slide a hand up her inner thigh, the smooth faberic creasing",
                                        "You slide a hand up her inner thigh, to just below her. . "])
            $ TempFocus += 2 if Player.climax < 40 else 0
            $ TempLust += 2 if GirlA.lust < 40 else 0
            $ GirlA.addiction -= 1 if D20S > 10 else 0
        elif GirlA.Clothes["hose"]:

            $ line = renpy.random.choice(["You reach out and stroke her thighs",
                                        "You lift her leg a bit and feel her firm thighs",
                                        "Her legs twitch a bit beneath your hands",
                                        "She gasps as you stroke her warm thighs",
                                        "You slide a hand up her inner thigh, to just above the hose",
                                        "You slide a hand up her inner thigh, to just below her. . "])
            $ TempFocus += 2 if Player.climax < 50 else 0
            $ TempLust += 2 if GirlA.lust < 50 else 0
            $ GirlA.addiction -= 1 if D20S > 10 else 0
        else:
            $ line = renpy.random.choice(["You reach out and stroke her thighs",
                                        "You lift her leg a bit and feel her firm thighs",
                                        "Her legs twitch a bit beneath your hands",
                                        "She gasps as you stroke her warm thighs",
                                        "You draw your hand from her knee to mid-thigh, and she gasps a little",
                                        "You slide a hand up her inner thigh, to just below her. . "])
            $ TempFocus += 2 if Player.climax < 50 else 0
            $ TempLust += 2 if GirlA.lust < 50 else 0
            $ GirlA.addiction -= 2 if D20S > 10 else 1




    elif Player.primary_Action in ["fondle_pussy", "finger_pussy"]:
        if Player.primary_Action == "finger_pussy" and D20S <= 10:
            $ line = renpy.random.choice(["You continue to finger " + GirlA.name + "_'s pussy. ",
                                                    "You continue to finger bang " + GirlA.name + "_'s pussy. ",
                                                    "You continue to finger blast " + GirlA.name + "_'s pussy. "])

            if GirlA.wearing_pants and not GirlA.upskirt:

                $ line = renpy.random.choice(["You slide a hand down her pants, and slide your fingers into her pussy underneath",
                                                    "You push her panties aside, and slide a finger between her lips",
                                                    "You slide a finger into her pussy and stroke the_top",
                                                    "You pull her pants out a bit and she gasps as you slide two fingers between her lips",
                                                    "You rub her clit with your palm as you dive into her pussy with your middle finger"])
            elif GirlA.wearing_skirt:
                if GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"].state:

                    $ line = renpy.random.choice(["You push her skirt and " + GirlA.Clothes["underwear"] + " aside, and slide a finger between her lips",
                                                    "You slide a finger under her " + GirlA.Clothes["underwear"] + " and stroke the top or her pussy",
                                                    "You lift her skirt a bit and she gasps as you pull her " + GirlA.Clothes["underwear"] + " aside and slide two fingers between her lips",
                                                    "You rub her clit with your thumb as you dive into her pussy with your middle finger"])
                else:
                    $ line = renpy.random.choice(["You push her skirt aside, and slide a finger between her lips",
                                                    "You slide a finger into her pussy and stroke the_top",
                                                    "You lift her skirt a bit and she gasps as you slide two fingers between her lips",
                                                    "You rub her clit with your thumb as you dive into her pussy with your middle finger"])
                    $ TempFocus += 2
                    $ TempLust += 2

            elif (GirlA.wearing_shorts or (GirlA == RogueX and GirlA.Clothes["underwear"] == "shorts")) and not GirlA.Clothes["underwear"] and (GirlA.wearing_shorts or (GirlA == RogueX and GirlA.Clothes["underwear"] == "shorts")) and not GirlA.Clothes["underwear"].state:

                $ line = renpy.random.choice(["You slide a hand down her shorts, and slide your fingers into her pussy underneath",
                                                "You push her shorts up, and slide a finger between her lips",
                                                "You slide a finger along her pussy and stroke to the_top",
                                                "You pull her shorts out a bit and she gasps as you slide two fingers between her lips",
                                                "You rub her clit with your palm as you dive into her pussy with your middle finger"])
            elif GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"] and GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"].state:

                $ line = renpy.random.choice(["You push her panties aside, and slide a finger between her lips",
                                                "You slide a finger along her pussy and stroke to the_top",
                                                "You lift her panties a bit and she gasps as you slide two fingers between her lips"])
            else:
                $ line = renpy.random.choice(["You reach out and slide a finger between her lips",
                                                "You slide a finger along her pussy and stroke to the_top",
                                                "You lift her lips a bit and she gasps as you slide two fingers between them",
                                                "You rub her clit with your thumb as you dive into her pussy with your middle finger"])
                $ TempFocus += 2
                $ TempLust += 2

            $ TempFocus += 4 if Player.climax < 50 else 3
            $ TempLust += 6 if GirlA.lust > 40 else 3
            $ GirlA.addiction -= 2
        else:

            $ line = renpy.random.choice(["You continue to stroke " + GirlA.name + "_'s pussy. ",
                                                    "You continue to rub " + GirlA.name + "_'s pussy. ",
                                                    "You continue to caress " + GirlA.name + "_'s pussy. "])

            if GirlA.wearing_pants and not GirlA.upskirt:

                $ line = renpy.random.choice(["You reach out and brush your hands across her pussy through the_pants",
                                                    "You slide a hand down her pants, and brush your hands across her pussy underneath",
                                                    "You put your hand against her mound and grind against it",
                                                    "You reach into her gap and she gasps as you slide your hand across and stroke her warm mound",
                                                    "As you dig your thumb into her, she gasps and raises up a bit",
                                                    "She gasps as you reach under her and lightly stroke her ass through the_pants",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])

            elif GirlA.wearing_skirt:
                if GirlA.Clothes["underwear"] == "shorts" and not GirlA.Clothes["underwear"].state:

                    $ line = renpy.random.choice(["You reach under skirt and ran your hands over the thin shorts covering her",
                                                    "You slide a hand up the leg of her shorts, and brush your hands across her pussy underneath",
                                                    "You put your hand against her mound and grind against it",
                                                    "You reach into her gap and she gasps as you slide your hand across and stroke her warm mound",
                                                    "As you dig your thumb into her, she gasps and raises up a bit",
                                                    "She gasps as you reach under her and lightly stroke her ass through the thin_shorts",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                elif GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"] and GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"].state:
                    $ line = renpy.random.choice(["You reach under skirt and brush across her_panties",
                                                    "You lift her skirt a bit and grind against her_panties",
                                                    "You lift her skirt a bit and she gasps as you pull her panties aside and stroke her lips",
                                                    "Her legs twitch a bit beneath her skirt as you press your thumb against her",
                                                    "She gasps as you rub her pussy through her_panties",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                elif GirlA.Clothes["hose"] in ["tights", "pantyhose"]:

                    $ line = renpy.random.choice(["You reach out and brush your hands across her cleft through the thin fabric",
                                                    "You grab her hose and pull them taut, elliciting a small gasp",
                                                    "You put your hand against her mound and grind against it",
                                                    "You reach into her gap and she gasps as you slide your hand across and stroke her lips through the thin material",
                                                    "Her legs twitch a bit as you press your thumb against her",
                                                    "She gasps as you reach under her hose and lightly stroke her ass",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                else:
                    $ line = renpy.random.choice(["You reach under skirt and brush across her bare lips",
                                                    "You lift her skirt a bit and grind against her warm mound",
                                                    "You lift her skirt a bit and she gasps as you stroke her moist lips",
                                                    "Her legs twitch a bit beneath her skirt as you press your thumb against her"
                                                    "She gasps as you rub her bare pussy",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                    if D20S <= 10:
                        $ TempFocus += 3 if Player.climax < 50 else 1
                        $ TempLust += 4 if GirlA.lust > 40 else 2
                        $ GirlA.addiction -= 2
                    else:
                        $ TempFocus += 1
                        $ TempLust += 1


            elif (GirlA.wearing_shorts or (GirlA == RogueX and GirlA.Clothes["underwear"] == "shorts")) and not GirlA.Clothes["underwear"] and (GirlA.wearing_shorts or (GirlA == RogueX and GirlA.Clothes["underwear"] == "shorts")) and not GirlA.Clothes["underwear"].state:

                $ line = renpy.random.choice(["You reach out and brush your hands across her pussy through the_shorts",
                                                "You slide a hand down her shorts, and brush your hands across her pussy underneath",
                                                "You put your hand against her mound and grind against it",
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her warm mound",
                                                "As you dig your thumb into her, she gasps and raises up a bit",
                                                "She gasps as you reach under her and lightly stroke her ass through the thin_shorts",
                                                "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
            elif GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"] and GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"].state:

                $ line = renpy.random.choice(["You reach out and brush your hands across her_panties",
                                                "You grab her panties and pull them taut, elliciting a small gasp",
                                                "You put your hand against her mound and grind against it",
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her lips through the thin material",
                                                "Her legs twitch a bit as you press your thumb against her",
                                                "She gasps as you reach under her panties and lightly stroke her ass",
                                                "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
            elif GirlA.Clothes["hose"] in ["tights", "pantyhose"]:

                $ line = renpy.random.choice(["You reach out and brush your hands across her cleft through the thin fabric",
                                                "You grab her hose and pull them taut, elliciting a small gasp",
                                                "You put your hand against her mound and grind against it",
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her lips through the thin material",
                                                "Her legs twitch a bit as you press your thumb against her",
                                                "She gasps as you reach under her hose and lightly stroke her ass",
                                                "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
            else:
                $ line = renpy.random.choice(["You reach out and brush your hands across her bare lips",
                                                "You put your hand against her mound and grind against it",
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her lips",
                                                "Her legs twitch a bit as you press your thumb against her",
                                                "She gasps as you reach under her and lightly stroke her ass",
                                                "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                if D20S <= 10:
                    $ TempFocus += 3 if Player.climax < 50 else 1
                    $ TempLust += 4 if GirlA.lust > 40 else 2
                    $ GirlA.addiction -= 2
                else:
                    $ TempFocus += 1
                    $ TempLust += 1

            if D20S > 10:
                $ TempFocus += 3 if Player.climax < 50 else 1
                $ TempLust += 4 if GirlA.lust > 40 else 2
                $ GirlA.addiction -= 2
            else:
                $ TempFocus += 2 if Player.climax < 50 else 1
                $ TempLust += 2 if GirlA.lust > 40 else 1
            if GirlA.Clothes["piercings"] and D20S <= 3:
                "You tug on her piercing with your thumb, then let it snap back"





    elif Player.primary_Action == "eat_pussy":
        $ line = renpy.random.choice(["You continue to lick " + GirlA.name + "_'s pussy. ",
                                                    "You continue to suck " + GirlA.name + "_'s pussy. ",
                                                    "You continue to tongue " + GirlA.name + "_'s pussy. "])

        if GirlA.wearing_pants and not GirlA.upskirt:
            $ line = renpy.random.choice(["You can feel her twitching as you grind your tongue against her, even through the thick material",
                                                    "She gasps as you press on her clit through the thick fabric",
                                                    "You rub her clit with your nose as you dive into her pussy with your tongue",
                                                    "You put your hand against her mound and lick the surface of her_pants",
                                                    "With a little nibble, you tug at the denim",
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])
            $ TempFocus += 1 if Player.climax < 70 else 0
            $ TempLust += 3 if GirlA.lust > 60 else 2
        else:
            if GirlA.wearing_skirt:
                if GirlA.Clothes["underwear"] == "shorts" and not GirlA.Clothes["underwear"].state:

                    $ line = renpy.random.choice(["You push her skirt up and lick at her pussy through her_shorts",
                                                        "You bend down and lick the edges of her lips through the_shorts",
                                                        "You spread the lips back beneath her shorts, and she gasps as you slide your tongue across them",
                                                        "You can feel her twitching as you grind your tongue against her clit",
                                                        "She gasps as you suck on her clit through the thin fabric",
                                                        "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                        "You put your hand against her mound and lick the juice from her thin_shorts",
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the walls aside",
                                                        "She gasps as you reach under her warm lips and lightly stroke her ass"])
                elif GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"] and GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"].state:

                    $ line = renpy.random.choice(["You push her skirt up and lick at her pussy through her_panties",
                                                        "You bend down and stroke the edges of her panties with your tongue",
                                                        "You spread the lips back beneath her panties, and she gasps as you slide your tongue across them",
                                                        "You can feel her twitching as you grind your tongue against her clit",
                                                        "She gasps as you suck on her clit through the thin fabric",
                                                        "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                        "You put your hand against her mound and lick the juice from her thin_panties",
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the walls aside",
                                                        "She gasps as you reach under her warm lips and lightly stroke her ass"])
                elif GirlA.Clothes["hose"] in ["tights", "pantyhose"]:

                    $ line = renpy.random.choice(["You push her skirt up and lick at her pussy through her hose",
                                                        "You bend down and stroke the edges of her lips through the hose",
                                                        "You spread the lips back beneath her hose, and she gasps as you slide your tongue across them",
                                                        "You can feel her twitching as you grind your tongue against her clit",
                                                        "She gasps as you suck on her clit through the thin fabric",
                                                        "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                        "You put your hand against her mound and lick the juice from her thin hose",
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the walls aside",
                                                        "She gasps as you reach under her warm lips and lightly stroke her ass"])
                else:
                    $ line = renpy.random.choice(["You push her skirt aside and stroke her lips with your tongue",
                                                        "You slide your tongue into her pussy and flick the roof with deft strokes",
                                                        "You spread the lips back and she gasps as you slide your tongue between them",
                                                        "You can feel her twitching as you grind your tongue against her clit",
                                                        "She gasps as you suck on her clit",
                                                        "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                        "You put your hand against her mound and lick around her lips",
                                                        "With a little nibble, you tug on her lower lips",
                                                        "You slowly lick into her gap and she gasps as you press the walls aside",
                                                        "She gasps as you reach under her warm lips and lightly stroke her ass"])
                    if D20S <= 10:
                        $ TempFocus += 3 if Player.climax < 70 else 1
                        $ TempLust += 4 if GirlA.lust > 60 else 2
                        $ GirlA.addiction -= 3
                    else:
                        $ TempFocus += 1
                        $ TempLust += 1


            elif (GirlA.wearing_shorts or (GirlA == RogueX and GirlA.Clothes["underwear"] == "shorts")) and not GirlA.Clothes["underwear"] and (GirlA.wearing_shorts or (GirlA == RogueX and GirlA.Clothes["underwear"] == "shorts")) and not GirlA.Clothes["underwear"].state:

                $ line = renpy.random.choice(["You bend down and lick the edges of her lips through her_shorts",
                                                    "You spread the lips back beneath her shorts, and she gasps as you slide your tongue across them",
                                                    "You can feel her twitching as you grind your tongue against her clit",
                                                    "She gasps as you suck on her clit through the thin fabric",
                                                    "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                    "You put your hand against her mound and lick the juice from her thin_shorts",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the walls aside",
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])
            elif GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"] and GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"].state:

                $ line = renpy.random.choice(["You bend down and stroke the edges of her panties with your tongue",
                                                    "You spread the lips back beneath her panties, and she gasps as you slide your tongue across them",
                                                    "You can feel her twitching as you grind your tongue against her clit",
                                                    "She gasps as you suck on her clit through the thin fabric",
                                                    "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                    "You put your hand against her mound and lick the juice from her thin_panties",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the walls aside",
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])
            elif GirlA.Clothes["hose"] in ["tights", "pantyhose"]:

                $ line = renpy.random.choice(["You bend down and stroke her lips with your tongue",
                                                    "You spread the lips back beneath her hose, and she gasps as you slide your tongue across them",
                                                    "You can feel her twitching as you grind your tongue against her clit",
                                                    "She gasps as you suck on her clit through the thin fabric",
                                                    "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                    "You put your hand against her mound and lick the juice from her thin hose",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the walls aside",
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])
            else:
                $ line = renpy.random.choice(["You bend down and stroke her lips with your tongue",
                                                    "You slide your tongue into her pussy and flick the roof with deft strokes",
                                                    "You spread the lips back and she gasps as you slide your tongue between them",
                                                    "You can feel her twitching as you grind your tongue against her clit",
                                                    "She gasps as you suck on her clit",
                                                    "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                    "You put your hand against her mound and lick around her lips",
                                                    "With a little nibble, you tug on her lower lips",
                                                    "You slowly lick into her gap and she gasps as you press the walls aside",
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])
                if D20S <= 10:
                    $ TempFocus += 3 if Player.climax < 70 else 1
                    $ TempLust += 4 if GirlA.lust > 60 else 2
                    $ GirlA.addiction -= 3
                else:
                    $ TempFocus += 1
                    $ TempLust += 1

            if D20S > 10:
                $ TempFocus += 4 if Player.climax < 70 else 1
                $ TempLust += 10 if GirlA.lust > 60 else 5
                $ GirlA.addiction -= 3
            else:
                $ TempFocus += 2 if Player.climax < 50 else 1
                $ TempLust += 5 if GirlA.lust > 60 else 3
            if GirlA.Clothes["piercings"] and D20S <= 3:
                "You tug on her piercing with your teeth, then let it snap back"



    elif Player.primary_Action == "fondle_ass":
        $ line = renpy.random.choice(["You continue to fondle " + GirlA.name + "_'s ass. ",
                                                "You continue to feel up " + GirlA.name + "_'s ass. ",
                                                "You continue to grope " + GirlA.name + "_'s ass. "])

        if GirlA.wearing_pants and not GirlA.upskirt:
            $ line = renpy.random.choice(["You reach out and brush your hands across the back of her_pants",
                                                "You slide a hand down her pants, and firmly cup her ass",
                                                "You put your hand against her rear and grind against it",
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her warm mound",
                                                "As you dig your thumb into her, she gasps and raises up a bit",
                                                "She gasps as you reach under her and lightly stroke her ass through the_pants",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])

        elif GirlA.wearing_skirt:

            if GirlA.Clothes["underwear"] == "shorts" and not GirlA.Clothes["underwear"].state:

                $ line = renpy.random.choice(["You reach under skirt and brush across her_shorts",
                                                "You lift her skirt a bit and grind against her_shorts",
                                                "You lift her skirt a bit and she gasps as you pull her shorts aside and stroke across her butt",
                                                "Her legs twitch a bit beneath her skirt as you give her cheeks a firm squeeze",
                                                "She gasps as you stroke her asshole through her_shorts",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
            elif GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"] and GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"].state:

                $ line = renpy.random.choice(["You reach under skirt and brush across her_panties",
                                                "You lift her skirt a bit and grind against her_panties",
                                                "You lift her skirt a bit and she gasps as you pull her panties aside and stroke across her butt",
                                                "Her legs twitch a bit beneath her skirt as you give her cheeks a firm squeeze",
                                                "She gasps as you stroke her asshole through her_panties",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
            elif GirlA.Clothes["hose"] in ["tights", "pantyhose"]:

                $ line = renpy.random.choice(["You reach under skirt and brush across her hose",
                                                "You lift her skirt a bit and grind against her hose",
                                                "You lift her skirt a bit and she gasps as you pull her hose aside and stroke across her butt",
                                                "Her legs twitch a bit beneath her skirt as you give her cheeks a firm squeeze",
                                                "She gasps as you stroke her asshole through her hose",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
            else:
                $ line = renpy.random.choice(["You reach under skirt and brush across her bare ass",
                                                "You lift her skirt a bit and grind against her warm cheeks",
                                                "You lift her skirt a bit and she gasps as you stroke asshole",
                                                "Her legs twitch a bit beneath her skirt as you press your thumb against her firm rear",
                                                "She gasps as you rub her bare hole",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
                if D20S <= 10:
                    $ TempFocus += 2 if Player.climax < 50 else 1
                    $ TempLust += 3 if GirlA.lust > 40 else 2
                    $ GirlA.addiction -= 1
                else:
                    $ TempFocus += 1
                    $ TempLust += 1


        elif (GirlA.wearing_shorts or (GirlA == RogueX and GirlA.Clothes["underwear"] == "shorts")) and not GirlA.Clothes["underwear"] and (GirlA.wearing_shorts or (GirlA == RogueX and GirlA.Clothes["underwear"] == "shorts")) and not GirlA.Clothes["underwear"].state:

            $ line = renpy.random.choice(["You reach out and brush your hands across her lightly covered cheeks",
                                            "You grab her shorts and pull them taut, elliciting a small gasp",
                                            "You reach into her gap and she gasps as you slide your hand across and stroke her hole through the thin material",
                                            "Her legs twitch a bit as you grind her puckered hole",
                                            "She gasps as you reach under her shorts and lightly stroke her warm flesh",
                                            "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
        elif GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"] and GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"].state:

            $ line = renpy.random.choice(["You reach out and brush your hands across her barely covered cheeks",
                                            "You grab her panties and pull them taut, elliciting a small gasp",
                                            "You reach into her gap and she gasps as you slide your hand across and stroke her hole through the thin material",
                                            "Her legs twitch a bit as you grind her puckered hole",
                                            "She gasps as you reach under her panties and lightly stroke her warm flesh",
                                            "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
        elif GirlA.Clothes["hose"] in ["tights", "pantyhose"]:

            $ line = renpy.random.choice(["You reach out and brush your hands across her barely covered cheeks",
                                            "You grab her hose and pull them taut, elliciting a small gasp",
                                            "You reach into her gap and she gasps as you slide your hand across and stroke her hole through the thin material",
                                            "Her legs twitch a bit as you grind her puckered hole",
                                            "She gasps as you reach under her hose and lightly stroke her warm flesh",
                                            "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
        else:
            $ line = renpy.random.choice(["You reach out and brush your hands across her bare ass",
                                            "You put your hand against her firm rear and grind against it",
                                            "You reach into her gap and she gasps as you slide your hand across and stroke her puckered hole",
                                            "Her legs twitch a bit as you press your thumb against her",
                                            "She gasps as you reach under her and lightly stroke her ass",
                                            "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
            if D20S <= 10:
                $ TempFocus += 2 if Player.climax < 50 else 1
                $ TempLust += 3 if GirlA.lust > 40 else 2
                $ GirlA.addiction -= 1
            else:
                $ TempFocus += 1
                $ TempLust += 1

        if D20S > 10:
            $ TempFocus += 2 if Player.climax < 50 else 1
            $ TempLust += 3 if GirlA.lust > 40 else 2
            $ GirlA.addiction -= 1
        else:
            $ TempFocus += 2 if Player.climax < 50 else 1
            $ TempLust += 2 if GirlA.lust > 40 else 1



    elif Player.primary_Action == "finger_ass":
        $ line = renpy.random.choice(["You continue to finger " + GirlA.name + "_'s asshole. ",
                                                    "You continue to finger bang " + GirlA.name + "_'s asshole. ",
                                                    "You continue to finger " + GirlA.name + "_'s rim. "])

        if GirlA.wearing_pants and not GirlA.upskirt:
            $ line = renpy.random.choice(["You slide a hand down her pants, and slide your fingers into her anus",
                                                    "You push her panties aside, and slide a finger between her cheeks",
                                                    "You slide a finger into her tight anus",
                                                    "You pull her pants out a bit and she gasps as you slide a finger up her hole",
                                                    "You gasps as you rub her asshole with your fingers"])
        elif GirlA.wearing_skirt:
            if GirlA.Clothes["underwear"] == "shorts" and not GirlA.Clothes["underwear"].state:

                $ line = renpy.random.choice(["You push her skirt and shorts up, and slide a finger into her anus",
                                                    "You slide a finger into her tight anus",
                                                    "You lift her skirt a bit and she gasps as you pull her shorts up and slide a finger into her anus",
                                                    "You rub her pussy with your thumb as you dive into her anus with your middle finger"])
            elif GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"] and GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"].state:

                $ line = renpy.random.choice(["You push her skirt and panties aside, and slide a finger into her anus",
                                                    "You slide a finger into her tight anus",
                                                    "You lift her skirt a bit and she gasps as you pull her panties aside and slide a finger into her anus",
                                                    "You rub her clit with your thumb as you dive into her pussy with your middle finger"])
            else:
                $ line = renpy.random.choice(["You push her skirt aside, and slide a finger into her anus",
                                                    "You slide a finger into her tight anus",
                                                    "You lift her skirt a bit and she gasps as you slide a finger into her anus",
                                                    "You rub her pussy with your thumb as you dive into her anus with your middle finger"])

        elif (GirlA.wearing_shorts or (GirlA == RogueX and GirlA.Clothes["underwear"] == "shorts")) and not GirlA.Clothes["underwear"] and (GirlA.wearing_shorts or (GirlA == RogueX and GirlA.Clothes["underwear"] == "shorts")) and not GirlA.Clothes["underwear"].state:

            $ line = renpy.random.choice(["You slide a hand down her shorts, and slide a finger into her anus",
                                                "You push her shorts up, and slide a finger between her lips",
                                                "You slide a finger into her tight anus",
                                                "You pull her shorts out a bit and she gasps as you slide a finger into her anus",
                                                "You rub her pussy with your palm as you dive into her anus with your middle finger"])
        elif GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"] and GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"].state:

            $ line = renpy.random.choice(["You push her panties aside, and slide a finger into her anus",
                                                "You slide a finger into her tight anus",
                                                "You lift her panties a bit and she gasps as you and slide a finger into her anus"])
        else:
            $ line = renpy.random.choice(["You reach out and slide a finger into her anus",
                                                "You slide a finger into her tight anus",
                                                "You press into her and she gasps as you  slide a finger into her anus",
                                                "You rub her pussy with your thumb as you dive into her anus with your middle finger"])

        $ TempFocus += 2 if Player.climax < 50 else 1
        $ TempLust += 6 if GirlA.lust > 70 else 3
        if not GirlA.used_to_anal:
            $ TempLust -= 3
        elif GirlA.used_to_anal < 2:
            $ TempLust += 1

        $ GirlA.addiction -= 2



    elif Player.primary_Action == "eat_ass":
        $ line = renpy.random.choice(["You continue to lick " + GirlA.name + "_'s ass. ",
                                                    "You continue to suck " + GirlA.name + "_'s ass. ",
                                                    "You continue to tongue " + GirlA.name + "_'s ass. "])

        if GirlA.wearing_pants and not GirlA.upskirt:
            $ line = renpy.random.choice(["You can feel her twitching as you grind your tongue against her anus, even through the thick material",
                                                        "She gasps as you press on her asshole through the thick fabric",
                                                        "You put your hand against her mound and lick the surface of her_pants",
                                                        "With a little nibble, you tug at the denim"])
            $ TempFocus += 1 if Player.climax < 70 else 0
            $ TempLust += 1 if GirlA.lust < 60 else 0
        else:
            if GirlA.wearing_skirt:
                if GirlA.Clothes["underwear"] == "shorts" and not GirlA.Clothes["underwear"].state:

                    $ line = renpy.random.choice(["You push her skirt up and lick at her asshole through her_shorts",
                                                        "You bend down and stroke the edges of her shorts with your tongue",
                                                        "You spread the cheeks back beneath her shorts, and she gasps as you slide your tongue into it",
                                                        "You can feel her twitching as you grind your tongue against her anus",
                                                        "She gasps as you suck on her asshole through the thin fabric",
                                                        "You rub her pussy with your thumb as you dive into her asshole with your tongue",
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the rim aside"])
                elif GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"] and GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"].state:

                    $ line = renpy.random.choice(["You push her skirt up and lick at her asshole through her_panties",
                                                        "You bend down and stroke the edges of her panties with your tongue",
                                                        "You spread the cheeks back beneath her panties, and she gasps as you slide your tongue into it",
                                                        "You can feel her twitching as you grind your tongue against her anus",
                                                        "She gasps as you suck on her asshole through the thin fabric",
                                                        "You rub her pussy with your thumb as you dive into her asshole with your tongue",
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the rim aside"])
                elif GirlA.Clothes["hose"] in ["tights", "pantyhose"]:

                    $ line = renpy.random.choice(["You push her skirt up and lick at her asshole through her hose",
                                                        "You bend down and stroke the edges of her hose with your tongue",
                                                        "You spread the cheeks back beneath her hose, and she gasps as you slide your tongue into it",
                                                        "You can feel her twitching as you grind your tongue against her anus",
                                                        "She gasps as you suck on her asshole through the thin fabric",
                                                        "You rub her pussy with your thumb as you dive into her asshole with your tongue",
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the rim aside"])
                else:
                    $ line = renpy.random.choice(["You push her skirt aside and stroke her asshole with your tongue",
                                                        "You spread the cheeks back, and she gasps as you slide your tongue into it",
                                                        "You can feel her twitching as you grind your tongue against her asshole",
                                                        "She gasps as you suck on her anus",
                                                        "You rub her pussy with your thumb as you dive into her asshole with your tongue",
                                                        "You put your hand against her mound and lick around her rim",
                                                        "You slowly lick into her gap and she gasps as you press the rim apart"])
                    if D20S <= 10:
                        $ TempFocus += 2 if Player.climax < 70 else 0
                        $ TempLust += 3 if GirlA.lust > 60 else 1
                        $ GirlA.addiction -= 3
                    else:
                        $ TempFocus += 1
                        $ TempLust += 1


            elif (GirlA.wearing_shorts or (GirlA == RogueX and GirlA.Clothes["underwear"] == "shorts")) and not GirlA.Clothes["underwear"] and (GirlA.wearing_shorts or (GirlA == RogueX and GirlA.Clothes["underwear"] == "shorts")) and not GirlA.Clothes["underwear"].state:

                $ line = renpy.random.choice(["You bend down and stroke the edges of her shorts with your tongue",
                                                    "You spread the cheeks back beneath her shorts, and she gasps as you slide your tongue into it",
                                                    "You can feel her twitching as you grind your tongue against her anus",
                                                    "She gasps as you suck on her anus through the thin fabric",
                                                    "You rub her pussy with your thumb as you dive into her anus with your tongue",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the rim apart"])
            elif GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"] and GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"].state:

                $ line = renpy.random.choice(["You bend down and stroke the edges of her panties with your tongue",
                                                    "You spread the cheeks back beneath her panties, and she gasps as you slide your tongue into it",
                                                    "You can feel her twitching as you grind your tongue against her anus",
                                                    "She gasps as you suck on her anus through the thin fabric",
                                                    "You rub her pussy with your thumb as you dive into her anus with your tongue",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the rim apart"])
            elif GirlA.Clothes["hose"] in ["tights", "pantyhose"]:

                $ line = renpy.random.choice(["You bend down and stroke the edges of her hose with your tongue",
                                                    "You spread the cheeks back beneath her hose, and she gasps as you slide your tongue into it",
                                                    "You can feel her twitching as you grind your tongue against her anus",
                                                    "She gasps as you suck on her anus through the thin fabric",
                                                    "You rub her pussy with your thumb as you dive into her anus with your tongue",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the rim apart"])
            else:
                $ line = renpy.random.choice(["You bend down and stroke her rim with your tongue",
                                                    "You slide your tongue into her asshole and flick the roof with deft strokes",
                                                    "You spread the cheeks back, and she gasps as you slide your tongue into it",
                                                    "You can feel her twitching as you grind your tongue against her rim",
                                                    "She gasps as you suck on her hole",
                                                    "You rub her clit with your thumb as you dive into her asshole with your tongue",
                                                    "You knead her cheeks and lick around her rim",
                                                    "With a little nibble, you toss her salad",
                                                    "You slowly lick into her gap and she gasps as you press the walls aside",
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])
                if D20S <= 10:
                    $ TempFocus += 2 if Player.climax < 70 else 0
                    $ TempLust += 3 if GirlA.lust > 60 else 1
                    $ GirlA.addiction -= 3
                else:
                    $ TempFocus += 1
                    $ TempLust += 1

            if D20S > 10:
                $ TempFocus += 3 if Player.climax < 70 else 0
                $ TempLust += 9 if GirlA.lust > 60 else 4
                $ GirlA.addiction -= 3
            else:
                $ TempFocus += 1 if Player.climax < 50 else 0
                $ TempLust += 4 if GirlA.lust > 60 else 2

        $ TempLust += 2 if GirlA.used_to_anal > 1 else 0



    elif Player.primary_Action == "dildo_pussy":
        if GirlA.wearing_pants and not GirlA.upskirt:
            $ line = renpy.random.choice(["You rub the dildo against the outside of her_pants",
                                        "You slap the dildo lightly against her mound"])
            $ TempFocus += 1 if Player.climax < 50 else 0
            $ TempLust += 3 if GirlA.lust < 50 else 1
        elif GirlA.hose_number() >= 10:
            $ line = renpy.random.choice(["You rub the dildo against the outside of her_tights",
                                        "You slap the dildo lightly at the outside of her_tights"])
            $ TempFocus += 1 if Player.climax < 50 else 0
            $ TempLust += 3 if GirlA.lust < 50 else 1
        elif GirlA.Clothes["hose"] in ["tights", "pantyhose"]:
            $ line = renpy.random.choice(["You rub the dildo against the outside of her hose",
                                        "You slap the dildo lightly at the outside of her hose"])
            $ TempFocus += 1 if Player.climax < 50 else 0
            $ TempLust += 3 if GirlA.lust < 50 else 1
        else:
            if GirlA.wearing_skirt and GirlA.Clothes["underwear"]:
                $ line = renpy.random.choice(["You push her skirt and panties aside, and slide the dildo into her pussy",
                                            "You slide the toy deep into her pussy",
                                            "She gasps as you rotate the dildo within her tight pussy",
                                            "You rub her clit with your thumb as you dive into her puss with the rubber phallus"])
                $ TempFocus += 2 if Player.climax < 50 else 1
                $ TempLust += 8 if GirlA.lust > 70 else 5
            elif GirlA.wearing_skirt:
                $ line = renpy.random.choice(["You push her skirt aside, and slide the dildo into her tight hole",
                                            "You slide the toy deep into her pussy",
                                            "You lift her skirt a bit and she gasps as you slide the dildo firmly into her tight puss",
                                            "She gasps as you rotate the dildo within her slit",
                                            "You rub her clit with your thumb as you dive into her pussy with the rubber phallus"])
                $ TempFocus += 2 if Player.climax < 50 else 1
                $ TempLust += 8 if GirlA.lust > 70 else 5
            elif GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"] and GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"].state:
                $ line = renpy.random.choice(["You push her panties aside, and slide the dildo into her tight pussy",
                                            "You slide the dildo into her moist slit and stroke it rapidly",
                                            "You lift her panties a bit and she gasps as you slide the dildo between her lower lips",
                                            "She gasps as you rub her tight pussy with the toy",
                                            "You rub her clit with your thumb as you dive into her pussy with the dildo",
                                            "You reach into her gap and she gasps as you slide the dildo in and press against her tight slit through the thin material"])
                $ TempFocus += 2 if Player.climax < 50 else 1
                $ TempLust += 8 if GirlA.lust > 70 else 5
            else:
                $ line = renpy.random.choice(["You reach out and slide the dildo along her mound",
                                            "You slide the toy into her pussy and stroke it slowly",
                                            "You pull her lips apart and she gasps as you slide the dildo between them",
                                            "You can feel her twitching as you press your thumb against her clit",
                                            "She gasps as you rub her clit with the hard rubber",
                                            "You rub her clit with your thumb as you dive into her pussy with the dildo",
                                            "You reach into her gap and she gasps as you slide the toy across and press it into her wet pussy"])
                $ TempFocus += 3 if Player.climax < 50 else 1
                $ TempLust += 10 if GirlA.lust > 70 else 8


    elif Player.primary_Action == "dildo_ass":
        if GirlA.wearing_pants and not GirlA.upskirt:
            $ line = renpy.random.choice(["You rub the dildo against the outside of her_pants",
                                        "You slap the dildo lightly against her ass"])
            $ TempFocus += 1 if Player.climax < 50 else 0
            $ TempLust += 3 if GirlA.lust < 50 else 1
        elif GirlA.hose_number() >= 10:
            $ line = renpy.random.choice(["You rub the dildo against the outside of her_tights",
                                        "You slap the dildo lightly at the outside of her_tights"])
            $ TempFocus += 1 if Player.climax < 50 else 0
            $ TempLust += 3 if GirlA.lust < 50 else 1
        elif GirlA.Clothes["hose"] in ["tights", "pantyhose"]:
            $ line = renpy.random.choice(["You rub the dildo against the outside of her hose",
                                        "You slap the dildo lightly at the outside of her hose"])
            $ TempFocus += 1 if Player.climax < 50 else 0
            $ TempLust += 3 if GirlA.lust < 50 else 1
        else:
            if GirlA.wearing_skirt and GirlA.Clothes["underwear"]:
                $ line = renpy.random.choice(["You push her skirt and panties aside, and slide the dildo into her ass",
                                            "You slide the toy deep into her ass",
                                            "She gasps as you rotate the dildo within her tight asshole",
                                            "You rub her clit with your thumb as you dive into her ass with the rubber phallus"])
                $ TempFocus += 2 if Player.climax < 50 else 1
                $ TempLust += 8 if GirlA.lust > 70 else 5
            elif GirlA.wearing_skirt:
                $ line = renpy.random.choice(["You push her skirt aside, and slide the dildo into her tight hole",
                                            "You slide the toy deep into her ass",
                                            "You lift her skirt a bit and she gasps as you slide the dildo firmly into her tight anus",
                                            "She gasps as you rotate the dildo within her ass",
                                            "You rub her clit with your thumb as you dive into her ass with the rubber phallus"])
                $ TempFocus += 2 if Player.climax < 50 else 1
                $ TempLust += 8 if GirlA.lust > 70 else 5
            elif GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"] and GirlA.Clothes["underwear"] and not GirlA.Clothes["underwear"].state:
                $ line = renpy.random.choice(["You push her panties aside, and slide the dildo into her tight ass",
                                            "You slide the dildo into her ass and stroke it rapidly",
                                            "You lift her panties a bit and she gasps as you slide the dildo between her cheeks",
                                            "She gasps as you rub her tight asshole with the toy",
                                            "You rub her clit with your thumb as you dive into her asshole with the dildo",
                                            "You reach into her gap and she gasps as you slide the dildo in and press against her tight anus through the thin material"])
                $ TempFocus += 2 if Player.climax < 50 else 1
                $ TempLust += 8 if GirlA.lust > 70 else 5
            else:
                $ line = renpy.random.choice(["You reach out and slide the dildo between her cheeks",
                                            "You slide the toy into her asshole and stroke it against the sides",
                                            "You pull her cheeks apart and she gasps as you slide the dildo between them",
                                            "You can feel her twitching as you press your thumb against her anus",
                                            "She gasps as you rub her anus with the hard rubber",
                                            "You rub her clit with your thumb as you dive into her asshole with the dildo",
                                            "You reach into her gap and she gasps as you slide the toy across and press it into her firm anus"])
                $ TempFocus += 3 if Player.climax < 50 else 1
                $ TempLust += 10 if GirlA.lust > 70 else 6
            if not GirlA.used_to_anal:
                $ TempLust -= 3
            elif GirlA.used_to_anal < 2:
                $ TempLust += 1


    elif girl_secondary_Action == "fondle_pussy":
        call Girl_Self_lines (GirlA)
        if "unseen" not in GirlA.recent_history:
            if Player.secondary_Action == "jerking_off" or "cockout" in Player.recent_history:
                $ TempLust += 2



    elif Player.primary_Action == "lesbian":
        call SexDialog_Threeway (GirlA, "lesbian", GirlB=Partner)

    elif Player.primary_Action == "footjob":
        $ line = GirlA.name + " continues stroke your cock with her feet. "

        if not action_speed:
            if GirlA.permanent_History["footjob"] > 2:
                $ line = line + "_She just seems to be enjoying the feel of it"
                $ TempLust += 2 if GirlA.lust < 60 else 0
            else:
                $ line = line + "_She just seems to be looking it over"
                $ TempLust += 2 if GirlA.lust < 40 else 0
                $ TempFocus += -3 if Player.climax > 50 else 2

            $ GirlA.addiction -= 1 if D20S > 10 else 2
            return

        if GirlA.permanent_History["footjob"] > 4:
            if action_speed <= 1:
                $ line = line + renpy.random.choice(["Her movements have become almost masterful, her slightest touch starts you twitching",
                                                "She slowly caresses you in a way that makes your blood boil, then pulls back at the last second",
                                                "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                                "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                                "You can't tell where she is at any moment, all you know is that it works"])

                $ TempFocus += 20 if Player.climax > 70 else 5
            else:

                $ line = line + renpy.random.choice(["Her movements have become almost masterful, her slightest touch starts you twitching",
                                                "Her expert strokes will have you boiling over in seconds",
                                                "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                                "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                                "You can't tell where she is at any moment, all you know is that it works"])

                $ TempFocus += 20 if Player.climax < 40 else 5

        elif GirlA.permanent_History["footjob"] >= 3:
            if action_speed <= 1:
                $ line = line + renpy.random.choice(["She's begining to figure things out, her toes cause tingles as they caress the shaft",
                                                "She's still learning, but learning fast",
                                                "She has a smooth motion going now, gentle and precise",
                                                "Her lessons are paying off, she's really becoming very talented at this",
                                                "She gently caresses the shaft, and brushes the balls in her other foot, giving them a light massage"])

                $ TempFocus += 15 if Player.climax > 60 else 5
            else:

                $ line = line + renpy.random.choice(["She's begining to figure things out, her toes cause tingles as they caress the shaft",
                                                "She's still learning, but learning fast",
                                                "Her feet glide smoothly across your cock",
                                                "She has a smooth motion going now, gentle and precise",
                                                "Her lessons are paying off, she's really becoming very talented at this",
                                                "She quickly strokes your cock, with a very deft pressure"])

                $ TempFocus += 15 if Player.climax < 60 else 7
        else:

            if action_speed <= 1:
                $ line = line + renpy.random.choice(["She makes up for her inexperience with determination, carefully stroking your cock",
                                            "She moves her feet up and down the shaft. She's a little rough at this, but at least she tries",
                                            "She strokes you gently. She isn't quite sure what to do with the balls",
                                            "Her toes fumble with your shaft a bit",
                                            "She nudges one of your balls too tightly, but stops when you wince",
                                            "She has a firm grip, and she's not letting go. This may take a few tries"])

                $ TempFocus += 10 if Player.climax > 60 else 5
            else:
                $ line = line + renpy.random.choice(["She really wasn't prepared for speeding up, and your cock often slips between her feet",
                                            "She rapidly moves her feet up and down the shaft. She's a little rough at this, but at least she tries",
                                            "She strokes you a bit too quickly, the friction is a bit uncomfortable",
                                            "Her toes fumble with your shaft a bit",
                                            "She nudges one of your balls too tightly, but stops when you wince",
                                            "She has a firm grip, and she's not letting go. This train is out of control"])

                $ TempFocus += 8 if Player.climax > 60 else 2

        $ TempLust += 2 if GirlA.lust < 60 else 0
        $ TempLust += 3 if GirlA.permanent_History["footjob"] > 2 else 0
        $ GirlA.addiction -= 1



    elif Player.primary_Action == "psy":
        $ line = GirlA.name + " continues work your cock. "

        if not action_speed:
            $ line = GirlA.name + "_'s construct just rests on your cock. "
            if GirlA.permanent_History["handjob"] > 2:
                $ line = line + "_She seems to be enjoying your reaction"
                $ TempLust += 2 if GirlA.lust < 60 else 0
            else:
                $ line = line + "_She just seems to be looking it over"
                $ TempLust += 2 if GirlA.lust < 40 else 0
                $ TempFocus += -3 if Player.climax > 50 else 2
            return

        if psychic == "handjob" or not psychic:

            $ line = line + renpy.random.choice(["Her movements are masterful, her slightest touch starts you twitching",
                                    "She's something of an expert, you feel a light tingle in your shaft",
                                    "She slowly caresses you in a way that makes your blood boil, then pulls back at the last second",
                                    "She really knows what to do, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                    "You can't tell where she is at any moment, all you know is that it works"])
            if action_speed <= 1:

                $ TempFocus += 15 if Player.climax > 60 else 5
            else:
                $ TempFocus += 15 if Player.climax < 60 else 7
            $ TempLust += 2 if GirlA.lust < 60 else 0
        elif psychic == "mouth":
            $ line = line + renpy.random.choice(["She masterfully bobs on your cock, and it twitches with each stroke",
                                "She smoothly bobs up and down on your cock, a frenzy of motion",
                                "She gobbles you up all the way to the base, then quickly draws out and plunges back in",
                                "She's really getting good at this, alternating between deep suction and quick licks across the head",
                                "She moves very smoothly, bobbing in and out like she's been doing this for years",
                                "She puts the shaft into her mouth and her tounge swirls rapidly around it"])
            $ TempFocus += 22 if Player.climax > 40 else 10
            $ TempLust += 3 if GirlA.lust > 60 else 1
        elif psychic == "tits":
            $ line = renpy.random.choice([GirlA.name + " juggles her breast projections up and down around your cock",
                                GirlA.name + " lightly strokes the head as it pops up between her tits",
                                GirlA.name + " has a smooth motion going now, gentle and precise",
                                GirlA.name + " pauses to rub her nipples across the shaft",
                                GirlA.name + " gently caresses the shaft between her tits"])
            $ TempFocus += 15 if Player.climax < 60 else 5
            $ TempLust += 6 if GirlA.lust > 60 else 3
        elif psychic == "sex" or psychic == "anal":

            $ line = line + renpy.random.choice(["It bounces rapidly against your cock",
                            "You thrust into it and she squeaks a bit",
                            "You quickly grind back and forth inside it",
                            "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                            "You pound away at it",
                            "She grinds it furiously back and forth along your cock"])
            $ TempFocus += 12 if Player.climax > 60 else 8
            $ TempLust += 12 if GirlA.lust > 80 else 6




    elif Player.primary_Action == "kiss":
        $ GirlA.addiction -= 3
        $ GirlA.addiction -= 3 if GirlA == JubesX else 0
        if GirlA.permanent_History["kiss"] > 10 and GirlA.love >= 700:
            $ line = renpy.random.choice(["She hungrily presses her lips against yours",
                                        "She confidently presses her lips against yours",
                                        "Her lips part as you hold her close",
                                        "You nibble her neck as she groans in pleasure",
                                        "You squeeze her tightly as your tongues jostle",
                                        "Her tongue dances around yours",
                                        "She nibbles your ear as her hands slide across your back",
                                        "Your hands slide down her body as your lips press hers"])
            $ TempFocus += 1 if Player.climax < 50 else 0
            $ TempFocus += 1 if Player.climax < 90 else 0
            $ TempLust += 3 if GirlA.lust < 50 else 0
            $ TempLust += 1 if GirlA.lust < 90 else 0
        elif GirlA.permanent_History["kiss"] > 5 or GirlA == EmmaX:
            $ line = renpy.random.choice(["She confidently presses her lips against yours",
                                        "You softly kiss her plump lips",
                                        "Her lips part as you hold her close",
                                        "You nibble her neck as she coos in pleasure",
                                        "You squeeze her tightly as your lips connect",
                                        "Her tongue flickers out to meet yours",
                                        "Your hands slide down her body as your lips brush hers"])
            $ TempFocus += 1 if Player.climax < 70 else 0
            $ TempLust += 3 if GirlA.lust < 50 else 0
            $ TempLust += 1 if GirlA.lust < 90 else 0
        else:
            $ line = renpy.random.choice(["She tentatively presses her lips against yours",
                                        "You softly kiss her plump lips",
                                        "Her lips part slightly as you hold her close",
                                        "You squeeze her tightly as your lips connect",
                                        "Your hands slide down her body as your lips brush hers"])
            $ TempFocus += 1 if Player.climax < 70 else 0
            $ TempLust += 2 if GirlA.lust < 30 else 0
            $ TempLust += 1 if GirlA.lust < 70 else 0
    else:


        "No trigger was set, or it was '[Player.primary_Action]'. Please tell Oni what happend up to this point."
        $ line = "Huh."

    $ line = line + "_."

    $ PrimaryLust += TempLust
    $ SecondaryLust += TempLust2 + 2

    return







label Offhand_Dialog(Girl=Primary, Templine=0):


    if Girl not in all_Girls:
        return
    if not Player.secondary_Action:
        return

    $ D20X = renpy.random.randint(1, 20)

    if Player.secondary_Action == "kiss":
        $ line = renpy.random.choice([" Your lips gently slide across hers.",
                        " Her lips part as you hold her close.",
                        " You nibble her neck as she groans in pleasure.",
                        " You squeeze her tightly as your tongues jostle.",
                        " Her tongue dances around yours.",
                        " She nibbles your ear as her hands slide across your back.",
                        " Your hands slide down her body as your lips press hers.",
                        " You kiss her passionately.",
                        " Your tongues swirl around each other's."])
        if Girl.love >= 300:
            call change_Girl_stat(Girl, "love", 1)
        $ PrimaryLust += 2 if Girl.lust < 50 else 1

    elif Player.secondary_Action == "fondle_breasts":
        if Girl == EmmaX and D20X >= 15:
            $ line = " You reach out and massage her enormous breasts."
            $ PrimaryLust += 1
            $ TempFocus += 1
        elif Girl == KittyX and D20X >= 15:
            $ line = " You reach out and massage her pert breasts."
        elif D20X >= 15:
            $ line = " You reach out and massage her glorious breasts."
        else:
            $ line = renpy.random.choice([" You reach out and massage her breasts.",
                            " You pass your hands gently over her warm breasts.",
                            " Her nipples catch lightly on your fingers as you grasp her warm flesh, you can feel them stiffen.",
                            " She gasps as you lightly thumb her rigid nipples."])
        $ PrimaryLust += 3
        $ TempFocus += 2 if Player.climax < 90 else 0

    elif Player.secondary_Action == "suck_breasts":
        if Girl.Clothes["bra"] or Girl.top_number() > 1:
            $ line = renpy.random.choice([" You bend down and motor-boat her breasts.",
                    " You tease her nipples with your tongue through her top.",
                    " You slowly lick her nipples through her moist top.",
                    " you gently place a nipple between your lips, and draw it out until it releases with a *pop*.",
                    " She gasps as you lightly lick her rigid nipples, poking through her top."])
        else:
            $ line = renpy.random.choice([" You bend down and motor-boat her breasts.",
                    " You gently nibble at her nipples as you suck on them.",
                    " You tease her nipples with your tongue.",
                    " You slowly lick around, and then blow across her nipples.",
                    " You gently place a nipple between your lips, and draw it out until it releases with a *pop*.",
                    " She gasps as you lightly lick her rigid nipples."])
        $ PrimaryLust += 4 if 60 < Girl.lust < 80 else 2
        $ TempFocus += 3 if Player.climax < 90 else 0

    elif Player.secondary_Action == "fondle_pussy":
        if Girl.pubes and D20X >= 15:
            $ line = " You draw your hand along her furry bush, dripping with her excitement."
        elif D20X >= 15:
            $ line = " You draw your hand along her smooth mount, slick with her excitement."
        else:
            $ line = renpy.random.choice([" You put your hand against her mound and grind against it.",
                        " You reach into her gap and she gasps as you slide your hand across and stroke her lips.",
                        " Her legs twitch a bit as you press your thumb against her.",
                        " You slide a finger along her lower lips, and she lets out a small shudder.",
                        " You reach between her legs and she gasps as you stroke along her crevice.",
                        " You slide a hand up her inner thigh, she moans a little as you reach the point where they meet."])
        $ PrimaryLust += 4 if 60 < Girl.lust < 90 else 2
        $ TempFocus += 4 if Player.climax < 90 else 0

    elif Player.secondary_Action == "eat_pussy":
        if Girl.bottom_number() <= 5 and Girl.underwear_number() <= 1:
            if Girl.pubes and D20X >= 15:
                $ line = " You press you nose into her furry bush, dripping with her excitement."
            elif D20X >= 15:
                $ line = " You press you nose against her smooth mount, slick with her excitement."
            else:
                $ line = renpy.random.choice([" You slide your tongue into her pussy and flick the roof with deft strokes.",
                        " You spread the lips back and she gasps as you slide your tongue between them.",
                        " You can feel her twitching as you grind your tongue against her clit.",
                        " She gasps as you suck on her clit.",
                        " You rub her clit with your thumb as you dive into her pussy with your tongue.",
                        " With a little nibble, you tug on her lower lips.",
                        " You slowly lick into her gap and she gasps as you press the walls aside."])
        else:
            $ line = renpy.random.choice([" You spread the lips back beneath the thin fabric, and she gasps as you slide your tongue across them.",
                    " She gasps as you suck on her clit through the fabric.",
                    " You rub her clit with your thumb as you press against her pussy with your tongue.",
                    " You put your hand against her mound and lick the juice that's collected.",
                    " With a little nibble, you tug back the fabric.",
                    " You slowly lick into her gap and she gasps as you press the walls aside."])
        $ PrimaryLust += 5 if Girl.lust > 50 else 2
        $ TempFocus += 4 if Player.climax < 90 else 0

    elif Player.secondary_Action == "fondle_ass":
        $ line = renpy.random.choice([" You reach out and brush your hands across her ass.",
                    " You put your hand against her firm rear and grind against it.",
                    " You reach between her legs and she gasps as you stroke along her crevice.",
                    " Her legs twitch a bit as you press your thumb against her.",
                    " She gasps as you reach under her and lightly stroke her ass.",
                    " You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks."])
        $ PrimaryLust += 2 if Girl.lust < 50 else 1
        $ TempFocus += 1 if Player.climax < 50 else 0
        $ TempFocus += 1 if Player.climax < 80 else 0

    elif Player.secondary_Action == "finger_ass":
        $ line = renpy.random.choice([" You reach out and slide a finger into her ass.",
                    " You slide a finger into her asshole and stroke the roof of it.",
                    " You can feel her twitching as you press your thumb against her clit.",
                    " She gasps as you rub her asshole with your fingers.",
                    " You rub her pussy with your thumb as you dive into her asshole with your middle finger.",
                    " You reach into her gap and she gasps as you slide your hand across and press against her hole.",
                    " She gasps as you reach under her warm lips and lightly stroke her ass."])
        $ PrimaryLust += 3 if Girl.lust > 70 and Girl.used_to_anal else 1
        $ TempFocus += 2 if Player.climax < 90 else 0

    elif Player.secondary_Action == "jerking_off":
        if Player.primary_Action == "masturbation":
            $ line = " You stroke your cock as you watch her go."
        elif Player.primary_Action == "lesbian":
            $ line = " You stroke your cock as you watch them."
        elif Player.primary_Action == "handjob":
            $ line = renpy.random.choice([" You also give it a little rub.",
                            " As she does so, you polish the knob a bit.",
                            " You help.",
                            " Your hand bumps into hers occasionally."])
        elif Player.primary_Action == "blowjob":
            if action_speed >= 3:
                $ line = "."
            else:
                $ line = renpy.random.choice([" You also give it a little rub.",
                            " As she does so, you work the shaft a bit.",
                            " Your fingers brush her lips.",
                            " Her lips brush your hand occasionally."])
        else:
            $ line = renpy.random.choice([" With your other hand, you stroke your shaft.",
                            " You stroke your cock with your other hand.",
                            " As you do, you stoke yourself."])
        if "unseen" not in Girl.recent_history:
            $ PrimaryLust += 3 if 20 < Girl.lust < 70 else 2
            $ TempFocus += 1 if Player.climax < 70 else 0
        $ TempFocus += 5
    return











label Girl_Self_lines(GirlA=Primary, Mode = "T3", Action=girl_secondary_Action, TempLustX=0, TempFocusX=0, D20X=0):





    $ D20X = renpy.random.randint(1, 20) if not D20X else D20X

    $ line = 0
    if not Action or D20X >= 15:

        if Player.primary_Action != "masturbation" and "passive" in GirlA.traits:

            $ line = 0
            return
        call Girl_Self_Set (GirlA, Mode, Action)

        if Mode == "T3":

            $ Action = girl_secondary_Action
        else:

            $ Action = second_girl_secondary_Action
        if not Action:
            return
        elif Action == "handjob" and not line:
            $ line = "Also, " + GirlA.name + " continues stroke your cock. "
        elif not line:
            $ line = "Also, " + GirlA.name + " continues to masturbate. "
    elif Action == "handjob":
        $ line = GirlA.name + " continues stroke your cock. "
    else:
        $ line = renpy.random.choice([GirlA.name + " continues to masturbate. ",
                                    GirlA.name + "_'s hands move across her body. ",
                                    GirlA.name + " continues to feel herself. ",
                                    GirlA.name + " can't keep still. "])

    if Action == "handjob":
        $ line = line + renpy.random.choice(["She lightly strokes the shaft, fingers sliding along the vein",
                                "She grasps the shaft firmly, and slowly slides along its length",
                                "She's becoming something of a handjob expert",
                                "Her expert strokes will have you boiling over in seconds",
                                "She strokes the shaft vigorously, lightly touching the tip",
                                "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                "Her hand slides slowly down your shaft"])
        if Player.primary_Action == "massage":
            $ TempFocusX += 10 if Player.climax > 60 else 4
            $ TempFocusX += 2 if GirlA.permanent_History["handjob"] > 2 else 0
        else:
            $ TempFocus += 10 if Player.climax > 60 else 4
            $ TempFocus += 2 if GirlA.permanent_History["handjob"] > 2 else 0

        $ TempLustX += 2 if GirlA.lust < 60 else 1
        $ TempLustX += 2 if GirlA.permanent_History["handjob"] > 2 else 0
        $ GirlA.addiction -= 1
    else:
        if GirlA.lust >= 80:
            if Action == "fondle_pussy":
                $ line = line + renpy.random.choice(["Her hand rapidly moves across her mound, firmly stroking her clit",
                                "She inserts two fingers into her dripping pussy and rapidly pistons them",
                                "She gasps as her fingers bury themselves deeply inside her",
                                "She gives a little squeal as she pinches her clit between her fingers",
                                "She fingers move quickly across her mound, constantly sliding across her clit",
                                "She fingers move rapidly up and down her inner thighs and belly, building towards their center",
                                "She spreads her lower lips and furiously strokes the inner lining",
                                "She alternately dives her fingers into herself, and licks the juices off of them",
                                "She slides two fingers firmly in and out of her tight gap as she massages the clit with her palm",
                                "She rapidly circles her fingers against her erect clit",
                                "She quickly slides a finger up and down the crease of her pussy",
                                "She lets out a moan as her fingers brush against her erect clit"])
            elif Action == "dildo_pussy":
                $ line = line + renpy.random.choice(["She moves the dildo in circles across her mound, firmly rubbing into it",
                                "She hungrily slams the dildo into her tight pussy, and pistons it in and out",
                                "She shoves the dildo firmly in and out of her grasping pussy",
                                "She quickly slides the phallus up and down her crease"])
            elif Action == "fondle_ass":
                $ line = line + renpy.random.choice(["Her hand rapidly moves across her ass, firmly stroking her tight hole",
                                "She inserts a finger deep into her grasping hole and rapidly pistons it",
                                "She gasps as she buries a finger deeply into her tight anus",
                                "She gives a little squeal as she pinches her clit between her fingers",
                                "Her fingers move quickly across her ass, constantly sliding across her rim",
                                "Her fingers move rapidly up and down her inner thighs and ass, building towards their center",
                                "She spreads her cheeks and furiously strokes the puckered rim",
                                "She slides two fingers firmly in and out of her tight hole",
                                "She rapidly circles her fingers against the sensitive rim",
                                "She lets out a moan as her fingers brush against her quivering hole"])
            elif Action == "dildo_ass":
                $ line = line + renpy.random.choice(["She moves the dildo in circles across her ass, firmly rubbing into it",
                                "She hungrily slams the dildo into her tight hole, and pistons it in and out",
                                "She shoves the dildo firmly in and out of her grasping asshole",
                                "She quickly slides the phallus up and down the crease of her ass"])
            elif Action == "vibrator_pussy":
                $ line = line + renpy.random.choice(["She traces the buzzing ball slowly down her body, barely grazing her mound",
                                "Her vibrator slides lightly across her pubic region, subtly avoiding her lips",
                                "She slides the buzzing egg into her dripping pussy and tugs it in and out",
                                "She presses the vibrator firmly against her clit and a shiver runs through her",
                                "Her whirring toy is dragged up and down her inner thighs, slowly building towards their center",
                                "She  spreads her lower lips and runs the device along the inner lining",
                                "She presses the toy deep into her and the vibrations send a shock through her body"])
            else:
                $ line = line + renpy.random.choice(["She passionately rubs her breasts, desperately tugging at her nipples",
                                "Her hands squeeze at her breasts, massaging them firmly with both hands",
                                "She hungrily cups her breasts and moves them in rapid circles",
                                "Her hands move constantly across her chest, alternately pulling at her nipples or just grazing her skin",
                                "She firmly pinches her nipples and gives them steady tugs",
                                "She passionately rubs her breasts, desperately tugging at her nipples"])

        elif GirlA.lust >= 50:
            if Action == "fondle_pussy":
                $ line = line + renpy.random.choice(["Her hand moves in circles across her mound, firmly rubbing into it",
                                "Her hands move along her sides, carefully caressing them",
                                "Her fingers move smoothly across her delta, occasionally grazing her lips",
                                "Her fingers move up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She gently slides a finger up and down the crease of her pussy",
                                "She lets out a gasp as her fingers brush against her erect clit"])
            elif Action == "dildo_pussy":
                $ line = line + renpy.random.choice(["She moves the dildo in circles across her mound, firmly rubbing into it",
                                "She traces the rubber phallus slowly down her body, barely grazing her mound",
                                "Her dildo slides lightly across her pubic region, subtly avoiding her lips",
                                "Her dildo is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She gently slides the phallus up and down the crease of her pussy",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
            elif Action == "fondle_ass":
                $ line = line + renpy.random.choice(["Her hand moves in circles across her ass, firmly rubbing into it",
                                "Her hands move along her sides, carefully caressing them",
                                "Her fingers move smoothly along her crack, occasionally grazing her asshole",
                                "Her fingers move up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her cheeks and caresses the tight hole within",
                                "She gently slides a finger up and down the crease of ass",
                                "She lets out a gasp as her fingers brush against her puckered hole"])
            elif Action == "dildo_ass":
                $ line = line + renpy.random.choice(["She traces the rubber phallus slowly down her body, barely grazing her ass",
                                "Her dildo slides lightly across her crack, subtly avoiding the hole",
                                "Her dildo is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her cheeks and caresses the rim beneath",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
            elif Action == "vibrator_pussy":
                $ line = line + renpy.random.choice(["She traces the buzzing ball slowly down her body, barely grazing her mound",
                                "Her vibrator slides lightly across her pubic region, subtly avoiding her lips",
                                "Her whirring toy is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She drags the vibrator slowly along her sides, carefully caressing them"])
            else:
                $ line = line + renpy.random.choice(["She gently rubs her breasts, dragging a finger across her nipple",
                                "She gently cups her breasts and moves them in slow circles",
                                "She moves her hands from her breasts to rub her neck",
                                "She lightly pinches one of her nipples",
                                "Her hands firmly caress her breasts, massaging them in circular motions",
                                "Her hands move along her breasts, carefully caressing them",
                                "She gasps as her finger brushes against an erect nipple"])
        else:

            if Action == "fondle_pussy":
                $ line = line + renpy.random.choice(["Her hand traces slowly down her body, barely grazing her mound",
                                "Her fingers move lightly across her pubic region, subtly avoiding her lips",
                                "Her fingers move up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "Her hands move along her sides, carefully caressing them"])
            elif Action == "dildo_pussy":
                $ line = line + renpy.random.choice(["She traces the rubber phallus slowly down her body, barely grazing her mound",
                                "Her dildo slides lightly across her pubic region, subtly avoiding her lips",
                                "Her dildo is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
            elif Action == "fondle_ass":
                $ line = line + renpy.random.choice(["Her hand traces slowly down her body, barely passing smoothly across her hips",
                                "Her fingers move lightly across her crack, subtly avoiding her rosebud",
                                "Her fingers move up and down her inner thighs, slowly building towards their center",
                                "Her hands move along her sides, carefully caressing them"])
            elif Action == "dildo_ass":
                $ line = line + renpy.random.choice(["She traces the rubber phallus slowly down her body, barely grazing her ass",
                                "Her dildo slides lightly across her crack, subtly avoiding the hole",
                                "Her dildo is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her cheeks and caresses the rim beneath",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
            elif Action == "vibrator_pussy":
                $ line = line + renpy.random.choice(["She traces the buzzing ball slowly down her body, barely grazing her mound",
                                "Her vibrator slides lightly across her pubic region, subtly avoiding her lips",
                                "Her whirring toy is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She drags the vibrator slowly along her sides, carefully caressing them"])
            else:
                $ line = line + renpy.random.choice(["She gently rubs her breasts, dragging a finger across her nipple",
                                "She gently cups her breasts and moves them in slow circles",
                                "She moves her hands from her breasts to rub her neck",
                                "She lightly pinches one of her nipples",
                                "She gasps as her finger brushes against an erect nipple"])





        $ TempLustX += 4 if GirlA.lust > 80 else 0
        $ TempLustX += 5 if GirlA.lust < 40 else 3
        $ TempLustX += 5 if Player.primary_Action == "masturbation" and GirlA != Partner else 0

        if Player.primary_Action == "massage":
            $ TempFocusX += 4 if Player.climax < 50 else 3
            call change_Player_stat("focus", 200, TempFocusX)
            call change_Girl_stat(GirlA, "lust", TempLustX)
            return
        else:
            if "TempFocus" not in locals().keys():
                "Tell Oni the error was \"[Player.primary_Action]\"."
            $ TempFocus += 4 if Player.climax < 50 else 3

        if Partner != GirlA:

            $ TempLust = TempLustX
        else:

            $ TempLust2 = TempLustX




    return






label Girl_Self_Set(GirlA=Primary, Mode = "T3", Action=girl_secondary_Action, Length=0, between_event_count=0, Options = []):



    if Mode == "T3" and Player.primary_Action != "masturbation":

        if "sub" in GirlA.traits:
            return


        if GirlA.SEXP >= 50 or approval_check(GirlA, 500, "I"):
            if GirlA.lust <= 30:
                return
        elif GirlA.SEXP >= 25 or approval_check(GirlA, 300, "I"):
            if GirlA.lust <= 50:
                return
        else:
            return

    if Mode == "T3" and Player.primary_Action == "masturbation":

        $ Options = ["fondle_pussy", "fondle_breasts", "fondle_ass"]
        if "dildo" in GirlA.inventory:
            $ Options.append("dildo_pussy")
            if GirlA.used_to_anal:
                $ Options.append("dildo_ass")
        if "vibrator" in GirlA.inventory:
            $ Options.append("vibrator_pussy")
    else:

        if GirlA.permanent_History["handjob"] >= 5 and Mode != "T5" and Player.primary_Action in ("fondle_pussy", "fondle_breasts", "fondle_thighs", "kiss", "fondle_ass", "suck_breasts"):

            $ Options.append("handjob")

        if Player.primary_Action not in ("sex", "fondle_pussy", "eat_pussy", "dildo_pussy"):

            if "dildo" in GirlA.inventory:
                $ Options.append("dildo_pussy")
            $ Options.append("fondle_pussy")

        if Player.primary_Action not in ("anal", "fondle_ass", "finger_ass", "eat_ass", "dildo_ass") and GirlA.used_to_anal:

            if "dildo" in GirlA.inventory:
                $ Options.append("dildo_ass")
            $ Options.append("fondle_ass")

        if "vibrator" in GirlA.inventory:
            $ Options.append("vibrator_pussy")

        if Player.primary_Action not in ("fondle_breasts", "suck_breasts"):

            $ Options.append("fondle_breasts")

        if GirlA.obedience < GirlA.inhibition:

            if "fondle_pussy" not in Options:
                $ Options.append("fondle_pussy")
            if "fondle_ass" not in Options:
                $ Options.append("fondle_ass")
            if "fondle_breasts" not in Options:
                $ Options.append("fondle_breasts")


    $ Length = len(Options)-1
    $ D20 = renpy.random.randint(1, 20)
    if D20 > = 18:
        $ between_event_count = 0
    elif D20 >= 15:
        $ between_event_count = 1
    elif D20 >= 12:
        $ between_event_count = 2
    elif D20 >= 10:
        $ between_event_count = 3
    else:
        $ between_event_count = renpy.random.randint(0, Length)

    $ between_event_count = Length if between_event_count > Length else between_event_count
    if Action != Options[between_event_count]:

        $ Action = Options[between_event_count]
        if Action == "handjob":
            $ line = GirlA.name + " slides her hand down and firmly grabs your dick. "
            $ approval = 3
        elif Action == "fondle_pussy":
            $ line = GirlA.name + "_'s hand slides down and begins to stroke her pussy. "
        elif Action == "dildo_pussy":
            $ line = GirlA.name + " pulls out her dildo and draws it toward her pussy. "
        elif Action == "fondle_ass":
            $ line = GirlA.name + "_'s hand slides behind her body, reaching toward her ass. "
        elif Action == "dildo_ass":
            $ line = GirlA.name + " pulls out her dildo and reaches it behind her. "
        elif Action == "vibrator_pussy":
            $ line = GirlA.name + " pulls out her vibrator and strokes it across her body. "
        else:
            $ line = GirlA.name + "_'s hands slide up her body and begin to kneed her breasts. "
    elif Action == "handjob":
        $ line = "Also, " + GirlA.name + " continues stroke your cock. "
    else:
        $ line = "Also, " + GirlA.name + " continues to masturbate. "

    if Mode == "T3":
        $ girl_secondary_Action = Action
    else:
        $ second_girl_secondary_Action = Action

    return







label SexDialog_Threeway(GirlA=Secondary, Mode=0, Action=0, GirlB=Primary, Templine=0, TempLust=0, TempLust2=0, TempFocus=0):







    call Threeway_Set (GirlA, Mode=Mode, GirlB=GirlB)

    if Mode == "lesbian":
        $ Action = girl_secondary_Action
        $ GirlB = Secondary
    else:
        $ Action = second_girl_main_action

    if line:

        return
    elif not Action:
        $ Action = "watch"

    if Action == "handjob":
        if D20S <= 8 and (Player.primary_Action == "blowjob" or Player.primary_Action == "handjob"):
            if Player.primary_Action == "blowjob":
                $ line = renpy.random.choice([GirlA.name + "_'s fingers brush against " + GirlB.name + "_'s lips as they work",
                                    GirlA.name + " and " + GirlB.name + " pause for a second to briefly kiss",
                                    GirlA.name + " takes a turn to suck on the head before passing it back",
                                    GirlA.name + " and " + GirlB.name + " get into an alternating rhythm"])
            elif Player.primary_Action == "handjob":
                $ line = renpy.random.choice([GirlA.name + "_'s fingers brush against " + GirlB.name + "_'s as they work",
                                    GirlA.name + " strokes " + GirlB.name + "_'s palm as she works",
                                    GirlA.name + " takes a turn to stroke a few times before passing it back",
                                    GirlA.name + " and " + GirlB.name + " get into an alternating rhythm"])
        else:
            if Player.primary_Action == "handjob":
                $ line = GirlA.name + " also continues to stroke your cock"
            else:
                $ line = GirlA.name + " continues stroke your cock"

            $ line = line + renpy.random.choice([", lightly stroking the shaft, fingers sliding along the vein",
                                ", grasping the shaft firmly, and slowly sliding along its length",
                                ", making up for years of lost time",
                                ", her expert strokes will have you boiling over in seconds",
                                ", stroking the shaft vigorously, lightly touching the tip",
                                ", moving very smoothly, stroking casually",
                                ", hand sliding slowly down your shaft"])
        $ TempFocus += 3 if Player.climax > 70 else 2

        $ TempLust += 2 if GirlA.lust < 60 else 0
        $ TempLust += 2 if GirlA.permanent_History["handjob"] > 2 else 0
        $ GirlA.addiction -= 1 if D20S > 10 else 2



    elif Action == "blowjob":
        if action_speed > 2 and Player.primary_Action == "blowjob":
            $ line = "Since " + GirlB.name + " is working so hard, " + GirlA.name + " settles for the occasional nibble or lick."
            $ TempFocus += 5 if Player.climax > 60 else 3
            $ TempLust += 2 if GirlA.lust > 80 else 1
        else:
            if D20S <= 8 and (Player.primary_Action == "blowjob" or Player.primary_Action == "handjob"):
                if Player.primary_Action == "blowjob":
                    $ line = renpy.random.choice([GirlA.name + "_'s tongue brushes against " + GirlB.name + "_'s as they work",
                                        GirlA.name + " and " + GirlB.name + " pause for a second to briefly kiss",
                                        GirlA.name + " takes a turn to suck on the head before passing it back",
                                        GirlA.name + " and " + GirlB.name + " get into an alternating rhythm"])
                elif Player.primary_Action == "handjob":
                    $ line = renpy.random.choice([GirlA.name + "_'s tongue brushes against " + GirlB.name + "_'s hand as they work",
                                        GirlA.name + " licks " + GirlB.name + "_'s palm as she works",
                                        GirlA.name + " takes a turn to stroke a few times before passing it back",
                                        GirlA.name + " and " + GirlB.name + " get into an alternating rhythm"])
                $ TempLust2 += 1 if GirlB.likes[GirlA.tag] >= 800 else 0
            else:
                if Player.primary_Action == "blowjob":
                    $ line = GirlA.name + " also continues to lick your cock"
                else:
                    $ line = "Also, " + GirlA.name + " continues lick your cock"

                $ line = line + renpy.random.choice([", settling into a gentle licking pace along the base",
                                    ", licking gently up and down the shaft",
                                    ", her tongue moves carefully along the shaft",
                                    ", really starting to learn some clever tricks to making you feel good",
                                    ", licking her way down the shaft, and gently teasing the balls"])

            $ TempFocus += 20 if Player.climax > 60 else 10
            $ TempLust += 2 if GirlA.lust > 80 else 1

            $ GirlA.addiction -= 2


    elif Action == "fondle_breasts":
        if Player.secondary_Action == "fondle_breasts" and Player.primary_Action != "lesbian":
            $ line = GirlA.name + " also continues to fondle " + GirlB.name + "_'s breasts"
        else:
            $ line = GirlA.name + " continues to fondle " + GirlB.name + "_'s breasts"

        $ line = line + renpy.random.choice([", giving little tugs to her nipples",
                                        ", cupping them firmly with both hands",
                                        ", gently moving them in slowly increasing circles",
                                        ", then moves her hands from her breasts to rub her neck",
                                        ", firmly pinching her nipples and giving them a tug",
                                        ", passing repeatedly against her rigid nipples"])
        $ TempLust += 2 if approval_check(GirlA, 500, "I") else 1
        $ TempLust2 += 5 if GirlB.likes[GirlA.tag] >= 800 else 2
        $ TempFocus += 1



    elif Action == "suck_breasts":
        if Player.secondary_Action == "fondle_breasts" and Player.primary_Action != "lesbian":
            $ line = GirlA.name + " also continues to suck " + GirlB.name + "_'s breasts"
        else:
            $ line = GirlA.name + " continues to suck " + GirlB.name + "_'s breasts"

        $ line = line + renpy.random.choice([", giving little tugs to her nipple",
                                        ", cupping them firmly with both hands",
                                        ", then moves her hands down along her side",
                                        ", licking slowly up her chest",
                                        ", firmly nibbling her nipples and giving them a tug",
                                        ", nibbling repeatedly at her rigid nipples"])
        $ TempLust += 2 if approval_check(GirlA, 500, "I") else 1
        $ TempLust2 += 4 if GirlB.likes[GirlA.tag] >= 800 else 2
        $ TempFocus += 1



    elif Action == "fondle_pussy":
        if (Player.primary_Action == "fondle_pussy" or Player.secondary_Action == "fondle_pussy") and Player.primary_Action != "lesbian":
            $ line = GirlA.name + " also continues to fondle " + GirlB.name + "_'s pussy"
            $ Templine = renpy.random.choice([", stroking across her clit",
                                        ", the two of you taking turns in your motions",
                                        ", her fingers brushing against yours as you work",
                                        ", rubbing against it vigorously",
                                        ", stroking into it vigorously",
                                        ", pressing firmly into it",
                                        ", sliding firmly into it",
                                        ", moving inside it with slow undulating motions",
                                        ", moving with slow undulating motions"])
        else:
            $ line = GirlA.name + " continues to fondle " + GirlB.name + "_'s pussy"
            $ Templine = renpy.random.choice([", running fingers gently up her cleft",
                                        ", stroking across her clit",
                                        ", taking a little taste of the warm juices on her finger",
                                        ", rubbing against it vigorously",
                                        "a",
                                        "b",
                                        "c",
                                        ", moving with slow undulating motions"])


            if Templine == "a":
                if Player.primary_Action == "sex" or Player.primary_Action == "anal":
                    $ Templine = ", her fingers brush against your cock as it goes in"
                elif Player.primary_Action == "eat_pussy":
                    $ Templine = ", your tongue slides past her fingers"
                elif Player.primary_Action == "dildo_pussy" or Player.secondary_Action == "dildo_pussy":
                    $ Templine = ", her fingers brush against the dildo as it goes in"
                else:
                    $ Templine = ", stroking into it vigorously"
            elif Templine == "b":
                if Player.primary_Action == "sex" or Player.primary_Action == "anal":
                    $ Templine = ", her fingers brushing up against your balls as you sink in"
                elif Player.primary_Action == "eat_pussy":
                    $ Templine = ", you briefly suck on one of her fingers"
                elif Player.primary_Action == "dildo_pussy" or Player.secondary_Action == "dildo_pussy":
                    $ Templine = ", her fingers brushing up against the dildo as it slides by"
                else:
                    $ Templine = ", sliding firmly into it"
            elif Templine == "c":
                if Player.primary_Action == "sex" or Player.primary_Action == "anal":
                    $ Templine = ", her fingers brush against your cock as it goes in"
                elif Player.primary_Action == "eat_pussy":
                    $ Templine = ", your tongue slides along her fingers"
                elif Player.primary_Action == "dildo_pussy" or Player.secondary_Action == "dildo_pussy":
                    $ Templine = ", her fingers brushing up against the dildo as it slides by"
                else:
                    $ Templine = ", moving inside it with slow undulating motions"

        $ line = line + Templine

        $ TempLust += 2 if approval_check(GirlA, 500, "I") else 1
        $ TempLust2 += 5 if GirlB.likes[GirlA.tag] >= 800 else 3
        $ TempFocus += 1




    elif Action == "eat_pussy":
        if (Player.primary_Action == "eat_pussy" or Player.secondary_Action == "eat_ pussy") and Player.primary_Action != "lesbian":
            $ line = GirlA.name + " also continues to lick " + GirlB.name + "_'s pussy"
        else:
            $ line = GirlA.name + " continues to lick " + GirlB.name + "_'s pussy"

        $ Templine = renpy.random.choice([", running her tongue gently up her cleft",
                                    ", stroking across her clit",
                                    ", taking a little taste of the warm juices flowing out",
                                    ", lapping against it vigorously",
                                    "a",
                                    "b",
                                    "c",
                                    ", moving with slow undulating motions"])


        if Templine == "a":
            if Player.primary_Action == "sex" or Player.primary_Action == "anal":
                $ Templine = ", her tongue brushes against your cock as it goes in"
            elif Player.primary_Action == "eat_pussy":
                $ Templine = ", her tongue brushing against yours as you work"
            elif Player.primary_Action == "fondle_pussy" or Player.secondary_Action == "fondle_pussy":
                $ Templine = ", her tongue slides along your fingers"
            elif Player.primary_Action == "dildo_pussy" or Player.secondary_Action == "dildo_pussy":
                $ Templine = ", her tongue brushes along the dildo as it goes in"
            else:
                $ Templine = ", lapping into it vigorously"
        elif Templine == "b":
            if Player.primary_Action == "sex" or Player.primary_Action == "anal":
                $ Templine = ", her longue lapping against your balls as you sink in"
            elif Player.primary_Action == "eat_pussy":
                $ Templine = ", you briefly kiss as you take turns"
            elif Player.primary_Action == "fondle_pussy" or Player.secondary_Action == "fondle_pussy":
                $ Templine = ", her tongue slides past your fingers"
            elif Player.primary_Action == "dildo_pussy" or Player.secondary_Action == "dildo_pussy":
                $ Templine = ", her tongue runs up against the dildo as it slides by"
            else:
                $ Templine = ", sliding firmly into it"
        elif Templine == "c":
            if Player.primary_Action == "sex" or Player.primary_Action == "anal":
                $ Templine = ", her tongue brushes against your cock as it goes in"
            elif Player.primary_Action == "eat_pussy":
                $ Templine = ", the two of you taking turns in your motions"
            elif Player.primary_Action == "fondle_pussy" or Player.secondary_Action == "fondle_pussy":
                $ Templine = ", her tongue slides past your fingers"
            elif Player.primary_Action == "dildo_pussy" or Player.secondary_Action == "dildo_pussy":
                $ Templine = ", her tongue runs up against the dildo as it slides by"
            else:
                $ Templine = ", moving inside it with slow undulating motions"

        $ line = line + Templine

        $ TempLust += 3 if approval_check(GirlA, 600, "I") else 1
        $ TempLust2 += 7 if GirlB.likes[GirlA.tag] >= 800 else 4
        $ TempFocus += 3



    elif Action == "fondle_ass":
        if Player.secondary_Action == "fondle_ass" and Player.primary_Action != "lesbian":
            $ line = GirlA.name + " also continues to fondle " + GirlB.name + "_'s ass"
            $ line = line + renpy.random.choice([", stroking across her rear",
                                        ", the two of you taking turns in your motions",
                                        ", her fingers brushing against yours as you work",
                                        ", rubbing it vigorously",
                                        ", squeezing it vigorously",
                                        ", pressing firmly into it",
                                        ", kneeding it with slow undulating motions",
                                        ", moving with slow undulating motions"])
        else:
            $ line = GirlA.name + " continues to fondle " + GirlB.name + "_'s ass"
            $ line = line + renpy.random.choice([", running fingers gently up her cleft",
                                        ", stroking across her rear",
                                        ", rubbing it vigorously",
                                        ", squeezing it vigorously",
                                        ", pressing firmly into it",
                                        ", kneeding it with slow undulating motions",
                                        ", moving with slow undulating motions"])

        $ TempLust += 1 if approval_check(GirlA, 500, "I") else 0
        $ TempLust2 += 3 if GirlB.likes[GirlA.tag] >= 800 else 1
        $ TempFocus += 1



    elif Action == "finger_ass":
        if (Player.primary_Action == "finger_ass" or Player.secondary_Action == "finger_ass") and Player.primary_Action != "lesbian":
            $ line = GirlA.name + " also continues to stroke " + GirlB.name + "_'s ass"
        else:
            $ line = GirlA.name + " continues to stroke " + GirlB.name + "_'s ass"

        $ Templine = renpy.random.choice([", stroking across her rim",
                                    ", stroking across her hole",
                                    ", circling it vigorously",
                                    "a",
                                    "b",
                                    "c",
                                    ", moving with slow undulating motions"])


        if Templine == "a":
            if Player.primary_Action == "sex" or Player.primary_Action == "anal":
                $ Templine = ", her fingers brush against your cock as it goes in"
            elif Player.primary_Action == "finger_ass" or Player.secondary_Action == "finger_ass":
                $ Templine = ", her fingers circling yours"
            elif Player.primary_Action == "dildo_ass" or Player.secondary_Action == "dildo_ass":
                $ Templine = ", her fingers brush against the dildo as it goes in"
            else:
                $ Templine = ", running fingers gently up her cleft"
        elif Templine == "b":
            if Player.primary_Action == "sex" or Player.primary_Action == "anal":
                $ Templine = ", her fingers brushing up against your balls as you sink in"
            elif Player.primary_Action == "finger_ass" or Player.secondary_Action == "finger_ass":
                $ Templine = ", the two of you taking turns in your motions"
            elif Player.primary_Action == "dildo_ass" or Player.secondary_Action == "dildo_ass":
                $ Templine = ", her fingers run along the dildo as it slides by"
            else:
                $ Templine = ", sliding firmly into it"
        elif Templine == "c":
            if Player.primary_Action == "sex" or Player.primary_Action == "anal":
                $ Templine = ", her fingers brush against your cock as it goes in"
            elif Player.primary_Action == "finger_ass" or Player.secondary_Action == "finger_ass":
                $ Templine = ", her fingers intertwine yours"
            elif Player.primary_Action == "dildo_ass" or Player.secondary_Action == "dildo_ass":
                $ Templine = ", her fingers brush against the dildo as it goes in"
            else:
                $ Templine = ", moving inside it with slow undulating motions"

        $ line = line + Templine

        if not GirlB.used_to_anal:
            $ TempLust2 -= 3
        $ TempLust += 2 if approval_check(GirlA, 700, "I") else 1
        $ TempLust2 += 5 if GirlB.likes[GirlA.tag] >= 800 else 3
        $ TempFocus += 1



    elif Action == "eat_ass":
        if (Player.primary_Action == "eat_ass" or Player.secondary_Action == "eat_ass") and Player.primary_Action != "lesbian":
            $ line = GirlA.name + " also continues to lick " + GirlB.name + "_'s ass"
        else:
            $ line = GirlA.name + " continues to lick " + GirlB.name + "_'s ass"

        $ Templine = renpy.random.choice([", tonguing across her rim",
                                    ", stroking across her hole",
                                    ", circling it vigorously",
                                    "a",
                                    "b",
                                    "c",
                                    ", moving with slow undulating motions"])


        if Templine == "a":
            if Player.primary_Action == "sex" or Player.primary_Action == "anal":
                $ Templine = ", her tongue brushes against your cock as it goes in"
            elif Player.primary_Action == "eat_ass":
                $ Templine = ", her tongue brushing against yours as you work"
            elif Player.primary_Action == "finger_ass" or Player.secondary_Action == "finger_ass":
                $ Templine = ", her tongue slides along your fingers"
            elif Player.primary_Action == "dildo_ass" or Player.secondary_Action == "dildo_ass":
                $ Templine = ", her tongue brushes along the dildo as it goes in"
            else:
                $ Templine = ", lapping into it vigorously"
        elif Templine == "b":
            if Player.primary_Action == "sex" or Player.primary_Action == "anal":
                $ Templine = ", her longue lapping against your balls as you sink in"
            elif Player.primary_Action == "eat_ass":
                $ Templine = ", you briefly kiss as you take turns"
            elif Player.primary_Action == "finger_ass" or Player.secondary_Action == "finger_ass":
                $ Templine = ", her tongue slides past your fingers"
            elif Player.primary_Action == "dildo_ass" or Player.secondary_Action == "dildo_ass":
                $ Templine = ", her tongue runs up against the dildo as it slides by"
            else:
                $ Templine = ", sliding firmly into it"
        elif Templine == "c":
            if Player.primary_Action == "sex" or Player.primary_Action == "anal":
                $ Templine = ", her tongue brushes against your cock as it goes in"
            elif Player.primary_Action == "eat_ass":
                $ Templine = ", the two of you taking turns in your motions"
            elif Player.primary_Action == "finger_ass" or Player.secondary_Action == "finger_ass":
                $ Templine = ", her tongue slides past your fingers"
            elif Player.primary_Action == "dildo_ass" or Player.secondary_Action == "dildo_ass":
                $ Templine = ", her tongue runs up against the dildo as it slides by"
            else:
                $ Templine = ", moving inside it with slow undulating motions"

        $ line = line + Templine

        $ TempLust += 3 if approval_check(GirlA, 800, "I") else 1
        $ TempLust2 += 4 if GirlB.likes[GirlA.tag] >= 800 else 2
        $ TempFocus += 3



    elif Action == "masturbation":
        call Girl_Self_lines (GirlA, "T5", second_girl_secondary_Action)
        $ TempLust = 0



    elif Action in ("kiss", "kiss girl", "kiss both"):
        if Player.primary_Action == "blowjob" and GirlA.permanent_History["blowjob"] > 5 and second_girl_main_action == "kiss girl":
            $ line = GirlA.name + " also continues to kiss " + GirlB.name
            $ line = line + renpy.random.choice([", occasionally taking a lick of your cock as well",
                                            ", licking along her cheek",
                                            ", nudging you out of her mouth to get a deep kiss in",
                                            ", taking the occasional lick down your shaft",
                                            ", nudging her aside to kiss the head of your cock"])
        elif Player.primary_Action == "blowjob" and second_girl_main_action == "kiss girl":
            $ line = GirlA.name + " also continues to kiss " + GirlB.name
            $ line = line + renpy.random.choice([", occasionally bumping into your cock as well",
                                            ", licking along her cheek",
                                            ", nudging you out of her mouth to get a deep kiss in",
                                            ", trailing kisses down her neck"])
        else:
            if Action == "kiss girl" or Mode == "lesbian":
                if Player.primary_Action == "lesbian" and Partner != GirlA:
                    $ line = GirlA.name + " continues to make out with " + GirlB.name
                else:
                    $ line = GirlA.name + " also continues to make out with " + GirlB.name
                $ line = line + renpy.random.choice([", occasionally coming up for air",
                                                ", licking along her cheek",
                                                ", grabbing her face in both hands",
                                                ", their tongues swirl around each other",
                                                ", occasionally nibbling at her ears",
                                                ", trailing kisses down her neck"])
            elif Action == "kiss":
                $ line = GirlA.name + " also continues to make out with you"
                $ line = line + renpy.random.choice([", occasionally coming up for air",
                                                ", licking along your cheek",
                                                ", grabbing your face in both hands",
                                                ", your tongues swirl around each other",
                                                ", occasionally nibbling at your ears",
                                                ", trailing kisses down your neck"])
            else:
                $ line = GirlA.name + " also continues to make out with both of you"
                $ line = line + renpy.random.choice([", occasionally coming up for air",
                                                ", licking along your cheek",
                                                ", occasionally nibbling your lip as well",
                                                ", nudging you aside to get a deep kiss in",
                                                ", all three of your tongues swirling",
                                                ", nudging her aside to give you a deep kiss"
                                                ", grabbing your face in both hands",
                                                ", your tongues swirl around each other",
                                                ", licking along her cheek",
                                                ", grabbing her face in both hands",
                                                ", their tongues swirl around each other",
                                                ", occasionally nibbling at her ears",
                                                ", trailing kisses down her neck"])
        $ TempLust += 1 if approval_check(GirlA, 500, "I") else 0
        $ TempLust += 1 if GirlA.likes[GirlB.tag] >= 800 else 0
        $ TempLust2 += 2 if GirlB.likes[GirlA.tag] >= 800 else 1
        $ TempFocus += 1


    elif Action == "watch":
        $ line = GirlA.name + " continues to watch the two of you"
        $ line = line + renpy.random.choice([", shifting uncomfortably",
                                        ", readjusting her clothes",
                                        ", glancing at the door",
                                        ", taking in " + GirlB.name + "_'s body",
                                        ", transfixed by the action"])
        $ TempLust += 1 if GirlA.likes[GirlB.tag] >= 600 else 0
        $ TempLust += 2 if GirlA.likes[GirlB.tag] >= 800 else 1
        $ TempLust2 += 1 if approval_check(GirlB, 500, "I") else 0
        $ TempLust2 += 1 if approval_check(GirlB, 700, "I") else 0
        $ TempFocus += 1
    else:


        "Nothing triggered. 1:[Player.primary_Action], 2:[Player.secondary_Action], 3:[girl_secondary_Action], 4:[second_girl_main_action], 5:[second_girl_secondary_Action]"


    $ TempLust2 += 2
    if Mode == "lesbian":
        $ PrimaryLust += (TempLust*3)
        $ SecondaryLust += (TempLust2*3)
    else:
        $ SecondaryLust += TempLust
        $ PrimaryLust += TempLust2

    $ Player.climax += TempFocus
    return








label Three_Change(LeadGirl=Primary, SecondGirl=Partner, D20S=0, PrimaryLust=0, SecondaryLust=0):





    if LeadGirl not in all_Girls:
        return
    if Partner == LeadGirl:
        "Let Oni know that both roles are set to [Girl.name]."
        return
    menu Three_Change_Menu:
        ch_p "Hey [Partner.name]. . ."
        "about [LeadGirl.name]. . .":
            menu:
                ch_p "about [LeadGirl.name]. . ."
                "why don't you kiss her?" if second_girl_secondary_Action != "kiss girl" and second_girl_secondary_Action != "kiss both":
                    call Threeway_Set (SecondGirl, "kiss girl", 0, second_girl_main_action, LeadGirl)
                "why don't you grab her tits?" if second_girl_main_action != "fondle_breasts":
                    call Threeway_Set (SecondGirl, "fondle_breasts", 0, second_girl_main_action, LeadGirl)
                "why don't you suck her breasts?" if second_girl_main_action != "suck_breasts":
                    call Threeway_Set (SecondGirl, "suck_breasts", 0, second_girl_main_action, LeadGirl)
                "why don't you finger her?" if second_girl_main_action != "fondle_pussy":
                    call Threeway_Set (SecondGirl, "fondle_pussy", 0, second_girl_main_action, LeadGirl)
                "why don't you go down on her?" if second_girl_main_action != "eat_pussy":
                    call Threeway_Set (SecondGirl, "eat_pussy", 0, second_girl_main_action, LeadGirl)
                "why don't you grab her ass?" if second_girl_main_action != "fondle_ass":
                    call Threeway_Set (SecondGirl, "fondle_ass", 0, second_girl_main_action, LeadGirl)
                "why don't you lick her ass?" if second_girl_main_action != "eat_ass":
                    call Threeway_Set (SecondGirl, "eat_ass", 0, second_girl_main_action, LeadGirl)
                "Wait, I meant. . .":
                    jump Three_Change_Menu
        "about me. . .":

            menu:
                ch_p "about me. . ."
                "why don't you kiss me?" if second_girl_secondary_Action != "kiss" and second_girl_secondary_Action != "kiss both":
                    call Threeway_Set (SecondGirl, "kiss", 0, second_girl_main_action, LeadGirl)
                "maybe take me in hand?" if second_girl_main_action != "handjob":
                    call Threeway_Set (SecondGirl, "handjob", 0, second_girl_main_action, LeadGirl)
                "maybe give me a lick?" if second_girl_main_action != "blowjob":
                    call Threeway_Set (SecondGirl, "blowjob", 0, second_girl_main_action, LeadGirl)
                "why don't you give me a show?" if second_girl_main_action != "masturbation":
                    call Threeway_Set (SecondGirl, "masturbation", 0, second_girl_main_action, LeadGirl)
                "Wait, I meant. . .":
                    jump Three_Change_Menu
        "never mind.":
            pass
    return





label Threeway_Set(GirlA=Secondary, Preset=0, Mode=0, Action=second_girl_main_action, GirlB=Primary, State = "watcher", TempLust=0, TempLust2=0, TempFocus=0):









    $ D20 = renpy.random.randint(1, 20)
    if not Preset:

        if Mode == "lesbian":

            if girl_secondary_Action == "kiss girl" and GirlA.lust <= 20 and GirlA.permanent_History["orgasmed"]< 1:

                return
            elif girl_secondary_Action and position_timer <= round:

                return
        elif second_girl_main_action and D20 < 15 and second_girl_main_action != "watch":

            return
        elif second_girl_main_action and position_timer <= round:

            return
    $ Options = ["watch", "masturbation", "masturbation", "masturbation"]

    if GirlA == GirlB and GirlA != Partner:
        $ GirlB = Partner
    elif GirlA == GirlB and GirlA != Primary:
        $ GirlB = Primary
    if GirlA == GirlB:
        "Tell Oni that in Threeway_Set, A:[GirlA.tag] and B:[GirlB.tag]"
        "[Girl.Gibberish]"

    if Player.primary_Action == "lesbian":

        $ State = "lesbian"
        $ Options = ["kiss girl", "kiss girl"]
        if Preset in ("handjob", "blowjob", "kiss", "kiss both"):

            $ State = "threeway"
        elif Preset:
            pass
        elif GirlA.likes[GirlB.tag] >= 600 and approval_check(GirlA, 500, "I"):

            pass
        else:

            if Action != "kiss girl":
                $ line = GirlA.name + " gives " + GirlB.name + " a passionate kiss"
                $ Action = "kiss girl"
                $ girl_secondary_Action = "kiss girl"
                if "lesbian" not in GirlA.recent_history:
                    $ GirlA.permanent_History["been_with_girl"] += 1
                    $ GirlA.recent_history.append("lesbian")
            return
    elif not approval_check(GirlA, 500, "I"):

        pass
    elif GirlA.likes[GirlB.tag] >= 600 and approval_check(GirlA, (1500-(10*GirlA.permanent_History["been_with_girl"])-(10*(GirlA.likes[GirlB.tag]-60)))):

        $ State = "threeway"
    elif approval_check(GirlA, 1000):

        $ State = "hetero"
    elif GirlA.likes[GirlB.tag] >= 700:

        $ State = "lesbian"

    if State == "lesbian" or State == "threeway":

        $ Options.extend(("fondle_breasts", "suck_breasts", "fondle_pussy", "fondle_ass", "kiss girl"))

        if approval_check(GirlA, 800, "I") or GirlA.likes[GirlB.tag] >= 800:
            $ Options.append("eat_pussy")
        if approval_check(GirlA, 900, "I") and GirlA.likes[GirlB.tag] >= 900:
            $ Options.append("eat_ass")







    if State == "hetero" or State == "threeway":

        if Player.primary_Action == "anal":
            $ Options.extend(("handjob", "kiss", "kiss"))
        else:
            $ Options.extend(("handjob", "blowjob", "kiss"))
    $ renpy.random.shuffle(Options)

    if Preset:
        if Preset in Options:

            $ Options[0] = Preset
            if GirlA == RogueX:
                ch_r "Ok, that seems fine. . ."
            elif GirlA == KittyX:
                ch_k "Oh, ok. . ."
            elif GirlA == EmmaX:
                ch_e "Oh, very well. . ."
            elif GirlA == LauraX:
                ch_l "Ok, that seems legit. . ."
            elif GirlA == JeanX:
                ch_j "Heh, Ok. . ."
            elif GirlA == StormX:
                ch_s "Ok, we can do that. . ."
            elif GirlA == JubesX:
                ch_v "Ok, I can do that. . ."
        elif approval_check(GirlA, 750, "I") or approval_check(GirlA, 1500):

            $ Options[0] = Preset
            if GirlA == RogueX:
                ch_r "I guess I could. . ."
            elif GirlA == KittyX:
                ch_k "If that's what you want, I could give it a try. . ."
            elif GirlA == EmmaX:
                ch_e "I suppose it's worth a try. . ."
            elif GirlA == LauraX:
                ch_l "Worth a shot. . ."
            elif GirlA == JeanX:
                ch_j "Sure, whatever. . ."
            elif GirlA == StormX:
                ch_s "Ok, we can do that. . ."
            elif GirlA == JubesX:
                ch_v "Ok, I can do that. . ."
        else:

            if GirlA == RogueX:
                ch_r "I don't really feel like doing that one. . ."
            elif GirlA == KittyX:
                ch_k "That doesn't seem as fun. . ."
            elif GirlA == EmmaX:
                ch_e "That doesn't really seem appropriate. . ."
            elif GirlA == LauraX:
                ch_l "Nah, not my style. . ."
            elif GirlA == JeanX:
                ch_j "Heh, you wish. . ."
            elif GirlA == StormX:
                ch_s "I don't think so."
            elif GirlA == JubesX:
                ch_v "Nah, I don't think so. . ."


    if Options[0] == Action:

        return
    elif Mode == "lesbian":
        $ line = GirlA.name + " shifts her position"
    elif not second_girl_main_action or second_girl_main_action == "masturbation":

        $ line = GirlA.name + " moves closer"
    else:

        $ line = GirlA.name + " shifts her position"


    if Options[0] == "masturbation":
        $ Action = "masturbation"
        call Girl_Self_lines (GirlA, "T5", second_girl_secondary_Action)
    elif Options[0] == "handjob":
        call Seen_First_Peen (GirlA, GirlB, React = 1)
        $ line = line + " before she slides her hand down and firmly grabs your dick"
        $ Action = "handjob"

        call show_Girl(GirlA, y_position = 0.25, transition = ease)

        $ approval = 4
        $ TempFocus += 3 if Player.climax > 70 else 2
        $ TempLust += 2 if GirlA.lust < 60 else 0
        $ TempLust += 2 if GirlA.permanent_History["handjob"] > 2 else 0
        $ GirlA.addiction -= 1 if D20 > 10 else 2
    elif Options[0] == "blowjob":
        call Seen_First_Peen (GirlA, GirlB, React = 1)
        $ line = line + " before she slides down and begins to slowly lick your cock"

        call show_Girl(GirlA, y_position = 0.25, transition = ease)

        $ Action = "blowjob"
        $ approval = 4

        $ TempFocus += 20 if Player.climax > 60 else 10
        $ TempLust += 2 if GirlA.lust > 80 else 1
        $ GirlA.addiction -= 2


    elif Options[0] == "fondle_breasts":

        $ line = line + " and slides her hands along " + GirlB.name + "_'s breasts"
        $ Action = "fondle_breasts"
        if "lesbian" not in GirlA.recent_history:
            $ GirlA.permanent_History["been_with_girl"] += 1
            $ GirlA.recent_history.append("lesbian")
        if "lesbian" not in GirlB.recent_history:
            $ GirlB.permanent_History["been_with_girl"] += 1
            $ GirlB.recent_history.append("lesbian")
        $ TempLust += 2 if approval_check(GirlA, 500, "I") else 1
        $ TempLust2 += 4 if GirlB.likes[GirlA.tag] >= 800 else 2
        $ TempFocus += 1
    elif Options[0] == "suck_breasts":

        $ line = line + " and slurps " + GirlB.name + "_'s nipple into her mouth"
        $ Action = "suck_breasts"
        if "lesbian" not in GirlA.recent_history:
            $ GirlA.permanent_History["been_with_girl"] += 1
            $ GirlA.recent_history.append("lesbian")
        if "lesbian" not in GirlB.recent_history:
            $ GirlB.permanent_History["been_with_girl"] += 1
            $ GirlB.recent_history.append("lesbian")
        $ TempLust += 2 if approval_check(GirlA, 500, "I") else 1
        $ TempLust2 += 5 if GirlB.likes[GirlA.tag] >= 800 else 2
        $ TempFocus += 1
    elif Options[0] == "fondle_pussy":

        $ line = line + " and runs her finger along " + GirlB.name + "_'s pussy"
        $ Action = "fondle_pussy"
        if "lesbian" not in GirlA.recent_history:
            $ GirlA.permanent_History["been_with_girl"] += 1
            $ GirlA.recent_history.append("lesbian")
        if "lesbian" not in GirlB.recent_history:
            $ GirlB.permanent_History["been_with_girl"] += 1
            $ GirlB.recent_history.append("lesbian")
        $ TempLust += 2 if approval_check(GirlA, 500, "I") else 1
        $ TempLust2 += 5 if GirlB.likes[GirlA.tag] >= 800 else 3
        $ TempFocus += 2
    elif Options[0] == "eat_pussy":

        $ line = line + " and runs her tongue along " + GirlB.name + "_'s pussy"
        $ Action = "eat_pussy"
        if "lesbian" not in GirlA.recent_history:
            $ GirlA.permanent_History["been_with_girl"] += 1
            $ GirlA.recent_history.append("lesbian")
        if "lesbian" not in GirlB.recent_history:
            $ GirlB.permanent_History["been_with_girl"] += 1
            $ GirlB.recent_history.append("lesbian")
        $ TempLust += 3 if approval_check(GirlA, 600, "I") else 1
        $ TempLust2 += 8 if GirlB.likes[GirlA.tag] >= 800 else 5
        $ TempFocus += 3
    elif Options[0] == "fondle_ass":

        $ line = line + " and gives " + GirlB.name + "_'s ass a firm squeeze"
        $ Action = "fondle_ass"
        if "lesbian" not in GirlA.recent_history:
            $ GirlA.permanent_History["been_with_girl"] += 1
            $ GirlA.recent_history.append("lesbian")
        if "lesbian" not in GirlB.recent_history:
            $ GirlB.permanent_History["been_with_girl"] += 1
            $ GirlB.recent_history.append("lesbian")
        $ TempLust += 1 if approval_check(GirlA, 400, "I") else 0
        $ TempLust2 += 3 if GirlB.likes[GirlA.tag] >= 600 else 2
        $ TempFocus += 1
    elif Options[0] == "eat_ass":

        $ line = line + " and starts to lick around " + GirlB.name + "_'s ass"
        $ Action = "eat_ass"
        if "lesbian" not in GirlA.recent_history:
            $ GirlA.permanent_History["been_with_girl"] += 1
            $ GirlA.recent_history.append("lesbian")
        if "lesbian" not in GirlB.recent_history:
            $ GirlB.permanent_History["been_with_girl"] += 1
            $ GirlB.recent_history.append("lesbian")
        $ TempLust += 3 if approval_check(GirlA, 800, "I") else 1
        $ TempLust2 += 6 if GirlB.likes[GirlA.tag] >= 800 else 4
        $ TempFocus += 2

    elif Options[0] == "kiss girl" or Mode == "lesbian":
        $ line = line + " and gives " + GirlB.name + " a passionate kiss"
        $ Action = "kiss girl"
        if Mode != "lesbian" and "kiss" in Options:
            if Player.primary_Action == "kiss":
                $ Action = "kiss both"
            elif girl_secondary_Action == "kiss":
                $ Action = "kiss both"
            elif second_girl_main_action == "kiss":
                $ Action = "kiss both"
        $ TempFocus += 1
    elif Options[0] == "kiss":
        $ line = line + " and gives you a passionate kiss"
        $ Action = "kiss"
        if "kiss girl" in Options:
            if Player.primary_Action == "kiss":
                $ Action = "kiss both"
            elif girl_secondary_Action == "kiss":
                $ Action = "kiss both"
            elif second_girl_main_action == "kiss":
                $ Action = "kiss both"
        $ TempLust += 1
        $ TempFocus += 1
    else:





        $ line = GirlA.name + " is just watching the two of you intently"
        $ Action = "watch"
        $ TempLust += 1 if GirlA.likes[GirlB.tag] >= 600 else 0
        $ TempLust += 2 if GirlA.likes[GirlB.tag] >= 800 else 1
        $ TempLust2 += 1 if approval_check(GirlB, 500, "I") else 0
        $ TempLust2 += 1 if approval_check(GirlB, 700, "I") else 0
        $ TempFocus += 1

    if Action == "kiss girl" or Action == "kiss both":

        if "lesbian" not in GirlA.recent_history:
            $ GirlA.permanent_History["been_with_girl"] += 1
            $ GirlA.recent_history.append("lesbian")
        if "lesbian" not in GirlB.recent_history:
            $ GirlB.permanent_History["been_with_girl"] += 1
            $ GirlB.recent_history.append("lesbian")
        $ TempLust += 1 if approval_check(GirlA, 500, "I") else 0
        $ TempLust += 1 if GirlA.likes[GirlB.tag] >= 800 else 0
        $ TempLust2 += 2 if GirlB.likes[GirlA.tag] >= 800 else 1
        $ TempFocus += 1


    if Preset:
        $ position_timer = round - 2
    else:

        $ position_timer = round - 1
    $ TempLust2 += 2
    if Mode == "lesbian":

        $ girl_secondary_Action = Action
        $ PrimaryLust += (TempLust*3)
        $ SecondaryLust += (TempLust2*3)
    elif Mode == "start":

        $ second_girl_main_action = Action
        $ GirlA.lust += TempLust2
    else:

        $ second_girl_main_action = Action
        $ SecondaryLust += TempLust
        $ PrimaryLust += TempLust2
    if Preset:

        $ GirlA.lust += TempLust
        $ GirlB.lust += TempLust2
    $ Player.climax += TempFocus

    return






label Dirty_Talk(Girl=Primary, D20=0, TempCheck=0, Templine=0, Temp_action=second_girl_main_action, ActiveGirl=0):




    if Player.primary_Action == "striptease" or not Player.primary_Action:

        return

    $ D20 = renpy.random.randint(1, 4)






















    if D20 == 1:

        return
    elif D20 == 4 and Partner in all_Girls:

        $ Girl = Partner
        $ ActiveGirl = Primary
        $ TempCheck = second_girl_main_action
        $ Temp_action = second_girl_main_action
    else:

        $ Girl = Primary
        $ ActiveGirl = Secondary
        $ TempCheck = Player.primary_Action
        $ Temp_action = girl_secondary_Action

    $ D20 = renpy.random.randint(1, 20)

    if "vocal" not in Girl.traits:

        if Girl.lust >= 60:
            pass
        else:
            return
    elif D20 >= 15 or Girl.session_orgasms >= 5:

        pass

    elif Girl == RogueX:

        if Player.primary_Action == "lesbian" or (Secondary == RogueX and Temp_action not in ("handjob", "blowjob", "masturbation")):


            if "unseen" not in RogueX.recent_history and D20 <= 5:

                $ Templine = "Hmm, enjoying the show, " +RogueX.player_petname + "?"
            elif D20 <= 10:
                pass
            elif Temp_action == "fondle_breasts":
                $ Templine = "Your titties feel so nice, " +ActiveGirl.name + "."
            elif Temp_action == "suck_breasts":
                $ Templine = "Your titties taste so good, " +ActiveGirl.name + "."
            elif Temp_action == "fondle_pussy":
                $ Templine = "You're sucking me in, " +ActiveGirl.name + "."
            elif Temp_action == "eat_pussy":
                $ Templine = "You taste so good, " +ActiveGirl.name + "."

            if not Templine:

                $ Templine = renpy.random.choice([
                                    "Touch'n ya is so amazing, " + ActiveGirl.name + "_.",
                                    "Your body feels so amazing. . .",
                                    "Mmmm. . .right there.",
                                    "Ya like that, " + ActiveGirl.name + "_?"
                                    ])

        elif TempCheck == "masturbation":
            if "unseen" not in RogueX.recent_history:

                if D20 <= 3:

                    if "cockout" in Player.recent_history:

                        $ Templine = renpy.random.choice([
                                                "Could I get some of that, " + RogueX.player_petname + "_?",
                                                "Why don'tcha bring that over here, " + RogueX.player_petname + "_?"
                                                ])
                    else:

                        $ Templine = renpy.random.choice([
                                                "Why so shy, " + RogueX.player_petname + "_?",
                                                "I'm showing mine, where's yours?"
                                                ])
                else:

                    $ Templine = renpy.random.choice([
                                                "I want ya so bad, " + RogueX.player_petname + "_.",
                                                "Come on over here, " + RogueX.player_petname + "_. Take me however ya want.",
                                                "Hmm, enjoying the show, " +RogueX.player_petname + "?",
                                                "I love the look you get on your face, " + RogueX.player_petname + "_."
                                                ])
        else:





            if D20 <= 10:
                pass
            elif RogueX.SEXP <= 20 or TempCheck == "kiss":

                $ Templine = renpy.random.choice([
                                    "Touching ya is so amazing, " + RogueX.player_petname + "_.",
                                    "Every time you touch me. . . it's like, I can't even put it into words.",
                                    "Mmmm. . .right there.",
                                    "Am I doing that right?",
                                    "Ya like that, " + RogueX.player_petname + "_?"
                                    ])
            elif TempCheck == "handjob":
                $ Templine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "Seems like you like my hand, huh, " + RogueX.player_petname + "_?",
                                    "I can feel you get harder in my hand. . .",
                                    ])
            elif TempCheck == "blowjob":
                $ Templine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "You taste so nice, " + RogueX.player_petname + "_.",
                                    "I can feel you get harder in my mouth. . .",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",
                                    ])
            elif TempCheck == "titjob":
                $ Templine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + RogueX.player_petname + "_.",
                                    "I can feel you get harder in there. . ."
                                    ])
            elif TempCheck == "sex" or TempCheck == "anal":
                if D20 <= 3 and TempCheck == "anal" and RogueX.used_to_anal <= 1:
                    $ Templine = "It. . .hurts. But it kinda feels good, too."
                else:
                    $ Templine = renpy.random.choice([
                                        "Your cock is so warm. . .",
                                        "Ohhh. . .that's sooo good.",
                                        "Ung, so deep. . .",
                                        "Keep it up, keep it up. . .",
                                        "Oh, don't stop. . .",
                                        "I can feel you get harder inside me. . ."
                                        ])

            if not Templine:

                if Primary == RogueX:
                    $ Templine = renpy.random.choice([
                                        "I want ya so bad, " + RogueX.player_petname + "_.",
                                        "Your touch is so amazin, " + RogueX.player_petname + "_.",
                                        "Oooh, right there. . .",
                                        "More, gimme more!",
                                        "I'm all yours, " + RogueX.player_petname + "_. Take me however ya want.",
                                        "I love it when ya do that, " + RogueX.player_petname + "_.",
                                        "I love the look you get on your face, " + RogueX.player_petname + "_."
                                        ])
                else:
                    $ Templine = renpy.random.choice([
                                        "I want ya so bad, " + RogueX.player_petname + "_.",
                                        "Could I get some of that, " + RogueX.player_petname + "_?",
                                        "Think ya could maybe share that, " + ActiveGirl.name + "_?",
                                        "Come on over here, " + RogueX.player_petname + "_. Take me however ya want.",
                                        "So that's what you look like from this angle.",
                                        "I love the look you get on your face, " + RogueX.player_petname + "_.",
                                        "That's right, give it to her.",
                                        "You're really getting into it, " + ActiveGirl.name + "_."
                                        ])

    elif Girl == KittyX:

        if Player.primary_Action == "lesbian" or (Secondary == KittyX and Temp_action not in ("handjob", "blowjob", "masturbation")):


            if "unseen" not in KittyX.recent_history and D20 <= 7:

                $ Templine = "Hmm, like what you see, " +KittyX.player_petname + "?"
            elif Temp_action == "fondle_breasts":
                if ActiveGirl in (EmmaX, StormX):
                    $ Templine = "I'm so jelly here " +ActiveGirl.name + "."
                else:
                    $ Templine = "I love these tits, " +ActiveGirl.name + "."
            elif Temp_action == "suck_breasts":
                if ActiveGirl in (EmmaX, StormX):
                    $ Templine = "These tits are {i}amazing,{/i} " +ActiveGirl.name + "."
                else:
                    $ Templine = "Hmm, you taste so good, " +ActiveGirl.name + "."
            elif Temp_action == "fondle_pussy":
                $ Templine = "So wet, " +ActiveGirl.name + "."
            elif Temp_action == "eat_pussy":
                if ActiveGirl == RogueX and RogueX.pubes:
                    $ Templine = "I love your little stripe, Rogue."
                else:
                    $ Templine = "You're drowning me here, " +ActiveGirl.name + "."

            if not Templine:

                $ Templine = renpy.random.choice([
                                    "You're so amazing, " + ActiveGirl.name + "_.",
                                    "You know how to push" + KittyX.like + "_every one of my buttons. . .",
                                    "Heh. . .{i}somebody{/i} seems to like that.",
                                    "That's" + KittyX.like + "_{i}so{/i} good.",
                                    "You taste so good. . ."
                                    ])

        elif TempCheck == "masturbation":
            if "unseen" not in KittyX.recent_history:

                if D20 <= 3:

                    if "cockout" in Player.recent_history:

                        $ Templine = renpy.random.choice([
                                                "Hmm, I'd like some of that, " + KittyX.player_petname + "_?",
                                                "Could I get a taste, " + KittyX.player_petname + "_?"
                                                ])
                    else:

                        $ Templine = renpy.random.choice([
                                                "Feeling shy, " + KittyX.player_petname + "_?",
                                                "How 'bout a little tat for tit?"
                                                ])
                else:

                    $ Templine = renpy.random.choice([
                                                "I really want you, " + KittyX.player_petname + "_.",
                                                "Come'ere, " + KittyX.player_petname + "_. Gimme a taste.",
                                                "Hmm, like the show, " +KittyX.player_petname + "?",
                                                "You look so cute over there, " + KittyX.player_petname + "_."
                                                ])
        else:





            if D20 <= 10:
                pass
            elif KittyX.SEXP <= 30 or TempCheck == "kiss":

                $ Templine = renpy.random.choice([
                                    "You're so amazing, " + KittyX.player_petname + "_.",
                                    "You know how to push, like, every one of my buttons. . .",
                                    "Heh. . .{i}somebody{/i} seems to like that.",
                                    "That's, like, {i}so{/i} good."
                                    ])
            elif TempCheck == "handjob":
                $ Templine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I love the way it" +KittyX.like + "feels in my hands.",
                                    "Seems like you like my hand, huh, " + RogueX.player_petname + "_?",
                                    "I can feel you get harder in my hand. . .",
                                    ])
            elif TempCheck == "blowjob":
                if D20 <= 3:
                    ch_k "I hope you don't think I'm[KittyX.like]a slut for saying this. . ."
                    $ Templine = "but I love how you taste, " + KittyX.player_petname + "_."
                else:
                    $ Templine = renpy.random.choice([
                                        "So warm. . .",
                                        "You taste so good, " + KittyX.player_petname + "_.",
                                        "You're getting harder in my mouth. . .",
                                        "Mmhmhm. . .",
                                        "-gulp-. . .",
                                        ])
            elif TempCheck == "titjob":
                $ Templine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + KittyX.player_petname + "_.",
                                    "I can feel you get harder in there. . ."
                                    ])
            elif TempCheck == "sex" or TempCheck == "anal":
                if D20 <= 3 and TempCheck == "anal" and KittyX.used_to_anal <= 1:
                    $ Templine = "Please. . .go slow, 'kay?  You feel so {i}big{/i}."
                else:
                    $ Templine = renpy.random.choice([
                                        "Your cock is so warm. . .",
                                        "Ohhh. . .that's sooo good.",
                                        "Mmm, you feel so huge. . .",
                                        "Ung, so deep. . .",
                                        "Oooohh. . .just like {i}that{/i}.",
                                        "Keep it up, keep it up. . .",
                                        "Oh, don't stop. . .",
                                        "Did you just get harder?"
                                        ])

            if not Templine:

                if Primary == KittyX:
                    $ Templine = renpy.random.choice([
                                            "This is {i}so{/i} hot, " + KittyX.player_petname + "_.",
                                            "I think I just" +KittyX.like + "discovered one of your other mutant powers, " + KittyX.player_petname + "_.",
                                            "I like it." +KittyX.Like + "a {i}lot{/i}.",
                                            "Oooh, that's it. . .",
                                            "More, gimme more!",
                                            "You're looking so cute, " +KittyX.player_petname + "_!",
                                            "I've never wanted a guy like I want you, " + KittyX.player_petname + "_."
                                            ])
                else:
                    $ Templine = renpy.random.choice([
                                            "Don't take all the fun, " + ActiveGirl.name + "_.",
                                            "I could use some attention over here, " + KittyX.player_petname + "_.",
                                            "I got something over here for you, " + KittyX.player_petname + "_.",
                                            "You're looking pretty good from over here.",
                                            "Looks like he likes the way you do that.",
                                            "Make sure you save some for {i}me{/i}!",
                                            "You two look {i}so{/i} sexy doing that.",
                                            "I can't believe you can take all of him like that!",
                                            "That looks like fun, " + ActiveGirl.name + "_."
                                            ])

    elif Girl == EmmaX:

        if Player.primary_Action == "lesbian" or (Secondary == EmmaX and Temp_action not in ("handjob", "blowjob", "masturbation")):


            if "unseen" not in EmmaX.recent_history and D20 <= 5:

                $ Templine = "Are you enjoying the performance, " +EmmaX.player_petname + "?"
            elif Temp_action == "fondle_breasts" or Temp_action == "suck_breasts":
                if ActiveGirl == KittyX:
                    $ Templine = "Oh my, these breasts are adorable!"
                else:
                    $ Templine = "These really are wonderfully. . . pert."
            elif Temp_action == "fondle_pussy":
                $ Templine = "Such pressure, " +ActiveGirl.name + "."
            elif Temp_action == "eat_pussy":
                if ActiveGirl == LauraX:
                    $ Templine = "Oh yes, that is a Howlett."
                else:
                    $ Templine = "What an exotic flavor, " + ActiveGirl.name + "_."
            if not Templine:

                $ Templine = renpy.random.choice([
                                    "Incredible, " + ActiveGirl.name + "_.",
                                    "You're surprisingly skilled at this. . .",
                                    "Well, that certainly got a positive response.",
                                    "Exceptional, darling.",
                                    "Delicious. . ."
                                    ])

        elif TempCheck == "masturbation":
            if "unseen" not in EmmaX.recent_history:

                if D20 <= 3:

                    if "cockout" in Player.recent_history:

                        $ Templine = renpy.random.choice([
                                                "Oh, I could use some of that, " + EmmaX.player_petname + "_.",
                                                "Why don't you join me over here, " + EmmaX.player_petname + "_?"
                                                ])
                    else:

                        $ Templine = renpy.random.choice([
                                                "Feeling shy, " + EmmaX.player_petname + "_?",
                                                "I feel like you aren't enjoying the show."
                                                ])
                else:

                    $ Templine = renpy.random.choice([
                                                "I need you over here, " + EmmaX.player_petname + "_.",
                                                "Come here, " + EmmaX.player_petname + "_. Take me.",
                                                "I hope you're enjoying the show, " +EmmaX.player_petname + ".",
                                                "I do love the look on your face, " + EmmaX.player_petname + "_."
                                                ])
        else:





            if D20 <= 10:
                pass
            elif EmmaX.SEXP <= 30 or TempCheck == "kiss":

                $ Templine = renpy.random.choice([
                                    "You're incredible, " + EmmaX.player_petname + "_.",
                                    "You're surprisingly skilled at this. . .",
                                    "Well, that certainly got a positive response.",
                                    "Exceptional work, darling.",
                                    ])
            elif TempCheck == "handjob":
                $ Templine = renpy.random.choice([
                                    "Your cock is so very warm. . .",
                                    "I trust you're enjoying the massage?",
                                    "I take it you're enjoying yourself, " + EmmaX.player_petname + "_?",
                                    "I can feel you grow harder. . .",
                                    ])
            elif TempCheck == "blowjob":
                $ Templine = renpy.random.choice([
                                    "So delicious. . .",
                                    "I must say, I enjoy the flavor, " + EmmaX.player_petname + "_.",
                                    "I can feel you get harder in my mouth. . .",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",
                                    ])
            elif TempCheck == "titjob":
                $ Templine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + EmmaX.player_petname + "_.",
                                    "Don't get lost in there now . .",
                                    "I can feel you get harder in there. . ."
                                    ])
            elif TempCheck == "sex" or TempCheck == "anal":
                $ Templine = renpy.random.choice([
                                    "Mmmm, give me more like that. . .",
                                    "Nngh, how filling. . .",
                                    "Ung, so deep. . .",
                                    "Keep it up, keep it up. . .",
                                    "Oh, don't stop. . .",
                                    "I can feel you get harder inside me. . ."
                                    ])

            if not Templine:

                if Primary == EmmaX:
                    $ Templine = renpy.random.choice([
                                        "I'm overwhelmed, " + EmmaX.player_petname + "_.",
                                        "Well now we have another skill to develop, " + EmmaX.player_petname + "_.",
                                        "Oooh, that's lovely. . .",
                                        "More, I want more!",
                                        "You're simply adorable, " + EmmaX.player_petname + "_.",
                                        "Ooh, you'll {i}have{/i} to do that one again. . .",
                                        "You certainly do leave an impression, " + EmmaX.player_petname + "_."
                                        ])
                else:
                    $ Templine = renpy.random.choice([
                                        "Oh " + EmmaX.player_petname + "_? Don't keep me waiting.",
                                        "Oh " + ActiveGirl.name + "_? Could you share some of that?",
                                        "Come on over here, " + EmmaX.player_petname + "_, ravish me.",
                                        "You certainly do put on a show.",
                                        "You're simply adorable, " + EmmaX.player_petname + "_.",
                                        "Nngh, give it to her.",
                                        "You seem to be enjoying yourself, " + ActiveGirl.name + "_."
                                        ])


    elif Girl == LauraX:

        if approval_check(LauraX, 1500):
            $ D20 -= 5
        elif approval_check(LauraX, 1200):
            $ D20 -= 3
        if D20 >= 10:

            pass
        elif Player.primary_Action == "lesbian" or (Secondary == LauraX and Temp_action not in ("handjob", "blowjob", "masturbation")):


            if "unseen" not in LauraX.recent_history and D20 <= 5:

                $ Templine = "Looking good, " +LauraX.player_petname + "?"
            elif Temp_action == "fondle_breasts":
                if ActiveGirl in (EmmaX, StormX):
                    $ Templine = "These things are huge."
                else:
                    $ Templine = "Your titties feel so nice, " +ActiveGirl.name + "."
            elif Temp_action == "suck_breasts":
                $ Templine = "Hmm, tasty."
            elif Temp_action == "fondle_pussy":
                $ Templine = "Cozy in there."
            elif Temp_action == "eat_pussy":
                if ActiveGirl == RogueX:
                    $ Templine = "Spicy."
                elif ActiveGirl == KittyX:
                    $ Templine = "Hmm, sweet."
                elif ActiveGirl == EmmaX:
                    $ Templine = "So many different flavors."
                elif ActiveGirl == JeanX:
                    $ Templine = "Huh, tangy."
                elif ActiveGirl == StormX:
                    $ Templine = "Very rich flavor."
                elif ActiveGirl == JubesX:
                    $ Templine = "Nice, very smooth."
            if not Templine:

                $ Templine = renpy.random.choice([
                                    "Good job, " + ActiveGirl.name + "_.",
                                    "You know what you're doing. . .",
                                    "Oooh, I liked that one.",
                                    "Great work.",
                                    "Tasty. . ."
                                    ])

        elif TempCheck == "masturbation":
            if "unseen" not in LauraX.recent_history:

                if D20 <= 3:

                    if "cockout" in Player.recent_history:

                        $ Templine = renpy.random.choice([
                                                "Hey, don't let that go to waste.",
                                                "Come here, " + LauraX.player_petname + "_."
                                                ])
                    else:

                        $ Templine = renpy.random.choice([
                                                "You aren't shy, are you " + LauraX.player_petname + "_?",
                                                "Pants, lose'em."
                                                ])
                else:

                    $ Templine = renpy.random.choice([
                                                "Get over here, " + LauraX.player_petname + "_.",
                                                "Not enjoying the show, " +LauraX.player_petname + "?",
                                                "Heh, the look on your face, " + LauraX.player_petname + "_."
                                                ])
        else:





            if D20 <= 5:
                pass
            elif LauraX.SEXP <= 30 or TempCheck == "kiss":

                $ Templine = renpy.random.choice([
                                    "You're good at this, " + LauraX.player_petname + "_.",
                                    "Huh, you seem to know what you're doing. . .",
                                    "Oh, hey down there.",
                                    "Hmm, like that.",
                                    ])
            elif TempCheck == "handjob":
                $ Templine = renpy.random.choice([
                                    "Hmm, your dick's so warm. . .",
                                    "This working for you?",
                                    "Seems like you're having fun, " + LauraX.player_petname + "_?",
                                    "You seem to be getting harder. . .",
                                    ])
            elif TempCheck == "blowjob":
                $ Templine = renpy.random.choice([
                                    "Mmm, delicious. . .",
                                    "That's an interesting taste, " + LauraX.player_petname + "_.",
                                    "Did you just get harder? . .",
                                    "-Slurp.-",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",
                                    ])
            elif TempCheck == "titjob":
                $ Templine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + LauraX.player_petname + "_.",
                                    "I can feel you get harder in there. . ."
                                    ])
            elif TempCheck == "sex" or TempCheck == "anal":
                $ Templine = renpy.random.choice([
                                    "Mmmm, yeah, gimme more like that. . .",
                                    "Nngh, how filling. . .",
                                    "Ung, so deep. . .",
                                    "Keep it up, keep it up. . .",
                                    "Ngh, don't stop. . .",
                                    "That's right, harder, faster. . ."
                                    ])

            if not Templine:

                if Primary == LauraX:
                    $ Templine = renpy.random.choice([
                                        "Wow, " + LauraX.player_petname + "_.",
                                        "That's great, " + LauraX.player_petname + "_.",
                                        "Oooh, that's nice. . .",
                                        "More!",
                                        "You're great, " + LauraX.player_petname + "_.",
                                        "Ok, that was a good one. . ."
                                        ])
                else:
                    $ Templine = renpy.random.choice([
                                        "Hey, " + LauraX.player_petname + "_? Don't keep me waiting.",
                                        "Hey, " + ActiveGirl.name + "_? Share, uh?",
                                        "Get over here, " + LauraX.player_petname + "_.",
                                        "Well you certainly put on a show.",
                                        "You're looking hot, " + LauraX.player_petname + "_.",
                                        "You're looking hot, " + ActiveGirl.name + "_.",
                                        "Nngh, yeah, stick it to her.",
                                        "Well you seem to be having fun, " + ActiveGirl.name + "_."
                                        ])


    elif Girl == JeanX:

        if approval_check(JeanX, 1500):
            $ D20 -= 5
        elif approval_check(JeanX, 1200):
            $ D20 -= 3
        if D20 >= 10:

            pass
        elif Player.primary_Action == "lesbian" or (Secondary == JeanX and Temp_action not in ("handjob", "blowjob", "masturbation")):


            if "unseen" not in JeanX.recent_history and D20 <= 5:

                $ Templine = "Enjoying the show, " +JeanX.player_petname + "?"
            elif Temp_action == "fondle_breasts":
                if ActiveGirl == EmmaX:
                    $ Templine = "How do you even cart these things around?"
                else:
                    $ Templine = "Mmm, these things are firm, " +ActiveGirl.name + "."
            elif Temp_action == "suck_breasts":
                $ Templine = "Mmmm, tasty."
            elif Temp_action == "fondle_pussy":
                $ Templine = "You like that, slut?"







            if not Templine:

                $ Templine = renpy.random.choice([
                                    "Keep up the pace, " + ActiveGirl.name + "_.",
                                    "Oh, good job there. . .",
                                    "Oooh, That was a good one.",
                                    "Good work.",
                                    "Tasty. . ."
                                    ])

        elif TempCheck == "masturbation":
            if "unseen" not in JeanX.recent_history:

                if D20 <= 3:

                    if "cockout" in Player.recent_history:

                        $ Templine = renpy.random.choice([
                                                "Hey, bring that one over here. . .",
                                                "Come here, " + JeanX.player_petname + "_."
                                                ])
                    else:

                        $ Templine = renpy.random.choice([
                                                "Why're you having all the fun " + JeanX.player_petname + "_?",
                                                "Hey, let me see that beautiful boy."
                                                ])
                else:

                    $ Templine = renpy.random.choice([
                                                "Get over here, " + JeanX.player_petname + "_.",
                                                "Not enjoying the show, " +JeanX.player_petname + "?",
                                                "The look on your face, " + JeanX.player_petname + "_."
                                                ])
        else:





            if D20 <= 5:
                pass
            elif JeanX.SEXP <= 30 or TempCheck == "kiss":

                $ Templine = renpy.random.choice([
                                    "You're good at this, " + JeanX.player_petname + "_.",
                                    "Huh, you seem to know what you're doing. . .",
                                    "Oh, hey down there.",
                                    "Hmm, like that.",
                                    ])
            elif TempCheck == "handjob":
                $ Templine = renpy.random.choice([
                                    "Hmm, your dick's so warm. . .",
                                    "This working for you?",
                                    "Seems like you're having fun, " + JeanX.player_petname + "_?",
                                    "You seem to be getting harder. . .",
                                    ])
            elif TempCheck == "blowjob":
                $ Templine = renpy.random.choice([
                                    "Mmm, delicious. . .",
                                    "That's an interesting flavor, " + JeanX.player_petname + "_.",
                                    "Did you just get harder? . .",
                                    "-Slurp.-",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",
                                    ])
            elif TempCheck == "titjob":
                $ Templine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + JeanX.player_petname + "_.",
                                    "I can feel you get harder in there. . ."
                                    ])
            elif TempCheck == "sex" or TempCheck == "anal":
                $ Templine = renpy.random.choice([
                                    "Mmmm, yeah, gimme more like that. . .",
                                    "Nngh, how filling. . .",
                                    "Ung, so deep. . .",
                                    "Keep it up, keep it up. . .",
                                    "Ngh, don't stop. . .",
                                    "That's right, harder, faster. . ."
                                    ])

            if not Templine:

                if Primary == JeanX:
                    $ Templine = renpy.random.choice([
                                        "Wow, " + JeanX.player_petname + "_.",
                                        "That's great, " + JeanX.player_petname + "_.",
                                        "Oooh, that's nice. . .",
                                        "More!",
                                        "You're great, " + JeanX.player_petname + "_.",
                                        "Ok, that was a good one. . ."
                                        ])
                else:
                    $ Templine = renpy.random.choice([
                                        "Hey, " + JeanX.player_petname + "_? Don't keep me waiting.",
                                        "Hey, " + ActiveGirl.name + "_? Share, uh?",
                                        "Get over here, " + JeanX.player_petname + "_.",
                                        "Well you certainly put on a show.",
                                        "You're looking hot, " + JeanX.player_petname + "_.",
                                        "You're looking hot, " + ActiveGirl.name + "_.",
                                        "Nngh, yeah, stick it to her.",
                                        "Well you seem to be having fun, " + ActiveGirl.name + "_."
                                        ])

    elif Girl == StormX:

        if Player.primary_Action == "lesbian" or (Secondary == StormX and Temp_action not in ("handjob", "blowjob", "masturbation")):


            if "unseen" not in StormX.recent_history and D20 <= 5:

                $ Templine = "So you do enjoy watching, " +StormX.player_petname + "?"
            elif Temp_action == "fondle_breasts" or Temp_action == "suck_breasts":
                if ActiveGirl == EmmaX:
                    $ Templine = "These really are quite impressive, Emma."
                else:
                    $ Templine = "So firm. . ."
            elif Temp_action == "fondle_pussy":
                $ Templine = "Do you enjoy that, " +ActiveGirl.name + "."
            elif Temp_action == "eat_pussy":
                if ActiveGirl == LauraX:
                    $ Templine = "Hmmm, that is a familiar taste. . ."
                else:
                    $ Templine = "What an exotic flavor, " + ActiveGirl.name + "_."
            if not Templine:

                $ Templine = renpy.random.choice([
                                    "Oh, " + ActiveGirl.name + "_.",
                                    "You are -very- skilled. . .",
                                    "Oh, you appear to have enjoyed that. . .",
                                    "Exceptional!",
                                    "Delicious. . ."
                                    ])

        elif TempCheck == "masturbation":
            if "unseen" not in StormX.recent_history:

                if D20 <= 3:

                    if "cockout" in Player.recent_history:

                        $ Templine = renpy.random.choice([
                                                "Oh, I could use some help here, " + StormX.player_petname + "_.",
                                                "Why do you not join me over here, " + StormX.player_petname + "_?"
                                                ])
                    else:

                        $ Templine = renpy.random.choice([
                                                "Do not be shy, " + StormX.player_petname + "_.",
                                                "Are you not enjoying the show?"
                                                ])
                else:

                    $ Templine = renpy.random.choice([
                                                "I need you over here, " + StormX.player_petname + "_.",
                                                "Come here, " + StormX.player_petname + "_. Take me.",
                                                "Are you not enjoying the show, " +StormX.player_petname + "?",
                                                "I do love the look on your face, " + StormX.player_petname + "_."
                                                ])
        else:





            if D20 <= 10:
                pass
            elif StormX.SEXP <= 30 or TempCheck == "kiss":

                $ Templine = renpy.random.choice([
                                    "You are incredible, " + StormX.player_petname + "_.",
                                    "You are quite skilled at this. . .",
                                    "You appear to have enjoyed that. . .",
                                    "Exceptional!",
                                    ])
            elif TempCheck == "handjob":
                $ Templine = renpy.random.choice([
                                    "Your cock is so very warm. . .",
                                    "You appear to be enjoying the massage?",
                                    "You appear to be enjoying yourself, " + StormX.player_petname + "_?",
                                    "I can feel you grow harder. . .",
                                    ])
            elif TempCheck == "blowjob":
                $ Templine = renpy.random.choice([
                                    "So delicious. . .",
                                    "I do enjoy this flavor, " + StormX.player_petname + "_.",
                                    "I can feel you get harder in my mouth. . .",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",
                                    ])
            elif TempCheck == "titjob":
                $ Templine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + StormX.player_petname + "_.",
                                    "Do not get lost in there now . .",
                                    "I can feel you get harder in there. . ."
                                    ])
            elif TempCheck == "sex" or TempCheck == "anal":
                $ Templine = renpy.random.choice([
                                    "Mmmm, more like that. . .",
                                    "Nngh, how. . . filling. . .",
                                    "Ung, so deep. . .",
                                    "Keep it up, keep it up. . .",
                                    "Oh, don't stop. . .",
                                    "I can feel you get harder inside me. . ."
                                    ])

            if not Templine:

                if Primary == StormX:
                    $ Templine = renpy.random.choice([
                                        "I am overwhelmed, " + StormX.player_petname + "_.",
                                        "You are coming along quite nicely, " + StormX.player_petname + "_.",
                                        "Oooh, that is magnificent. . .",
                                        "More, I want more. . .",
                                        "You are simply -adorable, - " + StormX.player_petname + "_.",
                                        "You will {i}have{/i} to do that one again. . .",
                                        "You do leave an impression, " + StormX.player_petname + "_."
                                        ])
                else:
                    $ Templine = renpy.random.choice([
                                        "Do not keep me waiting, " + StormX.player_petname + "_.",
                                        ActiveGirl.name + "_? Could you please share some of that?",
                                        "Come here, " + StormX.player_petname + "_, ravish me.",
                                        "You certainly do put on a show.",
                                        "You are simply adorable, " + StormX.player_petname + "_.",
                                        "Nngh, give it to her.",
                                        "You seem to be enjoying yourself, " + ActiveGirl.name + "_."
                                        ])



    elif Girl == JubesX:

        if D20 >= 10:

            pass
        elif Player.primary_Action == "lesbian" or (Secondary == JubesX and Temp_action not in ("handjob", "blowjob", "masturbation")):


            if "unseen" not in JubesX.recent_history and D20 <= 5:

                $ Templine = "Like what you see there, " +JubesX.player_petname + "?"
            elif Temp_action == "fondle_breasts":
                if ActiveGirl in (EmmaX, StormX):
                    $ Templine = "Wow, how do you work with these. . ."
                else:
                    $ Templine = "Maybe I need to find a new bra, " +ActiveGirl.name + "."
            elif Temp_action == "suck_breasts":
                $ Templine = "Hmm, hard not to take a nibble. . ."
            elif Temp_action == "fondle_pussy":
                $ Templine = "You're burning up. . ."
            elif Temp_action == "eat_pussy":
                if ActiveGirl == RogueX:
                    $ Templine = "So hot. . ."
                elif ActiveGirl == KittyX:
                    $ Templine = "Mmmm, sweet."
                elif ActiveGirl == EmmaX:
                    $ Templine = "So rich. . ."
                elif ActiveGirl == JeanX:
                    $ Templine = "Well, that's not bad. . ."
                elif ActiveGirl == StormX:
                    $ Templine = "Mmm. . . lovely. . ."
            if not Templine:

                $ Templine = renpy.random.choice([
                                    "Nice job, " + ActiveGirl.name + "_.",
                                    "You're hitting all the right places. . .",
                                    "Ooo! More of that. . .",
                                    "Great job.",
                                    "Yum. . ."
                                    ])

        elif TempCheck == "masturbation":
            if "unseen" not in JubesX.recent_history:

                if D20 <= 3:

                    if "cockout" in Player.recent_history:

                        $ Templine = renpy.random.choice([
                                                "Hey, let me in on that. . .",
                                                "Get over here, " + JubesX.player_petname + "_."
                                                ])
                    else:

                        $ Templine = renpy.random.choice([
                                                "Don't be shy, " + JubesX.player_petname + "_.",
                                                "Let me see what you're working with there. . ."
                                                ])
                else:

                    $ Templine = renpy.random.choice([
                                                "Get over here, " + JubesX.player_petname + "_.",
                                                "Don't you want in on this, " +JubesX.player_petname + "?",
                                                "Heh, you need to join me over here, " + JubesX.player_petname + "_."
                                                ])
        else:





            if D20 <= 5:
                pass
            elif JubesX.SEXP <= 30 or TempCheck == "kiss":

                $ Templine = renpy.random.choice([
                                    "Oh, um, you seem to know what you're doing, " + JubesX.player_petname + "_.",
                                    "Ohh. . . that's nice. . .",
                                    "Oh, nice. . .",
                                    "Hmm, do that one again. . .",
                                    ])
            elif TempCheck == "handjob":
                $ Templine = renpy.random.choice([
                                    "Hmm, your cock's so warm. . .",
                                    "Do you like this?",
                                    "You seem to be having fun, " + JubesX.player_petname + "_. . .",
                                    "Mmmm, you're getting harder in my hand. . .",
                                    ])
            elif TempCheck == "blowjob":
                $ Templine = renpy.random.choice([
                                    "Mmm, delicious. . .",
                                    "I can't believe how you taste, " + JubesX.player_petname + "_.",
                                    "You're really firming up. . .",
                                    "-Slurp.-",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",
                                    ])
            elif TempCheck == "titjob":
                $ Templine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + JubesX.player_petname + "_.",
                                    "I can feel you get harder in there. . ."
                                    ])
            elif TempCheck == "sex" or TempCheck == "anal":
                $ Templine = renpy.random.choice([
                                    "Gimme more. . . & more. . .",
                                    "Nngh, filling me. . .",
                                    "Ung, deeper and deeper. . .",
                                    "Keep it up, keep it up. . .",
                                    "Ngh, don't stop. . .",
                                    "Ngh, harder, harder. . ."
                                    ])

            if not Templine:

                if Primary == JubesX:
                    $ Templine = renpy.random.choice([
                                        "Wowow, " + JubesX.player_petname + "_.",
                                        "More like that, " + JubesX.player_petname + "_.",
                                        "Mmmm, that's nice. . .",
                                        "Gimme more!",
                                        "You're amazing, " + JubesX.player_petname + "_.",
                                        "Oooo. . . that was a good one. . ."
                                        ])
                else:
                    $ Templine = renpy.random.choice([
                                        "Hey, " + JubesX.player_petname + "_? Don't leave me waiting.",
                                        "Hey, " + ActiveGirl.name + "_? Let me in?",
                                        "Get over here, " + JubesX.player_petname + "_.",
                                        "Well. . . your certainly putting on a show.",
                                        "You're looking great there, " + JubesX.player_petname + "_.",
                                        "You're looking great there, " + ActiveGirl.name + "_.",
                                        "Nngh, oh yeah, get in there.",
                                        "Well that looks like a lot of fun, " + ActiveGirl.name + "_."
                                        ])


    if not Templine:

        if not ActiveGirl or second_girl_main_action == "masturbation":
            $ Templine = Girl.player_petname
        else:
            $ Templine = ActiveGirl.name
        $ Templine = renpy.random.choice([
                    "Mmmh. . .",
                    "Ung. . .",
                    "Ooooh. . .",
                    "Oooh, " + Templine + "_, yes. . ."
                    ])

    Girl.voice "[Templine]"













    return





label Sex_Basic_Dialog(Girl=0, Type=0):


    if Girl not in all_Girls:
        return
    if Girl == RogueX:
        if Type == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Type == 5:
            ch_r "Seriously, it'll be time to stop soon."
        elif Type == "done":
            ch_r "Ok, [Girl.player_petname], that's enough of that for now."
        elif Type == "tired":
            if not multi_action:
                ch_r "Look, I think we can stay on this one thing. . ."
            else:
                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"
        elif Type == "switch":
            ch_r "Mmm, so what else did you have in mind?"
        elif Type == "partner":
            ch_r "Sorry about that."
        elif Type == "swallowgood":
            ch_r "That was real sweet, [Girl.player_petname]."
        elif Type == "swallowfirst":
            ch_r "I'm not really a fan of that, [Girl.player_petname]."
        elif Type == "swallow2":
            ch_r "I'm starting to get used to that."
        elif Type == "warned":
            ch_r "Thanks for the head's up."
        elif Type == "notwarned":
            ch_r "I could use a warning next time. . ."


    elif Girl == KittyX:
        if Type == 10:
            ch_k "It's[KittyX.like]getting kinda late."
        elif Type == 5:
            ch_k "We should wrap this up."
        elif Type == "done":
            ch_k "Time to take a little break, for now."
        elif Type == "tired":
            if not multi_action:
                ch_k "Let's just. . . stick with this. . ."
            else:
                ch_k "I kinda need a break, so if we could wrap this up?"
        elif Type == "switch":
            ch_k "Mmm, so what else did you have in mind?"
        elif Type == "partner":
            ch_k "Well that was awkward."
        elif Type == "swallowgood":
            ch_k "Mmm, creamy."
        elif Type == "swallowfirst":
            ch_k "Kinda nasty, [Girl.player_petname]."
        elif Type == "swallow2":
            ch_k "I'm starting to get used to that."
        elif Type == "warned":
            ch_k "Thanks for the warning."
        elif Type == "notwarned":
            ch_k "You coulda warned me first."


    elif Girl == EmmaX:
        if Type == 10:
            ch_e "It's getting late. . ."
        elif Type == 5:
            ch_e "We should take a break soon."
        elif Type == "done":
            ch_e "We need to stop for a moment, let me catch my breath."
        elif Type == "tired":
            if not multi_action:
                ch_e "Focus on what we're doing, [Girl.player_petname]."
            else:
                ch_e "I could use a break, are you about finished here?"
        elif Type == "switch":
            ch_e "Ok then, what were you thinking?"
        elif Type == "partner":
            ch_e "Hmm, that was uncomfortable."
        elif Type == "swallowgood":
            ch_e "Delectable, [Girl.player_petname]."
        elif Type == "swallowfirst":
            ch_e "I can't say that it would be my favorite flavor. . ."
        elif Type == "swallow2":
            ch_e "It does grow on you. . ."
        elif Type == "warned":
            ch_e "I appreciate the warning."
        elif Type == "notwarned":
            ch_e "I should be upset, but I can't say I didn't enjoy that. . ."


    elif Girl == LauraX:
        if Type == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Type == 5:
            ch_l "Tic tock, [Girl.player_petname]."
        elif Type == "done":
            ch_l "Ok, [Girl.player_petname], breaktime."
        elif Type == "tired":
            if not multi_action:
                ch_l "Nah, let's just stick to this."
            else:
                ch_l "Maybe we could finish this up for now?"
        elif Type == "switch":
            ch_l "Ok then, what next?"
        elif Type == "partner":
            ch_l "I wonder if she's coming back."
        elif Type == "swallowgood":
            ch_l "Yum."
        elif Type == "swallowfirst":
            ch_l "That's. . . intense. . ."
        elif Type == "swallow2":
            ch_l "Mmmmm. . ."
        elif Type == "warned":
            ch_l "Thanks for the heads up."
        elif Type == "notwarned":
            ch_l "Why didn't you warn me?"


    elif Girl == JeanX:
        if Type == 10:
            ch_j "Wow, look at the time. . ."
        elif Type == 5:
            ch_j "We should probably wrap this up, [Girl.player_petname]."
        elif Type == "done":
            ch_j "Ok, [Girl.player_petname], time for a break."
        elif Type == "tired":
            if not multi_action:
                ch_j "I'd rather just stick to this."
            else:
                ch_j "Keep your eye on the prize. . ."
        elif Type == "switch":
            ch_j "Ok, what'd you have in mind?"
        elif Type == "partner":
            ch_j "I'm sure she'll be missed."
        elif Type == "swallowgood":
            ch_j "Mmm. . ."
        elif Type == "swallowfirst":
            ch_j "Mmm. . . robust. . ."
        elif Type == "swallow2":
            ch_j "Mmm. . ."
        elif Type == "warned":
            pass
        elif Type == "notwarned":
            ch_j "Warn me next thing though?"


    elif Girl == StormX:
        if Type == 10:
            ch_s "It is getting late, [Girl.player_petname]. . ."
        elif Type == 5:
            ch_s "We should take a break soon."
        elif Type == "done":
            ch_s "I need to take a moment to collect myself."
        elif Type == "tired":
            if not multi_action:
                ch_s "I would prefer to finish this."
            else:
                ch_s "Why not finish off here first?"
        elif Type == "switch":
            ch_s "Very well, what were you thinking?"
        elif Type == "partner":
            ch_s "I am sorry for the awkwardness."
        elif Type == "swallowgood":
            ch_s "That is. . . delicious. . ."
        elif Type == "swallowfirst":
            ch_s "How. . . interesting. . ."
        elif Type == "swallow2":
            ch_s "Mmmm. . ."
        elif Type == "warned":
            ch_s "I appreciate the warning. . ."
        elif Type == "notwarned":
            ch_s "I could have been warned. . ."


    elif Girl == JubesX:
        if Type == 10:
            ch_v "I could use a break soon. . ."
        elif Type == 5:
            ch_v ". . . I could really use a break here. . ."
        elif Type == "done":
            ch_v "Ok, that's it, I need a break."
        elif Type == "tired":
            if not multi_action:
                ch_v "Let's just keep doing this for a bit. . ."
            else:
                ch_v "Maybe we could wrap it up?"
        elif Type == "switch":
            ch_v "Ok then, what else?"
        elif Type == "partner":
            ch_v "Aw, that's a bummer. Anyway. . ."
        elif Type == "swallowgood":
            $ Girl.eyes = "closed"
            ch_v "Mmmmmmmm. . ."
            ch_v ". . ."
            $ Girl.eyes = "squint"
            ch_v "Ok. . ."
        elif Type == "swallowfirst":
            $ Girl.eyes = "closed"
            ch_v "Mmmmmmmm. . ."
            $ Girl.eyes = "surprised"
            ch_v "Wow! . . that's. . . incredible. . ."
            $ Girl.eyes = "squint"
            ch_v "Ok. . ."
        elif Type == "swallow2":
            $ Girl.eyes = "closed"
            ch_v "Mmmmmmmm. . ."
            ch_v ". . ."
            $ Girl.eyes = "squint"
            ch_v "Ok. . ."
        elif Type == "warned":
            ch_v "Thanks for the heads up. . ."
        elif Type == "notwarned":
            ch_v "You coulda warned me though. . ."

    return



label pulls_off_top_narration(Girl):
    if Girl == RogueX:
        "[Girl.name] shrugs and pulls her top open."
    elif Girl == KittyX:
        "[Girl.name] laughs and pulls her top open."
    elif Girl in [EmmaX, StormX]:
        "[Girl.name] sighs and tugs her breasts free of her clothes."
    elif Girl in [LauraX, JeanX, JubesX]:
        "[Girl.name] grunts and pulls her clothes aside."

    return

label auto_action_narrations(Girl, action):
    if action == "dildo_pussy":
        "You rub the dildo across her body, and along her moist slit."

        $ Girl.change_face("surprised", 1)
    elif action == "dildo_ass":
        "You rub the dildo across her body, and against her tight anus."

        $ Girl.change_face("surprised", 1)
    elif action == "sex":
        $ Girl.pose = "doggy"

        call show_sex(Girl, action)

        if Girl.wearing_skirt:
            "You press up against [Girl.name]'s backside, sliding her skirt up as you go."

            $ Girl.upskirt = True
        elif Girl.wearing_pants:
            "You press up against [Girl.name]'s backside, sliding her pants down as you do."

            $ Girl.Outfit.remove_Clothing(["pants", "skirt"])
        else:
            "You press up against [Girl.name]'s backside."

        $ Girl.seen_underwear = True

        "You rub the tip of your cock against her moist slit."

        $ Girl.change_face("surprised", 1)
    elif action == "anal":
        $ Girl.pose = "doggy"

        call show_sex(Girl, action)

        if Girl.wearing_skirt:
            "You press up against [Girl.name]'s backside, sliding her skirt up as you go."

            $ Girl.upskirt = True
        elif Girl.wearing_pants:
            "You press up against [Girl.name]'s backside, sliding her pants down as you do."

            $ Girl.Outfit.remove_Clothing(["pants", "skirt"])
        else:
            "You press up against [Girl.name]'s backside."

        $ Girl.seen_underwear = True

        "You press the tip of your cock against her tight rim."

        $ Girl.change_face("surprised", 1)
    elif action == "hotdog":
        $ Girl.pose = "doggy"

        call show_sex(Girl, action)

        "You press up against [Girl.name]'s backside."

        $ Girl.change_face("surprised", 1)

    return

label kissing_narrations(Girl):
    if Girl.permanent_History["kiss"] >= 10 and Girl.lust >= 80:
        $ line = renpy.random.choice(["She's all over you, running her hands along your body.",
            "She's all over you, licking all over your face and neck.",
            "She's all over you, kissing all over your face and grinding against you."])
    elif Girl.permanent_History["kiss"] > 7:
        $ line = renpy.random.choice(["She's really sucking face.",
            "You kiss deeply and passionately.",
            "You kiss deeply and passionately.",
            "You kiss deeply and passionately."])
    elif Girl.permanent_History["kiss"] > 3:
        $ line = renpy.random.choice(["She's really getting into it.",
            "She's really getting into it, her tongue's going at it.",
            "She's really getting into it, there's some heavy tongue action."])
    else:
        $ line = "You and " + Girl.name  + " make out for a while."

    "[line]"

    return


label start_of_sex_narration(Girl, action):
    $ check_line = renpy.random.choice(["glances around for voyeurs",
        "glances around to see if anyone notices what she's doing"])

    $ first_undressing_line = renpy.random.choice(["hesitantly pulls down your pants"])
    $ undressing_line = renpy.random.choice(["pulls down your pants"])

    if action == "sex":
        $ first_action_line = renpy.random.choice(["slowly presses against your rigid member"])

        $ action_line = renpy.random.choice(["climbs on top of you",
            "pushes you back and slowly presses against your rigid member",
            "lays back and slowly presses against your rigid member",
            "turns around and slowly presses against your rigid member",
            "bends over and presses her backside against you suggestively",
            "backs her ass up against your cock"])

        $ player_first_action_line = renpy.random.choice(["You guide it into place and slide it in",
            "You press her folds aside and nudge your cock in",
            "You take careful aim and then push your cock in"])

        $ player_action_line = renpy.random.choice(["You guide your cock into place and ram it home",
            "You guide it into place and slide it in",
            "You press her folds aside and nudge your cock in",
            "You take careful aim and then ram your cock in"])

        $ final_line = renpy.random.choice(["leans back a bit and your cock slides in"])
    elif action == "anal":
        $ first_action_line = renpy.random.choice(["slowly presses against your rigid member",
            "leans back and presses against you suggestively"])

        $ action_line = renpy.random.choice(["climbs on top of you",
            "pushes you back and slowly presses against your rigid member",
            "lays back and slowly presses against your rigid member",
            "turns around and slowly presses against your rigid member",
            "bends over and presses her backside against you suggestively",
            "leans back and presses against you suggestively",
            "backs her ass up against your cock"])

        $ player_first_action_line = renpy.random.choice(["You guide it into place and slide it in"])

        $ player_action_line = renpy.random.choice(["You guide your cock into place and ram it home",
            "You guide it into place and slide it in",
            "You take careful aim and then ram your cock in",
            "You press against her rim and nudge your cock in."])

        $ final_line = renpy.random.choice(["leans back a bit and your cock pops in"])
    elif action == "hotdog":
        $ first_action_line = renpy.random.choice(["slowly presses against your rigid member",
            "leans back and presses against you suggestively"])

        $ action_line = renpy.random.choice(["pushes you back and slowly presses against your rigid member",
            "turns around and slowly presses against your rigid member",
            "bends over and presses her backside against you suggestively",
            "leans back and presses against you suggestively",
            "backs her ass up against your cock"])

        $ player_first_action_line = None
        $ player_action_line = None
        $ final_line = None

    if taboo:
        if Girl in [RogueX, KittyX]:
            if (action == "sex" and not Girl.permanent_History["sex"]) or (action == "anal" and not Girl.permanent_History["anal"]):
                "[Girl.name] [check_line]. . ."

                if "cockout" in Player.recent_history:
                    "[Girl.name] [first_action_line]"
                else:
                    "She [first_undressing_line] and [first_action_line]."

                if player_first_action_line:
                    "[player_first_action_line]."
            else:
                if "cockout" in Player.recent_history:
                    "[Girl.name] [check_line], then [undressing_line] and [action_line]"
                else:
                    "[Girl.name] [check_line], then [action_line]."

                if player_action_line:
                    "[player_action_line]."
        elif Girl in [EmmaX, LauraX, JeanX, StormX, JubesX]:
            "[Girl.name] [check_line]."

            if "cockout" in Player.recent_history:
                "Then she [action_line]."
            else:
                "Then she [undressing_line] and [action_line]."

            if final_line:
                "She [final_line]."

        if Girl != JeanX:
            $ Girl.inhibition += int(taboo/10)
            $ Girl.lust += int(taboo/5)
        else:
            call change_Girl_stat(JeanX, "inhibition", int(taboo/10))
            call change_Girl_stat(JeanX, "lust", int(taboo/5))
    else:
        if Girl in [RogueX, KittyX]:
            if (action == "sex" and not Girl.permanent_History["sex"]) or (action == "anal" and not Girl.permanent_History["anal"]):
                if "cockout" in Player.recent_history:
                    "[Girl.name] [first_action_line]."
                else:
                    "[Girl.name] [first_undressing_line] and [first_action_line]."

                if player_first_action_line:
                    "[player_first_action_line]."
            else:
                if "cockout" in Player.recent_history:
                    "[Girl.name] [undressing_line] and [action_line]"
                else:
                    "[Girl.name] [action_line]."

                if player_action_line:
                    "[player_action_line]."
        elif Girl in [EmmaX, LauraX, JeanX, StormX, JubesX]:
            if "cockout" in Player.recent_history:
                "[Girl.name] [action_line]."
            else:
                "[Girl.name] [undressing_line] and [action_line]."

            if final_line:
                "She [final_line]."

    return

label knows_her_place_narrations(Girl, action):
    $ lines = ["[Girl.name] doesn't seem to be into this, but she knows her place.",
        "[Girl.name] doesn't seem to be into this, you're lucky she's so obedient."]

    $ line = renpy.random.choice(lines)

    "[line]"

    return

label not_ready_to_stop_narrations(Girl, action):
    $ lines = ["She continues to shake a little with pleasure.",
        "She is breathing heavily as your cock rubs inside her.",
        "She slowly turns back towards you and smiles.",
        "She doesn't seem ready to stop."]

    $ line = renpy.random.choice(lines)

    "[line]"

    return

label auto_accepted_narrations(Girl, action):
    if action == "fondle_thighs":
        "As you caress her thigh, [Girl.name] glances at you, and smiles."
    elif action == "fondle_breasts":
        "As you cup her breast, [Girl.name] gently nods."
    elif action == "suck_breasts":
        "As you dive in, [Girl.name] seems a bit surprised, but just makes a little \"coo.\""
    elif action == "fondle_pussy":
        "As your hand creeps up her thigh, [Girl.name] seems a bit surprised, but then nods."
    elif action == "finger_pussy":
        "As you slide a finger in, [Girl.name] seems a bit surprised, but seems into it."
    elif action == "eat_pussy":
        $ lines = ["As you crouch down and start to lick her pussy, " + Girl.name + " startles, but then sinks into the sensation.",
            "As you crouch down and start to lick her pussy, " + Girl.name + " jumps, but then softens.",
            "As you crouch down and start to lick her pussy, " + Girl.name + " starts, but then softens."]

        $ line = renpy.random.choice(lines)

        "[line]"
    elif action == "fondle_ass":
        $ lines = ["As your hand creeps down her backside, " + Girl.name + " seems a bit surprised, but then nods.",
            "As your hand creeps down her backside, " + Girl.name + " jumps a bit, and then relaxes.",
            "As your hand creeps down her backside, " + Girl.name + " shivers a bit, and then relaxes."]

        $ line = renpy.random.choice(lines)

        "[line]"
    elif action == "finger_ass":
        "As you slide a finger in, [Girl.name] tightens around it in surprise, but seems into it."
    elif action == "eat_ass":
        "As you crouch down and start to lick her asshole, [Girl.name] startles briefly, but then begins to melt."
    elif action in dildo_actions or action in sex_actions:
        "[Girl.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."

    return
