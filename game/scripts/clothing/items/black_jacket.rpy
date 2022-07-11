init -1 python:

    def black_jacket(Owner):
        name = "black jacket"
        string = "black_jacket"

        clothing_type = "jacket"

        dialogue_lines = {
            }

        shame = 0

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 2

        if Owner.tag == "Emma":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob"]
        elif Owner.tag == "Storm":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "titjob",
                "blowjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
