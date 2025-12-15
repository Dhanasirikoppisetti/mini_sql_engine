import csv

def load_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = [
            {k.lower().strip(): v.strip() for k, v in row.items()} 
            for row in reader
        ]
    return data


def apply_where(data, where):
    if where is None:
        return data

    result = []

    for row in data:
        match = True

        for cond in where:
            column = cond["column"].lower()
            operator = cond["operator"]
            value = cond["value"]

            cell = row.get(column)
            if cell is None:
                match = False
                break

            # try numeric comparison
            try:
                cell_int = int(cell)
                value_int = int(value)
            except:
                cell_int = None
                value_int = None

            if operator == "=" and str(cell).lower() != str(value).lower():
                match = False
            elif operator == "!=" and str(cell).lower() == str(value).lower():
                match = False
            elif operator == ">" and (cell_int is None or cell_int <= value_int):
                match = False
            elif operator == "<" and (cell_int is None or cell_int >= value_int):
                match = False
            elif operator == ">=" and (cell_int is None or cell_int < value_int):
                match = False
            elif operator == "<=" and (cell_int is None or cell_int > value_int):
                match = False

            if not match:
                break

        if match:
            result.append(row)

    return result


def apply_select(data, select_cols):
    if select_cols == ["*"]:
        return data
    result = []
    for row in data:
        new_row = {col.lower(): row[col.lower()] for col in select_cols if col.lower() in row}
        result.append(new_row)
    return result


def apply_count(data, column=None):
    if column is None or column == "*" or column.lower() == "count(*)":
        return len(data)
    else:
        return sum(1 for row in data if row.get(column) not in [None, ""])
