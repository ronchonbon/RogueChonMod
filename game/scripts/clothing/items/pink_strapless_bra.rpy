init -1 python:

    def pink_strapless_bra(Owner):
        name = "pink strapless bra"
        string = "pink_strapless_bra"

        clothing_type = "bra"

        dialogue_lines = {
            }

        shame = 0

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 2

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "blowjob",
            "sex",
            "doggy"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
