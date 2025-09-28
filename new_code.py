def add_numbers(a, b):
    return a + b

def jiu_jitsu_move(number):
    moves = {
        1: "Double leg / Takedown",
        2: "Pull guard / Sit to guard",
        3: "Scissor sweep / Basic sweep",
        4: "Pass guard → Side control",
        5: "Mount → Hold",
        6: "Armbar (from mount or guard)",
        7: "Americana / Keylock (from mount/side)",
        8: "Guillotine choke",
        9: "Rear-naked choke / Back control finish"
    }
    return moves.get(number, "Unknown move")

