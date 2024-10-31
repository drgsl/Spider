# sys is used to get the command line arguments
import sys

# shopCrawler is used to crawl an online shop
import src.Crawler.Shop.compari.shopCrawler as shopCrawler

# fileManager is used to save the data to a json file
# import Command
import src.Crawler.Shop.compari.fileManager as fileManager


if __name__ == '__main__':

    urls = []

    print(f"Found {len(sys.argv) - 1} url(s)")

    for i in range(1, len(sys.argv)):
        urls.append(sys.argv[i])

    productsInfo = shopCrawler.getProductsInfo(urls)

    fileManager.appendToEachFile(productsInfo)
    fileManager.saveToNewFile(productsInfo)
    
    print("Done :)")