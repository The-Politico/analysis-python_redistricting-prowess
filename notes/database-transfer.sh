# New pol
PGPASSWORD="<NEW_DB_PASS>" \
createdb \
  -h <NEW_DB_URL> \
  -U <NEW_DB_USER> \
  prowess_v1_new__XX && \
pg_dump -C -h localhost -U postgres prowess_v1_new__XX |\
    PGPASSWORD="<NEW_DB_PASS>" \
    psql \
      -h <NEW_DB_URL> \
      -U <NEW_DB_USER> \
      prowess_v1_new__XX

# New demo
PGPASSWORD="<NEW_DB_PASS>" \
createdb \
  -h <NEW_DB_URL> \
  -U <NEW_DB_USER> \
  prowess_v1_new__XX__census && \
pg_dump -C -h localhost -U postgres prowess_v1_new__XX__census |\
    PGPASSWORD="<NEW_DB_PASS>" \
    psql \
      -h <NEW_DB_URL> \
      -U <NEW_DB_USER> \
      prowess_v1_new__XX__census


# Old pol
PGPASSWORD="<NEW_DB_PASS>" \
createdb \
  -h <NEW_DB_URL> \
  -U <NEW_DB_USER> \
  prowess_v1_old__XX && \
pg_dump -C -h localhost -U postgres prowess_v1_old__XX |\
    PGPASSWORD="<NEW_DB_PASS>" \
    psql \
      -h <NEW_DB_URL> \
      -U <NEW_DB_USER> \
      prowess_v1_old__XX


# Old demo
PGPASSWORD="<NEW_DB_PASS>" \
createdb \
  -h <NEW_DB_URL> \
  -U <NEW_DB_USER> \
  prowess_v1_old__XX__census && \
pg_dump -C -h localhost -U postgres prowess_v1_old__XX__census |\
    PGPASSWORD="<NEW_DB_PASS>" \
    psql \
      -h <NEW_DB_URL> \
      -U <NEW_DB_USER> \
      prowess_v1_old__XX__census
