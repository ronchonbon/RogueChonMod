init -1 python:

    def black_bikini_top(Owner):
        name = "black bikini top"
        string = "black_bikini_top"

        clothing_type = "bra"

        dialogue_lines = {
            }

        shame = 0

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 2

        if Owner.tag == "Laura":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "sex"]
        elif Owner.tag == "Storm":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "titjob",
                "blowjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
