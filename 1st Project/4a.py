def find_max_prefix_repeat(T):
    # Υπολογισμός του μισού μήκους της ακολουθίας
    k = len(T) // 2 + 1
    max_prefix_repeat = ""

    # Έλεγχος για κάθε τιμή του i από 0 έως k-1
    for i in range(0, k):
        # Έλεγχος αν οι πρώτοι i+1 χαρακτήρες είναι ίσοι με τους επόμενους i+1 χαρακτήρες
        if T[:i+1] == T[i+1 : 2*i+2]:
            # Αν ναι, ενημέρωση του μέγιστου prefix repeat
            max_prefix_repeat = T[:i+1] 

    # Επιστροφή του μέγιστου prefix repeat, την διπλή του εμφάνιση
    return max_prefix_repeat + max_prefix_repeat

# Παράδειγμα χρήσης
T = "abcaabcajdjifoenbcajklopooopoojk"
result = find_max_prefix_repeat(T)

if result:
    print("Maximum prefix repeat:", result)
else:
    print("There is no prefix repeat.")