from engine import load_csv, apply_where, apply_select, apply_count
from parser import parse_sql

DATA_FILE = "data/customers.csv"


def main():
    data = load_csv(DATA_FILE)

    print("Mini SQL Engine CLI")
    print("Type your SQL query or 'exit' to quit.\n")

    while True:
        query = input("SQL> ").strip()

        if query.lower() in ("exit", "quit"):
            print("Exiting Mini SQL Engine.")
            break

        if not query:
            continue

        try:
            parsed = parse_sql(query)

           
            filtered_data = apply_where(data, parsed["where"])

            select_cols = parsed["select"]

            
            if len(select_cols) == 1 and select_cols[0].lower().startswith("count"):
                count_expr = select_cols[0].lower()

                if count_expr == "count(*)":
                    print(apply_count(filtered_data))
                else:
                   
                    column = count_expr.replace("count(", "").replace(")", "").strip()
                    print(apply_count(filtered_data, column))

           
            else:
                selected_data = apply_select(filtered_data, select_cols)

                if not selected_data:
                    print("No matching records found.")
                else:
                    for row in selected_data:
                        print(row)

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
