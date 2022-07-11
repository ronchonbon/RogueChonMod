init -1 python:

    def black_bra(Owner):
        name = "black bra"
        string = "black_bra"

        clothing_type = "bra"

        dialogue_lines = {
            }

        shame = 0

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 2

        if Owner.tag == "Rogue":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "blowjob",
                "sex",
                "doggy"]
        elif Owner.tag == "Storm":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "titjob",
                "blowjob"]
        elif Owner.tag == "Mystique":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
