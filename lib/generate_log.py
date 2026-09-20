from datetime import datetime
import requests


def generate_log(data):
    # Make sure the input is a list.
    if not isinstance(data, list):
        raise ValueError("Data must be a list.")

    # Create a filename using today's date.
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write each log entry to the file on its own line.
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Confirm that the log file was created.
    print(f"Log written to {filename}")

    return filename


def fetch_data():
    # Fetch a post from the JSONPlaceholder public API.
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    # Return the API data when the request succeeds.
    if response.status_code == 200:
        return response.json()

    # Return an empty dictionary if the request fails.
    return {}


if __name__ == "__main__":
    # Fetch data from the API when the script is run directly.
    post = fetch_data()

    print(
        "Fetched Post Title:",
        post.get("title", "No title found")
    )
