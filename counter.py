import time

# Startvärde
counter = 0

# While-loop som körs oändligt
while True:
    print(f"Counter: {counter}")  # Skriv ut aktuellt värde
    counter += 1  # Öka värdet med 1
    time.sleep(1)  # Vänta i 1 sekund
