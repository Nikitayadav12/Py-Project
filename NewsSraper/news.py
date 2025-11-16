import requests
from bs4 import BeautifulSoup

def scrape_bbc_headlines():
    url = "https://www.bbc.com/news"
    try:
        
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()

       
        soup = BeautifulSoup(response.text, 'html.parser')

        # BBC headlines are often in <h2> or <h3> with specific classes
        headlines = soup.find_all(['h2', 'h3'])

       
        headline_texts = [h.get_text(strip=True) for h in headlines if h.get_text(strip=True)]

        return headline_texts

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return []

def save_to_file(headlines, filename="headlines.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for hl in headlines:
                f.write(hl + "\n")
        print(f"✅ Headlines saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    print("Scraping BBC News headlines...")
    data = scrape_bbc_headlines()

    if data:
        save_to_file(data)
        print("Top 10 headlines:")
        for i, hl in enumerate(data[:10], start=1):
            print(f"{i}. {hl}")
    else:
        print("No headlines found.")
