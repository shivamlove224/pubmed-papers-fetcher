import requests
from typing import List, Dict, Any

def fetch_pubmed_papers(query: str, debug: bool = False) -> List[Dict[str, Any]]:
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

    search_params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 20
    }
    search_resp = requests.get(base_url, params=search_params)
    search_resp.raise_for_status()
    ids = search_resp.json()["esearchresult"]["idlist"]

    if debug:
        print(f"Found {len(ids)} IDs: {ids}")

    if not ids:
        return []

    fetch_params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "xml"
    }
    fetch_resp = requests.get(fetch_url, params=fetch_params)
    fetch_resp.raise_for_status()

    from xml.etree import ElementTree as ET
    root = ET.fromstring(fetch_resp.text)

    papers = []
    for article in root.findall(".//PubmedArticle"):
        try:
            pmid = article.findtext(".//PMID")
            title = article.findtext(".//ArticleTitle")
            pub_date = article.findtext(".//PubDate/Year") or "Unknown"
            authors = []
            affiliations = []
            for author in article.findall(".//Author"):
                last = author.findtext("LastName")
                fore = author.findtext("ForeName")
                name = f"{fore or ''} {last or ''}".strip()
                affs = [aff.text for aff in author.findall("AffiliationInfo/Affiliation") if aff.text]
                if name:
                    authors.append({"name": name, "affiliations": affs})
                    affiliations.extend(affs)
            corr_email = None
            for aff in affiliations:
                if "@" in aff:
                    corr_email = aff
                    break

            papers.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": pub_date,
                "Authors": authors,
                "Email": corr_email
            })
        except Exception as e:
            if debug:
                print(f"Error parsing article: {e}")
            continue

    return papers
