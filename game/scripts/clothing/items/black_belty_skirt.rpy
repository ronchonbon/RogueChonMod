init -1 python:

    def black_belty_skirt(Owner):
        name = "black belty skirt"
        image_string = "black_belty_skirt"

        clothing_type = "skirt"

        dialogue_lines = {
            }

        shame = 0

        hides = ["pussy"]
        covers = ["pussy"]

        number_of_states = 2

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "blowjob",
            "sex",
            "doggy"]

        return ClothingClass(Owner, name, image_string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
