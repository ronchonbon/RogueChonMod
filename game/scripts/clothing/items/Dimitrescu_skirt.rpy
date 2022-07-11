init -1 python:

    def Dimitrescu_skirt(Owner):
        name = "Lady Dimitrescu's skirt"
        string = "Dimitrescu_skirt"

        clothing_type = "skirt"

        dialogue_lines = {
            }

        shame = 0

        hides = ["pussy"]
        covers = ["pussy", "thighs"]

        number_of_states = 2

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "footjob",
            "sex",
            "doggy"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
