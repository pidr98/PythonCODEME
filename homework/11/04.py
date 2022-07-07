class Ssaki():
    def __init__(self, name, legs, hair, spine):
        self.name = name
        self.legs = legs
        self.hair = hair
        self.spine = spine

    def why_ssak(self):
        print(f'{self.name} - {self.legs}, {self.hair}, {self.spine}')

ssak = Ssaki('Ssaki', 4, True, True)
wilk = Ssaki('Wilk', 4, True, True)
kon = Ssaki('Koń', 4, True, True)
ssak.why_ssak()
wilk.why_ssak()
kon.why_ssak()