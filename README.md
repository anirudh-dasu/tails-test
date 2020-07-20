# Tails.com Test

We have two folders in this repo, server and client.

# Server

  - This is a flask application which returns stores over API.
  - In order to run this, do the following - `cd server && flask run`
 - The application will run on `http://localhost:5000`.
 - Stores are served at the endpoint `http://localhost:5000/stores`. This API accepts the following query parameters
    - `query` - A search string to filter the stores either by postcode or name.
    - `limit` - A limit for the number of results desired. Defaults to 10.
    - `offset` - To be used in conjunction with limit to get further results. Defaults to 0.
    - `with_coordinates` - If 'true', the coordinates of each location will be store from postcodes.io
- In order to run the tests, use the following command - `python -m unittest tests/test_stores.py`
- Logging is to STDOUT

# Client

- This is a basic VueJs application that displays a simple text field to search stores.
- In order to run this, do the following - `cd client && npm run serve`
- Note that, the flask app needs to be running on port 5000 for the client to work. In case, it is running on a differnt port, please change it in the `src/constants.js` file.
- As you are typing in the text field, only top 3 results will be displayed. To get the full list, you can click on the search icon, or hit Enter key or scroll the page.
- A minimum of two characters need to be typed for results to start showing.
