from collections import defaultdict

# Función para calcular el conjunto FIRST de un símbolo no terminal
def compute_first(symbol, productions, first, visited):
    if symbol in visited:
        return first[symbol]
    
    visited.add(symbol)
    
    for production in productions[symbol]:
        if production == ['e']:  # Regla 1: Si α ≡ ∈
            first[symbol].add('e')
        else:
            for char in production:
                if char.isupper():  # char es un No Terminal
                    char_first = compute_first(char, productions, first, visited)
                    first[symbol].update(char_first - {'e'})
                    if 'e' not in char_first:
                        break
                else:  # Regla 2: Si α ≡ a
                    first[symbol].add(char)
                    break
            else:
                first[symbol].add('e')
    
    return first[symbol]

# Función para calcular el conjunto FIRST de una cadena
def compute_first_string(string, productions, first):
    result = set()
    for symbol in string:
        if symbol.isupper():
            result.update(first[symbol] - {'e'})
            if 'e' not in first[symbol]:
                break
        else:
            result.add(symbol)
            break
    else:
        result.add('e')
    
    return result

# Función para calcular el conjunto FOLLOW de un símbolo no terminal
def compute_follow(productions, first, follow, start_symbol):
    follow[start_symbol].add('$')
    
    updated = True
    while updated:
        updated = False
        for lhs, rhs_list in productions.items():
            for rhs in rhs_list:
                follow_temp = follow[lhs].copy()
                for i in reversed(range(len(rhs))):
                    symbol = rhs[i]
                    if symbol.isupper():
                        if follow_temp - follow[symbol]:
                            follow[symbol].update(follow_temp)
                            updated = True
                        if 'e' in first[symbol]:
                            follow_temp.update(first[symbol] - {'e'})
                        else:
                            follow_temp = first[symbol]
                    else:
                        follow_temp = {symbol}
    
    return follow

# Función principal
def main():
    file_path = 'grammar.txt'  # Nombre del archivo que contiene la gramática
    
    # Leer la gramática desde el archivo
    productions = defaultdict(list)
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if '->' in line:
                lhs, rhs = line.split('->')
                lhs = lhs.strip()
                rhs_productions = rhs.strip().split('|')
                for production in rhs_productions:
                    productions[lhs].append(production.strip().split())

    # Inicializar conjuntos FIRST y FOLLOW
    first = defaultdict(set)
    follow = defaultdict(set)
    
    # Calcular FIRST para todos los no terminales
    visited = set()
    for non_terminal in productions:
        compute_first(non_terminal, productions, first, visited)
    
    # Calcular FOLLOW para todos los no terminales
    start_symbol = 'S'
    follow = compute_follow(productions, first, follow, start_symbol)
    
    # Imprimir los conjuntos FIRST y FOLLOW
    print("First sets:")
    for non_terminal, first_set in sorted(first.items()):
        if non_terminal.isupper():  # Solo imprimir no terminales
            print(f"First({non_terminal}) = {{ {', '.join(sorted(first_set))} }}")
    
    print("\nFollow sets:")
    for non_terminal, follow_set in sorted(follow.items()):
        if non_terminal.isupper():  # Solo imprimir no terminales
            print(f"Follow({non_terminal}) = {{ {', '.join(sorted(follow_set))} }}")

if __name__ == "__main__":
    main()