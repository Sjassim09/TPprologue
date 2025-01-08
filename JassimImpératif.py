def saisir_donnees():
    """
    Fonction pour saisir les noms et les notes des étudiants.
    Renvoie deux listes : noms et notes.
    """
    noms = []
    notes = []
    nombre_etudiants = int(input("Combien d'étudiants souhaitez-vous saisir ? "))

    for i in range(nombre_etudiants):
        nom = input(f"Nom de l'étudiant {i + 1} : ")
        note = float(input(f"Note de {nom} : "))
        noms.append(nom)
        notes.append(note)

    return noms, notes

def calculer_moyenne(notes):
    """
    Calcule la moyenne d'une liste de notes.
    """
    return sum(notes) / len(notes) if notes else 0

def afficher_repartition(noms, notes):
    """Affiche les étudiants ayant réussi et ceux en échec."""
    reussite = [noms[i] for i in range(len(notes)) if notes[i] >= 10]
    echec = [noms[i] for i in range(len(notes)) if notes[i] < 10]
    print("Étudiants ayant réussi :", ", ".join(reussite) if reussite else "Aucun")
    print("Étudiants en échec :", ", ".join(echec) if echec else "Aucun")

def meilleure_note(noms, notes):
    """Affiche le nom de l'étudiant ayant obtenu la meilleure note."""
    if notes:
        index_meilleure_note = notes.index(max(notes))
        print(f"La meilleure note est de {max(notes)} obtenue par {noms[index_meilleure_note]}.")
    else:
        print("Aucune note saisie.")

def meilleure_note(noms, notes):
    """Trouve l'étudiant avec la meilleure note et l'affiche."""
    index_max = notes.index(max(notes))
    print(f"L’étudiant ayant la meilleure note est {noms[index_max]} avec {notes[index_max]}.")

if __name__ == "__main__":
    noms, notes = saisir_donnees()
    print("\nDonnées saisies :")
    print("Noms :", noms)
    print("Notes :", notes)

    moyenne = calculer_moyenne(notes)
    print(f"La moyenne de la classe est de {moyenne:.2f}.")
    afficher_repartition(noms, notes)
    meilleure_note(noms, notes)