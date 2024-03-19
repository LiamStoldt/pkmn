"""Module and class for pokemon handling"""


class Stats:
    """Stats object for holding standard pokemon stats"""

    def __init__(self):
        self.max_hp: int = 0
        self.attack: int = 0
        self.defence: int = 0
        self.s_attack: int = 0
        self.s_defence: int = 0
        self.speed: int = 0


class Pokemon:
    """The pokmeon class"""

    def __init__(self):
        """Initialise all starting variables"""

        # organise stats
        self.stats = Stats()
        self.hp: int = 0

        # moveset
        self.moves = [None, None, None, None]

        # status conditions
        self.status_condition = None

        # xp and levelling
        self.xp: int = 0
        self.xp_to_next_level: int = 0
        self.level: int = 1
        self.level_to_evolution: int = None
        self.evolution_pokemon: Pokemon = None

    def take_damage(self, amount: int):
        """Make this pokemon take damage"""

        self.hp -= amount

    def add_status_condition(self, condition):
        """Add a status condition to this pokemon"""

        self.status_condition = condition
    
    def remove_status_condition(self):
        """Remove a statust condition from this pokemon"""

        self.status_condition = None
