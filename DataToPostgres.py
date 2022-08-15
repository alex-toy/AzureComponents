import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Helper functions
def get_connection_strings():
    return f"host={host} user={user} dbname={dbname} password={password} sslmode={sslmode}"

def drop_recreate(c, tablename, create):
    c.execute("DROP TABLE IF EXISTS {0};".format(tablename))
    c.execute(create)
    print("Finished creating table {0}".format(tablename))

def populate_table(cursor, filename, tablename):
    f = open(filename, 'r')
    next(f)
    try:
        cursor.copy_from(f, tablename, sep=",", null = "")
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
    print("Finished populating {0}".format(tablename))


########################################
# Update connection string information #
########################################
host = "alexeipostgresserver.postgres.database.azure.com"
user = "sqladminuser"
password = "Alexei.80"
sslmode = "require"

# Create a new DB
dbname = "postgres"
conn_string = get_connection_strings()
conn = psycopg2.connect(conn_string)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
print("Connection established")

cursor = conn.cursor()
dbname = "azurecomponentdata"
cursor.execute(f'DROP DATABASE IF EXISTS {dbname}')
cursor.execute(f"CREATE DATABASE {dbname}")
# Clean up initial connection
conn.commit()
cursor.close()
conn.close()

# Reconnect to the new DB
conn_string = get_connection_strings()
conn = psycopg2.connect(conn_string)
print("Connection established")
cursor = conn.cursor()



# Create accidents table
table = "accidents"
filename = "data/us_accidents.csv"

create = f"""
    CREATE TABLE {table} (
        ID VARCHAR(20) PRIMARY KEY,
        Severity INTEGER,
        Start_Time DATE, 
        End_Time DATE, 
        Start_Lat DECIMAL,
        Start_Lng DECIMAL,
        End_Lat DECIMAL,
        End_Lng DECIMAL,
        Distance DECIMAL,
        Description TEXT,
        Number TEXT,
        Street TEXT,
        Side VARCHAR(30),
        City TEXT,
        County TEXT,
        State character(6),
        Zipcode VARCHAR(30),
        Country VARCHAR(30),
        Timezone VARCHAR(50),
        Airport_Code TEXT,
        Weather_Timestamp DATE,
        Temperature DECIMAL,
        Wind_Chill DECIMAL,
        Humidity DECIMAL,
        Pressure DECIMAL,
        Visibility DECIMAL,
        Wind_Direction VARCHAR(50),
        Wind_Speed DECIMAL,
        Precipitation DECIMAL,
        Weather_Condition TEXT,
        Amenity BOOLEAN,
        Bump BOOLEAN,
        Crossing BOOLEAN,
        Give_Way BOOLEAN,
        Junction BOOLEAN,
        No_Exit BOOLEAN,
        Railway BOOLEAN,
        Roundabout BOOLEAN,
        Station BOOLEAN,
        Stop BOOLEAN,
        Traffic_Calming BOOLEAN,
        Traffic_Signal BOOLEAN,
        Turning_Loop BOOLEAN,
        Sunrise_Sunset TEXT,
        Civil_Twilight TEXT,
        autical_Twilight TEXT,
        Astronomical_Twilight TEXT
    );
"""

drop_recreate(cursor, table, create)
populate_table(cursor, filename, table)




# Clean up
conn.commit()
cursor.close()
conn.close()

print("All done!")