# Imports from other dependencies.
import io


def upload_df_to_psql(engine, df, destination_table):
    df.head(0).to_sql(
        destination_table,
        engine,
        if_exists="replace",
        index=False,
    )
    conn = engine.raw_connection()
    cur = conn.cursor()
    output = io.StringIO()

    df.to_csv(output, sep="\t", header=False, index=False)
    output.seek(0)

    # contents = output.getvalue()
    cur.copy_from(output, destination_table, null="")
    conn.commit()
