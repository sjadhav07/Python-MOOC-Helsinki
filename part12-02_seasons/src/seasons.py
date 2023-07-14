# Write your solution here:
def sort_by_seasons(items: list):
    def sort_by_seasons(item: dict):
        return item['seasons']
    return sorted(items, key = sort_by_seasons)