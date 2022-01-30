import advertools as adv
import pandas as pd
import requests
import json
import time


def main():
    sitemap_urls = adv.sitemap_to_df("https://www.kagome.co.jp/sitemap.xml")
    sitemap_urls_list = sitemap_urls["loc"].to_list()
    print(sitemap_urls_list)


if __name__ == "__main__":
    main()

