# Imports from python.
import os

MAIN_DB_CONFIG = os.environ.get("DB_URL_MAIN", "")

DB_CONFIGS = dict(
    main_archive=MAIN_DB_CONFIG,
    adam=os.environ.get("DB_URL_ADAM", MAIN_DB_CONFIG),
    baker=os.environ.get("DB_URL_BAKER", MAIN_DB_CONFIG),
    charlie=os.environ.get("DB_URL_CHARLIE", MAIN_DB_CONFIG),
    david=os.environ.get("DB_URL_DAVID", MAIN_DB_CONFIG),
    edward=os.environ.get("DB_URL_EDWARD", MAIN_DB_CONFIG),
    freddie=os.environ.get("DB_URL_FREDDIE", MAIN_DB_CONFIG),
    george=os.environ.get("DB_URL_GEORGE", MAIN_DB_CONFIG),
    harry=os.environ.get("DB_URL_HARRY", MAIN_DB_CONFIG),
    ida=os.environ.get("DB_URL_IDA", MAIN_DB_CONFIG),
    john=os.environ.get("DB_URL_JOHN", MAIN_DB_CONFIG),
    king=os.environ.get("DB_URL_KING", MAIN_DB_CONFIG),
    lewis=os.environ.get("DB_URL_LEWIS", MAIN_DB_CONFIG),
)
