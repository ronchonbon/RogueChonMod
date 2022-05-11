label StatHacks(Chr=0,Cnt=0):
    while True:
            menu:
                "[Chr.Name]: Love: [Chr.Love], Obedience: [Chr.Obed], Inhibition:[Chr.Inbt], Lust: [Chr.Lust] Taboo: [Taboo], Location: [Chr.Loc]"
                "Activities":
                    menu:
                        "Recent Actions":
                            "[Chr.RecentActions]"
                        "Daily Actions":
                            "[Chr.DailyActions]"
                        "Traits":
                            "[Chr.Traits]"
                        "History":
                            "[Chr.History]"
                "Gwen's face" if False:
                    call Gwen_FaceEditor
                "Raise Love":
                    $ Chr.Love += 100
                "Lower Love":
                    $ Chr.Love -= 100
                "Raise Obedience":
                    $ Chr.Obed += 100
                "Lower Obedience":
                    $ Chr.Obed -= 100
                "Raise Inhibitions":
                    $ Chr.Inbt += 100
                "Lower Inhibitions":
                    $ Chr.Inbt -= 100
                "Taboo toggle":
                    $ Taboo = 40 if Taboo != 40 else 0
                    "[Taboo]"
                "Small":
                    $ Cnt = 1
                    while Cnt:
                        menu:
                            "Raise Love":
                                $ Chr.Love += 10
                            "Lower Love":
                                $ Chr.Love -= 10
                            "Raise Obedience":
                                $ Chr.Obed += 10
                            "Lower Obedience":
                                $ Chr.Obed -= 10
                            "Raise Inhibitions":
                                $ Chr.Inbt += 10
                            "Lower Inhibitions":
                                $ Chr.Inbt -= 10
                            "Back":
                                $ Cnt = 0
                "Other":
                    menu:
                        "Raise Lust":
                            $ Chr.Lust += 10
                        "Lower Lust":
                            $ Chr.Lust -= 10
                        "Raise Addiction":
                            $ Chr.Addict += 10
                        "Lower Addiction":
                            $ Chr.Addict -= 10
                        "Back":
                            pass
                "Wardrobe":
                    call WardrobeEditor(Chr)

                "Return":
                    call Checkout
                    return


label Cheat_Menu(Girl=0):
        if Girl not in TotalGirls:
                $ Girl = Ch_Focus
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
                    $ Girl.Love = 1000
                    $ Girl.Inbt = 1000
                    $ Girl.Obed = 1000
                    $ Girl.Lust = 50
                    $ Girl.Addict = 0 #how addicted she is
                    $ Girl.Addictionrate = 0 #How faster her addiciton rises
                    $ Girl.Kissed = 1 #How many times they've kissed
                    $ Girl.Swallow = 0
            "50\%":
                    $ Girl.Love = 500
                    $ Girl.Inbt = 500
                    $ Girl.Obed = 500
                    $ Girl.Lust = 65
                    $ Girl.Addict = 0 #how addicted she is
                    $ Girl.Addictionrate = 10 #How faster her addiciton rises
                    $ Girl.Kissed = 10 #How many times they've kissed
                    $ Girl.Swallow = 0
            "25\%":
                    $ Girl.Love = 250
                    $ Girl.Inbt = 250
                    $ Girl.Obed = 250
                    $ Girl.Lust = 85
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
