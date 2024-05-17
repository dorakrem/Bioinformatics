def find_repetitions(sequences):
    repetitions = set()

    if len(sequences) > 2:
        # Find all unique substrings that appear at least twice in any sequence
        for seq in sequences:
            sequence_length = len(seq)
            substrings = set()

            # Iterate over all possible substring lengths
            for length in range(2, sequence_length // 2 + 1):
                # Slide a window of size `length` across the sequence
                for i in range(sequence_length - length + 1):
                    substring = seq[i:i + length]

                    # Check if the substring appears at least twice in all sequences
                    if all(seq.count(substring) >= 2 for seq in sequences):
                        substrings.add(substring)

            repetitions.update(substrings)
    else:
        print("Not enough sequences provided.")
        return  # Προσθήκη επιστροφής εδώ

    return list(repetitions)

# Example usage
sequences = ["AGTACGTACAGT", "AGTACGTGTACCGTAGT", "ACGTGTACGTCCGTACGAGT"]
repetitions = find_repetitions(sequences)

print("Repeated substrings found:", repetitions)
