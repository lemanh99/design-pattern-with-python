import threading


class Database:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        # Using double-checked locking to ensure thread safety
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Database, cls).__new__(cls)
                    # Initialize the database connection here
        return cls._instance

    def query(self, sql):
        # Database query logic here
        pass


class Application:
    def main(self):
        foo = Database()
        foo.query("SELECT ...")


if __name__ == "__main__":
    app = Application()
    app.main()
