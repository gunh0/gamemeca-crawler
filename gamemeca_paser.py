import requests
from bs4 import BeautifulSoup
import csv


def main():
    url = "https://trees.gamemeca.com/gamerank/#1521881342690-f60aa3c1-8642"

    # Send a GET request to the website and retrieve the HTML content
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    print(response.status_code)
    html_content = response.content
    print(html_content)

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the container that holds the data to be crawled
    data_container = soup.find("div", class_="vc_tta-panel-body")

    if data_container:
        table = data_container.find("table", id="tablepress-2008")
        if table:
            rows = table.find_all("tr")

            # Create a CSV file to store the crawled data
            with open(
                "game_rankings.csv", "w", newline="", encoding="utf-8"
            ) as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(["Rank", "Name", "Service", "Genre"])

                # Extract the desired data and write it to the CSV file
                for row in rows[1:]:
                    columns = row.find_all("td")
                    rank = columns[0].text.strip()
                    name = columns[1].find("a").text.strip()
                    service = columns[2].text.strip()
                    genre = columns[3].text.strip()
                    csv_writer.writerow([rank, name, service, genre])

            print("Data has been successfully crawled and saved to game_rankings.csv.")
        else:
            print("Table not found. Please check the HTML structure of the website.")
    else:
        print(
            "Data container not found. Please check the HTML structure of the website."
        )


if __name__ == "__main__":
    main()
