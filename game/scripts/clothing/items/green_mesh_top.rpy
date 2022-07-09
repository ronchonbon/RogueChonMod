init -1 python:

    def green_mesh_top(Owner):
        name = "green mesh top"
        string = "green_mesh_top"

        clothing_type = "top"

        dialogue_lines = {
            }

        shame = 1

        hides = []
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
