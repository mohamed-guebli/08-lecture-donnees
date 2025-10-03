#### Imports et définition des variables globales
FILENAME = "listes.csv"

#### Fonctions secondaires
def read_data(filename):
    """Retourne le contenu du fichier <filename> sous forme de liste de listes d'entiers.
    Args:
        filename (str): nom du fichier à lire
    Returns:
        list: le contenu du fichier (1 liste par ligne)
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
    data = []
    for line in lines:
        row = [int(x) for x in line.strip().split(';')]  # Remplace ',' par ';'
        data.append(row)
    return data

def get_list_k(data, k):
    """Retourne la kième liste de la liste de listes.
    Args:
        data (list): liste de listes
        k (int): indice de la liste à retourner
    Returns:
        list: la kième liste
    """
    return data[k]

def get_first(l):
    """Retourne le premier élément de la liste.
    Args:
        l (list): liste d'entiers
    Returns:
        int: premier élément de la liste
    """
    return l[0]

def get_last(l):
    """Retourne le dernier élément de la liste.
    Args:
        l (list): liste d'entiers
    Returns:
        int: dernier élément de la liste
    """
    return l[-1]

def get_max(l):
    """Retourne le maximum de la liste.
    Args:
        l (list): liste d'entiers
    Returns:
        int: maximum de la liste
    """
    return max(l)

def get_min(l):
    """Retourne le minimum de la liste.
    Args:
        l (list): liste d'entiers
    Returns:
        int: minimum de la liste
    """
    return min(l)

def get_sum(l):
    """Retourne la somme de la liste.
    Args:
        l (list): liste d'entiers
    Returns:
        int: somme de la liste
    """
    return sum(l)

#### Fonction principale
def main():
    data = read_data(FILENAME)
    print("Contenu du fichier :")
    for i, l in enumerate(data):
        print(f"Ligne {i}: {l}")

    k = 0  # Exemple : on prend la première ligne
    print(f"\nListe à l'indice {k}: {get_list_k(data, k)}")
    print(f"Premier élément: {get_first(get_list_k(data, k))}")
    print(f"Dernier élément: {get_last(get_list_k(data, k))}")
    print(f"Maximum: {get_max(get_list_k(data, k))}")
    print(f"Minimum: {get_min(get_list_k(data, k))}")
    print(f"Somme: {get_sum(get_list_k(data, k))}")

if __name__ == "__main__":
    main()
