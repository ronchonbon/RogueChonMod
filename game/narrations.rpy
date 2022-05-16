label Primary_SexDialog(GirlA=Primary,phrase = 0, Templust = 0, Templust2 = 0): #rkeljs
    #nee Rog*ue_SexDialog(phrase = 0, Templust = 0, Templust2 = 0)
    #called from Sex_Dialog as call Primary_SexDialog(Primary)
    if action_context == "skip" and line:
            # if the action was set by a previous trigger, skip this element
            $ action_context = 0
            return

    if primary_action == "handjob":
            $ line = GirlA.name + " continues stroke your cock. "

            if not action_speed:
                        $ line = GirlA.name + " holds your cock in her hand. "
                        if GirlA.action_counter["handjob"] > 2:
                                $ line = line + "She just seems to be enjoying the feel of it"
                                $ Templust += 2 if GirlA.lust < 60 else 0
                        else:
                                $ line = line + "She just seems to be looking it over"
                                $ Templust += 2 if GirlA.lust < 40 else 0
                                $ TempFocus += -3 if Player.Focus > 50 else 2
                        $ GirlA.Addict -= 1 if D20S > 10 else 2
                        return
            if GirlA in (EmmaX,LauraX,StormX):
                        #Laura and Emma have more experience to start
                        if action_speed <= 1:
                            #slow
                            $ line = line + renpy.random.choice(["Her movements have become masterful, her slightest touch starts you twitching",
                                    "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here",
                                    "She slowly caresses you in a way that makes your blood boil, then pulls back at the last second",
                                    "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                    "You can't tell where she is at any moment, all you know is that it works"])
                            $ TempFocus += 20 if Player.Focus < 60 else 7
                        else:
                            #fast
                            $ line = line + renpy.random.choice(["Her movements have become masterful, her slightest touch starts you twitching",
                                    "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here",
                                    "Her expert strokes will have you boiling over in seconds",
                                    "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, you can tell she's had plenty of practice",
                                    "You can't tell where she is at any moment, all you know is that it works"])
                            $ TempFocus += 20 if Player.Focus > 70 else 7
            elif GirlA.action_counter["handjob"] > 4:
                        # After the 5th time
                        if action_speed <= 1:
                            #slow
                            $ line = line + renpy.random.choice(["Her movements have become almost masterful, her slightest touch starts you twitching",
                                    "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here",
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She slowly caresses you in a way that makes your blood boil, then pulls back at the last second",
                                    "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                    "You can't tell where she is at any moment, all you know is that it works"])
                            $ TempFocus += 20 if Player.Focus < 40 else 5
                        else:
                            #fast
                            $ line = line + renpy.random.choice(["Her movements have become almost masterful, her slightest touch starts you twitching",
                                    "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here",
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "Her expert strokes will have you boiling over in seconds",
                                    "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                    "You can't tell where she is at any moment, all you know is that it works"])
                            $ TempFocus += 20 if Player.Focus > 70 else 5
            elif 2 < GirlA.action_counter["handjob"] <= 4:
                        #third through 5th time
                        if action_speed <= 1:
                            #slow
                            $ line = line + renpy.random.choice(["She's begining to figure things out, her fingers cause tingles as they caress the shaft",
                                    "She's still learning, but learning fast. Her hands sure are smooth",
                                    "She has a smooth motion going now, gentle and precise",
                                    "Her lessons are paying off, she's really becoming very talented at this",
                                    "She gently caresses the shaft, and cups the balls in her other hand, giving them a warm massage"])
                            $ TempFocus += 15 if Player.Focus < 60 else 7
                        else:
                            #fast
                            $ line = line + renpy.random.choice(["She's begining to figure things out, her fingers cause tingles as they caress the shaft",
                                    "She's still learning, but learning fast. Her hands sure are smooth",
                                    "Her hands glide smoothly across your cock",
                                    "She has a smooth motion going now, gentle and precise",
                                    "Her lessons are paying off, she's really becoming very talented at this",
                                    "She quickly strokes your cock, with a very deft pressure"])
                            $ TempFocus += 15 if Player.Focus > 60 else 5
            else:
                    #First and second time
                    if action_speed <= 1:
                        #slow
                        $ line = line + renpy.random.choice(["She makes up for her inexperience with determination, carefully stroking your cock",
                                "She moves her hands up and down the shaft. She's a little rough at this, but at least she tries",
                                "She strokes you gently. She isn't quite sure what to make of the balls",
                                "Her fingers fumble with your shaft a bit",
                                "She squeezes one of your balls too tightly, but stops when you wince",
                                "She has a firm grip, and she's not letting go. This may take a few tries"])
                        $ TempFocus += 12 if Player.Focus > 60 else 5
                    else:
                        #fast
                        $ line = line + renpy.random.choice(["She really wasn't prepared for speeding up, and your cock often slips out of her hand",
                                "She rapidly moves her hands up and down the shaft. She's a little rough at this, but at least she tries",
                                "She strokes you a bit too quickly, the friction is a bit uncomfortable",
                                "Her fingers fumble with your shaft a bit",
                                "She squeezes one of your balls too tightly, but stops when you wince",
                                "She has a firm grip, and she's not letting go. This train is out of control"])
                        $ TempFocus += 10 if Player.Focus > 60 else 2

            $ Templust += 2 if GirlA.lust < 60 else 0
            $ Templust += 2 if GirlA.action_counter["handjob"] > 2 else 0
            $ GirlA.Addict -= 1 if D20S > 10 else 2

    #End Handy dialog ////////////////////////////////////////////////////////////////////////////////////////////////////////


    elif primary_action == "titjob":
            #This can only ever be a primary action.

            if not action_speed:
                        if GirlA == KittyX:
                            $ line = GirlA.name + " begins to rub her chest against you"
                        elif GirlA.action_counter["titjob"] > 2:
                            $ line = GirlA.name + " begins to bounce her breasts up and down"
                        else:
                            $ line = GirlA.name + " squeezes her breasts together and slowly moves them along your shaft"
                        $ action_speed = 1
                        $ TempFocus += 12 if Player.Focus < 60 else 6
                        $ Templust += 6 if GirlA.lust > 60 else 3
                        return

            if GirlA in (EmmaX,StormX) or (GirlA.action_counter["titjob"] > 4 and GirlA.action_counter["blowjob"]):
                        #5th+ and blown
                        if action_speed <= 1:
                            #slow
                            $ line = renpy.random.choice([GirlA.name + " rocks her breasts up and down around your cock",
                                    GirlA.name + " lightly licks the head as it pops up between her tits",
                                    GirlA.name + " has a smooth motion going now, gentle and precise",
                                    GirlA.name + " pauses to rub her nipples across the shaft",
                                    "In between strokes "+ GirlA.name + " gently sucks on the head",
                                    GirlA.name + " drips some spittle down to make sure you're properly lubed",
                                    GirlA.name + " gently caresses the shaft between her tits"])

                            $ TempFocus += 15 if Player.Focus < 70 else 5
                            $ Templust += 7 if GirlA.lust > 60 else 4
                        else:
                            #fast
                            $ line = renpy.random.choice([GirlA.name + " rapidly rocks her breasts up and down around your cock",
                                    GirlA.name + " licks away at the head every time it pops up between her tits",
                                    GirlA.name + " has a smooth motion going now, quick by efficient",
                                    GirlA.name + " dances her nipples across the shaft",
                                    "In as she strokes faster and faster, " + GirlA.name + " bends down to suck on the head",
                                    GirlA.name + " covers her tits with drool to keep them well lubed",
                                    GirlA.name + " rapidly caresses the shaft between her tits"])

                            $ TempFocus += 20 if Player.Focus > 40 else 5
                            $ Templust += 6 if GirlA.lust > 70 else 4


            elif GirlA.action_counter["titjob"] > 1:
                    #third through 5th time
                    if action_speed <= 1:
                        #slow
                        $ line = renpy.random.choice([GirlA.name + " juggles her breasts up and down around your cock",
                                GirlA.name + " lightly strokes the head as it pops up between her tits",
                                GirlA.name + " has a smooth motion going now, gentle and precise",
                                GirlA.name + " pauses to rub her nipples across the shaft",
                                GirlA.name + " gently caresses the shaft between her tits"])

                        $ TempFocus += 15 if Player.Focus < 60 else 5
                        $ Templust += 6 if GirlA.lust > 60 else 3
                    else:
                        #fast
                        $ line = renpy.random.choice([GirlA.name + " rapidly juggles her breasts up and down around your cock",
                            GirlA.name + " lightly brushes the head with her chin as it pops up between her tits",
                            GirlA.name + " moves them up and down in a fluid rocking motion",
                            GirlA.name + " bounces her whole body up and down",
                            GirlA.name + " rapidly slides the shaft between her tits"])

                        $ TempFocus += 15 if Player.Focus > 50 else 7
                        $ Templust += 6 if GirlA.lust > 60 else 4

            else:
                    #First and second time
                    if action_speed <= 1:
                        #slow
                        $ line = renpy.random.choice([GirlA.name + " sort of squishes her breasts back and forth around your cock",
                            GirlA.name + " slides the cock up and down between her cleavage",
                            GirlA.name + " kind of bounces her tits around your cock",
                            GirlA.name + " smooshes her cleavage as tight as she can and rubs up and down"])

                        $ TempFocus += 12 if Player.Focus < 60 else 6
                        $ Templust += 6 if GirlA.lust > 60 else 3

                    else:
                        #fast
                        $ line = renpy.random.choice([GirlA.name + " sort of bounces her breasts off your cock",
                            GirlA.name + " tries to quickly slide the cock up and down between her cleavage, but it tends to slide out",
                            GirlA.name + " slaps her tits against your dick",
                            GirlA.name + " smooshes her cleavage as tight as she can and rubs up and down quite quickly"])

                        $ TempFocus += 8 if Player.Focus > 70 else 4
                        $ Templust += 5 if GirlA.lust > 60 else 3

            if GirlA == KittyX:
                    $ TempFocus -= 2
            elif GirlA in (EmmaX,StormX):
                    $ TempFocus += 1

            $ GirlA.Addict -= 2
    #End Action Titfuck ///////////////////////////////////////////////////////////////////////////////


    elif primary_action == "blowjob":
            if not action_speed:
                    #if Rog*ue is not moving
                    if "hungry" in GirlA.Traits:
                            $ GirlA.change_face("sly")
                            $ line = GirlA.name + " stares at your cock. She licks her lips in anticipation"
                            $ Templust += 3 if GirlA.lust < 40 else 1
                    elif GirlA.action_counter["blowjob"] > 2:
                            $ GirlA.change_face("sly")
                            $ line = GirlA.name + " stares at your cock. She seems pretty excited about it"
                            $ Templust += 2 if GirlA.lust < 60 else 0
                    elif GirlA == EmmaX:
                            $ GirlA.change_face("sly")
                            $ line = GirlA.name + " stares at your cock. She seems pretty intrigued by it"
                            $ Templust += 2 if GirlA.lust < 60 else 0
                    else:
                            $ GirlA.change_face("perplexed")
                            $ line = GirlA.name + " stares at your cock with trepidation"
                            $ Templust += 2 if GirlA.lust < 40 else 0

                    if GirlA.action_counter["blowjob"] <= 1 or (GirlA.obedience >= 500 and GirlA.obedience > GirlA.inhibition):
                            $ Templust += 2 if GirlA.lust > 60 else 0
                            $ line = line + ", but she seems to be waiting for some instruction"
                    else:
                            $ line = line + ", and then she gets started licking your cock"
                            $ action_speed = 1
                    return

            elif action_speed < 2:
                        $ line = GirlA.name + " continues to lick your cock. "
                        #if Rog*ue is the primary but is licking
            else:
                        $ line = GirlA.name + " continues to suck your cock. "
                        #if Rog*ue is the primary and is heading or sucking

            if action_speed == 1:
                    #action_speed 1 (licking)
                    if GirlA.action_counter["blowjob"] > 4 or GirlA in (EmmaX,LauraX,StormX):
                            #After the 5th time
                            $ line = line + renpy.random.choice(["Her deft licks are masterful, your cock twitches with each stroke",
                                    "She gently blows across the head as she covers your cock in smooth licks",
                                    "How many licks to the center of your cock? No way you're finding out",
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She's really getting good at this, alternating between deep suction and gentle licks",
                                    "She moves very smoothly, tongue dancing casually and very gently, like she's been doing this for years",
                                    "She puts the tip into her mouth and her tounge dances around it"])
                            $ TempFocus += 20 if Player.Focus < 70 else 15
                            $ Templust += 2 if GirlA.lust > 80 else 1

                    elif GirlA.action_counter["blowjob"] > 1:
                            #After the 2nd time
                            $ line = line + renpy.random.choice(["She's begining to figure things out, her tongue makes your hair stand on end",
                                    "She's still learning, but learning fast. She seems eager to use her mouth for more than talk",
                                    "She's settled into a gentle licking pace that washes over you like a warm bath",
                                    "She licks gently up and down the shaft. She's a little rough at this, but at least she tries",
                                    "Her tongue moves carefully along the shaft",
                                    "She's really starting to learn some clever tricks to making you feel good",
                                    "She licks her way down the shaft, and gently teases the balls"])
                            $ TempFocus += 20 if Player.Focus > 60 else 10
                            $ Templust += 2 if GirlA.lust > 80 else 1

                    else:
                            #First and second time
                            $ line = line + renpy.random.choice([GirlA.name + " makes up for her inexperience with determination, carefully licking your cock",
                                    "She takes a small lick and grimaces at the taste",
                                    "She tentatively kisses around the head a bit",
                                    "She nibbles one of your balls, but stops when you wince",
                                    "She licks all over your dick, but she doesn't really have a handle on it"])
                            $ TempFocus += 15 if Player.Focus > 60 else 5
                    $ GirlA.Addict -= 2

            elif action_speed == 2:
                    #action_speed 2 (heading)
                    if GirlA.action_counter["blowjob"] > 4 or GirlA in (EmmaX,LauraX,StormX):
                            #After the 5th time
                            $ line = line + renpy.random.choice(["She masterfully bobs on your cock, and it twitches with each stroke",
                                    "She rapidly bobs up and down on your cock, a frenzy of motion",
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She's really getting good at this, alternating between deep suction and quick licks across the head",
                                    "She moves very smoothly, bobbing in and out like she's been doing this for years",
                                    "She puts the tip into her mouth and her tounge swirls rapidly around it"])
                            $ TempFocus += 20 if Player.Focus < 80 else 10
                            $ Templust += 2 if GirlA.lust > 70 else 1

                    elif GirlA.action_counter["blowjob"] > 1:
                            #After the 2nd time
                            $ line = line + renpy.random.choice(["She's begining to figure things out, she bobs carefully up and down the head",
                                    "She's still learning, but learning fast. She keeps her teeth well clear, aside from a playful nip",
                                    "Her lips envelope you like a warm bath as she bobs in and out",
                                    "She's really starting to learn some clever tricks to making you feel good",
                                    "She rapidly licks her way around the head",
                                    "Her mouth envelopes the head, then she quickly draws it in and draws back with a pop"])
                            $ TempFocus += 15 if Player.Focus > 80 else 10
                            $ Templust += 1 if GirlA.lust > 60 else 0

                    else:
                            # First and second time
                            $ line = line + renpy.random.choice(["She really wasn't prepared for speeding up, and your cock often pops out of her mouth",
                                    "She puts the tip in her mouth and starts to actually suck in as hard as she can. She's a little rough at this, but at least she tries",
                                    "Her head bobs rapidly, until she goes a bit too deep and starts to gag",
                                    "She lets her teeth get a bit too much action",
                                    "She bobs quickly on your cock, but clamps down a bit too tight for comfort"])
                            $ TempFocus += 9 if Player.Focus > 80 else 3
                    $ GirlA.Addict -= 2

            elif action_speed == 3:
                    #action_speed 3 (sucking)
                    if GirlA.action_counter["blowjob"] > 4 or GirlA in (EmmaX,LauraX,StormX):
                            #After the 5th time
                            $ line = line + renpy.random.choice(["She masterfully bobs on your cock, and it twitches with each stroke",
                                    "She smoothly bobs up and down on your cock, a frenzy of motion",
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She gobbles you up all the way to the base, then quickly draws out and plunges back in",
                                    "She's really getting good at this, alternating between deep suction and quick licks across the head",
                                    "She moves very smoothly, bobbing in and out like she's been doing this for years",
                                    "She puts the shaft into her mouth and her tounge swirls rapidly around it"])
                            $ TempFocus += 22 if Player.Focus > 40 else 10
                            $ Templust += 3 if GirlA.lust > 60 else 1

                    elif GirlA.action_counter["blowjob"] > 1:
                            #After the 2nd time
                            $ line = line + renpy.random.choice(["She's begining to figure things out, she bobs carefully up and down the shaft",
                                    "She's still learning, but learning fast. She keeps her teeth well clear, aside from a playful nip",
                                    "Her lips envelope you like a warm bath as she bobs in and out",
                                    "She slowly draws you in to the base of your cock, then pulls back at the last second",
                                    "She's really starting to learn some clever tricks to making you feel good",
                                    "She rapidly licks her way up and down the shaft as her mouth envelopes you",
                                    "Her mouth envelopes the shaft, then she quickly draws it in and draws back with a pop"])
                            $ TempFocus += 15 if Player.Focus > 50 else 5

                    else:
                            #First and second time
                            $ line = line + renpy.random.choice(["She really wasn't prepared for putting it all the way in, and grimaces at the taste",
                                    "She puts the tip in her mouth and starts to actually suck in as hard as she can. She's a little rough at this, but at least she tries",
                                    "She sucks up and down your cock very quickly, but gets a bit dizzy and has to slow down",
                                    "Her head bobs rapidly, until she goes a bit too deep and starts to gag",
                                    "She lets her teeth get a bit too much action",
                                    "She bobs quickly on your cock, but clamps down a bit too tight for comfort"])
                            $ TempFocus += 6 if Player.Focus < 50 else 3
                    $ GirlA.Addict -= 2 if D20S > 10 else 3


            else:#action_speed = 4
                    #action_speed 4+ (Deep Throat)
                    if GirlA.action_counter["blowjob"] > 4 or GirlA in (EmmaX,LauraX,StormX):
                            #After the 5th time
                            $ line = line + renpy.random.choice(["She masterfully bobs on your cock, and it twitches with each stroke",
                                    "She rapidly bobs to the base of your cock, a frenzy of motion",
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She gobbles you up all the way to the base, then quickly draws out and plunges back in",
                                    "She's really getting good at this, alternating between deep suction and quick licks across the head",
                                    "She moves very smoothly, bobbing in and out like she's been doing this for years",
                                    "She puts the entire shaft into her mouth and her tounge swirls rapidly around it"])
                            $ TempFocus += 25 if Player.Focus > 40 else 8
                            $ Templust += 3 if GirlA.lust > 60 else 2

                    elif GirlA.action_counter["blowjob"] > 1:
                            #After the 2nd time
                            $ line = line + renpy.random.choice(["She's begining to figure things out, she bobs carefully up and down the shaft",
                                    "She's still learning, but learning fast. She keeps her teeth well clear, aside from a playful nip",
                                    "Her lips envelope you like a warm bath as she bobs in and out",
                                    "She slowly draws you in to the base of your cock, then pulls back at the last second",
                                    "She's really starting to learn some clever tricks to making you feel good",
                                    "She completely envelops the shaft with her throat.",
                                    "Her mouth envelopes the head, then she quickly draws it all the way in and draws back with a pop"])
                            $ TempFocus += 20 if Player.Focus > 40 else 5
                            $ Templust += -3 if GirlA.lust < 60 else -1
                            $ Templust += 5 if GirlA.obedience > 500 else 0

                    else:
                            #First and second time
                            $ line = line + renpy.random.choice(["She really wasn't prepared for going so deep, and gags a bit",
                                    "She puts the whole shaft in her mouth and starts to actually suck in as hard as she can. She's a little rough at this, but at least she tries",
                                    "She draws your cock into her mouth very qucikly, but gets a bit dizzy and has to slow down",
                                    "Her head bobs rapidly, until she goes a bit too deep and starts to gag",
                                    "She lets her teeth get a bit too much action",
                                    "She bobs quickly on your cock, but clamps down a bit too tight for comfort"])
                            $ TempFocus += 15 if Player.Focus > 80 else 5
                            $ Templust += -5 if GirlA.lust < 60 else -2
                            $ Templust += 7 if GirlA.obedience > 500 else 0
                    $ GirlA.Addict -= 3
            $ GirlA.Addict -= 3 if GirlA == JubesX else 0

    # end GirlA.action_counter["blowjob"]job                                 //////////////////////////////////////////////////////////////////////////////

    elif primary_action == "sex":
            #second_girl_primary_action not available

            if not action_speed:
                    #if Rog*ue is not moving
                    $ line = "She seems to be waiting for you to do something. . "
                    return

            elif action_speed < 2:
                    $ line = "You continue to pound "+ GirlA.name + ". "
                    #if Rog*ue is the primary but is licking
            else:
                    $ line = "You continue to slowly drive into " + GirlA.name + ". "
                    #if Rog*ue is the primary and is heading or sucking

            if GirlA.Sex > 4 or GirlA in (EmmaX,LauraX,StormX):
                if action_speed > 1:
                        # After the 5th time fast
                        $ line = line + renpy.random.choice(["She bounces rapidly against your cock",
                            "You thrust into her and she squeaks a bit",
                            "You quickly grind back and forth inside her",
                            "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                            "You pound away at her",
                            "She grinds furiously back and forth along your cock"])
                        $ TempFocus += 18 if Player.Focus > 50 else 12
                        $ Templust += 16 if GirlA.lust > 70 else 10
                else:
                        # After the 5th time slow
                        $ line = line + renpy.random.choice(["She bumps slowly against your cock",
                            "You thrust into her and she coos a bit",
                            "You slowly grind back and forth inside her",
                            "You alternate between long and slow thrusts, and the occasional quick one",
                            "You slowly slide back and forth near the entrance",
                            "She slides slowly back and forth along your cock, teasing you"])
                        $ TempFocus += 14 if Player.Focus < 60 else 12
                        $ Templust += 12 if 40 > GirlA.lust > 90 else 10

            elif GirlA.Sex > 1:
                if action_speed > 1:
                    #third through 5th time fast
                    $ line = line + renpy.random.choice(["She bounces rapidly against your cock",
                        "You thrust into her and she squeaks a bit",
                        "You quickly grind back and forth inside her",
                        "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                        "You pound away at her",
                        "She grinds furiously back and forth along your cock"])
                    $ TempFocus += 12 if Player.Focus > 50 else 9
                    $ Templust += 14 if GirlA.lust > 80 else 10
                else:
                    #third through 5th time slow
                    $ line = line + renpy.random.choice(["she bumps slowly against your cock",
                        "You thrust into her and she squeaks a bit",
                        "You slowly grind back and forth inside her",
                        "You alternate between long and slow thrusts, and the occasional quick one",
                        "You slowly slide back and forth near the entrance",
                        "She slides slowly back and forth along your cock"])
                    $ TempFocus += 12 if Player.Focus < 70 else 7
                    $ Templust += 10 if 50 > GirlA.lust > 90 else 8

            else:
                if action_speed > 1:
                    # First and second time fast
                    $ line = line + renpy.random.choice(["She bounces rapidly against your cock",
                        "You thrust into her and she squeeks in pain",
                        "You quickly grind back and forth inside her but she doesn't seem to have the rhythm down",
                        "She bounces rapidly against your cock, occasionally popping out and having to stick it back in",
                        "You pound away at her",
                        "She moves rapidly back and forth along your cock, but seems a bit uncomfortable"])
                    $ TempFocus += 10 if Player.Focus > 60 else 9
                    $ Templust += 10 if GirlA.lust > 80 else 6
                else:
                    # First and second time slow
                    $ line = line + renpy.random.choice(["She bumps slowly against your cock",
                        "You thrust into her and she squeaks a bit",
                        "You slowly grind back and forth inside her",
                        "You alternate between long and slow thrusts, and the occasional quick one",
                        "You slowly slide back and forth near the entrance",
                        "She slides slowly back and forth along your cock"])
                    $ TempFocus += 10 if Player.Focus < 70 else 9
                    $ Templust += 8 if 60 > GirlA.lust > 90 else 6

            $ GirlA.Addict -= 2

    # end GirlA.Sex                                 //////////////////////////////////////////////////////////////////////////////

    elif primary_action == "hotdog":
            #second_girl_primary_action not available
            #Templust2 in this action is how much lower body clothing she has on, it gets cleared at the end.
            $ Templust2 = 2
            if GirlA.Panties and not GirlA.PantiesDown:
                    #if panties are in the way
                    $ Templust2 -= 1
            if GirlA.HoseNum() >= 6:
                    #if complete hose
                    $ Templust2 -= 1
            if GirlA.Legs and not GirlA.Upskirt:
                    #If pants/skirt is up
                    $ Templust2 -= 2 if Templust2 <= 2 else Templust2

            if not action_speed:
                $ line = "She seems to be waiting for you to do something. . "
                return
            elif action_speed < 2:
                    $ line = "You continue to hotdog " + GirlA.name + ". "
            else:
                    $ line = "You continue to grind against " + GirlA.name + ". "

            if GirlA.action_counter["hotdog"] >= 2:
                if action_speed > 1:
                    # After the 2ndtime fast
                    $ line = line + renpy.random.choice(["She bounces rapidly against your cock",
                        "You thrust against her and she squeaks a bit",
                        "You quickly grind back and forth along her crack",
                        "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                        "You grind away at her",
                        "She grinds furiously back and forth along your cock"])
                    $ TempFocus += (Templust2 + 8) if Player.Focus < 60 else (Templust2 + 4)
                    $ Templust += (Templust2 + 8) if 50 > GirlA.lust > 80 else (Templust2 + 2)

                elif action_speed:
                    #2nd time slow
                    $ line = line + renpy.random.choice(["She grinds slowly against your cock",
                        "You thrust against her and she coos a bit",
                        "You slowly rub the tip across her pussy",
                        "You alternate between long and slow thrusts, and the occasional rapid ones",
                        "You slowly slide back and forth near her rim",
                        "She slides slowly back and forth along your cock, teasing you"])
                    $ TempFocus += (Templust2 + 8) if Player.Focus < 60 else (Templust2 + 3)
                    $ Templust += (Templust2 + 7) if 30 > GirlA.lust > 70 else (Templust2 + 3)

            else:
                #If you haven't done hotdog before
                if action_speed > 1:
                    #fast
                    $ line = line + renpy.random.choice(["She bounces rapidly against your cock",
                        "You thrust against her and she squeeks in surprise",
                        "You quickly grind back and forth against her but she doesn't seem to have the rhythm down",
                        "She bounces rapidly against your cock",
                        "You pound away at her",
                        "She slides rapidly back and forth along your cock, but seems a bit uncomfortable"])
                    $ TempFocus += (Templust2 + 5) if Player.Focus < 60 else (Templust2 + 3)
                    $ Templust += (Templust2 + 4) if 50 > GirlA.lust > 80 else (Templust2 + 2)

                elif action_speed:
                    #slow
                    $ line = line + renpy.random.choice(["She grinds slowly against your cock",
                        "You thrust into her crack and she squeaks a bit",
                        "You slowly grind back and forth across her rear",
                        "You slowly slide back and forth near her rim",
                        "She slides slowly back and forth along your cock"])
                    $ TempFocus += (Templust2 + 5) if Player.Focus < 60 else (Templust2 + 3)
                    $ Templust += (Templust2 + 5) if 50 > GirlA.lust > 70 else (Templust2 + 2)

            if Templust2:
                $ GirlA.Addict -= 1
                $ Templust2 = 0

    # end GirlA.action_counter["hotdog"]                                 //////////////////////////////////////////////////////////////////////////////


    elif primary_action == "anal":
            #second_girl_primary_action not available

            if not action_speed:
                $ line = "She seems to be waiting for you to do something. . "
                return

            elif action_speed < 2:
                    $ line = "You continue to pound into " + GirlA.name + "'s ass. "
            else:
                    $ line = "You continue to push into " + GirlA.name + "'s ass. "


            if GirlA.Anal >= 5:
                    if action_speed > 1:
                            #Fast
                            $ line = line + renpy.random.choice(["She bounces rapidly against your cock",
                                "You thrust into her and she squeaks a bit",
                                "You quickly grind back and forth inside her",
                                "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                                "You pound away at her",
                                "She grinds furiously back and forth along your cock"])
                            $ TempFocus += 18 if Player.Focus > 60 else 12
                            $ Templust += 14 if GirlA.lust > 80 else 9

                    else:
                            #Slow
                            $ line = line + renpy.random.choice(["She bumps slowly against your cock",
                                "You thrust into her and she coos a bit",
                                "You slowly grind back and forth inside her",
                                "You alternate between long and slow thrusts, and the occasional quick one",
                                "You slowly slide back and forth near the rim",
                                "She slides slowly back and forth along your cock, teasing you"])
                            $ TempFocus += 12 if Player.Focus > 60 else 9
                            $ Templust += 12 if 50 < GirlA.lust < 90 else 8

            elif GirlA.Loose:
                    #You've done some anal stuff before
                    if action_speed > 1:
                            #third through 5th time fast
                            $ line = line + renpy.random.choice(["She bounces rapidly against your cock",
                                "You thrust into her and she squeaks a bit",
                                "You quickly grind back and forth inside her",
                                "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                                "You pound away at her",
                                "She grinds furiously back and forth along your cock"])
                            $ TempFocus += 12 if Player.Focus > 60 else 8
                            $ Templust += 12 if GirlA.lust > 80 else 6

                    elif action_speed:
                            #third through 5th time
                            $ line = line + renpy.random.choice(["She bumps slowly against your cock",
                                "You thrust into her and she squeaks a bit",
                                "You slowly grind back and forth inside her",
                                "You alternate between long and slow thrusts, and the occasional quick one",
                                "You slowly slide back and forth near the rim",
                                "She slides slowly back and forth along your cock"])
                            $ TempFocus += 13 if Player.Focus > 60 else 8
                            $ Templust += 8 if 70 > GirlA.lust > 90 else 4

            else:
                    #If you haven't done anal things before
                    if action_speed > 1:
                            #fast
                            $ line = line + renpy.random.choice(["She bounces rapidly against your cock but seems to be in pain",
                                "You thrust into her and she squeeks in pain",
                                "You quickly grind back and forth inside her but she doesn't seem to have the rhythm down",
                                "She bounces rapidly against your cock, occasionally popping out and having to stick it back in",
                                "You pound away at her",
                                "She moves rapidly back and forth along your cock, but seems a bit uncomfortable"])
                            $ TempFocus += 10 if Player.Focus > 60 else 8
                            $ Templust += 2 if GirlA.lust > 80 else -3

                    elif action_speed:
                            #heading
                            $ line = line + renpy.random.choice(["She grits her teeth and slides slowly against your cock",
                                "You thrust into her and she squeaks a bit",
                                "You slowly grind back and forth inside her",
                                "You slowly slide back and forth near the rim",
                                "She slides slowly back and forth along your cock"])
                            $ TempFocus += 10 if Player.Focus > 60 else 6
                            $ Templust += 4 if GirlA.lust > 60 else -1

            if GirlA.Loose > 1:
                #If she's extra loose
                $ Templust += 1

            $ GirlA.Addict -= 3
            $ Templust = 0 if (GirlA.lust - Templust) < 0 else Templust

    # end GirlA.Anal                                 //////////////////////////////////////////////////////////////////////////////

    elif primary_action == "fondle_breasts":
                    $ line = "You continue to fondle " + GirlA.name + ". "
                    if not GirlA.Uptop and GirlA.Over and GirlA.Chest:
                                #Full top
                                $ line = line + renpy.random.choice(["You reach under her layers of clothing and massage her breasts",
                                    "You pass your hands gently over her warm breasts",
                                    "Her firm nipples catch on the fabric of her top as you grasp her warm flesh",
                                    "She gasps as you grasp her under her top"])
                                $ TempFocus += 2 if Player.Focus < 40 else 1
                                $ Templust += 4 if GirlA.lust > 50 else 2
                    elif not GirlA.Uptop and GirlA.Over:
                                #Just overtop
                                $ line = line + renpy.random.choice(["You reach under her top and massage her breasts",
                                    "You pass your hands gently over her warm breasts",
                                    "Her nipples catch on the fabric of her top as you grasp her warm flesh, you can see them stiffen",
                                    "She gasps as you grasp her under her " + GirlA.Over])
                                $ TempFocus += 2 if Player.Focus < 50 else 1
                                $ Templust += 4 if GirlA.lust > 50 else 2
                    elif not GirlA.Uptop and GirlA.Chest:
                                #just bra
                                $ line = line + renpy.random.choice(["You reach under her " + GirlA.Chest + " and massage her breasts",
                                    "You pass your hands gently over her warm breasts",
                                    "Her nipples catch on the fabric of her " + GirlA.Chest + " as you grasp her warm flesh, you can see them stiffen",
                                    "She gasps as you grasp her under her " + GirlA.Chest])
                                $ TempFocus += 3 if Player.Focus < 60 else 2
                                $ Templust += 5 if GirlA.lust > 50 else 2
                    elif GirlA.Pierce:
                                #pierced
                                $ line = line + renpy.random.choice(["You reach out and massage her glorious breasts",
                                    "You pass your hands gently over her warm breasts, and blow across her pierced nipples",
                                    "Her piercings catch lightly on your fingers as you grasp her warm flesh, you can see the nipples stiffen",
                                    "She gasps as you lightly thumb across her pierced nipples"])
                                $ TempFocus += 4 if Player.Focus < 70 else 2
                                $ Templust += 6 if GirlA.lust > 40 else 4
                    else: #topless
                                $ line = line + renpy.random.choice(["You reach out and massage her glorious breasts",
                                    "You pass your hands gently over her warm breasts, and blow across her nipples",
                                    "Her nipples catch lightly on your fingers as you grasp her warm flesh, you can see them stiffen",
                                    "She gasps as you lightly thumb her rigid nipples"])
                                $ TempFocus += 4 if Player.Focus < 60 else 2
                                $ Templust += 6 if GirlA.lust > 50 else 3
                    if D20S > 18:
                            if GirlA == KittyX:
                                    $ line = "You continue to fondle " + GirlA.name + ". They fit comfortably into your palms."
                            elif GirlA in (EmmaX,StormX):
                                    $ line = "You continue to fondle " + GirlA.name + ". You can barely wrap your hands around them."
                    $ GirlA.Addict -= 2

    # end Fondle breasts                                 //////////////////////////////////////////////////////////////////////////////
    elif primary_action == "suck_breasts":
                    $ line = "You continue to suck on " + GirlA.name + "'s breasts. "
                    if not GirlA.Uptop and GirlA.Over and GirlA.Chest:
                                #Full top
                                $ line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                        "You gently nibble at her nipples as you suck on them through the layered tops",
                                        "You  place a nipple between your lips, and give it a quick tug through the " + GirlA.Over,
                                        "She gasps as you gently nibble her rigid nipples poking through her tops"])
                                $ TempFocus += 2 if Player.Focus < 50 else 1
                                $ Templust += 2 if GirlA.lust < 30 else 1
                    elif not GirlA.Uptop and GirlA.Over:
                                #Just overtop
                                $ line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                        "You gently nibble at her nipples as you suck on them through the " + GirlA.Over,
                                        "You tease her nipples with your tongue through the fabric",
                                        "You slowly lick her nipples through her moist top",
                                        "You gently place a nipple between your lips, and draw it out until it releases with a *pop*",
                                        "She gasps as you lightly lick her rigid nipples, poking through her top"])
                                $ TempFocus += 2 if Player.Focus < 50 else 1
                                $ Templust += 5 if GirlA.lust > 50 else 3
                    elif not GirlA.Uptop and GirlA.Chest:
                                #just bra
                                $ line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                        "You tease her nipples with your tongue through her " + GirlA.Chest,
                                        "You slowly lick her nipples through her moist " + GirlA.Chest,
                                        "You gently place a nipple between your lips, and draw it out until it releases with a *pop*",
                                        "She gasps as you lightly lick her rigid nipples, poking through her " + GirlA.Chest])
                                $ TempFocus += 4 if Player.Focus < 60 else 3
                                $ Templust += 5 if GirlA.lust > 50 else 2
                    elif GirlA.Pierce:
                                #pierced
                                $ line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                    "You gently nibble at her nipples as you suck on them",
                                    "You tease her piercings with your tongue",
                                    "You slowly lick around, and then blow across her nipples",
                                    "You gently place a pierced nipple between your lips, and draw it out until it releases with a *pop*",
                                    "She gasps as you lightly lick her rigid nipples"])
                                $ TempFocus += 5 if Player.Focus < 70 else 4
                                $ Templust += 10 if GirlA.lust > 40 else 7
                                $ GirlA.Addict -= 2
                    else: #topless
                                $ line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                    "You gently nibble at her nipples as you suck on them",
                                    "You tease her nipples with your tongue",
                                    "You slowly lick around, and then blow across her nipples",
                                    "You gently place a nipple between your lips, and draw it out until it releases with a *pop*",
                                    "She gasps as you lightly lick her rigid nipples"])
                                $ TempFocus += 5 if Player.Focus < 60 else 3
                                $ Templust += 10 if GirlA.lust > 50 else 7
                                $ GirlA.Addict -= 2

    # end Suck breasts                                 //////////////////////////////////////////////////////////////////////////////

    elif primary_action == "fondle_thighs":  #second_girl_primary_action not available
                    $ line = "You continue to massage " + GirlA.name + "'s thighs. "

                    if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                #she's wearing pants of some sort. . .
                                $ line = renpy.random.choice(["Her legs twitch a bit in her pants as you caress them",
                                        "She gasps as you stroke her warm thighs through the pants",
                                        "You draw your hand from her knee to mid-thigh, and she gasps a little",
                                        "You slide a hand up her inner thigh, to just below her . . ."])
                                $ TempFocus += 1 if Player.Focus < 50 else 0
                                $ Templust += 1 if GirlA.lust < 50 else 0
                    elif GirlA.wearing_skirt and GirlA.HoseNum() >= 5:
                                # skirt with full hose
                                $ line = renpy.random.choice(["You reach under skirt and stroke her thighs",
                                        "You lift her skirt a bit and feel her firm thighs",
                                        "Her legs twitch a bit beneath her skirt",
                                        "She gasps as you stroke her lightly covered thighs",
                                        "You slide a hand up her inner thigh, to just below her . . "])
                                $ TempFocus += 2 if Player.Focus < 40 else 0
                                $ Templust += 2 if GirlA.lust < 40 else 0
                                $ GirlA.Addict -= 1 if D20S > 10 else 0
                    elif GirlA.wearing_skirt and GirlA.Hose:
                                #skirt with stockings
                                $ line = renpy.random.choice(["You reach under skirt and stroke her thighs",
                                        "You lift her skirt a bit and feel her firm thighs",
                                        "Her legs twitch a bit beneath her skirt",
                                        "She gasps as you stroke her warm thighs",
                                        "You slide a hand up her inner thigh, to just above the hose"])
                                $ TempFocus += 2 if Player.Focus < 50 else 0
                                $ Templust += 2 if GirlA.lust < 50 else 0
                                $ GirlA.Addict -= 1 if D20S > 10 else 0
                    elif GirlA.wearing_skirt:
                                #skirt and no hose
                                $ line = renpy.random.choice(["You reach under skirt and stroke her thighs",
                                        "You lift her skirt a bit and feel her firm thighs",
                                        "Her legs twitch a bit beneath her skirt",
                                        "She gasps as you stroke her warm thighs",
                                        "You draw your hand from her knee to mid-thigh, and she gasps a little",
                                        "You slide a hand up her inner thigh, to just her skirt"])
                                $ TempFocus += 2 if Player.Focus < 50 else 0
                                $ Templust += 2 if GirlA.lust < 50 else 0
                                $ GirlA.Addict -= 2 if D20S > 10 else 1
                    elif GirlA.HoseNum() >= 5:
                                # just hose
                                $ line = renpy.random.choice(["You reach out and stroke her lightly covered thighs",
                                        "You lift her leg a bit and feel her firm thighs",
                                        "Her legs twitch a bit beneath your hands",
                                        "She gasps as you stroke her warm thighs",
                                        "You slide a hand up her inner thigh, the smooth faberic creasing",
                                        "You slide a hand up her inner thigh, to just below her. . "])
                                $ TempFocus += 2 if Player.Focus < 40 else 0
                                $ Templust += 2 if GirlA.lust < 40 else 0
                                $ GirlA.Addict -= 1 if D20S > 10 else 0
                    elif GirlA.Hose:
                                #just stockings
                                $ line = renpy.random.choice(["You reach out and stroke her thighs",
                                        "You lift her leg a bit and feel her firm thighs",
                                        "Her legs twitch a bit beneath your hands",
                                        "She gasps as you stroke her warm thighs",
                                        "You slide a hand up her inner thigh, to just above the hose",
                                        "You slide a hand up her inner thigh, to just below her. . "])
                                $ TempFocus += 2 if Player.Focus < 50 else 0
                                $ Templust += 2 if GirlA.lust < 50 else 0
                                $ GirlA.Addict -= 1 if D20S > 10 else 0
                    else: #nude legs
                                $ line = renpy.random.choice(["You reach out and stroke her thighs",
                                        "You lift her leg a bit and feel her firm thighs",
                                        "Her legs twitch a bit beneath your hands",
                                        "She gasps as you stroke her warm thighs",
                                        "You draw your hand from her knee to mid-thigh, and she gasps a little",
                                        "You slide a hand up her inner thigh, to just below her. . "])
                                $ TempFocus += 2 if Player.Focus < 50 else 0
                                $ Templust += 2 if GirlA.lust < 50 else 0
                                $ GirlA.Addict -= 2 if D20S > 10 else 1

    # end fondle thighs                               //////////////////////////////////////////////////////////////////////////////


    elif primary_action == "fondle_pussy":
                    if action_speed == 2 and D20S <= 10:
                            $ line = renpy.random.choice(["You continue to finger " + GirlA.name + "'s pussy. ",
                                                    "You continue to finger bang " + GirlA.name + "'s pussy. ",
                                                    "You continue to finger blast " + GirlA.name + "'s pussy. "])

                            if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                            #pants
                                            $ line = renpy.random.choice(["You slide a hand down her pants, and slide your fingers into her pussy underneath",
                                                    "You push her panties aside, and slide a finger between her lips",
                                                    "You slide a finger into her pussy and stroke the top",
                                                    "You pull her pants out a bit and she gasps as you slide two fingers between her lips",
                                                    "You rub her clit with your palm as you dive into her pussy with your middle finger"])
                            elif GirlA.wearing_skirt:
                                    if GirlA.Panties and not GirlA.PantiesDown:
                                            #Just panties
                                            $ line = renpy.random.choice(["You push her skirt and " + GirlA.Panties + " aside, and slide a finger between her lips",
                                                    "You slide a finger under her " + GirlA.Panties + " and stroke the top or her pussy",
                                                    "You lift her skirt a bit and she gasps as you pull her " + GirlA.Panties + " aside and slide two fingers between her lips",
                                                    "You rub her clit with your thumb as you dive into her pussy with your middle finger"])
                                    else: #skirt, but nothing else
                                            $ line = renpy.random.choice(["You push her skirt aside, and slide a finger between her lips",
                                                    "You slide a finger into her pussy and stroke the top",
                                                    "You lift her skirt a bit and she gasps as you slide two fingers between her lips",
                                                    "You rub her clit with your thumb as you dive into her pussy with your middle finger"])
                                            $ TempFocus += 2
                                            $ Templust += 2
                            #no skirt or pants
                            elif (GirlA.PantsNum() == 6 or (GirlA == RogueX and GirlA.Panties == "shorts")) and not GirlA.PantiesDown:
                                        # just shorts on
                                        $ line = renpy.random.choice(["You slide a hand down her shorts, and slide your fingers into her pussy underneath",
                                                "You push her shorts up, and slide a finger between her lips",
                                                "You slide a finger along her pussy and stroke to the top",
                                                "You pull her shorts out a bit and she gasps as you slide two fingers between her lips",
                                                "You rub her clit with your palm as you dive into her pussy with your middle finger"])
                            elif GirlA.Panties and not GirlA.PantiesDown:
                                        #Just panties
                                        $ line = renpy.random.choice(["You push her panties aside, and slide a finger between her lips",
                                                "You slide a finger along her pussy and stroke to the top",
                                                "You lift her panties a bit and she gasps as you slide two fingers between her lips"])
                            else: #nothing
                                        $ line = renpy.random.choice(["You reach out and slide a finger between her lips",
                                                "You slide a finger along her pussy and stroke to the top",
                                                "You lift her lips a bit and she gasps as you slide two fingers between them",
                                                "You rub her clit with your thumb as you dive into her pussy with your middle finger"])
                                        $ TempFocus += 2
                                        $ Templust += 2

                            $ TempFocus += 4 if Player.Focus < 50 else 3
                            $ Templust += 6 if GirlA.lust > 40 else 3
                            $ GirlA.Addict -= 2

                    else: #if not fingerblasting or not high rolls
                            $ line = renpy.random.choice(["You continue to stroke " + GirlA.name + "'s pussy. ",
                                                    "You continue to rub " + GirlA.name + "'s pussy. ",
                                                    "You continue to caress " + GirlA.name + "'s pussy. "])

                            if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                            #pants on
                                            $ line = renpy.random.choice(["You reach out and brush your hands across her pussy through the pants",
                                                    "You slide a hand down her pants, and brush your hands across her pussy underneath",
                                                    "You put your hand against her mound and grind against it",
                                                    "You reach into her gap and she gasps as you slide your hand across and stroke her warm mound",
                                                    "As you dig your thumb into her, she gasps and raises up a bit",
                                                    "She gasps as you reach under her and lightly stroke her ass through the pants",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])

                            elif GirlA.wearing_skirt:
                                    if GirlA.Panties == "shorts" and not GirlA.PantiesDown:
                                            #shorts on
                                            $ line = renpy.random.choice(["You reach under skirt and ran your hands over the thin shorts covering her",
                                                    "You slide a hand up the leg of her shorts, and brush your hands across her pussy underneath",
                                                    "You put your hand against her mound and grind against it",
                                                    "You reach into her gap and she gasps as you slide your hand across and stroke her warm mound",
                                                    "As you dig your thumb into her, she gasps and raises up a bit",
                                                    "She gasps as you reach under her and lightly stroke her ass through the thin shorts",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                                    elif GirlA.Panties and not GirlA.PantiesDown: #Just panties
                                            $ line = renpy.random.choice(["You reach under skirt and brush across her panties",
                                                    "You lift her skirt a bit and grind against her panties",
                                                    "You lift her skirt a bit and she gasps as you pull her panties aside and stroke her lips",
                                                    "Her legs twitch a bit beneath her skirt as you press your thumb against her",
                                                    "She gasps as you rub her pussy through her panties",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                                    elif GirlA.HoseNum() >= 5:
                                            #just hose
                                            $ line = renpy.random.choice(["You reach out and brush your hands across her cleft through the thin fabric",
                                                    "You grab her hose and pull them taut, elliciting a small gasp",
                                                    "You put your hand against her mound and grind against it",
                                                    "You reach into her gap and she gasps as you slide your hand across and stroke her lips through the thin material",
                                                    "Her legs twitch a bit as you press your thumb against her",
                                                    "She gasps as you reach under her hose and lightly stroke her ass",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                                    else: #skirt, but nothing else
                                            $ line = renpy.random.choice(["You reach under skirt and brush across her bare lips",
                                                    "You lift her skirt a bit and grind against her warm mound",
                                                    "You lift her skirt a bit and she gasps as you stroke her moist lips",
                                                    "Her legs twitch a bit beneath her skirt as you press your thumb against her"
                                                    "She gasps as you rub her bare pussy",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                                            if D20S <= 10:
                                                $ TempFocus += 3 if Player.Focus < 50 else 1
                                                $ Templust += 4 if GirlA.lust > 40 else 2
                                                $ GirlA.Addict -= 2
                                            else: #If it touches skin
                                                $ TempFocus += 1
                                                $ Templust += 1

                            #no skirt or pants
                            elif (GirlA.PantsNum() == 6 or (GirlA == RogueX and GirlA.Panties == "shorts")) and not GirlA.PantiesDown:
                                        # just shorts on
                                        $ line = renpy.random.choice(["You reach out and brush your hands across her pussy through the shorts",
                                                "You slide a hand down her shorts, and brush your hands across her pussy underneath",
                                                "You put your hand against her mound and grind against it",
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her warm mound",
                                                "As you dig your thumb into her, she gasps and raises up a bit",
                                                "She gasps as you reach under her and lightly stroke her ass through the thin shorts",
                                                "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                            elif GirlA.Panties and not GirlA.PantiesDown:
                                        #Just panties
                                        $ line = renpy.random.choice(["You reach out and brush your hands across her panties",
                                                "You grab her panties and pull them taut, elliciting a small gasp",
                                                "You put your hand against her mound and grind against it",
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her lips through the thin material",
                                                "Her legs twitch a bit as you press your thumb against her",
                                                "She gasps as you reach under her panties and lightly stroke her ass",
                                                "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                            elif GirlA.HoseNum() >= 5:
                                        #just hose
                                        $ line = renpy.random.choice(["You reach out and brush your hands across her cleft through the thin fabric",
                                                "You grab her hose and pull them taut, elliciting a small gasp",
                                                "You put your hand against her mound and grind against it",
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her lips through the thin material",
                                                "Her legs twitch a bit as you press your thumb against her",
                                                "She gasps as you reach under her hose and lightly stroke her ass",
                                                "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                            else: #nothing
                                        $ line = renpy.random.choice(["You reach out and brush your hands across her bare lips",
                                                "You put your hand against her mound and grind against it",
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her lips",
                                                "Her legs twitch a bit as you press your thumb against her",
                                                "She gasps as you reach under her and lightly stroke her ass",
                                                "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                                        if D20S <= 10:
                                            $ TempFocus += 3 if Player.Focus < 50 else 1
                                            $ Templust += 4 if GirlA.lust > 40 else 2
                                            $ GirlA.Addict -= 2
                                        else: #If it touches skin
                                            $ TempFocus += 1
                                            $ Templust += 1

                            if D20S > 10:#If it touches skin
                                $ TempFocus += 3 if Player.Focus < 50 else 1
                                $ Templust += 4 if GirlA.lust > 40 else 2
                                $ GirlA.Addict -= 2
                            else:
                                $ TempFocus += 2 if Player.Focus < 50 else 1
                                $ Templust += 2 if GirlA.lust > 40 else 1
                            if GirlA.Pierce and D20S <= 3:
                                    "You tug on her piercing with your thumb, then let it snap back"


    # end fondle pussy                               /////////////////////////////////////////////////////////////////////////////


    elif primary_action == "eat_pussy":
                            $ line = renpy.random.choice(["You continue to lick " + GirlA.name + "'s pussy. ",
                                                    "You continue to suck " + GirlA.name + "'s pussy. ",
                                                    "You continue to tongue " + GirlA.name + "'s pussy. "])

                            if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                            $ line = renpy.random.choice(["You can feel her twitching as you grind your tongue against her, even through the thick material",
                                                    "She gasps as you press on her clit through the thick fabric",
                                                    "You rub her clit with your nose as you dive into her pussy with your tongue",
                                                    "You put your hand against her mound and lick the surface of her pants",
                                                    "With a little nibble, you tug at the denim",
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])
                                            $ TempFocus += 1 if Player.Focus < 70 else 0
                                            $ Templust += 3 if GirlA.lust > 60 else 2
                            else:
                                if GirlA.wearing_skirt:
                                        if GirlA.Panties == "shorts" and not GirlA.PantiesDown:
                                                #shorts on
                                                $ line = renpy.random.choice(["You push her skirt up and lick at her pussy through her shorts",
                                                        "You bend down and lick the edges of her lips through the shorts",
                                                        "You spread the lips back beneath her shorts, and she gasps as you slide your tongue across them",
                                                        "You can feel her twitching as you grind your tongue against her clit",
                                                        "She gasps as you suck on her clit through the thin fabric",
                                                        "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                        "You put your hand against her mound and lick the juice from her thin shorts",
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the walls aside",
                                                        "She gasps as you reach under her warm lips and lightly stroke her ass"])
                                        elif GirlA.Panties and not GirlA.PantiesDown:
                                                #Just panties
                                                $ line = renpy.random.choice(["You push her skirt up and lick at her pussy through her panties",
                                                        "You bend down and stroke the edges of her panties with your tongue",
                                                        "You spread the lips back beneath her panties, and she gasps as you slide your tongue across them",
                                                        "You can feel her twitching as you grind your tongue against her clit",
                                                        "She gasps as you suck on her clit through the thin fabric",
                                                        "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                        "You put your hand against her mound and lick the juice from her thin panties",
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the walls aside",
                                                        "She gasps as you reach under her warm lips and lightly stroke her ass"])
                                        elif GirlA.HoseNum() >= 5:
                                                #just hose
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
                                        else: #skirt, but nothing else
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
                                                    $ TempFocus += 3 if Player.Focus < 70 else 1
                                                    $ Templust += 4 if GirlA.lust > 60 else 2
                                                    $ GirlA.Addict -= 3
                                                else: #If it touches skin
                                                    $ TempFocus += 1
                                                    $ Templust += 1

                                #no skirt or pants
                                elif (GirlA.PantsNum() == 6 or (GirlA == RogueX and GirlA.Panties == "shorts")) and not GirlA.PantiesDown:
                                            # just shorts on
                                            $ line = renpy.random.choice(["You bend down and lick the edges of her lips through her shorts",
                                                    "You spread the lips back beneath her shorts, and she gasps as you slide your tongue across them",
                                                    "You can feel her twitching as you grind your tongue against her clit",
                                                    "She gasps as you suck on her clit through the thin fabric",
                                                    "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                    "You put your hand against her mound and lick the juice from her thin shorts",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the walls aside",
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])
                                elif GirlA.Panties and not GirlA.PantiesDown:
                                            #Just panties
                                            $ line = renpy.random.choice(["You bend down and stroke the edges of her panties with your tongue",
                                                    "You spread the lips back beneath her panties, and she gasps as you slide your tongue across them",
                                                    "You can feel her twitching as you grind your tongue against her clit",
                                                    "She gasps as you suck on her clit through the thin fabric",
                                                    "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                    "You put your hand against her mound and lick the juice from her thin panties",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the walls aside",
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])
                                elif GirlA.HoseNum() >= 5:
                                            #just hose
                                            $ line = renpy.random.choice(["You bend down and stroke her lips with your tongue",
                                                    "You spread the lips back beneath her hose, and she gasps as you slide your tongue across them",
                                                    "You can feel her twitching as you grind your tongue against her clit",
                                                    "She gasps as you suck on her clit through the thin fabric",
                                                    "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                    "You put your hand against her mound and lick the juice from her thin hose",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the walls aside",
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])
                                else: #nothing
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
                                                $ TempFocus += 3 if Player.Focus < 70 else 1
                                                $ Templust += 4 if GirlA.lust > 60 else 2
                                                $ GirlA.Addict -= 3
                                            else: #If it touches skin
                                                $ TempFocus += 1
                                                $ Templust += 1

                                if D20S > 10: #If it touches skin
                                    $ TempFocus += 4 if Player.Focus < 70 else 1
                                    $ Templust += 10 if GirlA.lust > 60 else 5
                                    $ GirlA.Addict -= 3
                                else:
                                    $ TempFocus += 2 if Player.Focus < 50 else 1
                                    $ Templust += 5 if GirlA.lust > 60 else 3
                                if GirlA.Pierce and D20S <= 3:
                                        "You tug on her piercing with your teeth, then let it snap back"

    # end lick pussy                               /////////////////////////////////////////////////////////////////////////////

    elif primary_action == "fondle_ass":
                        $ line = renpy.random.choice(["You continue to fondle " + GirlA.name + "'s ass. ",
                                                "You continue to feel up " + GirlA.name + "'s ass. ",
                                                "You continue to grope " + GirlA.name + "'s ass. "])

                        if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                        $ line = renpy.random.choice(["You reach out and brush your hands across the back of her pants",
                                                "You slide a hand down her pants, and firmly cup her ass",
                                                "You put your hand against her rear and grind against it",
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her warm mound",
                                                "As you dig your thumb into her, she gasps and raises up a bit",
                                                "She gasps as you reach under her and lightly stroke her ass through the pants",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])

                        elif GirlA.wearing_skirt:
                                # skirt
                                if GirlA.Panties == "shorts" and not GirlA.PantiesDown:
                                        #shorts on
                                        $ line = renpy.random.choice(["You reach under skirt and brush across her shorts",
                                                "You lift her skirt a bit and grind against her shorts",
                                                "You lift her skirt a bit and she gasps as you pull her shorts aside and stroke across her butt",
                                                "Her legs twitch a bit beneath her skirt as you give her cheeks a firm squeeze",
                                                "She gasps as you stroke her asshole through her shorts",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
                                elif GirlA.Panties and not GirlA.PantiesDown:
                                        #Just panties
                                        $ line = renpy.random.choice(["You reach under skirt and brush across her panties",
                                                "You lift her skirt a bit and grind against her panties",
                                                "You lift her skirt a bit and she gasps as you pull her panties aside and stroke across her butt",
                                                "Her legs twitch a bit beneath her skirt as you give her cheeks a firm squeeze",
                                                "She gasps as you stroke her asshole through her panties",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
                                elif GirlA.HoseNum() >= 5:
                                        #just hose
                                        $ line = renpy.random.choice(["You reach under skirt and brush across her hose",
                                                "You lift her skirt a bit and grind against her hose",
                                                "You lift her skirt a bit and she gasps as you pull her hose aside and stroke across her butt",
                                                "Her legs twitch a bit beneath her skirt as you give her cheeks a firm squeeze",
                                                "She gasps as you stroke her asshole through her hose",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
                                else: #skirt, but nothing else
                                        $ line = renpy.random.choice(["You reach under skirt and brush across her bare ass",
                                                "You lift her skirt a bit and grind against her warm cheeks",
                                                "You lift her skirt a bit and she gasps as you stroke asshole",
                                                "Her legs twitch a bit beneath her skirt as you press your thumb against her firm rear",
                                                "She gasps as you rub her bare hole",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
                                        if D20S <= 10:
                                            $ TempFocus += 2 if Player.Focus < 50 else 1
                                            $ Templust += 3 if GirlA.lust > 40 else 2
                                            $ GirlA.Addict -= 1
                                        else: #If it touches skin
                                            $ TempFocus += 1
                                            $ Templust += 1

                        #no skirt or pants
                        elif (GirlA.PantsNum() == 6 or (GirlA == RogueX and GirlA.Panties == "shorts")) and not GirlA.PantiesDown:
                                    # just shorts on
                                    $ line = renpy.random.choice(["You reach out and brush your hands across her lightly covered cheeks",
                                            "You grab her shorts and pull them taut, elliciting a small gasp",
                                            "You reach into her gap and she gasps as you slide your hand across and stroke her hole through the thin material",
                                            "Her legs twitch a bit as you grind her puckered hole",
                                            "She gasps as you reach under her shorts and lightly stroke her warm flesh",
                                            "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
                        elif GirlA.Panties and not GirlA.PantiesDown:
                                    # panties
                                    $ line = renpy.random.choice(["You reach out and brush your hands across her barely covered cheeks",
                                            "You grab her panties and pull them taut, elliciting a small gasp",
                                            "You reach into her gap and she gasps as you slide your hand across and stroke her hole through the thin material",
                                            "Her legs twitch a bit as you grind her puckered hole",
                                            "She gasps as you reach under her panties and lightly stroke her warm flesh",
                                            "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
                        elif GirlA.HoseNum() >= 5:
                                    #just hose
                                    $ line = renpy.random.choice(["You reach out and brush your hands across her barely covered cheeks",
                                            "You grab her hose and pull them taut, elliciting a small gasp",
                                            "You reach into her gap and she gasps as you slide your hand across and stroke her hole through the thin material",
                                            "Her legs twitch a bit as you grind her puckered hole",
                                            "She gasps as you reach under her hose and lightly stroke her warm flesh",
                                            "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
                        else: #nothing
                                    $ line = renpy.random.choice(["You reach out and brush your hands across her bare ass",
                                            "You put your hand against her firm rear and grind against it",
                                            "You reach into her gap and she gasps as you slide your hand across and stroke her puckered hole",
                                            "Her legs twitch a bit as you press your thumb against her",
                                            "She gasps as you reach under her and lightly stroke her ass",
                                            "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
                                    if D20S <= 10:
                                        $ TempFocus += 2 if Player.Focus < 50 else 1
                                        $ Templust += 3 if GirlA.lust > 40 else 2
                                        $ GirlA.Addict -= 1
                                    else: #If it touches skin
                                        $ TempFocus += 1
                                        $ Templust += 1

                        if D20S > 10:#If it touches skin
                            $ TempFocus += 2 if Player.Focus < 50 else 1
                            $ Templust += 3 if GirlA.lust > 40 else 2
                            $ GirlA.Addict -= 1
                        else:
                            $ TempFocus += 2 if Player.Focus < 50 else 1
                            $ Templust += 2 if GirlA.lust > 40 else 1

    # end fondle ass                               /////////////////////////////////////////////////////////////////////////////

    elif primary_action == "finger_ass":
                            $ line = renpy.random.choice(["You continue to finger " + GirlA.name + "'s asshole. ",
                                                    "You continue to finger bang " + GirlA.name + "'s asshole. ",
                                                    "You continue to finger " + GirlA.name + "'s rim. "])

                            if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                            $ line = renpy.random.choice(["You slide a hand down her pants, and slide your fingers into her anus",
                                                    "You push her panties aside, and slide a finger between her cheeks",
                                                    "You slide a finger into her tight anus",
                                                    "You pull her pants out a bit and she gasps as you slide a finger up her hole",
                                                    "You gasps as you rub her asshole with your fingers"])
                            elif GirlA.wearing_skirt:
                                    if GirlA.Panties == "shorts" and not GirlA.PantiesDown:
                                            #shorts on
                                            $ line = renpy.random.choice(["You push her skirt and shorts up, and slide a finger into her anus",
                                                    "You slide a finger into her tight anus",
                                                    "You lift her skirt a bit and she gasps as you pull her shorts up and slide a finger into her anus",
                                                    "You rub her pussy with your thumb as you dive into her anus with your middle finger"])
                                    elif GirlA.Panties and not GirlA.PantiesDown:
                                            #Just panties
                                           $ line = renpy.random.choice(["You push her skirt and panties aside, and slide a finger into her anus",
                                                    "You slide a finger into her tight anus",
                                                    "You lift her skirt a bit and she gasps as you pull her panties aside and slide a finger into her anus",
                                                    "You rub her clit with your thumb as you dive into her pussy with your middle finger"])
                                    else: #skirt, but nothing else
                                             $ line = renpy.random.choice(["You push her skirt aside, and slide a finger into her anus",
                                                    "You slide a finger into her tight anus",
                                                    "You lift her skirt a bit and she gasps as you slide a finger into her anus",
                                                    "You rub her pussy with your thumb as you dive into her anus with your middle finger"])
                            #no skirt or pants
                            elif (GirlA.PantsNum() == 6 or (GirlA == RogueX and GirlA.Panties == "shorts")) and not GirlA.PantiesDown:
                                    # just shorts on
                                    $ line = renpy.random.choice(["You slide a hand down her shorts, and slide a finger into her anus",
                                                "You push her shorts up, and slide a finger between her lips",
                                                "You slide a finger into her tight anus",
                                                "You pull her shorts out a bit and she gasps as you slide a finger into her anus",
                                                "You rub her pussy with your palm as you dive into her anus with your middle finger"])
                            elif GirlA.Panties and not GirlA.PantiesDown:
                                        #Just panties
                                        $ line = renpy.random.choice(["You push her panties aside, and slide a finger into her anus",
                                                "You slide a finger into her tight anus",
                                                "You lift her panties a bit and she gasps as you and slide a finger into her anus"])
                            else: #nothing
                                        $ line = renpy.random.choice(["You reach out and slide a finger into her anus",
                                                "You slide a finger into her tight anus",
                                                "You press into her and she gasps as you  slide a finger into her anus",
                                                "You rub her pussy with your thumb as you dive into her anus with your middle finger"])

                            $ TempFocus += 2 if Player.Focus < 50 else 1
                            $ Templust += 6 if GirlA.lust > 70 else 3
                            if not GirlA.Loose:
                                    $ Templust -= 3
                            elif GirlA.Loose < 2:
                                    $ Templust += 1

                            $ GirlA.Addict -= 2

    # end insert ass                              /////////////////////////////////////////////////////////////////////////////

    elif primary_action == "eat_ass":
                            $ line = renpy.random.choice(["You continue to lick " + GirlA.name + "'s ass. ",
                                                    "You continue to suck " + GirlA.name + "'s ass. ",
                                                    "You continue to tongue " + GirlA.name + "'s ass. "])

                            if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                                $ line = renpy.random.choice(["You can feel her twitching as you grind your tongue against her anus, even through the thick material",
                                                        "She gasps as you press on her asshole through the thick fabric",
                                                        "You put your hand against her mound and lick the surface of her pants",
                                                        "With a little nibble, you tug at the denim"])
                                                $ TempFocus += 1 if Player.Focus < 70 else 0
                                                $ Templust += 1 if GirlA.lust < 60 else 0
                            else:
                                if GirlA.wearing_skirt:
                                        if GirlA.Panties == "shorts" and not GirlA.PantiesDown:
                                                #shorts on
                                                $ line = renpy.random.choice(["You push her skirt up and lick at her asshole through her shorts",
                                                        "You bend down and stroke the edges of her shorts with your tongue",
                                                        "You spread the cheeks back beneath her shorts, and she gasps as you slide your tongue into it",
                                                        "You can feel her twitching as you grind your tongue against her anus",
                                                        "She gasps as you suck on her asshole through the thin fabric",
                                                        "You rub her pussy with your thumb as you dive into her asshole with your tongue",
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the rim aside"])
                                        elif GirlA.Panties and not GirlA.PantiesDown:
                                                #Just panties
                                                $ line = renpy.random.choice(["You push her skirt up and lick at her asshole through her panties",
                                                        "You bend down and stroke the edges of her panties with your tongue",
                                                        "You spread the cheeks back beneath her panties, and she gasps as you slide your tongue into it",
                                                        "You can feel her twitching as you grind your tongue against her anus",
                                                        "She gasps as you suck on her asshole through the thin fabric",
                                                        "You rub her pussy with your thumb as you dive into her asshole with your tongue",
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the rim aside"])
                                        elif GirlA.HoseNum() >= 5:
                                                #just hose
                                               $ line = renpy.random.choice(["You push her skirt up and lick at her asshole through her hose",
                                                        "You bend down and stroke the edges of her hose with your tongue",
                                                        "You spread the cheeks back beneath her hose, and she gasps as you slide your tongue into it",
                                                        "You can feel her twitching as you grind your tongue against her anus",
                                                        "She gasps as you suck on her asshole through the thin fabric",
                                                        "You rub her pussy with your thumb as you dive into her asshole with your tongue",
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the rim aside"])
                                        else: #skirt
                                                $ line = renpy.random.choice(["You push her skirt aside and stroke her asshole with your tongue",
                                                        "You spread the cheeks back, and she gasps as you slide your tongue into it",
                                                        "You can feel her twitching as you grind your tongue against her asshole",
                                                        "She gasps as you suck on her anus",
                                                        "You rub her pussy with your thumb as you dive into her asshole with your tongue",
                                                        "You put your hand against her mound and lick around her rim",
                                                        "You slowly lick into her gap and she gasps as you press the rim apart"])
                                                if D20S <= 10:
                                                    $ TempFocus += 2 if Player.Focus < 70 else 0
                                                    $ Templust += 3 if GirlA.lust > 60 else 1
                                                    $ GirlA.Addict -= 3
                                                else: #If it touches skin
                                                    $ TempFocus += 1
                                                    $ Templust += 1

                                #no skirt or pants
                                elif (GirlA.PantsNum() == 6 or (GirlA == RogueX and GirlA.Panties == "shorts")) and not GirlA.PantiesDown:
                                            # just shorts on
                                            $ line = renpy.random.choice(["You bend down and stroke the edges of her shorts with your tongue",
                                                    "You spread the cheeks back beneath her shorts, and she gasps as you slide your tongue into it",
                                                    "You can feel her twitching as you grind your tongue against her anus",
                                                    "She gasps as you suck on her anus through the thin fabric",
                                                    "You rub her pussy with your thumb as you dive into her anus with your tongue",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the rim apart"])
                                elif GirlA.Panties and not GirlA.PantiesDown:
                                            #Just panties
                                            $ line = renpy.random.choice(["You bend down and stroke the edges of her panties with your tongue",
                                                    "You spread the cheeks back beneath her panties, and she gasps as you slide your tongue into it",
                                                    "You can feel her twitching as you grind your tongue against her anus",
                                                    "She gasps as you suck on her anus through the thin fabric",
                                                    "You rub her pussy with your thumb as you dive into her anus with your tongue",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the rim apart"])
                                elif GirlA.HoseNum() >= 5:
                                            #just hose
                                            $ line = renpy.random.choice(["You bend down and stroke the edges of her hose with your tongue",
                                                    "You spread the cheeks back beneath her hose, and she gasps as you slide your tongue into it",
                                                    "You can feel her twitching as you grind your tongue against her anus",
                                                    "She gasps as you suck on her anus through the thin fabric",
                                                    "You rub her pussy with your thumb as you dive into her anus with your tongue",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the rim apart"])
                                else: #nothing
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
                                                $ TempFocus += 2 if Player.Focus < 70 else 0
                                                $ Templust += 3 if GirlA.lust > 60 else 1
                                                $ GirlA.Addict -= 3
                                            else: #If it touches skin
                                                $ TempFocus += 1
                                                $ Templust += 1

                                if D20S > 10: #If it touches skin
                                    $ TempFocus += 3 if Player.Focus < 70 else 0
                                    $ Templust += 9 if GirlA.lust > 60 else 4
                                    $ GirlA.Addict -= 3
                                else:
                                    $ TempFocus += 1 if Player.Focus < 50 else 0
                                    $ Templust += 4 if GirlA.lust > 60 else 2

                            $ Templust += 2 if GirlA.Loose > 1 else 0 #Bonus lust if she's anal experienced

    # end lick ass                               /////////////////////////////////////////////////////////////////////////////

    elif primary_action == "dildo_pussy":
                        if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                $ line = renpy.random.choice(["You rub the dildo against the outside of her pants",
                                        "You slap the dildo lightly against her mound"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0
                                $ Templust += 3 if GirlA.lust < 50 else 1
                        elif GirlA.HoseNum() >= 10:
                                $ line = renpy.random.choice(["You rub the dildo against the outside of her tights",
                                        "You slap the dildo lightly at the outside of her tights"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0
                                $ Templust += 3 if GirlA.lust < 50 else 1
                        elif GirlA.HoseNum() >= 5:
                                $ line = renpy.random.choice(["You rub the dildo against the outside of her hose",
                                        "You slap the dildo lightly at the outside of her hose"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0
                                $ Templust += 3 if GirlA.lust < 50 else 1
                        else:
                                if GirlA.wearing_skirt and GirlA.Panties:
                                    $ line = renpy.random.choice(["You push her skirt and panties aside, and slide the dildo into her pussy",
                                            "You slide the toy deep into her pussy",
                                            "She gasps as you rotate the dildo within her tight pussy",
                                            "You rub her clit with your thumb as you dive into her puss with the rubber phallus"])
                                    $ TempFocus += 2 if Player.Focus < 50 else 1
                                    $ Templust += 8 if GirlA.lust > 70 else 5
                                elif GirlA.wearing_skirt:
                                    $ line = renpy.random.choice(["You push her skirt aside, and slide the dildo into her tight hole",
                                            "You slide the toy deep into her pussy",
                                            "You lift her skirt a bit and she gasps as you slide the dildo firmly into her tight puss",
                                            "She gasps as you rotate the dildo within her slit",
                                            "You rub her clit with your thumb as you dive into her pussy with the rubber phallus"])
                                    $ TempFocus += 2 if Player.Focus < 50 else 1
                                    $ Templust += 8 if GirlA.lust > 70 else 5
                                elif GirlA.Panties and not GirlA.PantiesDown:
                                    $ line = renpy.random.choice(["You push her panties aside, and slide the dildo into her tight pussy",
                                            "You slide the dildo into her moist slit and stroke it rapidly",
                                            "You lift her panties a bit and she gasps as you slide the dildo between her lower lips",
                                            "She gasps as you rub her tight pussy with the toy",
                                            "You rub her clit with your thumb as you dive into her pussy with the dildo",
                                            "You reach into her gap and she gasps as you slide the dildo in and press against her tight slit through the thin material"])
                                    $ TempFocus += 2 if Player.Focus < 50 else 1
                                    $ Templust += 8 if GirlA.lust > 70 else 5
                                else:
                                    $ line = renpy.random.choice(["You reach out and slide the dildo along her mound",
                                            "You slide the toy into her pussy and stroke it slowly",
                                            "You pull her lips apart and she gasps as you slide the dildo between them",
                                            "You can feel her twitching as you press your thumb against her clit",
                                            "She gasps as you rub her clit with the hard rubber",
                                            "You rub her clit with your thumb as you dive into her pussy with the dildo",
                                            "You reach into her gap and she gasps as you slide the toy across and press it into her wet pussy"])
                                    $ TempFocus += 3 if Player.Focus < 50 else 1
                                    $ Templust += 10 if GirlA.lust > 70 else 8
    # end dildo pussy                              /////////////////////////////////////////////////////////////////////////////

    elif primary_action == "dildo_anal":
                        if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                $ line = renpy.random.choice(["You rub the dildo against the outside of her pants",
                                        "You slap the dildo lightly against her ass"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0
                                $ Templust += 3 if GirlA.lust < 50 else 1
                        elif GirlA.HoseNum() >= 10:
                                $ line = renpy.random.choice(["You rub the dildo against the outside of her tights",
                                        "You slap the dildo lightly at the outside of her tights"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0
                                $ Templust += 3 if GirlA.lust < 50 else 1
                        elif GirlA.HoseNum() >= 5:
                                $ line = renpy.random.choice(["You rub the dildo against the outside of her hose",
                                        "You slap the dildo lightly at the outside of her hose"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0
                                $ Templust += 3 if GirlA.lust < 50 else 1
                        else:
                                if GirlA.wearing_skirt and GirlA.Panties:
                                    $ line = renpy.random.choice(["You push her skirt and panties aside, and slide the dildo into her ass",
                                            "You slide the toy deep into her ass",
                                            "She gasps as you rotate the dildo within her tight asshole",
                                            "You rub her clit with your thumb as you dive into her ass with the rubber phallus"])
                                    $ TempFocus += 2 if Player.Focus < 50 else 1
                                    $ Templust += 8 if GirlA.lust > 70 else 5
                                elif GirlA.wearing_skirt:
                                    $ line = renpy.random.choice(["You push her skirt aside, and slide the dildo into her tight hole",
                                            "You slide the toy deep into her ass",
                                            "You lift her skirt a bit and she gasps as you slide the dildo firmly into her tight anus",
                                            "She gasps as you rotate the dildo within her ass",
                                            "You rub her clit with your thumb as you dive into her ass with the rubber phallus"])
                                    $ TempFocus += 2 if Player.Focus < 50 else 1
                                    $ Templust += 8 if GirlA.lust > 70 else 5
                                elif GirlA.Panties and not GirlA.PantiesDown:
                                    $ line = renpy.random.choice(["You push her panties aside, and slide the dildo into her tight ass",
                                            "You slide the dildo into her ass and stroke it rapidly",
                                            "You lift her panties a bit and she gasps as you slide the dildo between her cheeks",
                                            "She gasps as you rub her tight asshole with the toy",
                                            "You rub her clit with your thumb as you dive into her asshole with the dildo",
                                            "You reach into her gap and she gasps as you slide the dildo in and press against her tight anus through the thin material"])
                                    $ TempFocus += 2 if Player.Focus < 50 else 1
                                    $ Templust += 8 if GirlA.lust > 70 else 5
                                else:
                                    $ line = renpy.random.choice(["You reach out and slide the dildo between her cheeks",
                                            "You slide the toy into her asshole and stroke it against the sides",
                                            "You pull her cheeks apart and she gasps as you slide the dildo between them",
                                            "You can feel her twitching as you press your thumb against her anus",
                                            "She gasps as you rub her anus with the hard rubber",
                                            "You rub her clit with your thumb as you dive into her asshole with the dildo",
                                            "You reach into her gap and she gasps as you slide the toy across and press it into her firm anus"])
                                    $ TempFocus += 3 if Player.Focus < 50 else 1
                                    $ Templust += 10 if GirlA.lust > 70 else 6
                                if not GirlA.Loose:
                                        $ Templust -= 3
                                elif GirlA.Loose < 2:
                                        $ Templust += 1
    # end dildo ass                              /////////////////////////////////////////////////////////////////////////////

    elif primary_action == "masturbation":
                call Girl_Self_lines(GirlA) #Rog*ue_Self_lines
                if "unseen" not in GirlA.recent_history:
                    if offhand_action == "jackin" or "cockout" in Player.recent_history:
                            $ Templust += 2

    elif primary_action == "lesbian":
                call SexDialog_Threeway(GirlA,"lesbian",GirlB=Partner) #Rog*ue_SexDialog_Threeway("lesbian")

    elif primary_action == "footjob":
                        $ line = GirlA.name + " continues stroke your cock with her feet. "

                        if not action_speed:
                                    if GirlA.action_counter["footjob"] > 2:
                                            $ line = line + "She just seems to be enjoying the feel of it"
                                            $ Templust += 2 if GirlA.lust < 60 else 0
                                    else:
                                            $ line = line + "She just seems to be looking it over"
                                            $ Templust += 2 if GirlA.lust < 40 else 0
                                            $ TempFocus += -3 if Player.Focus > 50 else 2

                                    $ GirlA.Addict -= 1 if D20S > 10 else 2
                                    return

                        if GirlA.action_counter["footjob"] > 4:                          # After the 5th time
                                    if action_speed <= 1:                      #slow
                                        $ line = line + renpy.random.choice(["Her movements have become almost masterful, her slightest touch starts you twitching",
                                                "She slowly caresses you in a way that makes your blood boil, then pulls back at the last second",
                                                "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                                "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                                "You can't tell where she is at any moment, all you know is that it works"])

                                        $ TempFocus += 20 if Player.Focus > 70 else 5

                                    else:                               #fast
                                        $ line = line + renpy.random.choice(["Her movements have become almost masterful, her slightest touch starts you twitching",
                                                "Her expert strokes will have you boiling over in seconds",
                                                "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                                "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                                "You can't tell where she is at any moment, all you know is that it works"])

                                        $ TempFocus += 20 if Player.Focus < 40 else 5

                        elif GirlA.action_counter["footjob"] >= 3:                       #third through 5th time
                                    if action_speed <= 1:                      #slow
                                        $ line = line + renpy.random.choice(["She's begining to figure things out, her toes cause tingles as they caress the shaft",
                                                "She's still learning, but learning fast",
                                                "She has a smooth motion going now, gentle and precise",
                                                "Her lessons are paying off, she's really becoming very talented at this",
                                                "She gently caresses the shaft, and brushes the balls in her other foot, giving them a light massage"])

                                        $ TempFocus += 15 if Player.Focus > 60 else 5

                                    else:                               #fast
                                        $ line = line + renpy.random.choice(["She's begining to figure things out, her toes cause tingles as they caress the shaft",
                                                "She's still learning, but learning fast",
                                                "Her feet glide smoothly across your cock",
                                                "She has a smooth motion going now, gentle and precise",
                                                "Her lessons are paying off, she's really becoming very talented at this",
                                                "She quickly strokes your cock, with a very deft pressure"])

                                        $ TempFocus += 15 if Player.Focus < 60 else 7

                        else:                                   #First and second time
                                if action_speed <= 1:                      #slow
                                    $ line = line + renpy.random.choice(["She makes up for her inexperience with determination, carefully stroking your cock",
                                            "She moves her feet up and down the shaft. She's a little rough at this, but at least she tries",
                                            "She strokes you gently. She isn't quite sure what to do with the balls",
                                            "Her toes fumble with your shaft a bit",
                                            "She nudges one of your balls too tightly, but stops when you wince",
                                            "She has a firm grip, and she's not letting go. This may take a few tries"])

                                    $ TempFocus += 10 if Player.Focus > 60 else 5
                                else:                               #fast
                                    $ line = line + renpy.random.choice(["She really wasn't prepared for speeding up, and your cock often slips between her feet",
                                            "She rapidly moves her feet up and down the shaft. She's a little rough at this, but at least she tries",
                                            "She strokes you a bit too quickly, the friction is a bit uncomfortable",
                                            "Her toes fumble with your shaft a bit",
                                            "She nudges one of your balls too tightly, but stops when you wince",
                                            "She has a firm grip, and she's not letting go. This train is out of control"])

                                    $ TempFocus += 8 if Player.Focus > 60 else 2

                        $ Templust += 2 if GirlA.lust < 60 else 0
                        $ Templust += 3 if GirlA.action_counter["footjob"] > 2 else 0
                        $ GirlA.Addict -= 1

    #End Footy dialog ////////////////////////////////////////////////////////////////////////////////////////////////////////

    elif primary_action == "psy":
            $ line = GirlA.name + " continues work your cock. "

            if not action_speed:
                        $ line = GirlA.name + "'s construct just rests on your cock. "
                        if GirlA.action_counter["handjob"] > 2:
                                $ line = line + "She seems to be enjoying your reaction"
                                $ Templust += 2 if GirlA.lust < 60 else 0
                        else:
                                $ line = line + "She just seems to be looking it over"
                                $ Templust += 2 if GirlA.lust < 40 else 0
                                $ TempFocus += -3 if Player.Focus > 50 else 2
                        return

            if Psychic == "handjob" or not Psychic:
                        # After the 5th time
                        $ line = line + renpy.random.choice(["Her movements are masterful, her slightest touch starts you twitching",
                                    "She's something of an expert, you feel a light tingle in your shaft",
                                    "She slowly caresses you in a way that makes your blood boil, then pulls back at the last second",
                                    "She really knows what to do, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                    "You can't tell where she is at any moment, all you know is that it works"])
                        if action_speed <= 1:
                            #slow
                            $ TempFocus += 15 if Player.Focus > 60 else 5
                        else:
                            $ TempFocus += 15 if Player.Focus < 60 else 7
                        $ Templust += 2 if GirlA.lust < 60 else 0
            elif Psychic == "mouth":
                        $ line = line + renpy.random.choice(["She masterfully bobs on your cock, and it twitches with each stroke",
                                "She smoothly bobs up and down on your cock, a frenzy of motion",
                                "She gobbles you up all the way to the base, then quickly draws out and plunges back in",
                                "She's really getting good at this, alternating between deep suction and quick licks across the head",
                                "She moves very smoothly, bobbing in and out like she's been doing this for years",
                                "She puts the shaft into her mouth and her tounge swirls rapidly around it"])
                        $ TempFocus += 22 if Player.Focus > 40 else 10
                        $ Templust += 3 if GirlA.lust > 60 else 1
            elif Psychic == "tits":
                        $ line = renpy.random.choice([GirlA.name + " juggles her breast projections up and down around your cock",
                                GirlA.name + " lightly strokes the head as it pops up between her tits",
                                GirlA.name + " has a smooth motion going now, gentle and precise",
                                GirlA.name + " pauses to rub her nipples across the shaft",
                                GirlA.name + " gently caresses the shaft between her tits"])
                        $ TempFocus += 15 if Player.Focus < 60 else 5
                        $ Templust += 6 if GirlA.lust > 60 else 3
            elif Psychic == "sex" or Psychic == "anal":
                        #third through 5th time fast
                        $ line = line + renpy.random.choice(["It bounces rapidly against your cock",
                            "You thrust into it and she squeaks a bit",
                            "You quickly grind back and forth inside it",
                            "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                            "You pound away at it",
                            "She grinds it furiously back and forth along your cock"])
                        $ TempFocus += 12 if Player.Focus > 60 else 8
                        $ Templust += 12 if GirlA.lust > 80 else 6


    #End Psychic dialog ////////////////////////////////////////////////////////////////////////////////////////////////////////

    elif primary_action == "kiss":
                        $ GirlA.Addict -= 3
                        $ GirlA.Addict -= 3 if GirlA == JubesX else 0
                        if GirlA.action_counter["kiss"] > 10 and GirlA.love >= 700:#Loving
                                $ line = renpy.random.choice(["She hungrily presses her lips against yours",
                                        "She confidently presses her lips against yours",
                                        "Her lips part as you hold her close",
                                        "You nibble her neck as she groans in pleasure",
                                        "You squeeze her tightly as your tongues jostle",
                                        "Her tongue dances around yours",
                                        "She nibbles your ear as her hands slide across your back",
                                        "Your hands slide down her body as your lips press hers"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0
                                $ TempFocus += 1 if Player.Focus < 90 else 0
                                $ Templust += 3 if GirlA.lust < 50 else 0
                                $ Templust += 1 if GirlA.lust < 90 else 0
                        elif GirlA.action_counter["kiss"] > 5 or GirlA == EmmaX:#reasonably experienced
                                $ line = renpy.random.choice(["She confidently presses her lips against yours",
                                        "You softly kiss her plump lips",
                                        "Her lips part as you hold her close",
                                        "You nibble her neck as she coos in pleasure",
                                        "You squeeze her tightly as your lips connect",
                                        "Her tongue flickers out to meet yours",
                                        "Your hands slide down her body as your lips brush hers"])
                                $ TempFocus += 1 if Player.Focus < 70 else 0
                                $ Templust += 3 if GirlA.lust < 50 else 0
                                $ Templust += 1 if GirlA.lust < 90 else 0
                        else:#basic kissing
                                $ line = renpy.random.choice(["She tentatively presses her lips against yours",
                                        "You softly kiss her plump lips",
                                        "Her lips part slightly as you hold her close",
                                        "You squeeze her tightly as your lips connect",
                                        "Your hands slide down her body as your lips brush hers"])
                                $ TempFocus += 1 if Player.Focus < 70 else 0
                                $ Templust += 2 if GirlA.lust < 30 else 0
                                $ Templust += 1 if GirlA.lust < 70 else 0

    # end kissing                              /////////////////////////////////////////////////////////////////////////////
    else: #no primary_action was set, somehow
        "No trigger was set, or it was '[primary_action]'. Please tell Oni what happend up to this point."
        $ line = "Huh."

    $ line = line + "."
    # Wrap-up
    $ Primarylust += Templust
    $ Secondarylust += Templust2 + 2

    return

label Offhand_Dialog(Girl=Primary, phrase=0):
    #This is the dialog for what you're doing with your other hand while a primary action takes place
    #called by Sex_Dialog, if offhand_action and D20S <= 15: call Offhand_Dialog
    if Girl not in all_Girls:
            return
    if not offhand_action: #If there are no offhand options set, return
            return

    $ D20X = renpy.random.randint(1,20)

    if offhand_action == "kiss":
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
                        $ Girl.change_stat("love", 75, 1)
                $ Primarylust += 2 if Girl.lust < 50 else 1

    elif offhand_action == "fondle_breasts":
                if Girl == EmmaX and D20X >= 15:
                    $ line = " You reach out and massage her enormous breasts."
                    $ Primarylust += 1
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
                $ Primarylust += 3
                $ TempFocus += 2 if Player.Focus < 90 else 0

    elif offhand_action == "suck_breasts":
            if Girl.ChestNum() > 1 or Girl.OverNum() > 1:
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
            $ Primarylust += 4 if 60 < Girl.lust < 80 else 2
            $ TempFocus += 3 if Player.Focus < 90 else 0

    elif offhand_action == "fondle_pussy":
            if Girl.Pubes and D20X >= 15:
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
            $ Primarylust += 4 if 60 < Girl.lust < 90 else 2
            $ TempFocus += 4 if Player.Focus < 90 else 0

    elif offhand_action == "eat_pussy":
            if Girl.PantsNum() <= 5 and Girl.PantiesNum() <= 1:
                if Girl.Pubes and D20X >= 15:
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
            $ Primarylust += 5 if Girl.lust > 50 else 2
            $ TempFocus += 4 if Player.Focus < 90 else 0

    elif offhand_action == "fondle_ass":
            $ line = renpy.random.choice([" You reach out and brush your hands across her ass.",
                    " You put your hand against her firm rear and grind against it.",
                    " You reach between her legs and she gasps as you stroke along her crevice.",
                    " Her legs twitch a bit as you press your thumb against her.",
                    " She gasps as you reach under her and lightly stroke her ass.",
                    " You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks."])
            $ Primarylust += 2 if Girl.lust < 50 else 1
            $ TempFocus += 1 if Player.Focus < 50 else 0
            $ TempFocus += 1 if Player.Focus < 80 else 0

    elif offhand_action == "finger_ass":
            $ line = renpy.random.choice([" You reach out and slide a finger into her ass.",
                    " You slide a finger into her asshole and stroke the roof of it.",
                    " You can feel her twitching as you press your thumb against her clit.",
                    " She gasps as you rub her asshole with your fingers.",
                    " You rub her pussy with your thumb as you dive into her asshole with your middle finger.",
                    " You reach into her gap and she gasps as you slide your hand across and press against her hole.",
                    " She gasps as you reach under her warm lips and lightly stroke her ass."])
            $ Primarylust += 3 if Girl.lust > 70 and Girl.Loose else 1
            $ TempFocus += 2 if Player.Focus < 90 else 0

    elif offhand_action == "jackin":
            if primary_action == "masturbation":
                    $ line = " You stroke your cock as you watch her go."
            elif primary_action == "lesbian":
                    $ line = " You stroke your cock as you watch them."
            elif primary_action == "handjob":
                    $ line = renpy.random.choice([" You also give it a little rub.",
                            " As she does so, you polish the knob a bit.",
                            " You help.",
                            " Your hand bumps into hers occasionally."])
            elif primary_action == "blowjob":
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
                $ Primarylust += 3 if 20 < Girl.lust < 70 else 2
                $ TempFocus += 1 if Player.Focus < 70 else 0
            $ TempFocus += 5
    return
    #End Offhand check

label Offhand_Set(action_context = action_context, Tempprimary_action = offhand_action,Girl=0):
    #called by various sex activities to set primary_action 2, which is the player's secondary action related to the primary girl
    #if the action_context is "shift focus," it means that the player is attempting to make his secondary action into his primary one.
    $ Girl = Girlcheck(Girl)
    if action_context == "shift focus":
            if Tempprimary_action:
                $ offhand_action = 0
                if Tempprimary_action == "fondle_breasts":
                        "You shift your attention to her breasts."

                        jump before_fondle
                elif Tempprimary_action == "suck_breasts":
                        "You shift your attention to her breasts."

                        jump before_fondle
                elif Tempprimary_action == "fondle_pussy":
                        "You shift your attention to her pussy."

                        jump before_fondle
                elif Tempprimary_action == "eat_pussy":
                        "You shift your attention to her pussy."

                        jump before_fondle
                elif Tempprimary_action == "fondle_ass":
                        "You shift your attention to her ass."

                        jump before_fondle
                elif Tempprimary_action == "finger_ass":
                        "You shift your attention to her ass."

                        jump before_fondle
                else: #If offhand_action is "kiss"
                        "You go back to kissing her deeply."
                        jump KissPrep
            else: #if there's no offhand_action
                "You aren't doing anything else to shift to."
            return
    # End "shift" situation

    if primary_action:
        $ action_context = "auto"
        menu:
            "Also kiss her." if primary_action in ("fondle_breasts","fondle_pussy", "fondle_thighs", "fondle_ass", "finger_ass", "sex", "anal", "hotdog", "dildo_pussy", "dildo_anal"):
                    "You lean in and start kissing her."
                    $ offhand_action = "kiss"

            "Also fondle her breasts." if primary_action in ("kiss","fondle_pussy", "fondle_thighs", "fondle_ass", "finger_ass", "suck_breasts", "eat_pussy", "eat_ass", "sex", "anal", "hotdog", "footjob", "dildo_pussy", "dildo_anal"):
                    $ offhand_action = "fondle_breasts"
                    call offhand_action(Girl)

            "Also suck her breasts." if primary_action in ("fondle_breasts","fondle_pussy", "fondle_thighs", "fondle_ass", "finger_ass", "sex", "anal", "hotdog", "dildo_pussy", "dildo_anal"):
                    $ offhand_action = "suck_breasts"
                    call offhand_action(Girl)

            "Also fondle her pussy." if primary_action in ("kiss","fondle_breasts","fondle_thighs", "fondle_ass", "finger_ass", "suck_breasts", "eat_pussy", "eat_ass", "sex", "anal", "hotdog", "footjob", "dildo_pussy", "dildo_anal"):
                    $ offhand_action = "fondle_pussy"
                    call offhand_action(Girl)

            "Also fondle her ass." if primary_action in ("kiss","fondle_breasts","fondle_pussy", "fondle_thighs", "finger_ass", "suck_breasts", "eat_pussy", "eat_ass", "sex", "anal", "hotdog", "footjob", "dildo_pussy", "dildo_anal"):
                    $ offhand_action = "fondle_ass"
                    call offhand_action(Girl)

            "Also finger her ass." if primary_action in ("fondle_breasts","fondle_pussy", "fondle_thighs", "fondle_ass", "suck_breasts", "eat_pussy", "eat_ass", "sex", "hotdog", "footjob", "dildo_pussy"):
                    $ offhand_action = "finger_ass"
                    call offhand_action(Girl)

            "Also jack it." if primary_action in ("fondle_breasts","fondle_pussy", "fondle_thighs", "fondle_ass", "finger_ass", "suck_breasts", "eat_pussy", "eat_ass", "dildo_pussy", "dildo_anal"):
                    call Jackin(Girl)

            "Nevermind":
                pass
    else: #if a primary_action is not found. . .
        "There's some kind of bug here, let Oni know."

    $ action_context = 0
    return

label Girl_Self_lines(GirlA = Primary, Mode = "T3", Action = girl_offhand_action, TemplustX = 0, TempFocusX = 0, D20X=0):
    # The Mode can be T3 for primary_action 3 for a masturbation option, or T5/second_girl_offhand_action if it's setting a Threeway action.
    # call Girl_Self_lines(GirlA,"T5",second_girl_offhand_action)  X Rogu*e_Self_lines("T5",second_girl_offhand_action)
    # This sets a Action if there isn't one, or sets an intitial line
    # Primary if called from main sex dialog, secondary if called from Threesome

    $ D20X = renpy.random.randint(1, 20) if not D20X else D20X

    $ line = 0
    if not Action or D20X >= 15:
            #if there is no appropriate trigger set or if RNG says to pick a new one. . .
            if primary_action != "masturbation" and "passive" in GirlA.Traits:
                    # This bypasses self-set if Rog*ue is told not to take initiative
                    $ line = 0
                    return
            call Girl_Self_Set(GirlA,Mode,Action) #Rog*ue_Self_Set(Mode, Action)

            if Mode == "T3":
                    #Sets Action based on the result
                    $ Action = girl_offhand_action
            else:
                    #if Mode == "T5"
                    $ Action = second_girl_offhand_action
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
                                    GirlA.name + "'s hands move across her body. ",
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
                        if primary_action == "massage":
                                $ TempFocusX += 10 if Player.Focus > 60 else 4
                                $ TempFocusX += 2 if GirlA.action_counter["handjob"] > 2 else 0
                        else:
                                $ TempFocus += 10 if Player.Focus > 60 else 4
                                $ TempFocus += 2 if GirlA.action_counter["handjob"] > 2 else 0

                        $ TemplustX += 2 if GirlA.lust < 60 else 1
                        $ TemplustX += 2 if GirlA.action_counter["handjob"] > 2 else 0
                        $ GirlA.Addict -= 1
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
                elif Action == "dildo_anal":
                        $ line = line + renpy.random.choice(["She moves the dildo in circles across her ass, firmly rubbing into it",
                                "She hungrily slams the dildo into her tight hole, and pistons it in and out",
                                "She shoves the dildo firmly in and out of her grasping asshole",
                                "She quickly slides the phallus up and down the crease of her ass"])
                elif Action == "vibrator pussy":
                        $ line = line + renpy.random.choice(["She traces the buzzing ball slowly down her body, barely grazing her mound",
                                "Her vibrator slides lightly across her pubic region, subtly avoiding her lips",
                                "She slides the buzzing egg into her dripping pussy and tugs it in and out",
                                "She presses the vibrator firmly against her clit and a shiver runs through her",
                                "Her whirring toy is dragged up and down her inner thighs, slowly building towards their center",
                                "She  spreads her lower lips and runs the device along the inner lining",
                                "She presses the toy deep into her and the vibrations send a shock through her body"])
                else: # Action == "fondle_breasts"
                        $ line = line + renpy.random.choice(["She passionately rubs her breasts, desperately tugging at her nipples",
                                "Her hands squeeze at her breasts, massaging them firmly with both hands",
                                "She hungrily cups her breasts and moves them in rapid circles",
                                "Her hands move constantly across her chest, alternately pulling at her nipples or just grazing her skin",
                                "She firmly pinches her nipples and gives them steady tugs",
                                "She passionately rubs her breasts, desperately tugging at her nipples"])
        #End GirlA.lust >= 80
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
                elif Action == "dildo_anal":
                        $ line = line + renpy.random.choice(["She traces the rubber phallus slowly down her body, barely grazing her ass",
                                "Her dildo slides lightly across her crack, subtly avoiding the hole",
                                "Her dildo is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her cheeks and caresses the rim beneath",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "vibrator pussy":
                        $ line = line + renpy.random.choice(["She traces the buzzing ball slowly down her body, barely grazing her mound",
                                "Her vibrator slides lightly across her pubic region, subtly avoiding her lips",
                                "Her whirring toy is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She drags the vibrator slowly along her sides, carefully caressing them"])
                else: # Action == "fondle_breasts"
                        $ line = line + renpy.random.choice(["She gently rubs her breasts, dragging a finger across her nipple",
                                "She gently cups her breasts and moves them in slow circles",
                                "She moves her hands from her breasts to rub her neck",
                                "She lightly pinches one of her nipples",
                                "Her hands firmly caress her breasts, massaging them in circular motions",
                                "Her hands move along her breasts, carefully caressing them",
                                "She gasps as her finger brushes against an erect nipple"])
        #End GirlA.lust >= 50
        else: #if GirlA.lust < 50:
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
                elif Action == "dildo_anal":
                        $ line = line + renpy.random.choice(["She traces the rubber phallus slowly down her body, barely grazing her ass",
                                "Her dildo slides lightly across her crack, subtly avoiding the hole",
                                "Her dildo is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her cheeks and caresses the rim beneath",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "vibrator pussy":
                        $ line = line + renpy.random.choice(["She traces the buzzing ball slowly down her body, barely grazing her mound",
                                "Her vibrator slides lightly across her pubic region, subtly avoiding her lips",
                                "Her whirring toy is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She drags the vibrator slowly along her sides, carefully caressing them"])
                else: # Action == "fondle_breasts"
                        $ line = line + renpy.random.choice(["She gently rubs her breasts, dragging a finger across her nipple",
                                "She gently cups her breasts and moves them in slow circles",
                                "She moves her hands from her breasts to rub her neck",
                                "She lightly pinches one of her nipples",
                                "She gasps as her finger brushes against an erect nipple"])
                #End GirlA.lust 0-60
        #End Girl's Action masturbation dialog


        # Girl's Self-stat boosts
        $ TemplustX += 4 if GirlA.lust > 80 else 0
        $ TemplustX += 5 if GirlA.lust < 40 else 3                      #Bonus if she is relatively low lust
        $ TemplustX += 5 if primary_action == "masturbation" and GirlA != Partner else 0            #Bonus if masturbation is her primary action

        if primary_action == "massage":
                $ TempFocusX += 4 if Player.Focus < 50 else 3
                $ Player.change_stat("Focus", 200, TempFocusX)
                $ GirlA.change_stat("lust", 200, TemplustX)
                return
        else:
                if "TempFocus" not in locals().keys():
                        "Tell Oni the error was \"[primary_action]\"."
                $ TempFocus += 4 if Player.Focus < 50 else 3

        if Partner != GirlA:
                #If this is a primary, girl_offhand_action action
                $ Templust = TemplustX
        else:
                #If this is a Secondary, second_girl_offhand_action action
                $ Templust2 = TemplustX


    #End Action all dialog

    return

label Girl_Self_Set(GirlA=Primary, Mode = "T3", Action = girl_offhand_action, Length=0, between_event_count=0, Options =[]):
    #nee Rog*ue_Self_Set(Mode = "T3", Action = girl_offhand_action, Length=0, between_event_count=0, Options =[]):
    #If T3/girl_offhand_action is sent, this is for Primary role, offhand behavior
    #If T5/second_girl_offhand_action is sent, this is for Secondary role, threesome masturbation behavior
    if Mode == "T3" and primary_action != "masturbation":
                # This cuts it out if she's submissive or not horny enough to get busy
                if "sub" in GirlA.Traits:
                        return

                #if she's inexperienced or shy, skip this
                if GirlA.SEXP >= 50 or Approvalcheck(GirlA, 500, "I"):
                    if GirlA.lust <= 30:
                        return
                elif GirlA.SEXP >= 25 or Approvalcheck(GirlA, 300, "I"):
                    if GirlA.lust <= 50:
                        return
                else:
                        return

    if Mode == "T3" and primary_action == "masturbation":
                #sets base options as masturbatory
                $ Options = ["fondle_pussy", "fondle_breasts", "fondle_ass"]
                if "dildo" in GirlA.Inventory:
                        $ Options.append("dildo_pussy")
                        if GirlA.Loose:
                            $ Options.append("dildo_anal")
                if "vibrator" in GirlA.Inventory:
                        $ Options.append("vibrator pussy")

    else:
                if GirlA.action_counter["handjob"] >= 5 and Mode != "T5" and primary_action in ("fondle_pussy", "fondle_breasts", "fondle_thighs", "kiss", "fondle_ass", "suck_breasts"):
                        #if this is about the primary girl, and she's done handys, and you're feeling her up, she might feel you up
                        $ Options.append("handjob")

                if primary_action not in ("sex", "fondle_pussy", "eat_pussy", "dildo_pussy"):
                        #if you aren't touching her pussy, she might
                        if "dildo" in GirlA.Inventory:
                                $ Options.append("dildo_pussy")
                        $ Options.append("fondle_pussy")

                if primary_action not in ("anal", "fondle_ass", "finger_ass", "eat_ass", "dildo_anal") and GirlA.Loose:
                        #if you aren't messing with her ass, she might
                        if "dildo" in GirlA.Inventory:
                                $ Options.append("dildo_anal")
                        $ Options.append("fondle_ass")

                if "vibrator" in GirlA.Inventory:
                        $ Options.append("vibrator pussy")

                if primary_action not in ("fondle_breasts", "suck_breasts"):
                        #if you aren't dealing with her breasts. . .
                        $ Options.append("fondle_breasts")

                if GirlA.obedience < GirlA.inhibition:
                        #adds more options if she is not submissive
                        if "fondle_pussy" not in Options:
                                $ Options.append("fondle_pussy")
                        if "fondle_ass" not in Options:
                                $ Options.append("fondle_ass")
                        if "fondle_breasts" not in Options:
                                $ Options.append("fondle_breasts")
    # End filling options

    $ Length = len(Options)-1
    $ D20 = renpy.random.randint(1, 20)
    if D20 >=18:
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
            #If the action has changed, play change dialog
            $ Action = Options[between_event_count] #Sets Action to the selected Option
            if Action == "handjob":
                    $ line = GirlA.name + " slides her hand down and firmly grabs your dick. "
                    $ Approval = 3
            elif Action == "fondle_pussy":
                    $ line = GirlA.name + "'s hand slides down and begins to stroke her pussy. "
            elif Action == "dildo_pussy":
                    $ line = GirlA.name + " pulls out her dildo and draws it toward her pussy. "
            elif Action == "fondle_ass":
                    $ line = GirlA.name + "'s hand slides behind her body, reaching toward her ass. "
            elif Action == "dildo_anal":
                    $ line = GirlA.name + " pulls out her dildo and reaches it behind her. "
            elif Action == "vibrator pussy":
                    $ line = GirlA.name + " pulls out her vibrator and strokes it across her body. "
            else: # Action == "fondle_breasts"
                    $ line = GirlA.name + "'s hands slide up her body and begin to kneed her breasts. "
    elif Action == "handjob":
            $ line = "Also, " + GirlA.name + " continues stroke your cock. "
    else:
            $ line = "Also, " + GirlA.name + " continues to masturbate. "

    if Mode == "T3": #Sets Action based on the result
        $ girl_offhand_action = Action
    else:
        $ second_girl_offhand_action = Action

    return

label SexDialog_Threeway(GirlA = Secondary, Mode = 0, Action = 0, GirlB = Primary, phrase = 0, Templust = 0, Templust2 = 0, TempFocus = 0):
    #nee Rog*ue_SexDialog_Threeway(Mode = 0, Action = 0,
    # This is the dialog checked for primary_action 4, activated when GirlA is the second girl in a scene, or for Lesbian activities.
    # if Mode is "lesbian" then it means she's doing a girl/girl sequence, and activating secondary dialogs.
    # By default, GirlB will be the primary and this sequence will build text for what the secondary girl does.
    # In "lesbian" mode, GirlB will be the secondary girl, and this sequence will build text for what the primary will do to her.
    # Lesbian primary_action1 dialog calls "call SexDialog_Threeway(RogueX,"lesbian")" #nee "call Rog*ue_SexDialog_Threeway("lesbian")"

    call Threeway_Set(GirlA,Mode=Mode,GirlB=GirlB) #nee Rog*ue_Threeway_Set(Mode=Mode)   #Picks a new activty on a 7-9 roll or when not set, otherwise returns

    if Mode == "lesbian":
            $ Action = girl_offhand_action
            $ GirlB = Secondary
    else:
            $ Action = second_girl_primary_action

    if line:
            #if it picked something, it should have set a line and returned
            return
    elif not Action:
            $ Action = "watch"

    if Action == "handjob":
                    if D20S <= 8 and (primary_action == "blowjob" or primary_action == "handjob"): #This is a random bonus dialog
                        if primary_action == "blowjob": #If Kitty is blowing you
                            $ line = renpy.random.choice([GirlA.name + "'s fingers brush against " + GirlB.name + "'s lips as they work",
                                    GirlA.name + " and " + GirlB.name + " pause for a second to briefly kiss",
                                    GirlA.name + " takes a turn to suck on the head before passing it back",
                                    GirlA.name + " and " + GirlB.name + " get into an alternating rhythm"])
                        elif primary_action == "handjob":  #If Kitty is handying you
                            $ line = renpy.random.choice([GirlA.name + "'s fingers brush against " + GirlB.name + "'s as they work",
                                    GirlA.name + " strokes " + GirlB.name + "'s palm as she works",
                                    GirlA.name + " takes a turn to stroke a few times before passing it back",
                                    GirlA.name + " and " + GirlB.name + " get into an alternating rhythm"])
                    else:
                        if primary_action == "handjob": #if another girl is also handy
                                $ line = GirlA.name + " also continues to stroke your cock"
                        else: #if the other girl is doing something else
                                $ line = GirlA.name + " continues stroke your cock"

                        $ line = line + renpy.random.choice([", lightly stroking the shaft, fingers sliding along the vein",
                                ", grasping the shaft firmly, and slowly sliding along its length",
                                ", making up for years of lost time",
                                ", her expert strokes will have you boiling over in seconds",
                                ", stroking the shaft vigorously, lightly touching the tip",
                                ", moving very smoothly, stroking casually",
                                ", hand sliding slowly down your shaft"])
                    $ TempFocus += 3 if Player.Focus > 70 else 2

                    $ Templust += 2 if GirlA.lust < 60 else 0
                    $ Templust += 2 if GirlA.action_counter["handjob"] > 2 else 0
                    $ GirlA.Addict -= 1 if D20S > 10 else 2

    # end GirlA.action_counter["handjob"] Threeway                                //////////////////////////////////////////////////////////////////////////////

    elif Action == "blowjob":
                    if action_speed > 2 and primary_action == "blowjob":
                        $ line = "Since " + GirlB.name + " is working so hard, " + GirlA.name + " settles for the occasional nibble or lick."
                        $ TempFocus += 5 if Player.Focus > 60 else 3
                        $ Templust += 2 if GirlA.lust > 80 else 1
                    else:
                        if D20S <= 8 and (primary_action == "blowjob" or primary_action == "handjob"): #This is a random bonus dialog
                            if primary_action == "blowjob": #If Kitty is blowing you
                                $ line = renpy.random.choice([GirlA.name + "'s tongue brushes against " + GirlB.name + "'s as they work",
                                        GirlA.name + " and " + GirlB.name + " pause for a second to briefly kiss",
                                        GirlA.name + " takes a turn to suck on the head before passing it back",
                                        GirlA.name + " and " + GirlB.name + " get into an alternating rhythm"])
                            elif primary_action == "handjob": #If Kitty is handying you
                                $ line = renpy.random.choice([GirlA.name + "'s tongue brushes against " + GirlB.name + "'s hand as they work",
                                        GirlA.name + " licks " + GirlB.name + "'s palm as she works",
                                        GirlA.name + " takes a turn to stroke a few times before passing it back",
                                        GirlA.name + " and " + GirlB.name + " get into an alternating rhythm"])
                            $ Templust2 += 1 if GirlB.GirlLikecheck(GirlA) >= 800 else 0
                        else:
                            if primary_action == "blowjob": #if another girl is also blowing
                                    $ line = GirlA.name + " also continues to lick your cock"
                            else: #if the other girl is doing something else
                                    $ line = "Also, " + GirlA.name + " continues lick your cock"

                            $ line = line + renpy.random.choice([", settling into a gentle licking pace along the base",
                                    ", licking gently up and down the shaft",
                                    ", her tongue moves carefully along the shaft",
                                    ", really starting to learn some clever tricks to making you feel good",
                                    ", licking her way down the shaft, and gently teasing the balls"])

                        $ TempFocus += 20 if Player.Focus > 60 else 10
                        $ Templust += 2 if GirlA.lust > 80 else 1

                        $ GirlA.Addict -= 2
    # end GirlA.action_counter["blowjob"]job Threeway                                //////////////////////////////////////////////////////////////////////////////

    elif Action == "fondle_breasts":
                        if offhand_action == "fondle_breasts" and primary_action != "lesbian": #if you're also fondling them,
                            $ line = GirlA.name + " also continues to fondle " + GirlB.name + "'s breasts"
                        else:
                            $ line = GirlA.name + " continues to fondle " + GirlB.name + "'s breasts"

                        $ line = line + renpy.random.choice([", giving little tugs to her nipples",
                                        ", cupping them firmly with both hands",
                                        ", gently moving them in slowly increasing circles",
                                        ", then moves her hands from her breasts to rub her neck",
                                        ", firmly pinching her nipples and giving them a tug",
                                        ", passing repeatedly against her rigid nipples"])
                        $ Templust += 2 if Approvalcheck(GirlA, 500, "I") else 1  # GirlA's lust
                        $ Templust2 += 5 if GirlB.GirlLikecheck(GirlA) >= 800 else 2
                        $ TempFocus += 1
    # end Fondle breasts Threeway                                //////////////////////////////////////////////////////////////////////////////


    elif Action == "suck_breasts":
                        if offhand_action == "fondle_breasts" and primary_action != "lesbian": #if you're also fondling them,
                                $ line = GirlA.name + " also continues to suck " + GirlB.name + "'s breasts"
                        else:
                                $ line = GirlA.name + " continues to suck " + GirlB.name + "'s breasts"

                        $ line = line + renpy.random.choice([", giving little tugs to her nipple",
                                        ", cupping them firmly with both hands",
                                        ", then moves her hands down along her side",
                                        ", licking slowly up her chest",
                                        ", firmly nibbling her nipples and giving them a tug",
                                        ", nibbling repeatedly at her rigid nipples"])
                        $ Templust += 2 if Approvalcheck(GirlA, 500, "I") else 1  # GirlA's lust
                        $ Templust2 += 4 if GirlB.GirlLikecheck(GirlA) >= 800 else 2
                        $ TempFocus += 1
    # end Suck breasts Threeway                                //////////////////////////////////////////////////////////////////////////////


    elif Action == "fondle_pussy":
                        if (primary_action == "fondle_pussy" or offhand_action == "fondle_pussy") and primary_action != "lesbian": #if you're also fondling them,
                                $ line = GirlA.name + " also continues to fondle " + GirlB.name + "'s pussy"
                                $ phrase = renpy.random.choice([", stroking across her clit",
                                        ", the two of you taking turns in your motions",
                                        ", her fingers brushing against yours as you work",
                                        ", rubbing against it vigorously",
                                        ", stroking into it vigorously",
                                        ", pressing firmly into it",
                                        ", sliding firmly into it",
                                        ", moving inside it with slow undulating motions",
                                        ", moving with slow undulating motions"])
                        else:
                                $ line = GirlA.name + " continues to fondle " + GirlB.name + "'s pussy"
                                $ phrase = renpy.random.choice([", running fingers gently up her cleft",
                                        ", stroking across her clit",
                                        ", taking a little taste of the warm juices on her finger",
                                        ", rubbing against it vigorously",
                                        "a",
                                        "b",
                                        "c",
                                        ", moving with slow undulating motions"])

                                #a, b, and c can change depending on other circumstances at the time.
                                if phrase == "a":
                                    if primary_action == "sex" or primary_action == "anal":
                                            $ phrase = ", her fingers brush against your cock as it goes in"
                                    elif primary_action == "eat_pussy":
                                            $ phrase = ", your tongue slides past her fingers"
                                    elif primary_action == "dildo_pussy" or offhand_action == "dildo_pussy":
                                            $ phrase = ", her fingers brush against the dildo as it goes in"
                                    else:
                                            $ phrase = ", stroking into it vigorously"
                                elif phrase == "b":
                                    if primary_action == "sex" or primary_action == "anal":
                                            $ phrase = ", her fingers brushing up against your balls as you sink in"
                                    elif primary_action == "eat_pussy":
                                            $ phrase = ", you briefly suck on one of her fingers"
                                    elif primary_action == "dildo_pussy" or offhand_action == "dildo_pussy":
                                            $ phrase = ", her fingers brushing up against the dildo as it slides by"
                                    else:
                                            $ phrase = ", sliding firmly into it"
                                elif phrase == "c":
                                    if primary_action == "sex" or primary_action == "anal":
                                            $ phrase = ", her fingers brush against your cock as it goes in"
                                    elif primary_action == "eat_pussy":
                                            $ phrase = ", your tongue slides along her fingers"
                                    elif primary_action == "dildo_pussy" or offhand_action == "dildo_pussy":
                                            $ phrase = ", her fingers brushing up against the dildo as it slides by"
                                    else:
                                            $ phrase = ", moving inside it with slow undulating motions"
                                #End if the other girl is not fondling
                        $ line = line + phrase

                        $ Templust += 2 if Approvalcheck(GirlA, 500, "I") else 1  # GirlA's lust
                        $ Templust2 += 5 if GirlB.GirlLikecheck(GirlA) >= 800 else 3
                        $ TempFocus += 1

    # end fondle pussy Threeway                              /////////////////////////////////////////////////////////////////////////////


    elif Action == "eat_pussy":
                        if (primary_action == "eat_pussy" or offhand_action == "eat_ pussy") and primary_action != "lesbian": #if you're also fondling them,
                            $ line = GirlA.name + " also continues to lick " + GirlB.name + "'s pussy"
                        else:
                            $ line = GirlA.name + " continues to lick " + GirlB.name + "'s pussy"

                        $ phrase = renpy.random.choice([", running her tongue gently up her cleft",
                                    ", stroking across her clit",
                                    ", taking a little taste of the warm juices flowing out",
                                    ", lapping against it vigorously",
                                    "a",
                                    "b",
                                    "c",
                                    ", moving with slow undulating motions"])

                        #a, b, and c can change depending on other circumstances at the time.
                        if phrase == "a":
                                if primary_action == "sex" or primary_action == "anal":
                                        $ phrase = ", her tongue brushes against your cock as it goes in"
                                elif primary_action == "eat_pussy":
                                        $ phrase = ", her tongue brushing against yours as you work"
                                elif primary_action == "fondle_pussy" or offhand_action == "fondle_pussy":
                                        $ phrase = ", her tongue slides along your fingers"
                                elif primary_action == "dildo_pussy" or offhand_action == "dildo_pussy":
                                        $ phrase = ", her tongue brushes along the dildo as it goes in"
                                else:
                                        $ phrase = ", lapping into it vigorously"
                        elif phrase == "b":
                                if primary_action == "sex" or primary_action == "anal":
                                        $ phrase = ", her longue lapping against your balls as you sink in"
                                elif primary_action == "eat_pussy":
                                        $ phrase = ", you briefly kiss as you take turns"
                                elif primary_action == "fondle_pussy" or offhand_action == "fondle_pussy":
                                        $ phrase = ", her tongue slides past your fingers"
                                elif primary_action == "dildo_pussy" or offhand_action == "dildo_pussy":
                                        $ phrase = ", her tongue runs up against the dildo as it slides by"
                                else:
                                        $ phrase = ", sliding firmly into it"
                        elif phrase == "c":
                                if primary_action == "sex" or primary_action == "anal":
                                        $ phrase = ", her tongue brushes against your cock as it goes in"
                                elif primary_action == "eat_pussy":
                                        $ phrase = ", the two of you taking turns in your motions"
                                elif primary_action == "fondle_pussy" or offhand_action == "fondle_pussy":
                                        $ phrase = ", her tongue slides past your fingers"
                                elif primary_action == "dildo_pussy" or offhand_action == "dildo_pussy":
                                        $ phrase = ", her tongue runs up against the dildo as it slides by"
                                else:
                                        $ phrase = ", moving inside it with slow undulating motions"

                        $ line = line + phrase

                        $ Templust += 3 if Approvalcheck(GirlA, 600, "I") else 1  # GirlA's lust
                        $ Templust2 += 7 if GirlB.GirlLikecheck(GirlA) >= 800 else 4
                        $ TempFocus += 3

    # end lick pussy Threeway                              /////////////////////////////////////////////////////////////////////////////

    elif Action == "fondle_ass":
                        if offhand_action == "fondle_ass" and primary_action != "lesbian": #if you're also fondling them,
                                $ line = GirlA.name + " also continues to fondle " + GirlB.name + "'s ass"
                                $ line = line + renpy.random.choice([", stroking across her rear",
                                        ", the two of you taking turns in your motions",
                                        ", her fingers brushing against yours as you work",
                                        ", rubbing it vigorously",
                                        ", squeezing it vigorously",
                                        ", pressing firmly into it",
                                        ", kneeding it with slow undulating motions",
                                        ", moving with slow undulating motions"])
                        else:
                                $ line = GirlA.name + " continues to fondle " + GirlB.name + "'s ass"
                                $ line = line + renpy.random.choice([", running fingers gently up her cleft",
                                        ", stroking across her rear",
                                        ", rubbing it vigorously",
                                        ", squeezing it vigorously",
                                        ", pressing firmly into it",
                                        ", kneeding it with slow undulating motions",
                                        ", moving with slow undulating motions"])

                        $ Templust += 1 if Approvalcheck(GirlA, 500, "I") else 0  # GirlA's lust
                        $ Templust2 += 3 if GirlB.GirlLikecheck(GirlA) >= 800 else 1
                        $ TempFocus += 1
    # end fondle ass Threeway                              /////////////////////////////////////////////////////////////////////////////


    elif Action == "finger_ass":
                        if (primary_action == "finger_ass" or offhand_action == "finger_ass") and primary_action != "lesbian": #if you're also fondling them,
                                $ line = GirlA.name + " also continues to stroke " + GirlB.name + "'s ass"
                        else:
                                $ line = GirlA.name + " continues to stroke " + GirlB.name + "'s ass"

                        $ phrase = renpy.random.choice([", stroking across her rim",
                                    ", stroking across her hole",
                                    ", circling it vigorously",
                                    "a",
                                    "b",
                                    "c",
                                    ", moving with slow undulating motions"])

                        #a, b, and c can change depending on other circumstances at the time.
                        if phrase == "a":
                                if primary_action == "sex" or primary_action == "anal":
                                        $ phrase = ", her fingers brush against your cock as it goes in"
                                elif primary_action == "finger_ass" or offhand_action == "finger_ass":
                                        $ phrase = ", her fingers circling yours"
                                elif primary_action == "dildo_anal" or offhand_action == "dildo_anal":
                                        $ phrase = ", her fingers brush against the dildo as it goes in"
                                else:
                                        $ phrase = ", running fingers gently up her cleft"
                        elif phrase == "b":
                                if primary_action == "sex" or primary_action == "anal":
                                        $ phrase = ", her fingers brushing up against your balls as you sink in"
                                elif primary_action == "finger_ass" or offhand_action == "finger_ass":
                                        $ phrase = ", the two of you taking turns in your motions"
                                elif primary_action == "dildo_anal" or offhand_action == "dildo_anal":
                                        $ phrase = ", her fingers run along the dildo as it slides by"
                                else:
                                        $ phrase = ", sliding firmly into it"
                        elif phrase == "c":
                                if primary_action == "sex" or primary_action == "anal":
                                        $ phrase = ", her fingers brush against your cock as it goes in"
                                elif primary_action == "finger_ass" or offhand_action == "finger_ass":
                                        $ phrase = ", her fingers intertwine yours"
                                elif primary_action == "dildo_anal" or offhand_action == "dildo_anal":
                                        $ phrase = ", her fingers brush against the dildo as it goes in"
                                else:
                                        $ phrase = ", moving inside it with slow undulating motions"

                        $ line = line + phrase

                        if not GirlB.Loose:
                                        $ Templust2 -= 3
                        $ Templust += 2 if Approvalcheck(GirlA, 700, "I") else 1  # GirlA's lust
                        $ Templust2 += 5 if GirlB.GirlLikecheck(GirlA) >= 800 else 3
                        $ TempFocus += 1

    # end insert ass Threeway                             /////////////////////////////////////////////////////////////////////////////

    elif Action == "eat_ass":
                        if (primary_action == "eat_ass" or offhand_action == "eat_ass") and primary_action != "lesbian": #if you're also fondling them,
                                $ line = GirlA.name + " also continues to lick " + GirlB.name + "'s ass"
                        else:
                                $ line = GirlA.name + " continues to lick " + GirlB.name + "'s ass"

                        $ phrase = renpy.random.choice([", tonguing across her rim",
                                    ", stroking across her hole",
                                    ", circling it vigorously",
                                    "a",
                                    "b",
                                    "c",
                                    ", moving with slow undulating motions"])

                        #a, b, and c can change depending on other circumstances at the time.
                        if phrase == "a":
                                if primary_action == "sex" or primary_action == "anal":
                                        $ phrase = ", her tongue brushes against your cock as it goes in"
                                elif primary_action == "eat_ass":
                                        $ phrase = ", her tongue brushing against yours as you work"
                                elif primary_action == "finger_ass" or offhand_action == "finger_ass":
                                        $ phrase = ", her tongue slides along your fingers"
                                elif primary_action == "dildo_anal" or offhand_action == "dildo_anal":
                                        $ phrase = ", her tongue brushes along the dildo as it goes in"
                                else:
                                        $ phrase = ", lapping into it vigorously"
                        elif phrase == "b":
                                if primary_action == "sex" or primary_action == "anal":
                                        $ phrase = ", her longue lapping against your balls as you sink in"
                                elif primary_action == "eat_ass":
                                        $ phrase = ", you briefly kiss as you take turns"
                                elif primary_action == "finger_ass" or offhand_action == "finger_ass":
                                        $ phrase = ", her tongue slides past your fingers"
                                elif primary_action == "dildo_anal" or offhand_action == "dildo_anal":
                                        $ phrase = ", her tongue runs up against the dildo as it slides by"
                                else:
                                        $ phrase = ", sliding firmly into it"
                        elif phrase == "c":
                                if primary_action == "sex" or primary_action == "anal":
                                        $ phrase = ", her tongue brushes against your cock as it goes in"
                                elif primary_action == "eat_ass":
                                        $ phrase = ", the two of you taking turns in your motions"
                                elif primary_action == "finger_ass" or offhand_action == "finger_ass":
                                        $ phrase = ", her tongue slides past your fingers"
                                elif primary_action == "dildo_anal" or offhand_action == "dildo_anal":
                                        $ phrase = ", her tongue runs up against the dildo as it slides by"
                                else:
                                        $ phrase = ", moving inside it with slow undulating motions"

                        $ line = line + phrase

                        $ Templust += 3 if Approvalcheck(GirlA, 800, "I") else 1  # GirlA's lust
                        $ Templust2 += 4 if GirlB.GirlLikecheck(GirlA) >= 800 else 2
                        $ TempFocus += 3

    # end lick ass Threeway                              /////////////////////////////////////////////////////////////////////////////

    elif Action == "masturbation":
                        call Girl_Self_lines(GirlA,"T5",second_girl_offhand_action)  #nee Rog*ue_Self_lines
                        $ Templust = 0

    # end Masturbation Threeway                              /////////////////////////////////////////////////////////////////////////////

    elif Action in ("kiss", "kiss girl", "kiss both"):
                        if primary_action == "blowjob" and GirlA.action_counter["blowjob"] > 5 and second_girl_primary_action == "kiss girl":
                                    $ line = GirlA.name + " also continues to kiss " + GirlB.name
                                    $ line = line + renpy.random.choice([", occasionally taking a lick of your cock as well",
                                            ", licking along her cheek",
                                            ", nudging you out of her mouth to get a deep kiss in",
                                            ", taking the occasional lick down your shaft",
                                            ", nudging her aside to kiss the head of your cock"])
                        elif primary_action == "blowjob" and second_girl_primary_action == "kiss girl":
                                    $ line = GirlA.name + " also continues to kiss " + GirlB.name
                                    $ line = line + renpy.random.choice([", occasionally bumping into your cock as well",
                                            ", licking along her cheek",
                                            ", nudging you out of her mouth to get a deep kiss in",
                                            ", trailing kisses down her neck"])
                        else: #they're just kissing
                                    if Action == "kiss girl" or Mode == "lesbian":
                                        if primary_action == "lesbian" and Partner != GirlA:
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
                                    else: #Action == "kiss both":
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
                        $ Templust += 1 if Approvalcheck(GirlA, 500, "I") else 0  # GirlA's lust
                        $ Templust += 1 if GirlA.GirlLikecheck(GirlB) >= 800 else 0
                        $ Templust2 += 2 if GirlB.GirlLikecheck(GirlA) >= 800 else 1
                        $ TempFocus += 1
    # end Kissing Threeway                              /////////////////////////////////////////////////////////////////////////////

    elif Action == "watch":
                        $ line = GirlA.name + " continues to watch the two of you"
                        $ line = line + renpy.random.choice([", shifting uncomfortably",
                                        ", readjusting her clothes",
                                        ", glancing at the door",
                                        ", taking in " + GirlB.name + "'s body",
                                        ", transfixed by the action"])
                        $ Templust += 1 if GirlA.GirlLikecheck(GirlB) >= 600 else 0  # GirlA's lust
                        $ Templust += 2 if GirlA.GirlLikecheck(GirlB) >= 800 else 1  # GirlA's lust
                        $ Templust2 += 1 if Approvalcheck(GirlB, 500, "I") else 0
                        $ Templust2 += 1 if Approvalcheck(GirlB, 700, "I") else 0
                        $ TempFocus += 1
    # end watching Threeway                              /////////////////////////////////////////////////////////////////////////////

    else:
        "Nothing triggered. 1:[primary_action], 2:[offhand_action], 3:[girl_offhand_action], 4:[second_girl_primary_action], 5:[second_girl_offhand_action]" #diagnostic

    # Wrap-up
    $ Templust2 += 2
    if Mode == "lesbian":
            $ Primarylust += (Templust * 3)
            $ Secondarylust += (Templust2 * 3)
    else:
            $ Secondarylust += Templust
            $ Primarylust += Templust2

    $ Player.Focus += TempFocus
    return

label Three_Change(LeadGirl = Primary, SecondGirl = Partner, D20S=0, Primarylust=0, Secondarylust=0):
        #this is called when the player wants to change over a threeway behavior, and revolves around the partner girl
        # if changes what the Partner does to the lead girl
        # for Threeway secondary activity: #nee Rogue_Threeway_Set("preset", 0, second_girl_primary_action, "ActiveGirl")
        # call Three_Change(Primary,Partner)
        # call Threeway_Set(KittyX,"preset",0,second_girl_primary_action,RogueX)
        if LeadGirl not in all_Girls:
                return
        if Partner == LeadGirl:
                "Let Oni know that both roles are set to [Girl.name]."
                return
        menu Three_Change_Menu:
            ch_p "Hey [Partner.name]. . ."
            "about [LeadGirl.name]. . .": #about the primary girl. . .
                menu:
                    ch_p "about [LeadGirl.name]. . ."
                    "why don't you kiss her?" if second_girl_offhand_action != "kiss girl" and second_girl_offhand_action != "kiss both":
                                    call Threeway_Set(SecondGirl,"kiss girl", 0, second_girl_primary_action, LeadGirl)
                    "why don't you grab her tits?" if second_girl_primary_action != "fondle_breasts":
                                    call Threeway_Set(SecondGirl,"fondle_breasts",0, second_girl_primary_action, LeadGirl)
                    "why don't you suck her breasts?" if second_girl_primary_action != "suck_breasts":
                                    call Threeway_Set(SecondGirl,"suck_breasts",0, second_girl_primary_action, LeadGirl)
                    "why don't you finger her?" if second_girl_primary_action != "fondle_pussy":
                                    call Threeway_Set(SecondGirl,"fondle_pussy",0, second_girl_primary_action, LeadGirl)
                    "why don't you go down on her?" if second_girl_primary_action != "eat_pussy":
                                    call Threeway_Set(SecondGirl,"eat_pussy", 0, second_girl_primary_action, LeadGirl)
                    "why don't you grab her ass?" if second_girl_primary_action != "fondle_ass":
                                    call Threeway_Set(SecondGirl,"fondle_ass", 0, second_girl_primary_action, LeadGirl)
                    "why don't you lick her ass?" if second_girl_primary_action != "eat_ass":
                                    call Threeway_Set(SecondGirl,"eat_ass", 0, second_girl_primary_action, LeadGirl)
                    "wait, I meant. . .":
                                    jump Three_Change_Menu

            "about me. . .":
                menu:
                    ch_p "about me. . ."
                    "why don't you kiss me?" if second_girl_offhand_action != "kiss" and second_girl_offhand_action != "kiss both":
                                    call Threeway_Set(SecondGirl,"kiss", 0, second_girl_primary_action, LeadGirl)
                    "maybe take me in hand?" if second_girl_primary_action != "handjob":
                                    call Threeway_Set(SecondGirl,"handjob", 0, second_girl_primary_action, LeadGirl)
                    "maybe give me a lick?" if second_girl_primary_action != "blowjob":
                                    call Threeway_Set(SecondGirl,"blowjob", 0, second_girl_primary_action, LeadGirl)
                    "why don't you give me a show?" if second_girl_primary_action != "masturbation":
                                    call Threeway_Set(SecondGirl,"masturbation", 0, second_girl_primary_action, LeadGirl)
                    "wait, I meant. . .":
                                    jump Three_Change_Menu
            "never mind.":
                pass
        return

label Threeway_Set(GirlA=Secondary,Preset = 0, Mode = 0, Action = second_girl_primary_action, GirlB = Primary, State = "watcher", Templust = 0, Templust2 = 0, TempFocus = 0): #rkeljsv
            #nee Rog*ue_Threeway_Set(Preset = 0, Mode = 0,
            # Action defaults to second_girl_primary_action, the action of the seondary girl and GirlB to the lead girl in the scene
            # In lesbian mode, Action becomes girl_offhand_action, the secondary action of the primary girl, and GirlB is the secondary girl
            # If Set gets passed a preset, it chooses that preset, otherwise it chooses one randomly
            # for Lesbian: call Threeway_Set(Primary,"suck_breasts", "lesbian", girl_offhand_action,Secondary)
            # for Threeway: call Threeway_Set(SecondGirl,"fondle_breasts",0, second_girl_primary_action, LeadGirl)
            # position_change_timer is a value that gets set to a few digits lower then the current Round
            # The girl will not arbitrarily change motions until after this value has been passed.

            $ D20 = renpy.random.randint(1, 20)
            if not Preset:
                    #if no preset is offered
                    if Mode == "lesbian": #called from Les_Change()
                            #If it's in lesbian mode, there is already a trigger set, and the roll is good, continue
                            if girl_offhand_action == "kiss girl" and GirlA.lust <= 20 and GirlA.event_counter["orgasm"] < 1:
                                    # If kissing at low lust, keep doing it
                                    return
                            elif girl_offhand_action and position_change_timer <= Round:
                                    # If a girl_offhand_action is already set and it's under the count, return
                                    return
                    elif second_girl_primary_action and D20 < 15 and second_girl_primary_action != "watch":
                                    #If there is a trigger, it's not set to "watch," and the roll is good, continue
                                    return
                    elif second_girl_primary_action and position_change_timer <= Round:
                                    # if there's not a Preset, and it's only been X turns since the last change, return.
                                    return
            $ Options = ["watch", "masturbation", "masturbation", "masturbation"]

            if GirlA == GirlB and GirlA != Partner:
                    $ GirlB = Partner
            elif GirlA == GirlB and GirlA != Primary:
                    $ GirlB = Primary
            if GirlA == GirlB:
                    "Tell Oni that in Threeway_Set, A:[GirlA.Tag] and B:[GirlB.Tag]"
                    "[Girl.Gibberish]"

            if primary_action == "lesbian":
                    # if this was sent from a Lesbian action. . .
                    $ State = "lesbian"
                    $ Options = ["kiss girl","kiss girl"]
                    if Preset in ("handjob","blowjob","kiss","kiss both"):
                            #if you send it presets that you want the other girl to touch you. . .
                            $ State = "threeway"
                    elif Preset:
                            pass
                    elif GirlA.GirlLikecheck(GirlB) >= 600 and Approvalcheck(GirlA, 500, "I"):
                            #if she likes the other girl, and is unihibited. . .
                            pass
                    else:
                            #this returns if she doesn't like the other girl enough to do anything more.
                            if Action != "kiss girl":
                                    $ line = GirlA.name + " gives " + GirlB.name + " a passionate kiss"
                                    $ Action = "kiss girl"
                                    $ girl_offhand_action = "kiss girl"
                                    if "lesbian" not in GirlA.recent_history:
                                            $ GirlA.Les += 1
                                            $ GirlA.recent_history.append("lesbian")
                            return
            elif not Approvalcheck(GirlA, 500, "I"):
                    # If GirlA is too timid to do anything, stick to neutral options
                    pass
            elif GirlA.GirlLikecheck(GirlB) >= 600 and Approvalcheck(GirlA, (1500-(10*GirlA.Les)-(10*(GirlA.GirlLikecheck(GirlB)-60)))):
                    #If she likes both of you a lot, threeway
                    $ State = "threeway"
            elif Approvalcheck(GirlA, 1000):
                    #If she likes you well enough, Hetero
                    $ State = "hetero"
            elif GirlA.GirlLikecheck(GirlB) >= 700:
                    #if she doesn't like you but likes the other girl, lesbian
                    $ State = "lesbian"

            if State == "lesbian" or State == "threeway":
                #if she's into girls, add girl-touching options
                $ Options.extend(("fondle_breasts","suck_breasts","fondle_pussy","fondle_ass","kiss girl"))

                if Approvalcheck(GirlA, 800, "I") or GirlA.GirlLikecheck(GirlB) >= 800:
                    $ Options.append("eat_pussy")
                if Approvalcheck(GirlA, 900, "I") and GirlA.GirlLikecheck(GirlB) >= 900:
                    $ Options.append("eat_ass")


            if State == "hetero" or State == "threeway":
                #if she's into you, add you-touching options
                if primary_action == "anal":
                    $ Options.extend(("handjob","kiss","kiss"))
                else:
                    $ Options.extend(("handjob","blowjob","kiss"))
            $ renpy.random.shuffle(Options)

            if Preset:
                if Preset in Options:
                        #if the suggested action is in the possible actions. . .
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
                elif Approvalcheck(GirlA, 750, "I") or Approvalcheck(GirlA, 1500):
                        #if the suggestion is not in the options, but she's game anyway
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
                        #she refuses
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

            #Sets opening lines. . .
            if Options[0] == Action:
                    #If it's the same result, just hop back
                    return
            elif Mode == "lesbian":
                    $ line = GirlA.name + " shifts her position"
            elif not second_girl_primary_action or second_girl_primary_action == "masturbation":
                    #If this is the first action,
                    $ line = GirlA.name + " moves closer"
            else:
                    #If this is a new action
                    $ line = GirlA.name + " shifts her position"


            if Options[0] == "masturbation":
                        $ Action = "masturbation"
                        call Girl_Self_lines(GirlA,"T5",second_girl_offhand_action)  #nee Rog*ue_Self_lines
            elif Options[0] == "handjob":
                        call Seen_First_Peen(GirlA,GirlB,React=1)
                        $ line = line + " before she slides her hand down and firmly grabs your dick"
                        $ Action = "handjob"
                        if GirlA == RogueX:
                                show Rogue_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200
                        elif GirlA == KittyX:
                                show Kitty_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200
                        elif GirlA == EmmaX:
                                show Emma_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200
                        elif GirlA == LauraX:
                                show Laura_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200
                        elif GirlA == JeanX:
                                show Jean_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200
                        elif GirlA == StormX:
                                show Storm_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200
                        elif GirlA == JubesX:
                                show Jubes_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200
                        $ Approval = 4
                        $ TempFocus += 3 if Player.Focus > 70 else 2
                        $ Templust += 2 if GirlA.lust < 60 else 0
                        $ Templust += 2 if GirlA.action_counter["handjob"] > 2 else 0
                        $ GirlA.Addict -= 1 if D20 > 10 else 2
            elif Options[0] == "blowjob":
                        call Seen_First_Peen(GirlA,GirlB,React=1)
                        $ line = line + " before she slides down and begins to slowly lick your cock"
                        if GirlA == RogueX:
                                show Rogue_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200
                        elif GirlA == KittyX:
                                show Kitty_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200
                        elif GirlA == EmmaX:
                                show Emma_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200
                        elif GirlA == LauraX:
                                show Laura_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200
                        elif GirlA == JeanX:
                                show Jean_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200
                        elif GirlA == StormX:
                                show Storm_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200
                        elif GirlA == JubesX:
                                show Jubes_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200
                        $ Action = "blowjob"
                        $ Approval = 4

                        $ TempFocus += 20 if Player.Focus > 60 else 10
                        $ Templust += 2 if GirlA.lust > 80 else 1
                        $ GirlA.Addict -= 2
            #the above three do not apply to lesbian actions.

            elif Options[0] == "fondle_breasts":

                        $ line = line + " and slides her hands along " + GirlB.name + "'s breasts"
                        $ Action = "fondle_breasts"
                        if "lesbian" not in GirlA.recent_history:
                                $ GirlA.Les += 1
                                $ GirlA.recent_history.append("lesbian")
                        if "lesbian" not in GirlB.recent_history:
                                $ GirlB.Les += 1
                                $ GirlB.recent_history.append("lesbian")
                        $ Templust += 2 if Approvalcheck(GirlA, 500, "I") else 1  # GirlA's lust
                        $ Templust2 += 4 if GirlB.GirlLikecheck(GirlA) >= 800 else 2
                        $ TempFocus += 1
            elif Options[0] == "suck_breasts":

                        $ line = line + " and slurps " + GirlB.name + "'s nipple into her mouth"
                        $ Action = "suck_breasts"
                        if "lesbian" not in GirlA.recent_history:
                                $ GirlA.Les += 1
                                $ GirlA.recent_history.append("lesbian")
                        if "lesbian" not in GirlB.recent_history:
                                $ GirlB.Les += 1
                                $ GirlB.recent_history.append("lesbian")
                        $ Templust += 2 if Approvalcheck(GirlA, 500, "I") else 1  # GirlA's lust
                        $ Templust2 += 5 if GirlB.GirlLikecheck(GirlA) >= 800 else 2
                        $ TempFocus += 1
            elif Options[0] == "fondle_pussy":

                        $ line = line + " and runs her finger along " + GirlB.name + "'s pussy"
                        $ Action = "fondle_pussy"
                        if "lesbian" not in GirlA.recent_history:
                                $ GirlA.Les += 1
                                $ GirlA.recent_history.append("lesbian")
                        if "lesbian" not in GirlB.recent_history:
                                $ GirlB.Les += 1
                                $ GirlB.recent_history.append("lesbian")
                        $ Templust += 2 if Approvalcheck(GirlA, 500, "I") else 1  # GirlA's lust
                        $ Templust2 += 5 if GirlB.GirlLikecheck(GirlA) >= 800 else 3
                        $ TempFocus += 2
            elif Options[0] == "eat_pussy":

                        $ line = line + " and runs her tongue along " + GirlB.name + "'s pussy"
                        $ Action = "eat_pussy"
                        if "lesbian" not in GirlA.recent_history:
                                $ GirlA.Les += 1
                                $ GirlA.recent_history.append("lesbian")
                        if "lesbian" not in GirlB.recent_history:
                                $ GirlB.Les += 1
                                $ GirlB.recent_history.append("lesbian")
                        $ Templust += 3 if Approvalcheck(GirlA, 600, "I") else 1  # GirlA's lust
                        $ Templust2 += 8 if GirlB.GirlLikecheck(GirlA) >= 800 else 5
                        $ TempFocus += 3
            elif Options[0] == "fondle_ass":

                        $ line = line + " and gives " + GirlB.name + "'s ass a firm squeeze"
                        $ Action = "fondle_ass"
                        if "lesbian" not in GirlA.recent_history:
                                $ GirlA.Les += 1
                                $ GirlA.recent_history.append("lesbian")
                        if "lesbian" not in GirlB.recent_history:
                                $ GirlB.Les += 1
                                $ GirlB.recent_history.append("lesbian")
                        $ Templust += 1 if Approvalcheck(GirlA, 400, "I") else 0  # GirlA's lust
                        $ Templust2 += 3 if GirlB.GirlLikecheck(GirlA) >= 600 else 2
                        $ TempFocus += 1
            elif Options[0] == "eat_ass":

                        $ line = line + " and starts to lick around " + GirlB.name + "'s ass"
                        $ Action = "eat_ass"
                        if "lesbian" not in GirlA.recent_history:
                                $ GirlA.Les += 1
                                $ GirlA.recent_history.append("lesbian")
                        if "lesbian" not in GirlB.recent_history:
                                $ GirlB.Les += 1
                                $ GirlB.recent_history.append("lesbian")
                        $ Templust += 3 if Approvalcheck(GirlA, 800, "I") else 1  # GirlA's lust
                        $ Templust2 += 6 if GirlB.GirlLikecheck(GirlA) >= 800 else 4
                        $ TempFocus += 2

            elif Options[0] == "kiss girl" or Mode == "lesbian":
                        $ line = line + " and gives " + GirlB.name + " a passionate kiss"
                        $ Action = "kiss girl"
                        if Mode != "lesbian" and "kiss" in Options:
                                if primary_action == "kiss":
                                        $ Action = "kiss both"
                                elif girl_offhand_action == "kiss":
                                        $ Action = "kiss both"
                                elif second_girl_primary_action == "kiss":
                                        $ Action = "kiss both"
                        $ TempFocus += 1
            elif Options[0] == "kiss":
                        $ line = line + " and gives you a passionate kiss"
                        $ Action = "kiss"
                        if "kiss girl" in Options:
                                if primary_action == "kiss":
                                        $ Action = "kiss both"
                                elif girl_offhand_action == "kiss":
                                        $ Action = "kiss both"
                                elif second_girl_primary_action == "kiss":
                                        $ Action = "kiss both"
                        $ Templust += 1
                        $ TempFocus += 1

            else:
                        $ line = GirlA.name + " is just watching the two of you intently"
                        $ Action = "watch"
                        $ Templust += 1 if GirlA.GirlLikecheck(GirlB) >= 600 else 0  # GirlA's lust
                        $ Templust += 2 if GirlA.GirlLikecheck(GirlB) >= 800 else 1  # GirlA's lust
                        $ Templust2 += 1 if Approvalcheck(GirlB, 500, "I") else 0
                        $ Templust2 += 1 if Approvalcheck(GirlB, 700, "I") else 0
                        $ TempFocus += 1

            if Action == "kiss girl" or Action == "kiss both":
                        #If there's a semi-lesbian make-out. . .
                        if "lesbian" not in GirlA.recent_history:
                                $ GirlA.Les += 1
                                $ GirlA.recent_history.append("lesbian")
                        if "lesbian" not in GirlB.recent_history:
                                $ GirlB.Les += 1
                                $ GirlB.recent_history.append("lesbian")
                        $ Templust += 1 if Approvalcheck(GirlA, 500, "I") else 0  # GirlA's lust
                        $ Templust += 1 if GirlA.GirlLikecheck(GirlB) >= 800 else 0
                        $ Templust2 += 2 if GirlB.GirlLikecheck(GirlA) >= 800 else 1
                        $ TempFocus += 1

            # Wrap-up
            if Preset:
                    $ position_change_timer = Round - 2
            else:
                    #this sets a delay before the values change again on their own
                    $ position_change_timer = Round - 1
            $ Templust2 += 2
            if Mode == "lesbian":
                    #Sets Primary Girl's secondary action
                    $ girl_offhand_action = Action
                    $ Primarylust += (Templust * 3)
                    $ Secondarylust += (Templust2 * 3)
            elif Mode == "start":
                    #Sets Rog*ue's action and lust if this is a starting action
                    $ second_girl_primary_action = Action
                    $ GirlA.lust += Templust2
            else:
                    #Sets Secondary girl's action
                    $ second_girl_primary_action = Action
                    $ Secondarylust += Templust
                    $ Primarylust += Templust2
            if Preset:
                    #if this was done at your direction, apply lusts
                    $ GirlA.lust += Templust
                    $ GirlB.lust += Templust2
            $ Player.Focus += TempFocus

            return

label Dirty_Talk(Girl = Primary, D20=0, Tempcheck=0, phrase=0, Tempprimary_action=second_girl_primary_action, ActiveGirl=0):
    if primary_action == "strip" or not primary_action:
        return

    $ D20 = renpy.random.randint(1, 4)

    if D20 == 1:
        return
    elif D20 == 4 and Partner in all_Girls:
            #RNG said partner says a line
            $ Girl = Partner
            $ ActiveGirl = Primary
            $ Tempcheck = second_girl_primary_action
            $ Tempprimary_action = second_girl_primary_action
    else: #if D20 == 2 or 3
            #RNG said lead girl says a line
            $ Girl = Primary
            $ ActiveGirl = Secondary
            $ Tempcheck = primary_action
            $ Tempprimary_action = girl_offhand_action

    $ D20 = renpy.random.randint(1, 20)

    if "vocal" not in Girl.Traits:
            #if she's non-vocal, she will remain silent
            if Girl.lust >= 60:
                pass
            else:
                return
    elif D20 >= 15 or Girl.OCount >= 5:
            #drops it down to the generic grunts if roll over 15
            pass

    elif Girl == RogueX:
            # if the Girl is Rogue. . .
            if primary_action == "lesbian" or (Secondary == RogueX and Tempprimary_action not in ("handjob","blowjob","masturbation")):
                    #if this is a lesbian action, or if the threesome action is girl-focused

                    if "unseen" not in RogueX.recent_history and D20 <= 5:
                            #if they know you're watching, there is a 3/10 or 2/5 chance
                            $ phrase = "Hmm, enjoying the show, "+RogueX.Petname+"?" #you watching
                    elif D20 <= 10:
                            pass
                    elif Tempprimary_action == "fondle_breasts":
                            $ phrase = "Your titties feel so nice, "+ActiveGirl.name+"." #fondle breasts
                    elif Tempprimary_action == "suck_breasts":
                            $ phrase = "Your titties taste so good, "+ActiveGirl.name+"." #suck breasts
                    elif Tempprimary_action == "fondle_pussy":
                            $ phrase = "You're sucking me in, "+ActiveGirl.name+"." #fondle pussy
                    elif Tempprimary_action == "eat_pussy":
                            $ phrase = "You taste so good, "+ActiveGirl.name+"." #lick pussy

                    if not phrase:
                            #if nothing else is selected, or if D20: 1-3, or if D20: 14-15
                            $ phrase = renpy.random.choice([
                                    "Touch'n ya is so amazing, " + ActiveGirl.name + ".",
                                    "Your body feels so amazing. . .",
                                    "Mmmm. . .right there.",
                                    "Ya like that, " + ActiveGirl.name + "?"
                                    ])

            elif Tempcheck == "masturbation":
                    if "unseen" not in RogueX.recent_history:
                            #if she knows you're watching
                            if D20 <= 3:
                                # it's under a 3 roll
                                if "cockout" in Player.recent_history:
                                    # Your cock's out
                                    $ phrase = renpy.random.choice([
                                                "Could I get some of that, " + RogueX.Petname + "?",
                                                "Why don'tcha bring that over here, " + RogueX.Petname + "?"
                                                ])
                                else:
                                    # Your cock's not out
                                    $ phrase = renpy.random.choice([
                                                "Why so shy, " + RogueX.Petname + "?",
                                                "I'm showing mine, where's yours?"
                                                ])
                            else:
                                    # It's over a 3 roll
                                    $ phrase = renpy.random.choice([
                                                "I want ya so bad, " + RogueX.Petname + ".",
                                                "Come on over here, " + RogueX.Petname + ". Take me however ya want.",
                                                "Hmm, enjoying the show, "+RogueX.Petname+"?",
                                                "I love the look you get on your face, " + RogueX.Petname + "."
                                                ])
                    #else: D20 >=15, drops to generic options
            else:
                    #if neither lesbian nor masturbation
                    # Tempcheck will be trigger if primary or trigger4 if secondary
                    #this will not be masturbation, or girl-focused.

                    if D20 <= 10:
                            pass
                    elif RogueX.SEXP <= 20 or Tempcheck == "kiss":
                            #If she's relatively inexperienced
                            $ phrase = renpy.random.choice([
                                    "Touching ya is so amazing, " + RogueX.Petname + ".",
                                    "Every time you touch me. . . it's like, I can't even put it into words.",
                                    "Mmmm. . .right there.",
                                    "Am I doing that right?",
                                    "Ya like that, " + RogueX.Petname + "?"
                                    ])
                    elif Tempcheck == "handjob":
                        $ phrase = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "Seems like you like my hand, huh, " + RogueX.Petname + "?",
                                    "I can feel you get harder in my hand. . .",
                                    ])
                    elif Tempcheck == "blowjob":
                        $ phrase = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "You taste so nice, " + RogueX.Petname + ".",
                                    "I can feel you get harder in my mouth. . .",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",
                                    ])
                    elif Tempcheck == "titjob":
                        $ phrase = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + RogueX.Petname + ".",
                                    "I can feel you get harder in there. . ."
                                    ])
                    elif Tempcheck == "sex" or Tempcheck == "anal":
                        if D20 <= 3 and Tempcheck == "anal" and RogueX.Loose <= 1:
                            $ phrase = "It. . .hurts. But it kinda feels good, too." #anal
                        else:
                            $ phrase = renpy.random.choice([
                                        "Your cock is so warm. . .",
                                        "Ohhh. . .that's sooo good.",
                                        "Ung, so deep. . .",
                                        "Keep it up, keep it up. . .",
                                        "Oh, don't stop. . .",
                                        "I can feel you get harder inside me. . ."
                                        ])

                    if not phrase:
                        #if nothing else is selected, or if D20 < 10
                        if Primary == RogueX:
                                $ phrase = renpy.random.choice([
                                        "I want ya so bad, " + RogueX.Petname + ".",
                                        "Your touch is so amazin, " + RogueX.Petname + ".",
                                        "Oooh, right there. . .",
                                        "More, gimme more!",
                                        "I'm all yours, " + RogueX.Petname + ". Take me however ya want.",
                                        "I love it when ya do that, " + RogueX.Petname + ".",
                                        "I love the look you get on your face, " + RogueX.Petname + "."
                                        ])
                        else:
                                $ phrase = renpy.random.choice([
                                        "I want ya so bad, " + RogueX.Petname + ".",
                                        "Could I get some of that, " + RogueX.Petname + "?",
                                        "Think ya could maybe share that, " + ActiveGirl.name + "?",
                                        "Come on over here, " + RogueX.Petname + ". Take me however ya want.",
                                        "So that's what you look like from this angle.",
                                        "I love the look you get on your face, " + RogueX.Petname + ".",
                                        "That's right, give it to her.",
                                        "You're really getting into it, " + ActiveGirl.name + "."
                                        ])
    #end Rogue
    elif Girl == KittyX:
            # if the Girl is Kitty. . .
            if primary_action == "lesbian" or (Secondary == KittyX and Tempprimary_action not in ("handjob","blowjob","masturbation")):
                    #if this is a lesbian action, or if the threesome action is girl-focused

                    if "unseen" not in KittyX.recent_history and D20 <= 7:
                            #if they know you're watching, there is a 3/10 or 2/5 chance
                            $ phrase = "Hmm, like what you see, "+KittyX.Petname+"?" #you watching
                    elif Tempprimary_action == "fondle_breasts":
                        if ActiveGirl in (EmmaX,StormX):
                            $ phrase = "I'm so jelly here "+ActiveGirl.name+"." #fondle breasts
                        else:
                            $ phrase = "I love these tits, "+ActiveGirl.name+"." #fondle breasts
                    elif Tempprimary_action == "suck_breasts":
                        if ActiveGirl in (EmmaX,StormX):
                            $ phrase = "These tits are {i}amazing,{/i} "+ActiveGirl.name+"." #fondle breasts
                        else:
                            $ phrase = "Hmm, you taste so good, "+ActiveGirl.name+"." #suck breasts
                    elif Tempprimary_action == "fondle_pussy":
                            $ phrase = "So wet, "+ActiveGirl.name+"." #fondle pussy
                    elif Tempprimary_action == "eat_pussy":
                        if ActiveGirl == RogueX and RogueX.Pubes:
                            $ phrase = "I love your little stripe, Rogue." #lick pussy
                        else:
                            $ phrase = "You're drowning me here, "+ActiveGirl.name+"." #lick pussy

                    if not phrase:
                            #if nothing else is selected, or if D20: 1-3, or if D20: 14-15
                            $ phrase = renpy.random.choice([
                                    "You're so amazing, " + ActiveGirl.name + ".",
                                    "You know how to push" + KittyX.like + "every one of my buttons. . .",
                                    "Heh. . .{i}somebody{/i} seems to like that.",
                                    "That's" + KittyX.like + "{i}so{/i} good.",
                                    "You taste so good. . ."
                                    ])

            elif Tempcheck == "masturbation":
                    if "unseen" not in KittyX.recent_history:
                            #if she knows you're watching
                            if D20 <= 3:
                                # it's under a 3 roll
                                if "cockout" in Player.recent_history:
                                    # Your cock's out
                                    $ phrase = renpy.random.choice([
                                                "Hmm, I'd like some of that, " + KittyX.Petname + "?",
                                                "Could I get a taste, " + KittyX.Petname + "?"
                                                ])
                                else:
                                    # Your cock's not out
                                    $ phrase = renpy.random.choice([
                                                "Feeling shy, " + KittyX.Petname + "?",
                                                "How 'bout a little tat for tit?"
                                                ])
                            else:
                                    # It's over a 3 roll
                                    $ phrase = renpy.random.choice([
                                                "I really want you, " + KittyX.Petname + ".",
                                                "Come'ere, " + KittyX.Petname + ". Gimme a taste.",
                                                "Hmm, like the show, "+KittyX.Petname+"?",
                                                "You look so cute over there, " + KittyX.Petname + "."
                                                ])
                    #else: D20 >=17, drops to generic options
            else:
                #if neither lesbian nor masturbation
                    # Tempcheck will be trigger if primary or trigger4 if secondary
                    #this will not be masturbation, or girl-focused.

                    if D20 <= 10:
                            pass
                    elif KittyX.SEXP <= 30 or Tempcheck == "kiss":
                            #If she's relatively inexperienced
                            $ phrase = renpy.random.choice([
                                    "You're so amazing, " + KittyX.Petname + ".",
                                    "You know how to push, like, every one of my buttons. . .",
                                    "Heh. . .{i}somebody{/i} seems to like that.",
                                    "That's, like, {i}so{/i} good."
                                    ])
                    elif Tempcheck == "handjob":
                        $ phrase = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I love the way it"+KittyX.like+"feels in my hands.",
                                    "Seems like you like my hand, huh, " + RogueX.Petname + "?",
                                    "I can feel you get harder in my hand. . .",
                                    ])
                    elif Tempcheck == "blowjob":
                        if D20 <= 3:
                            ch_k "I hope you don't think I'm[KittyX.like]a slut for saying this. . ."
                            $ phrase = "but I love how you taste, " + KittyX.Petname + "."
                        else:
                            $ phrase = renpy.random.choice([
                                        "So warm. . .",
                                        "You taste so good, " + KittyX.Petname + ".",
                                        "You're getting harder in my mouth. . .",
                                        "Mmhmhm. . .",
                                        "-gulp-. . .",
                                        ])
                    elif Tempcheck == "titjob":
                        $ phrase = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + KittyX.Petname + ".",
                                    "I can feel you get harder in there. . ."
                                    ])
                    elif Tempcheck == "sex" or Tempcheck == "anal":
                        if D20 <= 3 and Tempcheck == "anal" and KittyX.Loose <= 1:
                            $ phrase = "Please. . .go slow, 'kay?  You feel so {i}big{/i}."
                        else:
                            $ phrase = renpy.random.choice([
                                        "Your cock is so warm. . .",
                                        "Ohhh. . .that's sooo good.",
                                        "Mmm, you feel so huge. . .",
                                        "Ung, so deep. . .",
                                        "Oooohh. . .just like {i}that{/i}.",
                                        "Keep it up, keep it up. . .",
                                        "Oh, don't stop. . .",
                                        "Did you just get harder?"
                                        ])

                    if not phrase:
                        #if nothing else is selected, or if D20 > 10
                        if Primary == KittyX:
                                $ phrase = renpy.random.choice([
                                            "This is {i}so{/i} hot, " + KittyX.Petname + ".",
                                            "I think I just"+KittyX.like+"discovered one of your other mutant powers, " + KittyX.Petname + ".",
                                            "I like it."+KittyX.Like+"a {i}lot{/i}.",
                                            "Oooh, that's it. . .",
                                            "More, gimme more!",
                                            "You're looking so cute, " +KittyX.Petname + "!",
                                            "I've never wanted a guy like I want you, " + KittyX.Petname + "."
                                            ])
                        else:
                                $ phrase = renpy.random.choice([
                                            "Don't take all the fun, " + ActiveGirl.name + ".",
                                            "I could use some attention over here, " + KittyX.Petname + ".",
                                            "I got something over here for you, " + KittyX.Petname + ".",
                                            "You're looking pretty good from over here.",
                                            "Looks like he likes the way you do that.",
                                            "Make sure you save some for {i}me{/i}!",
                                            "You two look {i}so{/i} sexy doing that.",
                                            "I can't believe you can take all of him like that!",
                                            "That looks like fun, " + ActiveGirl.name + "."
                                            ])
    #end Primary Kitty
    elif Girl == EmmaX:
            # if the Girl is Emma. . .
            if primary_action == "lesbian" or (Secondary == EmmaX and Tempprimary_action not in ("handjob","blowjob","masturbation")):
                    #if this is a lesbian action, or if the threesome action is girl-focused

                    if "unseen" not in EmmaX.recent_history and D20 <= 5:
                            #if they know you're watching, there is a 3/10 or 2/5 chance
                            $ phrase = "Are you enjoying the performance, "+EmmaX.Petname+"?" #you watching
                    elif Tempprimary_action == "fondle_breasts" or Tempprimary_action == "suck_breasts":
                            if ActiveGirl == KittyX:
                                $ phrase = "Oh my, these breasts are adorable!" #fondle breasts
                            else:
                                $ phrase = "These really are wonderfully. . . pert." #fondle breasts
                    elif Tempprimary_action == "fondle_pussy":
                                $ phrase = "Such pressure, "+ActiveGirl.name+"." #fondle pussy
                    elif Tempprimary_action == "eat_pussy":
                            if ActiveGirl == LauraX:
                                $ phrase = "Oh yes, that is a Howlett." #lick pussy
                            else:
                                $ phrase = "What an exotic flavor, " + ActiveGirl.name + "." #lick pussy
                    if not phrase:
                            #if nothing else is selected, or if D20: 1-3, or if D20: 14-15
                            $ phrase = renpy.random.choice([
                                    "Incredible, " + ActiveGirl.name + ".",
                                    "You're surprisingly skilled at this. . .",
                                    "Well, that certainly got a positive response.",
                                    "Exceptional, darling.",
                                    "Delicious. . ."
                                    ])

            elif Tempcheck == "masturbation":
                    if "unseen" not in EmmaX.recent_history:
                            #if she knows you're watching
                            if D20 <= 3:
                                # it's under a 3 roll
                                if "cockout" in Player.recent_history:
                                    # Your cock's out
                                    $ phrase = renpy.random.choice([
                                                "Oh, I could use some of that, " + EmmaX.Petname + ".",
                                                "Why don't you join me over here, " + EmmaX.Petname + "?"
                                                ])
                                else:
                                    # Your cock's not out
                                    $ phrase = renpy.random.choice([
                                                "Feeling shy, " + EmmaX.Petname + "?",
                                                "I feel like you aren't enjoying the show."
                                                ])
                            else:
                                    # It's over a 3 roll
                                    $ phrase = renpy.random.choice([
                                                "I need you over here, " + EmmaX.Petname + ".",
                                                "Come here, " + EmmaX.Petname + ". Take me.",
                                                "I hope you're enjoying the show, "+EmmaX.Petname+".",
                                                "I do love the look on your face, " + EmmaX.Petname + "."
                                                ])
                    #else: D20 >=15, drops to generic options
            else:
                    #if neither lesbian nor masturbation
                    # Tempcheck will be trigger if primary or trigger4 if secondary
                    #this will not be masturbation, or girl-focused.

                    if D20 <= 10:
                            pass
                    elif EmmaX.SEXP <= 30 or Tempcheck == "kiss":
                            #If she's relatively inexperienced
                            $ phrase = renpy.random.choice([
                                    "You're incredible, " + EmmaX.Petname + ".",
                                    "You're surprisingly skilled at this. . .",
                                    "Well, that certainly got a positive response.",
                                    "Exceptional work, darling.",
                                    ])
                    elif Tempcheck == "handjob":
                        $ phrase = renpy.random.choice([
                                    "Your cock is so very warm. . .",
                                    "I trust you're enjoying the massage?",
                                    "I take it you're enjoying yourself, " + EmmaX.Petname + "?",
                                    "I can feel you grow harder. . .",
                                    ])
                    elif Tempcheck == "blowjob":
                        $ phrase = renpy.random.choice([
                                    "So delicious. . .",
                                    "I must say, I enjoy the flavor, " + EmmaX.Petname + ".",
                                    "I can feel you get harder in my mouth. . .",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",
                                    ])
                    elif Tempcheck == "titjob":
                        $ phrase = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + EmmaX.Petname + ".",
                                    "Don't get lost in there now . .",
                                    "I can feel you get harder in there. . ."
                                    ])
                    elif Tempcheck == "sex" or Tempcheck == "anal":
                            $ phrase = renpy.random.choice([
                                    "Mmmm, give me more like that. . .",
                                    "Nngh, how filling. . .",
                                    "Ung, so deep. . .",
                                    "Keep it up, keep it up. . .",
                                    "Oh, don't stop. . .",
                                    "I can feel you get harder inside me. . ."
                                    ])

                    if not phrase:
                        #if nothing else is selected, or if D20 > 10
                        if Primary == EmmaX:
                                $ phrase = renpy.random.choice([
                                        "I'm overwhelmed, " + EmmaX.Petname + ".",
                                        "Well now we have another skill to develop, " + EmmaX.Petname + ".",
                                        "Oooh, that's lovely. . .",
                                        "More, I want more!",
                                        "You're simply adorable, " + EmmaX.Petname + ".",
                                        "Ooh, you'll {i}have{/i} to do that one again. . .",
                                        "You certainly do leave an impression, " + EmmaX.Petname + "."
                                        ])
                        else:
                                $ phrase = renpy.random.choice([
                                        "Oh " + EmmaX.Petname + "? Don't keep me waiting.",
                                        "Oh " + ActiveGirl.name + "? Could you share some of that?",
                                        "Come on over here, " + EmmaX.Petname + ", ravish me.",
                                        "You certainly do put on a show.",
                                        "You're simply adorable, " + EmmaX.Petname + ".",
                                        "Nngh, give it to her.",
                                        "You seem to be enjoying yourself, " + ActiveGirl.name + "."
                                        ])
            #End Emma's dirty talk lines
    #end Primary Emma
    elif Girl == LauraX:
            # if the Girl is Laura. . .
            if Approvalcheck(LauraX, 1500):
                    $ D20 -= 5
            elif Approvalcheck(LauraX, 1200):
                    $ D20 -= 3
            if D20 >= 10:
                    #drops it down to the generic grunts
                    pass
            elif primary_action == "lesbian" or (Secondary == LauraX and Tempprimary_action not in ("handjob","blowjob","masturbation")):
                    #if this is a lesbian action, or if the threesome action is girl-focused

                    if "unseen" not in LauraX.recent_history and D20 <= 5:
                            #if they know you're watching, there is a 3/10 or 2/5 chance
                            $ phrase = "Looking good, "+LauraX.Petname+"?" #you watching
                    elif Tempprimary_action == "fondle_breasts":
                            if ActiveGirl in (EmmaX,StormX):
                                $ phrase = "These things are huge." #fondle breasts
                            else:
                                $ phrase = "Your titties feel so nice, "+ActiveGirl.name+"." #fondle breasts
                    elif Tempprimary_action == "suck_breasts":
                            $ phrase = "Hmm, tasty." #suck breasts
                    elif Tempprimary_action == "fondle_pussy":
                                $ phrase = "Cozy in there." #fondle pussy
                    elif Tempprimary_action == "eat_pussy":
                            if ActiveGirl == RogueX:
                                $ phrase = "Spicy." #lick pussy
                            elif ActiveGirl == KittyX:
                                $ phrase = "Hmm, sweet." #lick pussy
                            elif ActiveGirl == EmmaX:
                                $ phrase = "So many different flavors." #lick pussy
                            elif ActiveGirl == JeanX:
                                $ phrase = "Huh, tangy." #lick pussy
                            elif ActiveGirl == StormX:
                                $ phrase = "Very rich flavor." #lick pussy
                            elif ActiveGirl == JubesX:
                                $ phrase = "Nice, very smooth." #lick pussy
                    if not phrase:
                            #if nothing else is selected, or if D20: 1-3, or if D20: 14-15
                            $ phrase = renpy.random.choice([
                                    "Good job, " + ActiveGirl.name + ".",
                                    "You know what you're doing. . .",
                                    "Oooh, I liked that one.",
                                    "Great work.",
                                    "Tasty. . ."
                                    ])

            elif Tempcheck == "masturbation":
                    if "unseen" not in LauraX.recent_history:
                            #if she knows you're watching
                            if D20 <= 3:
                                # it's under a 3 roll
                                if "cockout" in Player.recent_history:
                                    # Your cock's out
                                    $ phrase = renpy.random.choice([
                                                "Hey, don't let that go to waste.",
                                                "Come here, " + LauraX.Petname + "."
                                                ])
                                else:
                                    # Your cock's not out
                                    $ phrase = renpy.random.choice([
                                                "You aren't shy, are you " + LauraX.Petname + "?",
                                                "Pants, lose'em."
                                                ])
                            else:
                                    # It's over a 3 roll
                                    $ phrase = renpy.random.choice([
                                                "Get over here, " + LauraX.Petname + ".",
                                                "Not enjoying the show, "+LauraX.Petname+"?",
                                                "Heh, the look on your face, " + LauraX.Petname + "."
                                                ])
                    #else: D20 >=10, drops to generic options
            else:
                    #if neither lesbian nor masturbation
                    # Tempcheck will be trigger if primary or trigger4 if secondary
                    #this will not be masturbation, or girl-focused.

                    if D20 <= 5:
                            pass
                    elif LauraX.SEXP <= 30 or Tempcheck == "kiss":
                            #If she's relatively inexperienced
                            $ phrase = renpy.random.choice([
                                    "You're good at this, " + LauraX.Petname + ".",
                                    "Huh, you seem to know what you're doing. . .",
                                    "Oh, hey down there.",
                                    "Hmm, like that.",
                                    ])
                    elif Tempcheck == "handjob":
                        $ phrase = renpy.random.choice([
                                    "Hmm, your dick's so warm. . .",
                                    "This working for you?",
                                    "Seems like you're having fun, " + LauraX.Petname + "?",
                                    "You seem to be getting harder. . .",
                                    ])
                    elif Tempcheck == "blowjob":
                        $ phrase = renpy.random.choice([
                                    "Mmm, delicious. . .",
                                    "That's an interesting taste, " + LauraX.Petname + ".",
                                    "Did you just get harder? . .",
                                    "-Slurp.-",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",
                                    ])
                    elif Tempcheck == "titjob":
                        $ phrase = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + LauraX.Petname + ".",
                                    "I can feel you get harder in there. . ."
                                    ])
                    elif Tempcheck == "sex" or Tempcheck == "anal":
                            $ phrase = renpy.random.choice([
                                    "Mmmm, yeah, gimme more like that. . .",
                                    "Nngh, how filling. . .",
                                    "Ung, so deep. . .",
                                    "Keep it up, keep it up. . .",
                                    "Ngh, don't stop. . .",
                                    "That's right, harder, faster. . ."
                                    ])

                    if not phrase:
                        #if nothing else is selected, or if D20 > 10
                        if Primary == LauraX:
                                $ phrase = renpy.random.choice([
                                        "Wow, " + LauraX.Petname + ".",
                                        "That's great, " + LauraX.Petname + ".",
                                        "Oooh, that's nice. . .",
                                        "More!",
                                        "You're great, " + LauraX.Petname + ".",
                                        "Ok, that was a good one. . ."
                                        ])
                        else:
                                $ phrase = renpy.random.choice([
                                        "Hey, " + LauraX.Petname + "? Don't keep me waiting.",
                                        "Hey, " + ActiveGirl.name + "? Share, uh?",
                                        "Get over here, " + LauraX.Petname + ".",
                                        "Well you certainly put on a show.",
                                        "You're looking hot, " + LauraX.Petname + ".",
                                        "You're looking hot, " + ActiveGirl.name + ".",
                                        "Nngh, yeah, stick it to her.",
                                        "Well you seem to be having fun, " + ActiveGirl.name + "."
                                        ])
    #end Primary Laura

    elif Girl == JeanX:
            # if the Girl is Jean. . .
            if Approvalcheck(JeanX, 1500):
                    $ D20 -= 5
            elif Approvalcheck(JeanX, 1200):
                    $ D20 -= 3
            if D20 >= 10:
                    #drops it down to the generic grunts
                    pass
            elif primary_action == "lesbian" or (Secondary == JeanX and Tempprimary_action not in ("handjob","blowjob","masturbation")):
                    #if this is a lesbian action, or if the threesome action is girl-focused

                    if "unseen" not in JeanX.recent_history and D20 <= 5:
                            #if they know you're watching, there is a 3/10 or 2/5 chance
                            $ phrase = "Enjoying the show, "+JeanX.Petname+"?" #you watching
                    elif Tempprimary_action == "fondle_breasts":
                            if ActiveGirl == EmmaX:
                                $ phrase = "How do you even cart these things around?" #fondle breasts
                            else:
                                $ phrase = "Mmm, these things are firm, "+ActiveGirl.name+"." #fondle breasts
                    elif Tempprimary_action == "suck_breasts":
                            $ phrase = "Mmmm, tasty." #suck breasts
                    elif Tempprimary_action == "fondle_pussy":
                                $ phrase = "You like that, slut?" #fondle pussy

                    if not phrase:
                            #if nothing else is selected, or if D20: 1-3, or if D20: 14-15
                            $ phrase = renpy.random.choice([
                                    "Keep up the pace, " + ActiveGirl.name + ".",
                                    "Oh, good job there. . .",
                                    "Oooh, That was a good one.",
                                    "Good work.",
                                    "Tasty. . ."
                                    ])

            elif Tempcheck == "masturbation":
                    if "unseen" not in JeanX.recent_history:
                            #if she knows you're watching
                            if D20 <= 3:
                                # it's under a 3 roll
                                if "cockout" in Player.recent_history:
                                    # Your cock's out
                                    $ phrase = renpy.random.choice([
                                                "Hey, bring that one over here. . .",
                                                "Come here, " + JeanX.Petname + "."
                                                ])
                                else:
                                    # Your cock's not out
                                    $ phrase = renpy.random.choice([
                                                "Why're you having all the fun " + JeanX.Petname + "?",
                                                "Hey, let me see that beautiful boy."
                                                ])
                            else:
                                    # It's over a 3 roll
                                    $ phrase = renpy.random.choice([
                                                "Get over here, " + JeanX.Petname + ".",
                                                "Not enjoying the show, "+JeanX.Petname+"?",
                                                "The look on your face, " + JeanX.Petname + "."
                                                ])
                    #else: D20 >=10, drops to generic options
            else:
                    #if neither lesbian nor masturbation
                    # Tempcheck will be trigger if primary or trigger4 if secondary
                    #this will not be masturbation, or girl-focused.

                    if D20 <= 5:
                            pass
                    elif JeanX.SEXP <= 30 or Tempcheck == "kiss":
                            #If she's relatively inexperienced
                            $ phrase = renpy.random.choice([
                                    "You're good at this, " + JeanX.Petname + ".",
                                    "Huh, you seem to know what you're doing. . .",
                                    "Oh, hey down there.",
                                    "Hmm, like that.",
                                    ])
                    elif Tempcheck == "handjob":
                        $ phrase = renpy.random.choice([
                                    "Hmm, your dick's so warm. . .",
                                    "This working for you?",
                                    "Seems like you're having fun, " + JeanX.Petname + "?",
                                    "You seem to be getting harder. . .",
                                    ])
                    elif Tempcheck == "blowjob":
                        $ phrase = renpy.random.choice([
                                    "Mmm, delicious. . .",
                                    "That's an interesting flavor, " + JeanX.Petname + ".",
                                    "Did you just get harder? . .",
                                    "-Slurp.-",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",
                                    ])
                    elif Tempcheck == "titjob":
                        $ phrase = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + JeanX.Petname + ".",
                                    "I can feel you get harder in there. . ."
                                    ])
                    elif Tempcheck == "sex" or Tempcheck == "anal":
                            $ phrase = renpy.random.choice([
                                    "Mmmm, yeah, gimme more like that. . .",
                                    "Nngh, how filling. . .",
                                    "Ung, so deep. . .",
                                    "Keep it up, keep it up. . .",
                                    "Ngh, don't stop. . .",
                                    "That's right, harder, faster. . ."
                                    ])

                    if not phrase:
                        #if nothing else is selected, or if D20 > 10
                        if Primary == JeanX:
                                $ phrase = renpy.random.choice([
                                        "Wow, " + JeanX.Petname + ".",
                                        "That's great, " + JeanX.Petname + ".",
                                        "Oooh, that's nice. . .",
                                        "More!",
                                        "You're great, " + JeanX.Petname + ".",
                                        "Ok, that was a good one. . ."
                                        ])
                        else:
                                $ phrase = renpy.random.choice([
                                        "Hey, " + JeanX.Petname + "? Don't keep me waiting.",
                                        "Hey, " + ActiveGirl.name + "? Share, uh?",
                                        "Get over here, " + JeanX.Petname + ".",
                                        "Well you certainly put on a show.",
                                        "You're looking hot, " + JeanX.Petname + ".",
                                        "You're looking hot, " + ActiveGirl.name + ".",
                                        "Nngh, yeah, stick it to her.",
                                        "Well you seem to be having fun, " + ActiveGirl.name + "."
                                        ])
    #end Primary Jean
    elif Girl == StormX:
            # if the Girl is Storm. . .
            if primary_action == "lesbian" or (Secondary == StormX and Tempprimary_action not in ("handjob","blowjob","masturbation")):
                    #if this is a lesbian action, or if the threesome action is girl-focused

                    if "unseen" not in StormX.recent_history and D20 <= 5:
                            #if they know you're watching, there is a 3/10 or 2/5 chance
                            $ phrase = "So you do enjoy watching, "+StormX.Petname+"?" #you watching
                    elif Tempprimary_action == "fondle_breasts" or Tempprimary_action == "suck_breasts":
                            if ActiveGirl == EmmaX:
                                $ phrase = "These really are quite impressive, Emma." #fondle breasts
                            else:
                                $ phrase = "So firm. . ." #fondle breasts
                    elif Tempprimary_action == "fondle_pussy":
                                $ phrase = "Do you enjoy that, "+ActiveGirl.name+"." #fondle pussy
                    elif Tempprimary_action == "eat_pussy":
                            if ActiveGirl == LauraX:
                                $ phrase = "Hmmm, that is a familiar taste. . ." #lick pussy
                            else:
                                $ phrase = "What an exotic flavor, " + ActiveGirl.name + "." #lick pussy
                    if not phrase:
                            #if nothing else is selected, or if D20: 1-3, or if D20: 14-15
                            $ phrase = renpy.random.choice([
                                    "Oh, " + ActiveGirl.name + ".",
                                    "You are -very- skilled. . .",
                                    "Oh, you appear to have enjoyed that. . .",
                                    "Exceptional!",
                                    "Delicious. . ."
                                    ])

            elif Tempcheck == "masturbation":
                    if "unseen" not in StormX.recent_history:
                            #if she knows you're watching
                            if D20 <= 3:
                                # it's under a 3 roll
                                if "cockout" in Player.recent_history:
                                    # Your cock's out
                                    $ phrase = renpy.random.choice([
                                                "Oh, I could use some help here, " + StormX.Petname + ".",
                                                "Why do you not join me over here, " + StormX.Petname + "?"
                                                ])
                                else:
                                    # Your cock's not out
                                    $ phrase = renpy.random.choice([
                                                "Do not be shy, " + StormX.Petname + ".",
                                                "Are you not enjoying the show?"
                                                ])
                            else:
                                    # It's over a 3 roll
                                    $ phrase = renpy.random.choice([
                                                "I need you over here, " + StormX.Petname + ".",
                                                "Come here, " + StormX.Petname + ". Take me.",
                                                "Are you not enjoying the show, "+StormX.Petname+"?",
                                                "I do love the look on your face, " + StormX.Petname + "."
                                                ])
                    #else: D20 >=15, drops to generic options
            else:
                    #if neither lesbian nor masturbation
                    # Tempcheck will be trigger if primary or trigger4 if secondary
                    #this will not be masturbation, or girl-focused.

                    if D20 <= 10:
                            pass
                    elif StormX.SEXP <= 30 or Tempcheck == "kiss":
                            #If she's relatively inexperienced
                            $ phrase = renpy.random.choice([
                                    "You are incredible, " + StormX.Petname + ".",
                                    "You are quite skilled at this. . .",
                                    "You appear to have enjoyed that. . .",
                                    "Exceptional!",
                                    ])
                    elif Tempcheck == "handjob":
                        $ phrase = renpy.random.choice([
                                    "Your cock is so very warm. . .",
                                    "You appear to be enjoying the massage?",
                                    "You appear to be enjoying yourself, " + StormX.Petname + "?",
                                    "I can feel you grow harder. . .",
                                    ])
                    elif Tempcheck == "blowjob":
                        $ phrase = renpy.random.choice([
                                    "So delicious. . .",
                                    "I do enjoy this flavor, " + StormX.Petname + ".",
                                    "I can feel you get harder in my mouth. . .",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",
                                    ])
                    elif Tempcheck == "titjob":
                        $ phrase = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + StormX.Petname + ".",
                                    "Do not get lost in there now . .",
                                    "I can feel you get harder in there. . ."
                                    ])
                    elif Tempcheck == "sex" or Tempcheck == "anal":
                            $ phrase = renpy.random.choice([
                                    "Mmmm, more like that. . .",
                                    "Nngh, how. . . filling. . .",
                                    "Ung, so deep. . .",
                                    "Keep it up, keep it up. . .",
                                    "Oh, don't stop. . .",
                                    "I can feel you get harder inside me. . ."
                                    ])

                    if not phrase:
                        #if nothing else is selected, or if D20 > 10
                        if Primary == StormX:
                                $ phrase = renpy.random.choice([
                                        "I am overwhelmed, " + StormX.Petname + ".",
                                        "You are coming along quite nicely, " + StormX.Petname + ".",
                                        "Oooh, that is magnificent. . .",
                                        "More, I want more. . .",
                                        "You are simply -adorable,- " + StormX.Petname + ".",
                                        "You will {i}have{/i} to do that one again. . .",
                                        "You do leave an impression, " + StormX.Petname + "."
                                        ])
                        else:
                                $ phrase = renpy.random.choice([
                                        "Do not keep me waiting, " + StormX.Petname + ".",
                                        ActiveGirl.name + "? Could you please share some of that?",
                                        "Come here, " + StormX.Petname + ", ravish me.",
                                        "You certainly do put on a show.",
                                        "You are simply adorable, " + StormX.Petname + ".",
                                        "Nngh, give it to her.",
                                        "You seem to be enjoying yourself, " + ActiveGirl.name + "."
                                        ])
            #End Storm's dirty talk lines
    #end Primary Storm

    elif Girl == JubesX:
            # if the Girl is Jubes. . .
            if D20 >= 10:
                    #drops it down to the generic grunts
                    pass
            elif primary_action == "lesbian" or (Secondary == JubesX and Tempprimary_action not in ("handjob","blowjob","masturbation")):
                    #if this is a lesbian action, or if the threesome action is girl-focused

                    if "unseen" not in JubesX.recent_history and D20 <= 5:
                            #if they know you're watching, there is a 3/10 or 2/5 chance
                            $ phrase = "Like what you see there, "+JubesX.Petname+"?" #you watching
                    elif Tempprimary_action == "fondle_breasts":
                            if ActiveGirl in (EmmaX,StormX):
                                $ phrase = "Wow, how do you work with these. . ." #fondle breasts
                            else:
                                $ phrase = "Maybe I need to find a new bra, "+ActiveGirl.name+"." #fondle breasts
                    elif Tempprimary_action == "suck_breasts":
                            $ phrase = "Hmm, hard not to take a nibble. . ." #suck breasts
                    elif Tempprimary_action == "fondle_pussy":
                                $ phrase = "You're burning up. . ." #fondle pussy
                    elif Tempprimary_action == "eat_pussy":
                            if ActiveGirl == RogueX:
                                $ phrase = "So hot. . ." #lick pussy
                            elif ActiveGirl == KittyX:
                                $ phrase = "Mmmm, sweet." #lick pussy
                            elif ActiveGirl == EmmaX:
                                $ phrase = "So rich. . ." #lick pussy
                            elif ActiveGirl == JeanX:
                                $ phrase = "Well, that's not bad. . ." #lick pussy
                            elif ActiveGirl == StormX:
                                $ phrase = "Mmm. . . lovely. . ." #lick pussy
                    if not phrase:
                            #if nothing else is selected, or if D20: 1-3, or if D20: 14-15
                            $ phrase = renpy.random.choice([
                                    "Nice job, " + ActiveGirl.name + ".",
                                    "You're hitting all the right places. . .",
                                    "Ooo! More of that. . .",
                                    "Great job.",
                                    "Yum. . ."
                                    ])

            elif Tempcheck == "masturbation":
                    if "unseen" not in JubesX.recent_history:
                            #if she knows you're watching
                            if D20 <= 3:
                                # it's under a 3 roll
                                if "cockout" in Player.recent_history:
                                    # Your cock's out
                                    $ phrase = renpy.random.choice([
                                                "Hey, let me in on that. . .",
                                                "Get over here, " + JubesX.Petname + "."
                                                ])
                                else:
                                    # Your cock's not out
                                    $ phrase = renpy.random.choice([
                                                "Don't be shy, " + JubesX.Petname + ".",
                                                "Let me see what you're working with there. . ."
                                                ])
                            else:
                                    # It's over a 3 roll
                                    $ phrase = renpy.random.choice([
                                                "Get over here, " + JubesX.Petname + ".",
                                                "Don't you want in on this, "+JubesX.Petname+"?",
                                                "Heh, you need to join me over here, " + JubesX.Petname + "."
                                                ])
                    #else: D20 >=10, drops to generic options
            else:
                    #if neither lesbian nor masturbation
                    # Tempcheck will be trigger if primary or trigger4 if secondary
                    #this will not be masturbation, or girl-focused.

                    if D20 <= 5:
                            pass
                    elif JubesX.SEXP <= 30 or Tempcheck == "kiss":
                            #If she's relatively inexperienced
                            $ phrase = renpy.random.choice([
                                    "Oh, um, you seem to know what you're doing, " + JubesX.Petname + ".",
                                    "Ohh. . . that's nice. . .",
                                    "Oh, nice. . .",
                                    "Hmm, do that one again. . .",
                                    ])
                    elif Tempcheck == "handjob":
                        $ phrase = renpy.random.choice([
                                    "Hmm, your cock's so warm. . .",
                                    "Do you like this?",
                                    "You seem to be having fun, " + JubesX.Petname + ". . .",
                                    "Mmmm, you're getting harder in my hand. . .",
                                    ])
                    elif Tempcheck == "blowjob":
                        $ phrase = renpy.random.choice([
                                    "Mmm, delicious. . .",
                                    "I can't believe how you taste, " + JubesX.Petname + ".",
                                    "You're really firming up. . .",
                                    "-Slurp.-",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",
                                    ])
                    elif Tempcheck == "titjob":
                        $ phrase = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + JubesX.Petname + ".",
                                    "I can feel you get harder in there. . ."
                                    ])
                    elif Tempcheck == "sex" or Tempcheck == "anal":
                            $ phrase = renpy.random.choice([
                                    "Gimme more. . . & more. . .",
                                    "Nngh, filling me. . .",
                                    "Ung, deeper and deeper. . .",
                                    "Keep it up, keep it up. . .",
                                    "Ngh, don't stop. . .",
                                    "Ngh, harder, harder. . ."
                                    ])

                    if not phrase:
                        #if nothing else is selected, or if D20 > 10
                        if Primary == JubesX:
                                $ phrase = renpy.random.choice([
                                        "Wowow, " + JubesX.Petname + ".",
                                        "More like that, " + JubesX.Petname + ".",
                                        "Mmmm, that's nice. . .",
                                        "Gimme more!",
                                        "You're amazing, " + JubesX.Petname + ".",
                                        "Oooo. . . that was a good one. . ."
                                        ])
                        else:
                                $ phrase = renpy.random.choice([
                                        "Hey, " + JubesX.Petname + "? Don't leave me waiting.",
                                        "Hey, " + ActiveGirl.name + "? Let me in?",
                                        "Get over here, " + JubesX.Petname + ".",
                                        "Well. . . your certainly putting on a show.",
                                        "You're looking great there, " + JubesX.Petname + ".",
                                        "You're looking great there, " + ActiveGirl.name + ".",
                                        "Nngh, oh yeah, get in there.",
                                        "Well that looks like a lot of fun, " + ActiveGirl.name + "."
                                        ])
    #end Primary Jubes

    if not phrase:
            #if nothing else was chosen. . .
            if not ActiveGirl or second_girl_primary_action == "masturbation":
                    $ phrase = Girl.Petname
            else:
                    $ phrase = ActiveGirl.name
            $ phrase = renpy.random.choice([
                    "Mmmh. . .",
                    "Ung. . .",
                    "Ooooh. . .",
                    "Oooh, " + phrase + ", yes. . ."
                    ])

    Girl.voice "[phrase]"

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

    if Taboo:
        if Girl in [RogueX, KittyX]:
            if (action == "sex" and not Girl.Sex) or (action == "anal" and not Girl.Anal):
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
            $ Girl.inhibition += int(Taboo/10)
            $ Girl.lust += int(Taboo/5)
        else:
            $ JeanX.change_stat("inhibition", 90, int(Taboo/10))
            $ JeanX.change_stat("lust", 50, int(Taboo/5))
    else:
        if Girl in [RogueX, KittyX]:
            if (action == "sex" and not Girl.Sex) or (action == "anal" and not Girl.Anal):
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












label Sex_Basic_Dialog(Girl=0,Type=0): #rkeljsv
        # call Sex_Basic_Dialog(Girl,"done")
        #called from during sex scenes if a girl is getting tired. . .
        if Girl not in all_Girls:
                return
        if Girl == RogueX:
                if Type == "partner": #if a partner leaves during a scene
                                ch_r "Sorry about that."
                elif Type == "swallowgood":
                                ch_r "That was real sweet, [Girl.Petname]."
                elif Type == "swallowfirst":   #first time she's shallowed
                                ch_r "I'm not really a fan of that, [Girl.Petname]."
                elif Type == "swallow2":   #second time, no warning
                                ch_r "I'm starting to get used to that."
                elif Type == "warned":  #gave warning
                                ch_r "Thanks for the head's up."
                elif Type == "notwarned":  #no warning
                                ch_r "I could use a warning next time. . ."


        elif Girl == KittyX:
                if Type == "partner":
                                ch_k "Well that was awkward."
                elif Type == "swallowgood":
                                ch_k "Mmm, creamy."
                elif Type == "swallowfirst":
                                ch_k "Kinda nasty, [Girl.Petname]."
                elif Type == "swallow2":
                                ch_k "I'm starting to get used to that."
                elif Type == "warned":  #gave warning
                                ch_k "Thanks for the warning."
                elif Type == "notwarned":
                                ch_k "You coulda warned me first."


        elif Girl == EmmaX:
                if Type == "partner":
                                ch_e "Hmm, that was uncomfortable."
                elif Type == "swallowgood":
                                ch_e "Delectable, [Girl.Petname]."
                elif Type == "swallowfirst":
                                ch_e "I can't say that it would be my favorite flavor. . ."
                elif Type == "swallow2":
                                ch_e "It does grow on you. . ."
                elif Type == "warned":  #gave warning
                                ch_e "I appreciate the warning."
                elif Type == "notwarned":
                                ch_e "I should be upset, but I can't say I didn't enjoy that. . ."


        elif Girl == LauraX:
                if Type == "partner":
                                ch_l "I wonder if she's coming back."
                elif Type == "swallowgood":
                                ch_l "Yum."
                elif Type == "swallowfirst":
                                ch_l "That's. . . intense. . ."
                elif Type == "swallow2":
                                ch_l "Mmmmm. . ."
                elif Type == "warned":  #gave warning
                                ch_l "Thanks for the heads up."
                elif Type == "notwarned":
                                ch_l "Why didn't you warn me?"


        elif Girl == JeanX:
                if Type == "partner":
                                ch_j "I'm sure she'll be missed."
                elif Type == "swallowgood":
                                ch_j "Mmm. . ."
                elif Type == "swallowfirst":
                                ch_j "Mmm. . . robust. . ."
                elif Type == "swallow2":
                                ch_j "Mmm. . ."
                elif Type == "warned":  #gave warning
                                pass
                elif Type == "notwarned":
                                ch_j "Warn me next thing though?"


        elif Girl == StormX:
                if Type == "partner":
                                ch_s "I am sorry for the awkwardness."
                elif Type == "swallowgood":
                                ch_s "That is. . . delicious. . ."
                elif Type == "swallowfirst":
                                ch_s "How. . . interesting. . ."
                elif Type == "swallow2":
                                ch_s "Mmmm. . ."
                elif Type == "warned":  #gave warning
                                ch_s "I appreciate the warning. . ."
                elif Type == "notwarned":
                                ch_s "I could have been warned. . ."


        elif Girl == JubesX:
                if Type == "partner":
                                ch_v "Aw, that's a bummer. Anyway. . ."
                elif Type == "swallowgood":
                                $ Girl.Eyes = "closed"
                                ch_v "Mmmmmmmm. . ."
                                ch_v ". . ."
                                $ Girl.Eyes = "squint"
                                ch_v "Ok. . ."
                elif Type == "swallowfirst":
                                $ Girl.Eyes = "closed"
                                ch_v "Mmmmmmmm. . ."
                                $ Girl.Eyes = "surprised"
                                ch_v "Wow! . . that's. . . incredible. . ."
                                $ Girl.Eyes = "squint"
                                ch_v "Ok. . ."
                elif Type == "swallow2":
                                $ Girl.Eyes = "closed"
                                ch_v "Mmmmmmmm. . ."
                                ch_v ". . ."
                                $ Girl.Eyes = "squint"
                                ch_v "Ok. . ."
                elif Type == "warned":  #gave warning
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
        $ Girl.Pose = "doggy"

        call sex_launch(Girl, "sex")

        if Girl.wearing_skirt:
            "You press up against [Girl.name]'s backside, sliding her skirt up as you go."

            $ Girl.Upskirt = 1
        elif Girl.PantsNum() > 6:
            "You press up against [Girl.name]'s backside, sliding her pants down as you do."

            $ Girl.Legs = 0
        else:
            "You press up against [Girl.name]'s backside."

        $ Girl.SeenPanties = 1

        "You rub the tip of your cock against her moist slit."

        $ Girl.change_face("surprised", 1)
    elif action == "anal":
        $ Girl.Pose = "doggy"

        call sex_launch(Girl, "anal")

        if Girl.wearing_skirt:
            "You press up against [Girl.name]'s backside, sliding her skirt up as you go."

            $ Girl.Upskirt = 1
        elif Girl.PantsNum() > 6:
            "You press up against [Girl.name]'s backside, sliding her pants down as you do."

            $ Girl.Legs = 0
        else:
            "You press up against [Girl.name]'s backside."

        $ Girl.SeenPanties = 1

        "You press the tip of your cock against her tight rim."

        $ Girl.change_face("surprised", 1)
    elif action == "hotdog":
        $ Girl.Pose = "doggy"

        call sex_launch(Girl, "hotdog")

        "You press up against [Girl.name]'s backside."

        $ Girl.change_face("surprised", 1)

    return
