# fasta_stats.py - read a FASTA file and report stats per sequence

def gc_content(seq):
    return (seq.count("G") + seq.count("C")) / len(seq) * 100

def read_fasta(filename):
    sequences = {}
    current = None
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                current = line
                sequences[current] = ""
            else:
                sequences[current] = sequences[current] + line
    return sequences

# --- main part: use the tools above ---
seqs = read_fasta("proteins.fasta")
print("Found", len(seqs), "sequence(s):")
for header, seq in seqs.items():
    print("Protein:", header[:30])
    print("  Length:", len(seq))
    print("  GC content:", round(gc_content(seq), 2), "%")
