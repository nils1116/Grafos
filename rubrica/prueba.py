from grafo import GrafoListaConPesos

grafo01 = GrafoListaConPesos()

grafo01.adicionarVertice("Titanic")
grafo01.adicionarVertice("Son como niños")
grafo01.adicionarVertice("10 Things I Hate About You")
grafo01.adicionarVertice("Avengers")

grafo01.adicionarArco("Titanic", "Son como niños")
grafo01.adicionarArco("Son como niños", "Titanic")
grafo01.adicionarArco("Titanic", "10 Things I Hate About You")
grafo01.adicionarArco("10 Things I Hate About You", "Titanic")
grafo01.adicionarArco("Son como niños", "10 Things I Hate About You")
grafo01.adicionarArco("10 Things I Hate About You", "Son como niños")
grafo01.adicionarArco("Son como niños", "Avengers")
grafo01.adicionarArco("Avengers", "Son como niños")
grafo01.adicionarArco("10 Things I Hate About You", "Avengers")
grafo01.adicionarArco("Avengers", "10 Things I Hate About You")

print("¿Son adyacentes Titanic y Son como niños?:", grafo01.sonAdyacentes("Titanic", "Son como niños"))
print("¿Son adyacentes Titanic y Avengers?:", grafo01.sonAdyacentes("Titanic", "Avengers"))
print("¿Son adyacentes Son como niños y Avengers?:", grafo01.sonAdyacentes("Son como niños", "Avengers"))
print("¿Son adyacentes Titanic y 10 Things I Hate About You?:", grafo01.sonAdyacentes("Titanic", "10 Things I Hate About You"))

print("El grafo es:\n", grafo01, sep="")
print("Recorrido BFS desde Titanic:", grafo01.recorrerAnchura("Titanic"))
print("Todos los caminos de Titanic a Avengers:", grafo01.encontrarCaminos("Titanic", "Avengers"))

print("¿El grafo contiene un ciclo?:", grafo01.hayCiclo())
