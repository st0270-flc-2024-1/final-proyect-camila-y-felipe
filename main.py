from collections import defaultdict

# Function to compute the FIRST set of a non-terminal symbol
def compute_first(symbol, productions, first, visited):
    if symbol in visited:
        return first[symbol]
    
    visited.add(symbol)
    
    if symbol not in productions:  # If it's a terminal, it's already in FIRST
        first[symbol].add(symbol)
        visited.remove(symbol)
        return first[symbol]
    
    for production in productions[symbol]:
        for i, char in enumerate(production):
            if char.isupper():  # char is a non-terminal
                char_first = compute_first(char, productions, first, visited)
                first[symbol].update(char_first - {'e'})
                if 'e' not in char_first:
                    break
            else:  # char is a terminal
                first[symbol].add(char)
                break
        else:
            first[symbol].add('e')
    
    visited.remove(symbol)
    return first[symbol]

# Function to compute the FIRST set of a string
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

# Function to compute the FOLLOW set of a non-terminal symbol
def compute_follow(symbol, productions, first, follow, start_symbol):
    if not follow[symbol]:
        if symbol == start_symbol:
            follow[symbol].add('$')
    
        for lhs, rhs_list in productions.items():
            for rhs in rhs_list:
                for i, char in enumerate(rhs):
                    if char == symbol:
                        follow_suffix = rhs[i + 1:]
                        first_of_suffix = compute_first_string(follow_suffix, productions, first)
                        follow[symbol].update(first_of_suffix - {'e'})
                        if 'e' in first_of_suffix or not follow_suffix:
                            follow[symbol].update(compute_follow(lhs, productions, first, follow, start_symbol))
    
    return follow[symbol]

# Main function
def main():
    # Read the grammar from a file
    with open('grammar.txt', 'r') as file:
        grammar = file.read()

    # Parse the grammar
    productions = defaultdict(list)
    for line in grammar.strip().split('\n'):
        lhs, rhs = line.split('->')
        lhs = lhs.strip()
        rhs_productions = rhs.strip().split('|')
        for production in rhs_productions:
            productions[lhs].append(production.strip().split())

    # Initialize FIRST and FOLLOW sets
    first = defaultdict(set)
    follow = defaultdict(set)
    
    # Compute FIRST sets for all non-terminals
    visited = set()
    for non_terminal in productions:
        compute_first(non_terminal, productions, first, visited)
    
    # Compute FOLLOW sets for all non-terminals
    start_symbol = 'S'
    for non_terminal in productions:
        compute_follow(non_terminal, productions, first, follow, start_symbol)
    
    # Save the FIRST and FOLLOW sets to an output file
    with open('output.txt', 'w') as output_file:
        output_file.write("First sets:\n")
        for non_terminal, first_set in sorted(first.items()):
            if non_terminal.isupper():  # Only print non-terminals
                output_file.write(f"First({non_terminal}) = {{ {', '.join(sorted(first_set))} }}\n")
        
        output_file.write("\nFollow sets:\n")
        for non_terminal, follow_set in sorted(follow.items()):
            if non_terminal.isupper():  # Only print non-terminals
                output_file.write(f"Follow({non_terminal}) = {{ {', '.join(sorted(follow_set))} }}\n")

if __name__ == "__main__":
    main()
