# HTMLTableToMarkdown

"""
Converts online HTML tables to Markdown table.

Change only the url and print_cols variables 
  - for the URL and the columns to be included in the markdown tables, respectively
  - column numbering starts at zero (0), for the first column
"""

import pandas as pd

"""
Here are two example usages, that set the url and print_cols variables.
"""

"""
For 3Dprintingwiki link to empty spool weights tables
Print 5 columns: 0, 1, 2, 3 and 6
"""
# URL to table
url = 'https://3dprintingwiki.mywikis.wiki/wiki/Spool_weight'
# Columns to print
print_cols = [0, 1, 2, 3, 6]

"""
For Reddit link to empty spool weights tables
Print ALL 7 columns
"""
# URL to table
# url = 'https://www.reddit.com/r/3Dprinting/comments/4hlwse/empty_spool_weights_for_estimating_remaining/'
# Columns to print
# print_cols = [0, 1, 2, 3, 4, 5, 6]

if __name__ == '__main__':

    # read HTML tables from URL
    tables = pd.read_html(url)

    # extract the first table (which contains the weight data)
    first_table = tables[0]

    # Get the table columns that exist
    cols = list(first_table.columns.values)
    # Note this returns an extra 7th column - due to fault in table, so deleted end column
    # del cols[7:] # not really required

    # Markdown table header
    # Column headers: print(f"|{cols[0]}|{cols[1]}|{cols[2]}|{cols[3]}|{cols[4]}|{cols[5]}|{cols[6]}|")
    print("|", end='')
    for n in print_cols:
        print(f"{cols[n]}|", end='')
    print()
    # Lines: print("|---|---|---|---|---|---|---|")
    num_cols = len(print_cols)
    print("|", end='')
    for n in range(num_cols - 1):
        print("---|", end='')
    print("---|")

    # Print table entries in loop using "cols" list
    for n in range(len(first_table)):
        # Print each row
        print("|", end='')
        for col in print_cols:
            print(f"{first_table[cols[col]][n]}|", end='')
        print()
