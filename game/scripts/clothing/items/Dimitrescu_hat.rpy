init -1 python:

    def Dimitrescu_hat(Owner):
        name = "Lady Dimitrescu's hat"
        string = "Dimitrescu_hat"

        clothing_type = "face_outer_accessory"

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
            "titjob",
            "blowjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
