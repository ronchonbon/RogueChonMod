init -1 python:

    def white_choker(Owner):
        name = "white choker"
        image_string = "white_choker"

        clothing_type = "neck"

        dialogue_lines = {
            }

        shame = 0

        hides = []
        covers = []

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "blowjob",
            "doggy"]

        return ClothingClass(Owner, name, image_string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
