import requests
from bs4 import BeautifulSoup
import csv


def main():
    url = "https://trees.gamemeca.com/gamerank/#1521881342690-f60aa3c1-8642"

    # Send a GET request to the website and retrieve the HTML content
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    print(f"Response Status Code: {response.status_code}")

    html_content = response.content
    print(f"HTML Content: {html_content}")

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the ranking, title, service, and genre elements in the table
    table_ranking = soup.findAll("td", {"class": "column-1"})
    table_titles = soup.findAll("td", {"class": "column-2"})
    table_service = soup.findAll("td", {"class": "column-3"})
    table_genre = soup.findAll("td", {"class": "column-4"})

    # Create a CSV file to store the data
    with open("game_rankings.csv", "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Ranking", "Title", "Service", "Genre"])

        # Print the ranking, title, service, and genre for each entry and write to CSV
        for rank, title, service, genre in zip(
            table_ranking, table_titles, table_service, table_genre
        ):
            rank_text = rank.get_text().strip()
            title_text = title.get_text().strip()
            service_text = service.get_text().strip()
            genre_text = genre.get_text().strip()

            print(
                f"Ranking: {rank_text}, Title: {title_text}, Service: {service_text}, Genre: {genre_text}"
            )

            # Write the data to the CSV file
            csv_writer.writerow([rank_text, title_text, service_text, genre_text])

    print("Data has been successfully crawled and saved to game_rankings.csv.")


if __name__ == "__main__":
    main()
