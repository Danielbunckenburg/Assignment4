
#Question 4

# Define the file content
data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

# Points per card
points = {
    "Card 1": 8,
    "Card 2": 2,
    "Card 3": 0
}

# Initialize total points
total_points = 0

# Split the data by lines
lines = data.strip().split('\n')

for line in lines:
    # Extract card name
    card_name = line.split(':')[0].strip()

    # Add the card's points to the total
    total_points += points.get(card_name, 0)

print("Total points for all cards:", total_points)


