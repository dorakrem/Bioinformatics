from Bio import Align, SeqIO
from Bio.Align import PairwiseAligner

# Create a PairwiseAligner object
aligner = Align.PairwiseAligner()

# Set the parameters for global alignment
aligner.mode = 'global'
aligner.match_score = 1
aligner.mismatch_score = -1
aligner.open_gap_score = -1
aligner.extend_gap_score = -1

# Read the sequences from the FASTA files
sequence1_file = "BatSpikeProtein.fasta"
sequence2_file = "CovSpikeProtein.fasta"

sequence1 = str(SeqIO.read(sequence1_file, "fasta").seq)
sequence2 = str(SeqIO.read(sequence2_file, "fasta").seq)

#print(sequence1)
#print(sequence2)

# Perform the alignment
alignments = aligner.align(sequence1, sequence2)
best_alignment = alignments[0]

# Print the best alignment
print(best_alignment)

# Extract the aligned sequences
aligned_seq1 = best_alignment.query
aligned_seq2 = best_alignment.target

# Extract the LCS by comparing the aligned sequences
lcs = ''.join(char1 for char1, char2 in zip(aligned_seq1, aligned_seq2) if char1 == char2)

# Print the alignment score and LCS
print("Alignment Score:", best_alignment.score)
print("Longest Common Subsequence:", lcs)

# Print the lengths of the sequences
print("\nLength Sequence 1, BatSpikeProtein:", len(sequence1))
print("Length Sequence 2, CovSpikeProtein:", len(sequence2))
print("Length LCS:", len(lcs))