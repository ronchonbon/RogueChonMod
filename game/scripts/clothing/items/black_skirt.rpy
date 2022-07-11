init -1 python:

    def black_skirt(Owner):
        name = "black skirt"
        string = "black_skirt"

        clothing_type = "skirt"

        dialogue_lines = {
            }

        shame = 0

        hides = ["pussy"]
        covers = ["pussy"]

        number_of_states = 2

        if Owner.tag == "Rogue":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "blowjob",
                "sex",
                "doggy"]
        elif Owner.tag == "Laura":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "sex"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
