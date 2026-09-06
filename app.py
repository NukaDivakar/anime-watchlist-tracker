from anime import add_anime, view_all_anime, view_by_status, update_progress, mark_completed, delete_anime, show_top_rated

print("========== Anime Watchlist Tracker ==========")
print("1  :  Add a new anime")
print("2  :  View all anime")
print("3  :  View anime by status")
print("4  :  Update episodes watched")
print("5  :  Mark an anime as completed")
print("6  :  Delete an anime")
print("7  :  Show top rated completed anime")
print("8  :  Exit")

while True:
    choice = input("\nWhat do you want to do : ")

    if choice == "1":
        add_anime()
    if choice == "2":
        view_all_anime()
    if choice == "3":
        view_by_status()
    if choice == "4":
        update_progress()
    if choice == "5":
        mark_completed()
    if choice == "6":
        delete_anime()
    if choice == "7":
        show_top_rated()
    if choice == "8":
        break
