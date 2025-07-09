import argparse
from papers.fetcher import fetch_pubmed_papers
from papers.parser import filter_non_academic_authors
from papers.utils import save_to_csv, print_results

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    if args.debug:
        print(f"Fetching papers for query: {args.query}")

    papers = fetch_pubmed_papers(args.query, debug=args.debug)
    filtered = filter_non_academic_authors(papers, debug=args.debug)

    if args.file:
        save_to_csv(filtered, args.file)
        print(f"Results saved to {args.file}")
    else:
        print_results(filtered)

if __name__ == "__main__":
    main()
