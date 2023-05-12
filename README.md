# SnowflakeExamples
A public facing space to share and learn from examples of documented Snowflake Code

### Description of Tools in this repository
* to_sql.py is a toy example of reading and writing data to snowflake using pandas and no SQL
  1. Create a connection to the target Database and Schema
  2. Create a an example .csv file containing the current time
  3. Reads the .csv file into a dataframe
  4. Writes that dataframe to snowflake using the connection built above
  5. Read newly created table into a dataframe
  6. Print dataframe to check that it uploaded the current time
  7. Done!
