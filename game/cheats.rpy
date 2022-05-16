label StatHacks(Girl=0,counter=0):
    while True:
            menu:
                "[Girl.name]: love: [Girl.love], obedience: [Girl.obedience], Inhibition:[Girl.inhibition], lust: [Girl.lust] Taboo: [Taboo], Location: [Girl.location]"
                "Activities":
                    menu:
                        "Recent Actions":
                            "[Girl.recent_history]"
                        "Daily Actions":
                            "[Girl.daily_history]"
                        "Traits":
                            "[Girl.Traits]"
                        "History":
                            "[Girl.History]"
                "Gwen's face" if False:
                    call Gwen_FaceEditor
                "Raise love":
                    $ Girl.love += 100
                "Lower love":
                    $ Girl.love -= 100
                "Raise obedience":
                    $ Girl.obedience += 100
                "Lower obedience":
                    $ Girl.obedience -= 100
                "Raise Inhibitions":
                    $ Girl.inhibition += 100
                "Lower Inhibitions":
                    $ Girl.inhibition -= 100
                "Taboo toggle":
                    $ Taboo = 40 if Taboo != 40 else 0
                    "[Taboo]"
                "Small":
                    $ counter = 1
                    while counter:
                        menu:
                            "Raise love":
                                $ Girl.love += 10
                            "Lower love":
                                $ Girl.love -= 10
                            "Raise obedience":
                                $ Girl.obedience += 10
                            "Lower obedience":
                                $ Girl.obedience -= 10
                            "Raise Inhibitions":
                                $ Girl.inhibition += 10
                            "Lower Inhibitions":
                                $ Girl.inhibition -= 10
                            "Back":
                                $ counter = 0
                "Other":
                    menu:
                        "Raise lust":
                            $ Girl.lust += 10
                        "Lower lust":
                            $ Girl.lust -= 10
                        "Raise Addiction":
                            $ Girl.Addict += 10
                        "Lower Addiction":
                            $ Girl.Addict -= 10
                        "Back":
                            pass
                "Wardrobe":
                    call WardrobeEditor(Girl)

                "Return":
                    call checkout
                    return

label Cheat_Menu(Girl=0):
        if Girl not in all_Girls:
                $ Girl = focused_Girl
        menu:
            "Level-Up":
                $ Girl.action_counter["handjob"] += 5
                $ Girl.action_counter["blowjob"] += 5
                $ Girl.event_counter["swallowed"] += 5
                $ Girl.action_counter["handjob"] += 5
                $ Girl.event_counter["ass_slapped"] += 5
                $ Girl.action_counter["titjob"] += 5
                $ Girl.action_counter["sex"] += 5
                $ Girl.action_counter["anal"] += 5
                $ Girl.action_counter["hotdog"] += 5
                $ Girl.action_counter["masturbation"] += 5
                $ Girl.event_counter["orgasm"] += 5
                $ Girl.action_counter["fondle_breasts"] += 5
                $ Girl.action_counter["fondle_thighs"] += 5
                $ Girl.action_counter["fondle_pussy"] += 5
                $ Girl.action_counter["fondle_ass"] += 5
                $ Girl.action_counter["dildo_pussy"] += 5
                $ Girl.action_counter["dildo_ass"] += 5
                $ Girl.Plug += 5
                $ Girl.action_counter["suck_breasts"] += 5
                $ Girl.action_counter["finger_pussy"] += 5
                $ Girl.action_counter["finger_ass"] += 5
                $ Girl.action_counter["eat_pussy"] += 5
                $ Girl.action_counter["eat_ass"] += 5
                $ Girl.action_counter["blowjob"] += 5
                $ Girl.event_counter["swallowed"] += 5
                $ Girl.event_counter["creampied"] += 5
                $ Girl.event_counter["anal_creampied"] += 5
                $ Girl.SeenChest = 1
                $ Girl.SeenPanties = 1
                $ Girl.SeenPussy = 1
            "Level Reset":
                $ Girl.action_counter["handjob"] = 0
                $ Girl.action_counter["blowjob"] = 0
                $ Girl.event_counter["swallowed"] = 0
            "Toggle Taboo":
                if not Taboo:
                    $ Taboo = 40
                else:
                    $ Taboo = 0
            "Maxed":
                    $ Girl.love = 1000
                    $ Girl.inhibition = 1000
                    $ Girl.obedience = 1000
                    $ Girl.lust = 50
                    $ Girl.Addict = 0 #how addicted she is
                    $ Girl.Addictionrate = 0 #How faster her addiciton rises
                    $ Girl.action_counter["kiss"] = 1 #How many times they've kissed
                    $ Girl.event_counter["swallowed"] = 0
            "50\%":
                    $ Girl.love = 500
                    $ Girl.inhibition = 500
                    $ Girl.obedience = 500
                    $ Girl.lust = 65
                    $ Girl.Addict = 0 #how addicted she is
                    $ Girl.Addictionrate = 10 #How faster her addiciton rises
                    $ Girl.action_counter["kiss"] = 10 #How many times they've kissed
                    $ Girl.event_counter["swallowed"] = 0
            "25\%":
                    $ Girl.love = 250
                    $ Girl.inhibition = 250
                    $ Girl.obedience = 250
                    $ Girl.lust = 85
                    $ Girl.Addict = 10 #how addicted she is
                    $ Girl.Addictionrate = 50 #How faster her addiciton rises
                    $ Girl.action_counter["kiss"] = 10 #How many times they've kissed
                    $ Girl.event_counter["swallowed"] = 0
            "Juice up":
                    $ Player.Semen += 5
                    $ Girl.Action = 10
            "Cold Shower":
                    $ Player.Focus = 0
            "Exit":
                return
        jump Cheat_Menu
