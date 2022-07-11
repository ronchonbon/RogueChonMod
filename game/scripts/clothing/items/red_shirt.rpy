init -1 python:

    def red_shirt(Owner):
        name = "red shirt"
        string = "red_shirt"

        clothing_type = "top"

        dialogue_lines = {
            }

        shame = 0

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 2

        if Owner.tag == "Kitty":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "blowjob",
                "sex",
                "doggy"]
        elif Owner.tag == "Jubes":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "titjob",
                "blowjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
