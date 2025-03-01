import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(url, max_pages=5):
    visited = set()
    pages_to_visit = [url]
    
    while pages_to_visit and len(visited) < max_pages:
        current_url = pages_to_visit.pop(0)
        if current_url in visited:
            continue
        
        try:
            response = requests.get(current_url, timeout=5)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to fetch {current_url}: {e}")
            continue
        
        print(f"Crawling: {current_url}")
        visited.add(current_url)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            next_url = urljoin(current_url, link['href'])
            if next_url not in visited and next_url.startswith(url):
                pages_to_visit.append(next_url)

if __name__ == "__main__":
    start_url = "https://github.com/saurabhdev17233"  # Change this to your target URL
    crawl(start_url)
