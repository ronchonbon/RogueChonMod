label out_of_action_lines(Girl):
    if Girl == RogueX:
        $ line = renpy.random.choice(["Sorry, " + Girl.player_petname + " but I'm a bit worn out.",
            "I'm a bit worn out right now, " + Girl.player_petname + " maybe later.",
            "Sorry " + [Girl.player_petname] + " , I'm a bit worn out."])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["I'm sorry, " + Girl.player_petname + ", but I need a break."])

    Girl.voice "[line]"

    return

label end_of_sex_menu_not_multiaction_lines(Girl):
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

label sex_menu_caught_or_angry_lines(Girl):
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

label sex_menu_less_than_five_rounds(Girl):
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

label generic_exit_sex_menu_lines(Girl):
    if Girl == RogueX:
        ch_r "Huh? Ok."
    elif Girl == KittyX:
        ch_k "Ok, fine."
    elif Girl == EmmaX:
        ch_e "Fine."
    elif Girl == LauraX:
        ch_l "Ok, fine."
    elif Girl == JeanX:
        ch_j "Ok, fine."
    elif Girl == StormX:
        ch_s "That is fine."
    elif Girl == JubesX:
        ch_v "Sure, fine."

    return

label exit_sex_menu_experienced_first_round_lines(Girl):
    if Girl == RogueX:
        ch_r "Are you sure, [Girl.Petname]? I could really use some company."
    elif Girl == KittyX:
        ch_k "Are you sure, [Girl.Petname]? I wasn't exactly. . . finished."
    elif Girl == EmmaX:
        ch_e "Are you certain, [Girl.Petname]? Are you perhaps forgetting something?"
    elif Girl == LauraX:
        ch_l "Are you sure, [Girl.Petname]?"
        ch_l "I could go another round. . . or two. . ."
    elif Girl == JeanX:
        ch_j "Are you sure, [Girl.Petname]?"
        ch_j "I could go another round. . . or two. . ."
    elif Girl == StormX:
        ch_s "Are you certain, [Girl.Petname]? Are you perhaps forgetting something?"
    elif Girl == JubesX:
        ch_v "Are you sure, [Girl.Petname]?"
        ch_v "I could keep going. . ."

    return

label exit_sex_menu_experienced_addicted_lines(Girl):
    if Girl == RogueX:
        ch_r "I still need a little. . . contact."
    elif Girl == KittyX:
        ch_k "I need more touching."
    elif Girl == EmmaX:
        ch_e "I need more contact."
    elif Girl == LauraX:
        ch_l "I need more contact."
    elif Girl == JeanX:
        ch_j "I need some more skin contact."
        ch_j "You gonna leave me hanging?"
    elif Girl == StormX:
        ch_s "I need your touch."
    elif Girl == JubesX:
        ch_v "I'm a little drained, I need more contact."

    return

label exit_sex_menu_experienced_lines(Girl):
    if Girl == RogueX:
        ch_r "Don't leave me hang'in, [Girl.Petname]."
    elif Girl == KittyX:
        ch_k "I still need some more attention."
    elif Girl == EmmaX:
        ch_e "I'm afraid that still wasn't enough."
    elif Girl == LauraX:
        ch_l "Aren't you forgetting something?"
    elif Girl == JeanX:
        ch_j "Hey, you'd better get me off here."
        ch_j "You gonna leave me hanging?"
    elif Girl == StormX:
        ch_s "That was not enough to satisfy me."
    elif Girl == JubesX:
        ch_v "Hey! Don't leave me hanging here."

    return

label exit_sex_menu_done_for_now_unsatisfied_lines(Girl):
    if Girl == RogueX:
        ch_r "Way to leave a girl in the lurch. . ."
    elif Girl == KittyX:
        ch_k "Rude!"
    elif Girl == EmmaX:
        ch_e "Well! This might count against you next time."
    elif Girl == LauraX:
        ch_l "You'll regret that one."
    elif Girl == JeanX:
        ch_j "The die has been cast."
    elif Girl == StormX:
        ch_s "Perhaps I need to teach you to be more generous."
    elif Girl == JubesX:
        ch_v "Well, that sucks."

    return

label exit_sex_menu_done_for_now_satisfied_lines(Girl):
    if Girl == RogueX:
        ch_r "Well, you did at least do your part. . ."
    elif Girl == KittyX:
        ch_k "I guess I'll take what I can get. . ."
    elif Girl == EmmaX:
        ch_e "I suppose I'll have to blame myself as an educator."
    elif Girl == LauraX:
        ch_l "Selfish. . ."
    elif Girl == JeanX:
        ch_j "Booo. . ."
    elif Girl == StormX:
        ch_s "Perhaps I need to teach you to be more generous."
    elif Girl == JubesX:
        ch_v "So selfish. . ."

    return

label exit_sex_menu_gave_it_a_shot_unsatisfied_lines(Girl):
    if Girl == RogueX:
        ch_r "Way to leave a girl in the lurch. . ."
    elif Girl == KittyX:
        ch_k "Rude!"
    elif Girl == EmmaX:
        ch_e "Yes, disappointingly so. . ."
    elif Girl == LauraX:
        ch_l "Not a very good one."
    elif Girl == JeanX:
        ch_j "If that's what you want to call it. . ."
    elif Girl == StormX:
        ch_s "So that was the best you could achieve. . ."
    elif Girl == JubesX:
        ch_v "Well try again."

    return

label exit_sex_menu_gave_it_a_shot_satisfied_lines(Girl):
    if Girl == RogueX:
        ch_r "Well, fair enough. . ."
    elif Girl == KittyX:
        ch_k "I guess I'll take what I can get. . ."
    elif Girl == EmmaX:
        ch_e "I suppose you did. . . shame you couldn't do better. . ."
    elif Girl == LauraX:
        ch_l "Selfish. . ."
    elif Girl == JeanX:
        ch_j "Booo. . ."
    elif Girl == StormX:
        ch_s "So that was the best you could achieve. . ."
    elif Girl == JubesX:
        ch_v "So selfish. . ."

    return

label exit_sex_menu_did_my_part_lines(Girl):
    if Girl == RogueX:
        ch_r "I guess you did at that. . ."
    elif Girl == KittyX:
        ch_k "Well. . . yeah, but. . ."
    elif Girl == EmmaX:
        ch_e "Take it as a compliment that I expected more."
    elif Girl == LauraX:
        ch_l "Well. . . yeah, but. . ."
    elif Girl == JeanX:
        ch_j "Stingy. . ."
    elif Girl == StormX:
        ch_s "I had hoped for better.  . ."
    elif Girl == JubesX:
        ch_v "Yeah, but. . . keep doing that. . ."

    return

label exit_sex_menu_out_of_semen_lines(Girl):
    if Girl == RogueX:
        ch_r "Huh, can't be helped, I s'pose."
    elif Girl == KittyX:
        ch_k "Yeah, but [Girl.like]. . ."
    elif Girl == EmmaX:
        ch_e "I suppose that can't be helped. . ."
    elif Girl == LauraX:
        ch_l "Well, you could always try something else. . ."
    elif Girl == JeanX:
        ch_j "Your hands don't seem to be broken."
    elif Girl == StormX:
        ch_s "Well, I cannot push you to breaking. . ."
    elif Girl == JubesX:
        ch_l "Well, you could always try something else. . ."

    return

label exit_sex_menu_less_than_two_rounds_lines(Girl):
    if Girl == RogueX:
        ch_r "Mmmm. . ."
    elif Girl == KittyX:
        ch_k "Hehe. . ."
    elif Girl == EmmaX:
        ch_e "Excellent. . ."
    elif Girl == LauraX:
        ch_l "Good. . ."
    elif Girl == JeanX:
        ch_j "Good. . ."
    elif Girl == StormX:
        ch_s "Thank you."
    elif Girl == JubesX:
        ch_v "Cool. . ."

    return

label exit_sex_menu_more_than_two_rounds_lines(Girl):
    if Girl == RogueX:
        ch_r "Yeah, again. . ."
    elif Girl == KittyX:
        ch_k "You know it. . ."
    elif Girl == EmmaX:
        ch_e "Always. . ."
    elif Girl == LauraX:
        ch_l "Always. . ."
    elif Girl == JeanX:
        ch_j "Always. . ."
    elif Girl == StormX:
        ch_s "Always. . ."
    elif Girl == JubesX:
        ch_v "Yup. . ."

    return

label exit_sex_menu_girl_also_tired_lines(Girl):
    if Girl == RogueX:
        ch_r "I guess I'm a bit tuckered out too, [Girl.Petname]. I guess we can take a breather."
    elif Girl == KittyX:
        ch_k "I guess I'm kinda tired too, [Girl.Petname]. We can take a break. . ."
        ch_k ". . .for now."
    elif Girl == EmmaX:
        ch_e "I suppose I'm tired as well, [Girl.Petname]. We can take a breather. . ."
    elif Girl == LauraX:
        ch_l "Yeah, you look like you've had enough. We can take a break. . ."
        ch_l ". . .for now."
    elif Girl == JeanX:
        ch_j "Ok, sounds good. . ."
    elif Girl == StormX:
        ch_s "I could use some rest as well, [Girl.Petname]."
    elif Girl == JubesX:
        ch_v "Sure, I guess we can take a little break. . ."

    return

label sex_menu_cleanup_lines(Girl):
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

label end_of_action_lines(Girl):
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

label ten_rounds_left_lines(Girl):
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

label five_rounds_left_lines(Girl):
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

    return
