label out_of_action_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Sorry, " + Girl.player_petname + " but I'm a bit worn out."
            "I'm a bit worn out right now, " + Girl.player_petname + " maybe later."]
    elif Girl == KittyX:
        $ lines = ["Sorry, " + Girl.player_petname + " but I'm a bit worn out."
            "I'm kinda tired right now, " + Girl.player_petname + " later?"]
    elif Girl == EmmaX:
        $ lines = ["I'm sorry, " + Girl.player_petname + " but I need a break."
            "I'm rather tired right now, " + Girl.player_petname + " rain check?"]
    elif Girl == LauraX:
        $ lines = ["Maybe in a minute, I need a break."
            "Maybe later, " + Girl.player_petname + ""]
    elif Girl == JeanX:
        $ lines = ["Gimme a minute, k?"]
    elif Girl == StormX:
        $ lines = ["I am sorry, " + Girl.player_petname + " I need to take a break."]
    elif Girl == JubesX:
        $ lines = ["I could use a short break first."
            "Maybe later, " + Girl.player_petname + ""]

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

label sex_menu_less_than_five_rounds(Girl):
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
        $ lines = ["Are you sure, " + Girl.player_petname + "? I could really use some company."
    elif Girl == KittyX:
        $ lines = ["Are you sure, " + Girl.player_petname + "? I wasn't exactly. . . finished."
    elif Girl == EmmaX:
        $ lines = ["Are you certain, " + Girl.player_petname + "? Are you perhaps forgetting something?"
    elif Girl == LauraX:
        $ lines = ["Are you sure, " + Girl.player_petname + "?{p}I could go another round. . . or two. . ."]
    elif Girl == JeanX:
        $ lines = ["Are you sure, " + Girl.player_petname + "?{p}I could go another round. . . or two. . ."]
    elif Girl == StormX:
        $ lines = ["Are you certain, " + Girl.player_petname + "? Are you perhaps forgetting something?"]
    elif Girl == JubesX:
        $ lines = ["Are you sure, " + Girl.player_petname + "?{p}I could keep going. . ."]

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
        $ lines = ["Don't leave me hang'in, " + Girl.player_petname + "."]
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
        $ lines = ["Yeah, but [Girl.like]. . ."]
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
        $ lines = ["I guess I'm a bit tuckered out too, " + Girl.player_petname + ". I guess we can take a breather."]
    elif Girl == KittyX:
        $ lines = ["I guess I'm kinda tired too, " + Girl.player_petname + ". We can take a break. . .{p}. . .for now."]
    elif Girl == EmmaX:
        $ lines = ["I suppose I'm tired as well, " + Girl.player_petname + ". We can take a breather. . ."]
    elif Girl == LauraX:
        $ lines = ["Yeah, you look like you've had enough. We can take a break. . .{p}}. . .for now."]
    elif Girl == JeanX:
        $ lines = ["Ok, sounds good. . ."]
    elif Girl == StormX:
        $ lines = ["I could use some rest as well, " + Girl.player_petname + "."]
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

label end_of_action_lines(Girl, action):
    if Girl == RogueX:
        $ lines = ["Ok, " + Girl.player_petname + " that's enough of that for now."]
    elif Girl == KittyX:
        $ lines = ["Time to take a little break, for now.",
            "Ok, we need to take a break.",
            "Ok, I'm kinda done for now, I need a break."]

        if action == "blowjob":
            $ lines.append("Ok, I gotta rest my jaw for a minute. . .")
    elif Girl == EmmaX:
        $ lines = ["We need to stop for a moment, let me catch my breath.",
            ch_e "All right, " + Girl.player_petname + ", that's plenty for now.",
            ch_e "Ok, " + Girl.player_petname + ", that's enough of that for now.",
            ch_e "That's probably enough of that.",
            "Ok, that's enough, for now. . ."]

        if action in cock_actions:
            $ lines.append("Ok, seriously, I'm putting it down for a minute.")

        if action == "blowjob":
            $ lines.append("Ok, I need to rest my jaw for a minute. . .")
    elif Girl == LauraX:
        $ lines = ["Ok, " + Girl.player_petname + " breaktime.",
            ch_l "Ok, I'm kinda done for now, I need a break."]

        if action in passive_actions:
            $ lines.append("Ok, I'm taking a quick break. . .")
    elif Girl == JeanX:
        $ lines = ["Ok, " + Girl.player_petname + " time for a break.",
            ch_j "Ok, that's it, break time."]
    elif Girl == StormX:
        $ lines = ["I need to take a moment to collect myself.",
            ch_s "That is enough of that."]
    elif Girl == JubesX:
        $ lines = ["Ok, that's it, I need a break.",
            ch_s "" + Girl.player_petname + ", that will be enough for now."]

        if action in

    Girl.voice "[line]"

    return

label ten_rounds_left_lines(Girl, action):
    if Girl == RogueX:
        $ lines = ["You might want to wrap this up, it's getting late."]
    elif Girl == KittyX:
        $ lines = ["It's" + Girl.Like + "getting kinda late.",
            "It's kind of time to get moving.",
            "We might want to wrap this up, it's getting late."]
    elif Girl == EmmaX:
        $ lines = ["It's getting late. . .",
            "It's about time for a break.",
            "It's getting a bit late. . ."]

        if actions in active_actions:
            $ lines.append("You might want to wrap this up, it's getting late.")
            $ lines.append("You might want to think about your endgame here. . .")

        if actions in passive_actions:
            $ lines.append("I think I'll probably take a break soon.")
    elif Girl == LauraX:
        $ lines = ["It's getting late, we should wrap this up.",
            "It's kinda time to get moving.",
            "We might want to wrap this up, it's getting late."]
    elif Girl == JeanX:
        $ lines = ["Wow, look at the time. . ."]
    elif Girl == StormX:
        $ lines = ["It is getting late, " + Girl.player_petname + ". . ."]

        if actions in active_actions:
            $ lines.append("You might want to consider finishing. . .")

        if actions in passive_actions:
            $ lines.append("I will probably take a break soon.")
    elif Girl == JubesX:
        $ lines = ["I could use a break soon. . .",
            "Wow, look at the time. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label five_rounds_left_lines(Girl, action):
    if Girl == RogueX:
        $ lines = ["Seriously, it'll be time to stop soon."]
    elif Girl == KittyX:
        $ lines = ["We should wrap this up."
            "For real[Girl.like]time's up.",
            "Seriously, it'll be time to stop soon."]
    elif Girl == EmmaX:
        $ lines = ["We should take a break soon.",
            "Seriously, it'll be time to stop soon.",
            "Do you mind if we take a break?",
            "We'll need a break soon."]

        if action == "masturbation":
            $ lines.append("Ung, I'm almost finished. . .")
    elif Girl == LauraX:
        $ lines = ["Tick tock, " + Girl.player_petname + "."]

        if action == "masturbation":
            $ lines.append("Five minutes, maybe.")
    elif Girl == JeanX:
        $ lines = ["We should probably wrap this up, " + Girl.player_petname + ".",
            "Ok, can we take a break?"]
    elif Girl == StormX:
        $ lines = ["We should take a break soon.",
            "We shall require a break soon."]

        if action == "masturbation":
            $ lines.append("Ah! I am nearly finished. . .")
    elif Girl == JubesX:
        $ lines = [". . . I could really use a break here. . ."]

        if action == "masturbation":
            $ lines.append("Five minutes, maybe.")

    $ line = renpy.random.choice(lines)

    Girl.voice line

    return

label tired_lines(Girl):
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

label auto_rejected_lines(Girl, action):
    if Girl == RogueX:
        $ lines = ["Ah, ah, Just keep doing what you were doing, " + Girl.player_petname + ".",
            "Hey, just keep doing what you were doing, " + Girl.player_petname + ".",
            "Oh! No, no thank you, " + Girl.player_petname + ".",
            "Um, no, I'm not really. . . don't."]

        if action in hand_actions:
            $ lines.append("Hands off the merchandise, " + Girl.player_petname + ".",
                "Hands off, " + Girl.player_petname + ".")

        if action in finger_actions:
            $ lines.append("Keep it out of there, " + Girl.player_petname + ".",
                "Keep it outside, " + Girl.player_petname + ".")
    elif Girl == KittyX:
        $ lines = ["Nuh-uh, " + Girl.player_petname + ", get back to what you were doing.",
            "Oooo! Um, no, no thanks. No. . .",
            "Whoa, back off, " + Girl.player_petname + ".",
            "Um, don't do that. . .",
            "Um, what do you think you're doing?",
            "Hmm, kinda rude, " + Girl.player_petname + "."]

        if action in hand_actions:
            $ lines.append("Hands off, " + Girl.player_petname + ".")

        if action in ass_actions:
            $ lines.append("Um[Girl.like]what are you doing back there?!")

        if action in dildo_actions:
            $ lines.append("Hey, what are you planning to do with that?!")

        if action in ["fondle_thighs", pussy_actions, ass_actions]:
            $ lines.append("Heh, keep it above the belt, " + Girl.player_petname + ".")

        if action in [finger_actions, dildo_actions]:
            $ lines.append("Um, no take that out.")
    elif Girl == EmmaX:
        $ lines = ["Whoa, back off, " + Girl.player_petname + ".",
            "" + Girl.player_petname + "! Not now. . .",
            "Do you really think you can handle that?"]

        if action in hand_actions:
            $ lines.append("Hands off, " + Girl.player_petname + ".")

        if action in finger_actions:
            $ lines.append("Careful what you put in there, you may not get it back.")

        if action in mouth_actions:
            $ lines.append("I like where your head is at, so to speak, but perhaps hold off on that.")

        if action in ass_actions:
            $ lines.append("Oh? What exactly are you doing back there?")

        if action in fondle_actions:
            $ lines.append("Down boy, you were doing so well. . .")

        if action in dildo_actions:
            $ lines.append("Excuse yourself, what are you planning to do with that?!")

        if action in ["fondle_thighs", pussy_actions, ass_actions]:
            $ lines.append("Perhaps we keep it above the waist, " + Girl.player_petname + ".")

        if action == "hotdog":
            $ lines.append("You might want to take a step back, " + Girl.player_petname + "?")
    elif Girl == LauraX:
        $ lines = ["Roll it back, " + Girl.player_petname + ". . .",
            "Whoa, back off, " + Girl.player_petname + ".",
            "" + Girl.player_petname + "! No. . ."]

        if action in hand_actions:
            $ lines.append("Watch your hands, or lose them.",
                "Hands off, " + Girl.player_petname + ".")

        if action in dildo_actions:
            $ lines.append("Hey, what are you planning to do with that?!")

        if action in ["fondle_thighs", pussy_actions, ass_actions]:
            $ lines.append("Maybe we keep it above the waist, " + Girl.player_petname + ".")

        if action in anal_insertion_actions:
            $ lines.append("Oh? A backdoor intruder?")

        if action == "eat_pussy":
            $ lines.append("Hey, good instincts, but maybe hold off?")

        if action == "sex":
            $ lines.append("Oh, taking it all the way, are we?")

        if action == "hotdog":
            $ lines.append("You might want to take a step back, " + Girl.player_petname + "?")
    elif Girl == JeanX:
        $ lines = ["Not so fast, " + Girl.player_petname + ". . .",
            "Hmmm, not yet, " + Girl.player_petname + ".",
            "Ooo! Not right now, " + Girl.player_petname + ".",
            "Whoa there, " + Girl.player_petname + "!"]

        if action in dildo_actions:
            $ lines.append("Hey, what are you planning to do with that?!")

        if action in ["fondle_thighs", pussy_actions, ass_actions]]:
            $ lines.append("Keep it above the waist, " + Girl.player_petname + ".")

        if action in insertion_actions:
            $ lines.append("Just sticking it in?")

        if action in anal_insertion_actions:
            $ lines.append("Sticking in the back?")

        if action == "hotdog":
            $ lines.append("Little close there, " + Girl.player_petname + "?")
    elif Girl == StormX:
        $ lines = ["Probably not, right now. . .",
            "Show some self control. . .",
            "Perhaps show some control. . .",
            "You go too far, " + Girl.player_petname + ".",
            "" + Girl.player_petname + "! Not now. . .",
            "Are you certain that is what you want?"]

        if action in finger_actions:
            $ lines.append("Careful what you put in there, you may not get it back.")

        if action in hand_actions:
            $ lines.append("Release me, " + Girl.player_petname + ".")

        if action in dildo_actions:
            $ lines.append("Excuse yourself, what are you planning to do with that?!")

        if action in anal_insertion_actions:
            $ lines.append("Excuse me, what are you aiming at?")

        if action in ["fondle_thighs", pussy_actions, ass_actions]:
            $ lines.append("Perhaps we keep it above the waist, " + Girl.player_petname + ".")

        if action == "eat_pussy":
            $ lines.append("I appreciate the intent, but this is not the time for it.")

        if action == "hotdog":
            $ lines.append("You are rather close, " + Girl.player_petname + ". . .")
    elif Girl == JubesX:
        $ lines = ["Cool your jets, " + Girl.player_petname + ". . .",
            "Whoa, back off, " + Girl.player_petname + ".",
            "" + Girl.player_petname + "! No. . ."]

        if action in hand_actions:
            $ lines.append("Watch your hands, or lose them.",
                "Hands off, " + Girl.player_petname + ".")

        if action in ["fondle_thighs", pussy_actions, ass_actions]:
            $ lines.append("Maybe we keep it above the waist, " + Girl.player_petname + ".")

        if action == "eat_pussy":
            $ lines.append("Hey, good instincts, but maybe hold off?")

        if action == "sex":
            $ lines.append("Oh, taking it all the way, are we?")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label private_enough_lines(Girl, action):
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

label recent_action_lines(Girl, action):
    if Girl == RogueX:
        $ lines = ["Mmm, again? Ok.",
            "Mmm, again? Ok, let's get to it.",
            "Again? Ok.",
            "Again? K."]

        if action == "handjob":
            $ lines.append("Mmm, again? Let me flex my hand a bit. . .")

        if action == "footjob":
            $ lines.append("I don't want to wear them out. . .")

        if action == "titjob":
            $ lines.append("Mmm, again? Ok, let me get the girls ready.")

        if action == "blowjob":
            $ lines.append("Mmm, again? [[stretches her jaw]")

        if action in sex_actions:
            $ lines.append("You want to go again? Ok.")

        if action in anal_insertion_actions:
            $ lines.append("I think I'm warmed up. . .")
    if Girl == KittyX:
        $ lines = ["Mmm, again? Ok.",
            "Mmm, again?",
            "Mmm, again? Ok, let's get to it."]

        if action == "handjob":
            $ lines.append("You're giving me carpal tunnel. . .")

        if action == "footjob":
            $ lines.append("I'm getting foot cramps. . .")


        if action == "blowjob":
            $ lines.append("Mmm, again? [[stretches her jaw]")

        if action in sex_actions:
            $ lines.append("Another round? {i}Fine.{/i}")

        if action in anal_insertion_actions:
            $ lines.append("I guess I'm warmed up. . .")
    if Girl == EmmaX:
        $ lines = ["Mmmm, again? I suppose. . .",
            "Oh! Back for more?",
            "Mmm, again? Ok, let's get to it.",
            "Again? Oh, very well.",
            "Alright."]

        if action == "handjob":
            $ lines.append("I will need to grade papers later, you know. . .")

        if action == "footjob":
            $ lines.append("You know, heels are nightmare on the arches. . .")

        if action == "blowjob":
            $ lines.append("Mmm, again? [[yawns]")

        if action in sex_actions:
            $ lines.append("Again? " + Girl.player_petname + ", you're insatiable!")

        if action in anal_insertion_actions:
            $ lines.append("I am warmed up. . .")
    if Girl == LauraX:
        $ lines = ["Mmmm, again? I guess. . .",
            "Huh, again?",
            "Mmm, again? Ok, let's get to it.",
            "More of that, huh. . .",
            "Again? Fine, whatever."]

        if action == "handjob":
            $ lines.append("Hmm, another handy then. . .")

        if action == "blowjob":
            $ lines.append("Mmm, again? [[yawns]")

        if action in sex_actions:
            $ lines.append("Again? Your funeral.")

        if action in anal_insertion_actions:
            $ lines.append("I am warmed up. . .")

        if action in active_actions:
            $ lines.append("Sure, get in there.")
    if Girl == JeanX:
        $ lines = ["Mmmm, again? I guess. . .",
            "Huh, again?",
            "Mmm, again?",
            "Mmm, again? Ok, let's get to it.",
            "More of that, huh. . .",
            "Ok, sure.",
            "Again? Fine, whatever."]

        if action in job_actions:
            $ lines.append("Well, I guess another wouldn't hurt. . .")

        if action in sex_actions:
            $ lines.append("Again? Your funeral.")

        if action in anal_insertion_actions:
            $ lines.append("I am warmed up. . .")
    if Girl == StormX:
        $ lines = ["Mmmm, again? I suppose. . .",
            "You cannot get enough?",
            "Mmm, again?",
            "Mmm, again? Ok, let's get to it.",
            "I suppose so. . .",
            "Again? Oh, very well.",
            "Of course."]

        if action in job_actions:
            $ lines.append("I do not know if I have it in me. . .")

        if action in sex_actions:
            $ lines.append("Again? " + Girl.player_petname + ", you are a lion!")

        if action in anal_insertion_actions:
            $ lines.append("I am properly stretched out. . .")
    if Girl == JubesX:
        $ lines = ["Mmmm, again? I guess. . ."]

        if action == "handjob":
            $ lines.append("Hmm, another handy then. . .")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label taboo_action_rejected_lines(Girl, action):
    if Girl == RogueX:
        $ lines = ["I really don't think this is the right place for that!",
            "" + Girl.player_petname + "! Not in public!",
            "This just really isn't the time or place, " + Girl.player_petname + "!",
            "Not in such an exposed place, " + Girl.player_petname + ".",
            "Not here!",
            "I'd be a bit embarassed doing that here."]

        if action in [dildo_actions, cock_actions]:
            $ lines.append("You really expect me to do that here? You realize how. . . exposed that would be?",
                "You really expect me to do that here?",
                "Even if I wanted to, it certainly wouldn't be here!")

        if action in sex_actions:
            $ lines.append("That you would even suggest such a thing in a place like this. . .")
    elif Girl == KittyX:
        $ lines = ["I don't like being so. . . exposed.",
            "Time and place, " + Girl.player_petname + "!",
            "This just really isn't the time or place, " + Girl.player_petname + "!",
            "" + Girl.player_petname + "! Not here!",
            "" + Girl.player_petname + "! Time and place!",
            "This is way too exposed!",
            "Not here!",
            "Not here, not anywhere near here.",
            "[Girl.Like]not here though?"]

        if action in [dildo_actions, cock_actions]:
            $ lines.append("You're being ridiculous. That? Here?!")

        if action in passive_actions:
            $ lines.append("You really expect me to do that here? You realize how. . . exposed that would be?")

        if action in sex_actions:
            $ lines.append("I can't believe you'd even consider it around here!")
    elif Girl == EmmaX:
        $ lines = ["I can't be seen doing that with you.",
            "I have a reputation to maintain.",
            "I couldn't possibly do that. . . here!",
            "This is way too exposed!",
            "Not here!",
            "This truly isn't an appropriate place for that.",
            "How can you imagine this would be an appropriate location?",
            "This area is a bit too exposed for that sort of thing. . ."]

        if action in [dildo_actions, cock_actions]:
            $ lines.append("Can you imagine the scandal? Here?")

        if action == "anal":
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

        if action in [dildo_actions, cock_actions]:
            $ lines.append("You really expect me to do that here? This isn't exactly \"covert.\"",
                "This area is a bit too exposed for that sort of thing. . .")
    elif Girl == JeanX:
        $ lines = ["I'm. . . not comfortable. . . in public. . .",
            "I'm not comfortable in public right now. . .",
            "Not here!",
            "This is too public.",
            "I'm just not comfortable with that right now. . .",
            "This area is a bit too exposed for that sort of thing. . ."]

        if action in [dildo_actions, cock_actions]:
            $ lines.append("You really expect me to do that here?{p}You know I can't \"take care of that\" anymore. . .")
    elif Girl == StormX:
        $ lines = ["I should not be seen doing that.",
            "I do not wish to make a spectacle.",
            "This is much too exposed.",
            "Not here!",
            "This truly is not an appropriate place for that.",
            "This area is a bit too exposed for that sort of thing. . ."]

        if action in [dildo_actions, cock_actions]:
            $ lines.append("I could not possibly do that here.")

        if action in sex_actions:
            $ lines.append("How could you imagine that this would be an appropriate location?")
    elif Girl == JubesX:
        $ lines = ["I don't wanna make a scene."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label taboo_lines(Girl):
    if Girl == RogueX:
        $ lines = ["I told you not in public!",
            "I already told you this is too public!",
            "This is just way too exposed!",
            "I said not in public!"]

        if action in passive_actions:
            $ lines.append("I already told you that I wouldn't do that out here!")

        if action in dildo_actions:
            $ lines.append("Stop swinging that thing around in public!")

        if action == "hotdog":
            $ lines.append("I told you that I didn't want you rubb'in up on me in public!")
    elif Girl == KittyX:
        $ lines = ["Not here!",
            "This is just way too exposed!",
            "I told you this is too public!",
            "I said not in public!",
            "I already told you this is too public!",
            "I{i}just{/i}[Girl.like]told you, not in public!"]

        if action in passive_actions:
            $ lines.append("I already told you that I wouldn't do that out here!")

        if action in dildo_actions:
            $ lines.append("Stop swinging that thing around in public!")
    elif Girl == EmmaX:
        $ lines = []

        if action in passive_actions:
            $ lines.append()

        if action in dildo_actions:
            $ lines.append()
    elif Girl == LauraX:
        $ lines = []

        if action in passive_actions:
            $ lines.append()

        if action in dildo_actions:
            $ lines.append()
    elif Girl == JeanX:
        $ lines = []

        if action in passive_actions:
            $ lines.append()

        if action in dildo_actions:
            $ lines.append()

    ch_j "I told you. . . not here, " + Girl.player_petname + "."
    ch_s "This area is too public, " + Girl.player_petname + "."
    ch_v "I told you, not here, " + Girl.player_petname + "."




    ch_s "As I said, not here, " + Girl.player_petname + "."

    ch_e "As I said, not here, " + Girl.player_petname + "."
    ch_l "I told you, not here, " + Girl.player_petname + "."




        ch_l "I said not in public."
        ch_j "I told you I wasn't comfortable in public. . ."
        ch_s "I was very clear, this is too public."
        ch_v "I said not in public."


        ch_e "This is not an appropriate place for that."
        ch_l "This is just way too exposed!"
        ch_j "I don't want to show off the goods like that!"
        ch_s "This is not an appropriate place for that."


        ch_e "I told you this is too public!"
        ch_l "Like I told you, too public!"
        ch_j "Like I said, too public!"
        ch_s "I told you this is too public!"


        ch_e "Stop showing that thing around in public!"
        ch_l "Stop swinging that thing around in public!"
        ch_j "Stop swinging that thing around in public!"
        ch_s "Stop showing that thing around in public!"


            ch_e "I already told you that I wouldn't do that out here!"
            ch_l "I already told you that I wouldn't do that out here!"
            ch_s "I already told you that I wouldn't do that out here!"


                ch_e "I told you, not in public!"
                ch_l "I said not in public!"
                ch_j "I said not in public!"
                ch_s "I informed you, not in public!"



                    ch_l "I already told you this is too public!"
                    ch_j "I told you, I'm not comfortable with that. . ."

                    ch_e "I already told you this is too public!"
                    ch_l "I already told you this is too public!"
                    ch_j "I told you, I'm not comfortable with that. . ."
                    ch_s "I have already informed you, this is too public!"


                    ch_e "I already told you. . .not in such an exposed location."
                    ch_l "I told you. . . this place is too exposed."
                    ch_j "I'm not comfortable with that. . ."
                    ch_s "I already informed you. . .not in such an exposed location."

    Girl.voice "[line]"

    return

label action_not_done_yet_lines(Girl):
    if Girl == RogueX:
        $ lines = ["I just don't think I'm ready yet, " + Girl.player_petname + ". . .",
            "I. . . don't think that's. . .",
            "Not now, " + Girl.player_petname + ".",
            "Let's not, ok " + Girl.player_petname + "?",
            "Not yet, " + Girl.player_petname + ". . .",
            "Oh, um, no, I'm not really comfortable with that. . .",
            "Um, not down there, " + Girl.player_petname + ". . .",
            "I don't really want to touch it, " + Girl.player_petname + ". . .",
            "I'm not really up for that, " + Girl.player_petname + ". . .",
            "I don't think I'd like the taste, " + Girl.player_petname + ". . .",
            ". . . well I don't know about that, " + Girl.player_petname + ". . .",
            "I'm just not into toys, " + Girl.player_petname + ". . .",
            "I just don't think I'm ready yet, " + Girl.player_petname + ". . .",
            "I'm just not into that, " + Girl.player_petname + ". . .",
            "That's kinda naughty, " + Girl.player_petname + ". . ."]

    if Girl == RogueX:
        $ lines = ["I. . . don't think that's. . ."]


    ch_k "I'm[Girl.like]not ready for that, " + Girl.player_petname + ". . ."
    ch_e "I highly doubt you could handle them, " + Girl.player_petname + ". . ."
    ch_l "Look, I don't know if we're ready for that, " + Girl.player_petname + ". . ."
    ch_j "Look, don't touch, " + Girl.player_petname + ". . ."
    ch_s "Perhaps some other time, " + Girl.player_petname + ". . ."
    ch_v "Look, I don't know if we're ready for that, " + Girl.player_petname + ". . ."

    ch_k "Not. . . yet. . . maybe later."
    ch_e "Let's work up to that, perhaps. . ."
    ch_l "Let's work up to that maybe. ."
    ch_j "Let's work up to that maybe. ."
    ch_s "Mmm. . . that would. . . no. . ."
    ch_v "Let's work up to that maybe. ."

    ch_k "Not. . . yet. . . maybe later."
    ch_e "Seems a bit forward, " + Girl.player_petname + "."
    ch_l "Seems a bit aggressive, " + Girl.player_petname + "."
    ch_j "Look, don't touch, " + Girl.player_petname + "."
    ch_s "I would rather you did not, " + Girl.player_petname + "."
    ch_v "Kinda forward, " + Girl.player_petname + "."

    ch_k "Um, not down there, " + Girl.player_petname + ". . ."
    ch_e "I don't think we're there yet, " + Girl.player_petname + ". . ."
    ch_l "I don't think we're there yet, " + Girl.player_petname + ". . ."
    ch_j "I don't think we're there yet, " + Girl.player_petname + ". . ."
    ch_s "Perhaps go slower, " + Girl.player_petname + ". . ."
    ch_v "I don't think we're there yet, " + Girl.player_petname + ". . ."

    ch_k "That's pretty intimate, " + Girl.player_petname + ". . ."
    ch_e "I'm not sure we're at that stage, " + Girl.player_petname + ". . ."
    ch_j "Mmmm, not right now, " + Girl.player_petname + ". . ."
    ch_s "Oh, that would. . .perhaps not, " + Girl.player_petname + ". . ."
    ch_v "I'm not sure we're there yet, " + Girl.player_petname + ". . ."

    ch_k "Not yet, " + Girl.player_petname + ". . ."
    ch_e "Not yet, " + Girl.player_petname + ". . ."
    ch_l "Not yet, " + Girl.player_petname + ". . ."
    ch_j "Not yet, " + Girl.player_petname + ". . ."
    ch_s "I would rather not, " + Girl.player_petname + ". . ."
    ch_v "Not yet, " + Girl.player_petname + ". . ."

    ch_k "I. . . don't think that's. . ."
    ch_e "That's really not my usual style. . ."
    ch_l "That's really not my style. . ."
    ch_j "That's really not my style. . ."
    ch_s "I am unsure about that. . ."
    ch_v "That's really not my style. . ."

    ch_e "Are you sure though, " + Girl.player_petname + "?. . ."
    ch_l "Seriously, " + Girl.player_petname + ". . ."
    ch_j "Seriously, " + Girl.player_petname + ". . ."
    ch_s "Are you certain, " + Girl.player_petname + "? . ."
    ch_v "Seriously, " + Girl.player_petname + ". . ."

    ch_k "I'm not really up for that, " + Girl.player_petname + ". . ."
    ch_e "Perhaps later, " + Girl.player_petname + ". . ."
    ch_l "I'm not really into that, " + Girl.player_petname + ". . ."
    ch_j "Not really my thing, " + Girl.player_petname + ". . ."

    ch_k "I don't know about the taste, " + Girl.player_petname + ". . ."
    ch_e "I'm not sure you're up to my usual tastes, " + Girl.player_petname + ". . ."
    ch_l "I don't know if your taste will match your scent, " + Girl.player_petname + ". . ."
    ch_j "I have been wondering what you taste like, " + Girl.player_petname + ". . ."
    ch_s "I am not sure I would enjoy this, " + Girl.player_petname + ". . ."

    ch_e "I'm a bit past toys, " + Girl.player_petname + ". . ."
    ch_l "I'm just not into toys, " + Girl.player_petname + ". . ."
    ch_j "I'm just not into toys, " + Girl.player_petname + ". . ."
    ch_s "I'm a bit past toys, " + Girl.player_petname + ". . ."

    ch_k "I'm just not into toys, " + Girl.player_petname + ". . ."
    ch_e "I'm just not into toys, " + Girl.player_petname + ". . ."
    ch_l "I'm just not into toys, " + Girl.player_petname + ". . ."
    ch_s "I'm just not into toys, " + Girl.player_petname + ". . ."

    ch_k "I don't know, " + Girl.player_petname + ". . ."
    ch_e "I'm unsure, " + Girl.player_petname + ". . ."
    ch_l "Eh, " + Girl.player_petname + ". . ."
    ch_j "Well. . ."
    ch_s "I am unsure, " + Girl.player_petname + ". . ."

    ch_k "I don't know that I'm. . .[Girl.like]ready? . ."
    ch_e "I really doubt you understand what you're in for. . ."
    ch_l "Oh, you have no idea what you're in for. . ."
    ch_j "Oh, this would be interesting. . ."
    ch_s "I seriously doubt that you understand what you would be in for. . ."

    ch_k "I don't know that I'm. . .[Girl.like]that kind of girl?"
    ch_e "I don't know that you're ready for that yet."
    ch_l "I don't know that you're ready for that yet."
    ch_j "I don't know that you're ready for that yet."
    ch_s "I do not know that you are yet prepared for that."

    ch_k "That's kinda hot, " + Girl.player_petname + ". . ."
    ch_e "Hmm, that could be amusing, " + Girl.player_petname + ". . ."
    ch_l "Hmm, that could be amusing, " + Girl.player_petname + ". . ."
    ch_j "Hmm, that could be amusing, " + Girl.player_petname + ". . ."
    ch_s "Hmm, that could be entertaining, " + Girl.player_petname + ". . ."

    Girl.voice "[line]"

    return

label sorry_never_mind_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Ok, no problem, " + Girl.player_petname + ".",
            "Yeah, fine, " + Girl.player_petname + ".",
            "Yeah, ok, " + Girl.player_petname + ".",
            "Fine.",
            "No problem."]

    ch_k "It's cool, " + Girl.player_petname + "."
    ch_e "Don't concern yourself, " + Girl.player_petname + "."
    ch_l "No worries."
    ch_j "It's fine, I get it."
    ch_s "Don't concern yourself, " + Girl.player_petname + "."
    ch_v "Yeah, whatever."

    ch_k "No problem."
    ch_e "No offense taken. I get it."
    ch_l "It's cool."
    ch_s "No offense taken. I get it."

    ch_k "Yeah, ok, " + Girl.player_petname + "."
    ch_e "I appreciate your restraint."
    ch_l "It's cool."
    ch_s "I appreciate your restraint."

    ch_e "I appreciate your restraint, " + Girl.player_petname + "."
    ch_l "It's cool, " + Girl.player_petname + "."

    ch_s "I appreciate your restraint, " + Girl.player_petname + "."

    ch_e "Quite alright."
    ch_l "It's fine."
    ch_j "It's fine."
    ch_s "I understand."
    ch_v "It's fine."

    ch_e "That's all right, " + Girl.player_petname + "."
    ch_l "Yeah, ok, " + Girl.player_petname + "."
    ch_j "Ok, fine, " + Girl.player_petname + "."
    ch_s "That is fine, " + Girl.player_petname + "."

    ch_k "Aw, it's ok, " + Girl.player_petname + "."
    ch_e "No harm done, " + Girl.player_petname + "."
    ch_l "Cool."
    ch_j "Ok then."
    ch_s "It is fine, " + Girl.player_petname + "."

    ch_k "Yeah, ok, " + Girl.player_petname + "."
    ch_e "I thought as much, " + Girl.player_petname + "."
    ch_l "Yeah, ok, " + Girl.player_petname + "."
    ch_j "Yeah, ok, " + Girl.player_petname + "."
    ch_s "I thought as much, " + Girl.player_petname + "."

    ch_e "I'm sure, " + Girl.player_petname + "."
    ch_l "Yeah, ok, " + Girl.player_petname + "."
    ch_s "I'm sure, " + Girl.player_petname + "."

    ch_k "Yeah."
    ch_e "Thank you."
    ch_l "Sure, no problem."
    ch_j "Sure, it's fine."
    ch_s "Thank you."

    ch_e "I can appreciate your. . . drive."
    ch_l "Well, you are persistant."
    ch_j "Keep trying. . ."
    ch_s "I can appreciate your. . . desires."

    ch_k "It's cool."
    ch_e "I don't blame you for your. . . enthusiasm."
    ch_l "Hey, I can't blame you."
    ch_j "I get it."
    ch_s "I cannot blame you for your. . . desires."

    ch_k "No problem."
    ch_e "No harm in asking. Once."
    ch_l "So long as you don't push it."
    ch_j "So long as you don't push it."
    ch_s "There is no harm in asking."

    ch_k "{i}Well. . .{/i} I didn't say I didn't want to. . ."
    ch_e "I am willing to give it a try if you are. . ."
    ch_l "No no, not a problem. . ."
    ch_j "Oh, no, it's fine."
    ch_s "I am willing to give it a try if you are. . ."
    ch_v "No no, not a problem. . ."


    ch_k "Well[Girl.like]just take it easy, ok? . ."
    ch_e "Well, so long as you know what you're doing . ."
    ch_e "I didn't say I was opposed. . ."
    ch_l "Hey, whatever floats your boat. . ."
    ch_l "Get in there."
    ch_j "Sure, works for me. . ."
    ch_j "Get in there."
    ch_s "Oh, that is unfortunate. . ."
    ch_s "I did not say that I was opposed. . ."

    ch_k "I guess it doesn't feel so bad. . ."
    ch_e "Or not. . ."
    ch_l "Or not. . ."
    ch_j "I didn't say I minded. . ."
    ch_s "Or perhaps not. . ."

    ch_k "Well, now that you mention it. . ."
    ch_e "Well, now that you mention it. . ."
    ch_l "Well, now that you mention it. . ."
    ch_j "Well, now that you mention it. . ."
    ch_s "Well, now that you mention it. . ."

    Girl.voice "[line]"

    return

label maybe_later_lines(Girl):
    if Girl == RogueX:
        $ lines = ["I'll give it some thought, " + Girl.player_petname + ".",
            "It's. . . possible, " + Girl.player_petname + ".",
            "I'll be thinking about it, " + Girl.player_petname + ".",
            "Anything's possible, " + Girl.player_petname + ".",
            "Heh, maybe, " + Girl.player_petname + ".",
            "I'll give it some thought, " + Girl.player_petname + ".",
            ". . .{p}I guess?",
            "We'll have to see.",
            "I might get hungry, " + Girl.player_petname + ".",
            "Maybe I'll practice on my own time, " + Girl.player_petname + ".",
            "Yeah, maybe, " + Girl.player_petname + "."]


    ch_k "Um, yeah, maybe later."
    ch_e "Well, I can't rule it out. . ."
    ch_l "Eh. Maybe."
    ch_j ". . . I guess? Maybe."
    ch_s "I will give it some thought, " + Girl.player_petname + "."
    ch_v "Eh. Maybe."

    ch_k "I'll give it some thought, " + Girl.player_petname + "."
    ch_v "Maybe, " + Girl.player_petname + "."

    ch_k "Heh, maybe, " + Girl.player_petname + "."
    ch_e "Perhaps."
    ch_l "Maybe?"
    ch_v "Maybe?"

    ch_k "I'll give it some thought, " + Girl.player_petname + "."
    ch_e "I'll give it some thought, " + Girl.player_petname + "."
    ch_l "Maybe, " + Girl.player_petname + "."

    ch_k "It's. . . possible, " + Girl.player_petname + "."
    ch_e "It's. . . possible, " + Girl.player_petname + "."
    ch_l "It's. . . possible, " + Girl.player_petname + "."
    ch_v "It's. . . possible, " + Girl.player_petname + "."

    ch_k ". . ."
    ch_k "Maybe."
    ch_e ". . ."
    ch_e "I couldn't rule it out. . ."
    ch_l "Maybe."
    ch_j "Maybe."
    ch_s ". . ."
    ch_s "Perhaps. . ."
    ch_v "Maybe."

    ch_k "Maybe."
    ch_e "Perhaps."
    ch_l "Maybe."
    ch_j ". . . maybe."
    ch_s "Perhaps."

    ch_k "You[Girl.like]never know, " + Girl.player_petname + "."
    ch_e "I wouldn't rule it out, " + Girl.player_petname + "."
    ch_l "Yeah, maybe, " + Girl.player_petname + "."
    ch_j "Sure, whatever, " + Girl.player_petname + "."
    ch_s "I would not rule it out, " + Girl.player_petname + "."

    ch_e "Maybe I'll practice on my own time, " + Girl.player_petname + "."
    ch_l "Maybe I'll practice on my own time, " + Girl.player_petname + "."
    ch_s "Maybe I'll practice on my own time, " + Girl.player_petname + "."

    ch_k "Maybe I'll practice on my own time, " + Girl.player_petname + "."
    ch_e "Perhaps I'll practice on my own time, " + Girl.player_petname + "."

    ch_s "Perhaps I'll practice on my own time, " + Girl.player_petname + "."


    ch_e ". . ."
    ch_e "Perhaps."
    ch_l ". . ."
    ch_l "Maybe."
    ch_j "Well. . ."
    ch_j "Maybe."
    ch_s ". . ."
    ch_s "Perhaps."

    ch_k "Maybe, you never know."
    ch_e "Oh, most certainly. . ."
    ch_l "Probably. . ."
    ch_j "Sure, whatever. . ."
    ch_s "Oh, of that I am certain. . ."


    ch_e "I imagine we will. . ."
    ch_e ". . . often."
    ch_l "Oh, probably. . ."
    ch_l ". . . often."
    ch_j "Oh, probably. . ."
    ch_s "I imagine at some point we shall. . ."
    ch_s ". . . frequently."

    ch_k "Yeah, maybe, " + Girl.player_petname + "."
    ch_e "I imagine it will happen at some point, " + Girl.player_petname + "."
    ch_l "I gues eventually. . ."
    ch_j "I guess eventually. . ."
    ch_s "I expect it will happen at some point, " + Girl.player_petname + "."


    ch_k "I'll be thinking about it, " + Girl.player_petname + "."
    ch_e "I'll be thinking about it, " + Girl.player_petname + "."
    ch_l "I'll be thinking about it, " + Girl.player_petname + "."
    ch_j "Well, I'll give it some thought, " + Girl.player_petname + "."
    ch_v "I'll be thinking about it, " + Girl.player_petname + "."

    ch_k "Anything's possible, " + Girl.player_petname + "."
    ch_e "Anything's possible, " + Girl.player_petname + "."
    ch_l "Anything's possible, " + Girl.player_petname + "."
    ch_j ". . . I guess? Maybe."
    ch_s "I will give it some thought, " + Girl.player_petname + "."
    ch_v "Anything's possible, " + Girl.player_petname + "."

    Girl.voice "[line]"

    return

label begging_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Heh, I suppose I can hardly refuse ya when you use the magic words . . .",
            "You better work your mouth that hard on these.",
            "Well, if you're gonna beg. . ."]


    ch_k "Well[Girl.like]if you ask nicely. . ."
    ch_e "Politeness can be rewarded. . ."
    ch_l "Well if you're going to be a little bitch about it. . ."
    ch_j "Oh, fine, just don't start crying."
    ch_s "Well, I suppose. . ."
    ch_v "Geeze, don't whine about it. . ."

    ch_k "Only if you make it worth it."
    ch_e "Oh, if you insist. . ."
    ch_l "Ok, fine. . ."
    ch_s "Oh, if you insist. . ."
    ch_v "Ok, fine. . ."


    ch_s "I suppose it does not hurt. . ."

    ch_k "I like it when you beg. . ."
    ch_e "I do enjoy hearing you beg. . ."
    ch_l "Oooh, beg for me. . ."
    ch_s "I suppose it could not hurt. . ."
    ch_v "Oooh, beg for me. . ."


    ch_k "I like it when you beg. . ."
    ch_e "I do enjoy hearing you beg. . ."
    ch_l "Oooh, beg for me. . ."
    ch_j "Oooh, beg for me. . ."
    ch_s "Well, one could not hurt. . ."
    ch_v "Oooh, beg for me. . ."


    $ Line = renpy.random.choice(["Well, sure, I guess.",
        "Well. . . ok.",
        "I could maybe give it a try.",
        "I guess I could. . .",
        "Fiiine. . . [She licks her lips].",
        "Heh, ok, fine."]
    ch_k "[Line]"
    $ Line = renpy.random.choice(["Well, I suppose.",
        "Well. . . ok.",
        "I could perhaps give it a try.",
        "I suppose I could. . .",
        "Fine. . . [She licks her lips].",
        "Hmph, ok, fine."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Sure. Ahhhhhh.",
        "Well. . . alright.",
        "Yum.",
        "Sure, whip it out.",
        "Ok. . . [She licks her lips].",
        "Alright, let's see it."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Sure. Ahhhhhh.",
        "Well. . . alright.",
        "Yum.",
        "Sure, whip it out.",
        "Ok. . . [She licks her lips].",
        "Alright, let's see it."]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["Well, I suppose.",
        "Well. . . ok.",
        "I could perhaps give it a try.",
        "I suppose that I could. . .",
        "Fine. . . [She licks her lips].",
        "Hmph, ok, fine."]
    ch_s "[Line]"



    $ lines = ["Sure, put'im here.",
        "No Problem.",
        "Sure. Drop trou.",
        "Sure, I guess.",
        "Okay.",
        "Ok, lemme see it.",
        "I guess. . .",
        "I suppose, whip it out.",
        "Ok, [She gestures for you to come over].",
        "Heh, ok."]
    ch_r "[line]"


    $ Line = renpy.random.choice(["Sure, I guess.",
            "Ooooookay.",
            "Cool, lemme see it.",
            "I guess I could. . .",
            "Ok. . . [She gestures for you to come over].",
            "Heh, ok, ok."]
    ch_k "[Line]"
    $ Line = renpy.random.choice(["Oh, I suppose.",
        "I'll do it.",
        "Well, give it here.",
        "I suppose I could. . .",
        "Fine. . . [She gestures for you to come over].",
        "Ok, ok."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Sure, I guess.",
        "O-kay.",
        "Fine.",
        "I suppose I could. . .",
        "Ok. . . [She gestures for you to come over].",
        "Ok, ok."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Sure, I guess.",
        "Okay. . . ",
        "Fine.",
        "I suppose I could. . .",
        "Ok. . . Get over here. . .",
        "Ok, ok."]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["Oh, I suppose we might.",
        "I would do this.",
        "Very well, give it here.",
        "I suppose that I could. . .",
        ". . .Fine.[She gestures for you to come over]",
        "Ok, ok."]
    ch_s "[Line]"


    $ Line = renpy.random.choice(["Sure, I guess.",
            "Ooooookay.",
            "Cool, lemme see it.",
            "I guess I could. . .",
            "Ok. . . [She gestures for you to come over].",
            "Heh, ok, ok."]
    ch_k "[Line]"
    $ Line = renpy.random.choice(["Sure, I suppose.",
            "Fine.",
            "Very well, bring it out.",
            "I suppose I could. . .",
            "Fine. . . [She gestures for you to come over].",
            "Hmm, ok."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Sure, I guess.",
        "OK.",
        "Fine, lemme see it.",
        "I guess I could. . .",
        "Ok. . . [She gestures for you to come over].",
        "Heh, ok, ok."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Sure, I guess.",
        "OK.",
        "Fine, lemme see it.",
        "I guess I could. . .",
        "Ok. . . [She gestures for you to come over].",
        "Heh, ok, ok."]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["Hmm, I suppose.",
            "Fine.",
            "Very well, bring it out.",
            "I suppose that I could. . .",
            "Fine. . . [She gestures for you to come over].",
            "Hmm, ok."]
    ch_s "[Line]"

    Girl.voice "[line]"

    return

label please_not_good_enough_lines(Girl):
    if Girl == RogueX:
        $ lines = ["I'm afraid not this time, sorry " + Girl.player_petname + "."]


    ch_k "Um, still no."
    ch_e "This wasn't a \"tone\" issue."
    ch_l "Well if you're going to be a little bitch about it. . ."
    ch_j "No way."
    ch_s "No, thank you."
    ch_v "Geeze, don't whine about it. . ."

    ch_k "Um, still no."
    ch_e "This wasn't a \"tone\" issue."

    ch_j "Oh, don't cry."
    ch_s "No, I do not think so. . ."
    ch_s "It is not appropriate."

    ch_k "Nuh uh."
    ch_e "No."
    ch_l "No."
    ch_j "No."
    ch_s "No."
    ch_v "No."

    Girl.voice "[line]"

    return

label action_already_rejected_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Learn to take \"no\" for an answer, " + Girl.player_petname + ".",
            "I just don't want to, " + Girl.player_petname + ".",
            "I'aint tellin you again.",
            "Look, I already told you no thanks, " + Girl.player_petname + ".",
            "Read my lips, no.",
            "Learn to take \"no\" for an answer, " + Girl.player_petname + "."]


            ch_e "Don't make me repeat myself."
            ch_l "Don't ask again."
            ch_j "Don't ask again."
            ch_s "Do not make me repeat myself."

            ch_k "Look, I already told you no thanks, " + Girl.player_petname + "."
            ch_e "I've refused, end of story."
            ch_l "Look, I already told you no."
            ch_j "I already told you no."
            ch_s "I have refused. Learn to accept that."


            ch_k "You can eat a dick, 'cos I'm not."
            ch_e "Then I hope you can take care of yourself."
            ch_s "Then I hope you can take care of yourself."

            ch_k "I'm not telling you again."
            ch_e "I won't repeat myself."
            ch_l "I'm not telling you again."
            ch_j "I'm not telling you again."
            ch_s "I shall not repeat myself."

            $ Girl.ArmPose = 2
            $ Girl.ArmPose = 1
            $ Girl.Claws = 1
            ch_l "Suck this then."
            $ Girl.Claws = 0


            $ Girl.ArmPose = 2
            ch_j "You want me to make you suck yourself?"
            $ Girl.ArmPose = 1
            $ Girl.change_face("_angry",1,Eyes="_side")
            ch_j "Damn. . . forgot I can't do that. . ."
            ch_s "You go too far!"


            ch_e "Learn to take \"no\" for an answer, " + Girl.player_petname + "."

            ch_j "Learn to take \"no\" for an answer, " + Girl.player_petname + "."
            ch_s "Learn to take \"no\" for an answer, " + Girl.player_petname + "."

            ch_k "Learn to take \"no\" for an answer, " + Girl.player_petname + "."

            ch_l "Learn to take \"no\" for an answer, " + Girl.player_petname + "."



            ch_k "{i}Listen{/i}!"
            ch_e "You need to pay attention when I speak to you."
            ch_l "Listen to the words that are coming out of my mouth."
            ch_j "I don't want to have to go through this again."
            ch_s "I have been clear on this."
            ch_v "I'm pretty clear on this, NO."

            ch_k "How many times do I have to say \"no?\""
            ch_e "I don't appreciate having to repeat myself, " + Girl.player_petname + "."
            ch_l "I don't like to repeat myself, " + Girl.player_petname + "."

            ch_k "Not even, " + Girl.player_petname + "."
            ch_e "I really can't, " + Girl.player_petname + "."
            ch_l "I really can't, " + Girl.player_petname + "."
            ch_j "I really can't, " + Girl.player_petname + "."
            ch_v "I really can't, " + Girl.player_petname + "."

        ch_e "Don't question me again."
        ch_l "Don't push me."
        ch_j "Don't push your luck, " + Girl.player_petname + "."
        ch_s "Do not question me again."

        ch_k "Maybe[Girl.like]take \"no\" for an answer?"
        ch_e "Don't question me again."
        ch_l "Don't push it."
        ch_j "Know when to stop."


        ch_k "I'm just not into that."
        ch_e "I've made myself clear."
        ch_l "What did I tell you?"
        ch_j "What did I tell you?"
        ch_s "I believe I have made myself clear."

    Girl.voice "[line]"

    return

label otherwise_not_interested_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Not hap'nin.",
            "Not hap'nin, " + Girl.player_petname + ".",
            "No luck, " + Girl.player_petname + ".",
            "Tsk, not this time, " + Girl.player_petname + ".",
            "Shoo, " + Girl.player_petname + ".",
            "I. . . not there!!",
            "Ew!",
            "Um, no thanks, " + Girl.player_petname + ".",
            "What?! Gross!",
            "I'd really rather not.",
            "That isn't really how I planned to use my feet today"
            "How about let's not, " + Girl.player_petname + ".",
            "Not interested.",
            "No way.",
            "Not happening."]


        $ lines = ["I'd really rather not.",
            "Oh, um, no, I'm not really comfortable with that. . .",
            "Not right now, " + Girl.player_petname + ". . .",
            "Maybe not right now, ok?",
            "I don't think we need any toys, " + Girl.player_petname + "."]

    Girl.voice "[line]"


    ch_e "You wish."
    ch_l "Keep dreaming."
    ch_j "Yeah, you wish."
    ch_s "Hmm, no."
    ch_v "Cute, but no."

    ch_k "Um, no."

    ch_l "You wish."
    ch_j "You wish."
    ch_s "Hmm, no."
    ch_v "You wish."

    ch_k "Um, no thanks, " + Girl.player_petname + "."
    ch_e "No. Thank you."
    ch_l "Nope."
    ch_j "Nope."
    ch_s "No. Thank you."
    ch_v "Nope."

    ch_k "Oh, um, no, I'm not really comfortable with that. . ."
    ch_l "I'm really not cool with that. . ."
    ch_e "I'm really not comfortable with that. . ."
    ch_j "I'd rather not."
    ch_s "I would be uncomfortable with that. . ."
    ch_v "I'm really not cool with that. . ."

    ch_k "Let's not, ok " + Girl.player_petname + "?"
    ch_e "Let's not, ok " + Girl.player_petname + "?"
    ch_l "Let's not, ok " + Girl.player_petname + "?"
    ch_j "Let's not, ok " + Girl.player_petname + "?"
    ch_v "Let's not, ok " + Girl.player_petname + "?"


    ch_e "I'd rather not today. . ."
    ch_l "I'd rather not today. . ."
    ch_j "I'd rather not today. . ."
    ch_s "I would rather not. . ."
    ch_v "I'd rather not today. . ."

    ch_k "Not now, " + Girl.player_petname + "."
    ch_e "Not now, " + Girl.player_petname + "."
    ch_l "Not now, " + Girl.player_petname + "."
    ch_j "Not now, " + Girl.player_petname + "."
    ch_s "Not now, " + Girl.player_petname + "."
    ch_v "Not now, " + Girl.player_petname + "."

    ch_e "I'd rather not right now though."
    ch_l "Nah."
    ch_j "Nope."
    ch_s "I would rather not right now though."
    ch_v "Nah."

    ch_k "Not, right now " + Girl.player_petname + ". . ."
    ch_l "Not right now " + Girl.player_petname + ". . ."
    ch_j "Not right now " + Girl.player_petname + ". . ."
    ch_s "Perhaps later, " + Girl.player_petname + ". . ."

    ch_k "Later, " + Girl.player_petname + "!"
    ch_e "Perhaps later, " + Girl.player_petname + "."
    ch_l "I don't know, " + Girl.player_petname + "!"
    ch_j "I don't know, " + Girl.player_petname + ". . ."
    ch_s "Perhaps later, " + Girl.player_petname + "."

    ch_e "We don't need any toys, do we, " + Girl.player_petname + "?"
    ch_l "I don't think we need any toys, " + Girl.player_petname + "."
    ch_j "I don't think we need any toys, " + Girl.player_petname + "."
    ch_s "We don't need any toys, do we, " + Girl.player_petname + "?"


    ch_k "I don't think we need any toys, " + Girl.player_petname + "."
    ch_e "I don't think we need any toys, " + Girl.player_petname + "."
    ch_l "I don't think we need any toys, " + Girl.player_petname + "."
    ch_s "I don't think we need any toys, " + Girl.player_petname + "."

    ch_k "Not now, ok?"
    ch_e "Not now, " + Girl.player_petname + ". . ."
    ch_l "Not now, ok?"
    ch_j "Not now, ok?"
    ch_s "Not now, " + Girl.player_petname + ". . ."

    ch_k "Maybe[Girl.like]not right now? . ."
    ch_e "Perhaps another time would be better? . ."
    ch_l "Maybe later? . ."
    ch_j "I'm not in the mood right now . ."
    ch_s "Perhaps another time? . ."

    ch_k "Not. . . now. . ."
    ch_e "I don't think that would be appropriate. . ."
    ch_l "I don't think that would be appropriate. . ."
    ch_j "I don't think that would be appropriate. . ."
    ch_s "I do not believe that would be appropriate. . ."


    ch_k "No way."
    ch_e "No."
    ch_l "No."
    ch_j "No."
    ch_s "No, I do not think so."
    ch_v "No."

    ch_k "Nooope."
    ch_e "No."

    ch_j "I'm sorry, not now."

    ch_k "No luck " + Girl.player_petname + "."
    ch_e "No thank you, " + Girl.player_petname + "."
    ch_l "No thank you, " + Girl.player_petname + "."
    ch_j "No thanks, " + Girl.player_petname + "."
    ch_v "No thank you, " + Girl.player_petname + "."

    ch_k "Ugh!"
    ch_e "I know, I'm as disappointed as you are."
    ch_l "Yeah, sorry."
    ch_j "Yeah, sorry."
    ch_v "Yeah, sorry."

    ch_k "Scram, " + Girl.player_petname + "."

    ch_k "That's. . . not cool."
    ch_e "Not today, " + Girl.player_petname + "."
    ch_l "Not today, " + Girl.player_petname + "."
    ch_j "Not today, " + Girl.player_petname + "."
    ch_v "Not today, " + Girl.player_petname + "."

    ch_k "Ew."
    ch_e "I'm sorry, not now."
    ch_l "I'm sorry, not now."
    ch_v "I'm sorry, not now."

    ch_k "I don't wanna touch that."
    ch_e "No, I don't think so, " + Girl.player_petname + "."
    ch_l "I don't know where that's been lately."
    ch_j "I'd really prefer not touching that."
    ch_s "No, I do not think so, " + Girl.player_petname + "."

    ch_k "How about let's not, " + Girl.player_petname + "."
    ch_e "How about let's not, " + Girl.player_petname + "."
    ch_l "Nah."
    ch_j "Nah."
    ch_s "I would rather not, " + Girl.player_petname + "."

    ch_k "Nope."
    ch_e "I don't think I will."
    ch_l "Nope."

    $ Girl.change_face("_smile", 1)
    ch_j "Ha! Good one."
    ch_s "I do not think that I will."


    ch_e "No way."
    ch_l "No way."
    ch_j "No way."
    ch_s "No way."

    ch_k "No way."
    ch_e "No, thank you."
    ch_s "No, thank you."

    ch_k "I don't know about using my feet for. . . that."
    ch_e "I'm not in the mood for footplay today. . ."
    ch_l "I'd rather not."
    ch_j "I'd rather not."
    ch_s "I am truly in no mood for footplay today. . ."

    ch_k "Nuhuh."
    ch_e "I'm afraid not."
    ch_l "Yeah, no."
    ch_j "Not interested."
    ch_s "I must refuse."

    ch_e "I don't think you've earned that yet."
    ch_k "Noooope."
    ch_e "I don't think you've earned that yet."
    ch_l "You haven't earned it yet."
    ch_j "You haven't earned it yet."
    ch_s "I do not think you have earned that yet."

    ch_k "Noooop."
    ch_e "No, thank you."
    ch_l "No thanks."
    ch_j "No thanks."
    ch_s "Thank you, but no."

    return

label previous_action_rejected_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Sorry, " + Girl.player_petname + " you aren't touching these again.",
            "Sorry, " + Girl.player_petname + " you aren't getting these in your mouth.",
            "Sorry, keep your tongue in your mouth.",
            "Sorry, hands off the booty.",
            "Fresh!",
            "I think you should keep your fingers to yourself.",
            "Sorry, keep your hands out of there.",
            "I think you can manage it yourself this time. . .",
            "Not right now, " + Girl.player_petname + ". . .",
            "I think I'll let you know when I want you touching these again.",
            "I think I've got the taste out of my mouth, thanks.",
            "Sorry, you can keep your toys to yourself.",
            "Sorry, you can keep your toys out of there.",
            "Maybe you could go fuck yourself instead.",
            "Eh-eh, not anymore, " + Girl.player_petname + ".",
            "The only thing you can do with my ass is kiss it, " + Girl.player_petname + ".{p}. . .Don't get any ideas."]


    ch_k "You had your shot."
    ch_e "I'm afraid you haven't earned back my good graces."
    ch_l "You'll have to earn that back."
    ch_j "We've had enough of that."
    ch_s "No, I do not think so."
    ch_v "You'll have to earn that."

    ch_k "Sorry, " + Girl.player_petname + ", maybe later?"
    ch_e "I am sorry about that, but perhaps later?"
    ch_l "You'll have to earn that back."
    ch_j "We've had enough of that."
    ch_v "You'll have to earn that back."

    ch_k "Fresh!"
    ch_e "Hands."
    ch_l "Keep your hands to yourself."
    ch_j "Keep your hands to yourself."
    ch_v "Keep your hands to yourself."

    ch_k "Sorry, keep your hands out of there."
    ch_e "Sorry, keep your hands out of there."
    ch_l "Sorry, fingers outside."
    ch_j "You can keep those to yourself."
    ch_v "Sorry, keep your fingers outside."

    ch_k "Keep your head out of there."
    ch_e "Keep your head out of there."
    ch_l "Keep your head out of there."
    ch_j "Keep your tongue to yourself."
    ch_v "Keep your head out of there."

    ch_k "Sorry, hands to yourself."
    ch_e "I'm sorry, keep your hands to yourself."
    ch_l "Sorry, keep your hands to yourself."
    ch_j "Sorry, keep your hands to yourself."
    ch_v "Sorry, keep your hands to yourself."

    ch_k "I don't feel like it."
    ch_e "I don't feel like it."
    ch_l "I don't feel like it."
    ch_j "I don't feel like it."
    ch_v "I'm not into it."

    ch_k "Sorry, no more of that."
    ch_e "Sorry, no more of that."
    ch_l "Sorry, no more of that."
    ch_v "Sorry, no more of that."

    ch_k "I'm not feeling it today. . ."
    ch_e "I'd really rather not. . ."
    ch_l "I'm not into it today. . ."
    ch_j "I'm not into it today. . ."
    ch_s ". . . I would rather not."

    ch_k "I think I'll let you know when I want you touching these again."
    ch_e "I'm afraid you'll just have to remember the last time."
    ch_l "You'll know when it's time for that."
    ch_j "You'll know when it's time for that."
    ch_s "Our time together was a memory."

    ch_k "No, not this time."
    ch_e "I'm just not in the mood, " + Girl.player_petname + "."
    ch_l "Nah, not this time."
    ch_j "Nah, not this time."
    ch_s "I am just not in the mood, " + Girl.player_petname + "."

    ch_k "Sorry, you can keep your toys to yourself."
    ch_e "Sorry, you can keep your toys to yourself."
    ch_l "Sorry, you can keep your toys to yourself."
    ch_j "Sorry, you can keep your toys to yourself."
    ch_s "Sorry, you can keep your toys to yourself."

    ch_k "Sorry, you can keep your toys out of there."
    ch_e "Sorry, you can keep your toys out of there."
    ch_l "Sorry, you can keep your toys out of there."
    ch_s "Sorry, you can keep your toys out of there."

    ch_k "I'm not feeling it today. . ."
    ch_e "I'm not in the mood, " + Girl.player_petname + ". . ."
    ch_l "Not right now."
    ch_j "Not right now."
    ch_s "I am in no mood, " + Girl.player_petname + ". . ."


    ch_k "Maybe just[Girl.like]fuck yourself, huh?"
    ch_e "I'm sure you can figure out how to take care of that yourself."
    ch_l "Just jack it or something."
    ch_j "Maybe just fuck one of the others."
    ch_s "I am certain you can take care of that yourself."

    ch_k "That's[Girl.like]totally off the table."
    ch_e "You'll have to show me you're worth it again."
    ch_l "You'll have to earn it."
    ch_j "You'll have to earn that one. . ."
    ch_s "You shall have to display your worth to me again."


    ch_k "Yeah, not again."
    ch_e "Not under the circumstances."
    ch_l "Not anymore."
    ch_j "Not anymore."
    ch_s "Not under the circumstances."

    Girl.voice "[line]"

    return

label forced_but_not_unwelcome_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Fine, if that's what you want.",
            "Hmmph, well I guess you can go to town. . .",
            "Hmmph.",
            "Fine, I suppose.",
            "Oh. . . well, ok then. . .",
            "Well, at least make it worth it.",
            "Ok, get in there if you're so determined.",
            "Ok, fine, whip it out.",
            "Ok, fine"
            "Ok, fine. If we're going to do this, stick it in already.",
            "Ok, fine. Whatever."]


    ch_k "Rude! But. . . whatever."
    ch_e "That is not appropriate. . ."
    ch_e "but neither is it entirely unwelcome. . ."
    ch_l "Hey. . ."
    ch_l "Eh, whatever. . ."
    ch_j "Hey. . ."
    ch_j ". . .whatever. . ."
    ch_s "That is not appropriate. . ."
    ch_s "but neither is it entirely unwelcome. . ."
    ch_v "Hey. . ."
    ch_v "Well, whatever. . ."

    ch_k "Ugh, I guess if you're so enthusiastic. . ."
    ch_e "You'd better shower them with praise. . ."
    ch_l "Hmm. . . ok. . ."
    ch_s "Only if you do a good job. . ."
    ch_v "Hmm. . . ok. . ."

    ch_k "Hmmph."
    ch_e "Hmmph."
    ch_l "Hmmph."
    ch_s "Hmmph."
    ch_v "Hmmph."

    ch_k "Well. . . I guess. . ."
    ch_e "Oh, if you insist. . ."
    ch_l "Ok, fine. . ."
    ch_s "Oh, if you insist. . ."
    ch_v "Ok, fine. . ."

    ch_k "Ok, get in there if you're so determined."
    ch_e "If you insist. . ."
    ch_l "If you insist. . ."
    ch_j "I guess you won't take \"no\" for an answer. . ."
    ch_s "If you insist. . ."
    ch_v "Well I don't want to get in your way. . ."

    ch_k "Fine, I suppose."
    ch_e "Fine, I suppose."
    ch_l "Fine, I guess."
    ch_s ". . . I suppose."
    ch_v "Fine, I guess."

    ch_k "Oh. . . well, ok then. . ."
    ch_e "Well hello there. . ."
    ch_l "Well hello there. . ."
    ch_j "Ooo! Well ok then. . ."
    ch_s "That was unexpected. . ."
    ch_v "Um, hello? . ."

    ch_k "Ok, {i}fine{/i}."
    ch_e "Suit yourself."
    ch_l "Suit yourself."
    ch_s "If you must. . ."
    ch_v "Suit yourself."


    ch_e "Hm. Alright, but don't push your luck, " + Girl.player_petname + "."
    ch_l "Ok, fine."
    ch_j ". . . Ok, whatever."
    ch_s ". . . fine."


    ch_k "Ok, fine. . ."
    ch_e "Oh, fine. . ."
    ch_l "Whatever. . ."
    ch_j ". . ."
    ch_s ". . . fine. . ."
    $ Girl.change_face("_angry",1,Eyes="_side")
    ch_j "Whatever. . ."


    ch_k "Ok, fine. If we're going to do this, stick it in already."
    ch_e "Ok, fine. If we're going to do this, stick it in already."
    ch_l "Ok, fine. If we're going to do this, stick it in already."
    ch_j "Ok, fine. If we're going to do this, stick it in already."
    ch_s "Ok, fine. If we're going to do this, stick it in already."


    ch_k "Ok, fine."
    ch_e "Oh, very well."
    ch_l "Fine."
    ch_j "Fine."
    ch_s "Oh, very well."


    ch_k "Well! . . ok, fine, stick it in."
    ch_e "Fine, if it'll shut you up."
    ch_l "Fine, if it'll shut you up."
    ch_j ". . ."
    ch_j ". . . Ok. . ."
    ch_s "Fine, if it will silence you."

    ch_e "Oh, very well, get it over with."
    ch_l "Oh fine, get it over with."
    ch_j "Oh fine, get it over with."
    ch_s "Oh, very well, if you must."

    ch_k "Ok, fine. Whatever."
    ch_e "Alright, fine. Lay back."
    ch_l "Alright, fine."
    ch_j ". . ."
    ch_j ". . . fine."
    ch_s "Alright, fine then. Lie back."

    Girl.voice "[line]"

    return

label forced_but_welcome_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Sure, get in there.",
            "Fine, grab a cheek."]

    Girl.voice "[line]"

    return

label said_no_recently_lines(Girl):
    if Girl == RogueX:
        $ lines = ["I {i}just{/i} told you \"no,\" " + Girl.player_petname + ".",
        "I {i}just{/i} told you \"no,\" " + Girl.player_petname + ".",
        "What part of \"no,\" did you not get, " + Girl.player_petname + "?"]

    ch_k "[Girl.Like]no way, " + Girl.player_petname + "."
    ch_e "Your persistance is doing you no favors, " + Girl.player_petname + "."
    ch_l "Take a breath here, before you regret it."
    ch_j "I'm not used to repeating myself."
    ch_s "Do not persist in this, " + Girl.player_petname + "."
    ch_v "I already told you, \"no\"."

    ch_k "I[Girl.like]{i}just{/i} told you \"no!\""


    ch_s "Your persistance is doing you no favors, " + Girl.player_petname + "."

    ch_k "You don't[Girl.like]listen do you, " + Girl.player_petname + "."
    ch_e "You need to learn to take\"no\" for an answer, " + Girl.player_petname + "."
    ch_l "I just told you no, " + Girl.player_petname + "."
    ch_j "I just told you no, " + Girl.player_petname + "."
    ch_v "I just told you no, " + Girl.player_petname + "."

    ch_k "I {i}just{/i} told you \"no,\" " + Girl.player_petname + "."
    ch_e "I {i}just{/i} refused, " + Girl.player_petname + "."
    ch_l "I {i}just{/i} told you \"no,\" " + Girl.player_petname + "."
    ch_j "I {i}just{/i} told you \"no,\" " + Girl.player_petname + "."

    ch_k "What did I[Girl.like]{i}just{/i} tell you " + Girl.player_petname + "."
    ch_e "I believe I just told you, \"no.\""
    ch_l "Just told you I wouldn't, " + Girl.player_petname + "."
    ch_j "Just told you I wouldn't, " + Girl.player_petname + "."
    ch_s "You will need to accept a \"no\", " + Girl.player_petname + "."

    ch_e "What part of \"no,\" did you not get, " + Girl.player_petname + "?"
    ch_l "What part of \"no,\" did you not get, " + Girl.player_petname + "?"
    ch_j "What part of \"no,\" did you not get, " + Girl.player_petname + "?"
    ch_s "What part of \"no,\" did you not get, " + Girl.player_petname + "?"

    ch_k "You don't[Girl.like]listen do you, " + Girl.player_petname + "."
    ch_e "Pay attention, " + Girl.player_petname + "."
    ch_l "You should listen better, " + Girl.player_petname + "."
    ch_j "Don't make me repeat myself again, " + Girl.player_petname + "."
    ch_s "I have made myself clear, " + Girl.player_petname + "."

    ch_k "I{i}just{/i}[Girl.like]told you \"no!\""
    ch_e "I'm afraid that \"no\" is my final answer, " + Girl.player_petname + "."
    ch_l "Sorry, " + Girl.player_petname + " \"no.\""
    ch_j "I don't repeat myself."
    ch_s "I am afraid that \"no\" is my final answer, " + Girl.player_petname + "."


    ch_j "I don't repeat myself."
    ch_s "I am afraid that \"no\" is my final answer, " + Girl.player_petname + "."


        ch_l "Sorry, " + Girl.player_petname + " \"no.\""
        ch_j "I don't repeat myself."
        ch_s "I am afraid that \"no\" is my final answer, " + Girl.player_petname + "."

    Girl.voice "[line]"

    return

label action_accepted_enthusiastically_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Ok " + Girl.player_petname + " come and get'em.",
            "Ok " + Girl.player_petname + " go ahead.",
            "Oooooooh. . .",
            "God yes.",
            "Sure, grab a cheek.",
            "Sure, get in there."]


        ch_k "Ok " + Girl.player_petname + ", come and get'em."
        ch_e "That sounds lovely, ravish me."
        ch_l "Sure, sounds fun."
        ch_j "Sure, sounds fun."
        ch_s "I would love that. . ."
        ch_v "Sure, sounds fun."

        ch_k "Ok, fiiiine."
        ch_e "Oh very well. . ."
        ch_l "Sure."
        ch_j "Sure."
        ch_s "Oh very well. . ."
        ch_v "Sure."

        ch_k "Ok " + Girl.player_petname + ", go ahead."
        ch_e "Ok " + Girl.player_petname + ", go ahead."
        ch_l "Ok " + Girl.player_petname + ", go ahead."
        ch_j "Ok " + Girl.player_petname + ", go ahead."
        ch_s "Ok " + Girl.player_petname + ", go ahead."
        ch_v "Ok " + Girl.player_petname + ", go ahead."

        ch_k "Ok, whatever."
        ch_e "Mmmm, I couldn't refuse. . ."
        ch_l "Mmmm, I couldn't refuse. . ."
        ch_j "Mmmm, I couldn't refuse. . ."
        ch_s "Mmmm, I could not refuse. . ."
        ch_v "Mmmm, I couldn't refuse. . ."

        ch_k "Mmmmmm."
        ch_e "Mmmmmm. . ."
        ch_l "Mmmmmm. . ."
        ch_j "Mmmmmm. . ."
        ch_s "Mmmmmm. . ."
        ch_v "Mmmmmm. . ."

        ch_k "Oooooooh. . ."

        ch_k "Ok, go for it."
        ch_e "I can't exactly refuse. . ."
        ch_l "Yeah, ok. . ."
        ch_j "Yeah, ok. . ."
        ch_s "I suppose that is reasonable. . ."
        ch_v "Yeah, ok. . ."

        ch_k "Mmmmm. . ."

        ch_k "Wha. . ."
        ch_e "Mmm. . . naughty."
        ch_l "Mmm. . . naughty."
        ch_j "Mmm. . . naughty."
        ch_s "Mmm. . . naughty."
        ch_v "Mmm. . . naughty."

    Girl.voice "[line]"

    return

label daily_action_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Didn't get enough earlier?",
            "Maybe not so hard this time though.",
            "Maybe not so rough this time though.",
            "I'm still tingling a bit from earlier.",
            "You do have a smooth touch. . .",
            "Take it a bit gently, I'm still quivering from earlier.",
            "Again? Oh, you're insatiable!",
            "Must be my lucky day!",
            "You sure know how to keep a girl satisfied. . .",
            "Mmm. . ."]


    $ Line = renpy.random.choice(["Didn't get enough earlier?",
        "Take it easy though.",
        "Take it a bit gently, I'm still shaking from earlier.",
        "Huh? Again?",
        "I must have done something right.",
        "What a girl wants. . .",
        "Maybe not so rough this time though.",
        "Mmm. . ."]
    ch_k "[Line]"
    $ Line = renpy.random.choice(["You didn't get enough earlier?",
        "Relax, gently. . .",
        "Take it a bit gently, I'm still shaking from earlier.",
        "Huh? Again?",
        "I must have done something right.",
        "What a queen deserves. . .",
        "Perhaps not so rough this time?",
        "Mmm. . ."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["You didn't get enough earlier?",
        "Chill. . .",
        "Take it slow, I'm still shaking from earlier.",
        "Huh? Again?",
        "I must have done something right.",
        "I do like this treatment. . .",
        "Mmm, you like that? . .",
        "Mmm. . ."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["You didn't get enough earlier?",
        "Chill. . .",
        "Take it slow, I'm still shaking from earlier.",
        "Huh? Again?",
        "I must have done something right.",
        "I do like this. . .",
        "Mmm, you like that? . .",
        "Mmm. . ."]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["You didn't get enough earlier?",
        "Relax, gently. . .",
        "Gently. . . gently. . .",
        "Take it a bit gently, I am still glowing from earlier.",
        "Huh? Again?",
        "I must have done something right.",
        "What a queen deserves. . .",
        "Perhaps not so rough this time?",
        "Mmm. . ."]
    ch_s "[Line]"
    $ Line = renpy.random.choice(["You didn't get enough earlier?",
        "Relax. . .",
        "Take it slow, I'm still shaking from earlier.",
        "Huh? Again?",
        "I must have done something right.",
        "I guess fair's fair. . .",
        "Mmm, you like that? . .",
        "Mmm. . ."]
    ch_v "[Line]"


    $ Line = renpy.random.choice(["Another one?",
        "You're going to give me calluses.",
        "Didn't get enough earlier?",
        "My hand's kinda sore from earlier.",
        "My hand's kinda sore from earlier."]
    ch_k "[Line]"
    $ Line = renpy.random.choice(["Another?",
        "You're going to wear out my arm.",
        "Didn't get enough earlier?",
        "My hand's a bit sore from earlier.",
        "My hand's rather sore from before."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Another one?",
        "I'm glad I don't grow calluses.",
        "Didn't get enough earlier?",
        "Again the with handjobs, huh?",
        "I guess you want more."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Another one?",
        "Didn't get enough earlier?",
        "Again the with handjobs, huh?",
        "I guess you want more."]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["Another?",
        "My arm will wear out.",
        "You did not get enough earlier?",
        "My hand is quite sore from earlier.",
        "My hand is rather sore from before."]
    ch_s "[Line]"
    $ Line = renpy.random.choice(["Another one?",
        "I'm glad I don't grow calluses.",
        "Didn't get enough earlier?",
        "Again the with handjobs, huh?",
        "I guess you want more."]
    ch_v "[Line]"

    $ Line = renpy.random.choice(["Back again so soon?",
        "You're going to make me sore.",
        "Didn't get enough earlier?",
        "My tits are still kinda sore from earlier."]
    ch_k "[Line]"
    $ Line = renpy.random.choice(["Back again so soon?",
        "You're going to wear them out.",
        "Didn't get enough earlier?",
        "I'm still a bit sore from earlier."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Back for more?",
        "You're really working these puppies.",
        "Didn't get enough earlier?",
        "You're really working these puppies."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Back for more?",
        "You're really working these babies.",
        "Didn't get enough earlier?",
        "You're really working these babies."]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["Back again so soon?",
        "You will wear them out like this.",
        "You did not get enough earlier?",
        "I am still a bit sore from earlier."]
    ch_s "[Line]"


    $ Line = renpy.random.choice(["Back again so soon?",
        "You're going to give me lockhee- . . . jaw.",
        "Let me get some saliva going.",
        "Didn't get enough earlier?",
        "My jaw's still a bit sore from earlier.",
        "My jaw's still a bit sore from earlier."]
    ch_k "[Line]"
    $ Line = renpy.random.choice(["Back so soon?",
        "Let me get some saliva going.",
        "Didn't get enough earlier?",
        "My jaw's still sore from our prior engagement.",
        "My jaw's still a bit sore from earlier."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Back again so soon?",
        "Wear'in me out here.",
        "I must be too good at this.",
        "Let me get some saliva going.",
        "Didn't get enough earlier?"]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Back again so soon?",
        "You're wearing me out here.",
        "I must be too good at this.",
        "Didn't get enough earlier?"]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["Back so soon?",
        "I must prepare myself.",
        "You did not get enough earlier?",
        "My jaw is still rather sore.",
        "My jaw is still recovering."]
    ch_s "[Line]"


    $ Line = renpy.random.choice(["Breaking out the toys again?",
            "Didn't get enough earlier?",
            "You're going to wear me out."]
    ch_k "[Line]"
    $ Line = renpy.random.choice(["Breaking out the toys again?",
            "Didn't get enough earlier?",
            "You're going to wear me out."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Breaking out the toys again?",
            "Didn't get enough earlier?",
            "You're going to wear me out."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Breaking out the toys again?",
            "Didn't get enough earlier?",
            "You're going to wear me out."]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["Breaking out the toys again?",
            "You did not get enough earlier?",
            "You're going to wear me out."]
    ch_s "[Line]"

    $ Line = renpy.random.choice(["Breaking out the toys again?",
            "Didn't get enough earlier?",
            "I'm still a bit sore from earlier.",
            "You're going to wear me out."]
    ch_k "[Line]"
    $ Line = renpy.random.choice(["Breaking out the toys again?",
            "Didn't get enough earlier?",
            "I'm still a bit sore from earlier.",
            "You're going to wear me out."]
    ch_l "[Line]"


    $ Line = renpy.random.choice(["Another one?",
        "You're going to give me calluses.",
        "Didn't get enough earlier?",
        "My feet are kinda sore from earlier.",
        "My feet are kinda sore from earlier."]
    ch_k "[Line]"
    $ Line = renpy.random.choice(["Another?",
        "I'd rather not get calluses.",
        "Didn't get enough earlier?",
        "My feet are rather sore from earlier.",
        "My feet are rather sore from earlier."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Another?",
        "You did not get enough earlier?",
        "My feet are rather sore from earlier.",
        "My feet are rather sore from earlier."]
    ch_s "[Line]"


        $ Line = renpy.random.choice(["Back again so soon?",
                "So you'd like another round?",
                "You can't stay away from this. . .",
                "Didn't get enough earlier?",
                "You're wearing me out here!"]
        ch_k "[Line]"
        $ Line = renpy.random.choice(["Back again?",
                "You'd like another round?",
                "I suppose I am irresistible. . .",
                "Didn't get enough earlier?",
                "You're wearing me out, " + Girl.player_petname + "."]
        ch_e "[Line]"
        $ Line = renpy.random.choice(["Back again?",
                "You'd like another round?",
                "I must be better than I thought.",
                "Didn't get enough earlier?",
                "Your funeral, " + Girl.player_petname + "."]
        ch_l "[Line]"
        $ Line = renpy.random.choice(["Back again?",
                "You'd like another round?",
                "I must be better than I thought.",
                "Didn't get enough earlier?",
                "Your funeral, " + Girl.player_petname + "."]
        ch_j "[Line]"
        $ Line = renpy.random.choice(["Back again?",
                "You would like another round?",
                "I suppose that I can be irresistible. . .",
                "Did you not get enough earlier?",
                "You are wearing me out, " + Girl.player_petname + "."]
        ch_s "[Line]"

        $ Line = renpy.random.choice(["Back again so soon?",
                "So you'd like another round?",
                "I'm still a little sore from earlier.",
                "Didn't get enough earlier?",
                "You're wearing me out here!"]
        ch_k "[Line]"
        $ Line = renpy.random.choice(["Back again so soon?",
                "So you'd like another round?",
                "I'm still a little sore from earlier.",
                "Didn't get enough earlier?",
                "You're wearing me out, " + Girl.player_petname + "."]
        ch_e "[Line]"
        $ Line = renpy.random.choice(["Back again so soon?",
                "So you'd like another round?",
                "Again? Sure.",
                "Didn't get enough earlier?",
                "Your funeral, " + Girl.player_petname + "."]
        ch_l "[Line]"
        $ Line = renpy.random.choice(["Back again so soon?",
                "So you'd like another round?",
                "Again? Sure.",
                "Didn't get enough earlier?",
                "Your funeral, " + Girl.player_petname + "."]
        ch_j "[Line]"
        $ Line = renpy.random.choice(["Back again so soon?",
                "So you would like another round?",
                "I am still rather sore from earlier.",
                "You did not get enough earlier?",
                "You are tiring me, " + Girl.player_petname + "."]
        ch_s "[Line]"


        $ Line = renpy.random.choice(["Back again so soon?",
                "So you'd like another round?",
                "You're really digging this. . .",
                "Are you sure that's all you want?"]
        ch_k "[Line]"
        $ Line = renpy.random.choice(["Back again so soon?",
                "So you'd like another round?",
                "You're really into this. . .",
                "Are you sure that's all you want?"]
        ch_e "[Line]"
        $ Line = renpy.random.choice(["Back again so soon?",
                "So you'd like another round?",
                "You're really into this. . .",
                "Are you sure that's all you want?"]
        ch_l "[Line]"
        $ Line = renpy.random.choice(["Back again so soon?",
                "So you'd like another round?",
                "You're really into this. . .",
                "Are you sure that's all you want?"]
        ch_j "[Line]"
        $ Line = renpy.random.choice(["Back again so soon?",
                "So you would like another round?",
                "You really are into this. . .",
                "Are you sure that is all you would want?"]
        ch_s "[Line]"

    Girl.voice "[line]"

    return

label taboo_and_said_no_today_lines(Girl):
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

    ch_k "I told you not here!"
    ch_e "You've been warned."
    ch_l "I've had enough of this today."
    ch_j "I've had enough of this today."
    ch_s "This area is too public, " + Girl.player_petname + "."
    ch_v "I've had enough of this today."

    ch_k "I told you this was[Girl.like]too public!"
    ch_e "I told you I couldn't be seen like that."
    ch_l "I told you, I couldn't be caught like that."
    ch_j "I told you, I'm not comfortable in public."

    ch_k "I told you not to touch me like that in public!"
    ch_e "I told you not to touch me like that in public!"
    ch_l "I told you not to touch me like that in public!"
    ch_j "I told you not to touch me like that in public!"
    ch_s "I told you not to touch me like that in public!"
    ch_v "I told you, I couldn't be caught like that."

    ch_k "You already got your answer!"
    ch_j "You already got your answer!"
    ch_s "You already got your answer!"
    ch_v "You already got your answer!"

    ch_k "I told you that wasn't appropriate!"
    ch_e "I told you that wasn't appropriate!"
    ch_l "I told you that wasn't appropriate!"
    ch_j "I told you that wasn't appropriate!"
    ch_v "I told you that wasn't appropriate!"

    ch_k "I said not in public!"
    ch_e "I told you, this is too public!"
    ch_l "I said not in public."
    ch_j "I told you I wasn't comfortable in public. . ."
    ch_v "I said not in public."

    ch_k "This is just way too exposed!"
    ch_e "This is not an appropriate location for that. !"
    ch_l "This is just way too exposed!"
    ch_j "I don't want to show off the goods like that!"
    ch_s "This is not an appropriate location for that. !"


    ch_k "I told you, not in public!"
    ch_e "I told you, this is too public!"
    ch_l "Like I told you, not in public."
    ch_j "Like I said, not in public."
    ch_s "I told you, this is too public!"

    ch_k "Stop swinging that thing around in public!"
    ch_e "Stop showing that thing around in public!"
    ch_l "Stop swinging that thing around in public!"
    ch_j "Stop swinging that thing around in public!"
    ch_s "Stop showing that thing around in public!"

    ch_e "Stop swinging that thing around in public!"
    ch_l "Stop swinging that thing around in public!"
    ch_s "Stop swinging that thing around in public!"

    ch_e "I refuse to do this in public."
    ch_l "I said not in public."
    ch_j "I told you I wasn't comfortable in public. . ."
    ch_s "I refuse to do this in public."

    ch_k "I already told you. . .not in public!"
    ch_e "I already told you this is too public!"
    ch_l "I told you. . . this place is too exposed."
    ch_j "I'm not comfortable with that. . ."
    ch_s "I have already informed you. . . not in such an exposed location."

    ch_j "I'm not comfortable with that. . ."
    ch_s "I have already informed you. . . not in such an exposed location."

    ch_k "I{i}just{/i}[Girl.like]told, not in public!"
    ch_e "I just told you. . .not in such an exposed location."
    ch_l "I just told you. . .not in such an exposed location."
    ch_j "I just told you. . .not in such an exposed location."
    ch_s "I just informed you. . .not in such an exposed location."

    Girl.voice "[line]"

    return

label said_no_today_lines(Girl):
    if Girl == RogueX:
        $ lines = ["I already told you \"no,\" " + Girl.player_petname + ".",
            "I already told you no, take a hint.",
            "What part of \"no\" don't you understand?",
            "I already told you \"no,\" " + Girl.player_petname + ".",
            "I told you \"no\" earlier " + Girl.player_petname + "."]

    ch_k "I[Girl.like]already told you \"no.\""
    ch_e "I believe you know my answer on this matter."
    ch_l "Don't make me tell you again today."
    ch_j "Don't ask me again today."
    ch_s "I have already told you my answer."
    ch_v "Don't make me tell you again today."

    ch_k "[Girl.Like]take a lesson, " + Girl.player_petname + "."
    ch_e "I believe you know my answer on this matter."

    ch_s "I believe you know my answer on this matter."

    ch_e "I told you \"no,\" " + Girl.player_petname + "."
    ch_l "I told you \"no,\" " + Girl.player_petname + "."
    ch_j "I told you \"no,\" " + Girl.player_petname + "."
    ch_s "You will need to accept a \"no\", " + Girl.player_petname + "."
    ch_v "I told you \"no,\" " + Girl.player_petname + "."

    ch_e "I already refused, " + Girl.player_petname + "."
    ch_l "I already told you \"no,\" " + Girl.player_petname + "."
    ch_j "I already told you \"no,\" " + Girl.player_petname + "."
    ch_s "I already refused, " + Girl.player_petname + "."


    ch_k "I told you \"no,\" " + Girl.player_petname + "."
    ch_e "I told you \"no,\" " + Girl.player_petname + "."
    ch_l "Told you \"no,\" " + Girl.player_petname + "."
    ch_j "Told you \"no,\" " + Girl.player_petname + "."
    ch_s "I told you \"no,\" " + Girl.player_petname + "."

    ch_k "I already told you \"no,\" " + Girl.player_petname + "."
    ch_e "I already told you \"no,\" " + Girl.player_petname + "."
    ch_l "I already told you \"no,\" " + Girl.player_petname + "."
    ch_j "I already told you \"no,\" " + Girl.player_petname + "."
    ch_s "I already told you \"no,\" " + Girl.player_petname + "."

    ch_e "I said \"no,\" " + Girl.player_petname + "."
    ch_l "I told you \"no,\" " + Girl.player_petname + "."
    ch_j "I told you \"no,\" " + Girl.player_petname + "."
    ch_s "I said \"no,\" " + Girl.player_petname + "."

    ch_k "I already[Girl.like]told you \"no.\""
    ch_e "I believe I just told you \"no,\" " + Girl.player_petname + "."
    ch_l "I just told you \"no.\""
    ch_j "Not today."
    ch_s "I believe that I just told you \"no,\" " + Girl.player_petname + "."


    ch_l "I just told you \"no.\""
    ch_j "Not today."
    ch_s "I believe that I just told you \"no,\" " + Girl.player_petname + "."


    ch_k "I{i}just{/i}[Girl.like]told you \"no\" earlier!"
    ch_l "I'm believe I just told you \"no,\" " + Girl.player_petname + "."
    ch_j "I'm believe I just told you \"no,\" " + Girl.player_petname + "."
    ch_s "I believe that I just told you \"no,\" " + Girl.player_petname + "."

    Girl.voice "[line]"

    return

label forced_action_rejected_lines(Girl):
    if Girl == RogueX:
        $ lines = ["I don't want you touching me.",
            "I don't want your lips on me.",
            "Um, no way.",
            "Not even, " + Girl.player_petname + ".",
            "Not even that much.",
            "Stay out of my pants, " + Girl.player_petname + ".",
            "Hands off the booty!",
            "Ew, no way.",
            "I'm not that kind of girl!",
            "Not even with my feet.",
            "That isn't something I'd want!",
            "I'm not going to let you use that on me.",
            "I'm not doing that just because you have me over a barrel.",
            "That's a bit much, even for you.",
            "Even that's not worth it."]


    ch_k "Not even."
    ch_e "Don't push your luck."
    ch_l "No."
    ch_j "No."
    ch_s "You go too far."
    ch_v "No."

    ch_k "[Girl.Like]get your mouth away from me."
    ch_e "Not worth it."
    ch_l "Not worth it."
    ch_j ". . . no, not worth it."
    ch_v "Suck yourself."

    ch_k "Keep away from my kitty, " + Girl.player_petname + "."
    ch_e "I don't think so, " + Girl.player_petname + "."
    ch_l "I don't think so, " + Girl.player_petname + "."
    ch_j "I don't think so, " + Girl.player_petname + "."

    ch_v "I don't think so, " + Girl.player_petname + "."

    ch_k "Back off!"
    ch_e "Do you want to keep those fingers?"
    ch_l "Do you want to keep those fingers?"
    ch_j "Mmmm, no."
    ch_v "Do you want to keep those fingers?"

    ch_k "Um, no way."
    ch_e "I'm not going that far today."
    ch_l "I'm not going there today."
    ch_j "I'm not going there today."
    ch_v "I'm not going there today."

    ch_k "Ew, no way."
    ch_e "I don't think so."
    ch_l "I don't think so."
    ch_j "I don't think so."
    ch_v "I don't think so."


    $ Girl.change_face("_angry", 1)
    ch_k "Not even if you had a ten foot pole."
    $ Girl.change_face("_surprised", 2)
    ch_k "I mean. . ."
    $ Girl.change_face("_angry", 1)
    ch_k "You know what I mean!"

    ch_e "Even that is asking too much."
    ch_l "No."
    ch_j "No."
    ch_s "I am not comfortable with that."

    ch_k "No, that's just weird."
    ch_e "I couldn't put you through that."
    ch_l "No, try something else."
    ch_j "No, try something else."
    ch_s "I do not wish to do this."


    ch_k "I just can't do that!"
    ch_e "You go too far!"
    ch_l "That's just pushing it."
    ch_j "I'm not doing that."

    ch_e "I'm not going to let you use that on me."
    ch_l "I'm not going to let you use that on me."
    ch_j "I'm not going to let you use that on me."
    ch_s "I'm not going to let you use that on me."

    ch_k "I'm not going to let you use that on me."

    ch_k "I don't even want to step on it."
    ch_e "You really don't want my heels near your manhood."
    ch_l "You understand that I have claws down there too. . ."
    ch_j "Don't push it. . ."
    ch_s "Do not tempt me to show you what my feet can do."

    ch_k "Not even."
    ch_e "Don't overestimate your leverage here."
    ch_l "I'm over taking orders."
    ch_j "I'm the queen here!"
    ch_s "Do not overestimate your power here."

    ch_k "That's a bit much, even for you."
    ch_e "You're really shooting for the fences on that one."
    ch_l "You're going too far."
    ch_j "You're overestimating your power here."
    ch_s "You certainly are not wasting your shot."

    ch_k "Yeah, not happening."
    ch_e "I just don't see the benefit."
    ch_l "There's no point trying."
    ch_j "There's no point trying."
    ch_s "I just do not understand the benefit."

    Girl.voice "[line]"

    return


label try_something_else_lines(Girl):
    if Girl == RogueX:
        $ lines = ["I know you're having fun, but maybe we could try something else " + Girl.player_petname + ".",
            "" + Girl.player_petname + " this is getting uncomfortable, maybe we could try something else.",
            "" + Girl.player_petname + " this is nice, but could we do something else?",
            "" + Girl.player_petname + " I know you're having fun down there, but maybe we could try something else."]

    Girl.voice "[line]"

    return

label this_is_boring_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Well if that's your attitude, I don't need your \"help\"."]

    ch_k "Fun for you maybe, I'm tired of it."

    ch_e "You may be enjoying yourself, but I'm getting a bit sore."
    ch_l "Well, I've got better things to be doing."
    ch_j "Well, I've got better things to be doing."
    ch_s "Well however much you are enjoying yourself, I need to take a break."
    ch_v "This is kinda boring. . ."

    ch_l "I'm kinda bored here."
    ch_j "Well -I'm- bored."

    ch_e "Well perhaps you are enjoying yourself, but I'm tired of this."

    ch_e "No, I think not."
    ch_l "Not with that attitude."
    ch_j "Don't overestimate yourself."
    ch_s "No, I think not."

    ch_k "Not with that attitude, mister!"
    ch_e "No, I think not."
    ch_l "Not with that attitude."
    ch_j "Don't overestimate yourself."
    ch_s "No, I think not."


    ch_k "Hey, I've got better things to do if you're[Girl.like]going to be a dick about it."
    ch_e "You know, I do have better things to do with my time than this."
    ch_l "I have better things to do with my time."
    ch_j "I have better things to do with my time."
    ch_s "Perhaps some time alone would help you better evaluate your choices."

    ch_k "Well fuck you then."
    ch_e "Then I suppose you can handle this yourself."
    ch_l "Well fuck you then."
    ch_j "Well fuck you then."
    ch_s "Then I suppose you can handle this yourself."

    ch_k "Well fuck you then."
    ch_e "Well then."
    ch_l "Well fuck you then."
    ch_j "Ok, have fun with that then."
    ch_s "Well then."

    ch_k "Well if that's your attitude, I don't need your \"help\"."
    ch_e "Well if that's your attitude, I don't need your \"help\"."
    ch_l "Well if that's your attitude, I don't need your \"help\"."
    ch_s "Well if that's your attitude, I don't need your \"help\"."

    ch_e "I do have better things I could be doing."
    ch_l "Not interested."
    ch_j "Not interested."
    ch_s "I do have better things I could be doing."

    Girl.voice "[line]"

    return

label satisfied_lines(Girl):
    if Girl == RogueX:
        $ lines = ["That was. . . nice.",
            "That was . . . real pleasant, " + Girl.player_petname + ".",
            "I . . . really liked that, " + Girl.player_petname + ".",
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
            "That was . . . interesting " + Girl.player_petname + ". We'll have to do that again sometime.",
            "That was pretty hot, " + Girl.player_petname + ", we'll have to do that again sometime.",
            "That was really great, " + Girl.player_petname + ", we'll have to do that again sometime."]

    ch_k "I hope there was[Girl.like]enough to work with."
    ch_e "I'm sure it exceeded your expectations. . ."
    ch_l "Did you enjoy that?"
    ch_j "I bet you enjoyed that."
    ch_s "That was quite fun. . ."
    ch_v "Did you like that?"

    ch_k "I hope they were enough for you. . ."
    ch_e "Delectable, weren't they."
    ch_l "That was kinda nice."
    ch_j "Well that was fun."
    ch_s "That was certainly enjoyable."
    ch_v "That was kinda nice."

    ch_k "I liked that."
    ch_e "That was. . . pleasant."
    ch_l "That was. . . interesting."
    ch_j "Well that was. . . something."
    ch_s "Thank you for that."
    ch_v "That was. . . interesting."

    ch_k "Your hand is. . . bigger than mine."
    ch_e "I do appreciate some rather. . . aggressive attention down there."
    ch_l "You're really getting into the good stuff."
    ch_j "Well, that was a nice surprise. . ."
    ch_s "You certainly. . . reached some interesting places there. . ."
    ch_v "Wow. . . that was nice. . ."

    ch_k "Was it. . . good?"
    ch_e "I could really take advantage of your services more often. . ."
    ch_l "That was a really good use of that tongue of yours."
    ch_j "You really put that tongue to work. . ."
    ch_s "You really do have a talent for that. . ."
    ch_v "You really give me a run for my money. . ."

    ch_k "Huh. . . um. . ."
    ch_e "That was. . . nice. . ."
    ch_l "That was. . . nice. . ."
    ch_j "That was. . . nice. . ."
    ch_s "That was. . . nice. . ."
    ch_v "That was. . . nice. . ."

    ch_k "That was odd. . ."
    ch_e "You certainly surprise me. . ."
    ch_l "That was kinda wild. . ."
    ch_j "That was. . . interesting. . ."
    ch_s "That one caught me by surprise. . ."
    ch_v "That was kinda weird. . ."

    ch_k "That was. . . good for you?"
    ch_e "That was. . . invigorating."
    ch_l "That was. . . interesting."
    ch_j "That was. . . interesting."
    ch_s "That was. . . certainly interesting. . ."


    ch_k "It was so warm to the touch. . ."
    ch_e "What a lovely experience. . ."
    ch_l "That was kind of. . . pleasant. . ."
    ch_j "That was kinda fun. . ."
    ch_s "That was more enjoyable than I had expected. . ."

    ch_k "That was kinda fun."
    ch_e "Mmm, was that as good for you as it was for me?"
    ch_l "That was fun."
    ch_j "OK, that was fun."
    ch_s "Mmm, I did quite enjoy that!"

    ch_k "Huh, that wasn't bad."
    ch_e "Hmm, better than I'd imagined. . ."
    ch_l "Hey, whaddaya know, that wasn't bad."
    ch_j "Mmm, yeah, that was as good as I expected. . ."
    ch_s "Hmm, that certainly was enjoyable . ."

    ch_k "Thanks for the extra hand. . ."
    ch_e "I appreciate the work you put in. . ."
    ch_l "Thanks for the extra hand. . ."
    ch_j "Thanks for the extra hand. . ."
    ch_s "I appreciate the work you put in. . ."

    ch_k "I could feel you down there. . ."
    ch_e "Your cock was so warm . ."
    ch_l "Did you like that? . ."
    ch_j "Did you enjoy that? . ."
    ch_s "That certainly was an interesting experience. . ."


    ch_k "I feel like I've been waiting[Girl.like]a million years for that."
    ch_e "I assume I rocked your entire world."
    ch_l "I can tell, I was the best you've had."
    ch_j "Blew your mind, uh?"
    ch_s "I hope that was as enjoyable for you as it was for me."

    ch_k "Anal. . . huh, who knew?"
    ch_e "You really took to that well."
    ch_l "You seem to know your way around back there."
    ch_j "Hmmm, that was nice. . ."


    ch_k "Well, did that work for you?"
    ch_e "Was that enough for you?"
    ch_l "Enough for you?"
    ch_j "I guess that could have gone worse. . ."
    ch_s "Was that satisfactory?"


    if Girl.used_to_anal:
        ch_k "That was. . . interesting. . ."
        ch_l "That was. . . interesting. . ."
        ch_j "That was. . . interesting. . ."
    else:
        ch_k "Ouch. . ."
        ch_e "That was. . . engaging. . ."
        ch_l "Ouch. . ."
        ch_j "Ouch. . ."
        ch_s "That was. . . engaging. . ."

    Girl.voice "[line]"

    return

label was_that_enough_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Was that enough for you?",
            "Did you get your jollies?",
            "Did you like the taste?",
            "Well, I hope that got your rocks off.",
            "Did that work for you?",
            "Well, I hope that was enough for you.",
            "Did you get what you needed here?",
            "Ouch.",
            "Did you get what you needed here?",
            "Did you like that?",
            "Did you like that?"]


    ch_k "Not a disappointment, right?"
    ch_e "Well you certainly hit the jackpot."
    ch_l "That worked out for you?"
    ch_j "You get what you wanted out of that?"
    ch_s "I expect you enjoyed that. . ."
    ch_v "That worked out for you?"

    ch_k "Did that satisfy you?"
    ch_e "Did you get enough?"
    ch_l "Did you get enough?"
    ch_j "Did you get enough?"
    ch_s "Did you get enough?"
    ch_v "Did you get enough?"

    ch_k "Was that enough?"
    ch_e "Was that enough?"
    ch_l "Was that enough?"
    ch_j "Was that enough?"
    ch_s "Ok, was that good?"
    ch_v "Was that enough?"

    ch_k "Did you get what you needed?"
    ch_e "Did you find what you were looking for?"
    ch_l "Did you find what you were looking for?"
    ch_j "Did you find what you were looking for?"
    ch_s "Did you enjoy that?"
    ch_v "Did you find anything in there?"

    ch_k "Well, did you like the taste?"
    ch_e "I suppose that worked out for both of us. . ."
    ch_l "I suppose we both got something out of that. . ."
    ch_j "I guess that wasn't so bad. . ."
    ch_s "That was not so bad. . ."
    ch_v "Well, that wasn't so bad. . ."

    ch_k "Did you like that?"
    ch_e "Did you enjoy that?"

    ch_j "I bet you enjoyed that."
    ch_s "Did you enjoy that?"
    ch_v "Did you like that?"

    ch_k "Well? Satisfied?"
    ch_e "Was it everything you dreamed?"

    ch_s "Did that work for you?"

    ch_k "Did that work for you?"
    ch_e "Was it all you dreamed of?"'
    ch_l "Was that good for you?"
    ch_j "Was that good for you?"

    ch_v "Was that good for you?"


    ch_k "Did that work out for you?"
    ch_e "Was that sufficient?"
    ch_l "Did that do it for you?"
    ch_j "Pretty nice, right?"
    ch_s "Did that satisfy you?"

    ch_k "Well I hope you got something out of that."
    ch_e "I hope that lived up to expectations."
    ch_l "Well I hope you got something out of that."
    ch_j "I hope that worked out for you. . ."
    ch_s "I hope that met your standards."

    ch_k "I hope you enjoyed that."
    ch_e "Was it all you dreamed of?"
    ch_l "I hope you enjoyed that."
    ch_j "Well, got what you wanted from that?"
    ch_s "Did that meet your expectations?"


    ch_e "Did you enjoy that?"
    ch_l "Did you like that?"
    ch_s "Did you enjoy that?"

    ch_k "Did that work out for you?"


    ch_j "Did that do it for you?"

    ch_k "I hope that was worth the wait."
    ch_e "I hope you enjoyed that."
    ch_l "Satisfied?"
    ch_s "I hope you found that satisfactory."

    ch_k "Ouch."
    ch_k "I guess you got what you needed?"
    ch_e "Oooh."
    ch_e "It's been a while."
    ch_l "That was pleasant."
    ch_j "That was great. . ."
    ch_s "Well. . ."
    ch_s "That was quite an experience. . ."

    ch_k "Did you like that?"

    ch_l "Did you like that?"
    ch_j "Did you like that?"
    ch_s "Did you enjoy that?"

    Girl.voice "[line]"

    return

label get_out_lines(character):
    if character == RogueX:
        $ lines = ["I don't want to deal with you right now."
            "Buzz off already."
            "I really think you should leave."]
    elif character == KittyX:
        $ lines = ["Nooope."
            "GTFO."
            "Go. Now."]
    elif character == EmmaX:
        $ lines = ["I haven't any time for this."
            "Out."
            "I think you should leave now."]
    elif character == LauraX:
        $ lines = ["Nope."
            "Fuck off."
            "Get out before we both regret it."]
    elif character == JeanX:
        $ lines = ["Out!"]
    elif character == StormX:
        $ lines = ["Get out."
            "Out. Now."]
    elif character == JubesX:
        $ lines = ["Out!"]

    character.voice "[line]"

    if character in [RogueX, KittyX, EmmaX, LauraX, JeanX, JubesX]:
        $ lines = ["" + character.Name + " pushes you back into the hall and slams the door. You head back to your room."
            "" + character.Name + " shoves you back into the hall and slams the door. You head back to your room."]
    elif character == StormX:
        $ lines = ["" + character.Name + " pushes you to the top of the stairs and slams the door. You head back to your room."]
    "[line]"

    return

label first_time_pussy_eaten_lines(Girl):
    if Girl == RogueX:
        $ lines = ["That's pretty intimate, " + Girl.player_petname + ". . ."]

    Girl.voice "[line]"

    return

label first_time_ass_eaten_lines(Girl):
    if Girl == RogueX:
        if Girl.love >= Girl.obedience and Girl.love >= Girl.inhibition:
            Girl.voice "I'm not really sure I want you lick'in down there. . ."
        elif Girl.obedience >= Girl.inhibition:
            Girl.voice "You really don't have to if you don't want to."
        else:
            $ Girl.Eyes = "_sexy"

            Girl.voice "Hmm. . . it's worth a shot. . ."

    return

label trying_to_convince_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Ok, you're probably right. . ."]


    ch_k "Oh. . . you're probably right. . ."
    ch_e "You present a compelling case. . ."
    ch_l "You make a good point. . ."
    ch_j "You make a good point. . ."
    ch_s "I. . . would. . ."
    ch_v "You make a good point. . ."

    ch_k "Ok, you're probably right. . ."
    ch_e "Ok, you're probably right. . ."
    ch_l "Ok, you're probably right. . ."
    ch_j "Ok, you're probably right. . ."
    ch_s "Well. . . I might at that. . ."
    ch_v "Um. . . maybe? . ."


    $ Line = renpy.random.choice(["That's. . . true. . .",
                "I suppose. . .",
                "That's. . . that's a good point. . ."]
    ch_k "[Line]"
    $ Line = renpy.random.choice(["I can't exactly argue with that. . .",
                "I suppose. . .",
                "You raise a good point. . ."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Yeah, probably. . .",
                "I guess. . .",
                "Good point. . ."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Yeah, probably. . .",
                "I guess. . .",
                "Good point. . ."]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["I cannot argue with that. . .",
                "I suppose you have a point. . .",
                "You do raise a worthy point. . ."]
    ch_s "[Line]"


    $ Line = renpy.random.choice(["Well, sure, stick it in.",
            "I suppose. . .",
            "You've got me there."]
    ch_k "[Line]"
    $ Line = renpy.random.choice(["Well, sure, stick it in.",
            "I suppose. . .",
            "You make a compelling argument."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Well, sure, stick it in.",
            "I suppose. . .",
            "You've got me there."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Well, sure, stick it in.",
            "I suppose. . .",
            "You've got me there."]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["Well, sure, stick it in.",
            "I suppose. . .",
            "You make a compelling argument."]
    ch_s "[Line]"


    $ Line = renpy.random.choice(["Well, sure, stick it in.",
            "I suppose. . .",
            "You've got me there."]
    ch_k "[Line]"
    $ Line = renpy.random.choice(["Very well, stick it in.",
            "I suppose. . .",
            "You make a compelling argument."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Well, sure, stick it in.",
            "I suppose. . .",
            "You've got me there."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Very well, stick it in.",
            "I suppose. . .",
            "You make a compelling argument."]
    ch_s "[Line]"


    ch_k "Ok, you're probably right. . ."
    ch_e "You're probably right. . ."
    ch_l "You're probably right. . ."
    ch_j "You're probably right. . ."
    ch_s "You may be correct. . ."
    ch_v "Um. . . maybe. . ."


    $ Line = renpy.random.choice(["I can't exactly argue with that. . .",
                "I suppose. . .",
                "You raise a good point. . ."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Yeah, probably. . .",
                "I guess. . .",
                "Good point. . ."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Yeah, sure. . .",
                "I guess. . .",
                "Good point. . ."]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["I cannot exactly argue with that. . .",
                "I suppose. . .",
                "You do raise a good point. . ."]
    ch_s "[Line]"


    $ Line = renpy.random.choice(["Well, sure, ok.",
            "I suppose. . .",
            "That's. . . that's a good point. . ."]
    ch_k "[Line]"
    $ Line = renpy.random.choice(["I can't exactly argue with that. . .",
                "I suppose. . .",
                "You raise a good point. . ."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Yeah, probably. . .",
                "I guess. . .",
                "Good point. . ."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Yeah, probably. . .",
                "I guess. . .",
                "Good point. . ."]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["I cannot exactly argue with that. . .",
                "I suppose so. . .",
                "You do raise a good point. . ."]
    ch_s "[Line]"


    $ Line = renpy.random.choice(["Well, ok, put it here.",
        "Well. . . ok.",
        "I guess.",
        "I guess, whip it out.",
        "Fine. . . [She drools a bit into her cleavage].",
        "Heh, ok."]
    ch_k "[Line]"
    $ Line = renpy.random.choice(["Well, sure, come over here.",
            "Oh, very well.",
            "Mmmmm.",
            "Fine, whip it out.",
            "Fine. . . [She drools a bit into her cleavage].",
            "Oh, all right."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Well, ok, put it here.",
        "Well. . . ok.",
        "I guess.",
        "I guess, whip it out.",
        "Fine. . . [She drools a bit into her cleavage].",
        "Heh, ok."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Well, ok, put it here.",
        "Well. . . ok.",
        "I guess.",
        "I guess, whip it out.",
        "Heh, ok."]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["Fine, come over here.",
        "Oh, very well.",
        "Mmmmm.",
        "Fine, show me.",
        "Fine. . . [She drools a bit into her cleavage].",
        "Oh, all right."]
    ch_s "[Line]"

    Girl.voice "[line]"

    return

label unconvinced_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Tsk, not this time, " + Girl.player_petname + " that just seems. . . dirty.",
            "I really don't think that I would."]


    ch_k "Um, not this time, " + Girl.player_petname + ", that's too. . ."
    ch_e "I would, but still no, " + Girl.player_petname + "."
    ch_l "I would, but still no, " + Girl.player_petname + "."
    ch_j "I would, but still no, " + Girl.player_petname + "."
    ch_s "I would, but still no, " + Girl.player_petname + "."
    ch_v "I would, but still no, " + Girl.player_petname + "."

    ch_k "I really don't think so."
    ch_e "I really don't think so."
    ch_l "I really don't think so."
    ch_j "I really don't think so."
    ch_s "I really do not think so."
    ch_v "Doubt."

    ch_k "I really don't think that I would."
    ch_e "I don't think that I would."
    ch_l "I don't think that I would."
    ch_j "I don't think that I would."
    ch_s "I do not think that I would."
    ch_v "I really doubt that. . ."

    Girl.voice "[line]"

    return

label unsatisfied_lines(Girl):
    if Girl == RogueX:
        $ lines = ["I didn't exactly get off there. . .",
            "That didn't really do it for me. . .",
            "Hmm, you seemed to get more out of that than me. . ."]


    ch_k "Could you have maybe paid more attention? . ."
    ch_e "Could you have perhaps been more attentive? . ."
    ch_l "Forgetting someone? . ."
    ch_j "I think you need to get back down there."
    ch_s "I could have used some more attention to my needs. . ."

    ch_k "Hmm, you seemed to get more out of that than me. . ."
    ch_e "Hmm, you seemed to get more out of that than I did. . ."
    ch_l "Forgetting someone? . ."
    ch_j "I think you need to get back down there."
    ch_s "I am afraid that you got more out of that than I. . ."

    ch_k "I didn't get much out of that. . ."
    ch_e "I'm afraid that didn't do much for me. . ."
    ch_l "That didn't do much for me. . ."
    ch_j "I think you need to get back down there."
    ch_s "I am afraid that did not do much for me. . ."

    Girl.voice "[line]"

    return

label starting_to_get_bored_lines(Girl):

        if Girl == RogueX:
            $ lines = ["You like how those feel, huh?",
                "You're just going at them, huh?",
                "You like how that feels, huh?",
                "What are you even doing down there?",
                "Uh, that's nice, but. . .",
                "You like it down there?"]


        ch_k "You're just going at them, huh?"
        ch_e "They really are magnificent, aren't they?"
        ch_l "Enjoying yourself?"
        ch_j "Having fun there?"
        ch_s "You really seem to enjoy those. . ."
        ch_v "Having fun?"


        ch_k "Are they keeping you satisfied?"
        ch_e "Lovely, aren't they?"
        ch_l "This is kinda nice. . ."
        ch_j "This is kinda nice. . ."
        ch_s "You really seem to enjoy those. . ."

        ch_k "You like how those feel, huh?"
        ch_e "Luxurious, yes?"
        ch_l "Kinda nice, but. . ."
        ch_j "Kinda nice, but. . ."
        ch_s "Your hands are so warm. . ."
        ch_v "Ok, but, uh. . ."

        ch_k "You like how that feels, huh?"
        ch_e "You like how that feels, huh?"
        ch_l "Mmmm, you're enjoying that, huh?"
        ch_j "Mmmm, you're enjoying that, huh?"
        ch_s "Mmmm, yes. . . deeper. . ."

        ch_k "You like it down there?"
        ch_e "Isn't it just delicious?"
        ch_l "Isn't it just delicious?"
        ch_j "Isn't it just delicious?"
        ch_s "Oh, that is delightful. . ."
        ch_v "Yeah, I like that too. . ."

        ch_k "Uh, that's nice, but. . ."
        ch_e "Mmmm I do enjoy that. . ."
        ch_l "Mmmm. . ."
        ch_j "Mmmm. . ."
        ch_s "Mmmm. . ."
        ch_v "Mmmm. . ."

        ch_k "What are you even?"
        ch_e "Ungh, You're getting going there. . ."
        ch_l "Ungh, you're really getting in there. . ."
        ch_j "Ungh, you're really getting in there. . ."
        ch_s "Ooh, watch it, watch it. . ."

        ch_e "You certainly are enthusiastic. . ."
        ch_l "You seem to be enjoying yourself. . ."
        ch_j "You seem to be enjoying yourself. . ."
        ch_s "You are quite enthusiastic. . ."

    if Girl == RogueX:
        $ lines = ["Are you getting close here? I'm getting a little sore.",
            "Are you getting close here? My jaw's getting pretty sore.",
            "What are you even doing down there?",
            "Are you getting close here? I'm getting a little sore.",
            "Are you getting close here?"]


    ch_k "Are you getting close here? I'm getting a little sore."
    ch_e "Are you getting close here? I'm getting a bit sore."
    ch_l "Are you getting close here? I'm getting bored."
    ch_j "Hey, how you doing up there? About done?"
    ch_s "Are you getting close? This is making me a bit sore. . ."

    ch_e "So are we getting close?"
    ch_l "So are we getting close?"
    ch_j "Ok, had enough yet?"
    ch_s "Are you nearly finished?"

    ch_k "So are we[Girl.like]getting close here?"
    ch_e "So are we getting close here?"
    ch_l "We getting close here?"
    ch_j "Ok, that good enough?"
    ch_s "So are you nearly finished?"

    ch_k "Are you getting close here?"
    ch_e "Are we getting close here?"
    ch_l "Are we getting close here?"
    ch_j "'bout done there?"
    ch_s "Are you nearly satisfied?"

    ch_e "What are you even doing down there?"
    ch_l "What are you even doing down there?"
    ch_j "What are you even doing down there?"
    ch_s "What are you even doing down there?"

    ch_k "What are you even doing down there?"


    if Girl.used_to_anal:
    else:
        ch_k "So are we[Girl.like]getting close here? This is not super pleasant. . ."

    Girl.voice "[line]"

    return


label definitely_bored_now_lines(Girl):

    if Girl == RogueX:
        $ lines = ["I'm getting rug-burn here " + Girl.player_petname + ". Can we do something else?",
            "I'm getting a little tired, " + Girl.player_petname + ". Can we do something else?",
            "" + Girl.player_petname + ", this is getting uncomfortable, maybe we could try something else.",
            "Ow, i'm not used to this. Mind if we take a break?",
            "Can we be done with this now? I'm getting sore."]
    if Girl == RogueX:
        $ lines = ["I'm . . .getting . . .worn out. . . here, . . " + Girl.player_petname + ".",
            "I'm kinda done with this, " + Girl.player_petname + "."]

        if Girl == RogueX:
            $ lines = ["Can we. . . do something. . . else?"]


        ch_k "Maybe we could try something else here " + Girl.player_petname + "?"
        ch_e "Perhaps we could try something else, " + Girl.player_petname + "?"
        ch_l "Maybe it's time for something else, " + Girl.player_petname + "?"
        ch_j "Maybe it's time for something else, " + Girl.player_petname + "?"
        ch_s "I am sure that is fun, but could we try something different?"
        ch_v "Could we maybe try. . . something else?"


        ch_k "You look like you're having fun there, but maybe we could[Girl.like]try something else?"
        ch_e "You certainly seem to be enjoying yourself, but perhaps we could add some variety?"
        ch_l "Maybe change things up a little?"

        ch_j "Maybe try something else?"

        ch_k "" + Girl.player_petname + ", I know you're having fun down there, but maybe we could try something else."
        ch_e "" + Girl.player_petname + ", I know you're having fun down there, but maybe we could try something else."

        ch_k "" + Girl.player_petname + ", this is nice, but could we do something else?"
        ch_e "" + Girl.player_petname + ", this is nice, but could we do something else?"


        ch_k "" + Girl.player_petname + ", this is getting kind sore, maybe we could try something else."
        ch_e "" + Girl.player_petname + ", this is getting kind sore, maybe we could try something else."


        ch_k "" + Girl.player_petname + ", this is getting weird, maybe we could try something else."
        ch_e "" + Girl.player_petname + ", this is getting weird, maybe we could try something else."
        ch_l "" + Girl.player_petname + ", could we try something different?"
        ch_j "" + Girl.player_petname + ", could we try something different?"

        ch_k "Can we[Girl.Like]be done with this now? I'm getting sore."
        ch_e "Are you certain you didn't have anything else in mind?"
        ch_l "This working for you?"
        ch_j "Nice, right?"
        ch_s "Are you certain you didn't have anything else in mind?"

        ch_k "Are you getting close here? I'm cramping up."
        ch_e "Are you about done? I'm a little tired of this."
        ch_l "Are you getting close here? I'm bored."
        ch_j "Hey, you about done up there?"
        ch_s "Are you about finished? I am growing tired of this."

        ch_k "Can we[Girl.Like]be done with this now? I'm getting sore."
        ch_e "Could we be done here, my feet are getting sore."
        ch_l "Ok, seriously, let's try something different."
        ch_j "Ok, seriously, let's try something different."
        ch_s "Could we be done here, my feet are getting sore."

        ch_k "Ouch, hand cramp, can we[Girl.like]take a break?"
        ch_e "Hmm, I'm getting a bit of a cramp here."
        ch_e "Mind if we take a break?"
        ch_l "Hmm, this is boring, can we take a break?"
        ch_j "Ok, I'm bored now. Can we try something else?"
        ch_s "Hmm, I am developing a hand cramp here."
        ch_s "Mind if we take a break?"

        ch_k "I'm getting rug-burn here " + Girl.player_petname + ". Can we do something else?"
        ch_e "I'm getting a bit worn out, could we settle this some other way?"
        ch_l "Seriously, can we do something else?"
        ch_j "Ok, seriously, can't we do something else?"
        ch_s "This is becoming uncomfortable, is there some way I could finish you off?"

        ch_k "I'm[Girl.like]totally worn out here. Can we do something else?"
        ch_e "I'm getting a bit worn out here, could we do something else?"
        ch_l "I'm getting kinda bored. Can we do something else?"
        ch_j "Ok, that's enough of that. Can we do something else?"
        ch_s "My jaw is becoming uncomfortable, could we do something else?"

            ch_k "" + Girl.player_petname + ", this is getting uncomfortable, maybe we could try something else."
        ch_e "" + Girl.player_petname + ", this is getting uncomfortable, maybe we could try something else."
        ch_l "" + Girl.player_petname + ", this is getting uncomfortable, maybe we could try something else."
        ch_j "" + Girl.player_petname + ", this is getting uncomfortable, maybe we could try something else."
        ch_s "" + Girl.player_petname + ", this is getting uncomfortable, maybe we could try something else."

            ch_k "Ouch, foot cramp, can we[Girl.like]take a break?"
            ch_e "Hmm, foot cramp, could we take a short break?"
            ch_l "Hmm, this is getting a bit boring."
            ch_j "Hmm, my feet are cramping up here. . ."
            ch_s "Hmm, foot cramp. Could we take a short break?"


        ch_k "I'm . . .getting . . kinda tired. . . here. . ."
        ch_e "I'm . . .getting . . a bit. . . tired. . . here. . ."
        ch_s "I am . . .becoming . . a bit. . . worn out. . . here. . ."

        ch_k "I'm . . .getting . . kinda tired. . . of this. . ."
        ch_e "I'm . . .getting . . a bit. . . tired. . . of this. . ."
        ch_s "This is . . .becoming . . rather. . . uncomfortable. . ."

        ch_k "Can we. . . do something. . . else?"
        ch_e "Could we. . . do something. . . else?"
        ch_l "Hey. . . could we. . . try something. . . else?"
        ch_j "Hey. . . you. . . about done. . . there?"
        ch_s "Would you mind. . . a different. . . option?"

        ch_e "Can we. . . do something. . . else?"
        ch_l "Can we. . . do something. . . else?"
        ch_j "Can we. . . do something. . . else?"
        ch_s "Could we. . . do something. . . else?"

        ch_k "This is getting a bit dull."
        ch_e "I'm a bit bored by this."
        ch_l "I'm kinda bored by this."
        ch_j "Well this is not fun."
        ch_s "I am getting rather tired of this."

    Girl.voice "[line]"

    return


label no_ass_to_mouth_lines(Girl):
    if Girl == RogueX:
        $ lines = ["No thanks, " + Girl.player_petname + ". Maybe a Handy instead?"]

    Girl.voice "[line]"

    return

label since_you_are_so_nice_lines(Girl):
    if Girl == RogueX:
        $ line = renpoy.random.choice(["Well, since you're be'in so nice about it, I guess we can give it a go. . .",
            "I guess if you really want to try it. . .",
            "I guess it doesn't feel so bad. . ."]

    Girl.voice "[line]"

    return

label daily_action_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Back again so soon?",
            "You're going to give me calluses.",
            "Another one?",
            "Breaking out the toys again?",
            "So you'd like another go?",
            "You can't stay away from this booty. . .",
            "Are you sure that's all you want?",
            "You can't stay away from this. . .",
            "Didn't get enough earlier?",
            "You're going to wear me out.",
            "I'm still a bit sore from earlier.",
            "My arm's still a bit sore from earlier.",
            "My arm's still a bit sore from earlier.",
            "My feet are a bit sore from earlier.",
            "My feet are kinda sore from earlier.",
            "My tits are still a bit sore from earlier.",
            "You're going to give me lockjaw.",
            "Let me get some saliva going.",
            "Didn't get enough earlier?",
            "My jaw's still a bit sore from earlier.",
            "My jaw's still a bit sore from earlier."]

    Girl.voice "[line]"

    return

label used_to_action_lines(Girl):
    if Girl == RogueX:
        $ lines = ["You want some of this action?",
            "So you'd like another go?",
            "You want to stick it in my pussy again?",
            "You want to stick it in my ass again?",
            "You want me ta lube up your toy?",
            "You can't stay away from this. . .",
            "You want me to slick your pole?",
            "You can't stay away from this booty.",
            "You want me to ride your pole?",
            "You wanna dip your wick?",
            "So you'd like another handy?",
            "A little. . . [fist pumping hand gestures]?",
            "You want me to grease your skids?",
            "A little tender loving care?",
            "You want me to use my feet?",
            "So you'd like another foot rub?",
            "So you'd like me to. . . [she rubs her foot along your leg]?",
            "So you'd like another foot rub?",
            "You want some of this action [jiggles her tits]?",
            "So you'd like another titjob?",
            "A little. . . bounce?",
            "You want me to pillow your crank?",
            "A little soft embrace?",
            "You want some of this action [mimes blowing]?",
            "So you'd like another blowjob?",
            "A little. . . lick?",
            "You want me to wet your willy?",
            "A little tender loving care?"]


    $ Line = renpy.random.choice(["You want some of this?",
        "So you'd like another handy?",
        "A little. . . [fist pumping hand gestures]?",
        "A little TLC?"]
    ch_k "[Line]"
    $ Line = renpy.random.choice(["You want more?",
        "So you'd like another?",
        "More of this? [fist pumping hand gestures]",
        "Oh, did you want some attention?"]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["You want some more?",
        "So you'd like another handy?",
        "You want a. . . [fist pumping hand gestures]?",
        "Another handjob?"]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["You want some more?",
        "So you'd like another handjob?",
        "You want a. . . [fist pumping hand gestures]?",
        "Another handjob?"]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["You want more?",
        "So you would like another?",
        "More of this? [fist pumping hand gestures]",
        "Oh, did you want some attention?"]
    ch_s "[Line]"
    $ Line = renpy.random.choice(["You want some more?",
        "So you'd like another handy?",
        "You want a. . . [fist pumping hand gestures]?",
        "Another handjob?"]
    ch_v "[Line]"

    $ Line = renpy.random.choice(["You want some of this action [rubs her chest]?",\
        "So you'd like another titjob?",
        "A little. . . puffpuff?",
        "A little soft embrace?"]
    $ Line = renpy.random.choice(["You want some of these? [jiggles her tits]",
        "So you'd like another titjob?",
        "A little. . . [bounces tits]?",
        "A little warm embrace?"]
    ch_k "[Line]"
    $ Line = renpy.random.choice(["You want some of this action [rubs her chest]?",
        "So you'd like another titjob?",

        "Another titjob?",
        "A little [points at her chest]?"]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["You want some of this action [rubs her chest]?",
        "So you'd like another titjob?",

        "Another titjob?",
        "A little [points at her chest]?"]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["You wish to use these? [jiggles her tits]",
        "So you would like another titjob?",
        ". . . [bounces tits]?",
        "You would like to give it a hug?"]
    ch_s "[Line]"


    $ Line = renpy.random.choice(["You want me to [mimes blowing]?",
        "So you wanna 'nother blowjob?",
        "A little. . . lick?",
        "You want me to suck you off?",
        "A little tlc?"]
    ch_k "[Line]"
    $ Line = renpy.random.choice(["You want me to [mimes blowing]?",
        "So you want another blowjob?",
        "You want me to suck you off?",
        "Are you asking if I'm hungry?"]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["You want me to [mimes blowing]?",
        "So you want another blowjob?",
        "You want me to lick you?",
        "You want me to suck you off?",
        "A little bj?"]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["You want me to [mimes blowing]?",
        "So you want another blowjob?",
        "You want me to lick you?",
        "You want me to suck you off?",
        "A BJ?"]
    ch_j "[Line]"
    $ Line = renpy.random.choice([". . . [mimes blowing]?",
        "So you would like another blowjob?",
        "You wish for me to suck you off?",
        "Are you asking if I am hungry?"]
    ch_s "[Line]"


    $ Line = renpy.random.choice(["You want some of this action?",
            "So you'd like another go?",
            "You want to stick it in my pussy again?",
            "You want me ta lube up your toy?"]
    ch_k "[Line]"
    $ Line = 0
    $ Line = renpy.random.choice(["You want some of this action?",
            "So you'd like another go?",
            "You want to stick it in my pussy again?",
            "You want me ta lube up your toy?"]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["You want some of this action?",
            "So you'd like another go?",
            "You want to stick it in my pussy again?",
            "You want me ta lube up your toy?"]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["You want some of this action?",
            "So you'd like another go?",
            "You want to stick it in my pussy again?",
            "You want me ta lube up your toy?"]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["You want some of this action?",
            "So you'd like another go?",
            "You want to stick it in my pussy again?",
            "You want me ta lube up your toy?"]
    ch_s "[Line]"


    $ Line = renpy.random.choice(["You want some of this action?",
            "So you'd like another go?",
            "You want to stick it in my ass again?",
            "You want me ta lube up your toy?"]
    ch_k "[Line]"
    $ Line = renpy.random.choice(["You want some of this action?",
            "So you'd like another go?",
            "You'd like to stick it in my ass again?",
            "You'd like me to lube up your toy?"]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["You want some of this action?",
            "So you'd like another go?",
            "You want to stick it in my ass again?",
            "You want me ta lube up your toy?"]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["You want some of this action?",
            "So you'd like another go?",
            "You'd like to stick it in my ass again?",
            "You'd like me to lube up your toy?"]
    ch_s "[Line]"


    $ Line = renpy.random.choice(["You want me to use my feet?",
        "So you'd like another foot sesh?",
        "A little. . . [she rubs her foot along your leg]?",
        "A little TLC?"]
    ch_k "[Line]"
    $ Line = renpy.random.choice(["You'd like me to use my feet again?",
        "So you'd like another footjob?",
        "Mmmm, some. . . [she rubs her foot along your leg]?",
        "A little foot rub?"]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["You want me to use my feet?",
        "So you'd like another footjob?",
        "A little. . . [she rubs her foot along your leg]?",
        "A little TLC?"]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["You want me to use my feet?",
        "So you'd like another footjob?",
        "A little. . . [she rubs her foot along your leg]?",
        "A little foot rub?"]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["You would like me to use my feet again?",
        "So you would like another footjob?",
        "Mmmm, some. . . [she rubs her foot along your leg]?",
        "A little foot rub?"]
    ch_s "[Line]"


        $ Line = renpy.random.choice(["Oooh, you want some of this?",
                "So you'd like another round?",
                "You can't stay away from this. . .",
                "You gonna make me purr?",
                "You wanna slide into me?"]
        ch_k "[Line]"
        $ Line = renpy.random.choice(["Oh, you want some of this?",
                "You'd like another round?",
                "I suppose I am irresistible. . .",
                "Do you intend to make me melt?",
                "You want me to ride you?"]
        ch_e "[Line]"
        $ Line = renpy.random.choice(["Oh, you want some of this?",
                "You'd like another round?",
                "I must be better than I thought.",
                "I hope you don't plan on wearing me out.",
                "You want to plow me?"]
        ch_l "[Line]"
        $ Line = renpy.random.choice(["Oh, you want some of this?",
                "You'd like another round?",
                "I must be better than I thought.",
                "I hope you don't plan on wearing me out.",
                "You want to fuck me?"]
        ch_j "[Line]"
        $ Line = renpy.random.choice(["Oh, did you want some of this?",
                "You wouldd like another round?",
                "I suppose that I can be irresistible. . .",
                "I could get used to this. . .",
                "Did you want me to ride you?"]
        ch_s "[Line]"

        $ Line = renpy.random.choice(["Oooh, you want some of this?",
                "So you'd like another round?",
                "I do have booty for days. . .",
                "You gonna make me purr?",
                "You wanna slide into me?"]
        ch_k "[Line]"
        $ Line = renpy.random.choice(["Oooh, you want some of this?",
                "So you'd like another round?",
                "I knew you enjoyed it. . .",
                "Do you intend to make me melt?",
                "You want me to ride you?"]
        ch_e "[Line]"
        $ Line = renpy.random.choice(["Oooh, you want some of this?",
                "So you'd like another round?",
                "I knew you enjoyed it. . .",
                "I hope you don't plan on wearing me out.",
                "You want to plow me?"]
        ch_l "[Line]"
        $ Line = renpy.random.choice(["Oooh, you want some of this?",
                "So you'd like another round?",
                "I knew you enjoyed it. . .",
                "I hope you don't plan on wearing me out.",
                "You want to plow me?"]
        ch_j "[Line]"
        $ Line = renpy.random.choice(["Oooh, you wanted some of this?",
                "So you would like another round?",
                "I knew you would enjoy it. . .",
                "You want me to ride you?"]
        ch_s "[Line]"


        $ Line = renpy.random.choice(["Oooh, you want some of this?",
                "So you'd like another round?",
                "You're really digging this. . .",
                "You want another rub?"]
        ch_k "[Line]"
        $ Line = renpy.random.choice(["Oooh, you want some of this?",
                "So you'd like another round?",
                "You're really into this. . .",
                "You want another rub?"]
        ch_e "[Line]"
        $ Line = renpy.random.choice(["Oooh, you want some of this?",
                "So you'd like another round?",
                "You're really into this. . .",
                "You want another rub?"]
        ch_l "[Line]"
        $ Line = renpy.random.choice(["Oooh, you want some of this?",
                "So you'd like another round?",
                "You're really into this. . .",
                "You want another rub?"]
        ch_j "[Line]"
        $ Line = renpy.random.choice(["Oooh, you want some of this?",
                "So you would like another round?",
                "You really are into this. . .",
                "You want another rub?"]
        ch_s "[Line]"

    Girl.voice "[line]"

    return

label auto_accepted_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Ok, " + Girl.player_petname + ", let's do this.",
            "Hmm, stick it in. . .",
            "Hmm, I've apparently got someone's attention. . ."]


    ch_k "Oh. . . game on, " + Girl.player_petname + "."
    ch_e "Mmm, if you insist, " + Girl.player_petname + "."
    ch_l "Fine by me, " + Girl.player_petname + "."
    ch_j "Oh, if you must, " + Girl.player_petname + "."
    ch_s "Mmm, if you insist, " + Girl.player_petname + "."
    ch_v "Fine by me, " + Girl.player_petname + "."

    ch_k "Ooo, " + Girl.player_petname + ", toys!"
    ch_e "Hmm, " + Girl.player_petname + ", toys!"
    ch_l "Ooo, " + Girl.player_petname + ", toys!"
    ch_j "Ooo, " + Girl.player_petname + ", toys!"
    ch_s "Hmm, " + Girl.player_petname + ", toys!"

    ch_e "Mmmm, " + Girl.player_petname + ", toys. . ."
    ch_s "Mmmm, " + Girl.player_petname + ", toys. . ."


    if Girl.used_to_anal:
        "[Girl.name] is briefly startled, but melts into a sly smile."
        ch_k "Hmm, stick it in. . ."
        ch_e "Oooh, naughty boy. . ."
        ch_l "Yeah, ok. . ."
        ch_j "Oh! Sure. . ."
        ch_s "" + Girl.player_petname + ", I am surprised at you. . ."
    else:
        "[Girl.name] is briefly startled, but shrugs."
        ch_k "Oookay. . ."


    ch_k "Hmm, I've apparently got someone's attention. . ."
    ch_e "Now what shall we do with that . ."
    ch_l "Oh, what did you have in mind with that? . ."
    ch_j "Oh, what did you have in mind with that? . ."
    ch_s "Now what shall we do with that . ."

    Girl.voice "[line]"

    return

label were_done_here_lines(Girl):
    $ lines = ["[Girl.name] shoves you away and slaps you in the face.",
        "[Girl.name] shoves you away."]

    "[line]"

    if Girl == RogueX:
        $ lines = ["Jackass!{p}If that's how you want to treat me, we're done here!",
            "Dick!{p}}If that's how you want want to act, I'm out of here!"]


    "[Girl.name] shoves you away and slaps you in the face."
    ch_k "Jerk!"
    ch_k "I am not putting up with that shit!"
    ch_e "Impertinent!"
    ch_e "Do not test my patience with you."
    ch_l "Dick."
    ch_l "Don't push me."
    ch_j "Hey, I don't need my powers to hurt you."
    "[Girl.name] shoves you away and backhands you in the face."
    ch_s "That is unfortunate."
    ch_s "I am afraid that is -not- what will happen here."
    ch_v "Dick."
    ch_v "Don't push me."


    "[Girl.name] shoves you away and slaps you in the face."
    ch_k "Asshole!"
    ch_k "You need to ask nicer than that!"
    "[Girl.name] shoves you away and backhands you in the face."
    ch_e "Impertinent!"
    ch_e "You need to ask a lady first."

    ch_l "Yeah, not like that you won't."
    ch_j "Tsk tsk."

    ch_s "That is unfortunate."
    ch_s "I am afraid that is -not- what will happen here."


    "[Girl.name] shoves you away."
    ch_k "Jerk!"
    ch_k "I'm not into that!"
    ch_e "Don't push your luck, " + Girl.player_petname + "."
    ch_l "Don't push it, " + Girl.player_petname + "."
    ch_j "Don't push it, " + Girl.player_petname + "."
    ch_s "Do not go beyond yourself, " + Girl.player_petname + "."

    "[Girl.name] shoves you away and slaps you in the face."
    ch_k "Jerk!"
    ch_k "Ask nice if you want to stick something in my pussy!"
    ch_e "Ask nicely before trying anything like that!"
    ch_l "Jerk!"
    ch_l "Ask nice if you want to stick something in my pussy!"
    ch_j "Jerk!"
    ch_j "Ask nice if you want to stick something in my pussy!"
    ch_s "Ask nicely before trying anything like that!"

    "[Girl.name] shoves you away and slaps you in the face."
    ch_k "Jerk!"
    ch_k "Ask nice if you want to stick something in my ass!"
    ch_e "Ask nicely if you want to stick something in my ass!"
    ch_l "Jerk!"
    ch_l "Ask nice if you want to stick something in my ass!"
    ch_j "Jerk!"
    ch_j "Ask nice if you want to stick something in my ass!"
    ch_s "Ask nicely if you want to stick something in my ass!"

    Girl.voice "[line]"

    return

label knows_her_place_lines(Girl):
    $ lines = ["[Girl.name] doesn't seem to be into this, but she knows her place.",
        "[Girl.name] doesn't seem to be into this, you're lucky she's so obedient."]

    "[line]"

    return

label not_ready_to_stop_lines(Girl):
    $ lines = ["She continues to shake a little with pleasure.",
        "She is breathing heavily as your cock rubs inside her.",
        "She slowly turns back towards you and smiles.",
        "She doesn't seem ready to stop."]

    "[line]"

    return

label first_action_approval_lines(Girl):
    $ lines = ["Hmm, could be fun. . .",
        "Sure. . .",
        "Heh, might be fun.",
        "I guess. . .",
        "I guess it could be fun with a partner. . .",
        "Hmm, I've always wanted to try it. . .",
        "Hmm, it has been on my list. . .",
        "Hmm, you look ready for it, at least. . ."]


    ch_k "That's kinda gross. . ."
    ch_e "Hm, I didn't know that's what you were into."
    ch_l "Hm, I didn't know that's what you were into."
    ch_j "Mmmm, you're into that?"
    ch_s "Hmmm, an interesting proposal. . ."
    ch_v "Hm, I hadn't thought. . ."


    ch_k "I guess. . ."

    ch_l "Hmm. . ."
    ch_j "Hmm. . ."
    ch_s "I suppose. . ."
    ch_v "Hmm. . ."

    ch_k "Hadn't really considered that."
    ch_e "Hmm, I was wondering when you'd ask. . ."
    ch_l "Sounds fun. . ."
    ch_j "Sounds fun, but. . ."
    ch_s "Hmm, I was expecting you to ask. . ."


    ch_k "[Girl.Like]sure. . ."
    ch_e "I suppose. . ."
    ch_l "Huh. . ."
    ch_j "Huh. . ."
    ch_s "I suppose. . ."

    ch_k "I guess it could be fun with a partner. . ."
    ch_e "I guess it could be fun with a partner. . ."
    ch_l "I guess it could be fun with a partner. . ."
    ch_j "I guess it could be fun with a partner. . ."
    ch_s "I guess it could be fun with a partner. . ."

    ch_k "I guess it could be fun two-player. . ."
    ch_e "I suppose I could enjoy that. . ."
    ch_l "I guess it could be fun two-player. . ."
    ch_s "I suppose I could enjoy that. . ."

    ch_k "Sure. . ."
    ch_e "Very well. . ."
    ch_l "Sure. . ."
    ch_j "Sure. . ."
    ch_s "Very well. . ."


    ch_k "I can't say it hasn't crossed my mind. . ."
    ch_e "I was hoping you'd ask. . ."
    ch_l "I was hoping you'd ask. . ."
    ch_j "I was wondering when this would come up. . ."
    ch_s "I was hoping you would ask. . ."

    ch_k "Anything's worth a shot. . ."
    ch_e "I was getting tired of waiting. . ."
    ch_l "I was tired of waiting. . ."
    ch_j "I was tired of waiting. . ."
    ch_s "I was getting tired of waiting. . ."

    ch_k "Hmm, you look ready to go. . ."
    ch_e "Well if that's what gets you off. . ."
    ch_l "Well if that's what gets you off. . ."
    ch_j "Ok, we can start with that. . ."
    ch_s "Well if that is what satisfies you. . ."

    Girl.voice "[line]"

    return

label first_action_approval_mostly_love_lines(Girl):
    $ lines = ["Well, I've never really been able to touch people without draining them, this could be an interesting experience. . .",
        "If that's what you like. . .",
        "Huh, well that's certainly one way to get off.",
        "I've never really put something like that in my mouth. . . might be interesting.",
        "I've had a reasonable amount of experience with these, you know. . .",
        "I haven't actually used one of these, back there before. . .",
        "Well, I've never been able to do this before now, so this might be fun.",
        "I guess if you really want to try it. . .",
        "It looks like you need some relief. . ."]


    ch_k "That's, I don't know. . ."
    ch_e "Oh, are we there now?"
    ch_l "Oh, we're there now?"
    ch_j "Oh, we're there now?"
    ch_s "Oh, that is a bit forward!"
    ch_v "What? What're you talking about?"


    ch_k "I guess it could be interesting. . ."
    ch_e "I suppose you've earned something. . ."
    ch_l "You'd like that. . ."
    ch_j "Well, I guess it wouldn't be so bad. . ."
    ch_s "I might enjoy that. . ."
    ch_v "You'd like that. . ."


    ch_k "It's nice that you even thought about it."
    ch_e "I suppose you've earned something special. . ."
    ch_l "Well, maybe you deserve it."
    ch_j "I'd love to, but. . ."
    ch_s "I suppose you've earned something special. . ."


    ch_k "I have wondered what you. . . taste like."
    ch_e "I am curious if it tastes as good as it looks. . ."
    ch_l "I have wondered how you taste."
    ch_j "Well, I could hardly turn down that offer. . ."
    ch_s "I have been curious. . ."

    ch_k "I've had a reasonable amount of experience with these, you know. . ."
    ch_e "I've had a reasonable amount of experience with these, you know. . ."
    ch_l "I've had a reasonable amount of experience with these, you know. . ."
    ch_j "I've had a reasonable amount of experience with these, you know. . ."
    ch_s "I've had a reasonable amount of experience with these, you know. . ."

    ch_k "I[Girl.like]haven't actually used one of these, back there before. . ."
    ch_e "I suppose you might enjoy that. . ."
    ch_l "I haven't actually used one of these, back there before. . ."
    ch_s "I suppose you might enjoy that. . ."

    ch_k "I guess it couldn't hurt. . ."
    ch_e "I suppose it couldn't hurt. . ."
    ch_l "I guess it couldn't hurt. . ."
    ch_j "I suppose. . ."
    ch_s "I could enjoy that. . ."


    ch_k "I don't want you to think I'm some kind of slut. . ."
    ch_e "I wouldn't want you to get hurt. . ."
    ch_l "Well, you look so cute when you ask. . ."
    ch_j "I was wondering when this would come up. . ."
    ch_s "I would not want to. . . overwhelm you. . ."

    ch_k "I guess? . ."
    ch_e "I was wondering when you'd ask. . ."
    ch_l "I was hoping you'd ask. . ."
    ch_j "I was expecting this. . ."
    ch_s "I was hoping that you would ask. . ."

    ch_k "It does look a bit swollen. . ."
    ch_e "I wouldn't want to leave you. . . unattended. . ."
    ch_l "If that's what you're into. . ."
    ch_j "Ok, we can start with that. . ."
    ch_s "I would not wish to leave you. . . un-tended. . ."

    Girl.voice "[line]"

    return

label first_action_approval_mostly_obedience_lines(Girl):
    $ lines = ["If that's what you want, " + Girl.player_petname + ". . .",
        "If that's what you want. . .",
        "I suppose, if that's what you want. . .",
        "Ok, " + Girl.player_petname + ", I'm ready."]



        ch_k "You don't have to do that."
        ch_e "Is that what gets you off?"
        ch_l "Is that what gets you off?"
        ch_j "Is that what gets you off?"
        ch_s "That is what you want?"
        ch_v "Is that what gets you off?"

        ch_k "If you want, " + Girl.player_petname + ". . ."
        ch_e "If that's what you'd like, " + Girl.player_petname + ". . ."
        ch_l "If you want, " + Girl.player_petname + ". . ."

        ch_s "If that is what you want, " + Girl.player_petname + ". . ."


        ch_k "I mean. . ."
        ch_e "If that's what you want. . ."
        ch_l "If you'd like that. . ."
        ch_j "If you'd want that. . ."
        ch_s "If that is what you want. . ."


        ch_k "If you want me to. . ."
        ch_e "If that's what you want. . ."
        ch_l "If that's what you want. . ."
        ch_j "I could do that, I guess. . ."
        ch_s "If that is what you want. . ."

        ch_k "If that's what you want, " + Girl.player_petname + ". . ."
        ch_e "If that's what you want, " + Girl.player_petname + ". . ."
        ch_l "If that's what you want, " + Girl.player_petname + ". . ."
        ch_j "If that's what you want, " + Girl.player_petname + ". . ."
        ch_s "If that is what you want, " + Girl.player_petname + ". . ."

        ch_e "If you enjoy that, " + Girl.player_petname + ". . ."

        ch_j "If you want, " + Girl.player_petname + ". . ."
        ch_s "If you enjoy that, " + Girl.player_petname + ". . ."


        ch_k "I suppose if it's you, " + Girl.player_petname + ". . ."
        ch_e "If you insist, " + Girl.player_petname + ". . ."
        ch_l "Yes, " + Girl.player_petname + ". . ."
        ch_j "Ok, " + Girl.player_petname + ". . ."
        ch_s "If that is what you wish, " + Girl.player_petname + ". . ."

        ch_k "Well. . ."
        ch_e "I expected we'd get here at some point. . ."
        ch_l "I expected that. . ."
        ch_j "I expected that. . ."
        ch_s "I expected we would get here at some point. . ."

        ch_k "If you want. . ."
        ch_e "If that's what works for you. . ."
        ch_l "If that's what works for you. . ."
        ch_j "Ok, we can start with that. . ."
        ch_s "If that is what works for you. . ."

    Girl.voice "[line]"

    return

label first_action_approval_addicted_lines(Girl):
    $ lines = ["I think, if I could just touch that. . .",
        "I guess. . .",
        "I think. . . for some reason I really do want that in my mouth. . .",
        "Hmmmm. . . .",
        "Well. . . I bet it would feel really good down there."]


    ch_k "I kind of {i}need{/i} to. . ."
    ch_e "Mmmmmmmm. . ."
    ch_s "Mmmmmmmm. . ."
    ch_v "If you want, " + Girl.player_petname + ". . ."

    ch_k "Hmmmm. . . ."
    ch_e "Hmmmm. . . ."
    ch_l "Hmmmm. . . ."
    ch_j "Hmmmm. . . ."
    ch_s "Hmmmm. . . ."


    ch_k "My mouth is watering. . ."
    ch_e "I don't know if I could wait. . ."
    ch_l "[[wipes away a little drool]"
    ch_j "Mmmmm. . ."
    ch_s "I might enjoy that. . ."

    ch_k "Okay. . ."
    ch_e "Very well. . ."
    ch_l "Okay. . ."
    ch_j "Okay. . ."
    ch_s "Very well. . ."


    ch_k "I have kind of been hoping you might. . ."
    ch_e "I was wondering how it would feel with you. . ."
    ch_l "Sounds fun. . ."
    ch_j "That does sound fun. . ."
    ch_s "I was curious as to the effect that would have. . ."

    ch_k "I. . . if that's how you want to do it. . . maybe?"
    ch_e "Hmm, that would be an interesting experience. . ."
    ch_l "Hmm, sounds fun. . ."
    ch_j "Hmm, sounds fun. . ."
    ch_s "Hmm, that would certainly be interesting. . ."

    ch_k "Hmmm. . ."
    ch_e "Hrmm. . ."
    ch_l "Hrmm. . ."
    ch_j "Hrmm. . ."
    ch_s "Hrmm. . ."

    Girl.voice "[line]"

    return

label action_forcefully_approved_lines(Girl):
    $ lines = ["That's really what you want?",
        "That's it?",
        "This isn't going to become a habit, will it?",
        "You want me to do that again?",
        "The toys again?",
        "That's all you want?"]


    ch_k "That's it, right?"
    ch_e "No more than that?"
    ch_l "Nothing more than that?"
    ch_j "And that's it?"
    ch_s "Nothing more than that?"
    ch_v "Nothing more than that?"

    ch_k "This isn't going to become a habit, will it?"
    ch_e "You aren't getting used to this service, are you?"
    ch_l "You're kinda pushing it."
    ch_j "Well that's a big ask. . ."
    ch_s "You enjoy making use of these?"


    ch_k "You want me to do that again?"
    ch_e "Ugh, that again?"
    ch_l "Again?"
    ch_j "Again?"
    ch_s "Tsk, again?"

    ch_k "The toys again?"
    ch_e "The toys again?"
    ch_l "The toys again?"
    ch_j "The toys again?"
    ch_s "The toys again?"

    ch_k "That's all?"
    ch_e "That's it?"
    ch_l "That's it?"
    ch_j "That's it?"
    ch_s "That is all you want?"


    ch_k "Again? Why do you do this to me?"
    ch_e "Again? You're really wearing out your welcome."
    ch_l "I hope I don't wear you out."
    ch_j "You'll pay for this eventually. . ."
    ch_s "Oh, again?"

    ch_k "You really ask a lot here. . ."
    ch_e "You don't hold back. . ."
    ch_l "You don't hold back. . ."
    ch_j "Well you're optimistic. . ."
    ch_s "You do not restrain yourself. . ."

    ch_k "That's {i}all{/i} you want?"
    ch_e "Maybe that's going a bit too far. . ."
    ch_l "That's pushing it. . ."
    ch_j "Odd. . ."
    ch_s "Perhaps that is going a bit too far. . ."

    Girl.voice "[line]"

    return

label action_forcefully_accepted_lines(Girl):
    $ lines = ["Ok, fine.",
        ". . . Ok, if that's what you want.",
        "Well, there are worst ways to get you off. . .",
        "Whatever."]

    Girl.voice "[line]"

    ch_e "If you must. . ."
    ch_l "Going there, huh. . ."
    ch_j "Going there, huh. . ."
    ch_s "If you must. . ."
    ch_v "Going there, huh. . ."


    ch_l "If you must. . ."
    ch_j "If you must. . ."
    ch_v "If you haveta. . ."

    ch_k "Ok, geeze."
    ch_e "If you insist. . ."
    ch_l "If you insist. . ."
    ch_j "If you insist. . ."
    ch_s "If you insist. . ."
    ch_v "If you insist. . ."

    ch_l "Meh. . ."
    ch_j "Whatever. . ."

    ch_v "Meh. . ."

    ch_e "Very well."

    ch_j "Ok, fine."
    ch_s "Fine, we can do this."
    ch_v "Ok, fine."

    ch_k "Well, could be worse. . ."
    ch_e "I suppose there are worst ways to get you off. . ."
    ch_l "Well, could be worse. . ."
    ch_j "I can't fault your taste. . ."
    ch_s "I suppose this would not be too unpleasant. . ."

    ch_k "Whatever."
    ch_e "Fine."
    ch_l "Whatever."
    ch_j "Fine, let's get this over with."
    ch_s "Fine."

    ch_k "Ok, fine."
    ch_e "Ok, fine."
    ch_l "Ok, fine."
    ch_s "Ok, fine."

    ch_e "Oh, fine."
    ch_s "Oh, fine."

    ch_e "Oh, fine."
    ch_l "Ok, sure."
    ch_j "Ok, sure."
    ch_s "I supose that would be fine."

    ch_k "Ok, fiiiiine."
    ch_e "Oh, fine, if it will shut you up."
    ch_l "Ok, fine. Just make it good."
    ch_j "Ok, fine. Just make it good."
    ch_s "Oh, very well, if it will satisfy you."

    ch_e "Oh very well."
    ch_l "Whatever."
    ch_j "Whatever."
    ch_s "Oh very well."

    ch_k "Ok, fine."
    ch_e "Ok, fine."
    ch_l "Ok, fine."
    ch_j "Ok, fine."
    ch_s "Fine then."

    return

label action_done_five_times_lines(Girl):
    $ lines = ["I think I've got this well in hand.",
        "I kinda like this sensation.{p}}Never thought about touching people with my feet.",
        "I think I've got the hang of this.",
        "We're making a regular habit of this.",
        "This is. . . interesting.",
        "We're really making this a regular thing."]


    ch_k "Let me know any time you need me to give you a hand."
    ch_e "Please do call again. . ."
    ch_l "I think I've got this down, maybe I should get a punch card."
    ch_j "I'm pretty good at this, right?"
    ch_s "I have gotten used to these. . ."

    ch_k "Huh, I guess these are good for something."
    ch_e "You certainly get a lot of mileage out of these."
    ch_l "You seem to enjoy that."
    ch_j "Fun, right?"
    ch_s "You do seem to enjoy this."

    ch_k "I'm getting better at this. . . right?"
    ch_e "Best you've had, I'm sure."
    ch_l "I'm really getting the hang of this. . . right?"
    ch_j "I am loving this. You too, right?"
    ch_s "I expect that you enjoyed that."

    ch_k "Let me know any time you need me to \"foot you up.\""
    ch_e "I'm enjoying this experience."
    ch_l "I'm getting used to this. . ."
    ch_j "I'm getting used to this. . ."
    ch_s "I'm enjoying this experience."


    ch_k "Why did we not do this sooner?!"
    ch_e "We really should have done this sooner."
    ch_e "I can't imagine why I waited so long."
    ch_l "You know, this was a good idea."
    ch_j "You're pretty good at this. . ."
    ch_s "You are quite skilled at this."
    ch_s "I am glad you \"bumped into\" me."

    ch_k "I'm really starting to love this."
    ch_e "You're pretty good at that."
    ch_l "I'm glad you're into this."
    ch_j "I'm glad we have similar interests. . ."
    ch_s "You do certainly make the experience enjoyable."

    ch_k "I'm surprised how much I enjoy this."

    Girl.voice "[line]"

    return

label switching_action_lines(Girl):
    $ lines = ["Mmm, so what else did you have in mind?"]

    Girl.voice "[line]"

    return

label before_action_less_than_three_times_lines(Girl):
    $ lines = ["So you'd like another handy?",
        "Again?",
        "So you'd like another titjob?",
        "So you'd like another blowjob?",
        "You want to stick it in my pussy again?",
        "You want to stick it in my ass again?",
        "So you'd like another go?"]


    ch_k "Hmm, magic fingers. . ."
    ch_e "Enjoyed last time?. . ."
    ch_l "You seem to like this one. . ."
    ch_j "I guess you're getting used to these. . ."
    ch_s "You enjoyed it last time?. . ."
    ch_v "You seem to like this one. . ."

    ch_k "So you'd like another titjob?"
    ch_e "Hmm, another titjob?"
    ch_l "Another titjob??"
    ch_j "Again with the tits, uh?"
    ch_s "Hmm, another titjob?"

    ch_k "So you'd like another blowjob?"
    ch_e "Another blowjob?"
    ch_l "You'd like another blowjob?"
    ch_j "You'd like another blowjob?"
    ch_s "Another blowjob?"

    ch_k "You want to stick it in my pussy again?"
    ch_e "You want to stick it in my pussy again?"
    ch_l "You want to stick it in my pussy again?"
    ch_j "You want to stick it in my pussy again?"
    ch_s "You want to stick it in my pussy again?"

    ch_k "You want to stick it in my ass again?"
    ch_e "You want to stick it in my ass again?"
    ch_l "You want to stick it in my ass again?"
    ch_s "You want to stick it in my ass again?"

    ch_k "Hmm, magic toes. . ."
    ch_e "Oh, very well. . ."
    ch_l "Hmm, magic toes. . ."
    ch_j "Hmm, it is kinda fun. . ."
    ch_s "Oh, very well. . ."

    ch_k "So you'd like another round?"
    ch_e "Oh? Another round?"
    ch_l "Oh? Another round?"
    ch_j "Oh? Another round?"
    ch_s "Oh? Another round?"

    Girl.voice "[line]"

    return

label anal_insertion_not_loose_not_done_today_lines(Girl):
    if Girl == RogueX:
        $ lines = ["You could have been a bit more gentle last time, " + Girl.player_petname + ". . ."]

    ch_k "You could have been a bit more gentle last time, " + Girl.player_petname + ". . ."
    ch_l "You could have been a bit more gentle last time, " + Girl.player_petname + ". . ."


    ch_k "That was kind of. . . rough last time?"
    ch_e "Perhaps we can work up to that."
    ch_l "Maybe eventually. . ."
    ch_j "Maybe eventually. . ."
    ch_s "Perhaps we could work up to that."

    Girl.voice "[line]"

    return

label anal_insertion_not_loose_done_today_lines(Girl):
    if Girl == RogueX:
        $ lines = ["Sorry, I just need a little break back there, " + Girl.player_petname + "."]

        $ lines = ["I'm still a little sore from earlier, " + Girl.player_petname + "."]


ch_k "I'm not really over the last time, but. . ."

    ch_k "I'm still a little sore from earlier, " + Girl.player_petname + "."
    ch_v "I'm still a little sore from earlier, " + Girl.player_petname + "."
    ch_k "I'm still[Girl.like]sore from earlier. . ."
    ch_l "I'm still sore from earlier. . ."

    ch_k "Sorry, I just need a little break back there, " + Girl.player_petname + "."
    ch_l "Sorry, I just need a little break back there, " + Girl.player_petname + "."


    ch_k "I'm[Girl.like]a little sore here?"
    ch_e "Don't wear me out here."
    ch_l "Not right now."
    ch_j "Not right now."
    ch_s "Do not wear me out here."

    Girl.voice "[line]"

    return

label hard_cock_lines(Girl):
    if Girl == EmmaX:
        ch_e "My word " + Girl.player_petname + ", your member is hard enough to crack diamond. . . and I should know."
    elif Girl == LauraX:
        ch_l "Nice to see you're ready for business. . ."
    elif Girl == JeanX:
        ch_j "I see you won't need any encouragement. . ."
    elif Girl == StormX:
        ch_s "I must say " + Girl.player_petname + ", you certainly do seem to be. . . excited."

    Girl.voice "[line]"

    return

label first_time_asking_lines(Girl):
    $ lines = ["You want me to rub your cock, with my hand?",
        "Huh, so like a handy, but with my feet"
        "You want me to rub your cock with my breasts?",
        "You want me to put your dick. . . in my mouth?",
        "Hmmm, so you'd like to try out some toys?",
        "So, you'd like to take this to the next level? Actual sex? . . .",
        "Wait, so you want to stick it in my butt?!",
        "Wait, so you want to grind against my butt?!"]

    ch_k "So you want a handy then?"
    ch_e "You'd like me to take care of that for you?"
    ch_l "Handjob, huh. . ."
    ch_j "You want a handjob, hmm. . ."
    ch_s "You would like me to jerk you off?"
    ch_v "Handjob, huh. . ."
    $ Girl.blushing = "_blush1"

    ch_k "You want to rub your cock against my. . . breasts?"
    ch_e "Hmm, are you sure you can handle that, " + Girl.player_petname + "?"
    ch_l "You want a titjob, huh?"
    ch_j "Oh, you want me to put these to work. . ."
    $ Girl.change_face("_sly", 1)
    ch_j "I can't blame you. . ."
    ch_s "My breasts are really appealing to you, " + Girl.player_petname + "?"



    ch_k "You want me to suck your dick?"
    ch_e "So you'd like me to suck you off?"
    ch_l "You want me to suck your cock?"
    ch_j "Oh! You want me to suck you off?"
    ch_s "You would like me to suck on your penis?"


    ch_k "Huh, so you'd like me to touch your cock with my feet?"
    ch_e "Mmm, so you're into feet then, " + Girl.player_petname + "?"
    ch_l "Standard footjob?"
    ch_j "Oh, a foot person, eh?"
    ch_s "Oh, you would like me to use my feet, " + Girl.player_petname + "?"


    ch_k "I haven't really had much experience with this. . . "
    ch_e "Hmm, are you sure you're really prepared for this? . . "
    ch_l "Huh, you wanna fuck me? . . "
    ch_j "Oh, you wanna fuck . . "
    ch_s "Hmm, are you certain you are prepared for this? . . "


    ch_k "You want to go in the \"out\" door?!"
    ch_e "Oooh, naughty boy. Anal?"
    ch_l "Huh, anal?"
    ch_j "Oh, you're into anal?"
    ch_s "I am shocked! Anal?"


    ch_k "So, just grinding against me?"
    ch_e "You just want me to grind against you then?"
    ch_l "What, just grinding?"
    ch_j "What, just grinding?"
    ch_s "You would just like to press against each other like this?"

    ch_k "Hmmm, so you'd like to try out some toys?"
    ch_e "Hmmm, so you'd like to try out some toys?"
    ch_l "Hmmm, so you'd like to try out some toys?"
    ch_j "Hmmm, so you'd like to try out some toys?"
    ch_s "Hmmm, so you'd like to try out some toys?"

    ch_k "You want to try and fit that. . .?"
    ch_e "Hmm, you don't take half measures. . ."
    ch_l "You want to try and fit that. . .?"
    ch_s "Hmm, you don't take half measures. . ."

    Girl.voice "[line]"

    return

label first_time_forcing_lines(Girl):
    $ lines = ["I suppose there are worst things you could ask for.",
        "You had to go for the butt, uh?",
        "You'd really take it that far?",
        "Seriously?",
        ". . . That's all?"]


    ch_k "You'd really do this when you have me over a barrel?"
    ch_e "Are you sure this is how you'd like to use your.
    ch_j "Pretty bold of you. . ."
    ch_j "Pretty bold of you. . ."
    ch_s "This is what you would have me do?"


    ch_k "Anal? Really?"
    ch_e "Anal? That's your goto?"
    ch_l "Anal? That's what you're pushing for?"
    ch_j "That's the card you're going to play?"
    ch_s "Oh. Of course it would be anal."


    ch_k ". . . That's it?"
    ch_e ". . . nothing more than that?"
    ch_l ". . . nothing more?"

    ch_j ". . . nothing more?"
    if approval:
        ch_j "Which of us has a pussy here?"

    ch_s ". . . and no more than that?"

    ch_k "I suppose there are worst things you could ask for."
    ch_e "I suppose there are worst things you could ask for."
    ch_l "I suppose there are worst things you could ask for."
    ch_j "I suppose there are worst things you could ask for."
    ch_s "I suppose there are worst things you could ask for."

    ch_k "Always about the butt, huh?"
    ch_e "They always go for the butt. . ."
    ch_l "Always about the butt, huh?"
    ch_s "They always go for the butt. . ."

    Girl.voice "[line]"

    return

label mouth_not_enough(Girl):
    $ lines = ["My mouth wasn't enough?"]

    Girl.voice "[line]"

    return

label what_do_you_think_youre_doing_lines(Girl):
    $ lines = ["Hey, what do you think you're doing back there?!",
        "Hmm, kinda rude, " + Girl.player_petname + "."]

    Girl.voice "[line]"

    return

label hand_not_enough(Girl):
    $ lines = ["My hand wasn't enough?"]

    Girl.voice "[line]"

    return

label achievement_lines(Girl):
    $ lines = ["I guess you can call me \"Handi-Queen.\""
        "I guess I've gotten used to this foot thing.",
        "I'm really starting to enjoy this.",
        "I think I'm getting addicted to this.",
        "I think I'm getting addicted to this.",
        "I. . . really think I enjoy this. . ."]


    ch_k "I've kinda become[Girl.like]a \"Handi-Queen\" or something."
    ch_e "I've apparently become the \"queen\" of handjobs as well."
    ch_l "Looks like you filled out the punch card, " + Girl.player_petname + "."
    ch_j "This seems to be all we do lately. . ."
    ch_s "I seem to have become the \"queen\" of good handjobs."

    ch_k "I can't[Girl.like]get your taste out of my mind."
    ch_e "You taste positively intoxicating, " + Girl.player_petname + "."
    ch_l "Your flavor is intoxicating."
    ch_j "Wow, you know. . . I don't always love this. . ."
    $ Girl.change_face("_smile", 2)
    ch_j "but I guess with you it's different somehow. . ."
    $ Girl.blushing = "_blush1"
    ch_s "I cannot imagine how I went this long without such a delicacy, " + Girl.player_petname + "."


    ch_k "I guess I've gotten pretty smooth at the \"Kittypedi.\""
    ch_e "I'm glad that you enjoy my feet."
    ch_e "They've been trained well over the years."
    ch_l "I think I'm finally back into practice on this."
    ch_j "Hmm, this is kinda fun. . ."
    ch_s "I am glad that you convinced me to try this."
    ch_s "It feels so. . . intimate."


    ch_k "I just can't seem to quit you."
    ch_e "I seem to fit you like a glove. . ."
    ch_l "We're making this a regular thing, huh. . ."
    ch_j "Hey, I just noticed we've been doing this a lot. . ."
    ch_s "We do go well together. . ."

    ch_k "I didn't think I'd love this so much!"
    ch_e "You're one of the better partners I've had at that."
    ch_l "I think you've got a knack for that."
    ch_j "This has been fun exercise."
    ch_s "I have certainly come to enjoy this."

    ch_k "I. . . liked that a lot."
    ch_e "That was. . . pleasant."
    ch_l "That was. . . nice."
    ch_j "Ok, that was. . . fine."
    ch_s "That was. . . enjoyable."

    Girl.voice "[line]"

    return

label convinced_after_saying_no_lines(Girl):
    $ lines = ["I guess if it'll get you off. . .",
        "Fine!",
        "Hmm, I suppose. . .",
        "Oh, I suppose it isn't so bad. . .",
        "Ok, you've won me over on this one. . .",
        "Ok, ok, I have been itching for this. . .",
        "Well, I guess it's not so bad. . ."]

    Girl.voice "[line]"


    ch_e "Oh, fine!"
    ch_l "If it'll get you off my back. . ."
    ch_j "Oh, -fine-. . ."
    ch_s "Oh, very well. . ."
    ch_v "If it'll get you off my back. . ."

    ch_k "Hmm, I guess. . ."
    ch_e "Oh, very well then. . ."
    ch_l "Hmm, I guess. . ."
    ch_j "Hmm, I guess. . ."
    ch_s "Very well then. . ."

    ch_k "Ok, fine, I suppose it isn't {i}sooo{/i} bad. . ."
    ch_e "Fine, I suppose you've earned it. . ."
    ch_l "Fine. . ."
    ch_j "Fine. . ."
    ch_s "Fine, I suppose you have earned it. . ."

    ch_k "OK, geeze!"
    ch_e "Oh, very well."
    ch_l "Fine."
    ch_j "Fine."
    ch_s "Oh, very well."

    ch_k "You've made your case. . ."
    ch_e "Very well, you've convinced me. . ."
    ch_l "Ok, whatever. . ."
    ch_j "Ok, whatever. . ."
    ch_s "Very well, I am convinced. . ."

    ch_k "Well, ok, I've given it some thought, fine. . ."
    ch_e "After some consideration. . ."
    ch_e "It might be entertaining."
    ch_l "Well, if you're going to keep asking. . ."
    ch_l "Might be fun. . ."
    ch_j "Well, if you're going to keep asking. . ."
    ch_j "Might be fun. . ."
    ch_s "After some consideration. . ."
    ch_s "It might entertain me."

    ch_k "Well, I guess it's not so bad. . ."
    ch_e "It was rather entertaining. . ."
    ch_l "It was rather entertaining. . ."
    ch_j "It was fun enough. . ."
    ch_s "It was rather entertaining. . ."

    return

label accepted_without_question_lines(Girl, action):
    if Girl == RogueX:
        $ lines = ["Well. . . ok.",
            "Sure, I guess.",
            "Sure!",
            "Heh, ok, alright.",
            "Okay.",
            "Hells yeah.",
            "I guess. . .",
            "Fine. . . [She gestures for you to come over].",
            "Heh, ok, ok."]

        if action in ["fondle_pussy", "fondle_ass"]:
            $ lines.append("Well, sure, give it a rub.")

        if action == "titjob":
            $ lines.append("Fine. . . [She drools a bit into her cleavage].")

        if action == "blowjob":
            $ lines.append("Fine. . . [She licks her lips].",
                "Well, sure, ahhhhhh.",
                "Yum.")

        if action in ["sex", "anal"]:
            $ lines.append("Well, sure, stick it in.")

        if action in hand_actions:
            $ lines.append("Well, sure, put'im here.")

        if action in dildo_actions:
            $ lines.append("Well, sure, stick it in.",
                "I guess I could. . . stick it in.")

        if action in cock_actions:
            $ lines.append("I guess I could. . . whip it out.",
                "Ok, lemme see it.",
                "I suppose, drop trou.",
                "Sure, whip it out.")
    elif Girl == KittyX:
        $ lines = ["Sure, I guess.",
            "Ooooookay  .",
            "Ok. . . [She gestures for you to come over].",
            "Heh, ok, ok.",
            "Well. . . ok.",
            "Heh, ok.",
            "Sure!",
            "Um, yeah.",
            "Hells yeah.",
            "I guess we could do that.",
            "Ooooookay.",
            "Lol, ok, alright."]

        if action == "titjob":
            $ lines.append("Fine. . . [She drools a bit into her cleavage].")

        if action == "blowjob":
            $ lines.append("Yum.",
                "Ok. . . [She licks her lips].",
                "Well, sure, ahhhhhh.")

        if action in hand_actions:
            $ lines.append("Well, sure, give it a rub.")

        if action in active_actions:
            $ lines.append("You could, I guess.")

        if action in passive_actions:
            $ lines.append("I guess I could. . .")

        if action in dildo_actions:
            $ lines.append("I guess I could. . . stick it in.")

        if action in cock_actions:
            $ lines.append("Sure, whip it out.")

        if action in [dildo_actions, cock_actions]:
            $ lines.append("Cool, lemme see it.",
                "Well, sure, put it here.")

        if action in [dildo_actions, "sex", "anal"]:
            $ lines.append("Well, sure, stick it in.")
    elif Girl == EmmaX:
        $ lines = ["Oh, I suppose.",
            "Fine. . . [She gestures for you to come over].",
            "Ok, ok."]

        if action in passive_actions:
            $ lines.append("I suppose I could. . .",
                "I'll do it.")

        if action in [dildo_actions, cock_actions]:
            $ lines.append("Well, give it here.")
    elif Girl == LauraX:
        $ lines = ["Sure, I guess.",
            "O-kay.",
            "Fine.",
            "Ok. . . [She gestures for you to come over].",
            "Ok, ok."]

        if action in passive_actions:
            $ lines.append("I suppose I could. . .")
    elif Girl == JeanX:
        $ lines = ["Sure, I guess.",
            "Okay. . .   ",
            "Fine.",
            "Ok. . . Get over here. . .",
            "Ok, ok."]

        if action in passive_actions:
            $ lines.append("I suppose I could. . .")
    elif Girl == StormX:
        $ lines = ["Oh, I suppose we might.",
            ". . .Fine.[She gestures for you to come over]",
            "Ok, ok."]

        if action in passive_actions:
            $ lines.append("I would do this.",
                "I suppose that I could. . .")

        if action in [dildo_actions, cock_actions]:
            $ lines.append("Very well, give it here.")
    elif Girl = JubesX:
        $ lines = ["Sure, I guess.",
            "O-kay.",
            "Fine.",
            "Ok. . . [She gestures for you to come over].",
            "Ok, ok."]

        if action in passive_actions:
            $ lines.append("I suppose I could. . .")


    $ Line = renpy.random.choice(["Well, sure, come over here.",
        "Oh, very well.",
        "Mmmmm.",
        "Fine, whip it out.",
        "Fine. . . [She drools a bit into her cleavage].",
        "Oh, all right."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Well, sure, put it here.",
        "Well. . . ok.",
        "Yum.",
        "Sure, whip it out.",
        "Fine. . . [She drools a bit into her cleavage].",
        "Heh, ok."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Well, sure, put it here.",
        "Well. . . ok.",
        "Yum.",
        "Sure, whip it out.",
        "Heh, ok."]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["Fine, come over here.",
        "Oh, very well.",
        "Mmmmm.",
        "Fine, show me.",
        "Fine. . . [She drools a bit into her cleavage].",
        "Oh, all right."]
    ch_s "[Line]"


    $ Line = renpy.random.choice(["Well, ok.",
        "Well. . . ok.",
        "Mmmm.",
        "Sure, let me have it.",
        "Mmmm. . . [She licks her lips].",
        "Ok, fine."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Sure. Ahhhhhh.",
        "Well. . . alright.",
        "Yum.",
        "Sure, whip it out.",
        "Ok. . . [She licks her lips].",
        "Alright, let's see it."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Sure. Ahhhhhh.",
        "Well. . . alright.",
        "Yum.",
        "Sure, whip it out.",
        "Ok. . . [She licks her lips].",
        "Alright, let's see it."]
    ch_j "[Line]"
    $ Line = renpy.random.choice([". . . ok.",
        "Well. . . ok.",
        "Mmmm.",
        "Sure, let me have it.",
        "Mmmm. . . [She licks her lips].",
        "Ok, fine."]
    ch_s "[Line]"



    $ Line = renpy.random.choice(["Well, sure, stick it in.",
            "Well. . . ok.",
            "Sure!",
            "I guess I could. . . stick it in.",
            "Delightful.",
            "Hmm, ok, ok."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Well, sure, stick it in.",
            "Well. . . ok.",
            "Sure!",
            "I guess I could. . . stick it in.",
            "Hells yeah.",
            "Heh, ok, ok."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Well, sure, stick it in.",
            "Well. . . ok.",
            "Sure!",
            "I guess I could. . . stick it in.",
            "Hells yeah.",
            "Heh, ok, ok."]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["Well, sure, stick it in.",
            "Well. . . ok.",
            "Sure!",
            "I guess I could. . . stick it in.",
            "Delightful.",
            "Hmm, ok, ok."]
    ch_s "[Line]"



    $ Line = renpy.random.choice(["Well, sure, stick it in.",
            "Hmm. . . ok.",
            "Sure!",
            "I guess I could. . . stick it in.",
            "Delightful.",
            "Hmm, ok, ok."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Well, sure, stick it in.",
            "Well. . . ok.",
            "Sure!",
            "I guess I could. . . stick it in.",
            "Hells yeah.",
            "Heh, ok, ok."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Well, sure, stick it in.",
            "Hmm. . . ok.",
            "Sure!",
            "I guess I could. . . stick it in.",
            "Delightful.",
            "Hmm, ok, ok."]
    ch_s "[Line]"


    $ Line = renpy.random.choice(["Sure, I suppose.",
        "Fine.",
        "Very well, bring it out.",
        "I suppose I could. . .",
        "Fine. . . [She gestures for you to come over].",
        "Hmm, ok."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Sure, I guess.",
        "OK.",
        "Fine, lemme see it.",
        "I guess I could. . .",
        "Ok. . . [She gestures for you to come over].",
        "Heh, ok, ok."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Sure, I guess.",
        "OK.",
        "Fine, lemme see it.",
        "I guess I could. . .",
        "Ok. . . [She gestures for you to come over].",
        "Heh, ok, ok."]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["Hmm, I suppose.",
        "Fine.",
        "Very well, bring it out.",
        "I suppose that I could. . .",
        "Fine. . . [She gestures for you to come over].",
        "Hmm, ok."]
    ch_s "[Line]"


    $ Line = renpy.random.choice(["Well. . . fine, I accept.",
            "Sure!",
            "We could, I suppose.",
            "Hmmm, yes.",
            "How could I refuse?"]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Well. . . fine, let's do it.",
            "Sure.",
            "We could, I guess.",
            "Hmmm, sure.",
            "Sounds fun."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Well. . . fine, let's do it.",
            "Sure.",
            "We could, I guess.",
            "Hmmm, sure.",
            "Sounds fun."]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["Well. . . fine, I accept.",
            "Of course!",
            "We could, I suppose.",
            "Hmmm, yes.",
            "How could I refuse?"]
    ch_s "[Line]"



    $ Line = renpy.random.choice(["Well. . . ok.",
            "Sure!",
            "You could, I guess.",
            "Um, yeah.",
            "Heh, ok, ok."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Well. . . ok.",
            "Sure.",
            "You could, I guess.",
            "Um, yeah.",
            "Heh, ok, ok."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Well. . . ok.",
            "Sure.",
            "You could, I guess.",
            "Um, yeah.",
            "Heh, ok, ok."]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["Well. . . I suppose.",
            "Of course!",
            "We could, I suppose.",
            "Hmm, yes. Fine.",
            "Heh. Ok, ok."]
    ch_s "[Line]"




    $ Line = renpy.random.choice(["Well, sure, let me give it a rub.",
            "Very well.",
            "Nice!",
            "I suppose we could do that.",
            "Allow me. . .",
            "Heh, ok, ok."]
    ch_e "[Line]"
    $ Line = renpy.random.choice(["Well, sure, let me give it a rub.",
            "Very well.",
            "Nice!",
            "I guess we could do that.",
            "Ok, let me. . .",
            "Heh, ok, ok."]
    ch_l "[Line]"
    $ Line = renpy.random.choice(["Well, sure, let me give it a rub.",
            "Very well.",
            "Nice!",
            "I guess we could do that.",
            "Ok, let me. . .",
            "Heh, ok, ok."]
    ch_j "[Line]"
    $ Line = renpy.random.choice(["ery well then, let me give it a rub.",
            "Very well.",
            "Of course!",
            "I suppose that we could do that.",
            "Allow me. . .",
            "Heh, ok, ok."]
    ch_s "[Line]"

    Girl.voice "[line]"

    return

label pull_back_before_get_in_lines(Girl, action):
    if Girl == RogueX:
        if Girl.action_counter[action]:
            $ lines = ["Well ok, " + Girl.player_petname + ", no harm done. Just give me a little warning next time.",
                "Well ok, " + Girl.player_petname + ", it has been kinda fun."]
        else:
            $ lines = ["Well ok, " + Girl.player_petname + ", I'm not really ready for that, but maybe if you ask nicely next time . . ."]

            if action in anal_insertion_actions:
                $ lines.append("Well ok, " + Girl.player_petname + ", that's a bit dirty, maybe ask a girl?")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label would_you_like_more_lines(Girl):
    if Girl == RogueX:
        $ lines = ["You maybe want to try something more?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label caught_masturbating_lines(Girl):
    if Girl == RogueX:
        $ lines = []
    elif Girl == KittyX:
        $ lines = ["Eeep!{p}When did you get here?!"]
    elif Girl == EmmaX:
        $ lines = ["!{p}How long have you been there?!"]
    elif Girl == LauraX:
        $ lines = ["Huh.{p}}When did you get here?"]
    elif Girl == JeanX:
        $ lines = ["Oh, hey. . ." + Girl.player_petname + ".{p}}When did you get here?"]
    elif Girl == StormX:
        $ lines = ["!{p}}How long have you been there?!"]
    elif Girl == JubesX:
        $ lines = ["Oh!{p}}How long were you standing there?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label notices_penis_is_out_lines(Girl):
    if Girl == RogueX:
        $ lines = []
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

label too_late_to_masturbate_lines(Girl):
    if Girl == RogueX:
        $ lines = []
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

label template(Girl):
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
