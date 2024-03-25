import sys

from heap import *
from search import *
from sort import *
from utils import *

 
print("*** Bienvenue dans Search&Sort ***\n")
print("\nObjectif :\n\
    - Ce programme offre la possibilité de faire une recherche dans un tableau de réels trié avec l'algorithme de recherhce par dichotomie.\
    - Ce dernier offre également la possibilité de trier un tableau de réels avec les tris rapide et par tas.\n")

while True:
    operation = input(f"\nEntrez l'opération à éffectuer :\n\
    - 1: Recherche dichotomique\n\
    - 2: Tri rapide\n\
    - 3: Tri par tas\n\
Réponse ({stop_message}): ")
    
    control_exit(operation)
    
    if operation not in ('1', '2', '3'):
        print("\n!Vous devez entrer un chiffre entre 1, 2 et 3!\n")
        continue
    
    break

if operation == '1':
    print("\n!Le tableau à entrer doit être trié, sinon vous pourrez avoir des résultats érronés!\n")
else:
    while True:
        ordre = input(f"\nEntrez l'ordre du tri ('c' pour croissant et 'd' pour décroissant) ; {stop_message}) : ").lower()
        
        control_exit(ordre)
        
        if ordre not in ('c', 'd'):
            print("\n!Vous n'avez pas entré un ordre valide ('c' ou 'd')!\n")
            continue
        
        ordre = 0 if ordre == 'c' else 1
        break
    
    
while True:
    tableau = input(f"\nEntrez les éléments du tableau sous la forme t1,t2,...,tn (sans espace ; la virgule des réels est le '.' ; {stop_message}) : ").split(',')
    
    control_exit(tableau)
    
    try:
        tableau = [float(x) for x in tableau]
    except ValueError:
        print("\n!Au moins une des valeurs entrée n'est pas un réel!\n")
        continue
    
    break

if operation == '1':
    while True:
        element = input(f"\nEntrez l'élément à rechercher dans le tableau ({stop_message}): ")
        
        control_exit(element)
        
        try:
            element = float(element)
        except ValueError:
            print("\n!La valeur entrée n'est pas un réel!\n")
            continue
    
        break 
    
    position = dich_search(element, tableau)
    if  position == -1:
        print(f"\nL'élément '{element}' n'est pas dans le tableau donné.\n")
    else:
        print(f"\nL'élément '{element}' est bien pas dans le tableau donné, à la position '{position+1}'.\n")
        
elif operation == '2':
    quick_sort(tableau, order=ordre)
    print(f"\nLe tableau trié avec le tri rapide est: {tableau}.\n")
    
else: # operation == 3
    heap = Heap(tableau)
    heap.sort(order=ordre)
    print(f"\nLe tableau trié avec le tris par tas est: {tableau}\n")
    print("\nLe tableau trié sous forme de tas se présente comme suit:\n")
    print(heap)
    
bye()
               