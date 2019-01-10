class Player(object):
    """Only player in the game"""

    def __init__(self, stamina):
        """Constructor"""
        # self.isalive = True
        self.stamina = stamina


def perform_sleep(duration):
    player.stamina = player.stamina + 2*duration
    print(player.stamina)


def perform_run(duration):
    player.stamina = player.stamina - 4*duration
    print(player.stamina)


def player_action(action, duration):
    try:
        hours = int(duration)
        if action in action_map.keys():
            action_map[action](hours)
    except ValueError:
        print("You made a mistake")

action_map = {'sleep': perform_sleep, 'run': perform_run}

if __name__ == "__main__":
    player = Player(50)
    act = input("Choose action ")
    dur = input("Choose duration ")
    player_action(act, dur)
