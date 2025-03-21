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
    Movie("Inception", 148, 10, 100),
    Movie("Interstellar", 169, 12, 80),
    Movie("The Dark Knight", 152, 15, 50),
    Movie("Tenet", 150, 10, 60)
]

# Display available movies
print("Available Movies:")
for movie in movies:
    print(f"🎬 {movie.title} ({movie.duration} min) - ${movie.price}, Seats: {movie.seats_available}")

# Simulate booking
movies[0].book_ticket(5)  # Booking 5 seats for Inception
movies[2].book_ticket(55) # Trying to overbook The Dark Knight
movies[3].book_ticket(20) # Booking 20 seats for Tenet

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
plt.show()
