def main():
    codon = {
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
        "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }
    file = open('rna.txt', 'r')
    rna = file.read()
    rna = rna.upper()
    rna1 = rna[1:]
    rna2 = rna[2:]
    protein_string = ""
    protein_string_s = ""
    protein_string1 = ""
    protein_string1_s = ""
    protein_string2 = ""
    protein_string2_s = ""

    for i in range(0, len(rna)-(3+len(rna)%3), 3):
        """if codon[rna[i:i+3]] == "*" :
            break"""
        protein_string += codon[rna[i:i+3]]

    for i in range(0, len(rna1)-(3+len(rna1)%3), 3):
        """if codon[rna1[i:i+3]] == "*" :
            break"""
        protein_string1 += codon[rna1[i:i+3]]
    
    for i in range(0, len(rna2)-(3+len(rna2)%3), 3):
        """if codon[rna2[i:i+3]] == "*" :
            break"""
        protein_string2 += codon[rna2[i:i+3]]

    protein_string_s = protein_string[:protein_string.index('*')]
    protein_string1_s = protein_string1[:protein_string1.index('*')]
    protein_string2_s = protein_string2[:protein_string2.index('*')]


    print("Protein String: ", protein_string, "\n")
    print("Protein String: ", protein_string_s, "\n")
    print("Protein String: ", protein_string1, "\n")
    print("Protein String: ", protein_string1_s, "\n")
    print("Protein String: ", protein_string2, "\n")
    print("Protein String: ", protein_string2_s, "\n")

    


main()