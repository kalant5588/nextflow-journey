# gc_tool.py - calculate GC content for multiple sequences

def gc_content(seq):
    return (seq.count("G") + seq.count("C")) / len(seq) * 100

# A list of sequences to analyse
sequences = ["ATGC", "GGGGCCCC", "ATATAT", "TTTTAAAA"]

# Loop over each one and print its GC content
print("Analysing", len(sequences), "sequences:")
for seq in sequences:
    print(seq, "->", round(gc_content(seq), 2), "%")
