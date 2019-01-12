class Player(object):
    """Only one player in the game"""

    def __init__(self, stamina, satiety):
        """Constructor"""
        self.is_alive = True
        self.stamina = stamina
        self.satiety = satiety


def player_alive(player_check):
    if (player_check.satiety or player_check.stamina) <= 0:
        player_check.is_alive = False
        print("Game over!")


def update_player(player_update):
    print(player_update.stamina)
    print(player_update.satiety)


def perform_sleep(duration):
    """
    Function is called when 'sleep' action is selected
    Sleeping increases stamina
    """
    player.stamina = player.stamina + 4*duration
    player.satiety = player.satiety - 2*duration

    player_alive(player)
    if player.is_alive:
        update_player(player)


def perform_run(duration):
    """
    Function is called when 'run' action is selected
    Running decreases stamina
    """
    player.stamina = player.stamina - 4*duration
    player.satiety = player.satiety - 4*duration

    player_alive(player)
    if player.is_alive:
        update_player(player)


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
    player = Player(50.0, 50.0)
    while player.is_alive:
        act = input("Choose action ")
        dur = input("Choose duration ")
        player_action(act, dur)
