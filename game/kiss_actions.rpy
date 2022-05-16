label kiss(Girl):
    $ primary_action = "kiss"

    $ Round -= 5 if Round > 5 else (Round-1)

    call shift_focus(Girl)

    $ Approval = Approvalcheck(Girl, 700, TabM=1,Alt=[[RogueX,JeanX],500]) #reduced check for Rogue

    if Girl == EmmaX and not Approvalcheck(Girl, 1000):
        $ Girl.change_face("sadside")

        ch_e "Not when we barely know each other. . ."

        $ Girl.recent_history.append("no_kissing")
        $ Girl.daily_history.append("no_kissing")
        return
    if Approval > 1 and not Girl.action_counter["kiss"] and not Girl.Forced:
        $ Girl.change_face("sexy")
        $ Girl.Eyes = "side"

        if Girl == RogueX:
            ch_r "I've never really been able to do this, so I'm a bit excited to try. . ."
        elif Girl == KittyX:
            ch_k "You are kinda cute. . ."
        elif Girl == EmmaX:
            ch_e "Well, I suppose it couldn't hurt. . ."
        elif Girl == LauraX:
            ch_l "Worth a shot. . ."
        elif Girl == JeanX:
            ch_j "Why not?"
        elif Girl == StormX:
            ch_s "I would like that."
        elif Girl == JubesX:
            ch_v "I guess we did get off to a poor start. . ."
    elif Approval and not Girl.action_counter["kiss"]:
        $ Girl.change_face("sexy")
        $ Girl.Eyes = "side"

        if Girl == RogueX:
            ch_r "I guess it's worth a shot. . ."
        elif Girl == KittyX:
            ch_k "I'll give it a go. . ."
        elif Girl == EmmaX:
            ch_e "We could. . ."
        elif Girl == LauraX:
            ch_l "If you insist. . ."
        elif Girl == JeanX:
            ch_j "I mean, whatever. . ."
        elif Girl == StormX:
            ch_s "I suppose."
        elif Girl == JubesX:
            ch_v "I suppose we could. . ."
    elif Approval and "kissing" in Girl.recent_history:
        $ Girl.change_face("sexy", 1)

        if Girl == KittyX:
            ch_k "Prrr. . ."
        else:
            Girl.voice "Mmmm. . ."

        jump before_action
    elif Approval and "kissing" in Girl.daily_history:
        $ Girl.change_face("sexy", 1)

        $ line = renpy.random.choice(["A","B","C"])
        if line == "A":
            Girl.voice "Didn't get enough earlier?"
        elif Girl == RogueX:
            if line == "B":
                ch_r "{i}I'm{/i} used to being the one sucking people dry. . ."
            else:
                ch_r "Gimme some sugar, sugar."
        elif Girl == KittyX:
            if line == "B":
                ch_k "Meow."
            else:
                ch_k "Come'ere tasty."
        elif Girl == EmmaX:
            if line == "B":
                ch_e "Mmmm. . ."
            else:
                ch_e "Come and get it."
        elif Girl == LauraX:
            if line == "B":
                ch_l "Mmmmmm."
            else:
                ch_l "Get over here."
        elif Girl == JeanX:
            if line == "B":
                ch_j "MmMmmm. . ."
            else:
                ch_j "Oh, get over here."
        elif Girl == StormX:
            if line == "B":
                ch_s "Mmmm. . ."
            else:
                ch_s "Yes, let's."
        elif Girl == JubesX:
            if line == "B":
                ch_v "Mmmm. . ."
            else:
                ch_v "Sure, come to me."

        $ line = 0
    elif Approval > 1 and Girl.love > Girl.obedience:
        $ Girl.change_face("sexy")

        if Girl == RogueX:
            ch_r "Sure, why not?"
        elif Girl == KittyX:
            ch_k "Smooches!"
        elif Girl == EmmaX:
            ch_e "Mwa."
        elif Girl == LauraX:
            ch_l "Mmmmm. . ."
        elif Girl == JeanX:
            ch_j "MmMmmmm. . ."
        elif Girl == StormX:
            ch_s "Hrm. . ."
        elif Girl == JubesX:
            ch_v "Mmmm. . ."
    elif Approvalcheck(Girl, 500, "O") and Girl.obedience > Girl.love:
        $ Girl.change_face("normal")

        if Girl == RogueX:
            ch_r "If you wish."
        elif Girl == KittyX:
            ch_k "Sure, ok."
        elif Girl == EmmaX:
            ch_e "Of course."
        elif Girl == LauraX:
            ch_l "If you want."
        elif Girl == JeanX:
            ch_j "Ok. . ."
        elif Girl == StormX:
            ch_s "Very well. . ."
        elif Girl == JubesX:
            ch_v "Sure. . ."

        $ Girl.change_stat("obedience", 60, 1)
    elif Approvalcheck(Girl, 250, "O",Alt=[[KittyX,LauraX],300]) and Approvalcheck(Girl, 250, "L",Alt=[[KittyX,LauraX],200]):
        $ Girl.change_face("bemused")

        Girl.voice "Ok, fine."

        $ Girl.change_stat("obedience", 50, 3)
    elif Girl.Addict >= 50:
        $ Girl.change_face("sexy")
        $ Girl.Eyes = "manic"

        if Girl == RogueX:
            ch_r "Hm. . . ok, let's do this."
        elif Girl == KittyX:
            ch_k "I kinda have to."
        elif Girl == EmmaX:
            ch_e ". . . yes."
        elif Girl == LauraX:
            ch_l "I have to."
        elif Girl == JeanX:
            ch_j "Um. . . yeah. . ."
        elif Girl == StormX:
            ch_s ". . . yes. . ."
        elif Girl == JubesX:
            ch_v "Oh yes. . ."
    elif Approval:
        $ Girl.change_face("bemused")

        if Girl == RogueX:
            ch_r "hmm, ok."
        elif Girl == KittyX:
            ch_k "Yeah, whatever."
        elif Girl == EmmaX:
            ch_e "Very well."
        elif Girl == LauraX:
            ch_l "Sure."
        elif Girl == JeanX:
            ch_j "Whatever. . ."
        elif Girl == StormX:
            ch_s "Fine."
        elif Girl == JubesX:
            ch_v "Sure, ok. . ."
    else:
        $ Girl.change_face("normal") # Else
        $ Girl.Mouth = "sad"

        if Girl == RogueX:
            ch_r "Nah, I don't think I'm interested."
        elif Girl == KittyX:
            ch_k "Nope."
        elif Girl == EmmaX:
            ch_e "Hmmm, no."
        elif Girl == LauraX:
            ch_l "No."
        elif Girl == JeanX:
            ch_j "You wish. . ."
        elif Girl == StormX:
            ch_s "I do not think so."
        elif Girl == JubesX:
            ch_v "No thanks. . ."

        $ Girl.recent_history.append("no_kissing")
        $ Girl.daily_history.append("no_kissing")

        return

    jump before_action
