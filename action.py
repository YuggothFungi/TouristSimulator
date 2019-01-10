class Player(object):
    """Only one player in the game"""

    def __init__(self, stamina):
        """Constructor"""
        self.is_alive = True
        self.stamina = stamina


"""Function declaration"""
def perform_sleep(duration):
    """
    Function is called when 'sleep' action is selected
    Sleeping increases stamina
    """
    player.stamina = player.stamina + 2*duration
    print(player.stamina)


def perform_run(duration):
    """
    Function is called when 'run' action is selected
    Running decreases stamina
    """
    player.stamina = player.stamina - 4*duration
    if player.stamina > 0:
        print(player.stamina)
    else:
        player.is_alive = False
        print("Game over!")


def player_action(action, duration):
    """
    Calls perform_<action> function with hours parameter ("duration" to int)
    Need to get rid of this function after getting action-duration is changed from manual input to selection from enums
    """
    try:
        hours = int(duration)
        if action in action_map.keys():
            action_map[action](hours)
        else:
            print("Invalid action")
    except ValueError:
        print("Invalid duration")


"""?Define global variables?"""
action_map = {'sleep': perform_sleep, 'run': perform_run}


if __name__ == "__main__":
    """Create player and call for action while player is alive"""
    player = Player(50)
    while player.is_alive:
        act = input("Choose action ")
        dur = input("Choose duration ")
        player_action(act, dur)
