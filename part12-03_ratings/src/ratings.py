# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(items: list):
    def rating_order(item: dict):
        return item['rating']
    return sorted(items, key = rating_order, reverse = True)