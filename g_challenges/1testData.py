testGraph = Graph([
    Node("Alice", ["Monty", "Bob", "Felicia", "Dan"]),
    Node("Monty", ["Alice"]),
    Node("Bob", ["Alice", "Felicia"]),
    Node("Felicia", ["Alice", "Bob", "George", "Tien"]),
    Node("Dan", ["Alice", "Lloyd"]),
    Node("Lloyd", ["Dan", "George", "Henry"]),
    Node("Henry", ["Lloyd", "George"]),
    Node("George", ["Lloyd", "Henry", "Tien", "Felicia"]),
    Node("Adolf", ["Adolf"]),
    Node("Tien", ["Tri", "George", "Felicia", "Angie"]),
    Node("Tri", ["Tien", "Angie"]),
    Node("Angie", ["Tri", "Tien"])])
