init -1 python:

    def jean_shorts(Owner):
        name = "jean shorts"
        string = "jean_shorts"

        clothing_type = "pants"

        dialogue_lines = {
            }

        shame = 1

        hides = ["pussy"]
        covers = ["pussy"]

        if Girl in [RogueX, LauraX]:
            number_of_states = 1
        elif Girl == JubesX:
            number_of_states = 2

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
