original_score = []
for _ in range(3):
    original_score.append(int(input()))
alias_scores = original_score
replacement_scores = int(input())
additional_scores = int(input())

# Modify the shared list through alias_scores
alias_scores[0] = replacement_scores
alias_scores.append(additional_scores)

# Display both variables and check whether they share one object

print(f"Original: {original_score}")
print(f"Alias: {alias_scores}")
print(f"Shared: {original_score == alias_scores}")