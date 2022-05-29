
image Jean_sprite doggy:
    LiveComposite(

        (420,750),
        (0,0), ConditionSwitch(

            "not Player.sprite", "Jean_Doggy_Body",
            "Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Jean_Doggy_Fuck2_Top",
                    "action_speed > 1", "Jean_Doggy_Fuck_Top",
                    "action_speed", "Jean_Doggy_Anal_Head_Top",
                    "True", "Jean_Doggy_Body",
                    ),
            "Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Jean_Doggy_Fuck2_Top",
                    "action_speed > 1", "Jean_Doggy_Fuck_Top",
                    "True", "Jean_Doggy_Body",
                    ),
            "True", "Jean_Doggy_Body",
            ),
        (0,0), ConditionSwitch(

            "not Player.sprite", "Jean_Doggy_Ass",
            "Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Jean_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Jean_Doggy_Fuck_Ass",
                    "action_speed", "Jean_Doggy_Anal_Head_Ass",
                    "True", "Jean_Doggy_Ass",
                    ),
            "Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Jean_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Jean_Doggy_Fuck_Ass",
                    "True", "Jean_Doggy_Ass",
                    ),
            "True", "Jean_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(

            "Player.cock_position == 'footjob'", ConditionSwitch(
                    "action_speed > 1", "Jean_Doggy_Feet2",
                    "action_speed", "Jean_Doggy_Feet1",
                    "True", "Jean_Doggy_Feet0",
                    ),
            "not Player.sprite and show_feet", "Jean_Doggy_Feet0",
            "True", Null(),
            ),
        )
    align (0.6,0.0)
    yoffset 50


image Jean_Doggy_Body:
    LiveComposite(

        (420,750),
        (165,0),"Jean_Doggy_Hair_Under",
        (0,0), ConditionSwitch(

            "JeanX.outfit['bra'] == '_corset' and JeanX.top_pulled_up", "images/JeanDoggy/Jean_Doggy_Chest_Corset_Back.png",
            "True", Null(),
            ),
        (165,0), "Jean_Doggy_Head",

        (0,0), "images/JeanDoggy/Jean_Doggy_Body.png",
        (0,0), ConditionSwitch(

            "not JeanX.outfit['bra']", Null(),
            "JeanX.top_pulled_up", ConditionSwitch(
                    "JeanX.outfit['bra'] == '_lace_bra' and JeanX.outfit['top']", "images/JeanDoggy/Jean_Doggy_Chest_GreenBra_Up2.png",
                    "JeanX.outfit['bra'] == '_lace_bra'", "images/JeanDoggy/Jean_Doggy_Chest_GreenBra_Up.png",
                    "JeanX.outfit['bra'] == '_corset'", "images/JeanDoggy/Jean_Doggy_Chest_Corset_Up.png",
                    "JeanX.outfit['bra'] == '_sports_bra'", "images/JeanDoggy/Jean_Doggy_Chest_SportsBra_Up.png",
                    "JeanX.outfit['bra'] == '_bikini_top'", "images/JeanDoggy/Jean_Doggy_Chest_Bikini_Up.png",
                    "JeanX.outfit['top']", "images/JeanDoggy/Jean_Doggy_Chest_GreenBra_Up2.png",
                    "True", "images/JeanDoggy/Jean_Doggy_Chest_GreenBra_Up.png",
                    ),
            "JeanX.outfit['bra'] == '_lace_bra'", "images/JeanDoggy/Jean_Doggy_Chest_LaceBra.png",
            "JeanX.outfit['bra'] == '_corset'", "images/JeanDoggy/Jean_Doggy_Chest_Corset.png",
            "JeanX.outfit['bra'] == '_sports_bra'", "images/JeanDoggy/Jean_Doggy_Chest_SportsBra.png",
            "JeanX.outfit['bra'] == '_bikini_top'", "images/JeanDoggy/Jean_Doggy_Chest_Bikini.png",
            "True", "images/JeanDoggy/Jean_Doggy_Chest_GreenBra.png",
            ),





        (0,0), ConditionSwitch(

            "not JeanX.outfit['top']", Null(),
            "JeanX.outfit['top'] == '_yellow_shirt' and JeanX.top_pulled_up", "images/JeanDoggy/Jean_Doggy_Over_Tank_Up.png",
            "JeanX.outfit['top'] == '_yellow_shirt'", "images/JeanDoggy/Jean_Doggy_Over_Tank.png",
            "JeanX.outfit['top'] == '_green_shirt' and JeanX.top_pulled_up", "images/JeanDoggy/Jean_Doggy_Over_GreenShirt_Up.png",
            "JeanX.outfit['top'] == '_green_shirt'", "images/JeanDoggy/Jean_Doggy_Over_GreenShirt.png",
            "JeanX.outfit['top'] == '_pink_shirt' and JeanX.top_pulled_up", "images/JeanDoggy/Jean_Doggy_Over_PinkShirt_Up.png",
            "JeanX.outfit['top'] == '_pink_shirt'", "images/JeanDoggy/Jean_Doggy_Over_PinkShirt.png",
            "JeanX.outfit['top'] == '_towel' and not JeanX.top_pulled_up", "images/JeanDoggy/Jean_Doggy_Over_TowelTop.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JeanX.outfit['bottom'] or JeanX.upskirt", Null(),
            "JeanX.outfit['front_outer_accessory'] == '_suspenders' or JeanX.outfit['front_outer_accessory'] == '_suspenders2'", "images/JeanDoggy/Jean_Doggy_Suspenders.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "JeanX.spunk['back']", "images/JeanDoggy/Jean_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'fondle_breasts' or offhand_action == 'fondle_breasts'", "Jean_Doggy_GropeBreast",
            "True", Null()
            ),

        (165,0),"Jean_Doggy_Hair_Over",
        (0,0), "images/JeanDoggy/Jean_Doggy_Hand.png",
        )


    offset (-190,-40)




image Jean_Doggy_Head:
    LiveComposite(

        (420,750),


        (0,0), ConditionSwitch(

            "JeanX.blushing == '_blush2'", "images/JeanDoggy/Jean_Doggy_Head_Blush2.png",
            "JeanX.blushing", "images/JeanDoggy/Jean_Doggy_Head_Blush1.png",
            "True", "images/JeanDoggy/Jean_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(

            "JeanX.mouth == '_normal'", "images/JeanDoggy/Jean_Doggy_mouth_Normal.png",
            "JeanX.mouth == '_lipbite'", "images/JeanDoggy/Jean_Doggy_mouth_Smile.png",
            "JeanX.mouth == '_sucking'", "images/JeanDoggy/Jean_Doggy_mouth_Tongue.png",
            "JeanX.mouth == '_kiss'", "images/JeanDoggy/Jean_Doggy_mouth_Normal.png",
            "JeanX.mouth == '_sad'", "images/JeanDoggy/Jean_Doggy_mouth_Sad.png",
            "JeanX.mouth == '_smile'", "images/JeanDoggy/Jean_Doggy_mouth_Smile.png",
            "JeanX.mouth == '_smile'", "images/JeanDoggy/Jean_Doggy_mouth_Smile.png",
            "JeanX.mouth == '_surprised'", "images/JeanDoggy/Jean_Doggy_mouth_Open.png",
            "JeanX.mouth == '_tongue'", "images/JeanDoggy/Jean_Doggy_mouth_Tongue.png",
            "True", "images/JeanDoggy/Jean_Doggy_mouth_Smile.png",
            ),
        (0,0), ConditionSwitch(

            "JeanX.spunk['chin']", "images/JeanDoggy/Jean_Doggy_Spunk_Chin.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JeanX.spunk['mouth']", Null(),


            "JeanX.mouth == '_lipbite'", "images/JeanDoggy/Jean_Doggy_Spunk_Smile.png",
            "JeanX.mouth == '_smile'", "images/JeanDoggy/Jean_Doggy_Spunk_Smile.png",
            "JeanX.mouth == '_smile'", "images/JeanDoggy/Jean_Doggy_Spunk_Smile.png",
            "JeanX.mouth == '_sucking'", "images/JeanDoggy/Jean_Doggy_Spunk_Open.png",

            "JeanX.mouth == '_surprised'", "images/JeanDoggy/Jean_Doggy_Spunk_Open.png",
            "JeanX.mouth == '_tongue'", "images/JeanDoggy/Jean_Doggy_Spunk_Open.png",
            "True", "images/JeanDoggy/Jean_Doggy_Spunk_Normal.png",
            ),
        (0,0), ConditionSwitch(


            "JeanX.brows == '_angry'", "images/JeanDoggy/Jean_Doggy_brows_Angry.png",
            "JeanX.brows == '_sad'", "images/JeanDoggy/Jean_Doggy_brows_Sad.png",
            "JeanX.brows == '_surprised'", "images/JeanDoggy/Jean_Doggy_brows_Surprised.png",

            "True", "images/JeanDoggy/Jean_Doggy_brows_Normal.png",
            ),
        (0,0), "Jean_sprite Doggy Blink",
        (0,0), ConditionSwitch(

            "JeanX.wet or JeanX.outfit['hair'] == '_wet'", "images/JeanDoggy/Jean_Doggy_Hair_Wet_Under.png",
            "True", Null(),
            ),




















        )
    zoom 0.9


image Jean_Doggy_Hair_Under:

    ConditionSwitch(
                "JeanX.wet or JeanX.outfit['hair'] == '_wet'", "images/JeanDoggy/Jean_Doggy_Hair_Wet_Under.png",
                "JeanX.outfit['hair'] == 'pony'", Null(),
                "True", "images/JeanDoggy/Jean_Doggy_Hair_Short_Under.png",
                )
    zoom .9

image Jean_Doggy_Hair_Over:

    contains:
        ConditionSwitch(
                    "JeanX.wet or JeanX.outfit['hair'] == '_wet'", "images/JeanDoggy/Jean_Doggy_Hair_Wet_Over.png",
                    "JeanX.outfit['hair'] == 'pony'", "images/JeanDoggy/Jean_Doggy_Hair_Pony_Over.png",
                    "True", "images/JeanDoggy/Jean_Doggy_Hair_Short_Over.png",
                    )
    contains:
        ConditionSwitch(

                "JeanX.spunk['face']", "images/JeanDoggy/Jean_Doggy_Spunk_Facial.png",
                "True", Null(),
                )
    contains:
        ConditionSwitch(

                "JeanX.spunk['hair']", "images/JeanDoggy/Jean_Doggy_Spunk_Facial2.png",
                "True", Null(),
                )
    zoom .9


image Jean_sprite Doggy Blink:

    ConditionSwitch(
        "JeanX.eyes == '_sexy'", "images/JeanDoggy/Jean_Doggy_eyes_Sexy.png",
        "JeanX.eyes == '_side'", "images/JeanDoggy/Jean_Doggy_eyes_Normal.png",
        "JeanX.eyes == '_normal'", "images/JeanDoggy/Jean_Doggy_eyes_Normal.png",
        "JeanX.eyes == '_closed'", "images/JeanDoggy/Jean_Doggy_eyes_Closed.png",
        "JeanX.eyes == '_manic'", "images/JeanDoggy/Jean_Doggy_eyes_Surprised.png",
        "JeanX.eyes == '_down'", "images/JeanDoggy/Jean_Doggy_eyes_Sexy.png",
        "JeanX.eyes == '_stunned'", "images/JeanDoggy/Jean_Doggy_eyes_Stunned.png",
        "JeanX.eyes == '_surprised'", "images/JeanDoggy/Jean_Doggy_eyes_Surprised.png",
        "JeanX.eyes == '_squint'", "images/JeanDoggy/Jean_Doggy_eyes_Sexy.png",
        "True", "images/JeanDoggy/Jean_Doggy_eyes_Normal.png",
        ),






    3

    "images/JeanDoggy/Jean_Doggy_eyes_Closed.png"
    .25
    repeat

image Jean_Doggy_Ass:
    LiveComposite(

        (420,750),
        (0,0), ConditionSwitch(

            "JeanX.outfit['bottom'] == '_skirt'","images/JeanDoggy/Jean_Doggy_Legs_Skirt_Back.png",
            "not JeanX.upskirt", Null(),
            "JeanX.outfit['bottom'] == '_shorts'", "images/JeanDoggy/Jean_Doggy_Legs_Shorts_Back.png",
            "JeanX.outfit['bottom'] == '_pants'", "images/JeanDoggy/Jean_Doggy_Legs_Pants_Back.png",
            "JeanX.outfit['bottom'] == '_yoga_pants'", "images/JeanDoggy/Jean_Doggy_Legs_Yoga_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JeanX.underwear_pulled_down or (JeanX.outfit['bottom'] == '_pants' and not JeanX.upskirt)", Null(),
            "JeanX.outfit['underwear'] == '_green_panties'", "images/JeanDoggy/Jean_Doggy_Panties_Green_Back.png",
            "JeanX.outfit['underwear'] == '_bikini_bottoms'", Null(),
            "JeanX.outfit['underwear']", "images/JeanDoggy/Jean_Doggy_Panties_Green_Back.png",
            "True", Null(),
            ),
        (0,0), "images/JeanDoggy/Jean_Doggy_Ass.png",
        (0,0), ConditionSwitch(

            "JeanX.wet", "images/RogueDoggy/Rogue_Doggy_WetAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "JeanX.outfit['hose'] == '_stockings'", "images/JeanDoggy/Jean_Doggy_Hose_Stocking.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JeanX.underwear_pulled_down or (JeanX.outfit['bottom'] == '_pants' and not JeanX.upskirt)", Null(),
            "JeanX.outfit['underwear'] == '_green_panties'", "images/JeanDoggy/Jean_Doggy_Panties_Green_Down.png",
            "JeanX.outfit['underwear'] == '_bikini_bottoms'", Null(),
            "JeanX.outfit['underwear']", "images/JeanDoggy/Jean_Doggy_Panties_Green_Down.png",
            "True", Null(),
            ),


        (0,0), ConditionSwitch(

            "Player.sprite and Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Jean_Pussy_Fucking3",
                    "action_speed > 1", "Jean_Pussy_Fucking2",
                    "action_speed", "Jean_Pussy_Heading",
                    "True", "Jean_Pussy_animation0",
                    ),
            "primary_action == 'eat_pussy'", "images/JeanDoggy/Jean_Doggy_Pussy_Open.png",
            "JeanX.outfit['bottom'] and not JeanX.upskirt", "images/JeanDoggy/Jean_Doggy_Pussy_Closed.png",
            "JeanX.outfit['underwear'] and not JeanX.underwear_pulled_down", "images/JeanDoggy/Jean_Doggy_Pussy_Closed.png",
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'", "Jean_Pussy_Fingering",
            "primary_action == 'dildo pussy'", "Jean_Pussy_Fucking2",
            "True", "images/JeanDoggy/Jean_Doggy_Pussy_Closed.png",
            ),


        (0,0), ConditionSwitch(

            "JeanX.spunk['pussy'] and Player.cock_position == 'in'",Null(),
            "JeanX.spunk['pussy'] ", "images/JeanDoggy/Jean_Doggy_SpunkPussyClosed.png",
            "JeanX.grool and Player.cock_position == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "JeanX.grool", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JeanX.pubes", Null(),
            "Player.sprite and Player.cock_position == 'in'", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo pussy'", Null(),
            "JeanX.outfit['bottom'] == '_pants' and not JeanX.upskirt", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",
            "JeanX.underwear_pulled_down and primary_action == 'eat_pussy'", "images/JeanDoggy/Jean_Doggy_Pubes_Open.png",
            "JeanX.underwear_pulled_down", "images/JeanDoggy/Jean_Doggy_Pubes.png",
            "JeanX.outfit['underwear']", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",
            "JeanX.outfit['hose'] and JeanX.outfit['hose'] != '_stockings'", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",
            "primary_action == 'eat_pussy'", "images/JeanDoggy/Jean_Doggy_Pubes_Open.png",
            "True", "images/JeanDoggy/Jean_Doggy_Pubes.png",
            ),
        (0,0), ConditionSwitch(

            "Player.sprite", Null(),
            "JeanX.outfit['front_inner_accessory'] == '_ring'", "images/JeanDoggy/Jean_Doggy_PussyRing.png",
            "JeanX.outfit['front_inner_accessory'] == '_barbell'", "images/JeanDoggy/Jean_Doggy_PussyBarbell.png",
            "True", Null(),
            ),


        (0,0), ConditionSwitch(

            "Player.sprite and Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Jean_Anal_Fucking2",
                    "action_speed > 1", "Jean_Anal_Fucking",
                    "action_speed", "Jean_Anal_Heading",
                    "True", "Jean_Anal",
                    ),


            "JeanX.outfit['bottom'] and not JeanX.upskirt", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "JeanX.outfit['underwear'] and not JeanX.underwear_pulled_down", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "primary_action == 'finger_ass' or offhand_action == 'finger_ass'", "Jean_Anal_Fingering",
            "primary_action == 'dildo anal'", "Jean_Anal_Fucking",
            "JeanX.used_to_anal", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "True", "images/JeanDoggy/Jean_Doggy_Asshole_Tight.png",
            ),


        (0,0), ConditionSwitch(

            "not JeanX.spunk['anus'] or Player.sprite", Null(),
            "Player.cock_position == 'anal'", "images/JeanDoggy/Jean_Doggy_SpunkAnalOpen.png",
            "JeanX.used_to_anal", "images/JeanDoggy/Jean_Doggy_SpunkAnalLoose.png",
            "True", "images/JeanDoggy/Jean_Doggy_SpunkAnalLoose.png",
            ),
        (0,0), ConditionSwitch(

            "JeanX.underwear_pulled_down or not JeanX.outfit['underwear']", Null(),
            "Player.sprite and (Player.cock_position == 'in' or Player.cock_position == 'anal')", Null(),


            "JeanX.outfit['underwear'] == '_green_panties' and JeanX.grool", "images/JeanDoggy/Jean_Doggy_Panties_Green_Wet.png",
            "JeanX.outfit['underwear'] == '_green_panties'", "images/JeanDoggy/Jean_Doggy_Panties_Green.png",
            "JeanX.outfit['underwear'] == '_lace_panties'", "images/JeanDoggy/Jean_Doggy_Panties_Lace.png",
            "JeanX.outfit['underwear'] == '_bikini_bottoms' and JeanX.grool", "images/JeanDoggy/Jean_Doggy_Panties_Bikini_Wet.png",
            "JeanX.outfit['underwear'] == '_bikini_bottoms'", "images/JeanDoggy/Jean_Doggy_Panties_Bikini.png",
            "True", "images/JeanDoggy/Jean_Doggy_Panties_Green.png",
            ),
        (0,0), ConditionSwitch(

            "Player.sprite and (Player.cock_position == 'in' or Player.cock_position == 'anal')", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo pussy'", Null(),

            "JeanX.outfit['hose'] == '_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.outfit['underwear'] and JeanX.underwear_pulled_down", Null(),


            "JeanX.outfit['hose'] == '_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full.png",
            "JeanX.outfit['hose'] == '_ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "JeanX.outfit['bottom'] == '_pants'", ConditionSwitch(
                    "JeanX.upskirt", "images/JeanDoggy/Jean_Doggy_Legs_Pants_Down.png",
                    "JeanX.grool > 1", "images/JeanDoggy/Jean_Doggy_Legs_Pants_Wet.png",
                    "True", "images/JeanDoggy/Jean_Doggy_Legs_Pants.png",
                    ),
            "JeanX.outfit['bottom'] == '_yoga_pants'", ConditionSwitch(
                    "JeanX.upskirt", "images/JeanDoggy/Jean_Doggy_Legs_Yoga_Down.png",
                    "JeanX.grool > 1", "images/JeanDoggy/Jean_Doggy_Legs_Yoga_Wet.png",
                    "True", "images/JeanDoggy/Jean_Doggy_Legs_Yoga.png",
                    ),
            "JeanX.outfit['bottom'] == '_shorts'", ConditionSwitch(
                    "JeanX.upskirt", "images/JeanDoggy/Jean_Doggy_Legs_Shorts_Down.png",
                    "JeanX.grool > 1", "images/JeanDoggy/Jean_Doggy_Legs_Shorts_Wet.png",
                    "True", "images/JeanDoggy/Jean_Doggy_Legs_Shorts.png",
                    ),
            "JeanX.outfit['bottom'] == '_skirt'", ConditionSwitch(
                    "JeanX.upskirt and Player.sprite and Player.cock_position == 'anal' and action_speed" , "images/JeanDoggy/Jean_Doggy_Legs_Skirt_Up.png",
                    "JeanX.upskirt", "images/JeanDoggy/Jean_Doggy_Legs_Skirt_Up.png",
                    "True", "images/JeanDoggy/Jean_Doggy_Legs_Skirt.png",
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "JeanX.outfit['top'] == '_towel' and JeanX.upskirt", "images/JeanDoggy/Jean_Doggy_Over_TowelAss_Up.png",
            "JeanX.outfit['top'] == '_towel'", "images/JeanDoggy/Jean_Doggy_Over_TowelAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "JeanX.spunk['back']", "images/JeanDoggy/Jean_Doggy_SpunkAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "Player.sprite and Player.cock_position", Null(),
            "primary_action == 'eat_pussy'", "Rogue_Doggy_Lick_Pussy",
            "primary_action == 'eat_ass'", "Rogue_Doggy_Lick_Ass",
            "True", Null()
            ),
        (0,0), ConditionSwitch(

            "not Player.sprite or Player.cock_position != 'out'", Null(),
            "JeanX.outfit['bottom'] == '_skirt' and JeanX.upskirt", "images/JeanDoggy/Jean_Doggy_Hotdog_Upskirt_Back.png",
            "True", "images/JeanDoggy/Jean_Doggy_HotdogBack.png",
            ),
        (0,0), ConditionSwitch(

            "not Player.sprite or Player.cock_position != 'out'", Null(),


            "action_speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            "True", AlphaMask("Zero_Hotdog_animation0", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            ),






        )


image Jean_Doggy_Feet:
    contains:
        AlphaMask("Jean_Doggy_Shins", "images/JeanDoggy/Jean_Doggy_Feet_Toes.png")

image Jean_Doggy_Shins:



    contains:

        ConditionSwitch(
            "JeanX.outfit['hose'] == '_stockings'", "images/JeanDoggy/Jean_Doggy_Feet_HoseBack.png",
            "JeanX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Feet_HoseBack.png",
            "JeanX.outfit['hose'] == '_pantyhose'", "images/JeanDoggy/Jean_Doggy_Feet_HoseBack.png",
            "JeanX.outfit['hose'] == '_ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Feet_HoseBack_Holed.png",
            "True", "images/JeanDoggy/Jean_Doggy_Feet_Legs.png"
            )
    contains:


        ConditionSwitch(
            "JeanX.outfit['bottom'] == '_pants'", "images/JeanDoggy/Jean_Doggy_Feet_Pants.png",
            "JeanX.outfit['bottom'] == '_yoga_pants'", "images/JeanDoggy/Jean_Doggy_Feet_Yoga.png",
            "True", Null(),
            )
























image Jean_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom .55
        offset (280,380)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10
            ease 1 rotate 0
            repeat

















image Zero_Jean_Hotdog_animation0:


    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Jean_Hotdog_Moving:


    contains:
        "Zero_Doggy_Up"
        pos (175, 370)
        block:
            ease 1 ypos 330
            ease 1 ypos 420
            repeat






















image Zero_Jean_Doggy_animation0:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (169,545)
        block:
            ease 1 ypos 540
            pause 1
            ease 3 ypos 545
            repeat

image Zero_Jean_Doggy_Heading:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (171,545)
        block:
            ease 1 xpos 168 ypos 500
            pause 1
            ease 3 xpos 171 ypos 545
            repeat

image Zero_Jean_Doggy_Fucking2:

    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat

image Zero_Jean_Doggy_Fucking3:

    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .2 ypos 440
            pause .1
            ease .6 ypos 500
            repeat

image Jean_Pussy_Mask:


    contains:

        "images/RogueDoggy/Rogue_Doggy_SexMask.png"
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

image Jean_Pussy_Mask_animation0:


    contains:

        "images/RogueDoggy/Rogue_Doggy_SexMask.png"
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat


































image Jean_Pussy_animation0:

    subpixel True
    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat
    contains:
        ConditionSwitch(

            "JeanX.outfit['hose'] == '_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.outfit['underwear'] and JeanX.underwear_pulled_down", Null(),
            "JeanX.outfit['hose'] == '_ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Jean_Doggy_animation0", "Jean_Pussy_Mask_animation0")
    contains:


        AlphaMask("Jean_PussyHole_animation0", "Jean_Pussy_Hole_Mask_animation0")

image Jean_Pussy_Hole_Mask_animation0:

    contains:

        AlphaMask("images/JeanDoggy/Jean_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat

image Jean_PussyHole_animation0:

    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 512
            pause 1
            ease 3 ypos 515
            repeat


image Jean_Pussy_Heading:

    subpixel True
    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat
    contains:
        ConditionSwitch(

            "JeanX.outfit['hose'] == '_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.outfit['underwear'] and JeanX.underwear_pulled_down", Null(),
            "JeanX.outfit['hose'] == '_ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Jean_Doggy_Heading", "Jean_Pussy_Mask")
    contains:


        AlphaMask("Jean_Pussy_Heading_Flap", "Jean_Pussy_Hole_Mask")


image Jean_Pussy_Hole_Mask:

    contains:

        AlphaMask("images/JeanDoggy/Jean_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

image Jean_Pussy_Heading_Flap:

    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 505
            pause 1
            ease 3 ypos 515
            repeat

image Jean_Pussy_Fingering:

    subpixel True
    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .9
            pause 1
            ease 3 xzoom .6
            repeat
    contains:
        ConditionSwitch(

            "JeanX.outfit['hose'] == '_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.outfit['underwear'] and JeanX.underwear_pulled_down", Null(),
            "JeanX.outfit['hose'] == '_ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Pussy_Finger", "Rogue_doggy_pussy_mask")
    contains:


        AlphaMask("Jean_Pussy_Heading_Flap", "Jean_Pussy_Hole_Mask")



image Jean_Pussy_Fucking2:

    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FBase.png"
    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "JeanX.outfit['hose'] == '_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.outfit['underwear'] and JeanX.underwear_pulled_down", Null(),
            "JeanX.outfit['hose'] == '_ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )
    contains:


        ConditionSwitch(
            "primary_action == 'dildo pussy'", AlphaMask("Rogue_Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Jean_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            ),


image Jean_Pussy_Fucking3:

    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FBase.png"
    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "JeanX.outfit['hose'] == '_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.outfit['underwear'] and JeanX.underwear_pulled_down", Null(),
            "JeanX.outfit['hose'] == '_ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Jean_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")





image Jean_Anal:

    contains:

        "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png"
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:
        ConditionSwitch(

            "JeanX.outfit['hose'] == '_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.outfit['underwear'] and JeanX.underwear_pulled_down", Null(),
            "JeanX.outfit['hose'] == '_ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )
    contains:

        "Zero_Doggy_Insert"
        pos (172,500)




image Jean_Anal_Fingering:

    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullBase.png"
    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .6
        block:
            ease .5 zoom .75
            pause .5
            ease 1.5 zoom .6
            repeat
    contains:
        ConditionSwitch(

            "JeanX.outfit['hose'] == '_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.outfit['underwear'] and JeanX.underwear_pulled_down", Null(),
            "JeanX.outfit['hose'] == '_ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Doggy_Anal_Finger", "Rogue_Doggy_Anal_Fingering_Mask")


image Jean_Anal_Heading:

    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullBase.png"
    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .5
            repeat
    contains:
        ConditionSwitch(

            "JeanX.outfit['hose'] == '_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.outfit['underwear'] and JeanX.underwear_pulled_down", Null(),
            "JeanX.outfit['hose'] == '_ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Jean_Doggy_Anal_Heading", "Zero_Jean_Doggy_Anal_HeadingJunk")
    contains:

        AlphaMask("Zero_Jean_Doggy_Anal_Heading", "Jean_Doggy_Anal_Heading_Mask")

image Zero_Jean_Doggy_Anal_Heading:

    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500
            repeat

image Zero_Jean_Doggy_Anal_HeadingJunk:

    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600
            repeat

image Jean_Doggy_Anal_Heading_Mask:

    contains:
        "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .5
            repeat

image Jean_Doggy_Anal_Head_Top:

    contains:
        subpixel True
        "Jean_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Jean_Doggy_Anal_Head_Ass:

    contains:
        subpixel True
        "Jean_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7
            easein .9 ypos 0
            pause .9
            repeat


image Zero_Jean_Doggy_Anal1:

    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

image Jean_Anal_Fucking:

    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullBase.png"
    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullHole.png"
    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(

            "JeanX.outfit['hose'] == '_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.outfit['underwear'] and JeanX.underwear_pulled_down", Null(),
            "JeanX.outfit['hose'] == '_ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )
    contains:


        ConditionSwitch(

            "primary_action == 'dildo anal'", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Jean_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            ),

image Jean_Doggy_Anal_FullMask:
    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullHole.png"
    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(

            "JeanX.outfit['hose'] == '_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.outfit['underwear'] and JeanX.underwear_pulled_down", Null(),
            "JeanX.outfit['hose'] == '_ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )

image Jean_Doggy_Fuck_Top:

    contains:
        subpixel True
        "Jean_Doggy_Body"
        ypos 15
        pause .4
        block:
            ease .2 ypos 5
            pause .3
            ease 2 ypos 15
            repeat

image Jean_Doggy_Fuck_Ass:

    contains:
        subpixel True
        "Jean_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15
            ease .1 ypos -5
            pause .2
            ease 1.6 ypos 0
            repeat



image Zero_Jean_Doggy_Anal2:

    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Jean_Anal_Fucking2:

    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullBase.png"
    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullHole.png"
    contains:




        "images/JeanDoggy/Jean_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(

            "JeanX.outfit['hose'] == '_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.outfit['underwear'] and JeanX.underwear_pulled_down", Null(),
            "JeanX.outfit['hose'] == '_ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Jean_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")

image Jean_Doggy_Fuck2_Top:

    contains:
        subpixel True
        "Jean_Doggy_Body"
        ypos 20
        block:
            pause .15
            ease .1 ypos 0
            pause .1
            easein .5 ypos 20
            pause .05
            repeat

image Jean_Doggy_Fuck2_Ass:

    contains:
        subpixel True
        "Jean_Doggy_Ass"
        ypos 5
        block:
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .4 ypos 5
            pause .05
            repeat




image Jean_Doggy_Feet0:

    contains:
        "Jean_Doggy_Shins"
        pos (0, 0)
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat
    contains:
        ConditionSwitch(
                "Player.sprite", "Zero_Doggy_Up",
                "True", Null(),
                )
        zoom 1.2
        pos (160,480)
    contains:
        "Jean_Doggy_Feet"
        pos (0, 0)
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat

image Jean_Doggy_Feet1:

    contains:
        "Jean_Doggy_Shins"
        pos (0, 0)
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (160,480)
        block:
            pause .4
            ease 1.7 ypos 500
            ease .9 ypos 480
            repeat
    contains:
        "Jean_Doggy_Feet"
        pos (0, 0)
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat

image Jean_Doggy_Feet2:

    contains:
        "Jean_Doggy_Shins"
        pos (0, 0)
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (160,480)
        block:
            pause .07
            ease .6 ypos 500
            ease .28 ypos 480
            repeat
    contains:
        "Jean_Doggy_Feet"
        pos (0, 0)
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat











image Jean_sprite sex:
    LiveComposite(
        (1000,1000),
        (0,0), ConditionSwitch(

                "primary_action == 'eat_pussy'", "Jean_Sex_Lick",
                "not Player.sprite", "Jean_Sex_animation0",
                "Player.cock_position == 'in'", ConditionSwitch(

                        "action_speed >= 3", "Jean_Sex_Fucking_action_speed3",
                        "action_speed >= 2", "Jean_Sex_Fucking_action_speed2",
                        "action_speed", "Jean_Sex_Fucking_action_speed1",
                        "True", "Jean_Sex_Fucking_action_animation0",
                        ),
                "Player.cock_position == 'anal'", ConditionSwitch(

                        "action_speed >= 3", "Jean_Sex_Anal_action_speed3",
                        "action_speed >= 2", "Jean_Sex_Anal_action_speed2",
                        "action_speed", "Jean_Sex_Anal_action_speed1",
                        "True", "Jean_Sex_Anal_action_animation0",
                        ),
                "Player.sprite and Player.cock_position == 'out' and action_speed >= 2","Jean_Sex_Hotdog_action_speed2",
                "Player.sprite and Player.cock_position == 'out' and action_speed >= 1","Jean_Sex_Hotdog_action_speed1",







                "True", "Jean_Sex_animation0",
                ),
        )
    anchor (0.6, 0.0) zoom 0.8

image Jean_Sex_HairBack:

    "Jean_BJ_HairBack"
    zoom 0.5
    anchor (0.5, 0.5)
    rotate 20
    pos (490,320)

image Jean_Sex_Head:

    "Jean_BJ_Head"
    zoom 0.5
    anchor (0.5, 0.5)
    rotate 20
    pos (490,320)





image Jean_Sex_Torso:

    contains:

        ConditionSwitch(
            "JeanX.outfit['bra'] == '_corset'", "images/JeanSex/Jean_Sex_Over_Back.png",
            "JeanX.outfit['top'] == '_pink_shirt'", "images/JeanSex/Jean_Sex_Over_Back.png",
            "JeanX.top_pulled_up", Null(),
            "JeanX.outfit['bra'] == '_bikini_top' and not JeanX.outfit['top']", Null(),
            "not JeanX.outfit['bra'] and not JeanX.outfit['top']", Null(),
            "True", "images/JeanSex/Jean_Sex_Over_Back.png",
            )
    contains:

        "images/JeanSex/Jean_Sex_Body.png"
    contains:

















        ConditionSwitch(
            "JeanX.top_pulled_up", ConditionSwitch(

                    "JeanX.outfit['bra'] == '_sports_bra'", "images/JeanSex/Jean_Sex_Bra_Sports_Up.png",
                    "JeanX.outfit['bra'] == '_bikini_top'", "images/JeanSex/Jean_Sex_Bra_Bikini_Up.png",
                    "JeanX.outfit['bra'] == '_corset'", "images/JeanSex/Jean_Sex_Bra_Corset_Up.png",
                    "JeanX.outfit['bra'] == '_lace_bra'", "images/JeanSex/Jean_Sex_Bra_Green_Up.png",
                    "JeanX.outfit['bra']", "images/JeanSex/Jean_Sex_Bra_Green_Up.png",
                    "True", Null(),
                    ),
            "JeanX.outfit['bra'] == '_sports_bra'", "images/JeanSex/Jean_Sex_Bra_Sports.png",
            "JeanX.outfit['bra'] == '_bikini_top'", "images/JeanSex/Jean_Sex_Bra_Bikini.png",
            "JeanX.outfit['bra'] == '_corset'", "images/JeanSex/Jean_Sex_Bra_Corset.png",
            "JeanX.outfit['bra'] == '_lace_bra'", "images/JeanSex/Jean_Sex_Bra_Lace.png",
            "JeanX.outfit['bra']", "images/JeanSex/Jean_Sex_Bra_Green.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.top_pulled_up", ConditionSwitch(

                    "JeanX.outfit['top'] == '_green_shirt'", "images/JeanSex/Jean_Sex_Over_Green_Up.png",
                    "JeanX.outfit['top'] == '_pink_shirt'", "images/JeanSex/Jean_Sex_Over_Pink_Up.png",
                    "JeanX.outfit['top'] == '_yellow_shirt'", "images/JeanSex/Jean_Sex_Over_Yellow_Up.png",
                    "True", Null(),
                    ),
            "JeanX.outfit['top'] == '_green_shirt'", "images/JeanSex/Jean_Sex_Over_Green.png",
            "JeanX.outfit['top'] == '_pink_shirt'", "images/JeanSex/Jean_Sex_Over_Pink.png",
            "JeanX.outfit['top'] == '_yellow_shirt'", "images/JeanSex/Jean_Sex_Over_Yellow.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(

            "JeanX.outfit['front_inner_accessory'] == '_barbell'", ConditionSwitch(

                    "JeanX.top_pulled_up or (not JeanX.outfit['bra'] and not JeanX.outfit['top'])", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell.png",
                    "JeanX.outfit['top'] == '_green_shirt'", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Green.png",
                    "JeanX.outfit['top'] == '_pink_shirt'", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Pink.png",
                    "JeanX.outfit['top'] == '_yellow_shirt'", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Yellow.png",
                    "JeanX.outfit['bra'] == '_sports_bra'", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Bikini.png",
                    "JeanX.outfit['bra'] == '_bikini_top'", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Bikini.png",
                    "JeanX.outfit['bra'] == '_corset'", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Corset.png",
                    "JeanX.outfit['bra']", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Bra.png",
                    "True", Null(),
                    ),
            "JeanX.outfit['front_inner_accessory'] == '_ring'", ConditionSwitch(

                    "JeanX.top_pulled_up or (not JeanX.outfit['bra'] and not JeanX.outfit['top'])", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Loose.png",
                    "JeanX.outfit['top'] == '_green_shirt'", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Green.png",
                    "JeanX.outfit['top'] == '_pink_shirt'", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Pink.png",
                    "JeanX.outfit['top'] == '_yellow_shirt'", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Yellow.png",
                    "JeanX.outfit['bra'] == '_sports_bra'", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Bikini.png",
                    "JeanX.outfit['bra'] == '_bikini_top'", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Bikini.png",
                    "JeanX.outfit['bra'] == '_corset'", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Corset.png",
                    "JeanX.outfit['bra']", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Bra.png",
                    "True", Null(),
                    ),
            "True", Null(),
            )
    contains:

        ConditionSwitch(
                "not JeanX.spunk['breasts']", Null(),
                "True", "images/JeanSex/Jean_Sex_Spunk_Tits.png",
                )
    contains:
        ConditionSwitch(


            "primary_action == 'suck_breasts' or offhand_action == 'suck_breasts'", "Jean_Sex_Lick_Breasts",
            "True", Null()
            )
    contains:
        ConditionSwitch(

            "primary_action == 'fondle_breasts' or offhand_action == 'fondle_breasts'", "Jean_Sex_Fondle_Breasts",
            "True", Null()
            )
    zoom 1

image Jean_Sex_Lick_Breasts:
    "Lick_Anim"
    zoom 0.7
    offset (390,600)

image Jean_Sex_Fondle_Breasts:
    "GropeLeftBreast"
    zoom 1.5
    offset (120,-40)

image Jean_Sex_Body:

    contains:
        "Jean_Sex_HairBack"
    contains:






        AlphaMask("Jean_Sex_Torso", "images/JeanSex/Jean_Sex_ArmsMask.png")
    contains:





















        "Jean_Sex_Head"
    zoom 1.1
    offset (-40,-50)











































image Jean_Sex_Legs_S:

    contains:

        "images/JeanSex/Jean_Sex_Legs_Sex.png"
    contains:

        ConditionSwitch(
            "JeanX.grool", "images/JeanSex/Jean_Sex_Wet_Sex.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.spunk['pussy'] or JeanX.spunk['anus']", "images/JeanSex/Jean_Sex_Spunk_Pussy_S.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.outfit['hose'] == '_stockings'", "images/JeanSex/Jean_Sex_Hose_Stockings.png",
            "JeanX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JeanSex/Jean_Sex_Hose_StockingsGarter_S.png",
            "JeanX.outfit['hose'] == '_garterbelt'", "images/JeanSex/Jean_Sex_Hose_Garter_S.png",
            "True", Null(),
            )
    contains:











        ConditionSwitch(
            "JeanX.pubes", "images/JeanSex/Jean_Sex_Pubes_Sex.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(

            "JeanX.outfit['bottom'] and not JeanX.upskirt and JeanX.outfit['front_inner_accessory'] == '_ring'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Sex_Clothed.png",
            "JeanX.outfit['underwear'] and not JeanX.underwear_pulled_down and JeanX.outfit['front_inner_accessory'] == '_ring'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Sex_Clothed.png",
            "JeanX.outfit['hose'] == '_pantyhose' and not JeanX.underwear_pulled_down and JeanX.outfit['front_inner_accessory'] == '_ring'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Sex_Clothed.png",

            "JeanX.outfit['front_inner_accessory'] == '_barbell'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Sex.png",
            "JeanX.outfit['front_inner_accessory'] == '_ring'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Sex.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.outfit['bra'] == '_corset'", "images/JeanSex/Jean_Sex_Bra_Corset_Under_S.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.outfit['top'] == '_green_shirt' and not JeanX.top_pulled_up", "images/JeanSex/Jean_Sex_Over_Green_Under_S.png",
            "JeanX.outfit['top'] == '_pink_shirt'", "images/JeanSex/Jean_Sex_Over_Pink_Under_S.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.underwear_pulled_down", Null(),
            "JeanX.outfit['underwear'] == '_lace_panties'", "images/JeanSex/Jean_Sex_Panties_Sex_Lace.png",
            "JeanX.outfit['underwear'] == '_bikini_bottoms'", "images/JeanSex/Jean_Sex_Panties_Sex_Bikini.png",
            "JeanX.outfit['underwear'] and JeanX.grool", "images/JeanSex/Jean_Sex_Panties_Sex_Green_W.png",
            "JeanX.outfit['underwear']", "images/JeanSex/Jean_Sex_Panties_Sex_Green.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.underwear_pulled_down", Null(),


            "JeanX.outfit['hose'] == '_pantyhose'", "images/JeanSex/Jean_Sex_Hose_Pantyhose_S.png",
            "True", Null(),
            )
    contains:










        ConditionSwitch(
            "JeanX.outfit['bottom'] == '_skirt' and JeanX.upskirt", "images/JeanSex/Jean_Sex_Legs_Sex_Skirt_Up.png",
            "JeanX.outfit['bottom'] == '_skirt'", "images/JeanSex/Jean_Sex_Legs_Sex_Skirt.png",
            "JeanX.upskirt", Null(),
            "JeanX.outfit['bottom'] == '_pants' and JeanX.grool >=2", "images/JeanSex/Jean_Sex_Legs_Sex_Pants_W.png",
            "JeanX.outfit['bottom'] == '_pants'", "images/JeanSex/Jean_Sex_Legs_Sex_Pants.png",
            "JeanX.outfit['bottom'] == '_shorts' and JeanX.grool >=2", "images/JeanSex/Jean_Sex_Legs_Sex_Shorts_W.png",
            "JeanX.outfit['bottom'] == '_shorts'", "images/JeanSex/Jean_Sex_Legs_Sex_Shorts.png",
            "JeanX.outfit['bottom'] == '_yoga_pants' and JeanX.grool >=2", "images/JeanSex/Jean_Sex_Legs_Sex_Yoga_W.png",
            "JeanX.outfit['bottom'] == '_yoga_pants'", "images/JeanSex/Jean_Sex_Legs_Sex_Yoga.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.spunk['belly']", "images/JeanSex/Jean_Sex_Spunk_Belly_S.png",
            "True", Null(),
            )
    zoom 1


image Jean_Sex_Legs_A:

    contains:

        ConditionSwitch(
            "primary_action == 'eat_pussy'", "images/JeanSex/Jean_Sex_Legs_Lick.png",
            "True", "images/JeanSex/Jean_Sex_Legs_Anal.png",
            )
    contains:

        ConditionSwitch(
            "JeanX.grool", "images/JeanSex/Jean_Sex_Wet_Lick.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.spunk['anus'] and not action_speed", "images/JeanSex/Jean_Sex_Spunk_Pussy_S.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "not JeanX.pubes", Null(),
            "primary_action == 'eat_pussy'", "images/JeanSex/Jean_Sex_Pubes_Lick.png",
            "True", "images/JeanSex/Jean_Sex_Pubes_Anal.png",
            )
    contains:

        ConditionSwitch(
            "JeanX.outfit['bra'] == '_corset'", "images/JeanSex/Jean_Sex_Bra_Corset_Under_A.png",
            "True", Null(),
            )
    contains:








        ConditionSwitch(
            "JeanX.outfit['hose'] == '_stockings'", "images/JeanSex/Jean_Sex_Hose_Stockings.png",
            "JeanX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JeanSex/Jean_Sex_Hose_StockingsGarter_A.png",
            "JeanX.outfit['hose'] == '_garterbelt'", "images/JeanSex/Jean_Sex_Hose_Garter_A.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.spunk['pussy']", "images/JeanSex/Jean_Sex_Spunk_Pussy_A.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.underwear_pulled_down", Null(),
            "JeanX.outfit['underwear'] == '_lace_panties'", "images/JeanSex/Jean_Sex_Panties_Anal_Lace.png",
            "JeanX.outfit['underwear'] == '_bikini_bottoms'", "images/JeanSex/Jean_Sex_Panties_Anal_Bikini.png",
            "JeanX.outfit['underwear'] and JeanX.grool", "images/JeanSex/Jean_Sex_Panties_Anal_Green_W.png",
            "JeanX.outfit['underwear']", "images/JeanSex/Jean_Sex_Panties_Anal_Green.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.outfit['front_inner_accessory'] == '_barbell'", ConditionSwitch(

                    "JeanX.upskirt or (not JeanX.outfit['bottom'] and not JeanX.outfit['underwear'])", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Anal.png",
                    "JeanX.underwear_pulled_down and not JeanX.outfit['bottom']", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Anal.png",
                    "JeanX.outfit['underwear'] == '_lace_panties'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Lace.png",
                    "JeanX.outfit['underwear'] == '_bikini_bottoms'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Bikini.png",
                    "JeanX.outfit['underwear']", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Green.png",
                    "True", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Anal.png",
                    ),
            "JeanX.outfit['front_inner_accessory'] == '_ring'", ConditionSwitch(

                    "JeanX.upskirt or (not JeanX.outfit['bottom'] and not JeanX.outfit['underwear'])", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Anal.png",
                    "JeanX.underwear_pulled_down and not JeanX.outfit['bottom']", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Anal.png",
                    "JeanX.outfit['underwear'] == '_lace_panties'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Lace.png",
                    "JeanX.outfit['underwear'] == '_bikini_bottoms'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Bikini.png",
                    "JeanX.outfit['underwear']", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Green.png",
                    "True", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Anal.png",
                    ),
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "(JeanX.outfit['underwear'] and JeanX.underwear_pulled_down)", Null(),


            "JeanX.outfit['hose'] == '_pantyhose'", "images/JeanSex/Jean_Sex_Hose_Pantyhose_A.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.outfit['bottom'] == '_skirt' and JeanX.upskirt", "images/JeanSex/Jean_Sex_Legs_Anal_Skirt_Up.png",
            "JeanX.outfit['bottom'] == '_skirt' and primary_action == 'hotdog'", "images/JeanSex/Jean_Sex_Legs_Anal_Skirt_Up.png",
            "JeanX.outfit['bottom'] == '_skirt'", "images/JeanSex/Jean_Sex_Legs_Anal_Skirt.png",
            "JeanX.upskirt", Null(),
            "JeanX.outfit['bottom'] == '_pants' and JeanX.grool >=2", "images/JeanSex/Jean_Sex_Legs_Anal_Pants_W.png",
            "JeanX.outfit['bottom'] == '_pants'", "images/JeanSex/Jean_Sex_Legs_Anal_Pants.png",
            "JeanX.outfit['bottom'] == '_shorts' and JeanX.grool >=2", "images/JeanSex/Jean_Sex_Legs_Anal_Shorts_W.png",
            "JeanX.outfit['bottom'] == '_shorts'", "images/JeanSex/Jean_Sex_Legs_Anal_Shorts.png",
            "JeanX.outfit['bottom'] == '_yoga_pants' and JeanX.grool >=2", "images/JeanSex/Jean_Sex_Legs_Anal_Yoga_W.png",
            "JeanX.outfit['bottom'] == '_yoga_pants'", "images/JeanSex/Jean_Sex_Legs_Anal_Yoga.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.outfit['hose'] == '_pantyhose' and not JeanX.underwear_pulled_down", Null(),
            "JeanX.outfit['bottom'] and not JeanX.upskirt and JeanX.grool >=2", Null(),
            "JeanX.outfit['front_inner_accessory'] == '_barbell'", ConditionSwitch(

                    "JeanX.upskirt or (not JeanX.outfit['bottom'] and not JeanX.outfit['underwear'])", Null(),
                    "JeanX.outfit['bottom'] == '_skirt' and not JeanX.upskirt", Null(),
                    "JeanX.outfit['bottom'] == '_pants'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Pants.png",
                    "JeanX.outfit['bottom'] == '_shorts'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Shorts.png",
                    "JeanX.outfit['bottom'] == '_yoga_pants'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Yoga.png",
                    "True", Null(),
                    ),
            "JeanX.outfit['front_inner_accessory'] == '_ring'", ConditionSwitch(

                    "JeanX.upskirt or (not JeanX.outfit['bottom'] and not JeanX.outfit['underwear'])", Null(),
                    "JeanX.outfit['bottom'] == '_skirt' and not JeanX.upskirt", Null(),
                    "JeanX.outfit['bottom'] == '_pants'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Pants.png",
                    "JeanX.outfit['bottom'] == '_shorts'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Shorts.png",
                    "JeanX.outfit['bottom'] == '_yoga_pants'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Yoga.png",
                    "True", Null(),
                    ),
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.spunk['belly']", "images/JeanSex/Jean_Sex_Spunk_Belly_A.png",
            "True", Null(),
            )
    contains:
        ConditionSwitch(

            "Player.sprite and Player.cock_position", Null(),
            "primary_action == 'eat_pussy'", "Jean_Sex_Lick_Pussy",
            "primary_action == 'eat_ass'", "Jean_Sex_Lick_Ass",
            "True", Null()
            )
    zoom 1






image Jean_Sex_Body_Lick:

    contains:
        "Jean_Sex_Body"
        subpixel True
        pos (0,-80)
        block:
            ease 1 pos (0,-90)
            ease 1 pos (0,-80)
            repeat

image Jean_Sex_Legs_Lick:

    contains:

        "Jean_Sex_Legs_A"
        subpixel True
        pos (0,-40)
        block:
            ease 1 ypos -45
            ease 1 ypos -40
            repeat


image Jean_Sex_Lick_Pussy:
    "Lick_Anim"
    zoom 0.7
    offset (500,680)

image Jean_Sex_Lick_Ass:
    "Lick_Anim"
    zoom 0.7
    offset (500,740)


image Jean_Sex_Zero_Cock:

    contains:
        subpixel True

        ConditionSwitch(
                "Player.sprite", "Zero_blowjob_cock" ,
                "True", Null(),
                )
        subpixel True
        anchor (0.5,1.0)
        transform_anchor True
        offset (485,1000)
        zoom 0.48



image Jean_Sex_animation0:

    contains:

        subpixel True
        "Jean_Sex_Legs_S"
        pos (0,-190)
        block:
            pause 0.2
            ease 2 ypos -180
            pause 0.8
            ease 2 ypos -190
            repeat
    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-200)
        block:
            ease 2 ypos -190
            pause 0.8
            ease 2 ypos -200
            pause 0.2
            repeat







image Jean_Sex_Lick:






    contains:

        subpixel True
        "Jean_Sex_Legs_A"
        pos (0,-190)
        block:
            pause 0.2
            ease 2 ypos -180
            pause 0.8
            ease 2 ypos -190
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-230)
        block:
            ease 2 ypos -220
            pause 0.8
            ease 2 ypos -230
            pause 0.2
            repeat
    zoom 1.8
    offset (-500,-400)








image Jean_Sex_Fucking_action_animation0:

    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
    contains:

        subpixel True
        "Jean_Sex_Legs_S"
        pos (0,-250)
        block:
            pause 0.2
            ease 2 ypos -240
            pause 0.8
            ease 2 ypos -250
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-200)
        block:
            ease 2 ypos -190
            pause 0.8
            ease 2 ypos -200
            pause 0.2
            repeat







image Jean_Sex_Fucking_action_speed1:

    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
        block:
            pause 1.2
            ease 1 ypos 20
            pause 1.1
            ease 1.1 ypos -10
            pause 0.1
            ease .5 ypos 0
            repeat
    contains:

        subpixel True
        "Jean_Sex_Legs_S"
        pos (0,-250)
        block:
            pause 0.2
            ease 2 ypos -200
            pause 0.8
            ease 2 ypos -250
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-220)
        block:
            ease 2 ypos -190
            pause 0.8
            ease 2 ypos -220
            pause 0.2
            repeat








image Jean_Sex_Fucking_action_speed2:

    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
        block:
            pause 0.7
            ease 1.5 ypos 20
            pause 0.8
            ease 1.5 ypos 0
            pause 0.5
            repeat
    contains:

        subpixel True
        "Jean_Sex_Legs_S"
        pos (0,-200)
        block:
            pause 0.2
            ease 2 ypos -80
            pause 0.8
            ease 2 ypos -200
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-180)
        block:
            easeout 0.5 ypos -160
            easein 1.5 ypos -80
            pause 0.8
            easeout 1 ypos -130
            easein 1 ypos -180
            pause 0.2
            repeat









image Jean_Sex_Fucking_action_speed3:

    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
        block:
            pause 0.3
            ease 0.3 ypos 20
            pause 0.3
            ease 0.5 ypos 0
            pause 0.5
            repeat
    contains:

        subpixel True
        "Jean_Sex_Legs_S"
        pos (0,-200)
        block:
            pause 0.1
            ease 0.5 ypos -100
            pause 0.2
            ease 1.0 ypos -200
            pause 0.1
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-140)
        block:
            ease 0.6 ypos -60
            pause 0.2
            easeout 0.7 ypos -140
            easein 0.4 ypos -150
            repeat









image Jean_Sex_Anal_Spunk_Heading_Over:
    "images/JeanSex/Jean_Sex_Spunk_Anal_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8
    block:

        ease .75 xzoom 1.0
        pause 1.75
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.8
        repeat
image Jean_Sex_Anal_Spunk_Heading_Under:
    "images/JeanSex/Jean_Sex_Spunk_Anal_Under.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:

        ease .75 xzoom 1.0
        ease .25 xzoom 0.95
        pause 1.50
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Jean_Sex_Anal_Mask:


    contains:
        "images/JeanSex/Jean_Sex_Mask_Anal.png"
        yoffset 3



image Jean_Sex_Anal_action_animation0:

    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
    contains:

        subpixel True
        "Jean_Sex_Legs_A"
        pos (0,-250)
        block:
            pause 0.2
            ease 2 ypos -240
            pause 0.8
            ease 2 ypos -250
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-280)
        block:
            ease 2 ypos -270
            pause 0.8
            ease 2 ypos -280
            pause 0.2
            repeat






image Jean_Sex_Anal_action_speed1:

    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
        block:
            pause 1.2
            ease 1 ypos 20
            pause 1.1
            ease 1.1 ypos -10
            pause 0.1
            ease .5 ypos 0
            repeat
    contains:

        subpixel True
        "Jean_Sex_Legs_A"
        pos (0,-250)
        block:
            pause 0.2
            ease 2 ypos -200
            pause 0.8
            ease 2 ypos -250
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-250)
        block:
            ease 2 ypos -220
            pause 0.8
            ease 2 ypos -250
            pause 0.2
            repeat






image Jean_Sex_Anal_action_speed2:

    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
        block:
            pause 0.7
            ease 1.5 ypos 20
            pause 0.8
            ease 1.5 ypos 0
            pause 0.5
            repeat
    contains:

        subpixel True
        "Jean_Sex_Legs_A"
        pos (0,-200)
        block:
            pause 0.2
            ease 2 ypos -80
            pause 0.8
            ease 2 ypos -200
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-200)
        block:
            ease 2 ypos -100
            pause 0.8
            ease 2 ypos -200
            pause 0.2
            repeat






image Jean_Sex_Anal_action_speed3:

    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
        block:
            pause 0.3
            ease 0.3 ypos 20
            pause 0.3
            ease 0.5 ypos 0
            pause 0.5
            repeat
    contains:

        subpixel True
        "Jean_Sex_Legs_A"
        pos (0,-200)
        block:
            pause 0.1
            ease 0.5 ypos -100
            pause 0.2
            ease 1.0 ypos -200
            pause 0.1
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-190)
        block:
            ease 0.6 ypos -120
            pause 0.1

            ease 1.2 ypos -190



            repeat











image Jean_Sex_Hotdog_action_speed1:

    contains:

        subpixel True
        "Jean_Sex_Legs_A"
        pos (0,-200)
        block:
            pause 0.2
            ease 2 ypos -80
            pause 0.8
            ease 2 ypos -200
            repeat
    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
        alpha 0.8
        block:
            pause 0.7
            ease 1.5 ypos 20
            pause 0.8
            ease 1.5 ypos 0
            pause 0.5
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-200)
        block:







            ease 2 ypos -100
            pause 0.8
            ease 2 ypos -200
            pause 0.2
            repeat






image Jean_Sex_Hotdog_action_speed2:

    contains:

        subpixel True
        "Jean_Sex_Legs_A"
        pos (0,-200)
        block:
            pause 0.1
            ease 0.5 ypos -100
            pause 0.2
            ease 1.0 ypos -200
            pause 0.1
            repeat
    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
        alpha 0.8
        block:
            pause 0.3
            ease 0.3 ypos 20
            pause 0.3
            ease 0.5 ypos 0
            pause 0.5
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-190)
        block:
            ease 0.6 ypos -120
            pause 0.1
            ease 1.2 ypos -190



            repeat


















image Jean_sprite blowjob:
    LiveComposite(
        (858,928),
        (-270,-160), ConditionSwitch(

            "action_speed == 0", At("Jean_BJ_HairBack", Jean_BJ_Head_0()),
            "action_speed == 1", At("Jean_BJ_HairBack", Jean_BJ_Head_1()),
            "action_speed == 2", At("Jean_BJ_HairBack", Jean_BJ_Head_2()),
            "action_speed == 3", At("Jean_BJ_HairBack", Jean_BJ_Head_3()),
            "action_speed == 4", At("Jean_BJ_HairBack", Jean_BJ_Head_4()),
            "action_speed == 5", At("Jean_BJ_HairBack", Jean_BJ_Head_5()),
            "action_speed == 6", At("Jean_BJ_HairBack", Jean_BJ_Head_6()),
            "True", Null(),
            ),
        (-20,270), ConditionSwitch(

            "action_speed == 0", At("Jean_BJ_Backdrop", Jean_BJ_Body_0()),
            "action_speed == 1", At("Jean_BJ_Backdrop", Jean_BJ_Body_1()),
            "action_speed == 2", At("Jean_BJ_Backdrop", Jean_BJ_Body_2()),
            "action_speed == 3", At("Jean_BJ_Backdrop", Jean_BJ_Body_3()),
            "action_speed == 4", At("Jean_BJ_Backdrop", Jean_BJ_Body_4()),
            "action_speed == 5", At("Jean_BJ_Backdrop", Jean_BJ_Body_5()),
            "action_speed == 6", At("Jean_BJ_Backdrop", Jean_BJ_Body_6()),
            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(

            "action_speed == 0", At("Jean_BJ_Head", Jean_BJ_Head_0()),
            "action_speed == 1", At("Jean_BJ_Head", Jean_BJ_Head_1()),
            "action_speed == 2", At("Jean_BJ_Head", Jean_BJ_Head_2()),
            "action_speed == 3", At("Jean_BJ_Head", Jean_BJ_Head_3()),
            "action_speed == 4", At("Jean_BJ_Head", Jean_BJ_Head_4()),
            "action_speed == 5", At("Jean_BJ_Head", Jean_BJ_Head_5()),
            "action_speed == 6", At("Jean_BJ_Head", Jean_BJ_Head_6()),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "action_speed == 0", At("Zero_blowjob_cock", Jean_BJ_Cock_0()),
            "action_speed == 1", At("Zero_blowjob_cock", Jean_BJ_Cock_1()),
            "action_speed >= 2", At("Zero_blowjob_cock", Jean_BJ_Cock_2()),



            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(

            "action_speed < 3", Null(),
            "action_speed == 3", At(AlphaMask("Jean_BJ_Head", "Jean_BJ_mouthSuckingMask"), Jean_BJ_Head_3()),
            "action_speed == 4", At(AlphaMask("Jean_BJ_Head", "Jean_BJ_mouthSuckingMask"), Jean_BJ_Head_4()),
            "action_speed == 6", At(AlphaMask("Jean_BJ_Head", "Jean_BJ_mouthSuckingMask"), Jean_BJ_Head_6()),
            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(

            "action_speed == 2", At(AlphaMask("Jean_BJ_Head", "Jean_BJ_MaskHeadingComposite"), Jean_BJ_Head_2()),
            "action_speed == 5", At(AlphaMask("Jean_BJ_Head", "Jean_BJ_MaskHeadingComposite"), Jean_BJ_Head_5()),
            "True", Null(),
            ),
        (325,490), ConditionSwitch(

            "action_speed < 3 or not JeanX.spunk['mouth']", Null(),
            "action_speed == 3", At("JeanSuckingSpunk", Jean_BJ_Head_3()),
            "action_speed == 4", At("JeanSuckingSpunk", Jean_BJ_Head_4()),
            "action_speed == 6", At("JeanSuckingSpunk", Jean_BJ_Head_6()),
            "True", Null(),
            ),







        )
    zoom .55
    anchor (.5,.5)

image Jean_BJ_HairBack:

    ConditionSwitch(
            "JeanX.wet or JeanX.outfit['hair'] == '_wet'", "images/JeanBJFace/Jean_BJ_Hair_Wet_Under.png",
            "JeanX.outfit['hair'] == 'pony'", Null(),
            "True", "images/JeanBJFace/Jean_BJ_Hair_Short_Under.png",
            ),
    zoom 1.4
    anchor (0.5, 0.5)

image Jean_BJ_HairTop:

    ConditionSwitch(
            "JeanX.wet or JeanX.outfit['hair'] == '_wet'", "images/JeanBJFace/Jean_BJ_Hair_Wet_Over.png",
            "True", Null(),
            ),
    zoom 1.4
    anchor (0.5, 0.5)

image Jean_BJ_Backdrop1:
    contains:

        ConditionSwitch(
                "'blanket' in JeanX.recent_history", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
                "True", Null(),
                ),
        zoom 2
        anchor (.5,.5)
        pos (350,600)









image Jean_BJ_Head:
    LiveComposite(
        (858,928),
        (0,0), ConditionSwitch(

            "(JeanX.wet or JeanX.outfit['hair'] == '_wet') and renpy.showing('Jean_sprite sex')", "images/JeanBJFace/Jean_BJ_Hair_Wet_Mid.png",
            "JeanX.wet or JeanX.outfit['hair'] == '_wet'", Null(),
            "JeanX.outfit['hair'] == 'pony'", Null(),
            "True", "images/JeanBJFace/Jean_BJ_Hair_Short_Under.png",
            ),




        (0,0), ConditionSwitch(






            "JeanX.blushing == '_blush2'", "images/JeanBJFace/Jean_BJ_Head_Blush2.png",
            "JeanX.blushing", "images/JeanBJFace/Jean_BJ_Head_Blush1.png",
            "True", "images/JeanBJFace/Jean_BJ_Head_Blush0.png"
            ),
        (0,0), ConditionSwitch(






            "action_speed and renpy.showing('Jean_sprite blowjob')", ConditionSwitch(

                    "action_speed == 1", "images/JeanBJFace/Jean_BJ_mouth_Tongue.png",
                    "(action_speed == 2 or action_speed == 5)", Null(),
                    "action_speed == 3", "images/JeanBJFace/Jean_BJ_mouth_Sucking.png",
                    "action_speed == 4", "images/JeanBJFace/Jean_BJ_mouth_Sucking.png",
                    "action_speed == 6", "images/JeanBJFace/Jean_BJ_mouth_Sucking.png",
                    ),
            "action_speed == 3 and renpy.showing('Jean_sprite titjob')", "images/JeanBJFace/Jean_BJ_mouth_Tongue.png",
            "JeanX.mouth == '_normal'", "images/JeanBJFace/Jean_BJ_mouth_Smile.png",
            "JeanX.mouth == '_lipbite'", "images/JeanBJFace/Jean_BJ_mouth_Lipbite.png",
            "JeanX.mouth == '_sucking'", "images/JeanBJFace/Jean_BJ_mouth_Tongue.png",
            "JeanX.mouth == '_kiss'", "images/JeanBJFace/Jean_BJ_mouth_Kiss.png",
            "JeanX.mouth == '_sad'", "images/JeanBJFace/Jean_BJ_mouth_Sad.png",
            "JeanX.mouth == '_smile'", "images/JeanBJFace/Jean_BJ_mouth_Smile.png",
            "JeanX.mouth == '_smirk'", "images/JeanBJFace/Jean_BJ_mouth_Smirk.png",
            "JeanX.mouth == '_smile'", "images/JeanBJFace/Jean_BJ_mouth_Smile.png",
            "JeanX.mouth == '_surprised'", "images/JeanBJFace/Jean_BJ_mouth_Kiss.png",
            "JeanX.mouth == '_tongue'", "images/JeanBJFace/Jean_BJ_mouth_Tongue.png",
            "True", "images/JeanBJFace/Jean_BJ_mouth_Smile.png",
            ),
        (428,605), ConditionSwitch(


            "not renpy.showing('Jean_sprite blowjob')", Null(),
            "action_speed == 2", At("Jean_BJ_mouthHeading", Jean_BJ_mouthAnim()),
            "action_speed == 5", At("Jean_BJ_mouthHeading", Jean_BJ_mouthAnimC()),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "not JeanX.spunk['mouth']", Null(),
            "action_speed and renpy.showing('Jean_sprite blowjob')", ConditionSwitch(

                    "action_speed == 1", "images/JeanBJFace/Jean_BJ_Spunk_Tongue.png",
                    "(action_speed == 2 or action_speed == 5)", Null(),
                    "action_speed == 3", "images/JeanBJFace/Jean_BJ_Spunk_SuckingUnder.png",
                    "action_speed == 4", "images/JeanBJFace/Jean_BJ_Spunk_SuckingUnder.png",
                    "action_speed == 6", "images/JeanBJFace/Jean_BJ_Spunk_SuckingUnder.png",
                    ),
            "JeanX.mouth == '_normal'", "images/JeanBJFace/Jean_BJ_Spunk_Smile.png",



            "JeanX.mouth == '_smile'", "images/JeanBJFace/Jean_BJ_Spunk_Smile.png",


            "JeanX.mouth == '_tongue'", "images/JeanBJFace/Jean_BJ_Spunk_Tongue.png",
            "JeanX.mouth == '_sucking'", "images/JeanBJFace/Jean_BJ_Spunk_SuckingUnder.png",
            "True", "images/JeanBJFace/Jean_BJ_Spunk_Kiss.png",
            ),
        (0,0), ConditionSwitch(

            "JeanX.brows == '_normal'", "images/JeanBJFace/Jean_BJ_brows_Normal.png",
            "JeanX.brows == '_angry'", "images/JeanBJFace/Jean_BJ_brows_Angry.png",
            "JeanX.brows == '_sad'", "images/JeanBJFace/Jean_BJ_brows_Sad.png",
            "JeanX.brows == '_surprised'", "images/JeanBJFace/Jean_BJ_brows_Surprised.png",
            "JeanX.brows == '_confused'", "images/JeanBJFace/Jean_BJ_brows_Confused.png",
            "True", "images/JeanBJFace/Jean_BJ_brows_Normal.png",
            ),
        (0,0), "Jean_sprite BJ Blink",

        (0,0), ConditionSwitch(

            "JeanX.wet or JeanX.outfit['hair'] == '_wet'", "images/JeanBJFace/Jean_BJ_Hair_Wet_Over.png",
            "JeanX.outfit['hair'] == 'pony'", "images/JeanBJFace/Jean_BJ_Hair_Pony_Over.png",
            "True", "images/JeanBJFace/Jean_BJ_Hair_Short_Over.png",
            ),











        (0,0), ConditionSwitch(

            "JeanX.spunk['hair']", "images/JeanBJFace/Jean_BJ_Spunk_Facial2.png",
            "JeanX.spunk['face']", "images/JeanBJFace/Jean_BJ_Spunk_Facial1.png",
            "True", Null(),
            ),
        )
    zoom 1.4
    anchor (0.5, 0.5)


image Jean_sprite BJ Blink:

    ConditionSwitch(
            "JeanX.eyes == '_normal'", "images/JeanBJFace/Jean_BJ_eyes_Normal.png",
            "JeanX.eyes == '_sexy'", "images/JeanBJFace/Jean_BJ_eyes_Sexy.png",
            "JeanX.eyes == '_closed'", "images/JeanBJFace/Jean_BJ_eyes_Closed.png",
            "JeanX.eyes == '_surprised'", "images/JeanBJFace/Jean_BJ_eyes_Surprised.png",
            "JeanX.eyes == '_side'", "images/JeanBJFace/Jean_BJ_eyes_Side.png",
            "JeanX.eyes == '_stunned'", "images/JeanBJFace/Jean_BJ_eyes_Stunned.png",
            "JeanX.eyes == '_down'", "images/JeanBJFace/Jean_BJ_eyes_Down.png",
            "JeanX.eyes == '_manic'", "images/JeanBJFace/Jean_BJ_eyes_Surprised.png",
            "JeanX.eyes == '_squint'", "images/JeanBJFace/Jean_BJ_eyes_Sexy.png",
            "True", "images/JeanBJFace/Jean_BJ_eyes_Normal.png",
            ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/JeanBJFace/Jean_BJ_eyes_Closed.png"
    .25
    repeat

image Jean_BJ_mouthHeading:

    contains:
        "images/JeanBJFace/Jean_BJ_mouth_Sucking.png"
        zoom 1.4
        anchor (0.50,0.65)

image Jean_BJ_mouthSuckingMask:

    contains:
        "images/JeanBJFace/Jean_BJ_mouth_MaskS.png"
        zoom 1.4








image Jean_BJ_MaskHeading:

    contains:
        "images/JeanBJFace/Jean_BJ_mouth_MaskH.png"
        offset (-380,-595)

image Jean_BJ_MaskHeadingComposite:

    LiveComposite(
        (858,928),
        (300,462), ConditionSwitch(
            "action_speed == 2", At("Jean_BJ_MaskHeading", Jean_BJ_mouthAnim()),
            "action_speed == 5", At("Jean_BJ_MaskHeading", Jean_BJ_mouthAnimC()),
            "True", Null(),
            ),
        )
    zoom 1.8

image Jean_BJ_MaskHeadingSpunk:

    contains:

        ConditionSwitch(
                    "action_speed == 2", "images/JeanBJFace/Jean_BJ_Spunk_SuckingOver.png",
                    "True", Null(),
                    )


        subpixel True
        anchor (0.5, 0.65)
        zoom 0.58
        block:
            pause .20
            easeout .15 zoom 0.66
            linear .15 zoom 0.60
            easein .25 zoom 0.68
            pause .25

            pause .40
            easeout .40 zoom 0.60
            linear .10 zoom 0.66
            easein .30 zoom 0.58
            pause .30

            repeat


    zoom 1.8
    yoffset 180

image JeanSuckingSpunk:
    contains:
        "images/JeanBJFace/Jean_BJ_Spunk_SuckingOver.png"
        zoom 1.4
        anchor (0.5, 0.5)


image Jean_BJ_Backdrop:

    contains:

        ConditionSwitch(
                "'blanket' in JeanX.recent_history", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
                "True", Null(),
                )
        zoom 1.2
        anchor (.5,.5)
        pos (180,-400)
    contains:







        "Jean_TJ_Braback"
        subpixel True
        pos (0,0)
        transform_anchor True
    contains:







        "Jean_TJ_Body"
        subpixel True
        pos (0,0)
        transform_anchor True
    contains:







        "Jean_TJ_TitR"
        subpixel True
        pos (0,0)
        transform_anchor True
    contains:






        "Jean_TJ_Tits"
        subpixel True
        pos (0,0)
        transform_anchor True






    zoom 1.4
    offset (225,1100)




transform Jean_BJ_mouthAnim():

    subpixel True
    zoom 0.58
    block:
        pause .20
        easeout .15 zoom 0.66
        linear .15 zoom 0.60
        easein .25 zoom 0.68
        pause .25

        pause .40
        easeout .40 zoom 0.60
        linear .10 zoom 0.66
        easein .30 zoom 0.58
        pause .30

        repeat















transform Jean_BJ_Head_2():

    subpixel True
    offset (0,-40)
    block:
        ease 1 yoffset 40
        ease 1.5 offset (0,-40)
        repeat






transform Jean_BJ_mouthAnimC():

    subpixel True
    zoom 0.7
    block:
        pause .20
        ease .50 zoom 0.65
        pause .60
        ease .30 zoom 0.7
        pause .10
        ease .30 zoom 0.65
        pause .20
        ease .30 zoom 0.7
        repeat



transform Jean_BJ_Cock_0():

    anchor (.5,.5)
    rotate -10
transform Jean_BJ_Cock_1():

    subpixel True
    anchor (.5,.5)
    ease 0.5 rotate 0
    block:
        ease 2 rotate -5
        pause .5
        ease 2.5 rotate 0
        repeat
transform Jean_BJ_Cock_2():

    anchor (.5,.5)
    rotate 0
    alpha 1




transform Jean_BJ_Head_0():

    subpixel True
    ease 1.5 offset (0,0)
transform Jean_BJ_Body_0():

    subpixel True
    ease 1.5 offset (0,0)


transform Jean_BJ_Head_1():

    subpixel True
    ease 0.5 offset (0,-35)
    block:
        ease 2.5 offset (25,100)
        ease 2 offset (0,-35)
        pause .5
        repeat
transform Jean_BJ_Body_1():

    subpixel True
    ease 0.5 offset (0,-35)
    block:
        ease 2.5 offset (30,90)
        ease 2 offset (0,-35)
        pause .5
        repeat













transform Jean_BJ_Body_2():

    subpixel True
    offset (0,-40)
    block:
        ease 1 yoffset 15
        ease 1.5 offset (0,-40)
        repeat

transform Jean_BJ_Head_3():

    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 120
        ease 1.5 offset (0,50)
        repeat
transform Jean_BJ_Body_3():

    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 100
        ease 1.5 offset (0,50)
        repeat

transform Jean_BJ_Head_4():

    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1 yoffset 300
        pause .5
        ease 2 yoffset 100
        repeat
transform Jean_BJ_Body_4():

    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1.2 yoffset 250
        pause .5
        ease 1.8 yoffset 100
        repeat

transform Jean_BJ_Head_5():

    subpixel True
    offset (0,-30)
    block:
        ease 1 yoffset -20
        ease 1.5 offset (0,-30)
        repeat
transform Jean_BJ_Body_5():

    subpixel True
    offset (0,-30)
    block:
        ease 1 yoffset -20
        ease 1.5 offset (0,-30)
        repeat

transform Jean_BJ_Head_6():

    ease .5 offset (0,230)
    block:
        subpixel True
        ease 1 yoffset 250
        pause .5
        ease 2 yoffset 230
        repeat
transform Jean_BJ_Body_6():

    ease .5 offset (0,190)
    block:
        subpixel True
        ease 1.2 yoffset 200
        pause .5
        ease 1.8 yoffset 190
        repeat


















label Jean_BJ_Launch(Line=primary_action):
    if renpy.showing("Jean_sprite blowjob"):
        return


    if renpy.showing("Jean_sprite titjob"):
        hide Jean_sprite titjob
    else:
        call hide_girl(JeanX)
        if Line == "L" or Line == "cum":
            show Jean_sprite standing zorder JeanX.sprite_layer at sprite_location(stage_center):
                alpha 1
                ease 1 zoom 2.5 offset (150,80)
            with dissolve
        else:
            show Jean_sprite standing zorder JeanX.sprite_layer at sprite_location(stage_center):
                alpha 1
                zoom 2.5 offset (150,80)
            with dissolve
        hide Jean_sprite

    $ action_speed = 0

    if Line != "cum":
        $ primary_action = "blowjob"

    show Jean_sprite blowjob zorder 150:
        pos (645,510)
    if taboo and Line == "L":
        if len(Present) >= 2:
            if Present[0] != JeanX:
                "[JeanX.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != JeanX:
                "[JeanX.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[JeanX.name] looks around to see if anyone can see her."
        "She then bends down and puts your cock to her mouth."
    elif Line == "L":
        "[JeanX.name] smoothly bends down and places your cock against her cheek."

    return

label Jean_BJ_Reset:
    if not renpy.showing("Jean_sprite blowjob"):
        return

    call hide_girl(JeanX)
    $ action_speed = 0

    show Jean_sprite standing zorder JeanX.sprite_layer at sprite_location(stage_center):
        alpha 1
        zoom 2.5 offset (150,80)
    with dissolve

    show Jean_sprite standing zorder JeanX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .2
        ease .3 zoom 1 offset (0,0)
    pause 1.5
    show Jean_sprite standing zorder JeanX.sprite_layer at sprite_location(JeanX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
    return













image Jean_Hand_Under:
    "images/JeanSprite/handjean2.png"
    anchor (0.5,0.5)
    pos (-10,0)
    offset (0,130)

image Jean_Hand_Over:
    "images/JeanSprite/handjean1.png"
    anchor (0.5,0.5)
    pos (-10,0)
    offset (0,130)

transform Jean_Hand_1():
    subpixel True
    pos (-20,-100)
    rotate 5
    block:
        ease .5 pos (0,150) rotate -5
        pause 0.25
        ease 1.0 pos (-20,-100) rotate 5
        pause 0.1
        repeat

transform Jean_Hand_2():
    subpixel True
    pos (-15,-120)
    rotate 10
    block:
        ease 0.2 pos (-15,0) rotate 0
        pause 0.1
        ease 0.4 pos (-15,-120) rotate 10
        pause 0.1
        repeat
























transform Handcock_1J():
    subpixel True
    rotate_pad False
    ypos 400
    rotate 0
    block:
        ease .5 ypos 450 rotate -2
        pause 0.25
        ease 1.0 ypos 400 rotate 0
        pause 0.1
        repeat

transform Handcock_2J():
    subpixel True
    rotate_pad False
    ypos 400
    rotate 0
    block:
        ease .2 ypos 430 rotate -3
        ease .5 ypos 400 rotate 0
        pause 0.1
        repeat

image Jean_sprite handjob:
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Jean_Hand_Under"),
            "action_speed == 1", At("Jean_Hand_Under", Jean_Hand_1()),
            "action_speed >= 2", At("Jean_Hand_Under", Jean_Hand_2()),
            "action_speed", Null(),
            ),
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Zero_Handcock"),
            "action_speed == 1", At("Zero_Handcock", Handcock_1J()),
            "action_speed >= 2", At("Zero_Handcock", Handcock_2J()),
            "action_speed", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Jean_Hand_Over"),
            "action_speed == 1", At("Jean_Hand_Over", Jean_Hand_1()),
            "action_speed >= 2", At("Jean_Hand_Over", Jean_Hand_2()),
            "action_speed", Null(),
            ),
    anchor (0.51, -1.3)
    zoom 0.4








image Jean_Hand_Psychic:
    ConditionSwitch(
        "Psychic == 'mouth'", "images/JeanSprite/Psymouth.png",
        "Psychic == 'pussy'", "images/JeanSprite/PsyPussy.png",
        "Psychic == 'anal'", "images/JeanSprite/PsyAss.png",
        "Psychic == 'tits'", "images/JeanSprite/PsyTits.png",
        "True", "images/JeanSprite/handjeanP.png",
        )


    anchor (0.5,0.5)
    pos (-10,0)
    offset (0,130)
    block:
        ease 3 alpha 0.7
        ease 3 alpha 1
        repeat

image Jean_PJ_Animation:








    contains:
        ConditionSwitch(


            "not action_speed", Transform("Zero_Handcock"),
            "action_speed == 1", At("Zero_Handcock", Handcock_1J()),
            "action_speed >= 2", At("Zero_Handcock", Handcock_2J()),
            "action_speed", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Jean_Hand_Psychic"),
            "action_speed == 1", At("Jean_Hand_Psychic", Jean_Hand_1()),
            "action_speed >= 2", At("Jean_Hand_Psychic", Jean_Hand_2()),
            "action_speed", Null(),
            ),
    anchor (0.51, -1.3)
    zoom 0.4








image Jean_sprite titjob:

    contains:
        ConditionSwitch(

                    "not Player.sprite","Jean_TJ_0",
                    "action_speed == 1", "Jean_TJ_1",
                    "action_speed == 4", "Jean_TJ_4",
                    "action_speed == 5", "Jean_TJ_5",
                    "action_speed >= 2", "Jean_TJ_2",
                    "True",       "Jean_TJ_0",
                    )
    zoom .8
    transform_anchor True
    anchor (.5,.5)




image Jean_TJ_HairBack:

    "Jean_BJ_HairBack"
    transform_anchor True
    zoom .7
    anchor (0.5, 0.5)
    offset (30,-450)
    rotate 0

image Jean_TJ_Head:

    "Jean_BJ_Head"
    transform_anchor True
    zoom .7
    anchor (0.5, 0.5)
    offset (30,-450)
    rotate 0

image Jean_TJ_HairTop:

    ConditionSwitch(
                    "JeanX.wet or JeanX.outfit['hair'] == '_wet'", "images/JeanBJFace/Jean_BJ_Hair_Wet_Over.png",
                    "JeanX.outfit['hair'] == 'pony'", "images/JeanBJFace/Jean_BJ_Hair_Pony_Over.png",
                    "True", "images/JeanBJFace/Jean_BJ_Hair_Short_Over.png",
                    )




    transform_anchor True
    zoom .98
    anchor (0.5, 0.5)
    offset (30,-450)
    rotate 0

image JeanScreen:
    "images/JeanBJFace/screenshot0115.png"
    alpha 0.2

image Jean_TJ_ZeroCock:

    "Zero_blowjob_cock"
    transform_anchor True
    zoom .6
    anchor (0.5, 0.5)
    offset (70,50)
    rotate 0

image Jean_TJ_Body:

    contains:
        "images/JeanBJFace/Jean_TJ_Body.png"
    contains:

        ConditionSwitch(

                        "JeanX.outfit['bra'] == '_sports_bra'","images/JeanBJFace/Jean_TJ_Chest_SportsBra_Base.png",
                        "JeanX.outfit['bra'] == '_bikini_top'","images/JeanBJFace/Jean_TJ_Chest_Bikini_Base.png",
                        "True", Null(),
                        )
    contains:

        ConditionSwitch(

                        "JeanX.outfit['top'] == '_yellow_shirt'","images/JeanBJFace/Jean_TJ_Over_Tank_Base.png",
                        "JeanX.outfit['top'] == '_green_shirt'","images/JeanBJFace/Jean_TJ_Over_GreenShirt_Base.png",
                        "JeanX.outfit['top'] == '_pink_shirt'","images/JeanBJFace/Jean_TJ_Over_PinkShirt_Base.png",
                        "True", Null(),
                        )





    transform_anchor True
    zoom 1
    anchor (0.4, 1.0)

    rotate 0


image Jean_TJ_TitR:

    contains:

        ConditionSwitch(

                    "not renpy.showing('Jean_sprite titjob')", "images/JeanBJFace/Jean_TJ_TitR.png",
                    "True",  "images/JeanBJFace/Jean_TJ_TitRTJ.png",
                    )
    contains:

        ConditionSwitch(
                        "not JeanX.spunk['breasts']",Null(),
                        "True",       "images/JeanBJFace/Jean_TJ_Spunk_TitsUnder.png",
                        )
    transform_anchor True
    zoom 1
    anchor (0.4, 1.0)

    rotate 0

image Jean_TJ_Braback:






    contains:
        ConditionSwitch(
                        "JeanX.outfit['top'] == '_green_shirt'",Null(),
                        "JeanX.outfit['bra'] == '_green_bra' or JeanX.outfit['bra'] == '_lace_bra'","images/JeanBJFace/Jean_TJ_Chest_Bra_Base.png",
                        "True", Null(),
                        )
    transform_anchor True
    zoom 1
    anchor (0.4, 1.0)

    rotate 0

image Jean_TJ_BraStretch:

    contains:
        ConditionSwitch(

                        "JeanX.outfit['bra'] == '_bikini_top' or JeanX.outfit['bra'] == '_sports_bra'","images/JeanBJFace/Jean_TJ_Chest_Bikini_Stretch.png",
                        "True", Null(),
                        )
    transform_anchor True
    zoom 1
    anchor (0.4, 1.0)

    rotate 0


image Jean_TJ_Tits:

    contains:
        "images/JeanBJFace/Jean_TJ_TitL.png"
    contains:

        ConditionSwitch(
                        "JeanX.outfit['front_inner_accessory'] == '_ring'","images/JeanBJFace/Jean_TJ_Pierce_Ring.png",
                        "JeanX.outfit['front_inner_accessory'] == '_barbell'","images/JeanBJFace/Jean_TJ_Pierce_Barbell.png",
                        "True", Null(),
                        )
    contains:
        ConditionSwitch(

                    "not renpy.showing('Jean_sprite titjob')", Null(),
                    "True",  "images/JeanBJFace/Jean_TJ_TitRO.png",
                    )
    contains:
        ConditionSwitch(
                        "not JeanX.spunk['breasts']",Null(),
                        "True",       "images/JeanBJFace/Jean_TJ_Spunk_Tits.png",
                        )
    contains:

        ConditionSwitch(
                        "JeanX.outfit['bra'] == '_green_bra' and JeanX.top_pulled_up and JeanX.outfit['top'] == '_green_shirt'","images/JeanBJFace/Jean_TJ_Chest_Bra_UpS.png",
                        "JeanX.outfit['bra'] == '_green_bra' and JeanX.top_pulled_up","images/JeanBJFace/Jean_TJ_Chest_Bra_Up.png",
                        "JeanX.outfit['bra'] == '_lace_bra' and JeanX.top_pulled_up and JeanX.outfit['top'] == '_green_shirt'","images/JeanBJFace/Jean_TJ_Chest_Bra_UpS.png",
                        "JeanX.outfit['bra'] == '_lace_bra' and JeanX.top_pulled_up","images/JeanBJFace/Jean_TJ_Chest_Bra_Up.png",
                        "JeanX.outfit['bra'] == '_sports_bra' and JeanX.top_pulled_up","images/JeanBJFace/Jean_TJ_Chest_SportsBra_Up.png",
                        "JeanX.outfit['bra'] == '_bikini_top' and JeanX.top_pulled_up","images/JeanBJFace/Jean_TJ_Chest_Bikini_Up.png",
                        "JeanX.outfit['bra'] == '_green_bra' and JeanX.outfit['top'] == '_green_shirt'","images/JeanBJFace/Jean_TJ_Chest_Bra_Strapless.png",
                        "JeanX.outfit['bra'] == '_green_bra'","images/JeanBJFace/Jean_TJ_Chest_Bra_Top.png",
                        "JeanX.outfit['bra'] == '_lace_bra' and JeanX.outfit['top'] == '_green_shirt'","images/JeanBJFace/Jean_TJ_Chest_LaceBra_Strapless.png",
                        "JeanX.outfit['bra'] == '_lace_bra'","images/JeanBJFace/Jean_TJ_Chest_LaceBra_Top.png",
                        "JeanX.outfit['bra'] == '_sports_bra'","images/JeanBJFace/Jean_TJ_Chest_SportsBra_Top.png",
                        "JeanX.outfit['bra'] == '_bikini_top'","images/JeanBJFace/Jean_TJ_Chest_Bikini_Top.png",
                        "JeanX.outfit['bra'] == '_corset' and not JeanX.top_pulled_up and not renpy.showing('Jean_sprite titjob')", "images/JeanBJFace/Jean_TJ_Chest_Corset.png",
                        "True", Null(),
                        )
    contains:

        ConditionSwitch(

                        "JeanX.outfit['top'] == '_yellow_shirt' and JeanX.top_pulled_up","images/JeanBJFace/Jean_TJ_Over_Tank_Up.png",
                        "JeanX.outfit['top'] == '_yellow_shirt'","images/JeanBJFace/Jean_TJ_Over_Tank_Top.png",
                        "JeanX.outfit['top'] == '_green_shirt' and JeanX.top_pulled_up","images/JeanBJFace/Jean_TJ_Over_GreenShirt_Up.png",
                        "JeanX.outfit['top'] == '_pink_shirt' and JeanX.top_pulled_up","images/JeanBJFace/Jean_TJ_Over_PinkShirt_Up.png",
                        "JeanX.outfit['top'] == '_green_shirt'","images/JeanBJFace/Jean_TJ_Over_GreenShirt_Top.png",
                        "JeanX.outfit['top'] == '_pink_shirt'","images/JeanBJFace/Jean_TJ_Over_PinkShirt_Top.png",
                        "JeanX.outfit['top'] == '_towel' and not renpy.showing('Jean_sprite titjob')", "images/JeanBJFace/Jean_TJ_Over_Towel.png",
                        "True", Null(),
                        )
    contains:

        ConditionSwitch(
                        "JeanX.top_pulled_up", Null(),
                        "(not JeanX.outfit['top'] or JeanX.outfit['top'] == '_towel') and (not JeanX.outfit['bra'] or JeanX.outfit['bra'] == '_corset')", Null(),
                        "JeanX.outfit['front_inner_accessory'] == '_ring'","images/JeanBJFace/Jean_TJ_Pierce_RingC.png",
                        "JeanX.outfit['front_inner_accessory'] == '_barbell'","images/JeanBJFace/Jean_TJ_Pierce_BarbellC.png",
                        "True", Null(),
                        )
    transform_anchor True
    zoom 1
    anchor (0.4, 1.0)

    rotate 0





image Jean_TJ_0:

    contains:

        "Jean_TJ_Braback"
        subpixel True
        pos (0,0)
        transform_anchor True
        parallel:
            ease 2 ypos -20
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
    contains:

        "Jean_TJ_HairBack"
        subpixel True
        pos (0,0)
        transform_anchor True
        rotate 0
        parallel:
            ease 2 ypos -20
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
        parallel:
            pause .1
            ease 2 rotate -5
            pause .1
            ease 2 rotate 0
            repeat
    contains:

        "Jean_TJ_Body"
        subpixel True
        pos (0,0)
        transform_anchor True
        parallel:
            ease 2 ypos -20
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
    contains:

        "Jean_TJ_Head"
        subpixel True
        pos (0,0)
        transform_anchor True
        rotate 0
        parallel:
            ease 2 ypos -20
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
        parallel:
            pause .1
            ease 2 rotate -5
            pause .1
            ease 2 rotate 0
            repeat
    contains:

        "Jean_TJ_TitR"
        subpixel True
        pos (0,0)
        transform_anchor True
        parallel:
            ease 2 ypos -20
            pause .1
            ease 2 ypos -0
            pause .1
            repeat
    contains:

        subpixel True
        "Jean_TJ_ZeroCock"
        pos (0,0)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 rotate -3
            pause .1
            ease 2 rotate -5
            pause .1
            repeat
    contains:
        contains:
            "Jean_TJ_BraStretch"
        subpixel True
        pos (0,20)
        transform_anchor True
        yzoom .75
    contains:
        contains:
            "Jean_TJ_Tits"
        subpixel True
        pos (0,0)
        transform_anchor True
        parallel:
            ease 2 ypos -20
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
    contains:

        "Jean_TJ_HairTop"
        subpixel True
        pos (0,0)
        transform_anchor True
        rotate 0
        parallel:
            ease 2 ypos -20
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
        parallel:
            pause .1
            ease 2 rotate -5
            pause .1
            ease 2 rotate 0
            repeat





image Jean_TJ_1:

    contains:

        "Jean_TJ_Braback"
        subpixel True
        pos (0,140)
        transform_anchor True
        block:
            pause .1
            ease 1.9 ypos -20
            pause .4
            ease 1.8 ypos 150
            ease .5 ypos 140
            repeat
    contains:

        "Jean_TJ_HairBack"
        subpixel True
        pos (0,150)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos 0
            pause .2
            ease 2 ypos 150
            pause .5
            repeat
        parallel:
            ease 2 rotate 0
            pause .2
            ease 2 rotate -5
            pause .5
            repeat
    contains:

        "Jean_TJ_Body"
        subpixel True
        pos (0,150)
        transform_anchor True
        parallel:
            ease 2 ypos 0
            pause .2
            ease 2 ypos 150
            pause .5
            repeat
    contains:

        "Jean_TJ_Head"
        subpixel True
        pos (0,150)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos 0
            pause .2
            ease 2 ypos 150
            pause .5
            repeat
        parallel:
            ease 2 rotate 0
            pause .2
            ease 2 rotate -5
            pause .5
            repeat
    contains:

        "Jean_TJ_TitR"
        subpixel True
        pos (0,140)
        transform_anchor True
        block:
            pause .1
            ease 1.9 ypos -20
            pause .4
            ease 1.8 ypos 150
            ease .5 ypos 140
            repeat
    contains:

        subpixel True
        "Jean_TJ_ZeroCock"
        pos (0,25)
        transform_anchor True
        rotate -6
        parallel:
            ease 2 ypos 0
            pause .4
            ease 1.8 ypos 25
            pause .5
            repeat
    contains:






        contains:
            "Jean_TJ_BraStretch"
        subpixel True
        pos (0,145)
        transform_anchor True
        yzoom 1
        parallel:
            pause .1
            ease 1.9 ypos -70
            pause .4
            ease 2.3 ypos 145
            repeat
        parallel:
            pause .1
            ease 1.9 yzoom .5
            pause .4
            ease 1.8 yzoom 1
            pause .5
            repeat
    contains:
        contains:
            "Jean_TJ_Tits"
        subpixel True
        pos (0,140)
        transform_anchor True
        block:
            pause .1
            ease 1.9 ypos -20
            pause .4
            ease 1.8 ypos 150
            ease .5 ypos 140
            repeat
    contains:

        "Jean_TJ_HairTop"
        subpixel True
        pos (0,150)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos 0
            pause .2
            ease 2 ypos 150
            pause .5
            repeat
        parallel:
            ease 2 rotate 0
            pause .2
            ease 2 rotate -5
            pause .5
            repeat







image Jean_TJ_2:

    contains:

        "Jean_TJ_Braback"
        subpixel True
        pos (0,80)
        transform_anchor True
        block:
            ease .3 ypos 40
            ease .7 ypos -40
            pause .2
            ease .4 ypos 80
            repeat
    contains:

        "Jean_TJ_HairBack"
        subpixel True
        pos (0,80)
        transform_anchor True
        rotate -5
        parallel:
            ease 1 ypos -20
            pause .1
            ease .5 ypos 80
            repeat
        parallel:
            ease 1 rotate 0
            pause .1
            ease .5 rotate -5
            repeat
    contains:

        "Jean_TJ_Body"
        subpixel True
        pos (0,80)
        transform_anchor True
        parallel:
            ease 1 ypos -20
            pause .1
            ease .5 ypos 80
            repeat
    contains:

        "Jean_TJ_Head"
        subpixel True
        pos (0,80)
        transform_anchor True
        rotate -5
        parallel:
            ease 1 ypos -20
            pause .1
            ease .5 ypos 80
            repeat
        parallel:
            ease 1 rotate 0
            pause .1
            ease .5 rotate -5
            repeat
    contains:

        "Jean_TJ_TitR"
        subpixel True
        pos (0,80)
        transform_anchor True
        block:
            ease .3 ypos 40
            ease .7 ypos -40
            pause .2
            ease .4 ypos 80
            repeat
    contains:

        subpixel True
        "Jean_TJ_ZeroCock"
        pos (0,30)
        transform_anchor True
        rotate -4
        parallel:
            ease 1 ypos 0
            pause .2
            ease .4 ypos 30
            repeat
        parallel:
            ease 1 rotate -2
            pause .1
            ease .5 rotate -4
            repeat
    contains:
        contains:
            "Jean_TJ_BraStretch"
        subpixel True
        pos (0,50)
        transform_anchor True
        yzoom .75
        parallel:
            pause .2
            ease .8 ypos 0
            pause .3
            ease .3 ypos 50
            repeat
    contains:
        contains:
            "Jean_TJ_Tits"
        subpixel True
        pos (0,80)
        transform_anchor True
        block:
            ease .3 ypos 40
            ease .7 ypos -40
            pause .2
            ease .4 ypos 80
            repeat
    contains:

        "Jean_TJ_HairTop"
        subpixel True
        pos (0,80)
        transform_anchor True
        rotate -5
        parallel:
            ease 1 ypos -20
            pause .1
            ease .5 ypos 80
            repeat
        parallel:
            ease 1 rotate 0
            pause .1
            ease .5 rotate -5
            repeat






image Jean_TJ_4:

    contains:

        "Jean_TJ_Braback"
        subpixel True
        pos (0,5)
        transform_anchor True
        parallel:
            pause .2
            ease 1.9 ypos -30
            pause .2
            ease 1.9 ypos 5
            repeat
    contains:

        "Jean_TJ_HairBack"
        subpixel True
        pos (0,0)
        transform_anchor True
        rotate 0
        parallel:
            ease 2 ypos -20
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
        parallel:
            pause .1
            ease 2 rotate -5
            pause .1
            ease 2 rotate 0
            repeat
    contains:

        "Jean_TJ_Body"
        subpixel True
        pos (0,0)
        transform_anchor True
        parallel:
            ease 2 ypos -20
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
    contains:

        "Jean_TJ_Head"
        subpixel True
        pos (0,0)
        transform_anchor True
        rotate 0
        parallel:
            ease 2 ypos -20
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
        parallel:
            pause .1
            ease 2 rotate -5
            pause .1
            ease 2 rotate 0
            repeat
    contains:

        "Jean_TJ_TitR"
        subpixel True
        pos (0,5)
        transform_anchor True
        parallel:
            pause .2
            ease 1.9 ypos -30
            pause .2
            ease 1.9 ypos 5
            repeat
    contains:

        subpixel True
        "Jean_TJ_ZeroCock"
        pos (0,20)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos 0
            pause .1
            ease 2 ypos 20
            pause .1
            repeat
    contains:
        contains:
            "Jean_TJ_Tits"
        subpixel True
        pos (0,5)
        transform_anchor True
        parallel:
            pause .2
            ease 1.9 ypos -30
            pause .2
            ease 1.9 ypos 5
            repeat
    contains:

        "Jean_TJ_HairTop"
        subpixel True
        pos (0,0)
        transform_anchor True
        rotate 0
        parallel:
            ease 2 ypos -20
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
        parallel:
            pause .1
            ease 2 rotate -5
            pause .1
            ease 2 rotate 0
            repeat




image Jean_TJ_5:

    contains:

        "Jean_TJ_Braback"
        subpixel True
        pos (0,90)
        transform_anchor True
        parallel:
            pause .1
            ease 2 ypos 80
            pause .2
            ease 2 ypos 90
            pause .4
            repeat
    contains:

        "Jean_TJ_HairBack"
        subpixel True
        pos (0,130)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos 125
            pause .2
            ease 2 ypos 130
            pause .5
            repeat
        parallel:
            ease 2 rotate -5
            pause .5
            repeat
    contains:

        "Jean_TJ_Body"
        subpixel True
        pos (0,140)
        transform_anchor True
        parallel:
            ease 2 ypos 130
            pause .2
            ease 2 ypos 140
            pause .5
            repeat
    contains:

        "Jean_TJ_Head"
        subpixel True
        pos (0,130)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos 125
            pause .2
            ease 2 ypos 130
            pause .5
            repeat
        parallel:
            ease 2 rotate -5
            pause .5
            repeat
    contains:

        "Jean_TJ_TitR"
        subpixel True
        pos (0,90)
        transform_anchor True
        parallel:
            pause .1
            ease 2 ypos 80
            pause .2
            ease 2 ypos 90
            pause .4
            repeat
    contains:

        subpixel True
        "Jean_TJ_ZeroCock"
        pos (0,25)
        transform_anchor True
        rotate -10
    contains:
        contains:
            "Jean_TJ_BraStretch"
        subpixel True
        pos (-20,145)
        transform_anchor True
        yzoom 1
    contains:
        contains:
            "Jean_TJ_Tits"
        subpixel True
        pos (0,90)
        transform_anchor True
        parallel:
            pause .1
            ease 2 ypos 80
            pause .2
            ease 2 ypos 90
            pause .4
            repeat
    contains:

        "Jean_TJ_HairTop"
        subpixel True
        pos (0,130)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos 125
            pause .2
            ease 2 ypos 130
            pause .5
            repeat
        parallel:
            ease 2 rotate -5
            pause .5
            repeat













image GropeRightBreast_Jean:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (185,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30
            ease 1 rotate -60
            repeat

image GropeLeftBreast_Jean:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65
        pos (290,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 60
        block:
            ease 1 rotate 30
            ease 1 rotate 60
            repeat

image LickRightBreast_Jean:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (175,325)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (150,300)
            pause .5
            ease 1.5 rotate 30 pos (175,325)
            repeat


image LickLeftBreast_Jean:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (275,330)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (255,310)
            pause .5
            ease 1.5 rotate 30 pos (275,330)
            repeat

image GropeThigh_Jean:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (245,630)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (255,700)
            ease 1 rotate 100 pos (245,630)
            repeat

image GropePussy_Jean:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (245,560)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 pos (245,545)
                ease .75 rotate 170 pos (245,560)
            choice:
                ease .5 rotate 190 pos (245,545)
                pause .25
                ease 1 rotate 170 pos (245,560)
            repeat

image FingerPussy_Jean:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (265,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (275,615)
                pause .5
                ease 1 rotate 50 pos (265,640)
            choice:
                ease .5 rotate 40 pos (275,615)
                pause .5
                ease 1.75 rotate 50 pos (265,640)
            choice:
                ease 2 rotate 40 pos (275,615)
                pause .5
                ease 1 rotate 50 pos (265,640)
            choice:
                ease .25 rotate 40 pos (275,615)
                ease .25 rotate 50 pos (265,640)
                ease .25 rotate 40 pos (275,615)
                ease .25 rotate 50 pos (265,640)
            repeat

image Lickpussy_Jean:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (275,595)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (265,575)
            linear .5 rotate -60 pos (255,585)
            easein 1 rotate 10 pos (275,595)
            repeat

image VibratorRightBreast_Jean:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (165,310)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease .9 rotate 35 ypos 300
            pause .25
            ease .7 rotate 55 ypos 310
            pause .25
            repeat

image VibratorLeftBreast_Jean:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (270,310)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1.1 rotate 35 ypos 300
            pause .25
            ease .9 rotate 55 ypos 310
            pause .25
            repeat

image VibratorPussy_Jean:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (265,580)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 xpos 250
            pause .25
            ease 1 rotate 70 xpos 265
            pause .25
            repeat

image VibratorAnal_Jean:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (295,570)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 10
        block:
            ease 1 rotate 0 xpos 290
            pause .25
            ease 1 rotate 10 xpos 300
            pause .25
            repeat

image VibratorPussyInsert_Jean:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Jean:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0




image GirlGropeBothBreast_Jean:
    contains:
        "GirlGropeLeftBreast_Jean"
    contains:
        "GirlGropeRightBreast_Jean"

image GirlGropeLeftBreast_Jean:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (290,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate 10 pos (290,350)
            ease 1 rotate -10 pos (290,340)
            repeat

image GirlGropeRightBreast_Jean:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (170,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate -40 pos (170,350)
            ease 1 rotate -10 pos (170,340)
            repeat

image GirlGropeThigh_Jean:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        anchor (0.5,0.5)
        pos (0,0)
        alpha 0.5
        rotate 100













image GirlGropePussy_JeanSelf:
    contains:
        "GirlGropePussy_Jean"
        anchor (0.5,0.5)
        rotate -40

        pos (200,510)

image GirlGropePussy_Jean:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (240,540)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease .75 rotate 210 pos (240,535)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice:
                ease .5 rotate 210 pos (240,535)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice:
                ease .5 rotate 205 pos (240,535)
                ease .75 rotate 200 pos (240,540)
                ease .5 rotate 205 pos (240,535)
                ease .75 rotate 200 pos (240,540)
            choice:
                ease .3 rotate 205 pos (240,535)
                ease .3 rotate 200 pos (240,545)
                ease .3 rotate 205 pos (240,535)
                ease .3 rotate 200 pos (240,545)
            repeat

image GirlFingerPussy_Jean:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom .6
        pos (250,550)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease .75 rotate 210 pos (250,555)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice:
                ease .5 rotate 210 pos (250,555)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice:
                ease .5 rotate 205 ypos 565
                ease .75 rotate 200 ypos 570
                ease .5 rotate 205 ypos 565
                ease .75 rotate 200 ypos 570
            choice:
                ease .3 rotate 205 ypos 565
                ease .3 rotate 200 ypos 575
                ease .3 rotate 205 ypos 565
                ease .3 rotate 200 ypos 575
            repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
