# --------------drawing_book---------------#

def pageCount(num_pages, target):
    if num_pages % 2 == 0:
        num_pages = num_pages + 1
    if target % 2 == 0:
        target = target + 1

    # returns the minimum number of pages that must be turned in order to arrive at page p
    return min(target//2, num_pages//2 - target//2)


# --------------main---------------#
num_pages = 99  # n, the number of pages in the book
target = 49  # p, the page we are looking for

result = pageCount(num_pages, target)
print(result)
