init -1 python:

    def black_bikini_bottoms(Owner):
        name = "black bikini bottoms"
        string = "black_bikini_bottoms"

        clothing_type = "underwear"

        dialogue_lines = {
            }

        shame = 0

        hides = ["pussy"]
        covers = ["pussy"]

        if Owner.tag in ["Laura", "Jean"]:
            number_of_states = 2
        elif Owner.tag == "Storm":
            number_of_states = 3

        if Owner.tag == "Laura":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "sex"]
        elif Owner.tag in ["Jean", "Storm"]:
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
