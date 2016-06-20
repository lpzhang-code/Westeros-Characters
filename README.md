#README

### Files
`database_setup` contains the SQLAlchemy configuration, class, and mapper code that is injected into a Postgres database; `populate_database.py` inserts pre-prepared content into the database; `project.py` connects to the database and runs the Flask application. The `static` folder contains CSS for the view which is structured inside the `templates` folder. `client_secrets.json` contains data for properly implementing third party authentication. `Procfile` and `requirements.txt` are configuration files for hosting the application on Heroku.

### How to Use
This application allows users to view and share their favourite characters from the book and television series, "Game of Thrones". The home page displays a list of the eight most prominent Westeros houses, and characters that were recently added by users. Clicking on a specific house lists only the characters that belong to that house. Selecting the specific character opens up an item page displaying their portrait and bio. Users can log on through a third party authentication system provided by Google and once authenticated, they can add characters, or edit and delete those that they have already added. The application also contains a JSON endpoint allowing the retrieval of information on all characters stored in the database via API calls.
