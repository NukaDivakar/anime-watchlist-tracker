from db import get_connection

# ---------- helper function to print anime nicely ----------

def show_anime_list(anime_list):
    if len(anime_list) == 0:
        print("No anime found.")
        return

    for anime in anime_list:
        anime_id = anime[0]
        title = anime[1]
        genre = anime[2]
        status = anime[3]
        total_episodes = anime[4]
        episodes_watched = anime[5]
        rating = anime[6]

        print(f"ID              : {anime_id}")
        print(f"Title           : {title}")
        print(f"Genre           : {genre}")
        print(f"Status          : {status}")
        print(f"Episodes        : {episodes_watched} / {total_episodes}")
        print(f"Rating          : {rating}")
        print("-------------------------------------------")


# ---------- add a new anime to the list ----------

def add_anime():
    title = input("Enter anime title : ")
    genre = input("Enter genre : ")
    total_episodes = int(input("Enter total number of episodes : "))

    # every new anime starts as "plan to watch" with 0 episodes seen
    status = "plan to watch"
    episodes_watched = 0
    rating = None

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        insert into anime (title, genre, status, total_episodes, episodes_watched, rating)
        values (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (title, genre, status, total_episodes, episodes_watched, rating))
    connection.commit()

    print(f"'{title}' added to your watchlist !!!")

    cursor.close()
    connection.close()


# ---------- view every anime in the list ----------

def view_all_anime():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("select * from anime")
    anime_list = cursor.fetchall()

    show_anime_list(anime_list)

    cursor.close()
    connection.close()


# ---------- view anime filtered by status ----------

def view_by_status():
    status = input("Enter status to view (watching / completed / plan to watch / dropped) : ")
    status = status.lower()

    connection = get_connection()
    cursor = connection.cursor()

    query = "select * from anime where status = %s"
    cursor.execute(query, status)
    anime_list = cursor.fetchall()

    show_anime_list(anime_list)

    cursor.close()
    connection.close()


# ---------- update how many episodes you have watched ----------

def update_progress():
    anime_id = input("Enter the ID of the anime you want to update : ")
    episodes_watched = int(input("Enter episodes watched so far : "))

    connection = get_connection()
    cursor = connection.cursor()

    # if you are watching it, mark status as "watching" automatically
    query = """
        update anime
        set episodes_watched = %s, status = "watching"
        where id = %s
    """
    cursor.execute(query, (episodes_watched, anime_id))
    connection.commit()

    print("Progress updated successfully !!!")

    cursor.close()
    connection.close()


# ---------- mark an anime as completed and give it a rating ----------

def mark_completed():
    anime_id = input("Enter the ID of the anime you finished : ")
    rating = int(input("Enter your rating (1 to 10) : "))

    connection = get_connection()
    cursor = connection.cursor()

    # when completed, also set episodes_watched equal to total_episodes
    query = """
        update anime
        set status = "completed", rating = %s, episodes_watched = total_episodes
        where id = %s
    """
    cursor.execute(query, (rating, anime_id))
    connection.commit()

    print("Marked as completed. Enjoy the post-anime emptiness !!!")

    cursor.close()
    connection.close()


# ---------- delete an anime from the list ----------

def delete_anime():
    anime_id = input("Enter the ID of the anime you want to delete : ")

    connection = get_connection()
    cursor = connection.cursor()

    query = "delete from anime where id = %s"
    cursor.execute(query, anime_id)
    connection.commit()

    print("Anime removed from your list.")

    cursor.close()
    connection.close()


# ---------- show your top rated completed anime ----------

def show_top_rated():
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        select * from anime
        where status = "completed"
        order by rating desc
    """
    cursor.execute(query)
    anime_list = cursor.fetchall()

    show_anime_list(anime_list)

    cursor.close()
    connection.close()
