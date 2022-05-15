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
                $ Girl.Hand += 5
                $ Girl.Blow += 5
                $ Girl.Swallow += 5
                $ Girl.Hand += 5
                $ Girl.Slap += 5
                $ Girl.Tit += 5
                $ Girl.Sex += 5
                $ Girl.Anal += 5
                $ Girl.Hotdog += 5
                $ Girl.Mast += 5
                $ Girl.Org += 5
                $ Girl.FondleB += 5
                $ Girl.FondleT += 5
                $ Girl.FondleP += 5
                $ Girl.FondleA += 5
                $ Girl.DildoP += 5
                $ Girl.DildoA += 5
                $ Girl.Plug += 5
                $ Girl.SuckB += 5
                $ Girl.InsertP += 5
                $ Girl.InsertA += 5
                $ Girl.LickP += 5
                $ Girl.LickA += 5
                $ Girl.Blow += 5
                $ Girl.Swallow += 5
                $ Girl.CreamP += 5
                $ Girl.CreamA += 5
                $ Girl.SeenChest = 1
                $ Girl.SeenPanties = 1
                $ Girl.SeenPussy = 1
                "Hand [Girl.Hand], Blow [Girl.Blow], Swallow [Girl.Swallow]"
            "Level Reset":
                $ Girl.Hand = 0
                $ Girl.Blow = 0
                $ Girl.Swallow = 0
                "Hand [Girl.Hand], Blow [Girl.Blow], Swallow [Girl.Swallow]"
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
                    $ Girl.Kissed = 1 #How many times they've kissed
                    $ Girl.Swallow = 0
            "50\%":
                    $ Girl.love = 500
                    $ Girl.inhibition = 500
                    $ Girl.obedience = 500
                    $ Girl.lust = 65
                    $ Girl.Addict = 0 #how addicted she is
                    $ Girl.Addictionrate = 10 #How faster her addiciton rises
                    $ Girl.Kissed = 10 #How many times they've kissed
                    $ Girl.Swallow = 0
            "25\%":
                    $ Girl.love = 250
                    $ Girl.inhibition = 250
                    $ Girl.obedience = 250
                    $ Girl.lust = 85
                    $ Girl.Addict = 10 #how addicted she is
                    $ Girl.Addictionrate = 50 #How faster her addiciton rises
                    $ Girl.Kissed = 10 #How many times they've kissed
                    $ Girl.Swallow = 0
            "Juice up":
                    $ Player.Semen += 5
                    $ Girl.Action = 10
            "Cold Shower":
                    $ Player.Focus = 0
            "Exit":
                return
        jump Cheat_Menu
