[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/hBnzrcca)
# Final Project - First and Follow
- By: Felipe Castro Jaimes, C.C. 1034988011 and Camila Martinez, C.C. 1027802537
## Version of Operating System, Compiler and tools:
- Microsoft Windows 11 - Version 10.0.22631 Build 22631
- Python 3.12.2
## Instructions to run the tests
For running either the tests with the files in this repository, or your own defined files, follow these instructions:
- Clone this repository or download it and each useful file for the execution (main.py, grammar.txt).
- Check that you have the grammar you want to test in the grammar.txt and in the correct form.
- Be sure that the name of the txt files are the same name files you're calling on the main method for the reading and writing.
- Run the program with the following command ($ python main.py).
## The convention defined for the input/output:
- For the input we defined that the program will read a txt file which the user can edit for adding its own grammar. The form of the grammar will be as the one in the example (grammar.txt).  
- For the output we decided to define another txt file called output.txt, being the result, the sets of First and Follow of a grammar.
## Implementation:
Note: Before implementing the code it is necessary to import "defaultdict" from the "collections" module, to initialize lists or empty sets with a default value.
- Compute FIRST
  - The compute first function is implemented to compute the first set of a non-terminal symbol. If the symbol has already been visited, it returns its First sets, if it is a terminal it is added to its own First set, but if it is a non-terminal, it iterates over its productions and computes the First set. If all the symbols in the productions can be derived in epsilon, it is added to the First set.
  - The function compute_first_string is implemented to compute the First set of a string of symbols, iterating over each one. If it is a non-terminal its First set, without epsilon, is added to the result; if it is terminal it is added directly to the result; and if they all derive in epsilon then this is added as well.
- Compute FOLLOW
  - The compute_follow function is implemented to compute the Follow set of a non-terminal symbol. If the Follow set of the symbol is empty then it is initialized with "$". We iterate over the productions to find occurrences of the symbol; we compute the First set of the suffix following the symbol in the production, add the First set of the suffix to the Follow set of the symbol, not including epsilon, and if the First set of the suffix contains epsilon or the suffix is empty, we add the Follow set of the left-hand side of the production to the Follow set of the symbol.
- Grammar processing
  - The Main function is implemented to read the grammar from a txt file, calculate the First and Follow sets and save them to an output file. First e reads the grammar from a file, then we store the productions in a "defaultdict" of lists, initialize the sets First and Follow, compute for set for all non-terminals and save the sets to an output file.
## References:
- Mohammad Shakirul Islam - Find First and follow of a grammar in C++ (Youtube Video, Last Updated: 2018)
https://www.youtube.com/watch?v=sD1CdcpADgs
- fazeela - find First and Follow of any given grammar CD Lab (Youtube Video, Last Updated:2021) 
https://www.youtube.com/watch?v=w7yZkLihjGE&t=11s
- MikeDevide Github - First Follow
https://mikedevice.github.io/first-follow/ | https://github.com/MikeDevice/first-follow
- United States Naval Academy - First+Follow+Predict Calculator 
https://www.usna.edu/Users/cs/wcbrown/courses/F20SI413/firstFollowPredict/ffp.html
- Andrés Sicard Ramírez - ST0270 Lenguajes Formales y Compiladores (2024-1) - Análisis Sintáctico PDF
http://www1.eafit.edu.co/asr/cursos/st0270-lenguajes-formales-y-compiladores/diapositivas/analisis-sintactico.pdf
- GateVidyalay - First and Follow | Solved Examples (Last Updated: 2020) 
https://www.gatevidyalay.com/first-and-follow-compiler-design/
- HackingOff - Generate Predict, First, and Follow Sets from EBNF (Extended Backus Naur Form) Grammar (Last Updated : 2012) 
http://hackingoff.com/compilers/predict-first-follow-set
- AI ChatGPT 3.5 (OpenAI) (for testing and some debbuging problems)
- Aho, Alfred V., Monica S. Lam, Ravi Sethi and Jeffrey D. Ullman [1986] (2006). Compilers:
Principles, Techniques, & Tools. 2nd ed. Addison-Wesley. [Section 4.4.2]
- GeeksforGeeks. (2023, 28 febrero). Program to calculate First and Follow sets of given grammar. GeeksforGeeks. https://www.geeksforgeeks.org/program-calculate-first-follow-sets-given-grammar/
