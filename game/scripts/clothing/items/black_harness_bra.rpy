init -1 python:

    def black_harness_bra():
        name = "black harness bra"
        image_string = "black_harness_bra"

        clothing_type = "bra"

        Owner_names = ["Rogue"]

        dialogue_lines = {
            }

        shame = 2

        hides = []
        covers = ["breasts"]

        number_of_states = 2

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "titjob",
            "footjob",
            "blowjob",
            "sex",
            "doggy"]

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, Owner_names, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
