init -1 python:

    def yellow_jacket(Owner):
        name = "yellow jacket"
        string = "yellow_jacket"

        clothing_type = "yellow_jacket"

        dialogue_lines = {
            }

        shame = 0

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 3

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "titjob",
            "blowjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
