import csv
from datetime import datetime
import sqlalchemy
import snowflake.sqlalchemy
import pandas as pd

# Define a function to set up a connection to the user specified snowflake database and schema
def create_connection(snowflake_database,snowflake_schema):
    # Establish the connection to Snowflake
    url = snowflake.sqlalchemy.URL(
        user='<YOUR.EMAIL>@waterboards.ca.gov', # NOTE Replace this with your email
        account='<SNOWFLAKE.WEB.ENDPOINT>',      # NOTE Contact your program DBA for help setting this up
        authenticator='externalbrowser',
        warehouse='<YOUR_WAREHOUSE>',           # NOTE Contact your program DBA for help setting this up
        role = '<YOUR_SNOWFLAKE_ROLE>',           # NOTE Contact your program DBA for help setting this up. You'll need to request read/write permissions to run this code.
        database=snowflake_database,
        schema=snowflake_schema
        )
    engine = sqlalchemy.create_engine(url)
    connection = engine.connect()
    return connection

# ************************************************************
# Create an example CSV file containing the current time
# ************************************************************
# Get the current time
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Define the file name
csv_file = 'current_time.csv'

# Create and write to the CSV file
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Current Time'])
    writer.writerow([current_time])
# ************************************************************
# ************************************************************

# Use the function defined above to connect to the Database and Schema indicated
conn = create_connection('<DATABASE>','<SCHEMA>') # NOTE You'll need to insert the Dabase and Schema here for this code to function

# Read our example CSV file into a Pandas DataFrame
write_data_frame = pd.read_csv(csv_file)

# Uploading the DataFrame to Snowflake
write_data_frame.to_sql(
    name='Current_Time_Test',   # Give the table whatever name you want
    con=conn,                   # Provide connection information to specify Database and Schema upload target
    index=False,                # This indicates we don't want to include the dataframe index
    if_exists='replace'         # Choose 'append' if you want to add to an existing table
)

# Read the table you just created into a new pandas dataframe
read_data_frame = pd.read_sql_table('Current_Time_Test',con=conn)

# Print out the contents of the SQL table we just wrote to confirm that it got the current time
print(read_data_frame)

# Don't forget to close your Snowflake connection!
conn.close()
