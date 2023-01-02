import requests
# import mysql.connector

# Make a GET request to the NBA API endpoint for teams
response = requests.get("https://www.balldontlie.io/api/v1/teams")

# Check the status code of the response to make sure the request was successful
if response.status_code == 200:
  # Load the response data into a Python dictionary
  data = response.json()

  # Iterate through the list of teams in the response data
  for team in data["data"]:
    # Print the name of each team
    print("team:  "+team["full_name"]+((24-len(team["full_name"]))*" ")+"|| devision:    "+team["division"])

else:
  # If the request was not successful, print an error message
  print(f"An error occurred: {response.status_code}")
  
  ###################################################################3
  
# Connect to the database
cnx = mysql.connector.connect(user="username", password="password", host="host", database="database")

# Create a cursor object to execute queries
cursor = cnx.cursor()

# Create the SQL query to insert a row into the table
query = "INSERT INTO teams (name, conference, division) VALUES (%s, %s, %s)"

# Iterate through the list of teams in the response data
for team in data["data"]:
  # Extract the data for each team
  name = team["full_name"]
  conference = team["conference"]
  division = team["division"]

  # Execute the query to insert the data into the table
  cursor.execute(query, (name, conference, division))

# Commit the changes to the database
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()