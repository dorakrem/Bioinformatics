def compute_scores(string1, string2, k):
    n1 = len(string1)  # Υπολογισμός του μήκους της πρώτης συμβολοσειράς
    n2 = len(string2)  # Υπολογισμός του μήκους της δεύτερης συμβολοσειράς

    if n1 != n2:  # Έλεγχος μήκους
        raise ValueError("Οι συμβολοσειρές πρέπει να έχουν το ίδιο μήκος.")
    
    dp = [[0] * (n2 - k + 1) for _ in range(n1 - k + 1)]  # Δημιουργία πίνακα dp με μηδενικά
    
    def calculate_score(i, j, x):
        if x == k:
            return 0
        else:
            score = int(string1[i + x] == string2[j + x])  # Σκορ για την τρέχουσα θέση
        
            return score + calculate_score(i, j, x + 1)  # Αναδρομική κλήση για την επόμενη θέση
    
    for i in range(n1 - k + 1):
        for j in range(n2 - k + 1):
            dp[i][j] = calculate_score(i, j, 0)  # Υπολογισμός σκορ για κάθε θέση
    
    return dp

# Παράδειγμα χρήσης
string1 = "abcdvvdsg"
string2 = "abcggeges"
k = 3

try:
    scores = compute_scores(string1, string2, k)
    for row in scores:
        print(row)
except ValueError as e:
    print(e)
