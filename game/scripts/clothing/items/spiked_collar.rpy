init -1 python:

    def spiked_collar():
        name = "spiked collar"
        image_string = "spiked_collar"

        clothing_type = "neck"

        Owner_names = ["Rogue"]

        dialogue_lines = {
            "wardrobe": "Try your spiked collar on for me."
            }

        shame = 1

        hides = []
        covers = []

        number_of_states = 1

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