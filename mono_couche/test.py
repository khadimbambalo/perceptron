from perceptron_class import Neurone

neurone = Neurone()
neurone.poids = [0]*3
attendu = [1,0,1,0,1,1,0,1]
donnees = [
    [0,0,0],
    [0,0,1],
    [0,1,0],
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1]
]
i = 0
while( i < 8):
    neurone.apprentissage(donnees[i], attendu[i])
    print(f"Doonnees {donnees[i]}")
    print(f"valeur attendue {attendu[i]}")
    print(f"poids {neurone.poids}")
    print(f"seuil {neurone.seuil}")
    i = i + 1
    print("------------------------")



