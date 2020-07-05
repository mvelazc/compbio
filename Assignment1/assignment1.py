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
    rna = rna.rstrip("\n")
    reverse_rna = rna[::-1]
    rna1 = rna[1:]
    reverse_rna1 = rna[::-1]
    reverse_rna1 = reverse_rna1[1:]
    rna2 = rna[2:]
    reverse_rna2 = rna[::-1]
    reverse_rna2 = reverse_rna2[2:]
    rc_protein_string = ""
    protein_string = ""
    rc_protein_string1 = ""
    protein_string1 = ""
    protein_string2 = ""
    rc_protein_string2 = ""

    complement = ""

    for i in range(len(rna)):
        if rna[i] == "A":
            complement += "U"
        if rna[i] == "U":
            complement += "A"
        if rna[i] == "G":
            complement += "C"
        if rna[i] == "C":
            complement += "G"

    complement = complement[::-1]
    complement1 = complement[1:]
    complement2 = complement[2:]

    for i in range(0, len(rna)-(3+len(rna)%3), 3):
        protein_string += codon[rna[i:i+3]]
        rc_protein_string += codon[complement[i:i+3]]
        protein_string1 += codon[rna1[i:i+3]]
        rc_protein_string1 += codon[complement1[i:i+3]]
        protein_string2 += codon[rna2[i:i+3]]
        rc_protein_string2 += codon[complement2[i:i+3]]

    protein_string_s = protein_string[:protein_string.index('*')]
    protein_string1_s = protein_string1[:protein_string1.index('*')]
    protein_string2_s = protein_string2[:protein_string2.index('*')]
    rc_protein_string_s = rc_protein_string[:rc_protein_string.index('*')]
    rc_protein_string1_s = rc_protein_string1[:rc_protein_string1.index('*')]
    rc_protein_string2_s = rc_protein_string2[:rc_protein_string2.index('*')]


    print("Protein String [0]:\n" + protein_string.replace('*','') + "\n\n")
    print("Protein String [0] with stop codons:\n" + protein_string_s + "\n\n")
    print("***********************************************************************************************************************\n")
    print("Protein String [1]:\n" + protein_string1.replace('*','') + "\n\n")
    print("Protein String [1] with stop codons:\n" + protein_string1_s + "\n\n")
    print("***********************************************************************************************************************\n")
    print("Protein String [2]:\n" + protein_string2.replace('*','') + "\n\n")
    print("Protein String [2] with stop codons:\n" + protein_string2_s + "\n\n")
    print("***********************************************************************************************************************\n")
    print("REVERSE COMPLEMENT String [0]:\n" + rc_protein_string.replace('*','') + "\n\n")
    print("REVERSE COMPLEMENT String [0] with stop codons:\n" + rc_protein_string_s + "\n")
    print("***********************************************************************************************************************\n")
    print("REVERSE COMPLEMENT String [1]:\n" + rc_protein_string1.replace('*','') + "\n\n")
    print("REVERSE COMPLEMENT String [1] with stop codons:\n" + rc_protein_string1_s + "\n")
    print("***********************************************************************************************************************\n")
    print("REVERSE COMPLEMENT String [2]:\n" + rc_protein_string2.replace('*','') + "\n\n")
    print("REVERSE COMPLEMENT String [2] with stop codons:\n" + rc_protein_string2_s + "\n")



main()
