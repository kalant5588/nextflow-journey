# fasta_stats_bio.py - FASTA stats using Biopython
from Bio import SeqIO

filename = "proteins.fasta"

print("Analysing", filename)
for record in SeqIO.parse(filename, "fasta"):
    print(record.id, "-> length", len(record.seq))
