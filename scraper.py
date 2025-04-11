import requests
from bs4 import BeautifulSoup
import os

# Directory to store reports
os.makedirs("data", exist_ok=True)

def scrape_esg_report(url, company_name):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()
        with open(f"data/{company_name}_esg.txt", "w", encoding="utf-8") as file:
            file.write(text)
        print(f"✅ ESG report saved for {company_name}")
    else:
        print(f"❌ Failed to fetch report for {company_name}")

# Example usage
scrape_esg_report("https://www.infosys.com/sustainability/documents/infosys-esg-report-2022-23.pdf", "infosys")
