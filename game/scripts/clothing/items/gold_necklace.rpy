init -1 python:

    def gold_necklace(Owner):
        name = "gold necklace"
        string = "gold_necklace"

        clothing_type = "neck"

        dialogue_lines = {
            }

        shame = 0

        hides = []
        covers = []

        number_of_states = 1

        if Owner.tag == "Kitty":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "blowjob",
                "sex"]
        elif Owner.tag == "Storm":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "titjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
