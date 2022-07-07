init -1 python:

    def black_harness_bra(Owner):
        name = "black harness bra"
        image_string = "black_harness_bra"

        clothing_type = "bra"

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
            "blowjob",
            "sex",
            "doggy"]

        return ClothingClass(Owner, name, image_string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
