# daily_scrape.py

import pandas as pd
from datetime import datetime
from scraper import scrape_jobs 
from cluster import cluster_jobs  
def scrape_and_cluster():
    print("Scraping started at", datetime.now())

    # Step 1: Scrape new job listings
    df = scrape_jobs()  # Your custom function
    df.to_csv("jobs.csv", index=False)

    # Step 2: Cluster the jobs based on skills
    clustered_df = cluster_jobs(df)
    clustered_df.to_csv("cluster.csv", index=False)

    print("Scraping & clustering completed at", datetime.now())

if __name__ == "__main__":
    scrape_and_cluster()
