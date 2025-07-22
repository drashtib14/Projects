from modules.books import Role

try:
    if __name__ == "__main__":
        app = Role()
        app.run_menu()
except:
    print("Something went wrong")