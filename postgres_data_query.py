import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Helper functions
def get_connection_strings(host, user, dbname, password, sslmode):
    return f"host={host} user={user} dbname={dbname} password={password} sslmode={sslmode}"


########################################
# Update connection string information #
########################################
host = "alexeipostgresqlserver.postgres.database.azure.com"
user = "sqladminuser"
password = "Alexei.80"
sslmode = "require"

# Create a new DB
dbname = "azurecomponentdata"
conn_string = get_connection_strings(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
print("Connection established")

cursor = conn.cursor()
cursor.execute(f'SELECT * FROM information_schema.tables')
# Clean up initial connection
conn.commit()
cursor.close()
conn.close()

print("All done!")