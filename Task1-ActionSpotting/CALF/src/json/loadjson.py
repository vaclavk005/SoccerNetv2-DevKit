import json

with open('matches.json', 'r') as f:
    matches_data = json.load(f)

train_matches = matches_data['train_matches']
valid_matches = matches_data['valid_matches']
test_matches = matches_data['test_matches']

print("Train Matches:", train_matches)
print("Valid Matches:", valid_matches)
print("Test Matches:", test_matches)