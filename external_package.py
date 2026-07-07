# ALAB 356.1
# Task 3: Using PIP and an External Package
# Requires the 'requests' package; install with: pip install requests
import requests

# Public API to fetch a programming joke
def get_joke():
  url = "https://v2.jokeapi.dev/joke/Programming?type=single"
  response = requests.get(url)

  if response.status_code == 200: # check if request was successful
    data = response.json() # Parse data into a dictionary
    print("[Programming joke]")
    print(data["joke"])
  else:
    print(f"failed to get joke. Status code: {response.status_code}")

if __name__ == "__main__":
  get_joke()
