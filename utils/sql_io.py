def load_sql_file(file_path):
    sql_text = ""

    with open(file_path, "r") as sql_file:
        sql_text = sql_file.read()

    return sql_text.replace("\n", " ").replace("\t", "")
