label Primary_SexDialog(GirlA=Primary,TempLine = 0, TempLust = 0, TempLust2 = 0): #rkeljs
    #nee Rog*ue_SexDialog(TempLine = 0, TempLust = 0, TempLust2 = 0)
    #called from Sex_Dialog as call Primary_SexDialog(Primary)
    if Situation == "skip" and Line:
            # if the action was set by a previous trigger, skip this element
            $ Situation = 0
            return

    if Trigger == "hand":
            $ Line = GirlA.Name + " continues stroke your cock. "

            if not Speed:
                        $ Line = GirlA.Name + " holds your cock in her hand. "
                        if GirlA.Hand > 2:
                                $ Line = Line + "She just seems to be enjoying the feel of it"
                                $ TempLust += 2 if GirlA.Lust < 60 else 0
                        else:
                                $ Line = Line + "She just seems to be looking it over"
                                $ TempLust += 2 if GirlA.Lust < 40 else 0
                                $ TempFocus += -3 if Player.Focus > 50 else 2
                        $ GirlA.Addict -= 1 if D20S > 10 else 2
                        return
            if GirlA in (EmmaX,LauraX,StormX):
                        #Laura and Emma have more experience to start
                        if Speed <= 1:
                            #slow
                            $ Line = Line + renpy.random.choice(["Her movements have become masterful, her slightest touch starts you twitching",
                                    "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here",
                                    "She slowly caresses you in a way that makes your blood boil, then pulls back at the last second",
                                    "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                    "You can't tell where she is at any moment, all you know is that it works"])
                            $ TempFocus += 20 if Player.Focus < 60 else 7
                        else:
                            #fast
                            $ Line = Line + renpy.random.choice(["Her movements have become masterful, her slightest touch starts you twitching",
                                    "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here",
                                    "Her expert strokes will have you boiling over in seconds",
                                    "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, you can tell she's had plenty of practice",
                                    "You can't tell where she is at any moment, all you know is that it works"])
                            $ TempFocus += 20 if Player.Focus > 70 else 7
            elif GirlA.Hand > 4:
                        # After the 5th time
                        if Speed <= 1:
                            #slow
                            $ Line = Line + renpy.random.choice(["Her movements have become almost masterful, her slightest touch starts you twitching",
                                    "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here",
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She slowly caresses you in a way that makes your blood boil, then pulls back at the last second",
                                    "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                    "You can't tell where she is at any moment, all you know is that it works"])
                            $ TempFocus += 20 if Player.Focus < 40 else 5
                        else:
                            #fast
                            $ Line = Line + renpy.random.choice(["Her movements have become almost masterful, her slightest touch starts you twitching",
                                    "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here",
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "Her expert strokes will have you boiling over in seconds",
                                    "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                    "You can't tell where she is at any moment, all you know is that it works"])
                            $ TempFocus += 20 if Player.Focus > 70 else 5
            elif 2 < GirlA.Hand <= 4:
                        #third through 5th time
                        if Speed <= 1:
                            #slow
                            $ Line = Line + renpy.random.choice(["She's begining to figure things out, her fingers cause tingles as they caress the shaft",
                                    "She's still learning, but learning fast. Her hands sure are smooth",
                                    "She has a smooth motion going now, gentle and precise",
                                    "Her lessons are paying off, she's really becoming very talented at this",
                                    "She gently caresses the shaft, and cups the balls in her other hand, giving them a warm massage"])
                            $ TempFocus += 15 if Player.Focus < 60 else 7
                        else:
                            #fast
                            $ Line = Line + renpy.random.choice(["She's begining to figure things out, her fingers cause tingles as they caress the shaft",
                                    "She's still learning, but learning fast. Her hands sure are smooth",
                                    "Her hands glide smoothly across your cock",
                                    "She has a smooth motion going now, gentle and precise",
                                    "Her lessons are paying off, she's really becoming very talented at this",
                                    "She quickly strokes your cock, with a very deft pressure"])
                            $ TempFocus += 15 if Player.Focus > 60 else 5
            else:
                    #First and second time
                    if Speed <= 1:
                        #slow
                        $ Line = Line + renpy.random.choice(["She makes up for her inexperience with determination, carefully stroking your cock",
                                "She moves her hands up and down the shaft. She's a little rough at this, but at least she tries",
                                "She strokes you gently. She isn't quite sure what to make of the balls",
                                "Her fingers fumble with your shaft a bit",
                                "She squeezes one of your balls too tightly, but stops when you wince",
                                "She has a firm grip, and she's not letting go. This may take a few tries"])
                        $ TempFocus += 12 if Player.Focus > 60 else 5
                    else:
                        #fast
                        $ Line = Line + renpy.random.choice(["She really wasn't prepared for speeding up, and your cock often slips out of her hand",
                                "She rapidly moves her hands up and down the shaft. She's a little rough at this, but at least she tries",
                                "She strokes you a bit too quickly, the friction is a bit uncomfortable",
                                "Her fingers fumble with your shaft a bit",
                                "She squeezes one of your balls too tightly, but stops when you wince",
                                "She has a firm grip, and she's not letting go. This train is out of control"])
                        $ TempFocus += 10 if Player.Focus > 60 else 2

            $ TempLust += 2 if GirlA.Lust < 60 else 0
            $ TempLust += 2 if GirlA.Hand > 2 else 0
            $ GirlA.Addict -= 1 if D20S > 10 else 2

    #End Handy dialog ////////////////////////////////////////////////////////////////////////////////////////////////////////


    elif Trigger == "titjob":
            #This can only ever be a primary action.

            if not Speed:
                        if GirlA == KittyX:
                            $ Line = GirlA.Name + " begins to rub her chest against you"
                        elif GirlA.Tit > 2:
                            $ Line = GirlA.Name + " begins to bounce her breasts up and down"
                        else:
                            $ Line = GirlA.Name + " squeezes her breasts together and slowly moves them along your shaft"
                        $ Speed = 1
                        $ TempFocus += 12 if Player.Focus < 60 else 6
                        $ TempLust += 6 if GirlA.Lust > 60 else 3
                        return

            if GirlA in (EmmaX,StormX) or (GirlA.Tit > 4 and GirlA.Blow):
                        #5th+ and blown
                        if Speed <= 1:
                            #slow
                            $ Line = renpy.random.choice([GirlA.Name + " rocks her breasts up and down around your cock",
                                    GirlA.Name + " lightly licks the head as it pops up between her tits",
                                    GirlA.Name + " has a smooth motion going now, gentle and precise",
                                    GirlA.Name + " pauses to rub her nipples across the shaft",
                                    "In between strokes "+ GirlA.Name + " gently sucks on the head",
                                    GirlA.Name + " drips some spittle down to make sure you're properly lubed",
                                    GirlA.Name + " gently caresses the shaft between her tits"])

                            $ TempFocus += 15 if Player.Focus < 70 else 5
                            $ TempLust += 7 if GirlA.Lust > 60 else 4
                        else:
                            #fast
                            $ Line = renpy.random.choice([GirlA.Name + " rapidly rocks her breasts up and down around your cock",
                                    GirlA.Name + " licks away at the head every time it pops up between her tits",
                                    GirlA.Name + " has a smooth motion going now, quick by efficient",
                                    GirlA.Name + " dances her nipples across the shaft",
                                    "In as she strokes faster and faster, " + GirlA.Name + " bends down to suck on the head",
                                    GirlA.Name + " covers her tits with drool to keep them well lubed",
                                    GirlA.Name + " rapidly caresses the shaft between her tits"])

                            $ TempFocus += 20 if Player.Focus > 40 else 5
                            $ TempLust += 6 if GirlA.Lust > 70 else 4


            elif GirlA.Tit > 1:
                    #third through 5th time
                    if Speed <= 1:
                        #slow
                        $ Line = renpy.random.choice([GirlA.Name + " juggles her breasts up and down around your cock",
                                GirlA.Name + " lightly strokes the head as it pops up between her tits",
                                GirlA.Name + " has a smooth motion going now, gentle and precise",
                                GirlA.Name + " pauses to rub her nipples across the shaft",
                                GirlA.Name + " gently caresses the shaft between her tits"])

                        $ TempFocus += 15 if Player.Focus < 60 else 5
                        $ TempLust += 6 if GirlA.Lust > 60 else 3
                    else:
                        #fast
                        $ Line = renpy.random.choice([GirlA.Name + " rapidly juggles her breasts up and down around your cock",
                            GirlA.Name + " lightly brushes the head with her chin as it pops up between her tits",
                            GirlA.Name + " moves them up and down in a fluid rocking motion",
                            GirlA.Name + " bounces her whole body up and down",
                            GirlA.Name + " rapidly slides the shaft between her tits"])

                        $ TempFocus += 15 if Player.Focus > 50 else 7
                        $ TempLust += 6 if GirlA.Lust > 60 else 4

            else:
                    #First and second time
                    if Speed <= 1:
                        #slow
                        $ Line = renpy.random.choice([GirlA.Name + " sort of squishes her breasts back and forth around your cock",
                            GirlA.Name + " slides the cock up and down between her cleavage",
                            GirlA.Name + " kind of bounces her tits around your cock",
                            GirlA.Name + " smooshes her cleavage as tight as she can and rubs up and down"])

                        $ TempFocus += 12 if Player.Focus < 60 else 6
                        $ TempLust += 6 if GirlA.Lust > 60 else 3

                    else:
                        #fast
                        $ Line = renpy.random.choice([GirlA.Name + " sort of bounces her breasts off your cock",
                            GirlA.Name + " tries to quickly slide the cock up and down between her cleavage, but it tends to slide out",
                            GirlA.Name + " slaps her tits against your dick",
                            GirlA.Name + " smooshes her cleavage as tight as she can and rubs up and down quite quickly"])

                        $ TempFocus += 8 if Player.Focus > 70 else 4
                        $ TempLust += 5 if GirlA.Lust > 60 else 3

            if GirlA == KittyX:
                    $ TempFocus -= 2
            elif GirlA in (EmmaX,StormX):
                    $ TempFocus += 1

            $ GirlA.Addict -= 2
    #End Action Titfuck ///////////////////////////////////////////////////////////////////////////////


    elif Trigger == "blow":
            if not Speed:
                    #if Rog*ue is not moving
                    if "hungry" in GirlA.Traits:
                            $ GirlA.FaceChange("sly")
                            $ Line = GirlA.Name + " stares at your cock. She licks her lips in anticipation"
                            $ TempLust += 3 if GirlA.Lust < 40 else 1
                    elif GirlA.Blow > 2:
                            $ GirlA.FaceChange("sly")
                            $ Line = GirlA.Name + " stares at your cock. She seems pretty excited about it"
                            $ TempLust += 2 if GirlA.Lust < 60 else 0
                    elif GirlA == EmmaX:
                            $ GirlA.FaceChange("sly")
                            $ Line = GirlA.Name + " stares at your cock. She seems pretty intrigued by it"
                            $ TempLust += 2 if GirlA.Lust < 60 else 0
                    else:
                            $ GirlA.FaceChange("perplexed")
                            $ Line = GirlA.Name + " stares at your cock with trepidation"
                            $ TempLust += 2 if GirlA.Lust < 40 else 0

                    if GirlA.Blow <= 1 or (GirlA.Obed >= 500 and GirlA.Obed > GirlA.Inbt):
                            $ TempLust += 2 if GirlA.Lust > 60 else 0
                            $ Line = Line + ", but she seems to be waiting for some instruction"
                    else:
                            $ Line = Line + ", and then she gets started licking your cock"
                            $ Speed = 1
                    return

            elif Speed < 2:
                        $ Line = GirlA.Name + " continues to lick your cock. "
                        #if Rog*ue is the primary but is licking
            else:
                        $ Line = GirlA.Name + " continues to suck your cock. "
                        #if Rog*ue is the primary and is heading or sucking

            if Speed == 1:
                    #Speed 1 (licking)
                    if GirlA.Blow > 4 or GirlA in (EmmaX,LauraX,StormX):
                            #After the 5th time
                            $ Line = Line + renpy.random.choice(["Her deft licks are masterful, your cock twitches with each stroke",
                                    "She gently blows across the head as she covers your cock in smooth licks",
                                    "How many licks to the center of your cock? No way you're finding out",
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She's really getting good at this, alternating between deep suction and gentle licks",
                                    "She moves very smoothly, tongue dancing casually and very gently, like she's been doing this for years",
                                    "She puts the tip into her mouth and her tounge dances around it"])
                            $ TempFocus += 20 if Player.Focus < 70 else 15
                            $ TempLust += 2 if GirlA.Lust > 80 else 1

                    elif GirlA.Blow > 1:
                            #After the 2nd time
                            $ Line = Line + renpy.random.choice(["She's begining to figure things out, her tongue makes your hair stand on end",
                                    "She's still learning, but learning fast. She seems eager to use her mouth for more than talk",
                                    "She's settled into a gentle licking pace that washes over you like a warm bath",
                                    "She licks gently up and down the shaft. She's a little rough at this, but at least she tries",
                                    "Her tongue moves carefully along the shaft",
                                    "She's really starting to learn some clever tricks to making you feel good",
                                    "She licks her way down the shaft, and gently teases the balls"])
                            $ TempFocus += 20 if Player.Focus > 60 else 10
                            $ TempLust += 2 if GirlA.Lust > 80 else 1

                    else:
                            #First and second time
                            $ Line = Line + renpy.random.choice([GirlA.Name + " makes up for her inexperience with determination, carefully licking your cock",
                                    "She takes a small lick and grimaces at the taste",
                                    "She tentatively kisses around the head a bit",
                                    "She nibbles one of your balls, but stops when you wince",
                                    "She licks all over your dick, but she doesn't really have a handle on it"])
                            $ TempFocus += 15 if Player.Focus > 60 else 5
                    $ GirlA.Addict -= 2

            elif Speed == 2:
                    #Speed 2 (heading)
                    if GirlA.Blow > 4 or GirlA in (EmmaX,LauraX,StormX):
                            #After the 5th time
                            $ Line = Line + renpy.random.choice(["She masterfully bobs on your cock, and it twitches with each stroke",
                                    "She rapidly bobs up and down on your cock, a frenzy of motion",
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She's really getting good at this, alternating between deep suction and quick licks across the head",
                                    "She moves very smoothly, bobbing in and out like she's been doing this for years",
                                    "She puts the tip into her mouth and her tounge swirls rapidly around it"])
                            $ TempFocus += 20 if Player.Focus < 80 else 10
                            $ TempLust += 2 if GirlA.Lust > 70 else 1

                    elif GirlA.Blow > 1:
                            #After the 2nd time
                            $ Line = Line + renpy.random.choice(["She's begining to figure things out, she bobs carefully up and down the head",
                                    "She's still learning, but learning fast. She keeps her teeth well clear, aside from a playful nip",
                                    "Her lips envelope you like a warm bath as she bobs in and out",
                                    "She's really starting to learn some clever tricks to making you feel good",
                                    "She rapidly licks her way around the head",
                                    "Her mouth envelopes the head, then she quickly draws it in and draws back with a pop"])
                            $ TempFocus += 15 if Player.Focus > 80 else 10
                            $ TempLust += 1 if GirlA.Lust > 60 else 0

                    else:
                            # First and second time
                            $ Line = Line + renpy.random.choice(["She really wasn't prepared for speeding up, and your cock often pops out of her mouth",
                                    "She puts the tip in her mouth and starts to actually suck in as hard as she can. She's a little rough at this, but at least she tries",
                                    "Her head bobs rapidly, until she goes a bit too deep and starts to gag",
                                    "She lets her teeth get a bit too much action",
                                    "She bobs quickly on your cock, but clamps down a bit too tight for comfort"])
                            $ TempFocus += 9 if Player.Focus > 80 else 3
                    $ GirlA.Addict -= 2

            elif Speed == 3:
                    #Speed 3 (sucking)
                    if GirlA.Blow > 4 or GirlA in (EmmaX,LauraX,StormX):
                            #After the 5th time
                            $ Line = Line + renpy.random.choice(["She masterfully bobs on your cock, and it twitches with each stroke",
                                    "She smoothly bobs up and down on your cock, a frenzy of motion",
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She gobbles you up all the way to the base, then quickly draws out and plunges back in",
                                    "She's really getting good at this, alternating between deep suction and quick licks across the head",
                                    "She moves very smoothly, bobbing in and out like she's been doing this for years",
                                    "She puts the shaft into her mouth and her tounge swirls rapidly around it"])
                            $ TempFocus += 22 if Player.Focus > 40 else 10
                            $ TempLust += 3 if GirlA.Lust > 60 else 1

                    elif GirlA.Blow > 1:
                            #After the 2nd time
                            $ Line = Line + renpy.random.choice(["She's begining to figure things out, she bobs carefully up and down the shaft",
                                    "She's still learning, but learning fast. She keeps her teeth well clear, aside from a playful nip",
                                    "Her lips envelope you like a warm bath as she bobs in and out",
                                    "She slowly draws you in to the base of your cock, then pulls back at the last second",
                                    "She's really starting to learn some clever tricks to making you feel good",
                                    "She rapidly licks her way up and down the shaft as her mouth envelopes you",
                                    "Her mouth envelopes the shaft, then she quickly draws it in and draws back with a pop"])
                            $ TempFocus += 15 if Player.Focus > 50 else 5

                    else:
                            #First and second time
                            $ Line = Line + renpy.random.choice(["She really wasn't prepared for putting it all the way in, and grimaces at the taste",
                                    "She puts the tip in her mouth and starts to actually suck in as hard as she can. She's a little rough at this, but at least she tries",
                                    "She sucks up and down your cock very quickly, but gets a bit dizzy and has to slow down",
                                    "Her head bobs rapidly, until she goes a bit too deep and starts to gag",
                                    "She lets her teeth get a bit too much action",
                                    "She bobs quickly on your cock, but clamps down a bit too tight for comfort"])
                            $ TempFocus += 6 if Player.Focus < 50 else 3
                    $ GirlA.Addict -= 2 if D20S > 10 else 3


            else:#Speed = 4
                    #Speed 4+ (Deep Throat)
                    if GirlA.Blow > 4 or GirlA in (EmmaX,LauraX,StormX):
                            #After the 5th time
                            $ Line = Line + renpy.random.choice(["She masterfully bobs on your cock, and it twitches with each stroke",
                                    "She rapidly bobs to the base of your cock, a frenzy of motion",
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She gobbles you up all the way to the base, then quickly draws out and plunges back in",
                                    "She's really getting good at this, alternating between deep suction and quick licks across the head",
                                    "She moves very smoothly, bobbing in and out like she's been doing this for years",
                                    "She puts the entire shaft into her mouth and her tounge swirls rapidly around it"])
                            $ TempFocus += 25 if Player.Focus > 40 else 8
                            $ TempLust += 3 if GirlA.Lust > 60 else 2

                    elif GirlA.Blow > 1:
                            #After the 2nd time
                            $ Line = Line + renpy.random.choice(["She's begining to figure things out, she bobs carefully up and down the shaft",
                                    "She's still learning, but learning fast. She keeps her teeth well clear, aside from a playful nip",
                                    "Her lips envelope you like a warm bath as she bobs in and out",
                                    "She slowly draws you in to the base of your cock, then pulls back at the last second",
                                    "She's really starting to learn some clever tricks to making you feel good",
                                    "She completely envelops the shaft with her throat.",
                                    "Her mouth envelopes the head, then she quickly draws it all the way in and draws back with a pop"])
                            $ TempFocus += 20 if Player.Focus > 40 else 5
                            $ TempLust += -3 if GirlA.Lust < 60 else -1
                            $ TempLust += 5 if GirlA.Obed > 500 else 0

                    else:
                            #First and second time
                            $ Line = Line + renpy.random.choice(["She really wasn't prepared for going so deep, and gags a bit",
                                    "She puts the whole shaft in her mouth and starts to actually suck in as hard as she can. She's a little rough at this, but at least she tries",
                                    "She draws your cock into her mouth very qucikly, but gets a bit dizzy and has to slow down",
                                    "Her head bobs rapidly, until she goes a bit too deep and starts to gag",
                                    "She lets her teeth get a bit too much action",
                                    "She bobs quickly on your cock, but clamps down a bit too tight for comfort"])
                            $ TempFocus += 15 if Player.Focus > 80 else 5
                            $ TempLust += -5 if GirlA.Lust < 60 else -2
                            $ TempLust += 7 if GirlA.Obed > 500 else 0
                    $ GirlA.Addict -= 3
            $ GirlA.Addict -= 3 if GirlA == JubesX else 0

    # end GirlA.Blowjob                                 //////////////////////////////////////////////////////////////////////////////

    elif Trigger == "sex":
            #Trigger4 not available

            if not Speed:
                    #if Rog*ue is not moving
                    $ Line = "She seems to be waiting for you to do something. . "
                    return

            elif Speed < 2:
                    $ Line = "You continue to pound "+ GirlA.Name + ". "
                    #if Rog*ue is the primary but is licking
            else:
                    $ Line = "You continue to slowly drive into " + GirlA.Name + ". "
                    #if Rog*ue is the primary and is heading or sucking

            if GirlA.Sex > 4 or GirlA in (EmmaX,LauraX,StormX):
                if Speed > 1:
                        # After the 5th time fast
                        $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock",
                            "You thrust into her and she squeaks a bit",
                            "You quickly grind back and forth inside her",
                            "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                            "You pound away at her",
                            "She grinds furiously back and forth along your cock"])
                        $ TempFocus += 18 if Player.Focus > 50 else 12
                        $ TempLust += 16 if GirlA.Lust > 70 else 10
                else:
                        # After the 5th time slow
                        $ Line = Line + renpy.random.choice(["She bumps slowly against your cock",
                            "You thrust into her and she coos a bit",
                            "You slowly grind back and forth inside her",
                            "You alternate between long and slow thrusts, and the occasional quick one",
                            "You slowly slide back and forth near the entrance",
                            "She slides slowly back and forth along your cock, teasing you"])
                        $ TempFocus += 14 if Player.Focus < 60 else 12
                        $ TempLust += 12 if 40 > GirlA.Lust > 90 else 10

            elif GirlA.Sex > 1:
                if Speed > 1:
                    #third through 5th time fast
                    $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock",
                        "You thrust into her and she squeaks a bit",
                        "You quickly grind back and forth inside her",
                        "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                        "You pound away at her",
                        "She grinds furiously back and forth along your cock"])
                    $ TempFocus += 12 if Player.Focus > 50 else 9
                    $ TempLust += 14 if GirlA.Lust > 80 else 10
                else:
                    #third through 5th time slow
                    $ Line = Line + renpy.random.choice(["she bumps slowly against your cock",
                        "You thrust into her and she squeaks a bit",
                        "You slowly grind back and forth inside her",
                        "You alternate between long and slow thrusts, and the occasional quick one",
                        "You slowly slide back and forth near the entrance",
                        "She slides slowly back and forth along your cock"])
                    $ TempFocus += 12 if Player.Focus < 70 else 7
                    $ TempLust += 10 if 50 > GirlA.Lust > 90 else 8

            else:
                if Speed > 1:
                    # First and second time fast
                    $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock",
                        "You thrust into her and she squeeks in pain",
                        "You quickly grind back and forth inside her but she doesn't seem to have the rhythm down",
                        "She bounces rapidly against your cock, occasionally popping out and having to stick it back in",
                        "You pound away at her",
                        "She moves rapidly back and forth along your cock, but seems a bit uncomfortable"])
                    $ TempFocus += 10 if Player.Focus > 60 else 9
                    $ TempLust += 10 if GirlA.Lust > 80 else 6
                else:
                    # First and second time slow
                    $ Line = Line + renpy.random.choice(["She bumps slowly against your cock",
                        "You thrust into her and she squeaks a bit",
                        "You slowly grind back and forth inside her",
                        "You alternate between long and slow thrusts, and the occasional quick one",
                        "You slowly slide back and forth near the entrance",
                        "She slides slowly back and forth along your cock"])
                    $ TempFocus += 10 if Player.Focus < 70 else 9
                    $ TempLust += 8 if 60 > GirlA.Lust > 90 else 6

            $ GirlA.Addict -= 2

    # end GirlA.Sex                                 //////////////////////////////////////////////////////////////////////////////

    elif Trigger == "hotdog":
            #Trigger4 not available
            #TempLust2 in this action is how much lower body clothing she has on, it gets cleared at the end.
            $ TempLust2 = 2
            if GirlA.Panties and not GirlA.PantiesDown:
                    #if panties are in the way
                    $ TempLust2 -= 1
            if GirlA.HoseNum() >= 6:
                    #if complete hose
                    $ TempLust2 -= 1
            if GirlA.Legs and not GirlA.Upskirt:
                    #If pants/skirt is up
                    $ TempLust2 -= 2 if TempLust2 <= 2 else TempLust2

            if not Speed:
                $ Line = "She seems to be waiting for you to do something. . "
                return
            elif Speed < 2:
                    $ Line = "You continue to hotdog " + GirlA.Name + ". "
            else:
                    $ Line = "You continue to grind against " + GirlA.Name + ". "

            if GirlA.Hotdog >= 2:
                if Speed > 1:
                    # After the 2ndtime fast
                    $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock",
                        "You thrust against her and she squeaks a bit",
                        "You quickly grind back and forth along her crack",
                        "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                        "You grind away at her",
                        "She grinds furiously back and forth along your cock"])
                    $ TempFocus += (TempLust2 + 8) if Player.Focus < 60 else (TempLust2 + 4)
                    $ TempLust += (TempLust2 + 8) if 50 > GirlA.Lust > 80 else (TempLust2 + 2)

                elif Speed:
                    #2nd time slow
                    $ Line = Line + renpy.random.choice(["She grinds slowly against your cock",
                        "You thrust against her and she coos a bit",
                        "You slowly rub the tip across her pussy",
                        "You alternate between long and slow thrusts, and the occasional rapid ones",
                        "You slowly slide back and forth near her rim",
                        "She slides slowly back and forth along your cock, teasing you"])
                    $ TempFocus += (TempLust2 + 8) if Player.Focus < 60 else (TempLust2 + 3)
                    $ TempLust += (TempLust2 + 7) if 30 > GirlA.Lust > 70 else (TempLust2 + 3)

            else:
                #If you haven't done hotdog before
                if Speed > 1:
                    #fast
                    $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock",
                        "You thrust against her and she squeeks in surprise",
                        "You quickly grind back and forth against her but she doesn't seem to have the rhythm down",
                        "She bounces rapidly against your cock",
                        "You pound away at her",
                        "She slides rapidly back and forth along your cock, but seems a bit uncomfortable"])
                    $ TempFocus += (TempLust2 + 5) if Player.Focus < 60 else (TempLust2 + 3)
                    $ TempLust += (TempLust2 + 4) if 50 > GirlA.Lust > 80 else (TempLust2 + 2)

                elif Speed:
                    #slow
                    $ Line = Line + renpy.random.choice(["She grinds slowly against your cock",
                        "You thrust into her crack and she squeaks a bit",
                        "You slowly grind back and forth across her rear",
                        "You slowly slide back and forth near her rim",
                        "She slides slowly back and forth along your cock"])
                    $ TempFocus += (TempLust2 + 5) if Player.Focus < 60 else (TempLust2 + 3)
                    $ TempLust += (TempLust2 + 5) if 50 > GirlA.Lust > 70 else (TempLust2 + 2)

            if TempLust2:
                $ GirlA.Addict -= 1
                $ TempLust2 = 0

    # end GirlA.Hotdog                                 //////////////////////////////////////////////////////////////////////////////


    elif Trigger == "anal":
            #Trigger4 not available

            if not Speed:
                $ Line = "She seems to be waiting for you to do something. . "
                return

            elif Speed < 2:
                    $ Line = "You continue to pound into " + GirlA.Name + "'s ass. "
            else:
                    $ Line = "You continue to push into " + GirlA.Name + "'s ass. "


            if GirlA.Anal >= 5:
                    if Speed > 1:
                            #Fast
                            $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock",
                                "You thrust into her and she squeaks a bit",
                                "You quickly grind back and forth inside her",
                                "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                                "You pound away at her",
                                "She grinds furiously back and forth along your cock"])
                            $ TempFocus += 18 if Player.Focus > 60 else 12
                            $ TempLust += 14 if GirlA.Lust > 80 else 9

                    else:
                            #Slow
                            $ Line = Line + renpy.random.choice(["She bumps slowly against your cock",
                                "You thrust into her and she coos a bit",
                                "You slowly grind back and forth inside her",
                                "You alternate between long and slow thrusts, and the occasional quick one",
                                "You slowly slide back and forth near the rim",
                                "She slides slowly back and forth along your cock, teasing you"])
                            $ TempFocus += 12 if Player.Focus > 60 else 9
                            $ TempLust += 12 if 50 < GirlA.Lust < 90 else 8

            elif GirlA.Loose:
                    #You've done some anal stuff before
                    if Speed > 1:
                            #third through 5th time fast
                            $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock",
                                "You thrust into her and she squeaks a bit",
                                "You quickly grind back and forth inside her",
                                "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                                "You pound away at her",
                                "She grinds furiously back and forth along your cock"])
                            $ TempFocus += 12 if Player.Focus > 60 else 8
                            $ TempLust += 12 if GirlA.Lust > 80 else 6

                    elif Speed:
                            #third through 5th time
                            $ Line = Line + renpy.random.choice(["She bumps slowly against your cock",
                                "You thrust into her and she squeaks a bit",
                                "You slowly grind back and forth inside her",
                                "You alternate between long and slow thrusts, and the occasional quick one",
                                "You slowly slide back and forth near the rim",
                                "She slides slowly back and forth along your cock"])
                            $ TempFocus += 13 if Player.Focus > 60 else 8
                            $ TempLust += 8 if 70 > GirlA.Lust > 90 else 4

            else:
                    #If you haven't done anal things before
                    if Speed > 1:
                            #fast
                            $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock but seems to be in pain",
                                "You thrust into her and she squeeks in pain",
                                "You quickly grind back and forth inside her but she doesn't seem to have the rhythm down",
                                "She bounces rapidly against your cock, occasionally popping out and having to stick it back in",
                                "You pound away at her",
                                "She moves rapidly back and forth along your cock, but seems a bit uncomfortable"])
                            $ TempFocus += 10 if Player.Focus > 60 else 8
                            $ TempLust += 2 if GirlA.Lust > 80 else -3

                    elif Speed:
                            #heading
                            $ Line = Line + renpy.random.choice(["She grits her teeth and slides slowly against your cock",
                                "You thrust into her and she squeaks a bit",
                                "You slowly grind back and forth inside her",
                                "You slowly slide back and forth near the rim",
                                "She slides slowly back and forth along your cock"])
                            $ TempFocus += 10 if Player.Focus > 60 else 6
                            $ TempLust += 4 if GirlA.Lust > 60 else -1

            if GirlA.Loose > 1:
                #If she's extra loose
                $ TempLust += 1

            $ GirlA.Addict -= 3
            $ TempLust = 0 if (GirlA.Lust - TempLust) < 0 else TempLust

    # end GirlA.Anal                                 //////////////////////////////////////////////////////////////////////////////

    elif Trigger == "fondle breasts":
                    $ Line = "You continue to fondle " + GirlA.Name + ". "
                    if not GirlA.Uptop and GirlA.Over and GirlA.Chest:
                                #Full top
                                $ Line = Line + renpy.random.choice(["You reach under her layers of clothing and massage her breasts",
                                    "You pass your hands gently over her warm breasts",
                                    "Her firm nipples catch on the fabric of her top as you grasp her warm flesh",
                                    "She gasps as you grasp her under her top"])
                                $ TempFocus += 2 if Player.Focus < 40 else 1
                                $ TempLust += 4 if GirlA.Lust > 50 else 2
                    elif not GirlA.Uptop and GirlA.Over:
                                #Just overtop
                                $ Line = Line + renpy.random.choice(["You reach under her top and massage her breasts",
                                    "You pass your hands gently over her warm breasts",
                                    "Her nipples catch on the fabric of her top as you grasp her warm flesh, you can see them stiffen",
                                    "She gasps as you grasp her under her " + GirlA.Over])
                                $ TempFocus += 2 if Player.Focus < 50 else 1
                                $ TempLust += 4 if GirlA.Lust > 50 else 2
                    elif not GirlA.Uptop and GirlA.Chest:
                                #just bra
                                $ Line = Line + renpy.random.choice(["You reach under her " + GirlA.Chest + " and massage her breasts",
                                    "You pass your hands gently over her warm breasts",
                                    "Her nipples catch on the fabric of her " + GirlA.Chest + " as you grasp her warm flesh, you can see them stiffen",
                                    "She gasps as you grasp her under her " + GirlA.Chest])
                                $ TempFocus += 3 if Player.Focus < 60 else 2
                                $ TempLust += 5 if GirlA.Lust > 50 else 2
                    elif GirlA.Pierce:
                                #pierced
                                $ Line = Line + renpy.random.choice(["You reach out and massage her glorious breasts",
                                    "You pass your hands gently over her warm breasts, and blow across her pierced nipples",
                                    "Her piercings catch lightly on your fingers as you grasp her warm flesh, you can see the nipples stiffen",
                                    "She gasps as you lightly thumb across her pierced nipples"])
                                $ TempFocus += 4 if Player.Focus < 70 else 2
                                $ TempLust += 6 if GirlA.Lust > 40 else 4
                    else: #topless
                                $ Line = Line + renpy.random.choice(["You reach out and massage her glorious breasts",
                                    "You pass your hands gently over her warm breasts, and blow across her nipples",
                                    "Her nipples catch lightly on your fingers as you grasp her warm flesh, you can see them stiffen",
                                    "She gasps as you lightly thumb her rigid nipples"])
                                $ TempFocus += 4 if Player.Focus < 60 else 2
                                $ TempLust += 6 if GirlA.Lust > 50 else 3
                    if D20S > 18:
                            if GirlA == KittyX:
                                    $ Line = "You continue to fondle " + GirlA.Name + ". They fit comfortably into your palms."
                            elif GirlA in (EmmaX,StormX):
                                    $ Line = "You continue to fondle " + GirlA.Name + ". You can barely wrap your hands around them."
                    $ GirlA.Addict -= 2

    # end Fondle breasts                                 //////////////////////////////////////////////////////////////////////////////
    elif Trigger == "suck breasts":
                    $ Line = "You continue to suck on " + GirlA.Name + "'s breasts. "
                    if not GirlA.Uptop and GirlA.Over and GirlA.Chest:
                                #Full top
                                $ Line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                        "You gently nibble at her nipples as you suck on them through the layered tops",
                                        "You  place a nipple between your lips, and give it a quick tug through the " + GirlA.Over,
                                        "She gasps as you gently nibble her rigid nipples poking through her tops"])
                                $ TempFocus += 2 if Player.Focus < 50 else 1
                                $ TempLust += 2 if GirlA.Lust < 30 else 1
                    elif not GirlA.Uptop and GirlA.Over:
                                #Just overtop
                                $ Line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                        "You gently nibble at her nipples as you suck on them through the " + GirlA.Over,
                                        "You tease her nipples with your tongue through the fabric",
                                        "You slowly lick her nipples through her moist top",
                                        "You gently place a nipple between your lips, and draw it out until it releases with a *pop*",
                                        "She gasps as you lightly lick her rigid nipples, poking through her top"])
                                $ TempFocus += 2 if Player.Focus < 50 else 1
                                $ TempLust += 5 if GirlA.Lust > 50 else 3
                    elif not GirlA.Uptop and GirlA.Chest:
                                #just bra
                                $ Line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                        "You tease her nipples with your tongue through her " + GirlA.Chest,
                                        "You slowly lick her nipples through her moist " + GirlA.Chest,
                                        "You gently place a nipple between your lips, and draw it out until it releases with a *pop*",
                                        "She gasps as you lightly lick her rigid nipples, poking through her " + GirlA.Chest])
                                $ TempFocus += 4 if Player.Focus < 60 else 3
                                $ TempLust += 5 if GirlA.Lust > 50 else 2
                    elif GirlA.Pierce:
                                #pierced
                                $ Line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                    "You gently nibble at her nipples as you suck on them",
                                    "You tease her piercings with your tongue",
                                    "You slowly lick around, and then blow across her nipples",
                                    "You gently place a pierced nipple between your lips, and draw it out until it releases with a *pop*",
                                    "She gasps as you lightly lick her rigid nipples"])
                                $ TempFocus += 5 if Player.Focus < 70 else 4
                                $ TempLust += 10 if GirlA.Lust > 40 else 7
                                $ GirlA.Addict -= 2
                    else: #topless
                                $ Line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                    "You gently nibble at her nipples as you suck on them",
                                    "You tease her nipples with your tongue",
                                    "You slowly lick around, and then blow across her nipples",
                                    "You gently place a nipple between your lips, and draw it out until it releases with a *pop*",
                                    "She gasps as you lightly lick her rigid nipples"])
                                $ TempFocus += 5 if Player.Focus < 60 else 3
                                $ TempLust += 10 if GirlA.Lust > 50 else 7
                                $ GirlA.Addict -= 2

    # end Suck breasts                                 //////////////////////////////////////////////////////////////////////////////

    elif Trigger == "fondle thighs":  #Trigger4 not available
                    $ Line = "You continue to massage " + GirlA.Name + "'s thighs. "

                    if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                #she's wearing pants of some sort. . .
                                $ Line = renpy.random.choice(["Her legs twitch a bit in her pants as you caress them",
                                        "She gasps as you stroke her warm thighs through the pants",
                                        "You draw your hand from her knee to mid-thigh, and she gasps a little",
                                        "You slide a hand up her inner thigh, to just below her . . ."])
                                $ TempFocus += 1 if Player.Focus < 50 else 0
                                $ TempLust += 1 if GirlA.Lust < 50 else 0
                    elif GirlA.PantsNum() == 5 and GirlA.HoseNum() >= 5:
                                # skirt with full hose
                                $ Line = renpy.random.choice(["You reach under skirt and stroke her thighs",
                                        "You lift her skirt a bit and feel her firm thighs",
                                        "Her legs twitch a bit beneath her skirt",
                                        "She gasps as you stroke her lightly covered thighs",
                                        "You slide a hand up her inner thigh, to just below her . . "])
                                $ TempFocus += 2 if Player.Focus < 40 else 0
                                $ TempLust += 2 if GirlA.Lust < 40 else 0
                                $ GirlA.Addict -= 1 if D20S > 10 else 0
                    elif GirlA.PantsNum() == 5 and GirlA.Hose:
                                #skirt with stockings
                                $ Line = renpy.random.choice(["You reach under skirt and stroke her thighs",
                                        "You lift her skirt a bit and feel her firm thighs",
                                        "Her legs twitch a bit beneath her skirt",
                                        "She gasps as you stroke her warm thighs",
                                        "You slide a hand up her inner thigh, to just above the hose"])
                                $ TempFocus += 2 if Player.Focus < 50 else 0
                                $ TempLust += 2 if GirlA.Lust < 50 else 0
                                $ GirlA.Addict -= 1 if D20S > 10 else 0
                    elif GirlA.PantsNum() == 5:
                                #skirt and no hose
                                $ Line = renpy.random.choice(["You reach under skirt and stroke her thighs",
                                        "You lift her skirt a bit and feel her firm thighs",
                                        "Her legs twitch a bit beneath her skirt",
                                        "She gasps as you stroke her warm thighs",
                                        "You draw your hand from her knee to mid-thigh, and she gasps a little",
                                        "You slide a hand up her inner thigh, to just her skirt"])
                                $ TempFocus += 2 if Player.Focus < 50 else 0
                                $ TempLust += 2 if GirlA.Lust < 50 else 0
                                $ GirlA.Addict -= 2 if D20S > 10 else 1
                    elif GirlA.HoseNum() >= 5:
                                # just hose
                                $ Line = renpy.random.choice(["You reach out and stroke her lightly covered thighs",
                                        "You lift her leg a bit and feel her firm thighs",
                                        "Her legs twitch a bit beneath your hands",
                                        "She gasps as you stroke her warm thighs",
                                        "You slide a hand up her inner thigh, the smooth faberic creasing",
                                        "You slide a hand up her inner thigh, to just below her. . "])
                                $ TempFocus += 2 if Player.Focus < 40 else 0
                                $ TempLust += 2 if GirlA.Lust < 40 else 0
                                $ GirlA.Addict -= 1 if D20S > 10 else 0
                    elif GirlA.Hose:
                                #just stockings
                                $ Line = renpy.random.choice(["You reach out and stroke her thighs",
                                        "You lift her leg a bit and feel her firm thighs",
                                        "Her legs twitch a bit beneath your hands",
                                        "She gasps as you stroke her warm thighs",
                                        "You slide a hand up her inner thigh, to just above the hose",
                                        "You slide a hand up her inner thigh, to just below her. . "])
                                $ TempFocus += 2 if Player.Focus < 50 else 0
                                $ TempLust += 2 if GirlA.Lust < 50 else 0
                                $ GirlA.Addict -= 1 if D20S > 10 else 0
                    else: #nude legs
                                $ Line = renpy.random.choice(["You reach out and stroke her thighs",
                                        "You lift her leg a bit and feel her firm thighs",
                                        "Her legs twitch a bit beneath your hands",
                                        "She gasps as you stroke her warm thighs",
                                        "You draw your hand from her knee to mid-thigh, and she gasps a little",
                                        "You slide a hand up her inner thigh, to just below her. . "])
                                $ TempFocus += 2 if Player.Focus < 50 else 0
                                $ TempLust += 2 if GirlA.Lust < 50 else 0
                                $ GirlA.Addict -= 2 if D20S > 10 else 1

    # end fondle thighs                               //////////////////////////////////////////////////////////////////////////////


    elif Trigger == "fondle pussy":
                    if Speed == 2 and D20S <= 10:
                            $ Line = renpy.random.choice(["You continue to finger " + GirlA.Name + "'s pussy. ",
                                                    "You continue to finger bang " + GirlA.Name + "'s pussy. ",
                                                    "You continue to finger blast " + GirlA.Name + "'s pussy. "])

                            if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                            #pants
                                            $ Line = renpy.random.choice(["You slide a hand down her pants, and slide your fingers into her pussy underneath",
                                                    "You push her panties aside, and slide a finger between her lips",
                                                    "You slide a finger into her pussy and stroke the top",
                                                    "You pull her pants out a bit and she gasps as you slide two fingers between her lips",
                                                    "You rub her clit with your palm as you dive into her pussy with your middle finger"])
                            elif GirlA.PantsNum() == 5:
                                    if GirlA.Panties and not GirlA.PantiesDown:
                                            #Just panties
                                            $ Line = renpy.random.choice(["You push her skirt and " + GirlA.Panties + " aside, and slide a finger between her lips",
                                                    "You slide a finger under her " + GirlA.Panties + " and stroke the top or her pussy",
                                                    "You lift her skirt a bit and she gasps as you pull her " + GirlA.Panties + " aside and slide two fingers between her lips",
                                                    "You rub her clit with your thumb as you dive into her pussy with your middle finger"])
                                    else: #skirt, but nothing else
                                            $ Line = renpy.random.choice(["You push her skirt aside, and slide a finger between her lips",
                                                    "You slide a finger into her pussy and stroke the top",
                                                    "You lift her skirt a bit and she gasps as you slide two fingers between her lips",
                                                    "You rub her clit with your thumb as you dive into her pussy with your middle finger"])
                                            $ TempFocus += 2
                                            $ TempLust += 2
                            #no skirt or pants
                            elif (GirlA.PantsNum() == 6 or (GirlA == RogueX and GirlA.Panties == "shorts")) and not GirlA.PantiesDown:
                                        # just shorts on
                                        $ Line = renpy.random.choice(["You slide a hand down her shorts, and slide your fingers into her pussy underneath",
                                                "You push her shorts up, and slide a finger between her lips",
                                                "You slide a finger along her pussy and stroke to the top",
                                                "You pull her shorts out a bit and she gasps as you slide two fingers between her lips",
                                                "You rub her clit with your palm as you dive into her pussy with your middle finger"])
                            elif GirlA.Panties and not GirlA.PantiesDown:
                                        #Just panties
                                        $ Line = renpy.random.choice(["You push her panties aside, and slide a finger between her lips",
                                                "You slide a finger along her pussy and stroke to the top",
                                                "You lift her panties a bit and she gasps as you slide two fingers between her lips"])
                            else: #nothing
                                        $ Line = renpy.random.choice(["You reach out and slide a finger between her lips",
                                                "You slide a finger along her pussy and stroke to the top",
                                                "You lift her lips a bit and she gasps as you slide two fingers between them",
                                                "You rub her clit with your thumb as you dive into her pussy with your middle finger"])
                                        $ TempFocus += 2
                                        $ TempLust += 2

                            $ TempFocus += 4 if Player.Focus < 50 else 3
                            $ TempLust += 6 if GirlA.Lust > 40 else 3
                            $ GirlA.Addict -= 2

                    else: #if not fingerblasting or not high rolls
                            $ Line = renpy.random.choice(["You continue to stroke " + GirlA.Name + "'s pussy. ",
                                                    "You continue to rub " + GirlA.Name + "'s pussy. ",
                                                    "You continue to caress " + GirlA.Name + "'s pussy. "])

                            if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                            #pants on
                                            $ Line = renpy.random.choice(["You reach out and brush your hands across her pussy through the pants",
                                                    "You slide a hand down her pants, and brush your hands across her pussy underneath",
                                                    "You put your hand against her mound and grind against it",
                                                    "You reach into her gap and she gasps as you slide your hand across and stroke her warm mound",
                                                    "As you dig your thumb into her, she gasps and raises up a bit",
                                                    "She gasps as you reach under her and lightly stroke her ass through the pants",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])

                            elif GirlA.PantsNum() == 5:
                                    if GirlA.Panties == "shorts" and not GirlA.PantiesDown:
                                            #shorts on
                                            $ Line = renpy.random.choice(["You reach under skirt and ran your hands over the thin shorts covering her",
                                                    "You slide a hand up the leg of her shorts, and brush your hands across her pussy underneath",
                                                    "You put your hand against her mound and grind against it",
                                                    "You reach into her gap and she gasps as you slide your hand across and stroke her warm mound",
                                                    "As you dig your thumb into her, she gasps and raises up a bit",
                                                    "She gasps as you reach under her and lightly stroke her ass through the thin shorts",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                                    elif GirlA.Panties and not GirlA.PantiesDown: #Just panties
                                            $ Line = renpy.random.choice(["You reach under skirt and brush across her panties",
                                                    "You lift her skirt a bit and grind against her panties",
                                                    "You lift her skirt a bit and she gasps as you pull her panties aside and stroke her lips",
                                                    "Her legs twitch a bit beneath her skirt as you press your thumb against her",
                                                    "She gasps as you rub her pussy through her panties",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                                    elif GirlA.HoseNum() >= 5:
                                            #just hose
                                            $ Line = renpy.random.choice(["You reach out and brush your hands across her cleft through the thin fabric",
                                                    "You grab her hose and pull them taut, elliciting a small gasp",
                                                    "You put your hand against her mound and grind against it",
                                                    "You reach into her gap and she gasps as you slide your hand across and stroke her lips through the thin material",
                                                    "Her legs twitch a bit as you press your thumb against her",
                                                    "She gasps as you reach under her hose and lightly stroke her ass",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                                    else: #skirt, but nothing else
                                            $ Line = renpy.random.choice(["You reach under skirt and brush across her bare lips",
                                                    "You lift her skirt a bit and grind against her warm mound",
                                                    "You lift her skirt a bit and she gasps as you stroke her moist lips",
                                                    "Her legs twitch a bit beneath her skirt as you press your thumb against her"
                                                    "She gasps as you rub her bare pussy",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                                            if D20S <= 10:
                                                $ TempFocus += 3 if Player.Focus < 50 else 1
                                                $ TempLust += 4 if GirlA.Lust > 40 else 2
                                                $ GirlA.Addict -= 2
                                            else: #If it touches skin
                                                $ TempFocus += 1
                                                $ TempLust += 1

                            #no skirt or pants
                            elif (GirlA.PantsNum() == 6 or (GirlA == RogueX and GirlA.Panties == "shorts")) and not GirlA.PantiesDown:
                                        # just shorts on
                                        $ Line = renpy.random.choice(["You reach out and brush your hands across her pussy through the shorts",
                                                "You slide a hand down her shorts, and brush your hands across her pussy underneath",
                                                "You put your hand against her mound and grind against it",
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her warm mound",
                                                "As you dig your thumb into her, she gasps and raises up a bit",
                                                "She gasps as you reach under her and lightly stroke her ass through the thin shorts",
                                                "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                            elif GirlA.Panties and not GirlA.PantiesDown:
                                        #Just panties
                                        $ Line = renpy.random.choice(["You reach out and brush your hands across her panties",
                                                "You grab her panties and pull them taut, elliciting a small gasp",
                                                "You put your hand against her mound and grind against it",
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her lips through the thin material",
                                                "Her legs twitch a bit as you press your thumb against her",
                                                "She gasps as you reach under her panties and lightly stroke her ass",
                                                "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                            elif GirlA.HoseNum() >= 5:
                                        #just hose
                                        $ Line = renpy.random.choice(["You reach out and brush your hands across her cleft through the thin fabric",
                                                "You grab her hose and pull them taut, elliciting a small gasp",
                                                "You put your hand against her mound and grind against it",
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her lips through the thin material",
                                                "Her legs twitch a bit as you press your thumb against her",
                                                "She gasps as you reach under her hose and lightly stroke her ass",
                                                "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                            else: #nothing
                                        $ Line = renpy.random.choice(["You reach out and brush your hands across her bare lips",
                                                "You put your hand against her mound and grind against it",
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her lips",
                                                "Her legs twitch a bit as you press your thumb against her",
                                                "She gasps as you reach under her and lightly stroke her ass",
                                                "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                                        if D20S <= 10:
                                            $ TempFocus += 3 if Player.Focus < 50 else 1
                                            $ TempLust += 4 if GirlA.Lust > 40 else 2
                                            $ GirlA.Addict -= 2
                                        else: #If it touches skin
                                            $ TempFocus += 1
                                            $ TempLust += 1

                            if D20S > 10:#If it touches skin
                                $ TempFocus += 3 if Player.Focus < 50 else 1
                                $ TempLust += 4 if GirlA.Lust > 40 else 2
                                $ GirlA.Addict -= 2
                            else:
                                $ TempFocus += 2 if Player.Focus < 50 else 1
                                $ TempLust += 2 if GirlA.Lust > 40 else 1
                            if GirlA.Pierce and D20S <= 3:
                                    "You tug on her piercing with your thumb, then let it snap back"


    # end fondle pussy                               /////////////////////////////////////////////////////////////////////////////


    elif Trigger == "lick pussy":
                            $ Line = renpy.random.choice(["You continue to lick " + GirlA.Name + "'s pussy. ",
                                                    "You continue to suck " + GirlA.Name + "'s pussy. ",
                                                    "You continue to tongue " + GirlA.Name + "'s pussy. "])

                            if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                            $ Line = renpy.random.choice(["You can feel her twitching as you grind your tongue against her, even through the thick material",
                                                    "She gasps as you press on her clit through the thick fabric",
                                                    "You rub her clit with your nose as you dive into her pussy with your tongue",
                                                    "You put your hand against her mound and lick the surface of her pants",
                                                    "With a little nibble, you tug at the denim",
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])
                                            $ TempFocus += 1 if Player.Focus < 70 else 0
                                            $ TempLust += 3 if GirlA.Lust > 60 else 2
                            else:
                                if GirlA.PantsNum() == 5:
                                        if GirlA.Panties == "shorts" and not GirlA.PantiesDown:
                                                #shorts on
                                                $ Line = renpy.random.choice(["You push her skirt up and lick at her pussy through her shorts",
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
                                                $ Line = renpy.random.choice(["You push her skirt up and lick at her pussy through her panties",
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
                                               $ Line = renpy.random.choice(["You push her skirt up and lick at her pussy through her hose",
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
                                                $ Line = renpy.random.choice(["You push her skirt aside and stroke her lips with your tongue",
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
                                                    $ TempLust += 4 if GirlA.Lust > 60 else 2
                                                    $ GirlA.Addict -= 3
                                                else: #If it touches skin
                                                    $ TempFocus += 1
                                                    $ TempLust += 1

                                #no skirt or pants
                                elif (GirlA.PantsNum() == 6 or (GirlA == RogueX and GirlA.Panties == "shorts")) and not GirlA.PantiesDown:
                                            # just shorts on
                                            $ Line = renpy.random.choice(["You bend down and lick the edges of her lips through her shorts",
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
                                            $ Line = renpy.random.choice(["You bend down and stroke the edges of her panties with your tongue",
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
                                            $ Line = renpy.random.choice(["You bend down and stroke her lips with your tongue",
                                                    "You spread the lips back beneath her hose, and she gasps as you slide your tongue across them",
                                                    "You can feel her twitching as you grind your tongue against her clit",
                                                    "She gasps as you suck on her clit through the thin fabric",
                                                    "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                    "You put your hand against her mound and lick the juice from her thin hose",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the walls aside",
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])
                                else: #nothing
                                            $ Line = renpy.random.choice(["You bend down and stroke her lips with your tongue",
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
                                                $ TempLust += 4 if GirlA.Lust > 60 else 2
                                                $ GirlA.Addict -= 3
                                            else: #If it touches skin
                                                $ TempFocus += 1
                                                $ TempLust += 1

                                if D20S > 10: #If it touches skin
                                    $ TempFocus += 4 if Player.Focus < 70 else 1
                                    $ TempLust += 10 if GirlA.Lust > 60 else 5
                                    $ GirlA.Addict -= 3
                                else:
                                    $ TempFocus += 2 if Player.Focus < 50 else 1
                                    $ TempLust += 5 if GirlA.Lust > 60 else 3
                                if GirlA.Pierce and D20S <= 3:
                                        "You tug on her piercing with your teeth, then let it snap back"

    # end lick pussy                               /////////////////////////////////////////////////////////////////////////////

    elif Trigger == "fondle ass":
                        $ Line = renpy.random.choice(["You continue to fondle " + GirlA.Name + "'s ass. ",
                                                "You continue to feel up " + GirlA.Name + "'s ass. ",
                                                "You continue to grope " + GirlA.Name + "'s ass. "])

                        if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                        $ Line = renpy.random.choice(["You reach out and brush your hands across the back of her pants",
                                                "You slide a hand down her pants, and firmly cup her ass",
                                                "You put your hand against her rear and grind against it",
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her warm mound",
                                                "As you dig your thumb into her, she gasps and raises up a bit",
                                                "She gasps as you reach under her and lightly stroke her ass through the pants",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])

                        elif GirlA.PantsNum() == 5:
                                # skirt
                                if GirlA.Panties == "shorts" and not GirlA.PantiesDown:
                                        #shorts on
                                        $ Line = renpy.random.choice(["You reach under skirt and brush across her shorts",
                                                "You lift her skirt a bit and grind against her shorts",
                                                "You lift her skirt a bit and she gasps as you pull her shorts aside and stroke across her butt",
                                                "Her legs twitch a bit beneath her skirt as you give her cheeks a firm squeeze",
                                                "She gasps as you stroke her asshole through her shorts",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
                                elif GirlA.Panties and not GirlA.PantiesDown:
                                        #Just panties
                                        $ Line = renpy.random.choice(["You reach under skirt and brush across her panties",
                                                "You lift her skirt a bit and grind against her panties",
                                                "You lift her skirt a bit and she gasps as you pull her panties aside and stroke across her butt",
                                                "Her legs twitch a bit beneath her skirt as you give her cheeks a firm squeeze",
                                                "She gasps as you stroke her asshole through her panties",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
                                elif GirlA.HoseNum() >= 5:
                                        #just hose
                                        $ Line = renpy.random.choice(["You reach under skirt and brush across her hose",
                                                "You lift her skirt a bit and grind against her hose",
                                                "You lift her skirt a bit and she gasps as you pull her hose aside and stroke across her butt",
                                                "Her legs twitch a bit beneath her skirt as you give her cheeks a firm squeeze",
                                                "She gasps as you stroke her asshole through her hose",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
                                else: #skirt, but nothing else
                                        $ Line = renpy.random.choice(["You reach under skirt and brush across her bare ass",
                                                "You lift her skirt a bit and grind against her warm cheeks",
                                                "You lift her skirt a bit and she gasps as you stroke asshole",
                                                "Her legs twitch a bit beneath her skirt as you press your thumb against her firm rear",
                                                "She gasps as you rub her bare hole",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
                                        if D20S <= 10:
                                            $ TempFocus += 2 if Player.Focus < 50 else 1
                                            $ TempLust += 3 if GirlA.Lust > 40 else 2
                                            $ GirlA.Addict -= 1
                                        else: #If it touches skin
                                            $ TempFocus += 1
                                            $ TempLust += 1

                        #no skirt or pants
                        elif (GirlA.PantsNum() == 6 or (GirlA == RogueX and GirlA.Panties == "shorts")) and not GirlA.PantiesDown:
                                    # just shorts on
                                    $ Line = renpy.random.choice(["You reach out and brush your hands across her lightly covered cheeks",
                                            "You grab her shorts and pull them taut, elliciting a small gasp",
                                            "You reach into her gap and she gasps as you slide your hand across and stroke her hole through the thin material",
                                            "Her legs twitch a bit as you grind her puckered hole",
                                            "She gasps as you reach under her shorts and lightly stroke her warm flesh",
                                            "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
                        elif GirlA.Panties and not GirlA.PantiesDown:
                                    # panties
                                    $ Line = renpy.random.choice(["You reach out and brush your hands across her barely covered cheeks",
                                            "You grab her panties and pull them taut, elliciting a small gasp",
                                            "You reach into her gap and she gasps as you slide your hand across and stroke her hole through the thin material",
                                            "Her legs twitch a bit as you grind her puckered hole",
                                            "She gasps as you reach under her panties and lightly stroke her warm flesh",
                                            "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
                        elif GirlA.HoseNum() >= 5:
                                    #just hose
                                    $ Line = renpy.random.choice(["You reach out and brush your hands across her barely covered cheeks",
                                            "You grab her hose and pull them taut, elliciting a small gasp",
                                            "You reach into her gap and she gasps as you slide your hand across and stroke her hole through the thin material",
                                            "Her legs twitch a bit as you grind her puckered hole",
                                            "She gasps as you reach under her hose and lightly stroke her warm flesh",
                                            "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
                        else: #nothing
                                    $ Line = renpy.random.choice(["You reach out and brush your hands across her bare ass",
                                            "You put your hand against her firm rear and grind against it",
                                            "You reach into her gap and she gasps as you slide your hand across and stroke her puckered hole",
                                            "Her legs twitch a bit as you press your thumb against her",
                                            "She gasps as you reach under her and lightly stroke her ass",
                                            "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])
                                    if D20S <= 10:
                                        $ TempFocus += 2 if Player.Focus < 50 else 1
                                        $ TempLust += 3 if GirlA.Lust > 40 else 2
                                        $ GirlA.Addict -= 1
                                    else: #If it touches skin
                                        $ TempFocus += 1
                                        $ TempLust += 1

                        if D20S > 10:#If it touches skin
                            $ TempFocus += 2 if Player.Focus < 50 else 1
                            $ TempLust += 3 if GirlA.Lust > 40 else 2
                            $ GirlA.Addict -= 1
                        else:
                            $ TempFocus += 2 if Player.Focus < 50 else 1
                            $ TempLust += 2 if GirlA.Lust > 40 else 1

    # end fondle ass                               /////////////////////////////////////////////////////////////////////////////

    elif Trigger == "insert ass":
                            $ Line = renpy.random.choice(["You continue to finger " + GirlA.Name + "'s asshole. ",
                                                    "You continue to finger bang " + GirlA.Name + "'s asshole. ",
                                                    "You continue to finger " + GirlA.Name + "'s rim. "])

                            if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                            $ Line = renpy.random.choice(["You slide a hand down her pants, and slide your fingers into her anus",
                                                    "You push her panties aside, and slide a finger between her cheeks",
                                                    "You slide a finger into her tight anus",
                                                    "You pull her pants out a bit and she gasps as you slide a finger up her hole",
                                                    "You gasps as you rub her asshole with your fingers"])
                            elif GirlA.PantsNum() == 5:
                                    if GirlA.Panties == "shorts" and not GirlA.PantiesDown:
                                            #shorts on
                                            $ Line = renpy.random.choice(["You push her skirt and shorts up, and slide a finger into her anus",
                                                    "You slide a finger into her tight anus",
                                                    "You lift her skirt a bit and she gasps as you pull her shorts up and slide a finger into her anus",
                                                    "You rub her pussy with your thumb as you dive into her anus with your middle finger"])
                                    elif GirlA.Panties and not GirlA.PantiesDown:
                                            #Just panties
                                           $ Line = renpy.random.choice(["You push her skirt and panties aside, and slide a finger into her anus",
                                                    "You slide a finger into her tight anus",
                                                    "You lift her skirt a bit and she gasps as you pull her panties aside and slide a finger into her anus",
                                                    "You rub her clit with your thumb as you dive into her pussy with your middle finger"])
                                    else: #skirt, but nothing else
                                             $ Line = renpy.random.choice(["You push her skirt aside, and slide a finger into her anus",
                                                    "You slide a finger into her tight anus",
                                                    "You lift her skirt a bit and she gasps as you slide a finger into her anus",
                                                    "You rub her pussy with your thumb as you dive into her anus with your middle finger"])
                            #no skirt or pants
                            elif (GirlA.PantsNum() == 6 or (GirlA == RogueX and GirlA.Panties == "shorts")) and not GirlA.PantiesDown:
                                    # just shorts on
                                    $ Line = renpy.random.choice(["You slide a hand down her shorts, and slide a finger into her anus",
                                                "You push her shorts up, and slide a finger between her lips",
                                                "You slide a finger into her tight anus",
                                                "You pull her shorts out a bit and she gasps as you slide a finger into her anus",
                                                "You rub her pussy with your palm as you dive into her anus with your middle finger"])
                            elif GirlA.Panties and not GirlA.PantiesDown:
                                        #Just panties
                                        $ Line = renpy.random.choice(["You push her panties aside, and slide a finger into her anus",
                                                "You slide a finger into her tight anus",
                                                "You lift her panties a bit and she gasps as you and slide a finger into her anus"])
                            else: #nothing
                                        $ Line = renpy.random.choice(["You reach out and slide a finger into her anus",
                                                "You slide a finger into her tight anus",
                                                "You press into her and she gasps as you  slide a finger into her anus",
                                                "You rub her pussy with your thumb as you dive into her anus with your middle finger"])

                            $ TempFocus += 2 if Player.Focus < 50 else 1
                            $ TempLust += 6 if GirlA.Lust > 70 else 3
                            if not GirlA.Loose:
                                    $ TempLust -= 3
                            elif GirlA.Loose < 2:
                                    $ TempLust += 1

                            $ GirlA.Addict -= 2

    # end insert ass                              /////////////////////////////////////////////////////////////////////////////

    elif Trigger == "lick ass":
                            $ Line = renpy.random.choice(["You continue to lick " + GirlA.Name + "'s ass. ",
                                                    "You continue to suck " + GirlA.Name + "'s ass. ",
                                                    "You continue to tongue " + GirlA.Name + "'s ass. "])

                            if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                                $ Line = renpy.random.choice(["You can feel her twitching as you grind your tongue against her anus, even through the thick material",
                                                        "She gasps as you press on her asshole through the thick fabric",
                                                        "You put your hand against her mound and lick the surface of her pants",
                                                        "With a little nibble, you tug at the denim"])
                                                $ TempFocus += 1 if Player.Focus < 70 else 0
                                                $ TempLust += 1 if GirlA.Lust < 60 else 0
                            else:
                                if GirlA.PantsNum() == 5:
                                        if GirlA.Panties == "shorts" and not GirlA.PantiesDown:
                                                #shorts on
                                                $ Line = renpy.random.choice(["You push her skirt up and lick at her asshole through her shorts",
                                                        "You bend down and stroke the edges of her shorts with your tongue",
                                                        "You spread the cheeks back beneath her shorts, and she gasps as you slide your tongue into it",
                                                        "You can feel her twitching as you grind your tongue against her anus",
                                                        "She gasps as you suck on her asshole through the thin fabric",
                                                        "You rub her pussy with your thumb as you dive into her asshole with your tongue",
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the rim aside"])
                                        elif GirlA.Panties and not GirlA.PantiesDown:
                                                #Just panties
                                                $ Line = renpy.random.choice(["You push her skirt up and lick at her asshole through her panties",
                                                        "You bend down and stroke the edges of her panties with your tongue",
                                                        "You spread the cheeks back beneath her panties, and she gasps as you slide your tongue into it",
                                                        "You can feel her twitching as you grind your tongue against her anus",
                                                        "She gasps as you suck on her asshole through the thin fabric",
                                                        "You rub her pussy with your thumb as you dive into her asshole with your tongue",
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the rim aside"])
                                        elif GirlA.HoseNum() >= 5:
                                                #just hose
                                               $ Line = renpy.random.choice(["You push her skirt up and lick at her asshole through her hose",
                                                        "You bend down and stroke the edges of her hose with your tongue",
                                                        "You spread the cheeks back beneath her hose, and she gasps as you slide your tongue into it",
                                                        "You can feel her twitching as you grind your tongue against her anus",
                                                        "She gasps as you suck on her asshole through the thin fabric",
                                                        "You rub her pussy with your thumb as you dive into her asshole with your tongue",
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the rim aside"])
                                        else: #skirt
                                                $ Line = renpy.random.choice(["You push her skirt aside and stroke her asshole with your tongue",
                                                        "You spread the cheeks back, and she gasps as you slide your tongue into it",
                                                        "You can feel her twitching as you grind your tongue against her asshole",
                                                        "She gasps as you suck on her anus",
                                                        "You rub her pussy with your thumb as you dive into her asshole with your tongue",
                                                        "You put your hand against her mound and lick around her rim",
                                                        "You slowly lick into her gap and she gasps as you press the rim apart"])
                                                if D20S <= 10:
                                                    $ TempFocus += 2 if Player.Focus < 70 else 0
                                                    $ TempLust += 3 if GirlA.Lust > 60 else 1
                                                    $ GirlA.Addict -= 3
                                                else: #If it touches skin
                                                    $ TempFocus += 1
                                                    $ TempLust += 1

                                #no skirt or pants
                                elif (GirlA.PantsNum() == 6 or (GirlA == RogueX and GirlA.Panties == "shorts")) and not GirlA.PantiesDown:
                                            # just shorts on
                                            $ Line = renpy.random.choice(["You bend down and stroke the edges of her shorts with your tongue",
                                                    "You spread the cheeks back beneath her shorts, and she gasps as you slide your tongue into it",
                                                    "You can feel her twitching as you grind your tongue against her anus",
                                                    "She gasps as you suck on her anus through the thin fabric",
                                                    "You rub her pussy with your thumb as you dive into her anus with your tongue",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the rim apart"])
                                elif GirlA.Panties and not GirlA.PantiesDown:
                                            #Just panties
                                            $ Line = renpy.random.choice(["You bend down and stroke the edges of her panties with your tongue",
                                                    "You spread the cheeks back beneath her panties, and she gasps as you slide your tongue into it",
                                                    "You can feel her twitching as you grind your tongue against her anus",
                                                    "She gasps as you suck on her anus through the thin fabric",
                                                    "You rub her pussy with your thumb as you dive into her anus with your tongue",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the rim apart"])
                                elif GirlA.HoseNum() >= 5:
                                            #just hose
                                            $ Line = renpy.random.choice(["You bend down and stroke the edges of her hose with your tongue",
                                                    "You spread the cheeks back beneath her hose, and she gasps as you slide your tongue into it",
                                                    "You can feel her twitching as you grind your tongue against her anus",
                                                    "She gasps as you suck on her anus through the thin fabric",
                                                    "You rub her pussy with your thumb as you dive into her anus with your tongue",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the rim apart"])
                                else: #nothing
                                            $ Line = renpy.random.choice(["You bend down and stroke her rim with your tongue",
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
                                                $ TempLust += 3 if GirlA.Lust > 60 else 1
                                                $ GirlA.Addict -= 3
                                            else: #If it touches skin
                                                $ TempFocus += 1
                                                $ TempLust += 1

                                if D20S > 10: #If it touches skin
                                    $ TempFocus += 3 if Player.Focus < 70 else 0
                                    $ TempLust += 9 if GirlA.Lust > 60 else 4
                                    $ GirlA.Addict -= 3
                                else:
                                    $ TempFocus += 1 if Player.Focus < 50 else 0
                                    $ TempLust += 4 if GirlA.Lust > 60 else 2

                            $ TempLust += 2 if GirlA.Loose > 1 else 0 #Bonus lust if she's anal experienced

    # end lick ass                               /////////////////////////////////////////////////////////////////////////////

    elif Trigger == "dildo pussy":
                        if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                $ Line = renpy.random.choice(["You rub the dildo against the outside of her pants",
                                        "You slap the dildo lightly against her mound"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0
                                $ TempLust += 3 if GirlA.Lust < 50 else 1
                        elif GirlA.HoseNum() >= 10:
                                $ Line = renpy.random.choice(["You rub the dildo against the outside of her tights",
                                        "You slap the dildo lightly at the outside of her tights"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0
                                $ TempLust += 3 if GirlA.Lust < 50 else 1
                        elif GirlA.HoseNum() >= 5:
                                $ Line = renpy.random.choice(["You rub the dildo against the outside of her hose",
                                        "You slap the dildo lightly at the outside of her hose"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0
                                $ TempLust += 3 if GirlA.Lust < 50 else 1
                        else:
                                if GirlA.PantsNum() == 5 and GirlA.Panties:
                                    $ Line = renpy.random.choice(["You push her skirt and panties aside, and slide the dildo into her pussy",
                                            "You slide the toy deep into her pussy",
                                            "She gasps as you rotate the dildo within her tight pussy",
                                            "You rub her clit with your thumb as you dive into her puss with the rubber phallus"])
                                    $ TempFocus += 2 if Player.Focus < 50 else 1
                                    $ TempLust += 8 if GirlA.Lust > 70 else 5
                                elif GirlA.PantsNum() == 5:
                                    $ Line = renpy.random.choice(["You push her skirt aside, and slide the dildo into her tight hole",
                                            "You slide the toy deep into her pussy",
                                            "You lift her skirt a bit and she gasps as you slide the dildo firmly into her tight puss",
                                            "She gasps as you rotate the dildo within her slit",
                                            "You rub her clit with your thumb as you dive into her pussy with the rubber phallus"])
                                    $ TempFocus += 2 if Player.Focus < 50 else 1
                                    $ TempLust += 8 if GirlA.Lust > 70 else 5
                                elif GirlA.Panties and not GirlA.PantiesDown:
                                    $ Line = renpy.random.choice(["You push her panties aside, and slide the dildo into her tight pussy",
                                            "You slide the dildo into her moist slit and stroke it rapidly",
                                            "You lift her panties a bit and she gasps as you slide the dildo between her lower lips",
                                            "She gasps as you rub her tight pussy with the toy",
                                            "You rub her clit with your thumb as you dive into her pussy with the dildo",
                                            "You reach into her gap and she gasps as you slide the dildo in and press against her tight slit through the thin material"])
                                    $ TempFocus += 2 if Player.Focus < 50 else 1
                                    $ TempLust += 8 if GirlA.Lust > 70 else 5
                                else:
                                    $ Line = renpy.random.choice(["You reach out and slide the dildo along her mound",
                                            "You slide the toy into her pussy and stroke it slowly",
                                            "You pull her lips apart and she gasps as you slide the dildo between them",
                                            "You can feel her twitching as you press your thumb against her clit",
                                            "She gasps as you rub her clit with the hard rubber",
                                            "You rub her clit with your thumb as you dive into her pussy with the dildo",
                                            "You reach into her gap and she gasps as you slide the toy across and press it into her wet pussy"])
                                    $ TempFocus += 3 if Player.Focus < 50 else 1
                                    $ TempLust += 10 if GirlA.Lust > 70 else 8
    # end dildo pussy                              /////////////////////////////////////////////////////////////////////////////

    elif Trigger == "dildo anal":
                        if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                $ Line = renpy.random.choice(["You rub the dildo against the outside of her pants",
                                        "You slap the dildo lightly against her ass"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0
                                $ TempLust += 3 if GirlA.Lust < 50 else 1
                        elif GirlA.HoseNum() >= 10:
                                $ Line = renpy.random.choice(["You rub the dildo against the outside of her tights",
                                        "You slap the dildo lightly at the outside of her tights"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0
                                $ TempLust += 3 if GirlA.Lust < 50 else 1
                        elif GirlA.HoseNum() >= 5:
                                $ Line = renpy.random.choice(["You rub the dildo against the outside of her hose",
                                        "You slap the dildo lightly at the outside of her hose"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0
                                $ TempLust += 3 if GirlA.Lust < 50 else 1
                        else:
                                if GirlA.PantsNum() == 5 and GirlA.Panties:
                                    $ Line = renpy.random.choice(["You push her skirt and panties aside, and slide the dildo into her ass",
                                            "You slide the toy deep into her ass",
                                            "She gasps as you rotate the dildo within her tight asshole",
                                            "You rub her clit with your thumb as you dive into her ass with the rubber phallus"])
                                    $ TempFocus += 2 if Player.Focus < 50 else 1
                                    $ TempLust += 8 if GirlA.Lust > 70 else 5
                                elif GirlA.PantsNum() == 5:
                                    $ Line = renpy.random.choice(["You push her skirt aside, and slide the dildo into her tight hole",
                                            "You slide the toy deep into her ass",
                                            "You lift her skirt a bit and she gasps as you slide the dildo firmly into her tight anus",
                                            "She gasps as you rotate the dildo within her ass",
                                            "You rub her clit with your thumb as you dive into her ass with the rubber phallus"])
                                    $ TempFocus += 2 if Player.Focus < 50 else 1
                                    $ TempLust += 8 if GirlA.Lust > 70 else 5
                                elif GirlA.Panties and not GirlA.PantiesDown:
                                    $ Line = renpy.random.choice(["You push her panties aside, and slide the dildo into her tight ass",
                                            "You slide the dildo into her ass and stroke it rapidly",
                                            "You lift her panties a bit and she gasps as you slide the dildo between her cheeks",
                                            "She gasps as you rub her tight asshole with the toy",
                                            "You rub her clit with your thumb as you dive into her asshole with the dildo",
                                            "You reach into her gap and she gasps as you slide the dildo in and press against her tight anus through the thin material"])
                                    $ TempFocus += 2 if Player.Focus < 50 else 1
                                    $ TempLust += 8 if GirlA.Lust > 70 else 5
                                else:
                                    $ Line = renpy.random.choice(["You reach out and slide the dildo between her cheeks",
                                            "You slide the toy into her asshole and stroke it against the sides",
                                            "You pull her cheeks apart and she gasps as you slide the dildo between them",
                                            "You can feel her twitching as you press your thumb against her anus",
                                            "She gasps as you rub her anus with the hard rubber",
                                            "You rub her clit with your thumb as you dive into her asshole with the dildo",
                                            "You reach into her gap and she gasps as you slide the toy across and press it into her firm anus"])
                                    $ TempFocus += 3 if Player.Focus < 50 else 1
                                    $ TempLust += 10 if GirlA.Lust > 70 else 6
                                if not GirlA.Loose:
                                        $ TempLust -= 3
                                elif GirlA.Loose < 2:
                                        $ TempLust += 1
    # end dildo ass                              /////////////////////////////////////////////////////////////////////////////

    elif Trigger == "masturbation":
                call Girl_Self_Lines(GirlA) #Rog*ue_Self_Lines
                if "unseen" not in GirlA.RecentActions:
                    if Trigger2 == "jackin" or "cockout" in Player.RecentActions:
                            $ TempLust += 2

    elif Trigger == "lesbian":
                call SexDialog_Threeway(GirlA,"lesbian",GirlB=Partner) #Rog*ue_SexDialog_Threeway("lesbian")

    elif Trigger == "foot":
                        $ Line = GirlA.Name + " continues stroke your cock with her feet. "

                        if not Speed:
                                    if GirlA.Foot > 2:
                                            $ Line = Line + "She just seems to be enjoying the feel of it"
                                            $ TempLust += 2 if GirlA.Lust < 60 else 0
                                    else:
                                            $ Line = Line + "She just seems to be looking it over"
                                            $ TempLust += 2 if GirlA.Lust < 40 else 0
                                            $ TempFocus += -3 if Player.Focus > 50 else 2

                                    $ GirlA.Addict -= 1 if D20S > 10 else 2
                                    return

                        if GirlA.Foot > 4:                          # After the 5th time
                                    if Speed <= 1:                      #slow
                                        $ Line = Line + renpy.random.choice(["Her movements have become almost masterful, her slightest touch starts you twitching",
                                                "She slowly caresses you in a way that makes your blood boil, then pulls back at the last second",
                                                "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                                "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                                "You can't tell where she is at any moment, all you know is that it works"])

                                        $ TempFocus += 20 if Player.Focus > 70 else 5

                                    else:                               #fast
                                        $ Line = Line + renpy.random.choice(["Her movements have become almost masterful, her slightest touch starts you twitching",
                                                "Her expert strokes will have you boiling over in seconds",
                                                "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                                "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                                "You can't tell where she is at any moment, all you know is that it works"])

                                        $ TempFocus += 20 if Player.Focus < 40 else 5

                        elif GirlA.Foot >= 3:                       #third through 5th time
                                    if Speed <= 1:                      #slow
                                        $ Line = Line + renpy.random.choice(["She's begining to figure things out, her toes cause tingles as they caress the shaft",
                                                "She's still learning, but learning fast",
                                                "She has a smooth motion going now, gentle and precise",
                                                "Her lessons are paying off, she's really becoming very talented at this",
                                                "She gently caresses the shaft, and brushes the balls in her other foot, giving them a light massage"])

                                        $ TempFocus += 15 if Player.Focus > 60 else 5

                                    else:                               #fast
                                        $ Line = Line + renpy.random.choice(["She's begining to figure things out, her toes cause tingles as they caress the shaft",
                                                "She's still learning, but learning fast",
                                                "Her feet glide smoothly across your cock",
                                                "She has a smooth motion going now, gentle and precise",
                                                "Her lessons are paying off, she's really becoming very talented at this",
                                                "She quickly strokes your cock, with a very deft pressure"])

                                        $ TempFocus += 15 if Player.Focus < 60 else 7

                        else:                                   #First and second time
                                if Speed <= 1:                      #slow
                                    $ Line = Line + renpy.random.choice(["She makes up for her inexperience with determination, carefully stroking your cock",
                                            "She moves her feet up and down the shaft. She's a little rough at this, but at least she tries",
                                            "She strokes you gently. She isn't quite sure what to do with the balls",
                                            "Her toes fumble with your shaft a bit",
                                            "She nudges one of your balls too tightly, but stops when you wince",
                                            "She has a firm grip, and she's not letting go. This may take a few tries"])

                                    $ TempFocus += 10 if Player.Focus > 60 else 5
                                else:                               #fast
                                    $ Line = Line + renpy.random.choice(["She really wasn't prepared for speeding up, and your cock often slips between her feet",
                                            "She rapidly moves her feet up and down the shaft. She's a little rough at this, but at least she tries",
                                            "She strokes you a bit too quickly, the friction is a bit uncomfortable",
                                            "Her toes fumble with your shaft a bit",
                                            "She nudges one of your balls too tightly, but stops when you wince",
                                            "She has a firm grip, and she's not letting go. This train is out of control"])

                                    $ TempFocus += 8 if Player.Focus > 60 else 2

                        $ TempLust += 2 if GirlA.Lust < 60 else 0
                        $ TempLust += 3 if GirlA.Foot > 2 else 0
                        $ GirlA.Addict -= 1

    #End Footy dialog ////////////////////////////////////////////////////////////////////////////////////////////////////////

    elif Trigger == "psy":
            $ Line = GirlA.Name + " continues work your cock. "

            if not Speed:
                        $ Line = GirlA.Name + "'s construct just rests on your cock. "
                        if GirlA.Hand > 2:
                                $ Line = Line + "She seems to be enjoying your reaction"
                                $ TempLust += 2 if GirlA.Lust < 60 else 0
                        else:
                                $ Line = Line + "She just seems to be looking it over"
                                $ TempLust += 2 if GirlA.Lust < 40 else 0
                                $ TempFocus += -3 if Player.Focus > 50 else 2
                        return

            if Psychic == "hand" or not Psychic:
                        # After the 5th time
                        $ Line = Line + renpy.random.choice(["Her movements are masterful, her slightest touch starts you twitching",
                                    "She's something of an expert, you feel a light tingle in your shaft",
                                    "She slowly caresses you in a way that makes your blood boil, then pulls back at the last second",
                                    "She really knows what to do, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                    "You can't tell where she is at any moment, all you know is that it works"])
                        if Speed <= 1:
                            #slow
                            $ TempFocus += 15 if Player.Focus > 60 else 5
                        else:
                            $ TempFocus += 15 if Player.Focus < 60 else 7
                        $ TempLust += 2 if GirlA.Lust < 60 else 0
            elif Psychic == "mouth":
                        $ Line = Line + renpy.random.choice(["She masterfully bobs on your cock, and it twitches with each stroke",
                                "She smoothly bobs up and down on your cock, a frenzy of motion",
                                "She gobbles you up all the way to the base, then quickly draws out and plunges back in",
                                "She's really getting good at this, alternating between deep suction and quick licks across the head",
                                "She moves very smoothly, bobbing in and out like she's been doing this for years",
                                "She puts the shaft into her mouth and her tounge swirls rapidly around it"])
                        $ TempFocus += 22 if Player.Focus > 40 else 10
                        $ TempLust += 3 if GirlA.Lust > 60 else 1
            elif Psychic == "tits":
                        $ Line = renpy.random.choice([GirlA.Name + " juggles her breast projections up and down around your cock",
                                GirlA.Name + " lightly strokes the head as it pops up between her tits",
                                GirlA.Name + " has a smooth motion going now, gentle and precise",
                                GirlA.Name + " pauses to rub her nipples across the shaft",
                                GirlA.Name + " gently caresses the shaft between her tits"])
                        $ TempFocus += 15 if Player.Focus < 60 else 5
                        $ TempLust += 6 if GirlA.Lust > 60 else 3
            elif Psychic == "sex" or Psychic == "anal":
                        #third through 5th time fast
                        $ Line = Line + renpy.random.choice(["It bounces rapidly against your cock",
                            "You thrust into it and she squeaks a bit",
                            "You quickly grind back and forth inside it",
                            "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                            "You pound away at it",
                            "She grinds it furiously back and forth along your cock"])
                        $ TempFocus += 12 if Player.Focus > 60 else 8
                        $ TempLust += 12 if GirlA.Lust > 80 else 6


    #End Psychic dialog ////////////////////////////////////////////////////////////////////////////////////////////////////////

    elif Trigger == "kiss you":
                        $ GirlA.Addict -= 3
                        $ GirlA.Addict -= 3 if GirlA == JubesX else 0
                        if GirlA.Kissed > 10 and GirlA.Love >= 700:#Loving
                                $ Line = renpy.random.choice(["She hungrily presses her lips against yours",
                                        "She confidently presses her lips against yours",
                                        "Her lips part as you hold her close",
                                        "You nibble her neck as she groans in pleasure",
                                        "You squeeze her tightly as your tongues jostle",
                                        "Her tongue dances around yours",
                                        "She nibbles your ear as her hands slide across your back",
                                        "Your hands slide down her body as your lips press hers"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0
                                $ TempFocus += 1 if Player.Focus < 90 else 0
                                $ TempLust += 3 if GirlA.Lust < 50 else 0
                                $ TempLust += 1 if GirlA.Lust < 90 else 0
                        elif GirlA.Kissed > 5 or GirlA == EmmaX:#reasonably experienced
                                $ Line = renpy.random.choice(["She confidently presses her lips against yours",
                                        "You softly kiss her plump lips",
                                        "Her lips part as you hold her close",
                                        "You nibble her neck as she coos in pleasure",
                                        "You squeeze her tightly as your lips connect",
                                        "Her tongue flickers out to meet yours",
                                        "Your hands slide down her body as your lips brush hers"])
                                $ TempFocus += 1 if Player.Focus < 70 else 0
                                $ TempLust += 3 if GirlA.Lust < 50 else 0
                                $ TempLust += 1 if GirlA.Lust < 90 else 0
                        else:#basic kissing
                                $ Line = renpy.random.choice(["She tentatively presses her lips against yours",
                                        "You softly kiss her plump lips",
                                        "Her lips part slightly as you hold her close",
                                        "You squeeze her tightly as your lips connect",
                                        "Your hands slide down her body as your lips brush hers"])
                                $ TempFocus += 1 if Player.Focus < 70 else 0
                                $ TempLust += 2 if GirlA.Lust < 30 else 0
                                $ TempLust += 1 if GirlA.Lust < 70 else 0

    # end kissing                              /////////////////////////////////////////////////////////////////////////////
    else: #no Trigger was set, somehow
        "No trigger was set, or it was '[Trigger]'. Please tell Oni what happend up to this point."
        $ Line = "Huh."

    $ Line = Line + "."
    # Wrap-up
    $ PrimaryLust += TempLust
    $ SecondaryLust += TempLust2 + 2

    return

label Offhand_Dialog(Girl=Primary, TempLine=0):
    #This is the dialog for what you're doing with your other hand while a primary action takes place
    #called by Sex_Dialog, if Trigger2 and D20S <= 15: call Offhand_Dialog
    if Girl not in TotalGirls:
            return
    if not Trigger2: #If there are no offhand options set, return
            return

    $ D20X = renpy.random.randint(1,20)

    if Trigger2 == "kiss you":
                $ Line = renpy.random.choice([" Your lips gently slide across hers.",
                        " Her lips part as you hold her close.",
                        " You nibble her neck as she groans in pleasure.",
                        " You squeeze her tightly as your tongues jostle.",
                        " Her tongue dances around yours.",
                        " She nibbles your ear as her hands slide across your back.",
                        " Your hands slide down her body as your lips press hers.",
                        " You kiss her passionately.",
                        " Your tongues swirl around each other's."])
                if Girl.Love >= 300:
                        $ Girl.Statup("Love", 75, 1)
                $ PrimaryLust += 2 if Girl.Lust < 50 else 1

    elif Trigger2 == "fondle breasts":
                if Girl == EmmaX and D20X >= 15:
                    $ Line = " You reach out and massage her enormous breasts."
                    $ PrimaryLust += 1
                    $ TempFocus += 1
                elif Girl == KittyX and D20X >= 15:
                    $ Line = " You reach out and massage her pert breasts."
                elif D20X >= 15:
                    $ Line = " You reach out and massage her glorious breasts."
                else:
                    $ Line = renpy.random.choice([" You reach out and massage her breasts.",
                            " You pass your hands gently over her warm breasts.",
                            " Her nipples catch lightly on your fingers as you grasp her warm flesh, you can feel them stiffen.",
                            " She gasps as you lightly thumb her rigid nipples."])
                $ PrimaryLust += 3
                $ TempFocus += 2 if Player.Focus < 90 else 0

    elif Trigger2 == "suck breasts":
            if Girl.ChestNum() > 1 or Girl.OverNum() > 1:
                $ Line = renpy.random.choice([" You bend down and motor-boat her breasts.",
                    " You tease her nipples with your tongue through her top.",
                    " You slowly lick her nipples through her moist top.",
                    " you gently place a nipple between your lips, and draw it out until it releases with a *pop*.",
                    " She gasps as you lightly lick her rigid nipples, poking through her top."])
            else:
                $ Line = renpy.random.choice([" You bend down and motor-boat her breasts.",
                    " You gently nibble at her nipples as you suck on them.",
                    " You tease her nipples with your tongue.",
                    " You slowly lick around, and then blow across her nipples.",
                    " You gently place a nipple between your lips, and draw it out until it releases with a *pop*.",
                    " She gasps as you lightly lick her rigid nipples."])
            $ PrimaryLust += 4 if 60 < Girl.Lust < 80 else 2
            $ TempFocus += 3 if Player.Focus < 90 else 0

    elif Trigger2 == "fondle pussy":
            if Girl.Pubes and D20X >= 15:
                $ Line = " You draw your hand along her furry bush, dripping with her excitement."
            elif D20X >= 15:
                $ Line = " You draw your hand along her smooth mount, slick with her excitement."
            else:
                $ Line = renpy.random.choice([" You put your hand against her mound and grind against it.",
                        " You reach into her gap and she gasps as you slide your hand across and stroke her lips.",
                        " Her legs twitch a bit as you press your thumb against her.",
                        " You slide a finger along her lower lips, and she lets out a small shudder.",
                        " You reach between her legs and she gasps as you stroke along her crevice.",
                        " You slide a hand up her inner thigh, she moans a little as you reach the point where they meet."])
            $ PrimaryLust += 4 if 60 < Girl.Lust < 90 else 2
            $ TempFocus += 4 if Player.Focus < 90 else 0

    elif Trigger2 == "lick pussy":
            if Girl.PantsNum() <= 5 and Girl.PantiesNum() <= 1:
                if Girl.Pubes and D20X >= 15:
                    $ Line = " You press you nose into her furry bush, dripping with her excitement."
                elif D20X >= 15:
                    $ Line = " You press you nose against her smooth mount, slick with her excitement."
                else:
                    $ Line = renpy.random.choice([" You slide your tongue into her pussy and flick the roof with deft strokes.",
                        " You spread the lips back and she gasps as you slide your tongue between them.",
                        " You can feel her twitching as you grind your tongue against her clit.",
                        " She gasps as you suck on her clit.",
                        " You rub her clit with your thumb as you dive into her pussy with your tongue.",
                        " With a little nibble, you tug on her lower lips.",
                        " You slowly lick into her gap and she gasps as you press the walls aside."])
            else:
                $ Line = renpy.random.choice([" You spread the lips back beneath the thin fabric, and she gasps as you slide your tongue across them.",
                    " She gasps as you suck on her clit through the fabric.",
                    " You rub her clit with your thumb as you press against her pussy with your tongue.",
                    " You put your hand against her mound and lick the juice that's collected.",
                    " With a little nibble, you tug back the fabric.",
                    " You slowly lick into her gap and she gasps as you press the walls aside."])
            $ PrimaryLust += 5 if Girl.Lust > 50 else 2
            $ TempFocus += 4 if Player.Focus < 90 else 0

    elif Trigger2 == "fondle ass":
            $ Line = renpy.random.choice([" You reach out and brush your hands across her ass.",
                    " You put your hand against her firm rear and grind against it.",
                    " You reach between her legs and she gasps as you stroke along her crevice.",
                    " Her legs twitch a bit as you press your thumb against her.",
                    " She gasps as you reach under her and lightly stroke her ass.",
                    " You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks."])
            $ PrimaryLust += 2 if Girl.Lust < 50 else 1
            $ TempFocus += 1 if Player.Focus < 50 else 0
            $ TempFocus += 1 if Player.Focus < 80 else 0

    elif Trigger2 == "insert ass":
            $ Line = renpy.random.choice([" You reach out and slide a finger into her ass.",
                    " You slide a finger into her asshole and stroke the roof of it.",
                    " You can feel her twitching as you press your thumb against her clit.",
                    " She gasps as you rub her asshole with your fingers.",
                    " You rub her pussy with your thumb as you dive into her asshole with your middle finger.",
                    " You reach into her gap and she gasps as you slide your hand across and press against her hole.",
                    " She gasps as you reach under her warm lips and lightly stroke her ass."])
            $ PrimaryLust += 3 if Girl.Lust > 70 and Girl.Loose else 1
            $ TempFocus += 2 if Player.Focus < 90 else 0

    elif Trigger2 == "jackin":
            if Trigger == "masturbation":
                    $ Line = " You stroke your cock as you watch her go."
            elif Trigger == "lesbian":
                    $ Line = " You stroke your cock as you watch them."
            elif Trigger == "hand":
                    $ Line = renpy.random.choice([" You also give it a little rub.",
                            " As she does so, you polish the knob a bit.",
                            " You help.",
                            " Your hand bumps into hers occasionally."])
            elif Trigger == "blow":
                    if Speed >= 3:
                        $ Line = "."
                    else:
                        $ Line = renpy.random.choice([" You also give it a little rub.",
                            " As she does so, you work the shaft a bit.",
                            " Your fingers brush her lips.",
                            " Her lips brush your hand occasionally."])
            else:
                    $ Line = renpy.random.choice([" With your other hand, you stroke your shaft.",
                            " You stroke your cock with your other hand.",
                            " As you do, you stoke yourself."])
            if "unseen" not in Girl.RecentActions:
                $ PrimaryLust += 3 if 20 < Girl.Lust < 70 else 2
                $ TempFocus += 1 if Player.Focus < 70 else 0
            $ TempFocus += 5
    return
    #End Offhand check

label Offhand_Set(Situation = Situation, TempTrigger = Trigger2,Chr=0):
    #called by various sex activities to set Trigger 2, which is the player's secondary action related to the primary girl
    #if the Situation is "shift focus," it means that the player is attempting to make his secondary action into his primary one.
    $ Chr = GirlCheck(Chr)
    if Situation == "shift focus":
            if TempTrigger:
                $ Trigger2 = 0
                if TempTrigger == "fondle breasts":
                        "You shift your attention to her breasts."
                        jump expression Chr.Tag + "_FB_Prep"
                elif TempTrigger == "suck breasts":
                        "You shift your attention to her breasts."
                        jump expression Chr.Tag + "_SB_Prep"
                elif TempTrigger == "fondle pussy":
                        "You shift your attention to her pussy."
                        jump expression Chr.Tag + "_FP_Prep"
                elif TempTrigger == "lick pussy":
                        "You shift your attention to her pussy."
                        jump expression Chr.Tag + "_LP_Prep"
                elif TempTrigger == "fondle ass":
                        "You shift your attention to her ass."
                        jump expression Chr.Tag + "_FA_Prep"
                elif TempTrigger == "insert ass":
                        "You shift your attention to her ass."
                        jump expression Chr.Tag + "_IA_Prep"
                else: #If Trigger2 is "kiss you"
                        "You go back to kissing her deeply."
                        jump KissPrep
            else: #if there's no Trigger2
                "You aren't doing anything else to shift to."
            return
    # End "shift" situation

    if Trigger:
        $ Situation = "auto"
        menu:
            "Also kiss her." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "insert ass", "sex", "anal", "hotdog", "dildo pussy", "dildo anal"):
                    "You lean in and start kissing her."
                    $ Trigger2 = "kiss you"

            "Also fondle her breasts." if Trigger in ("kiss you","fondle pussy", "fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "foot", "dildo pussy", "dildo anal"):
                    $ Trigger2 = "fondle breasts"
                    call fondle_breasts(Chr)

            "Also suck her breasts." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "insert ass", "sex", "anal", "hotdog", "dildo pussy", "dildo anal"):
                    $ Trigger2 = "suck breasts"
                    call suck_breasts(Chr)

            "Also fondle her pussy." if Trigger in ("kiss you","fondle breasts","fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "foot", "dildo pussy", "dildo anal"):
                    $ Trigger2 = "fondle pussy"
                    call expression Chr.Tag + "_Fondle_Pussy"

            "Also fondle her ass." if Trigger in ("kiss you","fondle breasts","fondle pussy", "fondle thighs", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "foot", "dildo pussy", "dildo anal"):
                    $ Trigger2 = "fondle ass"
                    call expression Chr.Tag + "_Fondle_Ass"

            "Also finger her ass." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "suck breasts", "lick pussy", "lick ass", "sex", "hotdog", "foot", "dildo pussy"):
                    $ Trigger2 = "insert ass"
                    call expression Chr.Tag + "_Insert_Ass"

            "Also jack it." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "dildo pussy", "dildo anal"):
                    call Jackin(Chr)

            "Nevermind":
                pass
    else: #if a Trigger is not found. . .
        "There's some kind of bug here, let Oni know."

    $ Situation = 0
    return

label Girl_Self_Lines(GirlA = Primary, Mode = "T3", Action = Trigger3, TempLustX = 0, TempFocusX = 0, D20X=0):
    # The Mode can be T3 for Trigger 3 for a masturbation option, or T5/Trigger5 if it's setting a Threeway action.
    # call Girl_Self_Lines(GirlA,"T5",Trigger5)  X Rogu*e_Self_Lines("T5",Trigger5)
    # This sets a Action if there isn't one, or sets an intitial line
    # Primary if called from main sex dialog, secondary if called from Threesome

    $ D20X = renpy.random.randint(1, 20) if not D20X else D20X

    $ Line = 0
    if not Action or D20X >= 15:
            #if there is no appropriate trigger set or if RNG says to pick a new one. . .
            if Trigger != "masturbation" and "passive" in GirlA.Traits:
                    # This bypasses self-set if Rog*ue is told not to take initiative
                    $ Line = 0
                    return
            call Girl_Self_Set(GirlA,Mode,Action) #Rog*ue_Self_Set(Mode, Action)

            if Mode == "T3":
                    #Sets Action based on the result
                    $ Action = Trigger3
            else:
                    #if Mode == "T5"
                    $ Action = Trigger5
            if not Action:
                    return
            elif Action == "hand" and not Line:
                        $ Line = "Also, " + GirlA.Name + " continues stroke your cock. "
            elif not Line:
                        $ Line = "Also, " + GirlA.Name + " continues to masturbate. "
    elif Action == "hand":
                        $ Line = GirlA.Name + " continues stroke your cock. "
    else:
                        $ Line = renpy.random.choice([GirlA.Name + " continues to masturbate. ",
                                    GirlA.Name + "'s hands move across her body. ",
                                    GirlA.Name + " continues to feel herself. ",
                                    GirlA.Name + " can't keep still. "])

    if Action == "hand":
                        $ Line = Line + renpy.random.choice(["She lightly strokes the shaft, fingers sliding along the vein",
                                "She grasps the shaft firmly, and slowly slides along its length",
                                "She's becoming something of a handjob expert",
                                "Her expert strokes will have you boiling over in seconds",
                                "She strokes the shaft vigorously, lightly touching the tip",
                                "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                "Her hand slides slowly down your shaft"])
                        if Trigger == "massage":
                                $ TempFocusX += 10 if Player.Focus > 60 else 4
                                $ TempFocusX += 2 if GirlA.Hand > 2 else 0
                        else:
                                $ TempFocus += 10 if Player.Focus > 60 else 4
                                $ TempFocus += 2 if GirlA.Hand > 2 else 0

                        $ TempLustX += 2 if GirlA.Lust < 60 else 1
                        $ TempLustX += 2 if GirlA.Hand > 2 else 0
                        $ GirlA.Addict -= 1
    else:
        if GirlA.Lust >= 80:
                if Action == "fondle pussy":
                        $ Line = Line + renpy.random.choice(["Her hand rapidly moves across her mound, firmly stroking her clit",
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
                elif Action == "dildo pussy":
                        $ Line = Line + renpy.random.choice(["She moves the dildo in circles across her mound, firmly rubbing into it",
                                "She hungrily slams the dildo into her tight pussy, and pistons it in and out",
                                "She shoves the dildo firmly in and out of her grasping pussy",
                                "She quickly slides the phallus up and down her crease"])
                elif Action == "fondle ass":
                        $ Line = Line + renpy.random.choice(["Her hand rapidly moves across her ass, firmly stroking her tight hole",
                                "She inserts a finger deep into her grasping hole and rapidly pistons it",
                                "She gasps as she buries a finger deeply into her tight anus",
                                "She gives a little squeal as she pinches her clit between her fingers",
                                "Her fingers move quickly across her ass, constantly sliding across her rim",
                                "Her fingers move rapidly up and down her inner thighs and ass, building towards their center",
                                "She spreads her cheeks and furiously strokes the puckered rim",
                                "She slides two fingers firmly in and out of her tight hole",
                                "She rapidly circles her fingers against the sensitive rim",
                                "She lets out a moan as her fingers brush against her quivering hole"])
                elif Action == "dildo anal":
                        $ Line = Line + renpy.random.choice(["She moves the dildo in circles across her ass, firmly rubbing into it",
                                "She hungrily slams the dildo into her tight hole, and pistons it in and out",
                                "She shoves the dildo firmly in and out of her grasping asshole",
                                "She quickly slides the phallus up and down the crease of her ass"])
                elif Action == "vibrator pussy":
                        $ Line = Line + renpy.random.choice(["She traces the buzzing ball slowly down her body, barely grazing her mound",
                                "Her vibrator slides lightly across her pubic region, subtly avoiding her lips",
                                "She slides the buzzing egg into her dripping pussy and tugs it in and out",
                                "She presses the vibrator firmly against her clit and a shiver runs through her",
                                "Her whirring toy is dragged up and down her inner thighs, slowly building towards their center",
                                "She  spreads her lower lips and runs the device along the inner lining",
                                "She presses the toy deep into her and the vibrations send a shock through her body"])
                else: # Action == "fondle breasts"
                        $ Line = Line + renpy.random.choice(["She passionately rubs her breasts, desperately tugging at her nipples",
                                "Her hands squeeze at her breasts, massaging them firmly with both hands",
                                "She hungrily cups her breasts and moves them in rapid circles",
                                "Her hands move constantly across her chest, alternately pulling at her nipples or just grazing her skin",
                                "She firmly pinches her nipples and gives them steady tugs",
                                "She passionately rubs her breasts, desperately tugging at her nipples"])
        #End GirlA.Lust >= 80
        elif GirlA.Lust >= 50:
                if Action == "fondle pussy":
                        $ Line = Line + renpy.random.choice(["Her hand moves in circles across her mound, firmly rubbing into it",
                                "Her hands move along her sides, carefully caressing them",
                                "Her fingers move smoothly across her delta, occasionally grazing her lips",
                                "Her fingers move up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She gently slides a finger up and down the crease of her pussy",
                                "She lets out a gasp as her fingers brush against her erect clit"])
                elif Action == "dildo pussy":
                        $ Line = Line + renpy.random.choice(["She moves the dildo in circles across her mound, firmly rubbing into it",
                                "She traces the rubber phallus slowly down her body, barely grazing her mound",
                                "Her dildo slides lightly across her pubic region, subtly avoiding her lips",
                                "Her dildo is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She gently slides the phallus up and down the crease of her pussy",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "fondle ass":
                        $ Line = Line + renpy.random.choice(["Her hand moves in circles across her ass, firmly rubbing into it",
                                "Her hands move along her sides, carefully caressing them",
                                "Her fingers move smoothly along her crack, occasionally grazing her asshole",
                                "Her fingers move up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her cheeks and caresses the tight hole within",
                                "She gently slides a finger up and down the crease of ass",
                                "She lets out a gasp as her fingers brush against her puckered hole"])
                elif Action == "dildo anal":
                        $ Line = Line + renpy.random.choice(["She traces the rubber phallus slowly down her body, barely grazing her ass",
                                "Her dildo slides lightly across her crack, subtly avoiding the hole",
                                "Her dildo is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her cheeks and caresses the rim beneath",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "vibrator pussy":
                        $ Line = Line + renpy.random.choice(["She traces the buzzing ball slowly down her body, barely grazing her mound",
                                "Her vibrator slides lightly across her pubic region, subtly avoiding her lips",
                                "Her whirring toy is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She drags the vibrator slowly along her sides, carefully caressing them"])
                else: # Action == "fondle breasts"
                        $ Line = Line + renpy.random.choice(["She gently rubs her breasts, dragging a finger across her nipple",
                                "She gently cups her breasts and moves them in slow circles",
                                "She moves her hands from her breasts to rub her neck",
                                "She lightly pinches one of her nipples",
                                "Her hands firmly caress her breasts, massaging them in circular motions",
                                "Her hands move along her breasts, carefully caressing them",
                                "She gasps as her finger brushes against an erect nipple"])
        #End GirlA.Lust >= 50
        else: #if GirlA.Lust < 50:
                if Action == "fondle pussy":
                        $ Line = Line + renpy.random.choice(["Her hand traces slowly down her body, barely grazing her mound",
                                "Her fingers move lightly across her pubic region, subtly avoiding her lips",
                                "Her fingers move up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "Her hands move along her sides, carefully caressing them"])
                elif Action == "dildo pussy":
                        $ Line = Line + renpy.random.choice(["She traces the rubber phallus slowly down her body, barely grazing her mound",
                                "Her dildo slides lightly across her pubic region, subtly avoiding her lips",
                                "Her dildo is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "fondle ass":
                        $ Line = Line + renpy.random.choice(["Her hand traces slowly down her body, barely passing smoothly across her hips",
                                "Her fingers move lightly across her crack, subtly avoiding her rosebud",
                                "Her fingers move up and down her inner thighs, slowly building towards their center",
                                "Her hands move along her sides, carefully caressing them"])
                elif Action == "dildo anal":
                        $ Line = Line + renpy.random.choice(["She traces the rubber phallus slowly down her body, barely grazing her ass",
                                "Her dildo slides lightly across her crack, subtly avoiding the hole",
                                "Her dildo is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her cheeks and caresses the rim beneath",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "vibrator pussy":
                        $ Line = Line + renpy.random.choice(["She traces the buzzing ball slowly down her body, barely grazing her mound",
                                "Her vibrator slides lightly across her pubic region, subtly avoiding her lips",
                                "Her whirring toy is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She drags the vibrator slowly along her sides, carefully caressing them"])
                else: # Action == "fondle breasts"
                        $ Line = Line + renpy.random.choice(["She gently rubs her breasts, dragging a finger across her nipple",
                                "She gently cups her breasts and moves them in slow circles",
                                "She moves her hands from her breasts to rub her neck",
                                "She lightly pinches one of her nipples",
                                "She gasps as her finger brushes against an erect nipple"])
                #End GirlA.Lust 0-60
        #End Girl's Action masturbation dialog


        # Girl's Self-stat boosts
        $ TempLustX += 4 if GirlA.Lust > 80 else 0
        $ TempLustX += 5 if GirlA.Lust < 40 else 3                      #Bonus if she is relatively low lust
        $ TempLustX += 5 if Trigger == "masturbation" and GirlA != Partner else 0            #Bonus if masturbation is her primary action

        if Trigger == "massage":
                $ TempFocusX += 4 if Player.Focus < 50 else 3
                $ Player.Statup("Focus", 200, TempFocusX)
                $ GirlA.Statup("Lust", 200, TempLustX)
                return
        else:
                if "TempFocus" not in locals().keys():
                        "Tell Oni the error was \"[Trigger]\"."
                $ TempFocus += 4 if Player.Focus < 50 else 3

        if Partner != GirlA:
                #If this is a primary, Trigger3 action
                $ TempLust = TempLustX
        else:
                #If this is a Secondary, Trigger5 action
                $ TempLust2 = TempLustX


    #End Action all dialog

    return

label Girl_Self_Set(GirlA=Primary, Mode = "T3", Action = Trigger3, Length=0, Count2=0, Options =[]):
    #nee Rog*ue_Self_Set(Mode = "T3", Action = Trigger3, Length=0, Count2=0, Options =[]):
    #If T3/Trigger3 is sent, this is for Primary role, offhand behavior
    #If T5/Trigger5 is sent, this is for Secondary role, threesome masturbation behavior
    if Mode == "T3" and Trigger != "masturbation":
                # This cuts it out if she's submissive or not horny enough to get busy
                if "sub" in GirlA.Traits:
                        return

                #if she's inexperienced or shy, skip this
                if GirlA.SEXP >= 50 or ApprovalCheck(GirlA, 500, "I"):
                    if GirlA.Lust <= 30:
                        return
                elif GirlA.SEXP >= 25 or ApprovalCheck(GirlA, 300, "I"):
                    if GirlA.Lust <= 50:
                        return
                else:
                        return

    if Mode == "T3" and Trigger == "masturbation":
                #sets base options as masturbatory
                $ Options = ["fondle pussy", "fondle breasts", "fondle ass"]
                if "dildo" in GirlA.Inventory:
                        $ Options.append("dildo pussy")
                        if GirlA.Loose:
                            $ Options.append("dildo anal")
                if "vibrator" in GirlA.Inventory:
                        $ Options.append("vibrator pussy")

    else:
                if GirlA.Hand >= 5 and Mode != "T5" and Trigger in ("fondle pussy", "fondle breasts", "fondle thighs", "kiss you", "fondle ass", "suck breasts"):
                        #if this is about the primary girl, and she's done handys, and you're feeling her up, she might feel you up
                        $ Options.append("hand")

                if Trigger not in ("sex", "fondle pussy", "lick pussy", "dildo pussy"):
                        #if you aren't touching her pussy, she might
                        if "dildo" in GirlA.Inventory:
                                $ Options.append("dildo pussy")
                        $ Options.append("fondle pussy")

                if Trigger not in ("anal", "fondle ass", "insert ass", "lick ass", "dildo anal") and GirlA.Loose:
                        #if you aren't messing with her ass, she might
                        if "dildo" in GirlA.Inventory:
                                $ Options.append("dildo anal")
                        $ Options.append("fondle ass")

                if "vibrator" in GirlA.Inventory:
                        $ Options.append("vibrator pussy")

                if Trigger not in ("fondle breasts", "suck breasts"):
                        #if you aren't dealing with her breasts. . .
                        $ Options.append("fondle breasts")

                if GirlA.Obed < GirlA.Inbt:
                        #adds more options if she is not submissive
                        if "fondle pussy" not in Options:
                                $ Options.append("fondle pussy")
                        if "fondle ass" not in Options:
                                $ Options.append("fondle ass")
                        if "fondle breasts" not in Options:
                                $ Options.append("fondle breasts")
    # End filling options

    $ Length = len(Options)-1
    $ D20 = renpy.random.randint(1, 20)
    if D20 >=18:
            $ Count2 = 0
    elif D20 >= 15:
            $ Count2 = 1
    elif D20 >= 12:
            $ Count2 = 2
    elif D20 >= 10:
            $ Count2 = 3
    else:
            $ Count2 = renpy.random.randint(0, Length)

    $ Count2 = Length if Count2 > Length else Count2
    if Action != Options[Count2]:
            #If the action has changed, play change dialog
            $ Action = Options[Count2] #Sets Action to the selected Option
            if Action == "hand":
                    $ Line = GirlA.Name + " slides her hand down and firmly grabs your dick. "
                    $ Approval = 3
            elif Action == "fondle pussy":
                    $ Line = GirlA.Name + "'s hand slides down and begins to stroke her pussy. "
            elif Action == "dildo pussy":
                    $ Line = GirlA.Name + " pulls out her dildo and draws it toward her pussy. "
            elif Action == "fondle ass":
                    $ Line = GirlA.Name + "'s hand slides behind her body, reaching toward her ass. "
            elif Action == "dildo anal":
                    $ Line = GirlA.Name + " pulls out her dildo and reaches it behind her. "
            elif Action == "vibrator pussy":
                    $ Line = GirlA.Name + " pulls out her vibrator and strokes it across her body. "
            else: # Action == "fondle breasts"
                    $ Line = GirlA.Name + "'s hands slide up her body and begin to kneed her breasts. "
    elif Action == "hand":
            $ Line = "Also, " + GirlA.Name + " continues stroke your cock. "
    else:
            $ Line = "Also, " + GirlA.Name + " continues to masturbate. "

    if Mode == "T3": #Sets Action based on the result
        $ Trigger3 = Action
    else:
        $ Trigger5 = Action

    return

label SexDialog_Threeway(GirlA = Secondary, Mode = 0, Action = 0, GirlB = Primary, TempLine = 0, TempLust = 0, TempLust2 = 0, TempFocus = 0):
    #nee Rog*ue_SexDialog_Threeway(Mode = 0, Action = 0,
    # This is the dialog checked for Trigger 4, activated when GirlA is the second girl in a scene, or for Lesbian activities.
    # if Mode is "lesbian" then it means she's doing a girl/girl sequence, and activating secondary dialogs.
    # By default, GirlB will be the primary and this sequence will build text for what the secondary girl does.
    # In "lesbian" mode, GirlB will be the secondary girl, and this sequence will build text for what the primary will do to her.
    # Lesbian Trigger1 dialog calls "call SexDialog_Threeway(RogueX,"lesbian")" #nee "call Rog*ue_SexDialog_Threeway("lesbian")"

    call Threeway_Set(GirlA,Mode=Mode,GirlB=GirlB) #nee Rog*ue_Threeway_Set(Mode=Mode)   #Picks a new activty on a 7-9 roll or when not set, otherwise returns

    if Mode == "lesbian":
            $ Action = Trigger3
            $ GirlB = Secondary
    else:
            $ Action = Trigger4

    if Line:
            #if it picked something, it should have set a line and returned
            return
    elif not Action:
            $ Action = "watch"

    if Action == "hand":
                    if D20S <= 8 and (Trigger == "blow" or Trigger == "hand"): #This is a random bonus dialog
                        if Trigger == "blow": #If Kitty is blowing you
                            $ Line = renpy.random.choice([GirlA.Name + "'s fingers brush against " + GirlB.Name + "'s lips as they work",
                                    GirlA.Name + " and " + GirlB.Name + " pause for a second to briefly kiss",
                                    GirlA.Name + " takes a turn to suck on the head before passing it back",
                                    GirlA.Name + " and " + GirlB.Name + " get into an alternating rhythm"])
                        elif Trigger == "hand":  #If Kitty is handying you
                            $ Line = renpy.random.choice([GirlA.Name + "'s fingers brush against " + GirlB.Name + "'s as they work",
                                    GirlA.Name + " strokes " + GirlB.Name + "'s palm as she works",
                                    GirlA.Name + " takes a turn to stroke a few times before passing it back",
                                    GirlA.Name + " and " + GirlB.Name + " get into an alternating rhythm"])
                    else:
                        if Trigger == "hand": #if another girl is also handy
                                $ Line = GirlA.Name + " also continues to stroke your cock"
                        else: #if the other girl is doing something else
                                $ Line = GirlA.Name + " continues stroke your cock"

                        $ Line = Line + renpy.random.choice([", lightly stroking the shaft, fingers sliding along the vein",
                                ", grasping the shaft firmly, and slowly sliding along its length",
                                ", making up for years of lost time",
                                ", her expert strokes will have you boiling over in seconds",
                                ", stroking the shaft vigorously, lightly touching the tip",
                                ", moving very smoothly, stroking casually",
                                ", hand sliding slowly down your shaft"])
                    $ TempFocus += 3 if Player.Focus > 70 else 2

                    $ TempLust += 2 if GirlA.Lust < 60 else 0
                    $ TempLust += 2 if GirlA.Hand > 2 else 0
                    $ GirlA.Addict -= 1 if D20S > 10 else 2

    # end GirlA.Hand Threeway                                //////////////////////////////////////////////////////////////////////////////

    elif Action == "blow":
                    if Speed > 2 and Trigger == "blow":
                        $ Line = "Since " + GirlB.Name + " is working so hard, " + GirlA.Name + " settles for the occasional nibble or lick."
                        $ TempFocus += 5 if Player.Focus > 60 else 3
                        $ TempLust += 2 if GirlA.Lust > 80 else 1
                    else:
                        if D20S <= 8 and (Trigger == "blow" or Trigger == "hand"): #This is a random bonus dialog
                            if Trigger == "blow": #If Kitty is blowing you
                                $ Line = renpy.random.choice([GirlA.Name + "'s tongue brushes against " + GirlB.Name + "'s as they work",
                                        GirlA.Name + " and " + GirlB.Name + " pause for a second to briefly kiss",
                                        GirlA.Name + " takes a turn to suck on the head before passing it back",
                                        GirlA.Name + " and " + GirlB.Name + " get into an alternating rhythm"])
                            elif Trigger == "hand": #If Kitty is handying you
                                $ Line = renpy.random.choice([GirlA.Name + "'s tongue brushes against " + GirlB.Name + "'s hand as they work",
                                        GirlA.Name + " licks " + GirlB.Name + "'s palm as she works",
                                        GirlA.Name + " takes a turn to stroke a few times before passing it back",
                                        GirlA.Name + " and " + GirlB.Name + " get into an alternating rhythm"])
                            $ TempLust2 += 1 if GirlB.GirlLikeCheck(GirlA) >= 800 else 0
                        else:
                            if Trigger == "blow": #if another girl is also blowing
                                    $ Line = GirlA.Name + " also continues to lick your cock"
                            else: #if the other girl is doing something else
                                    $ Line = "Also, " + GirlA.Name + " continues lick your cock"

                            $ Line = Line + renpy.random.choice([", settling into a gentle licking pace along the base",
                                    ", licking gently up and down the shaft",
                                    ", her tongue moves carefully along the shaft",
                                    ", really starting to learn some clever tricks to making you feel good",
                                    ", licking her way down the shaft, and gently teasing the balls"])

                        $ TempFocus += 20 if Player.Focus > 60 else 10
                        $ TempLust += 2 if GirlA.Lust > 80 else 1

                        $ GirlA.Addict -= 2
    # end GirlA.Blowjob Threeway                                //////////////////////////////////////////////////////////////////////////////

    elif Action == "fondle breasts":
                        if Trigger2 == "fondle breasts" and Trigger != "lesbian": #if you're also fondling them,
                            $ Line = GirlA.Name + " also continues to fondle " + GirlB.Name + "'s breasts"
                        else:
                            $ Line = GirlA.Name + " continues to fondle " + GirlB.Name + "'s breasts"

                        $ Line = Line + renpy.random.choice([", giving little tugs to her nipples",
                                        ", cupping them firmly with both hands",
                                        ", gently moving them in slowly increasing circles",
                                        ", then moves her hands from her breasts to rub her neck",
                                        ", firmly pinching her nipples and giving them a tug",
                                        ", passing repeatedly against her rigid nipples"])
                        $ TempLust += 2 if ApprovalCheck(GirlA, 500, "I") else 1  # GirlA's lust
                        $ TempLust2 += 5 if GirlB.GirlLikeCheck(GirlA) >= 800 else 2
                        $ TempFocus += 1
    # end Fondle breasts Threeway                                //////////////////////////////////////////////////////////////////////////////


    elif Action == "suck breasts":
                        if Trigger2 == "fondle breasts" and Trigger != "lesbian": #if you're also fondling them,
                                $ Line = GirlA.Name + " also continues to suck " + GirlB.Name + "'s breasts"
                        else:
                                $ Line = GirlA.Name + " continues to suck " + GirlB.Name + "'s breasts"

                        $ Line = Line + renpy.random.choice([", giving little tugs to her nipple",
                                        ", cupping them firmly with both hands",
                                        ", then moves her hands down along her side",
                                        ", licking slowly up her chest",
                                        ", firmly nibbling her nipples and giving them a tug",
                                        ", nibbling repeatedly at her rigid nipples"])
                        $ TempLust += 2 if ApprovalCheck(GirlA, 500, "I") else 1  # GirlA's lust
                        $ TempLust2 += 4 if GirlB.GirlLikeCheck(GirlA) >= 800 else 2
                        $ TempFocus += 1
    # end Suck breasts Threeway                                //////////////////////////////////////////////////////////////////////////////


    elif Action == "fondle pussy":
                        if (Trigger == "fondle pussy" or Trigger2 == "fondle pussy") and Trigger != "lesbian": #if you're also fondling them,
                                $ Line = GirlA.Name + " also continues to fondle " + GirlB.Name + "'s pussy"
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
                                $ Line = GirlA.Name + " continues to fondle " + GirlB.Name + "'s pussy"
                                $ Templine = renpy.random.choice([", running fingers gently up her cleft",
                                        ", stroking across her clit",
                                        ", taking a little taste of the warm juices on her finger",
                                        ", rubbing against it vigorously",
                                        "a",
                                        "b",
                                        "c",
                                        ", moving with slow undulating motions"])

                                #a, b, and c can change depending on other circumstances at the time.
                                if Templine == "a":
                                    if Trigger == "sex" or Trigger == "anal":
                                            $ Templine = ", her fingers brush against your cock as it goes in"
                                    elif Trigger == "lick pussy":
                                            $ Templine = ", your tongue slides past her fingers"
                                    elif Trigger == "dildo pussy" or Trigger2 == "dildo pussy":
                                            $ Templine = ", her fingers brush against the dildo as it goes in"
                                    else:
                                            $ Templine = ", stroking into it vigorously"
                                elif Templine == "b":
                                    if Trigger == "sex" or Trigger == "anal":
                                            $ Templine = ", her fingers brushing up against your balls as you sink in"
                                    elif Trigger == "lick pussy":
                                            $ Templine = ", you briefly suck on one of her fingers"
                                    elif Trigger == "dildo pussy" or Trigger2 == "dildo pussy":
                                            $ Templine = ", her fingers brushing up against the dildo as it slides by"
                                    else:
                                            $ Templine = ", sliding firmly into it"
                                elif Templine == "c":
                                    if Trigger == "sex" or Trigger == "anal":
                                            $ Templine = ", her fingers brush against your cock as it goes in"
                                    elif Trigger == "lick pussy":
                                            $ Templine = ", your tongue slides along her fingers"
                                    elif Trigger == "dildo pussy" or Trigger2 == "dildo pussy":
                                            $ Templine = ", her fingers brushing up against the dildo as it slides by"
                                    else:
                                            $ Templine = ", moving inside it with slow undulating motions"
                                #End if the other girl is not fondling
                        $ Line = Line + Templine

                        $ TempLust += 2 if ApprovalCheck(GirlA, 500, "I") else 1  # GirlA's lust
                        $ TempLust2 += 5 if GirlB.GirlLikeCheck(GirlA) >= 800 else 3
                        $ TempFocus += 1

    # end fondle pussy Threeway                              /////////////////////////////////////////////////////////////////////////////


    elif Action == "lick pussy":
                        if (Trigger == "lick pussy" or Trigger2 == "lick  pussy") and Trigger != "lesbian": #if you're also fondling them,
                            $ Line = GirlA.Name + " also continues to lick " + GirlB.Name + "'s pussy"
                        else:
                            $ Line = GirlA.Name + " continues to lick " + GirlB.Name + "'s pussy"

                        $ Templine = renpy.random.choice([", running her tongue gently up her cleft",
                                    ", stroking across her clit",
                                    ", taking a little taste of the warm juices flowing out",
                                    ", lapping against it vigorously",
                                    "a",
                                    "b",
                                    "c",
                                    ", moving with slow undulating motions"])

                        #a, b, and c can change depending on other circumstances at the time.
                        if Templine == "a":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her tongue brushes against your cock as it goes in"
                                elif Trigger == "lick pussy":
                                        $ Templine = ", her tongue brushing against yours as you work"
                                elif Trigger == "fondle pussy" or Trigger2 == "fondle pussy":
                                        $ Templine = ", her tongue slides along your fingers"
                                elif Trigger == "dildo pussy" or Trigger2 == "dildo pussy":
                                        $ Templine = ", her tongue brushes along the dildo as it goes in"
                                else:
                                        $ Templine = ", lapping into it vigorously"
                        elif Templine == "b":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her longue lapping against your balls as you sink in"
                                elif Trigger == "lick pussy":
                                        $ Templine = ", you briefly kiss as you take turns"
                                elif Trigger == "fondle pussy" or Trigger2 == "fondle pussy":
                                        $ Templine = ", her tongue slides past your fingers"
                                elif Trigger == "dildo pussy" or Trigger2 == "dildo pussy":
                                        $ Templine = ", her tongue runs up against the dildo as it slides by"
                                else:
                                        $ Templine = ", sliding firmly into it"
                        elif Templine == "c":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her tongue brushes against your cock as it goes in"
                                elif Trigger == "lick pussy":
                                        $ Templine = ", the two of you taking turns in your motions"
                                elif Trigger == "fondle pussy" or Trigger2 == "fondle pussy":
                                        $ Templine = ", her tongue slides past your fingers"
                                elif Trigger == "dildo pussy" or Trigger2 == "dildo pussy":
                                        $ Templine = ", her tongue runs up against the dildo as it slides by"
                                else:
                                        $ Templine = ", moving inside it with slow undulating motions"

                        $ Line = Line + Templine

                        $ TempLust += 3 if ApprovalCheck(GirlA, 600, "I") else 1  # GirlA's lust
                        $ TempLust2 += 7 if GirlB.GirlLikeCheck(GirlA) >= 800 else 4
                        $ TempFocus += 3

    # end lick pussy Threeway                              /////////////////////////////////////////////////////////////////////////////

    elif Action == "fondle ass":
                        if Trigger2 == "fondle ass" and Trigger != "lesbian": #if you're also fondling them,
                                $ Line = GirlA.Name + " also continues to fondle " + GirlB.Name + "'s ass"
                                $ Line = Line + renpy.random.choice([", stroking across her rear",
                                        ", the two of you taking turns in your motions",
                                        ", her fingers brushing against yours as you work",
                                        ", rubbing it vigorously",
                                        ", squeezing it vigorously",
                                        ", pressing firmly into it",
                                        ", kneeding it with slow undulating motions",
                                        ", moving with slow undulating motions"])
                        else:
                                $ Line = GirlA.Name + " continues to fondle " + GirlB.Name + "'s ass"
                                $ Line = Line + renpy.random.choice([", running fingers gently up her cleft",
                                        ", stroking across her rear",
                                        ", rubbing it vigorously",
                                        ", squeezing it vigorously",
                                        ", pressing firmly into it",
                                        ", kneeding it with slow undulating motions",
                                        ", moving with slow undulating motions"])

                        $ TempLust += 1 if ApprovalCheck(GirlA, 500, "I") else 0  # GirlA's lust
                        $ TempLust2 += 3 if GirlB.GirlLikeCheck(GirlA) >= 800 else 1
                        $ TempFocus += 1
    # end fondle ass Threeway                              /////////////////////////////////////////////////////////////////////////////


    elif Action == "insert ass":
                        if (Trigger == "insert ass" or Trigger2 == "insert ass") and Trigger != "lesbian": #if you're also fondling them,
                                $ Line = GirlA.Name + " also continues to stroke " + GirlB.Name + "'s ass"
                        else:
                                $ Line = GirlA.Name + " continues to stroke " + GirlB.Name + "'s ass"

                        $ Templine = renpy.random.choice([", stroking across her rim",
                                    ", stroking across her hole",
                                    ", circling it vigorously",
                                    "a",
                                    "b",
                                    "c",
                                    ", moving with slow undulating motions"])

                        #a, b, and c can change depending on other circumstances at the time.
                        if Templine == "a":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her fingers brush against your cock as it goes in"
                                elif Trigger == "insert ass" or Trigger2 == "insert ass":
                                        $ Templine = ", her fingers circling yours"
                                elif Trigger == "dildo anal" or Trigger2 == "dildo anal":
                                        $ Templine = ", her fingers brush against the dildo as it goes in"
                                else:
                                        $ Templine = ", running fingers gently up her cleft"
                        elif Templine == "b":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her fingers brushing up against your balls as you sink in"
                                elif Trigger == "insert ass" or Trigger2 == "insert ass":
                                        $ Templine = ", the two of you taking turns in your motions"
                                elif Trigger == "dildo anal" or Trigger2 == "dildo anal":
                                        $ Templine = ", her fingers run along the dildo as it slides by"
                                else:
                                        $ Templine = ", sliding firmly into it"
                        elif Templine == "c":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her fingers brush against your cock as it goes in"
                                elif Trigger == "insert ass" or Trigger2 == "insert ass":
                                        $ Templine = ", her fingers intertwine yours"
                                elif Trigger == "dildo anal" or Trigger2 == "dildo anal":
                                        $ Templine = ", her fingers brush against the dildo as it goes in"
                                else:
                                        $ Templine = ", moving inside it with slow undulating motions"

                        $ Line = Line + Templine

                        if not GirlB.Loose:
                                        $ TempLust2 -= 3
                        $ TempLust += 2 if ApprovalCheck(GirlA, 700, "I") else 1  # GirlA's lust
                        $ TempLust2 += 5 if GirlB.GirlLikeCheck(GirlA) >= 800 else 3
                        $ TempFocus += 1

    # end insert ass Threeway                             /////////////////////////////////////////////////////////////////////////////

    elif Action == "lick ass":
                        if (Trigger == "lick ass" or Trigger2 == "lick ass") and Trigger != "lesbian": #if you're also fondling them,
                                $ Line = GirlA.Name + " also continues to lick " + GirlB.Name + "'s ass"
                        else:
                                $ Line = GirlA.Name + " continues to lick " + GirlB.Name + "'s ass"

                        $ Templine = renpy.random.choice([", tonguing across her rim",
                                    ", stroking across her hole",
                                    ", circling it vigorously",
                                    "a",
                                    "b",
                                    "c",
                                    ", moving with slow undulating motions"])

                        #a, b, and c can change depending on other circumstances at the time.
                        if Templine == "a":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her tongue brushes against your cock as it goes in"
                                elif Trigger == "lick ass":
                                        $ Templine = ", her tongue brushing against yours as you work"
                                elif Trigger == "insert ass" or Trigger2 == "insert ass":
                                        $ Templine = ", her tongue slides along your fingers"
                                elif Trigger == "dildo anal" or Trigger2 == "dildo anal":
                                        $ Templine = ", her tongue brushes along the dildo as it goes in"
                                else:
                                        $ Templine = ", lapping into it vigorously"
                        elif Templine == "b":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her longue lapping against your balls as you sink in"
                                elif Trigger == "lick ass":
                                        $ Templine = ", you briefly kiss as you take turns"
                                elif Trigger == "insert ass" or Trigger2 == "insert ass":
                                        $ Templine = ", her tongue slides past your fingers"
                                elif Trigger == "dildo anal" or Trigger2 == "dildo anal":
                                        $ Templine = ", her tongue runs up against the dildo as it slides by"
                                else:
                                        $ Templine = ", sliding firmly into it"
                        elif Templine == "c":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her tongue brushes against your cock as it goes in"
                                elif Trigger == "lick ass":
                                        $ Templine = ", the two of you taking turns in your motions"
                                elif Trigger == "insert ass" or Trigger2 == "insert ass":
                                        $ Templine = ", her tongue slides past your fingers"
                                elif Trigger == "dildo anal" or Trigger2 == "dildo anal":
                                        $ Templine = ", her tongue runs up against the dildo as it slides by"
                                else:
                                        $ Templine = ", moving inside it with slow undulating motions"

                        $ Line = Line + Templine

                        $ TempLust += 3 if ApprovalCheck(GirlA, 800, "I") else 1  # GirlA's lust
                        $ TempLust2 += 4 if GirlB.GirlLikeCheck(GirlA) >= 800 else 2
                        $ TempFocus += 3

    # end lick ass Threeway                              /////////////////////////////////////////////////////////////////////////////

    elif Action == "masturbation":
                        call Girl_Self_Lines(GirlA,"T5",Trigger5)  #nee Rog*ue_Self_Lines
                        $ TempLust = 0

    # end Masturbation Threeway                              /////////////////////////////////////////////////////////////////////////////

    elif Action in ("kiss you", "kiss girl", "kiss both"):
                        if Trigger == "blow" and GirlA.Blow > 5 and Trigger4 == "kiss girl":
                                    $ Line = GirlA.Name + " also continues to kiss " + GirlB.Name
                                    $ Line = Line + renpy.random.choice([", occasionally taking a lick of your cock as well",
                                            ", licking along her cheek",
                                            ", nudging you out of her mouth to get a deep kiss in",
                                            ", taking the occasional lick down your shaft",
                                            ", nudging her aside to kiss the head of your cock"])
                        elif Trigger == "blow" and Trigger4 == "kiss girl":
                                    $ Line = GirlA.Name + " also continues to kiss " + GirlB.Name
                                    $ Line = Line + renpy.random.choice([", occasionally bumping into your cock as well",
                                            ", licking along her cheek",
                                            ", nudging you out of her mouth to get a deep kiss in",
                                            ", trailing kisses down her neck"])
                        else: #they're just kissing
                                    if Action == "kiss girl" or Mode == "lesbian":
                                        if Trigger == "lesbian" and Partner != GirlA:
                                                $ Line = GirlA.Name + " continues to make out with " + GirlB.Name
                                        else:
                                                $ Line = GirlA.Name + " also continues to make out with " + GirlB.Name
                                        $ Line = Line + renpy.random.choice([", occasionally coming up for air",
                                                ", licking along her cheek",
                                                ", grabbing her face in both hands",
                                                ", their tongues swirl around each other",
                                                ", occasionally nibbling at her ears",
                                                ", trailing kisses down her neck"])
                                    elif Action == "kiss you":
                                        $ Line = GirlA.Name + " also continues to make out with you"
                                        $ Line = Line + renpy.random.choice([", occasionally coming up for air",
                                                ", licking along your cheek",
                                                ", grabbing your face in both hands",
                                                ", your tongues swirl around each other",
                                                ", occasionally nibbling at your ears",
                                                ", trailing kisses down your neck"])
                                    else: #Action == "kiss both":
                                        $ Line = GirlA.Name + " also continues to make out with both of you"
                                        $ Line = Line + renpy.random.choice([", occasionally coming up for air",
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
                        $ TempLust += 1 if ApprovalCheck(GirlA, 500, "I") else 0  # GirlA's lust
                        $ TempLust += 1 if GirlA.GirlLikeCheck(GirlB) >= 800 else 0
                        $ TempLust2 += 2 if GirlB.GirlLikeCheck(GirlA) >= 800 else 1
                        $ TempFocus += 1
    # end Kissing Threeway                              /////////////////////////////////////////////////////////////////////////////

    elif Action == "watch":
                        $ Line = GirlA.Name + " continues to watch the two of you"
                        $ Line = Line + renpy.random.choice([", shifting uncomfortably",
                                        ", readjusting her clothes",
                                        ", glancing at the door",
                                        ", taking in " + GirlB.Name + "'s body",
                                        ", transfixed by the action"])
                        $ TempLust += 1 if GirlA.GirlLikeCheck(GirlB) >= 600 else 0  # GirlA's lust
                        $ TempLust += 2 if GirlA.GirlLikeCheck(GirlB) >= 800 else 1  # GirlA's lust
                        $ TempLust2 += 1 if ApprovalCheck(GirlB, 500, "I") else 0
                        $ TempLust2 += 1 if ApprovalCheck(GirlB, 700, "I") else 0
                        $ TempFocus += 1
    # end watching Threeway                              /////////////////////////////////////////////////////////////////////////////

    else:
        "Nothing triggered. 1:[Trigger], 2:[Trigger2], 3:[Trigger3], 4:[Trigger4], 5:[Trigger5]" #diagnostic

    # Wrap-up
    $ TempLust2 += 2
    if Mode == "lesbian":
            $ PrimaryLust += (TempLust * 3)
            $ SecondaryLust += (TempLust2 * 3)
    else:
            $ SecondaryLust += TempLust
            $ PrimaryLust += TempLust2

    $ Player.Focus += TempFocus
    return

label Three_Change(LeadGirl = Primary, SecondGirl = Partner, D20S=0, PrimaryLust=0, SecondaryLust=0):
        #this is called when the player wants to change over a threeway behavior, and revolves around the partner girl
        # if changes what the Partner does to the lead girl
        # for Threeway secondary activity: #nee Rogue_Threeway_Set("preset", 0, Trigger4, "ActiveGirl")
        # call Three_Change(Primary,Partner)
        # call Threeway_Set(KittyX,"preset",0,Trigger4,RogueX)
        if LeadGirl not in TotalGirls:
                return
        if Partner == LeadGirl:
                "Let Oni know that both roles are set to [Girl.Name]."
                return
        menu Three_Change_Menu:
            ch_p "Hey [Partner.Name]. . ."
            "about [LeadGirl.Name]. . .": #about the primary girl. . .
                menu:
                    ch_p "about [LeadGirl.Name]. . ."
                    "why don't you kiss her?" if Trigger5 != "kiss girl" and Trigger5 != "kiss both":
                                    call Threeway_Set(SecondGirl,"kiss girl", 0, Trigger4, LeadGirl)
                    "why don't you grab her tits?" if Trigger4 != "fondle breasts":
                                    call Threeway_Set(SecondGirl,"fondle breasts",0, Trigger4, LeadGirl)
                    "why don't you suck her breasts?" if Trigger4 != "suck breasts":
                                    call Threeway_Set(SecondGirl,"suck breasts",0, Trigger4, LeadGirl)
                    "why don't you finger her?" if Trigger4 != "fondle pussy":
                                    call Threeway_Set(SecondGirl,"fondle pussy",0, Trigger4, LeadGirl)
                    "why don't you go down on her?" if Trigger4 != "lick pussy":
                                    call Threeway_Set(SecondGirl,"lick pussy", 0, Trigger4, LeadGirl)
                    "why don't you grab her ass?" if Trigger4 != "fondle ass":
                                    call Threeway_Set(SecondGirl,"fondle ass", 0, Trigger4, LeadGirl)
                    "why don't you lick her ass?" if Trigger4 != "lick ass":
                                    call Threeway_Set(SecondGirl,"lick ass", 0, Trigger4, LeadGirl)
                    "wait, I meant. . .":
                                    jump Three_Change_Menu

            "about me. . .":
                menu:
                    ch_p "about me. . ."
                    "why don't you kiss me?" if Trigger5 != "kiss you" and Trigger5 != "kiss both":
                                    call Threeway_Set(SecondGirl,"kiss you", 0, Trigger4, LeadGirl)
                    "maybe take me in hand?" if Trigger4 != "hand":
                                    call Threeway_Set(SecondGirl,"hand", 0, Trigger4, LeadGirl)
                    "maybe give me a lick?" if Trigger4 != "blow":
                                    call Threeway_Set(SecondGirl,"blow", 0, Trigger4, LeadGirl)
                    "why don't you give me a show?" if Trigger4 != "masturbation":
                                    call Threeway_Set(SecondGirl,"masturbation", 0, Trigger4, LeadGirl)
                    "wait, I meant. . .":
                                    jump Three_Change_Menu
            "never mind.":
                pass
        return

label Threeway_Set(GirlA=Secondary,Preset = 0, Mode = 0, Action = Trigger4, GirlB = Primary, State = "watcher", TempLust = 0, TempLust2 = 0, TempFocus = 0): #rkeljsv
            #nee Rog*ue_Threeway_Set(Preset = 0, Mode = 0,
            # Action defaults to Trigger4, the action of the seondary girl and GirlB to the lead girl in the scene
            # In lesbian mode, Action becomes Trigger3, the secondary action of the primary girl, and GirlB is the secondary girl
            # If Set gets passed a preset, it chooses that preset, otherwise it chooses one randomly
            # for Lesbian: call Threeway_Set(Primary,"suck breasts", "lesbian", Trigger3,Secondary)
            # for Threeway: call Threeway_Set(SecondGirl,"fondle breasts",0, Trigger4, LeadGirl)
            # ThreeCount is a value that gets set to a few digits lower then the current Round
            # The girl will not arbitrarily change motions until after this value has been passed.

            $ D20 = renpy.random.randint(1, 20)
            if not Preset:
                    #if no preset is offered
                    if Mode == "lesbian": #called from Les_Change()
                            #If it's in lesbian mode, there is already a trigger set, and the roll is good, continue
                            if Trigger3 == "kiss girl" and GirlA.Lust <= 20 and GirlA.Org < 1:
                                    # If kissing at low lust, keep doing it
                                    return
                            elif Trigger3 and ThreeCount <= Round:
                                    # If a Trigger3 is already set and it's under the count, return
                                    return
                    elif Trigger4 and D20 < 15 and Trigger4 != "watch":
                                    #If there is a trigger, it's not set to "watch," and the roll is good, continue
                                    return
                    elif Trigger4 and ThreeCount <= Round:
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

            if Trigger == "lesbian":
                    # if this was sent from a Lesbian action. . .
                    $ State = "lesbian"
                    $ Options = ["kiss girl","kiss girl"]
                    if Preset in ("hand","blow","kiss you","kiss both"):
                            #if you send it presets that you want the other girl to touch you. . .
                            $ State = "threeway"
                    elif Preset:
                            pass
                    elif GirlA.GirlLikeCheck(GirlB) >= 600 and ApprovalCheck(GirlA, 500, "I"):
                            #if she likes the other girl, and is unihibited. . .
                            pass
                    else:
                            #this returns if she doesn't like the other girl enough to do anything more.
                            if Action != "kiss girl":
                                    $ Line = GirlA.Name + " gives " + GirlB.Name + " a passionate kiss"
                                    $ Action = "kiss girl"
                                    $ Trigger3 = "kiss girl"
                                    if "lesbian" not in GirlA.RecentActions:
                                            $ GirlA.Les += 1
                                            $ GirlA.RecentActions.append("lesbian")
                            return
            elif not ApprovalCheck(GirlA, 500, "I"):
                    # If GirlA is too timid to do anything, stick to neutral options
                    pass
            elif GirlA.GirlLikeCheck(GirlB) >= 600 and ApprovalCheck(GirlA, (1500-(10*GirlA.Les)-(10*(GirlA.GirlLikeCheck(GirlB)-60)))):
                    #If she likes both of you a lot, threeway
                    $ State = "threeway"
            elif ApprovalCheck(GirlA, 1000):
                    #If she likes you well enough, Hetero
                    $ State = "hetero"
            elif GirlA.GirlLikeCheck(GirlB) >= 700:
                    #if she doesn't like you but likes the other girl, lesbian
                    $ State = "lesbian"

            if State == "lesbian" or State == "threeway":
                #if she's into girls, add girl-touching options
                $ Options.extend(("fondle breasts","suck breasts","fondle pussy","fondle ass","kiss girl"))

                if ApprovalCheck(GirlA, 800, "I") or GirlA.GirlLikeCheck(GirlB) >= 800:
                    $ Options.append("lick pussy")
                if ApprovalCheck(GirlA, 900, "I") and GirlA.GirlLikeCheck(GirlB) >= 900:
                    $ Options.append("lick ass")


            if State == "hetero" or State == "threeway":
                #if she's into you, add you-touching options
                if Trigger == "anal":
                    $ Options.extend(("hand","kiss you","kiss you"))
                else:
                    $ Options.extend(("hand","blow","kiss you"))
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
                elif ApprovalCheck(GirlA, 750, "I") or ApprovalCheck(GirlA, 1500):
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
                    $ Line = GirlA.Name + " shifts her position"
            elif not Trigger4 or Trigger4 == "masturbation":
                    #If this is the first action,
                    $ Line = GirlA.Name + " moves closer"
            else:
                    #If this is a new action
                    $ Line = GirlA.Name + " shifts her position"


            if Options[0] == "masturbation":
                        $ Action = "masturbation"
                        call Girl_Self_Lines(GirlA,"T5",Trigger5)  #nee Rog*ue_Self_Lines
            elif Options[0] == "hand":
                        call Seen_First_Peen(GirlA,GirlB,React=1)
                        $ Line = Line + " before she slides her hand down and firmly grabs your dick"
                        $ Action = "hand"
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
                        $ TempLust += 2 if GirlA.Lust < 60 else 0
                        $ TempLust += 2 if GirlA.Hand > 2 else 0
                        $ GirlA.Addict -= 1 if D20 > 10 else 2
            elif Options[0] == "blow":
                        call Seen_First_Peen(GirlA,GirlB,React=1)
                        $ Line = Line + " before she slides down and begins to slowly lick your cock"
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
                        $ Action = "blow"
                        $ Approval = 4

                        $ TempFocus += 20 if Player.Focus > 60 else 10
                        $ TempLust += 2 if GirlA.Lust > 80 else 1
                        $ GirlA.Addict -= 2
            #the above three do not apply to lesbian actions.

            elif Options[0] == "fondle breasts":

                        $ Line = Line + " and slides her hands along " + GirlB.Name + "'s breasts"
                        $ Action = "fondle breasts"
                        if "lesbian" not in GirlA.RecentActions:
                                $ GirlA.Les += 1
                                $ GirlA.RecentActions.append("lesbian")
                        if "lesbian" not in GirlB.RecentActions:
                                $ GirlB.Les += 1
                                $ GirlB.RecentActions.append("lesbian")
                        $ TempLust += 2 if ApprovalCheck(GirlA, 500, "I") else 1  # GirlA's lust
                        $ TempLust2 += 4 if GirlB.GirlLikeCheck(GirlA) >= 800 else 2
                        $ TempFocus += 1
            elif Options[0] == "suck breasts":

                        $ Line = Line + " and slurps " + GirlB.Name + "'s nipple into her mouth"
                        $ Action = "suck breasts"
                        if "lesbian" not in GirlA.RecentActions:
                                $ GirlA.Les += 1
                                $ GirlA.RecentActions.append("lesbian")
                        if "lesbian" not in GirlB.RecentActions:
                                $ GirlB.Les += 1
                                $ GirlB.RecentActions.append("lesbian")
                        $ TempLust += 2 if ApprovalCheck(GirlA, 500, "I") else 1  # GirlA's lust
                        $ TempLust2 += 5 if GirlB.GirlLikeCheck(GirlA) >= 800 else 2
                        $ TempFocus += 1
            elif Options[0] == "fondle pussy":

                        $ Line = Line + " and runs her finger along " + GirlB.Name + "'s pussy"
                        $ Action = "fondle pussy"
                        if "lesbian" not in GirlA.RecentActions:
                                $ GirlA.Les += 1
                                $ GirlA.RecentActions.append("lesbian")
                        if "lesbian" not in GirlB.RecentActions:
                                $ GirlB.Les += 1
                                $ GirlB.RecentActions.append("lesbian")
                        $ TempLust += 2 if ApprovalCheck(GirlA, 500, "I") else 1  # GirlA's lust
                        $ TempLust2 += 5 if GirlB.GirlLikeCheck(GirlA) >= 800 else 3
                        $ TempFocus += 2
            elif Options[0] == "lick pussy":

                        $ Line = Line + " and runs her tongue along " + GirlB.Name + "'s pussy"
                        $ Action = "lick pussy"
                        if "lesbian" not in GirlA.RecentActions:
                                $ GirlA.Les += 1
                                $ GirlA.RecentActions.append("lesbian")
                        if "lesbian" not in GirlB.RecentActions:
                                $ GirlB.Les += 1
                                $ GirlB.RecentActions.append("lesbian")
                        $ TempLust += 3 if ApprovalCheck(GirlA, 600, "I") else 1  # GirlA's lust
                        $ TempLust2 += 8 if GirlB.GirlLikeCheck(GirlA) >= 800 else 5
                        $ TempFocus += 3
            elif Options[0] == "fondle ass":

                        $ Line = Line + " and gives " + GirlB.Name + "'s ass a firm squeeze"
                        $ Action = "fondle ass"
                        if "lesbian" not in GirlA.RecentActions:
                                $ GirlA.Les += 1
                                $ GirlA.RecentActions.append("lesbian")
                        if "lesbian" not in GirlB.RecentActions:
                                $ GirlB.Les += 1
                                $ GirlB.RecentActions.append("lesbian")
                        $ TempLust += 1 if ApprovalCheck(GirlA, 400, "I") else 0  # GirlA's lust
                        $ TempLust2 += 3 if GirlB.GirlLikeCheck(GirlA) >= 600 else 2
                        $ TempFocus += 1
            elif Options[0] == "lick ass":

                        $ Line = Line + " and starts to lick around " + GirlB.Name + "'s ass"
                        $ Action = "lick ass"
                        if "lesbian" not in GirlA.RecentActions:
                                $ GirlA.Les += 1
                                $ GirlA.RecentActions.append("lesbian")
                        if "lesbian" not in GirlB.RecentActions:
                                $ GirlB.Les += 1
                                $ GirlB.RecentActions.append("lesbian")
                        $ TempLust += 3 if ApprovalCheck(GirlA, 800, "I") else 1  # GirlA's lust
                        $ TempLust2 += 6 if GirlB.GirlLikeCheck(GirlA) >= 800 else 4
                        $ TempFocus += 2

            elif Options[0] == "kiss girl" or Mode == "lesbian":
                        $ Line = Line + " and gives " + GirlB.Name + " a passionate kiss"
                        $ Action = "kiss girl"
                        if Mode != "lesbian" and "kiss you" in Options:
                                if Trigger == "kiss you":
                                        $ Action = "kiss both"
                                elif Trigger3 == "kiss you":
                                        $ Action = "kiss both"
                                elif Trigger4 == "kiss you":
                                        $ Action = "kiss both"
                        $ TempFocus += 1
            elif Options[0] == "kiss you":
                        $ Line = Line + " and gives you a passionate kiss"
                        $ Action = "kiss you"
                        if "kiss girl" in Options:
                                if Trigger == "kiss you":
                                        $ Action = "kiss both"
                                elif Trigger3 == "kiss you":
                                        $ Action = "kiss both"
                                elif Trigger4 == "kiss you":
                                        $ Action = "kiss both"
                        $ TempLust += 1
                        $ TempFocus += 1

            else:
                        $ Line = GirlA.Name + " is just watching the two of you intently"
                        $ Action = "watch"
                        $ TempLust += 1 if GirlA.GirlLikeCheck(GirlB) >= 600 else 0  # GirlA's lust
                        $ TempLust += 2 if GirlA.GirlLikeCheck(GirlB) >= 800 else 1  # GirlA's lust
                        $ TempLust2 += 1 if ApprovalCheck(GirlB, 500, "I") else 0
                        $ TempLust2 += 1 if ApprovalCheck(GirlB, 700, "I") else 0
                        $ TempFocus += 1

            if Action == "kiss girl" or Action == "kiss both":
                        #If there's a semi-lesbian make-out. . .
                        if "lesbian" not in GirlA.RecentActions:
                                $ GirlA.Les += 1
                                $ GirlA.RecentActions.append("lesbian")
                        if "lesbian" not in GirlB.RecentActions:
                                $ GirlB.Les += 1
                                $ GirlB.RecentActions.append("lesbian")
                        $ TempLust += 1 if ApprovalCheck(GirlA, 500, "I") else 0  # GirlA's lust
                        $ TempLust += 1 if GirlA.GirlLikeCheck(GirlB) >= 800 else 0
                        $ TempLust2 += 2 if GirlB.GirlLikeCheck(GirlA) >= 800 else 1
                        $ TempFocus += 1

            # Wrap-up
            if Preset:
                    $ ThreeCount = Round - 2
            else:
                    #this sets a delay before the values change again on their own
                    $ ThreeCount = Round - 1
            $ TempLust2 += 2
            if Mode == "lesbian":
                    #Sets Primary Girl's secondary action
                    $ Trigger3 = Action
                    $ PrimaryLust += (TempLust * 3)
                    $ SecondaryLust += (TempLust2 * 3)
            elif Mode == "start":
                    #Sets Rog*ue's action and Lust if this is a starting action
                    $ Trigger4 = Action
                    $ GirlA.Lust += TempLust2
            else:
                    #Sets Secondary girl's action
                    $ Trigger4 = Action
                    $ SecondaryLust += TempLust
                    $ PrimaryLust += TempLust2
            if Preset:
                    #if this was done at your direction, apply lusts
                    $ GirlA.Lust += TempLust
                    $ GirlB.Lust += TempLust2
            $ Player.Focus += TempFocus

            return

label Dirty_Talk(Girl = Primary, D20=0, TempCheck=0, TempLine=0, TempTrigger=Trigger4, ActiveGirl=0):  #rkeljsv


    if Trigger == "strip" or not Trigger:
            #if nothing that involves dirty talk. . .
            return

    $ D20 = renpy.random.randint(1, 4)
    # 1 is nobody, 2 and 3 is primary, 4 is secondary


    if D20 == 1:
            #RNG said no
            return
    elif D20 == 4 and Partner in TotalGirls:
            #RNG said partner says a line
            $ Girl = Partner
            $ ActiveGirl = Primary
            $ TempCheck = Trigger4
            $ TempTrigger = Trigger4
    else: #if D20 == 2 or 3
            #RNG said lead girl says a line
            $ Girl = Primary
            $ ActiveGirl = Secondary
            $ TempCheck = Trigger
            $ TempTrigger = Trigger3

    $ D20 = renpy.random.randint(1, 20)

    if "vocal" not in Girl.Traits:
            #if she's non-vocal, she will remain silent
            if Girl.Lust >= 60:
                pass
            else:
                return
    elif D20 >= 15 or Girl.OCount >= 5:
            #drops it down to the generic grunts if roll over 15
            pass

    elif Girl == RogueX:
            # if the Girl is Rogue. . .
            if Trigger == "lesbian" or (Secondary == RogueX and TempTrigger not in ("hand","blow","masturbation")):
                    #if this is a lesbian action, or if the threesome action is girl-focused

                    if "unseen" not in RogueX.RecentActions and D20 <= 5:
                            #if they know you're watching, there is a 3/10 or 2/5 chance
                            $ TempLine = "Hmm, enjoying the show, "+RogueX.Petname+"?" #you watching
                    elif D20 <= 10:
                            pass
                    elif TempTrigger == "fondle breasts":
                            $ TempLine = "Your titties feel so nice, "+ActiveGirl.Name+"." #fondle breasts
                    elif TempTrigger == "suck breasts":
                            $ TempLine = "Your titties taste so good, "+ActiveGirl.Name+"." #suck breasts
                    elif TempTrigger == "fondle pussy":
                            $ TempLine = "You're sucking me in, "+ActiveGirl.Name+"." #fondle pussy
                    elif TempTrigger == "lick pussy":
                            $ TempLine = "You taste so good, "+ActiveGirl.Name+"." #lick pussy

                    if not TempLine:
                            #if nothing else is selected, or if D20: 1-3, or if D20: 14-15
                            $ TempLine = renpy.random.choice([
                                    "Touch'n ya is so amazing, " + ActiveGirl.Name + ".",
                                    "Your body feels so amazing. . .",
                                    "Mmmm. . .right there.",
                                    "Ya like that, " + ActiveGirl.Name + "?"
                                    ])

            elif TempCheck == "masturbation":
                    if "unseen" not in RogueX.RecentActions:
                            #if she knows you're watching
                            if D20 <= 3:
                                # it's under a 3 roll
                                if "cockout" in Player.RecentActions:
                                    # Your cock's out
                                    $ TempLine = renpy.random.choice([
                                                "Could I get some of that, " + RogueX.Petname + "?",
                                                "Why don'tcha bring that over here, " + RogueX.Petname + "?"
                                                ])
                                else:
                                    # Your cock's not out
                                    $ TempLine = renpy.random.choice([
                                                "Why so shy, " + RogueX.Petname + "?",
                                                "I'm showing mine, where's yours?"
                                                ])
                            else:
                                    # It's over a 3 roll
                                    $ TempLine = renpy.random.choice([
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
                    elif RogueX.SEXP <= 20 or TempCheck == "kiss you":
                            #If she's relatively inexperienced
                            $ TempLine = renpy.random.choice([
                                    "Touching ya is so amazing, " + RogueX.Petname + ".",
                                    "Every time you touch me. . . it's like, I can't even put it into words.",
                                    "Mmmm. . .right there.",
                                    "Am I doing that right?",
                                    "Ya like that, " + RogueX.Petname + "?"
                                    ])
                    elif TempCheck == "hand":
                        $ TempLine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "Seems like you like my hand, huh, " + RogueX.Petname + "?",
                                    "I can feel you get harder in my hand. . .",
                                    ])
                    elif TempCheck == "blow":
                        $ TempLine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "You taste so nice, " + RogueX.Petname + ".",
                                    "I can feel you get harder in my mouth. . .",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",
                                    ])
                    elif TempCheck == "titjob":
                        $ TempLine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + RogueX.Petname + ".",
                                    "I can feel you get harder in there. . ."
                                    ])
                    elif TempCheck == "sex" or TempCheck == "anal":
                        if D20 <= 3 and TempCheck == "anal" and RogueX.Loose <= 1:
                            $ TempLine = "It. . .hurts. But it kinda feels good, too." #anal
                        else:
                            $ TempLine = renpy.random.choice([
                                        "Your cock is so warm. . .",
                                        "Ohhh. . .that's sooo good.",
                                        "Ung, so deep. . .",
                                        "Keep it up, keep it up. . .",
                                        "Oh, don't stop. . .",
                                        "I can feel you get harder inside me. . ."
                                        ])

                    if not TempLine:
                        #if nothing else is selected, or if D20 < 10
                        if Primary == RogueX:
                                $ TempLine = renpy.random.choice([
                                        "I want ya so bad, " + RogueX.Petname + ".",
                                        "Your touch is so amazin, " + RogueX.Petname + ".",
                                        "Oooh, right there. . .",
                                        "More, gimme more!",
                                        "I'm all yours, " + RogueX.Petname + ". Take me however ya want.",
                                        "I love it when ya do that, " + RogueX.Petname + ".",
                                        "I love the look you get on your face, " + RogueX.Petname + "."
                                        ])
                        else:
                                $ TempLine = renpy.random.choice([
                                        "I want ya so bad, " + RogueX.Petname + ".",
                                        "Could I get some of that, " + RogueX.Petname + "?",
                                        "Think ya could maybe share that, " + ActiveGirl.Name + "?",
                                        "Come on over here, " + RogueX.Petname + ". Take me however ya want.",
                                        "So that's what you look like from this angle.",
                                        "I love the look you get on your face, " + RogueX.Petname + ".",
                                        "That's right, give it to her.",
                                        "You're really getting into it, " + ActiveGirl.Name + "."
                                        ])
    #end Rogue
    elif Girl == KittyX:
            # if the Girl is Kitty. . .
            if Trigger == "lesbian" or (Secondary == KittyX and TempTrigger not in ("hand","blow","masturbation")):
                    #if this is a lesbian action, or if the threesome action is girl-focused

                    if "unseen" not in KittyX.RecentActions and D20 <= 7:
                            #if they know you're watching, there is a 3/10 or 2/5 chance
                            $ TempLine = "Hmm, like what you see, "+KittyX.Petname+"?" #you watching
                    elif TempTrigger == "fondle breasts":
                        if ActiveGirl in (EmmaX,StormX):
                            $ TempLine = "I'm so jelly here "+ActiveGirl.Name+"." #fondle breasts
                        else:
                            $ TempLine = "I love these tits, "+ActiveGirl.Name+"." #fondle breasts
                    elif TempTrigger == "suck breasts":
                        if ActiveGirl in (EmmaX,StormX):
                            $ TempLine = "These tits are {i}amazing,{/i} "+ActiveGirl.Name+"." #fondle breasts
                        else:
                            $ TempLine = "Hmm, you taste so good, "+ActiveGirl.Name+"." #suck breasts
                    elif TempTrigger == "fondle pussy":
                            $ TempLine = "So wet, "+ActiveGirl.Name+"." #fondle pussy
                    elif TempTrigger == "lick pussy":
                        if ActiveGirl == RogueX and RogueX.Pubes:
                            $ TempLine = "I love your little stripe, Rogue." #lick pussy
                        else:
                            $ TempLine = "You're drowning me here, "+ActiveGirl.Name+"." #lick pussy

                    if not TempLine:
                            #if nothing else is selected, or if D20: 1-3, or if D20: 14-15
                            $ TempLine = renpy.random.choice([
                                    "You're so amazing, " + ActiveGirl.Name + ".",
                                    "You know how to push" + KittyX.like + "every one of my buttons. . .",
                                    "Heh. . .{i}somebody{/i} seems to like that.",
                                    "That's" + KittyX.like + "{i}so{/i} good.",
                                    "You taste so good. . ."
                                    ])

            elif TempCheck == "masturbation":
                    if "unseen" not in KittyX.RecentActions:
                            #if she knows you're watching
                            if D20 <= 3:
                                # it's under a 3 roll
                                if "cockout" in Player.RecentActions:
                                    # Your cock's out
                                    $ TempLine = renpy.random.choice([
                                                "Hmm, I'd like some of that, " + KittyX.Petname + "?",
                                                "Could I get a taste, " + KittyX.Petname + "?"
                                                ])
                                else:
                                    # Your cock's not out
                                    $ TempLine = renpy.random.choice([
                                                "Feeling shy, " + KittyX.Petname + "?",
                                                "How 'bout a little tat for tit?"
                                                ])
                            else:
                                    # It's over a 3 roll
                                    $ TempLine = renpy.random.choice([
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
                    elif KittyX.SEXP <= 30 or TempCheck == "kiss you":
                            #If she's relatively inexperienced
                            $ TempLine = renpy.random.choice([
                                    "You're so amazing, " + KittyX.Petname + ".",
                                    "You know how to push, like, every one of my buttons. . .",
                                    "Heh. . .{i}somebody{/i} seems to like that.",
                                    "That's, like, {i}so{/i} good."
                                    ])
                    elif TempCheck == "hand":
                        $ TempLine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I love the way it"+KittyX.like+"feels in my hands.",
                                    "Seems like you like my hand, huh, " + RogueX.Petname + "?",
                                    "I can feel you get harder in my hand. . .",
                                    ])
                    elif TempCheck == "blow":
                        if D20 <= 3:
                            ch_k "I hope you don't think I'm[KittyX.like]a slut for saying this. . ."
                            $ TempLine = "but I love how you taste, " + KittyX.Petname + "."
                        else:
                            $ TempLine = renpy.random.choice([
                                        "So warm. . .",
                                        "You taste so good, " + KittyX.Petname + ".",
                                        "You're getting harder in my mouth. . .",
                                        "Mmhmhm. . .",
                                        "-gulp-. . .",
                                        ])
                    elif TempCheck == "titjob":
                        $ TempLine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + KittyX.Petname + ".",
                                    "I can feel you get harder in there. . ."
                                    ])
                    elif TempCheck == "sex" or TempCheck == "anal":
                        if D20 <= 3 and TempCheck == "anal" and KittyX.Loose <= 1:
                            $ TempLine = "Please. . .go slow, 'kay?  You feel so {i}big{/i}."
                        else:
                            $ TempLine = renpy.random.choice([
                                        "Your cock is so warm. . .",
                                        "Ohhh. . .that's sooo good.",
                                        "Mmm, you feel so huge. . .",
                                        "Ung, so deep. . .",
                                        "Oooohh. . .just like {i}that{/i}.",
                                        "Keep it up, keep it up. . .",
                                        "Oh, don't stop. . .",
                                        "Did you just get harder?"
                                        ])

                    if not TempLine:
                        #if nothing else is selected, or if D20 > 10
                        if Primary == KittyX:
                                $ TempLine = renpy.random.choice([
                                            "This is {i}so{/i} hot, " + KittyX.Petname + ".",
                                            "I think I just"+KittyX.like+"discovered one of your other mutant powers, " + KittyX.Petname + ".",
                                            "I like it."+KittyX.Like+"a {i}lot{/i}.",
                                            "Oooh, that's it. . .",
                                            "More, gimme more!",
                                            "You're looking so cute, " +KittyX.Petname + "!",
                                            "I've never wanted a guy like I want you, " + KittyX.Petname + "."
                                            ])
                        else:
                                $ TempLine = renpy.random.choice([
                                            "Don't take all the fun, " + ActiveGirl.Name + ".",
                                            "I could use some attention over here, " + KittyX.Petname + ".",
                                            "I got something over here for you, " + KittyX.Petname + ".",
                                            "You're looking pretty good from over here.",
                                            "Looks like he likes the way you do that.",
                                            "Make sure you save some for {i}me{/i}!",
                                            "You two look {i}so{/i} sexy doing that.",
                                            "I can't believe you can take all of him like that!",
                                            "That looks like fun, " + ActiveGirl.Name + "."
                                            ])
    #end Primary Kitty
    elif Girl == EmmaX:
            # if the Girl is Emma. . .
            if Trigger == "lesbian" or (Secondary == EmmaX and TempTrigger not in ("hand","blow","masturbation")):
                    #if this is a lesbian action, or if the threesome action is girl-focused

                    if "unseen" not in EmmaX.RecentActions and D20 <= 5:
                            #if they know you're watching, there is a 3/10 or 2/5 chance
                            $ TempLine = "Are you enjoying the performance, "+EmmaX.Petname+"?" #you watching
                    elif TempTrigger == "fondle breasts" or TempTrigger == "suck breasts":
                            if ActiveGirl == KittyX:
                                $ TempLine = "Oh my, these breasts are adorable!" #fondle breasts
                            else:
                                $ TempLine = "These really are wonderfully. . . pert." #fondle breasts
                    elif TempTrigger == "fondle pussy":
                                $ TempLine = "Such pressure, "+ActiveGirl.Name+"." #fondle pussy
                    elif TempTrigger == "lick pussy":
                            if ActiveGirl == LauraX:
                                $ TempLine = "Oh yes, that is a Howlett." #lick pussy
                            else:
                                $ TempLine = "What an exotic flavor, " + ActiveGirl.Name + "." #lick pussy
                    if not TempLine:
                            #if nothing else is selected, or if D20: 1-3, or if D20: 14-15
                            $ TempLine = renpy.random.choice([
                                    "Incredible, " + ActiveGirl.Name + ".",
                                    "You're surprisingly skilled at this. . .",
                                    "Well, that certainly got a positive response.",
                                    "Exceptional, darling.",
                                    "Delicious. . ."
                                    ])

            elif TempCheck == "masturbation":
                    if "unseen" not in EmmaX.RecentActions:
                            #if she knows you're watching
                            if D20 <= 3:
                                # it's under a 3 roll
                                if "cockout" in Player.RecentActions:
                                    # Your cock's out
                                    $ TempLine = renpy.random.choice([
                                                "Oh, I could use some of that, " + EmmaX.Petname + ".",
                                                "Why don't you join me over here, " + EmmaX.Petname + "?"
                                                ])
                                else:
                                    # Your cock's not out
                                    $ TempLine = renpy.random.choice([
                                                "Feeling shy, " + EmmaX.Petname + "?",
                                                "I feel like you aren't enjoying the show."
                                                ])
                            else:
                                    # It's over a 3 roll
                                    $ TempLine = renpy.random.choice([
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
                    elif EmmaX.SEXP <= 30 or TempCheck == "kiss you":
                            #If she's relatively inexperienced
                            $ TempLine = renpy.random.choice([
                                    "You're incredible, " + EmmaX.Petname + ".",
                                    "You're surprisingly skilled at this. . .",
                                    "Well, that certainly got a positive response.",
                                    "Exceptional work, darling.",
                                    ])
                    elif TempCheck == "hand":
                        $ TempLine = renpy.random.choice([
                                    "Your cock is so very warm. . .",
                                    "I trust you're enjoying the massage?",
                                    "I take it you're enjoying yourself, " + EmmaX.Petname + "?",
                                    "I can feel you grow harder. . .",
                                    ])
                    elif TempCheck == "blow":
                        $ TempLine = renpy.random.choice([
                                    "So delicious. . .",
                                    "I must say, I enjoy the flavor, " + EmmaX.Petname + ".",
                                    "I can feel you get harder in my mouth. . .",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",
                                    ])
                    elif TempCheck == "titjob":
                        $ TempLine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + EmmaX.Petname + ".",
                                    "Don't get lost in there now . .",
                                    "I can feel you get harder in there. . ."
                                    ])
                    elif TempCheck == "sex" or TempCheck == "anal":
                            $ TempLine = renpy.random.choice([
                                    "Mmmm, give me more like that. . .",
                                    "Nngh, how filling. . .",
                                    "Ung, so deep. . .",
                                    "Keep it up, keep it up. . .",
                                    "Oh, don't stop. . .",
                                    "I can feel you get harder inside me. . ."
                                    ])

                    if not TempLine:
                        #if nothing else is selected, or if D20 > 10
                        if Primary == EmmaX:
                                $ TempLine = renpy.random.choice([
                                        "I'm overwhelmed, " + EmmaX.Petname + ".",
                                        "Well now we have another skill to develop, " + EmmaX.Petname + ".",
                                        "Oooh, that's lovely. . .",
                                        "More, I want more!",
                                        "You're simply adorable, " + EmmaX.Petname + ".",
                                        "Ooh, you'll {i}have{/i} to do that one again. . .",
                                        "You certainly do leave an impression, " + EmmaX.Petname + "."
                                        ])
                        else:
                                $ TempLine = renpy.random.choice([
                                        "Oh " + EmmaX.Petname + "? Don't keep me waiting.",
                                        "Oh " + ActiveGirl.Name + "? Could you share some of that?",
                                        "Come on over here, " + EmmaX.Petname + ", ravish me.",
                                        "You certainly do put on a show.",
                                        "You're simply adorable, " + EmmaX.Petname + ".",
                                        "Nngh, give it to her.",
                                        "You seem to be enjoying yourself, " + ActiveGirl.Name + "."
                                        ])
            #End Emma's dirty talk lines
    #end Primary Emma
    elif Girl == LauraX:
            # if the Girl is Laura. . .
            if ApprovalCheck(LauraX, 1500):
                    $ D20 -= 5
            elif ApprovalCheck(LauraX, 1200):
                    $ D20 -= 3
            if D20 >= 10:
                    #drops it down to the generic grunts
                    pass
            elif Trigger == "lesbian" or (Secondary == LauraX and TempTrigger not in ("hand","blow","masturbation")):
                    #if this is a lesbian action, or if the threesome action is girl-focused

                    if "unseen" not in LauraX.RecentActions and D20 <= 5:
                            #if they know you're watching, there is a 3/10 or 2/5 chance
                            $ TempLine = "Looking good, "+LauraX.Petname+"?" #you watching
                    elif TempTrigger == "fondle breasts":
                            if ActiveGirl in (EmmaX,StormX):
                                $ TempLine = "These things are huge." #fondle breasts
                            else:
                                $ TempLine = "Your titties feel so nice, "+ActiveGirl.Name+"." #fondle breasts
                    elif TempTrigger == "suck breasts":
                            $ TempLine = "Hmm, tasty." #suck breasts
                    elif TempTrigger == "fondle pussy":
                                $ TempLine = "Cozy in there." #fondle pussy
                    elif TempTrigger == "lick pussy":
                            if ActiveGirl == RogueX:
                                $ TempLine = "Spicy." #lick pussy
                            elif ActiveGirl == KittyX:
                                $ TempLine = "Hmm, sweet." #lick pussy
                            elif ActiveGirl == EmmaX:
                                $ TempLine = "So many different flavors." #lick pussy
                            elif ActiveGirl == JeanX:
                                $ TempLine = "Huh, tangy." #lick pussy
                            elif ActiveGirl == StormX:
                                $ TempLine = "Very rich flavor." #lick pussy
                            elif ActiveGirl == JubesX:
                                $ TempLine = "Nice, very smooth." #lick pussy
                    if not TempLine:
                            #if nothing else is selected, or if D20: 1-3, or if D20: 14-15
                            $ TempLine = renpy.random.choice([
                                    "Good job, " + ActiveGirl.Name + ".",
                                    "You know what you're doing. . .",
                                    "Oooh, I liked that one.",
                                    "Great work.",
                                    "Tasty. . ."
                                    ])

            elif TempCheck == "masturbation":
                    if "unseen" not in LauraX.RecentActions:
                            #if she knows you're watching
                            if D20 <= 3:
                                # it's under a 3 roll
                                if "cockout" in Player.RecentActions:
                                    # Your cock's out
                                    $ TempLine = renpy.random.choice([
                                                "Hey, don't let that go to waste.",
                                                "Come here, " + LauraX.Petname + "."
                                                ])
                                else:
                                    # Your cock's not out
                                    $ TempLine = renpy.random.choice([
                                                "You aren't shy, are you " + LauraX.Petname + "?",
                                                "Pants, lose'em."
                                                ])
                            else:
                                    # It's over a 3 roll
                                    $ TempLine = renpy.random.choice([
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
                    elif LauraX.SEXP <= 30 or TempCheck == "kiss you":
                            #If she's relatively inexperienced
                            $ TempLine = renpy.random.choice([
                                    "You're good at this, " + LauraX.Petname + ".",
                                    "Huh, you seem to know what you're doing. . .",
                                    "Oh, hey down there.",
                                    "Hmm, like that.",
                                    ])
                    elif TempCheck == "hand":
                        $ TempLine = renpy.random.choice([
                                    "Hmm, your dick's so warm. . .",
                                    "This working for you?",
                                    "Seems like you're having fun, " + LauraX.Petname + "?",
                                    "You seem to be getting harder. . .",
                                    ])
                    elif TempCheck == "blow":
                        $ TempLine = renpy.random.choice([
                                    "Mmm, delicious. . .",
                                    "That's an interesting taste, " + LauraX.Petname + ".",
                                    "Did you just get harder? . .",
                                    "-Slurp.-",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",
                                    ])
                    elif TempCheck == "titjob":
                        $ TempLine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + LauraX.Petname + ".",
                                    "I can feel you get harder in there. . ."
                                    ])
                    elif TempCheck == "sex" or TempCheck == "anal":
                            $ TempLine = renpy.random.choice([
                                    "Mmmm, yeah, gimme more like that. . .",
                                    "Nngh, how filling. . .",
                                    "Ung, so deep. . .",
                                    "Keep it up, keep it up. . .",
                                    "Ngh, don't stop. . .",
                                    "That's right, harder, faster. . ."
                                    ])

                    if not TempLine:
                        #if nothing else is selected, or if D20 > 10
                        if Primary == LauraX:
                                $ TempLine = renpy.random.choice([
                                        "Wow, " + LauraX.Petname + ".",
                                        "That's great, " + LauraX.Petname + ".",
                                        "Oooh, that's nice. . .",
                                        "More!",
                                        "You're great, " + LauraX.Petname + ".",
                                        "Ok, that was a good one. . ."
                                        ])
                        else:
                                $ TempLine = renpy.random.choice([
                                        "Hey, " + LauraX.Petname + "? Don't keep me waiting.",
                                        "Hey, " + ActiveGirl.Name + "? Share, uh?",
                                        "Get over here, " + LauraX.Petname + ".",
                                        "Well you certainly put on a show.",
                                        "You're looking hot, " + LauraX.Petname + ".",
                                        "You're looking hot, " + ActiveGirl.Name + ".",
                                        "Nngh, yeah, stick it to her.",
                                        "Well you seem to be having fun, " + ActiveGirl.Name + "."
                                        ])
    #end Primary Laura

    elif Girl == JeanX:
            # if the Girl is Jean. . .
            if ApprovalCheck(JeanX, 1500):
                    $ D20 -= 5
            elif ApprovalCheck(JeanX, 1200):
                    $ D20 -= 3
            if D20 >= 10:
                    #drops it down to the generic grunts
                    pass
            elif Trigger == "lesbian" or (Secondary == JeanX and TempTrigger not in ("hand","blow","masturbation")):
                    #if this is a lesbian action, or if the threesome action is girl-focused

                    if "unseen" not in JeanX.RecentActions and D20 <= 5:
                            #if they know you're watching, there is a 3/10 or 2/5 chance
                            $ TempLine = "Enjoying the show, "+JeanX.Petname+"?" #you watching
                    elif TempTrigger == "fondle breasts":
                            if ActiveGirl == EmmaX:
                                $ TempLine = "How do you even cart these things around?" #fondle breasts
                            else:
                                $ TempLine = "Mmm, these things are firm, "+ActiveGirl.Name+"." #fondle breasts
                    elif TempTrigger == "suck breasts":
                            $ TempLine = "Mmmm, tasty." #suck breasts
                    elif TempTrigger == "fondle pussy":
                                $ TempLine = "You like that, slut?" #fondle pussy

                    if not TempLine:
                            #if nothing else is selected, or if D20: 1-3, or if D20: 14-15
                            $ TempLine = renpy.random.choice([
                                    "Keep up the pace, " + ActiveGirl.Name + ".",
                                    "Oh, good job there. . .",
                                    "Oooh, That was a good one.",
                                    "Good work.",
                                    "Tasty. . ."
                                    ])

            elif TempCheck == "masturbation":
                    if "unseen" not in JeanX.RecentActions:
                            #if she knows you're watching
                            if D20 <= 3:
                                # it's under a 3 roll
                                if "cockout" in Player.RecentActions:
                                    # Your cock's out
                                    $ TempLine = renpy.random.choice([
                                                "Hey, bring that one over here. . .",
                                                "Come here, " + JeanX.Petname + "."
                                                ])
                                else:
                                    # Your cock's not out
                                    $ TempLine = renpy.random.choice([
                                                "Why're you having all the fun " + JeanX.Petname + "?",
                                                "Hey, let me see that beautiful boy."
                                                ])
                            else:
                                    # It's over a 3 roll
                                    $ TempLine = renpy.random.choice([
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
                    elif JeanX.SEXP <= 30 or TempCheck == "kiss you":
                            #If she's relatively inexperienced
                            $ TempLine = renpy.random.choice([
                                    "You're good at this, " + JeanX.Petname + ".",
                                    "Huh, you seem to know what you're doing. . .",
                                    "Oh, hey down there.",
                                    "Hmm, like that.",
                                    ])
                    elif TempCheck == "hand":
                        $ TempLine = renpy.random.choice([
                                    "Hmm, your dick's so warm. . .",
                                    "This working for you?",
                                    "Seems like you're having fun, " + JeanX.Petname + "?",
                                    "You seem to be getting harder. . .",
                                    ])
                    elif TempCheck == "blow":
                        $ TempLine = renpy.random.choice([
                                    "Mmm, delicious. . .",
                                    "That's an interesting flavor, " + JeanX.Petname + ".",
                                    "Did you just get harder? . .",
                                    "-Slurp.-",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",
                                    ])
                    elif TempCheck == "titjob":
                        $ TempLine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + JeanX.Petname + ".",
                                    "I can feel you get harder in there. . ."
                                    ])
                    elif TempCheck == "sex" or TempCheck == "anal":
                            $ TempLine = renpy.random.choice([
                                    "Mmmm, yeah, gimme more like that. . .",
                                    "Nngh, how filling. . .",
                                    "Ung, so deep. . .",
                                    "Keep it up, keep it up. . .",
                                    "Ngh, don't stop. . .",
                                    "That's right, harder, faster. . ."
                                    ])

                    if not TempLine:
                        #if nothing else is selected, or if D20 > 10
                        if Primary == JeanX:
                                $ TempLine = renpy.random.choice([
                                        "Wow, " + JeanX.Petname + ".",
                                        "That's great, " + JeanX.Petname + ".",
                                        "Oooh, that's nice. . .",
                                        "More!",
                                        "You're great, " + JeanX.Petname + ".",
                                        "Ok, that was a good one. . ."
                                        ])
                        else:
                                $ TempLine = renpy.random.choice([
                                        "Hey, " + JeanX.Petname + "? Don't keep me waiting.",
                                        "Hey, " + ActiveGirl.Name + "? Share, uh?",
                                        "Get over here, " + JeanX.Petname + ".",
                                        "Well you certainly put on a show.",
                                        "You're looking hot, " + JeanX.Petname + ".",
                                        "You're looking hot, " + ActiveGirl.Name + ".",
                                        "Nngh, yeah, stick it to her.",
                                        "Well you seem to be having fun, " + ActiveGirl.Name + "."
                                        ])
    #end Primary Jean
    elif Girl == StormX:
            # if the Girl is Storm. . .
            if Trigger == "lesbian" or (Secondary == StormX and TempTrigger not in ("hand","blow","masturbation")):
                    #if this is a lesbian action, or if the threesome action is girl-focused

                    if "unseen" not in StormX.RecentActions and D20 <= 5:
                            #if they know you're watching, there is a 3/10 or 2/5 chance
                            $ TempLine = "So you do enjoy watching, "+StormX.Petname+"?" #you watching
                    elif TempTrigger == "fondle breasts" or TempTrigger == "suck breasts":
                            if ActiveGirl == EmmaX:
                                $ TempLine = "These really are quite impressive, Emma." #fondle breasts
                            else:
                                $ TempLine = "So firm. . ." #fondle breasts
                    elif TempTrigger == "fondle pussy":
                                $ TempLine = "Do you enjoy that, "+ActiveGirl.Name+"." #fondle pussy
                    elif TempTrigger == "lick pussy":
                            if ActiveGirl == LauraX:
                                $ TempLine = "Hmmm, that is a familiar taste. . ." #lick pussy
                            else:
                                $ TempLine = "What an exotic flavor, " + ActiveGirl.Name + "." #lick pussy
                    if not TempLine:
                            #if nothing else is selected, or if D20: 1-3, or if D20: 14-15
                            $ TempLine = renpy.random.choice([
                                    "Oh, " + ActiveGirl.Name + ".",
                                    "You are -very- skilled. . .",
                                    "Oh, you appear to have enjoyed that. . .",
                                    "Exceptional!",
                                    "Delicious. . ."
                                    ])

            elif TempCheck == "masturbation":
                    if "unseen" not in StormX.RecentActions:
                            #if she knows you're watching
                            if D20 <= 3:
                                # it's under a 3 roll
                                if "cockout" in Player.RecentActions:
                                    # Your cock's out
                                    $ TempLine = renpy.random.choice([
                                                "Oh, I could use some help here, " + StormX.Petname + ".",
                                                "Why do you not join me over here, " + StormX.Petname + "?"
                                                ])
                                else:
                                    # Your cock's not out
                                    $ TempLine = renpy.random.choice([
                                                "Do not be shy, " + StormX.Petname + ".",
                                                "Are you not enjoying the show?"
                                                ])
                            else:
                                    # It's over a 3 roll
                                    $ TempLine = renpy.random.choice([
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
                    elif StormX.SEXP <= 30 or TempCheck == "kiss you":
                            #If she's relatively inexperienced
                            $ TempLine = renpy.random.choice([
                                    "You are incredible, " + StormX.Petname + ".",
                                    "You are quite skilled at this. . .",
                                    "You appear to have enjoyed that. . .",
                                    "Exceptional!",
                                    ])
                    elif TempCheck == "hand":
                        $ TempLine = renpy.random.choice([
                                    "Your cock is so very warm. . .",
                                    "You appear to be enjoying the massage?",
                                    "You appear to be enjoying yourself, " + StormX.Petname + "?",
                                    "I can feel you grow harder. . .",
                                    ])
                    elif TempCheck == "blow":
                        $ TempLine = renpy.random.choice([
                                    "So delicious. . .",
                                    "I do enjoy this flavor, " + StormX.Petname + ".",
                                    "I can feel you get harder in my mouth. . .",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",
                                    ])
                    elif TempCheck == "titjob":
                        $ TempLine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + StormX.Petname + ".",
                                    "Do not get lost in there now . .",
                                    "I can feel you get harder in there. . ."
                                    ])
                    elif TempCheck == "sex" or TempCheck == "anal":
                            $ TempLine = renpy.random.choice([
                                    "Mmmm, more like that. . .",
                                    "Nngh, how. . . filling. . .",
                                    "Ung, so deep. . .",
                                    "Keep it up, keep it up. . .",
                                    "Oh, don't stop. . .",
                                    "I can feel you get harder inside me. . ."
                                    ])

                    if not TempLine:
                        #if nothing else is selected, or if D20 > 10
                        if Primary == StormX:
                                $ TempLine = renpy.random.choice([
                                        "I am overwhelmed, " + StormX.Petname + ".",
                                        "You are coming along quite nicely, " + StormX.Petname + ".",
                                        "Oooh, that is magnificent. . .",
                                        "More, I want more. . .",
                                        "You are simply -adorable,- " + StormX.Petname + ".",
                                        "You will {i}have{/i} to do that one again. . .",
                                        "You do leave an impression, " + StormX.Petname + "."
                                        ])
                        else:
                                $ TempLine = renpy.random.choice([
                                        "Do not keep me waiting, " + StormX.Petname + ".",
                                        ActiveGirl.Name + "? Could you please share some of that?",
                                        "Come here, " + StormX.Petname + ", ravish me.",
                                        "You certainly do put on a show.",
                                        "You are simply adorable, " + StormX.Petname + ".",
                                        "Nngh, give it to her.",
                                        "You seem to be enjoying yourself, " + ActiveGirl.Name + "."
                                        ])
            #End Storm's dirty talk lines
    #end Primary Storm

    elif Girl == JubesX:
            # if the Girl is Jubes. . .
            if D20 >= 10:
                    #drops it down to the generic grunts
                    pass
            elif Trigger == "lesbian" or (Secondary == JubesX and TempTrigger not in ("hand","blow","masturbation")):
                    #if this is a lesbian action, or if the threesome action is girl-focused

                    if "unseen" not in JubesX.RecentActions and D20 <= 5:
                            #if they know you're watching, there is a 3/10 or 2/5 chance
                            $ TempLine = "Like what you see there, "+JubesX.Petname+"?" #you watching
                    elif TempTrigger == "fondle breasts":
                            if ActiveGirl in (EmmaX,StormX):
                                $ TempLine = "Wow, how do you work with these. . ." #fondle breasts
                            else:
                                $ TempLine = "Maybe I need to find a new bra, "+ActiveGirl.Name+"." #fondle breasts
                    elif TempTrigger == "suck breasts":
                            $ TempLine = "Hmm, hard not to take a nibble. . ." #suck breasts
                    elif TempTrigger == "fondle pussy":
                                $ TempLine = "You're burning up. . ." #fondle pussy
                    elif TempTrigger == "lick pussy":
                            if ActiveGirl == RogueX:
                                $ TempLine = "So hot. . ." #lick pussy
                            elif ActiveGirl == KittyX:
                                $ TempLine = "Mmmm, sweet." #lick pussy
                            elif ActiveGirl == EmmaX:
                                $ TempLine = "So rich. . ." #lick pussy
                            elif ActiveGirl == JeanX:
                                $ TempLine = "Well, that's not bad. . ." #lick pussy
                            elif ActiveGirl == StormX:
                                $ TempLine = "Mmm. . . lovely. . ." #lick pussy
                    if not TempLine:
                            #if nothing else is selected, or if D20: 1-3, or if D20: 14-15
                            $ TempLine = renpy.random.choice([
                                    "Nice job, " + ActiveGirl.Name + ".",
                                    "You're hitting all the right places. . .",
                                    "Ooo! More of that. . .",
                                    "Great job.",
                                    "Yum. . ."
                                    ])

            elif TempCheck == "masturbation":
                    if "unseen" not in JubesX.RecentActions:
                            #if she knows you're watching
                            if D20 <= 3:
                                # it's under a 3 roll
                                if "cockout" in Player.RecentActions:
                                    # Your cock's out
                                    $ TempLine = renpy.random.choice([
                                                "Hey, let me in on that. . .",
                                                "Get over here, " + JubesX.Petname + "."
                                                ])
                                else:
                                    # Your cock's not out
                                    $ TempLine = renpy.random.choice([
                                                "Don't be shy, " + JubesX.Petname + ".",
                                                "Let me see what you're working with there. . ."
                                                ])
                            else:
                                    # It's over a 3 roll
                                    $ TempLine = renpy.random.choice([
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
                    elif JubesX.SEXP <= 30 or TempCheck == "kiss you":
                            #If she's relatively inexperienced
                            $ TempLine = renpy.random.choice([
                                    "Oh, um, you seem to know what you're doing, " + JubesX.Petname + ".",
                                    "Ohh. . . that's nice. . .",
                                    "Oh, nice. . .",
                                    "Hmm, do that one again. . .",
                                    ])
                    elif TempCheck == "hand":
                        $ TempLine = renpy.random.choice([
                                    "Hmm, your cock's so warm. . .",
                                    "Do you like this?",
                                    "You seem to be having fun, " + JubesX.Petname + ". . .",
                                    "Mmmm, you're getting harder in my hand. . .",
                                    ])
                    elif TempCheck == "blow":
                        $ TempLine = renpy.random.choice([
                                    "Mmm, delicious. . .",
                                    "I can't believe how you taste, " + JubesX.Petname + ".",
                                    "You're really firming up. . .",
                                    "-Slurp.-",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",
                                    ])
                    elif TempCheck == "titjob":
                        $ TempLine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + JubesX.Petname + ".",
                                    "I can feel you get harder in there. . ."
                                    ])
                    elif TempCheck == "sex" or TempCheck == "anal":
                            $ TempLine = renpy.random.choice([
                                    "Gimme more. . . & more. . .",
                                    "Nngh, filling me. . .",
                                    "Ung, deeper and deeper. . .",
                                    "Keep it up, keep it up. . .",
                                    "Ngh, don't stop. . .",
                                    "Ngh, harder, harder. . ."
                                    ])

                    if not TempLine:
                        #if nothing else is selected, or if D20 > 10
                        if Primary == JubesX:
                                $ TempLine = renpy.random.choice([
                                        "Wowow, " + JubesX.Petname + ".",
                                        "More like that, " + JubesX.Petname + ".",
                                        "Mmmm, that's nice. . .",
                                        "Gimme more!",
                                        "You're amazing, " + JubesX.Petname + ".",
                                        "Oooo. . . that was a good one. . ."
                                        ])
                        else:
                                $ TempLine = renpy.random.choice([
                                        "Hey, " + JubesX.Petname + "? Don't leave me waiting.",
                                        "Hey, " + ActiveGirl.Name + "? Let me in?",
                                        "Get over here, " + JubesX.Petname + ".",
                                        "Well. . . your certainly putting on a show.",
                                        "You're looking great there, " + JubesX.Petname + ".",
                                        "You're looking great there, " + ActiveGirl.Name + ".",
                                        "Nngh, oh yeah, get in there.",
                                        "Well that looks like a lot of fun, " + ActiveGirl.Name + "."
                                        ])
    #end Primary Jubes

    if not TempLine:
            #if nothing else was chosen. . .
            if not ActiveGirl or Trigger4 == "masturbation":
                    $ TempLine = Girl.Petname
            else:
                    $ TempLine = ActiveGirl.Name
            $ TempLine = renpy.random.choice([
                    "Mmmh. . .",
                    "Ung. . .",
                    "Ooooh. . .",
                    "Oooh, " + TempLine + ", yes. . ."
                    ])

    call AnyLine(Girl,TempLine)

    return

label Sex_Basic_Dialog(Girl=0,Type=0): #rkeljsv
        # call Sex_Basic_Dialog(Girl,"done")
        #called from during sex scenes if a girl is getting tired. . .
        if Girl not in TotalGirls:
                return
        if Girl == RogueX:
                if Type == 10:
                                ch_r "You might want to wrap this up, it's getting late."
                elif Type == 5:
                                ch_r "Seriously, it'll be time to stop soon."
                elif Type == "done":
                                ch_r "Ok, [Girl.Petname], that's enough of that for now."
                elif Type == "sitch":
                                ch_r "Mmm, so what else did you have in mind?"
                elif Type == "partner": #if a partner leaves during a scene
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
                if Type == 10:
                                ch_k "It's[KittyX.like]getting kinda late."
                elif Type == 5:
                                ch_k "We should wrap this up."
                elif Type == "done":
                                ch_k "Time to take a little break, for now."
                elif Type == "sitch":
                                ch_k "Mmm, so what else did you have in mind?"
                elif Type == "partner":
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
                if Type == 10:
                                ch_e "It's getting late. . ."
                elif Type == 5:
                                ch_e "We should take a break soon."
                elif Type == "done":
                                ch_e "We need to stop for a moment, let me catch my breath."
                elif Type == "sitch":
                                ch_e "Ok then, what were you thinking?"
                elif Type == "partner":
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
                if Type == 10:
                                ch_l "It's getting late, we should wrap this up."
                elif Type == 5:
                                ch_l "Tic tock, [Girl.Petname]."
                elif Type == "done":
                                ch_l "Ok, [Girl.Petname], breaktime."
                elif Type == "sitch":
                                ch_l "Ok then, what next?"
                elif Type == "partner":
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
                if Type == 10:
                                ch_j "Wow, look at the time. . ."
                elif Type == 5:
                                ch_j "We should probably wrap this up, [Girl.Petname]."
                elif Type == "done":
                                ch_j "Ok, [Girl.Petname], time for a break."
                elif Type == "sitch":
                                ch_j "Ok, what'd you have in mind?"
                elif Type == "partner":
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
                if Type == 10:
                                ch_s "It is getting late, [Girl.Petname]. . ."
                elif Type == 5:
                                ch_s "We should take a break soon."
                elif Type == "done":
                                ch_s "I need to take a moment to collect myself."
                elif Type == "sitch":
                                ch_s "Very well, what were you thinking?"
                elif Type == "partner":
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
                if Type == 10:
                                ch_v "I could use a break soon. . ."
                elif Type == 5:
                                ch_v ". . . I could really use a break here. . ."
                elif Type == "done":
                                ch_v "Ok, that's it, I need a break."
                elif Type == "sitch":
                                ch_v "Ok then, what else?"
                elif Type == "partner":
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

label out_of_action_dialog(character):
    if character == RogueX:
        ch_r "Sorry, [character.Petname], but I'm a bit worn out."
    elif character == KittyX:
        ch_k "Sorry, [character.Petname], but I'm a bit worn out."
    elif character == EmmaX:
        ch_e "I'm sorry, [character.Petname], but I need a break."
    elif character == LauraX:
        ch_l "Maybe in a minute, I need a break."
    elif character == JeanX:
        ch_j "Gimme a minute, k?"
    elif character == StormX:
        ch_s "I am sorry, [character.Petname], I need to take a break."
    elif character == JubesX:
        ch_v "I could use a short break first."

    return

label tired_dialog(character):
    if character == RogueX:
        if not MultiAction:
            ch_r "Look, I think we can stay on this one thing. . ."
        else:
            ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"
    elif character == KittyX:
        if not MultiAction:
            ch_k "Let's just. . . stick with this. . ."
        else:
            ch_k "I kinda need a break, so if we could wrap this up?"
    elif character == EmmaX:
        if not MultiAction:
            ch_e "Focus on what we're doing, [Girl.Petname]."
        else:
            ch_e "I could use a break, are you about finished here?"
    elif character == LauraX:
        if not MultiAction:
            ch_l "Nah, let's just stick to this."
        else:
            ch_l "Maybe we could finish this up for now?"
    elif character == JeanX:
        if not MultiAction:
            ch_j "I'd rather just stick to this."
        else:
            ch_j "Keep your eye on the prize. . ."
    elif character == StormX:
        if not MultiAction:
            ch_s "I would prefer to finish this."
        else:
            ch_s "Why not finish off here first?"
    elif character == JubesX:
        if not MultiAction:
            ch_v "Let's just keep doing this for a bit. . ."
        else:
            ch_v "Maybe we could wrap it up?"

    return

label angry_dialog(character):
    if character == RogueX:
        ch_r "I don't want to deal with you right now."
    elif character == KittyX:
        ch_k "I don't want to deal with you right now."
    elif character == EmmaX:
        ch_e "I'd rather not deal with you at the moment."
    elif character == LauraX:
        ch_l "You really don't want to try me right now."
    elif character == JeanX:
        ch_j "You really don't want to try me right now."
    elif character == StormX:
        ch_s "I do not want to deal with you right now."
    elif character == JubesX:
        ch_v "I'm definitely not in the mood for you right now."

    return

label go_back_dialog(character):
    if character == RogueX:
        $ Line = renpy.random.choice(["Ah, ah, Just keep doing what you were doing, " + character.Petname + ".",
            "Hey, just keep doing what you were doing, " + character.Petname + ".",
            "Hands off the merchandise, " + character.Petname + "."])
        ch_r "[Line]"
    elif character == KittyX:
        ch_k "Nuh-uh, [character.Petname], get back to what you were doing."
        ch_k "Heh, keep it above the belt, [KittyX.Petname]."
    elif character == EmmaX:
        ch_e "Down boy, you were doing so well. . ."
        ch_e "Perhaps we keep it above the waist, [EmmaX.Petname]."
    elif character == LauraX:
        ch_l "Roll it back, [LauraX.Petname]. . ."
        ch_l "Maybe we keep it above the waist, [LauraX.Petname]."
    elif character == JeanX:
        ch_j "Not so fast, [JeanX.Petname]. . ."
        ch_j "Keep it above the waist, [JeanX.Petname]."
    elif character == StormX:
        ch_s "Probably not right now. . ."
        ch_s "Perhaps we keep it above the waist, [StormX.Petname]."
    elif character == JubesX:
        ch_v "Cool your jets, [JubesX.Petname]. . ."
        ch_v "Maybe we keep it above the waist, [JubesX.Petname]."

    return

label private_enough_dialog(character):
    if character == RogueX:
        ch_r "I guess this is private enough. . ."
    elif character == KittyX:
        ch_k "I guess here is fine. . ."
    elif character == EmmaX:
        ch_e "This does seem less. . . exposed."
    elif character == LauraX:
        ch_l "This does seem less. . . exposed."
    elif character == JeanX:
        ch_j "I guess. . . maybe we could do it here. . ."
    elif character == StormX:
        ch_s "This is a bit more secluded."
    elif character == JubesX:
        ch_v "I guess this is less public. . ."

    return

label repeat_action_dialog(character):
    if character == RogueX:
        ch_r "Mmm, again? Ok."
    elif character == KittyX:
        ch_k "Mmm, again? Ok."
    elif character == EmmaX:
        ch_e "Mmmm, again? I suppose. . ."
    elif character == LauraX:
        ch_l "Mmmm, again? I guess. . ."
    elif character == JeanX:
        ch_j "Mmmm, again? I guess. . ."
    elif character == StormX:
        ch_s "Mmmm, again? I suppose. . ."
    elif character == JubesX:
        ch_v "Mmmm, again? I guess. . ."

    return

label not_in_public_dialog(character):
    if character == RogueX:
        ch_r "I really don't think this is the right place for that!"
    elif character == KittyX:
        ch_k "I don't like being so. . . exposed."
        ch_k "Time and place, [KittyX.Petname]!"
    elif character == EmmaX:
        ch_e "I can't be seen doing that with you."
        ch_e "I have a reputation to maintain."
    elif character == LauraX:
        ch_l "I try to stay off the radar."
    elif character == JeanX:
        ch_j "I'm. . . not comfortable. . . in public. . ."
    elif character == StormX:
        ch_s "I should not be seen doing that."
    elif character == JubesX:
        ch_v "I don't wanna make a scene."

    return

label already_said_not_here_dialog(character):
    if character == RogueX:
        ch_r "I told you not in public!"
    elif character == KittyX:
        ch_k "Not here!"
    elif character == EmmaX:
        ch_e "As I said, not here, [character.Petname]."
    elif character == LauraX:
        ch_l "I told you, not here, [LauraX.Petname]."
    elif character == JeanX:
        ch_j "I told you. . . not here, [JeanX.Petname]."
    elif character == StormX:
        ch_s "This area is too public, [StormX.Petname]."
        ch_s "As I said, not here, [StormX.Petname]."
    elif character == JubesX:
        ch_v "I told you, not here, [JubesX.Petname]."

    return

label not_ready_yet_dialog(character):
    if character == RogueX:
        ch_r "I just don't think I'm ready yet, [character.Petname]. . ."
    elif character == KittyX:
        ch_k "I'm[character.like]not ready for that, [character.Petname]. . ."
        ch_k "Not. . . yet. . . maybe later."
    elif character == EmmaX:
        ch_e "I highly doubt you could handle them, [character.Petname]. . ."
        ch_e "Seems a bit forward, [EmmaX.Petname]."
    elif character == LauraX:
        ch_l "Look, I don't know if we're ready for that, [LauraX.Petname]. . ."
        ch_l "Seems a bit aggressive, [LauraX.Petname]."
    elif character == JeanX:
        ch_j "Look, don't touch, [JeanX.Petname]. . ."
    elif character == StormX:
        ch_s "Perhaps some other time, [StormX.Petname]. . ."
        ch_s "I would rather you did not, [StormX.Petname]."
    elif character == JubesX:
        ch_v "Look, I don't know if we're ready for that, [JubesX.Petname]. . ."
        ch_v "Kinda forward, [JubesX.Petname]."

    return

label no_problem_dialog(character):
    if character == RogueX:
        ch_r "Ok, no problem, [character.Petname]."
        ch_r "Yeah, fine, [character.Petname]."
        ch_r "Yeah, ok, [character.Petname]."
    elif character == KittyX:
        ch_k "It's cool, [character.Petname]."
        ch_k "Yeah, ok, [KittyX.Petname]."
    elif character == EmmaX:
        ch_e "Don't concern yourself, [character.Petname]."
        ch_e "I appreciate your restraint."
    elif character == LauraX:
        ch_l "No worries."
        ch_l "It's cool."
    elif character == JeanX:
        ch_j "It's fine, I get it."
    elif character == StormX:
        ch_s "Don't concern yourself, [StormX.Petname]."
        ch_s "I appreciate your restraint."
    elif character == JubesX:
        ch_v "Yeah, whatever."

    return

label maybe_later_dialog(character):
    if character == RogueX:
        ch_r "I'll give it some thought, [character.Petname]."
        ch_r "Heh, maybe, [character.Petname]."
    elif character == KittyX:
        ch_k "Um, yeah, maybe later."
        ch_k "Heh, maybe, [KittyX.Petname]."
    elif character == EmmaX:
        ch_e "Well, I can't rule it out. . ."
        ch_e "Perhaps."
    elif character == LauraX:
        ch_l "Eh. Maybe."
        ch_l "Maybe?"
    elif character == JeanX:
        ch_j ". . . I guess? Maybe."
    elif character == StormX:
        ch_s "I will give it some thought, [StormX.Petname]."
    elif character == JubesX:
        ch_v "Eh. Maybe."
        ch_v "Maybe?"

    return

label reward_politeness_dialog(character):
    if character == RogueX:
        ch_r "Heh, I suppose I can hardly refuse ya when you use the magic words . . ."
        ch_r "You better work your mouth that hard on these."
    elif character == KittyX:
        ch_k "Well[character.like]if you ask nicely. . ."
    elif character == EmmaX:
        ch_e "Politeness can be rewarded. . ."
    elif character == LauraX:
        ch_l "Well if you're going to be a little bitch about it. . ."
    elif character == JeanX:
        ch_j "Oh, fine, just don't start crying."
    elif character == StormX:
        ch_s "Well, I suppose. . ."
        ch_s "I suppose it does not hurt. . ."
    elif character == JubesX:
        ch_v "Geeze, don't whine about it. . ."

    return

label please_not_good_enough_dialog(character):
    if character == RogueX:
        ch_r "I'm afraid not this time, sorry [character.Petname]."
    elif character == KittyX:
        ch_k "Um, still no."
    elif character == EmmaX:
        ch_e "This wasn't a \"tone\" issue."
    elif character == LauraX:
        ch_l "Well if you're going to be a little bitch about it. . ."
    elif character == JeanX:
        ch_j "No way."
        ch_j "Oh, don't cry."
    elif character == StormX:
        ch_s "No, thank you."
        ch_s "It is not appropriate."
    elif character == JubesX:
        ch_v "Geeze, don't whine about it. . ."

    return

label learn_to_take_no_dialog(character):
    if character == RogueX:
        ch_r "Learn to take \"no\" for an answer, [character.Petname]."
    elif character == KittyX:
        ch_k "{i}Listen{/i}!"
        ch_k "How many times do I have to say \"no?\""
    elif character == EmmaX:
        ch_e "You need to pay attention when I speak to you."
        ch_e "I don't appreciate having to repeat myself, [EmmaX.Petname]."
    elif character == LauraX:
        ch_l "Listen to the words that are coming out of my mouth."
        ch_l "I don't like to repeat myself, [LauraX.Petname]."
    elif character == JeanX:
        ch_j "I don't want to have to go through this again."
    elif character == StormX:
        ch_s "I have been clear on this."
    elif character == JubesX:
        ch_v "I'm pretty clear on this, NO."

    return

label not_happening_dialog(character):
    if character == RogueX:
        ch_r "Not hap'nin."
        ch_r "Not hap'nin, [character.Petname]."
        ch_r "No luck, [character.Petname]."
    elif character == KittyX:
        ch_k "No way."
        ch_k "Nooope."
    elif character == EmmaX:
        ch_e "No."
    elif character == LauraX:
        ch_l "No."
    elif character == JeanX:
        ch_j "No."
    elif character == StormX:
        ch_s "No, I do not think so."
    elif character == JubesX:
        ch_v "No."

    return

label you_had_your_shot_dialog(character):
    if character == RogueX:
        ch_r "Sorry, [character.Petname], you aren't touching these again."
        ch_r "Sorry, [character.Petname], you aren't getting these in your mouth."
        ch_r "Fresh!"
    elif character == KittyX:
        ch_k "You had your shot."
        ch_r "Fresh!"
    elif character == EmmaX:
        ch_e "I'm afraid you haven't earned back my good graces."
        ch_e "Hands."
    elif character == LauraX:
        ch_l "You'll have to earn that back."
        ch_l "Keep your hands to yourself."
    elif character == JeanX:
        ch_j "We've had enough of that."
        ch_j "Keep your hands to yourself."
    elif character == StormX:
        ch_s "No, I do not think so."
    elif character == JubesX:
        ch_v "You'll have to earn that."
        ch_v "Keep your hands to yourself."

    return

label forced_but_not_unwelcome_dialog(character):
    if character == RogueX:
        ch_r "Fine, if that's what you want."
        ch_r "Hmmph, well I guess you can go to town. . ."
        ch_r "Hmmph."
    elif character == KittyX:
        ch_k "Rude! But. . . whatever."
        ch_k "Hmmph."
    elif character == EmmaX:
        ch_e "That is not appropriate. . ."
        ch_e "but neither is it entirely unwelcome. . ."

        ch_e "Hmmph."
    elif character == LauraX:
        ch_l "Hey. . ."
        ch_l "Eh, whatever. . ."
        ch_l "Hmmph."
    elif character == JeanX:
        ch_j "Hey. . ."
        ch_j ". . .whatever. . ."

        ch_j ". . .whatever. . ."
    elif character == StormX:
        ch_s "That is not appropriate. . ."
        ch_s "but neither is it entirely unwelcome. . ."

        ch_s "Hmmph."
    elif character == JubesX:
        ch_v "Hey. . ."
        ch_v "Well, whatever. . ."

        ch_v "Hmmph."

    return

label just_told_you_no_dialog(character):
    if character == RogueX:
        ch_r "I {i}just{/i} told you \"no,\" [character.Petname]."
    elif character == KittyX:
        ch_k "[character.Like]no way, [character.Petname]."
        ch_k "I[KittyX.like]{i}just{/i} told you \"no!\""
    elif character == EmmaX:
        ch_e "Your persistance is doing you no favors, [character.Petname]."
    elif character == LauraX:
        ch_l "Take a breath here, before you regret it."
    elif character == JeanX:
        ch_j "I'm not used to repeating myself."
    elif character == StormX:
        ch_s "Do not persist in this, [StormX.Petname]."
    elif character == JubesX:
        ch_v "I already told you, \"no\"."

    return

label come_and_get_em_dialog(character):
    if character == RogueX:
        ch_r "Ok [character.Petname], come and get'em."
        ch_r "Ok [character.Petname], go ahead."
    elif character == KittyX:
        ch_k "Ok [character.Petname], come and get'em."
        ch_k "Ok [KittyX.Petname], go ahead."
    elif character == EmmaX:
        ch_e "That sounds lovely, ravish me."
        ch_e "Ok [EmmaX.Petname], go ahead."
    elif character == LauraX:
        ch_l "Sure, sounds fun."
        ch_l "Ok [LauraX.Petname], go ahead."
    elif character == JeanX:
        ch_j "Sure, sounds fun."
        ch_j "Ok [JeanX.Petname], go ahead."
    elif character == StormX:
        ch_s "I would love that. . ."
        ch_s "Ok [StormX.Petname], go ahead."
    elif character == JubesX:
        ch_v "Sure, sounds fun."
        ch_v "Ok [JubesX.Petname], go ahead."

    return

label gently_dialog(character):
    if character == RogueX:
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so hard this time though."
            "You do have a smooth touch. . .",
            "Mmm. . ."])
        ch_r "[Line]"
    elif character == KittyX:
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Take it easy though.",
            "Mmm. . ."])
        ch_k "[Line]"
    elif character == EmmaX:
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Mmm. . ."
            "Didn't get enough earlier?"])
        ch_e "[Line]"
    elif character == LauraX:
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Mmm. . ."])
        ch_l "[Line]"
    elif character == JeanX:
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Mmm. . ."])
        ch_j "[Line]"
    elif character == StormX:
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Gently. . . gently. . .",
            "Mmm. . ."])
        ch_s "[Line]"
    elif character == JubesX:
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax. . .",
            "Mmm. . ."])
        ch_v "[Line]"

    return

label had_enough_of_this_dialog(character):
    if character == RogueX:
        ch_r "I told you not to touch me like that in public!"
        ch_r "I told you we can't do that in public!"
    elif character == KittyX:
        ch_k "I told you not here!"
        ch_k "I told you not to touch me like that in public!"
    elif character == EmmaX:
        ch_e "You've been warned."
        ch_e "I told you not to touch me like that in public!"
    elif character == LauraX:
        ch_l "I've had enough of this today."
        ch_l "I told you not to touch me like that in public!"
    elif character == JeanX:
        ch_j "I've had enough of this today."
        ch_j "I told you not to touch me like that in public!"
    elif character == StormX:
        ch_s "I have already told you my answer."
        ch_s "I told you not to touch me like that in public!"
    elif character == JubesX:
        ch_v "I've had enough of this today."
        ch_v "I told you not to touch me like that in public!"

    return

label already_said_no_dialog(character):
    if character == RogueX:
        ch_r "I already told you \"no,\" [character.Petname]."
        ch_r "I already told you no, take a hint."
        ch_r "What part of \"no\" don't you understand?"
    elif character == KittyX:
        ch_k "I[character.like]already told you \"no.\""
        ch_k "[KittyX.Like]take a lesson, [KittyX.Petname]."
        ch_k "Get a clue, [KittyX.Petname]!"
        ch_k "I'm telling you to give it a rest!"
    elif character == EmmaX:
        ch_e "I believe you know my answer on this matter."
        ch_e "I'm not in the mood for this, [EmmaX.Petname]."
        ch_e "You heard me the first time."
    elif character == LauraX:
        ch_l "Don't make me tell you again today."
        ch_l "Grrrrrrrrr."
        ch_l "Back off!"
    elif character == JeanX:
        ch_j "Don't ask me again today."
        ch_j "Go away!"
        ch_j "Give me some space!"
    elif character == StormX:
        ch_s "I have already told you my answer."
        ch_s "I believe you know my answer on this matter."
        ch_s "I am far too irate for this."
        ch_s "Stop pestering me!"
    elif character == JubesX:
        ch_v "Don't make me tell you again today."
        ch_v "Grrrrrrrrr."
        ch_v "Back off!"

    return

label rather_not_dialog(character):
    if character == RogueX:
        ch_r "I'd really rather not."
    elif character == KittyX:
        ch_k "Um, no."
    elif character == EmmaX:
        ch_e "You wish."
    elif character == LauraX:
        ch_l "Keep dreaming."
        ch_l "You wish."
    elif character == JeanX:
        ch_j "Yeah, you wish."
        ch_j "You wish."
    elif character == StormX:
        ch_s "Hmm, no."
    elif character == JubesX:
        ch_v "Cute, but no."
        ch_v "You wish."

    return

label went_too_far_dialog(character):
    if character == RogueX:
        ch_r "I don't want you touching me."
        ch_r "I don't want your lips on me."
        ch_r "Not even that much."
    elif character == KittyX:
        ch_k "Not even."
    elif character == EmmaX:
        ch_e "Don't push your luck."
    elif character == LauraX:
        ch_l "No."
    elif character == JeanX:
        ch_j "No."
    elif character == StormX:
        ch_s "You go too far."
    elif character == JubesX:
        ch_v "No."

    return

label warm_hands_dialog(character):
    if character == RogueX:
        ch_r "You like how those feel, huh?"
        ch_r "You're just going at them, huh?"
    elif character == KittyX:
        ch_k "You like how those feel, huh?"
        ch_k "You're just going at them, huh?"
        ch_k "Are they keeping you satisfied?"
    elif character == EmmaX:
        ch_e "Luxurious, yes?"
        ch_e "They really are magnificent, aren't they?"
        ch_e "Lovely, aren't they?"
    elif character == LauraX:
        ch_l "Kinda nice, but. . ."
        ch_l "Enjoying yourself?"
        ch_l "This is kinda nice. . ."
    elif character == JeanX:
        ch_j "Kinda nice, but. . ."
        ch_j "Having fun there?"
        ch_j "This is kinda nice. . ."
    elif character == StormX:
        ch_s "Your hands are so warm. . ."
        ch_s "You really seem to enjoy those. . ."
        ch_s "You really seem to enjoy those. . ."
    elif character == JubesX:
        ch_v "Ok, but, uh. . ."
        ch_v "Having fun?"

    return

label try_something_else_dialog(character):
    if character == RogueX:
        ch_r "I know you're having fun, but maybe we could try something else [character.Petname]."
    elif character == KittyX:
        ch_k "You look like you're having fun there, but maybe we could[KittyX.like]try something else?"
        ch_k "Maybe we could try something else here [KittyX.Petname]?"
    elif character == EmmaX:
        ch_e "You certainly seem to be enjoying yourself, but perhaps we could add some variety?"
        ch_e "Perhaps we could try something else, [EmmaX.Petname]?"
    elif character == LauraX:
        ch_l "Maybe change things up a little?"
        ch_l "Maybe it's time for something else, [LauraX.Petname]?"
    elif character == JeanX:
        ch_j "Maybe try something else?"
        ch_j "Maybe it's time for something else, [JeanX.Petname]?"
    elif character == StormX:
        ch_s "I am sure that is fun, but could we try something different?"
    elif character == JubesX:
        ch_v "Could we maybe try. . . something else?"

    return

label this_is_boring_dialog(character):
    if character == RogueX:
        ch_r "Well if that's your attitude, I don't need your \"help\"."
    elif character == KittyX:
        ch_k "Fun for you maybe, I'm tired of it."
    elif character == EmmaX:
        ch_e "Well perhaps you are enjoying yourself, but I'm tired of this."
        ch_e "You may be enjoying yourself, but I'm getting a bit sore."
    elif character == LauraX:
        ch_l "I'm kinda bored here."
        ch_l "Well, I've got better things to be doing."
    elif character == JeanX:
        ch_j "Well -I'm- bored."
        ch_j "Well, I've got better things to be doing."
    elif character == StormX:
        ch_s "Well however much you are enjoying yourself, I need to take a break."
    elif character == JubesX:
        ch_v "This is kinda boring. . .."

    return

label wrap_this_up_dialog(character):
    if character == RogueX:
        ch_r "You might want to wrap this up, it's getting late."
    elif character == KittyX:
        ch_k "It's[KittyX.like]getting kinda late."
    elif character == EmmaX:
        ch_e "It's getting late. . ."
    elif character == LauraX:
        ch_l "It's getting late, we should wrap this up."
    elif character == JeanX:
        ch_j "Wow, look at the time. . ."
    elif character == StormX:
        ch_s "It is getting late, [character.Petname]. . ."
    elif character == JubesX:
        ch_v "I could use a break soon. . ."

    return

label time_to_stop_soon_dialog(character):
    if character == RogueX:
        ch_r "Seriously, it'll be time to stop soon."
    elif character == KittyX:
        ch_k "We should wrap this up."
    elif character == EmmaX:
        ch_e "We should take a break soon."
    elif character == LauraX:
        ch_l "Tick tock, [LauraX.Petname]."
    elif character == JeanX:
        ch_j "We should probably wrap this up, [character.Petname]."
    elif character == StormX:
        ch_s "We should take a break soon."
    elif character == JubesX:
        ch_v ". . . I could really use a break here. . ."

    return

label im_done_dialog(character):
    if character == RogueX:
        ch_r "Ok, [character.Petname], that's enough of that for now."
    elif character == KittyX:
        ch_k "Time to take a little break, for now."
    elif character == EmmaX:
        ch_e "We need to stop for a moment, let me catch my breath."
    elif character == LauraX:
        ch_l "Ok, [LauraX.Petname], breaktime."
    elif character == JeanX:
        ch_j "Ok, [Girl.Petname], time for a break."
    elif character == StormX:
        ch_s "I need to take a moment to collect myself."
    elif character == JubesX:
        ch_v "Ok, that's it, I need a break."

    return

label that_was_nice_dialog(character):
    if character == RogueX:
        ch_r "That was. . . nice."
        ch_r "That was . . . real pleasant, [character.Petname]."
        ch_r "I . . . really liked that, [character.Petname]."
    elif character == KittyX:
        ch_k "I liked that."
        ch_k "I hope there was[KittyX.like]enough to work with."
        ch_k "I hope they were enough for you. . ."
    elif character == EmmaX:
        ch_e "That was. . . pleasant."
        ch_e "I'm sure it exceeded your expectations. . ."
        ch_e "Delectable, weren't they."
    elif character == LauraX:
        ch_l "That was. . . interesting."
        ch_l "Did you enjoy that?"
        ch_l "That was kinda nice."
    elif character == JeanX:
        ch_j "Well that was. . . something."
        ch_j "I bet you enjoyed that."
    elif character == StormX:
        ch_s "Thank you for that."
        ch_s "That was quite fun. . ."
        ch_s "That was certainly enjoyable."
    elif character == JubesX:
        ch_v "That was. . . interesting."
        ch_v "Did you like that?"
        ch_v "That was kinda nice."

    return

label was_that_enough_dialog(character):
    if character == RogueX:
        ch_r "Was that enough for you?"
        ch_r "Did you get your jollies?"
        ch_r "Did you like the taste?"
    elif character == KittyX:
        ch_k "Was that enough?"
        ch_k "Not a disappointment, right?"
        ch_k "Did that satisfy you?"
    elif character == EmmaX:
        ch_e "Was that enough?"
        ch_e "Well you certainly hit the jackpot."
        ch_e "Did you get enough?"
    elif character == LauraX:
        ch_l "Was that enough?"
        ch_l "That worked out for you?"
        ch_l "Did you get enough?"
    elif character == JeanX:
        ch_j "Was that enough?"
        ch_j "You get what you wanted out of that?"
    elif character == StormX:
        ch_s "Ok, was that good?"
        ch_s "I expect you enjoyed that. . .."
        ch_s "Did you get enough?"
    elif character == JubesX:
        ch_v "Was that enough?"
        ch_v "That worked out for you?"
        ch_v "Did you get enough?"

    return

label take_a_breather_dialog(character):
    if character == RogueX:
        ch_r "We've been at it for a while now, let's take a breather."
    elif character == KittyX:
        ch_k "We've been at it for a while now, let's take a breather."
    elif character == EmmaX:
        ch_e "I think we could both do with a short break."
    elif character == LauraX:
        ch_l "You're looking a bit worn out, maybe take a break."
    elif character == JeanX:
        ch_j "You're looking a bit worn out, maybe take a break."
    elif character == StormX:
        ch_s "I think we could both do with a short break."
    elif character == JubesX:
        ch_v "Hey, I could use a break, how 'bout you?"

    return

label got_some_spunk_dialog(character):
    if character == RogueX:
        ch_r "Oh?"
    elif character == KittyX:
        ch_k "Huh?"
    elif character == EmmaX:
        ch_e "Huh?"
    elif character == LauraX:
        ch_l "What?"
    elif character == JeanX:
        ch_j "What?"
    elif character == StormX:
        ch_s "Oh, what do you mean?"
    elif character == JubesX:
        ch_v "What?"

    return

label thats_it_for_now_dialog(character):
    if character == RogueX:
        $ Line = renpy.random.choice(["That's it. . . for now."])
        character.voice "[Line]"
    elif character == KittyX:
        $ Line = renpy.random.choice(["That's it. . . for now."])
        character.voice "[Line]"
    elif character == EmmaX:
        $ Line = renpy.random.choice(["That's all you get. . . for now."])
        character.voice "[Line]"
    elif character == LauraX:
        $ Line = renpy.random.choice(["That's all. . . for now at least."])
        character.voice "[Line]"
    elif character == JeanX:
        $ Line = renpy.random.choice(["That's all. . . for now at least."])
        character.voice "[Line]"
    elif character == StormX:
        $ Line = renpy.random.choice(["I think that you have had enough for the moment."])
        character.voice "[Line]"
    elif character == JubesX:
        $ Line = renpy.random.choice(["Ok, that should be plenty for now."])
        character.voice "[Line]"

    return

label get_out_dialog(character):
    if character == RogueX:
        ch_r "I don't want to deal with you right now."
    elif character == KittyX:
        ch_k "Nooope."
    elif character == EmmaX:
        ch_e "I haven't any time for this."
    elif character == LauraX:
        ch_l "Nope."
    elif character == JeanX:
        ch_j "Out!"
    elif character == StormX:
        ch_s "Get out."
    elif character == JubesX:
        ch_v "Out!"

    if character == RogueX:
        ch_r "Buzz off already."
    elif character == KittyX:
        ch_k "GTFO."
    elif character == EmmaX:
        ch_e "Out."
    elif character == LauraX:
        ch_l "Fuck off."

    if character == RogueX:
        ch_r "I really think you should leave."
        "[RogueX.Name] pushes you back into the hall and slams the door. You head back to your room."
    elif character == KittyX:
        ch_k "Go. Now."
        "[KittyX.Name] pushes you back into the hall and slams the door. You head back to your room."
    elif character == EmmaX:
        ch_e "I think you should leave now."
        "[EmmaX.Name] pushes you back into the hall and slams the door. You head back to your room."
    elif character == LauraX:
        ch_l "Get out before we both regret it."
        "[LauraX.Name] shoves you back into the hall and slams the door. You head back to your room."
    elif character == JeanX:
        "[JeanX.Name] shoves you back into the hall and slams the door. You head back to your room."
    elif character == StormX:
        ch_s "Out. Now."
        "[StormX.Name] pushes you to the top of the stairs and slams the door. You head back to your room."
    elif character == JubesX:
        "[JubesX.Name] pushes you back into the hall and slams the door. You head back to your room."
