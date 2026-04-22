import random

# La base de données d'idées de ton Agent
projects_matrix = {
    "Physique_L1": ["Simulateur de chute libre avec frottements", "Calculateur de vecteurs force", "Optique : Loi de Snell-Descartes"],
    "Informatique": ["Mini explorateur de fichiers", "Compilateur de langage custom", "Gestionnaire de processus"],
    "IA_Data": ["Visualiseur de données météo", "Petit neurone artificiel (Perceptron)", "Analyseur de texte"],
    "Reseaux": ["Scanner de ports IP", "Chat local Client/Serveur", "Moniteur de ping"]
}

def get_random_project():
    domain = random.choice(list(projects_matrix.keys()))
    task = random.choice(projects_matrix[domain])
    return domain, task

if __name__ == "__main__":
    # Pour l'instant on teste juste la sortie
    d, t = get_random_project()
    print(f"PROJET_DU_JOUR={d}-{t.replace(' ', '_')}")
