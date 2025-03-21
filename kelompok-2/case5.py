import pandas as pd
import matplotlib.pyplot as plt

class Movie:
    def __init__(self, title, duration, price, seats_available):
        self.title = title
        self.duration = duration
        self.price = price
        self.seats_available = seats_available

    def book_ticket(self, num_tickets):
        if num_tickets <= self.seats_available:
            self.seats_available -= num_tickets
            print(f"✅ Successfully booked {num_tickets} ticket(s) for {self.title}.")
        else:
            print(f"❌ Not enough seats available for {self.title}. Only {self.seats_available} left.")

# List of movies
movies = [
    Movie("Agak Laen", 148, 10000, 100),
    Movie("Pocong Mualaf", 169, 12000, 100),
    Movie("Kunti bapak", 152, 15000, 100),
    Movie("AADC", 150, 10000, 100)
]


# Display available movies
print("Available Movies:")
for idx, movie in enumerate(movies):
    print(f"{idx + 1}. 🎬 {movie.title} ({movie.duration} min) - Rp{movie.price}, Seats: {movie.seats_available}")

# Simulate booking via user input
while True:
    try:
        movie_choice = int(input("Enter the number of the movie you want to book (or 0 to exit): "))
        if movie_choice == 0:
            break
        elif 1 <= movie_choice <= len(movies):
            num_tickets = int(input("Enter number of tickets: "))
            movies[movie_choice - 1].book_ticket(num_tickets)
        else:
            print("❌ Invalid movie choice. Try again.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Create DataFrame to store movie information
data = {
    "Title": [movie.title for movie in movies],
    "Duration": [movie.duration for movie in movies],
    "Price": [movie.price for movie in movies],
    "Seats Available": [movie.seats_available for movie in movies]
}
df = pd.DataFrame(data)
print("\nUpdated Movie Data:")
print(df)

# Visualizing occupancy rates
plt.figure(figsize=(8, 5))
plt.bar(df["Title"], 100 - df["Seats Available"], color='skyblue', label='Booked Seats')
plt.bar(df["Title"], df["Seats Available"], color='yellow', label='Available Seats', bottom=100 - df["Seats Available"])
plt.xlabel("Movies")
plt.ylabel("Seats")
plt.title("Movie Occupancy Rates")
plt.legend()
plt.xticks(rotation=45)
plt.show()
