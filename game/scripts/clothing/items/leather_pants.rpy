init -1 python:

    def leather_pants(Owner):
        name = "leather pants"
        string = "leather_pants"

        clothing_type = "pants"

        dialogue_lines = {
            }

        shame = 0

        hides = ["pussy"]
        covers = ["pussy", "thighs"]

        if Girl in [EmmaX, LauraX]:
            number_of_states = 1
        elif Girl == JubesX:
            number_of_states = 2

        if Girl in [EmmaX, JubesX]:
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob"]
        elif Girl == LauraX:
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "sex"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
