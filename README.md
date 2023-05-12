# SnowflakeExamples
## A public facing space to share and learn from examples of documented Snowflake Code

### ❗ NOTE: You must annonymize your code before attempting to contribute to this repository, otherwise your contribution will be rejected. Please remove the following: 
  * Names
  * Emails
  * Account specific information (e.g. account, role, warehouse)
  * Database information (e.g. database, schema, table)
  * Any other sensitive or personally identifiable information


### 📖 Description of Tools in this repository
* to_sql.py is a toy example of reading and writing data to snowflake using pandas and no SQL
  1. Update <FIELDS> with your account information. Without this step the code will fail. 
  2. Create a connection to the target Database and Schema
  3. Create a an example .csv file containing the current time
  4. Reads the .csv file into a dataframe
  5. Writes that dataframe to snowflake using the connection built above
  6. Read newly created table into a dataframe
  7. Print dataframe to check that it uploaded the current time
  8. Done!
