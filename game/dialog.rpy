label out_of_action_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Sorry, " + Girl.Petname + " but I'm a bit worn out.",
            "I'm a bit worn out right now, " + Girl.Petname + " maybe later."])

    Girl.voice "[line]"

    return

label tired_lines(Girl):
    if Girl == RogueX:
        if not multi_action:
            $ line = renpy.random.choice(["Look, I think we can stay on this one thing. . ."])
        else:
            $ line = renpy.random.choice(["I'm actually getting a little tired, so maybe we could wrap this up?"])

    Girl.voice "[line]"

    return

label angry_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I don't want to deal with you right now."])

    Girl.voice "[line]"

    return

label go_back_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Ah, ah, Just keep doing what you were doing, " + Girl.Petname + ".",
            "Hey, just keep doing what you were doing, " + Girl.Petname + ".",
            "Hands off the merchandise, " + Girl.Petname + ".",
            "Keep it out of there, " + Girl.Petname + ".",
            "Keep it outside, " + Girl.Petname + ".",
            "Hands off, " + Girl.Petname + ".",
            "Oh! No, no thank you, " + Girl.Petname + ".",
            "Um, no, I'm not really. . . don't."])

    Girl.voice "[line]"

    return

label private_enough_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I guess this is private enough. . .",
            "Ok, I guess this is private enough. . .",
            "I guess here would be ok. . .",
            "Well, at least you got us some privacy this time. . ."])

    Girl.voice "[line]"

    return

label recent_action_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Mmm, again? Ok.",
            "Mmm, again? Let me flex my hand a bit. . .",
            "I don't want to wear them out. . .",
            "Mmm, again? Ok, let me get the girls ready.",
            "Mmm, again? [[stretches her jaw]"
            "Mmm, again? Ok, let's get to it.",
            "You want to go again? Ok.",
            "I think I'm warmed up. . ."])

    Girl.voice "[line]"

    return

label not_in_public_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I really don't think this is the right place for that!",
            "" + Girl.Petname + "! Not in public!",
            "This just really isn't the time or place, " + Girl.Petname + "!",
            "Not in such an exposed place, " + Girl.Petname + ".",
            "You really expect me to do that here? You realize how. . . exposed that would be?",
            "You really expect me to do that here?",
            "Not here!",
            "Even if I wanted to, it certainly wouldn't be here!",
            "That you would even suggest such a thing in a place like this. . .",
            "I'd be a bit embarassed doing that here."])

    Girl.voice "[line]"

    return

label already_said_not_here_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I told you not in public!",
            "I already told you this is too public!",
            "This is just way too exposed!",
            "I said not in public!",
            "Stop swinging that thing around in public!",
            "I already told you that I wouldn't do that out here!",
            "I told you that I didn't want you rubb'in up on me in public!"])

    Girl.voice "[line]"

    return

label not_ready_yet_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I just don't think I'm ready yet, " + Girl.Petname + ". . .",
            "I. . . don't think that's. . .",
            "Not now, " + Girl.Petname + ".",
            "Let's not, ok " + Girl.Petname + "?",
            "Not yet, " + Girl.Petname + ". . .",
            "Oh, um, no, I'm not really comfortable with that. . .",
            "Um, not down there, " + Girl.Petname + ". . .",
            "I don't really want to touch it, " + Girl.Petname + ". . .",
            "I'm not really up for that, " + Girl.Petname + ". . .",
            "I don't think I'd like the taste, " + Girl.Petname + ". . .",
            ". . . well I don't know about that, " + Girl.Petname + ". . .",
            "I'm just not into toys, " + Girl.Petname + ". . .",
            "I just don't think I'm ready yet, " + Girl.Petname + ". . .",
            "I'm just not into that, " + Girl.Petname + ". . .",
            "That's kinda naughty, " + Girl.Petname + ". . ."])

    Girl.voice "[line]"

    return

label no_problem_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Ok, no problem, " + Girl.Petname + ".",
            "Yeah, fine, " + Girl.Petname + ".",
            "Yeah, ok, " + Girl.Petname + ".",
            "Fine.",
            "No problem."])

    Girl.voice "[line]"

    return

label maybe_later_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I'll give it some thought, " + Girl.Petname + ".",
            "It's. . . possible, " + Girl.Petname + ".",
            "I'll be thinking about it, " + Girl.Petname + ".",
            "Anything's possible, " + Girl.Petname + ".",
            "Heh, maybe, " + Girl.Petname + ".",
            "I'll give it some thought, " + Girl.Petname + ".",
            ". . .{p}I guess?",
            "We'll have to see.",
            "I might get hungry, " + Girl.Petname + ".",
            "Maybe I'll practice on my own time, " + Girl.Petname + ".",
            "Yeah, maybe, " + Girl.Petname + "."])

    Girl.voice "[line]"

    return

label reward_politeness_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Heh, I suppose I can hardly refuse ya when you use the magic words . . .",
            "You better work your mouth that hard on these.",
            "Well, if you're gonna beg. . ."])

    Girl.voice "[line]"

    return

label please_not_good_enough_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I'm afraid not this time, sorry " + Girl.Petname + "."])

    Girl.voice "[line]"

    return

label learn_to_take_no_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Learn to take \"no\" for an answer, " + Girl.Petname + ".",
            "I just don't want to, " + Girl.Petname + ".",
            "I'aint tellin you again.",
            "Look, I already told you no thanks, " + Girl.Petname + ".",
            "Read my lips, no.",
            "Learn to take \"no\" for an answer, " + Girl.Petname + "."])

    Girl.voice "[line]"

    return

label not_happening_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Not hap'nin.",
            "Not hap'nin, " + Girl.Petname + ".",
            "No luck, " + Girl.Petname + ".",
            "Tsk, not this time, " + Girl.Petname + ".",
            "Shoo, " + Girl.Petname + ".",
            "I. . . not there!!",
            "Ew!",
            "Um, no thanks, " + Girl.Petname + ".",
            "What?! Gross!",
            "I'd really rather not.",
            "That isn't really how I planned to use my feet today"
            "How about let's not, " + Girl.Petname + ".",
            "Not interested.",
            "No way.",
            "Not happening."])

    Girl.voice "[line]"

    return

label you_had_your_shot_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Sorry, " + Girl.Petname + " you aren't touching these again.",
            "Sorry, " + Girl.Petname + " you aren't getting these in your mouth.",
            "Sorry, keep your tongue in your mouth.",
            "Sorry, hands off the booty.",
            "Fresh!",
            "I think you should keep your fingers to yourself.",
            "Sorry, keep your hands out of there.",
            "I think you can manage it yourself this time. . .",
            "Not right now, " + Girl.Petname + ". . .",
            "I think I'll let you know when I want you touching these again.",
            "I think I've got the taste out of my mouth, thanks.",
            "Sorry, you can keep your toys to yourself.",
            "Sorry, you can keep your toys out of there.",
            "Maybe you could go fuck yourself instead.",
            "Eh-eh, not anymore, " + Girl.Petname + ".",
            "The only thing you can do with my ass is kiss it, " + Girl.Petname + ".{p}. . .Don't get any ideas."])

    Girl.voice "[line]"

    return

label forced_but_not_unwelcome_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Fine, if that's what you want.",
            "Hmmph, well I guess you can go to town. . .",
            "Hmmph.",
            "Fine, I suppose.",
            "Oh. . . well, ok then. . .",
            "Well, at least make it worth it.",
            "Ok, get in there if you're so determined.",
            "Ok, fine, whip it out.",
            "Ok, fine"
            "Ok, fine. If we're going to do this, stick it in already.",
            "Ok, fine. Whatever."])

    Girl.voice "[line]"

    return

label forced_but_welcome_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Sure, get in there.",
            "Fine, grab a cheek."])

    Girl.voice "[line]"

    return

label just_told_you_no_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I {i}just{/i} told you \"no,\" " + Girl.Petname + ".",
        "I {i}just{/i} told you \"no,\" " + Girl.Petname + ".",
        "What part of \"no,\" did you not get, " + Girl.Petname + "?"])

    Girl.voice "[line]"

    return

label come_and_get_em_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Ok " + Girl.Petname + " come and get'em.",
            "Ok " + Girl.Petname + " go ahead.",
            "Oooooooh. . .",
            "God yes.",
            "Sure, grab a cheek.",
            "Sure, get in there."])

    Girl.voice "[line]"

    return

label gently_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so hard this time though.",
            "Maybe not so rough this time though.",
            "I'm still tingling a bit from earlier.",
            "You do have a smooth touch. . .",
            "Take it a bit gently, I'm still quivering from earlier.",
            "Again? Oh, you're insatiable!",
            "Must be my lucky day!",
            "You sure know how to keep a girl satisfied. . .",
            "Mmm. . ."])

    Girl.voice "[line]"

    return

label had_enough_of_this_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I told you not to touch me like that in public!",
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
            "I told you that I didn't want you rubb'in up on me in public!"])

    Girl.voice "[line]"

    return

label already_said_no_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I already told you \"no,\" " + Girl.Petname + ".",
            "I already told you no, take a hint.",
            "What part of \"no\" don't you understand?",
            "I already told you \"no,\" " + Girl.Petname + ".",
            "I told you \"no\" earlier " + Girl.Petname + "."])

    Girl.voice "[line]"

    return

label rather_not_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I'd really rather not.",
            "Oh, um, no, I'm not really comfortable with that. . .",
            "Not right now, " + Girl.Petname + ". . .",
            "Maybe not right now, ok?",
            "I don't think we need any toys, " + Girl.Petname + "."])

    Girl.voice "[line]"

    return

label went_too_far_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I don't want you touching me.",
            "I don't want your lips on me.",
            "Um, no way.",
            "Not even, " + Girl.Petname + ".",
            "Not even that much.",
            "Stay out of my pants, " + Girl.Petname + ".",
            "Hands off the booty!",
            "Ew, no way.",
            "I'm not that kind of girl!",
            "Not even with my feet.",
            "That isn't something I'd want!",
            "I'm not going to let you use that on me.",
            "I'm not doing that just because you have me over a barrel.",
            "That's a bit much, even for you.",
            "Even that's not worth it."])

    Girl.voice "[line]"

    return

label warm_hands_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["You like how those feel, huh?",
            "You're just going at them, huh?",
            "You like how that feels, huh?",
            "What are you even doing down there?",
            "Uh, that's nice, but. . .",
            "You like it down there?"])

    Girl.voice "[line]"

    return

label try_something_else_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I know you're having fun, but maybe we could try something else " + Girl.Petname + ".",
            "" + Girl.Petname + " this is getting uncomfortable, maybe we could try something else.",
            "" + Girl.Petname + " this is nice, but could we do something else?",
            "" + Girl.Petname + " I know you're having fun down there, but maybe we could try something else."])

    Girl.voice "[line]"

    return

label this_is_boring_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Well if that's your attitude, I don't need your \"help\"."])

    Girl.voice "[line]"

    return

label wrap_this_up_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["You might want to wrap this up, it's getting late."])

    Girl.voice "[line]"

    return

label time_to_stop_soon_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Seriously, it'll be time to stop soon."])

    Girl.voice "[line]"

    return

label im_done_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Ok, " + Girl.Petname + " that's enough of that for now."])

    Girl.voice "[line]"

    return

label that_was_nice_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["That was. . . nice.",
            "That was . . . real pleasant, " + Girl.Petname + ".",
            "I . . . really liked that, " + Girl.Petname + ".",
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
            "That was . . . interesting " + Girl.Petname + ". We'll have to do that again sometime.",
            "That was pretty hot, " + Girl.Petname + ", we'll have to do that again sometime.",
            "That was really great, " + Girl.Petname + ", we'll have to do that again sometime."])

    Girl.voice "[line]"

    return

label was_that_enough_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Was that enough for you?",
            "Did you get your jollies?",
            "Did you like the taste?",
            "Well, I hope that got your rocks off.",
            "Did that work for you?",
            "Well, I hope that was enough for you.",
            "Did you get what you needed here?",
            "Ouch.",
            "Did you get what you needed here?",
            "Did you like that?",
            "Did you like that?"])

    Girl.voice "[line]"

    return

label take_a_breather_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["We've been at it for a while now, let's take a breather."])

    Girl.voice "[line]"

    return

label got_some_spunk_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Oh?"])

    Girl.voice "[line]"

    return

label thats_it_for_now_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["That's it. . . for now."])

    Girl.voice "[line]"

    return

label get_out_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I don't want to deal with you right now.",
            "Buzz off already.",
            "I really think you should leave."])

    Girl.voice "[line]"

    if Girl in [RogueX, KittyX, EmmaX, LauraX, JeanX, JubesX]:
        $ line = renpy.random.choice([Girl.name + " pushes you back into the hall and slams the door. You head back to your room.",
            "" + Girl.name + " shoves you back into the hall and slams the door. You head back to your room."])

    "[line]"

    return

label first_time_pussy_eaten_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["That's pretty intimate, " + Girl.Petname + ". . ."])

    Girl.voice "[line]"

    return

label first_time_ass_eaten_lines(Girl):
    if Girl == RogueX:
        if Girl.love >= Girl.obedience and Girl.love >= Girl.inhibition:
            Girl.voice "I'm not really sure I want you lick'in down there. . ."
        elif Girl.obedience >= Girl.inhibition:
            Girl.voice "You really don't have to if you don't want to."
        else:
            $ Girl.Eyes = "sexy"

            Girl.voice "Hmm. . . it's worth a shot. . ."

    return

label ass_sore_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I'm still a little sore from earlier, " + Girl.Petname + "."])

    Girl.voice "[line]"

    return

label not_into_ass_play(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I. . . don't think that's. . ."])

    Girl.voice "[line]"

    return

label think_would_enjoy_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Ok, you're probably right. . ."])

    Girl.voice "[line]"

    return

label unconvinced_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Tsk, not this time, " + Girl.Petname + " that just seems. . . dirty.",
            "I really don't think that I would."])

    Girl.voice "[line]"

    return

label didnt_get_off_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I didn't exactly get off there. . .",
            "That didn't really do it for me. . .",
            "Hmm, you seemed to get more out of that than me. . ."])

    Girl.voice "[line]"

    return

label getting_close_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Are you getting close here? I'm getting a little sore.",
            "Are you getting close here? My jaw's getting pretty sore.",
            "What are you even doing down there?",
            "Are you getting close here? I'm getting a little sore.",
            "Are you getting close here?"])

    Girl.voice "[line]"

    return

label getting_rugburn_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I'm getting rug-burn here " + Girl.Petname + ". Can we do something else?",
            "I'm getting a little tired, " + Girl.Petname + ". Can we do something else?",
            "" + Girl.Petname + ", this is getting uncomfortable, maybe we could try something else.",
            "Ow, i'm not used to this. Mind if we take a break?",
            "Can we be done with this now? I'm getting sore."])

    Girl.voice "[line]"

    return

label done_with_this_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I'm . . .getting . . .worn out. . . here, . . " + Girl.Petname + ".",
            "I'm kinda done with this, " + Girl.Petname + "."])

    Girl.voice "[line]"

    return

label can_we_do_something_else_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Can we. . . do something. . . else?"])

    Girl.voice "[line]"

    return

label no_ass_to_mouth_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["No thanks, " + Girl.Petname + ". Maybe a Handy instead?"])

    Girl.voice "[line]"

    return

label since_you_are_so_nice_lines(Girl):
    if Girl == RogueX:
        $ line = renpoy.random.choice(["Well, since you're be'in so nice about it, I guess we can give it a go. . .",
            "I guess if you really want to try it. . .",
            "I guess it doesn't feel so bad. . ."])

    Girl.voice "[line]"

    return

label daily_action_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Back again so soon?",
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
            "My jaw's still a bit sore from earlier."])

    Girl.voice "[line]"

    return

label used_to_action_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["You want some of this action?",
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
            "A little tender loving care?"])

    Girl.voice "[line]"

    return

label lets_do_this_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Ok, [Girl.Petname], let's do this.",
            "Hmm, stick it in. . .",
            "Hmm, I've apparently got someone's attention. . ."])

    Girl.voice "[line]"

    return

label were_done_here_lines(Girl):
    $ line = renpy.random.choice(["[Girl.name] shoves you away and slaps you in the face.",
        "[Girl.name] shoves you away."])

    "[line]"

    if Girl == RogueX:
        $ line = renpy.random.choice(["Jackass!{p}If that's how you want to treat me, we're done here!",
            "Dick!{p}}If that's how you want want to act, I'm out of here!"])

    Girl.voice "[line]"

    return

label knows_her_place_lines(Girl):
    $ line = renpy.random.choice(["[Girl.name] doesn't seem to be into this, but she knows her place.",
        "[Girl.name] doesn't seem to be into this, you're lucky she's so obedient."])

    "[line]"

    return

label not_ready_to_stop_lines(Girl):
    $ line = renpy.random.choice(["She continues to shake a little with pleasure.",
        "She is breathing heavily as your cock rubs inside her.",
        "She slowly turns back towards you and smiles.",
        "She doesn't seem ready to stop."])

    "[line]"

    return

label first_action_approval_lines(Girl):
    $ line = renpy.random.choice(["Hmm, could be fun. . .",
        "Sure. . .",
        "Heh, might be fun.",
        "I guess. . .",
        "I guess it could be fun with a partner. . .",
        "Hmm, I've always wanted to try it. . .",
        "Hmm, it has been on my list. . .",
        "Hmm, you look ready for it, at least. . ."])

    Girl.voice "[line]"

    return

label first_action_approval_mostly_love_lines(Girl):
    $ line = renpy.random.choice(["Well, I've never really been able to touch people without draining them, this could be an interesting experience. . .",
        "If that's what you like. . .",
        "Huh, well that's certainly one way to get off.",
        "I've never really put something like that in my mouth. . . might be interesting.",
        "I've had a reasonable amount of experience with these, you know. . .",
        "I haven't actually used one of these, back there before. . .",
        "Well, I've never been able to do this before now, so this might be fun.",
        "I guess if you really want to try it. . .",
        "It looks like you need some relief. . ."])

    Girl.voice "[line]"

    return

label first_action_approval_mostly_obedience_lines(Girl):
    $ line = renpy.random.choice(["If that's what you want, [Girl.Petname]. . .",
        "If that's what you want. . .",
        "I suppose, if that's what you want. . .",
        "Ok, [Girl.Petname], I'm ready."])

    Girl.voice "[line]"

    return

label first_action_approval_addicted_lines(Girl):
    $ line = renpy.random.choice(["I think, if I could just touch that. . .",
        "I guess. . .",
        "I think. . . for some reason I really do want that in my mouth. . .",
        "Hmmmm. . . .",
        "Well. . . I bet it would feel really good down there."])

    Girl.voice "[line]"

    return

label action_forcefully_approved_lines(Girl):
    $ line = renpy.random.choice(["That's really what you want?",
        "That's it?",
        "This isn't going to become a habit, will it?",
        "You want me to do that again?",
        "The toys again?",
        "That's all you want?"])

    Girl.voice "[line]"

    return

label action_forcefully_accepted_lines(Girl):
    $ line = renpy.random.choice(["Ok, fine.",
        ". . . Ok, if that's what you want.",
        "Well, there are worst ways to get you off. . .",
        "Whatever."])

    Girl.voice "[line]"

    return

label after_action_five_times_lines(Girl):
    $ line = renpy.random.choice(["I think I've got this well in hand.",
        "I kinda like this sensation.{p}}Never thought about touching people with my feet.",
        "I think I've got the hang of this.",
        "We're making a regular habit of this.",
        "This is. . . interesting.",
        "We're really making this a regular thing."])

    Girl.voice "[line]"

    return

label switching_action_lines(Girl):
    $ line = renpy.random.choice(["Mmm, so what else did you have in mind?"])

    Girl.voice "[line]"

    return

label before_action_less_than_three_times_lines(Girl):
    $ line = renpy.random.choice(["So you'd like another handy?",
        "Again?",
        "So you'd like another titjob?",
        "So you'd like another blowjob?",
        "You want to stick it in my pussy again?",
        "You want to stick it in my ass again?",
        "So you'd like another go?"])

    Girl.voice "[line]"

    return

label anal_insertion_not_loose_not_done_today_lines(Girl):
    $ line = renpy.random.choice(["You could have been a bit more gentle last time, [Girl.Petname]. . ."])

    Girl.voice "[line]"

    return

label anal_insertion_not_loose_done_today_lines(Girl):
    $ line = renpy.random.choice(["Sorry, I just need a little break back there, [Girl.Petname]."])

    Girl.voice "[line]"

    return

label hard_cock_lines(Girl):
    if Girl == EmmaX:
        ch_e "My word [Girl.Petname], your member is hard enough to crack diamond. . . and I should know."
    elif Girl == LauraX:
        ch_l "Nice to see you're ready for business. . ."
    elif Girl == JeanX:
        ch_j "I see you won't need any encouragement. . ."
    elif Girl == StormX:
        ch_s "I must say [Girl.Petname], you certainly do seem to be. . . excited."

    Girl.voice "[line]"

    return

label first_time_asking_lines(Girl):
    $ line = renpy.random.choice(["You want me to rub your cock, with my hand?",
        "Huh, so like a handy, but with my feet"
        "You want me to rub your cock with my breasts?",
        "You want me to put your dick. . . in my mouth?",
        "Hmmm, so you'd like to try out some toys?",
        "So, you'd like to take this to the next level? Actual sex? . . .",
        "Wait, so you want to stick it in my butt?!",
        "Wait, so you want to grind against my butt?!"])

    Girl.voice "[line]"

    return

label first_time_forcing_lines(Girl):
    $ line = renpy.random.choice(["I suppose there are worst things you could ask for.",
        "You had to go for the butt, uh?",
        "You'd really take it that far?",
        "Seriously?",
        ". . . That's all?"])

    Girl.voice "[line]"

    return

label mouth_not_enough(Girl):
    $ line = renpy.random.choice(["My mouth wasn't enough?"])

    Girl.voice "[line]"

    return

label what_do_you_think_youre_doing_lines(Girl):
    $ line = renpy.random.choice(["Hey, what do you think you're doing back there?!",
        "Hmm, kinda rude, [Girl.Petname]."])

    Girl.voice "[line]"

    return

label hand_not_enough(Girl):
    $ line = renpy.random.choice(["My hand wasn't enough?"])

    Girl.voice "[line]"

    return

label achievement_lines(Girl):
    $ line = renpy.random.choice(["I guess you can call me \"Handi-Queen.\""
        "I guess I've gotten used to this foot thing.",
        "I'm really starting to enjoy this.",
        "I think I'm getting addicted to this.",
        "I think I'm getting addicted to this.",
        "I. . . really think I enjoy this. . ."])

    Girl.voice "[line]"

    return

label convinced_after_saying_no_lines(Girl):
    $ line = renpy.random.choice(["I guess if it'll get you off. . .",
        "Fine!",
        "Hmm, I suppose. . .",
        "Oh, I suppose it isn't so bad. . .",
        "Ok, you've won me over on this one. . .",
        "Ok, ok, I have been itching for this. . .",
        "Well, I guess it's not so bad. . ."])

    Girl.voice "[line]"

    return

label accepted_without_question_lines(Girl):
    $ line = renpy.random.choice(["Well, sure, put'im here.",
        "Well. . . ok.",
        "Well, sure, give it a rub.",
        "I suppose, drop trou.",
        "Sure, I guess.",
        "Well, sure, stick it in.",
        "Yum.",
        "Well, sure, stick it in.",
        "Sure!",
        "Sure, whip it out.",
        "Fine. . . [She drools a bit into her cleavage].",
        "Heh, ok, alright.",
        "Well, sure, ahhhhhh.",
        "Okay.",
        "I guess I could. . . stick it in.",
        "Hells yeah.",
        "Ok, lemme see it.",
        "Fine. . . [She licks her lips].",
        "I guess. . .",
        "I guess I could. . . whip it out.",
        "Fine. . . [She gestures for you to come over].",
        "Heh, ok, ok."])

    Girl.voice "[line]"

    return

label pull_back_before_get_in_lines(Girl, action):
    if Girl.action_counter[action]:
        $ line = renpy.random.choice(["Well ok, [Girl.Petname], no harm done. Just give me a little warning next time.",
            "Well ok, [Girl.Petname], it has been kinda fun."])
    else:
        $ line = renpy.random.choice(["Well ok, [Girl.Petname], I'm not really ready for that, but maybe if you ask nicely next time . . .",
            "Well ok, [Girl.Petname], that's a bit dirty, maybe ask a girl?"])

    Girl.voice "[line]"

    return

label would_you_like_more_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["You maybe want to try something more?"])

    Girl.voice "[line]"

label template(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice([""])
    elif Girl == KittyX:
        $ line = renpy.random.choice([""])
    elif Girl == EmmaX:
        $ line = renpy.random.choice([""])
    elif Girl == LauraX:
        $ line = renpy.random.choice([""])
    elif Girl == JeanX:
        $ line = renpy.random.choice([""])
    elif Girl == StormX:
        $ line = renpy.random.choice([""])
    elif Girl == JubesX:
        $ line = renpy.random.choice([""])

    Girl.voice "[line]"

    return
