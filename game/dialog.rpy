label out_of_action_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Sorry, " + Girl.Petname + " but I'm a bit worn out."
            "I'm a bit worn out right now, " + Girl.Petname + " maybe later."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Sorry, " + Girl.Petname + " but I'm a bit worn out."
            "I'm kinda tired right now, " + Girl.Petname + " later?"])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["I'm sorry, " + Girl.Petname + " but I need a break."
            "I'm rather tired right now, " + Girl.Petname + " rain check?"])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Maybe in a minute, I need a break."
            "Maybe later, " + Girl.Petname + ""])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["Gimme a minute, k?"])
    elif Girl == StormX:
        $ line = renpy.random.choice(["I am sorry, " + Girl.Petname + " I need to take a break."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["I could use a short break first."
            "Maybe later, " + Girl.Petname + ""])

    Girl.voice "[line]"

    return

label tired_lines(Girl):
    if Girl == RogueX:
        if not multi_action:
            $ line = renpy.random.choice(["Look, I think we can stay on this one thing. . ."])
        else:
            $ line = renpy.random.choice(["I'm actually getting a little tired, so maybe we could wrap this up?"])
    elif Girl == KittyX:
        if not multi_action:
            $ line = renpy.random.choice(["Let's just. . . stick with this. . ."])
        else:
            $ line = renpy.random.choice(["I kinda need a break, so if we could wrap this up?"])
    elif Girl == EmmaX:
        if not multi_action:
            $ line = renpy.random.choice(["Focus on what we're doing, " + Girl.Petname + "."])
        else:
            $ line = renpy.random.choice(["I could use a break, are you about finished here?"])
    elif Girl == LauraX:
        if not multi_action:
            $ line = renpy.random.choice(["Nah, let's just stick to this."])
        else:
            $ line = renpy.random.choice(["Maybe we could finish this up for now?"])
    elif Girl == JeanX:
        if not multi_action:
            $ line = renpy.random.choice(["I'd rather just stick to this."])
        else:
            $ line = renpy.random.choice(["Keep your eye on the prize. . ."])
    elif Girl == StormX:
        if not multi_action:
            $ line = renpy.random.choice(["I would prefer to finish this."])
        else:
            $ line = renpy.random.choice(["Why not finish off here first?"])
    elif Girl == JubesX:
        if not multi_action:
            $ line = renpy.random.choice(["Let's just keep doing this for a bit. . ."])
        else:
            $ line = renpy.random.choice(["Maybe we could wrap it up?"])

    Girl.voice "[line]"

    return

label angry_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I don't want to deal with you right now."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["I don't want to deal with you right now."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["I'd rather not deal with you at the moment."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["You really don't want to try me right now."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["You really don't want to try me right now."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["I do not want to deal with you right now."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["I'm definitely not in the mood for you right now."])

    Girl.voice "[line]"

    return

label go_back_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Ah, ah, Just keep doing what you were doing, " + Girl.Petname + "."
            "Hey, just keep doing what you were doing, " + Girl.Petname + "."
            "Hands off the merchandise, " + Girl.Petname + "."
            "Keep it out of there, " + Girl.Petname + "."
            "Keep it outside, " + Girl.Petname + "."
            "Hands off, " + Girl.Petname + "."
            "Oh! No, no thank you, " + Girl.Petname + "."
            "Um, no, I'm not really. . . don't."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Nuh-uh, " + Girl.Petname + " get back to what you were doing."
            "Heh, keep it above the belt, " + Girl.Petname + "."
            "Um, no take that out."
            "Um, don't do that. . ."
            "Hands off, " + Girl.Petname + "."
            "Oooo! Um, no, no thanks. No. . ."
            "Whoa, back off, " + Girl.Petname + "."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["Down boy, you were doing so well. . ."
            "Perhaps we keep it above the waist, " + Girl.Petname + "."
            "Careful what you put in there, you may not get it back."
            "" + Girl.Petname + "! Not now. . ."
            "Hands off, " + Girl.Petname + "."
            "I like where your head is at, so to speak, but perhaps hold off on that."
            "Whoa, back off, " + Girl.Petname + "."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Roll it back, " + Girl.Petname + ". . ."
            "Maybe we keep it above the waist, " + Girl.Petname + "."
            "Watch your hands, or lose them."
            "" + Girl.Petname + "! No. . ."
            "Hands off, " + Girl.Petname + "."
            "Hey, good instincts, but maybe hold off?"
            "Whoa, back off, " + Girl.Petname + "."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["Not so fast, " + Girl.Petname + ". . ."
            "Keep it above the waist, " + Girl.Petname + "."
            "Not so fast, " + Girl.Petname + ". . ."
            "Hmmm, not yet, " + Girl.Petname + "."
            "Whoa there, " + Girl.Petname + "!"
            "Ooo! Not right now, " + Girl.Petname + "."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["Probably not right now. . ."
            "Perhaps we keep it above the waist, " + Girl.Petname + "."
            "Careful what you put in there, you may not get it back."
            "" + Girl.Petname + "! Not now. . ."
            "Release me, " + Girl.Petname + "."
            "I appreciate the intent, but this is not the time for it."
            "You go too far, " + Girl.Petname + "."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Cool your jets, " + Girl.Petname + ". . ."
            "Maybe we keep it above the waist, " + Girl.Petname + "."
            "Watch your hands, or lose them."
            "" + Girl.Petname + "! No. . ."
            "Hands off, " + Girl.Petname + "."
            "Hey, good instincts, but maybe hold off?"
            "Whoa, back off, " + Girl.Petname + "."])

    Girl.voice "[line]"

    return

label private_enough_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I guess this is private enough. . ."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["I guess here is fine. . ."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["This does seem less. . . exposed."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["This does seem less. . . exposed."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["I guess. . . maybe we could do it here. . ."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["This is a bit more secluded."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["I guess this is less public. . ."])

    Girl.voice "[line]"

    ch_r "Ok, I guess this is private enough. . ."
    ch_r "I guess here would be ok. . ."
    ch_r "Well, at least you got us some privacy this time. . ."

    return

label recent_action_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Mmm, again? Ok."
            "Mmm, again? Let me flex my hand a bit. . ."
            "I don't want to wear them out. . ."
            "Mmm, again? Ok, let me get the girls ready."
            "Mmm, again? [[stretches her jaw]"
            "Mmm, again? Ok, let's get to it."
            "You want to go again? Ok."
            "I think I'm warmed up. . ."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Mmm, again? Ok."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["Mmmm, again? I suppose. . ."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Mmmm, again? I guess. . ."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["Mmmm, again? I guess. . ."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["Mmmm, again? I suppose. . ."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Mmmm, again? I guess. . ."])

    Girl.voice "[line]"

    return

label not_in_public_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I really don't think this is the right place for that!"
            "" + Girl.Petname + "! Not in public!"
            "This just really isn't the time or place, " + Girl.Petname + "!"
            "Not in such an exposed place, " + Girl.Petname + "."
            "You really expect me to do that here? You realize how. . . exposed that would be?"
            "You really expect me to do that here?"
            "Not here!"
            "Even if I wanted to, it certainly wouldn't be here!"
            "That you would even suggest such a thing in a place like this. . ."
            "I'd be a bit embarassed doing that here."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["I don't like being so. . . exposed."
            "Time and place, " + Girl.Petname + "!"
            "" + Girl.Petname + "! Not here!"
            "" + Girl.Petname + "! Time and place!"
            "This just really isn't the time or place, " + Girl.Petname + "!"])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["I can't be seen doing that with you."
            "I have a reputation to maintain."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["I try to stay off the radar."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["I'm. . . not comfortable. . . in public. . ."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["I should not be seen doing that."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["I don't wanna make a scene."])

    Girl.voice "[line]"

    return

label already_said_not_here_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I told you not in public!"
            "I already told you this is too public!"
            "This is just way too exposed!"
            "I said not in public!"
            "Stop swinging that thing around in public!"
            "I already told you that I wouldn't do that out here!"
            "I told you that I didn't want you rubb'in up on me in public!"])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Not here!"])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["As I said, not here, " + Girl.Petname + "."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["I told you, not here, " + Girl.Petname + "."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["I told you. . . not here, " + Girl.Petname + "."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["This area is too public, " + Girl.Petname + "."
            "As I said, not here, " + Girl.Petname + "."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["I told you, not here, " + Girl.Petname + "."])

    Girl.voice "[line]"

    return

label not_ready_yet_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I just don't think I'm ready yet, " + Girl.Petname + ". . ."
            "I. . . don't think that's. . ."
            "Not now, " + Girl.Petname + "."
            "Let's not, ok " + Girl.Petname + "?"
            "Not yet, " + Girl.Petname + ". . ."
            "Oh, um, no, I'm not really comfortable with that. . ."
            "Um, not down there, " + Girl.Petname + ". . ."
            "I don't really want to touch it, " + Girl.Petname + ". . ."
            "I'm not really up for that, " + Girl.Petname + ". . ."
            "I don't think I'd like the taste, " + Girl.Petname + ". . ."
            ". . . well I don't know about that, " + Girl.Petname + ". . ."
            "I'm just not into toys, " + Girl.Petname + ". . ."
            "I just don't think I'm ready yet, " + Girl.Petname + ". . ."
            "I'm just not into that, " + Girl.Petname + ". . ."
            "That's kinda naughty, " + Girl.Petname + ". . ."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["I'm" + Girl.Like + "not ready for that, " + Girl.Petname + ". . ."
            "Not. . . yet. . . maybe later."
            "Oh, um, no, I'm not really comfortable with that. . ."
            "Not now, " + Girl.Petname + "."
            "Oh, um, no, I'm not really comfortable with that. . ."
            "Not yet, " + Girl.Petname + ". . ."
            "Let's not, ok " + Girl.Petname + "?"
            "Um, not down there, " + Girl.Petname + ". . ."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["I highly doubt you could handle them, " + Girl.Petname + ". . ."
            "Seems a bit forward, " + Girl.Petname + "."
            "Not now, " + Girl.Petname + "."
            "Let's not, ok " + Girl.Petname + "?"
            "I'd rather not today. . ."
            "Not yet, " + Girl.Petname + ". . ."
            "I'm really not comfortable with that. . ."
            "I don't think we're there yet, " + Girl.Petname + ". . ."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Look, I don't know if we're ready for that, " + Girl.Petname + ". . ."
            "Seems a bit aggressive, " + Girl.Petname + "."
            "I'm really not cool with that. . ."
            "I'd rather not today. . ."
            "I'm not sure we're there yet, " + Girl.Petname + ". . ."
            "Not now, " + Girl.Petname + "."
            "Let's not, ok " + Girl.Petname + "?"
            "I don't think we're there yet, " + Girl.Petname + ". . ."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["Look, don't touch, " + Girl.Petname + ". . ."
            "Not now, " + Girl.Petname + "."
            "Let's not, ok " + Girl.Petname + "?"
            "Not yet, " + Girl.Petname + ". . ."
            "I'd rather not."
            "I'd rather not today. . ."
            "I don't think we're there yet, " + Girl.Petname + ". . ."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["Perhaps some other time, " + Girl.Petname + ". . ."
            "I would rather you did not, " + Girl.Petname + "."
            "Not now, " + Girl.Petname + "."
            "I am unsure about that. . ."
            "I would rather not. . ."
            "I would rather not, " + Girl.Petname + ". . ."
            "I would be uncomfortable with that. . ."
            "Perhaps go slower, " + Girl.Petname + ". . ."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Look, I don't know if we're ready for that, " + Girl.Petname + ". . ."
            "Kinda forward, " + Girl.Petname + "."
            "I'm really not cool with that. . ."
            "I'd rather not today. . ."
            "Let's not, ok " + Girl.Petname + "?"
            "Not now, " + Girl.Petname + "."
            "I don't think we're there yet, " + Girl.Petname + ". . ."])

    Girl.voice "[line]"

    return

label no_problem_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Ok, no problem, " + Girl.Petname + "."
            "Yeah, fine, " + Girl.Petname + "."
            "Yeah, ok, " + Girl.Petname + "."])
        "Fine."
        "No problem."
    elif Girl == KittyX:
        $ line = renpy.random.choice(["It's cool, " + Girl.Petname + "."
            "Yeah, ok, " + Girl.Petname + "."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["Don't concern yourself, " + Girl.Petname + "."
            "I appreciate your restraint."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["No worries."
            "It's cool."
            "It's cool, " + Girl.Petname + "."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["It's fine, I get it."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["Don't concern yourself, " + Girl.Petname + "."
            "I appreciate your restraint."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Yeah, whatever."])

    Girl.voice "[line]"

    return

label maybe_later_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I'll give it some thought, " + Girl.Petname + "."
            "It's. . . possible, " + Girl.Petname + "."
            "I'll be thinking about it, " + Girl.Petname + "."
            "Anything's possible, " + Girl.Petname + "."
            "Heh, maybe, " + Girl.Petname + "."
            "I'll give it some thought, " + Girl.Petname + "."
            ". . .{p}I guess?"
            "We'll have to see."
            "I might get hungry, " + Girl.Petname + "."
            "Maybe I'll practice on my own time, " + Girl.Petname + "."
            "Yeah, maybe, " + Girl.Petname + "."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Um, yeah, maybe later."
            "I'll give it some thought, " + Girl.Petname + "."
            "Heh, maybe, " + Girl.Petname + "."
            "Anything's possible, " + Girl.Petname + "."
            "I'll be thinking about it, " + Girl.Petname + "."
            "It's. . . possible, " + Girl.Petname + "."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["Well, I can't rule it out. . ."
            "I'll give it some thought, " + Girl.Petname + "."
            "Perhaps."
            "I'll be thinking about it, " + Girl.Petname + "."
            "It's. . . possible, " + Girl.Petname + "."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Eh. Maybe."
            "Maybe, " + Girl.Petname + "."
            "Anything's possible, " + Girl.Petname + "."
            "Maybe?"
            "It's. . . possible, " + Girl.Petname + "."])
    elif Girl == JeanX:
        $ line = renpy.random.choice([". . . I guess? Maybe."
            "Well, I'll give it some thought, " + Girl.Petname + "."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["I will give it some thought, " + Girl.Petname + "."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Eh. Maybe."
            "Maybe, " + Girl.Petname + "."
            "Maybe?"
            "I'll be thinking about it, " + Girl.Petname + "."
            "Anything's possible, " + Girl.Petname + "."
            "It's. . . possible, " + Girl.Petname + "."])

    Girl.voice "[line]"

    return

label reward_politeness_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Heh, I suppose I can hardly refuse ya when you use the magic words . . ."
            "You better work your mouth that hard on these."
            "Well, if you're gonna beg. . ."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Well" + Girl.Like + "if you ask nicely. . ."
            "I like it when you beg. . ."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["Politeness can be rewarded. . ."
            "I do enjoy hearing you beg. . ."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Well if you're going to be a little bitch about it. . ."
            "Oooh, beg for me. . ."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["Oh, fine, just don't start crying."
            "Oooh, beg for me. . ."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["Well, I suppose. . ."
            "I suppose it could not hurt. . ."
            "Well, one could not hurt. . ."
            "I suppose it does not hurt. . ."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Geeze, don't whine about it. . ."
            "Oooh, beg for me. . ."])

    Girl.voice "[line]"

    return

label please_not_good_enough_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I'm afraid not this time, sorry " + Girl.Petname + "."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Um, still no."
            "Nuh uh."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["This wasn't a \"tone\" issue."
            "No."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Well if you're going to be a little bitch about it. . ."
            "No."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["No way."
            "No."
            "Oh, don't cry."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["No, thank you."
            "No."
            "It is not appropriate."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Geeze, don't whine about it. . ."
            "No."])

    Girl.voice "[line]"

    return

label learn_to_take_no_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Learn to take \"no\" for an answer, " + Girl.Petname + "."
            "I just don't want to, " + Girl.Petname + "."
            "I'aint tellin you again."
            "Look, I already told you no thanks, " + Girl.Petname + "."
            "Read my lips, no."
            "Learn to take \"no\" for an answer, " + Girl.Petname + "."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["{i}Listen{/i}!"
            "How many times do I have to say \"no?\""
            "I'm not telling you again."
            "Look, I already told you no thanks, " + Girl.Petname + "."
            "You can eat a dick, 'cos I'm not."
            "Learn to take \"no\" for an answer, " + Girl.Petname + "."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["You need to pay attention when I speak to you."
            "I don't appreciate having to repeat myself, " + Girl.Petname + "."
            "I've refused, end of story."
            "Then I hope you can take care of yourself."
            "Learn to take \"no\" for an answer, " + Girl.Petname + "."
            "I won't repeat myself."
            "Don't make me repeat myself."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Listen to the words that are coming out of my mouth."
            "I don't like to repeat myself, " + Girl.Petname + "."
            "Don't ask again."
            "Look, I already told you no."
            "Suck this then."
            "Learn to take \"no\" for an answer, " + Girl.Petname + "."
            "I'm not telling you again."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["I don't want to have to go through this again."
            "Don't ask again."
            "I already told you no."
            "You want me to make you suck yourself?"
            "Learn to take \"no\" for an answer, " + Girl.Petname + "."
            "I'm not telling you again."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["I have been clear on this."
            "Do not make me repeat myself."
            "I have refused. Learn to accept that."
            "Then I hope you can take care of yourself."
            "Learn to take \"no\" for an answer, " + Girl.Petname + "."
            "I shall not repeat myself."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["I'm pretty clear on this, NO."
            "Don't ask again."
            "Look, I already told you no."
            "Suck this then."
            "Learn to take \"no\" for an answer, " + Girl.Petname + "."
            "I'm not telling you again."])

    Girl.voice "[line]"

    return

label not_happening_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Not hap'nin."
            "Not hap'nin, " + Girl.Petname + "."
            "No luck, " + Girl.Petname + "."
            "Tsk, not this time, " + Girl.Petname + "."
            "Shoo, " + Girl.Petname + "."
            "I. . . not there!!"
            "Ew!"
            "Um, no thanks, " + Girl.Petname + "."
            "What?! Gross!"
            "I'd really rather not."
            "That isn't really how I planned to use my feet today"
            "How about let's not, " + Girl.Petname + "."
            "Not interested."
            "No way."
            "Not happening."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["No way."
            "Nuh uh."
            "Nooope."
            "Ew."
            "Ugh!"
            "That's. . . not cool."
            "Scram, " + Girl.Petname + "."
            "Um, no thanks, " + Girl.Petname + "."
            "No luck " + Girl.Petname + "."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["No."
            "I'm sorry, not now."
            "I know, I'm as disappointed as you are."
            "No. Thank you."
            "Not today, " + Girl.Petname + "."
            "No thank you, " + Girl.Petname + "."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["No."
            "I'm sorry, not now."
            "Yeah, sorry."
            "Not today, " + Girl.Petname + "."
            "Nope."
            "No thank you, " + Girl.Petname + "."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["No."
            "I'm sorry, not now."
            "Yeah, sorry."
            "Not today, " + Girl.Petname + "."
            "Nope."
            "No thanks, " + Girl.Petname + "."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["No, I do not think so."
            "No."
            "I'm sorry, not now."
            "No. Thank you."
            "No, I do not think so."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["No."
            "Nope."
            "Not today, " + Girl.Petname + "."
            "Yeah, sorry."
            "No thank you, " + Girl.Petname + "."])

    Girl.voice "[line]"

    return

label you_had_your_shot_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Sorry, " + Girl.Petname + " you aren't touching these again."
            "Sorry, " + Girl.Petname + " you aren't getting these in your mouth."
            "Sorry, keep your tongue in your mouth."
            "Sorry, hands off the booty."
            "Fresh!"
            "I think you should keep your fingers to yourself."
            "Sorry, keep your hands out of there."
            "I think you can manage it yourself this time. . ."
            "Not right now, " + Girl.Petname + ". . ."
            "I think I'll let you know when I want you touching these again."
            "I think I've got the taste out of my mouth, thanks."
            "Sorry, you can keep your toys to yourself."
            "Sorry, you can keep your toys out of there."
            "Maybe you could go fuck yourself instead."
            "Eh-eh, not anymore, " + Girl.Petname + "."
            "The only thing you can do with my ass is kiss it, " + Girl.Petname + ".{p}. . .Don't get any ideas."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["You had your shot."
            "Fresh!"
            "Sorry, no more of that."
            "I don't feel like it."
            "Sorry, hands to yourself."
            "Keep your head out of there."
            "Sorry, keep your hands out of there."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["I'm afraid you haven't earned back my good graces."
            "Hands."
            "Sorry, no more of that."
            "Keep your head out of there."
            "I'm sorry, keep your hands to yourself."
            "I don't feel like it."
            "Sorry, keep your hands out of there."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["You'll have to earn that back."
            "Keep your hands to yourself."
            "Sorry, no more of that."
            "Sorry, keep your hands to yourself."
            "Keep your head out of there."
            "I don't feel like it."
            "Sorry, fingers outside."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["We've had enough of that."
            "Keep your hands to yourself."
            "We've had enough of that."
            "I don't feel like it."
            "Sorry, keep your hands to yourself."
            "Keep your tongue to yourself."
            "You can keep those to yourself."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["No, I do not think so."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["You'll have to earn that."
            "Keep your hands to yourself."
            "Keep your head out of there."
            "Sorry, keep your hands to yourself."
            "I'm not into it."
            "Sorry, no more of that."
            "Sorry, keep your fingers outside."])

    Girl.voice "[line]"

    return

label forced_but_not_unwelcome_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Fine, if that's what you want."
            "Hmmph, well I guess you can go to town. . ."
            "Hmmph."
            "Fine, I suppose."
            "Oh. . . well, ok then. . ."
            "Well, at least make it worth it."
            "Ok, get in there if you're so determined."
            "Ok, fine, whip it out."
            "Ok, fine"
            "Ok, fine. If we're going to do this, stick it in already."
            "Ok, fine. Whatever."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Rude! But. . . whatever."
            "Hmmph."
            "Well. . . I guess. . ."
            "Fine, I suppose."
            "Ok, fine. . ."
            "Ok, {i}fine{/i}."
            "Oh. . . well, ok then. . ."
            "Ok, fine. If we're going to do this, stick it in already."
            "Ok, fine, whip it out."
            "Ok, get in there if you're so determined."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["That is not appropriate. . .{p}but neither is it entirely unwelcome. . ."
            "Hmmph."
            "Oh, if you insist. . ."
            "If you insist. . ."
            "Fine, I suppose."
            "Hm. Alright, but don't push your luck, " + Girl.Petname + "."
            "Well hello there. . ."
            "Ok, fine. If we're going to do this, stick it in already."
            "Oh, fine. . ."
            "Oh, very well."
            "Suit yourself."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Hey. . .{p}Eh, whatever. . ."
            "Hmmph."
            "Ok, fine. . ."
            "Ok, fine."
            "Ok, fine, whip it out."
            "Whatever. . ."
            "Ok, fine. If we're going to do this, stick it in already."
            "If you insist. . ."
            "Fine."
            "Fine, I guess."
            "Well hello there. . ."
            "Suit yourself."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["Hey. . .{p}. . . whatever. . ."
            ". . . whatever. . ."
            ". . . Ok, whatever."
            "Ooo! Well ok then. . ."
            ". . ."
            "Fine."
            "Ok, fine. If we're going to do this, stick it in already."
            "I guess you won't take \"no\" for an answer. . ."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["That is not appropriate. . .{p}}but neither is it entirely unwelcome. . ."
            "Hmmph."
            "Oh, if you insist. . ."
            "If you insist. . ."
            ". . . fine."
            "Ok, fine. If we're going to do this, stick it in already."
            "Oh, very well."
            ". . . I suppose."
            "That was unexpected. . ."
            "If you must. . ."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Hey. . .{p}}Well, whatever. . ."
            "Hmmph."
            "Ok, fine. . ."
            "Ok, fine."
            "Um, hello? . ."
            "Fine."
            "Whatever. . ."
            "Ok, fine. If we're going to do this, stick it in already."
            "Ok, fine, whip it out."
            "Suit yourself."
            "Well I don't want to get in your way. . ."
            "Fine, I guess."])

    Girl.voice "[line]"

    return

label forced_but_welcome_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Sure, get in there."
            "Fine, grab a cheek."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Ok, whatever."
            "Ok, geeze."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["If you must. . ."
            "If you insist. . ."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["If you must. . ."
            "Meh. . ."
            "Going there, huh. . ."
            "If you insist. . ."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["If you must. . ."
            "Whatever. . ."
            "If you insist. . ."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["If you must. . ."
            "If you insist. . ."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["If you haveta. . ."
            "Going there, huh. . ."
            "Meh. . ."
            "If you insist. . ."])

    Girl.voice "[line]"

    return

label just_told_you_no_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I {i}just{/i} told you \"no,\" " + Girl.Petname + "."
        "I {i}just{/i} told you \"no,\" " + Girl.Petname + "."
        "What part of \"no,\" did you not get, " + Girl.Petname + "?"])
    elif Girl == KittyX:
        $ line = renpy.random.choice([Girl.Like + "no way, " + Girl.Petname + "."
            "I" + Girl.Like + "{i}just{/i} told you \"no!\""])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["Your persistance is doing you no favors, " + Girl.Petname + "."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Take a breath here, before you regret it."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["I'm not used to repeating myself."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["Do not persist in this, " + Girl.Petname + "."
            "Your persistance is doing you no favors, " + Girl.Petname + "."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["I already told you, \"no\"."])

    Girl.voice "[line]"

    return

label come_and_get_em_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Ok " + Girl.Petname + " come and get'em."
            "Ok " + Girl.Petname + " go ahead."
            "Oooooooh. . ."
            "God yes."
            "Sure, grab a cheek."
            "Sure, get in there."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Ok " + Girl.Petname + " come and get'em."
            "Ok, whatever."
            "Mmmmmm."
            "Ok, go for it."
            "Oooooooh. . ."
            "Wha. . ."
            "Ok " + Girl.Petname + " go ahead."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["That sounds lovely, ravish me."
            "Mmmm, I couldn't refuse. . ."
            "Mmmmmm. . ."
            "I can't exactly refuse. . ."
            "Mmm. . . naughty."
            "Ok " + Girl.Petname + " go ahead."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Sure, sounds fun."
            "Mmmm, I couldn't refuse. . ."
            "Mmmmmm. . ."
            "Yeah, ok. . ."
            "Mmm. . . naughty."
            "Ok " + Girl.Petname + " go ahead."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["Sure, sounds fun."
            "Mmmm, I couldn't refuse. . ."
            "Mmmmmm. . ."
            "Yeah, ok. . ."
            "Mmm. . . naughty."
            "Ok " + Girl.Petname + " go ahead."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["I would love that. . ."
            "Mmmm, I couldn't refuse. . ."
            "Mmmmmm. . ."
            "Mmm. . . naughty."
            "I suppose that is reasonable. . ."
            "Ok " + Girl.Petname + " go ahead."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Sure, sounds fun."
            "Mmmm, I couldn't refuse. . ."
            "Mmmmmm. . ."
            "Mmm. . . naughty."
            "Yeah, ok. . ."
            "Ok " + Girl.Petname + " go ahead."])

    Girl.voice "[line]"

    return

label gently_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Didn't get enough earlier?"
            "Maybe not so hard this time though."
            "Maybe not so rough this time though."
            "I'm still tingling a bit from earlier."
            "You do have a smooth touch. . ."
            "Take it a bit gently, I'm still quivering from earlier."
            "Again? Oh, you're insatiable!"
            "Must be my lucky day!"
            "You sure know how to keep a girl satisfied. . ."
            "Mmm. . ."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Didn't get enough earlier?"
            "Maybe not so rough this time though."
            "Take it easy though."
            "Take it a bit gently, I'm still shaking from earlier."
            "Huh? Again?"
            "I must have done something right."
            "What a girl wants. . ."
            "Mmm. . ."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["You didn't get enough earlier?"
            "Huh? Again?"
            "Perhaps not so rough this time?"
            "I must have done something right."
            "What a queen deserves. . ."
            "Relax, gently. . ."
            "Take it a bit gently, I'm still shaking from earlier."
            "Mmm. . ."
            "Didn't get enough earlier?"])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["You didn't get enough earlier?"
            "Chill. . ."
            "Take it slow, I'm still shaking from earlier."
            "Huh? Again?"
            "I must have done something right."
            "I do like this treatment. . ."
            "Mmm, you like that? . ."
            "Mmm. . ."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["You didn't get enough earlier?"
            "Chill. . ."
            "Take it slow, I'm still shaking from earlier."
            "Huh? Again?"
            "I must have done something right."
            "I do like this. . ."
            "Mmm, you like that? . ."
            "Mmm. . ."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["You didn't get enough earlier?"
            "Gently. . . gently. . ."
            "Relax, gently. . ."
            "Take it a bit gently, I am still glowing from earlier."
            "Huh? Again?"
            "I must have done something right."
            "What a queen deserves. . ."
            "Perhaps not so rough this time?"
            "Mmm. . ."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["You didn't get enough earlier?"
            "Relax. . ."
            "Take it slow, I'm still shaking from earlier."
            "Huh? Again?"
            "I must have done something right."
            "I guess fair's fair. . ."
            "Mmm, you like that? . ."
            "Mmm. . ."])

    Girl.voice "[line]"

    return

label had_enough_of_this_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I told you not to touch me like that in public!"
            "I told you that wasn't appropriate!"
            "You already got your answer!"
            "I told you we can't do that in public!"
            "I already told you that I wouldn't jerk you off in public!"
            "This is just way too exposed!"
            "I already told you that I wouldn't suck you off in public!"
            "Not in public!"
            "Stop swinging that thing around in public!"
            "I already told you that I wouldn't bang you in public!"
            "I already told you that I wouldn't do that out here!"
            "I told you that I didn't want you rubb'in up on me in public!"])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["I told you not here!"
            "I told you not to touch me like that in public!"
            "You already got your answer!"
            "I told you that wasn't appropriate!"])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["You've been warned."
            "I told you not to touch me like that in public!"
            "You already got your answer!"
            "I told you that wasn't appropriate!"])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["I've had enough of this today."
            "I told you not to touch me like that in public!"
            "I told you that wasn't appropriate!"
            "You already got your answer!"])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["I've had enough of this today."
            "I told you not to touch me like that in public!"
            "I told you that wasn't appropriate!"
            "You already got your answer!"])
    elif Girl == StormX:
        $ line = renpy.random.choice(["I have already told you my answer."
            "I told you not to touch me like that in public!"
            "You already got your answer!"])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["I've had enough of this today."
            "I told you not to touch me like that in public!"
            "I told you that wasn't appropriate!"
            "I told you not to touch me like that in public!"
            "You already got your answer!"])

    Girl.voice "[line]"

    return

label already_said_no_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I already told you \"no,\" " + Girl.Petname + "."
            "I already told you no, take a hint."
            "What part of \"no\" don't you understand?"
            "I already told you \"no,\" " + Girl.Petname + "."
            "I told you \"no\" earlier " + Girl.Petname + "."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["I" + Girl.Like + "already told you \"no.\""
            "" + Girl.Like + "take a lesson, " + Girl.Petname + "."
            "Get a clue, " + Girl.Petname + "!"
            "I'm telling you to give it a rest!"])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["I believe you know my answer on this matter."
            "I'm not in the mood for this, " + Girl.Petname + "."
            "You heard me the first time."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Don't make me tell you again today."
            "Grrrrrrrrr."
            "Back off!"])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["Don't ask me again today."
            "Go away!"
            "Give me some space!"])
    elif Girl == StormX:
        $ line = renpy.random.choice(["I have already told you my answer."
            "I believe you know my answer on this matter."
            "I am far too irate for this."
            "Stop pestering me!"])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Don't make me tell you again today."
            "Grrrrrrrrr."
            "Back off!"])

    Girl.voice "[line]"

    return

label rather_not_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I'd really rather not."
            "Oh, um, no, I'm not really comfortable with that. . ."
            "Not right now, " + Girl.Petname + ". . ."
            "Maybe not right now, ok?"
            "I don't think we need any toys, " + Girl.Petname + "."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Um, no."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["You wish."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Keep dreaming."
            "You wish."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["Yeah, you wish."
            "You wish."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["Hmm, no."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Cute, but no."
            "You wish."])

    Girl.voice "[line]"

    return

label went_too_far_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I don't want you touching me."
            "I don't want your lips on me."
            "Um, no way."
            "Not even, " + Girl.Petname + "."
            "Not even that much."
            "Stay out of my pants, " + Girl.Petname + "."
            "Hands off the booty!"
            "Ew, no way."
            "I'm not that kind of girl!"
            "Not even with my feet."
            "That isn't something I'd want!"
            "I'm not going to let you use that on me."
            "I'm not doing that just because you have me over a barrel."
            "That's a bit much, even for you."
            "Even that's not worth it."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Not even."
            "Keep away from my kitty, " + Girl.Petname + "."
            "Back off!"
            "Um, no way."
            "Ew, no way."
            "Not even, " + Girl.Petname + "."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["Don't push your luck."
            "I don't think so, " + Girl.Petname + "."
            "I don't think so."
            "I really can't, " + Girl.Petname + "."
            "Do you want to keep those fingers?"
            "I'm not going that far today."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["No."
            "I don't think so, " + Girl.Petname + "."
            "I don't think so."
            "I really can't, " + Girl.Petname + "."
            "Do you want to keep those fingers?"
            "I'm not going there today."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["No."
            "I don't think so, " + Girl.Petname + "."
            "I don't think so."
            "I really can't, " + Girl.Petname + "."
            "Mmmm, no."
            "I'm not going there today."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["You go too far."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["No."
            "I don't think so, " + Girl.Petname + "."
            "I don't think so."
            "I really can't, " + Girl.Petname + "."
            "Do you want to keep those fingers?"
            "I'm not going there today."])

    Girl.voice "[line]"

    return

label warm_hands_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["You like how those feel, huh?"
            "You're just going at them, huh?"
            "You like how that feels, huh?"
            "What are you even doing down there?"
            "Uh, that's nice, but. . ."
            "You like it down there?"])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["You like how those feel, huh?"
            "You're just going at them, huh?"
            "Are they keeping you satisfied?"
            "You like how that feels, huh?"
            "You like it down there?"
            "Uh, that's nice, but. . ."
            "What are you even?"])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["Luxurious, yes?"
            "They really are magnificent, aren't they?"
            "lovely, aren't they?"
            "You like how that feels, huh?"
            "Isn't it just delicious?"
            "Mmmm I do enjoy that. . ."
            "Ungh, you're getting going there. . ."
            "You certainly are enthusiastic. . ."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Kinda nice, but. . ."
            "Enjoying yourself?"
            "This is kinda nice. . ."
            "Mmmm, you're enjoying that, huh?"
            "Isn't it just delicious?"
            "Mmmm. . ."
            "Ungh, you're really getting in there. . ."
            "You seem to be enjoying yourself. . ."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["Kinda nice, but. . ."
            "Having fun there?"
            "This is kinda nice. . ."
            "Mmmm, you're enjoying that, huh?"
            "Isn't it just delicious?"
            "Mmmm. . ."
            "Ungh, you're really getting in there. . ."
            "You seem to be enjoying yourself. . ."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["Your hands are so warm. . ."
            "You really seem to enjoy those. . ."
            "Mmmm, yes. . . deeper. . ."
            "Oh, that is delightful. . ."
            "Mmmm. . ."
            "Ooh, watch it, watch it. . ."
            "You are quite enthusiastic. . ."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Ok, but, uh. . ."
            "Having fun?"
            "Yeah, I like that too. . ."
            "Mmmm. . ."])

    Girl.voice "[line]"

    return

label try_something_else_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I know you're having fun, but maybe we could try something else " + Girl.Petname + "."
            "" + Girl.Petname + " this is getting uncomfortable, maybe we could try something else."
            "" + Girl.Petname + " this is nice, but could we do something else?"
            "" + Girl.Petname + " I know you're having fun down there, but maybe we could try something else."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["You look like you're having fun there, but maybe we could" + Girl.Like + "try something else?"
            "Maybe we could try something else here " + Girl.Petname + "?"
            "" + Girl.Petname + " I know you're having fun down there, but maybe we could try something else."
            "" + Girl.Petname + " this is nice, but could we do something else?"
            "" + Girl.Petname + " this is getting kind sore, maybe we could try something else."
            "" + Girl.Petname + " this is getting weird, maybe we could try something else."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["You certainly seem to be enjoying yourself, but perhaps we could add some variety?"
            "Perhaps we could try something else, " + Girl.Petname + "?"
            "" + Girl.Petname + " I know you're having fun down there, but maybe we could try something else."
            "" + Girl.Petname + " this is nice, but could we do something else?"
            "" + Girl.Petname + " this is getting kind sore, maybe we could try something else."
            "" + Girl.Petname + " this is getting weird, maybe we could try something else."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Maybe change things up a little?"
            "Maybe it's time for something else, " + Girl.Petname + "?"
            "" + Girl.Petname + " could we try something different?"])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["Maybe try something else?"
            "Maybe it's time for something else, " + Girl.Petname + "?"
            "" + Girl.Petname + " could we try something different?"])
    elif Girl == StormX:
        $ line = renpy.random.choice(["I am sure that is fun, but could we try something different?"])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Could we maybe try. . . something else?"])

    Girl.voice "[line]"

    return

label this_is_boring_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Well if that's your attitude, I don't need your \"help\"."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Fun for you maybe, I'm tired of it."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["Well perhaps you are enjoying yourself, but I'm tired of this."
            "You may be enjoying yourself, but I'm getting a bit sore."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["I'm kinda bored here."
            "Well, I've got better things to be doing."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["Well -I'm- bored."
            "Well, I've got better things to be doing."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["Well however much you are enjoying yourself, I need to take a break."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["This is kinda boring. . .."])

    Girl.voice "[line]"

    return

label wrap_this_up_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["You might want to wrap this up, it's getting late."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["It's" + Girl.Like + "getting kinda late."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["It's getting late. . ."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["It's getting late, we should wrap this up."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["Wow, look at the time. . ."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["It is getting late, " + Girl.Petname + ". . ."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["I could use a break soon. . ."])

    Girl.voice "[line]"

    return

label time_to_stop_soon_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Seriously, it'll be time to stop soon."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["We should wrap this up."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["We should take a break soon."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Tick tock, " + Girl.Petname + "."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["We should probably wrap this up, " + Girl.Petname + "."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["We should take a break soon."])
    elif Girl == JubesX:
        $ line = renpy.random.choice([". . . I could really use a break here. . ."])

    Girl.voice "[line]"

    return

label im_done_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Ok, " + Girl.Petname + " that's enough of that for now."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Time to take a little break, for now."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["We need to stop for a moment, let me catch my breath."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Ok, " + Girl.Petname + " breaktime."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["Ok, " + Girl.Petname + " time for a break."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["I need to take a moment to collect myself."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Ok, that's it, I need a break."])

    Girl.voice "[line]"

    return

label that_was_nice_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["That was. . . nice."
            "That was . . . real pleasant, " + Girl.Petname + "."
            "I . . . really liked that, " + Girl.Petname + "."
            "Certainly different with someone else at the wheel."
            "I. . . how'd I taste?"
            "That felt. . . interesting. . ."
            "Was. . . that something you liked?"
            "Well, it's really nice to finally be able to reach out and touch someone."
            "That was a real interesting experience. . ."
            "Well, that was certainly interesting."
            "That really wasn't half bad."
            "Well I liked that. . ."
            "Well that was a bit rough. . ."
            "That was . . . interesting " + Girl.Petname + ". We'll have to do that again sometime."
            "That was pretty hot, " + Girl.Petname + ", we'll have to do that again sometime."
            "That was really great, " + Girl.Petname + ", we'll have to do that again sometime."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["I liked that."
            "I hope there was" + Girl.Like + "enough to work with."
            "I hope they were enough for you. . ."
            "That was. . . good for you?"
            "Huh. . . um. . ."
            "I feel like I've been waiting" + Girl.Like + "a million years for that."
            "Anal. . . huh, who knew?"
            "I. . . liked that a lot."
            "That was odd. . ."
            "Was it. . . good?"
            "Your hand is. . . bigger than mine."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["That was. . . pleasant."
            "I'm sure it exceeded your expectations. . ."
            "Delectable, weren't they."
            "I do appreciate some rather. . . aggressive attention down there."
            "I could really take advantage of your services more often. . ."
            "That was. . . nice. . ."
            "You certainly surprise me. . ."
            "That was. . . invigorating."
            "That was. . . pleasant."
            "You really took to that well."
            "I assume I rocked your entire world."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["That was. . . interesting."
            "Did you enjoy that?"
            "That was kinda nice."
            "You're really getting into the good stuff."
            "That was a really good use of that tongue of yours."
            "That was. . . nice. . ."
            "You seem to know your way around back there."
            "I can tell, I was the best you've had."
            "That was. . . nice."
            "That was kinda wild. . ."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["Well that was. . . something."
            "I bet you enjoyed that."
            "Well, that was a nice surprise. . ."
            "You really put that tongue to work. . ."
            "That was. . . nice. . ."
            "Blew your mind, uh?"
            "Hmmm, that was nice. . ."
            "Ok, that was. . . fine."
            "That was. . . interesting. . ."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["Thank you for that."
            "That was quite fun. . ."
            "That was certainly enjoyable."
            "You certainly. . . reached some interesting places there. . ."
            "You really do have a talent for that. . ."
            "That was. . . nice. . ."
            "That one caught me by surprise. . ."
            "That was. . . certainly interesting. . ."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["That was. . . interesting."
            "Did you like that?"
            "That was kinda nice."
            "Wow. . . that was nice. . ."
            "You really give me a run for my money. . ."
            "That was. . . nice. . ."
            "That was kinda weird. . ."
            "I can tell, I was the best you've had."
            "You seem to know your way around back there."
            "That was. . . nice."
            "I hope that was as enjoyable for you as it was for me."
            "Well. . ."
            "That was quite an experience. . ."
            "That was. . . enjoyable."])

    Girl.voice "[line]"

    return

label was_that_enough_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Was that enough for you?"
            "Did you get your jollies?"
            "Did you like the taste?"
            "Well, I hope that got your rocks off."
            "Did that work for you?"
            "Well, I hope that was enough for you."
            "Did you get what you needed here?"
            "Ouch."
            "Did you get what you needed here?"
            "Did you like that?"
            "Did you like that?"])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Was that enough?"
            "Not a disappointment, right?"
            "Did that satisfy you?"
            "Did that work for you?"
            "Well, did you like the taste?"
            "Did you like that?"
            "Well? Satisfied?"
            "Ouch."
            "I hope that was worth the wait."
            "Well, did that work for you?"
            "I guess you got what you needed?"
            "Did you get what you needed?"])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["Was that enough?"
            "Well you certainly hit the jackpot."
            "Did you get enough?"
            "Did you find what you were looking for?"
            "I suppose that worked out for both of us. . ."
            "Did you enjoy that?"
            "I hope you enjoyed that."
            "Oooh."
            "Was that enough for you?"
            "It's been a while."
            "Was it everything you dreamed?"
            "Was it all you dreamed of?"])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Was that enough?"
            "That worked out for you?"
            "Did you get enough?"
            "Satisfied?"
            "That was pleasant."
            "Enough for you?"
            "Did you find what you were looking for?"
            "Was that good for you?"
            "I suppose we both got something out of that. . ."
            "Did you enjoy that?"])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["Was that enough?"
            "You get what you wanted out of that?"
            "Did you find what you were looking for?"
            "I bet you enjoyed that."
            "Satisfied?"
            "That was great. . ."
            "I guess that could have gone worse. . ."
            "Was that good for you?"
            "I guess that wasn't so bad. . ."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["Ok, was that good?"
            "I expect you enjoyed that. . .."
            "Did you get enough?"
            "Did you enjoy that?"
            "I hope you found that satisfactory."
            "Well. . ."
            "That was quite an experience. . ."
            "Was that satisfactory?"
            "That was not so bad. . ."
            "Did that work for you?"])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Was that enough?"
            "That worked out for you?"
            "Did you get enough?"
            "Did you find anything in there?"
            "Was that good for you?"
            "Well, that wasn't so bad. . ."
            "Did you like that?"
            "Satisfied?"
            "That was pleasant."
            "Enough for you?"])

    Girl.voice "[line]"

    return

label take_a_breather_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["We've been at it for a while now, let's take a breather."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["We've been at it for a while now, let's take a breather."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["I think we could both do with a short break."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["You're looking a bit worn out, maybe take a break."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["You're looking a bit worn out, maybe take a break."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["I think we could both do with a short break."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Hey, I could use a break, how 'bout you?"])

    Girl.voice "[line]"

    return

label got_some_spunk_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Oh?"])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Huh?"])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["Huh?"])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["What?"])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["What?"])
    elif Girl == StormX:
        $ line = renpy.random.choice(["Oh, what do you mean?"])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["What?"])

    Girl.voice "[line]"

    return

label thats_it_for_now_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["That's it. . . for now."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["That's it. . . for now."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["That's all you get. . . for now."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["That's all. . . for now at least."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["That's all. . . for now at least."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["I think that you have had enough for the moment."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Ok, that should be plenty for now."])

    Girl.voice "[line]"

    return

label get_out_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I don't want to deal with you right now."
            "Buzz off already."
            "I really think you should leave."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Nooope."
            "GTFO."
            "Go. Now."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["I haven't any time for this."
            "Out."
            "I think you should leave now."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Nope."
            "Fuck off."
            "Get out before we both regret it."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["Out!"])
    elif Girl == StormX:
        $ line = renpy.random.choice(["Get out."
            "Out. Now."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Out!"])

    Girl.voice "[line]"

    if Girl in [RogueX, KittyX, EmmaX, LauraX, JeanX, JubesX]:
        $ line = renpy.random.choice([Girl.name + " pushes you back into the hall and slams the door. You head back to your room."
            "" + Girl.name + " shoves you back into the hall and slams the door. You head back to your room."])
    elif Girl == StormX:
        $ line = renpy.random.choice([Girl.name + " pushes you to the top of the stairs and slams the door. You head back to your room."])
    "[line]"

    return

label first_time_pussy_eaten_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["That's pretty intimate, " + Girl.Petname + ". . ."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["That's pretty intimate, " + Girl.Petname + ". . ."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["I'm not sure we're at that stage, " + Girl.Petname + ". . ."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Not yet, " + Girl.Petname + ". . ."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["Mmmm, not right now, " + Girl.Petname + ". . ."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["Oh, that would. . .perhaps not, " + Girl.Petname + ". . ."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Not yet, " + Girl.Petname + ". . ."])

    Girl.voice "[line]"

    return

label first_time_ass_eaten_lines(Girl):
    if Girl == RogueX:
        if Girl.love >= Girl.obedience and Girl.love >= Girl.inhibition:
            "I'm not really sure I want you lick'in down there. . ."
        elif Girl.obedience >= Girl.inhibition:
            "You really don't have to if you don't want to."
        else:
            $ Girl.Eyes = "sexy"

            "Hmm. . . it's worth a shot. . ."
    elif Girl == KittyX:
        if Girl.love >= Girl.obedience and Girl.love >= Girl.inhibition:
            "That's, I don't know. . ."
        elif Girl.obedience >= Girl.inhibition:
            "You don't have to do that."
        else:
            $ Girl.Eyes = "sexy"

            "That's kinda gross. . ."
    elif Girl == EmmaX:
        if Girl.love >= Girl.obedience and Girl.love >= Girl.inhibition:
            "Oh, are we there now?"
        elif Girl.obedience >= Girl.inhibition:
            "Is that what gets you off?"
        else:
            $ Girl.Eyes = "sexy"

            "Hm, I didn't know that's what you were into."
    elif Girl == LauraX:
        if Girl.love >= Girl.obedience and Girl.love >= Girl.inhibition:
            "Oh, we're there now?"
        elif Girl.obedience >= Girl.inhibition:
            "Is that what gets you off?"
        else:
            $ Girl.Eyes = "sexy"

            "Hm, I didn't know that's what you were into."
    elif Girl == JeanX:
        if Girl.love >= Girl.obedience and Girl.love >= (Girl.inhibition - Girl.IX):
            "Oh, we're there now?"
        elif Girl.obedience >= (Girl.inhibition - Girl.IX):
            "Is that what gets you off?"
        else:
            $ Girl.Eyes = "sexy"

            "Mmmm, you're into that?"
    elif Girl == StormX:
        if Girl.love >= Girl.obedience and Girl.love >= Girl.inhibition:
            "Oh, that is a bit forward!"
        elif Girl.obedience >= Girl.inhibition:
            "That is what you want?"
        else:
            $ Girl.Eyes = "sexy"

            "Hmmm, an interesting proposal. . ."
    elif Girl == JubesX:
        if Girl.love >= Girl.obedience and Girl.love >= Girl.inhibition:
            "What? What're you talking about?"
        elif Girl.obedience >= Girl.inhibition:
            "Is that what gets you off?"
        else:
            $ Girl.Eyes = "sexy"

            "Hm, I hadn't thought. . ."

    Girl.voice "[line]"

    return

label ass_sore_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I'm still a little sore from earlier, " + Girl.Petname + "."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["I'm still a little sore from earlier, " + Girl.Petname + "."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["I'm still a little sore from earlier, " + Girl.Petname + "."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["I'm still a little sore from earlier, " + Girl.Petname + "."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["I'm still a little sore from earlier, " + Girl.Petname + "."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["I'm still a little sore from earlier, " + Girl.Petname + "."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["I'm still a little sore from earlier, " + Girl.Petname + "."])

    Girl.voice "[line]"

    return

label not_into_ass_play(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I. . . don't think that's. . ."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["I. . . don't think that's. . ."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["That's really not my usual style. . ."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["That's really not my style. . ."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["That's really not my style. . ."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["That's really not my usual style. . ."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["That's really not my style. . ."])

    Girl.voice "[line]"

    return

label think_would_enjoy_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Ok, you're probably right. . ."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Ok, you're probably right. . ."
            "Oh. . . you're probably right. . ."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["You're probably right. . ."
            "You present a compelling case. . ."
            "Ok, you're probably right. . ."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Ok, you're probably right. . ."
            "You make a good point. . ."
            "You're probably right. . ."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["Ok, you're probably right. . ."
            "You make a good point. . ."
            "You're probably right. . ."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["Well. . . I might at that. . ."
            "I. . . would. . ."
            "You may be correct. . ."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Um. . . maybe. . ."
            "You make a good point. . ."])

    Girl.voice "[line]"

    return

label unconvinced_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Tsk, not this time, " + Girl.Petname + " that just seems. . . dirty."
            "I really don't think that I would."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["I really don't think so."
            "I really don't think that I would."
            "Um, not this time, " + Girl.Petname + " that's too. . ."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["I really don't think so."
            "I don't think that I would."
            "I would, but still no, " + Girl.Petname + "."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["I really don't think so."
            "I don't think that I would."
            "I would, but still no, " + Girl.Petname + "."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["I really don't think so."
            "I don't think that I would."
            "I would, but still no, " + Girl.Petname + "."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["I really do not think so."
            "I do not think that I would."
            "I would, but still no, " + Girl.Petname + "."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["I would, but still no, " + Girl.Petname + "."
            "Doubt."
            "I really doubt that. . ."])

    Girl.voice "[line]"

    return

label didnt_get_off_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I didn't exactly get off there. . ."
            "That didn't really do it for me. . ."
            "Hmm, you seemed to get more out of that than me. . ."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Could you have maybe paid more attention? . ."
            "I didn't get much out of that. . ."
            "Hmm, you seemed to get more out of that than me. . ."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["Could you have perhaps been more attentive? . ."
            "I'm afraid that didn't do much for me. . ."
            "Hmm, you seemed to get more out of that than I did. . ."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Forgetting someone? . ."
            "That didn't do much for me. . ."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["I think you need to get back down there."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["I could have used some more attention to my needs. . ."
            "I am afraid that you got more out of that than me. . ."
            "I am afraid that did not do much for me. . ."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Forgetting someone? . ."
            "That didn't do much for me. . ."])

    Girl.voice "[line]"

    return

label getting_close_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Are you getting close here? I'm getting a little sore."
            "Are you getting close here? My jaw's getting pretty sore."
            "What are you even doing down there?"
            "Are you getting close here? I'm getting a little sore."
            "Are you getting close here?"])

    Girl.voice "[line]"

    return

label getting_rugburn_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I'm getting rug-burn here " + Girl.Petname + ". Can we do something else?"
            "I'm getting a little tired, " + Girl.Petname + ". Can we do something else?"
            "" + Girl.Petname + ", this is getting uncomfortable, maybe we could try something else."
            "Ow, i'm not used to this. Mind if we take a break?"
            "Can we be done with this now? I'm getting sore."])

    Girl.voice "[line]"

    return

label done_with_this_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["I'm . . .getting . . .worn out. . . here, . . " + Girl.Petname + "."
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
        $ line = renpoy.random.choice(["Well, since you're be'in so nice about it, I guess we can give it a go. . ."
            "I guess if you really want to try it. . ."
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
            "Are you sure that's all you want?"
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
            "You want me to slick your pole?"
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
        $ line = renpy.random.choice(["Ok, [Girl.Petname], let's do this."])

    Girl.voice "[line]"

    ch_r "Hmm, stick it in. . ."
    ch_r "Hmm, I've apparently got someone's attention. . ."

    return

label were_done_here_lines(Girl):
    $ line = renpy.random.choice(["[Girl.name] shoves you away and slaps you in the face."
        "[Girl.name] shoves you away."])

    "[line]"

    if Girl == RogueX:
        $ line = renpy.random.choice(["Jackass!{p}If that's how you want to treat me, we're done here!"
            "Dick!{p}}If that's how you want want to act, I'm out of here!"])

    Girl.voice "[line]"

    return

label knows_her_place_lines(Girl):
    $ line = renpy.random.choice(["[Girl.name] doesn't seem to be into this, but she knows her place."
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
    ch_r "Hmm, could be fun. . ."
    ch_r "Sure. . ."
    ch_r "Heh, might be fun."
    ch_r "I guess. . ."
    ch_r "I guess it could be fun with a partner. . ."
    ch_r "Hmm, I've always wanted to try it. . ."
    ch_r "Hmm, it has been on my list. . ."
    ch_r "Hmm, you look ready for it, at least. . ."

    ch_k "I guess. . ."

    return

label first_action_approval_mostly_love_lines(Girl):
    ch_r "Well, I've never really been able to touch people without draining them, this could be an interesting experience. . ."
    ch_r "If that's what you like. . ."
    ch_r "Huh, well that's certainly one way to get off."
    ch_r "I've never really put something like that in my mouth. . . might be interesting."
    ch_r "I've had a reasonable amount of experience with these, you know. . ."
    ch_r "I haven't actually used one of these, back there before. . ."
    ch_r "Well, I've never been able to do this before now, so this might be fun."
    ch_r "I guess if you really want to try it. . ."
    ch_r "It looks like you need some relief. . ."

    ch_k "I guess it could be interesting. . ."

    return

label first_action_approval_mostly_obedience_lines(Girl):
    ch_r "If that's what you want, [Girl.Petname]. . ."
    ch_r "If that's what you want. . ."
    ch_r "I suppose, if that's what you want. . ."
    ch_r "Ok, [Girl.Petname], I'm ready."

    ch_k "If you want, [Girl.Petname]. . ."

    return

label first_action_approval_addicted_lines(Girl):
    ch_r "I think, if I could just touch that. . ."
    ch_r "I guess. . ."
    ch_r "I think. . . for some reason I really do want that in my mouth. . ."
    ch_r "Hmmmm. . . ."
    ch_r "Well. . . I bet it would feel really good down there."

    ch_k "I kind of {i}need{/i} to. . ."

    return

label action_forcefully_approved_lines(Girl):
    ch_r "That's really what you want?"
    ch_r "That's it?"
    ch_r "This isn't going to become a habit, will it?"
    ch_r "You want me to do that again?"
    ch_r "The toys again?"
    ch_r "That's all you want?"

    return

label action_forcefully_accepted_lines(Girl):
    ch_r "Ok, fine."
    ch_r ". . . Ok, if that's what you want."
    ch_r "Well, there are worst ways to get you off. . ."
    ch_r "Whatever."

    return

label after_action_five_times_lines(Girl):
    ch_r "I think I've got this well in hand."
    ch_r "I kinda like this sensation.{p}}Never thought about touching people with my feet."
    ch_r "I think I've got the hang of this."

    if focused_Girl == RogueX:
        ch_r "We're making a regular habit of this."
    elif focused_Girl == KittyX:
        ch_k "Why did we not do this sooner?!"
    elif focused_Girl == EmmaX:
        ch_e "We really should have done this sooner."
        ch_e "I can't imagine why I waited so long."
    elif focused_Girl == LauraX:
        ch_l "You know, this was a good idea."
    elif focused_Girl == JeanX:
        ch_j "You're pretty good at this. . ."
    elif focused_Girl == StormX:
        ch_s "You are quite skilled at this."
        ch_s "I am glad you \"bumped into\" me."
    elif focused_Girl == JubesX:
        ch_v "You know, this was a good idea."

    if focused_Girl == RogueX:
        ch_r "We're making a regular habit of this."
    elif focused_Girl == KittyX:
        ch_k "I'm really starting to love this."
    elif focused_Girl == EmmaX:
        ch_e "You're pretty good at that."
    elif focused_Girl == LauraX:
        ch_l "I'm glad you're into this."
    elif focused_Girl == JeanX:
        ch_j "I'm glad we have similar interests. . ."
    elif focused_Girl == StormX:
        ch_s "You do certainly make the experience enjoyable."
    elif focused_Girl == JubesX:
        ch_v "I'm glad you're into this."

    if focused_Girl == RogueX:
        ch_r "This is. . . interesting."
    elif focused_Girl == KittyX:
        ch_k "I'm surprised how much I enjoy this."

    if focused_Girl == RogueX:
        ch_r "We're really making this a regular thing."
    elif focused_Girl == KittyX:
        ch_k "You're good at this. . ."
    elif focused_Girl == EmmaX:
        ch_e "You're surprisingly talented. . ."
    elif focused_Girl == LauraX:
        ch_l "You're really talented. . ."
    elif focused_Girl == JeanX:
        ch_j "MmMmmm, that was nice. . ."
    elif focused_Girl == StormX:
        ch_s "Mmmm, has anyone told you that you are quite good at this?"
    elif focused_Girl == JubesX:
        ch_v "Kissing you really feels great!"

    return

label switching_action_lines(Girl):
    ch_r "Mmm, so what else did you have in mind?"
    ch_k "Mmm, so what else did you have in mind?"
    ch_e "Ok then, what were you thinking?"
    ch_l "Ok then, what next?"
    ch_j "Ok, what'd you have in mind?"
    ch_s "Very well, what were you thinking?"
    ch_v "Ok then, what else?"

    return

label before_action_less_than_three_times_lines(Girl):
    ch_r "So you'd like another handy?"
    ch_r "Again?"
    ch_r "So you'd like another titjob?"
    ch_r "So you'd like another blowjob?"
    ch_r "You want to stick it in my pussy again?"
    ch_r "You want to stick it in my ass again?"
    ch_r "So you'd like another go?"

    return

label anal_insertion_not_loose_not_done_today_lines(Girl):
    ch_r "You could have been a bit more gentle last time, [Girl.Petname]. . ."

    return

label anal_insertion_not_loose_done_today_lines(Girl):
    ch_r "Sorry, I just need a little break back there, [Girl.Petname]."

    return

label hard_cock_lines(Girl):
    if focused_Girl == EmmaX:
        ch_e "My word [focused_Girl.Petname], your member is hard enough to crack diamond. . . and I should know."
    elif focused_Girl == LauraX:
        ch_l "Nice to see you're ready for business. . ."
    elif focused_Girl == JeanX:
        ch_j "I see you won't need any encouragement. . ."
    elif focused_Girl == StormX:
        ch_s "I must say [focused_Girl.Petname], you certainly do seem to be. . . excited."

    return

label first_time_asking_lines(Girl):
    ch_r "You want me to rub your cock, with my hand?"
    ch_r "Huh, so like a handy, but with my feet"
    ch_r "You want me to rub your cock with my breasts?"
    ch_r "You want me to put your dick. . . in my mouth?"
    ch_r "Hmmm, so you'd like to try out some toys?"
    ch_r "So, you'd like to take this to the next level? Actual sex? . . ."
    ch_r "Wait, so you want to stick it in my butt?!"
    ch_r "Wait, so you want to grind against my butt?!"

    return

label first_time_forcing_lines(Girl):
    ch_r "I suppose there are worst things you could ask for."
    ch_r "You had to go for the butt, uh?"
    ch_r "You'd really take it that far?"
    ch_r "Seriously?"
    ch_r ". . . That's all?"

    return

label mouth_not_enough(Girl):
    ch_r "My mouth wasn't enough?"

    return

label what_do_you_think_youre_doing_lines(Girl):
    ch_r "Hey, what do you think you're doing back there?!"
    ch_r "Hmm, kinda rude, [Girl.Petname]."

    return

label hand_not_enough(Girl):
    ch_r "My hand wasn't enough?"

    return

label achievement_lines(Girl):

    ch_r "I guess you can call me \"Handi-Queen.\""
    ch_r "I guess I've gotten used to this foot thing."
    ch_r "I'm really starting to enjoy this."

    if Girl == RogueX:
        ch_r "I think I'm getting addicted to this."
    elif Girl == KittyX:
        ch_k "I just can't seem to quit you."
    elif Girl == EmmaX:
        ch_e "I seem to fit you like a glove. . ."
    elif Girl == LauraX:
        ch_l "We're making this a regular thing, huh. . ."
    elif Girl == JeanX:
        ch_j "Hey, I just noticed we've been doing this a lot. . ."
    elif Girl == StormX:
        ch_s "We do go well together. . ."
    elif Girl == JubesX:
        ch_v "We're making this a regular thing, huh. . ."

    ch_r "I think I'm getting addicted to this."

    if Girl == RogueX:
        ch_r "I. . . really think I enjoy this. . ."
    elif Girl == KittyX:
        ch_k "I didn't think I'd love this so much!"
    elif Girl == EmmaX:
        ch_e "You're one of the better partners I've had at that."
    elif Girl == LauraX:
        ch_l "I think you've got a knack for that."
    elif Girl == JeanX:
        ch_j "This has been fun exercise."
    elif Girl == StormX:
        ch_s "I have certainly come to enjoy this."
    elif Girl == JubesX:
        ch_v "I think you've got a knack for that."

    return

label convinced_after_saying_no_lines(Girl):
    ch_r "I guess if it'll get you off. . ."
    ch_r "Fine!"
    ch_r "Hmm, I suppose. . ."
    ch_r "Oh, I suppose it isn't so bad. . ."
    ch_r "Ok, you've won me over on this one. . ."
    ch_r "Ok, ok, I have been itching for this. . ."
    ch_r "Well, I guess it's not so bad. . ."

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
    ch_r "[line]"

    return

label pull_back_before_get_in_lines(Girl, action):
    if Girl.action_counter[action]:
        ch_r "Well ok, [Girl.Petname], no harm done. Just give me a little warning next time."
        ch_r "Well ok, [Girl.Petname], it has been kinda fun."
    else:
        ch_r "Well ok, [Girl.Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
        ch_r "Well ok, [Girl.Petname], that's a bit dirty, maybe ask a girl?"

    return

label would_you_like_more_lines(Girl):
    if focused_Girl == RogueX:
        ch_r "You maybe want to try something more?"
    elif focused_Girl == KittyX:
        ch_k "Is that it?"
    elif focused_Girl == EmmaX:
        ch_e "You wouldn't be interested in something more? . ."
    elif focused_Girl == LauraX:
        ch_l "Huh, that's all there is to it?"
    elif focused_Girl == JeanX:
        ch_j "That was nice. . ."
    elif focused_Girl == StormX:
        ch_s "Oh. . . that was lovely."
    elif focused_Girl == JubesX:
        ch_v "Did you want. . . more?"

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
