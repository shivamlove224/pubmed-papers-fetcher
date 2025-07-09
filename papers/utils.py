import csv
from typing import List, Dict

def save_to_csv(data: List[Dict], filename: str) -> None:
    if not data:
        print("No data to save.")
        return

    keys = ["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"]
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def print_results(data: List[Dict]) -> None:
    if not data:
        print("No results found.")
        return

    for paper in data:
        print("\n--- Paper ---")
        print(f"PubmedID: {paper['PubmedID']}")
        print(f"Title: {paper['Title']}")
        print(f"Publication Date: {paper['Publication Date']}")
        print(f"Non-academic Author(s): {paper['Non-academic Author(s)']}")
        print(f"Company Affiliation(s): {paper['Company Affiliation(s)']}")
        print(f"Corresponding Author Email: {paper['Corresponding Author Email']}")
