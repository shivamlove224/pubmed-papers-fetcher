from typing import List, Dict

NON_ACADEMIC_KEYWORDS = [
    "pharma", "biotech", "inc", "llc", "gmbh", "ltd", "corporation",
    "solutions", "industries", "therapeutics", "technologies"
]

ACADEMIC_KEYWORDS = [
    "university", "institute", "college", "school", "hospital",
    "center", "centre", "academy", "faculty", "dept", "laboratory", "lab"
]

def is_non_academic(affiliation: str) -> bool:
    aff_lower = affiliation.lower()
    if any(keyword in aff_lower for keyword in ACADEMIC_KEYWORDS):
        return False
    if any(keyword in aff_lower for keyword in NON_ACADEMIC_KEYWORDS):
        return True
    return False

def filter_non_academic_authors(papers: List[Dict], debug: bool = False) -> List[Dict]:
    results = []
    for paper in papers:
        non_acad_authors = []
        company_names = set()

        for author in paper.get("Authors", []):
            for aff in author.get("affiliations", []):
                if is_non_academic(aff):
                    non_acad_authors.append(author["name"])
                    company_names.add(aff)

        if non_acad_authors:
            results.append({
                "PubmedID": paper.get("PubmedID"),
                "Title": paper.get("Title"),
                "Publication Date": paper.get("Publication Date"),
                "Non-academic Author(s)": ", ".join(non_acad_authors),
                "Company Affiliation(s)": "; ".join(company_names),
                "Corresponding Author Email": paper.get("Email")
            })
        elif debug:
            print(f"No non-academic authors found for paper {paper.get('PubmedID')}")

    return results
