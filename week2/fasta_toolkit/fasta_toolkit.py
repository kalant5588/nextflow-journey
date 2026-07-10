# fasta_toolkit.py - analyse protein sequences from a FASTA file
# Author: kalant5588

from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import pandas as pd


def analyse_fasta(filename):
    """Read a FASTA file and return a list of per-protein stats."""
    results = []
    for record in SeqIO.parse(filename, "fasta"):
        seq = str(record.seq)
        try:
            analysis = ProteinAnalysis(seq)
            mw = round(analysis.molecular_weight(), 2)
            pi = round(analysis.isoelectric_point(), 2)
        except ValueError:
            mw = None
            pi = None
        results.append({
            "id": record.id,
            "length": len(seq),
            "molecular_weight": mw,
            "isoelectric_point": pi,
        })
    return results

def make_report(filename, output_csv):
    """Analyse a FASTA and save a stats table to CSV."""
    results = analyse_fasta(filename)
    df = pd.DataFrame(results)
    print("Analysed", len(df), "proteins from", filename)
    print(df.describe())
    df.to_csv(output_csv, index=False)
    print("Saved results to", output_csv)
    return df

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python fasta_toolkit.py <input.fasta> <output.csv>")
        sys.exit(1)
    make_report(sys.argv[1], sys.argv[2])
