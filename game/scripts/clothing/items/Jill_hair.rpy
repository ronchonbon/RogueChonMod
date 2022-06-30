init -1 python:

    def Jill_hair():
        name = "Jill Valentine cosplay hair"
        image_string = "Jill_hair"

        clothing_type = "hair"

        Owner_names = ["Rogue"]

        dialogue_lines = {
            }

        shame = 0

        hides = []
        covers = []

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
