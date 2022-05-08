
class Neurone():
    poids = []
    seuil = 2

    def calculY(self, entree:[]):
        y = 0
        for i in (0, len(entree)-1):
            y = y + self.poids[i]*entree[i]
        return y

    def determinerZ(self, y):
        if (y - self.seuil) < 0:
            return 0
        else:
            return 1

    def apprentissage(self, entree:[], val_attendu):
        y = self.calculY(entree)
        val_sortie = self.determinerZ(y)
        if (val_attendu == val_sortie):
            print("true")
        else:
            print("false")
            for i in (0, len(entree)-1):
                self.poids[i] = self.poids[i] + (val_attendu - val_sortie)*entree[i]
            self.seuil = self.seuil - (val_attendu - val_sortie)