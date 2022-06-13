import csv
import json


def transform_tree(tree):
    res = []

    res_entry = []

    for key, val in tree.items():

        if isinstance(val, dict):
            res.append({

                "Name": key,

                "ID": val,

                "URL": key,

                "children": transform_tree(val),

            })

    return res


def add_leaf(tree, row):
    key = row[0]

    if len(row) > 2:

        if not key in tree:
            tree[key] = {}

        add_leaf(tree[key], row[1:])

    if len(row) == 2:
        tree[key] = row[-1]


class D_data:
    data_file = r'data.csv'

    def __init__(self):
        pass

    def main():

        tree = {}
        data_file = r'data.csv'
        with open(data_file) as csvfile:
            reader = csv.reader(csvfile)
            for rid, row in enumerate(reader):
                if rid == 0:
                    continue
                add_leaf(tree, row)
        with open('data.json', 'w', encoding='utf-8') as jsonf:

            res = transform_tree(tree)
            jsonString = json.dumps(res, sort_keys=True, indent=2, separators=(',', ': '))
            jsonf.write(jsonString)

    main()