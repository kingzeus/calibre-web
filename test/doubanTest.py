from cps.metadata_provider.douban import Douban

if __name__ == "__main__":
    douban = Douban()
    result = douban.search("知识考古学")
    for book in result:
        print(book)

