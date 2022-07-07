init -1 python:

    def spiked_collar(Owner):
        name = "spiked collar"
        image_string = "spiked_collar"

        clothing_type = "neck"

        dialogue_lines = {
            }

        shame = 1

        hides = []
        covers = []

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "blowjob",
            "sex",
            "doggy"]

        return ClothingClass(Owner, name, image_string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
