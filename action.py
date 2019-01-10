class Player(object):
    """Only player in the game"""

    def __init__(self, stamina):
        """Constructor"""
        self.is_alive = True
        self.stamina = stamina


def perform_sleep(duration):
    player.stamina = player.stamina + 2*duration
    print(player.stamina)


def perform_run(duration):
    player.stamina = player.stamina - 4*duration
    if player.stamina > 0:
        print(player.stamina)
    else:
        player.is_alive = False
        print("Game over!")


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
    while player.is_alive:
        act = input("Choose action ")
        dur = input("Choose duration ")
        player_action(act, dur)
