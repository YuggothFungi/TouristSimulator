class Player(object):
    """Only one player in the game"""

    def __init__(self, stamina, satiety):
        """Constructor"""
        self.is_alive = True
        self.stamina = stamina
        self.satiety = satiety


def player_alive(player_check):
    if player_check.satiety <= 0.0 or player_check.stamina <= 0.0:
        player_check.is_alive = False
        print("Game over!")


def update_player(player_update):
    print("Stamina: " + str(player_update.stamina))
    print("Satiety: " + str(player_update.satiety))


def perform_sleep(duration):
    """
    Function is called when 'sleep' action is selected
    Sleeping increases stamina
    """
    player.stamina = player.stamina + 4 * duration
    player.satiety = player.satiety - 2 * duration

    player_alive(player)
    if player.is_alive:
        update_player(player)


def perform_run(duration):
    """
    Function is called when 'run' action is selected
    Running decreases stamina
    """
    player.stamina = player.stamina - 4 * duration
    player.satiety = player.satiety - 4 * duration

    player_alive(player)
    if player.is_alive:
        update_player(player)


def perform_eat(meal_type):
    """
    Function is called when 'eat' action is selected
    Eating increases satiety
    To do: eating should take fixed duration depending on meal_type
    """
    player.satiety = player.satiety + meal_map[meal_type]
    update_player(player)


def player_action(action, duration=None, meal_type=None):
    """
    Calls perform_<action> function with hours parameter ("duration" to int)
    Need to get rid of this function after getting action-duration is changed from manual input to selection from enums
    """
    if action in action_map.keys():
        if duration is not None:
            try:
                hours = int(duration)
                action_map[action](hours)
            except ValueError:
                print("Invalid duration")

        if meal_type is not None:
            if meal_type in meal_map.keys():
                action_map[action](meal_type)
            else:
                print("Invalid action type")
    else:
        print("Invalid action")


"""?Define global variables?"""
action_map = {'sleep': perform_sleep, 'run': perform_run, 'eat': perform_eat}
meal_map = {'fast': 10.0, 'break': 10.0, 'lunch': 15.0, 'dinner': 20.0, 'feast': 30.0}

if __name__ == "__main__":
    """Create player and call for action while player is alive"""
    player = Player(50.0, 50.0)
    while player.is_alive:
        act = input("Choose action ")
        if act == 'eat':
            eat = input("Choose meal type ")
            player_action(act, None, eat)
        else:
            dur = input("Choose duration ")
            player_action(act, dur, None)
