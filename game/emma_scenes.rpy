label EmmaMeet:
    $ bg_current = "bg classroom"
    $ EmmaX.OutfitDay = "casual1"
    $ EmmaX.Outfit = "casual1"
    $ EmmaX.OutfitChange("casual1")
    call CleartheRoom(EmmaX,0,1)
    $ EmmaX.Loc = "bg emma"
    $ EmmaX.Love = 300
    $ EmmaX.Obed = 0
    $ EmmaX.Inbt = 200
    call Shift_Focus(EmmaX)
    call Set_The_Scene
    $ EmmaX.sprite_location = StageRight
    call LastNamer
    $ EmmaX.Petnames.append(_return)
    $ EmmaX.Petname = _return

    "You enter the classroom and have a seat."
    "The bell to class rings, but Professor McCoy seems to be late."
    "A strange woman enters the room and heads to the podium with a regal stride."
    $ EmmaX.FaceChange("normal")
    show Emma_Sprite at sprite_location(EmmaX.sprite_location) with easeinright
    $ EmmaX.Loc = "bg classroom"
    $ EmmaX.ArmPose = 1
    ch_u "Hello students. My name is Emma Frost, and I have been invited to conduct this class."
    ch_e "I hope that over my tenure here you will demonstrate talents and hard work worthy of my respect."
    "She scans her eyes over the room, passing over each student."
    $ EmmaX.FaceChange("surprised")
    pause 1
    $ EmmaX.FaceChange("sly",Mouth="sad")
    $ EmmaX.Statup("Love", 90, -10)
    $ EmmaX.Lust += 5
    "As her eyes pass over you, they briefly widen and then narrow."
    $ EmmaX.FaceChange("sly")
    ch_e "Very well, let us begin, class."
    $ EmmaX.FaceChange("normal")
    "The class is pretty basic today, mostly a lecture on her areas of expertise, psychology and literature."
    $ EmmaX.Lust += 5
    "She asks a lot of questions of the students, and singles you out more than once. You notice her glancing in your direction as other students answer."
    $ EmmaX.Lust += 5
    call Wait
    call CleartheRoom(EmmaX,0,1)
    $ EmmaX.Loc = "bg classroom"
    call Set_The_Scene
    ch_e "All right students, class dismissed."
    ch_e "[EmmaX.Petname], could you wait a moment, I have something to discuss with you."
    menu:
        extend ""
        "Yes?":
                $ EmmaX.Statup("Love", 70, 10)
                $ EmmaX.FaceChange("normal")
        "I've got places to be.":
                $ EmmaX.Statup("Love", 70, -15)
                $ EmmaX.Statup("Obed", 80, 10)
                $ EmmaX.FaceChange("angry")
                ch_e "[Player.Name], do not take that attitude with me."
                "She places herself in the doorway, preventing you from leaving."
        "For such a sexy teacher? I've got some time.":
                $ EmmaX.Statup("Love", 70, -5)
                $ EmmaX.Statup("Obed", 80, 5)
                $ EmmaX.FaceChange("angry",1, Mouth="smirk")
                ch_e "That's rather. . . inappropriate."
                $ EmmaX.FaceChange("bemused", Mouth="smile")
                $ EmmaX.Statup("Love", 70, 20)
                $ EmmaX.Statup("Lust", 50, 5)
                $ EmmaX.Statup("Inbt", 25, 15)
                ch_e "But also obvious, so I can't criticize you too harshly."

    ch_e "I've heard about you from Professor Xavier and. . . others."

    if Player.Rep <= 200:
        $ EmmaX.Statup("Obed", 80, 10)
        $ EmmaX.Statup("Inbt", 90, 15)
        $ EmmaX.Statup("Lust", 50, 5)
        $ EmmaX.FaceChange("angry", Brows="confused")
        ch_e "You seem to be a bit of a scoundrel. . ."
    elif Player.Rep < 600:
        $ EmmaX.Statup("Obed", 80, 5)
        $ EmmaX.Statup("Inbt", 90, 5)
        $ EmmaX.Statup("Lust", 50, 5)
        $ EmmaX.FaceChange("sly")
        ch_e "You have quite a reputation around campus. . ."
    else:
        $ EmmaX.FaceChange("smile")
        ch_e "You have managed a reasonble reputation. . ."

    if TotalSEXP >= 110 or (len(Player.Harem) >= 2 and "Historia" not in Player.Traits):
        $ EmmaX.Statup("Love", 70, 5)
        $ EmmaX.Statup("Obed", 80, 10)
        $ EmmaX.Statup("Inbt", 200, 10)
        $ EmmaX.Statup("Lust", 50, 5)
        $ EmmaX.FaceChange("sly")
        ch_e "and a number of conquests to your name. . ."
    elif TotalSEXP >= 60:
        $ EmmaX.Statup("Love", 70, 5)
        $ EmmaX.Statup("Obed", 80, 5)
        $ EmmaX.Statup("Inbt", 200, 5)
        $ EmmaX.Statup("Lust", 50, 2)
        $ EmmaX.FaceChange("smile")
        ch_e "and are not without some romantic entanglements. . ."
    else:
        $ EmmaX.FaceChange("smile", Brows="confused")
        ch_e "though I haven't heard of much of a romantic life. . ."

    if Player.Lvl >= 7:
        $ EmmaX.Statup("Love", 70, 5)
        $ EmmaX.Statup("Obed", 80, 5)
        $ EmmaX.FaceChange("smile")
        ch_e "but your grades have been excellent."
    elif Player.Lvl >= 3:
        $ EmmaX.FaceChange("normal", Brows="confused")
        ch_e "but your grades been marginal at best."
    else:
        $ EmmaX.Statup("Love", 70, -5)
        $ EmmaX.Statup("Lust", 10, -5, 1)
        $ EmmaX.FaceChange("normal", Brows="sad")
        ch_e "but you haven't been living up to your potential in class."

    $ EmmaX.FaceChange("normal", Eyes="side")
    ch_e "My particular interest in this case, however. . ."
    $ EmmaX.FaceChange("sly")
    ch_e "is that I cannot get a \"read\" on you."
    $ EmmaX.FaceChange("sly", Mouth="normal")
    ch_e "My mutant power is telepathy, the same as Professor Xavier's."
    ch_e "I've grown accustomed to knowing what those around me are thinking."
    $ EmmaX.FaceChange("bemused", Eyes="side")
    ch_e "With you. . . I cannot do that, which presents an interesting. . ."
    $ EmmaX.FaceChange("sly")
    ch_e "challenge. . ."
    menu:
        extend ""
        "I imagine it would.":
                $ EmmaX.Statup("Love", 70, 5)
                $ EmmaX.Statup("Inbt", 200, 5)
                $ EmmaX.FaceChange("normal")
                ch_e "Hmm, yes."
        "Huh.":
                $ EmmaX.Statup("Love", 70, -1)
                $ EmmaX.Statup("Obed", 80, -1)
                $ EmmaX.FaceChange("confused", Mouth="normal")
                ch_e ". . . yes."
                $ EmmaX.FaceChange("normal")
        "So you can't see what I'm picturing right now?":
                $ EmmaX.Statup("Obed", 80, 5)
                $ EmmaX.FaceChange("bemused")
                pause 0.5
                $ EmmaX.FaceChange("bemused", Eyes="down")
                "She glances downward."
                $ EmmaX.FaceChange("sly")
                $ EmmaX.Statup("Love", 70, 10)
                $ EmmaX.Statup("Inbt", 200, 10)
                $ EmmaX.Statup("Lust", 50, 15)
                ch_e "I can't read your mind, but I'm not blind, [EmmaX.Petname]."
    ch_e "In any case, I think we should set aside some time to talk."
    ch_e "I'd like to make you a personal project, so I can see how you tick."
    menu:
        extend ""
        "I'd be ok with that.":
                $ EmmaX.Statup("Love", 70, 5)
                $ EmmaX.Statup("Inbt", 200, 5)
                $ EmmaX.FaceChange("smile")
                ch_e "Excellent, I look forward to it."
        "I don't know if you should experiment on your students.":
                $ EmmaX.Statup("Love", 70, -5)
                $ EmmaX.FaceChange("normal", Mouth="sad")
                ch_e "There's nothing for you to worry about."
                $ EmmaX.FaceChange("sly")
                ch_e "I'll be. . . gentle."
        "If it means spending more time with you. . .":
                if ApprovalCheck(EmmaX, 295, "L"):
                    $ EmmaX.Statup("Inbt", 200, 5)
                    $ EmmaX.Statup("Lust", 50, 5)
                    $ EmmaX.FaceChange("sly")
                    ch_e "Oh, I believe we'll be spending a good deal of time together. . ."
                else:
                    $ EmmaX.FaceChange("angry")
                    ch_e "Much as it may pain me, it would. . ."
                    $ EmmaX.FaceChange("normal")
        "What do I get out of it?":
                if not ApprovalCheck(EmmaX, 290, "L"):
                    $ EmmaX.Statup("Love", 70, -5)
                    $ EmmaX.Statup("Obed", 80, 5)
                    $ EmmaX.Statup("Inbt", 200, 5)
                    $ EmmaX.FaceChange("angry")
                    ch_e "You'll stand some chance of passing this class, [EmmaX.Petname]."
                    $ EmmaX.FaceChange("normal")
                else:
                    if EmmaX.Obed > 0:
                        $ EmmaX.FaceChange("confused", Mouth="smirk")
                        ch_e "What would you {i}like{/i} to \"get out of it?\""
                        menu:
                            extend ""
                            "I guess if it helps your \"research.\" . .":
                                    $ EmmaX.Statup("Love", 70, 10)
                                    $ EmmaX.Statup("Obed", 80, -5)
                                    $ EmmaX.FaceChange("smile")
                                    ch_e "I'm glad to see that you can be reasonable."
                            "Spending more time with you would be plenty. . .":
                                    $ EmmaX.Statup("Love", 70, 5)
                                    $ EmmaX.Statup("Obed", 80, 5)
                                    $ EmmaX.Statup("Lust", 20, 5)
                                    $ EmmaX.FaceChange("sly")
                                    ch_e "It certainly should be."
                            "A kiss?":
                                    $ EmmaX.Statup("Love", 70, -5)
                                    $ EmmaX.Statup("Obed", 80, 10)
                                    $ EmmaX.FaceChange("surprised",1, Mouth="surprised")
                                    ch_e "[EmmaX.Petname], that is incredibly inappropriate!"
                                    $ EmmaX.FaceChange("sadside",0,Brows="angry")
                                    ch_e "I would {i}never{/i} consider such a thing with a student."
                                    if ApprovalCheck(EmmaX, 220, "I"):
                                        $ EmmaX.FaceChange("sly",1)
                                        $ EmmaX.Statup("Love", 70, 5)
                                        $ EmmaX.Statup("Obed", 80, 5)
                                        $ EmmaX.Statup("Inbt", 200, 5)
                                        $ EmmaX.Statup("Lust", 50, 5)
                                        ch_e ". . .never. . ."
                            "I think you know what I'd want. . .":
                                    $ EmmaX.Statup("Obed", 80, 5)
                                    $ EmmaX.Statup("Lust", 50, 5)
                                    $ EmmaX.FaceChange("sly",Brows="angry")
                                    ch_e "Yes, I imagine that I do. . ."
                                    if ApprovalCheck(EmmaX, 220, "I"):
                                        $ EmmaX.FaceChange("sly",1)
                                        $ EmmaX.Statup("Love", 70, 5)
                                        $ EmmaX.Statup("Obed", 80, 5)
                                        $ EmmaX.Statup("Inbt", 200, 10)
                                        $ EmmaX.Statup("Lust", 50, 5)
                                        ch_e "And we may be able to come to some sort of \"mutually beneficial\" arrangement."
                                    else:
                                        $ EmmaX.FaceChange("bemused",0)
                                        $ EmmaX.Statup("Love", 70, -5)
                                        ch_e "But figuring out whether I'm correct is the entire point here."
                    else: #if 0 Obedience
                        $ EmmaX.FaceChange("normal")
                        ch_e "The satisfaction of helping my. . . studies."
                        if ApprovalCheck(EmmaX, 300, "L"):
                            $ EmmaX.FaceChange("sly")
                            $ EmmaX.Statup("Obed", 80, 5)
                            $ EmmaX.Statup("Inbt", 200, 5)
                            $ EmmaX.Statup("Lust", 50, 5)
                            ch_e "-and maybe if you're good. . ."
                        else:
                            ch_e "-and nothing more."

    $ EmmaX.FaceChange("normal",0)
    ch_e "That said, class is finished for the day and I have some paperwork to attend to, so I'll see you. . ."
    ch_e ". . . later. . ."
    hide Emma_Sprite with easeoutright
    "She strides out of the room and down the hall."
    $ EmmaX.Loc = "bg emma"
    $ EmmaX.History.append("met")
    $ ActiveGirls.append(EmmaX) if EmmaX not in ActiveGirls else ActiveGirls
    $ Round -= 10
    return

label Emma_Teacher_Caught(Girl = 0):
    #add this scene for when Emma is a teacher, and catches one of the girls fucking around in class.
    #add options for getting away with it
    if  "noticed " + Girl.Tag in EmmaX.RecentActions:
            return
    if ApprovalCheck(EmmaX, 500, "I") and ApprovalCheck(EmmaX, 1500) and EmmaX.GirlLikeCheck(Girl) >= 500:
            "[EmmaX.Name] notices the two of you, but just tilts her head in approval and continues on."
            $ EmmaX.GLG(Girl,800,3,1)
            $ Girl.GLG(EmmaX,800,3,1)
            $ EmmaX.RecentActions.append("noticed " + Girl.Tag)
            return

    ch_e "[Player.Name]? [Girl.Name]? Could you stop what you're doing immediately?"
    call Checkout(1)

    $ Girl.FaceChange("bemused", 2, Eyes="side")
    call AllReset(Girl)
    if ApprovalCheck(Girl, 700, "I"):
            $ Girl.FaceChange("bemused", 1)
            "[Girl.Name] shrugs and returns to her seat."
            call Partner_Like(EmmaX,2,-1,500,Girl) #if likes emma 500+, +2, else -1
    else:
            "[Girl.Name] jumps and dashes out of the room."
            call Partner_Like(EmmaX,-2,-3,500,Girl) #if likes emma 500+, -2, else -3
            call Remove_Girl(Girl)

    $ Girl.Rep -= 1
    call Partner_Like(Girl,3,2,800,EmmaX)  #if likes the girl 800+, +3, else +2
    $ EmmaX.GLG(Girl,800,3,1)

    $ Player.Rep -= 1
    ch_e "Thank you."
    ch_e "And [Player.Name], see me after class for detention. . ."

    $ renpy.pop_call()
    $ renpy.pop_call()
    $ Player.Traits.append("detention")
    $ Player.DailyActions.append("detention")
    jump Class_Room

label Emma_Caught_Classroom:
            #This label is called from a Location
            call Shift_Focus(EmmaX)
            "As you walk down the halls, you hear some odd noises coming from the classroom."                           #fix this scene, pants option
            show blackscreen onlayer black
            $ Player.AddWord(1,"interruption") #adds to Recent
            $ bg_current = "bg classroom"
            call CleartheRoom(EmmaX,0,1)
            $ EmmaX.OutfitChange(Changed=1)
            $ EmmaX.Loc = 0
            call Set_The_Scene
            $ EmmaX.Loc = "bg desk"
            $ Taboo = 0
            $ EmmaX.FaceChange("sexy")
            $ EmmaX.Eyes = "closed"
            $ EmmaX.ArmPose = 1
            $ Count = 0
            hide blackscreen onlayer black
            $ Trigger = "masturbation"
            $ Trigger3 = "fondle pussy"
            $ Trigger5 = "fondle breasts"
            $ EmmaX.RecentActions.append("classcaught")
            $ EmmaX.DailyActions.append("unseen")
            $ EmmaX.RecentActions.append("unseen")
            $ Line = 0
            $ EmmaX.DrainWord("no masturbation")
            $ EmmaX.RecentActions.append("masturbation")
            $ EmmaX.DailyActions.append("masturbation")
            "You see [EmmaX.Name] leaning back against her desk, her hands tracing slow paths across her body."

            if "Historia" in Player.Traits:
                    call Emma_M_Interupted
            else:
                    call Emma_M_Cycle
            if "angry" in EmmaX.RecentActions:
                    return

            $ EmmaX.Eyes = "sexy"
            $ EmmaX.Brows = "confused"
            $ EmmaX.Mouth = "normal"
            $ EmmaX.ArmPose = 1
            $ EmmaX.OutfitChange()
            $ bg_current = "bg classroom"
            call Display_Girl(EmmaX)
            if "classcaught" in EmmaX.History:
                    ch_e "I notice you make a habit of dropping in."
                    $ EmmaX.OutfitChange()
            else:
                    # First time caught
                    $ EmmaX.History.append("classcaught")
                    if "Historia" not in Player.Traits:
                        $ temp_modifier = 25
                    ch_e "Well."
                    $ EmmaX.FaceChange("angry", Eyes="side")
                    ch_e "It appears that you've caught me in a somewhat. . . compromising position. . ."
                    menu:
                        extend ""
                        "Yup.":
                                $ EmmaX.FaceChange("perplexed", Mouth="normal")
                                $ EmmaX.Statup("Love", 70, -1)
                                $ EmmaX.Statup("Obed", 50, -2)
                                $ EmmaX.Statup("Lust", 80, -5)
                                ch_e "Er, well. . ."
                        "Are you supposed to be shlicking it in class?":
                                $ EmmaX.FaceChange("angry", Eyes="side")
                                $ EmmaX.Statup("Obed", 50, 5)
                                $ EmmaX.Statup("Inbt", 70, 5)
                                ch_e "Hrm."
                                $ EmmaX.FaceChange("sly", Brows="angry")
                                $ EmmaX.Statup("Lust", 80, 3)
                                ch_e "I imagine I shouldn't, but you know how it can be,"
                                $ EmmaX.Brows = "normal"
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "-surrounded by attractive co-eds all day long. . ."
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "yourself included. . ."
                        "I think it was pretty hot.":
                                $ EmmaX.FaceChange("sly")
                                $ EmmaX.Statup("Love", 70, 5)
                                $ EmmaX.Statup("Obed", 50, 10)
                                $ EmmaX.Statup("Inbt", 70, 10)
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "Hmm, well I suppose I can't blame you for that. . ."
                        "What do you mean?":
                                $ EmmaX.FaceChange("angry")
                                $ EmmaX.Statup("Love", 70, -10)
                                $ EmmaX.Statup("Obed", 50, -5)
                                ch_e "I mean how I was. . ."
                                $ EmmaX.FaceChange("surprised")
                                $ EmmaX.Statup("Love", 70, 15)
                                $ EmmaX.Statup("Obed", 50, 15)
                                $ EmmaX.Statup("Inbt", 70, 5)
                                ch_e "Oh!"
                                $ EmmaX.FaceChange("perplexed")
                                ch_e "Yes, obviously it was nothing, just getting some. . ."
                                $ EmmaX.Eyes = "side"
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "paperwork done. . ."
                                $ EmmaX.FaceChange("sly")
                                $ Line = 1
                    ch_e "So how did you want to handle this. . . situation?"
                    menu:
                        extend ""
                        "I think I can forget all about it.":
                                $ EmmaX.FaceChange("smile")
                                $ EmmaX.Statup("Love", 80, 10)
                                $ EmmaX.Statup("Obed", 60, 10)
                                $ EmmaX.Statup("Inbt", 70, 15)
                                ch_e "Thank you, [EmmaX.Petname]. I appreciate your discretion."
                                $ EmmaX.FaceChange("sly")
                                ch_e "Are you {i}certain{/i} there's nothing I could do to thank you?"
                        "What solution did you have in mind?":
                                $ EmmaX.FaceChange("sly")
                                $ EmmaX.Statup("Love", 70, 5)
                                $ EmmaX.Statup("Obed", 60, 15)
                                $ EmmaX.Statup("Inbt", 70, 15)
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "Oh, I'm sure I could make it worth your while. . ."
                        "What situation?":
                                if Line != 1:
                                        $ EmmaX.FaceChange("confused")
                                        $ EmmaX.Statup("Love", 70, -10)
                                        $ EmmaX.Statup("Obed", 50, -5)
                                        ch_e "I mean how I was. . ."
                                        $ EmmaX.FaceChange("surprised")
                                        $ EmmaX.Statup("Love", 70, 15)
                                        $ EmmaX.Statup("Obed", 50, 15)
                                        $ EmmaX.Statup("Inbt", 70, 5)
                                        ch_e "Oh!"
                                        $ EmmaX.FaceChange("perplexed")
                                        ch_e "Yes, obviously it was nothing, just getting some. . ."
                                        $ EmmaX.Eyes = "side"
                                        $ EmmaX.Statup("Lust", 80, 5)
                                        ch_e "paperwork done. . ."
                                        $ EmmaX.FaceChange("sly")
                                else:
                                        $ EmmaX.FaceChange("angry")
                                        $ EmmaX.Statup("Love", 70, -5)
                                        $ EmmaX.Statup("Inbt", 70, 5)
                                        ch_e "I do wonder if you're just being dense. . ."
                                        $ EmmaX.FaceChange("sly")
                                        ch_e "Still. . ."
                    $ Line = 0
                    $ MultiAction = 0
                    $ temp_modifier = 25
                    menu:
                        extend ""
                        "Could you strip?":
                                $ EmmaX.Statup("Love", 70, 5)
                                $ EmmaX.Statup("Obed", 50, 10)
                                $ EmmaX.Statup("Inbt", 70, 15)
                                ch_e "So you wanted a better view of the action?"
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "I suppose I could accomodate that. . ."
                                ch_e "to a point. . ."
                                "Ms Frost walks to the door and locks it behind her."
                                $ Taboo = 0
                                $ EmmaX.Taboo = 0
                                if "Historia" in Player.Traits:
                                        return 1
                                call Group_Strip(EmmaX)
                        "Could you just keep going?":
                                $ EmmaX.Statup("Love", 70, 10)
                                $ EmmaX.Statup("Obed", 50, 15)
                                $ EmmaX.Statup("Inbt", 70, 15)
                                ch_e "Oh, you wanted to watch some more?"
                                ch_e "I can't exactly blame you."
                                $ EmmaX.Eyes = "down"
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "Were you going to put on a show as well?"
                                menu:
                                    "Yeah!":
                                        $ EmmaX.Statup("Love", 70, 5)
                                        $ EmmaX.Statup("Inbt", 70, 10)
                                        $ EmmaX.Statup("Lust", 80, 5)
                                        ch_e "Excellent."
                                        if "Historia" not in Player.Traits:
                                            call Seen_First_Peen(EmmaX)
                                        "You begin to stroke your cock."
                                        $ Trigger2 = "jackin"
                                    "No, you go ahead.":
                                        $ EmmaX.FaceChange("sad")
                                        $ EmmaX.Statup("Love", 70, -10)
                                        $ EmmaX.Statup("Obed", 50, 5)
                                        $ EmmaX.Statup("Inbt", 70, 5)
                                        ch_e "Pity."
                                $ EmmaX.FaceChange("sly")
                                "[EmmaX.Name] walks to the door and locks it behind her."
                                $ Taboo = 0
                                $ EmmaX.Taboo = 0
                                $Trigger = "masturbation"
                                $Trigger3 = "fondle breasts"
                                "She leans back and runs her fingertips along her breasts."
                                if "Historia" in Player.Traits:
                                        return 1
                                call Emma_M_Cycle
                        "Could I feel you up?":
                                $ EmmaX.Statup("Love", 70, 5)
                                $ EmmaX.Statup("Obed", 50, 10)
                                $ EmmaX.Statup("Inbt", 70, 10)
                                ch_e "Hmm, I could use some help . . .around the office. . . "
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "perhaps you have some suggestions?"
                                "[EmmaX.Name] walks to the door and locks it behind her."
                                $ Taboo = 0
                                $ EmmaX.Taboo = 0
                                if "Historia" in Player.Traits:
                                        return 1
                                call Emma_FB_Prep
                        "Could you give me a hand? [[point to your cock]":
                                $ EmmaX.Statup("Love", 70, -5)
                                $ EmmaX.Statup("Obed", 50, 5)
                                $ EmmaX.Brows = "surprised"
                                ch_e "I appreciate boldness, [EmmaX.Petname], but be a bit more realistic."
                                $ EmmaX.Brows = "normal"
                                $ EmmaX.Statup("Love", 70, 10)
                                $ EmmaX.Statup("Inbt", 70, 5)
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "Perhaps instead I could just offer a little. . . token of my appreciation."
                                "[EmmaX.Name] walks to the door and locks it behind her."
                                $ Taboo = 0
                                $ EmmaX.Taboo = 0
                                if "Historia" in Player.Traits:
                                        return 1
                                call Group_Strip(EmmaX)
                        "I should just get going then.":
                                $ EmmaX.FaceChange("surprised")
                                $ EmmaX.Statup("Obed", 50, 5)
                                ch_e "Oh."
                                $ EmmaX.FaceChange("confused")
                                $ EmmaX.Statup("Love", 70, -5)
                                $ EmmaX.Statup("Inbt", 70, -5)
                                ch_e "Well, I suppose. . ."
                                $ EmmaX.FaceChange("perplexed")
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "I'll see you. . . in class then. . ."
                    $ EmmaX.OutfitChange()
                    "Afterwards, [EmmaX.Name] collects her things and strides toward the door."
                    "She turns back with her hand on the door."
                    $ EmmaX.FaceChange("sly")
                    ch_e "Oh, and [EmmaX.Petname]?"
                    ch_e "You can just call me \"Emma.\""
                    $ EmmaX.Name = "Emma"
                    $ EmmaX.Names.append("Emma")
                    $ EmmaX.Loc = "bg emma"
                    hide Emma_Sprite with easeoutleft
                    $ Round = 20 if Round > 20 else Round
                    $ MultiAction = 1
            return

label Emma_Detention:
            #This label is called from a Location
            call Shift_Focus(EmmaX)
            call CleartheRoom(EmmaX,0,1)
            if "traveling" in Player.RecentActions:
                    "You enter the room and see [EmmaX.Name] waiting for you at the back of the room."
            else:
                    "After class, the students file out, and you wait a few minutes until they're all gone."
                    "Once the last student leaves, [EmmaX.Name] approaches you."
            show blackscreen onlayer black
            $ bg_current = "bg classroom"
            $ EmmaX.Loc = "bg classroom"
            $ EmmaX.OutfitChange()
            call Set_The_Scene
            $ EmmaX.FaceChange("sly")
            $ EmmaX.ArmPose = 2
            $ Count = 0
            call CleartheRoom(EmmaX,0,1)
            hide blackscreen onlayer black
            $ Line = 0
            if "detention" in Player.DailyActions:
                    ch_e "I'm glad you take your. . . education seriously."
            else:
                    #if you skipped detention
                    $ EmmaX.FaceChange("surprised")
                    ch_e "Oh, [EmmaX.Petname], you really shouldn't skip your detention like that. . ."
            $ Player.Traits.remove("detention")
            $ EmmaX.RecentActions.append("detention")
            $ EmmaX.DailyActions.append("detention")
            $ EmmaX.FaceChange("sly")
            $ EmmaX.Statup("Lust", 80, 3)
            ch_e "You've been such a naughty pupil. . ."
            $ EmmaX.ArmPose = 1
            $ EmmaX.FaceChange("sadside", Brows="normal")
            $ EmmaX.Statup("Lust", 80, 5)
            ch_e "Chasing after those young girls. . ."
            $ EmmaX.FaceChange("sly")
            $ EmmaX.Statup("Lust", 80, 3)
            if "detention" in EmmaX.History:
                    ch_e "How will we deal with it this time?"
            else:
                    #first time
                    ch_e "What am I to do with you. . ."
                    $ EmmaX.History.append("detention")

            "[EmmaX.Name] walks to the door and locks it behind her."
            $ Taboo = 0
            $ EmmaX.Taboo = 0
            $ Player.Traits.append("locked")
            menu:
                extend ""
                "I guess I should focus on my studies.":
                        if ApprovalCheck(EmmaX, 900) and "classcaught" in EmmaX.History:
                                $ EmmaX.FaceChange("perplexed")
                                $ EmmaX.Statup("Inbt", 70, -3)
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "Oh. Really? I was thinking of a more. . . recreational punishment."
                                menu:
                                    extend ""
                                    "Kidding, of course, what should we do? [[sex stuff]":
                                        $ EmmaX.FaceChange("sly")
                                        $ EmmaX.Statup("Love", 90, 3)
                                        $ EmmaX.Statup("Obed", 60, 5)
                                        $ EmmaX.Statup("Inbt", 70, 5)
                                        ch_e "Why do I put up with you?"
                                        call Emma_SexMenu
                                    "No, you're right, I take my education too lightly.":
                                        $ EmmaX.Statup("Love", 80, 1)
                                        $ EmmaX.Statup("Inbt", 70, -2)
                                        $ EmmaX.Statup("Lust", 80, 5)
                                        ch_e "Oh. Ok. Um. . ."
                                        $ EmmaX.FaceChange("sad")
                                        $ EmmaX.Statup("Obed", 60, 5)
                                        $ EmmaX.Statup("Lust", 80, 5)
                                        ch_e "I guess we could go over some of the topics from today's class then. . ."
                                        $ EmmaX.Statup("Lust", 80, 5)
                                        $ Player.XP += 10
                        else:
                                        #She's not into you yet.
                                        $ EmmaX.FaceChange("sad", Mouth="normal")
                                        $ EmmaX.Statup("Love", 50, 5)
                                        $ EmmaX.Statup("Love", 80, 5)
                                        $ EmmaX.Statup("Obed", 60, 5)
                                        $ EmmaX.Statup("Lust", 80, 5)
                                        ch_e "Yes. . . Exactly. . ."
                                        $ EmmaX.Statup("Inbt", 50, 5)
                                        $ EmmaX.Statup("Lust", 80, 5)
                                        ch_e "I guess we could go over some of the topics from today's class then. . ."
                                        $ EmmaX.Statup("Inbt", 70, 5)
                                        $ EmmaX.Statup("Lust", 80, 5)
                                        $ Player.XP += 10
                "I could think of a few things. . . [[sex stuff]":
                        if ApprovalCheck(EmmaX, 900) and "classcaught" in EmmaX.History:
                                $ EmmaX.FaceChange("sly")
                                $ EmmaX.Statup("Lust", 80, 5)
                                $ EmmaX.Statup("Love", 90, 5)
                                $ EmmaX.Statup("Obed", 60, 5)
                                $ EmmaX.Statup("Inbt", 70, 5)
                                ch_e "I just bet you can. . ."
                                call Emma_SexMenu
                        else:
                                #She's not into you yet.
                                $ EmmaX.FaceChange("sad", Mouth="smirk")
                                $ EmmaX.Statup("Love", 80, 5)
                                $ EmmaX.Statup("Obed", 60, 5)
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "I'm sure you could. . . but unfortunately this isn't the time for it."
                                $ EmmaX.Statup("Inbt", 50, 5)
                                $ EmmaX.Statup("Inbt", 70, 5)
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "We'll just have to settle for going over some of the topics from today's class. . ."
                                $ EmmaX.Statup("Inbt", 50, 5)
                                $ EmmaX.Statup("Lust", 80, 5)
                                $ Player.XP += 10
            $ Round -= 20 if Round > 20 else 0
            ch_e "Ok, I think that's plenty for now. . ."
            ch_e "You wouldn't want to make this a habit. . ."
            $ temp_modifier = 0
            $ EmmaX.OutfitChange()
            $ Player.DrainWord("locked",0,0,1)
            return

label Emma_Taboo_Talk:
        # This scene plays when you first try to do sexy stuff with Emma in public

        if "taboo" in EmmaX.History:
            return

        $ EmmaX.FaceChange("sly")
        if "taboocheck" not in EmmaX.History:
                ch_e "[EmmaX.Petname], I know that we've had some. . . fun,"
                $ EmmaX.FaceChange("sly", Eyes="side")
                ch_e "but that was between us, in private."
                $ EmmaX.FaceChange("sly")
                ch_e "I can't have our trysts become. . . public knowledge."
                ch_e "I am a teacher here, you understand."
                ch_e "You're a student."
                $ EmmaX.FaceChange("sadside")
                ch_e "It's complicated."
                ch_e "So I'm afraid that we can only. . ."
                $ EmmaX.FaceChange("sad")
                ch_e ". . .interact, when we're alone."
                ch_e "Do you understand?"
        else:
                ch_e "I believe I made clear why I couldn't do anything like that in public. . ."

        $ Line = 1
        while Line >= 1:
            menu:
                extend ""
                "Yeah, I suppose.":
                    $ EmmaX.FaceChange("smile")
                    if "taboocheck" in EmmaX.History:
                            pass
                    elif Line != 4:
                            #if you didn't ask all the questions first
                            $ EmmaX.Statup("Love", 60, 10)
                            $ EmmaX.Statup("Love", 70, 10)
                            $ EmmaX.Statup("Love", 90, 10)
                            $ EmmaX.Statup("Obed", 60, 5)
                            $ EmmaX.Statup("Inbt", 70, 5)
                    else:
                            $ EmmaX.Statup("Love", 60, 10)
                            $ EmmaX.Statup("Love", 90, 10)

                    ch_e "Thank you for your discretion."
                    $ EmmaX.FaceChange("sly")
                    if ApprovalCheck(EmmaX, 2000) and "taboocheck" in EmmaX.History:
                            ch_e "Although. . . I suppose we could make an exception. . ."
                            $ EmmaX.Statup("Inbt", 90, 10)
                            $ Line = -1
                    else:
                            ch_e "I do hope that we can still find some time to meet up."
                            $ Line = 0

                "I don't care who sees us." if Line != 2 and Line != 4:
                    if "taboocheck" in EmmaX.History:
                            ch_e "I'm aware. . ."
                            if ApprovalCheck(EmmaX, 500, "I"):
                                    $ EmmaX.FaceChange("sly")
                                    ch_e "Frankly, I don't either."
                                    $ EmmaX.FaceChange("angry", Eyes="side")
                                    ch_e "It's not about that though, if we get caught, I get fired."
                                    $ EmmaX.FaceChange("angry")
                                    ch_e "If I get fired, then I can't stay here."
                                    $ EmmaX.FaceChange("sly")
                                    ch_e "So that really isn't an option."
                            else:
                                    $ EmmaX.FaceChange("confused", 1)
                                    ch_e "You might not, but I have a reputation to maintain."
                    elif ApprovalCheck(EmmaX, 500, "I"):
                                    $ EmmaX.Statup("Lust", 80, 5)
                                    $ EmmaX.Statup("Inbt", 70, 5)
                                    $ EmmaX.FaceChange("sly")
                                    ch_e "Frankly, I don't either."
                                    $ EmmaX.FaceChange("angry", Eyes="side")
                                    ch_e "It's not about that though, if we get caught, I get fired."
                                    $ EmmaX.FaceChange("angry")
                                    $ EmmaX.Statup("Love", 90, 10)
                                    $ EmmaX.Statup("Obed", 60, 10)
                                    ch_e "If I get fired, then I can't stay here."
                                    $ EmmaX.FaceChange("sly")
                                    ch_e "So that really isn't an option."
                    else:
                                    $ EmmaX.Statup("Lust", 80, 5)
                                    $ EmmaX.Statup("Love", 90, 10)
                                    $ EmmaX.Statup("Obed", 60, 10)
                                    $ EmmaX.FaceChange("confused", 1)
                                    ch_e "Well you might not, but I have a reputation to maintain."
                    $ EmmaX.FaceChange("sly")
                    ch_e "So can you understand why we must be discrete?"
                    $ Line = 4 if Line != 1 else 2

                "Couldn't you just mindwipe anyone who sees?" if Line != 3 and Line != 4:
                    if "taboocheck" in EmmaX.History:
                            ch_e "Yes, we've been over why that wouldn't exactly be an option."
                    else:
                            if ApprovalCheck(EmmaX, 500, "I"):
                                $ EmmaX.FaceChange("sly")
                                $ EmmaX.Statup("Lust", 80, 5)
                                $ EmmaX.Statup("Love", 80, 5)
                                $ EmmaX.Statup("Obed", 60, 5)
                                $ EmmaX.Statup("Inbt", 70, 5)
                                ch_e "You must have read my mind."
                            elif ApprovalCheck(EmmaX, 800, "LO"):
                                $ EmmaX.FaceChange("sly",1)
                                $ EmmaX.Statup("Lust", 80, 5)
                                $ EmmaX.Statup("Love", 90, 10)
                                $ EmmaX.Statup("Obed", 60, 10)
                                $ EmmaX.Statup("Inbt", 70, 5)
                                ch_e "Oh, you naughty boy."
                            else:
                                $ EmmaX.FaceChange("surprised",1)
                                $ EmmaX.Statup("Lust", 80, 5)
                                $ EmmaX.Statup("Obed", 60, 10)
                                $ EmmaX.Statup("Inbt", 50, 15)
                                $ EmmaX.Statup("Inbt", 70, 10)
                                ch_e "What? I would never!"
                            $ EmmaX.FaceChange("angry",Eyes="side")
                            ch_e "Either way though, that's not really an option either."
                    ch_e "I can't muck about with the students' minds too much without Charles catching on."
                    ch_e "Casually mindwiping students certainly wouldn't pass unnoticed."
                    if EmmaX in Rules:
                            #if Xavier ignores you
                            ch_p "But Xavier is off the board now. . ."
                            $ EmmaX.FaceChange("sly")
                            ch_e "I suppose that's true. . ."
                            ch_e "A little helpful editing might not hurt. . ."
                            $ Line = -1
                    else:
                            $ EmmaX.FaceChange("confused",Mouth="normal")
                            ch_e "So are we on the same page here?"
                            $ Line = 4 if Line != 1 else 3

                "I don't care, let's do it." if Line == 4:
                    $ Line = 0
                    if ApprovalCheck(EmmaX, 2000):
                            $ EmmaX.FaceChange("surprised", Eyes="side")
                            $ EmmaX.Statup("Lust", 80, 5)
                            $ EmmaX.Statup("Inbt", 50, 15)
                            $ EmmaX.Statup("Inbt", 70, 10)
                            ch_e "Oh, I will get in so much trouble for this. . ."
                            $ EmmaX.Statup("Love", 90, 5)
                            $ EmmaX.Statup("Obed", 60, 15)
                            $ EmmaX.FaceChange("sly")
                            ch_e "but you're worth it."
                            $ Line = -1
                    elif ApprovalCheck(EmmaX, 800, "I"):
                            $ EmmaX.FaceChange("surprised", Eyes="side")
                            $ EmmaX.Statup("Lust", 80, 5)
                            $ EmmaX.Statup("Obed", 60, 15)
                            ch_e "Oh, I will get in so much trouble for this. . ."
                            $ EmmaX.FaceChange("sly")
                            ch_e "but it will be so much fun."
                            $ Line = -1
                    elif "taboocheck" in EmmaX.History:
                            $ EmmaX.FaceChange("angry")
                            $ EmmaX.Statup("Love", 90, -5)
                            $ EmmaX.Statup("Obed", 60, -5)
                            ch_e "You're going to have to respect my boundaries on this one."
                            $ EmmaX.RecentActions.append("angry")
                            $ EmmaX.DailyActions.append("angry")
                            $ renpy.pop_call() #drops it past the sex menu
                    else:
                            $ EmmaX.FaceChange("angry")
                            $ EmmaX.Statup("Love", 90, -5)
                            $ EmmaX.Statup("Obed", 60, -5)
                            $ EmmaX.Statup("Inbt", 70, 10)
                            ch_e "Well that's just too bad."
                            ch_e "If you can't respect such a simple limitation, then I believe we're done for now."
                            $ EmmaX.RecentActions.append("angry")
                            $ EmmaX.DailyActions.append("angry")
                            $ renpy.pop_call() #drops it past the sex menu
        #end loop if Line < 1

        if "taboocheck" not in EmmaX.History:
                $ EmmaX.History.append("taboocheck")
        if Line == -1:
                #if she agrees to do it
                $ EmmaX.History.append("taboo")
                $ EmmaX.History.remove("taboocheck")
        $ Line = 0
        return

label Emma_ThreeCheck(Pass=3,Quest=[],Girl=0,BO=[]):
        # This is called when Emma is asked whether to do a threesome
        if EmmaX.SEXP <= 30:
                $ EmmaX.FaceChange("confused")
                ch_e "[EmmaX.Petname], I barely put up with you, don't try to bring other girls into this."
                return
        if "three" in EmmaX.History:
                return

        $ Line = 0
        $ BO = TotalGirls[:]
        $ BO.remove(EmmaX)
        while BO:
                if "saw with " + BO[0].Tag in EmmaX.Traits:
                        $ Line = "I saw you with " + BO[0].Tag
                if BO[0].Loc == bg_current:
                        $ Girl = BO[0]
                        $ BO = [1]
                $ BO.remove(BO[0])

        if not Girl or Girl not in TotalGirls:
            $ Quest.append(2)
            if Line:
                $ EmmaX.FaceChange("angry", Eyes = "side")
                if Line:
                        ch_e "[Line] earlier. I'm not sure how I feel about that." #"I saw you with Rogue"
                $ Line = 0
                if "sleeptime" in EmmaX.History:
                        # if you tried to have a sleepover
                        ch_e "I saw you considering having me sleep over with that. . . girl. . ."
                        $ EmmaX.History.remove("sleeptime")

        if "threecheck" not in EmmaX.History:
                $ EmmaX.FaceChange("bemused", Eyes = "side")
                "[EmmaX.Name] moves close to you and whispers. . ."
                if ApprovalCheck(EmmaX, 900, "L"):
                        ch_e "[EmmaX.Petname], I really do. . . care for you. . ."
                elif ApprovalCheck(EmmaX, 800, "L"):
                        ch_e "[EmmaX.Petname], I do think you're. . . interesting. . ."
                elif ApprovalCheck(EmmaX, 500, "O"):
                        ch_e "[EmmaX.Petname], there is something. . . compelling about you. . ."
                elif ApprovalCheck(EmmaX, 500, "I"):
                        ch_e "[EmmaX.Petname], you know that I'm. . . flexible,"
                else:
                        ch_e "[EmmaX.Petname], I don't know what this even is yet, but. . ."
                ch_e "I'm a teacher at this school, and I can't exactly be caught forming some sort of. . ."
                ch_e "harem with the students."
                ch_e "Just you and I would be scandalous, but multiple students?"
                ch_e "That could be a disaster."
        else:
                ch_e "I already explained why I couldn't do this around other girls."
        while Pass > 0:
            menu:
                extend ""
                "Yeah, I suppose.":
                        $ EmmaX.FaceChange("smile")
                        if "threecheck" not in EmmaX.History:
                                $ EmmaX.Statup("Love", 60, 10)
                                $ EmmaX.Statup("Love", 90, 10)

                        ch_e "Thank you for not insisting."
                        $ EmmaX.FaceChange("sly")
                        if Pass == 1 and ApprovalCheck(EmmaX, 2000):
                            ch_e "though I suppose. . . perhaps I could make an exception. . ."
                            $ Pass = 0
                        else:
                            ch_e "I do hope that we can still find some. . . personal time?"
                            $ Pass = -1

                "But she's cool with it." if 2 not in Quest:
                        # This can add up to 2 if both girls refuse, or -2 if both are really into it.
                        # -1 more likely
                        $ Quest.append(2)
                        if Girl.Loc == bg_current:
                                $ Pass -= 1
                                if "poly Emma" in Girl.Traits:
                                        #If Rogue is already on board
                                        if Girl == RogueX:
                                                ch_r "Yeah, like I said, ready when you are."
                                        elif Girl == KittyX:
                                                ch_k "Yup, sounds fun."
                                        elif Girl == LauraX:
                                                ch_l "Yeah, I'm in."
                                else:
                                        $ Girl.Traits.append("poly Emma")
                                        if ApprovalCheck(Girl, 1500) and Girl.LikeEmma >= 800:
                                                if Girl == RogueX:
                                                        ch_r "I really am."
                                                elif Girl == KittyX:
                                                        ch_k "Yeah, you bet."
                                                elif Girl == LauraX:
                                                        ch_l "Sure."
                                        elif ApprovalCheck(Girl, 1500) and Girl.LikeEmma >= 600:
                                                if Girl == RogueX:
                                                        ch_r "Yeah, you'll do."
                                                elif Girl == KittyX:
                                                        ch_k "Yeah, you're ok."
                                                elif Girl == LauraX:
                                                        ch_l "Yeah, it's cool."
                                        elif ApprovalCheck(Girl, 2000):
                                                if Girl == RogueX:
                                                        ch_r "You and I get along like cats and bitches. . ."
                                                        ch_r "but I do want to make him happy."
                                                elif Girl == KittyX:
                                                        ch_k "I don't like you much, but I do want him to be happy."
                                                elif Girl == LauraX:
                                                        ch_l "Ugh, yeah. . ."
                                                        ch_l "I mean this guy seems to like you."
                                        elif ApprovalCheck(Girl, 500) and Girl.LikeEmma >= 800:
                                                if Girl == RogueX:
                                                        ch_r "This guy I could take or leave, but you clean up real nice."
                                                elif Girl == KittyX:
                                                        ch_k "Well, I don't know about this guy, but. . . you're pretty."
                                                elif Girl == LauraX:
                                                        ch_l "Hey, even without [Player.Name] here, you're a catch."
                                        else:
                                                if Girl == RogueX:
                                                        ch_r "I said no such thing!"
                                                elif Girl == KittyX:
                                                        ch_k "I didn't say anything like that!"
                                                elif Girl == LauraX:
                                                        ch_l "Say what now?"
                                                $ Girl.Traits.remove("poly Emma")
                                                $ Pass += 1
                        if EmmaX.GirlLikeCheck(Girl) >= 700:
                                ch_e "And you're quite fetching yourself dear. . ."
                                $ Pass -= 1 if Pass > 0 else 0
                        elif EmmaX.GirlLikeCheck(Girl) >= 500:
                                ch_e "And you're. . . acceptable. . ."
                        else:
                                ch_e "And that's just lovely, really. . ."
                                $ Pass += 1
                        ch_e "But I'm afraid that any sort of dalliance would be an issue."
                #end "she's cool with it"

                "Xavier doesn't care." if Taboo and EmmaX in Rules and 3 not in Quest:
                                $ Quest.append(3)
                                ch_e "Well, that may be, but it could still get out."
                                $ Pass -= 1

                "Xavier won't find out here." if not Taboo and 3 not in Quest:
                                $ Quest.append(3)
                                ch_e "Well, that may be, but it could still get out."
                                $ Pass -= 1

                "I don't care, let's do this." if Quest:
                        if ApprovalCheck(EmmaX, 2000) and Pass <= 2:
                                $ EmmaX.FaceChange("surprised", Eyes="side")
                                $ EmmaX.Statup("Lust", 80, 5)
                                $ EmmaX.Statup("Inbt", 50, 15)
                                $ EmmaX.Statup("Inbt", 70, 10)
                                $ EmmaX.Statup("Love", 90, 5)
                                $ EmmaX.Statup("Obed", 60, 15)
                                ch_e "Oh, I could get in so much trouble for this. . ."
                                $ EmmaX.FaceChange("sly")
                                ch_e "but you're worth it."
                                $ Pass = 0
                        elif ApprovalCheck(EmmaX, 800, "I") and Pass <= 2:
                                $ EmmaX.FaceChange("surprised", Eyes="side")
                                $ EmmaX.Statup("Lust", 80, 5)
                                $ EmmaX.Statup("Obed", 60, 15)
                                ch_e "Oh, I could get in so much trouble for this. . ."
                                $ EmmaX.FaceChange("sly")
                                ch_e "but it will be so much fun."
                                $ Pass = 0
                        elif "threecheck" not in EmmaX.History:
                                $ EmmaX.FaceChange("angry")
                                $ EmmaX.Statup("Love", 90, -5)
                                $ EmmaX.Statup("Obed", 60, -5)
                                ch_e "You're going to have to learn to take \"no\" for an answer on this one."
                                $ EmmaX.RecentActions.append("angry")
                                $ EmmaX.DailyActions.append("angry")
                                $ Pass = -1
                        else:
                                $ EmmaX.FaceChange("angry")
                                $ EmmaX.Statup("Love", 90, -5)
                                $ EmmaX.Statup("Obed", 60, -5)
                                $ EmmaX.Statup("Inbt", 70, 10)
                                ch_e "Well that's just too bad."
                                ch_e "If you can't respect such a simple limitation, then I believe we're done for now."
                                $ EmmaX.RecentActions.append("angry")
                                $ EmmaX.DailyActions.append("angry")
                                $ Pass = -1

        if "threecheck" not in EmmaX.History:
                $ EmmaX.History.append("threecheck")
        if Pass == -1:
                # if the conditions added up to failure state, it exits the sex menu
                $ renpy.pop_call() #drops it past the sex menu
        else:
                #if the conditions don't add up to failure, then it results in a success state
                $ EmmaX.History.append("three")
                $ EmmaX.History.remove("threecheck")
                if Girl in TotalGirls:
                        if "poly " + Girl.Tag not in EmmaX.Traits:
                                $ EmmaX.Traits.append("poly " + Girl.Tag)
                        $ EmmaX.RecentActions.append("noticed " + Girl.Tag)
                        $ Girl.RecentActions.append("noticed Emma")
        return

label Emma_Love(Shipping=[],Shipshape=0,BO=[]):
        $ EmmaX.DrainWord("asked meet")
        # Shipping is used to track who else you're involved with
        $ BO = TotalGirls[:]
        $ BO.remove(EmmaX)
        while BO:
            if ApprovalCheck(BO[0], 1200, "LO"):
                    $ Shipping.append(BO[0])
            $ BO.remove(BO[0])
        $ Shipshape = len(Shipping)

        if EmmaX.Loc == bg_current or EmmaX in Party:
                "[EmmaX.Name] glances over at you with an apprising look on her face."
        else:
                "[EmmaX.Name] turns a corner and notices you."
        if bg_current != "bg emma" and bg_current != "bg player":
                "With little word, she takes your hand and pulls you back to her room."
                $ bg_current = "bg emma"
        $ EmmaX.Loc = bg_current
        call Set_The_Scene
        call CleartheRoom(EmmaX)
        call Taboo_Level
        $ EmmaX.DailyActions.append("relationship")

        $ EmmaX.FaceChange("sexy",Eyes="side")
        ch_e "As you are aware, this. . . situation has been going for a while now."
        ch_e "It's been very. . . comfortable for me."
        $ EmmaX.FaceChange("sexy")
        ch_e "I have enjoyed your company. . . is what I'm trying to say."
        menu:
                extend ""
                "It's more than just company, we're together in this.":
                        $ EmmaX.FaceChange("smile",1)
                        $ EmmaX.Statup("Love", 200, 10)
                        $ EmmaX.Statup("Inbt", 90, 5)
                        ch_e "Yes!"
                        ch_e "Yes, we certainly are more than that."
                        $ EmmaX.FaceChange("sly")
                        ch_e "You must have read my mind."
                "I've enjoyed it a lot too.":
                        $ EmmaX.FaceChange("sly")
                        $ EmmaX.Statup("Love", 200, 5)
                        $ EmmaX.Statup("Obed", 90, 2)
                        ch_e "Yes, I imagine you have."
                        ch_e "Perhaps it was more than that though. . ."
                "Yeah, it's been fun.":
                        $ EmmaX.FaceChange("confused")
                        $ EmmaX.Statup("Obed", 90, 5)
                        ch_e "Yes, \"fun.\""
                        $ EmmaX.FaceChange("angry",Eyes="side")
                        ch_e "It is fun, but I was thinking. . ."
                        $ EmmaX.FaceChange("sly")
                "Oh, ok.":
                        $ EmmaX.FaceChange("confused",Eyes="side")
                        ch_e "Um, yes. . ."
                        ch_e ". . ."
                        $ EmmaX.FaceChange("confused")
                        ch_e "I'm not sure I was clear. . ."
                "Yeah, you're a good ride.":
                    $ EmmaX.FaceChange("angry")
                    if not ApprovalCheck(EmmaX, 1600):
                            $ EmmaX.Statup("Obed", 90, -5)
                            $ EmmaX.Statup("Inbt", 90, -5)
                            $ EmmaX.Eyes="side"
                            ch_e "Never mind, this was a bad idea."
                            jump Emma_Love_End
                    ch_e "Such impertinence!"
                    if ApprovalCheck(EmmaX, 1000, "OI"):
                            $ EmmaX.FaceChange("sly",2)
                            $ EmmaX.Statup("Obed", 90, 10)
                            $ EmmaX.Statup("Inbt", 90, 5)
                            $ EmmaX.Statup("Lust", 70, 5)
                            ch_e "I am though, yes."
                            $ EmmaX.Blush = 1
                    else:
                            $ EmmaX.FaceChange("sexy")
                            $ EmmaX.Statup("Obed", 90, 5)
                            $ EmmaX.Statup("Inbt", 90, 5)
                            ch_e "I suppose that's part of your charm though."

        ch_e "I certainly do care for you. . ."
        ch_e "Perhaps more than I have for anyone else in a long time."
        if ApprovalCheck(EmmaX, 1600):
                $ EmmaX.FaceChange("sexy",Eyes="side")
                ch_e "Perhaps more than I ever have."
        ch_e ". . ."
        ch_e "What I'm trying to say is. . ."
        $ EmmaX.FaceChange("sexy",Brows="sad")
        ch_e "I love you."
        menu:
                extend ""
                "I love you too, [EmmaX.Pet]!":
                    $ EmmaX.FaceChange("smile",2)
                    $ EmmaX.Statup("Love", 200, 20)
                    $ EmmaX.Statup("Inbt", 90, 10)
                    ch_e "I dearly hoped that you did!"
                    $ EmmaX.Petnames.append("lover")
                    jump Emma_Love_End
                "Wow! That's cool.":
                    $ EmmaX.FaceChange("confused")
                    $ EmmaX.Statup("Love", 200, 5)
                    ch_e "Cool?"
                    ch_e "Don't you have anything else you'd like to say to me?"
                    $ EmmaX.FaceChange("sadside",2)
                "Oh, ok.":
                    $ EmmaX.FaceChange("confused",2)
                    $ EmmaX.Statup("Obed", 90, 5)
                    $ EmmaX.Statup("Inbt", 90, -5)
                    ch_e "Ok?"
                    $ EmmaX.FaceChange("angry")
                    ch_e "Is that all the response you have for me?"
                "Ha!":
                    $ EmmaX.FaceChange("surprised",2)
                    $ EmmaX.Statup("Love", 200, -5)
                    $ EmmaX.Statup("Obed", 90, 10)
                    $ EmmaX.Statup("Inbt", 90, -5)
                    ch_e "!"
                    $ EmmaX.FaceChange("angry",2)
                    ch_e "Well that's hardly the response I expected."
        ch_e "I would hope that you also love me. . ."
        menu:
                extend ""
                "Oh! Yes, of course I love you, [EmmaX.Pet]!":
                            $ EmmaX.NameCheck() #checks reaction to petname
                            $ EmmaX.FaceChange("smile",2)
                            $ EmmaX.Statup("Love", 90, 15)
                            $ EmmaX.Statup("Obed", 90, 2)
                            ch_e "I dearly hoped that you did!"
                            $ EmmaX.Petnames.append("lover")
                            jump Emma_Love_End
                "Oh. Oooooh! Yeah, sure.":
                    if ApprovalCheck(EmmaX, 1200, "OI"):
                            $ EmmaX.FaceChange("sly",1)
                            $ EmmaX.Statup("Love", 200, 5)
                            $ EmmaX.Statup("Obed", 90, 10)
                    if ApprovalCheck(EmmaX, 1200, "OI"):
                            $ EmmaX.FaceChange("sly",1,Brows="angry")
                            $ EmmaX.Statup("Love", 200, 5)
                            $ EmmaX.Statup("Obed", 90, 5)
                            $ EmmaX.Statup("Inbt", 90, -5)
                    ch_e "I'm glad to see that you caught up with the situation."
                "Oh. That's awkward.":
                            $ EmmaX.FaceChange("angry",2)
                            $ EmmaX.Statup("Love", 200, -15)
                            $ EmmaX.Statup("Obed", 90, 15)
                            $ EmmaX.Statup("Inbt", 90, -10)
                            ch_e "Awkward?!"
                            ch_e "This situation is about to become considerably more \"awkward.\""
                            $ EmmaX.Blush = 1
                            $ Line = "angry"

        ch_e "I'm giving you one last chance here."
        ch_e "This is not a time for fooling around."
        ch_e "Do you love me, or not?"
        menu:
                extend ""
                "Yes, of course I love you, [EmmaX.Pet]!":
                            $ EmmaX.NameCheck() #checks reaction to petname
                            $ EmmaX.FaceChange("sly",2)
                            $ EmmaX.Statup("Love", 90, 5)
                            $ EmmaX.Statup("Obed", 90, 15)
                            $ EmmaX.Statup("Inbt", 90, 5)
                            ch_e "Took you long enough to get there."
                            $ EmmaX.Petnames.append("lover")
                            jump Emma_Love_End
                "I can't really say yet.":
                    if Line != "angry" or ApprovalCheck(EmmaX, 800, "OI"):
                            $ EmmaX.FaceChange("sadside")
                            $ EmmaX.Statup("Obed", 90, 5)
                    else:
                            $ EmmaX.FaceChange("angry")
                            $ EmmaX.Statup("Love", 200, -5)
                            $ EmmaX.Statup("Obed", 90, 5)
                            $ EmmaX.Statup("Inbt", 90, -5)
                    ch_e "Oh."
                "No.":
                    if Line == "angry" or not ApprovalCheck(EmmaX, 800, "OI"):
                            $ EmmaX.FaceChange("angry")
                            $ EmmaX.Statup("Love", 200, -10)
                            $ EmmaX.Statup("Obed", 90, 10)
                            $ EmmaX.Statup("Inbt", 90, -5)
                    else:
                            $ EmmaX.FaceChange("sadside")
                            $ EmmaX.Statup("Love", 200, -10)
                            $ EmmaX.Statup("Obed", 90, 10)
                            $ EmmaX.Statup("Inbt", 90, -5)
                    ch_e "Oh."

        ch_e "Is it because of someone else?"
        $ Line = 0
        menu:
                extend ""
                "Yes, it's [RogueX.Name]." if RogueX in Shipping and Shipshape < 3:
                    $ Line = RogueX
                "Yes, it's [KittyX.Name]." if KittyX in Shipping and Shipshape < 3:
                        $ Line = KittyX
                "Yes, it's [LauraX.Name]." if LauraX in Shipping and Shipshape < 3:
                        $ Line = LauraX
                "Yes, it's the others" if Shipshape > 1:
                    $ EmmaX.Statup("Obed", 90, 15)
                    $ EmmaX.Statup("Inbt", 90, 5)
                    $ EmmaX.Statup("Lust", 90, 5)
                    ch_e "I suppose I can't blame you there."
                "There's nobody else.":
                    $ EmmaX.FaceChange("sadside")
                    $ EmmaX.Statup("Love", 200, -15)
                    $ EmmaX.Statup("Obed", 90, 15)
                    $ EmmaX.Statup("Inbt", 90, 5)
                    if ApprovalCheck(EmmaX, 1000, "OI"):
                        ch_e "Hmmm. . . well I suppose I can take solace in that."
                    else:
                        ch_e "I see."
                "It's a \"you\" problem.":
                    $ EmmaX.FaceChange("angry")
                    $ EmmaX.Statup("Love", 200, -25)
                    $ EmmaX.Statup("Obed", 90, 15)
                    ch_e "Oh is it now?"
                    $ EmmaX.Statup("Love", 200, -10)
                    ch_e "I can think of a great many ways to make this a \"you\" problem."
                    $ EmmaX.RecentActions.append("angry")
                    $ EmmaX.DailyActions.append("angry")
        if Line:
                #If you called out a girl,
                if EmmaX.GirlLikeCheck(Line) >= 800:
                        $ EmmaX.Statup("Love", 200, 5)
                        $ EmmaX.Statup("Obed", 90, 20)
                        $ EmmaX.Statup("Inbt", 90, 5)
                        $ EmmaX.Statup("Lust", 90, 5)
                        ch_e "Yes, she is lovely."
                else:
                        $ EmmaX.FaceChange("angry",Eyes="side")
                        $ EmmaX.Statup("Love", 200, -5)
                        $ EmmaX.Statup("Obed", 90, 20)
                        ch_e "That cow!"
                        $ EmmaX.RecentActions.append("angry")
                        $ EmmaX.GLG(Line,800,-50,1)
        ch_e "I suppose I'll just have to let this go."
        ch_e "I'll. . . see you in a bit."
        ch_e "I need some time to consider this."

label Emma_Love_End:
        if "lover" not in EmmaX.Petnames:
                hide Emma_Sprite with easeoutright
                call Remove_Girl(EmmaX)
                $ EmmaX.Loc = "hold" #puts her off the board for the day
                return

        "[EmmaX.Name] pulls closer to you and snuggles into your arms."
        $ EmmaX.Statup("Love", 200, 25)
        $ EmmaX.Statup("Lust", 90, 5)
        ch_e "So. . . now that we have some time together. . ."
        $ EmmaX.Statup("Lust", 90, 10)

        if not EmmaX.Sex:
            ch_e "I think we've certainly waited long enough. . ."
        else:
            ch_e "Whatever do you intend to do about it?"
        $ Player.AddWord(1,"interruption") #adds to Recent
        menu:
                extend ""
                "Yeah, let's do this. . . [[have sex]":
                    $ EmmaX.Statup("Inbt", 30, 20)
                    $ EmmaX.Statup("Obed", 70, 10)
                    ch_e "Hmm. . ."
                    call Emma_SexAct("sex")
                "I have something else in mind. . .[[choose another activity]":
                    $ EmmaX.Brows = "confused"
                    $ EmmaX.Statup("Obed", 70, 25)
                    ch_e "Something like. . ."
                    $ temp_modifier = 20
                    call Emma_SexMenu
        return

label Emma_Love_Redux:
         #this is for if you rejected her but want a second chance
        $ Line = 0
        $ EmmaX.DailyActions.append("relationship")
        if EmmaX.Event[6] >= 25:
                #if this is the second time through
                ch_p "I hope you've forgiven me, I still love you."
                $ EmmaX.Statup("Love", 95, 10)
                if ApprovalCheck(EmmaX, 950, "L"):
                    $ Line = "love"
                else:
                    $ EmmaX.FaceChange("angry")
                    ch_e "I don't believe you're sufficiently contrite, [EmmaX.Petname]."
                    $ EmmaX.Eyes="side"
                    ch_e ". . ."
                    $ EmmaX.FaceChange("angry",Mouth="lipbite")
                    ch_e "I didn't tell you to stop."
        else:
                    ch_p "Remember when I told you that I didn't love you?"
                    $ EmmaX.FaceChange("perplexed",1)
                    ch_e ". . ."
                    $ EmmaX.FaceChange("angry", Eyes="side")
                    ch_e "I believe I do remember something to that effect, yes."
        if Line != "love":
                menu:
                    extend ""
                    "I'm sorry, I didn't mean it.":
                            $ EmmaX.Eyes = "surprised"
                            ch_e "Oh? So you do love me?"
                            ch_p "Yeah. I mean, yes, I love you, [EmmaX.Name]."
                            $ EmmaX.Statup("Love", 200, 10)
                            if ApprovalCheck(EmmaX, 950, "L"):
                                $ Line = "love"
                            else:
                                $ EmmaX.FaceChange("sadside")
                                ch_e "I'm not sure that I still do. . ."
                    "I've changed my mind, so. . .":
                            if ApprovalCheck(EmmaX, 950, "L"):
                                $ Line = "love"
                                $ EmmaX.Eyes = "surprised"
                                ch_e "Oh?"
                            else:
                                $ EmmaX.Mouth = "sad"
                                ch_e "Oh, you've changed your mind. Lovely."
                                $ EmmaX.Statup("Inbt", 90, 10)
                                $ EmmaX.FaceChange("sadside")
                                ch_e "Perhaps I have too. . ."
                    "Um, never mind.":
                                $ EmmaX.Statup("Love", 200, -30)
                                $ EmmaX.Statup("Obed", 50, 10)
                                $ EmmaX.FaceChange("angry")
                                ch_e "Don't you dare."
                                $ EmmaX.RecentActions.append("angry")
        if Line == "love":
                $ EmmaX.Statup("Love", 200, 40)
                $ EmmaX.Statup("Obed", 90, 10)
                $ EmmaX.Statup("Inbt", 90, 10)
                $ EmmaX.FaceChange("smile")
                ch_e "I couldn't be happier!"
                ch_e "I love you too, [EmmaX.Petname]!"
                if EmmaX.Event[6] < 25:
                        $ EmmaX.FaceChange("sly")
                        "She grabs the back of your head and pulls you close."
                        ch_e "You shouldn't have kept me waiting."
                $ EmmaX.Petnames.append("lover")
        $ EmmaX.Event[6] = 25
        return

label Emma_Sub:     #Emma_Update
        $ EmmaX.DrainWord("asked meet")
        call Shift_Focus(EmmaX)

        if EmmaX.Loc != bg_current and EmmaX not in Party:
                "[EmmaX.Name] shows up and says she needs to talk to you."
        else:
                "[EmmaX.Name] approaches you, looking to talk."
        $ EmmaX.Loc = bg_current
        call Set_The_Scene
        call CleartheRoom(EmmaX)
        call Taboo_Level
        $ EmmaX.DailyActions.append("relationship")
        $ EmmaX.FaceChange("bemused", 1)

        $ Line = 0
        ch_e "I've been noticing, you have a sort of"
        ch_e ". . . commanding air about you, [EmmaX.Petname]."
        menu:
            extend ""
            "I guess. That's just kind of what comes naturally for me.":
                            $ EmmaX.Statup("Obed", 200, 10)
                            $ EmmaX.Statup("Inbt", 50, 5)
            "Sorry. I didn't mean to come off like that.":
                            $ EmmaX.FaceChange("startled", 2)
                            $ EmmaX.Statup("Love", 80, 5)
                            $ EmmaX.Statup("Obed", 200, -5)
                            $ EmmaX.Statup("Inbt", 50, -5)
                            ch_e "Oh, don't apologize. . ."
            "Yup. Deal with it.":
                    if ApprovalCheck(EmmaX, 1000, "LO"):
                            $ EmmaX.Statup("Obed", 200, 20)
                            $ EmmaX.Statup("Inbt", 50, 10)
                            ch_e "Ehem. . ."
                    else:
                            $ EmmaX.Statup("Love", 200, -10)
                            $ EmmaX.Statup("Obed", 200, 10)
                            $ EmmaX.Statup("Inbt", 50, 5)
                            $ EmmaX.FaceChange("angry")
                            ch_e "Well, that wasn't exactly what I had in mind." #(Loss of points)
                            menu:
                                extend ""
                                "Guess you don't know me so well, huh?":
                                        ch_e "I suppose that I don't."
                                        $ Line = "rude"
                                "Sorry.  I kind of thought you were getting into me being like that.":
                                        $ EmmaX.FaceChange("sexy", 2)
                                        $ EmmaX.Eyes = "side"
                                        $ EmmaX.Statup("Love", 95, 5)
                                        $ EmmaX.Statup("Obed", 200, 5)
                                        $ EmmaX.Statup("Inbt", 50, 5)
                                        ch_e "Not. . . quite like that, no. . ."

        if not Line:
                # She's advancing to the next stage
                ch_e "What I was getting at, is that I think that I tend to. . ."
                $ EmmaX.FaceChange("sly", 2)
                ch_e "-enjoy when you take a firm hand with me."
                $ EmmaX.FaceChange("smile", 1)
                menu:
                    extend ""
                    "Good. If you wanna be with me, that's how it'll be.":
                            if ApprovalCheck(EmmaX, 1000, "LO"):
                                $ EmmaX.Statup("Obed", 200, 15)
                                $ EmmaX.Statup("Inbt", 50, 10)
                            else:
                                $ EmmaX.FaceChange("sadside", 1)
                                $ EmmaX.Statup("Love", 200, -5)
                                $ EmmaX.Statup("Obed", 200, 10)
                            ch_e "Perhaps with a touch more class, [EmmaX.Petname]. . ."
                            menu:
                                extend ""
                                "Whatever.  That's how it is.  Take it or leave it.":
                                        $ EmmaX.FaceChange("angry")
                                        $ EmmaX.Statup("Love", 200, -10)
                                        $ EmmaX.Statup("Obed", 200, 5)
                                        ch_e "I suppose you could use a bit more maturity first."
                                        $ Line = "rude"
                                "I think I could maybe do that." :
                                        $ EmmaX.FaceChange("bemused", 2)
                                        $ EmmaX.Eyes = "side"
                                        $ EmmaX.Statup("Love", 95, 5)
                                        $ EmmaX.Statup("Obed", 200, 3)
                                        $ EmmaX.Statup("Inbt", 50, 5)
                                        ch_e "That's good to hear."

                    "Yeah?  You think it's sexy?":
                                $ EmmaX.FaceChange("bemused", 2)
                                $ EmmaX.Eyes = "side"
                                $ EmmaX.Statup("Obed", 200, 5)
                                $ EmmaX.Statup("Inbt", 50, 10)


                    "You sure you don't want me to back off a little?":
                            $ EmmaX.FaceChange("startled", 1)
                            $ EmmaX.Statup("Obed", 200, -5)
                            menu:
                                ch_e "I wouldn't want to make you. . . uncomfortable."
                                "Only if you're okay with it.":
                                    $ EmmaX.FaceChange("bemused", 2)
                                    $ EmmaX.Statup("Love", 95, 10)
                                    $ EmmaX.Statup("Inbt", 50, 10)
                                    $ Line = 0
                                "Uhm. . .yeah.  I {i}do{/i} think it's weird.  Sorry.":
                                    $ EmmaX.Statup("Love", 200, -15)
                                    $ EmmaX.Statup("Obed", 200, -5)
                                    $ EmmaX.Statup("Inbt", 50, -10)
                                    $ Line = "embarrassed"

                    "I don't really care what you like.  I do what I want.":
                                    $ EmmaX.Statup("Love", 200, -10)
                                    $ EmmaX.Statup("Obed", 200, 15)
                                    $ EmmaX.FaceChange("angry")
                                    ch_e "Ugh. I think I may have misjudged you."
                                    $ Line = "rude"

        if not Line:
            $ EmmaX.FaceChange("bemused", 1, Eyes="side")
            ch_e "I'm more used to being in charge of the situation."
            ch_e "When you take control of things. . ."
            ch_e "I find it quite. . . exciting."
            menu:
                extend ""
                "Don't you think that relationship's kinda. . .weird?":
                        $ EmmaX.Statup("Love", 200, -5)
                        $ EmmaX.Statup("Inbt", 50, -15)
                        ch_e "Not at all, just perhaps a bit. . . unconventional."
                "I think I could get used to that kinda thing.":
                        $ EmmaX.Statup("Obed", 200, 5)
                        $ EmmaX.Statup("Inbt", 50, 5)
                        $ EmmaX.FaceChange("smile", 1)

        if not Line:
            $ EmmaX.FaceChange("smile", 1)
            ch_e "That sounds delightful. If you don't mind, could I refer to you as. . . sir?"
            $ EmmaX.FaceChange("sly", 2)
            ch_e "Would you enjoy that?"
            $ EmmaX.Blush = 1
            menu:
                extend ""
                "That has a nice ring to it.":
                                $ EmmaX.Statup("Love", 95, 5)
                                $ EmmaX.Statup("Obed", 200, 15)
                                $ EmmaX.Statup("Inbt", 50, 5)
                                ch_e "Very well then. . .{i}sir{/i}."
                                $ EmmaX.Petname = "sir"
                "I think I'd rather stick with what we've got going.":
                    $ EmmaX.FaceChange("confused", 2)
                    ch_e "Hmm."
                    $ EmmaX.Statup("Inbt", 50, -5)
                    $ EmmaX.FaceChange("sadside", 1)
                    menu:
                        ch_e ". . . could you perhaps still take the lead in things?"
                        "I like that idea.":
                                $ EmmaX.Statup("Obed", 200, 10)
                                $ EmmaX.FaceChange("smile", 1)
                                ch_e "That should do then, [EmmaX.Petname]."
                        "This is getting really awkward.":
                                $ EmmaX.Statup("Love", 200, -10)
                                $ EmmaX.Statup("Obed", 200, -50)
                                $ EmmaX.Statup("Inbt", 50, -15)
                                $Line = "embarrassed"

        $ EmmaX.History.append("sir")
        if not Line:
                $ EmmaX.Blush = 1
                $ EmmaX.Petnames.append("sir")
                #put in stuff that happens if this succeeds
        elif Line == "rude":
                hide Emma_Sprite with easeoutright
                call Remove_Girl(EmmaX)
                $ renpy.pop_call()
                "[EmmaX.Name] marches out the door in a huff, leaving you alone."
        elif Line == "embarrassed":
                $ EmmaX.FaceChange("sad", 2)
                ch_e "Well, I. . . um. . .."
                $ EmmaX.FaceChange("sly", 1)
                ch_e "I was testing you. Obviously. That would be unprofessional."
                $ EmmaX.FaceChange("sadside", 2)
                ch_e "I should go.  I think I see a student over there in need."
                $ EmmaX.Blush = 1
                hide Emma_Sprite with easeoutright
                call Remove_Girl(EmmaX)
                $ renpy.pop_call()
                "[EmmaX.Name] dashes out the door, leaving you alone. It didn't look like she could get away fast enough."
        return

label Emma_Sub_Asked: #Emma_Update
        $ Line = 0
        $ EmmaX.FaceChange("sadside", 1)
        ch_e "I might."
        ch_e "If I did, I would also remember that you seemed unprepared for the role."
        menu:
            extend ""
            "Well, I wanted to say I was sorry.  And I was hoping maybe we could give it another shot.":
                    if "sir" in EmmaX.Petnames and ApprovalCheck(EmmaX, 850, "O"):
                            #if this is asking about the "master" name, and her Obedience is higher than 700
                            pass
                    elif ApprovalCheck(EmmaX, 550, "O"):
                            #if it's instead about earning the "sir" title, and her approval is over 500
                            pass
                    else: #if it failed both those things,
                            ch_e "Perhaps when you've done a bit more soul-searching. . ." #Failed again. :(
                            $ Line = "rude"

                    if Line != "rude":
                            $ EmmaX.Statup("Love", 90, 10)
                            $ EmmaX.FaceChange("sly", 1)
                            ch_e "I suppose I could give you another chance."
                            ch_e "I appreciate that you recognize you made an error."
                            ch_e "Fine, we can give it another try."

            "Listen. . .I know it's what you want.  Do you want to try again, or not?":
                    $ EmmaX.FaceChange("bemused", 1)
                    if "sir" in EmmaX.Petnames and ApprovalCheck(EmmaX, 850, "O"):
                            ch_e "Ok, fine."
                    elif not ApprovalCheck(EmmaX, 600, "O"):
                            ch_e "Not at the moment, no."
                            $ Line = "rude"
                    else:
                            #if it's instead about earning the "sir" title, and her approval is over 500
                            $ EmmaX.FaceChange("sadside", 1)
                            ch_e "You do tend to push your luck."
                            $ EmmaX.Eyes = "squint"
                            ch_e "Perhaps you are right, but I do think an apology is still in order."
                            menu:
                                extend ""
                                "Okay, I'm sorry I was so rude about it.":
                                                $ EmmaX.Statup("Love", 90, 15)
                                                $ EmmaX.Statup("Inbt", 50, 10)
                                                $ EmmaX.FaceChange("bemused", 1, Eyes="side")
                                                ch_e "Apology accepted. . ."
                                "Not gonna happen.":
                                        if "sir" in EmmaX.Petnames and ApprovalCheck(EmmaX, 900, "O"):
                                                $ EmmaX.Statup("Love", 200, -5)
                                                $ EmmaX.Statup("Obed", 200, 10)
                                                ch_e ". . ."
                                        elif ApprovalCheck(EmmaX,650, "O"):
                                                $ EmmaX.Statup("Love", 200, -5)
                                                $ EmmaX.Statup("Obed", 200, 10)
                                                ch_e "I- um. . .hmmm. . ."
                                        else: #if it failed both those things,
                                                $ EmmaX.Statup("Love", 200, -10)
                                                $ EmmaX.Statup("Obed", 90, -10)
                                                $ EmmaX.Statup("Obed", 200, -10)
                                                $ EmmaX.Statup("Inbt", 50, -15)
                                                "[EmmaX.Name] sighs and rolls her eyes."
                                                $ EmmaX.FaceChange("angry", 1, Eyes="side")
                                                ch_e "You really don't learn, do you?"
                                                $ Line = "rude"
                                "Ok, never mind then.":
                                                $ EmmaX.FaceChange("angry", 1)
                                                $ EmmaX.Statup("Love", 200, -10)
                                                $ EmmaX.Statup("Obed", 90, -10)
                                                $ EmmaX.Statup("Obed", 200, -10)
                                                $ EmmaX.Statup("Inbt", 50, -15)
                                                ch_e "I don't know what I saw in you."
                                                $ Line = "rude"

        $ EmmaX.RecentActions.append("asked sub")
        $ EmmaX.DailyActions.append("asked sub")
        if Line == "rude":
                #If line hasn't been set to "rude" by something above, then it skips right past this
                hide Emma_Sprite with easeoutright
                call Remove_Girl(EmmaX)
                $ EmmaX.RecentActions.append("angry")
                $ renpy.pop_call()
                "[EmmaX.Name] marches out the door, leaving you alone.  She looked pretty upset."
        elif "sir" in EmmaX.Petnames:
                #it didn't fail and "sir" was covered
                $ EmmaX.Statup("Obed", 200, 50)
                $ EmmaX.Petnames.append("master")
                $ EmmaX.Petname = "master"
                $ EmmaX.Eyes = "sly"
                ch_e ". . . master. . ."
        else:
                #it didn't fail
                $ EmmaX.Statup("Obed", 200, 30)
                $ EmmaX.Petnames.append("sir")
                $ EmmaX.Petname = "sir"
                $ EmmaX.Eyes = "sly"
                ch_e ". . . sir."
        return

label Emma_Master:  #Emma_Update
        $ EmmaX.DrainWord("asked meet")
        call Shift_Focus(EmmaX)
        $ EmmaX.Loc = bg_current
        call Set_The_Scene
        if EmmaX.Loc != bg_current and EmmaX not in Party:
            "[EmmaX.Name] shows up and says she needs to talk to you."
        else:
            "[EmmaX.Name] approaches you, looking to talk."
        call CleartheRoom(EmmaX)
        $ EmmaX.DailyActions.append("relationship")
        call Taboo_Level
        $ Line = 0
        $ EmmaX.FaceChange("bemused", 1)
        ch_e "[EmmaX.Petname], if you don't mind my saying so. . ."
        ch_e "I do think that your more. . . assertive direction has been quite. . ."
        ch_e ". . . exhilarating."
        menu:
            extend ""
            "I like it too.":
                    $ EmmaX.FaceChange("sly", 1)
                    ch_e "Good, good. . ."
                    ch_e "That being the case, perhaps we would be able to. . ."
                    ch_e "Go a bit deeper?"
                    menu:
                        extend ""
                        "Nah.  This is just about perfect.":
                                $ EmmaX.FaceChange("sad", 1)
                                $ EmmaX.Statup("Obed", 200, -15)
                                $ EmmaX.Statup("Inbt", 50, 10)
                                ch_e "Oh? I suppose. . ."
                                $ Line = "fail"
                        "What'd you have in mind?":
                                $ EmmaX.Eyes = "side"
                                ch_e "Hmm, well I was just considering, perhaps I could refer to you as. . ."
                                ch_e ". . . {i}master{/i}?"
                                $ EmmaX.Eyes = "squint"
                                ch_e "Would you like that? Would that appeal to you?"
                                menu:
                                    extend ""
                                    "Oh, yeah.  I'd like that.":
                                            ch_e "Lovely. . ."
                                    "Uhm. . .nah.  That's too much.":
                                            $ EmmaX.FaceChange("sad", 1)
                                            $ EmmaX.Statup("Obed", 200, -15)
                                            $ EmmaX.Statup("Inbt", 50, 5)
                                            ch_e "Oh. Very well then, forget I said anything about it."
                                            ch_e "Forget. . . forget. . . "
                                            ch_e "Oh, never mind, I forgot that doesn't actually work on you."
                                            ch_e "Just, be discreet."
                                            $ Line = "fail"

                        "Actually, I'd prefer we stopped doing it. I don't want to be too controlling.":
                                $ EmmaX.FaceChange("sly", 1)
                                $ EmmaX.Statup("Love", 200, 15)
                                $ EmmaX.Statup("Obed", 200, -10)
                                $ EmmaX.Statup("Inbt", 50, 10)
                                ch_e "Well, I suppose you must be true to your nature. . ."
                                $ Line = "fail"

                        "Actually, let's stop that. It's creeping me out.":
                                $ EmmaX.FaceChange("perplexed", 2)
                                $ EmmaX.Statup("Love", 200, -10)
                                $ EmmaX.Statup("Obed", 200, -50)
                                $ EmmaX.Statup("Inbt", 50, -15)
                                ch_e "Well. We wouldn't want that now."
                                $ EmmaX.Blush = 1
                                $ Line = "embarrassed"

            "As if I care what you think, slut.":
                    $ EmmaX.FaceChange("angry", 1)
                    $ EmmaX.Statup("Love", 200, -20)
                    $ EmmaX.Statup("Obed", 200, 10)
                    $ EmmaX.Statup("Inbt", 50, -10)
                    menu:
                        ch_e "What was that?"
                        "Sorry. I just don't care what you want.":
                                if ApprovalCheck(EmmaX, 1400, "LO"):
                                        $ EmmaX.Statup("Obed", 200, 10)
                                        ch_e "That's. . ."
                                        $ EmmaX.FaceChange("sly", 1)
                                        $ EmmaX.Statup("Love", 200, 20)
                                        $ EmmaX.Statup("Inbt", 50, 15)
                                        ch_e ". . .not entirely off the mark."
                                else:
                                        $ EmmaX.Statup("Love", 200, -15)
                                        $ EmmaX.Statup("Obed", 200, -10)
                                        $ EmmaX.Statup("Inbt", 50, 5)
                                        $ EmmaX.FaceChange("angry", 1)
                                        ch_e "!!!"
                                        $ Line = "rude"

                        "Sorry. I'm just trying to do the \"control\" thing.  I thought you'd like it. Too much?":
                                $ EmmaX.Statup("Love", 200, 10)
                                $ EmmaX.Statup("Obed", 200, 10)
                                $ EmmaX.Statup("Inbt", 50, 5)
                                ch_e "You. . . may have a bit of work to do on that."

            "Not me.  It's kind of creepy.":
                        $ EmmaX.FaceChange("sad", 2)
                        $ EmmaX.Statup("Love", 200, -10)
                        $ EmmaX.Statup("Obed", 200, -20)
                        $ EmmaX.Statup("Inbt", 50, -25)
                        ch_e "Oh.  Well we wouldn't want that. . ."
                        $ Line = "embarrassed"

        $ EmmaX.History.append("master")
        if Line == "rude":
                $ EmmaX.RecentActions.append("angry")
                call Remove_Girl(EmmaX)
                $ renpy.pop_call()
                "[EmmaX.Name] storms out the door in a huff."
        elif Line == "embarrassed":
                call Remove_Girl(EmmaX)
                $ renpy.pop_call()
                "[EmmaX.Name] dashed out of the room, leaving you alone.  She looked really embarrassed."
        elif Line != "fail":
                $ EmmaX.Statup("Obed", 200, 50)
                $ EmmaX.Petnames.append("master")
                $ EmmaX.Petname = "master"
                ch_e ". . .master."
        return

label Emma_Sexfriend:   #Emma_Update
        $ EmmaX.DrainWord("asked meet")
        #set this to occur after class
        if EmmaX in Player.Harem:
                $ EmmaX.Petnames.append("sex friend")
                return
        $ EmmaX.Loc = bg_current
        call Set_The_Scene
        call CleartheRoom(EmmaX,1,1)
        $ EmmaX.DailyActions.append("relationship")
        call Taboo_Level
        $ Line = 0
        "After class, the students file out of the room."
        $ EmmaX.FaceChange("bemused", 1)
        ch_e "[Player.Name], could I have a word with you?" #blushing expression
        menu:
                extend ""
                "I'm in a hurry.":
                        $ EmmaX.FaceChange("angry", 1)
                        ch_e "That's. . . not an appropriate response." #Angry expression.  Loss of points
                        $ EmmaX.Statup("Love", 200, -20)
                        $ EmmaX.Statup("Obed", 50, 3)
                        $ Line = "rude"

                "This doesn't sound good.":
                        $ EmmaX.FaceChange("sly", 1)
                        ch_e "Settle down, it's nothing. . . unpleasant."

                "Yeah.  What's up?":
                        pass

        if not Line: #all this gets skipped if the "rude" response was procced above
                if ApprovalCheck(EmmaX, 850, "L"):
                        $ EmmaX.FaceChange("sly", 1)
                        ch_e "I just, enjoy spending time with you, as you're aware?"
                        menu:
                            extend ""
                            "I thought so.":
                                    $ EmmaX.FaceChange("sexy", 1)
                                    $ EmmaX.Statup("Love", 90, 10)
                                    $ EmmaX.Statup("Inbt", 80, 5)
                                    ch_e "I {i}was{/i} hoping you'd be aware, [EmmaX.Petname]."
                            "Really?":
                                    $ EmmaX.FaceChange("perplexed", 1)
                                    ch_e "Um, yes." #Blushing expression

                            "Don't complicate things.":
                                    $ EmmaX.FaceChange("angry", 1)
                                    $ EmmaX.Statup("Love", 200, -10)
                                    $ EmmaX.Statup("Obed", 50, 5)
                                    $ EmmaX.Statup("Inbt", 80, -5)
                                    ch_e "I'm sorry if you find this discussion too \"complicated.\""
                                    $ Line = "rude"
                elif ApprovalCheck(EmmaX, 1000, "LI"):
                        $ EmmaX.FaceChange("sexy", 1)
                        ch_e "I just thought you should know how. . . intriguing I find you."
                        menu:
                            extend ""
                            "That's really nice of you to say.":
                                    $ EmmaX.Statup("Love", 80, 5)
                                    $ EmmaX.Statup("Inbt", 80, 5)
                                    ch_e "Certainly." #Blushing expression
                            "Me?  You really think so?":
                                    ch_e "Don't be overly modest, [EmmaX.Petname]." #Blushing expression
                            "Are you going somewhere with this?":
                                    $ EmmaX.FaceChange("angry")
                                    ch_e "Perhaps not." #Angry expression.  Loss of points
                                    $ Line = "rude"
                else: #if it reaches this block, it's because it failed the "like" check above.
                        $ EmmaX.Mouth = "smile"
                        $ EmmaX.Brows = "sad"
                        $ EmmaX.Eyes = "side"
                        ch_e "This may sound a bit. . . unconventional."
                        menu:
                            extend ""
                            "Well, you've got me intrigued.  Now you {i}have{/i} to tell me.":
                                ch_e "You'll keep this between the two of us?"
                                menu:
                                    extend ""
                                    "[EmmaX.Name]. . . I really like you.  I promise.":
                                            $ EmmaX.FaceChange("smile")
                                            $ EmmaX.Statup("Love", 90, 10)
                                            $ EmmaX.Statup("Inbt", 80, 5)
                                            ch_e "Very well. . ."
                                    "Uhm. . . okay?":
                                            ch_e "Well. .  ."
                                    "No promises.":
                                            $ EmmaX.FaceChange("perplexed",2)
                                            $ EmmaX.Statup("Inbt", 80, -5)
                                            ch_e "Hmm. . . never mind, then."
                                            $ Line = "embarrassed"
                            "Uhm, I think I've had my fill of {i}weird{/i}, thanks":
                                            $ EmmaX.FaceChange("angry",1)
                                            ch_e "Live in suspense then."
                                            $ Line = "rude"

        if not Line:
                ch_e "I was considering. . . "
                ch_e "Perhaps we could take our relationship a little further, if you wanted to."
                menu:
                    extend ""
                    "You mean. . . like, being {i}friends with benefits{/i}?":
                            ch_e "I suppose you could put it that way."
                            ch_e "What do you think?" #Blushing expression
                            menu:
                                extend ""
                                "Sounds amazing!  Count me in.":
                                            $ EmmaX.FaceChange("smile",1)
                                            $ EmmaX.Statup("Love", 80, 10)
                                            $ EmmaX.Statup("Obed", 50, 10)
                                            $ EmmaX.Statup("Inbt", 200, 50)
                                            $ EmmaX.Statup("Lust", 200, 5)
                                            "[EmmaX.Name] leans in and gives you a passionate kiss."
                                            $ EmmaX.Kissed += 1
                                            ch_e "I can't wait to get started, [EmmaX.Petname]."
                                "That's pretty slutty, [EmmaX.Name].":
                                        if ApprovalCheck(EmmaX, 2000):
                                            $ EmmaX.FaceChange("angry",1,Brows="confused")
                                            $ EmmaX.Statup("Love", 200, -10)
                                            $ EmmaX.Statup("Obed", 50, 15)
                                            ch_e "I suppose you're not wrong."
                                        else:
                                            $ EmmaX.FaceChange("angry",1)
                                            $ EmmaX.Statup("Love", 200, -30)
                                            $ EmmaX.Statup("Obed", 50, 10)
                                            $ EmmaX.Statup("Inbt", 80, -20)
                                            ch_e "Then I suppose I'll have to take care of that elsewhere!"
                                            $ Line = "rude"
                    "Uhm, to be honest, I'd rather not.":
                                            $ EmmaX.FaceChange("sadside",2)
                                            $ EmmaX.Statup("Obed", 50, 15)
                                            $ EmmaX.Statup("Inbt", 80, -15)
                                            ch_e "Oh. Suit yourself, I suppose."
                                            ch_e "I should be leaving."
                                            $ Line = "sad"

        if Line == "rude":
                $ EmmaX.FaceChange("angry",1)
                $ EmmaX.RecentActions.append("angry")
                $ EmmaX.Statup("Love", 200, -20)
                $ EmmaX.Statup("Obed", 50, 5)
                $ EmmaX.Statup("Inbt", 80, -10)
                hide Emma_Sprite with easeoutright
                $ EmmaX.RecentActions.append("angry")
                "[EmmaX.Name] storms off in a huff.  She seemed pretty mad at you."
        elif Line == "embarrassed":
                $ EmmaX.FaceChange("perplexed",1)
                $ EmmaX.Statup("Love", 200, -10)
                $ EmmaX.Statup("Obed", 50, 5)
                $ EmmaX.Statup("Inbt", 80, -20)
                hide Emma_Sprite with easeoutright
                "[EmmaX.Name] dashes out of the room, leaving you alone.  That was very strange."
        elif Line == "sad":
                hide Emma_Sprite with easeoutbottom
                "[EmmaX.Name] wanders into the hall, leaving you alone.  You think you may have hurt her feelings."
        else: #if you kept Line unused throughout, then you passed all the checks, so. . .
                $ EmmaX.Petnames.append("sex friend")
                $ EmmaX.FaceChange("sly",2)
                $ EmmaX.Statup("Inbt", 80, 10)
                $ EmmaX.Statup("Lust", 80, 10)
                "[EmmaX.Name] leans in and carresses your body."
                "As she does so, you feel a tickle as if her mouth is surrounding your cock."
                "You look back at her and she winks."
                ch_e "I do have a few tricks up my sleeves, [EmmaX.Petname]."
                ch_e "I'll see you later, I hope."
                hide Emma_Sprite with easeoutright
                "She leaves the room, and the phantom \"lips\" give you one final kiss. "
        call Remove_Girl(EmmaX)
        return

label Emma_Fuckbuddy:   #Emma_Update
        $ EmmaX.DrainWord("asked meet")
        $ EmmaX.DailyActions.append("relationship")
        "Out of nowhere, you feel a tongue sliding across your cock."
        "Even though you're fully dressed, it definitely feels like a mouth has enveloped your cock."
        "You look down, but can't see any movement, although your cock has become diamond hard."
        "As you try to control your obvious erection, a voice tickles the back of your mind,"
        ch_e "To me, my X-Man. . ."
        "-and suddenly the pressure is gone."
        "Looking around, you don't see anyone nearby, and it doesn't look like anyone else noticed what happened."
        "Maybe you'll check up on [EmmaX.Name] later. . ."
        $ EmmaX.Petnames.append("fuck buddy")
        $ EmmaX.Event[10] += 1
        return
