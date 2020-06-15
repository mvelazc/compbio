from Bio.Seq import Seq
from Bio.Alphabet import generic_rna

def main():
    file = open('rna.txt', 'r')
    rna = file.read()
    rna = rna.upper()
    rna = rna.rstrip("\n")

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

    rc_seq = Seq(complement[:-2], generic_rna)
    rc_seq1 = Seq(complement[1:-1], generic_rna)
    rc_seq2 = Seq(complement[2:], generic_rna)

    seq = Seq(rna[:-2], generic_rna)
    seq1 = Seq(rna[1:-1], generic_rna)
    seq2 = Seq(rna[2:], generic_rna)

    print("Protein String [0]:\n" + seq.translate() + "\n")
    print("Protein String [0] With Stop Codon:\n" + seq.translate(to_stop=True) + "\n")
    print("***********************************************************************************************************************\n")

    print("Protein String [1]:\n" + seq1.translate() + "\n")
    print("Protein String [1] With Stop Codon:\n" + seq1.translate(to_stop=True) + "\n")
    print("***********************************************************************************************************************\n")

    print("Protein String [2]:\n" + seq2.translate() + "\n")
    print("Protein String [2] With Stop Codon:\n" + seq2.translate(to_stop=True) + "\n")
    print("***********************************************************************************************************************\n")

    print("REVERSE COMPLEMENT String [0]:\n" + rc_seq.translate() + "\n")
    print("REVERSE COMPLEMENT String [0] With Stop Codon:\n" + rc_seq.translate(to_stop=True) + "\n")
    print("***********************************************************************************************************************\n")

    print("REVERSE COMPLEMENT String [1]:\n" + rc_seq1.translate() + "\n")
    print("REVERSE COMPLEMENT String [1] With Stop Codon:\n" + rc_seq1.translate(to_stop=True) + "\n")
    print("***********************************************************************************************************************\n")

    print("REVERSE COMPLEMENT String [2]:\n" + rc_seq2.translate() + "\n")
    print("REVERSE COMPLEMENT String [2] With Stop Codon:\n" + rc_seq2.translate(to_stop=True) + "\n")

main()
