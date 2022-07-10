label out_of_Actions_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Sorry, " + Girl.player_petname + " but I'm a bit worn out.",
            "I'm a bit worn out right now, " + Girl.player_petname + " maybe later."]
    elif Girl == KittyX:
        $ lines = ["Sorry, " + Girl.player_petname + " but I'm a bit worn out.",
            "I'm kinda tired right now, " + Girl.player_petname + " later?"]
    elif Girl == EmmaX:
        $ lines = ["I'm sorry, " + Girl.player_petname + " but I need a break.",
            "I'm rather tired right now, " + Girl.player_petname + " rain check?"]
    elif Girl == LauraX:
        $ lines = ["Maybe in a minute, I need a break.",
            "Maybe later, " + Girl.player_petname + "_"]
    elif Girl == JeanX:
        $ lines = ["Gimme a minute, k?"]
    elif Girl == StormX:
        $ lines = ["I am sorry, " + Girl.player_petname + " I need to take a break."]
    elif Girl == JubesX:
        $ lines = ["I could use a short break first.",
            "Maybe later, " + Girl.player_petname + "_"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label end_of_sex_menu_not_multiaction_lines(Girl):
    if Girl == RogueX:
        $ lines = ["That's it. . . for now."]
    elif Girl == KittyX:
        $ lines = ["That's it. . . for now."]
    elif Girl == EmmaX:
        $ lines = ["That's all you get. . . for now."]
    elif Girl == LauraX:
        $ lines = ["That's all. . . for now at least."]
    elif Girl == JeanX:
        $ lines = ["That's all. . . for now at least."]
    elif Girl == StormX:
        $ lines = ["I think that you have had enough for the moment."]
    elif Girl == JubesX:
        $ lines = ["Ok, that should be plenty for now."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label sex_menu_caught_or_angry_lines(Girl):
    if Girl == RogueX:
        $ lines = ["I don't want to deal with you right now."]
    elif Girl == KittyX:
        $ lines = ["I don't want to deal with you right now."]
    elif Girl == EmmaX:
        $ lines = ["I'd rather not deal with you at the moment."]
    elif Girl == LauraX:
        $ lines = ["You really don't want to try me right now."]
    elif Girl == JeanX:
        $ lines = ["You really don't want to try me right now."]
    elif Girl == StormX:
        $ lines = ["I do not want to deal with you right now."]
    elif Girl == JubesX:
        $ lines = ["I'm definitely not in the mood for you right now."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label sex_menu_less_than_five_rounds_lines(Girl):
    if Girl == RogueX:
        $ lines = ["We've been at it for a while now, let's take a breather."]
    elif Girl == KittyX:
        $ lines = ["We've been at it for a while now, let's take a breather."]
    elif Girl == EmmaX:
        $ lines = ["I think we could both do with a short break."]
    elif Girl == LauraX:
        $ lines = ["You're looking a bit worn out, maybe take a break."]
    elif Girl == JeanX:
        $ lines = ["You're looking a bit worn out, maybe take a break."]
    elif Girl == StormX:
        $ lines = ["I think we could both do with a short break."]
    elif Girl == JubesX:
        $ lines = ["Hey, I could use a break, how 'bout you?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label generic_exit_sex_menu_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Huh? Ok."]
    elif Girl == KittyX:
        $ lines = ["Ok, fine."]
    elif Girl == EmmaX:
        $ lines = ["Fine."]
    elif Girl == LauraX:
        $ lines = ["Ok, fine."]
    elif Girl == JeanX:
        $ lines = ["Ok, fine."]
    elif Girl == StormX:
        $ lines = ["That is fine."]
    elif Girl == JubesX:
        $ lines = ["Sure, fine."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_experienced_first_round_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Are you sure, " + Girl.player_petname + "_? I could really use some company."]
    elif Girl == KittyX:
        $ lines = ["Are you sure, " + Girl.player_petname + "_? I wasn't exactly. . . finished."]
    elif Girl == EmmaX:
        $ lines = ["Are you certain, " + Girl.player_petname + "_? Are you perhaps forgetting something?"]
    elif Girl == LauraX:
        $ lines = ["Are you sure, " + Girl.player_petname + "_?{p}I could go another round. . . or two. . ."]
    elif Girl == JeanX:
        $ lines = ["Are you sure, " + Girl.player_petname + "_?{p}I could go another round. . . or two. . ."]
    elif Girl == StormX:
        $ lines = ["Are you certain, " + Girl.player_petname + "_? Are you perhaps forgetting something?"]
    elif Girl == JubesX:
        $ lines = ["Are you sure, " + Girl.player_petname + "_?{p}I could keep going. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_experienced_addicted_lines(Girl):
    if Girl == RogueX:
        $ lines = ["I still need a little. . . contact."]
    elif Girl == KittyX:
        $ lines = ["I need more touching."]
    elif Girl == EmmaX:
        $ lines = ["I need more contact."]
    elif Girl == LauraX:
        $ lines = ["I need more contact."]
    elif Girl == JeanX:
        $ lines = ["I need some more skin contact.{p}}You gonna leave me hanging?"]
    elif Girl == StormX:
        $ lines = ["I need your touch."]
    elif Girl == JubesX:
        $ lines = ["I'm a little drained, I need more contact."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_experienced_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Don't leave me hang'in, " + Girl.player_petname + "_."]
    elif Girl == KittyX:
        $ lines = ["I still need some more attention."]
    elif Girl == EmmaX:
        $ lines = ["I'm afraid that still wasn't enough."]
    elif Girl == LauraX:
        $ lines = ["Aren't you forgetting something?"]
    elif Girl == JeanX:
        $ lines = ["Hey, you'd better get me off here.{p}You gonna leave me hanging?"]
    elif Girl == StormX:
        $ lines = ["That was not enough to satisfy me."]
    elif Girl == JubesX:
        $ lines = ["Hey! Don't leave me hanging here."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_done_for_now_unsatisfied_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Way to leave a girl in the lurch. . ."]
    elif Girl == KittyX:
        $ lines = ["Rude!"]
    elif Girl == EmmaX:
        $ lines = ["Well! This might count against you next time."]
    elif Girl == LauraX:
        $ lines = ["You'll regret that one."]
    elif Girl == JeanX:
        $ lines = ["The die has been cast."]
    elif Girl == StormX:
        $ lines = ["Perhaps I need to teach you to be more generous."]
    elif Girl == JubesX:
        $ lines = ["Well, that sucks."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_done_for_now_satisfied_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Well, you did at least do your part. . ."]
    elif Girl == KittyX:
        $ lines = ["I guess I'll take what I can get. . ."]
    elif Girl == EmmaX:
        $ lines = ["I suppose I'll have to blame myself as an educator."]
    elif Girl == LauraX:
        $ lines = ["Selfish. . ."]
    elif Girl == JeanX:
        $ lines = ["Booo. . ."]
    elif Girl == StormX:
        $ lines = ["Perhaps I need to teach you to be more generous."]
    elif Girl == JubesX:
        $ lines = ["So selfish. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_gave_it_a_shot_unsatisfied_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Way to leave a girl in the lurch. . ."]
    elif Girl == KittyX:
        $ lines = ["Rude!"]
    elif Girl == EmmaX:
        $ lines = ["Yes, disappointingly so. . ."]
    elif Girl == LauraX:
        $ lines = ["Not a very good one."]
    elif Girl == JeanX:
        $ lines = ["If that's what you want to call it. . ."]
    elif Girl == StormX:
        $ lines = ["So that was the best you could achieve. . ."]
    elif Girl == JubesX:
        $ lines = ["Well try again."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_gave_it_a_shot_satisfied_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Well, fair enough. . ."]
    elif Girl == KittyX:
        $ lines = ["I guess I'll take what I can get. . ."]
    elif Girl == EmmaX:
        $ lines = ["I suppose you did. . . shame you couldn't do better. . ."]
    elif Girl == LauraX:
        $ lines = ["Selfish. . ."]
    elif Girl == JeanX:
        $ lines = ["Booo. . ."]
    elif Girl == StormX:
        $ lines = ["So that was the best you could achieve. . ."]
    elif Girl == JubesX:
        $ lines = ["So selfish. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_did_my_part_lines(Girl):
    if Girl == RogueX:
        $ lines = ["I guess you did at that. . ."]
    elif Girl == KittyX:
        $ lines = ["Well. . . yeah, but. . ."]
    elif Girl == EmmaX:
        $ lines = ["Take it as a compliment that I expected more."]
    elif Girl == LauraX:
        $ lines = ["Well. . . yeah, but. . ."]
    elif Girl == JeanX:
        $ lines = ["Stingy. . ."]
    elif Girl == StormX:
        $ lines = ["I had hoped for better.  . ."]
    elif Girl == JubesX:
        $ lines = ["Yeah, but. . . keep doing that. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_out_of_semen_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Huh, can't be helped, I s'pose."]
    elif Girl == KittyX:
        $ lines = ["Yeah, but " + Girl.like + "_. . ."]
    elif Girl == EmmaX:
        $ lines = ["I suppose that can't be helped. . ."]
    elif Girl == LauraX:
        $ lines = ["Well, you could always try something else. . ."]
    elif Girl == JeanX:
        $ lines = ["Your hands don't seem to be broken."]
    elif Girl == StormX:
        $ lines = ["Well, I cannot push you to breaking. . ."]
    elif Girl == JubesX:
        $ lines = ["Well, you could always try something else. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_less_than_two_rounds_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Mmmm. . ."]
    elif Girl == KittyX:
        $ lines = ["Hehe. . ."]
    elif Girl == EmmaX:
        $ lines = ["Excellent. . ."]
    elif Girl == LauraX:
        $ lines = ["Good. . ."]
    elif Girl == JeanX:
        $ lines = ["Good. . ."]
    elif Girl == StormX:
        $ lines = ["Thank you."]
    elif Girl == JubesX:
        $ lines = ["Cool. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_more_than_two_rounds_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Yeah, again. . ."]
    elif Girl == KittyX:
        $ lines = ["You know it. . ."]
    elif Girl == EmmaX:
        $ lines = ["Always. . ."]
    elif Girl == LauraX:
        $ lines = ["Always. . ."]
    elif Girl == JeanX:
        $ lines = ["Always. . ."]
    elif Girl == StormX:
        $ lines = ["Always. . ."]
    elif Girl == JubesX:
        $ lines = ["Yup. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_girl_also_tired_lines(Girl):
    if Girl == RogueX:
        $ lines = ["I guess I'm a bit tuckered out too, " + Girl.player_petname + "_. I guess we can take a breather."]
    elif Girl == KittyX:
        $ lines = ["I guess I'm kinda tired too, " + Girl.player_petname + "_. We can take a break. . .{p}. . .for now."]
    elif Girl == EmmaX:
        $ lines = ["I suppose I'm tired as well, " + Girl.player_petname + "_. We can take a breather. . ."]
    elif Girl == LauraX:
        $ lines = ["Yeah, you look like you've had enough. We can take a break. . .{p}}. . .for now."]
    elif Girl == JeanX:
        $ lines = ["Ok, sounds good. . ."]
    elif Girl == StormX:
        $ lines = ["I could use some rest as well, " + Girl.player_petname + "_."]
    elif Girl == JubesX:
        $ lines = ["Sure, I guess we can take a little break. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label sex_menu_cleanup_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Oh?"]
    elif Girl == KittyX:
        $ lines = ["Huh?"]
    elif Girl == EmmaX:
        $ lines = ["Huh?"]
    elif Girl == LauraX:
        $ lines = ["What?"]
    elif Girl == JeanX:
        $ lines = ["What?"]
    elif Girl == StormX:
        $ lines = ["Oh, what do you mean?"]
    elif Girl == JubesX:
        $ lines = ["What?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label end_of_action_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Ok, " + Girl.player_petname + " that's enough of that for now."]
    elif Girl == KittyX:
        $ lines = ["Time to take a little break, for now.",
            "Ok, we need to take a break.",
            "Ok, I'm kinda done for now, I need a break."]

        if Action_type == "blowjob":
            $ lines.append("Ok, I gotta rest my jaw for a minute. . .")
    elif Girl == EmmaX:
        $ lines = ["We need to stop for a moment, let me catch my breath.",
            "All right, " + Girl.player_petname + "_, that's plenty for now.",
            "Ok, " + Girl.player_petname + "_, that's enough of that for now.",
            "That's probably enough of that.",
            "Ok, that's enough, for now. . ."]

        if Action_type in cock_Action_types:
            $ lines.append("Ok, seriously, I'm putting it down for a minute.")

        if Action_type == "blowjob":
            $ lines.append("Ok, I need to rest my jaw for a minute. . .")
    elif Girl == LauraX:
        $ lines = ["Ok, " + Girl.player_petname + " breaktime.",
            "Ok, I'm kinda done for now, I need a break."]

        if Action_type in passive_Action_types:
            $ lines.append("Ok, I'm taking a quick break. . .")
    elif Girl == JeanX:
        $ lines = ["Ok, " + Girl.player_petname + " time for a break.",
            "Ok, that's it, break time."]
    elif Girl == StormX:
        $ lines = ["I need to take a moment to collect myself.",
            "That is enough of that."]
    elif Girl == JubesX:
        $ lines = ["Ok, that's it, I need a break.",
            "" + Girl.player_petname + "_, that will be enough for now."]

    Girl.voice "[line]"

    return

label ten_rounds_left_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["You might want to wrap this up, it's getting late."]
    elif Girl == KittyX:
        $ lines = ["It's" + Girl.Like + "_getting kinda late.",
            "It's kind of time to get moving.",
            "We might want to wrap this up, it's getting late."]
    elif Girl == EmmaX:
        $ lines = ["It's getting late. . .",
            "It's about time for a break.",
            "It's getting a bit late. . ."]

        if Action_type in active_Action_types:
            $ lines.append("You might want to wrap this up, it's getting late.")
            $ lines.append("You might want to think about your endgame here. . .")

        if Action_type in passive_Action_types:
            $ lines.append("I think I'll probably take a break soon.")
    elif Girl == LauraX:
        $ lines = ["It's getting late, we should wrap this up.",
            "It's kinda time to get moving.",
            "We might want to wrap this up, it's getting late."]
    elif Girl == JeanX:
        $ lines = ["Wow, look at the time. . ."]
    elif Girl == StormX:
        $ lines = ["It is getting late, " + Girl.player_petname + "_. . ."]

        if Action_type in active_Action_types:
            $ lines.append("You might want to consider finishing. . .")

        if Action_type in passive_Action_types:
            $ lines.append("I will probably take a break soon.")
    elif Girl == JubesX:
        $ lines = ["I could use a break soon. . .",
            "Wow, look at the time. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label five_rounds_left_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Seriously, it'll be time to stop soon."]
    elif Girl == KittyX:
        $ lines = ["We should wrap this up.",
            "For real" + Girl.like + "_time's up.",
            "Seriously, it'll be time to stop soon."]
    elif Girl == EmmaX:
        $ lines = ["We should take a break soon.",
            "Seriously, it'll be time to stop soon.",
            "Do you mind if we take a break?",
            "We'll need a break soon."]

        if Action_type == "masturbation":
            $ lines.append("Ung, I'm almost finished. . .")
    elif Girl == LauraX:
        $ lines = ["Tick tock, " + Girl.player_petname + "_."]

        if Action_type == "masturbation":
            $ lines.append("Five minutes, maybe.")
    elif Girl == JeanX:
        $ lines = ["We should probably wrap this up, " + Girl.player_petname + "_.",
            "Ok, can we take a break?"]
    elif Girl == StormX:
        $ lines = ["We should take a break soon.",
            "We shall require a break soon."]

        if Action_type == "masturbation":
            $ lines.append("Ah! I am nearly finished. . .")
    elif Girl == JubesX:
        $ lines = [". . . I could really use a break here. . ."]

        if Action_type == "masturbation":
            $ lines.append("Five minutes, maybe.")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label tired_lines(Girl, Action_type):
    if Girl == RogueX:
        if not multi_action:
            $ lines = ["Look, I think we can stay on this one thing. . ."]
        else:
            $ lines = ["I'm actually getting a little tired, so maybe we could wrap this up?"]
    if Girl == KittyX:
        if not multi_action:
            $ lines = ["I'm kinda tired, could we just wrap this up. . .",
                "Actually I'm getting a bit worn out, let's finish up here. . ."]
        else:
            $ lines = ["I'm actually getting a little tired, so maybe we could wrap this up?",
                "I kinda need a break, so if we could wrap this up?"]
    elif Girl == EmmaX:
        if not multi_action:
            $ lines = ["I'm kinda tired, could we just wrap this up. . ."]
        else:
            $ lines = ["Actually, could we wrap this up soon?",
                "I'm actually getting a little tired, perhaps we could wrap this up?"]
    elif Girl == LauraX:
        if not multi_action:
            $ lines = ["Maybe we could finish this up for now?"]
        else:
            $ lines = ["I need a break, can we wrap on this?"]
    elif Girl == JeanX:
        if not multi_action:
            $ lines = [ "I'd like to stick with this."]
        else:
            $ lines = []
    elif Girl == StormX:
        if not multi_action:
            $ lines = ["I would prefer to finish this."]
        else:
            $ lines = []
    elif Girl == JubesX:
        if not multi_action:
            $ lines = ["Maybe we could finish this up for now?"]
        else:
            $ lines = []

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label auto_rejected_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Ah, ah, Just keep doing what you were doing, " + Girl.player_petname + "_.",
            "Hey, just keep doing what you were doing, " + Girl.player_petname + "_.",
            "Oh! No, no thank you, " + Girl.player_petname + "_.",
            "Um, no, I'm not really. . . don't."]

        if Action_type in hand_Action_types:
            $ lines.append("Hands off the merchandise, " + Girl.player_petname + "_.")
            $ lines.append("Hands off, " + Girl.player_petname + "_.")

        if Action_type in finger_Action_types:
            $ lines.append("Keep it out of there, " + Girl.player_petname + "_.")
            $ lines.append("Keep it outside, " + Girl.player_petname + "_.")
    elif Girl == KittyX:
        $ lines = ["Nuh-uh, " + Girl.player_petname + "_, get back to what you were doing.",
            "Oooo! Um, no, no thanks. No. . .",
            "Whoa, back off, " + Girl.player_petname + "_.",
            "Um, don't do that. . .",
            "Um, what do you think you're doing?",
            "Hmm, kinda rude, " + Girl.player_petname + "_."]

        if Action_type in hand_Action_types:
            $ lines.append("Hands off, " + Girl.player_petname + "_.")

        if Action_type in ass_Action_types:
            $ lines.append("Um" + Girl.like + "_what are you doing back there?!")

        if Action_type in dildo_Action_types:
            $ lines.append("Hey, what are you planning to do with that?!")

        if Action_type in below_Action_types:
            $ lines.append("Heh, keep it above the belt, " + Girl.player_petname + "_.")

        if Action_type in insertion_Action_types:
            $ lines.append("Um, no take that out.")
    elif Girl == EmmaX:
        $ lines = ["Whoa, back off, " + Girl.player_petname + "_.",
            "" + Girl.player_petname + "_! Not now. . .",
            "Do you really think you can handle that?"]

        if Action_type in hand_Action_types:
            $ lines.append("Hands off, " + Girl.player_petname + "_.")

        if Action_type in finger_Action_types:
            $ lines.append("Careful what you put in there, you may not get it back.")

        if Action_type in mouth_Action_types:
            $ lines.append("I like where your head is at, so to speak, but perhaps hold off on that.")

        if Action_type in ass_Action_types:
            $ lines.append("Oh? What exactly are you doing back there?")

        if Action_type in fondle_Action_types:
            $ lines.append("Down boy, you were doing so well. . .")

        if Action_type in dildo_Action_types:
            $ lines.append("Excuse yourself, what are you planning to do with that?!")

        if Action_type in below_Action_types:
            $ lines.append("Perhaps we keep it above the waist, " + Girl.player_petname + "_.")

        if Action_type == "hotdog":
            $ lines.append("You might want to take a step back, " + Girl.player_petname + "_?")
    elif Girl == LauraX:
        $ lines = ["Roll it back, " + Girl.player_petname + "_. . .",
            "Whoa, back off, " + Girl.player_petname + "_.",
            "" + Girl.player_petname + "_! No. . ."]

        if Action_type in hand_Action_types:
            $ lines.append("Watch your hands, or lose them.")
            $ lines.append("Hands off, " + Girl.player_petname + "_.")

        if Action_type in dildo_Action_types:
            $ lines.append("Hey, what are you planning to do with that?!")

        if Action_type in below_Action_types:
            $ lines.append("Maybe we keep it above the waist, " + Girl.player_petname + "_.")

        if Action_type in anal_insertion_Action_types:
            $ lines.append("Oh? A backdoor intruder?")

        if Action_type == "eat_pussy":
            $ lines.append("Hey, good instincts, but maybe hold off?")

        if Action_type == "sex":
            $ lines.append("Oh, taking it all the way, are we?")

        if Action_type == "hotdog":
            $ lines.append("You might want to take a step back, " + Girl.player_petname + "_?")
    elif Girl == JeanX:
        $ lines = ["Not so fast, " + Girl.player_petname + "_. . .",
            "Hmmm, not yet, " + Girl.player_petname + "_.",
            "Ooo! Not right now, " + Girl.player_petname + "_.",
            "Whoa there, " + Girl.player_petname + "_!"]

        if Action_type in dildo_Action_types:
            $ lines.append("Hey, what are you planning to do with that?!")

        if Action_type in below_Action_types:
            $ lines.append("Keep it above the waist, " + Girl.player_petname + "_.")

        if Action_type in insertion_Action_types:
            $ lines.append("Just sticking it in?")

        if Action_type in anal_insertion_Action_types:
            $ lines.append("Sticking in the back?")

        if Action_type == "hotdog":
            $ lines.append("Little close there, " + Girl.player_petname + "_?")
    elif Girl == StormX:
        $ lines = ["Probably not, right now. . .",
            "Show some self control. . .",
            "Perhaps show some control. . .",
            "You go too far, " + Girl.player_petname + "_.",
            "" + Girl.player_petname + "_! Not now. . .",
            "Are you certain that is what you want?"]

        if Action_type in finger_Action_types:
            $ lines.append("Careful what you put in there, you may not get it back.")

        if Action_type in hand_Action_types:
            $ lines.append("Release me, " + Girl.player_petname + "_.")

        if Action_type in dildo_Action_types:
            $ lines.append("Excuse yourself, what are you planning to do with that?!")

        if Action_type in anal_insertion_Action_types:
            $ lines.append("Excuse me, what are you aiming at?")

        if Action_type in below_Action_types:
            $ lines.append("Perhaps we keep it above the waist, " + Girl.player_petname + "_.")

        if Action_type == "eat_pussy":
            $ lines.append("I appreciate the intent, but this is not the time for it.")

        if Action_type == "hotdog":
            $ lines.append("You are rather close, " + Girl.player_petname + "_. . .")
    elif Girl == JubesX:
        $ lines = ["Cool your jets, " + Girl.player_petname + "_. . .",
            "Whoa, back off, " + Girl.player_petname + "_.",
            "" + Girl.player_petname + "_! No. . ."]

        if Action_type in hand_Action_types:
            $ lines.append("Watch your hands, or lose them.")
            $ lines.append("Hands off, " + Girl.player_petname + "_.")

        if Action_type in below_Action_types:
            $ lines.append("Maybe we keep it above the waist, " + Girl.player_petname + "_.")

        if Action_type == "eat_pussy":
            $ lines.append("Hey, good instincts, but maybe hold off?")

        if Action_type == "sex":
            $ lines.append("Oh, taking it all the way, are we?")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label private_enough_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I guess this is private enough. . .",
            "Ok, I guess this is private enough. . .",
            "I guess here would be ok. . .",
            "Well, at least you got us some privacy this time. . ."]
    elif Girl == KittyX:
        $ lines = ["I guess here is fine. . .",
            "I guess this is more secluded. . .",
            "I guess this is out of the way. . .",
            "I guess this is a better location . .",
            "Well, I guess if it's here. . .",
            "Ok, I guess this is private enough. . .",
            "Ok, I guess this is private enough. . .",
            "Well, at least you got us some privacy this time. . .",
            "Um, I guess this is secluded enough. . ."]
    elif Girl == EmmaX:
        $ lines = ["This does seem less. . . exposed.",
            "I suppose this is more private.",
            "I suppose this is secluded enough. . .",
            "I suppose this is a better location . .",
            "Here, hmm?. . .",
            "Ok, I suppose this is secluded enough. . .",
            "Well, at least you got us some privacy this time. . .",
            "Um, I suppose this is secluded enough. . ."]
    elif Girl == LauraX:
        $ lines = ["This does seem less. . . exposed.",
            "Yeah, this is more covert.",
            "I guess this is secluded enough. . .",
            "I guess this is a better location . .",
            "Well, this is a bit more secure. . .",
            "Ok, I guess this is secluded enough. . .",
            "Hmm, this is private enough. . .",
            "Well, at least you got us some privacy this time. . .",
            "Um, I guess this is secure enough. . ."]
    elif Girl == JeanX:
        $ lines = ["I guess. . . maybe we could do it here. . .",
            "Ok, yeah, this is better.",
            "I guess here is fine. . .",
            "I guess this is a better location . .",
            "Well, I guess here might not be that bad. . .",
            "Ok, I guess this is secluded enough. . .",
            "Hmm, this is private enough. . .",
            "Well, at least you got us some privacy this time. . .",
            "Um, I guess we're alone enough like this. . ."]
    elif Girl == StormX:
        $ lines = ["This is a bit more secluded.",
            "I do suppose this is more private.",
            "I suppose this is secluded enough. . .",
            "I suppose that this is a better location . .",
            "Here, hmm?. . .",
            "Fine, I suppose this is secluded enough. . .",
            "Well, at least you got us some privacy this time. . ."]
    elif Girl == JubesX:
        $ lines = ["I guess this is less public. . .",
            "Well, this is a bit more secure. . .",
            "Well, at least you got us some privacy this time. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label recent_action_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Mmm, again? Ok.",
            "Mmm, again? Ok, let's get to it.",
            "Again? Ok.",
            "Mmmm. . .",
            "I guess I have a bit more in me. . .",
            "Again? K."]

        if Action_type == "handjob":
            $ lines.append("Mmm, again? Let me flex my hand a bit. . .")

        if Action_type == "footjob":
            $ lines.append("I don't want to wear them out. . .")

        if Action_type == "titjob":
            $ lines.append("Mmm, again? Ok, let me get the girls ready.")

        if Action_type == "blowjob":
            $ lines.append("Mmm, again? [stretches her jaw]")

        if Action_type in sex_Action_types:
            $ lines.append("You want to go again? Ok.")

        if Action_type in anal_insertion_Action_types:
            $ lines.append("I think I'm warmed up. . .")
    if Girl == KittyX:
        $ lines = ["Mmm, again? Ok.",
            "Mmm, again?",
            "Mmmm. . .",
            "I guess I could give it another go. . .",
            "Prrr. . .",
            "Mmm, again? Ok, let's get to it."]

        if Action_type == "handjob":
            $ lines.append("You're giving me carpal tunnel. . .")

        if Action_type == "footjob":
            $ lines.append("I'm getting foot cramps. . .")

        if Action_type == "blowjob":
            $ lines.append("Mmm, again? [stretches her jaw]")

        if Action_type in sex_Action_types:
            $ lines.append("Another round? {i}Fine.{/i}")

        if Action_type in anal_insertion_Action_types:
            $ lines.append("I guess I'm warmed up. . .")
    if Girl == EmmaX:
        $ lines = ["Mmmm, again? I suppose. . .",
            "Oh! Back for more?",
            "Mmm, again? Ok, let's get to it.",
            "Again? Oh, very well.",
            "I still have some. . . work I could be doing. . .",
            "Mmmm. . .",
            "Alright."]

        if Action_type == "handjob":
            $ lines.append("I will need to grade papers later, you know. . .")

        if Action_type == "footjob":
            $ lines.append("You know, heels are nightmare on the arches. . .")

        if Action_type == "blowjob":
            $ lines.append("Mmm, again? [yawns]")

        if Action_type in sex_Action_types:
            $ lines.append("Again? " + Girl.player_petname + "_, you're insatiable!")

        if Action_type in anal_insertion_Action_types:
            $ lines.append("I am warmed up. . .")
    if Girl == LauraX:
        $ lines = ["Mmmm, again? I guess. . .",
            "Huh, again?",
            "Mmm, again? Ok, let's get to it.",
            "More of that, huh. . .",
            "I have built up some more tension. . .",
            "Mmmm. . .",
            "Again? Fine, whatever."]

        if Action_type == "handjob":
            $ lines.append("Hmm, another handy then. . .")

        if Action_type == "blowjob":
            $ lines.append("Mmm, again? [yawns]")

        if Action_type in sex_Action_types:
            $ lines.append("Again? Your funeral.")

        if Action_type in anal_insertion_Action_types:
            $ lines.append("I am warmed up. . .")

        if Action_type in active_Action_types:
            $ lines.append("Sure, get in there.")
    if Girl == JeanX:
        $ lines = ["Mmmm, again? I guess. . .",
            "Huh, again?",
            "Mmm, again?",
            "Mmm, again? Ok, let's get to it.",
            "More of that, huh. . .",
            "Mmmm. . .",
            "Ok, sure.",
            "Again? Fine, whatever."]

        if Action_type in job_Action_types:
            $ lines.append("Well, I guess another wouldn't hurt. . .")

        if Action_type in sex_Action_types:
            $ lines.append("Again? Your funeral.")

        if Action_type in anal_insertion_Action_types:
            $ lines.append("I am warmed up. . .")
    if Girl == StormX:
        $ lines = ["Mmmm, again? I suppose. . .",
            "You cannot get enough?",
            "Mmm, again?",
            "Mmm, again? Ok, let's get to it.",
            "I suppose so. . .",
            "Again? Oh, very well.",
            "I suppose that I was not. . . finished. . .",
            "Mmmm. . .",
            "Of course."]

        if Action_type in job_Action_types:
            $ lines.append("I do not know if I have it in me. . .")

        if Action_type in sex_Action_types:
            $ lines.append("Again? " + Girl.player_petname + "_, you are a lion!")

        if Action_type in anal_insertion_Action_types:
            $ lines.append("I am properly stretched out. . .")
    if Girl == JubesX:
        $ lines = ["Mmmm, again? I guess. . .",
            "I have built up some more stress. . ."]

        if Action_type == "handjob":
            $ lines.append("Hmm, another handy then. . .")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label taboo_action_rejected_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I really don't think this is the right place for that!",
            "" + Girl.player_petname + "_! Not in public!",
            "This just really isn't the time or place, " + Girl.player_petname + "_!",
            "Not in such an exposed place, " + Girl.player_petname + "_.",
            "Not here!",
            "I'd be a bit embarassed doing that here."]

        if Action_type in cock_Action_types:
            $ lines.append("You really expect me to do that here? You realize how. . . exposed that would be?")
            $ lines.append("You really expect me to do that here?")
            $ lines.append("Even if I wanted to, it certainly wouldn't be here!")

        if Action_type in sex_Action_types:
            $ lines.append("That you would even suggest such a thing in a place like this. . .")

        if Action_type in passive_Action_types:
            $ lines.append("I can't do that here!")
    elif Girl == KittyX:
        $ lines = ["I don't like being so. . . exposed.",
            "Time and place, " + Girl.player_petname + "_!",
            "This just really isn't the time or place, " + Girl.player_petname + "_!",
            "" + Girl.player_petname + "_! Not here!",
            "" + Girl.player_petname + "_! Time and place!",
            "This is way too exposed!",
            "Not here!",
            "Certainly not here!",
            "Not here, not anywhere near here.",
            "" + Girl.Like + "_not here though?"]

        if Action_type in cock_Action_types:
            $ lines.append("You're being ridiculous. That? Here?!")

        if Action_type in passive_Action_types:
            $ lines.append("You really expect me to do that here? You realize how. . . exposed that would be?")

        if Action_type in sex_Action_types:
            $ lines.append("I can't believe you'd even consider it around here!")
    elif Girl == EmmaX:
        $ lines = ["I can't be seen doing that with you.",
            "I have a reputation to maintain.",
            "I couldn't possibly do that. . . here!",
            "This is way too exposed!",
            "Obviously not in someplace so exposed.",
            "Not here!",
            "This truly isn't an appropriate place for that.",
            "How can you imagine this would be an appropriate location?",
            "This area is a bit too exposed for that sort of thing. . ."]

        if Action_type in cock_Action_types:
            $ lines.append("Can you imagine the scandal? Here?")

        if Action_type == "anal":
            if approval_check(EmmaX, 500, "I"):
                $ lines.append("How can you imagine this would be an appropriate location?.{p}This place, I mean, not anal.{p}Anal can be nice, sometimes.")
            else:
                $ lines.append("How can you imagine this would be an appropriate location?.{p}This place, I mean, not anal.{p}Anal can be nice, sometimes.{p}Maybe not with you.")
    elif Girl == LauraX:
        $ lines = ["I try to stay off the radar.",
            "This area's too exposed.",
            "Not here!",
            "This is too exposed.",
            "This place is way too exposed."]

        if Action_type in cock_Action_types:
            $ lines.append("You really expect me to do that here? This isn't exactly \"covert\".")
            $ lines.append("This area is a bit too exposed for that sort of thing. . .")

        if Action_type in passive_Action_types:
            $ lines.append("I couldn't do that in public.")
    elif Girl == JeanX:
        $ lines = ["I'm. . . not comfortable. . . in public. . .",
            "I'm not comfortable in public right now. . .",
            "Not here!",
            "This is too public.",
            "I'm just not comfortable with that right now. . .",
            "This area is a bit too exposed for that sort of thing. . ."]

        if Action_type in cock_Action_types:
            $ lines.append("You really expect me to do that here?{p}You know I can't \"take care of that\" anymore. . .")

        if Action_type in passive_Action_types:
            $ lines.append("I. . . couldn't do that in public. . .")
    elif Girl == StormX:
        $ lines = ["I should not be seen doing that.",
            "I do not wish to make a spectacle.",
            "This is much too exposed.",
            "Not here!",
            "This truly is not an appropriate place for that.",
            "This area is a bit too exposed for that sort of thing. . ."]

        if Action_type in cock_Action_types:
            $ lines.append("I could not possibly do that here.")

        if Action_type in sex_Action_types:
            $ lines.append("How could you imagine that this would be an appropriate location?")

        if Action_type in passive_Action_types:
            $ lines.append("I cannot do that here.")
    elif Girl == JubesX:
        $ lines = ["I don't wanna make a scene."]

        if Action_type in passive_Action_types:
            $ lines.append("I don't want to do this in public!")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label taboo_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I told you not in public!",
            "I already told you this is too public!",
            "This is just way too exposed!",
            "I said not in public!"]

        if Action_type in passive_Action_types:
            $ lines.append("I already told you that I wouldn't do that out here!")

        if Action_type in dildo_Action_types:
            $ lines.append("Stop swinging that thing around in public!")

        if Action_type == "hotdog":
            $ lines.append("I told you that I didn't want you rubb'in up on me in public!")
    elif Girl == KittyX:
        $ lines = ["Not here!",
            "This is just way too exposed!",
            "I told you this is too public!",
            "I said not in public!",
            "I already told you this is too public!",
            "I{i}just{/i}" + Girl.like + "_told you, not in public!"]

        if Action_type in passive_Action_types:
            $ lines.append("I already told you that I wouldn't do that out here!")

        if Action_type in dildo_Action_types:
            $ lines.append("Stop swinging that thing around in public!")
    elif Girl == EmmaX:
        $ lines = ["As I said, not here, " + Girl.player_petname + "_.",
            "This is not an appropriate place for that.",
            "I told you this is too public!",
            "I told you, not in public!",
            "I already told you this is too public!",
            "I already told you. . . not in such an exposed location."]

        if Action_type in passive_Action_types:
            $ lines.append("I already told you that I wouldn't do that out here!")

        if Action_type in dildo_Action_types:
            $ lines.append("Stop showing that thing around in public!")
    elif Girl == LauraX:
        $ lines = ["I told you, not here, " + Girl.player_petname + "_.",
            "I said not in public.",
            "This is just way too exposed!",
            "Like I told you, too public!",
            "I said not in public!",
            "I already told you this is too public!",
            "I told you. . . this place is too exposed."]

        if Action_type in passive_Action_types:
            $ lines.append("I already told you that I wouldn't do that out here!")

        if Action_type in dildo_Action_types:
            $ lines.append("Stop swinging that thing around in public!")
    elif Girl == JeanX:
        $ lines = ["I told you. . . not here, " + Girl.player_petname + "_.",
            "I told you I wasn't comfortable in public. . .",
            "I don't want to show off the goods like that!",
            "Like I said, too public!",
            "I said not in public!",
            "I told you, I'm not comfortable with that. . .",
            "I'm not comfortable with that. . ."]

        if Action_type in dildo_Action_types:
            $ lines.append("Stop swinging that thing around in public!")
    elif Girl == StormX:
        $ lines = ["This area is too public, " + Girl.player_petname + "_.",
            "As I said, not here, " + Girl.player_petname + "_.",
            "I was very clear, this is too public.",
            "This is not an appropriate place for that.",
            "I told you this is too public!",
            "I informed you, not in public!",
            "I have already informed you, this is too public!",
            "I already informed you. . . not in such an exposed location."]

        if Action_type in passive_Action_types:
            $ lines.append("I already told you that I wouldn't do that out here!")

        if Action_type in dildo_Action_types:
            $ lines.append("Stop showing that thing around in public!")
    elif Girl == JubesX:
        $ lines = ["I told you, not here, " + Girl.player_petname + "_.",
            "I said not in public."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label action_not_done_yet_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I just don't think I'm ready yet, " + Girl.player_petname + "_. . .",
            "I. . . don't think that's. . .",
            "That's. . . a little intimate, " + Girl.player_petname + "_.",
            "Not now, " + Girl.player_petname + "_.",
            "Let's not, ok " + Girl.player_petname + "_?",
            "Not yet, " + Girl.player_petname + "_. . .",
            "Oh, um, no, I'm not really comfortable with that. . .",
            "I'm not really up for that, " + Girl.player_petname + "_. . .",
            ". . . well I don't know about that, " + Girl.player_petname + "_. . .",
            "I just don't think I'm ready yet, " + Girl.player_petname + "_. . .",
            "I'm just not into that, " + Girl.player_petname + "_. . .",
            "I. . . don't think that's. . ."]

        if Action_type in pussy_Action_types:
            $ lines.append("Um, not down there, " + Girl.player_petname + "_. . .")

        if Action_type in ass_Action_types:
            $ lines.append("That's kinda naughty, " + Girl.player_petname + "_. . .")

        if Action_type in dildo_Action_types:
            $ lines.append("I'm just not into toys, " + Girl.player_petname + "_. . .")

        if Action_type == "handjob":
            $ lines.append("I don't really want to touch it, " + Girl.player_petname + "_. . .")

        if Action_type == "blowjob":
            $ lines.append("I don't think I'd like the taste, " + Girl.player_petname + "_. . .")
    elif Girl == KittyX:
        $ lines = ["I'm" + Girl.like + "_not ready for that, " + Girl.player_petname + "_. . .",
            "Not. . . yet. . . maybe later.",
            "Not yet, " + Girl.player_petname + "_. . .",
            "I. . . don't think that's. . .",
            "I'm not really up for that, " + Girl.player_petname + "_. . .",
            "I don't know that I'm. . ." + Girl.like + "_ready? . .",
            "I don't know, " + Girl.player_petname + "_. . .",
            "That's kinda hot, " + Girl.player_petname + "_. . ."]

        if Action_type in pussy_Action_types:
            $ lines.append("Um, not down there, " + Girl.player_petname + "_. . .")

        if Action_type in dildo_Action_types:
            $ lines.append("I'm just not into toys, " + Girl.player_petname + "_. . .")

        if Action_type in ["eat_pussy", "eat_ass"]:
            $ lines.append("That's pretty intimate, " + Girl.player_petname + "_. . .")

        if Action_type in ["eat_ass", "dildo_ass", "anal"]:
            $ lines.append("I don't know that I'm. . ." + Girl.like + "_that kind of girl?")

        if Action_type == "masturbation":
            $ lines.append("That's. . . private? You know?")

        if Action_type == "blowjob":
            $ lines.append("I don't know about the taste, " + Girl.player_petname + "_. . .")
    elif Girl == EmmaX:
        $ lines = ["Let's work up to that, perhaps. . .",
            "Seems a bit forward, " + Girl.player_petname + "_.",
            "I don't think we're there yet, " + Girl.player_petname + "_. . .",
            "I'm not sure we're at that stage, " + Girl.player_petname + "_. . .",
            "Not yet, " + Girl.player_petname + "_. . .",
            "Are you sure though, " + Girl.player_petname + "_?. . .",
            "Perhaps later, " + Girl.player_petname + "_. . .",
            "I'm unsure, " + Girl.player_petname + "_. . .",
            "I don't know that you're ready for that yet.",
            "Hmm, that could be amusing, " + Girl.player_petname + "_. . ."]

        if Action_type in breast_Action_types:
            $ lines.append("I highly doubt you could handle them, " + Girl.player_petname + "_. . .")

        if Action_type in ass_Action_types:
            $ lines.append("That's really not my usual style. . .")

        if Action_type in dildo_Action_types:
            $ lines.append("I'm a bit past toys, " + Girl.player_petname + "_. . .")
            $ lines.append("I'm just not into toys, " + Girl.player_petname + "_. . .")

        if Action_type in sex_Action_types:
            $ lines.append("I really doubt you understand what you're in for. . .")

        if Action_type == "masturbation":
            $ lines.append("I don't know that I want to perform.")

        if Action_type == "blowjob":
            $ lines.append("I'm not sure you're up to my usual tastes, " + Girl.player_petname + "_. . .")
    elif Girl == LauraX:
        $ lines = ["Look, I don't know if we're ready for that, " + Girl.player_petname + "_. . .",
            "Let's work up to that maybe. .",
            "Seems a bit aggressive, " + Girl.player_petname + "_.",
            "I don't think we're there yet, " + Girl.player_petname + "_. . .",
            "Not yet, " + Girl.player_petname + "_. . .",
            "Seriously, " + Girl.player_petname + "_. . .",
            "Eh, " + Girl.player_petname + "_. . .",
            "I don't know that I want to do that right now.",
            "Hmm, that could be amusing, " + Girl.player_petname + "_. . ."]

        if Action_type in ass_Action_types:
            $ lines.append("That's really not my style. . .")
            $ lines.append("I'm not really into that, " + Girl.player_petname + "_. . .")

        if Action_type in dildo_Action_types:
            $ lines.append("I'm just not into toys, " + Girl.player_petname + "_. . .")

        if Action_type == "blowjob":
            $ lines.append("I don't know if your taste will match your scent, " + Girl.player_petname + "_. . .")

        if Action_type in ["sex", "anal"]:
            $ lines.append("Oh, you have no idea what you're in for. . .")
            $ lines.append("I don't know that you're ready for that yet.")
    elif Girl == JeanX:
        $ lines = ["Let's work up to that maybe. .",
            "I don't think we're there yet, " + Girl.player_petname + "_. . .",
            "Mmmm, not right now, " + Girl.player_petname + "_. . .",
            "Not yet, " + Girl.player_petname + "_. . .",
            "Seriously, " + Girl.player_petname + "_. . .",
            "Well. . .",
            "I don't know, it's kind of a bad time. . .",
            "Hmm, that could be amusing, " + Girl.player_petname + "_. . ."]

        if Action_type in hand_Action_types:
            $ lines.append("Look, don't touch, " + Girl.player_petname + "_. . .")

        if Action_type in ass_Action_types:
            $ lines.append("That's really not my style. . .")
            $ lines.append("Not really my thing, " + Girl.player_petname + "_. . .")

        if Action_type in dildo_Action_types:
            $ lines.append("I'm just not into toys, " + Girl.player_petname + "_. . .")

        if Action_type == "blowjob":
            $ lines.append("I have been wondering what you taste like, " + Girl.player_petname + "_. . .")

        if Action_type in ["sex", "anal"]:
            $ lines.append("Oh, this would be interesting. . .")
            $ lines.append("I don't know that you're ready for that yet.")
    elif Girl == StormX:
        $ lines = ["Perhaps some other time, " + Girl.player_petname + "_. . .",
            "Mmm. . . that would. . . no. . .",
            "Perhaps go slower, " + Girl.player_petname + "_. . .",
            "Oh, that would. . .perhaps not, " + Girl.player_petname + "_. . .",
            "I would rather not, " + Girl.player_petname + "_. . .",
            "I am unsure about that. . .",
            "I am unsure about this.",
            "Are you certain, " + Girl.player_petname + "_? . .",
            "I am not sure I would enjoy this, " + Girl.player_petname + "_. . .",
            "I am unsure, " + Girl.player_petname + "_. . .",
            "Hmm, that could be entertaining, " + Girl.player_petname + "_. . ."]

        if Action_type in dildo_Action_types:
            $ lines.append("I'm a bit past toys, " + Girl.player_petname + "_. . .")
            $ lines.append("I'm just not into toys, " + Girl.player_petname + "_. . .")

        if Action_type in active_Action_types:
            $ lines.append("I would rather you did not, " + Girl.player_petname + "_.")

        if Action_type in ["sex", "anal"]:
            $ lines.append("I seriously doubt that you understand what you would be in for. . .")
            $ lines.append("I do not know that you are yet prepared for that.")
    elif Girl == JubesX:
        $ lines = ["Look, I don't know if we're ready for that, " + Girl.player_petname + "_. . .",
            "Let's work up to that maybe. .",
            "I don't know, I'm not really into it right now.",
            "Kinda forward, " + Girl.player_petname + "_.",
            "I don't think we're there yet, " + Girl.player_petname + "_. . .",
            "I'm not sure we're there yet, " + Girl.player_petname + "_. . .",
            "Not yet, " + Girl.player_petname + "_. . .",
            "Seriously, " + Girl.player_petname + "_. . ."]

        if Action_type in ass_Action_types:
            $ lines.append("That's really not my style. . .")

        if Action_type in dildo_Action_types:
            $ lines.append("I'm just not into toys, " + Girl.player_petname + "_. . .")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label sorry_never_mind_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Ok, no problem, " + Girl.player_petname + "_.",
            "Yeah, fine, " + Girl.player_petname + "_.",
            "Yeah, ok, " + Girl.player_petname + "_.",
            "Fine.",
            "No problem."]
    elif Girl == KittyX:
        $ lines = ["It's cool, " + Girl.player_petname + "_.",
            "No problem.",
            "Yeah, ok, " + Girl.player_petname + "_.",
            "Aw, it's ok, " + Girl.player_petname + "_.",
            "Yeah.",
            "It's cool."]
    elif Girl == EmmaX:
        $ lines = ["Don't concern yourself, " + Girl.player_petname + "_.",
            "No offense taken. I get it.",
            "I appreciate your restraint.",
            "I appreciate your restraint, " + Girl.player_petname + "_.",
            "Quite alright.",
            "That's all right, " + Girl.player_petname + "_.",
            "No harm done, " + Girl.player_petname + "_.",
            "I thought as much, " + Girl.player_petname + "_.",
            "I'm sure, " + Girl.player_petname + "_.",
            "Thank you.",
            "I can appreciate your. . . drive.",
            "I don't blame you for your. . . enthusiasm.",
            "No harm in asking. Once."]
    elif Girl == LauraX:
        $ lines = ["No worries.",
            "It's cool.",
            "It's cool, " + Girl.player_petname + "_.",
            "It's fine.",
            "Yeah, ok, " + Girl.player_petname + "_.",
            "Cool.",
            "Sure, no problem.",
            "Well, you are persistent.",
            "Hey, I can't blame you.",
            "So long as you don't push it."]
    elif Girl == JeanX:
        $ lines = ["It's fine, I get it.",
            "It's fine.",
            "Ok, fine, " + Girl.player_petname + "_.",
            "Ok then.",
            "Yeah, ok, " + Girl.player_petname + "_.",
            "Sure, it's fine.",
            "Keep trying. . .",
            "I get it.",
            "So long as you don't push it."]
    elif Girl == StormX:
        $ lines = ["Don't concern yourself, " + Girl.player_petname + "_.",
            "No offense taken. I get it.",
            "I appreciate your restraint.",
            "I appreciate your restraint, " + Girl.player_petname + "_.",
            "I understand.",
            "That is fine, " + Girl.player_petname + "_.",
            "It is fine, " + Girl.player_petname + "_.",
            "I thought as much, " + Girl.player_petname + "_.",
            "I'm sure, " + Girl.player_petname + "_.",
            "Thank you.",
            "I can appreciate your. . . desires.",
            "I cannot blame you for your. . . desires.",
            "There is no harm in asking."]
    elif Girl == JubesX:
        $ lines = ["Yeah, whatever.",
            "It's fine."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label maybe_later_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I'll give it some thought, " + Girl.player_petname + "_.",
            "It's. . . possible, " + Girl.player_petname + "_.",
            "I'll be thinking about it, " + Girl.player_petname + "_.",
            "Anything's possible, " + Girl.player_petname + "_.",
            "Heh, maybe, " + Girl.player_petname + "_.",
            "I'll give it some thought, " + Girl.player_petname + "_.",
            ". . .{p}I guess?",
            "We'll have to see.",
            "I might get hungry, " + Girl.player_petname + "_.",
            "Yeah, maybe, " + Girl.player_petname + "_."]

        if Action_type in dildo_Action_types:
            $ lines.append("Maybe I'll practice on my own time, " + Girl.player_petname + "_.")

        if Action_type == "masturbation":
            if Girl.lust > 50:
                $ lines.append("Well, definitely later. . . but I'll have to think about inviting you.")
            else:
                $ lines.append("Hmm, maybe. . . I'll let you know.")
    elif Girl == KittyX:
        $ lines = ["Um, yeah, maybe later.",
            "I'll give it some thought, " + Girl.player_petname + "_.",
            "Heh, maybe, " + Girl.player_petname + "_.",
            "It's. . . possible, " + Girl.player_petname + "_.",
            ". . .{p}}Maybe.",
            "Maybe.",
            "You" + Girl.like + "_never know, " + Girl.player_petname + "_.",
            "Maybe, you never know.",
            "Yeah, maybe, " + Girl.player_petname + "_.",
            "I'll be thinking about it, " + Girl.player_petname + "_.",
            "Anything's possible, " + Girl.player_petname + "_."]

        if Action_type in dildo_Action_types:
            $ lines.append("Maybe I'll practice on my own time, " + Girl.player_petname + "_.")

        if Action_type == "masturbation":
            if Girl.lust > 50:
                $ lines.append("Well, I know what {i}I'll{/i} be doing later. Not sure if you can come.{p}I mean- you know, be there.{p}I'm not sure you'll {i}be{/i} there.{p}. . .coming.")
            else:
                $ lines.append("Hmm, maybe. . . I'll text you?")
    elif Girl == EmmaX:
        $ lines = ["Well, I can't rule it out. . .",
            "I'll give it some thought, " + Girl.player_petname + "_.",
            "It's. . . possible, " + Girl.player_petname + "_.",
            ". . .{p}}I couldn't rule it out. . .",
            "Perhaps.",
            "I wouldn't rule it out, " + Girl.player_petname + "_.",
            ". . .{p}Perhaps.",
            "Oh, most certainly. . .", "I imagine we will. . .{p}}. . . often.",
            "I imagine it will happen at some point, " + Girl.player_petname + "_.",
            "I'll be thinking about it, " + Girl.player_petname + "_.",
            "Anything's possible, " + Girl.player_petname + "_."]

        if Action_type in dildo_Action_types:
            $ lines.append("Maybe I'll practice on my own time, " + Girl.player_petname + "_.")
            $ lines.append("Perhaps I'll practice on my own time, " + Girl.player_petname + "_.")

        if Action_type == "masturbation":
            if Girl.lust > 50:
                $ lines.append("I have plans for. . . later, but perhaps you could take part.")
            else:
                $ lines.append("I couldn't say.")
    elif Girl == LauraX:
        $ lines = ["Eh. Maybe.",
            "Maybe?",
            "Maybe, " + Girl.player_petname + "_.",
            "It's. . . possible, " + Girl.player_petname + "_.",
            "Maybe.",
            "Yeah, maybe, " + Girl.player_petname + "_.",
            ". . .{p}}Maybe.",
            "Probably. . .",
            "Oh, probably. . .{p}. . . often.",
            "I gues eventually. . .",
            "I'll be thinking about it, " + Girl.player_petname + "_.",
            "Anything's possible, " + Girl.player_petname + "_."]

        if Action_type in dildo_Action_types:
            $ lines.append("Maybe I'll practice on my own time, " + Girl.player_petname + "_.")

        if Action_type == "masturbation":
            if Girl.lust > 50:
                $ lines.append("I probably will be, but not with an audience.")
            else:
                $ lines.append("Hmm, maybe. . .")
    elif Girl == JeanX:
        $ lines = [". . . I guess? Maybe.",
            "Maybe.",
            ". . . maybe.",
            "Sure, whatever, " + Girl.player_petname + "_.",
            "Well. . .{p}}Maybe.",
            "Sure, whatever. . .",
            "Oh, probably. . .",
            "I guess eventually. . .",
            "Well, I'll give it some thought, " + Girl.player_petname + "_."]

        if Action_type in dildo_Action_types:
            $ lines.append("Maybe I'll practice on my own time, " + Girl.player_petname + "_.")

        if Action_type == "masturbation":
            if Girl.lust > 50:
                $ lines.append("Well -I- will, but after you leave.")
            else:
                $ lines.append("Well. . . maybe. . .")
    elif Girl == StormX:
        $ lines = ["I will give it some thought, " + Girl.player_petname + "_.",
            ". . .{p}Perhaps. . .",
            "Perhaps.",
            "I would not rule it out, " + Girl.player_petname + "_.",
            ". . .{p}Perhaps.",
            "Oh, of that I am certain. . .",
            "I imagine at some point we shall. . .{p}. . . frequently.",
            "I expect it will happen at some point, " + Girl.player_petname + "_.",
            "I will give it some thought, " + Girl.player_petname + "_."]

        if Action_type in dildo_Action_types:
            $ lines.append("Maybe I'll practice on my own time, " + Girl.player_petname + "_.")
            $ lines.append("Perhaps I'll practice on my own time, " + Girl.player_petname + "_.")

        if Action_type == "masturbation":
            if Girl.lust > 50:
                $ lines.append("I expect that I will be finished by then. . .")
            else:
                $ lines.append("We shall see.")
    elif Girl == JubesX:
        $ lines = ["Eh. Maybe.",
        "Maybe, " + Girl.player_petname + "_.",
        "Maybe?",
        "It's. . . possible, " + Girl.player_petname + "_.",
        "Maybe.",
        "I'll be thinking about it, " + Girl.player_petname + "_.",
        "Anything's possible, " + Girl.player_petname + "_."]

        if Action_type in dildo_Action_types:
            $ lines.append("Maybe I'll practice on my own time, " + Girl.player_petname + "_.")

        if Action_type == "masturbation":
            if Girl.lust > 50:
                $ lines.append("Maybe, just not with so many eyes on me. . .")
            else:
                $ lines.append("Hmm, maaaybe. . .")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label pull_back_before_get_in_lines(Girl, Action_type):
    if Girl == RogueX:
        if Girl.permanent_History[action]:
            $ lines = ["Well ok, " + Girl.player_petname + "_, no harm done. Just give me a little warning next time.",
                "Well ok, " + Girl.player_petname + "_, it has been kinda fun."]
        else:
            $ lines = ["Well ok, " + Girl.player_petname + "_, I'm not really ready for that, but maybe if you ask nicely next time . . ."]

            if Action_type in anal_insertion_Action_types:
                $ lines.append("Well ok, " + Girl.player_petname + "_, that's a bit dirty, maybe ask a girl?")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label would_you_like_more_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["You maybe want to try something more?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label caught_masturbating_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["H- how long you been stand'in there, " + Girl.player_petname + "_?"]
    elif Girl == KittyX:
        $ lines = ["Eeep!{p}When did you get here?!"]
    elif Girl == EmmaX:
        $ lines = ["!{p}How long have you been there?!"]
    elif Girl == LauraX:
        $ lines = ["Huh.{p}}When did you get here?"]
    elif Girl == JeanX:
        $ lines = ["Oh, hey. . ." + Girl.player_petname + "_.{p}}When did you get here?"]
    elif Girl == StormX:
        $ lines = ["!{p}}How long have you been there?!"]
    elif Girl == JubesX:
        $ lines = ["Oh!{p}}How long were you standing there?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label notices_penis_is_out_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["And why is your cock out like that?!"]
    elif Girl == KittyX:
        $ lines = ["And um. . . your cock is out. . . "]
    elif Girl == EmmaX:
        $ lines = ["And I see you've been busy. . . "]
    elif Girl == LauraX:
        $ lines = ["And um. . . you have your penis out. . . "]
    elif Girl == JeanX:
        $ lines = ["I see you've been making yourself at home. . . "]
    elif Girl == StormX:
        $ lines = [". . . I notice you're taken care of yourself. . . "]
    elif Girl == JubesX:
        $ lines = ["And um. . . you have your penis out. . . "]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

label too_late_to_masturbate_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["It's getting too late to do much about it right now though."]
    elif Girl == KittyX:
        $ lines = ["It's getting kinda late to do anything about it. . ."]
    elif Girl == EmmaX:
        $ lines = ["Unfortunately it's getting rather late."]
    elif Girl == LauraX:
        $ lines = ["I kinda needed a break anyway. . ."]
    elif Girl == JeanX:
        $ lines = ["I could use a break anyway. . ."]
    elif Girl == StormX:
        $ lines = ["It seems that it has gotten late while I was. . . distracted."]
    elif Girl == JubesX:
        $ lines = ["Well, I kinda needed a break anyway. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label begging_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Heh, I suppose I can hardly refuse ya when you use the magic words . . .",
            "Well, if you're gonna beg. . .",
            "Sure, put'im here.",
            "No problem.",
            "Sure, I guess.",
            "Okay.",
            "I guess. . .",
            "Ok, [She gestures for you to come over].",
            "Heh, ok.",
            "Well. . . ok.",
            "Sure!",
            "I guess I could. . . give it a go.",
            "Heh, ok, ok.",
            "Well, sure, ahhhhhh.",
            "Well. . . ok.",
            "I guess a taste couldn't hurt.",
            "I guess I could. . . whip it out.",
            "Fine. . . [She licks her lips].",
            "Heh, ok, alright."]

        if Action_type in cock_Action_types:
            $ lines.append("Ok, lemme see it.")
            $ lines.append("Sure. Drop trou.")
            $ lines.append("I suppose, whip it out.")

        if Action_type == "masturbation":
            $ lines.append("I suppose it would help to have something nice to look at. . .")
            $ lines.append("I've kind of needed this anyways. . .",)

        if Action_type == "suck_breasts":
            $ lines.append("You better work your mouth that hard on these.")
    elif Girl == KittyX:
        $ lines = ["Well" + Girl.like + "_if you ask nicely. . .",
            "Only if you make it worth it.",
            "I like it when you beg. . .",
            "Well, sure, I guess.",
            "Well. . . ok.",
            "Heh, ok, fine.",
            "Sure, I guess.",
            "Ooooookay.",
            "Ok. . . [She gestures for you to come over].",
            "Heh, ok, ok."]

        if Action_type in cock_Action_types:
            $ lines.append("Cool, lemme see it.")

        if Action_type in passive_Action_types:
            $ lines.append("I could maybe give it a try.")
            $ lines.append("I guess I could. . .")

        if Action_type == "blowjob":
            $ lines.append("Fiiine. . . [She licks her lips].")
    elif Girl == EmmaX:
        $ lines = ["Politeness can be rewarded. . .",
            "Oh, if you insist. . .",
            "I do enjoy hearing you beg. . .",
            "Well, I suppose.",
            "Well. . . ok.",
            "I could perhaps give it a try.",
            "I suppose I could. . .",
            "Fine. . . [She licks her lips].",
            "Hmph, ok, fine.",
            "Oh, I suppose.",
            "I'll do it.",
            "Well, give it here.",
            "I suppose I could. . .",
            "Fine. . . [She gestures for you to come over].",
            "Ok, ok.",
            "Sure, I suppose.",
            "Fine.",
            "Very well, bring it out.",
            "Hmm, ok.",
            "Huh. Ok.",
            "Couldn't hurt having you around. . .",
            "Two birds with one stone. . .",
            "K.",
            "Sure, why not?",
            "Lol, ok."]
    elif Girl == LauraX:
        $ lines = ["Well if you're going to be a little bitch about it. . .",
            "Ok, fine. . .",
            "Oooh, beg for me. . .",
            "Sure. Ahhhhhh.",
            "Well. . . alright.",
            "Yum.",
            "Sure, whip it out.",
            "Ok. . . [She licks her lips].",
            "Alright, let's see it.",
            "O-kay.",
            "Fine.",
            "I suppose I could. . .",
            "Ok. . . [She gestures for you to come over].",
            "Ok, ok.",
            "Sure, I guess.",
            "OK.",
            "Fine, lemme see it.",
            "I guess I could. . .",
            "Heh, ok, ok.",
            "Ok.",
            "It couldn't hurt having you around. . .",
            "Very well.",
            "Sure, why not?",
            "[chuckles]. . . ok.",
            "Huh. Ok.",
            "Couldn't hurt. . .",
            "Alright.",
            "Sure.",
            "Heh, ok."]
    elif Girl == JeanX:
        $ lines = ["Oh, fine, just don't start crying.",
            "Ok, fine. . .",
            "Oooh, beg for me. . .",
            "Sure. Ahhhhhh.",
            "Well. . . alright.",
            "Yum.",
            "Sure, whip it out.",
            "Ok. . . [She licks her lips].",
            "Alright, let's see it.",
            "Sure, I guess.",
            "Okay. . . ",
            "Fine.",
            "I suppose I could. . .",
            "Ok. . . Get over here. . .",
            "Ok, ok.",
            "OK.",
            "Fine, lemme see it.",
            "I guess I could. . .",
            "Ok. . . [She gestures for you to come over].",
            "Heh, ok, ok.",
            "Sure. Ok.",
            "Couldn't hurt. . .",
            "Alright.",
            "Sure.",
            "Sure, why not. . ."]
    elif Girl == StormX:
        $ lines = ["Well, I suppose. . .",
            "Oh, if you insist. . .",
            "I suppose it does not hurt. . .",
            "I suppose it could not hurt. . .",
            "Well, one could not hurt. . .",
            "[line]"
            "[line]"
            "[line]"
            "Well, I suppose.",
            "Well. . . ok.",
            "I could perhaps give it a try.",
            "I suppose that I could. . .",
            "Fine. . . [She licks her lips].",
            "Hmph, ok, fine.",
            "Oh, I suppose we might.",
            "I would do this.",
            "Very well, give it here.",
            "I suppose that I could. . .",
            ". . . Fine. [She gestures for you to come over]",
            "Ok, ok.",
            "Hmm, I suppose.",
            "Fine.",
            "Very well, bring it out.",
            "I suppose that I could. . .",
            "Fine. . . [She gestures for you to come over].",
            "Hmm, ok.",
            "You really do like to watch.",
            "Once more?",
            "You enjoy watching me do that?",
            "You want me to take care of myself?"]
    elif Girl == JubesX:
        $ lines = ["Geeze, don't whine about it. . .",
            "Ok, fine. . .",
            "Huh. Ok.",
            "Couldn't hurt. . .",
            "Alright.",
            "Sure.",
            "Heh, ok."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label please_not_good_enough_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I'm afraid not this time, sorry " + Girl.player_petname + "_."]
    elif Girl == KittyX:
        $ lines = ["Um, still no.",
            "Nuh uh."]
    elif Girl == EmmaX:
        $ lines = ["This wasn't a \"tone\" issue.",
            "No."]
    elif Girl == LauraX:
        $ lines = ["Well if you're going to be a little bitch about it. . .",
            "No."]
    elif Girl == JeanX:
        $ lines = ["No way.",
            "Oh, don't cry.",
            "No."]
    elif Girl == StormX:
        $ lines = ["No, thank you.",
            "No, I do not think so. . .",
            "It is not appropriate.",
            "No."]
    elif Girl == JubesX:
        $ lines = ["Geeze, don't whine about it. . .",
            "No."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label action_already_rejected_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Learn to take \"no\" for an answer, " + Girl.player_petname + "_.",
            "I just don't want to, " + Girl.player_petname + "_.",
            "I'aint tellin you again.",
            "Look, I already told you no thanks, " + Girl.player_petname + "_.",
            "Read my lips, no.",
            "Learn to take \"no\" for an answer, " + Girl.player_petname + "_."]
    elif Girl == KittyX:
        $ lines = ["Look, I already told you no thanks, " + Girl.player_petname + "_.",
            "You can eat a dick, 'cos I'm not.",
            "I'm not telling you again.",
            "Learn to take \"no\" for an answer, " + Girl.player_petname + "_.",
            "{i}Listen{/i}!",
            "How many times do I have to say \"no\"?"
            "Not even, " + Girl.player_petname + "_.",
            "Maybe" + Girl.like + "_take \"no\" for an answer?",
            "I'm just not into that."]
    elif Girl == EmmaX:
        $ lines = ["Don't make me repeat myself.",
            "I've refused, end of story.",
            "Then I hope you can take care of yourself.",
            "I won't repeat myself.",
            "Learn to take \"no\" for an answer, " + Girl.player_petname + "_.",
            "You need to pay attention when I speak to you.",
            "I don't appreciate having to repeat myself, " + Girl.player_petname + "_.",
            "I really can't, " + Girl.player_petname + "_.",
            "Don't question me again.",
            "I've made myself clear."]
    elif Girl == LauraX:
        $ lines = ["Don't ask again.",
            "Look, I already told you no.",
            "I'm not telling you again.",
            "Suck this then.",
            "Learn to take \"no\" for an answer, " + Girl.player_petname + "_.",
            "Listen to the words that are coming out of my mouth.",
            "I don't like to repeat myself, " + Girl.player_petname + "_.",
            "I really can't, " + Girl.player_petname + "_.",
            "Don't push me.",
            "Don't push it.",
            "What did I tell you?"]
    elif Girl == JeanX:
        $ lines = ["Don't ask again.",
            "I already told you no.",
            "I'm not telling you again.",
            "You want me to make you suck yourself?",
            "Damn. . . forgot I can't do that. . .",
            "Learn to take \"no\" for an answer, " + Girl.player_petname + "_.",
            "I don't want to have to go through this again.",
            "I really can't, " + Girl.player_petname + "_.",
            "Don't push your luck, " + Girl.player_petname + "_.",
            "Know when to stop.",
            "What did I tell you?"]
    elif Girl == StormX:
        $ lines = ["Do not make me repeat myself.",
            "I have refused. Learn to accept that.",
            "Then I hope you can take care of yourself.",
            "I shall not repeat myself.",
            "You go too far!",
            "Learn to take \"no\" for an answer, " + Girl.player_petname + "_.",
            "I have been clear on this.",
            "Do not question me again.",
            "I believe I have made myself clear."]
    elif Girl == JubesX:
        $ lines = ["I'm pretty clear on this, NO.",
            "I really can't, " + Girl.player_petname + "_."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label otherwise_not_interested_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Nah, I don't think I'm interested.",
            "Heh, no, I'm not doing that.",
            "Not hap'nin.",
            "Not hap'nin, " + Girl.player_petname + "_.",
            "No luck, " + Girl.player_petname + "_.",
            "Tsk, not this time, " + Girl.player_petname + "_.",
            "Shoo, " + Girl.player_petname + "_.",
            "I. . . not there!!",
            "Ew!",
            "Um, no thanks, " + Girl.player_petname + "_.",
            "What?! Gross!",
            "I'd really rather not.",
            "That isn't really how I planned to use my feet today"
            "How about let's not, " + Girl.player_petname + "_.",
            "Not interested.",
            "No way.",
            "Not happening.",
            "I'd really rather not.",
            "Oh, um, no, I'm not really comfortable with that. . .",
            "Not right now, " + Girl.player_petname + "_. . .",
            "Maybe not right now, ok?",
            "I don't think we need any toys, " + Girl.player_petname + "_."]
    elif Girl == KittyX:
        $ lines = ["Um, no.",
            "Um, no thanks, " + Girl.player_petname + "_.",
            "Oh, um, no, I'm not really comfortable with that. . .",
            "Let's not, ok " + Girl.player_petname + "_?",
            "Not now, " + Girl.player_petname + "_.",
            "Not, right now " + Girl.player_petname + "_. . .",
            "Later, " + Girl.player_petname + "_!",
            "I don't think we need any toys, " + Girl.player_petname + "_.",
            "Not now, ok?",
            "Maybe" + Girl.like + "_not right now? . .",
            "Not. . . now. . .",
            "Um, no.",
            "No way.",
            "Nooope.",
            "No luck " + Girl.player_petname + "_.",
            "Ugh!",
            "Scram, " + Girl.player_petname + "_.",
            "That's. . . not cool.",
            "Ew.",
            "I don't wanna touch that.",
            "How about let's not, " + Girl.player_petname + "_.",
            "Nope.",
            "No way.",
            "I don't know about using my feet for. . . that.",
            "Nuhuh.",
            "Noooope.",
            "Noooop."]
    elif Girl == EmmaX:
        $ lines = ["You wish.",
            "Hmmm, no."
            "No. Thank you.",
            "I don't think so, " + Girl.player_petname + "_.",
            "I'm really not comfortable with that. . .",
            "Let's not, ok " + Girl.player_petname + "_?",
            "I'd rather not today. . .",
            "Not now, " + Girl.player_petname + "_.",
            "I'd rather not right now though.",
            "Perhaps later, " + Girl.player_petname + "_.",
            "We don't need any toys, do we, " + Girl.player_petname + "_?",
            "I don't think we need any toys, " + Girl.player_petname + "_.",
            "Not now, " + Girl.player_petname + "_. . .",
            "Perhaps another time would be better? . .",
            "I don't think that would be appropriate. . .",
            "No.",
            "No thank you, " + Girl.player_petname + "_.",
            "I know, I'm as disappointed as you are.",
            "Not today, " + Girl.player_petname + "_.",
            "I'm sorry, not now.",
            "No, I don't think so, " + Girl.player_petname + "_.",
            "How about let's not, " + Girl.player_petname + "_.",
            "I don't think I will.",
            "No way.",
            "No, thank you.",
            "I'm not in the mood for footplay today. . .",
            "I'm afraid not.",
            "I don't think you've earned that yet.",
            "No, thank you."]
    elif Girl == LauraX:
        $ lines = ["Keep dreaming.",
            "You wish.",
            "Nope.",
            "I'm really not cool with that. . .",
            "Let's not, ok " + Girl.player_petname + "_?",
            "I'd rather not today. . .",
            "Not now, " + Girl.player_petname + "_.",
            "Nah.",
            "Not right now " + Girl.player_petname + "_. . .",
            "I don't know, " + Girl.player_petname + "_!",
            "I don't think we need any toys, " + Girl.player_petname + "_.",
            "Not now, ok?",
            "Maybe later? . .",
            "I don't think that would be appropriate. . .",
            "No.",
            "No thank you, " + Girl.player_petname + "_.",
            "Yeah, sorry.",
            "Not today, " + Girl.player_petname + "_.",
            "I'm sorry, not now.",
            "I don't know where that's been lately.",
            "Nah.",
            "Nope.",
            "Um, no.",
            "No way.",
            "I'd rather not.",
            "Yeah, no.",
            "You haven't earned it yet.",
            "No thanks."]
    elif Girl == JeanX:
        $ lines = ["Yeah, you wish.",
            "You wish.",
            "You wish. . .",
            "Nope.",
            "I'd rather not.",
            "Let's not, ok " + Girl.player_petname + "_?",
            "I'd rather not today. . .",
            "Not now, " + Girl.player_petname + "_.",
            "Nope.",
            "Not right now " + Girl.player_petname + "_. . .",
            "I don't know, " + Girl.player_petname + "_. . .",
            "I don't think we need any toys, " + Girl.player_petname + "_.",
            "Not now, ok?",
            "I'm not in the mood right now . .",
            "I don't think that would be appropriate. . .",
            "No.",
            "Um, no.",
            "I'm sorry, not now.",
            "No thanks, " + Girl.player_petname + "_.",
            "Yeah, sorry.",
            "Not today, " + Girl.player_petname + "_.",
            "I'd really prefer not touching that.",
            "Nah.",
            "Ha! Good one.",
            "No way.",
            "I'd rather not.",
            "Not interested.",
            "You haven't earned it yet.",
            "No thanks."]
    elif Girl == StormX:
        $ lines = ["Hmm, no.",
            "I do not think so.",
            "No. Thank you.",
            "I would be uncomfortable with that. . .",
            "I would rather not. . .",
            "Not now, " + Girl.player_petname + "_.",
            "I would rather not right now though.",
            "Perhaps later, " + Girl.player_petname + "_. . .",
            "Perhaps later, " + Girl.player_petname + "_.",
            "I do not think so, " + Girl.player_petname + "_.",
            "We don't need any toys, do we, " + Girl.player_petname + "_?",
            "I don't think we need any toys, " + Girl.player_petname + "_.",
            "Not now, " + Girl.player_petname + "_. . .",
            "Perhaps another time? . .",
            "I do not believe that would be appropriate. . .",
            "No, I do not think so.",
            "No, I do not think so, " + Girl.player_petname + "_.",
            "I would rather not, " + Girl.player_petname + "_.",
            "I do not think that I will.",
            "No way.",
            "No, thank you.",
            "I am truly in no mood for footplay today. . .",
            "I must refuse.",
            "I do not think you have earned that yet.",
            "Thank you, but no."]
    elif Girl == JubesX:
        $ lines = ["Cute, but no.",
            "No thanks. . .",
            "You wish.",
            "Nope.",
            "I'm really not cool with that. . .",
            "Let's not, ok " + Girl.player_petname + "_?",
            "I'd rather not today. . .",
            "Not now, " + Girl.player_petname + "_.",
            "Nah.",
            "Um. . . no.",
            "No.",
            "No thank you, " + Girl.player_petname + "_.",
            "Yeah, sorry.",
            "Not today, " + Girl.player_petname + "_.",
            "I'm sorry, not now."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label previous_action_rejected_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Sorry, " + Girl.player_petname + " you aren't touching these again.",
            "Sorry, " + Girl.player_petname + " you aren't getting these in your mouth.",
            "Sorry, keep your tongue in your mouth.",
            "Sorry, hands off the booty.",
            "Fresh!",
            "Nope, not anymore, you'll have to go back to Internet porn.",
            "I think you should keep your fingers to yourself.",
            "Sorry, keep your hands out of there.",
            "I think you can manage it yourself this time. . .",
            "Not right now, " + Girl.player_petname + "_. . .",
            "I think I'll let you know when I want you touching these again.",
            "I think I've got the taste out of my mouth, thanks.",
            "Sorry, you can keep your toys to yourself.",
            "Sorry, you can keep your toys out of there.",
            "Maybe you could go fuck yourself instead.",
            "Eh-eh, not anymore, " + Girl.player_petname + "_.",
            "The only thing you can do with my ass is kiss it, " + Girl.player_petname + "_.{p}. . .Don't get any ideas."]
    elif Girl == KittyX:
        $ lines = ["You had your shot.",
            "Sorry, " + Girl.player_petname + "_, maybe later?",
            "Fresh!",
            "Sorry, keep your hands out of there.",
            "Keep your head out of there.",
            "Sorry, hands to yourself.",
            "Sorry, maybe try a porn game or something.",
            "I don't feel like it.",
            "Sorry, no more of that.",
            "I'm not feeling it today. . .",
            "I think I'll let you know when I want you touching these again.",
            "No, not this time.",
            "Sorry, you can keep your toys to yourself.",
            "Sorry, you can keep your toys out of there.",
            "I'm not feeling it today. . .",
            "Maybe just" + Girl.like + "_fuck yourself, huh?",
            "That's" + Girl.like + "_totally off the table.",
            "Yeah, not again."]
    elif Girl == EmmaX:
        $ lines = ["I'm afraid you haven't earned back my good graces.",
            "I am sorry about that, but perhaps later?",
            "Hands.",
            "Sorry, keep your hands out of there.",
            "Keep your head out of there.",
            "I'm sorry, keep your hands to yourself.",
            "I don't feel like it.",
            "I'm sure you can find something else to watch.",
            "Sorry, no more of that.",
            "I'd really rather not. . .",
            "I'm afraid you'll just have to remember the last time.",
            "I'm just not in the mood, " + Girl.player_petname + "_.",
            "Sorry, you can keep your toys to yourself.",
            "Sorry, you can keep your toys out of there.",
            "I'm not in the mood, " + Girl.player_petname + "_. . .",
            "I'm sure you can figure out how to take care of that yourself.",
            "You'll have to show me you're worth it again.",
            "Not under the circumstances."]
    elif Girl == LauraX:
        $ lines = ["You'll have to earn that back.",
            "Keep your hands to yourself.",
            "Sorry, fingers outside.",
            "Keep your head out of there.",
            "Sorry, keep your hands to yourself.",
            "I don't feel like it.",
            "Sorry, no more of that.",
            "I'm not into it today. . .",
            "I'm not into it right now.",
            "You'll know when it's time for that.",
            "Nah, not this time.",
            "Sorry, you can keep your toys to yourself.",
            "Sorry, you can keep your toys out of there.",
            "Not right now.",
            "Just jack it or something.",
            "You'll have to earn it.",
            "Not anymore."]
    elif Girl == JeanX:
        $ lines = ["We've had enough of that.",
            "Keep your hands to yourself.",
            "You can keep those to yourself.",
            "Keep your tongue to yourself.",
            "Sorry, keep your hands to yourself.",
            "Eh, I think I'm ok for now. . .",
            "I don't feel like it.",
            "I'm not into it today. . .",
            "You'll know when it's time for that.",
            "Nah, not this time.",
            "Sorry, you can keep your toys to yourself.",
            "Not right now.",
            "Maybe just fuck one of the others.",
            "You'll have to earn that one. . .",
            "Not anymore."]
    elif Girl == StormX:
        $ lines = ["No, I do not think so.",
            ". . . I would rather not.",
            "Our time together was a memory.",
            "I am just not in the mood, " + Girl.player_petname + "_.",
            "Sorry, you can keep your toys to yourself.",
            "Sorry, you can keep your toys out of there.",
            "I am in no mood, " + Girl.player_petname + "_. . .",
            "I am certain you can take care of that yourself.",
            "I expect that you can entertain yourself elsewhere.",
            "You shall have to display your worth to me again.",
            "Not under the circumstances."]
    elif Girl == JubesX:
        $ lines = ["You'll have to earn that.",
            "You'll have to earn that back.",
            "Keep your hands to yourself.",
            "Sorry, keep your fingers outside.",
            "I'm not into it right now.",
            "Keep your head out of there.",
            "Sorry, keep your hands to yourself.",
            "I'm not into it.",
            "Sorry, no more of that."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label forced_but_not_unwelcome_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Fine, if that's what you want.",
            "Hmmph, well I guess you can go to town. . .",
            "Hmmph.",
            "Fine, I suppose.",
            "Oh. . . well, ok then. . .",
            "Well, at least make it worth it.",
            "Ok, get in there if you're so determined.",
            "Ok, fine, whip it out.",
            "Ok, fine.",
            "Ok, fine. I'll give it a try.",
            "Ok, fine. If we're going to do this, stick it in already.",
            "Ok, fine. Whatever."]
    elif Girl == KittyX:
        $ lines = ["Rude! But. . . whatever.",
            "Ugh, I guess if you're so enthusiastic. . .",
            "Hmmph.",
            "Well. . . I guess. . .",
            "Ok, get in there if you're so determined.",
            "Fine, I suppose.",
            "Fiiine, geeze.",
            "Oh. . . well, ok then. . .",
            "Ok, {i}fine{/i}.",
            "Ok, fine. . .",
            "Ok, fine. If we're going to do this, stick it in already.",
            "Ok, fine.",
            "Ok, fine, whip it out.",
            "Well! . . ok, fine, stick it in.",
            "Ok, fine. Whatever."]
    elif Girl == EmmaX:
        $ lines = ["That is not appropriate. . .",
            "but neither is it entirely unwelcome. . .",
            "You'd better shower them with praise. . .",
            "Hmmph.",
            "Oh, if you insist. . .",
            "If you insist. . .",
            "Oh, if it will shut you up.",
            "Fine, I suppose.",
            "Oh, very well.",
            "Well hello there. . .",
            "Suit yourself.",
            "Hm. Alright, but don't push your luck, " + Girl.player_petname + "_.",
            "Oh, fine. . .",
            "Ok, fine. If we're going to do this, stick it in already.",
            "Oh, very well.",
            "Fine, if it'll shut you up.",
            "Oh, very well, get it over with.",
            "Alright, fine. Lay back."]
    elif Girl == LauraX:
        $ lines = ["Hey. . .",
            "Eh, whatever. . .",
            "Hmm. . . ok. . .",
            "Hmmph.",
            "Ok, fine. . .",
            "If you insist. . .",
            "Fine, I guess.",
            "Well hello there. . .",
            "Suit yourself.",
            "Ok, fine, whip it out.",
            "Ok, fine.",
            "Whatever. . .",
            "Whatever.",
            "Ok, fine. If we're going to do this, stick it in already.",
            "Fine.",
            "Fine, if it'll shut you up.",
            "Oh fine, get it over with.",
            "Alright, fine."]
    elif Girl == JeanX:
        $ lines = ["Hey. . .{p}. . .whatever. . .",
            "I guess you won't take \"no\" for an answer. . .",
            "Ooo! Well ok then. . .",
            ". . . Ok, whatever.",
            ". . .{p}Whatever. . .",
            "Ok, fine. If we're going to do this, stick it in already.",
            "Fine.",
            ". . .{p}. . . Ok. . .",
            ". . .{p}Ok, fine, whip it out.",
            "Oh. . . fine. . .",
            "Oh fine, get it over with.",
            ". . .{p}. . . fine."]
    elif Girl == StormX:
        $ lines = ["That is not appropriate. . .",
            "but neither is it entirely unwelcome. . .",
            "Only if you do a good job. . .",
            "Hmmph.",
            "Oh, if you insist. . .",
            "If you insist. . .",
            ". . . I suppose.",
            "That was unexpected. . .",
            "If you must. . .",
            ". . . fine.",
            ". . . fine. . .",
            "Fine, if you insist.",
            "Ok, fine. If we're going to do this, stick it in already.",
            "Oh, very well.",
            "Fine, if it will silence you.",
            "Oh, very well, if you must.",
            "Alright, fine then. Lie back."]
    elif Girl == JubesX:
        $ lines = ["Hey. . .{p}Well, whatever. . .",
            "Hmm. . . ok. . .",
            "Whatever.",
            "Hmmph.",
            "Ok, fine. . .",
            "Well I don't want to get in your way. . .",
            "Fine, I guess.",
            "Um, hello? . .",
            "Suit yourself."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label forced_but_welcome_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Sure, get in there.",
            "Fine, grab a cheek."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label said_no_recently_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I {i}just{/i} told you \"no,\" " + Girl.player_petname + "_.",
            "I {i}just{/i} told you \"no,\" " + Girl.player_petname + "_.",
            "What part of \"no,\" did you not get, " + Girl.player_petname + "_?"]
    elif Girl == KittyX:
        $ lines = ["" + Girl.Like + "_no way, " + Girl.player_petname + "_.",
            "I" + Girl.like + "_{i}just{/i} told you \"no\"!"
            "You don't" + Girl.like + "_listen do you, " + Girl.player_petname + "_.",
            "I {i}just{/i} told you \"no,\" " + Girl.player_petname + "_.",
            "What did I" + Girl.like + "_{i}just{/i} tell you " + Girl.player_petname + "_.",
            "You don't" + Girl.like + "_listen do you, " + Girl.player_petname + "_.",
            "I{i}just{/i}" + Girl.like + "_told you \"no\"!"]
    elif Girl == EmmaX:
        $ lines = ["Your persistence is doing you no favors, " + Girl.player_petname + "_.",
            "You need to learn to take\"no\" for an answer, " + Girl.player_petname + "_.",
            "I {i}just{/i} refused, " + Girl.player_petname + "_.",
            "I believe I just told you, \"no\"."
            "What part of \"no,\" did you not get, " + Girl.player_petname + "_?",
            "Pay attention, " + Girl.player_petname + "_.",
            "I'm afraid that \"no\" is my final answer, " + Girl.player_petname + "_."]
    elif Girl == LauraX:
        $ lines = ["Take a breath here, before you regret it.",
            "I just told you no, " + Girl.player_petname + "_.",
            "I {i}just{/i} told you \"no,\" " + Girl.player_petname + "_.",
            "Just told you I wouldn't, " + Girl.player_petname + "_.",
            "What part of \"no,\" did you not get, " + Girl.player_petname + "_?",
            "You should listen better, " + Girl.player_petname + "_.",
            "Sorry, " + Girl.player_petname + " \"no\"."]
    elif Girl == JeanX:
        $ lines = ["I'm not used to repeating myself.",
            "I just told you no, " + Girl.player_petname + "_.",
            "I {i}just{/i} told you \"no,\" " + Girl.player_petname + "_.",
            "Just told you I wouldn't, " + Girl.player_petname + "_.",
            "What part of \"no,\" did you not get, " + Girl.player_petname + "_?",
            "Don't make me repeat myself again, " + Girl.player_petname + "_.",
            "I don't repeat myself."]
    elif Girl == StormX:
        $ lines = ["Do not persist in this, " + Girl.player_petname + "_.",
            "Your persistance is doing you no favors, " + Girl.player_petname + "_.",
            "You will need to accept a \"no\", " + Girl.player_petname + "_.",
            "What part of \"no,\" did you not get, " + Girl.player_petname + "_?",
            "I have made myself clear, " + Girl.player_petname + "_.",
            "I am afraid that \"no\" is my final answer, " + Girl.player_petname + "_."]
    elif Girl == JubesX:
        $ lines = ["I already told you, \"no\".",
            "I just told you no, " + Girl.player_petname + "_."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label action_accepted_enthusiastically_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Ok " + Girl.player_petname + " come and get'em.",
            "Ok " + Girl.player_petname + " go ahead.",
            "Oooooooh. . .",
            "God yes.",
            "Sure, grab a cheek.",
            "Sure, get in there."]
    elif Girl == KittyX:
        $ lines = ["Ok " + Girl.player_petname + "_, come and get'em.",
            "Ok, fiiiine.",
            "Ok " + Girl.player_petname + "_, go ahead.",
            "Ok, whatever.",
            "Mmmmmm.",
            "Oooooooh. . .",
            "Ok, go for it.",
            "Mmmmm. . .",
            "Wha. . ."]
    elif Girl == EmmaX:
        $ lines = ["That sounds lovely, ravish me.",
            "Oh very well. . .",
            "Ok " + Girl.player_petname + "_, go ahead.",
            "Mmmm, I couldn't refuse. . .",
            "Mmmmmm. . .",
            "I can't exactly refuse. . .",
            "Mmm. . . naughty."]
    elif Girl == LauraX:
        $ lines = ["Sure, sounds fun.",
            "Sure.",
            "Ok " + Girl.player_petname + "_, go ahead.",
            "Mmmm, I couldn't refuse. . .",
            "Mmmmmm. . .",
            "Yeah, ok. . .",
            "Mmm. . . naughty."]
    elif Girl == JeanX:
        $ lines = ["Sure, sounds fun.",
            "Sure.",
            "Ok " + Girl.player_petname + "_, go ahead.",
            "Mmmm, I couldn't refuse. . .",
            "Mmmmmm. . .",
            "Yeah, ok. . .",
            "Mmm. . . naughty."]
    elif Girl == StormX:
        $ lines = ["I would love that. . .",
            "Oh very well. . .",
            "Ok " + Girl.player_petname + "_, go ahead.",
            "Mmmm, I could not refuse. . .",
            "Mmmmmm. . .",
            "I suppose that is reasonable. . .",
            "Mmm. . . naughty."]
    elif Girl == JubesX:
        $ lines = ["Sure, sounds fun.",
            "Sure.",
            "Ok " + Girl.player_petname + "_, go ahead.",
            "Mmmm, I couldn't refuse. . .",
            "Mmmmmm. . .",
            "Yeah, ok. . .",
            "Mmm. . . naughty."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label daily_action_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Didn't get enough earlier?",
            "Again? Oh, you're insatiable!",
            "Must be my lucky day!",
            "Mmm. . .",
            "Back again so soon?",
            "Another one?",
            "So you'd like another go?",
            "You can't stay away from this. . ."]

        if Action_type in hand_Action_types or Action_type in mouth_Action_types or Action_type == "hotdog":
            $ lines.append("Are you sure that's all you want?")

            if Action_type == "kiss":
                $ lines.append("Gimme some sugar, sugar.")
                $ lines.append("Let me get some saliva going.")
            elif Action_type in hand_Action_types:
                $ lines.append("You do have a smooth touch. . .")
        elif Action_type in ["sex", "anal"]:
            $ lines.append("Maybe not so hard this time though.")
            $ lines.append("Maybe not so rough this time though.")
            $ lines.append("I'm still a bit sore from earlier.")

            if Action_type == "anal":
                $ lines.append("You can't stay away from this booty. . .")
        elif Action_type in fondle_Action_types or Action_type in dildo_Action_types or Action_type in ["sex", "anal"]:
            $ lines.append("You sure know how to keep a girl satisfied. . .")
            $ lines.append("I'm still tingling a bit from earlier.")
            $ lines.append("Take it a bit gently, I'm still quivering from earlier.")
            $ lines.append("You're going to wear me out.")

            if Action_type in dildo_Action_types:
                $ lines.append("Breaking out the toys again?")
        elif Action_type == "masturbation":
            $ lines.append("You enjoyed the show?")
            $ lines.append("It is nice to have an audience. . .")
        elif Action_type == "blowjob":
            $ lines.append("{i}I'm{/i} used to being the one sucking people dry. . .")
            $ lines.append("My jaw's still a bit sore from earlier.")
            $ lines.append("You're going to give me lockjaw.")
        elif Action_type == "titjob":
            $ lines.append("My tits are still a bit sore from earlier.")
        elif Action_type == "handjob":
            $ lines.append("My arm's still a bit sore from earlier.")
            $ lines.append("You're going to give me calluses.")
        elif Action_type == "footjob":
            $ lines.append("My feet are kinda sore from earlier.")
            $ lines.append("My feet are a bit sore from earlier.")
    elif Girl == KittyX:
        $ lines = ["Didn't get enough earlier?",
            "Meow.",
            "Another one?",
            "Huh? Again?",
            "I must have done something right.",
            "Mmm. . .",
            "Was it that good?",
            "You're really digging this. . .",
            "Back again so soon?",
            "So you'd like another round?",
            "You can't stay away from this. . ."]

        if Action_type in hand_Action_types or Action_type in mouth_Action_types or Action_type == "hotdog":
            $ lines.append("Are you sure that's all you want?")

            if Action_type == "kiss":
                $ lines.append("Let me get some saliva going.")
                $ lines.append("Come'ere tasty.")
        elif Action_type in ["sex", "anal"]:
            $ lines.append("Maybe not so rough this time though.")
            $ lines.append("You're going to make me sore.")
            $ lines.append("I'm still a bit sore from earlier.")
            $ lines.append("I'm still a little sore from earlier.")
        elif Action_type in fondle_Action_types or Action_type in dildo_Action_types or Action_type in ["sex", "anal"]:
            $ lines.append("You're going to wear me out.")
            $ lines.append("You're wearing me out here!")
            $ lines.append("Take it a bit gently, I'm still shaking from earlier.")
            $ lines.append("Take it easy though.")

            if Action_type in dildo_Action_types:
                $ lines.append("Breaking out the toys again?")
            elif Action_type "eat_pussy":
                $ lines.append("What a girl wants. . .")
        elif Action_type == "masturbation":
            $ lines.append("I kinda liked the audience. . .")
        elif Action_type == "blowjob":
            $ lines.append("My jaw's still a bit sore from earlier.")
            $ lines.append("You're going to give me lockhee- . . . jaw.")
        elif Action_type == "titjob":
            $ lines.append("My tits are still kinda sore from earlier.")
        elif Action_type == "handjob":
            $ lines.append("You're going to give me calluses")
            $ lines.append("My hand's kinda sore from earlier.")
        elif Action_type == "footjob":
            $ lines.append("My feet are kinda sore from earlier.")
    elif Girl == EmmaX:
        $ lines = ["You didn't get enough earlier?",
            "Back again so soon?",
            "So you'd like another round?",
            "You're really into this. . .",
            "Didn't get enough earlier?",
            "Back again?",
            "You'd like another round?",
            "I suppose I am irresistible. . .",
            "Back so soon?",
            "Huh? Again?",
            "Mmmm. . .",
            "Mmm. . .",
            "Come and get it.",
            "Another?",
            "I was that good?",
            "I must have done something right."]

        if Action_type in hand_Action_types or Action_type in mouth_Action_types or Action_type == "hotdog":
            $ lines.append("Are you sure that's all you want?")

            if Action_type == "kiss":
                $ lines.append("Let me get some saliva going.")
            elif Action_type in hand_Action_types:
                $ lines.append("Relax, gently. . .")
        elif Action_type in ["sex", "anal"]:
            $ lines.append("Perhaps not so rough this time?")
            $ lines.append("I'm still a bit sore from earlier.")
            $ lines.append("I'm still a little sore from earlier.")
        elif Action_type in fondle_Action_types or Action_type in dildo_Action_types or Action_type in ["sex", "anal"]:
            $ lines.append("You're wearing me out, " + Girl.player_petname + "_.")
            $ lines.append("You're going to wear me out.")
            $ lines.append("Take it a bit gently, I'm still shaking from earlier.")

            if Action_type in dildo_Action_types:
                $ lines.append("Breaking out the toys again?")
            elif Action_type "eat_pussy":
                $ lines.append("What a queen deserves. . .")
        elif Action_type == "masturbation":
            $ lines.append("I did enjoy the audience participation. . .")
        elif Action_type == "blowjob":
            $ lines.append("My jaw's still a bit sore from earlier.")
            $ lines.append("My jaw's still sore from our prior engagement.")
        elif Action_type == "titjob":
            $ lines.append("You're going to wear them out.")
        elif Action_type == "handjob":
            $ lines.append("I'd rather not get calluses.")
            $ lines.append("You're going to wear out my arm.")
            $ lines.append("My hand's a bit sore from earlier.")
            $ lines.append("My hand's rather sore from before.")
        elif Action_type == "footjob":
            $ lines.append("My feet are rather sore from earlier.")
    elif Girl == LauraX:
        $ lines = ["You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right."
            "I do like this treatment. . .",
            "Mmm, you like that? . .",
            "Mmm. . .",
            "Another one?",
            "Mmmmmm.",
            "Get over here.",
            "Did you enjoy that?",
            "Didn't get enough earlier?",
            "I guess you want more.",
            "Back for more?",
            "I must be too good at this."
            "Again? Sure.",
            "You're really into this. . .",
            "Back again so soon?",
            "So you'd like another round?",
            "Back again?",
            "You'd like another round?",
            "I must be better than I thought."]

        if Action_type in hand_Action_types or Action_type in mouth_Action_types or Action_type == "hotdog":
            $ lines.append("Are you sure that's all you want?")

            if Action_type == "kiss":
                $ lines.append("Let me get some saliva going.")
            elif Action_type in hand_Action_types:
                $ lines.append("Chill. . .")
        elif Action_type in ["sex", "anal"]:
            $ lines.append("I'm still a bit sore from earlier.")
        elif Action_type in fondle_Action_types or Action_type in dildo_Action_types or Action_type in ["sex", "anal"]:
            $ lines.append("Take it slow, I'm still shaking from earlier.")
            $ lines.append("Wear'in me out here.")
            $ lines.append("You're going to wear me out.")

            if Action_type in dildo_Action_types:
                $ lines.append("Breaking out the toys again?")
        elif Action_type == "masturbation":
            $ lines.append("I liked having an audience. . .")
        elif Action_type == "titjob":
            $ lines.append("You're really working these puppies.")
        elif Action_type == "handjob":
            $ lines.append("I'm glad I don't grow calluses.")
            $ lines.append("Again with the handjobs, huh?")
    elif Girl == JeanX:
        $ lines = ["You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "I do like this. . .",
            "Mmm, you like that? . .",
            "Mmm. . .",
            "MmMmmm. . .",
            "Oh, get over here.",
            "Did you enjoy that?",
            "Another one?",
            "Didn't get enough earlier?",
            "I guess you want more.",
            "Back for more?",
            "I must be too good at this.",
            "Back again?",
            "You'd like another round?",
            "I must be better than I thought.",
            "Back again so soon?",
            "So you'd like another round?",
            "Again? Sure.",
            "You're really into this. . ."]

        if Action_type in hand_Action_types or Action_type in mouth_Action_types or Action_type == "hotdog":
            $ lines.append("Are you sure that's all you want?")

            if Action_type in hand_Action_types:
                $ lines.append("Chill. . .")
        elif Action_type in fondle_Action_types or Action_type in dildo_Action_types or Action_type in ["sex", "anal"]:
            $ lines.append("Take it slow, I'm still shaking from earlier.")
            $ lines.append("You're wearing me out here.")
            $ lines.append("You're going to wear me out.")

            if Action_type in dildo_Action_types:
                $ lines.append("Breaking out the toys again?")
        elif Action_type == "masturbation":
            $ lines.append("I do like having an audience. . .")
        elif Action_type == "titjob":
            $ lines.append("You're really working these babies.")
        elif Action_type == "handjob":
            $ lines.append("Again the with handjobs, huh?")
    elif Girl == StormX:
        $ lines = ["You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "Mmm. . .",
            "You did not get enough earlier?",
            "Back so soon?",
            "Mmmm. . .",
            "Yes, let's.",
            "I must prepare myself.",
            "You did not get enough earlier?",
            "Another?",
            "Back again?",
            "You would like another round?",
            "I suppose that I can be irresistible. . .",
            "Did you not get enough earlier?",
            "Back again so soon?",
            "So you would like another round?",
            "You really are into this. . ."]

        if Action_type in hand_Action_types or Action_type in mouth_Action_types or Action_type == "hotdog":
            $ lines.append("Are you sure that is all you would want?")

            if Action_type in hand_Action_types:
                $ lines.append("Relax, gently. . .")
                $ lines.append("Gently. . . gently. . .")
        elif Action_type in ["sex", "anal"]:
            $ lines.append("Perhaps not so rough this time?")
            $ lines.append("I am still a bit sore from earlier.")
            $ lines.append("I am still rather sore from earlier.")
        elif Action_type in fondle_Action_types or Action_type in dildo_Action_types or Action_type in ["sex", "anal"]:
            $ lines.append("Take it a bit gently, I am still glowing from earlier.")
            $ lines.append("You're going to wear me out.")
            $ lines.append("You are wearing me out, " + Girl.player_petname + "_.")
            $ lines.append("You are tiring me, " + Girl.player_petname + "_.")

            if Action_type in dildo_Action_types:
                $ lines.append("Breaking out the toys again?")
            elif Action_type "eat_pussy":
                $ lines.append("What a queen deserves. . .")
                $ lines.append("I did enjoy the audience participation. . .")
        elif Action_type == "masturbation":
            $ lines.append("I put on quite the show?")
        elif Action_type == "blowjob":
            $ lines.append("My jaw is still rather sore.")
            $ lines.append("My jaw is still recovering.")
        elif Action_type == "titjob":
            $ lines.append("You will wear them out like this.")
        elif Action_type == "handjob":
            $ lines.append("My arm will wear out.")
            $ lines.append("My hand is quite sore from earlier.")
            $ lines.append("My hand is rather sore from before.")
        elif Action_type == "footjob":
            $ lines.append("My feet are rather sore from earlier.")
    elif Girl == JubesX:
        $ lines = ["You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "I guess fair's fair. . .",
            "Mmmm. . .",
            "Sure, come to me.",
            "Mmm, you like that? . .",
            "Did you enjoy that?",
            "Mmm. . .",
            "Another one?",
            "I guess you want more."]

        if Action_type in hand_Action_types:
                $ lines.append("Relax. . .")
                $ lines.append("Take it slow, I'm still shaking from earlier.")
        elif Action_type == "masturbation":
            $ lines.append("I enjoyed having an audience. . .")
        elif Action_type == "handjob":
            $ lines.append("I'm glad I don't grow calluses.")
            $ lines.append("Again with the handjobs, huh?")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label taboo_and_said_no_today_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I told you not to touch me like that in public!",
            "I told you that wasn't appropriate!",
            "You already got your answer!",
            "I told you we can't do that in public!",
            "I already told you that I wouldn't jerk you off in public!",
            "This is just way too exposed!",
            "I already told you that I wouldn't suck you off in public!",
            "Not in public!",
            "Stop swinging that thing around in public!",
            "I already told you that I wouldn't bang you in public!",
            "I already told you that I wouldn't do that out here!",
            "I told you that I didn't want you rubb'in up on me in public!"]
    elif Girl == KittyX:
        $ lines = ["I told you not here!",
            "I told you this was" + Girl.like + "_too public!",
            "I told you not to touch me like that in public!",
            "You already got your answer!",
            "I told you that wasn't appropriate!",
            "I said not in public!",
            "This is just way too exposed!",
            "I told you, not in public!",
            "Stop swinging that thing around in public!",
            "I already told you. . . not in public!",
            "I{i}just{/i}" + Girl.like + "_told, not in public!"]
    elif Girl == EmmaX:
        $ lines = ["You've been warned.",
            "I told you I couldn't be seen like that.",
            "I told you not to touch me like that in public!",
            "I told you that wasn't appropriate!",
            "I told you, this is too public!",
            "This is not an appropriate location for that. !",
            "I told you, this is too public!",
            "Stop showing that thing around in public!",
            "Stop swinging that thing around in public!",
            "I refuse to do this in public.",
            "I already told you this is too public!",
            "I just told you. . . not in such an exposed location."]
    elif Girl == LauraX:
        $ lines = ["I've had enough of this today.",
            "I told you, I couldn't be caught like that.",
            "I told you not to touch me like that in public!",
            "I told you that wasn't appropriate!",
            "I said not in public.",
            "This is just way too exposed!",
            "Like I told you, not in public.",
            "Stop swinging that thing around in public!",
            "I said not in public.",
            "I told you. . . this place is too exposed.",
            "I just told you. . . not in such an exposed location."]
    elif Girl == JeanX:
        $ lines = ["I've had enough of this today.",
            "I told you, I'm not comfortable in public.",
            "I told you not to touch me like that in public!",
            "You already got your answer!",
            "I told you that wasn't appropriate!",
            "I told you I wasn't comfortable in public. . .",
            "I don't want to show off the goods like that!",
            "Like I said, not in public.",
            "Stop swinging that thing around in public!",
            "I'm not comfortable with that. . .",
            "I just told you. . . not in such an exposed location."]
    elif Girl == StormX:
        $ lines = ["This area is too public, " + Girl.player_petname + "_.",
            "I told you not to touch me like that in public!",
            "You already got your answer!",
            "This is not an appropriate location for that. !",
            "I told you, this is too public!",
            "Stop showing that thing around in public!",
            "Stop swinging that thing around in public!",
            "I refuse to do this in public.",
            "I have already informed you. . . not in such an exposed location.",
            "I just informed you. . . not in such an exposed location."]
    elif Girl == JubesX:
        $ lines = ["I've had enough of this today.",
            "I told you, I couldn't be caught like that.",
            "You already got your answer!",
            "I told you that wasn't appropriate!",
            "I said not in public."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label said_no_today_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I already told you \"no,\" " + Girl.player_petname + "_.",
            "I already told you no, take a hint.",
            "What part of \"no\" don't you understand?",
            "I already told you \"no,\" " + Girl.player_petname + "_.",
            "I told you \"no\" earlier " + Girl.player_petname + "_."]
    elif Girl == KittyX:
        $ lines = ["I" + Girl.like + "_already told you \"no\"."
            "" + Girl.Like + "_take a lesson, " + Girl.player_petname + "_.",
            "I told you \"no,\" " + Girl.player_petname + "_.",
            "I already told you \"no,\" " + Girl.player_petname + "_.",
            "I already" + Girl.like + "_told you \"no\"."
            "I{i}just{/i}" + Girl.like + "_told you \"no\" earlier!"]
    elif Girl == EmmaX:
        $ lines = ["I believe you know my answer on this matter.",
            "I told you \"no,\" " + Girl.player_petname + "_.",
            "I already refused, " + Girl.player_petname + "_.",
            "I already told you \"no,\" " + Girl.player_petname + "_.",
            "I said \"no,\" " + Girl.player_petname + "_.",
            "I believe I just told you \"no,\" " + Girl.player_petname + "_."]
    elif Girl == LauraX:
        $ lines = ["Don't make me tell you again today.",
            "I told you \"no,\" " + Girl.player_petname + "_.",
            "I already told you \"no,\" " + Girl.player_petname + "_.",
            "Told you \"no,\" " + Girl.player_petname + "_.",
            "I already told you \"no,\" " + Girl.player_petname + "_.",
            "I just told you \"no\"."
            "I'm believe I just told you \"no,\" " + Girl.player_petname + "_."]
    elif Girl == JeanX:
        $ lines = ["Don't ask me again today.",
            "I already told you \"no,\" " + Girl.player_petname + "_.",
            "Told you \"no,\" " + Girl.player_petname + "_.",
            "I already told you \"no,\" " + Girl.player_petname + "_.",
            "I told you \"no,\" " + Girl.player_petname + "_.",
            "Not today.",
            "I believe I just told you \"no,\" " + Girl.player_petname + "_."]
    elif Girl == StormX:
        $ lines = ["I have already told you my answer.",
            "I believe you know my answer on this matter.",
            "You will need to accept a \"no\", " + Girl.player_petname + "_.",
            "I already refused, " + Girl.player_petname + "_.",
            "I told you \"no,\" " + Girl.player_petname + "_.",
            "I already told you \"no,\" " + Girl.player_petname + "_.",
            "I said \"no,\" " + Girl.player_petname + "_.",
            "I believe that I just told you \"no,\" " + Girl.player_petname + "_."]
    elif Girl == JubesX:
        $ lines = ["Don't make me tell you again today.",
            "I told you \"no,\" " + Girl.player_petname + "_."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label forced_action_rejected_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I don't want you touching me.",
            "I don't want your lips on me.",
            "Um, no way.",
            "Not even, " + Girl.player_petname + "_.",
            "Not even that much.",
            "Stay out of my pants, " + Girl.player_petname + "_.",
            "Hands off the booty!",
            "Ew, no way.",
            "I'm not doing something so. . . intimate with you watching.",
            "I'm not that kind of girl!",
            "Not even with my feet.",
            "That isn't something I'd want!",
            "I'm not going to let you use that on me.",
            "I'm not doing that just because you have me over a barrel.",
            "That's a bit much, even for you.",
            "Even that's not worth it."]
    elif Girl == KittyX:
        $ lines = ["Not even.",
            "" + Girl.Like + "_get your mouth away from me.",
            "Keep away from my kitty, " + Girl.player_petname + "_.",
            "Back off!",
            "Um, no way.",
            "Ew, no way.",
            "Not even if you had a ten foot pole.{p}I mean. . .{p}}You know what I mean!",
            "No, that's just weird.",
            "I just can't do that!",
            "I'm not going to let you use that on me.",
            "I don't even want to step on it.",
            "I. . . can't, not with you watching.",
            "Not even.",
            "That's a bit much, even for you.",
            "Yeah, not happening."]
    elif Girl == EmmaX:
        $ lines = ["Don't push your luck.",
            "Not worth it.",
            "I don't think so, " + Girl.player_petname + "_.",
            "Do you want to keep those fingers?",
            "I'm not going that far today.",
            "I don't think so.",
            "Even that is asking too much.",
            "I couldn't put you through that.",
            "That's something I won't do.",
            "You go too far!",
            "I'm not going to let you use that on me.",
            "You really don't want my heels near your manhood.",
            "Don't overestimate your leverage here.",
            "You're really shooting for the fences on that one.",
            "I just don't see the benefit."]
    elif Girl == LauraX:
        $ lines = ["No.",
            "Not worth it.",
            "I don't think so, " + Girl.player_petname + "_.",
            "Do you want to keep those fingers?",
            "I'm not going there today.",
            "I don't think so.",
            "No.",
            "No, try something else.",
            "This is just too weird for me.",
            "That's just pushing it.",
            "I'm not going to let you use that on me.",
            "You understand that I have claws down there too. . .",
            "I'm over taking orders.",
            "You're going too far.",
            "There's no point trying."]
    elif Girl == JeanX:
        $ lines = ["No.",
            ". . . no, not worth it.",
            "I don't think so, " + Girl.player_petname + "_.",
            "Mmmm, no.",
            "I'm not going there today.",
            "I don't think so.",
            "No.",
            "No, try something else.",
            "I'm not doing that.",
            "I'm not going to let you use that on me.",
            "Don't push it. . .",
            "Nope, too kinky.",
            "I'm the queen here!",
            "You're overestimating your power here.",
            "There's no point trying."]
    elif Girl == StormX:
        $ lines = ["You go too far.",
            "I am not comfortable with that.",
            "I do not wish to do this.",
            "I'm not going to let you use that on me.",
            "Do not tempt me to show you what my feet can do.",
            "Do not overestimate your power here.",
            "I will not do that.",
            "You certainly are not wasting your shot.",
            "I just do not understand the benefit."]
    elif Girl == JubesX:
        $ lines = ["No.",
            "Suck yourself.",
            "I don't think so, " + Girl.player_petname + "_.",
            "Do you want to keep those fingers?",
            "I'm not going there today.",
            "This isn't something I'm into.",
            "I don't think so."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label try_something_else_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I know you're having fun, but maybe we could try something else " + Girl.player_petname + "_.",
            "" + Girl.player_petname + " this is getting uncomfortable, maybe we could try something else.",
            "" + Girl.player_petname + " this is nice, but could we do something else?",
            "" + Girl.player_petname + " I know you're having fun down there, but maybe we could try something else."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label this_is_boring_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Well if that's your attitude, I don't need your \"help\"."]
    elif Girl == KittyX:
        $ lines = ["Fun for you maybe, I'm tired of it.",
            "Not with that attitude, mister!",
            "Hey, I've got better things to do if you're" + Girl.like + "_going to be a dick about it.",
            "Well fuck you then.",
            "Well if that's your attitude, I don't need your \"help\"."]
    elif Girl == LauraX:
        $ lines = ["Well, I've got better things to be doing.",
            "I'm kinda bored here.",
            "Not with that attitude.",
            "I have better things to do with my time.",
            "Well fuck you then.",
            "Well if that's your attitude, I don't need your \"help\".",
            "Not interested."]
    elif Girl == EmmaX:
        $ lines = ["You may be enjoying yourself, but I'm getting a bit sore.",
            "Well perhaps you are enjoying yourself, but I'm tired of this.",
            "No, I think not.",
            "You know, I do have better things to do with my time than this.",
            "Then I suppose you can handle this yourself.",
            "Well then.",
            "Well if that's your attitude, I don't need your \"help\".",
            "I do have better things I could be doing."]
    elif Girl == JeanX:
        $ lines = ["Well, I've got better things to be doing.",
            "Well -I'm- bored.",
            "Don't overestimate yourself.",
            "Don't overestimate yourself.",
            "I have better things to do with my time.",
            "Well fuck you then.",
            "Ok, have fun with that then.",
            "Not interested."]
    elif Girl == StormX:
        $ lines = ["Well however much you are enjoying yourself, I need to take a break.",
            "No, I think not.",
            "Perhaps some time alone would help you better evaluate your choices.",
            "Then I suppose you can handle this yourself.",
            "Well then.",
            "Well if that's your attitude, I don't need your \"help\".",
            "I do have better things I could be doing."]
    elif Girl == JubesX:
        $ lines = ["This is kinda boring. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label satisfied_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["That was. . . nice.",
            "That was . . . real pleasant, " + Girl.player_petname + "_.",
            "I . . . really liked that, " + Girl.player_petname + "_.",
            "Certainly different with someone else at the wheel.",
            "I. . . how'd I taste?",
            "That felt. . . interesting. . .",
            "Was. . . that something you liked?",
            "Well, it's really nice to finally be able to reach out and touch someone.",
            "That was a real interesting experience. . .",
            "Well, that was certainly interesting.",
            "That really wasn't half bad.",
            "Well I liked that. . .",
            "Well that was a bit rough. . .",
            "That was . . . interesting " + Girl.player_petname + "_. We'll have to do that again sometime.",
            "That was pretty hot, " + Girl.player_petname + "_, we'll have to do that again sometime.",
            "That was really great, " + Girl.player_petname + "_, we'll have to do that again sometime."]
    elif Girl == KittyX:
        $ lines = ["I hope there was" + Girl.like + "_enough to work with.",
            "I hope they were enough for you. . .",
            "I liked that.",
            "Your hand is. . . bigger than mine.",
            "Was it. . . good?",
            "Huh. . . um. . .",
            "That was odd. . .",
            "That was. . . good for you?",
            "It was so warm to the touch. . .",
            "That was kinda fun.",
            "Huh, that wasn't bad.",
            "Thanks for the extra hand. . .",
            "I could feel you down there. . .",
            "I feel like I've been waiting" + Girl.like + "_a million years for that.",
            "Anal. . . huh, who knew?",
            "Well, did that work for you?",
            "That was. . . interesting. . .",
            "Ouch. . ."]
    elif Girl == EmmaX:
        $ lines = ["I'm sure it exceeded your expectations. . .",
            "Delectable, weren't they.",
            "That was. . . pleasant.",
            "I do appreciate some rather. . . aggressive attention down there.",
            "I could really take advantage of your services more often. . .",
            "That was. . . nice. . .",
            "You certainly surprise me. . .",
            "That was. . . invigorating.",
            "What a lovely experience. . .",
            "Mmm, was that as good for you as it was for me?",
            "Hmm, better than I'd imagined. . .",
            "I appreciate the work you put in. . .",
            "Your cock was so warm . .",
            "I assume I rocked your entire world.",
            "You really took to that well.",
            "Was that enough for you?",
            "That was. . . engaging. . ."]
    elif Girl == LauraX:
        $ lines = ["Did you enjoy that?",
            "That was kinda nice.",
            "That was. . . interesting.",
            "You're really getting into the good stuff.",
            "That was a really good use of that tongue of yours.",
            "That was. . . nice. . .",
            "That was kinda wild. . .",
            "That was. . . interesting.",
            "That was kind of. . . pleasant. . .",
            "That was fun.",
            "Hey, whaddaya know, that wasn't bad.",
            "Thanks for the extra hand. . .",
            "Did you like that? . .",
            "I can tell, I was the best you've had.",
            "You seem to know your way around back there.",
            "Enough for you?",
            "That was. . . interesting. . .",
            "Ouch. . ."]
    elif Girl == JeanX:
        $ lines = ["I bet you enjoyed that.",
            "Well that was fun.",
            "Well that was. . . something.",
            "Well, that was a nice surprise. . .",
            "You really put that tongue to work. . .",
            "That was. . . nice. . .",
            "That was. . . interesting.",
            "That was kinda fun. . .",
            "OK, that was fun.",
            "Mmm, yeah, that was as good as I expected. . .",
            "Thanks for the extra hand. . .",
            "Did you enjoy that? . .",
            "Blew your mind, uh?",
            "Hmmm, that was nice. . .",
            "I guess that could have gone worse. . .",
            "That was. . . interesting. . .",
            "Ouch. . ."]
    elif Girl == StormX:
        $ lines = ["That was quite fun. . .",
            "That was certainly enjoyable.",
            "Thank you for that.",
            "You certainly. . . reached some interesting places there. . .",
            "You really do have a talent for that. . .",
            "That was. . . nice. . .",
            "That one caught me by surprise. . .",
            "That was. . . certainly interesting. . .",
            "That was more enjoyable than I had expected. . .",
            "Mmm, I did quite enjoy that!",
            "Hmm, that certainly was enjoyable . .",
            "I appreciate the work you put in. . .",
            "That certainly was an interesting experience. . .",
            "I hope that was as enjoyable for you as it was for me.",
            "Was that satisfactory?",
            "That was. . . engaging. . ."]
    elif Girl == JubesX:
        $ lines = ["Did you like that?",
            "That was kinda nice.",
            "That was. . . interesting.",
            "Wow. . . that was nice. . .",
            "You really give me a run for my money. . .",
            "That was. . . nice. . .",
            "That was kinda weird. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label was_that_enough_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Was that enough for you?",
            "Did you get your jollies?",
            "Did you like the taste?",
            "Well, I hope that got your rocks off.",
            "Did that work for you?",
            "Well, I hope that was enough for you.",
            "Ouch.",
            "Did you get what you needed here?",
            "Did you like that?"]
    elif Girl == KittyX:
        $ lines = ["Not a disappointment, right?",
            "Did that satisfy you?",
            "Was that enough?",
            "Did you get what you needed?",
            "Well, did you like the taste?",
            "Did you like that?",
            "Well? Satisfied?",
            "Did that work for you?",
            "Did that work out for you?",
            "Well I hope you got something out of that.",
            "I hope you enjoyed that.",
            "Did that work out for you?",
            "I hope that was worth the wait.",
            "Ouch.",
            "I guess you got what you needed?",
            "Did you like that?"]
    elif Girl == EmmaX:
        $ lines = ["Well you certainly hit the jackpot.",
            "Did you get enough?",
            "Was that enough?",
            "Did you find what you were looking for?",
            "I suppose that worked out for both of us. . .",
            "Did you enjoy that?",
            "Was it everything you dreamed?",
            "Was it all you dreamed of?",
            "Was that sufficient?",
            "I hope that lived up to expectations.",
            "Was it all you dreamed of?",
            "Did you enjoy that?",
            "I hope you enjoyed that.",
            "Oooh.",
            "It's been a while."]
    elif Girl == LauraX:
        $ lines = ["That worked out for you?",
            "Did you get enough?",
            "Was that enough?",
            "Did you find what you were looking for?",
            "I suppose we both got something out of that. . .",
            "Was that good for you?",
            "Did that do it for you?",
            "Well I hope you got something out of that.",
            "I hope you enjoyed that.",
            "Did you like that?",
            "Satisfied?",
            "That was pleasant.",
            "Did you like that?"]
    elif Girl == JeanX:
        $ lines = ["You get what you wanted out of that?",
            "Did you get enough?",
            "Was that enough?",
            "Did you find what you were looking for?",
            "I guess that wasn't so bad. . .",
            "I bet you enjoyed that.",
            "Was that good for you?",
            "Pretty nice, right?",
            "I hope that worked out for you. . .",
            "Well, got what you wanted from that?",
            "Did that do it for you?",
            "That was great. . .",
            "Did you like that?"]
    elif Girl == StormX:
        $ lines = ["I expect you enjoyed that. . .",
            "Did you get enough?",
            "Ok, was that good?",
            "That was not so bad. . .",
            "Did you enjoy that?",
            "Did that work for you?",
            "Did that satisfy you?",
            "I hope that met your standards.",
            "Did that meet your expectations?",
            "I hope you found that satisfactory.",
            "Well. . .",
            "That was quite an experience. . ."]
    elif Girl == JubesX:
        $ lines = ["That worked out for you?",
            "Did you get enough?",
            "Was that enough?",
            "Did you find anything in there?",
            "Well, that wasn't so bad. . .",
            "Did you like that?",
            "Was that good for you?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label get_out_lines(Girl):
    if Girl == RogueX:
        $ lines = ["I don't want to deal with you right now.",
            "Buzz off already.",
            "I really think you should leave."]
    elif Girl == KittyX:
        $ lines = ["Nooope.",
            "GTFO.",
            "Go. Now."]
    elif Girl == EmmaX:
        $ lines = ["I haven't any time for this.",
            "Out.",
            "I think you should leave now."]
    elif Girl == LauraX:
        $ lines = ["Nope.",
            "Fuck off.",
            "Get out before we both regret it."]
    elif Girl == JeanX:
        $ lines = ["Out!"]
    elif Girl == StormX:
        $ lines = ["Get out.",
            "Out. Now."]
    elif Girl == JubesX:
        $ lines = ["Out!"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    if Girl in [RogueX, KittyX, EmmaX, LauraX, JeanX, JubesX]:
        $ lines = ["" + Girl.name + " pushes you back into the hall and slams the door. You head back to your room.",
            "" + Girl.name + " shoves you back into the hall and slams the door. You head back to your room."]
    elif Girl == StormX:
        $ lines = ["" + Girl.name + " pushes you to the top of the stairs and slams the door. You head back to your room."]
    "[line]"

    return

label first_time_pussy_eaten_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["That's pretty intimate, " + Girl.player_petname + "_. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label first_time_ass_eaten_lines(Girl, Action_type):
    if Girl == RogueX:
        if Girl.love >= Girl.obedience and Girl.love >= Girl.inhibition:
            Girl.voice "I'm not really sure I want you lick'in down there. . ."
        elif Girl.obedience >= Girl.inhibition:
            Girl.voice "You really don't have to if you don't want to."
        else:
            $ Girl.eyes = "sexy"

            Girl.voice "Hmm. . . it's worth a shot. . ."

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

    return

label trying_to_convince_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Ok, you're probably right. . .",
            "Well, ok, put it here.",
            "Well. . . ok.",
            "I guess.",
            "I guess, whip it out.",
            "Fine. . . [She drools a bit into her cleavage].",
            "Heh, ok, alright.",
            "Well, sure, stick it in.",
            "I suppose. . .",
            "Well, sure, give it a rub.",
            "You've got me there."]
    elif Girl == KittyX:
        $ lines = ["Oh. . . you're probably right. . .",
            "Ok, you're probably right. . .",
            "That's. . . true. . .",
            "You've got me there.",
            "Well, sure, stick it in.",
            "I suppose. . .",
            "You've got me there.",
            "Well, sure, ok.",
            "I suppose. . .",
            "That's. . . that's a good point. . .",
            "Well, ok, put it here.",
            "Well. . . ok.",
            "I guess.",
            "I guess, whip it out.",
            "Fine. . . [She drools a bit into her cleavage].",
            "Heh, ok."]
    elif Girl == EmmaX:
        $ lines = ["You present a compelling case. . .",
            "Ok, you're probably right. . .",
            "You're probably right. . .",
            "I can't exactly argue with that. . .",
            "I suppose. . .",
            "You raise a good point. . .",
            "Well, sure, stick it in.",
            "You make a compelling argument.",
            "Very well, stick it in.",
            "Well, sure, come over here.",
            "Oh, very well.",
            "Mmmmm.",
            "Fine, whip it out.",
            "Fine. . . [She drools a bit into her cleavage].",
            "Oh, all right."]
    elif Girl == LauraX:
        $ lines = ["You make a good point. . .",
            "Ok, you're probably right. . .",
            "Well, sure, stick it in.",
            "I suppose. . .",
            "You've got me there.",
            "You're probably right. . .",
            "I guess. . .",
            "Good point. . .",
            "Yeah, probably. . .",
            "Well, ok, put it here.",
            "Well. . . ok.",
            "I guess.",
            "I guess, whip it out.",
            "Fine. . . [She drools a bit into her cleavage].",
            "Heh, ok."]
    elif Girl == JeanX:
        $ lines = ["You make a good point. . .",
            "Ok, you're probably right. . .",
            "Well, sure, stick it in.",
            "I suppose. . .",
            "You've got me there.",
            "You're probably right. . .",
            "Yeah, sure. . .",
            "Yeah, probably. . .",
            "I guess. . .",
            "Good point. . .",
            "Well, ok, put it here.",
            "Well. . . ok.",
            "I guess.",
            "I guess, whip it out.",
            "Heh, ok."]
    elif Girl == StormX:
        $ lines = ["I. . . would. . .",
            "Well. . . I might at that. . .",
            "You may be correct. . .",
            "I cannot argue with that. . .",
            "I suppose you have a point. . .",
            "You do raise a worthy point. . .",
            "Well, sure, stick it in.",
            "I suppose. . .",
            "You make a compelling argument.",
            "Very well, stick it in.",
            "I cannot exactly argue with that. . .",
            "I suppose. . .",
            "You do raise a good point. . .",
            "Fine, come over here.",
            "Oh, very well.",
            "Mmmmm.",
            "Fine, show me.",
            "Fine. . . [She drools a bit into her cleavage].",
            "Oh, all right."]
    elif Girl == JubesX:
        $ lines = ["You make a good point. . .",
            "Um. . . maybe? . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label unconvinced_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Tsk, not this time, " + Girl.player_petname + " that just seems. . . dirty.",
            "I really don't think that I would."]
    elif Girl == KittyX:
        $ lines = ["Um, not this time, " + Girl.player_petname + "_, that's too. . .",
            "I really don't think so.",
            "I really don't think that I would."]
    elif Girl == EmmaX:
        $ lines = ["I would, but still no, " + Girl.player_petname + "_.",
            "I really don't think so.",
            "I don't think that I would."]
    elif Girl == LauraX:
        $ lines = ["I would, but still no, " + Girl.player_petname + "_.",
            "I really don't think so.",
            "I don't think that I would."]
    elif Girl == JeanX:
        $ lines = ["I would, but still no, " + Girl.player_petname + "_.",
            "I really don't think so.",
            "I don't think that I would."]
    elif Girl == StormX:
        $ lines = ["I would, but still no, " + Girl.player_petname + "_.",
            "I really do not think so.",
            "I do not think that I would."]
    elif Girl == JubesX:
        $ lines = ["I would, but still no, " + Girl.player_petname + "_.",
            "Doubt.",
            "I really doubt that. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label unsatisfied_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I didn't exactly get off there. . .",
            "That didn't really do it for me. . .",
            "Hmm, you seemed to get more out of that than me. . ."]
    elif Girl == KittyX:
        $ lines = ["Could you have maybe paid more attention? . .",
            "Hmm, you seemed to get more out of that than me. . .",
            "I didn't get much out of that. . ."]
    elif Girl == LauraX:
        $ lines = ["Forgetting someone? . .",
            "That didn't do much for me. . ."]
    elif Girl == EmmaX:
        $ lines = ["Could you have perhaps been more attentive? . .",
            "Hmm, you seemed to get more out of that than I did. . .",
            "I'm afraid that didn't do much for me. . ."]
    elif Girl == JeanX:
        $ lines = ["I think you need to get back down there."]
    elif Girl == StormX:
        $ lines = ["I could have used some more attention to my needs. . .",
            "I am afraid that you got more out of that than I. . .",
            "I am afraid that did not do much for me. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label starting_to_get_bored_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["You like how those feel, huh?",
            "You're just going at them, huh?",
            "You like how that feels, huh?",
            "What are you even doing down there?",
            "Uh, that's nice, but. . .",
            "You like it down there?",
            "Are you getting close here? I'm getting a little sore.",
            "Are you getting close here? My jaw's getting pretty sore.",
            "What are you even doing down there?",
            "Are you getting close here? I'm getting a little sore.",
            "Are you getting close here?"]
    elif Girl == KittyX:
        $ lines = ["You're just going at them, huh?",
            "Are they keeping you satisfied?",
            "You like how those feel, huh?",
            "You like how that feels, huh?",
            "You like it down there?",
            "Uh, that's nice, but. . .",
            "What are you even?",
            "Are you getting close here? I'm getting a little sore.",
            "So are we" + Girl.like + "_getting close here?",
            "Are you getting close here?",
            "What are you even doing down there?",
            "So are we" + Girl.like + "_getting close here? This is not super pleasant. . ."]
    elif Girl == EmmaX:
        $ lines = ["They really are magnificent, aren't they?",
            "Lovely, aren't they?",
            "Luxurious, yes?",
            "You like how that feels, huh?",
            "Isn't it just delicious?",
            "Mmmm I do enjoy that. . .",
            "Ungh, You're getting going there. . .",
            "Are you getting close here? I'm getting a bit sore.",
            "So are we getting close?",
            "So are we getting close here?",
            "Are we getting close here?",
            "What are you even doing down there?",
            "You certainly are enthusiastic. . ."]
    elif Girl == LauraX:
        $ lines = ["Enjoying yourself?",
            "You seem to be enjoying yourself. . .",
            "This is kinda nice. . .",
            "Kinda nice, but. . .",
            "Mmmm, you're enjoying that, huh?",
            "Isn't it just delicious?",
            "Mmmm. . .",
            "Ungh, you're really getting in there. . .",
            "Are you getting close here? I'm getting bored.",
            "So are we getting close?",
            "We getting close here?",
            "Are we getting close here?",
            "What are you even doing down there?"]
    elif Girl == JeanX:
        $ lines = ["Having fun there?",
            "This is kinda nice. . .",
            "Kinda nice, but. . .",
            "Mmmm, you're enjoying that, huh?",
            "Isn't it just delicious?",
            "Mmmm. . .",
            "Ungh, you're really getting in there. . .",
            "You seem to be enjoying yourself. . .",
            "Hey, how you doing up there? About done?",
            "Ok, had enough yet?",
            "Ok, that good enough?",
            "'bout done there?",
            "What are you even doing down there?"]
    elif Girl == StormX:
        $ lines = ["You really seem to enjoy those. . .",
            "You really seem to enjoy those. . .",
            "Your hands are so warm. . .",
            "Mmmm, yes. . . deeper. . .",
            "Oh, that is delightful. . .",
            "Mmmm. . .",
            "Ooh, watch it, watch it. . .",
            "You are quite enthusiastic. . .",
            "Are you getting close? This is making me a bit sore. . .",
            "Are you nearly finished?",
            "So are you nearly finished?",
            "Are you nearly satisfied?",
            "What are you even doing down there?"]
    elif Girl == JubesX:
        $ lines = ["Having fun?",
            "Ok, but, uh. . .",
            "Yeah, I like that too. . .",
            "Mmmm. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label definitely_bored_now_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I'm getting rug-burn here " + Girl.player_petname + "_. Can we do something else?",
            "I'm getting a little tired, " + Girl.player_petname + "_. Can we do something else?",
            "" + Girl.player_petname + "_, this is getting uncomfortable, maybe we could try something else.",
            "Ow, i'm not used to this. Mind if we take a break?",
            "Can we be done with this now? I'm getting sore.",
            "I'm . . .getting . . .worn out. . . here, . . " + Girl.player_petname + "_.",
            "I'm kinda done with this, " + Girl.player_petname + "_.",
            "Can we. . . do something. . . else?"]
    elif Girl == KittyX:
        $ lines = ["Maybe we could try something else here " + Girl.player_petname + "_?",
            "You look like you're having fun there, but maybe we could" + Girl.like + "_try something else?",
            "" + Girl.player_petname + "_, I know you're having fun down there, but maybe we could try something else.",
            "" + Girl.player_petname + "_, this is nice, but could we do something else?",
            "" + Girl.player_petname + "_, this is getting kind sore, maybe we could try something else.",
            "" + Girl.player_petname + "_, this is getting weird, maybe we could try something else.",
            "Can we" + Girl.Like + "_be done with this now? I'm getting sore.",
            "Are you getting close here? I'm cramping up.",
            "Can we" + Girl.Like + "_be done with this now? I'm getting sore.",
            "Ouch, hand cramp, can we" + Girl.like + "_take a break?",
            "I'm getting rug-burn here " + Girl.player_petname + "_. Can we do something else?",
            "I'm" + Girl.like + "_totally worn out here. Can we do something else?",
            "" + Girl.player_petname + "_, this is getting uncomfortable, maybe we could try something else.",
            "Ouch, foot cramp, can we" + Girl.like + "_take a break?",
            "I'm . . .getting . . kinda tired. . . here. . .",
            "I'm . . .getting . . kinda tired. . . of this. . .",
            "Can we. . . do something. . . else?",
            "This is getting a bit dull."]
    elif Girl == EmmaX:
        $ lines = ["Perhaps we could try something else, " + Girl.player_petname + "_?",
            "You certainly seem to be enjoying yourself, but perhaps we could add some variety?",
            "" + Girl.player_petname + "_, I know you're having fun down there, but maybe we could try something else.",
            "" + Girl.player_petname + "_, this is nice, but could we do something else?",
            "" + Girl.player_petname + "_, this is getting kind sore, maybe we could try something else.",
            "" + Girl.player_petname + "_, this is getting weird, maybe we could try something else.",
            "Are you certain you didn't have anything else in mind?",
            "Are you about done? I'm a little tired of this.",
            "Could we be done here, my feet are getting sore.",
            "Hmm, I'm getting a bit of a cramp here.",
            "Mind if we take a break?",
            "I'm getting a bit worn out, could we settle this some other way?",
            "I'm getting a bit worn out here, could we do something else?",
            "" + Girl.player_petname + "_, this is getting uncomfortable, maybe we could try something else.",
            "Hmm, foot cramp, could we take a short break?",
            "I'm . . .getting . . a bit. . . tired. . . here. . .",
            "I'm . . .getting . . a bit. . . tired. . . of this. . .",
            "Could we. . . do something. . . else?",
            "Can we. . . do something. . . else?",
            "I'm a bit bored by this."]
    elif Girl == LauraX:
        $ lines = ["Maybe it's time for something else, " + Girl.player_petname + "_?",
            "Maybe change things up a little?",
            "" + Girl.player_petname + "_, could we try something different?",
            "This working for you?",
            "Are you getting close here? I'm bored.",
            "Ok, seriously, let's try something different.",
            "Hmm, this is boring, can we take a break?",
            "Seriously, can we do something else?",
            "I'm getting kinda bored. Can we do something else?",
            "" + Girl.player_petname + "_, this is getting uncomfortable, maybe we could try something else.",
            "Hmm, this is getting a bit boring.",
            "Hey. . . could we. . . try something. . . else?",
            "Can we. . . do something. . . else?",
            "I'm kinda bored by this."]
    elif Girl == JeanX:
        $ lines = ["Maybe it's time for something else, " + Girl.player_petname + "_?",
            "Maybe try something else?",
            "" + Girl.player_petname + "_, could we try something different?",
            "Nice, right?",
            "Hey, you about done up there?",
            "Ok, seriously, let's try something different.",
            "Ok, I'm bored now. Can we try something else?",
            "Ok, seriously, can't we do something else?",
            "Ok, that's enough of that. Can we do something else?",
            "" + Girl.player_petname + "_, this is getting uncomfortable, maybe we could try something else.",
            "Hmm, my feet are cramping up here. . .",
            "Hey. . . you. . . about done. . . there?",
            "Can we. . . do something. . . else?",
            "Well this is not fun."]
    elif Girl == StormX:
        $ lines = ["I am sure that is fun, but could we try something different?",
            "Are you certain you didn't have anything else in mind?",
            "Are you about finished? I am growing tired of this.",
            "Could we be done here, my feet are getting sore.",
            "Hmm, I am developing a hand cramp here.",
            "Mind if we take a break?",
            "This is becoming uncomfortable, is there some way I could finish you off?",
            "My jaw is becoming uncomfortable, could we do something else?",
            "" + Girl.player_petname + "_, this is getting uncomfortable, maybe we could try something else.",
            "Hmm, foot cramp. Could we take a short break?",
            "I am . . .becoming . . a bit. . . worn out. . . here. . .",
            "This is . . .becoming . . rather. . . uncomfortable. . .",
            "Would you mind. . . a different. . . option?",
            "Could we. . . do something. . . else?",
            "I am getting rather tired of this."]
    elif Girl == JubesX:
        $ lines = ["Could we maybe try. . . something else?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label no_ass_to_mouth_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["No thanks, " + Girl.player_petname + "_. Maybe a Handy instead?"]

    Girl.voice "[line]"

    return

label since_you_are_so_nice_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Well, since you're be'in so nice about it, I guess we can give it a go. . .",
            "I guess if you really want to try it. . .",
            "I guess it doesn't feel so bad. . ."]
    elif Girl == KittyX:
        $ lines = ["{i}Well. . .{/i} I didn't say I didn't want to. . .",
            "Well" + Girl.like + "_just take it easy, ok? . .",
            "I guess it doesn't feel so bad. . .",
            "Well, now that you mention it. . ."]
    elif Girl == EmmaX:
        $ lines = ["I am willing to give it a try if you are. . .",
            "Well, so long as you know what you're doing . .",
            "Or not. . .",
            "Well, now that you mention it. . .",
            "I didn't say I was opposed. . ."]
    elif Girl == LauraX:
        $ lines = ["No no, not a problem. . .",
            "Hey, whatever floats your boat. . .",
            "Get in there.",
            "Or not. . .",
            "Well, now that you mention it. . ."]
    elif Girl == JeanX:
        $ lines = ["Oh, no, it's fine.",
            "Sure, works for me. . .",
            "Get in there.",
            "I didn't say I minded. . .",
            "Well, now that you mention it. . ."]
    elif Girl == StormX:
        $ lines = ["I am willing to give it a try if you are. . .",
            "Oh, that is unfortunate. . .",
            "I did not say that I was opposed. . .",
            "Or perhaps not. . .",
            "Well, now that you mention it. . ."]
    elif Girl == JubesX:
        $ lines = ["No no, not a problem. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label used_to_action_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["You want some of this action?",
            "So you'd like another go?",
            "You can't stay away from this. . ."]

        if Action_type == "masturbation":
            $ lines.append("You sure do like to watch.")
            $ lines.append("So you'd like me to go again?")
            $ lines.append("You want to watch some more?")
            $ lines.append("You want me ta diddle myself?")
        elif Action_type == "handjob":
            $ lines.append("So you'd like another handy?")
            $ lines.append("A little. . . [fist pumping hand gestures]?")
            $ lines.append("A little tender loving care?")
        elif Action_type == "footjob":
            $ lines.append("You want me to use my feet?")
            $ lines.append("So you'd like another foot rub?")
            $ lines.append("So you'd like me to. . . [she rubs her foot along your leg]?")
            $ lines.append("So you'd like another foot rub?")
        elif Action_type == "titjob":
            $ lines.append("A little soft embrace?")
            $ lines.append("You want some of this action [jiggles her tits]?")
            $ lines.append("So you'd like another titjob?")
            $ lines.append("You want me to pillow your crank?")
        elif Action_type == "blowjob":
            $ lines.append("You want some of this action [mimes blowing]?")
            $ lines.append("So you'd like another blowjob?")
            $ lines.append("A little. . . lick?")
            $ lines.append("You want me to wet your willy?")
            $ lines.append("You want me to slick your pole?")
            $ lines.append("You want me to grease your skids?")
        elif Action_type in dildo_Action_types:
            $ lines.append("You want me ta lube up your toy?")
        elif Action_type == "sex":
            $ lines.append("You want to stick it in my pussy again?")
            $ lines.append("You want me to ride your pole?")
            $ lines.append("You wanna dip your wick?")
        elif Action_type == "anal":
            $ lines.append("You want to stick it in my ass again?")
            $ lines.append("You can't stay away from this booty.")
            $ lines.append("You want me to ride your pole?")
            $ lines.append("You wanna dip your wick?")
        elif Action_type == "hotdog":
            $ lines.append("A little. . . bounce?")
    elif Girl == KittyX:
        $ lines = ["You want some of this?",
            "You want some of this action?",
            "So you'd like another go?",
            "Oooh, you want some of this?",
            "You can't stay away from this. . .",
            "So you'd like another round?",
            "You're really digging this. . .",
            "Again?"]

        if Action_type == "masturbation":
            $ lines.append("You like to watch me.")
            $ lines.append("You want me to get myself off?")
        elif Action_type == "handjob":
            $ lines.append("So you'd like another handy?")
            $ lines.append("A little. . . [fist pumping hand gestures]?")
            $ lines.append("A little TLC?")
            $ lines.append("You want another rub?")
        elif Action_type == "footjob":
            $ lines.append("You want me to use my feet?")
            $ lines.append("So you'd like another foot sesh?")
            $ lines.append("A little. . . [she rubs her foot along your leg]?")
            $ lines.append("You want another rub?")
        elif Action_type == "titjob":
            $ lines.append("You want some of this action [rubs her chest]?")
            $ lines.append("So you'd like another titjob?")
            $ lines.append("A little. . . puffpuff?")
            $ lines.append("A little soft embrace?")
        elif Action_type == "blowjob":
            $ lines.append("You want me to [mimes blowing]?")
            $ lines.append("So you wanna 'nother blowjob?")
            $ lines.append("A little. . . lick?")
            $ lines.append("You want me to suck you off?")
        elif Action_type in dildo_Action_types:
            $ lines.append("You want me ta lube up your toy?")
        elif Action_type == "sex":
            $ lines.append("You want to stick it in my pussy again?")
            $ lines.append("You wanna slide into me?")
            $ lines.append("You gonna make me purr?")
        elif Action_type == "anal":
            $ lines.append("You want to stick it in my ass again?")
            $ lines.append("I do have booty for days. . .")
            $ lines.append("You wanna slide into me?")
        elif Action_type == "hotdog":
            $ lines.append("You want another rub?")
    elif Girl == EmmaX:
        $ lines = ["You want more?",
            "So you'd like another?",
            "You want some of this action?",
            "So you'd like another go?",
            "Oh, you want some of this?",
            "You'd like another round?",
            "I knew you enjoyed it. . .",
            "I suppose I am irresistible. . .",
            "Oooh, you want some of this?",
            "So you'd like another round?",
            "You're really into this. . .",
            "Once more?"]

        if Action_type == "masturbation":
            $ lines.append("You really do like to watch.")
            $ lines.append("You enjoy watching me.")
            $ lines.append("You want me to take care of myself?")
        elif Action_type == "handjob":
            $ lines.append("More of this? [fist pumping hand gestures]")
            $ lines.append("Oh, did you want some attention?")
        elif Action_type == "footjob":
            $ lines.append("You'd like me to use my feet again?")
            $ lines.append("So you'd like another footjob?")
            $ lines.append("Mmmm, some. . . [she rubs her foot along your leg]?")
            $ lines.append("A little foot rub?")
        elif Action_type == "titjob":
            $ lines.append("You want some of these? [jiggles her tits]")
            $ lines.append("So you'd like another titjob?")
            $ lines.append("A little. . . [bounces tits]?")
            $ lines.append("A little warm embrace?")
        elif Action_type == "blowjob":
            $ lines.append("You want me to [mimes blowing]?")
            $ lines.append("So you want another blowjob?")
            $ lines.append("You want me to suck you off?")
            $ lines.append("Are you asking if I'm hungry?")
        elif Action_type in dildo_Action_types:
            $ lines.append("You'd like me to lube up your toy?")
        elif Action_type == "sex":
            $ lines.append("You want to stick it in my pussy again?")
            $ lines.append("Do you intend to make me melt?")
            $ lines.append("You want me to ride you?")
        elif Action_type == "anal":
            $ lines.append("You'd like to stick it in my ass again?")
            $ lines.append("You want me to ride you?")
        elif Action_type == "hotdog":
            $ lines.append("You want another rub?")
    elif Girl == LauraX:
        $ lines = ["You want some more?",
            "You want some of this action?",
            "So you'd like another go?",
            "Oh, you want some of this?",
            "You'd like another round?",
            "I must be better than I thought.",
            "I hope you don't plan on wearing me out.",
            "Oooh, you want some of this?",
            "So you'd like another round?",
            "I knew you enjoyed it. . .",
            "You're really into this. . .",
            "Again?"]

        if Action_type == "masturbation":
            $ lines.append("You like to watch.")
            $ lines.append("You really like to watch me.")
            $ lines.append("You want me to masturbate again?")
        elif Action_type == "handjob":
            $ lines.append("So you'd like another handy?")
            $ lines.append("You want a. . . [fist pumping hand gestures]?")
            $ lines.append("Another handjob?")
            $ lines.append("A little TLC?")
        elif Action_type == "footjob":
            $ lines.append("You want me to use my feet?")
            $ lines.append("So you'd like another footjob?")
            $ lines.append("A little. . . [she rubs her foot along your leg]?")
        elif Action_type == "titjob":
            $ lines.append("You want some of this action [rubs her chest]?")
            $ lines.append("So you'd like another titjob?")
            $ lines.append("Another titjob?")
            $ lines.append("A little [points at her chest]?")
        elif Action_type == "blowjob":
            $ lines.append("You want me to [mimes blowing]?")
            $ lines.append("So you want another blowjob?")
            $ lines.append("You want me to lick you?")
            $ lines.append("You want me to suck you off?")
            $ lines.append("A little bj?")
        elif Action_type in dildo_Action_types:
            $ lines.append("You want me ta lube up your toy?")
        elif Action_type == "sex":
            $ lines.append("You want to stick it in my pussy again?")
            $ lines.append("You want to plow me?")
        elif Action_type == "anal":
            $ lines.append("You want to stick it in my ass again?")
            $ lines.append("You want to plow me?")
        elif Action_type == "hotdog":
            $ lines.append("You want another rub?")
    elif Girl == JeanX:
        $ lines = ["You want some more?",
            "You want some of this action?",
            "So you'd like another go?",
            "Oh, you want some of this?",
            "You'd like another round?",
            "I must be better than I thought.",
            "I knew you enjoyed it. . .",
            "I hope you don't plan on wearing me out.",
            "Oooh, you want some of this?",
            "So you'd like another round?",
            "You're really into this. . .",
            "Again?"]

        if Action_type == "masturbation":
            $ lines.append("You do like to watch.")
            $ lines.append("You'd like me to masturbate again?")
            $ lines.append("You like to watch me.")
        elif Action_type == "handjob":
            $ lines.append("So you'd like another handjob?")
            $ lines.append("You want a. . . [fist pumping hand gestures]?")
            $ lines.append("Another handjob?")
        elif Action_type == "footjob":
            $ lines.append("You want me to use my feet?")
            $ lines.append("So you'd like another footjob?")
            $ lines.append("A little foot rub?")
            $ lines.append("A little. . . [she rubs her foot along your leg]?")
        elif Action_type == "titjob":
            $ lines.append("You want some of this action [rubs her chest]?")
            $ lines.append("So you'd like another titjob?")
            $ lines.append("Another titjob?")
            $ lines.append("A little [points at her chest]?")
        elif Action_type == "blowjob":
            $ lines.append("You want me to [mimes blowing]?")
            $ lines.append("So you want another blowjob?")
            $ lines.append("You want me to lick you?")
            $ lines.append("You want me to suck you off?")
            $ lines.append("A BJ?")
        elif Action_type in dildo_Action_types:
            $ lines.append("You want me ta lube up your toy?")
        elif Action_type == "sex":
            $ lines.append("You want to stick it in my pussy again?")
            $ lines.append("You want to fuck me?")
            $ lines.append("You want to plow me?")
        elif Action_type == "anal":
            $ lines.append("You want to fuck me?")
            $ lines.append("You want to plow me?")
        elif Action_type == "hotdog":
            $ lines.append("You want another rub?")
    elif Girl == StormX:
        $ lines = ["You want more?",
            "So you would like another?",
            "You want some more?",
            "You want some of this action?",
            "So you'd like another go?",
            "Oh, did you want some of this?",
            "You would like another round?",
            "I suppose that I can be irresistible. . .",
            "I could get used to this. . .",
            "Oooh, you wanted some of this?",
            "So you would like another round?",
            "I knew you would enjoy it. . .",
            "You really are into this. . .",
            "Once more?"]

        if Action_type == "masturbation":
            $ lines.append("You really do like to watch.")
            $ lines.append("You enjoy watching me do that?")
            $ lines.append("You want me to take care of myself?")
        elif Action_type == "handjob":
            $ lines.append("More of this? [fist pumping hand gestures]")
            $ lines.append("Oh, did you want some attention?")
            $ lines.append("So you'd like another handy?")
            $ lines.append("Another handjob?")
        elif Action_type == "footjob":
            $ lines.append("You would like me to use my feet again?")
            $ lines.append("So you would like another footjob?")
            $ lines.append("Mmmm, some. . . [she rubs her foot along your leg]?")
            $ lines.append("A little foot rub?")
        elif Action_type == "titjob":
            $ lines.append("You wish to use these? [jiggles her tits]")
            $ lines.append("So you would like another titjob?")
            $ lines.append(". . . [bounces tits]?")
            $ lines.append("You would like to give it a hug?")
        elif Action_type == "blowjob":
            $ lines.append(". . . [mimes blowing]?")
            $ lines.append("So you would like another blowjob?")
            $ lines.append("You wish for me to suck you off?")
            $ lines.append("Are you asking if I am hungry?")
        elif Action_type in dildo_Action_types:
            $ lines.append("You want me ta lube up your toy?")
        elif Action_type == "sex":
            $ lines.append("You want to stick it in my pussy again?")
            $ lines.append("Did you want me to ride you?")
            $ lines.append("You want me to ride you?")
        elif Action_type == "anal":
            $ lines.append("You'd like to stick it in my ass again?")
            $ lines.append("Did you want me to ride you?")
            $ lines.append("You want me to ride you?")
        elif Action_type == "hotdog":
            $ lines.append("You want another rub?")
    elif Girl == JubesX:
        $ lines = ["Again?"]

        if Action_type == "masturbation":
            $ lines.append("You do enjoy watching.")
            $ lines.append("You really enjoy watching me.")
        elif Action_type == "blowjob":
            $ lines.append("You want me to shlick again?")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label auto_accepted_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Ok, " + Girl.player_petname + "_, let's do this.",
            "Hmm, stick it in. . .",
            "Hmm, I've apparently got someone's attention. . ."]
    elif Girl == KittyX:
        $ lines = ["Oh. . . game on, " + Girl.player_petname + "_.",
            "Ooo, " + Girl.player_petname + "_, toys!",
            "Hmm, stick it in. . .",
            "Oookay. . .",
            "Hmm, I've apparently got someone's attention. . ."]
    elif Girl == EmmaX:
        $ lines = ["Mmm, if you insist, " + Girl.player_petname + "_.",
            "Hmm, " + Girl.player_petname + "_, toys!",
            "Mmmm, " + Girl.player_petname + "_, toys. . .",
            "Oooh, naughty boy. . .",
            "Now what shall we do with that . ."]
    elif Girl == LauraX:
        $ lines = ["Fine by me, " + Girl.player_petname + "_.",
            "Ooo, " + Girl.player_petname + "_, toys!",
            "Yeah, ok. . .",
            "Oh, what did you have in mind with that? . ."]
    elif Girl == JeanX:
        $ lines = ["Oh, if you must, " + Girl.player_petname + "_.",
            "Ooo, " + Girl.player_petname + "_, toys!",
            "Oh! Sure. . .",
            "Oh, what did you have in mind with that? . ."]
    elif Girl == StormX:
        $ lines = ["Mmm, if you insist, " + Girl.player_petname + "_.",
            "Hmm, " + Girl.player_petname + "_, toys!",
            "Mmmm, " + Girl.player_petname + "_, toys. . .",
            "" + Girl.player_petname + "_, I am surprised at you. . .",
            "Now what shall we do with that . ."]
    elif Girl == JubesX:
        $ lines = ["Fine by me, " + Girl.player_petname + "_."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label were_done_here_lines(Girl, Action_type):
    $ lines = ["" + Girl.name + " shoves you away and slaps you in the face.",
        "" + Girl.name + " shoves you away."]

    "[line]"

    if Girl == RogueX:
        $ lines = ["Jackass!{p}If that's how you want to treat me, we're done here!",
            "Dick!{p}}If that's how you want want to act, I'm out of here!"]
    elif Girl == KittyX:
        $ lines = ["Jerk!{p}}I am not putting up with that shit!",
            "Asshole!{p}You need to ask nicer than that!",
            "Jerk!{p}}I'm not into that!",
            "Jerk!{p}Ask nice if you want to stick something in my pussy!",
            "Jerk!{p}}Ask nice if you want to stick something in my ass!"]
    elif Girl == EmmaX:
        $ lines = ["Impertinent!{p}Do not test my patience with you.",
            "Impertinent!{p}You need to ask a lady first.",
            "Don't push your luck, " + Girl.player_petname + "_.",
            "Ask nicely before trying anything like that!",
            "Ask nicely if you want to stick something in my ass!"]
    elif Girl == LauraX:
        $ lines = ["Dick.{p}Don't push me.",
            "Yeah, not like that you won't.",
            "Don't push it, " + Girl.player_petname + "_.",
            "Jerk!{p}}Ask nice if you want to stick something in my pussy!",
            "Jerk!{p}Ask nice if you want to stick something in my ass!"]
    elif Girl == JeanX:
        $ lines = ["Hey, I don't need my powers to hurt you.",
            "Tsk tsk.{p}Don't push it, " + Girl.player_petname + "_.",
            "Jerk!{p}Ask nice if you want to stick something in my pussy!",
            "Jerk!{p}Ask nice if you want to stick something in my ass!"]
    elif Girl == StormX:
        $ lines = ["That is unfortunate.",
            "I am afraid that is -not- what will happen here.",
            "That is unfortunate.",
            "I am afraid that is -not- what will happen here.",
            "Do not go beyond yourself, " + Girl.player_petname + "_.",
            "Ask nicely before trying anything like that!",
            "Ask nicely if you want to stick something in my ass!"]
    elif Girl == JubesX:
        $ lines = ["Dick.{p}Don't push me."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label first_action_approval_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Hmm, could be fun. . .",
            "Sure. . .",
            "Heh, might be fun.",
            "I guess. . .",
            "Hmm, I've always wanted to try it. . .",
            "Hmm, it has been on my list. . ."]

        if Action_type == "masturbation":
            $ lines.append("I guess it could be fun with you watching. . .")

        if Action_type in dildo_Action_types:
            $ lines.append("I guess it could be fun with a partner. . .")

        if Action_type in cock_Action_types:
            $ lines.append("Hmm, you look ready for it, at least. . .")
    elif Girl == KittyX:
        $ lines = ["That's kinda gross. . .",
            "I guess. . .",
            "Hadn't really considered that.",
            "" + Girl.Like + "_sure. . .",
            "This could be kinda fun . . .",
            "I guess it could be fun with a partner. . .",
            "I guess it could be fun two-player. . .",
            "Sure. . .",
            "I can't say it hasn't crossed my mind. . .",
            "Anything's worth a shot. . .",
            "Hmm, you look ready to go. . ."]
    elif Girl == EmmaX:
        $ lines = ["Hm, I didn't know that's what you were into.",
            "Hmm, I was wondering when you'd ask. . .",
            "I suppose. . .",
            "I guess it could be fun with a partner. . .",
            "I suppose I could enjoy that. . .",
            "Very well. . .",
            "I do enjoy a good performance . . .",
            "I was hoping you'd ask. . .",
            "I was getting tired of waiting. . .",
            "Well if that's what gets you off. . ."]
    elif Girl == LauraX:
        $ lines = ["Hm, I didn't know that's what you were into.",
            "Hmm. . .",
            "Sounds fun. . .",
            "Huh. . .",
            "I guess it could be fun with a partner. . .",
            "I guess it could be fun two-player. . .",
            "Sure. . .",
            "I was hoping you'd ask. . .",
            "I was tired of waiting. . .",
            "Well if that's what gets you off. . ."]
    elif Girl == JeanX:
        $ lines = ["Mmmm, you're into that?",
            "Hmm. . .",
            "Sounds fun, but. . .",
            "Huh. . .",
            "I do have some free time. . .",
            "I do have some time. . .",
            "I guess it could be fun with a partner. . .",
            "Sure. . .",
            "I was wondering when this would come up. . .",
            "I was tired of waiting. . .",
            "Ok, we can start with that. . ."]
    elif Girl == StormX:
        $ lines = ["Hmmm, an interesting proposal. . .",
            "I suppose. . .",
            "Hmm, I was expecting you to ask. . .",
            "I suppose. . .",
            "I guess it could be fun with a partner. . .",
            "I suppose I could enjoy that. . .",
            "Very well. . .",
            "I do not mind an audience . . .",
            "I was hoping you would ask. . .",
            "I was getting tired of waiting. . .",
            "Well if that is what satisfies you. . ."]
    elif Girl == JubesX:
        $ lines = ["Hm, I hadn't thought. . .",
            "Hmm. . .",
            "I could work off some stress. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label first_action_approval_mostly_love_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["If that's what you like. . ."]

        if Action_type in dildo_Action_types:
            $ lines.append("I've had a reasonable amount of experience with these, you know. . .")

        if Action_type in cock_Action_types:
            $ lines.append("It looks like you need some relief. . .")
            $ lines.append("Huh, well that's certainly one way to get off.")

        if Action_type in contact_Action_types:
            $ lines.append("Well, I've never really been able to touch people without draining them, this could be an interesting experience. . .")
            $ lines.append("Well, I've never been able to do this before now, so this might be fun.")

        if Action_type in kinky_Action_types:
            $ lines.append("I guess if you really want to try it. . .")

        if Action_type == "masturbation":
            $ lines.append("Since my love life's been a bit. . . limited, I've gotten pretty good at this.")

        if Action_type == "blowjob":
            $ lines.append("I've never really put something like that in my mouth. . . might be interesting.")

        if Action_type == "dildo_ass":
            $ lines.append("I haven't actually used one of these, back there before. . .")
    elif Girl == KittyX:
        $ lines = ["That's, I don't know. . .",
            "I guess it could be interesting. . .",
            "It's nice that you even thought about it.",
            "I have wondered what you. . . taste like.",
            "This is kind of {i}intimate{/i} . . .",
            "I've had a reasonable amount of experience with these, you know. . .",
            "I" + Girl.like + "_haven't actually used one of these, back there before. . .",
            "I guess it couldn't hurt. . .",
            "I don't want you to think I'm some kind of slut. . .",
            "I guess? . .",
            "It does look a bit swollen. . ."]
    elif Girl == EmmaX:
        $ lines = ["Oh, are we there now?",
            "I suppose you've earned something. . .",
            "I suppose you've earned something special. . .",
            "I am curious if it tastes as good as it looks. . .",
            "I've had a reasonable amount of experience with these, you know. . .",
            "I suppose you might enjoy that. . .",
            "I suppose it couldn't hurt. . .",
            "I don't usually show this side . . .",
            "I wouldn't want you to get hurt. . .",
            "I was wondering when you'd ask. . .",
            "I wouldn't want to leave you. . . unattended. . ."]
    elif Girl == LauraX:
        $ lines = ["Oh, we're there now?",
            "You'd like that. . .",
            "Well, maybe you deserve it.",
            "I have wondered how you taste.",
            "I've had a reasonable amount of experience with these, you know. . .",
            "I haven't actually used one of these, back there before. . .",
            "I guess it couldn't hurt. . .",
            "I don't know, are you sure?",
            "Well, you look so cute when you ask. . .",
            "I was hoping you'd ask. . .",
            "If that's what you're into. . ."]
    elif Girl == JeanX:
        $ lines = ["Oh, we're there now?",
            "Well, I guess it wouldn't be so bad. . .",
            "I'd love to, but. . .",
            "Well, I could hardly turn down that offer. . .",
            "I've had a reasonable amount of experience with these, you know. . .",
            "I suppose. . .",
            "I was wondering when this would come up. . .",
            "Well. . .",
            "I was expecting this. . .",
            "Ok, we can start with that. . ."]
    elif Girl == StormX:
        $ lines = ["Oh, that is a bit forward!",
            "I might enjoy that. . .",
            "I suppose you've earned something special. . .",
            "I have been curious. . .",
            "I've had a reasonable amount of experience with these, you know. . .",
            "I suppose you might enjoy that. . .",
            "I am usually alone for this . . .",
            "I could enjoy that. . .",
            "I would not want to. . . overwhelm you. . .",
            "I was hoping that you would ask. . .",
            "I would not wish to leave you. . . un-tended. . ."]
    elif Girl == JubesX:
        $ lines = ["What? What're you talking about?",
            "You'd like that. . .",
            "I don't know, are you sure?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label first_action_approval_mostly_obedience_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["If that's what you want, " + Girl.player_petname + "_. . .",
            "If that's what you want. . .",
            "I suppose, if that's what you want. . .",
            "Ok, " + Girl.player_petname + "_, I'm ready."]
    elif Girl == KittyX:
        $ lines = ["You don't have to do that.",
            "If you want, " + Girl.player_petname + "_. . .",
            "I mean. . .",
            "Ok by me, " + Girl.player_petname + "_. .",
            "If you want me to. . .",
            "If that's what you want, " + Girl.player_petname + "_. . .",
            "I suppose if it's you, " + Girl.player_petname + "_. . .",
            "Well. . .",
            "If you want. . ."]
    elif Girl == EmmaX:
        $ lines = ["Is that what gets you off?",
            "If that's what you'd like, " + Girl.player_petname + "_. . .",
            "If that's what you want. . .",
            "If that's what you want, " + Girl.player_petname + "_. . .",
            "If you enjoy that, " + Girl.player_petname + "_. . .",
            "If you insist, " + Girl.player_petname + "_. . .",
            "If that's what you're into, " + Girl.player_petname + "_. . .",
            "I expected we'd get here at some point. . .",
            "If that's what works for you. . ."]
    elif Girl == LauraX:
        $ lines = ["Is that what gets you off?",
            "If you want, " + Girl.player_petname + "_. . .",
            "If you'd like that. . .",
            "If that's what you want. . .",
            "If that's what you're into. . .",
            "If that's what you want, " + Girl.player_petname + "_. . .",
            "Yes, " + Girl.player_petname + "_. . .",
            "I expected that. . .",
            "If that's what works for you. . ."]
    elif Girl == JeanX:
        $ lines = ["Is that what gets you off?",
            "If you'd want that. . .",
            "I could do that, I guess. . .",
            "If that's what you're into. . .",
            "If that's what you want, " + Girl.player_petname + "_. . .",
            "If you want, " + Girl.player_petname + "_. . .",
            "Ok, " + Girl.player_petname + "_. . .",
            "I expected that. . .",
            "Ok, we can start with that. . ."]
    elif Girl == StormX:
        $ lines = ["That is what you want?",
            "If that is what you want, " + Girl.player_petname + "_. . .",
            "If that is what you want. . .",
            "If you enjoy that, " + Girl.player_petname + "_. . .",
            "If that is what you wish, " + Girl.player_petname + "_. . .",
            "If you enjoy watching, " + Girl.player_petname + "_. . .",
            "I expected we would get here at some point. . .",
            "If that is what works for you. . ."]
    elif Girl == JubesX:
        $ lines = ["Is that what gets you off?",
            "If that's what you're into. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label first_action_approval_addicted_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I guess. . .",
            "Hmmmm. . . ."]

        if Action_type == "handjob":
            $ lines.append("I think, if I could just touch that. . .")
        elif Action_type == "blowjob":
            $ lines.append("I think. . . for some reason I really do want that in my mouth. . .")
        elif Action_type in below_Action_types:
            $ lines.append("Well. . . I bet it would feel really good down there.")
    elif Girl == KittyX:
        $ lines = ["I kind of {i}need{/i} to. . .",
            "Hmmmm. . . .",
            "Okay. . .",
            "I have kind of been hoping you might. . .",
            "I. . . if that's how you want to do it. . . maybe?",
            "Hmmm. . ."]

        if Action_type == "blowjob" or Action_type == "kiss":
            $ lines.append("My mouth is watering. . .")
    elif Girl == EmmaX:
        $ lines = ["Mmmmmmmm. . .",
            "Hmmmm. . . .",
            "I don't know if I could wait. . .",
            "Very well. . .",
            "I was wondering how it would feel with you. . .",
            "Hmm, that would be an interesting experience. . .",
            "Hrmm. . ."]
    elif Girl == LauraX:
        $ lines = ["Hmmmm. . . .",
            "Okay. . .",
            "Sounds fun. . .",
            "Hmm, sounds fun. . .",
            "Hrmm. . ."]

        if Action_type == "blowjob" or Action_type == "kiss":
            $ lines.append("[wipes away a little drool]")
    elif Girl == JeanX:
        $ lines = ["Hmmmm. . . .",
            "Mmmmm. . .",
            "Okay. . .",
            "That does sound fun. . .",
            "Hmm, sounds fun. . .",
            "Hrmm. . ."]
    elif Girl == StormX:
        $ lines = ["Mmmmmmmm. . .",
            "Hmmmm. . . .",
            "I might enjoy that. . .",
            "Very well. . .",
            "I was curious as to the effect that would have. . .",
            "Hmm, that would certainly be interesting. . .",
            "Hrmm. . ."]
    elif Girl == JubesX:
        $ lines = ["If you want, " + Girl.player_petname + "_. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label action_forcefully_approved_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["That's really what you want?",
            "This isn't going to become a habit, will it?",
            "You want me to do that again?"]

        if Action_type in dildo_Action_types:
            $ lines.append("The toys again?")
        elif Action_type in ["kiss", "fondle_thighs", "fondle_ass", "hotdog"]:
            $ lines.append("That's it?")
            $ lines.append("That's all you want?")
        elif Action_type == "masturbation":
            $ lines.append("So you just want to watch then?")
            $ lines.append("You want to watch me again?")
    elif Girl == KittyX:
        $ lines = ["This isn't going to become a habit, will it?",
            "Again? Why do you do this to me?",
            "You really ask a lot here. . ."]

        if Action_type in job_Action_types:
            $ lines.append("You want me to do that again?")
        elif Action_type in dildo_Action_types:
            $ lines.append("The toys again?")
        elif Action_type in ["kiss", "fondle_thighs", "fondle_ass", "hotdog"]:
            $ lines.append("That's it, right?")
            $ lines.append("That's all?")
            $ lines.append("That's {i}all{/i} you want?")
        elif Action_type == "masturbation":
            $ lines.append("So you {i}just{/i} want to watch. . .")
            $ lines.append("Again? Just looking?",)
    elif Girl == EmmaX:
        $ lines = ["Ugh, that again?",
            "Again? You're really wearing out your welcome.",
            "You don't hold back. . .",
            "Maybe that's going a bit too far. . ."]

        if Action_type in job_Action_types:
            $ lines.append("You aren't getting used to this service, are you?")
        elif Action_type in dildo_Action_types:
            $ lines.append("The toys again?")
        elif Action_type in ["kiss", "fondle_thighs", "fondle_ass", "hotdog"]:
            $ lines.append("No more than that?")
            $ lines.append("That's it?")
        elif Action_type == "masturbation":
            $ lines.append("But. . . {i}only{/i} a show?")
            $ lines.append("Again? Just you only want to watch?")
    elif Girl == LauraX:
        $ lines = ["You're kinda pushing it.",
            "Again?",
            "I hope I don't wear you out.",
            "Hmm, again?",
            "You don't hold back. . .",
            "That's pushing it. . ."]

        if Action_type in dildo_Action_types:
            $ lines.append("The toys again?")
        elif Action_type in ["kiss", "fondle_thighs", "fondle_ass", "hotdog"]:
            $ lines.append("Nothing more than that?")
            $ lines.append("That's it?")
        elif Action_type == "masturbation":
            $ lines.append("And you {i}just{/i} want to watch. . .")
    elif Girl == JeanX:
        $ lines = ["Well that's a big ask. . .",
            "Again?",
            "Hmm, again?",
            "You'll pay for this eventually. . .",
            "Well you're optimistic. . ."]

        if Action_type in dildo_Action_types:
            $ lines.append("The toys again?")
        elif Action_type in ["kiss", "fondle_thighs", "fondle_ass", "hotdog"]:
            $ lines.append("And that's it?")
            $ lines.append("That's it?")
        elif Action_type in ["footjob", "hotdog"]:
            $ lines.append("Odd. . .")
        elif Action_type == "masturbation":
            $ lines.append("But -just- watch, right? . .")
    elif Girl == StormX:
        $ lines = ["Tsk, again?",
            "Oh, again?",
            "You do not restrain yourself. . .",
            "Perhaps that is going a bit too far. . ."]

        if Action_type in dildo_Action_types:
            $ lines.append("The toys again?")
        elif Action_type in ["kiss", "fondle_thighs", "fondle_ass", "hotdog"]:
            $ lines.append("Nothing more than that?")
            $ lines.append("That is all you want?")
            $ lines.append("And that is -all- that you expect?")
        elif Action_type in ["footjob", "titjob"]:
            $ lines.append("You enjoy making use of these?")
        elif Action_type == "masturbation":
            $ lines.append("You only like to watch?")
    elif Girl == JubesX:
        $ lines = ["Hmm, again?"]

        if Action_type in ["kiss", "fondle_thighs", "fondle_ass", "hotdog"]:
            $ lines.append("Nothing more than that?")
        elif Action_type == "masturbation":
            $ lines.append("Nothing more than watching? . .")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label action_forcefully_accepted_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Ok, fine.",
            ". . . Ok, if that's what you want.",
            "Well, there are worst ways to get you off. . .",
            "I suppose, let me get comfortable. . .",
            "Whatever."]
    elif Girl == KittyX:
        $ lines = ["Ok, geeze.",
            "Well, could be worse. . .",
            "Whatever.",
            "Fine. . .",
            "Ok, fine.",
            "Ok, fiiiiine."]
    elif Girl == EmmaX:
        $ lines = ["If you must. . .",
            "If you insist. . .",
            "Very well.",
            "I suppose there are worst ways to get you off. . .",
            "Fine.",
            "Ok, fine.",
            "Fine. . .",
            "Oh, fine, if it will shut you up.",
            "Oh very well.",
            "Ok, fine."]
    elif Girl == LauraX:
        $ lines = ["Going there, huh. . .",
            "If you must. . .",
            "If you insist. . .",
            "Meh. . .",
            "Well, could be worse. . .",
            "Whatever.",
            "Ok, fine.",
            "Ok, sure.",
            "Whatever. . .",
            "Ok, fine. Just make it good.",
            "Whatever."]
    elif Girl == JeanX:
        $ lines = ["Going there, huh. . .",
            "If you must. . .",
            "If you insist. . .",
            "Whatever. . .",
            "Ok, fine.",
            "I can't fault your taste. . .",
            "Fine, let's get this over with.",
            "Ok, sure.",
            "Oh. . . fine. . .",
            "Ok, fine. Just make it good.",
            "Whatever."]
    elif Girl == StormX:
        $ lines = ["If you must. . .",
            "If you insist. . .",
            "Fine, we can do this.",
            "I suppose this would not be too unpleasant. . .",
            "Fine.",
            "Ok, fine.",
            "Oh, fine.",
            "I supose that would be fine.",
            "Oh, very well, if it will satisfy you.",
            "Oh very well.",
            ". . .Fine.",
            "Fine then."]
    elif Girl == JubesX:
        $ lines = ["Going there, huh. . .",
            "If you haveta. . .",
            "If you insist. . .",
            "Meh. . .",
            "Whatevs. . .",
            "Ok, fine."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label action_done_five_times_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I think I've got the hang of this.",
            "We're making a regular habit of this.",
            "This is. . . interesting.",
            "We're really making this a regular thing."]

        if Action_type == "handjob":
            $ lines.append("I think I've got this well in hand.")
        elif Action_type == "footjob":
            $ lines.append("I kinda like this sensation.{p}}Never thought about touching people with my feet.")
    elif Girl == KittyX:
        $ lines = ["Why did we not do this sooner?!",
            "I'm really starting to love this.",
            "I'm surprised how much I enjoy this."]

        if Action_type == "handjob":
            $ lines.append("Let me know any time you need me to give you a hand.")
        elif Action_type == "footjob":
            $ lines.append("Let me know any time you need me to \"foot you up\".")
        elif Action_type == "titjob":
            $ lines.append("Huh, I guess these are good for something.")
        elif Action_type == "blowjob":
            $ lines.append("I'm getting better at this. . . right?")
    elif Girl == EmmaX:
        $ lines = ["Please do call again. . .",
            "I'm enjoying this experience.",
            "We really should have done this sooner.",
            "I can't imagine why I waited so long."]

        if Action_type in cock_actions or Action_type in fondle_Action_types:
            $ lines.append("Best you've had, I'm sure.")

            if Action_type == "titjob":
                $ lines.append("You certainly get a lot of mileage out of these.")
        elif Action_type in active_Action_types:
            $ lines.append("You're pretty good at that.")
    elif Girl == LauraX:
        $ lines = ["I think I've got this down, maybe I should get a punch card.",
            "You seem to enjoy that.",
            "I'm getting used to this. . .",
            "You know, this was a good idea.",
            "I'm glad you're into this."]

        if Action_type in passive_Action_types:
            $ lines.append("I'm really getting the hang of this. . . right?")
    elif Girl == JeanX:
        $ lines = ["Fun, right?",
            "I am loving this. You too, right?",
            "I'm getting used to this. . .",
            "I'm glad we have similar interests. . ."]

        if Action_type in active_Action_types:
            $ lines.append("You're pretty good at this. . .")
        elif Action_type in passive_Action_types:
            $ lines.append("I'm pretty good at this, right?")
    elif Girl == StormX:
        $ lines = ["I have gotten used to these. . .",
            "You do seem to enjoy this.",
            "I expect that you enjoyed that.",
            "I'm enjoying this experience.",
            "I am glad you \"bumped into\" me.",
            "You do certainly make the experience enjoyable."]

        if Action_type in active_Action_types:
            $ lines.append("You are quite skilled at this.")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label switching_action_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Mmm, so what else did you have in mind?"]
    elif Girl == KittyX:
        $ lines = ["Mmm, so what else did you have in mind?",
            "Ok, so what were you thinking?"]
    elif Girl == EmmaX:
        $ lines = ["Very well, what did you want to do?",
            "Mmm, so what else did you have in mind?",
            "Ok then, what were you thinking?"]
    elif Girl == LauraX:
        $ lines = ["Ok, so what did you have in mind?",
            "Mmm, so what else did you have in mind?"]
    elif Girl == JeanX:
        $ lines = ["Mmm, so what else did you have in mind?",
            "Ok, so what did you have in mind?"]
    elif Girl == StormX:
        $ lines = ["Very well, what did you want to do?",
            "Mmm, so what else did you have in mind?",
            "Ok then, what were you thinking?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label before_action_less_than_three_times_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Again?",
            "So you'd like another go?"]

        if Action_type == "handjob":
            $ lines.append("So you'd like another handy?")

        if Action_type == "titjob":
            $ lines.append("So you'd like another titjob?")

        if Action_type == "blowjob":
            $ lines.append("So you'd like another blowjob?")

        if Action_type == "masturbation":
            $ lines.append("You like to watch, huh?")

        if Action_type in ["dildo_pussy", "sex"]:
            $ lines.append("You want to stick it in my pussy again?")

        if Action_type in ["dildo_ass", "anal"]:
            $ lines.append("You want to stick it in my ass again?")
    elif Girl == KittyX:
        $ lines = ["Did you. . . like it last time?",
            "So you'd like another round?"]

        if Action_type == "handjob":
            $ lines.append("Hmm, magic fingers. . .")

        if Action_type == "footjob":
            $ lines.append("Hmm, magic toes. . .")

        if Action_type == "titjob":
            $ lines.append("So you'd like another titjob?")

        if Action_type == "blowjob":
            $ lines.append("So you'd like another blowjob?")

        if Action_type in ["dildo_pussy", "sex"]:
            $ lines.append("You want to stick it in my pussy again?")

        if Action_type in ["dildo_ass", "anal"]:
            $ lines.append("You want to stick it in my ass again?")
    elif Girl == EmmaX:
        $ lines = ["Enjoyed last time?. . .",
            "Oh, very well. . .",
            "Oh? Another round?"]

        if Action_type == "titjob":
            $ lines.append("Hmm, another titjob?")

        if Action_type == "blowjob":
            $ lines.append("Another blowjob?")

        if Action_type == "masturbation":
            $ lines.append("You enjoyed the show?")

        if Action_type in ["dildo_pussy", "sex"]:
            $ lines.append("You want to stick it in my pussy again?")

        if Action_type in ["dildo_ass", "anal"]:
            $ lines.append("You want to stick it in my ass again?")
    elif Girl == LauraX:
        $ lines = ["You seem to like this one. . .",
            "Did you. . . like it last time?",
            "Oh? Another round?"]

        if Action_type == "footjob":
            $ lines.append("Hmm, magic toes. . .")

        if Action_type == "titjob":
            $ lines.append("Another titjob??")

        if Action_type == "blowjob":
            $ lines.append("You'd like another blowjob?")

        if Action_type in ["dildo_pussy", "sex"]:
            $ lines.append("You want to stick it in my pussy again?")

        if Action_type in ["dildo_ass", "anal"]:
            $ lines.append("You want to stick it in my ass again?")
    elif Girl == JeanX:
        $ lines = ["You enjoyed that, huh.",
            "Hmm, it is kinda fun. . .",
            "Oh? Another round?"]

        if Action_type == job_Action_types:
            $ lines.append("I guess you're getting used to these. . .")

        if Action_type == "titjob":
            $ lines.append("Again with the tits, uh?")

        if Action_type == "blowjob":
            $ lines.append("You'd like another blowjob?")

        if Action_type in ["dildo_pussy", "sex"]:
            $ lines.append("You want to stick it in my pussy again?")
    elif Girl == StormX:
        $ lines = ["You enjoyed it last time?. . .",
            "Oh, very well. . .",
            "Oh? Another round?"]

        if Action_type == "titjob":
            $ lines.append("Hmm, another titjob?")

        if Action_type == "blowjob":
            $ lines.append("Another blowjob?")

        if Action_type == "masturbation":
            $ lines.append("You enjoyed the show?")

        if Action_type in ["dildo_pussy", "sex"]:
            $ lines.append("You want to stick it in my pussy again?")

        if Action_type in ["dildo_ass", "anal"]:
            $ lines.append("You want to stick it in my ass again?")
    elif Girl == JubesX:
        $ lines = ["You seem to like this one. . .",
            "Was last time fun?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label anal_insertion_not_loose_not_done_today_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["You could have been a bit more gentle last time, " + Girl.player_petname + "_. . ."]
    elif Girl == KittyX:
        $ lines = ["You could have been a bit more gentle last time, " + Girl.player_petname + "_. . .",
            "That was kind of. . . rough last time?"]
    elif Girl == EmmaX:
        $ lines = ["Perhaps we can work up to that."]
    elif Girl == LauraX:
        $ lines = ["You could have been a bit more gentle last time, " + Girl.player_petname + "_. . .",
            "Maybe eventually. . ."]
    elif Girl == JeanX:
        $ lines = ["Maybe eventually. . ."]
    elif Girl == StormX:
        $ lines = ["Perhaps we could work up to that."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label anal_insertion_not_loose_done_today_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Sorry, I just need a little break back there, " + Girl.player_petname + "_.",
            "I'm still a little sore from earlier, " + Girl.player_petname + "_."]
    elif Girl == KittyX:
        $ lines = ["I'm not really over the last time, but. . .",
            "I'm still a little sore from earlier, " + Girl.player_petname + "_.",
            "I'm still" + Girl.like + "_sore from earlier. . .",
            "Sorry, I just need a little break back there, " + Girl.player_petname + "_.",
            "I'm" + Girl.like + "_a little sore here?"]
    elif Girl == EmmaX:
        $ lines = ["Don't wear me out here."]
    elif Girl == LauraX:
        $ lines = ["I'm still sore from earlier. . .",
            "Sorry, I just need a little break back there, " + Girl.player_petname + "_.",
            "Not right now."]
    elif Girl == JeanX:
        $ lines = ["Not right now."]
    elif Girl == StormX:
        $ lines = ["Do not wear me out here."]
    elif Girl == JubesX:
        $ lines = ["I'm still a little sore from earlier, " + Girl.player_petname + "_."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label hard_cock_lines(Girl, Action_type):
    if Girl == EmmaX:
        $ lines = ["My word " + Girl.player_petname + "_, your member is hard enough to crack diamond. . . and I should know."]
    elif Girl == LauraX:
        $ lines = ["Nice to see you're ready for business. . ."]
    elif Girl == JeanX:
        $ lines = ["I see you won't need any encouragement. . ."]
    elif Girl == StormX:
        $ lines = ["I must say " + Girl.player_petname + "_, you certainly do seem to be. . . excited."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label first_time_asking_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = []

        if Action_type == "masturbation":
            $ lines.append("You want me to get myself off, while you watch?")
        elif Action_type == "handjob":
            $ lines.append("You want me to rub your cock, with my hand?")
        elif Action_type == "footjob":
            $ lines.append("Huh, so like a handy, but with my feet?")
        elif Action_type == "titjob":
            $ lines.append("You want me to rub your cock with my breasts?")
        elif Action_type == "blowjob":
            $ lines.append("You want me to put your dick. . . in my mouth?")
        elif Action_type in dildo_Action_types:
            $ lines.append("Hmmm, so you'd like to try out some toys?")
        elif Action_type == "sex":
            $ lines.append("So, you'd like to take this to the next level? Actual sex? . . .")
        elif Action_type == "anal":
            $ lines.append("Wait, so you want to stick it in my butt?!")
        elif Action_type == "hotdog":
            $ lines.append("Wait, so you want to grind against my butt?!")
    elif Girl == KittyX:
        $ lines = ["I haven't really had much experience with this. . . "]

        if Action_type == "masturbation":
            $ lines.append("You want me to. . . touch myself?{p}And you're going to . . .watch?")
        elif Action_type == "handjob":
            $ lines.append("So you want a handy then?")
        elif Action_type == "footjob":
            $ lines.append("Huh, so you'd like me to touch your cock with my feet?")
        elif Action_type == "titjob":
            $ lines.append("You want to rub your cock against my. . . breasts?")
        elif Action_type == "blowjob":
            $ lines.append("You want me to suck your dick?")
        elif Action_type in dildo_Action_types:
            $ lines.append("Hmmm, so you'd like to try out some toys?")
        elif Action_type == "anal":
            $ lines.append("You want to go in the \"out\" door?!")
        elif Action_type == "hotdog":
            $ lines.append("So, just grinding against me?")

        if Action_type in [dildo_Action_types, "sex", "anal"]:
            $ lines.append("You want to try and fit that. . .?")
    elif Girl == EmmaX:
        $ lines = ["Hmm, are you sure you can handle that, " + Girl.player_petname + "_?",
            "Hmm, are you sure you're really prepared for this? . . ",
            "Hmm, you don't take half measures. . ."]

        if Action_type == "masturbation":
            $ lines.append("So you enjoy a good show then. . .")
        elif Action_type == "footjob":
            $ lines.append("Mmm, so you're into feet then, " + Girl.player_petname + "_?")
        elif Action_type == "blowjob":
            $ lines.append("So you'd like me to suck you off?")
        elif Action_type in dildo_Action_types:
            $ lines.append("Hmmm, so you'd like to try out some toys?")
        elif Action_type == "anal":
            $ lines.append("Oooh, naughty boy. Anal?")
        elif Action_type == "hotdog":
            $ lines.append("You just want me to grind against you then?")

        if Action_type in passive_Action_types:
            $ lines.append("You'd like me to take care of that for you?")
    elif Girl == LauraX:
        $ lines = []

        if Action_type == "masturbation":
            $ lines.append("So you want me to masturbate while you watch?")
        elif Action_type == "handjob":
            $ lines.append("Handjob, huh. . .")
        elif Action_type == "footjob":
            $ lines.append("Standard footjob?")
        elif Action_type == "titjob":
            $ lines.append("You want a titjob, huh?")
        elif Action_type == "blowjob":
            $ lines.append("You want me to suck your cock?")
        elif Action_type in dildo_Action_types:
            $ lines.append("Hmmm, so you'd like to try out some toys?")
        elif Action_type == "sex":
            $ lines.append("Huh, you wanna fuck me? . . ")
        elif Action_type == "anal":
            $ lines.append("Huh, anal?")
        elif Action_type == "hotdog":
            $ lines.append("What, just grinding?")

        if Action_type in [dildo_Action_types, "sex", "anal"]:
            $ lines.append("You want to try and fit that. . .?")
    elif Girl == JeanX:
        $ lines = ["I can't blame you. . ."]

        if Action_type == "masturbation":
            $ lines.append("Oh, so you want to watch while I get off?")
        elif Action_type == "handjob":
            $ lines.append("You want a handjob, hmm. . .")
        elif Action_type == "footjob":
            $ lines.apppend("Oh, a foot person, eh?")
        elif Action_type == "titjob":
            $ lines.append("Oh, you want me to put these to work. . .")
        elif Action_type == "blowjob":
            $ lines.append("Oh! You want me to suck you off?")
        elif Action_type in dildo_Action_types:
            $ lines.append("Hmmm, so you'd like to try out some toys?")
        elif Action_type == "sex":
            $ lines.append("Oh, you wanna fuck . . ")
        elif Action_type == "anal":
            $ lines.append("Oh, you're into anal?")
        elif Action_type == "hotdog":
            $ lines.append("What, just grinding?")
    elif Girl == StormX:
        $ lines = ["Hmm, are you certain you are prepared for this? . . ",
            "Hmm, you don't take half measures. . ."]

        if Action_type == "masturbation":
            $ lines.append("Oh, so you like the watch? . .")
        elif Action_type == "handjob":
            $ lines.append("You would like me to jerk you off?")
        elif Action_type == "footjob":
            $ lines.append("Oh, you would like me to use my feet, " + Girl.player_petname + "_?")
        elif Action_type == "blowjob":
            $ lines.append("You would like me to suck on your penis?")
        elif Action_type in dildo_Action_types:
            $ lines.append("Hmmm, so you'd like to try out some toys?")
        elif Action_type == "anal":
            $ lines.append("I am shocked! Anal?")
        elif Action_type == "hotdog":
            $ lines.append("You would just like to press against each other like this?")

        if Action_type in breast_Action_types:
            $ lines.append("My breasts are really appealing to you, " + Girl.player_petname + "_?")
    elif Girl == JubesX:
        $ lines = []

        if Action_type == "masturbation":
            $ lines.append("So you like watching me masturbate?")
        elif Action_type == "handjob":
            $ lines.append("Handjob, huh. . .")

    if len(lines) > 0:
        $ line = renpy.random.choice(lines)

        Girl.voice "[line]"

    return

label first_time_forcing_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I suppose there are worst things you could ask for.",
            "Seriously?"]

        if Action_type in anal_insertion_Action_types:
            $ lines.append("You had to go for the butt, uh?")

        if Action_type in ["sex", "anal"]:
            $ lines.append("You'd really take it that far?")

        if Action_type in ["kiss", "fondle_thighs", "fondle_ass", "hotdog"]:
            $ lines.append(". . . That's all?")
    elif Girl == KittyX:
        $ lines = ["I suppose there are worst things you could ask for."]

        if Action_type in ass_Action_types:
            $ lines.append("Always about the butt, huh?")

        if Action_type in ["sex", "anal"]:
            $ lines.append("You'd really do this when you have me over a barrel?")

        if Action_type in ["kiss", "fondle_thighs", "fondle_ass", "hotdog"]:
            $ lines.append(". . . That's it?")

        if Action_type == "anal":
            $ lines.append("Anal? Really?")
    elif Girl == EmmaX:
        $ lines = ["I suppose there are worst things you could ask for."]

        if Action_type in ass_Action_types:
            $ lines.append("They always go for the butt. . .")

        if Action_type in ["sex", "anal"]:
            $ lines.append("Are you sure this is how you'd like to use your power?")

        if Action_type in ["kiss", "fondle_thighs", "fondle_ass", "hotdog"]:
            $ lines.append(". . . nothing more than that?")

        if Action_type == "anal":
            $ lines.append("Anal? That's your goto?")
    elif Girl == LauraX:
        $ lines = ["I suppose there are worst things you could ask for."]

        if Action_type in ass_Action_types:
            $ lines.append("Always about the butt, huh?")

        if Action_type in ["kiss", "fondle_thighs", "fondle_ass", "hotdog"]:
            $ lines.append(". . . nothing more?")

        if Action_type == "anal":
            $ lines.append("Anal? That's what you're pushing for?")
    elif Girl == JeanX:
        $ lines = ["That's the card you're going to play?",
            "I suppose there are worst things you could ask for."]

        if Action_type in ["sex", "anal"]:
            $ lines.append("Pretty bold of you. . .")

        if Action_type in ["kiss", "fondle_thighs", "fondle_ass", "hotdog"]:
            $ lines.append(". . . nothing more?{p}Which of us has a pussy here?")
    elif Girl == StormX:
        $ lines = ["This is what you would have me do?",
            "I suppose there are worst things you could ask for."]

        if Action_type in ass_Action_types:
            $ lines.append("They always go for the butt. . .")

        if Action_type in ["kiss", "fondle_thighs", "fondle_ass", "hotdog"]:
            $ lines.append(". . . and no more than that?")

        if Action_type == "anal":
            $ lines.append("Oh. Of course it would be anal.")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label mouth_not_enough(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["My mouth wasn't enough?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label what_do_you_think_youre_doing_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Hey, what do you think you're doing back there?!",
            "Hmm, kinda rude, " + Girl.player_petname + "_."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label hand_not_enough(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["My hand wasn't enough?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label achievement_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I. . . really think I enjoy this. . ."
            "I'm really starting to enjoy this.",
            "I think I'm getting addicted to this.",
            "I. . . really think I enjoy this. . ."]

        if Action_type == "handjob":
            $ lines.append("I guess you can call me \"Handi-Queen\".")
        elif Action_type == "footjob":
            $ lines.append("I guess I've gotten used to this foot thing.")
    elif Girl == KittyX:
        $ lines = ["I just can't seem to quit you.",
            "I didn't think I'd love this so much!",
            "I. . . liked that a lot."]

        if Action_type == "handjob":
            $ lines.append("I've kinda become" + Girl.like + "_a \"Handi-Queen\" or something.")
        elif Action_type == "footjob":
            $ lines.append("I guess I've gotten pretty smooth at the \"Kittypedi\".")
        elif Action_type == "blowjob":
            $ lines.append("I can't" + Girl.like + "_get your taste out of my mind.")
    elif Girl == EmmaX:
        $ lines = ["I seem to fit you like a glove. . .",
            "You're one of the better partners I've had at that.",
            "That was. . . pleasant."]

        if Action_type == "handjob":
            $ lines.append("I've apparently become the \"queen\" of handjobs as well.")
        elif Action_type == "footjob":
            $ lines.append("I'm glad that you enjoy my feet.")
        elif Action_type == "blowjob":
            $ lines.append("You taste positively intoxicating, " + Girl.player_petname + "_.")
        elif Action_type == "titjob":
            $ lines.append("They've been trained well over the years.")
    elif Girl == LauraX:
        $ lines = ["Looks like you filled out the punch card, " + Girl.player_petname + "_.",
            "I think I'm finally back into practice on this.",
            "We're making this a regular thing, huh. . .",
            "I think you've got a knack for that.",
            "That was. . . nice."]

        if Action_type == "blowjob":
            $ lines.append("Your flavor is intoxicating.")
    elif Girl == JeanX:
        $ lines = ["This seems to be all we do lately. . .",
            "Wow, you know. . . I don't always love this. . . but I guess with you it's different somehow. . .",
            "Hmm, this is kinda fun. . .",
            "Hey, I just noticed we've been doing this a lot. . .",
            "This has been fun exercise.",
            "Ok, that was. . . fine."]
    elif Girl == StormX:
        $ lines = ["I am glad that you convinced me to try this.",
            "It feels so. . . intimate.",
            "We do go well together. . .",
            "I have certainly come to enjoy this.",
            "That was. . . enjoyable."]

        if Action_type == "handjob":
            $ lines.append("I seem to have become the \"queen\" of good handjobs.")
        elif Action_type == "blowjob":
            $ lines.append("I cannot imagine how I went this long without such a delicacy, " + Girl.player_petname + "_.")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label convinced_after_saying_no_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I guess if it'll get you off. . .",
            "Fine!",
            "Hmm, I suppose. . .",
            "Oh, I suppose it isn't so bad. . .",
            "Ok, you've won me over on this one. . .",
            "Ok, ok, I have been itching for this. . .",
            "Well, I guess it's not so bad. . ."]
    elif Girl == KittyX:
        $ lines = ["Hmm, I guess. . .",
            "Ok, fine, I suppose it isn't {i}sooo{/i} bad. . .",
            "OK, geeze!",
            "You've made your case. . .",
            "Well, ok, I've given it some thought, fine. . .",
            "Well, I guess it's not so bad. . ."]
    elif Girl == EmmaX:
        $ lines = ["Oh, fine!",
            "Oh, very well then. . .",
            "Fine, I suppose you've earned it. . .",
            "Oh, very well.",
            "Very well, you've convinced me. . .",
            "After some consideration. . .",
            "It might be entertaining.",
            "It was rather entertaining. . ."]
    elif Girl == LauraX:
        $ lines = ["If it'll get you off my back. . .",
            "Hmm, I guess. . .",
            "Fine. . .",
            "Fine.",
            "Ok, whatever. . .",
            "Well, if you're going to keep asking. . .",
            "Might be fun. . .",
            "It was rather entertaining. . ."]
    elif Girl == JeanX:
        $ lines = ["Oh, -fine-. . .",
            "Hmm, I guess. . .",
            "Fine. . .",
            "Fine.",
            "Ok, whatever. . .",
            "Well, if you're going to keep asking. . .",
            "Might be fun. . .",
            "It was fun enough. . ."]
    elif Girl == StormX:
        $ lines = ["Oh, very well. . .",
            "Very well then. . .",
            "Fine, I suppose you have earned it. . .",
            "Oh, very well.",
            "Very well, I am convinced. . .",
            "After some consideration. . .",
            "It might entertain me.",
            "It was rather entertaining. . ."]
    elif Girl == JubesX:
        $ lines = ["If it'll get you off my back. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label accepted_without_question_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Well. . . ok.",
            "Sure, I guess.",
            "Sure!",
            "Heh, ok, alright.",
            "Okay.",
            "Hells yeah.",
            "I guess. . .",
            "Fine. . . [She gestures for you to come over].",
            "Heh, ok, ok.",
            "Well. . . ok.",
            "I suppose it would help to have something nice to look at. . .",
            "I've kind of needed this anyways. . .",
            "Sure!",
            "I guess I could. . . give it a go.",
            "Heh, ok, ok."]

        if Action_type == "titjob":
            $ lines.append("Fine. . . [She drools a bit into her cleavage].")
        elif Action_type == "blowjob":
            $ lines.append("Fine. . . [She licks her lips].")
            $ lines.append("Well, sure, ahhhhhh.")
            $ lines.append("Yum.")
        elif Action_type in ["sex", "anal"]:
            $ lines.append("Well, sure, stick it in.")
        elif Action_type in hand_Action_types:
            $ lines.append("Well, sure, give it a rub.")
        elif Action_type in dildo_Action_types:
            $ lines.append("Well, sure, stick it in.")
            $ lines.append("I guess I could. . . stick it in.")
        elif Action_type in cock_Action_types:
            $ lines.append("I guess I could. . . whip it out.")
            $ lines.append("Ok, lemme see it.")
            $ lines.append("I suppose, drop trou.")
            $ lines.append("Sure, whip it out.")
            $ lines.append("Well, sure, put'im here.")
    elif Girl == KittyX:
        $ lines = ["Sure, I guess.",
            "Ooooookay    .",
            "Ok. . . [She gestures for you to come over].",
            "Heh, ok, ok.",
            "Well. . . ok.",
            "Heh, ok.",
            "Sure!",
            "Um, yeah.",
            "Hells yeah.",
            "I guess we could do that.",
            "Ooooookay.",
            "Lol, ok, alright.",
            "Huh. Ok.",
            "Couldn't hurt having you around. . .",
            "Two birds with one stone. . .",
            "K.",
            "Sure, why not?",
            "Lol, ok."]

        if Action_type == "titjob":
            $ lines.append("Fine. . . [She drools a bit into her cleavage].")
        elif Action_type == "blowjob":
            $ lines.append("Yum.")
            $ lines.append("Ok. . . [She licks her lips].")
            $ lines.append("Well, sure, ahhhhhh.")
        elif Action_type in ["sex", "anal"]:
            $ lines.append("Well, sure, stick it in.")
        elif Action_type in hand_Action_types:
            $ lines.append("Well, sure, give it a rub.")
        elif Action_type in active_Action_types:
            $ lines.append("You could, I guess.")
        elif Action_type in passive_Action_types:
            $ lines.append("I guess I could. . .")
        elif Action_type in dildo_Action_types:
            $ lines.append("I guess I could. . . stick it in.")
            $ lines.append("Well, sure, stick it in.")
        elif Action_type in cock_Action_types:
            $ lines.append("Cool, lemme see it.")
            $ lines.append("Well, sure, put it here.")
            $ lines.append("Sure, whip it out.")
    elif Girl == EmmaX:
        $ lines = ["Oh, I suppose.",
            "Fine. . . [She gestures for you to come over].",
            "Ok, ok.",
            "Well, sure, come over here.",
            "Oh, very well.",
            "Mmmmm.",
            "Fine, whip it out.",
            "Fine. . . [She drools a bit into her cleavage].",
            "Oh, all right.",
            "Well, ok.",
            "Well. . . ok.",
            "Mmmm.",
            "Sure, let me have it.",
            "Mmmm. . . [She licks her lips].",
            "Ok, fine.",
            "Well, sure, stick it in.",
            "Hmm. . . ok.",
            "Sure!",
            "I guess I could. . . stick it in.",
            "Delightful.",
            "Hmm, ok, ok.",
            "Sure, I suppose.",
            "Fine.",
            "Very well, bring it out.",
            "I suppose I could. . .",
            "Fine. . . [She gestures for you to come over].",
            "Hmm, ok.",
            "Well. . . fine, I accept.",
            "Sure!",
            "We could, I suppose.",
            "Hmmm, yes.",
            "How could I refuse?",
            "You could, I guess.",
            "Um, yeah.",
            "Well, sure, let me give it a rub.",
            "Very well.",
            "Nice!",
            "I suppose we could do that.",
            "Allow me. . .",
            "Heh, ok, ok.",
            "Ok.",
            "It couldn't hurt having you around. . .",
            "Very well.",
            "Sure, why not?",
            "[chuckles]. . . ok."]

        if Action_type in passive_Action_types:
            $ lines.append("I suppose I could. . .")
            $ lines.append("I'll do it.")

        if Action_type in cock_Action_types:
            $ lines.append("Well, give it here.")
    elif Girl == LauraX:
        $ lines = ["Sure, I guess.",
            "O-kay.",
            "Fine.",
            "Ok. . . [She gestures for you to come over].",
            "Ok, ok.",
            "Well, sure, put it here.",
            "Well. . . ok.",
            "Yum.",
            "Sure, whip it out.",
            "Fine. . . [She drools a bit into her cleavage].",
            "Heh, ok.",
            "Sure. Ahhhhhh.",
            "Well. . . alright.",
            "Ok. . . [She licks her lips].",
            "Alright, let's see it.",
            "Well. . . ok.",
            "Sure!",
            "I guess I could. . . stick it in.",
            "Hells yeah.",
            "Well, sure, stick it in.",
            "Well. . . ok.",
            "Sure, I guess.",
            "OK.",
            "Fine, lemme see it.",
            "I guess I could. . .",
            "Ok. . . [She gestures for you to come over].",
            "Well. . . fine, let's do it.",
            "Sure.",
            "We could, I guess.",
            "Hmmm, sure.",
            "Sounds fun.",
            "Well. . . ok.",
            "Sure.",
            "You could, I guess.",
            "Um, yeah.",
            "Well, sure, let me give it a rub.",
            "Very well.",
            "Nice!",
            "I guess we could do that.",
            "Ok, let me. . .",
            "Heh, ok, ok.",
            "Huh. Ok.",
            "Couldn't hurt. . .",
            "Alright.",
            "Sure.",
            "Heh, ok."]

        if Action_type in passive_Action_types:
            $ lines.append("I suppose I could. . .")
    elif Girl == JeanX:
        $ lines = ["Sure, I guess.",
            "Okay. . .   ",
            "Fine.",
            "Ok. . . Get over here. . .",
            "Ok, ok.",
            "Well, sure, put it here.",
            "Well. . . ok.",
            "Heh, ok.",
            "Sure. Ahhhhhh.",
            "Well. . . alright.",
            "Yum.",
            "Sure, whip it out.",
            "Ok. . . [She licks her lips].",
            "Alright, let's see it.",
            "Well, sure, stick it in.",
            "Sure!",
            "I guess I could. . . stick it in.",
            "Hells yeah.",
            "Sure, I guess.",
            "OK.",
            "Fine, lemme see it.",
            "I guess I could. . .",
            "Ok. . . [She gestures for you to come over].",
            "Well. . . fine, let's do it.",
            "We could, I guess.",
            "Hmmm, sure.",
            "Sounds fun.",
            "Well. . . ok.",
            "Sure.",
            "You could, I guess.",
            "Um, yeah.",
            "Well, sure, let me give it a rub.",
            "Very well.",
            "Nice!",
            "I guess we could do that.",
            "Ok, let me. . .",
            "Heh, ok, ok.",
            "Sure. Ok.",
            "Couldn't hurt. . .",
            "Alright.",
            "Sure.",
            "Sure, why not. . ."]

        if Action_type in passive_Action_types:
            $ lines.append("I suppose I could. . .")
    elif Girl == StormX:
        $ lines = ["Oh, I suppose we might.",
            ". . . Fine. [She gestures for you to come over]",
            "Ok, ok.",
            "Fine, come over here.",
            "Oh, very well.",
            "Mmmmm.",
            "Fine, show me.",
            "Fine. . . [She drools a bit into her cleavage].",
            "Oh, all right.",
            ". . . ok.",
            "Well. . . ok.",
            "Mmmm.",
            "Sure, let me have it.",
            "Mmmm. . . [She licks her lips].",
            "Ok, fine.",
            "Well, sure, stick it in.",
            "Sure!",
            "I guess I could. . . stick it in.",
            "Delightful.",
            "Hmm, ok, ok.",
            "Hmm, I suppose.",
            "Fine.",
            "Very well, bring it out.",
            "I suppose that I could. . .",
            "Fine. . . [She gestures for you to come over].",
            "Hmm, ok.",
            "Well. . . fine, I accept.",
            "Of course!",
            "We could, I suppose.",
            "Hmmm, yes.",
            "How could I refuse?",
            "Well. . . I suppose.",
            "Hmm, yes. Fine.",
            "Heh. Ok, ok.",
            "Very well then, let me give it a rub.",
            "Very well.",
            "I suppose that we could do that.",
            "Allow me. . .",
            "Fine.",
            "It could not hurt having you around. . .",
            "Very well.",
            "Sure, why not?",
            "[chuckles]. . . Fine."]

        if Action_type in passive_Action_types:
            $ lines.append("I would do this.")
            $ lines.append("I suppose that I could. . .")

        if Action_type in cock_Action_types:
            $ lines.append("Very well, give it here.")
    elif Girl == JubesX:
        $ lines = ["Sure, I guess.",
            "O-kay.",
            "Fine.",
            "Ok. . . [She gestures for you to come over].",
            "Ok, ok.",
            "Huh. Ok.",
            "Couldn't hurt. . .",
            "Alright.",
            "Sure.",
            "Heh, ok."]

        if Action_type in passive_Action_types:
            $ lines.append("I suppose I could. . .")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label excited_for_first_kiss_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I've never really been able to do this, so I'm a bit excited to try. . ."]
    elif Girl == KittyX:
        $ lines = ["You are kinda cute. . ."]
    elif Girl == EmmaX:
        $ lines = ["Well, I suppose it couldn't hurt. . ."]
    elif Girl == LauraX:
        $ lines = ["Worth a shot. . ."]
    elif Girl == JeanX:
        $ lines = ["Why not?"]
    elif Girl == StormX:
        $ lines = ["I would like that."]
    elif Girl == JubesX:
        $ lines = ["I guess we did get off to a poor start. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label less_excited_for_first_kiss_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I guess it's worth a shot. . ."]
    elif Girl == KittyX:
        $ lines = ["I'll give it a go. . ."]
    elif Girl == EmmaX:
        $ lines = ["We could. . ."]
    elif Girl == LauraX:
        $ lines = ["If you insist. . ."]
    elif Girl == JeanX:
        $ lines = ["I mean, whatever. . ."]
    elif Girl == StormX:
        $ lines = ["I suppose."]
    elif Girl == JubesX:
        $ lines = ["I suppose we could. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label excited_for_kiss_love_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Sure, why not?"]
    elif Girl == KittyX:
        $ lines = ["Smooches!"]
    elif Girl == EmmaX:
        $ lines = ["Mwa."]
    elif Girl == LauraX:
        $ lines = ["Mmmmm. . ."]
    elif Girl == JeanX:
        $ lines = ["MmMmmmm. . ."]
    elif Girl == StormX:
        $ lines = ["Hrm. . ."]
    elif Girl == JubesX:
        $ lines = ["Mmmm. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label excited_for_kiss_obedience_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["If you wish."]
    elif Girl == KittyX:
        $ lines = ["Sure, ok."]
    elif Girl == EmmaX:
        $ lines = ["Of course."]
    elif Girl == LauraX:
        $ lines = ["If you want."]
    elif Girl == JeanX:
        $ lines = ["Ok. . ."]
    elif Girl == StormX:
        $ lines = ["Very well. . ."]
    elif Girl == JubesX:
        $ lines = ["Sure. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label kiss_addicted_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Hm. . . ok, let's do this."]
    elif Girl == KittyX:
        $ lines = ["I kinda have to."]
    elif Girl == EmmaX:
        $ lines = [". . . yes."]
    elif Girl == LauraX:
        $ lines = ["I have to."]
    elif Girl == JeanX:
        $ lines = ["Um. . . yeah. . ."]
    elif Girl == StormX:
        $ lines = [". . . yes. . ."]
    elif Girl == JubesX:
        $ lines = ["Oh yes. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label kiss_accepted_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Hmm, ok."]
    elif Girl == KittyX:
        $ lines = ["Yeah, whatever."]
    elif Girl == EmmaX:
        $ lines = ["Very well."]
    elif Girl == LauraX:
        $ lines = ["Sure."]
    elif Girl == JeanX:
        $ lines = ["Whatever. . ."]
    elif Girl == StormX:
        $ lines = ["Fine."]
    elif Girl == JubesX:
        $ lines = ["Sure, ok. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label lend_some_helping_hands_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Well, " + Girl.player_petname + "_, I suppose I could use some help with these. . .",
            "Well, " + Girl.player_petname + "_, I suppose you could help me with these. . ."]
    elif Girl == KittyX:
        $ lines = ["Um, you know, maybe start up top?",
            "I'd" + Girl.like + "_love it if you could give me a hand. . ."]
    elif Girl == EmmaX:
        $ lines = ["Hm, well I do have my hands full with these. . .",
            "I suppose I could use some added attention. . ."]
    elif Girl == LauraX:
        $ lines = ["Huh. Well I guess you could work the top?",
            "Yeah, I guess? . ."]
    elif Girl == JeanX:
        $ lines = ["Hmm, ok, give these a squeeze. . .",
            "Ok, sure. . ."]
    elif Girl == StormX:
        $ lines = ["You could give me a breast massage. . ."]
    elif Girl == JubesX:
        $ lines = ["Well, ok, gimme a hand with these?",
            "Cool. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label why_dont_we_take_care_of_each_other_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Well what did you have in mind?"]
    elif Girl == KittyX:
        $ lines = ["I think I could help with that. . ."]
    elif Girl == EmmaX:
        $ lines = ["I suppose I could spare some attention. . ."]
    elif Girl == LauraX:
        $ lines = ["Like what?"]
    elif Girl == JeanX:
        $ lines = ["Like what?"]
    elif Girl == StormX:
        $ lines = ["Oh, what did you have in mind?"]
    elif Girl == JubesX:
        $ lines = ["Like what?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label well_in_hand_lust_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Well, " + Girl.player_petname + "_, I suppose I do at that . ."]
    elif Girl == KittyX:
        $ lines = ["Well {i}I{/i} think so. . ."]
    elif Girl == EmmaX:
        $ lines = ["So you prefer to watch. . ."]
    elif Girl == LauraX:
        $ lines = ["I am getting pretty close. . ."]
    elif Girl == JeanX:
        $ lines = ["I'm getting there. . ."]
    elif Girl == StormX:
        $ lines = ["I see you prefer to watch. . ."]
    elif Girl == JubesX:
        $ lines = ["Sure, just gimme a sec. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label well_in_hand_approved_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Well I did, but I think I've got it taken care of for now. . ."]
    elif Girl == KittyX:
        $ lines = ["Yeah. . . but I think I'm kinda done. . ."]
    elif Girl == EmmaX:
        $ lines = ["I did, but I wasn't intending perfomance art."]
    elif Girl == LauraX:
        $ lines = ["Yeah. . . but I can take a break. . ."]
    elif Girl == JeanX:
        $ lines = ["Yeah. . . but I can take a break. . ."]
    elif Girl == StormX:
        $ lines = ["True, but I was not expecting an audience."]
    elif Girl == JubesX:
        $ lines = ["Yeah. . . but I could take a break. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label well_in_hand_disapproved_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Well I did, but now you've blown the mood."]
    elif Girl == KittyX:
        $ lines = ["Hrmph, yeah, I kinda {i}did.{/i}"]
    elif Girl == EmmaX:
        $ lines = ["I did, but now the mood is ruined. . ."]
    elif Girl == LauraX:
        $ lines = ["-until you messed it up."]
    elif Girl == JeanX:
        $ lines = ["-well I -was.-"]
    elif Girl == StormX:
        $ lines = ["Well, I had, before you interrupted. . ."]
    elif Girl == JubesX:
        $ lines = ["Well I -did.-"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label what_did_you_come_over_for_approval_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["So what did you come over for anyway, " + Girl.player_petname + "_?"]
    elif Girl == KittyX:
        $ lines = ["So what are you" + Girl.like + "_even doing here?"]
    elif Girl == EmmaX:
        $ lines = ["Why are you even in my room?"]
    elif Girl == LauraX:
        $ lines = ["Why are you in my room?"]
    elif Girl == JeanX:
        $ lines = ["Why are you in my room?"]
    elif Girl == StormX:
        $ lines = ["What brought you here?"]
    elif Girl == JubesX:
        $ lines = ["So, what're you doing here?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label fancy_bumping_into_you_approval_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["So . . . fancy bumping into you here, " + Girl.player_petname + "_. . ."]
    elif Girl == KittyX:
        $ lines = ["I" + Girl.like + "_didn't expect to see you here. . ."]
    elif Girl == EmmaX:
        $ lines = ["I wasn't expecting visitors. . ."]
    elif Girl == LauraX:
        $ lines = ["I wasn't expecting company. . ."]
    elif Girl == JeanX:
        $ lines = ["I didn't call for anyone. . ."]
    elif Girl == StormX:
        $ lines = ["I did not expect interruptions. . ."]
    elif Girl == JubesX:
        $ lines = ["I didn't think anyone would be dropping by. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label what_did_you_come_over_for_disapproval_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Well if you don't mind, I'd kind of appreciate you getting out of here. Maybe knock next time?"]
    elif Girl == KittyX:
        $ lines = ["So in case you couldn't tell, I was a little {i}busy?{/i} Maybe knock sometime?"]
    elif Girl == EmmaX:
        $ lines = ["You may have noticed, I had some work to take care of, so if you'll leave me to it. . ."]
    elif Girl == LauraX:
        $ lines = ["I was kinda busy, so get out."]
    elif Girl == JeanX:
        $ lines = ["I was busy, so get out."]
    elif Girl == StormX:
        $ lines = ["I am afraid that I do not have time to deal with you right now. . ."]
    elif Girl == JubesX:
        $ lines = ["I was taking care of something, bye."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    "[Girl.name] kicks you out of her room."

    return

label fancy_bumping_into_you_disapproval_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Well if you don't mind, I'm getting out of here. Maybe knock next time?"]
    elif Girl == KittyX:
        $ lines = ["So. . . I'm getting out of here? Maybe knock sometime?"]
    elif Girl == EmmaX:
        $ lines = ["I think I'll be leaving, if you don't mind."]
    elif Girl == LauraX:
        $ lines = ["I'm getting out of here, but maybe knock next time."]
    elif Girl == JeanX:
        $ lines = ["I'm leaving, but maybe knock next time?"]
    elif Girl == StormX:
        $ lines = ["I will be leaving now, if you do not mind."]
    elif Girl == JubesX:
        $ lines = ["Ugh, I've got to get going anyway."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label masturbation_join_in_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Yeah, did you want something, " + Girl.player_petname + "_?"]
    elif Girl == KittyX:
        $ lines = ["Like what you see?"]
    elif Girl == EmmaX:
        $ lines = ["Enjoying the show?"]
    elif Girl == LauraX:
        $ lines = ["Are you enjoying this?"]
    elif Girl == JeanX:
        $ lines = ["Like what you see?"]
    elif Girl == StormX:
        $ lines = ["Enjoying yourself?"]
    elif Girl == JubesX:
        $ lines = ["Oh, are you having fun?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label masturbation_excellent_show_cock_out(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Well, I imagine it was. . ."]
    elif Girl == KittyX:
        $ lines = ["Um, I mean. . . yeah. . ."]
    elif Girl == EmmaX:
        $ lines = ["Well, obviously. . ."]
    elif Girl == LauraX:
        $ lines = ["Really? Weird. . ."]
    elif Girl == JeanX:
        $ lines = ["True. . ."]
    elif Girl == StormX:
        $ lines = ["I imagine it was. . ."]
    elif Girl == JubesX:
        $ lines = ["Oh. . . um. . .thanks?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label masturbation_excellent_show_cock_out_happy_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["And the view from this angle ain't so bad either. . ."]
    elif Girl == KittyX:
        $ lines = ["I um. . . like what I'm seeing too. . ."]
    elif Girl == EmmaX:
        $ lines = ["And I suppose you bring a lot to the table as well, don't you. . ."]
    elif Girl == LauraX:
        $ lines = ["I um. . . you're not so bad yourself. . ."]
    elif Girl == JeanX:
        $ lines = ["And you can put on quite a show yourself. . ."]
    elif Girl == StormX:
        $ lines = ["And I have been missing a show myself. . ."]
    elif Girl == JubesX:
        $ lines = ["I, um. . . you're not so bad yourself. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label masturbation_just_got_here_cock_out_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["A likely story . . ."]
    elif Girl == KittyX:
        $ lines = ["Long enough to whip that out?"]
    elif Girl == EmmaX:
        $ Girl.eyes = "squint"

        $ lines = ["Long enough to raise your sails?"]
    elif Girl == LauraX:
        $ lines = ["Long enough to whip that out?"]
    elif Girl == JeanX:
        $ lines = ["A likely story. . ."]
    elif Girl == StormX:
        $ lines = ["Long enough, it would appear. . ."]
    elif Girl == JubesX:
        $ lines = ["Not by the looks of that thing."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label masturbation_just_got_here_cock_out_happy_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Still, can't blame a fella for take'in inspirations."]
    elif Girl == KittyX:
        $ lines = ["I, um, guess I should be flattered?"]
    elif Girl == EmmaX:
        $ lines = ["I suppose you couldn't help yourself under the circumstances. . ."]
    elif Girl == LauraX:
        $ lines = ["It was really that interesting?"]
    elif Girl == JeanX:
        $ lines = ["I guess I can't blame you. . ."]
    elif Girl == StormX:
        $ lines = ["I expect that you could not contain your enthusiasm. . ."]
    elif Girl == JubesX:
        $ lines = ["I guess I made an impression?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label masturbation_watching_for_long_enough_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Well I hope you got a good show out of it. . ."]
    elif Girl == KittyX:
        $ lines = ["I hope I kept you entertained. . ."]
    elif Girl == EmmaX:
        $ lines = ["Enjoying the show?"]
    elif Girl == LauraX:
        $ lines = ["I must have put on a show. . ."]
    elif Girl == JeanX:
        $ lines = ["Nice of you to let me know. . ."]
    elif Girl == StormX:
        $ lines = ["And I assume you enjoyed the show?"]
    elif Girl == JubesX:
        $ lines = ["I guess it must have been interesting. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label masturbation_just_got_here_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["A likely story . . ."]
    elif Girl == KittyX:
        $ lines = ["Yeah, I just bet. . ."]
    elif Girl == EmmaX:
        $ lines = ["Yes, I'm sure. . ."]
    elif Girl == LauraX:
        $ lines = ["Uh-huh. . ."]
    elif Girl == JeanX:
        $ lines = ["Uh-huh. . ."]
    elif Girl == StormX:
        $ lines = ["That seems likely. . ."]
    elif Girl == JubesX:
        $ lines = ["Suuuure. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label masturbation_keep_going_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Well, alright. . ."]
    elif Girl == KittyX:
        $ lines = ["Sure. . ."]
    elif Girl == EmmaX:
        $ lines = ["I suppose. . ."]
    elif Girl == LauraX:
        $ lines = ["Ok. . ."]
    elif Girl == JeanX:
        $ lines = ["Ok. . ."]
    elif Girl == StormX:
        $ lines = ["I could. . ."]
    elif Girl == JubesX:
        $ lines = ["Ok. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label masturbation_worn_out_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["I need to take a little break here, " + Girl.player_petname + "_.",
            "I'm kinda worn out, maybe time for a break. . ."]
    elif Girl == KittyX:
        $ lines = ["Gimme a minute, I need to collect myself here. . ."]
    elif Girl == EmmaX:
        $ lines = ["Allow me to collect myself. . .",
            "Gimme a minute, I need to collect myself here. . ."]
    elif Girl == LauraX:
        $ lines = ["I need a minute here. . ."]
    elif Girl == JeanX:
        $ lines = ["I need a minute here. . ."]
    elif Girl == StormX:
        $ lines = ["Give me a moment to recover. . ."]
    elif Girl == JubesX:
        $ lines = ["I need a break anyway. . .",
            "I need a minute here. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label end_of_masturbation_satisfied_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["That really worked for me, " + Girl.player_petname + "_. How about you?"]
    elif Girl == KittyX:
        $ lines = ["Well that worked for me, how 'bout you?"]
    elif Girl == EmmaX:
        $ lines = ["I suppose that took care of my needs, at least."]
    elif Girl == LauraX:
        $ lines = ["I guess that worked out, how about you?"]
    elif Girl == JeanX:
        $ lines = ["I got off, how about you?"]
    elif Girl == StormX:
        $ lines = ["I enjoyed that, at least."]
    elif Girl == JubesX:
        $ lines = ["Well. . . I certainly enjoyed that. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label end_of_masturbation_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Yeah, what did you want?"]
    elif Girl == KittyX:
        $ lines = ["Um, yeah?"]
    elif Girl == EmmaX:
        $ lines = ["Yes?"]
    elif Girl == LauraX:
        $ lines = ["So, what next?"]
    elif Girl == JeanX:
        $ lines = ["So, what next?"]
    elif Girl == StormX:
        $ lines = ["Yes?"]
    elif Girl == JubesX:
        $ lines = ["So, what'd you wanna do next?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label masturbation_good_here_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Well. . . ok then. . ."]
    elif Girl == KittyX:
        $ lines = ["Well. . . ok. . ."]
    elif Girl == EmmaX:
        $ lines = ["Well. . . yes. . ."]
    elif Girl == LauraX:
        $ lines = ["Ok."]
    elif Girl == JeanX:
        $ lines = ["Ok."]
    elif Girl == StormX:
        $ lines = [". . . fine then. . ."]
    elif Girl == JubesX:
        $ lines = ["Ok, cool. . ."]

label masturbation_stop_for_now_lines(Girl, Action_type):
    if Girl == RogueX:
        $ lines = ["Well if you say so."]
    elif Girl == KittyX:
        $ lines = ["I guess? . ."]
    elif Girl == EmmaX:
        $ lines = ["I . . . yes . ."]
    elif Girl == LauraX:
        $ lines = ["Hrmm."]
    elif Girl == JeanX:
        $ lines = ["Hrmm."]
    elif Girl == StormX:
        $ lines = ["I . . . fine . ."]
    elif Girl == JubesX:
        $ lines = ["Hrmm."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label maybe_blowjob_instead_lines(Girl):
    if Girl == RogueX:
        $ lines = ["I could just. . . blow you instead?",
            "I could maybe. . . you know, [she pushes her tongue against the side of her cheek]?"]
    elif Girl == KittyX:
        $ lines = ["Could I[Girl.like]. . . blow you instead?"]
    elif Girl == EmmaX:
        $ lines = ["You seemed to enjoy blowjobs, would that work instead?",
            "Would you perhaps prefer a blowjob?"]
    elif Girl == LauraX:
        $ lines = ["I could maybe blow you?"]
    elif Girl == JeanX:
        $ lines = ["What about a blowjob then?"]
    elif Girl == StormX:
        $ lines = ["You seemed to enjoy blowjobs, would that work instead?",
            "Would you perhaps prefer a blowjob?"]
    elif Girl == JubesX:
        $ lines = []

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label maybe_handjob_instead_lines(Girl):
    if Girl.permanent_History["handjob"]:
        if Girl == RogueX:
            $ lines = ["Maybe you'd settle for a handy?"]
        elif Girl == KittyX:
            $ lines = ["Maybe I could just use my hand?",
                "Maybe you'd[Girl.like]settle for a handy?"]
        elif Girl == EmmaX:
            $ lines = ["I could just stroke you off, perhaps?",
                "Perhaps a handjob?"]
        elif Girl == LauraX:
            $ lines = ["Couldn't I just use my hand again?{p}You seemed to like that.",
                "I could give you a handy?"]
        elif Girl == JeanX:
            $ lines = ["I could give you a hand job?"]
        elif Girl == StormX:
            $ lines = ["I could just stroke you off, perhaps?",
                "Perhaps a handjob?"]
        elif Girl == JubesX:
            $ lines = []
    else:
        if Girl == RogueX:
            $ lines = ["I could maybe. . . [she makes a jerking motion with her hand]?"]
        elif Girl == KittyX:
            $ lines = ["I could maybe. . . [she makes a jerking motion with her hand]?"]
        elif Girl == EmmaX:
            $ lines = ["Would my hand be an adequate substitute?"]
        elif Girl == LauraX:
            $ lines = ["I could maybe use my hand instead, how's that sound?"]
        elif Girl == JeanX:
            $ lines = ["I could give you a hand job?"]
        elif Girl == StormX:
            $ lines = ["Would my hand be an adequate substitute?"]
        elif Girl == JubesX:
            $ lines = []

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label alternative_rejected_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Ok, whatever.",
            "Ok, your loss."]
    elif Girl == KittyX:
        $ lines = ["Nah."]
    elif Girl == EmmaX:
        $ lines = ["Well, that's too bad.",
            "Pity."]
    elif Girl == LauraX:
        $ lines = ["Nah.",
            "Fine, be that way."]
    elif Girl == JeanX:
        $ lines = ["Well then too bad, I guess.",
            "Too bad then."]
    elif Girl == StormX:
        $ lines = ["Well. That is unfortunate. . .",
            "That is unfortunate."]
    elif Girl == JubesX:
        $ lines = []

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label meeting_in_shower_lines(Girl, approval, first, someone_left):
    if Girl == RogueX:
        if first:
            ch_r "Hey, [Girl.player_petname]."

            if not approval:
                ch_r "See ya later."
        elif not approval and someone_left:
            ch_r "Yeah, I'll see you too."
        elif not approval:
            ch_r "Yeah, I should get going though."
        else:
            ch_r "Yeah, hey."
    elif Girl == KittyX:
        if first:
            ch_k "Hey, [Girl.player_petname]."

            if not approval:
                ch_k "Oh, um, I should get out of your way. . ."
        elif not approval and someone_left:
            ch_k "Yeah, see ya."
        elif not approval:
            ch_k "Oh, well. . . I should get going."
        else:
            ch_k "Yeah, hi."
    elif Girl == EmmaX:
        if first:
            ch_e "Oh, hello, [Girl.player_petname]."

            if not approval:
                ch_e "I should get going."
        elif not approval and someone_left:
            ch_e "Yes, I should also get going."
        elif not approval:
            ch_e "You two look like you have some business. . ."
        else:
            ch_e "Yes, hello."
    elif Girl == LauraX:
        if first:
            ch_l "Oh, hey."

            if not approval:
                ch_l "See you later."
        elif not approval and someone_left:
            ch_l "Yeah, I'm heading out too."
        elif not approval:
            ch_l "I'll get out of your way."
        else:
            ch_l "Hey."
    elif Girl == JeanX:
        if first:
            ch_j "Oh, hey. . . you."

            if not approval:
                ch_j "Later."
        elif not approval and someone_left:
            ch_j "Yeah, I'm done too."
        elif not approval:
            ch_j "I'm headed out."
        else:
            ch_j "Hey."
    elif Girl == StormX:
        if first:
            ch_s "Oh, hello, [Girl.player_petname]."

            if not approval:
                ch_s "I am heading out at the moment."
        elif not approval and someone_left:
            ch_s "Yes, I am also leaving."
        elif not approval:
            ch_s "I wouldn't want to be a bother. . ."
        else:
            ch_s "Yes, hello."
    elif Girl == JubesX:
        if first:
            ch_v "Yo, [Girl.player_petname]."

            if not approval:
                ch_v "I should, uh, get going. . ."
        elif not approval and someone_left:
            ch_v "Yeah, see ya."
        elif not approval:
            ch_v "Oh, so. . . I should head out."
        else:
            ch_v "Yeah, hey."

    return

label template(Girl, Action_type):
    if Girl == RogueX:
        $ lines = []
    elif Girl == KittyX:
        $ lines = []
    elif Girl == EmmaX:
        $ lines = []
    elif Girl == LauraX:
        $ lines = []
    elif Girl == JeanX:
        $ lines = []
    elif Girl == StormX:
        $ lines = []
    elif Girl == JubesX:
        $ lines = []

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return
