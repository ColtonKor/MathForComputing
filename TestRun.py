import urllib.request
import re

def print_unicode_grid(doc_url: str):

    with urllib.request.urlopen(doc_url) as response:
        html = response.read().decode("utf-8")

    cells = re.findall(r"<td[^>]*>(.*?)</td>", html, flags=re.DOTALL)

    clean_cells = [re.sub(r"<.*?>", "", cell).strip() for cell in cells if cell.strip()]

    coords = {}
    max_x, max_y = 0, 0

    for i in range(0, len(clean_cells), 3):
        try:
            x = int(clean_cells[i])
            symbol = clean_cells[i+1]
            y = int(clean_cells[i+2])

            coords[(x, y)] = symbol
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        except (ValueError, IndexError):
            continue


    for y in range(max_y + 1):
        row = []
        for x in range(max_x + 1):
            row.append(coords.get((x, y), " "))
        print("".join(row))


print_unicode_grid("https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub")