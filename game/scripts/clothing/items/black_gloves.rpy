init -1 python:

    def black_gloves(Owner):
        name = "black gloves"
        string = "black_gloves"

        clothing_type = "gloves"

        dialogue_lines = {
            }

        shame = 0

        hides = []
        covers = []

        number_of_states = 1

        if Owner.tag == "Rogue":
            poses = [
                "arm pose 1",
                "arm pose 2"]
        elif Owner.tag == "Kitty":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "sex"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
