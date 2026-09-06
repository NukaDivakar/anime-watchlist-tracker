# Anime Watchlist Tracker

A command-line app I built to keep track of the anime I'm watching, have finished, plan to watch, or dropped halfway through. Runs on Python and stores everything in a MySQL database.

I got tired of forgetting which episode I was on for shows I'd paused for weeks, so I built this instead of using another tracking app.

## What it does

- Add anime to your list
- See everything you've added
- Filter by status — watching, completed, plan to watch, dropped
- Update your episode progress (it auto-switches the status to "watching" for you)
- Mark something as completed and give it a rating out of 10
- Delete anime you don't want on the list anymore
- Pull up your top-rated completed shows

## Built with

- Python 3
- MySQL, using `pymysql` to connect

## Files

```
anime-watchlist-tracker/
├── app.py              # the menu you actually interact with
├── anime.py            # all the actual logic behind each option
├── db.py               # handles the MySQL connection
├── anime_tracker.sql   # sets up the database and table
└── README.md
```

## Getting it running

1. Clone it down
   ```
   git clone https://github.com/NukaDivakar/anime-watchlist-tracker.git
   cd anime-watchlist-tracker
   ```

2. Install the one dependency
   ```
   pip install pymysql
   ```

3. Set up the database — this creates the `anime_tracker` database and the table it needs
   ```
   mysql -u root -p < anime_tracker.sql
   ```

4. Open `db.py` and swap in your own MySQL password:
   ```python
   connection = connect(
       host="localhost",
       user="root",
       password="your_mysql_password",   # put yours here
       database="anime_tracker"
   )
   ```
   Heads up — the password sitting in this file right now is just something I used locally for testing. It's not a real credential, but you should still put in your own before running this.

5. Run it
   ```
   python app.py
   ```

## The database

One table, `anime`, with these columns:

| Column            | Type         | What it's for                          |
|-------------------|--------------|------------------------------------------|
| id                | INT          | Auto-incrementing ID                      |
| title             | VARCHAR(150) | Anime title                               |
| genre             | VARCHAR(50)  | Genre                                     |
| status            | VARCHAR(20)  | watching / completed / plan to watch / dropped |
| total_episodes    | INT          | How many episodes it has total            |
| episodes_watched  | INT          | How far you've gotten (starts at 0)       |
| rating            | INT          | Your rating out of 10, once it's completed |

## Things I'd still like to add

- A search bar instead of scrolling through everything
- Sorting by episode count or genre
- Maybe a basic web UI at some point, instead of the terminal menu
