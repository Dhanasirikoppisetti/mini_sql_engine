def parse_sql(query):
    query = query.strip().rstrip(";")
    query_lower = query.lower()
    if not query_lower.startswith("select"):
        raise Exception("Only SELECT queries are supported")

    if "from" not in query_lower:
        raise Exception("Missing FROM clause")

    select_idx = query_lower.index("select") + len("select")
    from_idx = query_lower.index("from")
    select_part = query[select_idx:from_idx].strip()
    rest = query[from_idx + len("from"):].strip()

    if select_part == "*":
        select_cols = ["*"]
    else:
        select_cols = [c.strip() for c in select_part.split(",")]

    # Parse FROM and WHERE
    if "where" in rest.lower():
        where_idx = rest.lower().index("where")
        table_part = rest[:where_idx].strip()
        where_part = rest[where_idx + len("where"):].strip()
        table = table_part
        where = parse_where(where_part)
    else:
        table = rest
        where = None

    return {
        "select": select_cols,
        "from": table,
        "where": where
    }

def parse_where(where_text):
    conditions = []
    operators = ["<=", ">=", "!=", "=", ">", "<"]

    # split by AND (case-insensitive)
    parts = where_text.split("AND")

    for part in parts:
        part = part.strip()
        for op in operators:
            if op in part:
                col, val = part.split(op, 1)
                col = col.strip()
                val = val.strip().strip("'")

                if val.isdigit():
                    val = int(val)

                conditions.append({
                    "column": col,
                    "operator": op,
                    "value": val
                })
                break

    if not conditions:
        raise Exception("Invalid WHERE clause")

    return conditions
