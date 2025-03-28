class Band:
    """Band class representing a band with musicians."""

    def __init__(self, name=""):
        """Initialize a Band with a name and empty musicians list."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        musician_strings = [str(musician) for musician in self.musicians]
        return f"{self.name} ({', '.join(musician_strings)})"

    def __repr__(self):
        """Return a string representation of the Band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to the band's list of musicians."""
        self.musicians.append(musician)

    def play(self):
        """Simulate each musician in the band playing their first instrument or needing one."""
        play_results = []
        for musician in self.musicians:
            play_results.append(musician.play())
        return '\n'.join(play_results)