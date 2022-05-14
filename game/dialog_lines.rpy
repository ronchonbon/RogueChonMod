label out_of_action_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["Sorry, " + character.Petname + " but I'm a bit worn out."
            "I'm a bit worn out right now, " + character.Petname + " maybe later."])
    elif character == KittyX:
        $ line = renpy.random.choice(["Sorry, " + character.Petname + " but I'm a bit worn out."
            "I'm kinda tired right now, " + character.Petname + " later?"])
    elif character == EmmaX:
        $ line = renpy.random.choice(["I'm sorry, " + character.Petname + " but I need a break."
            "I'm rather tired right now, " + character.Petname + " rain check?"])
    elif character == LauraX:
        $ line = renpy.random.choice(["Maybe in a minute, I need a break."
            "Maybe later, " + character.Petname + ""])
    elif character == JeanX:
        $ line = renpy.random.choice(["Gimme a minute, k?"])
    elif character == StormX:
        $ line = renpy.random.choice(["I am sorry, " + character.Petname + " I need to take a break."])
    elif character == JubesX:
        $ line = renpy.random.choice(["I could use a short break first."
            "Maybe later, " + character.Petname + ""])

    character.voice "[line]"

    return

label tired_lines(character, multi = MultiAction):
    if character == RogueX:
        if not multi:
            $ line = renpy.random.choice(["Look, I think we can stay on this one thing. . ."])
        else:
            $ line = renpy.random.choice(["I'm actually getting a little tired, so maybe we could wrap this up?"])
    elif character == KittyX:
        if not multi:
            $ line = renpy.random.choice(["Let's just. . . stick with this. . ."])
        else:
            $ line = renpy.random.choice(["I kinda need a break, so if we could wrap this up?"])
    elif character == EmmaX:
        if not multi:
            $ line = renpy.random.choice(["Focus on what we're doing, " + character.Petname + "."])
        else:
            $ line = renpy.random.choice(["I could use a break, are you about finished here?"])
    elif character == LauraX:
        if not multi:
            $ line = renpy.random.choice(["Nah, let's just stick to this."])
        else:
            $ line = renpy.random.choice(["Maybe we could finish this up for now?"])
    elif character == JeanX:
        if not multi:
            $ line = renpy.random.choice(["I'd rather just stick to this."])
        else:
            $ line = renpy.random.choice(["Keep your eye on the prize. . ."])
    elif character == StormX:
        if not multi:
            $ line = renpy.random.choice(["I would prefer to finish this."])
        else:
            $ line = renpy.random.choice(["Why not finish off here first?"])
    elif character == JubesX:
        if not multi:
            $ line = renpy.random.choice(["Let's just keep doing this for a bit. . ."])
        else:
            $ line = renpy.random.choice(["Maybe we could wrap it up?"])

    character.voice "[line]"

    return

label angry_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["I don't want to deal with you right now."])
    elif character == KittyX:
        $ line = renpy.random.choice(["I don't want to deal with you right now."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["I'd rather not deal with you at the moment."])
    elif character == LauraX:
        $ line = renpy.random.choice(["You really don't want to try me right now."])
    elif character == JeanX:
        $ line = renpy.random.choice(["You really don't want to try me right now."])
    elif character == StormX:
        $ line = renpy.random.choice(["I do not want to deal with you right now."])
    elif character == JubesX:
        $ line = renpy.random.choice(["I'm definitely not in the mood for you right now."])

    character.voice "[line]"

    return

label go_back_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["Ah, ah, Just keep doing what you were doing, " + character.Petname + "."
            "Hey, just keep doing what you were doing, " + character.Petname + "."
            "Hands off the merchandise, " + character.Petname + "."
            "Keep it out of there, " + character.Petname + "."
            "Keep it outside, " + character.Petname + "."
            "Hands off, " + character.Petname + "."
            "Oh! No, no thank you, " + character.Petname + "."
            "Um, no, I'm not really. . . don't."])
    elif character == KittyX:
        $ line = renpy.random.choice(["Nuh-uh, " + character.Petname + " get back to what you were doing."
            "Heh, keep it above the belt, " + character.Petname + "."
            "Um, no take that out."
            "Um, don't do that. . ."
            "Hands off, " + character.Petname + "."
            "Oooo! Um, no, no thanks. No. . ."
            "Whoa, back off, " + character.Petname + "."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["Down boy, you were doing so well. . ."
            "Perhaps we keep it above the waist, " + character.Petname + "."
            "Careful what you put in there, you may not get it back."
            character.Petname + "! Not now. . ."
            "Hands off, " + character.Petname + "."
            "I like where your head is at, so to speak, but perhaps hold off on that."
            "Whoa, back off, " + character.Petname + "."])
    elif character == LauraX:
        $ line = renpy.random.choice(["Roll it back, " + character.Petname + ". . ."
            "Maybe we keep it above the waist, " + character.Petname + "."
            "Watch your hands, or lose them."
            character.Petname + "! No. . ."
            "Hands off, " + character.Petname + "."
            "Hey, good instincts, but maybe hold off?"
            "Whoa, back off, " + character.Petname + "."])
    elif character == JeanX:
        $ line = renpy.random.choice(["Not so fast, " + character.Petname + ". . ."
            "Keep it above the waist, " + character.Petname + "."
            "Not so fast, " + character.Petname + ". . ."
            "Hmmm, not yet, " + character.Petname + "."
            "Whoa there, " + character.Petname + "!"
            "Ooo! Not right now, " + character.Petname + "."])
    elif character == StormX:
        $ line = renpy.random.choice(["Probably not right now. . ."
            "Perhaps we keep it above the waist, " + character.Petname + "."
            "Careful what you put in there, you may not get it back."
            character.Petname + "! Not now. . ."
            "Release me, " + character.Petname + "."
            "I appreciate the intent, but this is not the time for it."
            "You go too far, " + character.Petname + "."])
    elif character == JubesX:
        $ line = renpy.random.choice(["Cool your jets, " + character.Petname + ". . ."
            "Maybe we keep it above the waist, " + character.Petname + "."
            "Watch your hands, or lose them."
            character.Petname + "! No. . ."
            "Hands off, " + character.Petname + "."
            "Hey, good instincts, but maybe hold off?"
            "Whoa, back off, " + character.Petname + "."])

    character.voice "[line]"

    return

label private_enough_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["I guess this is private enough. . ."])
    elif character == KittyX:
        $ line = renpy.random.choice(["I guess here is fine. . ."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["This does seem less. . . exposed."])
    elif character == LauraX:
        $ line = renpy.random.choice(["This does seem less. . . exposed."])
    elif character == JeanX:
        $ line = renpy.random.choice(["I guess. . . maybe we could do it here. . ."])
    elif character == StormX:
        $ line = renpy.random.choice(["This is a bit more secluded."])
    elif character == JubesX:
        $ line = renpy.random.choice(["I guess this is less public. . ."])

    character.voice "[line]"

    return

label recent_action_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["Mmm, again? Ok."
            "Mmm, again? Let me flex my hand a bit. . ."
            "I don't want to wear them out. . ."
            "Mmm, again? Ok, let me get the girls ready."
            "Mmm, again? [[stretches her jaw]"
            "Mmm, again? Ok, let's get to it."
            "You want to go again? Ok."
            "I think I'm warmed up. . ."])
    elif character == KittyX:
        $ line = renpy.random.choice(["Mmm, again? Ok."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["Mmmm, again? I suppose. . ."])
    elif character == LauraX:
        $ line = renpy.random.choice(["Mmmm, again? I guess. . ."])
    elif character == JeanX:
        $ line = renpy.random.choice(["Mmmm, again? I guess. . ."])
    elif character == StormX:
        $ line = renpy.random.choice(["Mmmm, again? I suppose. . ."])
    elif character == JubesX:
        $ line = renpy.random.choice(["Mmmm, again? I guess. . ."])

    character.voice "[line]"

    return

label not_in_public_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["I really don't think this is the right place for that!"
            character.Petname + "! Not in public!"
            "This just really isn't the time or place, " + character.Petname + "!"
            "Not in such an exposed place, " + character.Petname + "."
            "You really expect me to do that here? You realize how. . . exposed that would be?"
            "You really expect me to do that here?"
            "Not here!"
            "Even if I wanted to, it certainly wouldn't be here!"
            "That you would even suggest such a thing in a place like this. . ."
            "I'd be a bit embarassed doing that here."])
    elif character == KittyX:
        $ line = renpy.random.choice(["I don't like being so. . . exposed."
            "Time and place, " + character.Petname + "!"
            character.Petname + "! Not here!"
            character.Petname + "! Time and place!"
            "This just really isn't the time or place, " + character.Petname + "!"])
    elif character == EmmaX:
        $ line = renpy.random.choice(["I can't be seen doing that with you."
            "I have a reputation to maintain."])
    elif character == LauraX:
        $ line = renpy.random.choice(["I try to stay off the radar."])
    elif character == JeanX:
        $ line = renpy.random.choice(["I'm. . . not comfortable. . . in public. . ."])
    elif character == StormX:
        $ line = renpy.random.choice(["I should not be seen doing that."])
    elif character == JubesX:
        $ line = renpy.random.choice(["I don't wanna make a scene."])

    character.voice "[line]"

    return

label already_said_not_here_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["I told you not in public!"
            "I already told you this is too public!"
            "This is just way too exposed!"
            "I said not in public!"
            "Stop swinging that thing around in public!"
            "I already told you that I wouldn't do that out here!"
            "I told you that I didn't want you rubb'in up on me in public!"])
    elif character == KittyX:
        $ line = renpy.random.choice(["Not here!"])
    elif character == EmmaX:
        $ line = renpy.random.choice(["As I said, not here, " + character.Petname + "."])
    elif character == LauraX:
        $ line = renpy.random.choice(["I told you, not here, " + character.Petname + "."])
    elif character == JeanX:
        $ line = renpy.random.choice(["I told you. . . not here, " + character.Petname + "."])
    elif character == StormX:
        $ line = renpy.random.choice(["This area is too public, " + character.Petname + "."
            "As I said, not here, " + character.Petname + "."])
    elif character == JubesX:
        $ line = renpy.random.choice(["I told you, not here, " + character.Petname + "."])

    character.voice "[line]"

    return

label not_ready_yet_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["I just don't think I'm ready yet, " + character.Petname + ". . ."
            "I. . . don't think that's. . ."
            "Not now, " + character.Petname + "."
            "Let's not, ok " + character.Petname + "?"
            "Not yet, " + character.Petname + ". . ."
            "Oh, um, no, I'm not really comfortable with that. . ."
            "Um, not down there, " + character.Petname + ". . ."
            "I don't really want to touch it, " + character.Petname + ". . ."
            "I'm not really up for that, " + character.Petname + ". . ."
            "I don't think I'd like the taste, " + character.Petname + ". . ."
            ". . . well I don't know about that, " + character.Petname + ". . ."
            "I'm just not into toys, " + character.Petname + ". . ."
            "I just don't think I'm ready yet, " + character.Petname + ". . ."
            "I'm just not into that, " + character.Petname + ". . ."
            "That's kinda naughty, " + character.Petname + ". . ."])
    elif character == KittyX:
        $ line = renpy.random.choice(["I'm" + character.Like + "not ready for that, " + character.Petname + ". . ."
            "Not. . . yet. . . maybe later."
            "Oh, um, no, I'm not really comfortable with that. . ."
            "Not now, " + character.Petname + "."
            "Oh, um, no, I'm not really comfortable with that. . ."
            "Not yet, " + character.Petname + ". . ."
            "Let's not, ok " + character.Petname + "?"
            "Um, not down there, " + character.Petname + ". . ."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["I highly doubt you could handle them, " + character.Petname + ". . ."
            "Seems a bit forward, " + character.Petname + "."
            "Not now, " + character.Petname + "."
            "Let's not, ok " + character.Petname + "?"
            "I'd rather not today. . ."
            "Not yet, " + character.Petname + ". . ."
            "I'm really not comfortable with that. . ."
            "I don't think we're there yet, " + character.Petname + ". . ."])
    elif character == LauraX:
        $ line = renpy.random.choice(["Look, I don't know if we're ready for that, " + character.Petname + ". . ."
            "Seems a bit aggressive, " + character.Petname + "."
            "I'm really not cool with that. . ."
            "I'd rather not today. . ."
            "I'm not sure we're there yet, " + character.Petname + ". . ."
            "Not now, " + character.Petname + "."
            "Let's not, ok " + character.Petname + "?"
            "I don't think we're there yet, " + character.Petname + ". . ."])
    elif character == JeanX:
        $ line = renpy.random.choice(["Look, don't touch, " + character.Petname + ". . ."
            "Not now, " + character.Petname + "."
            "Let's not, ok " + character.Petname + "?"
            "Not yet, " + character.Petname + ". . ."
            "I'd rather not."
            "I'd rather not today. . ."
            "I don't think we're there yet, " + character.Petname + ". . ."])
    elif character == StormX:
        $ line = renpy.random.choice(["Perhaps some other time, " + character.Petname + ". . ."
            "I would rather you did not, " + character.Petname + "."
            "Not now, " + character.Petname + "."
            "I am unsure about that. . ."
            "I would rather not. . ."
            "I would rather not, " + character.Petname + ". . ."
            "I would be uncomfortable with that. . ."
            "Perhaps go slower, " + character.Petname + ". . ."])
    elif character == JubesX:
        $ line = renpy.random.choice(["Look, I don't know if we're ready for that, " + character.Petname + ". . ."
            "Kinda forward, " + character.Petname + "."
            "I'm really not cool with that. . ."
            "I'd rather not today. . ."
            "Let's not, ok " + character.Petname + "?"
            "Not now, " + character.Petname + "."
            "I don't think we're there yet, " + character.Petname + ". . ."])

    character.voice "[line]"

    return

label no_problem_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["Ok, no problem, " + character.Petname + "."
            "Yeah, fine, " + character.Petname + "."
            "Yeah, ok, " + character.Petname + "."])
        "Fine."
        "No problem."
    elif character == KittyX:
        $ line = renpy.random.choice(["It's cool, " + character.Petname + "."
            "Yeah, ok, " + character.Petname + "."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["Don't concern yourself, " + character.Petname + "."
            "I appreciate your restraint."])
    elif character == LauraX:
        $ line = renpy.random.choice(["No worries."
            "It's cool."
            "It's cool, " + character.Petname + "."])
    elif character == JeanX:
        $ line = renpy.random.choice(["It's fine, I get it."])
    elif character == StormX:
        $ line = renpy.random.choice(["Don't concern yourself, " + character.Petname + "."
            "I appreciate your restraint."])
    elif character == JubesX:
        $ line = renpy.random.choice(["Yeah, whatever."])

    character.voice "[line]"

    return

label maybe_later_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["I'll give it some thought, " + character.Petname + "."
            "It's. . . possible, " + character.Petname + "."
            "I'll be thinking about it, " + character.Petname + "."
            "Anything's possible, " + character.Petname + "."
            "Heh, maybe, " + character.Petname + "."])

        "I'll give it some thought, " + character.Petname + "."
        ". . .{p}I guess?"
        "We'll have to see."
        "I might get hungry, " + character.Petname + "."
        "Maybe I'll practice on my own time, " + character.Petname + "."
        "Yeah, maybe, " + character.Petname + "."
    elif character == KittyX:
        $ line = renpy.random.choice(["Um, yeah, maybe later."
            "I'll give it some thought, " + character.Petname + "."
            "Heh, maybe, " + character.Petname + "."
            "Anything's possible, " + character.Petname + "."
            "I'll be thinking about it, " + character.Petname + "."
            "It's. . . possible, " + character.Petname + "."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["Well, I can't rule it out. . ."
            "I'll give it some thought, " + character.Petname + "."
            "Perhaps."
            "I'll be thinking about it, " + character.Petname + "."
            "It's. . . possible, " + character.Petname + "."])
    elif character == LauraX:
        $ line = renpy.random.choice(["Eh. Maybe."
            "Maybe, " + character.Petname + "."
            "Anything's possible, " + character.Petname + "."
            "Maybe?"
            "It's. . . possible, " + character.Petname + "."])
    elif character == JeanX:
        $ line = renpy.random.choice([". . . I guess? Maybe."
            "Well, I'll give it some thought, " + character.Petname + "."])
    elif character == StormX:
        $ line = renpy.random.choice(["I will give it some thought, " + character.Petname + "."])
    elif character == JubesX:
        $ line = renpy.random.choice(["Eh. Maybe."
            "Maybe, " + character.Petname + "."
            "Maybe?"
            "I'll be thinking about it, " + character.Petname + "."
            "Anything's possible, " + character.Petname + "."
            "It's. . . possible, " + character.Petname + "."])

    character.voice "[line]"

    return

label reward_politeness_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["Heh, I suppose I can hardly refuse ya when you use the magic words . . ."
            "You better work your mouth that hard on these."
            "Well, if you're gonna beg. . ."])
    elif character == KittyX:
        $ line = renpy.random.choice(["Well" + character.Like + "if you ask nicely. . ."
            "I like it when you beg. . ."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["Politeness can be rewarded. . ."
            "I do enjoy hearing you beg. . ."])
    elif character == LauraX:
        $ line = renpy.random.choice(["Well if you're going to be a little bitch about it. . ."
            "Oooh, beg for me. . ."])
    elif character == JeanX:
        $ line = renpy.random.choice(["Oh, fine, just don't start crying."
            "Oooh, beg for me. . ."])
    elif character == StormX:
        $ line = renpy.random.choice(["Well, I suppose. . ."
            "I suppose it could not hurt. . ."
            "Well, one could not hurt. . ."
            "I suppose it does not hurt. . ."])
    elif character == JubesX:
        $ line = renpy.random.choice(["Geeze, don't whine about it. . ."
            "Oooh, beg for me. . ."])

    character.voice "[line]"

    return

label please_not_good_enough_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["I'm afraid not this time, sorry " + character.Petname + "."])
    elif character == KittyX:
        $ line = renpy.random.choice(["Um, still no."
            "Nuh uh."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["This wasn't a \"tone\" issue."
            "No."])
    elif character == LauraX:
        $ line = renpy.random.choice(["Well if you're going to be a little bitch about it. . ."
            "No."])
    elif character == JeanX:
        $ line = renpy.random.choice(["No way."
            "No."
            "Oh, don't cry."])
    elif character == StormX:
        $ line = renpy.random.choice(["No, thank you."
            "No."
            "It is not appropriate."])
    elif character == JubesX:
        $ line = renpy.random.choice(["Geeze, don't whine about it. . ."
            "No."])

    character.voice "[line]"

    return

label learn_to_take_no_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["Learn to take \"no\" for an answer, " + character.Petname + "."
            "I just don't want to, " + character.Petname + "."
            "I'aint tellin you again."
            "Look, I already told you no thanks, " + character.Petname + "."
            "Read my lips, no."
            "Learn to take \"no\" for an answer, " + character.Petname + "."])
    elif character == KittyX:
        $ line = renpy.random.choice(["{i}Listen{/i}!"
            "How many times do I have to say \"no?\""
            "I'm not telling you again."
            "Look, I already told you no thanks, " + character.Petname + "."
            "You can eat a dick, 'cos I'm not."
            "Learn to take \"no\" for an answer, " + character.Petname + "."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["You need to pay attention when I speak to you."
            "I don't appreciate having to repeat myself, " + character.Petname + "."
            "I've refused, end of story."
            "Then I hope you can take care of yourself."
            "Learn to take \"no\" for an answer, " + character.Petname + "."
            "I won't repeat myself."
            "Don't make me repeat myself."])
    elif character == LauraX:
        $ line = renpy.random.choice(["Listen to the words that are coming out of my mouth."
            "I don't like to repeat myself, " + character.Petname + "."
            "Don't ask again."
            "Look, I already told you no."
            "Suck this then."
            "Learn to take \"no\" for an answer, " + character.Petname + "."
            "I'm not telling you again."])
    elif character == JeanX:
        $ line = renpy.random.choice(["I don't want to have to go through this again."
            "Don't ask again."
            "I already told you no."
            "You want me to make you suck yourself?"
            "Learn to take \"no\" for an answer, " + character.Petname + "."
            "I'm not telling you again."])
    elif character == StormX:
        $ line = renpy.random.choice(["I have been clear on this."
            "Do not make me repeat myself."
            "I have refused. Learn to accept that."
            "Then I hope you can take care of yourself."
            "Learn to take \"no\" for an answer, " + character.Petname + "."
            "I shall not repeat myself."])
    elif character == JubesX:
        $ line = renpy.random.choice(["I'm pretty clear on this, NO."
            "Don't ask again."
            "Look, I already told you no."
            "Suck this then."
            "Learn to take \"no\" for an answer, " + character.Petname + "."
            "I'm not telling you again."])

    character.voice "[line]"

    return

label not_happening_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["Not hap'nin."
            "Not hap'nin, " + character.Petname + "."
            "No luck, " + character.Petname + "."
            "Tsk, not this time, " + character.Petname + "."
            "Shoo, " + character.Petname + "."
            "I. . . not there!!"
            "Ew!"
            "Um, no thanks, " + character.Petname + "."
            "What?! Gross!"
            "I'd really rather not."
            "That isn't really how I planned to use my feet today"
            "How about let's not, " + character.Petname + "."
            "Not interested."
            "No way."
            "Not happening."])
    elif character == KittyX:
        $ line = renpy.random.choice(["No way."
            "Nuh uh."
            "Nooope."
            "Ew."
            "Ugh!"
            "That's. . . not cool."
            "Scram, " + character.Petname + "."
            "Um, no thanks, " + character.Petname + "."
            "No luck " + character.Petname + "."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["No."
            "I'm sorry, not now."
            "I know, I'm as disappointed as you are."
            "No. Thank you."
            "Not today, " + character.Petname + "."
            "No thank you, " + character.Petname + "."])
    elif character == LauraX:
        $ line = renpy.random.choice(["No."
            "I'm sorry, not now."
            "Yeah, sorry."
            "Not today, " + character.Petname + "."
            "Nope."
            "No thank you, " + character.Petname + "."])
    elif character == JeanX:
        $ line = renpy.random.choice(["No."
            "I'm sorry, not now."
            "Yeah, sorry."
            "Not today, " + character.Petname + "."
            "Nope."
            "No thanks, " + character.Petname + "."])
    elif character == StormX:
        $ line = renpy.random.choice(["No, I do not think so."
            "No."
            "I'm sorry, not now."
            "No. Thank you."
            "No, I do not think so."])
    elif character == JubesX:
        $ line = renpy.random.choice(["No."
            "Nope."
            "Not today, " + character.Petname + "."
            "Yeah, sorry."
            "No thank you, " + character.Petname + "."])

    character.voice "[line]"

    return

label you_had_your_shot_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["Sorry, " + character.Petname + " you aren't touching these again."
            "Sorry, " + character.Petname + " you aren't getting these in your mouth."
            "Sorry, keep your tongue in your mouth."
            "Sorry, hands off the booty."
            "Fresh!"
            "I think you should keep your fingers to yourself."
            "Sorry, keep your hands out of there."
            "I think you can manage it yourself this time. . ."
            "Not right now, " + character.Petname + ". . ."
            "I think I'll let you know when I want you touching these again."
            "I think I've got the taste out of my mouth, thanks."
            "Sorry, you can keep your toys to yourself."
            "Sorry, you can keep your toys out of there."
            "Maybe you could go fuck yourself instead."
            "Eh-eh, not anymore, " + character.Petname + "."
            "The only thing you can do with my ass is kiss it, " + character.Petname + ".{p}. . .Don't get any ideas."])
    elif character == KittyX:
        $ line = renpy.random.choice(["You had your shot."
            "Fresh!"
            "Sorry, no more of that."
            "I don't feel like it."
            "Sorry, hands to yourself."
            "Keep your head out of there."
            "Sorry, keep your hands out of there."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["I'm afraid you haven't earned back my good graces."
            "Hands."
            "Sorry, no more of that."
            "Keep your head out of there."
            "I'm sorry, keep your hands to yourself."
            "I don't feel like it."
            "Sorry, keep your hands out of there."])
    elif character == LauraX:
        $ line = renpy.random.choice(["You'll have to earn that back."
            "Keep your hands to yourself."
            "Sorry, no more of that."
            "Sorry, keep your hands to yourself."
            "Keep your head out of there."
            "I don't feel like it."
            "Sorry, fingers outside."])
    elif character == JeanX:
        $ line = renpy.random.choice(["We've had enough of that."
            "Keep your hands to yourself."
            "We've had enough of that."
            "I don't feel like it."
            "Sorry, keep your hands to yourself."
            "Keep your tongue to yourself."
            "You can keep those to yourself."])
    elif character == StormX:
        $ line = renpy.random.choice(["No, I do not think so."])
    elif character == JubesX:
        $ line = renpy.random.choice(["You'll have to earn that."
            "Keep your hands to yourself."
            "Keep your head out of there."
            "Sorry, keep your hands to yourself."
            "I'm not into it."
            "Sorry, no more of that."
            "Sorry, keep your fingers outside."])

    character.voice "[line]"

    return

label forced_but_not_unwelcome_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["Fine, if that's what you want."
            "Hmmph, well I guess you can go to town. . ."
            "Hmmph."
            "Fine, I suppose."
            "Oh. . . well, ok then. . ."
            "Well, at least make it worth it."
            "Ok, get in there if you're so determined."])
            "Ok, fine, whip it out."
            "Ok, fine"
            "Ok, fine. If we're going to do this, stick it in already."
            "Ok, fine. Whatever."])
    elif character == KittyX:
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
    elif character == EmmaX:
        $ line = renpy.random.choice(["That is not appropriate. . .{p}but neither is it entirely unwelcome. . ."
            "Hmmph."
            "Oh, if you insist. . ."
            "If you insist. . ."
            "Fine, I suppose."
            "Hm. Alright, but don't push your luck, " + character.Petname + "."
            "Well hello there. . ."
            "Ok, fine. If we're going to do this, stick it in already."
            "Oh, fine. . ."
            "Oh, very well."
            "Suit yourself."])
    elif character == LauraX:
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
    elif character == JeanX:
        $ line = renpy.random.choice(["Hey. . .{p}. . . whatever. . ."
            ". . . whatever. . ."
            ". . . Ok, whatever."
            "Ooo! Well ok then. . ."
            ". . ."
            "Fine."
            "Ok, fine. If we're going to do this, stick it in already."
            "I guess you won't take \"no\" for an answer. . ."])
    elif character == StormX:
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
    elif character == JubesX:
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

    character.voice "[line]"

    return

label forced_but_welcome_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["Sure, get in there."
            "Fine, grab a cheek."])
    elif character == KittyX:
        $ line = renpy.random.choice(["Ok, whatever."
            "Ok, geeze."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["If you must. . ."
            "If you insist. . ."])
    elif character == LauraX:
        $ line = renpy.random.choice(["If you must. . ."
            "Meh. . ."
            "Going there, huh. . ."
            "If you insist. . ."])
    elif character == JeanX:
        $ line = renpy.random.choice(["If you must. . ."
            "Whatever. . ."
            "If you insist. . ."])
    elif character == StormX:
        $ line = renpy.random.choice(["If you must. . ."
            "If you insist. . ."])
    elif character == JubesX:
        $ line = renpy.random.choice(["If you haveta. . ."
            "Going there, huh. . ."
            "Meh. . ."
            "If you insist. . ."])

    character.voice "[line]"

    return

label just_told_you_no_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["I {i}just{/i} told you \"no,\" " + character.Petname + "."])
        "I {i}just{/i} told you \"no,\" " + character.Petname + "."
        "What part of \"no,\" did you not get, " + character.Petname + "?"
    elif character == KittyX:
        $ line = renpy.random.choice([character.Like + "no way, " + character.Petname + "."
            "I" + character.Like + "{i}just{/i} told you \"no!\""])
    elif character == EmmaX:
        $ line = renpy.random.choice(["Your persistance is doing you no favors, " + character.Petname + "."])
    elif character == LauraX:
        $ line = renpy.random.choice(["Take a breath here, before you regret it."])
    elif character == JeanX:
        $ line = renpy.random.choice(["I'm not used to repeating myself."])
    elif character == StormX:
        $ line = renpy.random.choice(["Do not persist in this, " + character.Petname + "."
            "Your persistance is doing you no favors, " + character.Petname + "."])
    elif character == JubesX:
        $ line = renpy.random.choice(["I already told you, \"no\"."])

    character.voice "[line]"

    return

label come_and_get_em_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["Ok " + character.Petname + " come and get'em."
            "Ok " + character.Petname + " go ahead."
            "Oooooooh. . ."
            "God yes."
            "Sure, grab a cheek."
            "Sure, get in there."])
    elif character == KittyX:
        $ line = renpy.random.choice(["Ok " + character.Petname + " come and get'em."
            "Ok, whatever."
            "Mmmmmm."
            "Ok, go for it."
            "Oooooooh. . ."
            "Wha. . ."
            "Ok " + character.Petname + " go ahead."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["That sounds lovely, ravish me."
            "Mmmm, I couldn't refuse. . ."
            "Mmmmmm. . ."
            "I can't exactly refuse. . ."
            "Mmm. . . naughty."
            "Ok " + character.Petname + " go ahead."])
    elif character == LauraX:
        $ line = renpy.random.choice(["Sure, sounds fun."
            "Mmmm, I couldn't refuse. . ."
            "Mmmmmm. . ."
            "Yeah, ok. . ."
            "Mmm. . . naughty."
            "Ok " + character.Petname + " go ahead."])
    elif character == JeanX:
        $ line = renpy.random.choice(["Sure, sounds fun."
            "Mmmm, I couldn't refuse. . ."
            "Mmmmmm. . ."
            "Yeah, ok. . ."
            "Mmm. . . naughty."
            "Ok " + character.Petname + " go ahead."])
    elif character == StormX:
        $ line = renpy.random.choice(["I would love that. . ."
            "Mmmm, I couldn't refuse. . ."
            "Mmmmmm. . ."
            "Mmm. . . naughty."
            "I suppose that is reasonable. . ."
            "Ok " + character.Petname + " go ahead."])
    elif character == JubesX:
        $ line = renpy.random.choice(["Sure, sounds fun."
            "Mmmm, I couldn't refuse. . ."
            "Mmmmmm. . ."
            "Mmm. . . naughty."
            "Yeah, ok. . ."
            "Ok " + character.Petname + " go ahead."])

    character.voice "[line]"

    return

label gently_lines(character):
    if character == RogueX:
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
    elif character == KittyX:
        $ line = renpy.random.choice(["Didn't get enough earlier?"
            "Maybe not so rough this time though."
            "Take it easy though."
            "Take it a bit gently, I'm still shaking from earlier."
            "Huh? Again?"
            "I must have done something right."
            "What a girl wants. . ."
            "Mmm. . ."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["You didn't get enough earlier?"
            "Huh? Again?"
            "Perhaps not so rough this time?"
            "I must have done something right."
            "What a queen deserves. . ."
            "Relax, gently. . ."
            "Take it a bit gently, I'm still shaking from earlier."
            "Mmm. . ."
            "Didn't get enough earlier?"])
    elif character == LauraX:
        $ line = renpy.random.choice(["You didn't get enough earlier?"
            "Chill. . ."
            "Take it slow, I'm still shaking from earlier."
            "Huh? Again?"
            "I must have done something right."
            "I do like this treatment. . ."
            "Mmm, you like that? . ."
            "Mmm. . ."])
    elif character == JeanX:
        $ line = renpy.random.choice(["You didn't get enough earlier?"
            "Chill. . ."
            "Take it slow, I'm still shaking from earlier."
            "Huh? Again?"
            "I must have done something right."
            "I do like this. . ."
            "Mmm, you like that? . ."
            "Mmm. . ."])
    elif character == StormX:
        $ line = renpy.random.choice(["You didn't get enough earlier?"
            "Gently. . . gently. . ."
            "Relax, gently. . ."
            "Take it a bit gently, I am still glowing from earlier."
            "Huh? Again?"
            "I must have done something right."
            "What a queen deserves. . ."
            "Perhaps not so rough this time?"
            "Mmm. . ."])
    elif character == JubesX:
        $ line = renpy.random.choice(["You didn't get enough earlier?"
            "Relax. . ."
            "Take it slow, I'm still shaking from earlier."
            "Huh? Again?"
            "I must have done something right."
            "I guess fair's fair. . ."
            "Mmm, you like that? . ."
            "Mmm. . ."])

    character.voice "[line]"

    return

label had_enough_of_this_lines(character):
    if character == RogueX:
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
    elif character == KittyX:
        $ line = renpy.random.choice(["I told you not here!"
            "I told you not to touch me like that in public!"
            "You already got your answer!"
            "I told you that wasn't appropriate!"])
    elif character == EmmaX:
        $ line = renpy.random.choice(["You've been warned."
            "I told you not to touch me like that in public!"
            "You already got your answer!"
            "I told you that wasn't appropriate!"])
    elif character == LauraX:
        $ line = renpy.random.choice(["I've had enough of this today."
            "I told you not to touch me like that in public!"
            "I told you that wasn't appropriate!"
            "You already got your answer!"])
    elif character == JeanX:
        $ line = renpy.random.choice(["I've had enough of this today."
            "I told you not to touch me like that in public!"
            "I told you that wasn't appropriate!"
            "You already got your answer!"])
    elif character == StormX:
        $ line = renpy.random.choice(["I have already told you my answer."
            "I told you not to touch me like that in public!"
            "You already got your answer!"])
    elif character == JubesX:
        $ line = renpy.random.choice(["I've had enough of this today."
            "I told you not to touch me like that in public!"
            "I told you that wasn't appropriate!"
            "I told you not to touch me like that in public!"
            "You already got your answer!"])

    character.voice "[line]"

    return

label already_said_no_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["I already told you \"no,\" " + character.Petname + "."
            "I already told you no, take a hint."
            "What part of \"no\" don't you understand?"
            "I already told you \"no,\" " + character.Petname + "."
            "I told you \"no\" earlier " + character.Petname + "."])
    elif character == KittyX:
        $ line = renpy.random.choice(["I" + character.Like + "already told you \"no.\""
            character.Like + "take a lesson, " + character.Petname + "."
            "Get a clue, " + character.Petname + "!"
            "I'm telling you to give it a rest!"])
    elif character == EmmaX:
        $ line = renpy.random.choice(["I believe you know my answer on this matter."
            "I'm not in the mood for this, " + character.Petname + "."
            "You heard me the first time."])
    elif character == LauraX:
        $ line = renpy.random.choice(["Don't make me tell you again today."
            "Grrrrrrrrr."
            "Back off!"])
    elif character == JeanX:
        $ line = renpy.random.choice(["Don't ask me again today."
            "Go away!"
            "Give me some space!"])
    elif character == StormX:
        $ line = renpy.random.choice(["I have already told you my answer."
            "I believe you know my answer on this matter."
            "I am far too irate for this."
            "Stop pestering me!"])
    elif character == JubesX:
        $ line = renpy.random.choice(["Don't make me tell you again today."
            "Grrrrrrrrr."
            "Back off!"])

    character.voice "[line]"

    return

label rather_not_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["I'd really rather not."
            "Oh, um, no, I'm not really comfortable with that. . ."
            "Not right now, " + character.Petname + ". . ."
            "Maybe not right now, ok?"
            "I don't think we need any toys, " + character.Petname + "."])
    elif character == KittyX:
        $ line = renpy.random.choice(["Um, no."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["You wish."])
    elif character == LauraX:
        $ line = renpy.random.choice(["Keep dreaming."
            "You wish."])
    elif character == JeanX:
        $ line = renpy.random.choice(["Yeah, you wish."
            "You wish."])
    elif character == StormX:
        $ line = renpy.random.choice(["Hmm, no."])
    elif character == JubesX:
        $ line = renpy.random.choice(["Cute, but no."
            "You wish."])

    character.voice "[line]"

    return

label went_too_far_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["I don't want you touching me."
            "I don't want your lips on me."
            "Um, no way."
            "Not even, " + character.Petname + "."
            "Not even that much."
            "Stay out of my pants, " + character.Petname + "."
            "Hands off the booty!"
            "Ew, no way."
            "I'm not that kind of girl!"
            "Not even with my feet."
            "That isn't something I'd want!"
            "I'm not going to let you use that on me."
            "I'm not doing that just because you have me over a barrel."
            "That's a bit much, even for you."
            "Even that's not worth it."])
    elif character == KittyX:
        $ line = renpy.random.choice(["Not even."
            "Keep away from my kitty, " + character.Petname + "."
            "Back off!"
            "Um, no way."
            "Ew, no way."
            "Not even, " + character.Petname + "."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["Don't push your luck."
            "I don't think so, " + character.Petname + "."
            "I don't think so."
            "I really can't, " + character.Petname + "."
            "Do you want to keep those fingers?"
            "I'm not going that far today."])
    elif character == LauraX:
        $ line = renpy.random.choice(["No."
            "I don't think so, " + character.Petname + "."
            "I don't think so."
            "I really can't, " + character.Petname + "."
            "Do you want to keep those fingers?"
            "I'm not going there today."])
    elif character == JeanX:
        $ line = renpy.random.choice(["No."
            "I don't think so, " + character.Petname + "."
            "I don't think so."
            "I really can't, " + character.Petname + "."
            "Mmmm, no."
            "I'm not going there today."])
    elif character == StormX:
        $ line = renpy.random.choice(["You go too far."])
    elif character == JubesX:
        $ line = renpy.random.choice(["No."
            "I don't think so, " + character.Petname + "."
            "I don't think so."
            "I really can't, " + character.Petname + "."
            "Do you want to keep those fingers?"
            "I'm not going there today."])

    character.voice "[line]"

    return

label warm_hands_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["You like how those feel, huh?"
            "You're just going at them, huh?"
            "You like how that feels, huh?"
            "What are you even doing down there?"
            "Uh, that's nice, but. . ."
            "You like it down there?"])
    elif character == KittyX:
        $ line = renpy.random.choice(["You like how those feel, huh?"
            "You're just going at them, huh?"
            "Are they keeping you satisfied?"
            "You like how that feels, huh?"
            "You like it down there?"
            "Uh, that's nice, but. . ."
            "What are you even?"])
    elif character == EmmaX:
        $ line = renpy.random.choice(["Luxurious, yes?"
            "They really are magnificent, aren't they?"
            "lovely, aren't they?"
            "You like how that feels, huh?"
            "Isn't it just delicious?"
            "Mmmm I do enjoy that. . ."
            "Ungh, you're getting going there. . ."
            "You certainly are enthusiastic. . ."])
    elif character == LauraX:
        $ line = renpy.random.choice(["Kinda nice, but. . ."
            "Enjoying yourself?"
            "This is kinda nice. . ."
            "Mmmm, you're enjoying that, huh?"
            "Isn't it just delicious?"
            "Mmmm. . ."
            "Ungh, you're really getting in there. . ."
            "You seem to be enjoying yourself. . ."])
    elif character == JeanX:
        $ line = renpy.random.choice(["Kinda nice, but. . ."
            "Having fun there?"
            "This is kinda nice. . ."
            "Mmmm, you're enjoying that, huh?"
            "Isn't it just delicious?"
            "Mmmm. . ."
            "Ungh, you're really getting in there. . ."
            "You seem to be enjoying yourself. . ."])
    elif character == StormX:
        $ line = renpy.random.choice(["Your hands are so warm. . ."
            "You really seem to enjoy those. . ."
            "Mmmm, yes. . . deeper. . ."
            "Oh, that is delightful. . ."
            "Mmmm. . ."
            "Ooh, watch it, watch it. . ."
            "You are quite enthusiastic. . ."])
    elif character == JubesX:
        $ line = renpy.random.choice(["Ok, but, uh. . ."
            "Having fun?"
            "Yeah, I like that too. . ."
            "Mmmm. . ."])

    character.voice "[line]"

    return

label try_something_else_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["I know you're having fun, but maybe we could try something else " + character.Petname + "."
            character.Petname + " this is getting uncomfortable, maybe we could try something else."
            character.Petname + " this is nice, but could we do something else?"
            character.Petname + " I know you're having fun down there, but maybe we could try something else."])
    elif character == KittyX:
        $ line = renpy.random.choice(["You look like you're having fun there, but maybe we could" + character.Like + "try something else?"
            "Maybe we could try something else here " + character.Petname + "?"
            character.Petname + " I know you're having fun down there, but maybe we could try something else."
            character.Petname + " this is nice, but could we do something else?"
            character.Petname + " this is getting kind sore, maybe we could try something else."
            character.Petname + " this is getting weird, maybe we could try something else."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["You certainly seem to be enjoying yourself, but perhaps we could add some variety?"
            "Perhaps we could try something else, " + character.Petname + "?"
            character.Petname + " I know you're having fun down there, but maybe we could try something else."
            character.Petname + " this is nice, but could we do something else?"
            character.Petname + " this is getting kind sore, maybe we could try something else."
            character.Petname + " this is getting weird, maybe we could try something else."])
    elif character == LauraX:
        $ line = renpy.random.choice(["Maybe change things up a little?"
            "Maybe it's time for something else, " + character.Petname + "?"
            character.Petname + " could we try something different?"])
    elif character == JeanX:
        $ line = renpy.random.choice(["Maybe try something else?"
            "Maybe it's time for something else, " + character.Petname + "?"
            character.Petname + " could we try something different?"])
    elif character == StormX:
        $ line = renpy.random.choice(["I am sure that is fun, but could we try something different?"])
    elif character == JubesX:
        $ line = renpy.random.choice(["Could we maybe try. . . something else?"])

    character.voice "[line]"

    return

label this_is_boring_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["Well if that's your attitude, I don't need your \"help\"."])
    elif character == KittyX:
        $ line = renpy.random.choice(["Fun for you maybe, I'm tired of it."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["Well perhaps you are enjoying yourself, but I'm tired of this."
            "You may be enjoying yourself, but I'm getting a bit sore."])
    elif character == LauraX:
        $ line = renpy.random.choice(["I'm kinda bored here."
            "Well, I've got better things to be doing."])
    elif character == JeanX:
        $ line = renpy.random.choice(["Well -I'm- bored."
            "Well, I've got better things to be doing."])
    elif character == StormX:
        $ line = renpy.random.choice(["Well however much you are enjoying yourself, I need to take a break."])
    elif character == JubesX:
        $ line = renpy.random.choice(["This is kinda boring. . .."])

    character.voice "[line]"

    return

label wrap_this_up_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["You might want to wrap this up, it's getting late."])
    elif character == KittyX:
        $ line = renpy.random.choice(["It's" + character.Like + "getting kinda late."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["It's getting late. . ."])
    elif character == LauraX:
        $ line = renpy.random.choice(["It's getting late, we should wrap this up."])
    elif character == JeanX:
        $ line = renpy.random.choice(["Wow, look at the time. . ."])
    elif character == StormX:
        $ line = renpy.random.choice(["It is getting late, " + character.Petname + ". . ."])
    elif character == JubesX:
        $ line = renpy.random.choice(["I could use a break soon. . ."])

    character.voice "[line]"

    return

label time_to_stop_soon_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["Seriously, it'll be time to stop soon."])
    elif character == KittyX:
        $ line = renpy.random.choice(["We should wrap this up."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["We should take a break soon."])
    elif character == LauraX:
        $ line = renpy.random.choice(["Tick tock, " + character.Petname + "."])
    elif character == JeanX:
        $ line = renpy.random.choice(["We should probably wrap this up, " + character.Petname + "."])
    elif character == StormX:
        $ line = renpy.random.choice(["We should take a break soon."])
    elif character == JubesX:
        $ line = renpy.random.choice([". . . I could really use a break here. . ."])

    character.voice "[line]"

    return

label im_done_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["Ok, " + character.Petname + " that's enough of that for now."])
    elif character == KittyX:
        $ line = renpy.random.choice(["Time to take a little break, for now."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["We need to stop for a moment, let me catch my breath."])
    elif character == LauraX:
        $ line = renpy.random.choice(["Ok, " + character.Petname + " breaktime."])
    elif character == JeanX:
        $ line = renpy.random.choice(["Ok, " + character.Petname + " time for a break."])
    elif character == StormX:
        $ line = renpy.random.choice(["I need to take a moment to collect myself."])
    elif character == JubesX:
        $ line = renpy.random.choice(["Ok, that's it, I need a break."])

    character.voice "[line]"

    return

label that_was_nice_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["That was. . . nice."
            "That was . . . real pleasant, " + character.Petname + "."
            "I . . . really liked that, " + character.Petname + "."
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
            "That was . . . interesting " + character.Petname + ". We'll have to do that again sometime."
            "That was pretty hot, " + character.Petname + ", we'll have to do that again sometime."
            "That was really great, " + character.Petname + ", we'll have to do that again sometime."])
    elif character == KittyX:
        $ line = renpy.random.choice(["I liked that."
            "I hope there was" + character.Like + "enough to work with."
            "I hope they were enough for you. . ."
            "That was. . . good for you?"
            "Huh. . . um. . ."
            "I feel like I've been waiting" + character.Like + "a million years for that."
            "Anal. . . huh, who knew?"
            "I. . . liked that a lot."
            "That was odd. . ."
            "Was it. . . good?"
            "Your hand is. . . bigger than mine."])
    elif character == EmmaX:
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
    elif character == LauraX:
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
    elif character == JeanX:
        $ line = renpy.random.choice(["Well that was. . . something."
            "I bet you enjoyed that."
            "Well, that was a nice surprise. . ."
            "You really put that tongue to work. . ."
            "That was. . . nice. . ."
            "Blew your mind, uh?"
            "Hmmm, that was nice. . ."
            "Ok, that was. . . fine."
            "That was. . . interesting. . ."])
    elif character == StormX:
        $ line = renpy.random.choice(["Thank you for that."
            "That was quite fun. . ."
            "That was certainly enjoyable."
            "You certainly. . . reached some interesting places there. . ."
            "You really do have a talent for that. . ."
            "That was. . . nice. . ."
            "That one caught me by surprise. . ."
            "That was. . . certainly interesting. . ."])
    elif character == JubesX:
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

    character.voice "[line]"

    return

label was_that_enough_lines(character):
    if character == RogueX:
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
    elif character == KittyX:
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
    elif character == EmmaX:
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
    elif character == LauraX:
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
    elif character == JeanX:
        $ line = renpy.random.choice(["Was that enough?"
            "You get what you wanted out of that?"
            "Did you find what you were looking for?"
            "I bet you enjoyed that."
            "Satisfied?"
            "That was great. . ."
            "I guess that could have gone worse. . ."
            "Was that good for you?"
            "I guess that wasn't so bad. . ."])
    elif character == StormX:
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
    elif character == JubesX:
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

    character.voice "[line]"

    return

label take_a_breather_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["We've been at it for a while now, let's take a breather."])
    elif character == KittyX:
        $ line = renpy.random.choice(["We've been at it for a while now, let's take a breather."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["I think we could both do with a short break."])
    elif character == LauraX:
        $ line = renpy.random.choice(["You're looking a bit worn out, maybe take a break."])
    elif character == JeanX:
        $ line = renpy.random.choice(["You're looking a bit worn out, maybe take a break."])
    elif character == StormX:
        $ line = renpy.random.choice(["I think we could both do with a short break."])
    elif character == JubesX:
        $ line = renpy.random.choice(["Hey, I could use a break, how 'bout you?"])

    character.voice "[line]"

    return

label got_some_spunk_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["Oh?"])
    elif character == KittyX:
        $ line = renpy.random.choice(["Huh?"])
    elif character == EmmaX:
        $ line = renpy.random.choice(["Huh?"])
    elif character == LauraX:
        $ line = renpy.random.choice(["What?"])
    elif character == JeanX:
        $ line = renpy.random.choice(["What?"])
    elif character == StormX:
        $ line = renpy.random.choice(["Oh, what do you mean?"])
    elif character == JubesX:
        $ line = renpy.random.choice(["What?"])

    character.voice "[line]"

    return

label thats_it_for_now_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["That's it. . . for now."])
    elif character == KittyX:
        $ line = renpy.random.choice(["That's it. . . for now."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["That's all you get. . . for now."])
    elif character == LauraX:
        $ line = renpy.random.choice(["That's all. . . for now at least."])
    elif character == JeanX:
        $ line = renpy.random.choice(["That's all. . . for now at least."])
    elif character == StormX:
        $ line = renpy.random.choice(["I think that you have had enough for the moment."])
    elif character == JubesX:
        $ line = renpy.random.choice(["Ok, that should be plenty for now."])

    character.voice "[line]"

    return

label get_out_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["I don't want to deal with you right now."
            "Buzz off already."
            "I really think you should leave."])
    elif character == KittyX:
        $ line = renpy.random.choice(["Nooope."
            "GTFO."
            "Go. Now."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["I haven't any time for this."
            "Out."
            "I think you should leave now."])
    elif character == LauraX:
        $ line = renpy.random.choice(["Nope."
            "Fuck off."
            "Get out before we both regret it."])
    elif character == JeanX:
        $ line = renpy.random.choice(["Out!"])
    elif character == StormX:
        $ line = renpy.random.choice(["Get out."
            "Out. Now."])
    elif character == JubesX:
        $ line = renpy.random.choice(["Out!"])

    character.voice "[line]"

    if character in [RogueX, KittyX, EmmaX, LauraX, JeanX, JubesX]:
        $ line = renpy.random.choice([character.name + " pushes you back into the hall and slams the door. You head back to your room."
            character.name + " shoves you back into the hall and slams the door. You head back to your room."])
    elif character == StormX:
        $ line = renpy.random.choice([character.name + " pushes you to the top of the stairs and slams the door. You head back to your room."])
    "[line]"

    return

label first_time_pussy_eaten_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["That's pretty intimate, " + character.Petname + ". . ."])
    elif character == KittyX:
        $ line = renpy.random.choice(["That's pretty intimate, " + character.Petname + ". . ."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["I'm not sure we're at that stage, " + character.Petname + ". . ."])
    elif character == LauraX:
        $ line = renpy.random.choice(["Not yet, " + character.Petname + ". . ."])
    elif character == JeanX:
        $ line = renpy.random.choice(["Mmmm, not right now, " + character.Petname + ". . ."])
    elif character == StormX:
        $ line = renpy.random.choice(["Oh, that would. . .perhaps not, " + character.Petname + ". . ."])
    elif character == JubesX:
        $ line = renpy.random.choice(["Not yet, " + character.Petname + ". . ."])

    character.voice "[line]"

    return

label first_time_ass_eaten_lines(character):
    if character == RogueX:
        if character.love >= character.obedience and character.love >= character.inhibition:
            "I'm not really sure I want you lick'in down there. . ."
        elif character.obedience >= character.inhibition:
            "You really don't have to if you don't want to."
        else:
            $ character.Eyes = "sexy"

            "Hmm. . . it's worth a shot. . ."
    elif character == KittyX:
        if character.love >= character.obedience and character.love >= character.inhibition:
            "That's, I don't know. . ."
        elif character.obedience >= character.inhibition:
            "You don't have to do that."
        else:
            $ character.Eyes = "sexy"

            "That's kinda gross. . ."
    elif character == EmmaX:
        if character.love >= character.obedience and character.love >= character.inhibition:
            "Oh, are we there now?"
        elif character.obedience >= character.inhibition:
            "Is that what gets you off?"
        else:
            $ character.Eyes = "sexy"

            "Hm, I didn't know that's what you were into."
    elif character == LauraX:
        if character.love >= character.obedience and character.love >= character.inhibition:
            "Oh, we're there now?"
        elif character.obedience >= character.inhibition:
            "Is that what gets you off?"
        else:
            $ character.Eyes = "sexy"

            "Hm, I didn't know that's what you were into."
    elif character == JeanX:
        if character.love >= character.obedience and character.love >= (character.inhibition - character.IX):
            "Oh, we're there now?"
        elif character.obedience >= (character.inhibition - character.IX):
            "Is that what gets you off?"
        else:
            $ character.Eyes = "sexy"

            "Mmmm, you're into that?"
    elif character == StormX:
        if character.love >= character.obedience and character.love >= character.inhibition:
            "Oh, that is a bit forward!"
        elif character.obedience >= character.inhibition:
            "That is what you want?"
        else:
            $ character.Eyes = "sexy"

            "Hmmm, an interesting proposal. . ."
    elif character == JubesX:
        if character.love >= character.obedience and character.love >= character.inhibition:
            "What? What're you talking about?"
        elif character.obedience >= character.inhibition:
            "Is that what gets you off?"
        else:
            $ character.Eyes = "sexy"

            "Hm, I hadn't thought. . ."

    character.voice "[line]"

    return

label ass_sore_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["I'm still a little sore from earlier, " + character.Petname + "."])
    elif character == KittyX:
        $ line = renpy.random.choice(["I'm still a little sore from earlier, " + character.Petname + "."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["I'm still a little sore from earlier, " + character.Petname + "."])
    elif character == LauraX:
        $ line = renpy.random.choice(["I'm still a little sore from earlier, " + character.Petname + "."])
    elif character == JeanX:
        $ line = renpy.random.choice(["I'm still a little sore from earlier, " + character.Petname + "."])
    elif character == StormX:
        $ line = renpy.random.choice(["I'm still a little sore from earlier, " + character.Petname + "."])
    elif character == JubesX:
        $ line = renpy.random.choice(["I'm still a little sore from earlier, " + character.Petname + "."])

    character.voice "[line]"

    return

label not_into_ass_play(character):
    if character == RogueX:
        $ line = renpy.random.choice(["I. . . don't think that's. . ."])
    elif character == KittyX:
        $ line = renpy.random.choice(["I. . . don't think that's. . ."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["That's really not my usual style. . ."])
    elif character == LauraX:
        $ line = renpy.random.choice(["That's really not my style. . ."])
    elif character == JeanX:
        $ line = renpy.random.choice(["That's really not my style. . ."])
    elif character == StormX:
        $ line = renpy.random.choice(["That's really not my usual style. . ."])
    elif character == JubesX:
        $ line = renpy.random.choice(["That's really not my style. . ."])

    character.voice "[line]"

    return

label think_would_enjoy_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["Ok, you're probably right. . ."])
    elif character == KittyX:
        $ line = renpy.random.choice(["Ok, you're probably right. . ."
            "Oh. . . you're probably right. . ."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["You're probably right. . ."
            "You present a compelling case. . ."
            "Ok, you're probably right. . ."])
    elif character == LauraX:
        $ line = renpy.random.choice(["Ok, you're probably right. . ."
            "You make a good point. . ."
            "You're probably right. . ."])
    elif character == JeanX:
        $ line = renpy.random.choice(["Ok, you're probably right. . ."
            "You make a good point. . ."
            "You're probably right. . ."])
    elif character == StormX:
        $ line = renpy.random.choice(["Well. . . I might at that. . ."
            "I. . . would. . ."
            "You may be correct. . ."])
    elif character == JubesX:
        $ line = renpy.random.choice(["Um. . . maybe. . ."
            "You make a good point. . ."])

    character.voice "[line]"

    return

label unconvinced_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["Tsk, not this time, " + character.Petname + " that just seems. . . dirty."
            "I really don't think that I would."])
    elif character == KittyX:
        $ line = renpy.random.choice(["I really don't think so."
            "I really don't think that I would."
            "Um, not this time, " + character.Petname + " that's too. . ."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["I really don't think so."
            "I don't think that I would."
            "I would, but still no, " + character.Petname + "."])
    elif character == LauraX:
        $ line = renpy.random.choice(["I really don't think so."
            "I don't think that I would."
            "I would, but still no, " + character.Petname + "."])
    elif character == JeanX:
        $ line = renpy.random.choice(["I really don't think so."
            "I don't think that I would."
            "I would, but still no, " + character.Petname + "."])
    elif character == StormX:
        $ line = renpy.random.choice(["I really do not think so."
            "I do not think that I would."
            "I would, but still no, " + character.Petname + "."])
    elif character == JubesX:
        $ line = renpy.random.choice(["I would, but still no, " + character.Petname + "."
            "Doubt."
            "I really doubt that. . ."])

    character.voice "[line]"

    return

label didnt_get_off_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["I didn't exactly get off there. . ."
            "That didn't really do it for me. . ."
            "Hmm, you seemed to get more out of that than me. . ."])
    elif character == KittyX:
        $ line = renpy.random.choice(["Could you have maybe paid more attention? . ."
            "I didn't get much out of that. . ."
            "Hmm, you seemed to get more out of that than me. . ."])
    elif character == EmmaX:
        $ line = renpy.random.choice(["Could you have perhaps been more attentive? . ."
            "I'm afraid that didn't do much for me. . ."
            "Hmm, you seemed to get more out of that than I did. . ."])
    elif character == LauraX:
        $ line = renpy.random.choice(["Forgetting someone? . ."
            "That didn't do much for me. . ."])
    elif character == JeanX:
        $ line = renpy.random.choice(["I think you need to get back down there."])
    elif character == StormX:
        $ line = renpy.random.choice(["I could have used some more attention to my needs. . ."
            "I am afraid that you got more out of that than me. . ."
            "I am afraid that did not do much for me. . ."])
    elif character == JubesX:
        $ line = renpy.random.choice(["Forgetting someone? . ."
            "That didn't do much for me. . ."])

    character.voice "[line]"

    return

label getting_close_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["Are you getting close here? I'm getting a little sore."
            "Are you getting close here? My jaw's getting pretty sore."
            "What are you even doing down there?"
            "Are you getting close here? I'm getting a little sore."
            "Are you getting close here?"])

    character.voice "[line]"

    return

label getting_rugburn_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["I'm getting rug-burn here " + character.Petname + ". Can we do something else?"
            "I'm getting a little tired, " + character.Petname + ". Can we do something else?"
            character.Petname + ", this is getting uncomfortable, maybe we could try something else."
            "Ow, i'm not used to this. Mind if we take a break?"
            "Can we be done with this now? I'm getting sore."])

    character.voice "[line]"

    return

label done_with_this_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["I'm . . .getting . . .worn out. . . here, . . " + character.Petname + "."
            "I'm kinda done with this, " + character.Petname + "."])

    character.voice "[line]"

    return

label can_we_do_something_else_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["Can we. . . do something. . . else?"])

    character.voice "[line]"

    return

label no_ass_to_mouth_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["No thanks, " + character.Petname + ". Maybe a Handy instead?"])

    character.voice "[line]"

    return

label since_you_are_so_nice_lines(character):
    if character == RogueX:
        $ line = renpoy.random.choice(["Well, since you're be'in so nice about it, I guess we can give it a go. . ."
            "I guess if you really want to try it. . ."
            "I guess it doesn't feel so bad. . ."])

    character.voice "[line]"

    return

label daily_action_lines(character):
    if character == RogueX:
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

    character.voice "[line]"

    return

label used_to_action_lines(character):
    if character == RogueX:
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

    character.voice "[line]"

    return

label lets_do_this_lines(character):
    if character == RogueX:
        $ line = renpy.random.choice(["Ok, [character.Petname], let's do this."])

    character.voice "[line]"

    return

label were_done_here_lines(character):
    $ line = renpy.random.choice(["[character.name] shoves you away and slaps you in the face."
        "[character.name] shoves you away."])

    "[line]"

    if character == RogueX:
        $ line = renpy.random.choice(["Jackass!{p}If that's how you want to treat me, we're done here!"
            "Dick!{p}}If that's how you want want to act, I'm out of here!"])

    character.voice "[line]"

    return

label knows_her_place_lines(character):
    $ line = renpy.random.choice(["[character.name] doesn't seem to be into this, but she knows her place."
        "[character.name] doesn't seem to be into this, you're lucky she's so obedient."])

    "[line]"

    return

label not_ready_to_stop_lines(character):
    $ line = renpy.random.choice(["She continues to shake a little with pleasure.",
        "She is breathing heavily as your cock rubs inside her.",
        "She slowly turns back towards you and smiles.",
        "She doesn't seem ready to stop."])

    "[line]"

    return

label template(character):
    if character == RogueX:
        $ line = renpy.random.choice([""])
    elif character == KittyX:
        $ line = renpy.random.choice([""])
    elif character == EmmaX:
        $ line = renpy.random.choice([""])
    elif character == LauraX:
        $ line = renpy.random.choice([""])
    elif character == JeanX:
        $ line = renpy.random.choice([""])
    elif character == StormX:
        $ line = renpy.random.choice([""])
    elif character == JubesX:
        $ line = renpy.random.choice([""])

    character.voice "[line]"

    return
